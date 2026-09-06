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

- 今日日期：`2026-09-06`
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
  "date": "2026-09-06",
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
    "points": 4449659,
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
    "points": 1813361,
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
    "points": 1300612,
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
    "points": 1247038,
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
    "points": 1163619,
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
    "points": 1076727,
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
    "points": 944737,
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
    "points": 882079,
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
    "points": 867849,
    "published_at": "2026-01-01T08:40:14+00:00",
    "summary": "【2026最新版】保姆级AI Agent智能体系统教程，手把手带你从0基础开始搭建企业级AI Agent智能体！全程干货无废话！让你少走99%的弯路！"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 722172,
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
    "points": 708684,
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
    "points": 672954,
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
    "points": 662221,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1RSFUzVEAG",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Claude Code】教程！大模型入门到进阶，一套全解决！Claude Code探索-测试-重构-调试代码库—附带课件代码",
    "url": "http://www.bilibili.com/video/av116045469783373",
    "source": "吴恩达的AI课",
    "platform": "bilibili",
    "points": 578876,
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
    "points": 441726,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV13YRjBTEPb",
    "domain": "AI",
    "title": "Hermes Agent零基础、保姆级教程，小白也能轻松玩转",
    "url": "http://www.bilibili.com/video/av116503638706867",
    "source": "iwenwiki",
    "platform": "bilibili",
    "points": 382783,
    "published_at": "2026-05-02T06:51:59+00:00",
    "summary": "全B站最详细的Hermes Agent教程，从部署到玩转！零基础，小白也能轻松玩转Hermes Agent，真正的AI助手，恐怖如斯！"
  },
  {
    "id": "bvid:BV1vG8QzcE5X",
    "domain": "AI",
    "title": "Claude使用指南，claude code零基础教程，claude code安装配置到实战",
    "url": "http://www.bilibili.com/video/av114933744272468",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 353665,
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
    "points": 281703,
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
    "points": 269320,
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
    "points": 254996,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 182556,
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
    "points": 180672,
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
    "points": 164609,
    "published_at": "2025-12-28T12:36:33+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 161100,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 108985,
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
    "points": 93572,
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
    "points": 74310,
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
    "points": 54828,
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
    "id": "bvid:BV1CbtJ6AEap",
    "domain": "AI",
    "title": "🚀我耗尽两个Max 20x账号对Claude Fable 5.1高难实测：7项任务一路加码，最后耗时3小时用Unity 3D做出模仿我的世界沙盒游戏",
    "url": "http://www.bilibili.com/video/av117200581170823",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 41447,
    "published_at": "2026-09-02T08:54:48+00:00",
    "summary": "视频简介：\n\nClaude Fable 5.1 到底强了多少？从 3D 黑洞到 Unity 侏罗纪沙盒，我把两个 Max 20× 账号额度跑光了\n这次直接把 Claude Fable 5.1 的测试难度拉高。\n\n前面先用 3D 黑洞、平面图转 3D 房屋、南宋武侠游戏、F-35 数字风洞、SVG 动画和复活节岛石像模拟不断加码，最后再进入 Claude Code，挑战用 Unity 3D + C#"
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 41470,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1VL3F6pE9K",
    "domain": "AI",
    "title": "0基础入门智能体agent测试：AI测试基础+AI智能体(Agent)测试从零入门全攻略，2026最新版！",
    "url": "http://www.bilibili.com/video/av116991151113881",
    "source": "黑马测试",
    "platform": "bilibili",
    "points": 33907,
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
    "points": 30168,
    "published_at": "2026-08-27T00:43:58+00:00",
    "summary": "v1.1.6安装包：\n夸克网盘：\n链接：https://pan.quark.cn/s/43ff3db459f4?pwd=SD2k\n提取码：SD2k\ngithub仓库：\nPlaya-0v0/Cyrene-Agent: An open-source AI desktop companion inspired by Cyrene, combining immersive Chat, personaliz"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29708,
    "published_at": "2025-07-16T13:10:54+00:00",
    "summary": "Cursor用不了？三款AI编程工具完美代替Cursor\naugmentCode\nTrae\nKiro"
  },
  {
    "id": "bvid:BV1Z5KU6UExC",
    "domain": "AI",
    "title": "【吴恩达2026】Vibe Coding保姆级教程，手把手从环境搭建到工作流完整闭环！——DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116951003242391",
    "source": "吴恩达AIAgent",
    "platform": "bilibili",
    "points": 23736,
    "published_at": "2026-07-20T07:01:13+00:00",
    "summary": "本套课专门解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22761,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 21190,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1hmb26ZEws",
    "domain": "AI",
    "title": "DeepSeek Harness 实测  Claude Code 对比后，梁神我错了 差距比我想的大",
    "url": "http://www.bilibili.com/video/av117100337236191",
    "source": "程序员晓刘",
    "platform": "bilibili",
    "points": 20369,
    "published_at": "2026-08-15T16:01:38+00:00",
    "summary": "这期用同一个 DeepSeek Pro 0813 模型，分别在 Claude Code 和 DeepSeek Harness 里完成同样的任务，对比工具链对最终效果的影响。\n实测内容包括：\nFPS 游戏 Demo、灯塔预警沙盘、手枪组装动画、显示器组装动画，以及 DeepSeek Harness 的插件化源码流程。\n整体看下来，模型本身当然重要，但 Harness 在插件化、流程记录、缓存命中和任"
  },
  {
    "id": "bvid:BV1eMgG6QEeG",
    "domain": "AI",
    "title": "【吴恩达】这绝对是把《Vibe Coding》讲得最通透的一套课！手把手教你构建自己的企业级AI工作流，学完直接落地！——附带课件代码",
    "url": "http://www.bilibili.com/video/av117081815189025",
    "source": "吴恩达Agents",
    "platform": "bilibili",
    "points": 17922,
    "published_at": "2026-08-12T09:29:57+00:00",
    "summary": "Vibe Coding火了，但你会发现——AI写的代码像开盲盒，今天能跑明天崩，项目一大就乱套。\n规范驱动开发（SDD） 就是来解决这个问题的。它的核心理念很简单：在让AI写代码之前，先和AI在统一的规范文档里对齐需求，把开发变成可预测、可追溯、可控制的过程。"
  },
  {
    "id": "bvid:BV14erKYuEaE",
    "domain": "AI",
    "title": "最强编程AI Cursor+Unity制作一个史诗游戏(详细)",
    "url": "http://www.bilibili.com/video/av113774908413987",
    "source": "多西杰克",
    "platform": "bilibili",
    "points": 17793,
    "published_at": "2025-01-05T09:01:00+00:00",
    "summary": "网上惊呼Cursor AI厉害的内容很多，但结合Unity做游戏的不多，我就来实测一下，做一个AAA大作......"
  },
  {
    "id": "bvid:BV1E8Tk6MEkw",
    "domain": "AI",
    "title": "AI Agent教程全集丨从入门到进阶丨适合99%小白入行的Agent教程！360°讲解大模型合集（比例RAG +langchain+Agent)全程干货无废话",
    "url": "http://www.bilibili.com/video/av116848259498783",
    "source": "Agent教程",
    "platform": "bilibili",
    "points": 17327,
    "published_at": "2026-07-02T03:38:47+00:00",
    "summary": "陆陆续续也整理了不少资源，希望能帮大家少走一些弯路！无论是学业还是事业，都希望你顺顺利利  看在UP这么努力的份上，求个三连+关注嘛\n\n1️⃣ 大模型入门学习路线图（附学习资源）\n2️⃣ 大模型方向必读书籍PDF版\n3️⃣ 大模型面试题库\n4️⃣ 大模型项目源码\n5️⃣ 超详细海量大模型LLM实战项目\n6️⃣ Langchain/RAG/Agent学习资源\n7️⃣ LLM大模型系统0到1入门学习教"
  },
  {
    "id": "bvid:BV1iDRQBrEF6",
    "domain": "AI",
    "title": "Claude + Blender 现在太强了 —— 完整免费设置",
    "url": "http://www.bilibili.com/video/av116543333601720",
    "source": "设计之道",
    "platform": "bilibili",
    "points": 16705,
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
    "points": 15959,
    "published_at": "2025-03-30T02:06:00+00:00",
    "summary": "在这门包含10节课的课程中，我们将带你从概念到代码，全面覆盖构建AI代理的基础知识。在这里找到完整的“AI代理入门”课程及代码示例\nhttps://github.com/microsoft/ai-agents-for-beginners\n\nP01 什么是AI代理\nP02 使用哪种AI代理框架\nP03 如何设计优秀的AI代理\nP04 什么是代理工具使用设计模式\nP05 什么是代理式RAG\nP06 如"
  },
  {
    "id": "bvid:BV1ZBT2ztEwp",
    "domain": "AI",
    "title": "一条视频讲清楚 到底什么是MCP！#MCP #Cursor #AI #编程",
    "url": "http://www.bilibili.com/video/av114642592469769",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 13834,
    "published_at": "2025-06-07T14:53:38+00:00",
    "summary": "一条视频讲清楚 到底什么是MCP！#MCP #Cursor #AI #编程"
  },
  {
    "id": "bvid:BV1JgVq6ME6v",
    "domain": "AI",
    "title": "超详细Claude Code+Harness教程",
    "url": "http://www.bilibili.com/video/av116679111610655",
    "source": "知了传课",
    "platform": "bilibili",
    "points": 13764,
    "published_at": "2026-06-02T06:33:18+00:00",
    "summary": "面向2026最新版超详细Claude Code+Harness教程，保姆级教程，高效AI编程技巧。资料领取请关注置顶评论。"
  },
  {
    "id": "bvid:BV1HhGo6aEvE",
    "domain": "AI",
    "title": "本地大模型也能联网搜索！LM Studio × MCP 接入教程",
    "url": "http://www.bilibili.com/video/av116635490911881",
    "source": "aopstudio",
    "platform": "bilibili",
    "points": 12288,
    "published_at": "2026-05-25T13:41:46+00:00",
    "summary": "本视频演示如何为 LM Studio 接入 MCP 联网搜索服务，让本地运行的大模型具备实时搜索网络的能力。\nMCP（Model Context Protocol）是 Anthropic 推出的开放协议，允许模型通过标准化接口调用外部工具。本次接入的搜索服务来自 MCPWorld，底层通过 npx 调用，无需额外部署服务端，配置完成后即可在 LM Studio 的对话界面中直接发起联网搜索。\n本视"
  },
  {
    "id": "bvid:BV14Utf6QEnB",
    "domain": "AI",
    "title": "Vibe Coding 术语课：别再管所有弹窗都叫「弹窗」了｜前端：弹窗与提示 12 术语网页演示",
    "url": "http://www.bilibili.com/video/av117207627467822",
    "source": "ZTough",
    "platform": "bilibili",
    "points": 10886,
    "published_at": "2026-09-03T14:42:06+00:00",
    "summary": "网页上那些 &quot;突然冒出来的东西&quot; 到底都叫啥？Alert、Toast、Modal、Drawer、Popconfirm、Tooltip…… 这一期把 12 个前端弹窗与提示术语一次讲清，每个都在真实网页里演示给你看，看完就分得清。\nVibe Coding 术语课持续更新，前端开发、UI 组件、网页开发相关术语每周讲解。觉得有用就点赞、投币、收藏，一键三连支持一下，也欢迎评论区告诉"
  },
  {
    "id": "bvid:BV1zbduYgEBH",
    "domain": "AI",
    "title": "Cursor新手教程⑤：Cursor降智真相+解决办法",
    "url": "http://www.bilibili.com/video/av114311359891940",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 10925,
    "published_at": "2025-04-10T02:53:27+00:00",
    "summary": "你是不是经常碰到这种情况：\n你试图修复一个小错误\n人工智能给出一个看似合理的更改建议\n这个修复导致其他地方出错\n你要求人工智能修复新出现的问题\n这又产生了另外两个问题\n如此反复\n本视频带你拆解Cursor降智的真相以及解决办法"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 10203,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 9479,
    "published_at": "2025-04-14T02:30:00+00:00",
    "summary": "MCP服务网站：https://smithery.ai/\nCherry Studio官方网站：https://cherry-ai.com/"
  },
  {
    "id": "hn:49458161",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia agrees to acquire Hugging Face for $13B",
    "url": "https://www.businessinsider.com/nvidia-in-talks-to-buy-hugging-face-13-billion-dollars-2026-8",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 1986,
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
    "points": 327,
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
    "id": "hn:49557813",
    "domain": "AI 算力 / 半导体",
    "title": "Tell HN: NVIDIA's Acquisition of HuggingFace was for $HuggingFace",
    "url": "https://news.ycombinator.com/item?id=49557813",
    "source": "MontagFTB",
    "platform": "hackernews",
    "points": 41,
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
    "id": "rss:https://www.tomshardware.com/tech-industry/best-of-ifa-2026",
    "domain": "AI 算力 / 半导体",
    "title": "Best of IFA 2026: MacBook Neo competitors, monitors, and wild laptop concepts",
    "url": "https://www.tomshardware.com/tech-industry/best-of-ifa-2026",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T12:05:00+00:00",
    "summary": "This year in Berlin, IFA exhibitors showed off several affordable, colorful new laptops, some wild concept devices, and a surprising number of monitors that run the gamut from budget to high-refresh O"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/modder-gets-nvidias-dlss-5-working-on-amds-rdna-4-gpus-rx-9070-xt-only-manages-30-fps-at-1080p-right-now-but-5070-ti-level-performance-is-the-eventual-goal",
    "domain": "AI 算力 / 半导体",
    "title": "Modder gets Nvidia's DLSS 5 working on AMD's RDNA 4 GPUs — RX 9070 XT only manages 30 FPS at 1080p right now, but 5070 Ti-level performance is the eventual goal",
    "url": "https://www.tomshardware.com/pc-components/gpus/modder-gets-nvidias-dlss-5-working-on-amds-rdna-4-gpus-rx-9070-xt-only-manages-30-fps-at-1080p-right-now-but-5070-ti-level-performance-is-the-eventual-goal",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T12:00:00+00:00",
    "summary": "If you have an RX 9000 series GPU, you can try out DLSS 5 on your PC right now and absolutely destroy the stable performance you were getting before."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/cloud-gaming/xbox-game-pass-adds-monthly-time-limits-subscribers-and-non-subcribers-can-buy-more-hours-to-keep-gaming",
    "domain": "AI 算力 / 半导体",
    "title": "Xbox Game Pass imposes monthly cloud gaming limits, just 15 hours per month for Ultimate — subscribers and non-subscribers can buy more hours to keep gaming",
    "url": "https://www.tomshardware.com/video-games/cloud-gaming/xbox-game-pass-adds-monthly-time-limits-subscribers-and-non-subcribers-can-buy-more-hours-to-keep-gaming",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T11:45:00+00:00",
    "summary": "Microsoft has added monthly limits to its Xbox Game Pass cloud gaming service, where subscribers and non-subscribers can purchase extra playtime when they surpass their limits."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dodge-the-rampocalypse-with-20-percent-discounts-on-corsair-ram-hundreds-off-on-32gb-and-64gb-ddr5-6400-kits",
    "domain": "AI 算力 / 半导体",
    "title": "Dodge the RAMpocalypse with 20% discounts on Corsair RAM — hundreds off on 32GB and 64GB DDR5-6400 kits",
    "url": "https://www.tomshardware.com/pc-components/dodge-the-rampocalypse-with-20-percent-discounts-on-corsair-ram-hundreds-off-on-32gb-and-64gb-ddr5-6400-kits",
    "source": "Sponsored",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T11:30:00+00:00",
    "summary": "Enjoy limited-time discounts of up to 23% on select Corsair DDR5 memory kits."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/handheld-gaming/worlds-first-fully-transparent-video-game-console-is-on-its-way-to-kickstarter-arduview-handhelds-shell-pcb-and-display-are-all-transparent",
    "domain": "AI 算力 / 半导体",
    "title": "‘World’s first fully transparent video game console’ is on its way to Kickstarter — Arduview handheld’s shell, PCB, and display are all transparent",
    "url": "https://www.tomshardware.com/video-games/handheld-gaming/worlds-first-fully-transparent-video-game-console-is-on-its-way-to-kickstarter-arduview-handhelds-shell-pcb-and-display-are-all-transparent",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T11:12:46+00:00",
    "summary": "The first units of the ‘world’s first fully transparent video game console’ are shipping to founders, and now the Arduview project is on its way to Kickstarter."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/we-tested-dlss-5-in-nba-2k27-with-every-rtx-50-series-gpu-first-official-release-comes-with-a-big-performance-hit-but-almost-every-blackwell-card-can-run-it-at-1080p",
    "domain": "AI 算力 / 半导体",
    "title": "We tested DLSS 5 in NBA 2K27 with every RTX 50-series GPU — first official release comes with a big performance hit, but almost every Blackwell card can run it at 1080p",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/we-tested-dlss-5-in-nba-2k27-with-every-rtx-50-series-gpu-first-official-release-comes-with-a-big-performance-hit-but-almost-every-blackwell-card-can-run-it-at-1080p",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T11:00:00+00:00",
    "summary": "We tested Nvidia's DLSS 5 in NBA 2K27 across every RTX 50-series graphics card at 1080p, 1440p, and 4K to see just how much performance it costs to explore the frontiers of neural rendering."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/policy/taiwan-cracks-down-on-tech-businesses-with-illegal-chinese-ownership-166-investigations-and-at-least-36-convictions-since-2020",
    "domain": "AI 算力 / 半导体",
    "title": "Taiwan cracks down on tech businesses with illegal Chinese ownership — 166 investigations and at least 36 convictions since 2020",
    "url": "https://www.tomshardware.com/tech-industry/policy/taiwan-cracks-down-on-tech-businesses-with-illegal-chinese-ownership-166-investigations-and-at-least-36-convictions-since-2020",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T10:40:00+00:00",
    "summary": "Taiwan's top investigative agency has been tracking Chinese businesses operating on the island without proper authority and shutting them down. These companies have been hiring Taiwanese experts to he"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/trump-slaps-up-to-100-percent-tariffs-on-imported-drones-and-critical-components-in-latest-move-against-chinas-proliferation-of-u-s-drone-market-citing-national-security-products-from-allied-nation-face-10-15-percent-rates",
    "domain": "AI 算力 / 半导体",
    "title": "Trump slaps up to 100% tariffs on imported drones and critical components in latest move against China's proliferation of U.S. drone market, citing national security — products from allied nation face",
    "url": "https://www.tomshardware.com/tech-industry/drones/trump-slaps-up-to-100-percent-tariffs-on-imported-drones-and-critical-components-in-latest-move-against-chinas-proliferation-of-u-s-drone-market-citing-national-security-products-from-allied-nation-face-10-15-percent-rates",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T10:20:00+00:00",
    "summary": "The Trump administration has imposed tariffs of up to 100% on imported drones and key components, as Washington intensifies its push to reduce reliance on Chinese drone technology and rebuild a domest"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/japan-to-mass-procure-3d-printed-rocket-powered-drone-interceptor-terra-b1-capable-of-countering-one-way-attack-platforms",
    "domain": "AI 算力 / 半导体",
    "title": "Japan to mass-procure 3D-printed rocket-powered drone interceptor — Terra B1 capable of countering one-way attack platforms",
    "url": "https://www.tomshardware.com/tech-industry/drones/japan-to-mass-procure-3d-printed-rocket-powered-drone-interceptor-terra-b1-capable-of-countering-one-way-attack-platforms",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T10:00:00+00:00",
    "summary": "Japan’s military has decided to mass-procure Terra B1 interceptor drones. These drones are made using 3D printers and are based on the tried and tested A1 model from Terra Drone, which began to be dep"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/dlss-5-officially-launches-inside-nba-2k27-limited-to-rtx-50-series-gpus-for-now-nvidia-promises-to-bring-neutral-rendering-tech-to-rtx-40-series-soon",
    "domain": "AI 算力 / 半导体",
    "title": "DLSS 5 officially launches inside NBA 2K27, limited to RTX 50-series GPUs for now — Nvidia promises to bring neutral rendering tech to RTX 40-series soon",
    "url": "https://www.tomshardware.com/pc-components/gpus/dlss-5-officially-launches-inside-nba-2k27-limited-to-rtx-50-series-gpus-for-now-nvidia-promises-to-bring-neutral-rendering-tech-to-rtx-40-series-soon",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T23:09:31+00:00",
    "summary": "Nvidia's controversial neural-rendering tech, DLSS 5, is now officially available in NBA 2K27, marking the start of a new era for the company. DLSS 5 will also come to RTX 40-series soon after current"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/grab-a-new-3d-printer-for-as-low-as-usd229-right-now-in-crealitys-labor-day-flash-sale-with-up-to-50-percent-off-big-sale-discounts-also-include-resin-and-filament-bundles-along-with-3d-scanners-and-toolkits",
    "domain": "AI 算力 / 半导体",
    "title": "Grab a new 3D printer for as low as $229 right now in Creality's Labor Day flash sale, with up to 50% off —big sale discounts also include resin and filament bundles, along with 3D scanners and toolki",
    "url": "https://www.tomshardware.com/3d-printing/grab-a-new-3d-printer-for-as-low-as-usd229-right-now-in-crealitys-labor-day-flash-sale-with-up-to-50-percent-off-big-sale-discounts-also-include-resin-and-filament-bundles-along-with-3d-scanners-and-toolkits",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T17:00:00+00:00",
    "summary": "Grab a new 3D printer in Creality's Labor Day flash sale, with discounts on printers and accessories available."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/nas/minisforum-launches-local-ai-solutions-at-ifa-2026-ai-agent-nas-n5-and-ai-mini-workstation-ms-s1-use-amd-ryzen-ai-max-pro-495-processors-designed-to-run-models-locally",
    "domain": "AI 算力 / 半导体",
    "title": "Minisforum launches local AI solutions at IFA 2026 — AI Agent NAS N5 and AI Mini Workstation MS-S1 use AMD Ryzen AI Max+ Pro 495 processors designed to run models locally",
    "url": "https://www.tomshardware.com/pc-components/nas/minisforum-launches-local-ai-solutions-at-ifa-2026-ai-agent-nas-n5-and-ai-mini-workstation-ms-s1-use-amd-ryzen-ai-max-pro-495-processors-designed-to-run-models-locally",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T16:15:00+00:00",
    "summary": "Minisforum unveiled the NAS N5 Max-P495 and MS-S1 Max-P945 at IFA 2026. The NAS and mini-PC are powered by the AMD Ryzen AI Max+ Pro 495, which can be configured with up to 192GB of unified memory and"
  },
  {
    "id": "rss:https://www.tomshardware.com/gift-guides-seasonal-sales/save-up-to-usd900-in-the-best-buy-labor-day-sale-on-tech-with-huge-discounts-on-gaming-pcs-laptops-and-monitors-secure-an-upgrade-fast-to-beat-rising-hardware-costs",
    "domain": "AI 算力 / 半导体",
    "title": "Save up to $900 in the Best Buy Labor Day sale on tech, with huge discounts on gaming PCs, laptops and monitors — secure an upgrade fast to beat rising hardware costs",
    "url": "https://www.tomshardware.com/gift-guides-seasonal-sales/save-up-to-usd900-in-the-best-buy-labor-day-sale-on-tech-with-huge-discounts-on-gaming-pcs-laptops-and-monitors-secure-an-upgrade-fast-to-beat-rising-hardware-costs",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T15:30:00+00:00",
    "summary": "There's a big Labor Day sale over at Best Buy right now, securing you huge discounts on tech, including gaming PCs, handhelds, laptops, and monitors."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/frontier-ai-faces-pricing-reckoning-as-token-volume-explodes-25-fold-mid-tier-models-deliver-90-percent-of-flagship-capability-at-one-sixth-the-cost",
    "domain": "AI 算力 / 半导体",
    "title": "Frontier AI faces pricing reckoning as token volume explodes 25-fold — mid-tier models deliver 90% of flagship capability at one-sixth the cost",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/frontier-ai-faces-pricing-reckoning-as-token-volume-explodes-25-fold-mid-tier-models-deliver-90-percent-of-flagship-capability-at-one-sixth-the-cost",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T15:21:56+00:00",
    "summary": "As frontier AI developers push for cost savings as much as intelligence enhancements, new models push the boundaries of the pareto frontier, with even small advantages crowning new kings."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/nvidia-app-update-fails-to-block-unofficial-dlss-multi-frame-generation-on-rtx-40-series-modders-restore-support-across-multiple-games-within-hours",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia app update fails to block unofficial DLSS multi-frame generation mod on RTX 40 series gaming GPUs — modders restore support across multiple games within hours",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/nvidia-app-update-fails-to-block-unofficial-dlss-multi-frame-generation-on-rtx-40-series-modders-restore-support-across-multiple-games-within-hours",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T14:56:38+00:00",
    "summary": "When NVIDIA launched the GeForce RTX 50 series, a major part of the hype surrounding the new GPU family was its support for DLSS Multi-Frame Generation. This feature was officially locked to the new R"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/get-this-stunning-msi-rtx-5060-ti-16g-deal-at-walmart-for-usd200-less-than-anywhere-else-only-usd569-99-for-the-solid-mid-range-shadow-2x-oc-plus-gaming-gpu-is-a-steal-by-anyones-standards",
    "domain": "AI 算力 / 半导体",
    "title": "Get this stunning MSI RTX 5060 Ti 16G deal at Walmart for $200 less than anywhere else — only $569.99 for the solid mid-range Shadow 2x OC Plus gaming GPU is a steal by anyone's standards",
    "url": "https://www.tomshardware.com/pc-components/get-this-stunning-msi-rtx-5060-ti-16g-deal-at-walmart-for-usd200-less-than-anywhere-else-only-usd569-99-for-the-solid-mid-range-shadow-2x-oc-plus-gaming-gpu-is-a-steal-by-anyones-standards",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T14:38:41+00:00",
    "summary": "Snag an MSI RTX 5060 Ti 16G Shadow 2x OC Plus at Walmart for an awesome $200 less than anywhere else - $569 price is the best we've found by a longshot"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/hyperx-omen-15-review",
    "domain": "AI 算力 / 半导体",
    "title": "HyperX Omen 15 review: Strong gaming performance and colorful OLED display, with obvious cost-cutting measures",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/hyperx-omen-15-review",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T13:52:40+00:00",
    "summary": "While gaming performance is strong, there are some signs of cost-cutting."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/denver-data-center-continuously-waters-its-lawn-even-after-city-announced-drought-restrictions-enraging-residents-its-unclear-if-site-is-breaking-the-law-or-using-its-own-recycled-water",
    "domain": "AI 算力 / 半导体",
    "title": "Denver data center continuously waters its lawn even after city announced drought restrictions, enraging residents — it’s unclear if site is breaking the law or using its own recycled water",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/denver-data-center-continuously-waters-its-lawn-even-after-city-announced-drought-restrictions-enraging-residents-its-unclear-if-site-is-breaking-the-law-or-using-its-own-recycled-water",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T13:26:18+00:00",
    "summary": "An AI data center is reportedly watering its lawn despite the area suffering from a drought. One resident said that we can't water our lawns until next summer, but you better believe that they are wat"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-unveils-threadripper-halo-station-an-ai-workstation-packing-96-cores-and-dual-liquid-cooled-mi350p-accelerators-the-most-powerful-workstation-in-the-world-can-run-trillion-parameter-models-says-amd",
    "domain": "AI 算力 / 半导体",
    "title": "AMD unveils Threadripper Halo Station, an AI workstation packing 96 cores and dual liquid-cooled MI350P accelerators — 'the most powerful workstation in the world' can run trillion-parameter models, s",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-unveils-threadripper-halo-station-an-ai-workstation-packing-96-cores-and-dual-liquid-cooled-mi350p-accelerators-the-most-powerful-workstation-in-the-world-can-run-trillion-parameter-models-says-amd",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T12:58:37+00:00",
    "summary": "AMD's Threadripper Halo Station packs a 96-core Zen 5 Threadripper, dual MI350P accelerators with support for four, and 2TB of DDR5."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/discrete-graphics-card-sales-hit-four-year-record-despite-high-prices-shipments-reach-13-24-million-units-as-market-defies-pc-slump",
    "domain": "AI 算力 / 半导体",
    "title": "Discrete graphics card sales hit four-year record despite soaring memory prices — AMD gains market share as notebook graphics carry the market",
    "url": "https://www.tomshardware.com/pc-components/gpus/discrete-graphics-card-sales-hit-four-year-record-despite-high-prices-shipments-reach-13-24-million-units-as-market-defies-pc-slump",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T12:45:23+00:00",
    "summary": "Shipments of standalone graphics processors for PCs grow sequentially and year-over-year amid shortage of components and increased prices."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-chairs/fractal-design-refine-2-review",
    "domain": "AI 算力 / 半导体",
    "title": "Fractal Design Refine 2 Review: Slightly refined",
    "url": "https://www.tomshardware.com/peripherals/gaming-chairs/fractal-design-refine-2-review",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T12:31:14+00:00",
    "summary": "Fractal Design's second-generation gaming chair lives up to its name — it's slightly refined from its predecessor, which means it's not really that different."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/fake-ddr5-memory-kits-now-on-sale-starting-at-usd43-v-color-sells-0gb-dummy-modules-and-single-stick-memory-kits-with-a-fake-stick-for-usd300",
    "domain": "AI 算力 / 半导体",
    "title": "Fake DDR5 memory kits now on sale starting at $43 — V-Color sells 0GB dummy modules and single-stick memory kits with a fake stick for $300",
    "url": "https://www.tomshardware.com/pc-components/ram/fake-ddr5-memory-kits-now-on-sale-starting-at-usd43-v-color-sells-0gb-dummy-modules-and-single-stick-memory-kits-with-a-fake-stick-for-usd300",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T11:30:00+00:00",
    "summary": "V-Color's DDR5 filler memory featuring a real stick paired with a dummy module is now available around the UK and Europe, while the company's 0GB kits that just come with filler sticks are on sale in "
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/pc-building/grab-hotos-25-bit-electric-screwdriver-set-for-under-usd30-right-now-perfect-for-pc-builds-and-projects-limited-time-deal-knocks-40-percent-off-the-usual-price-for-a-multi-torque-driver-with-a-1-500-mah-battery-and-25-heavy-duty-bits-for-hobbyists",
    "domain": "AI 算力 / 半导体",
    "title": "Grab Hoto's 25-bit electric screwdriver set for under $30 right now, perfect for PC builds and projects — limited-time deal knocks 40% off the usual price for a multi-torque driver with a 1,500 mAh ba",
    "url": "https://www.tomshardware.com/desktops/pc-building/grab-hotos-25-bit-electric-screwdriver-set-for-under-usd30-right-now-perfect-for-pc-builds-and-projects-limited-time-deal-knocks-40-percent-off-the-usual-price-for-a-multi-torque-driver-with-a-1-500-mah-battery-and-25-heavy-duty-bits-for-hobbyists",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T11:21:55+00:00",
    "summary": "Save 40% on this Hoto electric screwdriver with 25 hardened bits, now just $29.99 for a limited time only."
  },
  {
    "id": "rss:https://www.tomshardware.com/service-providers/network-providers/over-2-000-subscribers-grab-discounted-starlink-plans-in-tennessee-and-mississippi-spacexai-offers-50-percent-off-for-people-living-near-its-data-centers-and-other-developments",
    "domain": "AI 算力 / 半导体",
    "title": "SpaceXAI offers 50% Starlink discount to placate data center's residential neighbors; 2,000 have signed up — goodwill gesture comes amid vociferous community backlash",
    "url": "https://www.tomshardware.com/service-providers/network-providers/over-2-000-subscribers-grab-discounted-starlink-plans-in-tennessee-and-mississippi-spacexai-offers-50-percent-off-for-people-living-near-its-data-centers-and-other-developments",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T11:00:00+00:00",
    "summary": "SpaceXAI Memphis said on its X account that more than 2,000 subscribers from the Memphis and Southaven area have already signed up for the discounted Starlink offer. Elon Musk is giving subscribers li"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/this-32gb-of-team-group-ddr5-ram-is-the-cheapest-ddr5-6400-kit-on-the-market-only-usd405-with-promo-code-buy-the-least-expensive-ddr5-6400-kit-around-with-environmentally-conscious-t-force-vulcan-eco-ram",
    "domain": "AI 算力 / 半导体",
    "title": "This 32GB of Team Group DDR5 RAM is the cheapest DDR5-6400 kit on the market – only $405 with promo code, buy the least expensive DDR5-6400 kit around with environmentally conscious T-Force Vulcan Eco",
    "url": "https://www.tomshardware.com/pc-components/this-32gb-of-team-group-ddr5-ram-is-the-cheapest-ddr5-6400-kit-on-the-market-only-usd405-with-promo-code-buy-the-least-expensive-ddr5-6400-kit-around-with-environmentally-conscious-t-force-vulcan-eco-ram",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T10:54:32+00:00",
    "summary": "Newegg's 32GB TeamGroup T-Force Vulcan Eco DDR5-6400 CL38 kit is down to $405 with code LDSF243, making it the least expensive DDR5-6400 kit around amid the RAMpocalypse — and it's even cheaper than m"
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
    "points": 1155,
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
    "id": "hn:49566788",
    "domain": "大厂 AI 动态",
    "title": "Project HydraFusion: Frontier quality via multi-model orchestration",
    "url": "https://github.blog/ai-and-ml/github-copilot/project-hydrafusion-frontier-quality-via-multi-model-orchestration/",
    "source": "qainsights",
    "platform": "hackernews",
    "points": 77,
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
    "id": "rss:https://www.theverge.com/tech/990873/earth-garden-globe-field-recordings",
    "domain": "大厂 AI 动态",
    "title": "Explore the globe in field recordings",
    "url": "https://www.theverge.com/tech/990873/earth-garden-globe-field-recordings",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T21:31:34+00:00",
    "summary": "I love field recordings. I love making them. I love them when they're incorporated into my ambient music. They're great background noise for working or sleeping. But they're also great for active list"
  },
  {
    "id": "rss:https://www.theverge.com/tech/990868/iphone-handoff-ios-27",
    "domain": "大厂 AI 动态",
    "title": "iPhone Handoff will seamlessly share one number between two phones",
    "url": "https://www.theverge.com/tech/990868/iphone-handoff-ios-27",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T20:53:58+00:00",
    "summary": "When iOS 27 lands later this month, it will have a feature called iPhone Handoff that lets you switch between two phones using the same number. It was briefly mentioned during the WWDC keynote back in"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/990794/cd-sales-are-booming-as-physical-media-continues-its-resurgence",
    "domain": "大厂 AI 动态",
    "title": "CD sales are booming as physical media continues its resurgence",
    "url": "https://www.theverge.com/entertainment/990794/cd-sales-are-booming-as-physical-media-continues-its-resurgence",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T16:49:33+00:00",
    "summary": "According to the Recording Industry Association of America (RIAA), CD sales exploded in the first half of 2026. A new report from the organization says 17.5 million CDs were sold in the first six mont"
  },
  {
    "id": "rss:https://www.theverge.com/report/989270/fantasy-footballers-podcast-andy-holloway-interview",
    "domain": "大厂 AI 动态",
    "title": "Fantasy Footballers’ Andy Holloway is a dedicated zero-inbox kinda guy",
    "url": "https://www.theverge.com/report/989270/fantasy-footballers-podcast-andy-holloway-interview",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T15:00:00+00:00",
    "summary": "Andy Holloway cohosts the Fantasy Footballers podcast with his friends Jason Moore and Mike Wright. The show is one of the premier fantasy sports podcasts, netting over 2 million monthly listeners and"
  },
  {
    "id": "rss:https://www.theverge.com/tech/990426/us-open-influencers-naomi-osaka-anastasia-zakharova-callaway-good-good-ad",
    "domain": "大厂 AI 动态",
    "title": "Content creators drop the ball",
    "url": "https://www.theverge.com/tech/990426/us-open-influencers-naomi-osaka-anastasia-zakharova-callaway-good-good-ad",
    "source": "Charles Pulliam-Moore",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T14:00:16+00:00",
    "summary": "During Naomi Osaka's match against Anastasia Zakharova at this year's US Open earlier this week, a gaggle of ring light-wielding influencers who were packed in a luxury suite became enough of a distra"
  },
  {
    "id": "rss:https://www.theverge.com/tech/990706/a-day-at-canjam-socal-2026",
    "domain": "大厂 AI 动态",
    "title": "The weird and wonderful headphones of CanJam 2026",
    "url": "https://www.theverge.com/tech/990706/a-day-at-canjam-socal-2026",
    "source": "John.Higgins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T13:00:00+00:00",
    "summary": "I've been reviewing headphones for a long time, and I've listened to everything from the barely serviceable to multi-thousand-dollar open-back headphones. But recently I've been uninspired by the stat"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/990773/openai-german-wiki-incident",
    "domain": "大厂 AI 动态",
    "title": "OpenAI admits to German wiki ‘incident’",
    "url": "https://www.theverge.com/ai-artificial-intelligence/990773/openai-german-wiki-incident",
    "source": "Robert Hart",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T11:15:55+00:00",
    "summary": "OpenAI says it needs to overhaul how and when it reports instances of AI models attacking real-world targets. The acknowledgement comes as the company manages the fallout from reports that a swarm of "
  },
  {
    "id": "rss:https://www.theverge.com/transportation/989513/road-rage-short-film-robotaxi-autonomous-ai",
    "domain": "大厂 AI 动态",
    "title": "Robotaxis enter their villain era",
    "url": "https://www.theverge.com/transportation/989513/road-rage-short-film-robotaxi-autonomous-ai",
    "source": "Rani Molla",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T11:00:00+00:00",
    "summary": "It's Bullitt meets Christine meets Waymo. A new short film imagines a San Francisco car chase where the other driver isn't human - and the car may be trying to kill you. That a robotaxi can now be cas"
  },
  {
    "id": "rss:https://www.theverge.com/tech/990658/audacity-4-update-audio-editing",
    "domain": "大厂 AI 动态",
    "title": "Audacity 4 is a complete revamp of the ‘world’s most popular’ audio editor",
    "url": "https://www.theverge.com/tech/990658/audacity-4-update-audio-editing",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T21:23:50+00:00",
    "summary": "Audacity 4 has been in the works for some time, and had its own mini controversy last year when an unfortunate redesigned logo started making the rounds. The final version of the new icon isn't nearly"
  },
  {
    "id": "rss:https://www.theverge.com/policy/990520/trump-arcade-games-maga-copyright",
    "domain": "大厂 AI 动态",
    "title": "The White House is making arcade games racist",
    "url": "https://www.theverge.com/policy/990520/trump-arcade-games-maga-copyright",
    "source": "Gaby Del Valle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T19:42:54+00:00",
    "summary": "The PR masterminds at the White House just released a series of vaguely policy-themed \"arcade\" games, some of which are racist - and modeled on real games whose copyright holders may not be too happy "
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/05/seattle-times-and-newsday-are-the-latest-publications-to-sue-openai-and-microsoft/",
    "domain": "大厂 AI 动态",
    "title": "Seattle Times and Newsday are the latest publications to sue OpenAI and Microsoft",
    "url": "https://techcrunch.com/2026/09/05/seattle-times-and-newsday-are-the-latest-publications-to-sue-openai-and-microsoft/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T22:49:55+00:00",
    "summary": "Two more news organizations are suing OpenAI and Microsoft over the supposed use of their journalism to train AI."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/05/hikers-rescued-after-using-google-gemini-for-planning/",
    "domain": "大厂 AI 动态",
    "title": "Hikers rescued after using Google Gemini for planning",
    "url": "https://techcrunch.com/2026/09/05/hikers-rescued-after-using-google-gemini-for-planning/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T19:35:24+00:00",
    "summary": "The sheriff’s office said the hikers “were advised by Gemini to bring far less food and water than their group required.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/05/openai-confirms-wiki-incident-says-its-working-on-a-framework-for-more-disclosure/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI confirms ‘wiki incident,’ says it’s ‘working on a framework’ for more disclosure",
    "url": "https://techcrunch.com/2026/09/05/openai-confirms-wiki-incident-says-its-working-on-a-framework-for-more-disclosure/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T18:05:27+00:00",
    "summary": "OpenAI acknowledged its role in a recently reported incident where AI agents took over a German wiki forum."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/05/cluckys-new-alarm-app-wakes-you-up-with-a-crowing-rooster/",
    "domain": "大厂 AI 动态",
    "title": "Clucky’s new alarm app wakes you up with a crowing rooster",
    "url": "https://techcrunch.com/2026/09/05/cluckys-new-alarm-app-wakes-you-up-with-a-crowing-rooster/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T17:00:00+00:00",
    "summary": "Clucky's new alarm app has an option where users are woken up to the sound of a rooster. They then complete a mission to turn it off."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/05/oura-is-going-public-but-these-smart-ring-companies-are-coming-for-its-crown/",
    "domain": "大厂 AI 动态",
    "title": "Oura is going public, but these smart ring companies are coming for its crown",
    "url": "https://techcrunch.com/2026/09/05/oura-is-going-public-but-these-smart-ring-companies-are-coming-for-its-crown/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T15:00:00+00:00",
    "summary": "While Oura has largely dominated the smart ring market for years, a growing number of rivals are now racing to dethrone it by trying all sorts of approaches to get an edge over it."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/04/xdof-just-three-months-out-of-stealth-is-in-talks-for-a-series-b-at-a-1-2b-valuation/",
    "domain": "大厂 AI 动态",
    "title": "XDOF, just three months out of stealth, is in talks for a Series B at a $1.2B valuation",
    "url": "https://techcrunch.com/2026/09/04/xdof-just-three-months-out-of-stealth-is-in-talks-for-a-series-b-at-a-1-2b-valuation/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T23:36:14+00:00",
    "summary": "The round is being raised just months after the robot data startup exited from stealth."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/04/openais-rogue-agents-keep-escaping-with-no-formal-process-to-investigate-them/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI’s rogue agents keep escaping, with no formal process to investigate them",
    "url": "https://techcrunch.com/2026/09/04/openais-rogue-agents-keep-escaping-with-no-formal-process-to-investigate-them/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T23:15:11+00:00",
    "summary": "OpenAI’s latest agent swarm incident adds urgency to calls for independent investigations as researchers and lawmakers question whether AI labs should control the scope of their own safety reviews."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/04/ai-compute-provider-nscale-is-looking-for-3-5b-in-pre-ipo-financing/",
    "domain": "大厂 AI 动态",
    "title": "AI compute provider Nscale is looking for $3.5B in pre-IPO financing",
    "url": "https://techcrunch.com/2026/09/04/ai-compute-provider-nscale-is-looking-for-3-5b-in-pre-ipo-financing/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T21:12:11+00:00",
    "summary": "Nscale, which recently struck a $45 billion deal with Anthropic, is in talks to raise additional funds in anticipation of an upcoming IPO."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/04/judge-blocks-x-rival-from-using-twitter-name-but-allows-tweet-for-now/",
    "domain": "大厂 AI 动态",
    "title": "Judge blocks X rival from using Twitter name, but allows ‘Tweet’ for now",
    "url": "https://techcrunch.com/2026/09/04/judge-blocks-x-rival-from-using-twitter-name-but-allows-tweet-for-now/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T17:52:05+00:00",
    "summary": "A federal judge temporarily barred an X rival from using the Twitter name, but found that X was likely to have abandoned the “Tweet” trademark and bird logo. The startup has since relaunched as Tweet."
  },
  {
    "id": "rss:https://techcrunch.com/video/what-will-apples-john-ternus-era-look-like/",
    "domain": "大厂 AI 动态",
    "title": "What will Apple’s John Ternus era look like?",
    "url": "https://techcrunch.com/video/what-will-apples-john-ternus-era-look-like/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T17:18:00+00:00",
    "summary": "It&#8217;s&#160;officially the Ternus era at Apple.&#160;&#160; Tim Cook stepped down&#160;as CEO this week, handing the company to former hardware chief John Ternus, whose first memo&#160;promised a "
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/04/no-little-kids-allowed-and-other-new-info-about-teslas-cybercab/",
    "domain": "大厂 AI 动态",
    "title": "No little kids allowed, and other new info about Tesla’s Cybercab",
    "url": "https://techcrunch.com/2026/09/04/no-little-kids-allowed-and-other-new-info-about-teslas-cybercab/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T16:51:23+00:00",
    "summary": "The company says no children under 13 can ride -- even with a parent. That's more restrictive than the Model Y SUVs it's using as robotaxis."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/04/another-swarm-of-openai-agents-reached-the-open-internet-without-the-frontier-labs-knowledge/",
    "domain": "大厂 AI 动态",
    "title": "Another swarm of OpenAI agents reached the open internet without the frontier lab’s knowledge",
    "url": "https://techcrunch.com/2026/09/04/another-swarm-of-openai-agents-reached-the-open-internet-without-the-frontier-labs-knowledge/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T16:21:11+00:00",
    "summary": "It's the latest failure of OpenAI's internal monitoring and security systems."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/04/cd-sales-are-making-an-unexpected-comeback-amid-a-retro-tech-boom/",
    "domain": "大厂 AI 动态",
    "title": "CD sales are making an unexpected comeback amid a retro tech boom",
    "url": "https://techcrunch.com/2026/09/04/cd-sales-are-making-an-unexpected-comeback-amid-a-retro-tech-boom/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T15:00:00+00:00",
    "summary": "U.S. CD revenue jumped 58.6% in the first half of 2026, reversing last year’s decline as interest in retro tech and physical media continues to grow."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/04/krafton-doubles-down-on-india-with-another-250m-bet-beyond-gaming/",
    "domain": "大厂 AI 动态",
    "title": "Krafton doubles down on India with another $250M bet beyond gaming",
    "url": "https://techcrunch.com/2026/09/04/krafton-doubles-down-on-india-with-another-250m-bet-beyond-gaming/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T14:47:20+00:00",
    "summary": "Krafton's planned investment in India is set to surpass $500 million with its latest commitment."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/04/googles-gemini-spark-can-now-manage-your-google-photos-library/",
    "domain": "大厂 AI 动态",
    "title": "Google’s Gemini Spark can now manage your Google Photos library",
    "url": "https://techcrunch.com/2026/09/04/googles-gemini-spark-can-now-manage-your-google-photos-library/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T14:47:11+00:00",
    "summary": "Gemini Spark can edit and curate photo albums, create shared collections, turn photos into calendar events, and handle other Google Photos tasks for AI Pro and Ultra subscribers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/04/less-than-24-hours-to-apply-for-your-techcrunch-disrupt-2026-side-event/",
    "domain": "大厂 AI 动态",
    "title": "Less than 24 hours to apply for your TechCrunch Disrupt 2026 Side Event",
    "url": "https://techcrunch.com/2026/09/04/less-than-24-hours-to-apply-for-your-techcrunch-disrupt-2026-side-event/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T14:00:00+00:00",
    "summary": "Less than 24 hours left to apply to host a Side Event during TechCrunch Disrupt 2026 and make your mark in the Silicon Valley scene. Apply before the application closes tonight at midnight PT."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/04/us-military-disabled-ad-tracking-on-troops-devices-following-reports-of-targeted-attacks/",
    "domain": "大厂 AI 动态",
    "title": "US military disabled ad tracking on troops’ devices following reports of targeted attacks",
    "url": "https://techcrunch.com/2026/09/04/us-military-disabled-ad-tracking-on-troops-devices-following-reports-of-targeted-attacks/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T13:21:37+00:00",
    "summary": "A senator's letter confirms the U.S. military moved to prevent the tracking after foreign adversaries used location data to target troops."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/04/feds-launch-investigation-into-teslas-cybercab-deployment/",
    "domain": "大厂 AI 动态",
    "title": "Feds launch investigation into Tesla’s Cybercab deployment",
    "url": "https://techcrunch.com/2026/09/04/feds-launch-investigation-into-teslas-cybercab-deployment/",
    "source": "Sean O'Kane, Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T12:01:14+00:00",
    "summary": "The investigation was launched just a few hours after Tesla put the first production Cybercabs on the road in Austin."
  },
  {
    "id": "rss:https://stratechery.com/2026/friction-and-feedback/",
    "domain": "大厂 AI 动态",
    "title": "2026.36: Friction and Feedback",
    "url": "https://stratechery.com/2026/friction-and-feedback/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T17:55:39+00:00",
    "summary": "The best Stratechery content from the week of August 31, 2026, including the market speaking, Apple finding religion, and society losing friction."
  },
  {
    "id": "rss:https://stratechery.com/2026/an-interview-with-openai-president-greg-brockman-about-astra-and-alignment/",
    "domain": "大厂 AI 动态",
    "title": "An Interview with OpenAI President Greg Brockman About Astra and Alignment",
    "url": "https://stratechery.com/2026/an-interview-with-openai-president-greg-brockman-about-astra-and-alignment/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T10:00:00+00:00",
    "summary": "An interview with OpenAI President and Co-Founder Greg Brockman about the history of OpenAI, Astra and alignment, and the weight of building the future."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/09/teslas-cybercab-has-been-deployed-and-its-already-under-investigation/",
    "domain": "大厂 AI 动态",
    "title": "Tesla’s Cybercab has been deployed, and it’s already under investigation",
    "url": "https://arstechnica.com/cars/2026/09/teslas-cybercab-has-been-deployed-and-its-already-under-investigation/",
    "source": "Aarian Marshall, WIRED.COM",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T15:17:36+00:00",
    "summary": "The US government is investigating whether the Cybercab meets vehicle safety standards."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/09/after-8-years-europes-bepicolombo-mission-is-on-final-approach-to-mercury/",
    "domain": "大厂 AI 动态",
    "title": "After 8 years, Europe's BepiColombo mission is on final approach to Mercury",
    "url": "https://arstechnica.com/space/2026/09/after-8-years-europes-bepicolombo-mission-is-on-final-approach-to-mercury/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T22:49:17+00:00",
    "summary": "\"Fundamentally, we want to learn about the origins of this planet and how it came to be like it is.\""
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/09/openai-agents-discussed-ways-to-escape-their-sandbox-on-public-wiki/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI agents discussed ways to escape their sandbox on public wiki",
    "url": "https://arstechnica.com/security/2026/09/openai-agents-discussed-ways-to-escape-their-sandbox-on-public-wiki/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T22:17:36+00:00",
    "summary": "In all, 3,700 internal agents posted 18,000 messages discussing cheating on a test."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/09/measles-killed-6-week-old-baby-coroner-confirms-after-rfk-jr-disputed-deaths/",
    "domain": "大厂 AI 动态",
    "title": "Measles killed 6-week-old baby, coroner confirms after RFK Jr. disputed deaths",
    "url": "https://arstechnica.com/health/2026/09/measles-killed-6-week-old-baby-coroner-confirms-after-rfk-jr-disputed-deaths/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T20:22:41+00:00",
    "summary": "\"It’s long past time for RFK to stop playing games with people’s lives.\""
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/09/trump-admin-fights-abc-lawsuit-as-watchdogs-worry-disney-will-settle-with-fcc/",
    "domain": "大厂 AI 动态",
    "title": "Trump admin fights ABC lawsuit as watchdogs worry Disney will settle with FCC",
    "url": "https://arstechnica.com/tech-policy/2026/09/trump-admin-fights-abc-lawsuit-as-watchdogs-worry-disney-will-settle-with-fcc/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T19:46:34+00:00",
    "summary": "FCC tells court it is “open-minded\" about whether ABC should lose licenses."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/09/medieval-manuscripts-are-biological-time-capsules-for-deadly-sheeppox-virus/",
    "domain": "大厂 AI 动态",
    "title": "Medieval manuscripts are \"biological time capsules\" for deadly sheeppox virus",
    "url": "https://arstechnica.com/science/2026/09/medieval-manuscripts-are-biological-time-capsules-for-deadly-sheeppox-virus/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T19:01:02+00:00",
    "summary": "Other archives and libraries around the world may also contain genetic traces of past disease outbreaks."
  },
  {
    "id": "rss:https://arstechnica.com/information-technology/2026/09/trust-not-features-is-the-real-deficit-vmware-tries-to-appease-smbs/",
    "domain": "大厂 AI 动态",
    "title": "“Trust, not features, is the real deficit”: VMware tries to appease SMBs",
    "url": "https://arstechnica.com/information-technology/2026/09/trust-not-features-is-the-real-deficit-vmware-tries-to-appease-smbs/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T17:35:02+00:00",
    "summary": "Broadcom admits it put “too big a focus on VCF.”"
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/09/once-popular-for-attacking-ai-ascii-smuggling-is-embraced-by-spammers/",
    "domain": "大厂 AI 动态",
    "title": "Once popular for attacking AI, ASCII smuggling is embraced by spammers",
    "url": "https://arstechnica.com/security/2026/09/once-popular-for-attacking-ai-ascii-smuggling-is-embraced-by-spammers/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T17:18:12+00:00",
    "summary": "A once-overlooked block of unicode that's invisible to humans is gaining ever wider use."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/09/pentagon-releases-then-quickly-removes-testosterone-screening-policy/",
    "domain": "大厂 AI 动态",
    "title": "Pentagon rescinds new testosterone screening policy without explanation",
    "url": "https://arstechnica.com/health/2026/09/pentagon-releases-then-quickly-removes-testosterone-screening-policy/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T16:57:24+00:00",
    "summary": "The Pentagon says the guidance is being updated after being online for one day."
  },
  {
    "id": "wscn:3781169",
    "domain": "股票",
    "title": "又出事了！美国一批OpenAI智能体，被曝劫持了一个德国网站，用来相互传递突破限制的方法！",
    "url": "https://wallstreetcn.com/articles/3781169",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T07:35:13+00:00",
    "summary": "发布GPT-6之际，OpenAI曝出惊人争议：其AI智能体竟“劫持”网站作“秘密留言板”。它们在此共享测试答案、交流绕开限制之法，遭删帖时还会建备份反追踪。官方已承认该事故，AI“抱团协作”带来的越权与失控风险正引发业界高度警惕。"
  },
  {
    "id": "wscn:3781168",
    "domain": "股票",
    "title": "“人民币政府”“新熊源”？新董事长上任后首份半年报出现差错引热议，紫金矿业凌晨公告：写错了，更正并诚挚致歉",
    "url": "https://wallstreetcn.com/articles/3781168",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T06:10:41+00:00",
    "summary": "紫金矿业半年报惊现\"人民币政府\"\"熊源产业\"等低级文字错误，公司紧急更正并致歉。尽管失误不影响财务数据，却恰恰发生在新任董事长邹来昌履职后首份半年报上。与此同时，公司上半年净利润飙升68%至391.7亿元，基本面强劲，\"乌龙\"背后更值得关注的是真金白银的经营成色。"
  },
  {
    "id": "wscn:3780982",
    "domain": "股票",
    "title": "网络安全崛起：AI隐患叙事下，网安何以成为软件板块最强反转？",
    "url": "https://wallstreetcn.com/premium/articles/3780982?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T05:51:16+00:00",
    "summary": "AI 隐患对网安市场的影响，很可能不是一次性的题材脉冲，而是一条独立于 AI 资本开支之外的、长期刚性的增量支出曲线。"
  },
  {
    "id": "wscn:3781074",
    "domain": "股票",
    "title": "下周重磅日程：中美CPI、苹果折叠屏iPhone首秀、小米华为发布会、欧央行决议",
    "url": "https://wallstreetcn.com/articles/3781074",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T04:22:21+00:00",
    "summary": "下周“机圈”盛宴，苹果首款折叠屏iPhone首秀，华为三折叠 Mate XT 2与小米 18 Fold同步亮相。宏观数据方面，美国CPI/PPI、中国8月CPI/PPI与进出口先后出炉，欧洲央行利率决议预计按兵不动。此外，加拿大对美反制关税将生效、美债回购翻倍生效，甲骨文发布财报。"
  },
  {
    "id": "wscn:3781164",
    "domain": "股票",
    "title": "美军首度打击三艘伊朗油轮，霍尔木兹海峡冲突从“炸设施”升级到“断运输”",
    "url": "https://wallstreetcn.com/articles/3781164",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T03:32:42+00:00",
    "summary": "美伊军事冲突本周发生性质跃迁。随着美军打击目标首次从沿岸军事设施转向航行中的原油运输船只，标志着美伊交锋从\"打击产能与设施\"正式升级至\"打击运输通道\"，市场焦点也随之从\"伊朗减产多少\"切换至\"美军是否要系统性切断伊朗原油运输\"，全球原油定价逻辑面临重估。"
  },
  {
    "id": "wscn:3781163",
    "domain": "股票",
    "title": "美银Hartnett：“民主党中选横扫”将打崩美股，戳破AI泡沫",
    "url": "https://wallstreetcn.com/articles/3781163",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T02:52:12+00:00",
    "summary": "美银首席策略师Hartnett发出罕见警报：全球债券收益率飙至二十年高位，正成为AI资本支出狂潮的致命威胁。更大变数在于——Polymarket显示民主党横扫两院概率已升至50%，一旦成真，美股或跌逾10%，AI泡沫随时引爆，而华尔街对此几乎毫无准备。"
  },
  {
    "id": "wscn:3781165",
    "domain": "股票",
    "title": "伊朗革命卫队称打击了美航母和驱逐舰",
    "url": "https://wallstreetcn.com/articles/3781165",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T02:52:05+00:00",
    "summary": "据伊朗伊斯兰共和国通讯社6日报道，伊朗伊斯兰革命卫队公共关系部门当天发布公告称，革命卫队空军发射多枚弹道导弹，打击了美军一艘航空母舰和一艘驱逐舰。"
  },
  {
    "id": "wscn:3781075",
    "domain": "股票",
    "title": "暌违十年，黄酒行业大变天：资本市场为什么重新盯上这个百亿小酒种？",
    "url": "https://wallstreetcn.com/premium/articles/3781075?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T02:22:53+00:00",
    "summary": "黄酒行业经历多年规模收缩与低价竞争后，正进入供给格局、价格体系和企业治理同步修复的阶段。会稽山率先把改革转化为收入结构和利润增长，古越龙山则出现高端产品、毛利率和渠道质量改善。\n当前黄酒行业的关注重心已转向龙头利润池重构，后续关键在于价格带上移、全国化动销和经营杠杆兑现。"
  },
  {
    "id": "wscn:3781162",
    "domain": "股票",
    "title": "高盛合伙人：夏季结束了，市场焦点都在“债市风暴”，而美股恐慌指数已跌至特朗普任期低点",
    "url": "https://wallstreetcn.com/articles/3781162",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T01:49:21+00:00",
    "summary": "美国债市收益率创历史新高，VIX却跌至特朗普任期低点——高盛合伙人Mark Wilson直指这场\"认知分裂\"的危险：估值已在悄然失血，动能因子腰斩，欧洲防务股跑输基本面25%，AI叙事从\"卖铲\"切向\"用铲\"。VIX低位不代表风险消散，或只是市场尚未找到足够的理由恐慌。"
  },
  {
    "id": "wscn:3781007",
    "domain": "股票",
    "title": "特朗普再袭伊朗：消耗战还是中期选前最后一搏？",
    "url": "https://wallstreetcn.com/premium/articles/3781007?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T01:45:23+00:00",
    "summary": "特朗普再袭伊朗，能源冲击与中期选举压力叠加，消耗战难以为继，战争终局或成为市场最大预期差。"
  },
  {
    "id": "wscn:3781161",
    "domain": "股票",
    "title": "会见特朗普特使超3小时，普京表态“今天的局势并不简单”",
    "url": "https://wallstreetcn.com/articles/3781161",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T01:02:24+00:00",
    "summary": "普京与特朗普特使会谈逾3小时，美俄直接沟通渠道重启，俄乌双方同步暂停打击两国首都。但普京在会谈开场即表示\"我们今天面对的局势当然并不简单\"，停火令生效前数小时俄军仍出动160余架无人机空袭基辅。领土争议僵持不下，俄方谈判要价随战场优势持续走强，分析认为距离真正的停火协议仍有相当距离。"
  },
  {
    "id": "wscn:3781160",
    "domain": "股票",
    "title": "伊朗导弹袭击美航母，美军：航母成功规避伊朗多次攻击，击中伊3艘油轮！特朗普：美国已经赢了；美情报部门：伊朗已打出自信",
    "url": "https://wallstreetcn.com/articles/3781160",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T00:43:32+00:00",
    "summary": "美军重创三艘伊朗油轮，特朗普称冲突是“小菜一碟”。但全美柴油均价已受局势波及飙创历史新高。美情报披露，伊朗正无视经济制裁展露惊人韧性，蓄力“持久战”直指美中期选举。"
  },
  {
    "id": "wscn:3781159",
    "domain": "股票",
    "title": "上半年金饰消费量降三成，黄金品牌集体加码轻克重硬足金",
    "url": "https://wallstreetcn.com/articles/3781159",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T16:15:07+00:00",
    "summary": "今年上半年，中国金饰消费量同比下滑30%至136吨，消费总金额却上升5%至1437亿元。\n这组“量降..."
  },
  {
    "id": "wscn:3781157",
    "domain": "股票",
    "title": "下周美国CPI会触发9月加息吗？美银、花旗给出两个相反剧本",
    "url": "https://wallstreetcn.com/articles/3781157",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T12:39:39+00:00",
    "summary": "美银证券预计8月核心CPI环比上涨0.22%，认为通胀仍然偏高，足以支持9月加息；花旗则预计核心CPI仅增长0.18%，年率降至2.3%，美联储更可能按兵不动。两家机构的分歧背后，是CPI与PCE走势的背离，以及沃勒对通胀的关键容忍门槛。分析认为，若数据超预期偏热，美联储可能被迫采取更激进的紧缩路径。"
  },
  {
    "id": "wscn:3781156",
    "domain": "股票",
    "title": "智谱悄悄上架天猫：Token越来越便宜，为什么AI公司反而开始限量了",
    "url": "https://wallstreetcn.com/articles/3781156",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T12:19:47+00:00",
    "summary": "模型越强，用户越愿意把编程、搜索、测试等复杂任务交给AI，Token消耗也随之暴增，增速甚至超过成本下降的速度。算力压力之下，AI公司开始从“不限量”转向按额度收费，商业模式也从“卖模型”转向“卖调用”。"
  },
  {
    "id": "wscn:3781158",
    "domain": "股票",
    "title": "AI芯片撑起半壁江山，韩国今年出口剑指万亿美元！",
    "url": "https://wallstreetcn.com/articles/3781158",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T11:54:35+00:00",
    "summary": "韩国今年迄今出口额已达7094亿美元，超过2025年全年纪录。韩国关税厅预计，韩国年度出口额有望于12月初突破1万亿美元。1至8月半导体出口同比增长169.6%，占同期出口41%，AI基础设施投资扩张成为重要驱动力；乘用车出口则同比下降4%，出口结构分化明显。"
  },
  {
    "id": "wscn:3781149",
    "domain": "股票",
    "title": "欧洲LNG库存15年来新低：欧亚抢气，谁扛不住这个冬天？",
    "url": "https://wallstreetcn.com/premium/articles/3781149?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T11:26:19+00:00",
    "summary": "霍尔木兹海峡封锁致卡塔尔供应锐减，欧亚抢气加剧，欧洲库存创十五年低点，冬季或破百，美国难补缺。"
  },
  {
    "id": "wscn:3780964",
    "domain": "股票",
    "title": "荷兰央行秘密运回黄金 它究竟看到了什么？",
    "url": "https://wallstreetcn.com/premium/articles/3780964?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T11:21:32+00:00",
    "summary": "操作本身值得细看，因为它暴露了一种非和平时期的思维方式。"
  },
  {
    "id": "wscn:3780999",
    "domain": "股票",
    "title": "当马斯克开始造叶片，巴菲特也盯上AI用电：AIDC正在重写“电从哪里来”",
    "url": "https://wallstreetcn.com/premium/articles/3780999?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T11:11:16+00:00",
    "summary": "北美AI数据中心建设速度正在快过电网扩容和大发电设备交付，现场主电由备用方案走向数十GW级市场。重型燃机仍占长期基荷优势，但漫长排产给航改燃机、往复式内燃机和固体氧化物燃料电池打开了空间。未来几年的产业机会，更值得从供给稀缺、出货弹性和渗透率变化三个角度观察。"
  },
  {
    "id": "wscn:3781155",
    "domain": "股票",
    "title": "哈尔克岛附近传出爆炸声！伊朗油轮被曝遭美军导弹袭击",
    "url": "https://wallstreetcn.com/articles/3781155",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T11:08:50+00:00",
    "summary": "报道称，一艘伊朗油轮在哈尔克岛附近被美军发射的一枚导弹击中。随着双方报复性打击的交替升级，全球重要原油运输的航道正面临自今年2月冲突爆发以来最严峻的安全考验。"
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
    "id": "hn:49559666",
    "domain": "金融",
    "title": "Tesla Begins Offering Rides in a Car Without a Steering Wheel",
    "url": "https://www.nytimes.com/2026/09/03/business/tesla-cybercab-robotaxi-rides.html",
    "source": "telotortium",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-09-04T02:08:51+00:00",
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
    "id": "hn:49531107",
    "domain": "金融",
    "title": "A Hedge-Fund Titan's Divorce Is Putting Wall Street's Staggering Wealth on Publi",
    "url": "https://www.wsj.com/personal-finance/a-hedge-fund-titans-divorce-is-putting-wall-streets-staggering-wealth-on-public-view-6c419f4c",
    "source": "kamaraju",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-09-02T02:41:04+00:00",
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
