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

- 今日日期：`2026-11-21`
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
  "date": "2026-11-21",
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
    "points": 2274762,
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
    "points": 2142077,
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
    "points": 1566079,
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
    "points": 1508905,
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
    "points": 1482923,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1aeLqzUE6L",
    "domain": "AI",
    "title": "10分钟讲清楚 Prompt, Agent, MCP 是什么",
    "url": "http://www.bilibili.com/video/av114410228025650",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 915978,
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
    "points": 907202,
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
    "points": 759938,
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
    "points": 597378,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV1kr4h6fExw",
    "domain": "AI",
    "title": "DeepSeek 新出的 Super Agent 是什么？真有用么？",
    "url": "http://www.bilibili.com/video/av117564076202051",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 520696,
    "published_at": "2026-11-05T13:35:56+00:00",
    "summary": "DeepSeek Harness 团队最新开源的 Super-agent 是什么？和传统 Agent 有什么区别？它是怎么工作的？真的能提升 AI 工作的效率么？一期视频带你掌握 Super-agent 智能体，对 AI 小白、AI 编程爱好者、前端和后端程序员、AI 应用开发求职者都有帮助\n编程学习教程+实战项目+简历模板：codefather.cn\n免费 AI 编程教程：github.com/"
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 485105,
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
    "points": 436712,
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
    "points": 434203,
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
    "points": 428646,
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
    "points": 364091,
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
    "points": 331040,
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
    "points": 302952,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1h3W76wEem",
    "domain": "AI",
    "title": "Claude(Code)桌面APP，保姆级全攻略，一期视频精通，顶级Agent软件长什么样？",
    "url": "http://www.bilibili.com/video/av117580048108571",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 287670,
    "published_at": "2026-11-08T09:14:07+00:00",
    "summary": "最近Claude桌面端（Claude Desktop） 有了一大波功能更新。随着一步步的迭代，它已经把 Claude Code 的编程、Claude Design 的设计，以及 Claude Cowork 的办公等核心能力，全部收入了同一个桌面客户端，特别是Claude Code已经从原本黑乎乎的命令行工具，进化成了桌面客户端的完全体形态。再搭配上超强的Opus5.5 模型，已经能称得上是地表顶级"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 238239,
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
    "points": 187453,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1qJs16WEJj",
    "domain": "AI",
    "title": "今天体验的人生副本是:沉迷vibe coding走火入魔的AI嘉豪",
    "url": "http://www.bilibili.com/video/av117635899524333",
    "source": "vibe睦头人",
    "platform": "bilibili",
    "points": 185730,
    "published_at": "2026-11-18T06:01:48+00:00",
    "summary": "ai生成，仅供娱乐，如有雷同，纯属巧合（（"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 166546,
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
    "points": 164165,
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
    "points": 162189,
    "published_at": "2025-02-18T13:13:51+00:00",
    "summary": "我试用了几十种AI编程辅助工具，找到了其中三个免费，并且效果最好的方案。 本期视频就来跟大家分享一下。视频中间会穿插很多AI编程工具的使用技巧，还有看待AI编程的一些个人思考。本期视频没有广告都是个人的经验干货，废话不多说我们直接开始。"
  },
  {
    "id": "bvid:BV1AJen6SEVQ",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Agent智能体】教程！大模型入门到进阶，一套全解决！Agentic AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av117274400790619",
    "source": "吴恩达Agent",
    "platform": "bilibili",
    "points": 158110,
    "published_at": "2026-09-15T09:48:26+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n1. 构建智能体设计模式：反射、工具使用、规划与多智能体工作流；\n2. 将人工智能与外部工具集成：数据库、API、网络搜索与代码执行；\n3. 评估并优化人工智能系统：性能指标、错误分析与生产部署\n4、使用开放标准格式和最佳实践创建可重复使用的技能，并组合以创建复杂的工作流程。\n5、建立定制代码生成技能，审核你的代"
  },
  {
    "id": "bvid:BV1eYPpeWEnT",
    "domain": "AI",
    "title": "Cursor + MCP = 王炸！彻底颠覆我的Cursor工作流，效率直接起飞",
    "url": "http://www.bilibili.com/video/av114073660301264",
    "source": "御风大世界",
    "platform": "bilibili",
    "points": 151896,
    "published_at": "2025-02-27T03:19:03+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1Qcg6zgEhU",
    "domain": "AI",
    "title": "【AI Agent实战】从零开始教你搭建Agent智能体，小白也能学会的保姆级教程！让你少走99%弯路！",
    "url": "http://www.bilibili.com/video/av114771105945944",
    "source": "讲AI的小坛",
    "platform": "bilibili",
    "points": 127534,
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
    "points": 118393,
    "published_at": "2026-07-27T09:19:37+00:00",
    "summary": "还在卷传统软件测试？2026年必学的AI智能体(Agent)测试来了！本期视频专为0基础小白打造，从软件测试基础讲起...若要本视频配套资源笔记可加up主企微（请看置顶留言最后一句话）。"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 94380,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1cVW86JE2e",
    "domain": "AI",
    "title": "Vibe Coding 完不会获客？我用 AI 做了一个「营销数据库」！【B站AI创造公开赛】",
    "url": "http://www.bilibili.com/video/av117587245599812",
    "source": "熠辉IndieDev",
    "platform": "bilibili",
    "points": 76352,
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
    "points": 62980,
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
    "points": 57093,
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
    "points": 50673,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1uVSUBkEfZ",
    "domain": "AI",
    "title": "Microsoft Copilot完整教程(上) 从入门到Agent 一站式掌握AI办公",
    "url": "http://www.bilibili.com/video/av116351721084069",
    "source": "星小脉",
    "platform": "bilibili",
    "points": 47331,
    "published_at": "2026-04-05T11:00:20+00:00",
    "summary": "2026年最全面的Microsoft Copilot教程上半部分。从Copilot首页入门到Agent深度解析，涵盖搜索、资料库、AI视频生成、Copilot Pages、PowerPoint智能幻灯片等全部功能。由培训了6万人的AI顾问Cherie Brock与Sabrina Ramonov联合讲解。"
  },
  {
    "id": "bvid:BV1wpxq6VEXx",
    "domain": "AI",
    "title": "【AI时代的STM32教程】AI Agent 初体验",
    "url": "http://www.bilibili.com/video/av117529699682124",
    "source": "keysking",
    "platform": "bilibili",
    "points": 42355,
    "published_at": "2026-10-30T11:52:06+00:00",
    "summary": "一句话，让 AI 帮我们完成第一个 STM32C5 程序！🚀\n本期我们一起认识 AI Agent，学习如何描述开发需求，并借助开源的 STM32C5DevSkills，让 AI 完成工程创建、芯片配置、代码编写和编译烧录，让律动小板上的小灯闪烁起来！\n也特别感谢 @意法半导体中国   对本系列教程的支持～下期我们再亲手走一遍开发流程，把 Agent 替我们完成的工作，一步步搞明白！"
  },
  {
    "id": "bvid:BV1hmb26ZEws",
    "domain": "AI",
    "title": "DeepSeek Harness 实测  Claude Code 对比后，梁神我错了 差距比我想的大",
    "url": "http://www.bilibili.com/video/av117100337236191",
    "source": "程序员晓刘",
    "platform": "bilibili",
    "points": 41858,
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
    "points": 41539,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV1uwxG6DEra",
    "domain": "AI",
    "title": "3分钟讲透：Vibe Coding如何避免💩屎山代码",
    "url": "http://www.bilibili.com/video/av117513727838880",
    "source": "鲤哥builder",
    "platform": "bilibili",
    "points": 32101,
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
    "points": 31304,
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
    "points": 29990,
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
    "points": 27076,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1f57C6YErb",
    "domain": "AI",
    "title": "手把手教你Codex安装和使用MCP！新手必备~",
    "url": "http://www.bilibili.com/video/av116696861907147",
    "source": "Raina测试",
    "platform": "bilibili",
    "points": 19809,
    "published_at": "2026-06-06T11:29:00+00:00",
    "summary": "这一期给大家分享下在codex里面如何配置和使用MCP，和skill一样，MCP也是我们平时用得比较多的，所以建议大家也可以学一下它的基础配置和使用~\n步骤都不难，跟着操作就可以了"
  },
  {
    "id": "bvid:BV13sJcz9Egm",
    "domain": "AI",
    "title": "让AI替你打工！教你用Trae+MCP自动操作网页，采集数据，有手就能学会！mcp教程，mcp实战，mcp开发",
    "url": "http://www.bilibili.com/video/av114521544852773",
    "source": "大模型实战课程",
    "platform": "bilibili",
    "points": 17611,
    "published_at": "2025-05-17T05:36:05+00:00",
    "summary": "让AI替你打工！教你用Trae+MCP自动操作网页，采集数据，有手就能学会！mcp教程，mcp实战，mcp开发"
  },
  {
    "id": "bvid:BV1xh3C6cEGv",
    "domain": "AI",
    "title": "两周完成一篇SCI论文，用claude code帮你干",
    "url": "http://www.bilibili.com/video/av117002408559933",
    "source": "博士大师兄木水",
    "platform": "bilibili",
    "points": 16758,
    "published_at": "2026-07-29T08:53:04+00:00",
    "summary": "大师兄八股文SCI速成模板已制作成skill，手把手带你实现一键生成SCI论文初稿"
  },
  {
    "id": "bvid:BV1yyQEBdEkm",
    "domain": "AI",
    "title": "【2026B站最全】Claude Code+软件测试实操教程!看完我直接删了收藏夹所有测试教程,从账号注册到Plan驱动测试项目,小白3天上手！",
    "url": "http://www.bilibili.com/video/av116408092525631",
    "source": "软件测试大神",
    "platform": "bilibili",
    "points": 15646,
    "published_at": "2026-04-15T09:55:02+00:00",
    "summary": "配套资料👉：https://b23.tv/qvhxmaQ\n包括:AI测试网站，几十个AI场景测试完整流程，skil文档，测试八股文，项目源码，测试用例模板，工具安装包，学习计划表，学习路线，100g测试新人资料包等等，资料百分百免费，放心领取~"
  },
  {
    "id": "bvid:BV14a4y1T7Cp",
    "domain": "AI",
    "title": "VS Code + CursorCode 插件，AI 帮你编写、调试代码",
    "url": "http://www.bilibili.com/video/av654787185",
    "source": "马隆工作室",
    "platform": "bilibili",
    "points": 14668,
    "published_at": "2023-04-11T11:48:41+00:00",
    "summary": "免费， VS Code + CursorCode 插件，AI 帮你编写、调试代码"
  },
  {
    "id": "bvid:BV1Yhb66LEaF",
    "domain": "AI",
    "title": "3分钟，教你什么是vibe coding",
    "url": "http://www.bilibili.com/video/av117115000524101",
    "source": "开聊pro",
    "platform": "bilibili",
    "points": 14525,
    "published_at": "2026-08-18T06:12:25+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 14257,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
  },
  {
    "id": "bvid:BV1rCJdzFEQg",
    "domain": "AI",
    "title": "让AI帮你干活：WindowsMCP安装和使用！",
    "url": "http://www.bilibili.com/video/av115242814212549",
    "source": "磊哥AI实战",
    "platform": "bilibili",
    "points": 13786,
    "published_at": "2025-09-22T00:00:00+00:00",
    "summary": "AI 自动操作你的电脑，解放双手，提升工作效率。"
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
    "points": 1115,
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
    "points": 670,
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
    "id": "hn:50581438",
    "domain": "AI 算力 / 半导体",
    "title": "US SEC's Nvidia probe is examining potential accounting issues – sources",
    "url": "https://www.marketscreener.com/news/us-sec-s-nvidia-probe-is-examining-potential-accounting-issues-sources-say-ce785ed3dd8ff627",
    "source": "ftchd",
    "platform": "hackernews",
    "points": 288,
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
    "points": 290,
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
    "points": 136,
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
    "id": "hn:50538942",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Chair Harvey Jones says board doesn't intend to reinstate Huang as CEO",
    "url": "https://www.cnbc.com/2026/11/17/nvidia-nvda-earnings-report-q3-2027.html",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 56,
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
    "id": "rss:https://www.eetimes.com/pat-gelsinger-goes-hunting-for-europes-unbuilt-tech-companies/",
    "domain": "AI 算力 / 半导体",
    "title": "Pat Gelsinger Goes Hunting for Europe’s Unbuilt Tech Companies",
    "url": "https://www.eetimes.com/pat-gelsinger-goes-hunting-for-europes-unbuilt-tech-companies/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T22:23:32+00:00",
    "summary": "Playground Global is searching CEA laboratories for technologies that could create new markets—but global capital complicates European sovereignty. The post Pat Gelsinger Goes Hunting for Europe’s Unb"
  },
  {
    "id": "rss:https://www.eetimes.com/palo-alto-networks-expands-into-enterprise-ai-with-4-5b-deal/",
    "domain": "AI 算力 / 半导体",
    "title": "Palo Alto Networks Expands into Enterprise AI with $4.5B Deal",
    "url": "https://www.eetimes.com/palo-alto-networks-expands-into-enterprise-ai-with-4-5b-deal/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T15:37:26+00:00",
    "summary": "Enterprise security outfit Palo Alto Networks snaps up a startup with a platform for post-training and inference of open-weight AI models. The post Palo Alto Networks Expands into Enterprise AI with $"
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
    "id": "rss:https://www.tomshardware.com/pc-components/microsd-cards/sandisk-512gb-microsd-express-deal-slashes-switch-2-storage-by-24-percent-in-amazon-black-friday-offer-price-hits-under-usd100-amid-storage-squeeze",
    "domain": "AI 算力 / 半导体",
    "title": "SanDisk 512GB MicroSD Express deal slashes Switch 2 storage by 24% in Amazon Black Friday offer — price hits under $100 amid storage squeeze",
    "url": "https://www.tomshardware.com/pc-components/microsd-cards/sandisk-512gb-microsd-express-deal-slashes-switch-2-storage-by-24-percent-in-amazon-black-friday-offer-price-hits-under-usd100-amid-storage-squeeze",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-21T10:32:35+00:00",
    "summary": "SanDisk's large 512 GB MicroSD Express card has dropped to just $98 at Amazon, marking a 24% discount when compared to its original list price in a rare storage offer."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-keyboards/asus-rog-strix-scope-ii-96-gaming-keyboard-crashes-to-all-time-low-in-early-black-friday-offer-grab-39-percent-off-a-premium-board-packed-full-of-features",
    "domain": "AI 算力 / 半导体",
    "title": "Asus ROG Strix Scope II 96 gaming keyboard crashes to all-time low in early Black Friday offer — grab 39% off a premium board packed full of features",
    "url": "https://www.tomshardware.com/peripherals/gaming-keyboards/asus-rog-strix-scope-ii-96-gaming-keyboard-crashes-to-all-time-low-in-early-black-friday-offer-grab-39-percent-off-a-premium-board-packed-full-of-features",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-21T09:52:39+00:00",
    "summary": "The Asus ROG Strix Scope II 96 has hit an all-time low price in this Amazon early Black Friday offer, which has slashed the gaming keyboard's price by 39%."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-mice/razers-mmo-mouse-hits-all-time-low-price-at-under-usd60-at-amazon-in-black-friday-deal-naga-v2-hyperspeed-price-craters-by-42-percent-in-stellar-gaming-mouse-offer",
    "domain": "AI 算力 / 半导体",
    "title": "Razer's MMO mouse hits all-time low price at under $60 at Amazon in Black Friday deal — Naga V2 Hyperspeed price craters by 42% in stellar gaming mouse offer",
    "url": "https://www.tomshardware.com/peripherals/gaming-mice/razers-mmo-mouse-hits-all-time-low-price-at-under-usd60-at-amazon-in-black-friday-deal-naga-v2-hyperspeed-price-craters-by-42-percent-in-stellar-gaming-mouse-offer",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-21T09:04:58+00:00",
    "summary": "Razer's Naga V2 Hyperspeed gaming mouse is now just $56 at Amazon, hitting an all-time low price just in time for Black Friday."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/samsungs-gorgeous-49-inch-odyssey-oled-g9-hits-a-new-all-time-low-price-of-usd854-amazon-black-friday-deal-slashes-33-percent-off-gaming-monitor-upgrade",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung’s gorgeous 49-inch Odyssey OLED G9 hits a new all-time low price of $854 — Amazon Black Friday deal slashes 33% off gaming monitor upgrade",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/samsungs-gorgeous-49-inch-odyssey-oled-g9-hits-a-new-all-time-low-price-of-usd854-amazon-black-friday-deal-slashes-33-percent-off-gaming-monitor-upgrade",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-21T08:02:41+00:00",
    "summary": "Now's your chance to own a massive 49-inch ultrawide QD-OLED gaming monitor now that it's hit a new all-time low price on Amazon for Black Friday."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/south-korea-busts-54-students-cheating-on-national-college-admission-exam-by-deploying-emergency-disaster-alert-during-test-ai-micro-cameras-and-phones-drive-cheating-epidemic-that-forced-government-crackdown",
    "domain": "AI 算力 / 半导体",
    "title": "South Korea busts 54 students cheating on national college admission exam by deploying emergency disaster alert during test",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/south-korea-busts-54-students-cheating-on-national-college-admission-exam-by-deploying-emergency-disaster-alert-during-test-ai-micro-cameras-and-phones-drive-cheating-epidemic-that-forced-government-crackdown",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T21:00:00+00:00",
    "summary": "The South Korean government used extra measures to prevent cheating in its national college admission exams, due to a confession from a tax accountant exam top scorer admitting to AI-assisted cheating"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-usd2-400-on-a-tricked-out-corsair-rtx-5090-prebuilt-in-black-friday-run-up-sale-sweet-spec-list-also-includes-9950x3d-64gb-ram-and-4tb-storage",
    "domain": "AI 算力 / 半导体",
    "title": "Save $2,400 on a tricked-out Corsair RTX 5090 prebuilt gaming PC in Black Friday run-up sale — sweet spec list also includes 9950X3D, 64GB RAM, and 4TB storage",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-usd2-400-on-a-tricked-out-corsair-rtx-5090-prebuilt-in-black-friday-run-up-sale-sweet-spec-list-also-includes-9950x3d-64gb-ram-and-4tb-storage",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T20:09:47+00:00",
    "summary": "Prices for RTX 5090 prebuilt PCs have spiked above five figures almost everywhere, but you can still get this Corsair Millennium system for $8999.99, or $2400 off, ahead of the Black Friday rush."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-mathematician-claims-to-have-solved-167-year-old-math-problem-with-claude-riemann-hypothesis-proof-allegedly-discovered-but-remains-unconfirmed",
    "domain": "AI 算力 / 半导体",
    "title": "Anthropic mathematician claims to have solved 167-year-old math problem with Claude",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-mathematician-claims-to-have-solved-167-year-old-math-problem-with-claude-riemann-hypothesis-proof-allegedly-discovered-but-remains-unconfirmed",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T16:30:08+00:00",
    "summary": "An anthropic mathematician claims to have solved the Riemann hypothesis using Claude."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/vast-data-says-petabyte-ssds-will-outgrow-raid-in-todays-parallel-file-systems-simulation-of-a-900-pb-system-puts-data-loss-odds-at-1-in-11-over-10-years",
    "domain": "AI 算力 / 半导体",
    "title": "VAST says petabyte SSDs will outgrow today’s parallel file system RAID",
    "url": "https://www.tomshardware.com/pc-components/ssds/vast-data-says-petabyte-ssds-will-outgrow-raid-in-todays-parallel-file-systems-simulation-of-a-900-pb-system-puts-data-loss-odds-at-1-in-11-over-10-years",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T15:00:00+00:00",
    "summary": "VAST Data’s Glenn Lockwood told SC26 that petabyte SSDs need global declustering plus extra parity to avoid data loss."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/get-32gb-of-ddr5-ram-for-usd111-in-this-premium-am5-gaming-bundle-from-newegg-4-item-combo-includes-9950x3d-32gb-v-color-ddr5-ram-asus-rog-strix-x870e-e-gaming-motherboard-and-2tb-samsung-990-pro-ssd-for-only-usd1-549",
    "domain": "AI 算力 / 半导体",
    "title": "Get 32GB of DDR5 RAM for $111 in this premium AM5 gaming bundle from Newegg",
    "url": "https://www.tomshardware.com/pc-components/get-32gb-of-ddr5-ram-for-usd111-in-this-premium-am5-gaming-bundle-from-newegg-4-item-combo-includes-9950x3d-32gb-v-color-ddr5-ram-asus-rog-strix-x870e-e-gaming-motherboard-and-2tb-samsung-990-pro-ssd-for-only-usd1-549",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T14:30:06+00:00",
    "summary": "Newegg’s freshest Black Friday combo deal takes $369 off four premium PC components, including the Ryzen 9 9950X3D, 32GB DDR5-6000 RAM, Asus ROG Strix X870E-E motherboard, 2TB Samsung SSD, and a free "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/phison-details-ssd-with-a-built-in-npu-and-64gb-of-memory-that-supports-pytorch-and-llama-cpp-running-on-the-drive-second-design-merges-fast-pslc-cache-and-qlc-capacity-behind-one-controller",
    "domain": "AI 算力 / 半导体",
    "title": "Phison details SSD with a built-in NPU and 64GB of memory that supports AI frameworks on the drive",
    "url": "https://www.tomshardware.com/pc-components/ssds/phison-details-ssd-with-a-built-in-npu-and-64gb-of-memory-that-supports-pytorch-and-llama-cpp-running-on-the-drive-second-design-merges-fast-pslc-cache-and-qlc-capacity-behind-one-controller",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T14:00:00+00:00",
    "summary": "Phison showed a computational-storage SSD with an NPU and 64GB of memory, plus Mixed Media pSLC and QLC drives, at SC26."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/thousands-of-vulnerable-fridges-patched-against-cyberattacks-in-secret-operation-uk-takes-action-following-hacks-that-destroyed-food-supplies-with-50-degree-defrosting-hijack",
    "domain": "AI 算力 / 半导体",
    "title": "Thousands of vulnerable fridges patched against cyberattacks in secret operation",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/thousands-of-vulnerable-fridges-patched-against-cyberattacks-in-secret-operation-uk-takes-action-following-hacks-that-destroyed-food-supplies-with-50-degree-defrosting-hijack",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T13:30:00+00:00",
    "summary": "Following devastating hacks that caused European fridges to reach 50 degrees Celsius, destroying food stocks, the U.K. has implemented nationwide patching to ensure similar attacks won't affect its fr"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/policy/jensen-huang-question-gets-reporter-ejected-from-trump-xi-putin-summit-journalist-asked-us-president-if-former-nvidia-ceo-had-been-disloyal-to-the-united-states",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang question gets reporter ejected from Trump-Xi-Putin summit",
    "url": "https://www.tomshardware.com/tech-industry/policy/jensen-huang-question-gets-reporter-ejected-from-trump-xi-putin-summit-journalist-asked-us-president-if-former-nvidia-ceo-had-been-disloyal-to-the-united-states",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T13:00:00+00:00",
    "summary": "Annmarie Hordern, Bloomberg's chief political correspondent and co-host of its leading program, was barred from the historic trilateral meeting between the leaders of Russia, China, and the U.S. after"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/lawyers-usd9-450-private-ai-server-of-12-used-nvidia-v100s-now-runs-every-deepseek-v4-1-flash-expert-at-4-bit-nvfp4-up-to-184-tokens-per-second-on-code-and-long-documents-start-answering-in-about-half-the-time",
    "domain": "AI 算力 / 半导体",
    "title": "Lawyer’s $9,450 private AI server with 12 used Nvidia V100s now runs every DeepSeek V4.1 Flash expert",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/lawyers-usd9-450-private-ai-server-of-12-used-nvidia-v100s-now-runs-every-deepseek-v4-1-flash-expert-at-4-bit-nvfp4-up-to-184-tokens-per-second-on-code-and-long-documents-start-answering-in-about-half-the-time",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T12:30:00+00:00",
    "summary": "A lawyer’s private AI server now runs DeepSeek V4.1 Flash on 12 used Nvidia V100 GPUs, with every expert at 4-bit NVFP4."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/mini-pcs/msi-edgemesa-n-ai-plus-review",
    "domain": "AI 算力 / 半导体",
    "title": "MSI EdgeMesa N AI+ review: RTX Spark power comes to Windows on Arm desktops, but there are trade-offs",
    "url": "https://www.tomshardware.com/desktops/mini-pcs/msi-edgemesa-n-ai-plus-review",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T12:00:00+00:00",
    "summary": "MSI's EdgeMesa N AI+ brings Nvidia RTX Spark N1X power to a Windows-on-Arm mini PC with 128GB of unified memory, strong local AI performance, and the ability to game on the side. But its high $7,499 p"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/amazon-lists-the-asus-rog-strix-g16-at-a-new-all-time-low-price-of-usd1-179-rtx-5060-powered-gaming-laptop-comes-with-16gb-of-ddr5-ram-and-a-1tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon lists the Asus ROG Strix G16 at a new all-time low price of $1,179",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/amazon-lists-the-asus-rog-strix-g16-at-a-new-all-time-low-price-of-usd1-179-rtx-5060-powered-gaming-laptop-comes-with-16gb-of-ddr5-ram-and-a-1tb-ssd",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T11:45:00+00:00",
    "summary": "Pick up a new gaming laptop for less with $575 off the Asus ROG G16 at Amazon."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/supercomputers/power-and-cooling-limits-push-100-000-accelerator-ai-clusters-past-single-data-centers-google-cisco-and-marvell-target-scale-across-networking-across-regions",
    "domain": "AI 算力 / 半导体",
    "title": "Power and cooling limits force AI clusters with 100,000+ accelerators to use multiple data centers",
    "url": "https://www.tomshardware.com/tech-industry/supercomputers/power-and-cooling-limits-push-100-000-accelerator-ai-clusters-past-single-data-centers-google-cisco-and-marvell-target-scale-across-networking-across-regions",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T11:30:00+00:00",
    "summary": "Faster GPUs are no longer enough as power constraints, network congestion, and communication overhead force the industry to rethink how massive AI systems are built."
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
    "id": "hn:50552424",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Neon",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/",
    "source": "yigitdemirag",
    "platform": "hackernews",
    "points": 1055,
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
    "points": 575,
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
    "points": 370,
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
    "id": "hn:50577901",
    "domain": "大厂 AI 动态",
    "title": "Google workers tell their employer not to punish schools that don't want AI",
    "url": "https://www.motherjones.com/politics/2026/11/google-alphabet-union-school-ai-protest-gemini-workers-petition/",
    "source": "cdrnsf",
    "platform": "hackernews",
    "points": 276,
    "published_at": "2026-11-20T16:59:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:50550415",
    "domain": "大厂 AI 动态",
    "title": "Genie 4 is now available",
    "url": "https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/",
    "source": "leumon",
    "platform": "hackernews",
    "points": 292,
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
    "points": 284,
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
    "id": "hn:50554374",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Neon looks like an Opus 5.5 competitor",
    "url": "https://micjm.com/blog/gemini-4-neon-looks-like-a-top-model/",
    "source": "seizethecheese",
    "platform": "hackernews",
    "points": 255,
    "published_at": "2026-11-19T00:29:45+00:00",
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
    "id": "hn:50569519",
    "domain": "大厂 AI 动态",
    "title": "What Comes After AGI?",
    "url": "https://institute.deepmind.com/essays/what-comes-after-agi/",
    "source": "jdkee",
    "platform": "hackernews",
    "points": 167,
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
    "points": 123,
    "published_at": "2026-11-19T09:28:56+00:00",
    "summary": ""
  },
  {
    "id": "hn:50582629",
    "domain": "大厂 AI 动态",
    "title": "A few hours ago Google DeepMind created a math horizon repo",
    "url": "https://github.com/google-deepmind/math-horizon",
    "source": "RubenLtke",
    "platform": "hackernews",
    "points": 44,
    "published_at": "2026-11-20T21:42:21+00:00",
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
    "id": "rss:https://www.theverge.com/streaming/1039096/youtube-social-media-addiction-school-districts-settlement",
    "domain": "大厂 AI 动态",
    "title": "YouTube is reportedly preparing to settle social media addiction claims for $3 billion",
    "url": "https://www.theverge.com/streaming/1039096/youtube-social-media-addiction-school-districts-settlement",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T20:43:52+00:00",
    "summary": "YouTube is preparing to pay $3 billion to thousands of school districts to settle claims that its \"addictive design\" harmed kids, according to Bloomberg. Sources tell the publication that YouTube reac"
  },
  {
    "id": "rss:https://www.theverge.com/games/1036279/gta-vi-sales",
    "domain": "大厂 AI 动态",
    "title": "Rockstar says GTA VI made $3.79 billion in its first day",
    "url": "https://www.theverge.com/games/1036279/gta-vi-sales",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T19:35:06+00:00",
    "summary": "GTA VI earned $3.79 billion in its first day of sales, which set \"a new record for entertainment across any medium,\" according to an announcement from Rockstar Games. The game also sold 32.5 million p"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1037933/eufy-omni-c28-robot-vacuum-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Eufy’s Omni C28 is 53 percent off ahead of Black Friday",
    "url": "https://www.theverge.com/gadgets/1037933/eufy-omni-c28-robot-vacuum-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T19:15:00+00:00",
    "summary": "Hosting Thanksgiving can be fun, but cleaning up afterwards? Not so much. Eufy&#8217;s Omni C28 robot vacuum / mop hybrid can help, and thanks to an early Black Friday deal, you can pick it up at a ne"
  },
  {
    "id": "rss:https://www.theverge.com/policy/1038892/trump-foreign-data-centers-tax",
    "domain": "大厂 AI 动态",
    "title": "Trump threatens ‘tremendous tax’ for moving AI data centers outside the US",
    "url": "https://www.theverge.com/policy/1038892/trump-foreign-data-centers-tax",
    "source": "Lauren Feiner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T18:50:19+00:00",
    "summary": "President Donald Trump promised to put a \"tremendous tax\" on companies that build data centers outside of the US, even as states and cities around the country are placing restrictions on new applicati"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1037749/microsd-express-card-nintendo-switch-2-black-friday-2026-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Multiplying your Switch 2’s storage costs less than usual right now",
    "url": "https://www.theverge.com/gadgets/1037749/microsd-express-card-nintendo-switch-2-black-friday-2026-deal-sale",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T18:15:00+00:00",
    "summary": "Expanding your Nintendo Switch 2’s 256GB of built-in storage with a microSD card is pricier than it was with Nintendo’s original console. That’s because microSD Express cards, while physically identic"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1038834/google-assistant-smart-speakers-nest-app-killed-shut-down",
    "domain": "大厂 AI 动态",
    "title": "Google says it’s going to shut off Google Assistant on smart speakers next year",
    "url": "https://www.theverge.com/tech/1038834/google-assistant-smart-speakers-nest-app-killed-shut-down",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T18:00:00+00:00",
    "summary": "Google is announcing some significant changes to its smart home software. Starting next year, the company will shut down the Nest app in favor of the Google Home app and retire Google Assistant on its"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1035460/best-early-black-friday-apple-deals-2026",
    "domain": "大厂 AI 动态",
    "title": "Here are the Apple deals actually worth picking up ahead of Black Friday",
    "url": "https://www.theverge.com/gadgets/1035460/best-early-black-friday-apple-deals-2026",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T17:33:59+00:00",
    "summary": "A new pair of AirPods or the latest Apple Watch can make a great holiday gift, but they can also take a pretty big dent out of your budget. That’s especially true this year, as rising hardware prices "
  },
  {
    "id": "rss:https://www.theverge.com/tech/1038692/teenage-engineering-ep-bc-1-cd-compact-disc-player-broadcast-series-bluetooth",
    "domain": "大厂 AI 动态",
    "title": "Teenage Engineering’s first CD player puts the spinning disc on display",
    "url": "https://www.theverge.com/tech/1038692/teenage-engineering-ep-bc-1-cd-compact-disc-player-broadcast-series-bluetooth",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T17:05:52+00:00",
    "summary": "Teenage Engineering announced what it describes as \"a modern take on a classic CD player\" with its new EP/BC-1 featuring a slab-like design that leaves the spinning disc exposed instead of hiding it u"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1010051/anthropic-riemann-hypothesis-millennium-prize-problem",
    "domain": "大厂 AI 动态",
    "title": "Anthropic mathematician claims to have solved prestigious Millennium Prize problem with Claude",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1010051/anthropic-riemann-hypothesis-millennium-prize-problem",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T16:34:13+00:00",
    "summary": "Anthropic mathematician Levent Alp&#246;ge claims he has proved the Riemann hypothesis, one of mathematics's most notoriously difficult problems, with the help of Claude, cracking a puzzle that has el"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/1038444/boys-noize-7llvsion-interview",
    "domain": "大厂 AI 动态",
    "title": "Boys Noize turns to the club (and an obscure Italian synth) for inspiration on 7LLVSION",
    "url": "https://www.theverge.com/entertainment/1038444/boys-noize-7llvsion-interview",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T16:22:15+00:00",
    "summary": "If you're wondering how Alex Ridha's (aka Boys Noize) collaboration with Nine Inch Nails influenced his new record 7LLVSION, the answer is simple: It didn't. That's not to say Ridha didn't learn anyth"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/20/startup-sues-apple-in-india-over-tap-to-share-contacts-feature/",
    "domain": "大厂 AI 动态",
    "title": "Startup sues Apple in India over tap-to-share contacts feature",
    "url": "https://techcrunch.com/2026/11/20/startup-sues-apple-in-india-over-tap-to-share-contacts-feature/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-21T04:00:00+00:00",
    "summary": "A U.S. startup is seeking $162 million in damages and an injunction to impact iPhone and Apple Watch imports to India."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/20/experts-warn-nearly-everyone-in-ai-is-susceptible-to-a-honey-trap-scheme-right-now/",
    "domain": "大厂 AI 动态",
    "title": "Experts warn: Nearly everyone in AI is susceptible to a honey-trap scheme right now",
    "url": "https://techcrunch.com/2026/11/20/experts-warn-nearly-everyone-in-ai-is-susceptible-to-a-honey-trap-scheme-right-now/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T20:58:29+00:00",
    "summary": "Techies are building technology that can advance all aspects of the world — but can they protect their hearts? That's the vulnerability that honey pots exploit."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/20/daniel-ek-backs-ai-researchers-fusion-power-startup-heres-what-theyre-building/",
    "domain": "大厂 AI 动态",
    "title": "Daniel Ek backs AI researcher’s fusion power startup. Here’s what they’re building.",
    "url": "https://techcrunch.com/2026/11/20/daniel-ek-backs-ai-researchers-fusion-power-startup-heres-what-theyre-building/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T19:53:41+00:00",
    "summary": "Spotify founder Daniel Ek is backing Europa Fusion, a fusion power startup founded by an AI researcher. Here's what the startup is building."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/20/ai-claimed-a-solution-to-the-167-year-old-riemann-hypothesis-and-a-human-did-too/",
    "domain": "大厂 AI 动态",
    "title": "AI claimed a solution to the 167-year-old Riemann hypothesis — and a human did, too",
    "url": "https://techcrunch.com/2026/11/20/ai-claimed-a-solution-to-the-167-year-old-riemann-hypothesis-and-a-human-did-too/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T19:32:08+00:00",
    "summary": "Mathematicians are having their minds blown by the latest AI-driven result — and there's a competing human solution, too."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/20/super-hot-rock-geothermal-could-end-data-center-energy-woes/",
    "domain": "大厂 AI 动态",
    "title": "Super-hot rock geothermal could end data center energy woes",
    "url": "https://techcrunch.com/2026/11/20/super-hot-rock-geothermal-could-end-data-center-energy-woes/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T18:34:00+00:00",
    "summary": "New geothermal startups are betting that they can leapfrog today's leaders to deliver terawatts of electricity nearly anywhere."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/20/chips-can-survive-the-space-environment-can-their-financing/",
    "domain": "大厂 AI 动态",
    "title": "Chips can survive the space environment — can their financing?",
    "url": "https://techcrunch.com/2026/11/20/chips-can-survive-the-space-environment-can-their-financing/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T17:40:01+00:00",
    "summary": "Lenders don't want SpaceX shooting their collateral into orbit. What does that mean for space data centers writ large?"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/20/bending-spoons-buys-mailchimp-for-3-68-billion/",
    "domain": "大厂 AI 动态",
    "title": "Bending Spoons buys Mailchimp for $3.68B",
    "url": "https://techcrunch.com/2026/11/20/bending-spoons-buys-mailchimp-for-3-68-billion/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T16:16:06+00:00",
    "summary": "Intuit acquired the company in 2021 for roughly $12 billion, so it looks like Bending Spoons is getting quite a bargain."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/20/a-transcription-firm-used-by-police-prosecutors-and-tech-giants-exposed-customer-data-online/",
    "domain": "大厂 AI 动态",
    "title": "A transcription firm used by police, prosecutors, and tech giants exposed customer data online",
    "url": "https://techcrunch.com/2026/11/20/a-transcription-firm-used-by-police-prosecutors-and-tech-giants-exposed-customer-data-online/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T15:46:07+00:00",
    "summary": "Exclusive: A simple security lapse exposed transcriptions of police interviews and bodycam footage on a cloud server without a password."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/20/6-ai-powered-gadgets-that-could-make-your-home-office-smarter/",
    "domain": "大厂 AI 动态",
    "title": "Six AI-powered gadgets that could make your home office smarter",
    "url": "https://techcrunch.com/2026/11/20/6-ai-powered-gadgets-that-could-make-your-home-office-smarter/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T14:00:00+00:00",
    "summary": "From notetakers to webcams, here are six AI-powered gadgets to upgrade your workspace."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/20/behind-jensen-huangs-exit-questions-about-a-management-style-reportedly-built-on-fear/",
    "domain": "大厂 AI 动态",
    "title": "Behind Jensen Huang’s exit, questions about a management style reportedly built on fear",
    "url": "https://techcrunch.com/2026/11/20/behind-jensen-huangs-exit-questions-about-a-management-style-reportedly-built-on-fear/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T13:25:00+00:00",
    "summary": "Elon Musk may have been overstating it when he said Nvidia’s employees “love” the ousted Jensen Huang."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/20/california-ag-subpoenas-nvidia-over-worries-about-huangs-ties-with-china/",
    "domain": "大厂 AI 动态",
    "title": "California AG subpoenas Nvidia over worries about Huang’s ties with China",
    "url": "https://techcrunch.com/2026/11/20/california-ag-subpoenas-nvidia-over-worries-about-huangs-ties-with-china/",
    "source": "Ram Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-20T13:21:11+00:00",
    "summary": "\"The conduct of Nvidia and its former CEO raises bright red flags, including about the ways in which the company may have misled investors,\" California AG Rob Bonta said."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/20/the-u-s-national-cyber-director-is-stepping-down/",
    "domain": "大厂 AI 动态",
    "title": "The US national cyber director is stepping down",
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
    "id": "hn:50556287",
    "domain": "股票",
    "title": "Ruby2ßhell: Pre-authentication RCE on stock Rails",
    "url": "https://verialabs.com/ruby2shell/",
    "source": "jdns",
    "platform": "hackernews",
    "points": 403,
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
    "id": "hn:50583254",
    "domain": "股票",
    "title": "Nasdaq erases all 2026 gains",
    "url": "https://www.cnbc.com/2026/11/19/stock-market-today-live-updates.html",
    "source": "mv4",
    "platform": "hackernews",
    "points": 131,
    "published_at": "2026-11-20T22:29:06+00:00",
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
    "points": 129,
    "published_at": "2026-11-15T19:46:02+00:00",
    "summary": ""
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
    "id": "hn:50542361",
    "domain": "股票",
    "title": "Interesting Learnings Working for a Startup",
    "url": "https://news.ycombinator.com/item?id=50542361",
    "source": "Jessiejia11",
    "platform": "hackernews",
    "points": 21,
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
    "points": 195,
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
    "id": "hn:50525658",
    "domain": "金融",
    "title": "Pentagon fails ninth straight audit despite progress in organizing finances",
    "url": "https://www.reuters.com/business/aerospace-defense/pentagon-fails-ninth-straight-audit-despite-progress-organizing-finances-2026-11-16/",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 151,
    "published_at": "2026-11-17T00:23:21+00:00",
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
    "id": "hn:50236506",
    "domain": "金融",
    "title": "F45 (Fedora 45) Final Is No-Go",
    "url": "https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/EWDOYT6TOMFY4XPL5MJC2QWCDJBOR6MU/",
    "source": "gnabgib",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-10-25T22:09:09+00:00",
    "summary": ""
  }
]
```
