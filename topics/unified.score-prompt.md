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

- 今日日期：`2026-11-20`
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
  "date": "2026-11-20",
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
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "8分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 2139309,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 1560455,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 1507093,
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
    "points": 1480881,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 906426,
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
    "points": 759054,
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
    "points": 597254,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV13YRjBTEPb",
    "domain": "AI",
    "title": "Hermes Agent零基础、保姆级教程，小白也能轻松玩转",
    "url": "http://www.bilibili.com/video/av116503638706867",
    "source": "iwenwiki",
    "platform": "bilibili",
    "points": 436326,
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
    "points": 433957,
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
    "points": 428581,
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
    "points": 363005,
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
    "points": 358864,
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
    "points": 330564,
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
    "points": 302401,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 237755,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1h3W76wEem",
    "domain": "AI",
    "title": "Claude(Code)桌面APP，保姆级全攻略，一期视频精通，顶级Agent软件长什么样？",
    "url": "http://www.bilibili.com/video/av117580048108571",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 226689,
    "published_at": "2026-11-08T09:14:07+00:00",
    "summary": "最近Claude桌面端（Claude Desktop） 有了一大波功能更新。随着一步步的迭代，它已经把 Claude Code 的编程、Claude Design 的设计，以及 Claude Cowork 的办公等核心能力，全部收入了同一个桌面客户端，特别是Claude Code已经从原本黑乎乎的命令行工具，进化成了桌面客户端的完全体形态。再搭配上超强的Opus5.5 模型，已经能称得上是地表顶级"
  },
  {
    "id": "bvid:BV1468g6DEWs",
    "domain": "AI",
    "title": "【全100集】(允许白嫖) 2026最全最细的AI教程零基础入门到精通，一周带你小白变大神！全程干货无废话！存下吧，少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av117115386404821",
    "source": "AI产品经理入门教程-",
    "platform": "bilibili",
    "points": 219236,
    "published_at": "2026-08-18T13:11:45+00:00",
    "summary": "【2026最新版AI教程零基础入门到精通｜配套学习路线+工具包+实战项目，看置顶评论自取】\n 本套教程专为零基础设计，从AI是什么到独立用AI解决实际问题，手把手带你系统走完从入门到精通的完整路径。 ✅ AI认知入门：什么是AI/大模型、它们能做什么不能做什么、别被营销话术忽悠\n✅ 核心技能掌握：提示词工程、多轮对话技巧、让AI稳定输出的方法论\n✅ 进阶能力突破：AI工作流搭建、智能体开发、多工具"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 187377,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1sZMq6qEko",
    "domain": "AI",
    "title": "从0做出你的第一个App ｜ 零基础AI编程保姆教程",
    "url": "http://www.bilibili.com/video/av117038647352026",
    "source": "木子不写代码",
    "platform": "bilibili",
    "points": 183672,
    "published_at": "2026-08-07T12:15:00+00:00",
    "summary": "这期视频，我会手把手带你，用 AI 做出你的第一个 App。\n全程假设你没有任何编程和AI的基础，\n我们从如何写需求提示词开始，\n到确定页面结构和设计，\n产品需求文档，\n开发计划，\n第一版APP验收，\ngit代码存档，\n二次开发，\n界面美化，\n做好的APP也会开源给到大家，\n我也会演示如何获取这个项目源代码并且用AI继续定制开发，\n视频到最后，\n你会收获一个为自己的工作和生活定制的专属APP！\n和"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 166501,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV1b5AeeGEFc",
    "domain": "AI",
    "title": "Cursor太贵？分享三个免费AI编程方案+海量编程技巧【如何看待AI编程】",
    "url": "http://www.bilibili.com/video/av114025056699722",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 162152,
    "published_at": "2025-02-18T13:13:51+00:00",
    "summary": "我试用了几十种AI编程辅助工具，找到了其中三个免费，并且效果最好的方案。 本期视频就来跟大家分享一下。视频中间会穿插很多AI编程工具的使用技巧，还有看待AI编程的一些个人思考。本期视频没有广告都是个人的经验干货，废话不多说我们直接开始。"
  },
  {
    "id": "bvid:BV1qJs16WEJj",
    "domain": "AI",
    "title": "今天体验的人生副本是:沉迷vibe coding走火入魔的AI嘉豪",
    "url": "http://www.bilibili.com/video/av117635899524333",
    "source": "vibe睦头人",
    "platform": "bilibili",
    "points": 148736,
    "published_at": "2026-11-18T06:01:48+00:00",
    "summary": "ai生成，仅供娱乐，如有雷同，纯属巧合（（"
  },
  {
    "id": "bvid:BV1VL3F6pE9K",
    "domain": "AI",
    "title": "0基础入门智能体agent测试：AI测试基础+AI智能体(Agent)测试从零入门全攻略，2026最新版！",
    "url": "http://www.bilibili.com/video/av116991151113881",
    "source": "黑马测试",
    "platform": "bilibili",
    "points": 117610,
    "published_at": "2026-07-27T09:19:37+00:00",
    "summary": "还在卷传统软件测试？2026年必学的AI智能体(Agent)测试来了！本期视频专为0基础小白打造，从软件测试基础讲起...若要本视频配套资源笔记可加up主企微（请看置顶留言最后一句话）。"
  },
  {
    "id": "bvid:BV1kGo6BdEsT",
    "domain": "AI",
    "title": "如何用Claude Skill 做高质量 PPT（附完整教程）",
    "url": "http://www.bilibili.com/video/av116474832361424",
    "source": "阿西_出海",
    "platform": "bilibili",
    "points": 104927,
    "published_at": "2026-04-27T04:45:20+00:00",
    "summary": "很多人问我上期爆了的那条视频里，那个 PPT 是怎么做的。\n其实我是用 Anthropic 最近出的 Claude Design 做的，这个功能一发出来就在全网传疯了，一条推文就冲上了 6000 多万曝光。\n本期视频我会带你手把手从 0 到 1 把这个Skill 装好，然后一起跑一个成品效果出来。"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 94376,
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
    "points": 90787,
    "published_at": "2026-07-26T01:30:00+00:00",
    "summary": "模组：Numen\n项目地址：https://github.com/Dwinovo/minecraft-numen"
  },
  {
    "id": "bvid:BV1woHQ6kEtv",
    "domain": "AI",
    "title": "【2026最新版】Workbuddy财务自动化办公实战教程，搭建数字员工，能够秒做账、报税、报销、出报表、做财务分析、编制预算、处理合并报表",
    "url": "http://www.bilibili.com/video/av117404038466491",
    "source": "Max极客菌",
    "platform": "bilibili",
    "points": 86973,
    "published_at": "2026-10-08T07:22:21+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1cVW86JE2e",
    "domain": "AI",
    "title": "Vibe Coding 完不会获客？我用 AI 做了一个「营销数据库」！【B站AI创造公开赛】",
    "url": "http://www.bilibili.com/video/av117587245599812",
    "source": "熠辉IndieDev",
    "platform": "bilibili",
    "points": 76247,
    "published_at": "2026-11-10T01:00:00+00:00",
    "summary": "产品做出来了，第一批用户去哪找？我用两个月做了 BizPeel，收录700多个公开营收的产品，拆解真实获客动作。本期演示在 Google Antigravity 接入 BizPeel MCP，由 Gemini 4 Argon 查找同类产品、整理增长实验；报告生成时用 Gemini Flash 清洗数据，再由 Gemini 4 Argon 撰写。\n\n注： 部分Google技术仅适用于出海场景。"
  },
  {
    "id": "bvid:BV19wXvBpEaL",
    "domain": "AI",
    "title": "认真用 Claude Code 的人，迟早会遇见 Everything Claude Code",
    "url": "http://www.bilibili.com/video/av116319122885806",
    "source": "极客魔导师",
    "platform": "bilibili",
    "points": 64155,
    "published_at": "2026-03-30T16:47:51+00:00",
    "summary": "Everything Claude Code 是目前 GitHub 上 116K star 的 Claude Code 配置项目。本期从斜杠命令、子代理、Hooks 到学习系统，带你把这个项目真正用起来。"
  },
  {
    "id": "bvid:BV17Lap6VEUr",
    "domain": "AI",
    "title": "【全80集】Vibe Coding 零基础入门到实战教程，由浅入深（全程干货）",
    "url": "http://www.bilibili.com/video/av117353572468721",
    "source": "数据拾光屋",
    "platform": "bilibili",
    "points": 61970,
    "published_at": "2026-10-02T09:25:00+00:00",
    "summary": "本套教程专门为零基础学员而制，全程干货无废话，喜欢的小伙伴记得点赞三连喔 ~"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 50648,
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
    "points": 47841,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1uVSUBkEfZ",
    "domain": "AI",
    "title": "Microsoft Copilot完整教程(上) 从入门到Agent 一站式掌握AI办公",
    "url": "http://www.bilibili.com/video/av116351721084069",
    "source": "星小脉",
    "platform": "bilibili",
    "points": 47078,
    "published_at": "2026-04-05T11:00:20+00:00",
    "summary": "2026年最全面的Microsoft Copilot教程上半部分。从Copilot首页入门到Agent深度解析，涵盖搜索、资料库、AI视频生成、Copilot Pages、PowerPoint智能幻灯片等全部功能。由培训了6万人的AI顾问Cherie Brock与Sabrina Ramonov联合讲解。"
  },
  {
    "id": "bvid:BV1hmb26ZEws",
    "domain": "AI",
    "title": "DeepSeek Harness 实测  Claude Code 对比后，梁神我错了 差距比我想的大",
    "url": "http://www.bilibili.com/video/av117100337236191",
    "source": "程序员晓刘",
    "platform": "bilibili",
    "points": 41594,
    "published_at": "2026-08-15T16:01:38+00:00",
    "summary": "这期用同一个 DeepSeek Pro 0813 模型，分别在 Claude Code 和 DeepSeek Harness 里完成同样的任务，对比工具链对最终效果的影响。\n实测内容包括：\nFPS 游戏 Demo、灯塔预警沙盘、手枪组装动画、显示器组装动画，以及 DeepSeek Harness 的插件化源码流程。\n整体看下来，模型本身当然重要，但 Harness 在插件化、流程记录、缓存命中和任"
  },
  {
    "id": "bvid:BV1XiD5BQEAj",
    "domain": "AI",
    "title": "Claude Code 接入微信、一行命令把Claude Code装进微信、保姆级教程、微信支持Claude Code（cc-connect）远程开发",
    "url": "http://www.bilibili.com/video/av116350093694897",
    "source": "下班学AI",
    "platform": "bilibili",
    "points": 41528,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV1wpxq6VEXx",
    "domain": "AI",
    "title": "【AI时代的STM32教程】AI Agent 初体验",
    "url": "http://www.bilibili.com/video/av117529699682124",
    "source": "keysking",
    "platform": "bilibili",
    "points": 40880,
    "published_at": "2026-10-30T11:52:06+00:00",
    "summary": "一句话，让 AI 帮我们完成第一个 STM32C5 程序！🚀\n本期我们一起认识 AI Agent，学习如何描述开发需求，并借助开源的 STM32C5DevSkills，让 AI 完成工程创建、芯片配置、代码编写和编译烧录，让律动小板上的小灯闪烁起来！\n也特别感谢 @意法半导体中国   对本系列教程的支持～下期我们再亲手走一遍开发流程，把 Agent 替我们完成的工作，一步步搞明白！"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 34720,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1sQaL6vEkb",
    "domain": "AI",
    "title": "小白向，ai入门第一课：agent的部署和使用！",
    "url": "http://www.bilibili.com/video/av117349378166797",
    "source": "沈三殊",
    "platform": "bilibili",
    "points": 34383,
    "published_at": "2026-09-28T15:30:36+00:00",
    "summary": "详细的agent部署介绍：https://pan.quark.cn/s/3846914c6da7\n欢迎来到ai的世界！！\n有疑问欢迎私信。"
  },
  {
    "id": "bvid:BV1uwxG6DEra",
    "domain": "AI",
    "title": "3分钟讲透：Vibe Coding如何避免💩屎山代码",
    "url": "http://www.bilibili.com/video/av117513727838880",
    "source": "鲤哥builder",
    "platform": "bilibili",
    "points": 31587,
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
    "points": 31296,
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
    "points": 29988,
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
    "points": 29074,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 27059,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1spTy6DEb4",
    "domain": "AI",
    "title": "Claude code接管科研全流程：cc-kaiti 带你从 0 走到开题报告和答辩 PPT",
    "url": "http://www.bilibili.com/video/av116866278233889",
    "source": "做科研的大师兄",
    "platform": "bilibili",
    "points": 26144,
    "published_at": "2026-07-05T07:53:28+00:00",
    "summary": "十二年科研经验加持的课题开题Skill，从零开始到拿到一份完整的开题报告及开题PPT，仅需一天！\n\n本次视频分享的cc-kaiti这个skill文件及配套的资料包，在后台私我“cc开题”获取~"
  },
  {
    "id": "bvid:BV1yyQEBdEkm",
    "domain": "AI",
    "title": "【2026B站最全】Claude Code+软件测试实操教程!看完我直接删了收藏夹所有测试教程,从账号注册到Plan驱动测试项目,小白3天上手！",
    "url": "http://www.bilibili.com/video/av116408092525631",
    "source": "软件测试大神",
    "platform": "bilibili",
    "points": 15629,
    "published_at": "2026-04-15T09:55:02+00:00",
    "summary": "配套资料👉：https://b23.tv/qvhxmaQ\n包括:AI测试网站，几十个AI场景测试完整流程，skil文档，测试八股文，项目源码，测试用例模板，工具安装包，学习计划表，学习路线，100g测试新人资料包等等，资料百分百免费，放心领取~"
  },
  {
    "id": "bvid:BV11aYs6PE2p",
    "domain": "AI",
    "title": "AI Agent接入Photoshop：MCP 实现自然语言修图",
    "url": "http://www.bilibili.com/video/av117239051323475",
    "source": "W不懂跨境",
    "platform": "bilibili",
    "points": 14462,
    "published_at": "2026-09-09T03:54:24+00:00",
    "summary": "本期教程介绍 Photoshop MCP 的安装与配置，并演示如何将 AI Agent 接入 Photoshop，通过 MCP 调用 Photoshop 工具，实现自然语言控制与自动修图。\n\n最大的特点，也是大家都关心的问题：\n1、整个过程不需要Adobe Developer 账号。\n2、不需要购买额外的 AI 服务。\n3、不要求 Photoshop 必须为正版\n4、支持所有的 Photoshop"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 14225,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
  },
  {
    "id": "bvid:BV1wFpP6uE1s",
    "domain": "AI",
    "title": "【开源】让手机自己操作 App！手上的 ai Agent！GitHub开源安卓App推荐",
    "url": "http://www.bilibili.com/video/av117394643097499",
    "source": "补药满减哇",
    "platform": "bilibili",
    "points": 13722,
    "published_at": "2026-10-07T01:05:00+00:00",
    "summary": "开源安卓 AI Agent：RikkaHub Agent Pure\n它能「看懂」屏幕、自己操作各种 App，也能组队干活。\n\n⬇️ 下载 &amp; 源码（AGPL-3.0）\nhttps://github.com/wuyhong715/rikkahub-agent-pure\n\n▶ 本片讲两件事\n① 无障碍屏幕自动化：读控件树定位、实时决策，不是死坐标脚本\n② 专家团系统：每个专家有自己的模型/工具"
  },
  {
    "id": "bvid:BV1EEM96uEPP",
    "domain": "AI",
    "title": "【逆向】掌握MCP功能使用修改分析，成为逆向高手！",
    "url": "http://www.bilibili.com/video/av117030460131623",
    "source": "009安乐",
    "platform": "bilibili",
    "points": 13721,
    "published_at": "2026-08-03T07:47:28+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1tDnV6ME79",
    "domain": "AI",
    "title": "当我把claude code搬进安卓设备……",
    "url": "http://www.bilibili.com/video/av117462439826705",
    "source": "Grey-Oak",
    "platform": "bilibili",
    "points": 13233,
    "published_at": "2026-10-18T14:44:02+00:00",
    "summary": "cccodroid 是一个开源的安卓应用，把 Claude Code 装进你的安卓设备。不用 root，不刷机，也不套 Linux 虚拟环境，工具直接在安卓上原生运行。\n\n视频全程实机录屏（联想y700二代平板，骁龙 8+），没有连电脑：\n· 一句话让它改代码，先给计划，你点批准才动手\n· 终端里 pkg install rust，现场打包 APK 装上\n· docx / xlsx / pptx "
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
    "points": 1114,
    "published_at": "2026-11-14T02:52:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:50418016",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia CEO Jensen Huang's letter to staff about affair",
    "url": "https://nvidianews.nvidia.com/news/a-message-to-our-company",
    "source": "karimf",
    "platform": "hackernews",
    "points": 988,
    "published_at": "2026-11-08T22:20:09+00:00",
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
    "points": 665,
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
    "points": 485,
    "published_at": "2026-11-15T23:55:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:50416801",
    "domain": "AI 算力 / 半导体",
    "title": "Statement from Nvidia board of directors",
    "url": "https://nvidianews.nvidia.com/news/statement-from-nvidia-board-of-directors",
    "source": "vincentchau",
    "platform": "hackernews",
    "points": 495,
    "published_at": "2026-11-08T20:26:43+00:00",
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
    "id": "hn:50518567",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia was in trouble before the Jensen Huang mess",
    "url": "https://www.wired.com/story/nvidia-was-already-in-trouble-before-the-jensen-huang-mess/",
    "source": "Brajeshwar",
    "platform": "hackernews",
    "points": 289,
    "published_at": "2026-11-16T15:24:09+00:00",
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
    "id": "hn:50511982",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang might return to Nvidia as CEO",
    "url": "https://www.reuters.com/world/china/jensen-huang-discusses-comeback-nvidia-ceo-with-allies-ft-reports-2026-11-15/",
    "source": "YakubYilmaz",
    "platform": "hackernews",
    "points": 177,
    "published_at": "2026-11-15T23:24:53+00:00",
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
    "id": "hn:50497155",
    "domain": "AI 算力 / 半导体",
    "title": "Serving GLM-5.3 at 607.8 tok/s across two Nvidia DGX stations with vLLM",
    "url": "https://developer.nvidia.com/blog/when-one-gpu-isnt-enough-serving-glm-5-3-across-two-nvidia-dgx-stations-with-vllm/",
    "source": "wondersky",
    "platform": "hackernews",
    "points": 149,
    "published_at": "2026-11-14T14:09:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:50509883",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang discusses comeback as Nvidia CEO with allies",
    "url": "https://www.ft.com/content/45383d86-33c4-4d99-86e5-5e058d3567c1",
    "source": "eyalitki",
    "platform": "hackernews",
    "points": 135,
    "published_at": "2026-11-15T19:31:11+00:00",
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
    "id": "hn:50546253",
    "domain": "AI 算力 / 半导体",
    "title": "Dutch resist 'unacceptable' US bid to tighten semiconductor export controls",
    "url": "https://www.politico.eu/article/dutch-resist-unacceptable-us-bid-to-tighten-semiconductor-export-controls-asml/",
    "source": "sergdigon",
    "platform": "hackernews",
    "points": 38,
    "published_at": "2026-11-18T13:46:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:50557420",
    "domain": "AI 算力 / 半导体",
    "title": "Wife of Senior Nvidia Executive Caught Up in Alleged AI Chip Smuggling Scandal",
    "url": "https://www.gadgetreview.com/wife-of-senior-nvidia-executive-caught-up-in-alleged-ai-chip-smuggling-scandal",
    "source": "mgh2",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-11-19T08:23:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:50538942",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Chair Harvey Jones says board doesn't intend to reinstate Huang as CEO",
    "url": "https://www.cnbc.com/2026/11/17/nvidia-nvda-earnings-report-q3-2027.html",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-11-17T22:08:34+00:00",
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
    "id": "hn:50467191",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia CEO Jensen Huang resigns after reports of extramarital relationships",
    "url": "https://www.nbcnews.com/tech/tech-news/nvidia-ceo-jensen-huang-resigns-reports-extramarital-relationships-rcna608402",
    "source": "sonabinu",
    "platform": "hackernews",
    "points": 72,
    "published_at": "2026-11-12T14:00:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:50520867",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia board not considering reinstating Jensen Huang as chief executive",
    "url": "https://www.ft.com/content/e5275763-d7e2-4857-8ac6-6b888111986a",
    "source": "doener",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-11-16T18:17:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:50486489",
    "domain": "AI 算力 / 半导体",
    "title": "Arm boss Rene Haas approached in Nvidia CEO search",
    "url": "https://www.ft.com/content/2a64f698-46dd-4178-a3f4-4c5f4c0a0926",
    "source": "bazzmt",
    "platform": "hackernews",
    "points": 66,
    "published_at": "2026-11-13T17:10:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:50392256",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia was in 1 in 11 startup rounds over $100M last year",
    "url": "https://datahyena.com/research/a-chipmaker-was-in-one-of-every-eleven-100m-rounds/",
    "source": "ghostfoxgod",
    "platform": "hackernews",
    "points": 82,
    "published_at": "2026-11-06T13:48:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:50521575",
    "domain": "AI 算力 / 半导体",
    "title": "U.S. tightens controls on remote access to AI technology amid Nvidia fallout",
    "url": "https://www.npr.org/2026/11/16/nx-s1-6042883/nvidia-jensen-huang-commerce-department",
    "source": "jethronethro",
    "platform": "hackernews",
    "points": 31,
    "published_at": "2026-11-16T19:09:05+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/anthropic-ipo-and-the-b2d-strategy/",
    "domain": "AI 算力 / 半导体",
    "title": "Anthropic’s IPO and the B2D Strategy",
    "url": "https://www.eetimes.com/anthropic-ipo-and-the-b2d-strategy/",
    "source": "Moshe Zalcberg",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T09:43:53+00:00",
    "summary": "From Nvidia’s CUDA to Anthropic's Claude Code, developer adoption can drive enterprise sales, but hardware startups show how difficult conversion can be. The post Anthropic&#8217;s IPO and the B2D Str"
  },
  {
    "id": "rss:https://www.eetimes.com/geehy-launches-the-g32r502-1kw-fully-digital-bidirectional-energy-storage-inverter-solution/",
    "domain": "AI 算力 / 半导体",
    "title": "Geehy Launches G32R502 1kW Bidirectional Inverter Solution",
    "url": "https://www.eetimes.com/geehy-launches-the-g32r502-1kw-fully-digital-bidirectional-energy-storage-inverter-solution/",
    "source": "Geehy Semiconductor",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T07:00:00+00:00",
    "summary": "Explore Geehy’s G32R502 1kW bidirectional energy storage inverter reference design, featuring digital control, high efficiency, and UPS functionality. The post Geehy Launches G32R502 1kW Bidirectional"
  },
  {
    "id": "rss:https://www.eetimes.com/memory-rd-is-a-high-stakes-game/",
    "domain": "AI 算力 / 半导体",
    "title": "Memory R&D Is a High-Stakes Game",
    "url": "https://www.eetimes.com/memory-rd-is-a-high-stakes-game/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T22:21:15+00:00",
    "summary": "AI is driving memory makers’ research agenda, while partnerships help share the cost and risk of developing technologies beyond the next process node. The post Memory R&amp;D Is a High-Stakes Game app"
  },
  {
    "id": "rss:https://www.eetimes.com/gartner-warns-of-risks-behind-sovereign-tech-claims/",
    "domain": "AI 算力 / 半导体",
    "title": "Gartner Warns of Risks Behind Sovereign Tech Claims",
    "url": "https://www.eetimes.com/gartner-warns-of-risks-behind-sovereign-tech-claims/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T16:30:35+00:00",
    "summary": "Gartner research predicts that digital sovereignty will become a core component of national security strategies globally by 2030. The post Gartner Warns of Risks Behind Sovereign Tech Claims appeared "
  },
  {
    "id": "rss:https://www.eetimes.com/shaping-the-form-function-and-future-of-humanoid-robotics/",
    "domain": "AI 算力 / 半导体",
    "title": "Shaping the Form, Function, and Future of Humanoid Robotics",
    "url": "https://www.eetimes.com/shaping-the-form-function-and-future-of-humanoid-robotics/",
    "source": "Henkel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T14:32:48+00:00",
    "summary": "Humanoid robotics is moving rapidly from concept toward real-world applications, creating new engineering challenges across sensing, movement, assembly, reliability and long-term serviceability. As ro"
  },
  {
    "id": "rss:https://www.eetimes.com/nvidia-reports-115-8b-in-quarterly-revenue-under-interim-ceo/",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Reports $115.8B in Quarterly Revenue Under Interim CEO",
    "url": "https://www.eetimes.com/nvidia-reports-115-8b-in-quarterly-revenue-under-interim-ceo/",
    "source": "News Desk",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T10:26:18+00:00",
    "summary": "Strong AI infrastructure demand helped Nvidia revenue and profit as the company deals with leadership changes. The post Nvidia Reports $115.8B in Quarterly Revenue Under Interim CEO appeared first on "
  },
  {
    "id": "rss:https://www.eetimes.com/quantum-stocks-are-headed-for-a-correction-investor-charles-beyrouthy-says/",
    "domain": "AI 算力 / 半导体",
    "title": "Quantum Stocks Are Headed for a Correction, Investor Charles Beyrouthy Says",
    "url": "https://www.eetimes.com/quantum-stocks-are-headed-for-a-correction-investor-charles-beyrouthy-says/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T23:39:34+00:00",
    "summary": "Charles Beyrouthy warns quantum stocks face a correction as investors ignore revenue and tech differences; watch where he sees opportunity next. The post Quantum Stocks Are Headed for a Correction, In"
  },
  {
    "id": "rss:https://www.eetimes.com/beyond-one-turn-how-a-single-chip-multiturn-position-sensor-is-reshaping-actuator-design/",
    "domain": "AI 算力 / 半导体",
    "title": "Beyond One Turn: How a Single-Chip Multiturn Position Sensor Is Reshaping Actuator Design",
    "url": "https://www.eetimes.com/beyond-one-turn-how-a-single-chip-multiturn-position-sensor-is-reshaping-actuator-design/",
    "source": "Analog Devices",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T15:00:00+00:00",
    "summary": "Discover how advanced multiturn position sensing can transform industrial motion control without the limitations of traditional mechanical solutions. Explore how magnetic sensing technology enables ac"
  },
  {
    "id": "rss:https://www.eetimes.com/qnity-at-one-randy-king-on-shrink-stack-and-the-materials-behind-ai/",
    "domain": "AI 算力 / 半导体",
    "title": "Qnity at One: Randy King on Shrink, Stack and the Materials Behind AI",
    "url": "https://www.eetimes.com/qnity-at-one-randy-king-on-shrink-stack-and-the-materials-behind-ai/",
    "source": "Randal King, Senior Vice President and Chief Technology and Sustainability Officer, Qnity",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T14:00:00+00:00",
    "summary": "Qnity CTO Randy King on year one as an independent company, shrink-and-stack chips and the materials challenges of advanced packaging for AI. The post Qnity at One: Randy King on Shrink, Stack and the"
  },
  {
    "id": "rss:https://www.eetimes.com/koduri-oxmiq-offers-ip-tools-for-indian-teams-to-design-ai-chips/",
    "domain": "AI 算力 / 半导体",
    "title": "Koduri’s Oxmiq Offers IP, Tools for Indian Teams to Design AI Chips",
    "url": "https://www.eetimes.com/koduri-oxmiq-offers-ip-tools-for-indian-teams-to-design-ai-chips/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T13:30:00+00:00",
    "summary": "India's AI infrastructure needs could exceed 6 GW by 2030. Oxmiq Labs CEO Raja Koduri explains why domestic chip design and custom systems matter. The post Koduri’s Oxmiq Offers IP, Tools for Indian T"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/score-a-huge-49-percent-saving-on-a-2tb-samsung-9100-pro-ssd-while-you-can-now-17-5-cents-per-gb-ultra-fast-gen-5-drive-is-the-perfect-pc-storage-upgrade-down-to-usd349-99",
    "domain": "AI 算力 / 半导体",
    "title": "Score a huge 49% saving on a 2TB Samsung 9100 Pro SSD while you can",
    "url": "https://www.tomshardware.com/pc-components/ssds/score-a-huge-49-percent-saving-on-a-2tb-samsung-9100-pro-ssd-while-you-can-now-17-5-cents-per-gb-ultra-fast-gen-5-drive-is-the-perfect-pc-storage-upgrade-down-to-usd349-99",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T11:04:48+00:00",
    "summary": "A huge discount on Amazon has brought the Gen 5 2TB Samsung 9100 Pro down to $349.99, an almost half-price saving compared to its list price."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/redditor-puts-pc-into-checked-baggage-from-us-to-uk-flight-desktop-unit-miraculously-arrives-in-one-piece",
    "domain": "AI 算力 / 半导体",
    "title": "Redditor forced to bring desktop PC in checked luggage on US-to-UK flight with GPU still installed — GPU stayed installed and tempered glass didn't shatter",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/redditor-puts-pc-into-checked-baggage-from-us-to-uk-flight-desktop-unit-miraculously-arrives-in-one-piece",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T11:00:00+00:00",
    "summary": "A pissed traveler decided to check their desktop CPU after a check-in attendant refused to have it carried in the cabin, despite being historically allowed by the airline."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-helped-amd-improve-its-upcoming-flagship-gpu-design-by-14-percent-ppa-gpt-models-also-helping-lisa-sus-outfit-boost-its-new-cpus",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI helped AMD improve its upcoming flagship GPU design by 14% PPA — GPT models also helped Lisa Su's outfit boost its new CPUs",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-helped-amd-improve-its-upcoming-flagship-gpu-design-by-14-percent-ppa-gpt-models-also-helping-lisa-sus-outfit-boost-its-new-cpus",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T10:30:00+00:00",
    "summary": "OpenAI helped AMD improve its upcoming flagship GPU design by 14% PPA — GPT models also helping Lisa Su's outfit boost its new CPUs"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/robotics/autonomous-5-tonne-john-deere-skid-steer-loader-trained-to-perform-acrobatic-maneuvers-using-ai-researchers-discuss-reinforcement-learning-tech-in-a-paper-titled-heavy-metal-acrobatics",
    "domain": "AI 算力 / 半导体",
    "title": "Autonomous 5-ton John Deere skid-steer loader trained to perform acrobatic maneuvers using AI",
    "url": "https://www.tomshardware.com/tech-industry/robotics/autonomous-5-tonne-john-deere-skid-steer-loader-trained-to-perform-acrobatic-maneuvers-using-ai-researchers-discuss-reinforcement-learning-tech-in-a-paper-titled-heavy-metal-acrobatics",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T10:00:00+00:00",
    "summary": "Videos of an incredibly acrobatic, nimble, and graceful John Deere 332G 5-tonne skid-steer loader have been shared by a group of researchers from the U.S. and Switzerland."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/get-an-rtx-5070-for-just-usd839-99-a-rare-savings-in-the-gpu-wasteland-msi-geforce-rtx-5070-ventus-2x-oc-12-gb-is-currently-on-sale-at-newegg",
    "domain": "AI 算力 / 半导体",
    "title": "Get an RTX 5070 for just $839.99, a rare savings in the GPU wasteland",
    "url": "https://www.tomshardware.com/pc-components/get-an-rtx-5070-for-just-usd839-99-a-rare-savings-in-the-gpu-wasteland-msi-geforce-rtx-5070-ventus-2x-oc-12-gb-is-currently-on-sale-at-newegg",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T00:59:02+00:00",
    "summary": "Get an RTX 5070 for just $839.99 — MSI GeForce RTX 5070 Ventus 2X OC 12 GB is currently on sale at Newegg"
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/routers/score-tp-link-archer-with-full-wi-fi-7-support-and-10-gbps-wired-networking-for-incredible-55-percent-off-its-regular-price-be9500-router-is-now-just-usd89-99-a-steep-discount-from-the-regular-usd199-99-price",
    "domain": "AI 算力 / 半导体",
    "title": "Score TP-Link Archer with full Wi-Fi 7 support and 10 Gbps wired networking for incredible 55% off its regular price",
    "url": "https://www.tomshardware.com/networking/routers/score-tp-link-archer-with-full-wi-fi-7-support-and-10-gbps-wired-networking-for-incredible-55-percent-off-its-regular-price-be9500-router-is-now-just-usd89-99-a-steep-discount-from-the-regular-usd199-99-price",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T23:20:25+00:00",
    "summary": "Get TP-Link Archer BE9500 with full Wi-Fi 7 support and 10 Gbps WAN for just $89.99, or 55% off its regular $199.99 price"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/new-windows-11-lock-screen-zero-day-unlocks-bitlocker-protected-pcs-with-just-a-few-keystrokes-win-u-keyboard-trick-lets-physical-attackers-run-usb-payloads-or-create-new-admin-accounts",
    "domain": "AI 算力 / 半导体",
    "title": "New Windows 11 lock screen zero-day unlocks BitLocker-protected PCs with just a few keystrokes",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/new-windows-11-lock-screen-zero-day-unlocks-bitlocker-protected-pcs-with-just-a-few-keystrokes-win-u-keyboard-trick-lets-physical-attackers-run-usb-payloads-or-create-new-admin-accounts",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T21:30:00+00:00",
    "summary": "Windows 0-day lets attackers run software by partially bypass the lock screen with just some keystrokes — even BitLocker-protected machines are seemingly vulnerable"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/ai-data-center-power-demand-will-double-by-2030-thanks-to-usd4-trillion-in-spending-adding-an-entire-great-britain-to-energy-strain-93-large-ai-factories-with-projected-capacity-of-around-50-gigawatts",
    "domain": "AI 算力 / 半导体",
    "title": "AI data center power demand will double by 2030 thanks to $4 trillion in spending, adding an entire Great Britain to energy strain",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/ai-data-center-power-demand-will-double-by-2030-thanks-to-usd4-trillion-in-spending-adding-an-entire-great-britain-to-energy-strain-93-large-ai-factories-with-projected-capacity-of-around-50-gigawatts",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T21:00:00+00:00",
    "summary": "IEA's report says that power production and distribution is barely keeping up with the rapid growth of AI data centers."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-continues-layoffs-with-cuts-to-its-it-department-hundreds-of-employees-reportedly-affected-companys-workforce-reduced-by-27-800-under-lip-bu-tan",
    "domain": "AI 算力 / 半导体",
    "title": "Intel continues layoffs with cuts to its IT department, hundreds of employees reportedly affected",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-continues-layoffs-with-cuts-to-its-it-department-hundreds-of-employees-reportedly-affected-companys-workforce-reduced-by-27-800-under-lip-bu-tan",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T14:58:13+00:00",
    "summary": "Intel continues to reduce headcount, IT department affected this time."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/supermicro-sued-by-shareholders-over-claims-nvidia-executives-wife-must-have-known-about-illicit-china-sales-former-chief-growth-officer-cenly-chen-is-married-to-outgoing-nvidia-vp-jay-puri",
    "domain": "AI 算力 / 半导体",
    "title": "Supermicro sued by shareholders over claims Nvidia executive’s wife knew about illicit China sales",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/supermicro-sued-by-shareholders-over-claims-nvidia-executives-wife-must-have-known-about-illicit-china-sales-former-chief-growth-officer-cenly-chen-is-married-to-outgoing-nvidia-vp-jay-puri",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T14:00:00+00:00",
    "summary": "A civil lawsuit claimed that there was \"no way Cenly Chen lacked knowledge about the company's illicit sales.\""
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/developer-vibe-codes-windows-11-alternative-operating-system-for-amd64-arm64-and-riscv64-hardware-libernt-is-a-free-64-bit-clone-promising-reliable-stable-and-efficient-performance",
    "domain": "AI 算力 / 半导体",
    "title": "Developer vibe codes Windows 11 alternative operating system for amd64, arm64, and riscv64 hardware",
    "url": "https://www.tomshardware.com/software/windows/developer-vibe-codes-windows-11-alternative-operating-system-for-amd64-arm64-and-riscv64-hardware-libernt-is-a-free-64-bit-clone-promising-reliable-stable-and-efficient-performance",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T13:30:00+00:00",
    "summary": "There’s a new vibe-coded OS in town going by the name of LiberNT."
  },
  {
    "id": "hn:50552424",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Neon",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/",
    "source": "yigitdemirag",
    "platform": "hackernews",
    "points": 1035,
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
    "points": 574,
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
    "points": 350,
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
    "id": "hn:50550415",
    "domain": "大厂 AI 动态",
    "title": "Genie 4 is now available",
    "url": "https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/",
    "source": "leumon",
    "platform": "hackernews",
    "points": 288,
    "published_at": "2026-11-18T18:49:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:50554374",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Neon looks like an Opus 5.5 competitor",
    "url": "https://micjm.com/blog/gemini-4-neon-looks-like-a-top-model/",
    "source": "seizethecheese",
    "platform": "hackernews",
    "points": 254,
    "published_at": "2026-11-19T00:29:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:50541790",
    "domain": "大厂 AI 动态",
    "title": "Why is Gemini 4 Carbon taking so long?",
    "url": "https://kernel.dev/blog/why-is-gemini-4-carbon-taking-so-long/",
    "source": "deenadz",
    "platform": "hackernews",
    "points": 281,
    "published_at": "2026-11-18T04:14:04+00:00",
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
    "id": "hn:50557885",
    "domain": "大厂 AI 动态",
    "title": "DeepMind Employees Are Unionising",
    "url": "https://www.gdmunion.co.uk",
    "source": "nervai",
    "platform": "hackernews",
    "points": 121,
    "published_at": "2026-11-19T09:28:56+00:00",
    "summary": ""
  },
  {
    "id": "hn:50569519",
    "domain": "大厂 AI 动态",
    "title": "What Comes After AGI?",
    "url": "https://institute.deepmind.com/essays/what-comes-after-agi/",
    "source": "jdkee",
    "platform": "hackernews",
    "points": 72,
    "published_at": "2026-11-20T02:44:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:50551601",
    "domain": "大厂 AI 动态",
    "title": "Google Gemini's \"Tasks\" Personal Assistant Is Now Free",
    "url": "https://blog.google/innovation-and-ai/products/gemini-app/tasks-in-gemini-free-new-features/",
    "source": "hackeratrandom",
    "platform": "hackernews",
    "points": 57,
    "published_at": "2026-11-18T20:20:17+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/tech/1038227/apple-ai-agent-engineer-job-listing",
    "domain": "大厂 AI 动态",
    "title": "Apple is hiring engineers to build its own AI agent",
    "url": "https://www.theverge.com/tech/1038227/apple-ai-agent-engineer-job-listing",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T22:31:41+00:00",
    "summary": "Apple is working on its own AI agent that can perform a range of tasks for you, including browsing the web, working across apps, writing code, and calling services. That's according to a job listing s"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1038063/nvidia-stock-market-price-earnings",
    "domain": "大厂 AI 动态",
    "title": "A brief history of Nvidia’s recent stock fluctuations",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1038063/nvidia-stock-market-price-earnings",
    "source": "Ellen Thomas",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T21:59:35+00:00",
    "summary": "\"We've got this,\" Colette Kress, interim CEO of Nvidia, said Tuesday night as she closed out the embattled chip company's third quarter earnings call. By Thursday, the company's stock price was hoveri"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1038157/meta-quest-vr-3d-movies-tv-app",
    "domain": "大厂 AI 动态",
    "title": "Meta now sells 3D movies on Quest VR headsets",
    "url": "https://www.theverge.com/tech/1038157/meta-quest-vr-3d-movies-tv-app",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T21:12:06+00:00",
    "summary": "Meta now offers more than 150 3D movies that you can buy or rent to watch in VR on its Quest 3 and 3S headsets, the company announced today. The movies are available in Meta's TV app and include title"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1038087/meta-muse-charm-ai-price",
    "domain": "大厂 AI 动态",
    "title": "Meta’s Muse Charm might cost $300",
    "url": "https://www.theverge.com/tech/1038087/meta-muse-charm-ai-price",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T20:22:17+00:00",
    "summary": "Meta is planning to price the Muse Charm, a little gadget with a screen that lets you chat with your Muse AI agent, at $300, according to The Information. CEO Mark Zuckerberg revealed the gadget earli"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1038059/google-search-homepage-ai-chats",
    "domain": "大厂 AI 动态",
    "title": "Google is putting AI chats right on the homepage",
    "url": "https://www.theverge.com/tech/1038059/google-search-homepage-ai-chats",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T20:05:06+00:00",
    "summary": "Google is updating its homepage to include AI searches. In a post on X, Google's vice president of product, Robby Stein, shows how you can now open a collapsible sidebar to view and continue your AI c"
  },
  {
    "id": "rss:https://www.theverge.com/policy/1037987/fcc-prison-cellphone-signal-jamming",
    "domain": "大厂 AI 动态",
    "title": "FCC greenlights rule allowing prisons to jam cellphone signals",
    "url": "https://www.theverge.com/policy/1037987/fcc-prison-cellphone-signal-jamming",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T19:40:28+00:00",
    "summary": "The Federal Communications Commission voted unanimously to allow state and local prisons to jam cellphones. In an announcement on Thursday, the FCC argues the rule will help combat an \"influx of contr"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1037790/sony-wh-1000xm5-black-friday-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Sony’s WH-1000XM5 are cheaper than ever for Black Friday",
    "url": "https://www.theverge.com/gadgets/1037790/sony-wh-1000xm5-black-friday-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T19:35:52+00:00",
    "summary": "Back in my day, the only “Doorbuster” sales were at physical retail stores. But now, you can get ultra-low prices before Black Friday whether you want to shop in-store or online. One that stands out i"
  },
  {
    "id": "rss:https://www.theverge.com/games/1038010/valve-steam-machine-waitlist-supply",
    "domain": "大厂 AI 动态",
    "title": "You can now buy a Steam Machine without getting on a waitlist",
    "url": "https://www.theverge.com/games/1038010/valve-steam-machine-waitlist-supply",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T19:33:22+00:00",
    "summary": "Valve announced some updates about Steam Machine availability today, including good news if you want to buy one right now and potential bad news about future supply due to RAMaggedon. The good news: Y"
  },
  {
    "id": "rss:https://www.theverge.com/news/1037951/instagram-amazon-affiliate-links-influencers-ads",
    "domain": "大厂 AI 动态",
    "title": "Some creators are skeptical of Instagram’s new affiliate program",
    "url": "https://www.theverge.com/news/1037951/instagram-amazon-affiliate-links-influencers-ads",
    "source": "Mia Sato",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T19:12:30+00:00",
    "summary": "For years, influencers have come up with workarounds on social media to figure out how to share affiliate links with followers. A new integration between Instagram and Amazon was announced earlier thi"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1037042/sonos-black-friday-2026-speaker-soundbar-deals-sale",
    "domain": "大厂 AI 动态",
    "title": "Sonos is taking up to 30 percent off speakers and soundbars right now",
    "url": "https://www.theverge.com/gadgets/1037042/sonos-black-friday-2026-speaker-soundbar-deals-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T18:33:08+00:00",
    "summary": "Sonos speakers and soundbars aren&#8217;t exactly cheap, but thankfully the company&#8217;s Black Friday sale has already begun, making everything a little easier to afford through November 30th. Most"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/20/the-u-s-national-cyber-director-is-stepping-down/",
    "domain": "大厂 AI 动态",
    "title": "The U.S. national cyber director is stepping down",
    "url": "https://techcrunch.com/2026/11/20/the-u-s-national-cyber-director-is-stepping-down/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T09:14:19+00:00",
    "summary": "The news comes as businesses across the country report a flurry of technical outages, the causes of which are still unknown."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/19/apple-may-be-developing-its-own-ai-agent-that-runs-your-mac/",
    "domain": "大厂 AI 动态",
    "title": "Apple may be developing its own AI agent that runs your Mac",
    "url": "https://techcrunch.com/2026/11/19/apple-may-be-developing-its-own-ai-agent-that-runs-your-mac/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T00:56:01+00:00",
    "summary": "The iPhone maker appears to be building agents that can compete with the likes of Meta Muse, Instinct, Claude, and OpenAI Dots."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/19/anthropics-7-founders-cashed-out-nearly-2b-in-record-breaking-ipo/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic’s 7 founders cashed out nearly $2B in record-breaking IPO",
    "url": "https://techcrunch.com/2026/11/19/anthropics-7-founders-cashed-out-nearly-2b-in-record-breaking-ipo/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T00:43:50+00:00",
    "summary": "At the upgraded $83/share IPO price, Anthropic's seven founders each pocketed $280 million, while the company nabbed nearly $105 billion."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/19/anthropic-rival-says-companies-can-mostly-skip-the-pricey-models/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic rival says companies can (mostly) skip the pricey models",
    "url": "https://techcrunch.com/2026/11/19/anthropic-rival-says-companies-can-mostly-skip-the-pricey-models/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T00:26:03+00:00",
    "summary": "On the day Anthropic went public, Fireworks AI’s co-founder made the case for open source models as a cheaper alternative, and addressed the breaches that have cost the company some customers’ trust."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/19/elon-musk-says-spacex-has-a-plan-to-eliminate-cell-phone-dead-zones/",
    "domain": "大厂 AI 动态",
    "title": "Elon Musk says SpaceX has a plan to eliminate cell phone dead zones",
    "url": "https://techcrunch.com/2026/11/19/elon-musk-says-spacex-has-a-plan-to-eliminate-cell-phone-dead-zones/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T23:37:56+00:00",
    "summary": "SpaceX CEO Elon Musk said the company has completed the design of a miniature rooftop cell tower that could provide better coverage to mobile phones and eliminate dead zones."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/19/want-to-see-your-live-ai-usage-on-your-macs-icons-this-clever-new-app-lets-you/",
    "domain": "大厂 AI 动态",
    "title": "Want to see your live AI usage on your Mac’s icons? This clever new app lets you",
    "url": "https://techcrunch.com/2026/11/19/want-to-see-your-live-ai-usage-on-your-macs-icons-this-clever-new-app-lets-you/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T22:33:26+00:00",
    "summary": "IconSwapper brings your Mac's app icons to life with real-time data, animations, and playful customizations that make your desktop more fun."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/19/metas-new-muse-charm-device-may-cost-300/",
    "domain": "大厂 AI 动态",
    "title": "Meta’s new Muse Charm device may cost $300",
    "url": "https://techcrunch.com/2026/11/19/metas-new-muse-charm-device-may-cost-300/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T21:58:06+00:00",
    "summary": "Meta hasn't denied the reporting from The Information, saying only that it will \"have more to share soon\" about its upcoming AI wearable."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/19/these-tech-outages-are-giving-y2k-ai-agent-style/",
    "domain": "大厂 AI 动态",
    "title": "These tech outages are giving Y2K, AI agent style",
    "url": "https://techcrunch.com/2026/11/19/these-tech-outages-are-giving-y2k-ai-agent-style/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T21:42:31+00:00",
    "summary": "Are the recent outages in the airline booking systems, banking platforms, and productivity platforms really a coincidence? There's actually likely something deeper going on, cybersecurity experts say."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/19/uber-tests-rides-for-kids-as-young-as-10-with-extra-pay-for-drivers/",
    "domain": "大厂 AI 动态",
    "title": "Uber tests rides for kids as young as 10, with extra pay for drivers",
    "url": "https://techcrunch.com/2026/11/19/uber-tests-rides-for-kids-as-young-as-10-with-extra-pay-for-drivers/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T21:33:24+00:00",
    "summary": "Uber is testing the new program in three U.S. cities."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/19/nvidia-ceo-jensen-huangs-affair-with-alleged-chinese-spy-a-timeline/",
    "domain": "大厂 AI 动态",
    "title": "The unfolding Jensen Huang scandal: a timeline",
    "url": "https://techcrunch.com/2026/11/19/nvidia-ceo-jensen-huangs-affair-with-alleged-chinese-spy-a-timeline/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T20:18:49+00:00",
    "summary": "Jensen Huang has resigned from Nvidia following an affair, which could have ramifications for national security as the U.S. and China race to develop the most advanced AI infrastructure."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/19/anthropics-ipo-could-deliver-156-billion-to-charity/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic’s IPO could deliver $156B to charity",
    "url": "https://techcrunch.com/2026/11/19/anthropics-ipo-could-deliver-156-billion-to-charity/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T19:10:45+00:00",
    "summary": "At a stock price of $95, the frontier lab's Public Benefit Foundation, its employee donations, and the company's match tot up to $156 billion."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/19/google-gives-gemini-the-ability-to-use-your-mac-for-you/",
    "domain": "大厂 AI 动态",
    "title": "Google gives Gemini the ability to use your Mac for you",
    "url": "https://techcrunch.com/2026/11/19/google-gives-gemini-the-ability-to-use-your-mac-for-you/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T18:09:11+00:00",
    "summary": "Google's latest update to Gemini brings an AI agent to the Mac that can organize files, fill out forms, and tackle multistep workflows."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/19/metas-ai-agent-muse-is-mixing-up-conversations-and-exposing-private-data-report-says/",
    "domain": "大厂 AI 动态",
    "title": "Meta’s AI agent Muse is mixing up conversations and could be exposing private data, report says",
    "url": "https://techcrunch.com/2026/11/19/metas-ai-agent-muse-is-mixing-up-conversations-and-exposing-private-data-report-says/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T17:38:40+00:00",
    "summary": "In some of these instances, employees said Muse surfaced messages about childcare requests they never made, career advice they never asked for, product orders they never placed, and bank account balan"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/19/former-alibaba-execs-everful-raises-48-5m-to-connect-retailers-with-chinese-factories/",
    "domain": "大厂 AI 动态",
    "title": "Former Alibaba exec’s Everful raises $48.5M to connect retailers with Chinese factories",
    "url": "https://techcrunch.com/2026/11/19/former-alibaba-execs-everful-raises-48-5m-to-connect-retailers-with-chinese-factories/",
    "source": "Kate Park",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T17:00:00+00:00",
    "summary": "Everful has raised $48.5 million to expand its factory-direct sourcing platform, helping retailers source products from overseas manufacturers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/19/anthropic-hits-nasdaq-exchanges-at-110-27-above-ipo-price/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic hits Nasdaq exchanges at $111, 33% above IPO price",
    "url": "https://techcrunch.com/2026/11/19/anthropic-hits-nasdaq-exchanges-at-110-27-above-ipo-price/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T16:59:23+00:00",
    "summary": "Anthropic's IPO price was set at $83, representing more than $80 billion in new capital raised."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/19/at-nasdaq-opening-bell-anthropic-ceo-recommits-to-pacing-ai-development/",
    "domain": "大厂 AI 动态",
    "title": "At Nasdaq opening bell, Anthropic CEO recommits to pacing AI development",
    "url": "https://techcrunch.com/2026/11/19/at-nasdaq-opening-bell-anthropic-ceo-recommits-to-pacing-ai-development/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T16:19:41+00:00",
    "summary": "In his Nasdaq opening bell speech, Dario Amodei reiterated Anthropic's commitment to pacing AI development, regardless of business or political pressure."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/19/u-k-government-forced-to-disclose-secret-apple-backdoor-order/",
    "domain": "大厂 AI 动态",
    "title": "UK government forced to disclose secret Apple backdoor order",
    "url": "https://techcrunch.com/2026/11/19/u-k-government-forced-to-disclose-secret-apple-backdoor-order/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T15:32:20+00:00",
    "summary": "The U.K. tribunal's ruling rejected London's claim that disclosing the order would be damaging to national security."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/19/anthropics-ipo-puts-ais-circular-financing-boom-to-the-test/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic’s IPO puts AI’s circular financing boom to the test",
    "url": "https://techcrunch.com/2026/11/19/anthropics-ipo-puts-ais-circular-financing-boom-to-the-test/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T14:54:39+00:00",
    "summary": "Anthropic faces enormous compute commitments as it goes public, but its biggest infrastructure partners, including Amazon and Google, could continue profiting from AI even if Anthropic loses its lead."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/19/nimble-enters-the-item-tracking-market-with-eco-friendly-luggage-tags-and-keychains/",
    "domain": "大厂 AI 动态",
    "title": "Nimble enters the item-tracking market with eco-friendly luggage tags and keychains",
    "url": "https://techcrunch.com/2026/11/19/nimble-enters-the-item-tracking-market-with-eco-friendly-luggage-tags-and-keychains/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T14:00:00+00:00",
    "summary": "As Google takes on Apple in the item-tracking market, Nimble is hoping its trackable wallets, keychains, luggage tags, and passport covers stand out."
  },
  {
    "id": "hn:50556287",
    "domain": "股票",
    "title": "Ruby2ßhell: Pre-authentication RCE on stock Rails",
    "url": "https://verialabs.com/ruby2shell/",
    "source": "jdns",
    "platform": "hackernews",
    "points": 399,
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
    "id": "hn:50510005",
    "domain": "股票",
    "title": "Do House members' stock trades beat the market? A test of 8,900 trades",
    "url": "https://arkanumdata.com/research/house-trades",
    "source": "Bluestein",
    "platform": "hackernews",
    "points": 128,
    "published_at": "2026-11-15T19:46:02+00:00",
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
    "id": "hn:50401029",
    "domain": "股票",
    "title": "The AI sell-off compared to well-known stock market crashes",
    "url": "https://www.kadoa.com/companies/insights/ai-selloff-perspective",
    "source": "hubraumhugo",
    "platform": "hackernews",
    "points": 101,
    "published_at": "2026-11-07T02:20:06+00:00",
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
    "id": "hn:50542361",
    "domain": "股票",
    "title": "Interesting Learnings Working for a Startup",
    "url": "https://news.ycombinator.com/item?id=50542361",
    "source": "Jessiejia11",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-11-18T05:52:37+00:00",
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
    "id": "hn:50445463",
    "domain": "股票",
    "title": "Anthropic Targets $1.4T Valuation in IPO",
    "url": "https://www.bloomberg.com/news/videos/2026-11-10/anthropic-targets-1-4-trillion-valuation-in-ipo-video",
    "source": "rndsignals",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-11-10T19:56:11+00:00",
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
    "id": "hn:50456668",
    "domain": "股票",
    "title": "Anthropic says a key AI safety alarm has been triggered, days before its IPO",
    "url": "https://finance.yahoo.com/markets/article/anthropic-says-a-key-ai-safety-alarm-has-been-triggered-days-before-its-ipo-171519615.html",
    "source": "healsdata",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-11-11T18:23:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:50386483",
    "domain": "股票",
    "title": "Major Investors Are Skeptical Anthropic IPO Can Achieve $1.5T Valuation",
    "url": "https://www.wsj.com/finance/major-investors-are-skeptical-anthropic-ipo-can-achieve-1-5-trillion-valuation-ca965d8b",
    "source": "sandinmyjoints",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-11-06T00:17:47+00:00",
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
    "id": "hn:50326281",
    "domain": "股票",
    "title": "Ant: Can unprecedented revenue growth outrun irresponsibly large investment",
    "url": "https://leonlins.com/writing/anthropic_ipo",
    "source": "avoidboringppl",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-11-01T14:56:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:50323575",
    "domain": "股票",
    "title": "We're Living in the Age of the Imperial CEO",
    "url": "https://www.wsj.com/tech/ai/anthropic-ipo-dual-class-stock-founder-control-4c43a56d",
    "source": "pretext",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-11-01T08:09:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:50251762",
    "domain": "股票",
    "title": "Anthropic Is the Most Ridiculous IPO of 2026 [pdf]",
    "url": "https://www.newconstructs.com/wp-content/uploads/2026/10/Anthropic-Is-The-Most-Ridiculous-IPO-of-2026.pdf",
    "source": "simonebrunozzi",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-10-26T22:06:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:50243343",
    "domain": "股票",
    "title": "Anthropic rushing IPO before AI bubble bursts",
    "url": "https://nypost.com/2026/10/23/business/wall-street-is-urging-anthropic-openai-to-do-their-ipos-in-a-hurry-heres-why/",
    "source": "nothrowaways",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-10-26T13:30:05+00:00",
    "summary": ""
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
    "id": "hn:50391456",
    "domain": "金融",
    "title": "Tesla to wind down Cybertruck production",
    "url": "https://www.nbcnews.com/tech/tech-news/tesla-wind-cybertruck-production-years-poor-sales-markets-rcna607817",
    "source": "PLenz",
    "platform": "hackernews",
    "points": 1167,
    "published_at": "2026-11-06T12:13:51+00:00",
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
    "points": 178,
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
    "id": "hn:50414427",
    "domain": "金融",
    "title": "Tesla Hasn't Had a Successful New Product Launch Since JB Straubel Stepped Down",
    "url": "https://cleantechnica.com/2026/11/07/tesla-hasnt-had-a-successful-new-product-launch-since-jb-straubel-stepped-down-as-cto/",
    "source": "gumby",
    "platform": "hackernews",
    "points": 208,
    "published_at": "2026-11-08T16:07:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:50525658",
    "domain": "金融",
    "title": "Pentagon fails ninth straight audit despite progress in organizing finances",
    "url": "https://www.reuters.com/business/aerospace-defense/pentagon-fails-ninth-straight-audit-despite-progress-organizing-finances-2026-11-16/",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 150,
    "published_at": "2026-11-17T00:23:21+00:00",
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
    "id": "hn:50190168",
    "domain": "金融",
    "title": "Epic Games Inc v Apple Inc",
    "url": "https://www.judgments.fedcourt.gov.au/judgments/Judgments/fca/single/2026/2026fca1552",
    "source": "Mayzie",
    "platform": "hackernews",
    "points": 193,
    "published_at": "2026-10-22T01:52:03+00:00",
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
    "id": "hn:50236073",
    "domain": "金融",
    "title": "Nvidia and Micron Make Up 34% of America's Earnings Boom",
    "url": "https://www.wsj.com/finance/stocks/the-earnings-boom-is-heavily-reliant-on-just-a-handful-of-stocks-21decb53",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 176,
    "published_at": "2026-10-25T21:07:38+00:00",
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
    "id": "hn:50543108",
    "domain": "金融",
    "title": "Firefox opens hotline for users sick of Microsoft shoving Edge down their throat",
    "url": "https://www.neowin.net/news/firefox-opens-hotline-for-windows-users-fed-up-with-microsoft-shoving-edge-down-their-throat/",
    "source": "bundie",
    "platform": "hackernews",
    "points": 36,
    "published_at": "2026-11-18T07:51:58+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.25047",
    "domain": "金融",
    "title": "A joint framework for SPX, VIX and VXX",
    "url": "https://arxiv.org/abs/2611.25047",
    "source": "Martino Grasselli, Andrea Stanghellini, Sara Svaluto-Ferro",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T05:00:00+00:00",
    "summary": "arXiv:2611.25047v1 Announce Type: new Abstract: Options on VXX bring the dynamics of the VIX futures curve into the joint SPX-VIX calibration problem. We construct a common model by specifying the VIX"
  },
  {
    "id": "rss:https://arxiv.org/abs/2508.05022",
    "domain": "金融",
    "title": "A Multivariate Generalized Cox Model for Dependent and Simultaneous Default Times",
    "url": "https://arxiv.org/abs/2508.05022",
    "source": "Djibril Gueye, Alejandra Quintos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T05:00:00+00:00",
    "summary": "arXiv:2508.05022v2 Announce Type: cross Abstract: We propose a framework for dependent default times where each name defaults when an increasing driver crosses an independent unit exponential threshol"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.25218",
    "domain": "金融",
    "title": "The American Medical Directory Panel: Comparing AI-Assisted and LLM Transcription with Manual Data Entry at Scale",
    "url": "https://arxiv.org/abs/2611.25218",
    "source": "Christian M. Dahl, Sophie Li, Rasmus Emil Nyholm, Maja U. Pedersen, Anthony Wray",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T05:00:00+00:00",
    "summary": "arXiv:2611.25218v1 Announce Type: cross Abstract: How closely does machine transcription agree with manual double-entry data? We digitize the 1912 and 1921 editions of the American Medical Directory, "
  },
  {
    "id": "rss:https://arxiv.org/abs/1910.14023",
    "domain": "金融",
    "title": "Firm Entry and Exit with Unbounded Productivity",
    "url": "https://arxiv.org/abs/1910.14023",
    "source": "Akshay Shanker, John Stachurski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T05:00:00+00:00",
    "summary": "arXiv:1910.14023v4 Announce Type: replace Abstract: In Hopenhayn's (1992) entry-exit model productivity is bounded, implying that the predicted firm size distribution cannot match the power law tail o"
  },
  {
    "id": "rss:https://arxiv.org/abs/2408.03134",
    "domain": "金融",
    "title": "Incomplete-market CAPM equilibria in continuous time",
    "url": "https://arxiv.org/abs/2408.03134",
    "source": "Nikolaos Constantinou, Christoph Czichowsky, Martin Herdegen, David Martins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T05:00:00+00:00",
    "summary": "arXiv:2408.03134v4 Announce Type: replace Abstract: We study continuous-time CAPM equilibria with general mean-variance preferences of the form $U(\\mu,\\sigma)$, where $U$ is strictly quasiconcave, inc"
  },
  {
    "id": "rss:https://arxiv.org/abs/2505.19276",
    "domain": "金融",
    "title": "A General Theory of Risk Sharing",
    "url": "https://arxiv.org/abs/2505.19276",
    "source": "Vasily Melnikov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T05:00:00+00:00",
    "summary": "arXiv:2505.19276v3 Announce Type: replace Abstract: We introduce a new paradigm for risk sharing that generalizes earlier models based on discrete agents and extends them to allow for sharing risk wit"
  },
  {
    "id": "rss:https://arxiv.org/abs/2509.08096",
    "domain": "金融",
    "title": "Joint calibration of the volatility surface and variance term structure",
    "url": "https://arxiv.org/abs/2509.08096",
    "source": "Jiwook Yoo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T05:00:00+00:00",
    "summary": "arXiv:2509.08096v2 Announce Type: replace Abstract: I study the calibration of option pricing models with an objective that combines errors on the implied volatility surface and on the variance term s"
  },
  {
    "id": "rss:https://arxiv.org/abs/2510.15942",
    "domain": "金融",
    "title": "Intrinsic Geometry of the Stock Market from Graph Ricci Flow",
    "url": "https://arxiv.org/abs/2510.15942",
    "source": "Bhargavi Srinivasan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T05:00:00+00:00",
    "summary": "arXiv:2510.15942v3 Announce Type: replace Abstract: We use the discrete Ollivier-Ricci curvature with Ricci flow to examine the intrinsic geometry of financial markets through the empirical correlatio"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.01897",
    "domain": "金融",
    "title": "Shared Models, Selective Trading, and Order Flow",
    "url": "https://arxiv.org/abs/2610.01897",
    "source": "Victoria Ruojie Li, Arka Prava Bandyopadhyay",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T05:00:00+00:00",
    "summary": "arXiv:2610.01897v2 Announce Type: replace Abstract: We study whether the diversity of language models installed in a trading population carries over to the orders that reach the market. In simulated m"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.16151",
    "domain": "金融",
    "title": "Neural Estimation of Irreversibility in Real and Simulated Limit Order Book Paths",
    "url": "https://arxiv.org/abs/2610.16151",
    "source": "Hyeonjun Yeo, Doohwi Cha, Yoontae Hwang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T05:00:00+00:00",
    "summary": "arXiv:2610.16151v3 Announce Type: replace Abstract: A path indistinguishable from its own reverse carries no arrow of time, so time irreversibility is a necessary condition for a directed mechanism to"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.37957",
    "domain": "金融",
    "title": "Multiscale Reconstruction of Weighted Networks from Coarse-Grained Data",
    "url": "https://arxiv.org/abs/2609.37957",
    "source": "Mattia Marzi, Frank P. Pijpers, Diego Garlaschelli",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T05:00:00+00:00",
    "summary": "arXiv:2609.37957v2 Announce Type: replace-cross Abstract: Network reconstruction from partial information is usually performed at the same resolution level at which constraints are observable. This be"
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
    "id": "hn:50202671",
    "domain": "金融",
    "title": "AI compute is the new oil–and needs a new market",
    "url": "https://www.economist.com/finance-and-economics/2026/10/22/ai-compute-is-the-new-oil-and-needs-a-new-market",
    "source": "ijidak",
    "platform": "hackernews",
    "points": 54,
    "published_at": "2026-10-22T23:45:16+00:00",
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
  },
  {
    "id": "hn:50394130",
    "domain": "金融",
    "title": "Tesla Ends Cybertruck Production",
    "url": "https://www.heise.de/en/news/Tesla-ends-Cybertruck-production-in-Texas-11515739.html",
    "source": "Betelbuddy",
    "platform": "hackernews",
    "points": 26,
    "published_at": "2026-11-06T16:05:54+00:00",
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
    "id": "hn:50194602",
    "domain": "金融",
    "title": "Full Disk Encryption on Fedora with TPM2",
    "url": "https://www.apalrd.net/posts/2026/ent_luks/",
    "source": "speckx",
    "platform": "hackernews",
    "points": 34,
    "published_at": "2026-10-22T12:46:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:50236506",
    "domain": "金融",
    "title": "F45 (Fedora 45) Final Is No-Go",
    "url": "https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/EWDOYT6TOMFY4XPL5MJC2QWCDJBOR6MU/",
    "source": "gnabgib",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-10-25T22:09:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:50467087",
    "domain": "电子信息与芯片",
    "title": "Jensen Huang resigns",
    "url": "https://apnews.com/article/nvidia-megaspeed-china-singapore-huang-5403f152a601cf82ce939f1d24fffa0f",
    "source": "lldb",
    "platform": "hackernews",
    "points": 4060,
    "published_at": "2026-11-12T13:52:29+00:00",
    "summary": ""
  }
]
```
