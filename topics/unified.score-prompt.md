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

- 今日日期：`2026-11-16`
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
  "date": "2026-11-16",
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
    "id": "bvid:BV1REx46NEc4",
    "domain": "AI",
    "title": "【全网最全】DeepSeek Harness超详细教程！50分钟吃透DSH，让SuperAgent给你干活！",
    "url": "http://www.bilibili.com/video/av117540671982699",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 2857621,
    "published_at": "2026-11-01T10:22:02+00:00",
    "summary": "DeepSeek Harness超详细教程！\n大家可以速速收藏啦~\n耗时60天制作！感谢大家的三联\n未来还会出其他AI教程，大家可以关注一下~"
  },
  {
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "8分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 2125743,
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
    "points": 1522923,
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
    "points": 1496756,
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
    "points": 1467442,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1yorUYWEGD",
    "domain": "AI",
    "title": "普通人也可以看的 AI 编程指南 | Cursor 教程｜Cursor 使用技巧和思路｜如何免费使用 Cursor｜AI 编程",
    "url": "http://www.bilibili.com/video/av113786467981446",
    "source": "不正经的前端啊",
    "platform": "bilibili",
    "points": 948042,
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
    "points": 914062,
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
    "points": 902246,
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
    "points": 755238,
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
    "points": 675640,
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
    "points": 596690,
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
    "points": 434457,
    "published_at": "2026-05-02T06:51:59+00:00",
    "summary": "全B站最详细的Hermes Agent教程，从部署到玩转！零基础，小白也能轻松玩转Hermes Agent，真正的AI助手，恐怖如斯！"
  },
  {
    "id": "bvid:BV1AnQNYxEsy",
    "domain": "AI",
    "title": "MCP是啥？技术原理是什么？一个视频搞懂MCP的一切。Windows系统配置MCP，Cursor Cline使用MCP",
    "url": "http://www.bilibili.com/video/av114155298228756",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 428228,
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
    "points": 357079,
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
    "points": 327853,
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
    "points": 299499,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1qGc7zwEX6",
    "domain": "AI",
    "title": "史上最强 AI 编程工具Cursor来啦！Cursor保姆级使用教程！新手友好！看到就是赚到！！！",
    "url": "http://www.bilibili.com/video/av116061928226926",
    "source": "知名的阿呆同学",
    "platform": "bilibili",
    "points": 289219,
    "published_at": "2026-02-19T07:34:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1e3t4etExj",
    "domain": "AI",
    "title": "手摸手的AI编程cursor实战【小白教程】",
    "url": "http://www.bilibili.com/video/av113148447169565",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 239816,
    "published_at": "2024-09-17T01:00:00+00:00",
    "summary": "喜欢的朋友可以三连+关注～这对我真的很重要"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 234466,
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
    "points": 186904,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1bNSCYAE7p",
    "domain": "AI",
    "title": "Cursor新手入门教程01：基础设置与配置｜设为中文、适合新手的Rules for AI、Feature配置等",
    "url": "http://www.bilibili.com/video/av113416781959475",
    "source": "花叔v",
    "platform": "bilibili",
    "points": 185881,
    "published_at": "2024-11-03T03:06:28+00:00",
    "summary": "本期视频主要介绍了Cursor编辑器的基础设置和配置，适合新手入门观看。\n\n视频主要内容包括:\n- Cursor的下载安装\n- 中文插件的安装配置 \n- Rules for AI的设置\n- Model和Features的配置\n- 一个简单的图片压缩网站示例\n\n时间戳:\n00:28 Cursor下载安装\n00:58 Cursor界面介绍\n01:40 中文插件安装配置\n04:58 Account登录设"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 166036,
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
    "points": 163481,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1csJC6yEQx",
    "domain": "AI",
    "title": "哪里能用上OPUS5.5？性价比如何？从夯到拉盘点",
    "url": "http://www.bilibili.com/video/av117443095759250",
    "source": "能工智人永不为奴",
    "platform": "bilibili",
    "points": 152300,
    "published_at": "2026-10-15T04:46:25+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1JY4w6kEAe",
    "domain": "AI",
    "title": "【全网首发】Claude防封号独家指南！前后花了5万元！小白保姆级教程【包含对话铺垫/IP DNS/订阅方式/历史记录清除】",
    "url": "http://www.bilibili.com/video/av117546107800312",
    "source": "Gemini3-",
    "platform": "bilibili",
    "points": 119415,
    "published_at": "2026-11-02T09:26:34+00:00",
    "summary": "视频内已经将所有的网站进行打码，没有吐露任何网址，也没有推广违规AI服务\n简介无推广内容\n视频中演示网站有正规ICP备案与ICP许可"
  },
  {
    "id": "bvid:BV1VL3F6pE9K",
    "domain": "AI",
    "title": "0基础入门智能体agent测试：AI测试基础+AI智能体(Agent)测试从零入门全攻略，2026最新版！",
    "url": "http://www.bilibili.com/video/av116991151113881",
    "source": "黑马测试",
    "platform": "bilibili",
    "points": 113251,
    "published_at": "2026-07-27T09:19:37+00:00",
    "summary": "还在卷传统软件测试？2026年必学的AI智能体(Agent)测试来了！本期视频专为0基础小白打造，从软件测试基础讲起...若要本视频配套资源笔记可加up主企微（请看置顶留言最后一句话）。"
  },
  {
    "id": "bvid:BV1h3W76wEem",
    "domain": "AI",
    "title": "Claude(Code)桌面APP，保姆级全攻略，一期视频精通，顶级Agent软件长什么样？",
    "url": "http://www.bilibili.com/video/av117580048108571",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 111062,
    "published_at": "2026-11-08T09:14:07+00:00",
    "summary": "最近Claude桌面端（Claude Desktop） 有了一大波功能更新。随着一步步的迭代，它已经把 Claude Code 的编程、Claude Design 的设计，以及 Claude Cowork 的办公等核心能力，全部收入了同一个桌面客户端，特别是Claude Code已经从原本黑乎乎的命令行工具，进化成了桌面客户端的完全体形态。再搭配上超强的Opus5.5 模型，已经能称得上是地表顶级"
  },
  {
    "id": "bvid:BV1hsKzzcEkz",
    "domain": "AI",
    "title": "十分钟Cursor教程！关于Cursor你可能不知道的事",
    "url": "http://www.bilibili.com/video/av114756006448971",
    "source": "GeekHour",
    "platform": "bilibili",
    "points": 82698,
    "published_at": "2025-06-28T10:12:00+00:00",
    "summary": "十分钟Cursor教程，视频中的资料可以关注同名gzh后下载！"
  },
  {
    "id": "bvid:BV1UJ2HYaEhw",
    "domain": "AI",
    "title": "cursor 小白使用教程",
    "url": "http://www.bilibili.com/video/av113272145582089",
    "source": "AI_Julie",
    "platform": "bilibili",
    "points": 77224,
    "published_at": "2024-10-08T14:02:28+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV143wwz6E8F",
    "domain": "AI",
    "title": "Claude code科研使用展示与思路分享（提速就靠Ai）",
    "url": "http://www.bilibili.com/video/av116211882920985",
    "source": "科研推土机",
    "platform": "bilibili",
    "points": 77015,
    "published_at": "2026-03-11T18:12:00+00:00",
    "summary": "本期给大家带来的是Claude在Vscode的科研应用演示与我最近的一些心得使用心得，科研速度嘎嘎提升。论文复现画图、数据分析就靠Claude code。这个课程也是科研推土机「系统管理文献课程2.0」学员催我更新的内容，希望能帮助到大家～，这个视频重点讲两个事情：\n1️⃣ 资料获取，free不用怀疑，我是良心可言博主，，关注我(GZTSHNR)～\n2️⃣ 展示如何在VS code实操应用clau"
  },
  {
    "id": "bvid:BV1KocTzHE3Z",
    "domain": "AI",
    "title": "2027版 Cursor+Claude AI编程 1天快速上手 视频教程",
    "url": "http://www.bilibili.com/video/av116040285622077",
    "source": "java1234官方",
    "platform": "bilibili",
    "points": 69821,
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
    "points": 66036,
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
    "points": 61259,
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
    "points": 56969,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV17Lap6VEUr",
    "domain": "AI",
    "title": "【全80集】Vibe Coding 零基础入门到实战教程，由浅入深（全程干货）",
    "url": "http://www.bilibili.com/video/av117353572468721",
    "source": "数据拾光屋",
    "platform": "bilibili",
    "points": 55555,
    "published_at": "2026-10-02T09:25:00+00:00",
    "summary": "本套教程专门为零基础学员而制，全程干货无废话，喜欢的小伙伴记得点赞三连喔 ~"
  },
  {
    "id": "bvid:BV1cVW86JE2e",
    "domain": "AI",
    "title": "Vibe Coding 完不会获客？我用 AI 做了一个「营销数据库」！【B站AI创造公开赛】",
    "url": "http://www.bilibili.com/video/av117587245599812",
    "source": "熠辉IndieDev",
    "platform": "bilibili",
    "points": 52855,
    "published_at": "2026-11-10T01:00:00+00:00",
    "summary": "产品做出来了，第一批用户去哪找？我用两个月做了 BizPeel，收录700多个公开营收的产品，拆解真实获客动作。本期演示在 Google Antigravity 接入 BizPeel MCP，由 Gemini 4 Argon 查找同类产品、整理增长实验；报告生成时用 Gemini Flash 清洗数据，再由 Gemini 4 Argon 撰写。\n\n注： 部分Google技术仅适用于出海场景。"
  },
  {
    "id": "bvid:BV1uVSUBkEfZ",
    "domain": "AI",
    "title": "Microsoft Copilot完整教程(上) 从入门到Agent 一站式掌握AI办公",
    "url": "http://www.bilibili.com/video/av116351721084069",
    "source": "星小脉",
    "platform": "bilibili",
    "points": 45823,
    "published_at": "2026-04-05T11:00:20+00:00",
    "summary": "2026年最全面的Microsoft Copilot教程上半部分。从Copilot首页入门到Agent深度解析，涵盖搜索、资料库、AI视频生成、Copilot Pages、PowerPoint智能幻灯片等全部功能。由培训了6万人的AI顾问Cherie Brock与Sabrina Ramonov联合讲解。"
  },
  {
    "id": "bvid:BV1VQWb6eEeo",
    "domain": "AI",
    "title": "全网最详细的 AI 入门课：一期视频搞懂 58 个 AI 术语，从大模型到 Agent、MCP、Skill",
    "url": "http://www.bilibili.com/video/av117587144940374",
    "source": "亚里今天也要AI",
    "platform": "bilibili",
    "points": 44305,
    "published_at": "2026-11-09T15:20:10+00:00",
    "summary": "这可能是你看过的，最详细的 AI 入门课。\n一期视频，带你搞懂 AI 里最常见的 58 个概念和名词：从最基础的大模型、Token，到现在最火的 Agent、MCP、Skill，每一个都讲清楚它是什么、怎么工作，和其他概念有什么区别。\n五个部分循序渐进，最后用学到的词，一句一句读懂一页真的模型更新日志。\n\n00:00 开场\n00:27 课程路线：五个部分\n【第一部分 AI 和大模型是什么】\n00:"
  },
  {
    "id": "bvid:BV1hxMbzqEzU",
    "domain": "AI",
    "title": "小智MCP自由了！我开源了个命令行神器实现多MCP聚合",
    "url": "http://www.bilibili.com/video/av114686414625640",
    "source": "闪电蘑菇",
    "platform": "bilibili",
    "points": 43541,
    "published_at": "2025-06-15T08:31:55+00:00",
    "summary": "- 我写的小智客户端命令行工具\n - github: https://github.com/shenjingnan/xiaozhi-client\n - gitee: https://gitee.com/shenjingnan/xiaozhi-client\n\n- 小智官方MCP示例代码仓库：\n - github: https://github.com/78/mcp-calculator\n - git"
  },
  {
    "id": "bvid:BV1hmb26ZEws",
    "domain": "AI",
    "title": "DeepSeek Harness 实测  Claude Code 对比后，梁神我错了 差距比我想的大",
    "url": "http://www.bilibili.com/video/av117100337236191",
    "source": "程序员晓刘",
    "platform": "bilibili",
    "points": 40402,
    "published_at": "2026-08-15T16:01:38+00:00",
    "summary": "这期用同一个 DeepSeek Pro 0813 模型，分别在 Claude Code 和 DeepSeek Harness 里完成同样的任务，对比工具链对最终效果的影响。\n实测内容包括：\nFPS 游戏 Demo、灯塔预警沙盘、手枪组装动画、显示器组装动画，以及 DeepSeek Harness 的插件化源码流程。\n整体看下来，模型本身当然重要，但 Harness 在插件化、流程记录、缓存命中和任"
  },
  {
    "id": "bvid:BV1zXAuzUEWt",
    "domain": "AI",
    "title": "【2026最新版】目前B站最全最细的 Cursor+Skills实战指南教程，手把手带你开发爆款app，全程干货无废话！Agent Skills教程｜AI 编程",
    "url": "http://www.bilibili.com/video/av116272180238922",
    "source": "大模型碎碎念",
    "platform": "bilibili",
    "points": 38414,
    "published_at": "2026-03-22T09:52:46+00:00",
    "summary": "制作不易，麻烦各位观众老爷一键三连呀【点赞、投币、收藏】感谢支持～\n‍视频配套笔记、AI大模型笔记代码：https://www.bilibili.com/read/cv43354937/?jump_opus=1"
  },
  {
    "id": "bvid:BV1gwcAzkEhw",
    "domain": "AI",
    "title": "Claude Code Agent Teams上手指南+项目实测",
    "url": "http://www.bilibili.com/video/av116037064331269",
    "source": "程序员阿江-Relakkes",
    "platform": "bilibili",
    "points": 36460,
    "published_at": "2026-02-08T23:30:00+00:00",
    "summary": "用Claude Code干复杂任务总碰到三个问题：\n\n上下文越来越长开始遗忘、任务只能串行效率低、单Agent视角单一容易漏检。\n\nClaude官方发布的Agent Teams功能正好解决这些痛点\n\n一个Team Lead拆任务，多个Teammate并行执行，还能互相通信协调。\n\n本期视频从核心概念、使用场景、底层架构到真实项目实战，带你完整搞懂Agent Teams的正确打开方式。"
  },
  {
    "id": "bvid:BV1wpxq6VEXx",
    "domain": "AI",
    "title": "【AI时代的STM32教程】AI Agent 初体验",
    "url": "http://www.bilibili.com/video/av117529699682124",
    "source": "keysking",
    "platform": "bilibili",
    "points": 35878,
    "published_at": "2026-10-30T11:52:06+00:00",
    "summary": "一句话，让 AI 帮我们完成第一个 STM32C5 程序！🚀\n本期我们一起认识 AI Agent，学习如何描述开发需求，并借助开源的 STM32C5DevSkills，让 AI 完成工程创建、芯片配置、代码编写和编译烧录，让律动小板上的小灯闪烁起来！\n也特别感谢 @意法半导体中国   对本系列教程的支持～下期我们再亲手走一遍开发流程，把 Agent 替我们完成的工作，一步步搞明白！"
  },
  {
    "id": "bvid:BV1raQXYpEsz",
    "domain": "AI",
    "title": "Cursor免费无限使用教程,几分钟省下一百多块",
    "url": "http://www.bilibili.com/video/av114167931477037",
    "source": "自由程序员八哥",
    "platform": "bilibili",
    "points": 34624,
    "published_at": "2025-03-15T18:49:37+00:00",
    "summary": "Cursor免费无限使用教程\n新链接链接：夸克网盘：链接：https://pan.quark.cn/s/6d825a22413a"
  },
  {
    "id": "bvid:BV17YPqzcES4",
    "domain": "AI",
    "title": "挑战用Cursor30分钟搭建完整小程序",
    "url": "http://www.bilibili.com/video/av116171517069277",
    "source": "前端老兵AI",
    "platform": "bilibili",
    "points": 33231,
    "published_at": "2026-03-05T12:00:00+00:00",
    "summary": "用AI写小程序，到底能有多快？ 我做了9年前端，小程序项目做了不下20个。今天我做一个实验——完全用Cursor从零搭建一个完整的待办清单 小程序，包含首页列表、新增编辑、分类筛选、本地存储，全程计时。"
  },
  {
    "id": "bvid:BV1iEWx6bETT",
    "domain": "AI",
    "title": "20分钟AI网关保姆级教程",
    "url": "http://www.bilibili.com/video/av117585249042482",
    "source": "GeekHour",
    "platform": "bilibili",
    "points": 28159,
    "published_at": "2026-11-09T10:39:59+00:00",
    "summary": "这期视频带你从零开始搭建和使用1Panel AI 网关，一个入口、一个API连接和管理所有大模型。\n\n工具地址：https://1panel.cn/ai-gateway.html"
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 27118,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 26905,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1kowRzSEi3",
    "domain": "AI",
    "title": "【2026最新版】目前B站最全最细的 CurSor AI编程零基础全套教程，手把手教你搭建高效Cursor工作流，全程干货无废话！让你少走99%的弯路！！",
    "url": "http://www.bilibili.com/video/av116244816661654",
    "source": "聚客Ai联盟",
    "platform": "bilibili",
    "points": 26073,
    "published_at": "2026-03-17T13:54:44+00:00",
    "summary": "【本视频课件笔记代码/学习大纲/全套面试真题请戳链接获取→https://www.bilibili.com/read/cv42205069/？jump_opus=1】\n制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持~"
  },
  {
    "id": "bvid:BV1i4GNzWEHP",
    "domain": "AI",
    "title": "【Cursor安装】目前最好用的AI编程软件Cursor安装教程+如何汉化",
    "url": "http://www.bilibili.com/video/av114824105302737",
    "source": "兔子喵爱编程",
    "platform": "bilibili",
    "points": 25620,
    "published_at": "2025-07-09T16:05:07+00:00",
    "summary": "有无编程基础都可以尝试一下AI编程，编程真的很简单也很有趣！！\n后面会出详细的cursor使用教程，大家可以持续追更一下"
  },
  {
    "id": "hn:50459703",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia is preparing to oust Jensen Huang",
    "url": "https://www.wsj.com/business/nvidia-is-preparing-to-oust-nvidia-ceo-jensen-huang-30f421ad",
    "source": "jbredeche",
    "platform": "hackernews",
    "points": 1226,
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
    "points": 1103,
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
    "points": 987,
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
    "points": 818,
    "published_at": "2026-11-13T02:16:24+00:00",
    "summary": ""
  },
  {
    "id": "hn:50362905",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia RTX Spark encrypted firmware slows inference speed to 35% on Linux",
    "url": "https://www.mindstudio.ai/blog/linux-nvidia-rtx-spark-laptop",
    "source": "novaRom",
    "platform": "hackernews",
    "points": 617,
    "published_at": "2026-11-04T08:46:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:50501631",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia deliberately kept GPU prices high through circular financing deals",
    "url": "https://www.techspot.com/news/114558-nvidia-deliberately-kept-gpu-prices-high-through-circular.html",
    "source": "madihaa",
    "platform": "hackernews",
    "points": 446,
    "published_at": "2026-11-14T22:26:30+00:00",
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
    "id": "hn:50487864",
    "domain": "AI 算力 / 半导体",
    "title": "$11.4M in Nvidia hardware vanishes during shipment from CA to TX",
    "url": "https://www.freightwaves.com/news/11-4-million-in-nvidia-hardware-vanishes-during-shipment-from-california-to-texas",
    "source": "crescit_eundo",
    "platform": "hackernews",
    "points": 385,
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
    "id": "hn:50512235",
    "domain": "AI 算力 / 半导体",
    "title": "What's Next for Nvidia?",
    "url": "https://steveblank.com/2026/11/15/whats-next-for-nvidia/",
    "source": "zdw",
    "platform": "hackernews",
    "points": 254,
    "published_at": "2026-11-15T23:55:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:50348962",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia – open-source auto-ontology",
    "url": "https://github.com/NVIDIA/auto-ontology",
    "source": "campervans",
    "platform": "hackernews",
    "points": 292,
    "published_at": "2026-11-03T07:04:50+00:00",
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
    "id": "hn:50511982",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang might return to Nvidia as CEO",
    "url": "https://www.reuters.com/world/china/jensen-huang-discusses-comeback-nvidia-ceo-with-allies-ft-reports-2026-11-15/",
    "source": "YakubYilmaz",
    "platform": "hackernews",
    "points": 166,
    "published_at": "2026-11-15T23:24:53+00:00",
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
    "id": "hn:50497155",
    "domain": "AI 算力 / 半导体",
    "title": "Serving GLM-5.3 at 607.8 tok/s across two Nvidia DGX stations with vLLM",
    "url": "https://developer.nvidia.com/blog/when-one-gpu-isnt-enough-serving-glm-5-3-across-two-nvidia-dgx-stations-with-vllm/",
    "source": "wondersky",
    "platform": "hackernews",
    "points": 146,
    "published_at": "2026-11-14T14:09:25+00:00",
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
    "id": "hn:50509883",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang discusses comeback as Nvidia CEO with allies",
    "url": "https://www.ft.com/content/45383d86-33c4-4d99-86e5-5e058d3567c1",
    "source": "eyalitki",
    "platform": "hackernews",
    "points": 124,
    "published_at": "2026-11-15T19:31:11+00:00",
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
    "id": "hn:50387738",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Kubernetes Engine (NVKE)",
    "url": "https://github.com/dsx-ai-factory/nvke",
    "source": "gkapur",
    "platform": "hackernews",
    "points": 124,
    "published_at": "2026-11-06T03:16:26+00:00",
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
    "id": "hn:50511763",
    "domain": "AI 算力 / 半导体",
    "title": "Huang Discusses Comeback as Nvidia Chief with Allies, FT Says",
    "url": "https://www.bloomberg.com/news/articles/2026-11-15/huang-discusses-comeback-as-nvidia-chief-with-allies-ft-says",
    "source": "nstj",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-11-15T22:53:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:50491690",
    "domain": "AI 算力 / 半导体",
    "title": "An open letter to the Nvidia Board of Directors",
    "url": "https://standwithjensen.com/",
    "source": "iLuddite",
    "platform": "hackernews",
    "points": 50,
    "published_at": "2026-11-13T23:34:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:50476257",
    "domain": "AI 算力 / 半导体",
    "title": "US Intel isn't sure if Alice Huang spied on Nvidia for China",
    "url": "https://www.cnn.com/2026/11/12/politics/alice-huang-us-intel-jensen-huang-nvidia",
    "source": "Leary",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-11-13T00:02:34+00:00",
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
    "id": "rss:https://www.eetimes.com/the-sound-of-smarter-farming/",
    "domain": "AI 算力 / 半导体",
    "title": "The Sound of Smarter Farming",
    "url": "https://www.eetimes.com/the-sound-of-smarter-farming/",
    "source": "Rebecca Pool",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-16T06:59:20+00:00",
    "summary": "From birdsong and pollinator wingbeats to the vibrations of insects feeding inside plants, acoustic sensors and AI are helping farmers monitor biodiversity, improve pollination, and detect threats to "
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/hacker-gets-doom-running-on-a-usb-flash-drives-built-in-lcd-played-by-copying-files-hacker-dumps-firmware-from-chip-with-scrubbed-markings-through-an-open-debug-port-then-gets-the-game-running-with-ai-help",
    "domain": "AI 算力 / 半导体",
    "title": "Hacker gets Doom running on a USB flash drive's built-in LCD, played by copying files",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/hacker-gets-doom-running-on-a-usb-flash-drives-built-in-lcd-played-by-copying-files-hacker-dumps-firmware-from-chip-with-scrubbed-markings-through-an-open-debug-port-then-gets-the-game-running-with-ai-help",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-16T10:30:00+00:00",
    "summary": "Aaron Christophel ported Doom to the LCD on a MOVESPEED MSSU10 flash drive and controls it with file transfers."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/operating-systems/developer-creates-a-100-percent-valid-zip-file-that-doubles-as-a-bios-bootable-operating-system-hiding-bios-boot-flags-inside-uncompressed-files-and-turning-file-headers-into-cpu-instructions",
    "domain": "AI 算力 / 半导体",
    "title": "Developer creates a 100% valid ZIP file that doubles as a BIOS-bootable operating system",
    "url": "https://www.tomshardware.com/software/operating-systems/developer-creates-a-100-percent-valid-zip-file-that-doubles-as-a-bios-bootable-operating-system-hiding-bios-boot-flags-inside-uncompressed-files-and-turning-file-headers-into-cpu-instructions",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-16T10:00:00+00:00",
    "summary": "Crafty techie concocts ZIP that's simultaneously a valid archive, BIOS-bootable, and a Multiboot image"
  },
  {
    "id": "rss:https://www.tomshardware.com/gift-guides-seasonal-sales/30-must-have-pc-tool-gifts-for-hobbyists-and-makers-essential-bench-upgrades-for-enthusiasts-with-a-project-from-electric-screwdrivers-to-cordless-air-dusters",
    "domain": "AI 算力 / 半导体",
    "title": "30 must-have PC tool gifts for hobbyists and makers",
    "url": "https://www.tomshardware.com/gift-guides-seasonal-sales/30-must-have-pc-tool-gifts-for-hobbyists-and-makers-essential-bench-upgrades-for-enthusiasts-with-a-project-from-electric-screwdrivers-to-cordless-air-dusters",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T21:00:00+00:00",
    "summary": "Whether you're a PC builder or a hobbyist with a 3D printer, you'll need tools to build, clean, repair and complete your projects. Here are some of the best ones you can pick up for a techie over this"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/robotics-engineer-leaves-nvidia-over-lack-of-transparency-around-jensen-huangs-exit-details-decision-joins-chorus-of-disgruntled-staff-as-petition-to-reinstate-former-ceo-passes-150-000-signatures",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia engineer leaves company over lack of transparency around Jensen Huang’s exit, details decision",
    "url": "https://www.tomshardware.com/tech-industry/robotics-engineer-leaves-nvidia-over-lack-of-transparency-around-jensen-huangs-exit-details-decision-joins-chorus-of-disgruntled-staff-as-petition-to-reinstate-former-ceo-passes-150-000-signatures",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T17:56:15+00:00",
    "summary": "Dai's post shows how much Nvidia employees looked up to the former CEO."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/controllers-gamepads/cockpit-simulator-737x-cdu-v2-review-an-essential-component-for-flight-sim-enthusiasts",
    "domain": "AI 算力 / 半导体",
    "title": "Cockpit-Simulator 737X CDU (v2) Review: An Essential Component for Flight Sim Enthusiasts",
    "url": "https://www.tomshardware.com/peripherals/controllers-gamepads/cockpit-simulator-737x-cdu-v2-review-an-essential-component-for-flight-sim-enthusiasts",
    "source": "Dan Mateescu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T17:30:00+00:00",
    "summary": "The CS 737X CDU (v2) by Cockpit-Simulator is a plug-and-play, 1:1 replica of a Boeing 737 Control Display Unit for home cockpit builds."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-5090-stock-returns-to-newegg-with-21-models-but-scarcity-pricing-keeps-the-cheapest-air-cooled-cards-at-least-three-times-msrp",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia RTX 5090 stock returns to Newegg with 21 models",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-5090-stock-returns-to-newegg-with-21-models-but-scarcity-pricing-keeps-the-cheapest-air-cooled-cards-at-least-three-times-msrp",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T17:00:00+00:00",
    "summary": "After rumors of Nvidia GeForce RTX 5090 graphics cards being withdrawn from the consumer retail channel it is pleasing to see major U.S. eTailers like Newegg stuffed with cheaper stock today."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/fbi-disrupts-north-korean-facestealer-campaign-behind-usd5-billion-binance-hack-doj-seizes-facestealer-cloud-infrastructure-containing-900-videos-of-tech-workers-hackers-used-ai-deepfakes-to-steal-usd400-million-and-compromise-open-source-software",
    "domain": "AI 算力 / 半导体",
    "title": "FBI disrupts North Korean FaceStealer campaign behind $5 billion Binance hack",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/fbi-disrupts-north-korean-facestealer-campaign-behind-usd5-billion-binance-hack-doj-seizes-facestealer-cloud-infrastructure-containing-900-videos-of-tech-workers-hackers-used-ai-deepfakes-to-steal-usd400-million-and-compromise-open-source-software",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T16:30:00+00:00",
    "summary": "US DoJ partially disrupts FaceStealer campaign that's taken $400m from victims and threatens open-source software — gov techs disrupt cloud infrastructure and find 900 videos of targeted tech workers"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/357-detailed-cpu-die-shots-spanning-1971-to-2024-crammed-into-a-new-gallery-motorola-68000-intel-486dx2-amd-athlon-xp-apple-m1-and-many-more-in-beautiful-detail",
    "domain": "AI 算力 / 半导体",
    "title": "357 detailed CPU die shots spanning 1971 to 2024 crammed into a new gallery",
    "url": "https://www.tomshardware.com/pc-components/cpus/357-detailed-cpu-die-shots-spanning-1971-to-2024-crammed-into-a-new-gallery-motorola-68000-intel-486dx2-amd-athlon-xp-apple-m1-and-many-more-in-beautiful-detail",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T16:00:00+00:00",
    "summary": "A CPU enthusiast has put together an eye-popping visual database containing crystal clear detailed die shots of 357 legendary, and some lesser-known, processors."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/microsoft-365-outage-leads-to-chlorine-gas-poisoning-of-15-hotel-guests-email-warning-system-fails-40-first-responders-deployed-for-triage-four-hospitalized",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft 365 outage leads to chlorine gas poisoning of 15 hotel guests",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/microsoft-365-outage-leads-to-chlorine-gas-poisoning-of-15-hotel-guests-email-warning-system-fails-40-first-responders-deployed-for-triage-four-hospitalized",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T15:41:13+00:00",
    "summary": "The 'maintenance safety system' relied on Microsoft Outlook to send warning messages to the operator."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/judge-denies-motion-to-dismiss-dram-price-fixing-lawsuit-against-micron-samsung-and-sk-hynix-says-chipmakers-acted-like-hawks-flying-in-formation-finds-evidence-of-dram-collusion-plausible-after-500-percent-price-surge",
    "domain": "AI 算力 / 半导体",
    "title": "Judge denies motion to dismiss DRAM price-fixing lawsuit against Micron, Samsung, and SK hynix, finds evidence of DRAM collusion plausible after 500% price surge",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/judge-denies-motion-to-dismiss-dram-price-fixing-lawsuit-against-micron-samsung-and-sk-hynix-says-chipmakers-acted-like-hawks-flying-in-formation-finds-evidence-of-dram-collusion-plausible-after-500-percent-price-surge",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T15:09:50+00:00",
    "summary": "The judge characterized the three companies as \"hawks flying in formation\" when it came to their business decisions."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/3d-printing-developer-creates-self-hostable-non-planar-printing-slicer-pancakeslicer-makes-non-planar-3d-printing-accessible-potentially-leading-to-rapid-community-development",
    "domain": "AI 算力 / 半导体",
    "title": "3D printing dev’s free tool unlocks curved printing along all three axes",
    "url": "https://www.tomshardware.com/3d-printing/3d-printing-developer-creates-self-hostable-non-planar-printing-slicer-pancakeslicer-makes-non-planar-3d-printing-accessible-potentially-leading-to-rapid-community-development",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T15:00:00+00:00",
    "summary": "PancakeSlicer is a self-hostable non-planar 3D printing slicer that might finally make non-planar slicing more accessible to the masses."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/enthusiast-builds-a-working-486-dx2-retro-pc-on-a-breadboard-in-just-16-days-immediately-runs-doom-build-includes-a-66-mhz-intel-chip-and-custom-five-inch-3d-printed-display",
    "domain": "AI 算力 / 半导体",
    "title": "Enthusiast builds a working 486 DX2 retro PC on a breadboard in just 16 days, immediately runs Doom",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/enthusiast-builds-a-working-486-dx2-retro-pc-on-a-breadboard-in-just-16-days-immediately-runs-doom-build-includes-a-66-mhz-intel-chip-and-custom-five-inch-3d-printed-display",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T14:30:00+00:00",
    "summary": "An app engineer has showcased his homemade breadboard 486DX2 PC running Doom, put together in just over two weeks."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/pentagon-tests-pack-hunting-with-autonomous-war-robots-darpa-experimented-with-four-drone-ground-vehicles-that-detected-tracked-and-engaged-simulated-threats",
    "domain": "AI 算力 / 半导体",
    "title": "Pentagon tests pack hunting with autonomous war robots",
    "url": "https://www.tomshardware.com/tech-industry/drones/pentagon-tests-pack-hunting-with-autonomous-war-robots-darpa-experimented-with-four-drone-ground-vehicles-that-detected-tracked-and-engaged-simulated-threats",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T14:19:24+00:00",
    "summary": "The Pentagon has been testing packs of autonomous ground vehicles in simulated combat situations."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/nvidia-board-director-cashed-out-usd1-billion-in-stock-before-jensen-huang-scandal-mark-stevens-sold-4-2-million-shares-without-a-trading-plan",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia board director cashed out $1 billion in stock before Jensen Huang scandal",
    "url": "https://www.tomshardware.com/tech-industry/nvidia-board-director-cashed-out-usd1-billion-in-stock-before-jensen-huang-scandal-mark-stevens-sold-4-2-million-shares-without-a-trading-plan",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T14:00:00+00:00",
    "summary": "Nvidia Board Director sold around 4.2 million shares beginning August 31 and ending September 18, with the sale making him somewhere around $947 million."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/two-hpe-juniper-network-routers-grounded-all-the-us-flights-on-friday-faas-decades-old-copper-network-buckled-under-a-feature-hpe-says-worked-as-intended-creaking-air-traffic-communication-system-became-overloaded-by-very-high-rate-pinging",
    "domain": "AI 算力 / 半导体",
    "title": "Two HPE Juniper network routers grounded all US flights on Friday",
    "url": "https://www.tomshardware.com/networking/two-hpe-juniper-network-routers-grounded-all-the-us-flights-on-friday-faas-decades-old-copper-network-buckled-under-a-feature-hpe-says-worked-as-intended-creaking-air-traffic-communication-system-became-overloaded-by-very-high-rate-pinging",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T13:42:51+00:00",
    "summary": "The FAA determined that a rogue feature in two newly installed routers are to blame for the communications glitches that caused the nationwide ground stop."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-reclaims-overall-cpu-market-share-for-the-first-time-since-2025-massive-desktop-gains-offset-amds-record-server-and-mobile-growth",
    "domain": "AI 算力 / 半导体",
    "title": "Intel reclaims overall CPU market share for the first time since 2025",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-reclaims-overall-cpu-market-share-for-the-first-time-since-2025-massive-desktop-gains-offset-amds-record-server-and-mobile-growth",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T13:30:00+00:00",
    "summary": "AMD continues to gain server CPU market share amid skyrocketing shipments of data center processors as sales of client CPUs drop in the third quarter, says Mercury Research."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/university-of-rochester-researchers-made-a-3d-bioprinter-from-a-modified-ender-3-usd450-bioprinter-makes-engineered-living-material-research-accessible",
    "domain": "AI 算力 / 半导体",
    "title": "Modified Ender 3 becomes a $450 bioprinter for 3D printing engineered living materials",
    "url": "https://www.tomshardware.com/3d-printing/university-of-rochester-researchers-made-a-3d-bioprinter-from-a-modified-ender-3-usd450-bioprinter-makes-engineered-living-material-research-accessible",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T13:00:00+00:00",
    "summary": "Microbiologists at the University of Rochester have modified an Ender 3 FDM printer into a 3D bioprinter for $450 and outperforming 3D bioprinters costing more than $100,000."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/dev-hacks-coway-air-purifier-to-cut-it-off-from-the-cloud-now-runs-locally-in-home-assistant-fan-downloads-the-certificate-over-plain-http-letting-a-home-server-stand-in-for-coways",
    "domain": "AI 算力 / 半导体",
    "title": "Dev hacks Coway air purifier to cut it off from the cloud",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/dev-hacks-coway-air-purifier-to-cut-it-off-from-the-cloud-now-runs-locally-in-home-assistant-fan-downloads-the-certificate-over-plain-http-letting-a-home-server-stand-in-for-coways",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T12:30:00+00:00",
    "summary": "A developer reverse-engineered his Coway Airmega IconS air purifier to run it locally in Home Assistant, without Coway’s cloud."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/elon-musk-signs-petition-to-reinstate-jensen-huang-as-nvidia-ceo-over-130-000-sign-online-petition-but-not-all-nvidians-support-jensens-return",
    "domain": "AI 算力 / 半导体",
    "title": "Elon Musk signs petition to reinstate Jensen Huang as Nvidia CEO",
    "url": "https://www.tomshardware.com/tech-industry/elon-musk-signs-petition-to-reinstate-jensen-huang-as-nvidia-ceo-over-130-000-sign-online-petition-but-not-all-nvidians-support-jensens-return",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T12:00:00+00:00",
    "summary": "An online petition with over 91,000 signatures is calling for the reinstatement of Nvidia's disgraced former CEO."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/pc-building/dr-lisa-su-graces-the-opening-of-micro-centers-new-austin-store-amd-ceo-meets-with-gamers-autographs-a-9070-xt-gpu-and-hands-out-300-swag-bags",
    "domain": "AI 算力 / 半导体",
    "title": "Dr. Lisa Su graces the opening of Micro Center's new Austin store",
    "url": "https://www.tomshardware.com/desktops/pc-building/dr-lisa-su-graces-the-opening-of-micro-centers-new-austin-store-amd-ceo-meets-with-gamers-autographs-a-9070-xt-gpu-and-hands-out-300-swag-bags",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T11:30:00+00:00",
    "summary": "AMD gave away 300 swag bags to lucky shoppers, plus raffled off AMD gear, including a Radeon RX 9070 XT that Dr. Lisa Su autographed."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/xbox/the-original-xbox-was-released-25-years-ago-today-microsofts-pentium-iii-and-nvidia-gpu-powered-console-did-surprisingly-well-in-a-ps2-dominated-era",
    "domain": "AI 算力 / 半导体",
    "title": "The original Xbox was released 25 years ago today",
    "url": "https://www.tomshardware.com/video-games/xbox/the-original-xbox-was-released-25-years-ago-today-microsofts-pentium-iii-and-nvidia-gpu-powered-console-did-surprisingly-well-in-a-ps2-dominated-era",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T11:00:00+00:00",
    "summary": "Microsoft’s first games console hit North America 25 years ago today powered by a Pentium III CPU and Nvidia GPU."
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
    "points": 871,
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
    "points": 738,
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
    "points": 737,
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
    "points": 572,
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
    "points": 569,
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
    "points": 506,
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
    "points": 295,
    "published_at": "2026-11-10T16:07:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:50355504",
    "domain": "大厂 AI 动态",
    "title": "Google researchers demand freedom to tell the world what they know about AI",
    "url": "https://www.washingtonpost.com/technology/2026/11/03/google-deepmind-staff-protest-lifetime-ban-criticizing-company/",
    "source": "nsagent",
    "platform": "hackernews",
    "points": 92,
    "published_at": "2026-11-03T17:55:26+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/tech/1033355/apples-new-study-looks-to-improve-the-effectiveness-of-ai-health-tools",
    "domain": "大厂 AI 动态",
    "title": "Apple’s new study looks to improve the effectiveness of AI health tools",
    "url": "https://www.theverge.com/tech/1033355/apples-new-study-looks-to-improve-the-effectiveness-of-ai-health-tools",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-16T01:26:56+00:00",
    "summary": "Apple announced a new study today with the goal of better understanding how people interact with conversational AI health tools and how useful their responses actually are. The company is conducting t"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/1034013/armand-hammers-snakes-ladders-review",
    "domain": "大厂 AI 动态",
    "title": "Listen to this: Armand Hammer’s Snakes &#038; Ladders",
    "url": "https://www.theverge.com/entertainment/1034013/armand-hammers-snakes-ladders-review",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T21:49:22+00:00",
    "summary": "I open with this caveat: I haven't had a ton of time to digest the surprise Armand Hammer record that dropped this week. Billy Woods and Elucid rarely miss, though, and my initial reaction is that Sna"
  },
  {
    "id": "rss:https://www.theverge.com/science/1034006/vulcan-rocket-fails-destroying-40-amazon-leo-satellites",
    "domain": "大厂 AI 动态",
    "title": "Vulcan rocket fails, destroying 40 Amazon Leo satellites",
    "url": "https://www.theverge.com/science/1034006/vulcan-rocket-fails-destroying-40-amazon-leo-satellites",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T21:05:02+00:00",
    "summary": "United Launch Alliance (ULA) suffered what is reportedly its first mission failure in its 20-year history, failing to deliver 40 Amazon Leo satellites to orbit. Leo is Amazon's competitor to SpaceX's "
  },
  {
    "id": "rss:https://www.theverge.com/tech/1033999/jensen-huang-return-nvidia-megaspeed",
    "domain": "大厂 AI 动态",
    "title": "Jensen Huang might be plotting a return and more of the latest Nvidia drama",
    "url": "https://www.theverge.com/tech/1033999/jensen-huang-return-nvidia-megaspeed",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T20:43:49+00:00",
    "summary": "The drama around Nvidia co-founder and former CEO Jensen Huang is evolving quickly. The latest edition of our Stepback newsletter should get you up to speed, but there have already been a number of ne"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1033984/congress-export-rules-ai-chips-china",
    "domain": "大厂 AI 动态",
    "title": "Congress wants to tighten export rules on AI chips after Nvidia spy scandal",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1033984/congress-export-rules-ai-chips-china",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T19:15:43+00:00",
    "summary": "Unsurprisingly, following the scandal involving now-former Nvidia CEO Jensen Huang and a suspected Chinese spy, Congress is looking to further restrict exports of AI chips. Both Democrats and Republic"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1033620/fantikk-s1-pro-electric-screwdriver-black-friday-2026-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Fanttik’s S1 Pro electric screwdriver is $40 off in the run-up to Black Friday",
    "url": "https://www.theverge.com/gadgets/1033620/fantikk-s1-pro-electric-screwdriver-black-friday-2026-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T17:00:00+00:00",
    "summary": "Amazon’s early Black Friday promos are already underway, and we’ll be highlighting some of our favorites over the next few days on our Shopping page. Among them is the Fanttik S1 Pro Cordless Electric"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1033968/apples-first-smart-glasses-are-coming-together",
    "domain": "大厂 AI 动态",
    "title": "Apple’s first smart glasses are coming together",
    "url": "https://www.theverge.com/tech/1033968/apples-first-smart-glasses-are-coming-together",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T16:59:16+00:00",
    "summary": "Apple's smart glasses are among the worst-kept secrets in the tech world. Bloomberg's Mark Gurman says the company's first model, which will lack augmented reality features, will be announced at June'"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/1033895/rachelle-hampton-normal-gossip-interview",
    "domain": "大厂 AI 动态",
    "title": "Rachelle Hampton won’t admit how long she spent charting the use of ‘murmur’ in Twilight",
    "url": "https://www.theverge.com/entertainment/1033895/rachelle-hampton-normal-gossip-interview",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T16:00:00+00:00",
    "summary": "Rachelle Hampton is a writer and co-owner at Defector Media, and the host of Normal Gossip, a podcast of anonymous listener-submitted stories about everyday drama. Whether that's lies about luxury woo"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1033432/lg-b6e-oled-tv-best-buy-doorbuster-black-friday-2026-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "LG’s budget-friendly B6E OLED TV is up to 50 percent off this weekend",
    "url": "https://www.theverge.com/gadgets/1033432/lg-b6e-oled-tv-best-buy-doorbuster-black-friday-2026-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T14:00:00+00:00",
    "summary": "LG&#8217;s B6E was already one of the most affordable OLED TVs you could buy, but it&#8217;s an even better deal now that it’s included as part of Best Buy’s latest doorbuster event. Now through the e"
  },
  {
    "id": "rss:https://www.theverge.com/podcast/1033948/sony-aibo-robot-dog-version-history",
    "domain": "大厂 AI 动态",
    "title": "The Sony Aibo was a robot revolution dressed like a dog",
    "url": "https://www.theverge.com/podcast/1033948/sony-aibo-robot-dog-version-history",
    "source": "David Pierce",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T13:57:30+00:00",
    "summary": "In the 1990s, Sony was absolutely convinced that we were on the precipice of a robot takeover. Pretty soon, the company decided, we'd all be living among countless humanoid robots. Some would be our c"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/15/helsing-backer-plural-raises-1-1b-to-fund-europes-next-moonshots/",
    "domain": "大厂 AI 动态",
    "title": "Helsing backer Plural raises $1.1B to fund Europe’s next moonshots",
    "url": "https://techcrunch.com/2026/11/15/helsing-backer-plural-raises-1-1b-to-fund-europes-next-moonshots/",
    "source": "Anna Heim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-16T07:00:00+00:00",
    "summary": "Operator-led VC firm Plural has raised €1 billion in new capital ($1.1 billion), joining a growing cohort of larger European funds that also includes Mundi Ventures’ Kembara and EQT-managed Scaleup Eu"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/15/apple-launches-new-app-to-study-how-people-use-ai-for-health/",
    "domain": "大厂 AI 动态",
    "title": "Apple launches new app to study how people use AI for health",
    "url": "https://techcrunch.com/2026/11/15/apple-launches-new-app-to-study-how-people-use-ai-for-health/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-16T01:30:00+00:00",
    "summary": "Apple's new app for a study will answer everyday medical questions"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/15/indian-chip-startup-bharat-semi-lands-24m-seed-round-as-it-eyes-global-ai-sensor-market/",
    "domain": "大厂 AI 动态",
    "title": "Indian chip startup Bharat Semi lands $24M seed round as it eyes global AI sensor market",
    "url": "https://techcrunch.com/2026/11/15/indian-chip-startup-bharat-semi-lands-24m-seed-round-as-it-eyes-global-ai-sensor-market/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T23:30:00+00:00",
    "summary": "Bharat Semi says it has secured design wins for its AI-enabled sensor technology with companies including General Atomics."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/15/is-bad-news-for-jensen-huang-also-bad-news-for-the-ai-industry/",
    "domain": "大厂 AI 动态",
    "title": "Is bad news for Jensen Huang also bad news for the AI industry?",
    "url": "https://techcrunch.com/2026/11/15/is-bad-news-for-jensen-huang-also-bad-news-for-the-ai-industry/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T21:56:35+00:00",
    "summary": "\"Jensen is Nvidia, right? And so much of this economy is riding on Nvidia.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/15/snl-gathers-all-the-tech-tycoons-for-a-lesson-in-dating-and-spycraft/",
    "domain": "大厂 AI 动态",
    "title": "SNL gathers all the tech tycoons for a lesson in dating and spycraft",
    "url": "https://techcrunch.com/2026/11/15/snl-gathers-all-the-tech-tycoons-for-a-lesson-in-dating-and-spycraft/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T20:20:57+00:00",
    "summary": "While awkward, creepy tech executives have become a recurring theme on Saturday Night Live, this week’s episode gave the cast a chance to show off all their impressions at once."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/15/flaming-hydras-new-kickstarter-campaign-rethinks-e-book-ownership-and-digital-lending/",
    "domain": "大厂 AI 动态",
    "title": "Flaming Hydra’s new Kickstarter campaign rethinks e-book ownership and digital lending",
    "url": "https://techcrunch.com/2026/11/15/flaming-hydras-new-kickstarter-campaign-rethinks-e-book-ownership-and-digital-lending/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T18:29:14+00:00",
    "summary": "A new Kickstarter campaign aims to usher in the “return of the human internet.”"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/15/techcrunch-mobility-the-nvidia-backup-plan-for-chinas-self-driving-industry/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Mobility: The Nvidia backup plan for China’s self-driving industry",
    "url": "https://techcrunch.com/2026/11/15/techcrunch-mobility-the-nvidia-backup-plan-for-chinas-self-driving-industry/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T17:05:00+00:00",
    "summary": "Welcome back to TechCrunch Mobility, your hub for the future of transportation and now, more than ever, the role AI is playing in it."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/15/the-tech-products-we-enthusiastically-recommend-this-holiday-season/",
    "domain": "大厂 AI 动态",
    "title": "The tech products we enthusiastically recommend this holiday season",
    "url": "https://techcrunch.com/2026/11/15/the-tech-products-we-enthusiastically-recommend-this-holiday-season/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T16:00:00+00:00",
    "summary": "We've been reviewing a bunch of new gadgets at TechCrunch this year, and we have some clear favorites to share for your Black Friday shopping and beyond."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/14/where-was-nvidias-security-team/",
    "domain": "大厂 AI 动态",
    "title": "Where was Nvidia’s security team?",
    "url": "https://techcrunch.com/2026/11/14/where-was-nvidias-security-team/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T00:08:07+00:00",
    "summary": "Nvidia’s security chief quietly left in August, and now that CEO Jensen Huang has stepped down over his relationships, including one with an executive at a company suspected of funneling chips to Chin"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/14/elon-musk-other-tech-execs-sign-petition-calling-on-nvidia-to-reinstate-jensen-huang/",
    "domain": "大厂 AI 动态",
    "title": "Elon Musk, other tech execs sign petition calling on Nvidia to reinstate Jensen Huang",
    "url": "https://techcrunch.com/2026/11/14/elon-musk-other-tech-execs-sign-petition-calling-on-nvidia-to-reinstate-jensen-huang/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-14T21:41:22+00:00",
    "summary": "The petition had attracted more than 115,000 signatures as of Saturday afternoon."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/14/tesla-opens-cybercab-pre-orders-for-personal-use-with-geo-restrictions-and-a-299-monthly-fee/",
    "domain": "大厂 AI 动态",
    "title": "Tesla opens Cybercab pre-orders ‘for personal use,’ with geo restrictions and a $299 monthly fee",
    "url": "https://techcrunch.com/2026/11/14/tesla-opens-cybercab-pre-orders-for-personal-use-with-geo-restrictions-and-a-299-monthly-fee/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-14T20:04:44+00:00",
    "summary": "Even Elon Musk said the monthly fee is \"too high.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/14/got-an-iphone-duo-these-9-settings-make-it-easier-to-use/",
    "domain": "大厂 AI 动态",
    "title": "Got an iPhone Duo? These 9 settings make it easier to use",
    "url": "https://techcrunch.com/2026/11/14/got-an-iphone-duo-these-9-settings-make-it-easier-to-use/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-14T18:00:00+00:00",
    "summary": "From Touch ID shortcuts to smarter volume buttons and camera tricks, these tweaks make Apple's foldable iPhone easier to use every day."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/14/transportation-secretary-blames-routine-equipment-upgrade-for-grounding-flights-nationwide/",
    "domain": "大厂 AI 动态",
    "title": "Transportation secretary blames ‘routine’ equipment upgrade for grounding flights nationwide",
    "url": "https://techcrunch.com/2026/11/14/transportation-secretary-blames-routine-equipment-upgrade-for-grounding-flights-nationwide/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-14T17:45:04+00:00",
    "summary": "FAA administrator Bryan Bedford also said there's \"zero evidence of anything AI-related.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/14/the-ai-graveyard-a-running-list-of-projects-and-startups-that-didnt-make-it/",
    "domain": "大厂 AI 动态",
    "title": "The AI graveyard: a running list of projects and startups that didn’t make it",
    "url": "https://techcrunch.com/2026/11/14/the-ai-graveyard-a-running-list-of-projects-and-startups-that-didnt-make-it/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-14T17:30:00+00:00",
    "summary": "From Apple's repeatedly delayed Siri AI to OpenAI's messy \"super app\" launch, here's a look at the AI projects that shut down or missed expectations."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/14/asian-governments-react-to-nvidia-ceo-jensen-huangs-exit/",
    "domain": "大厂 AI 动态",
    "title": "Asian governments react to Nvidia CEO Jensen Huang’s exit",
    "url": "https://techcrunch.com/2026/11/14/asian-governments-react-to-nvidia-ceo-jensen-huangs-exit/",
    "source": "Kate Park",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-14T16:34:15+00:00",
    "summary": "Some governments moved to confirm chip supply commitments, while others are monitoring the impact on local projects or addressing ongoing investigations."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/11/vulcan-rocket-fails-during-launch-dealing-major-blow-to-spacex-competitors/",
    "domain": "大厂 AI 动态",
    "title": "Vulcan rocket fails during launch, dealing major blow to SpaceX competitors",
    "url": "https://arstechnica.com/space/2026/11/vulcan-rocket-fails-during-launch-dealing-major-blow-to-spacex-competitors/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T23:11:54+00:00",
    "summary": "This was the first total mission failure in United Launch Alliance's 20-year history."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/11/how-the-worlds-fires-changed-while-humanity-hit-pause/",
    "domain": "大厂 AI 动态",
    "title": "How the world’s fires changed while humanity hit pause",
    "url": "https://arstechnica.com/science/2026/11/how-the-worlds-fires-changed-while-humanity-hit-pause/",
    "source": "Yook Ji Hun",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T12:07:34+00:00",
    "summary": "COVID-19 lockdowns cut global fire activity by 12.3 percent."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/11/with-starship-catch-spacex-still-shows-it-can-dazzle-the-world/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX returned its Starship rocket on Saturday—but there's a catch",
    "url": "https://arstechnica.com/space/2026/11/with-starship-catch-spacex-still-shows-it-can-dazzle-the-world/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T00:40:59+00:00",
    "summary": "It felt like stepping into the future."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/11/james-webb-telescope-finds-ice-older-than-the-star-it-orbits/",
    "domain": "大厂 AI 动态",
    "title": "James Webb telescope finds ice older than the star it orbits",
    "url": "https://arstechnica.com/science/2026/11/james-webb-telescope-finds-ice-older-than-the-star-it-orbits/",
    "source": "Jacek Krywko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-14T12:15:48+00:00",
    "summary": "Radiation and collisions reshape the planetary building materials."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/11/winemakers-are-learning-that-conservation-can-be-good-for-business/",
    "domain": "大厂 AI 动态",
    "title": "Winemakers are learning that conservation can be good for business",
    "url": "https://arstechnica.com/science/2026/11/winemakers-are-learning-that-conservation-can-be-good-for-business/",
    "source": "Hannah V. Herrero, Erin L. Bunting, Jane Southworth, Jason K. Blackburn, and Stephanie Insalaco-Wyner, The Conversation",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-14T12:05:51+00:00",
    "summary": "Healthy soils, native plants, and fewer chemicals are helping vineyards adapt."
  },
  {
    "id": "rss:https://www.producthunt.com/products/trusty-csv",
    "domain": "大厂 AI 动态",
    "title": "Trusty CSV",
    "url": "https://www.producthunt.com/products/trusty-csv",
    "source": "Yusef Hassan Montero",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T09:19:42+00:00",
    "summary": "Edit CSV files like code, not like a spreadsheet Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/bytevoice",
    "domain": "大厂 AI 动态",
    "title": "ByteVoice",
    "url": "https://www.producthunt.com/products/bytevoice",
    "source": "Zac Zuo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-16T01:45:10+00:00",
    "summary": "Talk to your coding agents and hear them back Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/freebuff-2",
    "domain": "大厂 AI 动态",
    "title": "Freebuff",
    "url": "https://www.producthunt.com/products/freebuff-2",
    "source": "kar en",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T17:59:28+00:00",
    "summary": "The 100% free coding agent Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/stateweave",
    "domain": "大厂 AI 动态",
    "title": "StateWeave",
    "url": "https://www.producthunt.com/products/stateweave",
    "source": "Aleksandar Blazhev",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T20:32:35+00:00",
    "summary": "Test your AI agent on working clones of the apps it uses Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/glifa",
    "domain": "大厂 AI 动态",
    "title": "Glifa",
    "url": "https://www.producthunt.com/products/glifa",
    "source": "Łukasz Majda",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-15T12:25:03+00:00",
    "summary": "The Markdown editor for Mac you can ask for anything Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/centralize",
    "domain": "大厂 AI 动态",
    "title": "Centralize",
    "url": "https://www.producthunt.com/products/centralize",
    "source": "Michael Farr",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-14T21:21:02+00:00",
    "summary": "Relationship Workspace for Enterprise Deal Teams Discussion | Link"
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
    "id": "hn:50346153",
    "domain": "股票",
    "title": "Intel stock collapse worsens as $3.5T chip rout spreads",
    "url": "https://finance.yahoo.com/markets/article/the-intel-stock-collapse-is-getting-worse--and-the-37-trillion-chip-rout-is-spreading-212154947.html",
    "source": "entryleveljobsc",
    "platform": "hackernews",
    "points": 237,
    "published_at": "2026-11-03T00:08:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:50381623",
    "domain": "股票",
    "title": "Nasdaq plummets 4% into correction territory",
    "url": "https://www.cnbc.com/2026/11/04/stock-market-today-live-updates.html",
    "source": "kristianp",
    "platform": "hackernews",
    "points": 227,
    "published_at": "2026-11-05T17:11:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:50342284",
    "domain": "股票",
    "title": "Oracle files to sell $20B in new stock, bonds to finance AI buildout",
    "url": "https://www.cnbc.com/2026/11/02/oracle-files-to-sell-20-billion-in-new-stock-bonds-to-finance-ai-buildout.html",
    "source": "smartmic",
    "platform": "hackernews",
    "points": 200,
    "published_at": "2026-11-02T19:27:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:50510005",
    "domain": "股票",
    "title": "Do House members' stock trades beat the market? A test of 8,900 trades",
    "url": "https://arkanumdata.com/research/house-trades",
    "source": "Bluestein",
    "platform": "hackernews",
    "points": 114,
    "published_at": "2026-11-15T19:46:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:50384822",
    "domain": "股票",
    "title": "$2.5T has been wiped from US stocks",
    "url": "https://finlaws.substack.com/p/25t-has-been-wiped-from-us-stocks",
    "source": "madihaa",
    "platform": "hackernews",
    "points": 164,
    "published_at": "2026-11-05T21:39:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:50382179",
    "domain": "股票",
    "title": "Nasdaq Sinks 5% as Investors Retreat from AI Trade After Election",
    "url": "https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-11-05-2026",
    "source": "armcat",
    "platform": "hackernews",
    "points": 163,
    "published_at": "2026-11-05T18:00:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:50151376",
    "domain": "股票",
    "title": "The obscure trust looming over Anthropic's IPO",
    "url": "https://www.wsj.com/tech/ai/anthropic-ipo-private-trust-188f41f7?st=RtdGHg&reflink=desktopwebshare_permalink",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 154,
    "published_at": "2026-10-19T12:06:03+00:00",
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
    "id": "hn:50507517",
    "domain": "股票",
    "title": "A Human Reads the Anthropic IPO Filing",
    "url": "https://www.nytimes.com/2026/11/15/business/anthropic-ipo-filing-prospectus.html",
    "source": "saikatsg",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-11-15T15:18:06+00:00",
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
    "id": "hn:50362274",
    "domain": "股票",
    "title": "AI stocks slide as Texas governor result raises data center risks",
    "url": "https://www.cnbc.com/2026/11/04/ai-stocks-texas-governor-data-centers.html",
    "source": "1659447091",
    "platform": "hackernews",
    "points": 56,
    "published_at": "2026-11-04T07:00:20+00:00",
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
    "id": "hn:50386909",
    "domain": "股票",
    "title": "Investors wipe $2.5T off Nasdaq as blue tsunami prompts AI fears",
    "url": "https://www.reuters.com/legal/transactional/ai-data-center-stocks-slip-democratic-sweep-clouds-expansion-plans-2026-11-05/",
    "source": "lilerjee",
    "platform": "hackernews",
    "points": 46,
    "published_at": "2026-11-06T01:11:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:50463421",
    "domain": "股票",
    "title": "Nvidia's Disappearing Singapore Sales Deepen Mystery Around Megaspeed",
    "url": "https://www.wsj.com/business/earnings/nvidias-disappearing-singapore-sales-deepen-mystery-around-megaspeed-7d483180",
    "source": "ea016",
    "platform": "hackernews",
    "points": 23,
    "published_at": "2026-11-12T05:31:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:50352405",
    "domain": "股票",
    "title": "US Hedge Funds Just Sold Every AI Stock They Bought Since 2025",
    "url": "https://finance.yahoo.com/markets/stocks/articles/us-hedge-funds-just-sold-113114644.html",
    "source": "robin_reala",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-11-03T14:27:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:50389401",
    "domain": "股票",
    "title": "Global stocks tumble as AI panic grips markets after Democrats' midterm success",
    "url": "https://www.theguardian.com/business/live/2026/nov/06/global-stocks-tumble-ai-panic-markets-democrats-midterms-success-jobs-oil-dollar-latest-news-updates",
    "source": "drayfield",
    "platform": "hackernews",
    "points": 36,
    "published_at": "2026-11-06T07:52:53+00:00",
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
    "id": "hn:50351712",
    "domain": "股票",
    "title": "Anthropic's IPO Filing Warns It May Be 'Imminently' Close to RSI",
    "url": "https://epyhia.com/anthropic-s-ipo-filing-warns-it-may-be-imminently-close-to-recursive",
    "source": "arbuge",
    "platform": "hackernews",
    "points": 34,
    "published_at": "2026-11-03T13:26:43+00:00",
    "summary": ""
  },
  {
    "id": "hn:50384382",
    "domain": "股票",
    "title": "Chip stocks get slaughtered as Wall Street in worst post-midterm day since 1896",
    "url": "https://finance.yahoo.com/markets/article/chip-stocks-get-slaughtered-as-wall-street-heads-for-its-worst-post-midterm-day-since-1896-163413900.html",
    "source": "novaRom",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-11-05T20:58:36+00:00",
    "summary": ""
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
    "id": "hn:50167295",
    "domain": "股票",
    "title": "Data center stocks slide as Korea IPO plunges 30%, pressuring tech sentiment",
    "url": "https://www.cnbc.com/2026/10/20/data-center-stocks-slide-as-korea-ipo-plunges-30percent-pressuring-tech-sentiment.html",
    "source": "PLenz",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-10-20T14:50:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:50142772",
    "domain": "股票",
    "title": "How the Fed Is Quietly Inflating the AI Bubble While Hiking Your Electric Bill",
    "url": "https://www.thebignewsletter.com/p/how-the-federal-reserve-secretly",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 30,
    "published_at": "2026-10-18T16:48:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:50171533",
    "domain": "股票",
    "title": "Anthropic S-1 Shows Red-Hot Growth, Risks and Computing Costs",
    "url": "https://www.wsj.com/tech/ai/anthropic-revenue-growth-ipo-accaf0f1",
    "source": "mmmmmbop",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-10-20T19:34:39+00:00",
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
    "points": 1164,
    "published_at": "2026-11-06T12:13:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:50154244",
    "domain": "金融",
    "title": "DeepSeek banned from U.S. federal civilian agencies under new DHS order",
    "url": "https://www.reuters.com/technology/us-banning-chinese-ai-deepseek-government-agency-it-systems-2026-10-19/",
    "source": "cmrdporcupine",
    "platform": "hackernews",
    "points": 584,
    "published_at": "2026-10-19T16:16:46+00:00",
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
    "id": "hn:50173487",
    "domain": "金融",
    "title": "Feds suspect ransom negotiator ran ShinyHunters extortion site",
    "url": "https://krebsonsecurity.com/2026/10/feds-suspect-ransom-negotiator-ran-shinyhunters-extortion-site/",
    "source": "Bender",
    "platform": "hackernews",
    "points": 270,
    "published_at": "2026-10-20T22:21:05+00:00",
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
    "id": "hn:50131440",
    "domain": "金融",
    "title": "US federal budget deficit jumps 12% in one year to nearly $2 Trillion",
    "url": "https://finance.yahoo.com/economy/policy/article/the-us-federal-budget-deficit-for-2026-just-came-in-its-1992-trillion-191917669.html",
    "source": "ck2",
    "platform": "hackernews",
    "points": 208,
    "published_at": "2026-10-17T14:22:05+00:00",
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
    "id": "hn:50505905",
    "domain": "金融",
    "title": "Jensen Huang allegedly manufactured the GPU shortage",
    "url": "https://wccftech.com/jensen-huang-financed-ai-startups-absorb-excess-silicon/",
    "source": "bobsoap",
    "platform": "hackernews",
    "points": 63,
    "published_at": "2026-11-15T10:53:50+00:00",
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
    "id": "hn:50387406",
    "domain": "金融",
    "title": "Tesla and SpaceX lose over $420B in combined market cap in the two days",
    "url": "https://techlaws.pages.dev/tesla-and-spacex-lose-over-420b-in-combined-market-cap-in-the-two-days/",
    "source": "Pepitobombito",
    "platform": "hackernews",
    "points": 84,
    "published_at": "2026-11-06T02:30:25+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.17530",
    "domain": "金融",
    "title": "AI and the Two Margins of Work: Why Job Losses Show Up Before Job Creation",
    "url": "https://arxiv.org/abs/2611.17530",
    "source": "Mark Esposito, Liu Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-16T05:00:00+00:00",
    "summary": "arXiv:2611.17530v1 Announce Type: new Abstract: Technological change acts on labor demand at two margins: adjustment within established activities and the creation of additional activities, often by n"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.17902",
    "domain": "金融",
    "title": "Well-Posedness of Semimartingale Optimal Transport with Partial Marginal Constraints for Model Calibration",
    "url": "https://arxiv.org/abs/2611.17902",
    "source": "Jean-Fran\\c{c}ois Chassagneux, St\\'ephane Cr\\'epey, Gr\\'egoire Loeper, Justin Ruelland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-16T05:00:00+00:00",
    "summary": "arXiv:2611.17902v1 Announce Type: new Abstract: We study the well-posedness and stability of a semimartingale optimal transport problem with partial marginal constraints at several maturities, motivat"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.17942",
    "domain": "金融",
    "title": "Mapping NGFS Climate Pathways to GICS Sectors: Application to Portfolio Decarbonization",
    "url": "https://arxiv.org/abs/2611.17942",
    "source": "Maxime Jourand, Adel Medjabri",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-16T05:00:00+00:00",
    "summary": "arXiv:2611.17942v1 Announce Type: new Abstract: Portfolio climate alignment is limited by the mismatch between asset managers' sector classifications and those of climate scenarios. This article propo"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.17984",
    "domain": "金融",
    "title": "Menu Design Meets Market Design: Strategic Simplicity vs. Choice Complexity",
    "url": "https://arxiv.org/abs/2611.17984",
    "source": "Gian Caspari, Paul Erg\\\"un Hild, Michael Hilweg-Waldeck, Manshu Khanna, Vincent Meisner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-16T05:00:00+00:00",
    "summary": "arXiv:2611.17984v1 Announce Type: new Abstract: Strategic simplicity removes the incentive to misreport preferences, but it does not ensure that participants can identify what they prefer. We study th"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.18150",
    "domain": "金融",
    "title": "Who Should Be on the Panel? Task-Conditioned Persona Selection for LLM Trading Agents",
    "url": "https://arxiv.org/abs/2611.18150",
    "source": "Boming Yang, Yuquan Wang, Jiaxian Guo, Yusuke Iwasawa, Yutaka Matsuo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-16T05:00:00+00:00",
    "summary": "arXiv:2611.18150v1 Announce Type: new Abstract: Multi-agent LLM systems are built by fixing a cast of roles and then designing how the cast coordinates. Which agents should make up the group for a giv"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.18214",
    "domain": "金融",
    "title": "Local Stochastic Volatility Iterations",
    "url": "https://arxiv.org/abs/2611.18214",
    "source": "Christian Bayer, Denis Belomestny, Paul P. Hager, John Schoenmakers",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-16T05:00:00+00:00",
    "summary": "arXiv:2611.18214v1 Announce Type: new Abstract: We propose a calibration method for local stochastic volatility models that determines the leverage factor by a fixed-point iteration. Each iteration si"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.18367",
    "domain": "金融",
    "title": "DECODE: Decomposable Environments for COntrolled Sequential-Decision Evaluation",
    "url": "https://arxiv.org/abs/2611.18367",
    "source": "Diego Silva Prado, Bruno Caldas de Souza, Tiago Amaral Penteado de Jesus, Ricardo Guimar\\~aes Herrmann, Cristiano Breuel, Cristiano Bevitori Maffia De Oliveira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-16T05:00:00+00:00",
    "summary": "arXiv:2611.18367v1 Announce Type: cross Abstract: When a sequential decision system falls short of an optimum, its score does not reveal which modifications would improve its decisions. DECODE is a be"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.18531",
    "domain": "金融",
    "title": "Alignment by Socialization: Learning Tradeoffs Under Selection",
    "url": "https://arxiv.org/abs/2611.18531",
    "source": "Thomas Brennan, Andrew W. Lo, Chaoyi Zhao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-16T05:00:00+00:00",
    "summary": "arXiv:2611.18531v1 Announce Type: cross Abstract: Artificial intelligence (AI) agents are expected to complete tasks while following rules of conduct, but these objectives can conflict. We study how e"
  },
  {
    "id": "rss:https://arxiv.org/abs/2408.03134",
    "domain": "金融",
    "title": "Incomplete-market CAPM equilibria in continuous time",
    "url": "https://arxiv.org/abs/2408.03134",
    "source": "Nikolaos Constantinou, Christoph Czichowsky, Martin Herdegen, David Martins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-16T05:00:00+00:00",
    "summary": "arXiv:2408.03134v3 Announce Type: replace Abstract: We study continuous-time CAPM equilibria with general mean-variance preferences of the form $U(\\mu,\\sigma)$, where $U$ is strictly quasiconcave, inc"
  },
  {
    "id": "rss:https://arxiv.org/abs/2506.16355",
    "domain": "金融",
    "title": "Social Media Can Suppress or Fuel Misinformation at Its Source, Depending on Civic Engagement",
    "url": "https://arxiv.org/abs/2506.16355",
    "source": "Gavin Wang, Haofei Qin, Xiao Tang, Lynn Wu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-16T05:00:00+00:00",
    "summary": "arXiv:2506.16355v2 Announce Type: replace Abstract: Social media is widely viewed as a channel for spreading misinformation, but its effects may begin earlier, by shaping whether misinformation is pro"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.31512",
    "domain": "金融",
    "title": "Tolerable Inflation, Intolerable Uncertainty",
    "url": "https://arxiv.org/abs/2609.31512",
    "source": "Eric Vansteenberghe",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-16T05:00:00+00:00",
    "summary": "arXiv:2609.31512v2 Announce Type: replace Abstract: How much of an inflation deviation a central bank should tolerate is a well-defined optimum in the New Keynesian model, but it cannot be identified:"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.01540",
    "domain": "金融",
    "title": "Social Networks and the Propagation of Household Shocks to Asset Prices",
    "url": "https://arxiv.org/abs/2611.01540",
    "source": "Faisal Quaiyyum",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-16T05:00:00+00:00",
    "summary": "arXiv:2611.01540v3 Announce Type: replace Abstract: When can local household disturbances move credit prices? I develop a financially weighted propagation operator on the social network. In a conditio"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.15747",
    "domain": "金融",
    "title": "Huge If True: Learning from the Size of the Surprise",
    "url": "https://arxiv.org/abs/2611.15747",
    "source": "Thomas Graeber, Christopher Roth, Marco Sammon, Constantin Schesch",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-16T05:00:00+00:00",
    "summary": "arXiv:2611.15747v2 Announce Type: replace Abstract: Responses to earnings surprises depend on an unknown multiplier mapping earnings to value. Investors, however, learn about the news and the multipli"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.25610",
    "domain": "金融",
    "title": "Match classification in the last round of four-team round-robin tournaments",
    "url": "https://arxiv.org/abs/2605.25610",
    "source": "L\\'aszl\\'o Csat\\'o, Andr\\'as Gyimesi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-16T05:00:00+00:00",
    "summary": "arXiv:2605.25610v3 Announce Type: replace-cross Abstract: Classification of matches played in the last rounds of sports competitions is a well-established tool for evaluating tournament designs. Our p"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.13880",
    "domain": "金融",
    "title": "A Horizon-Specific Attribute-Conditioned Neural Network for Estimating Health-State Transition Probabilities in Irregular Longitudinal Data: The LANTERN Framework",
    "url": "https://arxiv.org/abs/2606.13880",
    "source": "Bright Kwaku Manu, Beckett Sterner, Petar Jevtic",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-16T05:00:00+00:00",
    "summary": "arXiv:2606.13880v2 Announce Type: replace-cross Abstract: Accurate estimation of health-state transition probabilities is essential for long-term care insurance modeling. Conventional actuarial multi-"
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
    "id": "hn:50161207",
    "domain": "金融",
    "title": "U.S. Supreme Court to review 1868 federal ban on home distilling of liquor",
    "url": "https://www.staradvertiser.com/2026/10/19/breaking-news/u-s-supreme-court-to-review-1868-federal-ban-on-home-distilling-of-liquor/",
    "source": "Jimmc414",
    "platform": "hackernews",
    "points": 68,
    "published_at": "2026-10-20T04:02:26+00:00",
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
    "id": "hn:50156189",
    "domain": "金融",
    "title": "The US orders every civilian agency to rip out DeepSeek, even tools built on it",
    "url": "https://madrobot.blog/2026/10/19/us-bans-deepseek-federal-agencies-dhs-order-remove-third-party/",
    "source": "jacquesm",
    "platform": "hackernews",
    "points": 66,
    "published_at": "2026-10-19T18:41:10+00:00",
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
    "id": "hn:50360067",
    "domain": "金融",
    "title": "Tesla allegedly misled South Korean customers about automated-driving tech",
    "url": "https://www.reuters.com/business/autos-transportation/tesla-misled-south-korean-customers-about-automated-driving-tech-consumer-group-2026-11-04/",
    "source": "EA-3167",
    "platform": "hackernews",
    "points": 29,
    "published_at": "2026-11-04T00:19:50+00:00",
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
    "id": "hn:50159683",
    "domain": "金融",
    "title": "Trump Appointees Asked a Federal Agency to Acquire a Voting Machine and Hack It",
    "url": "https://www.propublica.org/article/cisa-election-security-donald-trump",
    "source": "soundworlds",
    "platform": "hackernews",
    "points": 29,
    "published_at": "2026-10-20T00:09:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:50152041",
    "domain": "金融",
    "title": "Federal judge rules Flock violated the fourth amendment",
    "url": "https://twitter.com/scotus_wire/status/2106487374624514071",
    "source": "vessenes",
    "platform": "hackernews",
    "points": 27,
    "published_at": "2026-10-19T13:14:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:50467087",
    "domain": "电子信息与芯片",
    "title": "Jensen Huang resigns",
    "url": "https://apnews.com/article/nvidia-megaspeed-china-singapore-huang-5403f152a601cf82ce939f1d24fffa0f",
    "source": "lldb",
    "platform": "hackernews",
    "points": 4052,
    "published_at": "2026-11-12T13:52:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:50459321",
    "domain": "电子信息与芯片",
    "title": "Jensen Huang said to have had relationship with executive who reports to him",
    "url": "https://www.nytimes.com/2026/11/11/technology/jensen-huang-nvidia-affair.html",
    "source": "louiereederson",
    "platform": "hackernews",
    "points": 412,
    "published_at": "2026-11-11T22:03:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:50471621",
    "domain": "电子信息与芯片",
    "title": "Singapore Says U.S. Not Helpful on Investigation into Suspected Spy's Company",
    "url": "https://www.nytimes.com/2026/11/12/business/nvidia-megaspeed-alice-huang.html",
    "source": "tedd4u",
    "platform": "hackernews",
    "points": 186,
    "published_at": "2026-11-12T18:14:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:50498051",
    "domain": "电子信息与芯片",
    "title": "Smuggling of 1.5M AI GPUs could be the cause of Huang's departure",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/mass-smuggling-of-nvidia-ai-gpus-could-be-the-underlying-cause-of-jensen-huangs-departure-analysts-claim-more-than-1-5-gigawatts-of-banned-chips-tracked-to-china-despite-export-controls",
    "source": "marginalia_nu",
    "platform": "hackernews",
    "points": 61,
    "published_at": "2026-11-14T15:58:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:50473868",
    "domain": "电子信息与芯片",
    "title": "Jensen Huang Third Affair Allegations Revealed",
    "url": "https://www.forbes.com/sites/alisondurkee/2026/11/12/jensen-huang-had-a-third-affair-with-another-nvidia-employee-report-says/",
    "source": "FinnLobsien",
    "platform": "hackernews",
    "points": 58,
    "published_at": "2026-11-12T20:36:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:50427486",
    "domain": "电子信息与芯片",
    "title": "Commerce Dept Inquiry into Megaspeed Halted After Nvdia Intervention",
    "url": "https://www.nytimes.com/2026/11/09/business/economy/nvidia-megaspeed-investigation-huang.html",
    "source": "louiereederson",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-11-09T16:10:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:50459679",
    "domain": "电子信息与芯片",
    "title": "Jensen Huang had a second affair – with an employee",
    "url": "https://www.cnbc.com/2026/11/11/nvidia-jensen-huang-affair-employee.html",
    "source": "justswim",
    "platform": "hackernews",
    "points": 52,
    "published_at": "2026-11-11T22:29:27+00:00",
    "summary": ""
  }
]
```
