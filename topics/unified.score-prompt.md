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

- 今日日期：`2026-08-17`
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
  "date": "2026-08-17",
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
    "points": 4256586,
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
    "points": 1718176,
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
    "points": 1674421,
    "published_at": "2026-03-14T14:22:56+00:00",
    "summary": "AI 核心概念大串联：LLM, Token, Context, Context Window, Prompt, User Prompt, System Prompt, Tool, MCP, Agent, Agent Skill，一期视频带你打通 AI 底层逻辑！"
  },
  {
    "id": "bvid:BV1j9MP6wEV9",
    "domain": "AI",
    "title": "从零开始，学会让桌面Agent帮你干活！【小白教程】",
    "url": "http://www.bilibili.com/video/av116861865887789",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 1331360,
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
    "points": 1274803,
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
    "points": 1134022,
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
    "points": 1063726,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV12omoB4ExF",
    "domain": "AI",
    "title": "黑马程序员全网最全Coze智能体入门到项目实战全套教程，从AI Agent开发入门到6大AI智能体实战项目，涵盖提示词Prompt、RAG、Bot发布微信公众号",
    "url": "http://www.bilibili.com/video/av115713129843205",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 1043421,
    "published_at": "2025-12-15T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：251215\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\n人工智能开发热门教程：\nAI大模型开发：BV1h1V"
  },
  {
    "id": "bvid:BV1aeLqzUE6L",
    "domain": "AI",
    "title": "10分钟讲清楚 Prompt, Agent, MCP 是什么",
    "url": "http://www.bilibili.com/video/av114410228025650",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 874675,
    "published_at": "2025-05-01T09:00:00+00:00",
    "summary": "up的科学星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV1wugF6YEL3",
    "domain": "AI",
    "title": "再见Claude Code！你好DeepSeek Harness！",
    "url": "http://www.bilibili.com/video/av117089415204498",
    "source": "Lau博士的云组会",
    "platform": "bilibili",
    "points": 597768,
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
    "points": 577957,
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
    "points": 515387,
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
    "points": 437613,
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
    "points": 397826,
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
    "points": 352115,
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
    "points": 266564,
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
    "points": 239849,
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
    "points": 239282,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1i9Z8YhEja",
    "domain": "AI",
    "title": "学 AI，看这个视频就够了！最全程序员 AI 指南：AI核心概念、实用AI工具、AI编程技巧、AI开发技术",
    "url": "http://www.bilibili.com/video/av114262957626976",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 184551,
    "published_at": "2025-04-01T13:56:58+00:00",
    "summary": "AI 时代，程序员要学什么才能不被淘汰呢？这个视频给你答案。带你快速了解 AI 核心概念、AI 常用工具、AI 编程技巧、AI + 编程技术，走在时代的前沿，算是一期硬核的程序员 AI 学习指南视频了~\n还为大家准备了免费开源 AI 知识库：https://ai.codefather.cn，有帮助的话记得三连哦~\n涉及知识点：大模型、Prompt、AI开发平台、RAG知识库、MCP、Ollama本"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 179302,
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
    "points": 167176,
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
    "points": 163806,
    "published_at": "2025-12-28T12:36:33+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 159019,
    "published_at": "2026-04-27T08:51:41+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n   喜欢视频课程的同学一键三连多多支持一下，长按点赞五秒=lv6大佬 可以的发送彩色弹幕哦。\n配套源码项目已打包评论区回复up"
  },
  {
    "id": "bvid:BV11urFBrEc4",
    "domain": "AI",
    "title": "🚀告别Vibe Coding！用Superpowers让Claude Code写出工程级代码，一次通过零报错！遵循TDD最佳实践！支持Codex",
    "url": "http://www.bilibili.com/video/av115877227860495",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 154680,
    "published_at": "2026-01-11T15:43:58+00:00",
    "summary": "🚀开发者必看！Superpowers把专业工程团队方法论固化成Skills，让Claude Code告别越写越乱的困境：规格驱动+代码质量双重保障！AI编程新范式！头脑风暴+计划+执行一条龙自动化\n\n\n🚀🚀🚀 视频简介：\n🎬 本期视频详细演示了开源AI编程工作流系统Superpowers的完整使用方法，并通过开发一款iOS时间线笔记原生应用来实测其效果。\n🔧 核心内容：\nSuperpowers工作"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 133481,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 119664,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1KoGE6cE53",
    "domain": "AI",
    "title": "🚀Claude Code重大突破：Workflow功能完整实战教程！ultrawork召唤无数个Agent协同！自动生成JS脚本实现可复用的精准可控工作流",
    "url": "http://www.bilibili.com/video/av116629702777532",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 117080,
    "published_at": "2026-05-24T13:11:48+00:00",
    "summary": "视频简介：\n 全球首测！Anthropic未官宣的Claude Code Workflow隐藏功能完整使用指南，三大阶段六种形态精准解析！AI编程进入脚本化新纪元\n\n 本期视频详细演示了Anthropic为Claude Code V2.1.47和V2.1.48秘密新增的颠覆性Workflow功能！这个被官方从Changelog中紧急删除却未从代码中移除的&quot;隐藏神器&quot;，将成为继M"
  },
  {
    "id": "bvid:BV1dpdZYBE9q",
    "domain": "AI",
    "title": "零代码让AI秒接海量MCP工具！最适合小白的MCP集合平台",
    "url": "http://www.bilibili.com/video/av114340703243255",
    "source": "AI研究室-帆哥",
    "platform": "bilibili",
    "points": 99791,
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
    "points": 93221,
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
    "points": 91367,
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
    "points": 84414,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV143wwz6E8F",
    "domain": "AI",
    "title": "Claude code科研使用展示与思路分享（提速就靠Ai）",
    "url": "http://www.bilibili.com/video/av116211882920985",
    "source": "科研推土机",
    "platform": "bilibili",
    "points": 74069,
    "published_at": "2026-03-11T18:12:00+00:00",
    "summary": "本期给大家带来的是Claude在Vscode的科研应用演示与我最近的一些心得使用心得，科研速度嘎嘎提升。论文复现画图、数据分析就靠Claude code。这个课程也是科研推土机「系统管理文献课程2.0」学员催我更新的内容，希望能帮助到大家～，这个视频重点讲两个事情：\n1️⃣ 资料获取，free不用怀疑，我是良心可言博主，，关注我(GZTSHNR)～\n2️⃣ 展示如何在VS code实操应用clau"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 54117,
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
    "points": 47625,
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
    "points": 44341,
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
    "points": 40642,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1Y6uC6TE1m",
    "domain": "AI",
    "title": "疯狂Vibe Coding一周，我烧了近100亿Token，做了5个项目！",
    "url": "http://www.bilibili.com/video/av117080321957877",
    "source": "神烦老狗",
    "platform": "bilibili",
    "points": 40574,
    "published_at": "2026-08-12T03:12:41+00:00",
    "summary": "项目地址：\nlocal-ops — 本地服务指挥台（零依赖 Python + 原生前端）：https://github.com/laogou717/local-ops\nmd-wechat — 公众号排版工具：https://github.com/laogou717/md-wechat\ndaydream-room — 白日梦陈列室：https://github.com/laogou717/daydr"
  },
  {
    "id": "bvid:BV1XiD5BQEAj",
    "domain": "AI",
    "title": "Claude Code 接入微信、一行命令把Claude Code装进微信、保姆级教程、微信支持Claude Code（cc-connect）远程开发",
    "url": "http://www.bilibili.com/video/av116350093694897",
    "source": "下班学AI",
    "platform": "bilibili",
    "points": 38846,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV1cCj2ztEf5",
    "domain": "AI",
    "title": "Cursor+Claude Code+Claude 4终极组合！仅用10分钟为开源项目Magentic-UI完美集成JWT用户认证系统，编程效率提升300%",
    "url": "http://www.bilibili.com/video/av114574527307727",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 35131,
    "published_at": "2025-05-26T14:20:15+00:00",
    "summary": "Cursor+Claude Code+Claude 4终极组合！仅用10分钟为开源项目Magentic-UI完美集成JWT用户认证系统，编程效率提升300%，告别传统开发模式！小白也能轻松开发商业项目\n\n🚀🚀🚀视频简介：\n✅【保姆级教程】从技术栈分析到功能实现：Claude Code完整开发流程深度解析！从零开始为微软开源智能体项目添加完整用户认证功能，支持注册登录退出，让你的AI应用瞬间变身多用"
  },
  {
    "id": "bvid:BV1YJ336EEBk",
    "domain": "AI",
    "title": "【AI陪玩】开袋即食的AI接入我的世界教程！",
    "url": "http://www.bilibili.com/video/av116981806143216",
    "source": "万昇Dwin",
    "platform": "bilibili",
    "points": 34206,
    "published_at": "2026-07-26T01:30:00+00:00",
    "summary": "模组：Numen\n项目地址：https://github.com/Dwinovo/minecraft-numen"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 34132,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1sRRYY2EBo",
    "domain": "AI",
    "title": "利用AI编程工具Trae或Cursor免费生成CAD图纸",
    "url": "http://www.bilibili.com/video/av114132447665738",
    "source": "vjmap",
    "platform": "bilibili",
    "points": 32387,
    "published_at": "2025-03-09T12:24:12+00:00",
    "summary": "AI编程助手如Trae和Cursor正在革新工程设计领域的CAD绘图流程。传统CAD绘图耗时且易出错，而AI工具通过代码生成技术，能够将自然语言指令转化为精确的代码，自动生成符合标准的CAD图纸，极大提升了设计效率。这些工具不仅支持多模态输入（如图片、草图），还提供了智能代码补全、错误修复等功能，进一步简化了开发流程。随着大模型如deepseek和claude3.7的出现，AI的智能化程度进一步提"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29623,
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
    "points": 24802,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22708,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1gf3T6KEef",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Vibe Coding】教程！从环境搭建到工作流完整闭环，一套全解决！DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116979708990688",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 22065,
    "published_at": "2026-07-25T08:47:37+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1Z5KU6UExC",
    "domain": "AI",
    "title": "【吴恩达2026】Vibe Coding保姆级教程，手把手从环境搭建到工作流完整闭环！——DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116951003242391",
    "source": "吴恩达AIAgent",
    "platform": "bilibili",
    "points": 21760,
    "published_at": "2026-07-20T07:01:13+00:00",
    "summary": "本套课专门解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 19441,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1BygA6KEAi",
    "domain": "AI",
    "title": "DeepSeek Harness + ComfyUI：Agent开始自己跑AI工作流了！",
    "url": "http://www.bilibili.com/video/av117093508910174",
    "source": "啦啦啦的小黄瓜",
    "platform": "bilibili",
    "points": 16135,
    "published_at": "2026-08-14T11:01:16+00:00",
    "summary": "小助理联系方式：zhuli240828\nComfyUI节点详解网址：uinodes.com，网站使用教程：\n[ComfyUI]全网最详细节点测试以及参数详解，近千节点持续更新，纯干货教程总结梳理。\n\nMiniMax Music3模型以及工作流：https://pan.quark.cn/s/f19f1109a481\n所有模型以及工作流分享：https://pan.quark.cn/s/ef8c640"
  },
  {
    "id": "bvid:BV1DPwGe1Ekf",
    "domain": "AI",
    "title": "Cursor从小白到专家-第15课：如何用Cursor+Dify搭建本地知识库？",
    "url": "http://www.bilibili.com/video/av113836698898908",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 14323,
    "published_at": "2025-01-16T08:55:00+00:00",
    "summary": "在第九课“如何用 cursor + coze 搭建线上知识库”的分享后，有一部分精神股东表示，想要本地知识库的搭建教程。\n.\n有求必应，今天第15课的分享就是“用 cursor + dify 搭建本地知识库”，手把手教会。我们第16课见 ~"
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
    "id": "hn:49323686",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia dramatically reduces amount of OpenAI infra financing it may guarantee",
    "url": "https://www.reuters.com/business/nvidia-scales-back-250-billion-openai-data-center-guarantee-wsj-reports-2026-08-14/",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 143,
    "published_at": "2026-08-16T21:07:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:49189234",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia’s Vera Whitepaper Has a Thread Loose",
    "url": "https://chipsandcheese.com/p/nvidias-vera-whitepaper-has-a-thread",
    "source": "pella",
    "platform": "hackernews",
    "points": 208,
    "published_at": "2026-08-05T21:24:45+00:00",
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
    "id": "hn:49322519",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia discloses $21B stake in SpaceX at end of second quarter",
    "url": "https://www.cnbc.com/2026/08/14/nvidia-discloses-21-billion-stake-in-spacex-at-end-of-second-quarter.html",
    "source": "johnbarron",
    "platform": "hackernews",
    "points": 40,
    "published_at": "2026-08-16T18:40:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:49325115",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC Uses Old Fabs to Make New Chips [video]",
    "url": "https://www.youtube.com/watch?v=cDxVYQrxeiQ",
    "source": "eig",
    "platform": "hackernews",
    "points": 14,
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
    "id": "rss:https://www.tomshardware.com/pc-components/this-portable-external-cd-dvd-drive-comes-with-a-2-5-inch-sata-and-an-sd-card-slot-for-just-usd26-save-10-percent-on-a-modern-essential-for-keeping-physical-media-alive",
    "domain": "AI 算力 / 半导体",
    "title": "This portable, external CD/DVD drive comes with a 2.5-inch SATA and an SD Card slot for just $26 — Save 10% on a modern essential for keeping physical media alive",
    "url": "https://www.tomshardware.com/pc-components/this-portable-external-cd-dvd-drive-comes-with-a-2-5-inch-sata-and-an-sd-card-slot-for-just-usd26-save-10-percent-on-a-modern-essential-for-keeping-physical-media-alive",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T15:18:31+00:00",
    "summary": "If you have a bunch of old CDs or DVDs lying around and want something quick and simple to access them, this external drive can get the job done for you for less than $30 while offering extra features"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/dude-youre-getting-a-dell-ai-server-rack-dell-recycles-famous-ad-campaign-to-appeal-to-its-new-ai-overlords",
    "domain": "AI 算力 / 半导体",
    "title": "Dell CEO unveils new 'Dude, you’re getting a Dell (AI server rack)' video — PC maker recycles famous PC ad campaign to tout its new AI data center products",
    "url": "https://www.tomshardware.com/tech-industry/dude-youre-getting-a-dell-ai-server-rack-dell-recycles-famous-ad-campaign-to-appeal-to-its-new-ai-overlords",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T14:31:33+00:00",
    "summary": "Dell has created a humorous AI-era update to its iconic early-2000s 'Dude, you’re getting a Dell' series of commercials."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/maker-compresses-a-2-9mb-song-1000-times-with-metas-ai-codec-and-prints-it-on-paper-as-eight-qr-codes",
    "domain": "AI 算力 / 半导体",
    "title": "Maker compresses a 2.9MB song by 1000x and prints it on paper as eight QR codes — 21KB song is two minutes long, requires a neural network for playback",
    "url": "https://www.tomshardware.com/tech-industry/maker-compresses-a-2-9mb-song-1000-times-with-metas-ai-codec-and-prints-it-on-paper-as-eight-qr-codes",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T14:22:36+00:00",
    "summary": "The open-source codec Meta released in 2022 converts a waveform into discrete tokens that a matching decoder turns back into audio."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/ukraine-destroys-tu-95-bomber-using-48000-chinese-drone-clone",
    "domain": "AI 算力 / 半导体",
    "title": "Ukraine built a $48,000 long-range drone after covertly snapping Chinese factory photos, clone destroys Russian Tu-95 bomber — attack drone has 2,000 km range, country builds 6,000 flying-wing drones ",
    "url": "https://www.tomshardware.com/tech-industry/drones/ukraine-destroys-tu-95-bomber-using-48000-chinese-drone-clone",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T13:20:00+00:00",
    "summary": "The drone that destroyed a Tupolev Tu-95MS strategic bomber at Russia's Engels-2 air base last month turns out to be the MICH 2000."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/macos-screen-sharing-flaw-exploited-to-root-macs-and-plant-monero-miners",
    "domain": "AI 算力 / 半导体",
    "title": "Critical macOS Screen Sharing flaw gives attackers remote root access — CISA bumps bug to 9.8 severity following active Monero cryptojacking attacks",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/macos-screen-sharing-flaw-exploited-to-root-macs-and-plant-monero-miners",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T13:00:00+00:00",
    "summary": "The Dutch National Cyber Security Centre (NCSC-NL) says that attackers are actively exploiting CVE-2026-65400, an authentication bypass in macOS Screen Sharing."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/google-reportedly-taps-amd-to-design-next-generation-tpu-hybrid-ai-asic-could-integrate-on-package-cpu-cores-for-reinforcement-learning",
    "domain": "AI 算力 / 半导体",
    "title": "Google reportedly taps AMD to design next-generation TPU — hybrid AI ASIC could integrate on-package CPU cores for reinforcement learning",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/google-reportedly-taps-amd-to-design-next-generation-tpu-hybrid-ai-asic-could-integrate-on-package-cpu-cores-for-reinforcement-learning",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T12:40:00+00:00",
    "summary": "Google may be building a TPU with on-package CPU cores specifically for agentic and reinforced learning workloads, according to a rumor."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-says-it-will-launch-new-core-with-nova-lake-on-desktop-first-not-in-data-center-vp-robert-hallock-hopes-enthusiasts-do-the-math-compared-to-amd",
    "domain": "AI 算力 / 半导体",
    "title": "Intel says it will launch new core with Nova Lake on desktop first, not in data center — VP Robert Hallock hopes enthusiasts ‘do the math’ compared to AMD",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-says-it-will-launch-new-core-with-nova-lake-on-desktop-first-not-in-data-center-vp-robert-hallock-hopes-enthusiasts-do-the-math-compared-to-amd",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T12:10:00+00:00",
    "summary": "Intel’s Robert Hallock says he hopes enthusiasts “do the math” compared to AMD, highlighting that the company’s new core architecture will release in consumer processors before the data center."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/3d-printed-sound-powered-jet-engines-propel-micro-drones-fliers-are-completely-silent-researchers-use-ultrasonic-frequencies-to-drive-12-000-rpm-silent-hovering-fliers",
    "domain": "AI 算力 / 半导体",
    "title": "3D-printed sound-powered jet engines propel micro drones — fliers are completely silent; researchers use ultrasonic frequencies to drive 12,000-RPM silent hovering fliers",
    "url": "https://www.tomshardware.com/3d-printing/3d-printed-sound-powered-jet-engines-propel-micro-drones-fliers-are-completely-silent-researchers-use-ultrasonic-frequencies-to-drive-12-000-rpm-silent-hovering-fliers",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T11:50:00+00:00",
    "summary": "A specially shaped 3D-printed resonator can make air shoot out of its nozzle and provide thrust when it hit with the proper frequency. While the prototypes don't deliver practical levels of thrust yet"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/3d-printing-enthusiast-creates-flock-sock-camera-blind-slip-on-cover-attaches-to-broom-handle-to-make-it-easy-to-put-on-devices-placed-on-traffic-and-streetlights",
    "domain": "AI 算力 / 半导体",
    "title": "3D-printing enthusiast creates ‘Flock Sock’ to blind controversial cameras, shares design — slip-on cover attaches to broom handle to make it easy to put on devices placed on traffic and streetlights",
    "url": "https://www.tomshardware.com/3d-printing/3d-printing-enthusiast-creates-flock-sock-camera-blind-slip-on-cover-attaches-to-broom-handle-to-make-it-easy-to-put-on-devices-placed-on-traffic-and-streetlights",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T11:30:00+00:00",
    "summary": "SquidInk created a 3D-printing model that would allow anyone to build an easy-to-install \"protective cover\" for Flock cameras. The \"Flock Sock\" slips on these devices in seconds using a broom handle, "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/the-pc-age-began-45-years-ago-with-the-breakthrough-intel-8088-processor-8-bit-bus-fueled-45-years-of-x86-dominance",
    "domain": "AI 算力 / 半导体",
    "title": "The PC age began 45 years ago with the breakthrough Intel 8088 processor — 8-bit bus fueled 45 years of x86 dominance",
    "url": "https://www.tomshardware.com/pc-components/cpus/the-pc-age-began-45-years-ago-with-the-breakthrough-intel-8088-processor-8-bit-bus-fueled-45-years-of-x86-dominance",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T11:20:00+00:00",
    "summary": "45 years ago, in August 1981, the PC age began in earnest with the launch of the IBM PC Model 5150. At its heart was the Intel 8088 microprocessor."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/modern-oled-tvs-are-just-as-susceptible-to-burn-in-as-older-models-but-theyre-much-brighter-longevity-test-highlights-luminance-headroom-and-efficiency-as-mitigations",
    "domain": "AI 算力 / 半导体",
    "title": "Modern OLEDs are just as vulnerable to burn-in as 2017 panels in 10,000-hour test — twice the brightness and 27% efficiency gains offer crucial headroom",
    "url": "https://www.tomshardware.com/monitors/modern-oled-tvs-are-just-as-susceptible-to-burn-in-as-older-models-but-theyre-much-brighter-longevity-test-highlights-luminance-headroom-and-efficiency-as-mitigations",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T11:10:00+00:00",
    "summary": "Rtings.com's latest update on their Accelerated Longevity Test shows that modern OLED TVs don't offer a clear advantage over older models in terms of burn-in since both show similar image retention af"
  },
  {
    "id": "rss:https://www.tomshardware.com/maker-stem/xtool-m2-color-craft-laser-and-engraver-review",
    "domain": "AI 算力 / 半导体",
    "title": "xTool M2 color craft laser and engraver review: Improved print head and positioning cameras at a lower price",
    "url": "https://www.tomshardware.com/maker-stem/xtool-m2-color-craft-laser-and-engraver-review",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T11:05:00+00:00",
    "summary": "The M2 is xTool’s second take on an all-in-one craft tool in a box. It isn’t just an iterative update to the M1 Ultra, the new M2 color craft laser and engraver thoroughly remixes the offering by addi"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/thieves-swap-rtx-5080-gpus-for-rtx-3060s-in-chinese-gaming-hotels-rogue-downgrades-go-unnoticed-until-sudden-blackout-exposes-usd12-000-heist",
    "domain": "AI 算力 / 半导体",
    "title": "Thieves swap RTX 5080 GPUs for RTX 3060s in Chinese gaming hotels — rogue 'downgrades' go unnoticed until sudden blackout exposes $12,000 heist",
    "url": "https://www.tomshardware.com/pc-components/gpus/thieves-swap-rtx-5080-gpus-for-rtx-3060s-in-chinese-gaming-hotels-rogue-downgrades-go-unnoticed-until-sudden-blackout-exposes-usd12-000-heist",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T10:50:00+00:00",
    "summary": "Two thieves in China have been arrested after they were caught stealing high-end GPUs from gaming hotels. They'd check into rooms with RTX 5080s, replace them with RTX 3060s that looked similar, and n"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/former-missouri-farm-bureau-president-offers-his-farm-for-a-data-center",
    "domain": "AI 算力 / 半导体",
    "title": "Ex-farm bureau chief invites AI data center developers to buy his land —argues blocked $6.3B project will just move to willing neighbors, defies 500-jurisdiction moratorium wave and 70% public opposit",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/former-missouri-farm-bureau-president-offers-his-farm-for-a-data-center",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T10:30:00+00:00",
    "summary": "Blake Hurst spent a decade running the state's largest farm lobby. Now he's publicly courting the developers his neighbors froze out."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/ukrainian-drone-regiment-decimates-3-500-strong-u-s-armored-brigade-combat-team-in-war-game-reveals-shortcomings-in-american-response-as-drones-easily-spotted-and-destroyed-tanks-and-heavy-armored-vehicles",
    "domain": "AI 算力 / 半导体",
    "title": "Ukrainian drone regiment ‘decimates’ 3,500-strong U.S. armored brigade combat team in war game — High drone kill-rate forced continuous 'respawns,' reveals shortcomings in American response as drones ",
    "url": "https://www.tomshardware.com/tech-industry/drones/ukrainian-drone-regiment-decimates-3-500-strong-u-s-armored-brigade-combat-team-in-war-game-reveals-shortcomings-in-american-response-as-drones-easily-spotted-and-destroyed-tanks-and-heavy-armored-vehicles",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T10:00:00+00:00",
    "summary": "The 3rd Brigade Combat Team (3rd BCT) of the 1st Cavalry Division was defeated in military exercises by the opposing force, which included a regiment of Ukrainian drone operators. Even though the 3rd "
  },
  {
    "id": "rss:https://www.tomshardware.com/software/applications/rogue-ios-developer-creates-app-that-simulates-messages-sent-by-carrier-pigeon-messages-only-travel-at-100mph-la-to-nyc-correspondence-takes-22-hours-to-deliver-virtual-birds-can-get-distracted-or-even-lost",
    "domain": "AI 算力 / 半导体",
    "title": "Rogue iOS developer creates app that simulates messages sent by carrier pigeon; messages only travel at 100mph — LA to NYC correspondence takes 22 hours to deliver; virtual birds can get distracted or",
    "url": "https://www.tomshardware.com/software/applications/rogue-ios-developer-creates-app-that-simulates-messages-sent-by-carrier-pigeon-messages-only-travel-at-100mph-la-to-nyc-correspondence-takes-22-hours-to-deliver-virtual-birds-can-get-distracted-or-even-lost",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T09:30:00+00:00",
    "summary": "Carrier Pidge slows down your electronic communications to a more natural speed."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/grab-this-rtx-5070-gaming-pc-for-just-usd1-499-saving-usd600-off-list-price-acer-nitro-85-prebuilt-comes-with-16gb-of-ram-core-ultra-7-265f-and-a-1tb-pcie-4-0-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Grab this RTX 5070 gaming PC for just $1,499, saving $600 off list price — Acer Nitro 85 prebuilt comes with 16GB of RAM, Core Ultra 7 265F, and a 1TB PCIe 4.0 SSD",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/grab-this-rtx-5070-gaming-pc-for-just-usd1-499-saving-usd600-off-list-price-acer-nitro-85-prebuilt-comes-with-16gb-of-ram-core-ultra-7-265f-and-a-1tb-pcie-4-0-ssd",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T20:53:34+00:00",
    "summary": "The Acer Nitro 85 gaming desktop is currently on sale for $1,499, which is $600 off its regular price for a PC that would otherwise cost you $2,000 to spec out yourself."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/hdds/peer-reviewed-study-of-443000-backblaze-drivers-ranks-hgst-most-reliable-and-toshiba-least",
    "domain": "AI 算力 / 半导体",
    "title": "Peer-reviewed study of 443,000 Backblaze hard drives ranks HGST most reliable and Toshiba the least — Analysis of 1.66 million drive-years finds Seagate and Toshiba HDDs fail at roughly twice the rate",
    "url": "https://www.tomshardware.com/pc-components/hdds/peer-reviewed-study-of-443000-backblaze-drivers-ranks-hgst-most-reliable-and-toshiba-least",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T15:30:10+00:00",
    "summary": "Backblaze's quarterly reports compare whichever drives are available at the time."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/futuristic-mosquito-zapping-laser-now-available-to-buy-video-shows-device-in-action-tiny-device-shoots-down-bugs-like-a-personal-air-defense-system-but-costs-usd1-000",
    "domain": "AI 算力 / 半导体",
    "title": "Futuristic mosquito-zapping laser now available to buy, video shows device in action — tiny device shoots down bugs like a personal air defense system, but costs $1,000",
    "url": "https://www.tomshardware.com/peripherals/futuristic-mosquito-zapping-laser-now-available-to-buy-video-shows-device-in-action-tiny-device-shoots-down-bugs-like-a-personal-air-defense-system-but-costs-usd1-000",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T15:04:47+00:00",
    "summary": "This anti-mosquito air defense laser system has successfully passed the crowdfunding stage and is now readily available on the market. It costs around $1,000, but it will be money well spent if it can"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/grab-this-nvidia-rtx-5070-ti-gaming-pc-for-usd2-099-before-it-sells-out-prebuilt-powerhouse-includes-a-core-ultra-7-265kf-32gb-ram-1tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Grab this Nvidia RTX 5070 Ti gaming PC for $2,099 before it sells out —prebuilt powerhouse includes a Core Ultra 7 265KF, 32GB RAM, 1TB SSD",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/grab-this-nvidia-rtx-5070-ti-gaming-pc-for-usd2-099-before-it-sells-out-prebuilt-powerhouse-includes-a-core-ultra-7-265kf-32gb-ram-1tb-ssd",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T14:23:36+00:00",
    "summary": "The Acer Predator Orion 6000 gaming desktop is currently on sale for $2,099, $700 off its regular price."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/nvidia-turns-usd5b-intel-stock-bet-into-usd30b-windfall-filing-reveals-new-usd21b-spacex-stake-and-complete-exit-from-arm-stock",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia turns $5B Intel stock bet into $30B windfall — filing reveals new $21B SpaceX stake and complete exit from Arm stock",
    "url": "https://www.tomshardware.com/tech-industry/nvidia-turns-usd5b-intel-stock-bet-into-usd30b-windfall-filing-reveals-new-usd21b-spacex-stake-and-complete-exit-from-arm-stock",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T14:16:35+00:00",
    "summary": "Nvidia quietly makes strategic and financial investments in clients, partners, and suppliers: CoreWeave, Coherent, Intel, Nokia, and SpaceX."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/vlc-media-player-bug-reportedly-causes-33-second-delay-when-playing-mp3-files-on-windows-developers-say-microsoft-defender-is-to-blame",
    "domain": "AI 算力 / 半导体",
    "title": "Devs blame Windows for VLC media player bug that causes 33-second delay when playing MP3 files — creators allege Microsoft Defender blocking plugin cache is to blame",
    "url": "https://www.tomshardware.com/software/windows/vlc-media-player-bug-reportedly-causes-33-second-delay-when-playing-mp3-files-on-windows-developers-say-microsoft-defender-is-to-blame",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T13:30:00+00:00",
    "summary": "VLC developers say a Windows 11 issue involving Microsoft Defender can interfere with the media player's plugin cache and cause unusually long playback delays."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-ryzen-7-7700x3d-vs-ryzen-7-7800x3d-faceoff",
    "domain": "AI 算力 / 半导体",
    "title": "AMD Ryzen 7 7700X3D vs Ryzen 7 7800X3D faceoff — seeing double with Zen 4 X3D",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-ryzen-7-7700x3d-vs-ryzen-7-7800x3d-faceoff",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T13:25:00+00:00",
    "summary": "AMD's Ryzen 7 7700X3D takes on the old favorite across performance, pricing, and power consumption."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/white-house-authorizes-private-companies-to-hack-foreign-cybercrime-groups",
    "domain": "AI 算力 / 半导体",
    "title": "White House authorizes private companies to launch 'hack-back' cyberattacks that destroy data and systems, targeting foreign cybercrime organizations — vetted organizations can now conduct offensive c",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/white-house-authorizes-private-companies-to-hack-foreign-cybercrime-groups",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T13:00:00+00:00",
    "summary": "President Trump signed a memorandum on August 12 establishing the first U.S. program that lets vetted private companies conduct offensive cyber operations."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/this-week-on-toms-hardware-premium-august-14-2026-testing-the-bc-250-our-interview-with-intels-robert-hallock-and-a-big-week-for-optical",
    "domain": "AI 算力 / 半导体",
    "title": "This week on Tom's Hardware Premium: August 14, 2026 — Testing the BC-250, our interview with Intel's Robert Hallock, and a big week for optical",
    "url": "https://www.tomshardware.com/tech-industry/this-week-on-toms-hardware-premium-august-14-2026-testing-the-bc-250-our-interview-with-intels-robert-hallock-and-a-big-week-for-optical",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T12:30:00+00:00",
    "summary": "This week, we tested AMD's BC-250 in gaming workloads, published an unredacted interview with an AMD executive, and published a slew of articles surrounding a new flashpoint in the ongoing AI buildout"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/flight-ready-drones-3d-printed-and-built-on-aircraft-carrier-during-us-navy-exercise-a-containerized-factory-on-uss-essex-functioned-despite-rough-seas-and-12-foot-waves",
    "domain": "AI 算力 / 半导体",
    "title": "US Navy 3D prints combat-ready drones and 1,000+ parts aboard aircraft carrier during exercise — containerized factory fabricated 80-mph FPVs and critical spares despite rough seas and 12-foot waves",
    "url": "https://www.tomshardware.com/tech-industry/drones/flight-ready-drones-3d-printed-and-built-on-aircraft-carrier-during-us-navy-exercise-a-containerized-factory-on-uss-essex-functioned-despite-rough-seas-and-12-foot-waves",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T12:10:00+00:00",
    "summary": "During a two-week journey to Hawaii, a containerized factory aboard the USS Essex 3D-printed a dozen flight-ready drones, as well as over 1,000 parts including vital spares for Apache helicopters."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/liquid-cooling/ocypus-sigma-l36-pro-review",
    "domain": "AI 算力 / 半导体",
    "title": "Ocypus Sigma L36 Pro Review: How is this LCD AIO so cheap?",
    "url": "https://www.tomshardware.com/pc-components/liquid-cooling/ocypus-sigma-l36-pro-review",
    "source": "Albert Thomas",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T12:05:00+00:00",
    "summary": "The Ocypus Sigma L36 Pro is a high-performance AIO that includes a fancy 3.5-inch display and a low price tag. We’ve tested this liquid cooler paired with AMD’s Ryzen 9 9950X3D CPU to benchmark therma"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/sk-hynix-is-allegedly-out-of-replacement-ssds-for-warranty-returns-chipmakers-original-price-refund-leaves-buyers-stranded-in-the-storage-shortage",
    "domain": "AI 算力 / 半导体",
    "title": "SK hynix runs out of replacement SSDs and defaults to original purchase price refunds — fine-print warranty clause shortchanges buyers as drive prices double",
    "url": "https://www.tomshardware.com/pc-components/ssds/sk-hynix-is-allegedly-out-of-replacement-ssds-for-warranty-returns-chipmakers-original-price-refund-leaves-buyers-stranded-in-the-storage-shortage",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T11:50:00+00:00",
    "summary": "A Redditor reports a case in which SK hynix reportedly offers a refund for a malfunctioning SSD at the original purchase price instead of a direct replacement."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-says-pc-market-is-a-tale-of-two-kingdoms-with-mainstream-taking-a-beating-vp-suggests-a-split-between-mainstream-and-enthusiast-sockets-across-the-industry",
    "domain": "AI 算力 / 半导体",
    "title": "Intel says PC market is ‘a tale of two kingdoms’ with mainstream ‘taking a beating’ — VP suggests a split between mainstream and enthusiast sockets across the industry",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-says-pc-market-is-a-tale-of-two-kingdoms-with-mainstream-taking-a-beating-vp-suggests-a-split-between-mainstream-and-enthusiast-sockets-across-the-industry",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T11:30:00+00:00",
    "summary": "Intel VP Robert Hallock suggests the PC industry is going to see a split between mainstream and enthusiast sockets if current market conditions don’t let up."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/nanya-engineer-used-360-degree-cam-hidden-in-snacks-in-attempt-to-steal-dram-process-tech-for-china-it-security-team-pinpointed-perp-due-to-cameras-leaky-wireless-signals",
    "domain": "AI 算力 / 半导体",
    "title": "Engineer used 360-degree cam hidden in bag of snacks in attempt to steal DRAM process tech for China — IT security team pinpointed perp due to camera's leaky wireless signals",
    "url": "https://www.tomshardware.com/pc-components/dram/nanya-engineer-used-360-degree-cam-hidden-in-snacks-in-attempt-to-steal-dram-process-tech-for-china-it-security-team-pinpointed-perp-due-to-cameras-leaky-wireless-signals",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T11:00:00+00:00",
    "summary": "Nanya engineer tried to steal DRAM process technology, manufacturing methods to pass them to a Chinese rival and get a higher-paid job, but gets caught and now faces time in prison."
  },
  {
    "id": "hn:49306491",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia discloses $21B stake in SpaceX",
    "url": "https://www.ft.com/content/6f66a76d-0b2d-4301-886c-87ecc046731b",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-08-15T01:02:55+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/an-introduction-to-software-prototyping-unlocking-soc-software-verification-with-profpga-cs/",
    "domain": "AI 算力 / 半导体",
    "title": "An Introduction to Software Prototyping: Unlocking SoC Software Verification with proFPGA CS",
    "url": "https://www.eetimes.com/an-introduction-to-software-prototyping-unlocking-soc-software-verification-with-profpga-cs/",
    "source": "Siemens",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T15:22:50+00:00",
    "summary": "Discover how the Veloce™ proFPGA CS platform delivers a flexible, modular architecture that scales across the full spectrum of SoC software verification needs. The post An Introduction to Software Pro"
  },
  {
    "id": "rss:https://www.eetimes.com/intel-at-a-memory-crossroads-again/",
    "domain": "AI 算力 / 半导体",
    "title": "Intel at a Memory Crossroads, Again",
    "url": "https://www.eetimes.com/intel-at-a-memory-crossroads-again/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T13:01:36+00:00",
    "summary": "The CPU specialist heeds a memory comeback while memory chips transform from commodity to AI gold rush. The post Intel at a Memory Crossroads, Again appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/semiconductor-equipment-shifts-to-build-to-print-manufacturing/",
    "domain": "AI 算力 / 半导体",
    "title": "Semiconductor Equipment Shifts To Build-to-Print Manufacturing",
    "url": "https://www.eetimes.com/semiconductor-equipment-shifts-to-build-to-print-manufacturing/",
    "source": "Emily Newton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T10:56:17+00:00",
    "summary": "Semiconductor equipment OEMs look to build-to-print for greater capacity. The post Semiconductor Equipment Shifts To Build-to-Print Manufacturing appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/smartphone-makers-squeezed-by-soaring-chip-costs/",
    "domain": "AI 算力 / 半导体",
    "title": "Smartphone Makers Squeezed by Soaring Chip Costs",
    "url": "https://www.eetimes.com/smartphone-makers-squeezed-by-soaring-chip-costs/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T18:47:35+00:00",
    "summary": "Chip costs are gutting smartphone margins; expect pricier iPhones and fewer cheap phones. The post Smartphone Makers Squeezed by Soaring Chip Costs appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/enabling-robot-operating-systems/",
    "domain": "AI 算力 / 半导体",
    "title": "Enabling Robot Operating Systems—Introducing the ADI Trinamic Motor Controller ROS1 Driver",
    "url": "https://www.eetimes.com/enabling-robot-operating-systems/",
    "source": "Krizelle Paulene Apostol , Software Systems Engineer, Jamila Macagba , Senior Software Systems Engineer, and Maggie Maralit , Software Systems Design Engineering Manager",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T16:14:17+00:00",
    "summary": "Robot Operating System (ROS) drivers were developed on Analog Devices prod ucts so that they can be readily used within a ROS ecosystem. This article will give an overview on how to use and integrate "
  },
  {
    "id": "rss:https://www.eetimes.com/ais-next-bottleneck-is-public-consent/",
    "domain": "AI 算力 / 半导体",
    "title": "AI’s Next Bottleneck Is Public Consent",
    "url": "https://www.eetimes.com/ais-next-bottleneck-is-public-consent/",
    "source": "Zaheer Ali",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T14:13:06+00:00",
    "summary": "AI’s next choke point isn’t chips—it’s public trust as states slow data centers over power, water, and secrecy. The post AI&#8217;s Next Bottleneck Is Public Consent appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/neuromorphic-computing-needs-more-than-novel-chips/",
    "domain": "AI 算力 / 半导体",
    "title": "Neuromorphic Computing Needs More Than Novel Chips",
    "url": "https://www.eetimes.com/neuromorphic-computing-needs-more-than-novel-chips/",
    "source": "Isaac Lopez, President, OmniScale Media & Charity Plata, Communications Chair, SC26",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T13:00:00+00:00",
    "summary": "Katie Schuman on why neuromorphic computing needs HPC engineers, compilers, and shared hardware access to move from promise to practice. The post Neuromorphic Computing Needs More Than Novel Chips app"
  },
  {
    "id": "rss:https://www.eetimes.com/using-agents-to-maximize-nvidia-jetson-memory-usage-at-the-edge/",
    "domain": "AI 算力 / 半导体",
    "title": "Using Agents to Maximize NVIDIA Jetson Memory Usage at the Edge",
    "url": "https://www.eetimes.com/using-agents-to-maximize-nvidia-jetson-memory-usage-at-the-edge/",
    "source": "Morten Block, Global Eng. Director, Segments and Technology go-to-market",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T12:00:00+00:00",
    "summary": "Discover how NVIDIA Jetson's software optimization stack can reclaim significant memory, enabling teams to run bigger AI workloads at a lower module cost. The post Using Agents to Maximize NVIDIA Jets"
  },
  {
    "id": "rss:https://www.eetimes.com/hong-kong-electronics-fairs-launch-in-october/",
    "domain": "AI 算力 / 半导体",
    "title": "Hong Kong Electronics Fairs Launch in October!",
    "url": "https://www.eetimes.com/hong-kong-electronics-fairs-launch-in-october/",
    "source": "HKTDC",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T08:00:00+00:00",
    "summary": "Cutting-Edge Technologies on Display This October, Shaping the Future of Industries The post Hong Kong Electronics Fairs Launch in October! appeared first on EE Times."
  },
  {
    "id": "hn:49248477",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia is pulling Wall Street into the AI buildout",
    "url": "https://thenextweb.com/news/nvidia-500-billion-wall-street-ai-infrastructure-funding-package",
    "source": "berkeleyjunk",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-08-10T19:25:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:49279812",
    "domain": "AI 算力 / 半导体",
    "title": "Why space is a terrible place to cool a data center",
    "url": "https://thenewstack.io/spacex-and-nvidias-orbital-ai-datacenter-fantasy/",
    "source": "CrankyBear",
    "platform": "hackernews",
    "points": 16,
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
    "points": 966,
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
    "points": 865,
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
    "points": 306,
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
    "id": "hn:48965880",
    "domain": "大厂 AI 动态",
    "title": "Ollama: All Aboard Open Models",
    "url": "https://ollama.com/blog/all-aboard-open-models",
    "source": "inferhaven",
    "platform": "hackernews",
    "points": 138,
    "published_at": "2026-07-19T07:59:44+00:00",
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
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/980817/openai-disbands-preparedness-team",
    "domain": "大厂 AI 动态",
    "title": "OpenAI reportedly disbanded its preparedness team",
    "url": "https://www.theverge.com/ai-artificial-intelligence/980817/openai-disbands-preparedness-team",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T21:32:56+00:00",
    "summary": "According to the Financial Times, OpenAI disbanded its preparedness team at the end of last month. The job of the preparedness team was to assess if models posed serious risks and develop ways to miti"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/980799/open-mike-eagle-and-kenny-segal-doomed-review",
    "domain": "大厂 AI 动态",
    "title": "Open Mike Eagle and Kenny Segal crafted a hip hop breakup masterpiece",
    "url": "https://www.theverge.com/entertainment/980799/open-mike-eagle-and-kenny-segal-doomed-review",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T20:31:37+00:00",
    "summary": "\"Breakups are… tough.\" It's the opening lines of an interlude towards the end of DOOMED! Called \"It Happens in Every Universe.\" It's also basically the thesis of the entire record. It's no grand revel"
  },
  {
    "id": "rss:https://www.theverge.com/tech/980752/amazon-class-action-arbitration-terms-and-conditions",
    "domain": "大厂 AI 动态",
    "title": "Amazon is trying to crush class-action suits before they get started",
    "url": "https://www.theverge.com/tech/980752/amazon-class-action-arbitration-terms-and-conditions",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T17:35:02+00:00",
    "summary": "On Friday, Amazon customers received an email alerting them to an update to the site's terms and conditions. Most notably, it stated that disputes would now be resolved through arbitration and said us"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/980742/chatgpts-computer-history-tracks-your-clicks-and-keystrokes",
    "domain": "大厂 AI 动态",
    "title": "ChatGPT’s Computer History tracks your clicks and keystrokes",
    "url": "https://www.theverge.com/ai-artificial-intelligence/980742/chatgpts-computer-history-tracks-your-clicks-and-keystrokes",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T14:56:40+00:00",
    "summary": "ChatGPT's desktop app on macOS has a new feature called Computer History that turns your actions into training data, learning how you work, suggesting automations, and even picking up tasks you left h"
  },
  {
    "id": "rss:https://www.theverge.com/column/980337/rogue-ai-science-fiction-openai",
    "domain": "大厂 AI 动态",
    "title": "Rogue AI aren’t science fiction anymore",
    "url": "https://www.theverge.com/column/980337/rogue-ai-science-fiction-openai",
    "source": "Robert Hart",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T12:00:00+00:00",
    "summary": "This is The Stepback, a weekly newsletter breaking down one essential story from the tech world. For more on AI safety, follow Robert Hart. The Stepback arrives in our subscribers' inboxes at 8AM ET. "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/980448/polaroid-go-second-generation-film-pack-bundle-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Polaroid’s tiny instant camera is $72 and includes a free pack of film",
    "url": "https://www.theverge.com/gadgets/980448/polaroid-go-second-generation-film-pack-bundle-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T03:00:00+00:00",
    "summary": "Smartphone cameras are convenient, but they lack the charm of analog instant cameras. If you’re trying to relive the nostalgia of waiting for an instant photo to develop, Amazon is selling the second-"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/980720/matt-groening-simpsons-hit-run-d23",
    "domain": "大厂 AI 动态",
    "title": "Matt Groening lets slip that Simpsons: Hit &#038; Run might be making a comeback",
    "url": "https://www.theverge.com/entertainment/980720/matt-groening-simpsons-hit-run-d23",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T21:56:13+00:00",
    "summary": "At D23, when asked about the potential for a sequel to the cult classic The Simpsons: Hit &#38; Run game, Matt Groening replied, \"I think the original game is coming back in some form,\" before current"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/980502/roleplay-as-an-ai-chatbot",
    "domain": "大厂 AI 动态",
    "title": "Have a laugh at AI’s expense by roleplaying as a chatbot",
    "url": "https://www.theverge.com/entertainment/980502/roleplay-as-an-ai-chatbot",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T20:45:00+00:00",
    "summary": "Your AI Slop Bores Me is brilliant in its simplicity. There are two tabs: human and LARP as an AI. On one side you enter a request. On the other, you submit an answer. But the important thing is that "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/980275/elektron-model-cycles-model-samples-groovebox-electronic-music-instruments-review",
    "domain": "大厂 AI 动态",
    "title": "Don&#8217;t overlook Elektron&#8217;s budget electronic music instruments",
    "url": "https://www.theverge.com/gadgets/980275/elektron-model-cycles-model-samples-groovebox-electronic-music-instruments-review",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T17:00:00+00:00",
    "summary": "When I'm asked what to buy if you want to get into making electronic music, I often recommend Elektron's budget-minded Model:Samples and Model:Cycles grooveboxes. They don't grab headlines the way Tee"
  },
  {
    "id": "rss:https://www.theverge.com/report/980288/switched-on-pop-nate-sloan-charlie-harding-podcast-netflix-interview",
    "domain": "大厂 AI 动态",
    "title": "Switched on Pop’s Nate Sloan and Charlie Harding love fresh vegetables and guitar pedals",
    "url": "https://www.theverge.com/report/980288/switched-on-pop-nate-sloan-charlie-harding-podcast-netflix-interview",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T15:00:00+00:00",
    "summary": "As if you needed more reason to love Carly Rae Jepsen's \"Call Me Maybe\" beyond its pop perfection, it is also, according to lore, the genesis for Switched on Pop, one of the best music podcasts out th"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/16/stripe-will-reportedly-acquire-ai-gateway-startup-openrouter-for-7b/",
    "domain": "大厂 AI 动态",
    "title": "Stripe will reportedly acquire AI gateway startup OpenRouter for $7B+",
    "url": "https://techcrunch.com/2026/08/16/stripe-will-reportedly-acquire-ai-gateway-startup-openrouter-for-7b/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T20:57:04+00:00",
    "summary": "OpenRouter's CEO recently described the startup as Stripe for AI."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/16/why-people-arent-buying-mark-zuckerbergs-ai-future/",
    "domain": "大厂 AI 动态",
    "title": "Why people aren’t buying Mark Zuckerberg’s AI future",
    "url": "https://techcrunch.com/2026/08/16/why-people-arent-buying-mark-zuckerbergs-ai-future/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T20:32:01+00:00",
    "summary": "On the latest episode of Equity podcast, we discuss why not everyone is buying Zuckerberg’s vision."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/16/anthropic-ceo-says-ai-backlash-is-fundamentally-a-crisis-of-trust/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic CEO says AI backlash is ‘fundamentally a crisis of trust’",
    "url": "https://techcrunch.com/2026/08/16/anthropic-ceo-says-ai-backlash-is-fundamentally-a-crisis-of-trust/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T16:53:51+00:00",
    "summary": "Dario Amodei is pushing back against the idea that he's been painting an overly pessimistic picture of AI."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/16/techcrunch-mobility-the-shifting-flight-path-of-electric-air-taxis/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Mobility: The shifting flight path of electric air taxis",
    "url": "https://techcrunch.com/2026/08/16/techcrunch-mobility-the-shifting-flight-path-of-electric-air-taxis/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T16:04:00+00:00",
    "summary": "Welcome back to TechCrunch Mobility — your central hub for news and insights on the future of transportation."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/15/woman-claims-her-stepfather-used-grok-to-transform-childhood-photo-into-explicit-imagery/",
    "domain": "大厂 AI 动态",
    "title": "Woman claims her stepfather used Grok to transform childhood photo into explicit imagery",
    "url": "https://techcrunch.com/2026/08/15/woman-claims-her-stepfather-used-grok-to-transform-childhood-photo-into-explicit-imagery/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T21:29:19+00:00",
    "summary": "The woman claimed that AI tools are \"taking everyday life and turning it into child sexual abuse.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/15/anthropic-shares-more-details-about-how-claudes-new-watermarks-will-work/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic shares more details about how Claude’s new watermarks will work",
    "url": "https://techcrunch.com/2026/08/15/anthropic-shares-more-details-about-how-claudes-new-watermarks-will-work/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T18:58:39+00:00",
    "summary": "How will the watermarking actually work? Can it be hidden with editing? And how does this affect code?"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/15/spacex-officially-closes-its-cursor-acquisition/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX officially closes its Cursor acquisition",
    "url": "https://techcrunch.com/2026/08/15/spacex-officially-closes-its-cursor-acquisition/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T16:30:00+00:00",
    "summary": "AI coding startup Cursor is now officially a part of SpaceX."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/15/how-to-tell-if-your-ai-platforms-accounts-have-been-hacked/",
    "domain": "大厂 AI 动态",
    "title": "How to tell if your AI platforms’ accounts have been hacked",
    "url": "https://techcrunch.com/2026/08/15/how-to-tell-if-your-ai-platforms-accounts-have-been-hacked/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T16:10:00+00:00",
    "summary": "A guide on how to check if hackers have broken into your accounts on the most popular AI platforms."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/15/every-fusion-startup-that-has-raised-over-100m/",
    "domain": "大厂 AI 动态",
    "title": "Every fusion startup that has raised over $100M",
    "url": "https://techcrunch.com/2026/08/15/every-fusion-startup-that-has-raised-over-100m/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T13:15:20+00:00",
    "summary": "Fusion startups have raised $7.1 billion to date, with the majority of it going to a handful of companies."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/08/wildfire-smoke-now-bigger-prenatal-threat-than-human-sources-of-air-pollution/",
    "domain": "大厂 AI 动态",
    "title": "Wildfire smoke now bigger prenatal threat than human sources of air pollution",
    "url": "https://arstechnica.com/science/2026/08/wildfire-smoke-now-bigger-prenatal-threat-than-human-sources-of-air-pollution/",
    "source": "Liza Gross",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T10:00:59+00:00",
    "summary": "Regulations reduced prenatal exposure to harmful emissions, but wildfire smoke is erasing gains."
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/08/visionquest-trailer-kicks-off-disneys-d23-fan-event/",
    "domain": "大厂 AI 动态",
    "title": "VisionQuest trailer kicks off Disney's D23 fan event",
    "url": "https://arstechnica.com/culture/2026/08/visionquest-trailer-kicks-off-disneys-d23-fan-event/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T21:21:27+00:00",
    "summary": "Also: Ahsoka S2 teaser, Doomsday trailer, news about MCU's X-Men and Star Wars: Starfighter"
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/08/ukraine-strikes-major-russian-rocket-factory-with-cruise-missiles/",
    "domain": "大厂 AI 动态",
    "title": "Ukraine strikes major Russian rocket factory with cruise missiles",
    "url": "https://arstechnica.com/space/2026/08/ukraine-strikes-major-russian-rocket-factory-with-cruise-missiles/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T15:46:05+00:00",
    "summary": "\"Flamingo missiles were used. A good achievement.\""
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/08/so-much-solar-digging-into-the-list-of-every-us-power-plant-that-went-online-this-year/",
    "domain": "大厂 AI 动态",
    "title": "So much solar: Digging into the list of every US power plant that went online this year",
    "url": "https://arstechnica.com/science/2026/08/so-much-solar-digging-into-the-list-of-every-us-power-plant-that-went-online-this-year/",
    "source": "Dan Gearino, Inside Climate News",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T11:09:57+00:00",
    "summary": "Utility-scale solar leads by a mile, followed by batteries. Fossil fuels, not so much."
  },
  {
    "id": "rss:https://www.producthunt.com/products/chert",
    "domain": "大厂 AI 动态",
    "title": "Chert",
    "url": "https://www.producthunt.com/products/chert",
    "source": "Garry Tan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T04:01:04+00:00",
    "summary": "Vapi for FaceTime: AI video agents in a few lines Discussion | Link"
  },
  {
    "id": "rss:https://sspai.com/post/113524",
    "domain": "大厂 AI 动态",
    "title": "派早报：😭（放声大哭）成为最流行 emoji",
    "url": "https://sspai.com/post/113524",
    "source": "少数派编辑部",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T22:54:56+00:00",
    "summary": "😭（放声大哭）成为最流行 emoji美国要求合作方在中美 AI 竞赛中「选边站」ChatGPT 上线使用历史记录功能美国政府敦促苹果不要购买中国内存芯片uBlock Origin 放弃维护 Facebook 广告规则索尼加速向娱乐业务转型看看就行的简讯少数派的近期动态你可能错过的好文章查看全文"
  },
  {
    "id": "rss:https://sspai.com/post/113495",
    "domain": "大厂 AI 动态",
    "title": "浏览器扩展合集： 我们为你找到了这 6 款实用、 有趣的「新玩意」",
    "url": "https://sspai.com/post/113495",
    "source": "克莱德",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T04:48:21+00:00",
    "summary": "在浏览器扩展这边，近期又有哪些好用、有趣的「新玩意」呢？查看全文"
  },
  {
    "id": "rss:https://sspai.com/post/111974",
    "domain": "大厂 AI 动态",
    "title": "有毒职场正在炼成：OKR 变成 KPI，敏捷开发变成切碎的瀑布",
    "url": "https://sspai.com/post/111974",
    "source": "LOSSES",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T07:07:54+00:00",
    "summary": "Matrix首页推荐Matrix是少数派的写作社区，我们主张分享真实的产品体验，有实用价值的经验与思考。我们会不定期挑选Matrix最优质的文章，展示来自用户的最真实的体验和观点。文章代表作者个人观点 ...查看全文"
  },
  {
    "id": "hn:48959297",
    "domain": "大厂 AI 动态",
    "title": "Our Approach to Bioresilience: Isomorphic Labs and Google DeepMind",
    "url": "https://deepmind.google/blog/our-approach-to-bioresilience/",
    "source": "bookofjoe",
    "platform": "hackernews",
    "points": 83,
    "published_at": "2026-07-18T16:02:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:49187259",
    "domain": "大厂 AI 动态",
    "title": "Sula: A Gemini protocol server written in Scryer Prolog",
    "url": "https://sagredo.dev/projects/sula/",
    "source": "triska",
    "platform": "hackernews",
    "points": 58,
    "published_at": "2026-08-05T18:52:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:48993130",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.6 Flash",
    "url": "https://console.cloud.google.com/agent-platform/publishers/google/model-garden/gemini-3.6-flash",
    "source": "marrf",
    "platform": "hackernews",
    "points": 74,
    "published_at": "2026-07-21T14:56:15+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/14/talks-to-sell-paypal-to-stripe-and-advent-are-heating-up/",
    "domain": "大厂 AI 动态",
    "title": "Talks to sell PayPal to Stripe and Advent are heating up",
    "url": "https://techcrunch.com/2026/08/14/talks-to-sell-paypal-to-stripe-and-advent-are-heating-up/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T22:43:24+00:00",
    "summary": "PayPal is still reportedly negotiating a potential sale to Stripe and private equity firm Advent, as the fintech firm's new CEO attempts to turn the company around."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/14/self-driving-trucks-are-officially-testing-on-california-highways/",
    "domain": "大厂 AI 动态",
    "title": "Self-driving trucks are officially testing on California highways",
    "url": "https://techcrunch.com/2026/08/14/self-driving-trucks-are-officially-testing-on-california-highways/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T20:37:49+00:00",
    "summary": "Aurora Innovation and Kodiak AI, two companies developing self-driving trucks, have received permits from the California Department of Motor Vehicles."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/14/thrives-joshua-kushner-chides-silicon-valley-vcs-over-ai-euphoria/",
    "domain": "大厂 AI 动态",
    "title": "Thrive’s Joshua Kushner chides Silicon Valley VCs over AI euphoria",
    "url": "https://techcrunch.com/2026/08/14/thrives-joshua-kushner-chides-silicon-valley-vcs-over-ai-euphoria/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T19:33:00+00:00",
    "summary": "The AI opportunity is huge, but \"it would also be a grave error in our minds to let excitement weaken our investment discipline,\" Kushner warns in his first-ever investment letter."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/14/what-we-know-about-the-alleged-iranian-hacks-on-u-s-water-utilities/",
    "domain": "大厂 AI 动态",
    "title": "What we know about the alleged Iranian hacks on US water utilities",
    "url": "https://techcrunch.com/2026/08/14/what-we-know-about-the-alleged-iranian-hacks-on-u-s-water-utilities/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T19:04:32+00:00",
    "summary": "Over the last couple of weeks, hackers have targeted and broken into the systems of several water plants in the United States. Here’s what we know and don’t know about this wave of attacks allegedly c"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/14/read-it-later-app-pocket-is-shutting-down-here-are-the-best-alternatives/",
    "domain": "大厂 AI 动态",
    "title": "Read-it-later app Pocket shut down — here are the best alternatives",
    "url": "https://techcrunch.com/2026/08/14/read-it-later-app-pocket-is-shutting-down-here-are-the-best-alternatives/",
    "source": "Ivan Mehta, Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T18:58:15+00:00",
    "summary": "Pocket users have until October 8, 2025, to export their saved articles and other items, including lists, archives, favorites, notes, and highlights."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/14/unforgetful-is-a-new-reminders-app-for-people-who-cant-stop-hitting-snooze/",
    "domain": "大厂 AI 动态",
    "title": "Unforgetful is a new reminders app for people who can’t stop hitting snooze",
    "url": "https://techcrunch.com/2026/08/14/unforgetful-is-a-new-reminders-app-for-people-who-cant-stop-hitting-snooze/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T16:21:04+00:00",
    "summary": "Unforgetful, the latest app from longtime indie developer Marco Arment, is designed to make reminders harder to ignore — or accidentally dismiss."
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
    "id": "hn:49311379",
    "domain": "股票",
    "title": "OpenAI talent exodus raises 'huge red flag' ahead of IPO",
    "url": "https://www.cnbc.com/2026/08/14/open-ai-ipo-red-flag.html",
    "source": "pseudolus",
    "platform": "hackernews",
    "points": 27,
    "published_at": "2026-08-15T15:25:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:49322233",
    "domain": "股票",
    "title": "AI is not just one bubble, strategist says – but a 'rolling sequence of bubbles'",
    "url": "https://fortune.com/2026/08/16/ai-bubble-sequence-saas-software-stocks-silver-prices-chipmakers/",
    "source": "pessimizer",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-08-16T18:05:39+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3779438",
    "domain": "股票",
    "title": "干预退潮、加息接棒：为什么日央行提前进入加息快车道？",
    "url": "https://wallstreetcn.com/premium/articles/3779438?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T03:43:51+00:00",
    "summary": "美日干预效果退潮，加息接棒成稳汇率关键；日央行被迫加快加息，但财政约束限制空间，9月加息及指引决定日元能否趋势修复。"
  },
  {
    "id": "wscn:3779575",
    "domain": "股票",
    "title": "关税预期驱动铜流向美国，铜价七周连涨剑指历史纪录，LME现货升水创2021年以来最大",
    "url": "https://wallstreetcn.com/articles/3779575",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T03:33:47+00:00",
    "summary": "受特朗普关税预期驱动，大量铜金属抢先涌入美国，全球供应随之骤紧。LME铜现货升水一度飙至每吨478美元，创2021年逼仓行情以来最大差值；库存跌至今年2月最低。三个月期铜现报14368美元，年内累涨逾15%，连涨七周，距历史高点仅一步之遥。"
  },
  {
    "id": "wscn:3779574",
    "domain": "股票",
    "title": "每日400万桶！战火下的能源生命线：中东产油国借\"暗航\"稳住全球油价",
    "url": "https://wallstreetcn.com/articles/3779574",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T03:21:54+00:00",
    "summary": "美伊冲突持续数月，中东产油国却以一套\"暗航\"转运体系悄然突破封锁——关闭应答器穿越霍尔木兹海峡、在阿曼湾完成货物转移，实际日均运量远超市场估计的400万桶。这套隐秘供应链叠加管道替代、战略库存释放与需求下滑，将布伦特原油压制在每桶80至90美元。"
  },
  {
    "id": "wscn:3779573",
    "domain": "股票",
    "title": "办公Agent的聚合路线“四国杀”正式打响",
    "url": "https://wallstreetcn.com/articles/3779573",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T02:59:17+00:00",
    "summary": "纷争开始"
  },
  {
    "id": "wscn:3779570",
    "domain": "股票",
    "title": "日本Q2 GDP年化增速1.1%，大幅低于预期2%，中东冲突拖累资本开支",
    "url": "https://wallstreetcn.com/articles/3779570",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T02:52:31+00:00",
    "summary": "日本二季度GDP年化增速仅1.1%，远逊预期2%，资本开支意外环比下滑1.2%，私人消费原地踏步，内需全面哑火，美伊冲突引发的能源涨价与供应链中断成最大拖累。出口独撑局面，但在一定程度上得益于日元偏弱，经济降速令日本央行加息路径愈发两难。"
  },
  {
    "id": "wscn:3779566",
    "domain": "股票",
    "title": "华尔街投行看好茅台转型：转向“爱马仕模式”，目标价2100元",
    "url": "https://wallstreetcn.com/articles/3779566",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T02:51:59+00:00",
    "summary": "杰富瑞认为，贵州茅台正加速向奢侈品运营模式转型，管理层主动收缩供给、稳定渠道价格，其逻辑越来越像爱马仕。与此同时，“茅台银行”贷款规模同比缩减约80%，资本正向股东回报集中。管理层从产量导向转向市场导向，主动维护稀缺性与定价权。"
  },
  {
    "id": "wscn:3779571",
    "domain": "股票",
    "title": "摩根大通：GLM-5.3升级+DeepSeek提价重塑中国AI，上调智谱与MiniMax目标价",
    "url": "https://wallstreetcn.com/articles/3779571",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T02:50:01+00:00",
    "summary": "摩根大通的核心逻辑是：GLM-5.3通过强化后训练实现内生能力跃升，护城河更稳固；DeepSeek API提价为MiniMax提供喘息空间，但其核心竞争力仍待M3.1验证。其更看好能力端，认为拥有\"前沿智能\"定价权的模型比单纯低价模型更具投资价值。"
  },
  {
    "id": "wscn:3779568",
    "domain": "股票",
    "title": "A股三大股指集体上涨，长鑫大涨8%市值逼近4万亿，贵州茅台跌近4%，恒科指涨2%，存储芯片爆发",
    "url": "https://wallstreetcn.com/articles/3779568",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T02:47:06+00:00",
    "summary": "半导体产业链震荡上扬，有研新材涨停，芯朋微涨超10%，普冉股份、中科飞测、长鑫科技涨超7%。玻璃基板概念震荡拉升，沃格光电涨停，红星发展、艾森股份、彩虹股份、力诺药包、京东方A、凯盛科技跟涨。早盘PCB概念延续上周强势，华正新材涨停，金禄电子、博敏电子、山东玻纤、宏昌电子、中国巨石等跟涨。"
  },
  {
    "id": "wscn:3779563",
    "domain": "股票",
    "title": "BTIG警告：8至10月美股系统性回调风险上升，此刻是削减风险敞口最佳时机",
    "url": "https://wallstreetcn.com/articles/3779563",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T02:45:17+00:00",
    "summary": "美股高位、波动率极低、投资者自满情绪爆棚——BTIG首席技术策略师在此刻拉响警报。自1990年以来，标普500在中期选举年8月至10月几乎无一幸免，每次至少回调7%。当前RSP与200日均线偏离达11%，VIX处于年内低点，看跌保护需求近乎归零，长端利率更逆势走高发出背离信号，“时钟正在滴答作响”。"
  },
  {
    "id": "wscn:3779550",
    "domain": "股票",
    "title": "摩根大通预警的不是2027年的粮食危机 而是“全球断裂”",
    "url": "https://wallstreetcn.com/premium/articles/3779550?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T02:40:30+00:00",
    "summary": "2027年粮荒的引信。"
  },
  {
    "id": "wscn:3779569",
    "domain": "股票",
    "title": "全球糖价升至年内高点：强厄尔尼诺概率升至81%，印度禁糖出口至9月底",
    "url": "https://wallstreetcn.com/articles/3779569",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T02:40:19+00:00",
    "summary": "厄尔尼诺持续增强，极强事件概率超90%——全球糖市警报拉响。原糖期货触及逾一年高点17.11美分/磅，巴西收割受扰、印泰季风受损、乌克兰甜菜产量骤降23%，多重供应压力叠加，气候风险溢价料持续推高糖价。"
  },
  {
    "id": "wscn:3779556",
    "domain": "股票",
    "title": "通胀顽固、财政扩张、AI热潮三重夹击，全球债券避险光环褪色",
    "url": "https://wallstreetcn.com/articles/3779556",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T02:04:37+00:00",
    "summary": "全球债券市场正经历一场结构性颠覆。通胀顽固、财政扩张与AI投资热潮三重压力叠加，驱动32个掉期市场三分之二计入加息预期，未来一年七大主要市场合计预期加息近400基点。韩国国债年内跌近9%，美债长端收益率创数十年新高——当各国央行被迫同步收紧，债券的避险神话正在瓦解。"
  },
  {
    "id": "wscn:3779564",
    "domain": "股票",
    "title": "芯片厂二季报里的信号：需求比三个月前更强，价格上行开始“扩散”",
    "url": "https://wallstreetcn.com/articles/3779564",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T02:01:17+00:00",
    "summary": "摩根大通认为，全球半导体二季报释放明确看多信号：一是需求超预期，台积电等晶圆巨头全面上调资本支出加速扩产；二是涨价效应正向设备和材料端实质性“扩散”，设备商借提价推升毛利率；三是存储巨头通过长期协议与巨额预付款，提前锁定未来数年的极高利润底线。"
  },
  {
    "id": "wscn:3779154",
    "domain": "股票",
    "title": "医药行业的三重共振：资金转向、业绩反转和AI重构，谁在买入？在买什么？",
    "url": "https://wallstreetcn.com/premium/articles/3779154?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T01:55:15+00:00",
    "summary": "AI对制药研发底座的重构——这可能是医药行业未来十年最大的结构性阿尔法。"
  },
  {
    "id": "wscn:3779562",
    "domain": "股票",
    "title": "资本关键时刻来临？AI叙事从技术转向融资，巨头现金流告急、债市已拉响警报",
    "url": "https://wallstreetcn.com/articles/3779562",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T01:37:22+00:00",
    "summary": "桥水警告“资本关键时刻”来临。大摩预测，2028年前约1.75万亿美元AI建设资金的筹集将来自信贷市场。然而风险已现：甲骨文CDS飙至180基点，自由现金流逼近-400亿美元。“新债王”Gundlach直言，用GPU抵押发行长期债券，无异于“用香蕉做30年ABS”。"
  },
  {
    "id": "wscn:3779561",
    "domain": "股票",
    "title": "高盛：美联储9月不会加息，市场定价仍偏鹰",
    "url": "https://wallstreetcn.com/articles/3779561",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T01:14:13+00:00",
    "summary": "高盛首席经济学家Jan Hatzius最新判断：9月美联储加息\"已极不可能\"。消费降温、就业趋势接近停滞、通胀持续改善三线共振，正从根本上瓦解加息理由。市场利率定价仍偏鹰，向下调整空间犹存。高盛维持收益率曲线变陡、美股年底前续创新高判断。欧洲方面，欧央行9月或加息25基点，但下一步更可能会降息。"
  },
  {
    "id": "wscn:3779560",
    "domain": "股票",
    "title": "美债逼近40万亿，美银Hartnett：做多黄金是当下最优解",
    "url": "https://wallstreetcn.com/articles/3779560",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T00:51:28+00:00",
    "summary": "美国国债逼近40万亿美元关口，美银Hartnett认为“做多黄金”是当前最优解——黄金是对抗美元贬值、债券崩溃与政治风险的最佳对冲。与此同时，AI融资狂潮推动企业债供给同比激增61%，正结构性挤出国债买家，债务利息支出已达1.4万亿美元。Hartnett警告，11月选举结果将是决定年底市场走向的最大变量。"
  },
  {
    "id": "wscn:3779423",
    "domain": "股票",
    "title": "从660kW到4.8MW：英伟达800V白皮书打开了多大的AI电力新市场？",
    "url": "https://wallstreetcn.com/premium/articles/3779423?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T00:41:03+00:00",
    "summary": "英伟达最新800VDC白皮书将AI数据中心供电从技术讨论推进到工程执行阶段：2026年三季度Power Rack率先进入生产，随后向2MW级Power Center和4.8MW级Power Block扩展。随着AI机柜功率持续提升，供电系统正成为制约算力密度的重要基础设施，高功率PSU、HVDC、直流保护、液冷、储能与SST等环节的价值量随之上升。800V产业链将如何沿着机架、集群和数据大厅逐级兑"
  },
  {
    "id": "wscn:3779558",
    "domain": "股票",
    "title": "\"有钱也买不到\"！供需失衡加剧，磷化铟掀史上最大涨价潮",
    "url": "https://wallstreetcn.com/articles/3779558",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T00:39:49+00:00",
    "summary": "AI算力需求爆发推动磷化铟（InP）基板与外延片严重供不应求，第四季度价格涨幅将超10%，创历史最大单次涨幅，且已历经多轮连续调涨。上游基板产能瓶颈难以快速突破，供需失衡短期难解。供应商直言，即便愿意加价，货源也未必能够到手。"
  },
  {
    "id": "wscn:3779554",
    "domain": "股票",
    "title": "特斯拉Roadster或本月亮相：搭载SpaceX推进器，能“飞行”的超级跑车",
    "url": "https://wallstreetcn.com/articles/3779554",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T00:23:42+00:00",
    "summary": "等了近十年，特斯拉新一代Roadster汽车最快本月或将亮相。它搭载源自火箭技术的冷气推进器，将能“飞行”。发布现场将上演无人驾驶特技表演，演示地点设在SpaceX德克萨斯测试基地。马斯克亲口警告“可能出差错，但无论如何都会很精彩”，限量版售价或高达数百万美元。"
  },
  {
    "id": "hn:49151871",
    "domain": "股票",
    "title": "Situational Awareness and the Impending Stock Market Volatility",
    "url": "https://www.emergingtrajectories.com/lh/situational-awareness-bigger-picture/",
    "source": "cl42",
    "platform": "hackernews",
    "points": 72,
    "published_at": "2026-08-03T06:17:53+00:00",
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
    "id": "hn:48958985",
    "domain": "股票",
    "title": "Traders are increasingly betting against SpaceX just weeks after IPO",
    "url": "https://www.ft.com/content/2b96703d-440b-46db-8d86-9fff9ecc59d5",
    "source": "ethanhawksley",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-07-18T15:26:13+00:00",
    "summary": ""
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
    "id": "hn:48984021",
    "domain": "股票",
    "title": "Mark Cuban: fight inequality by giving all workers company stock",
    "url": "https://fortune.com/2026/07/20/mark-cuban-income-inequality-company-stock-spacex-ipo-cost-plus-drugs/",
    "source": "01-_-",
    "platform": "hackernews",
    "points": 46,
    "published_at": "2026-07-20T19:52:49+00:00",
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
    "id": "hn:49162737",
    "domain": "股票",
    "title": "Palantir soars 12% on blowout quarter, with US commercial revenue soaring ~150%",
    "url": "https://www.cnbc.com/2026/08/03/palantir-pltr-earnings-q2-2026.html",
    "source": "gslin",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-08-03T23:36:32+00:00",
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
    "points": 142,
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
    "id": "hn:49174369",
    "domain": "金融",
    "title": "Waymo CEO explains why Tesla’s camera-only self-driving falls short",
    "url": "https://electrek.co/2026/08/04/waymo-co-ceo-camera-only-self-driving-tesla/",
    "source": "theanonymousone",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-08-04T20:11:15+00:00",
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
    "id": "hn:49190429",
    "domain": "金融",
    "title": "Data shows just how hard Tesla's Cybertruck has flopped",
    "url": "https://www.msn.com/en-us/autos/general/this-data-shows-just-how-hard-tesla-s-cybertruck-has-actually-flopped/ar-AA29sikQ",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-08-05T23:25:10+00:00",
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
    "id": "hn:48986112",
    "domain": "金融",
    "title": "The Fedora project grapples with change",
    "url": "https://lwn.net/SubscriberLink/1081557/cde56e450fe4bf10/",
    "source": "chmaynard",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-07-20T23:17:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:49114620",
    "domain": "金融",
    "title": "'Talk Is Cheap': Wall Street Delivers Harsh Verdict on Warsh Fed",
    "url": "https://www.bloomberg.com/news/articles/2026-07-30/-talk-is-cheap-wall-street-delivers-harsh-verdict-on-warsh-fed",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-07-30T19:33:17+00:00",
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
  },
  {
    "id": "hn:48986211",
    "domain": "金融",
    "title": "Delayed Boeing jets only fit for baked bean tins, Emirates boss says",
    "url": "https://finance.yahoo.com/technology/articles/delayed-boeing-jets-only-fit-162341761.html",
    "source": "devonnull",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-07-20T23:29:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:49033778",
    "domain": "金融",
    "title": "Reality Bites Elon Musk and His Tesla, SpaceX Believers",
    "url": "https://www.wsj.com/finance/stocks/reality-bites-elon-musk-and-his-tesla-spacex-believers-1b639591",
    "source": "doener",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-07-24T10:59:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:49100970",
    "domain": "金融",
    "title": "Trump administration Is Repurposing Federal Land for A.I. Data Centers",
    "url": "https://www.nytimes.com/2026/07/29/climate/trump-federal-data-centers.html",
    "source": "cdrnsf",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-07-29T18:09:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:49028304",
    "domain": "金融",
    "title": "US announces double-digit tariffs on most of globe to replace expiring duties",
    "url": "https://finance.yahoo.com/economy/policy/article/trump-administration-announces-the-next-phase-of-global-tariffs-with-10-to-125-rates-on-much-of-the-globe-210032314.html",
    "source": "ck2",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-07-23T21:28:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:49047488",
    "domain": "金融",
    "title": "Stripe in talks to acquire OpenRouter in potential $10B deal, WSJ reports",
    "url": "https://finance.yahoo.com/technology/ai/articles/stripe-talks-acquire-openrouter-potential-215104525.html",
    "source": "nlpnerd",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-07-25T13:38:45+00:00",
    "summary": ""
  }
]
```
