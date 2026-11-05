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

- 今日日期：`2026-11-05`
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
  "date": "2026-11-05",
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
    "points": 2208994,
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
    "points": 2082927,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1REx46NEc4",
    "domain": "AI",
    "title": "【全网最全】DeepSeek Harness超详细教程！50分钟吃透DSH，让SuperAgent给你干活！",
    "url": "http://www.bilibili.com/video/av117540671982699",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 1849343,
    "published_at": "2026-11-01T10:22:02+00:00",
    "summary": "DeepSeek Harness超详细教程！\n大家可以速速收藏啦~\n耗时60天制作！感谢大家的三联\n未来还会出其他AI教程，大家可以关注一下~"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 1470263,
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
    "points": 1433655,
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
    "points": 1432324,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV14rzQB9EJj",
    "domain": "AI",
    "title": "Claude Code 从 0 到 1 全攻略：MCP / SubAgent / Agent Skill / Hook / 图片 / 上下文处理/ 后台任务",
    "url": "http://www.bilibili.com/video/av115954889596221",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 1341997,
    "published_at": "2026-01-25T08:55:20+00:00",
    "summary": "时间戳如下，方便大家跳转观看：\n \n第一部分：环境搭建与基础交互\n- 01:09 安装 Claude Code\n- 01:43 登录与授权\n- 02:55 第一个实战问题\n- 03:12 三种模式详解 (默认/自动/规划)\n \n第二部分：复杂任务处理与终端控制\n- 06:00 执行终端命令 (Bash)\n- 06:49 使用规划模式 (Plan Mode)\n- 11:06 跳过所有权限检测 (da"
  },
  {
    "id": "bvid:BV1aeLqzUE6L",
    "domain": "AI",
    "title": "10分钟讲清楚 Prompt, Agent, MCP 是什么",
    "url": "http://www.bilibili.com/video/av114410228025650",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 909561,
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
    "points": 891198,
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
    "points": 742987,
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
    "points": 675321,
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
    "points": 595559,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV1AnQNYxEsy",
    "domain": "AI",
    "title": "MCP是啥？技术原理是什么？一个视频搞懂MCP的一切。Windows系统配置MCP，Cursor Cline使用MCP",
    "url": "http://www.bilibili.com/video/av114155298228756",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 427131,
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
    "points": 346897,
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
    "points": 321364,
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
    "points": 293731,
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
    "points": 226111,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV15XDfBSE2t",
    "domain": "AI",
    "title": "ClaudeCode平替:OpenCode详细使用教程看这一个就够了（内含超详细安装文档+软件安装包）",
    "url": "http://www.bilibili.com/video/av116379604881806",
    "source": "鹏哥C语言",
    "platform": "bilibili",
    "points": 199751,
    "published_at": "2026-04-13T09:00:00+00:00",
    "summary": "opencodeopencode使用全攻略opencode教程opencode和claudecodeopencode使用技巧opencode实战opencode coworkopencode安装opencode开发opencode使用教程opencode教程opencode安装教程opencode使用全攻略opencode和claudecodeopencode skillsopencode插件op"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 185835,
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
    "points": 164787,
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
    "points": 162149,
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
    "points": 161727,
    "published_at": "2025-02-18T13:13:51+00:00",
    "summary": "我试用了几十种AI编程辅助工具，找到了其中三个免费，并且效果最好的方案。 本期视频就来跟大家分享一下。视频中间会穿插很多AI编程工具的使用技巧，还有看待AI编程的一些个人思考。本期视频没有广告都是个人的经验干货，废话不多说我们直接开始。"
  },
  {
    "id": "bvid:BV1sZMq6qEko",
    "domain": "AI",
    "title": "从0做出你的第一个App ｜ 零基础AI编程保姆教程",
    "url": "http://www.bilibili.com/video/av117038647352026",
    "source": "木子不写代码",
    "platform": "bilibili",
    "points": 156224,
    "published_at": "2026-08-07T12:15:00+00:00",
    "summary": "这期视频，我会手把手带你，用 AI 做出你的第一个 App。\n全程假设你没有任何编程和AI的基础，\n我们从如何写需求提示词开始，\n到确定页面结构和设计，\n产品需求文档，\n开发计划，\n第一版APP验收，\ngit代码存档，\n二次开发，\n界面美化，\n做好的APP也会开源给到大家，\n我也会演示如何获取这个项目源代码并且用AI继续定制开发，\n视频到最后，\n你会收获一个为自己的工作和生活定制的专属APP！\n和"
  },
  {
    "id": "bvid:BV1eYPpeWEnT",
    "domain": "AI",
    "title": "Cursor + MCP = 王炸！彻底颠覆我的Cursor工作流，效率直接起飞",
    "url": "http://www.bilibili.com/video/av114073660301264",
    "source": "御风大世界",
    "platform": "bilibili",
    "points": 151756,
    "published_at": "2025-02-27T03:19:03+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 149680,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1LQaN6RE3v",
    "domain": "AI",
    "title": "【 豆包Agent保姆级教程】吊打付费!  豆包彻底玩明白！只看这一期就够了！10节付费课内容全公开，零基础也能学会!",
    "url": "http://www.bilibili.com/video/av117325671961695",
    "source": "豆包Agent官方教程",
    "platform": "bilibili",
    "points": 103627,
    "published_at": "2026-09-26T09:57:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1VL3F6pE9K",
    "domain": "AI",
    "title": "0基础入门智能体agent测试：AI测试基础+AI智能体(Agent)测试从零入门全攻略，2026最新版！",
    "url": "http://www.bilibili.com/video/av116991151113881",
    "source": "黑马测试",
    "platform": "bilibili",
    "points": 102105,
    "published_at": "2026-07-27T09:19:37+00:00",
    "summary": "还在卷传统软件测试？2026年必学的AI智能体(Agent)测试来了！本期视频专为0基础小白打造，从软件测试基础讲起...若要本视频配套资源笔记可加up主企微（请看置顶留言最后一句话）。"
  },
  {
    "id": "bvid:BV1K6YM69ESq",
    "domain": "AI",
    "title": "AI+网络安全实战：从Agent入门到AI智能体挖漏洞教程！网络安全|信息安全|黑客技术|渗透测试|SRC漏洞挖掘|AI审计|HVV护网行动|靶场练习-码士集团",
    "url": "http://www.bilibili.com/video/av117247037213495",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 95614,
    "published_at": "2026-09-10T13:47:24+00:00",
    "summary": "这套课程围绕「AI+网络安全」展开，从AI智能体基础入门，到WorkBuddy、Trae等主流Agent工具的实际应用，再到API-Key接入、Skill使用等核心能力，逐步进入AI漏洞挖掘、代码审计、CTF题目分析等安全实战场景。同时结合SRC漏洞挖掘、HVV护网、安全竞赛以及网络安全就业方向，帮助你系统了解AI在网络安全学习、开发与实战中的应用方式。适合网络安全初学者、安全从业者以及希望利用A"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 94244,
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
    "points": 76817,
    "published_at": "2026-03-11T18:12:00+00:00",
    "summary": "本期给大家带来的是Claude在Vscode的科研应用演示与我最近的一些心得使用心得，科研速度嘎嘎提升。论文复现画图、数据分析就靠Claude code。这个课程也是科研推土机「系统管理文献课程2.0」学员催我更新的内容，希望能帮助到大家～，这个视频重点讲两个事情：\n1️⃣ 资料获取，free不用怀疑，我是良心可言博主，，关注我(GZTSHNR)～\n2️⃣ 展示如何在VS code实操应用clau"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operit教程：入门安卓最强大ai平台operitAI",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 75610,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV19wXvBpEaL",
    "domain": "AI",
    "title": "认真用 Claude Code 的人，迟早会遇见 Everything Claude Code",
    "url": "http://www.bilibili.com/video/av116319122885806",
    "source": "极客魔导师",
    "platform": "bilibili",
    "points": 64103,
    "published_at": "2026-03-30T16:47:51+00:00",
    "summary": "Everything Claude Code 是目前 GitHub 上 116K star 的 Claude Code 配置项目。本期从斜杠命令、子代理、Hooks 到学习系统，带你把这个项目真正用起来。"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 50140,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1EfY76YEwp",
    "domain": "AI",
    "title": "14k Star Claude Code 开源桌面端，能自动操作电脑了！",
    "url": "http://www.bilibili.com/video/av117251936293145",
    "source": "程序员阿江-Relakkes",
    "platform": "bilibili",
    "points": 49529,
    "published_at": "2026-09-11T10:30:01+00:00",
    "summary": "基于此前泄露的 Claude Code 源代码，我做了一个开源桌面端 cc-haha，并持续迭代。\n这次重构了 Computer Use 电脑操控功能：AI 能自己看屏幕、操作 APP，在 Mac 后台搭建小镇，也不占用我的鼠标键盘。\n本期从下载安装、模型配置到权限授权，带你一步步用起来。支持自选模型，不需要 Claude 账号。"
  },
  {
    "id": "bvid:BV1vYFQzQE4P",
    "domain": "AI",
    "title": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！Claude Code Hooks回调+Agent Teams全自动开发零轮询",
    "url": "http://www.bilibili.com/video/av116046157647899",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 47801,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1JY4w6kEAe",
    "domain": "AI",
    "title": "【全网首发】Claude防封号独家指南！前后花了5万元！小白保姆级教程【包含对话铺垫/IP DNS/订阅方式/历史记录清除】",
    "url": "http://www.bilibili.com/video/av117546107800312",
    "source": "Gemini3-",
    "platform": "bilibili",
    "points": 47005,
    "published_at": "2026-11-02T09:26:34+00:00",
    "summary": "视频内已经将所有的网站进行打码，没有吐露任何网址，也没有推广违规AI服务\n简介无推广内容\n视频中演示网站有正规ICP备案与ICP许可"
  },
  {
    "id": "bvid:BV17Lap6VEUr",
    "domain": "AI",
    "title": "【全80集】Vibe Coding 零基础入门到实战教程，由浅入深（全程干货）",
    "url": "http://www.bilibili.com/video/av117353572468721",
    "source": "数据拾光屋",
    "platform": "bilibili",
    "points": 42435,
    "published_at": "2026-10-02T09:25:00+00:00",
    "summary": "本套教程专门为零基础学员而制，全程干货无废话，喜欢的小伙伴记得点赞三连喔 ~"
  },
  {
    "id": "bvid:BV1XiD5BQEAj",
    "domain": "AI",
    "title": "Claude Code 接入微信、一行命令把Claude Code装进微信、保姆级教程、微信支持Claude Code（cc-connect）远程开发",
    "url": "http://www.bilibili.com/video/av116350093694897",
    "source": "下班学AI",
    "platform": "bilibili",
    "points": 41206,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV1hmb26ZEws",
    "domain": "AI",
    "title": "DeepSeek Harness 实测  Claude Code 对比后，梁神我错了 差距比我想的大",
    "url": "http://www.bilibili.com/video/av117100337236191",
    "source": "程序员晓刘",
    "platform": "bilibili",
    "points": 36828,
    "published_at": "2026-08-15T16:01:38+00:00",
    "summary": "这期用同一个 DeepSeek Pro 0813 模型，分别在 Claude Code 和 DeepSeek Harness 里完成同样的任务，对比工具链对最终效果的影响。\n实测内容包括：\nFPS 游戏 Demo、灯塔预警沙盘、手枪组装动画、显示器组装动画，以及 DeepSeek Harness 的插件化源码流程。\n整体看下来，模型本身当然重要，但 Harness 在插件化、流程记录、缓存命中和任"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 34641,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1C3jt64EPS",
    "domain": "AI",
    "title": "B站讲的最好的Vibe Coding企业级项目实战教程（2026最新版）从入门到进阶，七天速通Claude Code+Codex+CursorAI工程化编程开发",
    "url": "http://www.bilibili.com/video/av116787425383675",
    "source": "图灵学院诸葛",
    "platform": "bilibili",
    "points": 33085,
    "published_at": "2026-06-21T09:48:04+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n 【本视频笔记代码、大模型最新学习路线、系统学习课程、实战案例、电子书+问题解答等戳这里获取→https://www.bilibili.com/read/cv39576966/?jump_opus=1】"
  },
  {
    "id": "bvid:BV1sQaL6vEkb",
    "domain": "AI",
    "title": "小白向，ai入门第一课：agent的部署和使用！",
    "url": "http://www.bilibili.com/video/av117349378166797",
    "source": "沈三殊",
    "platform": "bilibili",
    "points": 31573,
    "published_at": "2026-09-28T15:30:36+00:00",
    "summary": "详细的agent部署介绍：https://pan.quark.cn/s/3846914c6da7\n欢迎来到ai的世界！！\n有疑问欢迎私信。"
  },
  {
    "id": "bvid:BV13tuqzwEm9",
    "domain": "AI",
    "title": "一个视频彻底掌握ClaudeCode使用MCP",
    "url": "http://www.bilibili.com/video/av114851586252599",
    "source": "创哥的AI实验室",
    "platform": "bilibili",
    "points": 30106,
    "published_at": "2025-07-14T12:32:55+00:00",
    "summary": "Claude Code命令行的方式，让MCP的操作也令很多朋友感觉不适，这个视频专门做了一些介绍。\n\n希望能帮助到大家。"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29926,
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
    "points": 29038,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV11K9gBqEnW",
    "domain": "AI",
    "title": "【杀戮尖塔2】AI MOD 配置教程第一期来辣！手把手教你怎么改提示词！以及如何设计自己的爬塔玩法",
    "url": "http://www.bilibili.com/video/av116341654755924",
    "source": "分歧点WhatIf",
    "platform": "bilibili",
    "points": 28724,
    "published_at": "2026-04-03T16:14:43+00:00",
    "summary": "每个参数都是干什么的，如何修改提示词的教程。\n不知道这是什么？请看合集内的视频~\n我做了一个 AI 的杀戮尖塔2MOD！\n可以和怪物对话，策反怪物，带着怪物爬塔（重写了几乎每一个怪物在友方时候的行为），还能给怪物打防御，带个沙虫全吃了！\n可以和上古之民对话，聊嗨了会给你 1～2 个额外赐福，还能帮你指示为未来\n可以让偷窃草蜢偷队友的 key 卡，想无限？偷了！\n可以和商人讨价还价，甚至白嫖\n多人的"
  },
  {
    "id": "bvid:BV1B97868EZK",
    "domain": "AI",
    "title": "Claude Code全流程开发实战丨MCP实战、Skills+Agent多工具协作、AI编程、自动化工作流、私有化部署、转行AI岗",
    "url": "http://www.bilibili.com/video/av116810192131401",
    "source": "博学谷",
    "platform": "bilibili",
    "points": 27153,
    "published_at": "2026-06-25T10:11:09+00:00",
    "summary": "视频配套资源领取方式戳：https://www.bilibili.com/opus/1217780115004456969\n或关注【博学谷】公综号回复关键词领取：260625\n学完本课程，你将能够独立完成AI Agent 研发与落地：深度掌握 Claude Code 辅助编程、Skill 技能包编排与 MCP 协议集成打通私有系统连接的“桥梁”，并能学会私有化部署。最终凭借“AI Coding 重"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 26231,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 25731,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22847,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:50362905",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia RTX Spark encrypted firmware slows inference speed to 35% on Linux",
    "url": "https://www.mindstudio.ai/blog/linux-nvidia-rtx-spark-laptop",
    "source": "novaRom",
    "platform": "hackernews",
    "points": 600,
    "published_at": "2026-11-04T08:46:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:50293047",
    "domain": "AI 算力 / 半导体",
    "title": "Alleged Chinese spy had 'close relationship' with Nvidia boss Jensen Huang",
    "url": "https://nypost.com/2026/10/29/business/alleged-chinese-spy-had-close-relationship-with-nvidia-boss-jensen-huang-report/",
    "source": "mgh2",
    "platform": "hackernews",
    "points": 360,
    "published_at": "2026-10-29T17:43:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:50219700",
    "domain": "AI 算力 / 半导体",
    "title": "GPU-unlock: FP/BF16 instruction issue rate on Nvidia 3000's cards",
    "url": "https://github.com/Zagitta/gpu-unlock",
    "source": "fragebogen",
    "platform": "hackernews",
    "points": 353,
    "published_at": "2026-10-24T09:58:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:50348962",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia – open-source auto-ontology",
    "url": "https://github.com/NVIDIA/auto-ontology",
    "source": "campervans",
    "platform": "hackernews",
    "points": 288,
    "published_at": "2026-11-03T07:04:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:50327058",
    "domain": "AI 算力 / 半导体",
    "title": "Seoul Viosys begins production of rare-earth-free white light emitter",
    "url": "https://www.semiconductor-today.com/news_items/2026/oct/seoul-291026.shtml",
    "source": "gmays",
    "platform": "hackernews",
    "points": 193,
    "published_at": "2026-11-01T16:23:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:50236073",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia and Micron Make Up 34% of America's Earnings Boom",
    "url": "https://www.wsj.com/finance/stocks/the-earnings-boom-is-heavily-reliant-on-just-a-handful-of-stocks-21decb53",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 176,
    "published_at": "2026-10-25T21:07:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:50275128",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Nemotron 3.5 Transcribe: open ASR for 40 languages",
    "url": "https://huggingface.co/blog/nvidia/nemotron-transcribe-granary",
    "source": "wondersky",
    "platform": "hackernews",
    "points": 134,
    "published_at": "2026-10-28T15:17:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:50363861",
    "domain": "AI 算力 / 半导体",
    "title": "RTX 5090 Street Prices Top $9k as Nvidia GPU Costs Climb",
    "url": "https://aroundprague.cz/en/news/us/rtx-5090-street-prices-top-9-000-as-nvidia-gpu-costs-climb",
    "source": "teleforce",
    "platform": "hackernews",
    "points": 61,
    "published_at": "2026-11-04T11:02:23+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/why-magnetic-sensor-selection-has-become-a-system-architecture-decision/",
    "domain": "AI 算力 / 半导体",
    "title": "Why Magnetic Sensor Selection Has Become a System Architecture Decision",
    "url": "https://www.eetimes.com/why-magnetic-sensor-selection-has-become-a-system-architecture-decision/",
    "source": "Christopher McGrady",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T09:00:00+00:00",
    "summary": "Kiloampere busbars, 2,000 V solar platforms, hollow-shaft robot joints and nanoamp standby budgets are pulling magnetic sensing in directions no single sensing principle can follow. Ask a traction inv"
  },
  {
    "id": "rss:https://www.eetimes.com/what-makes-a-quantum-company-valuable/",
    "domain": "AI 算力 / 半导体",
    "title": "What Makes a Quantum Company Valuable?",
    "url": "https://www.eetimes.com/what-makes-a-quantum-company-valuable/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T07:00:28+00:00",
    "summary": "Quantum investors weigh technical progress against customer demand, commercial timing, and the ability to build lasting value. The post What Makes a Quantum Company Valuable? appeared first on EE Time"
  },
  {
    "id": "rss:https://www.eetimes.com/chiplets-meta-scale-chiplet-velocity-accelerating-ai-soc-development-to-match-the-rapid-evolution-of-ai-model/",
    "domain": "AI 算力 / 半导体",
    "title": "Chiplets: Meta-Scale Chiplet Velocity Accelerating AI SoC Development to Match the Rapid Evolution of AI Model",
    "url": "https://www.eetimes.com/chiplets-meta-scale-chiplet-velocity-accelerating-ai-soc-development-to-match-the-rapid-evolution-of-ai-model/",
    "source": "AspenCore Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T20:30:12+00:00",
    "summary": "This event session is presented by Olivia Wu, Distinguished Engineer at Meta AI model architectures are evolving faster than traditional chip development cycles, and at Meta&#8217;s scale—serving bill"
  },
  {
    "id": "rss:https://www.eetimes.com/silicon-photonics-hits-the-big-time/",
    "domain": "AI 算力 / 半导体",
    "title": "Silicon Photonics Hits the Big Time",
    "url": "https://www.eetimes.com/silicon-photonics-hits-the-big-time/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T19:51:38+00:00",
    "summary": "The land grab for silicon photonics aims to beat the power wall associated with copper interconnects. We also interviewed Salience Labs about its $125 million funding for optical circuit switching. Th"
  },
  {
    "id": "rss:https://www.eetimes.com/ablics-small-smart-and-simple-strategy-for-high-value-analog-semicondutors/",
    "domain": "AI 算力 / 半导体",
    "title": "ABLIC’s Small, Smart, and Simple Strategy for High-Value Analog Semicondutors",
    "url": "https://www.eetimes.com/ablics-small-smart-and-simple-strategy-for-high-value-analog-semicondutors/",
    "source": "ABLIC",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T17:00:00+00:00",
    "summary": "ABLIC’s Satoshi Hanazawa discusses its low-power analog semiconductor strategy, target markets, product innovation and development approach. The post ABLIC&#8217;s Small, Smart, and Simple Strategy fo"
  },
  {
    "id": "rss:https://www.eetimes.com/stmicroelectronics-expands-stm32-roadmap-for-cloud-ai-and-physical-ai/",
    "domain": "AI 算力 / 半导体",
    "title": "STMicroelectronics Expands STM32 Roadmap for Cloud AI and Physical AI",
    "url": "https://www.eetimes.com/stmicroelectronics-expands-stm32-roadmap-for-cloud-ai-and-physical-ai/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T14:37:17+00:00",
    "summary": "Unified STM32 platform adds automotive-grade STM32A and power-focused STM32G5 MCUs. The post STMicroelectronics Expands STM32 Roadmap for Cloud AI and Physical AI appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/quantum-roadmaps-are-finally-meeting-reality/",
    "domain": "AI 算力 / 半导体",
    "title": "Quantum Roadmaps Are Finally Meeting Reality",
    "url": "https://www.eetimes.com/quantum-roadmaps-are-finally-meeting-reality/",
    "source": "Marie Lepske",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T09:11:15+00:00",
    "summary": "Quantum computing revenue surpassed $1 billion in 2025, but missed forecasts highlight the gap between commercial expectations and delivery. The post Quantum Roadmaps Are Finally Meeting Reality appea"
  },
  {
    "id": "rss:https://www.eetimes.com/is-there-room-for-small-scale-osats-in-india-chip-packaging-boom/",
    "domain": "AI 算力 / 半导体",
    "title": "Is There Room for Small-Scale OSATs in India’s Chip Packaging Boom?",
    "url": "https://www.eetimes.com/is-there-room-for-small-scale-osats-in-india-chip-packaging-boom/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T23:30:00+00:00",
    "summary": "Small OSATs in India can start with ₹1.5–₹2 billion (~$15.8–$21 million), consultant Nitin Dodia said. But anchor customers, skilled staff, and qualification determine who survives. The post Is There "
  },
  {
    "id": "rss:https://www.eetimes.com/u-s-manufacturing-activity-gains-momentum-in-october/",
    "domain": "AI 算力 / 半导体",
    "title": "U.S. Manufacturing Activity Gains Momentum in October",
    "url": "https://www.eetimes.com/u-s-manufacturing-activity-gains-momentum-in-october/",
    "source": "News Desk",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T19:08:38+00:00",
    "summary": "Economic activity in the U.S. manufacturing sector expanded in October driven by accelerating production and steady gains in new orders. The post U.S. Manufacturing Activity Gains Momentum in October "
  },
  {
    "id": "rss:https://www.eetimes.com/accepting-orders-for-the-led-light-sourced-projection-aligners/",
    "domain": "AI 算力 / 半导体",
    "title": "Accepting Orders for the LED Light-Sourced Projection Aligners",
    "url": "https://www.eetimes.com/accepting-orders-for-the-led-light-sourced-projection-aligners/",
    "source": "USHIO INC.",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T15:54:08+00:00",
    "summary": "Ushio has been accepting orders for LED-based UX-4 wafer aligners since July 2026, offering mercury-free, high-throughput lithography. The post Accepting Orders for the LED Light-Sourced Projection Al"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/nintendo/nintendo-rom-chip-supplier-macronix-quits-to-focus-on-chips-for-ai-data-centers-game-key-cards-may-be-more-available-as-large-game-storage-chips-become-more-expensive",
    "domain": "AI 算力 / 半导体",
    "title": "Nintendo ROM chip supplier Macronix quits to focus on chips for AI data centers, reports indicate",
    "url": "https://www.tomshardware.com/video-games/nintendo/nintendo-rom-chip-supplier-macronix-quits-to-focus-on-chips-for-ai-data-centers-game-key-cards-may-be-more-available-as-large-game-storage-chips-become-more-expensive",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T17:10:59+00:00",
    "summary": "Macronix, one of Nintendo's ROM chip manufacturers, is shutting down the business to reallocate manufacturing for NOR and NAND flash chips that the AI industry demands."
  },
  {
    "id": "rss:https://www.tomshardware.com/service-providers/network-providers/t-mobile-launches-usd90-5-gbps-fiber-internet-plan-2-5x-speed-boost-comes-with-10-year-price-guarantee",
    "domain": "AI 算力 / 半导体",
    "title": "T-Mobile launches $90 5 Gbps fiber internet plan",
    "url": "https://www.tomshardware.com/service-providers/network-providers/t-mobile-launches-usd90-5-gbps-fiber-internet-plan-2-5x-speed-boost-comes-with-10-year-price-guarantee",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T16:50:33+00:00",
    "summary": "T-Mobile is offering up to 5 Gbps fiber internet for less than $100/month"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/team-group-ceo-warns-memory-crisis-could-reach-point-where-even-money-cant-buy-goods-will-get-worse-next-year-with-no-downward-trend-in-price-whatsoever",
    "domain": "AI 算力 / 半导体",
    "title": "Team Group CEO warns memory crisis could reach point where 'even money can't buy goods' — will get worse next year, with 'no downward trend in price whatsoever'",
    "url": "https://www.tomshardware.com/pc-components/dram/team-group-ceo-warns-memory-crisis-could-reach-point-where-even-money-cant-buy-goods-will-get-worse-next-year-with-no-downward-trend-in-price-whatsoever",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T15:28:30+00:00",
    "summary": "“How can prices fall when there’s nothing left?” Team Group CEO Chen Ching-wen said during the company's earnings call."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-mice/logitech-g-pro-x3-superstrike-review",
    "domain": "AI 算力 / 半导体",
    "title": "Logitech G Pro X3 Superstrike Review: $200 for the illusion of a click",
    "url": "https://www.tomshardware.com/peripherals/gaming-mice/logitech-g-pro-x3-superstrike-review",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T15:00:00+00:00",
    "summary": "Logitech's G Pro X3 Superstrike is a minor but noticeable update to its revolutionary mouse — there's a new chipset and the weight has been rebalanced, so it lasts longer and feels better. And it cost"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/thermal-paste/thermal-grizzly-launches-phasesheet-ptm-pro-with-improved-thermal-conductivity-new-thermal-pad-promises-easier-installation-and-better-cooling-performance",
    "domain": "AI 算力 / 半导体",
    "title": "Thermal Grizzly launches PhaseSheet PTM Pro with improved thermal conductivity — new thermal pad promises easier installation and better cooling performance",
    "url": "https://www.tomshardware.com/pc-components/thermal-paste/thermal-grizzly-launches-phasesheet-ptm-pro-with-improved-thermal-conductivity-new-thermal-pad-promises-easier-installation-and-better-cooling-performance",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T14:36:13+00:00",
    "summary": "Designed for CPUs, GPUs, and other components without an integrated heat spreader, the PhaseSheet PTM Pro is reusable, electrically non-conductive, and less susceptible to the pump-out effect associat"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/micron-details-ambitious-dram-and-nand-roadmap-3d-nand-high-na-euv-new-materials-and-custom-silicon-makes-a-comeback",
    "domain": "AI 算力 / 半导体",
    "title": "Micron details ambitious DRAM and NAND roadmap — 3D NAND, High-NA EUV, new materials, and custom silicon makes a comeback",
    "url": "https://www.tomshardware.com/pc-components/dram/micron-details-ambitious-dram-and-nand-roadmap-3d-nand-high-na-euv-new-materials-and-custom-silicon-makes-a-comeback",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T14:00:00+00:00",
    "summary": "As DRAM and 3D NAND are about to adopt all-new technologies, custom types of memory are about to become mainstream as AI developers face limitations with current solutions."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/ai-data-centers-comprehensively-defeated-at-us-midterm-elections-45-measures-put-on-the-ballot-as-americans-overwhelmingly-vote-against-developments",
    "domain": "AI 算力 / 半导体",
    "title": "AI data centers comprehensively defeated at US midterm elections — 45 measures put on the ballot as Americans overwhelmingly vote against developments",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/ai-data-centers-comprehensively-defeated-at-us-midterm-elections-45-measures-put-on-the-ballot-as-americans-overwhelmingly-vote-against-developments",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T13:13:32+00:00",
    "summary": "Several counties put data center issues on the ballot during the midterm elections, with most Americans voting against data center development in their county."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cryptocurrency/binance-heist-began-with-fake-job-interviews-and-a-malicious-homebrew-download-attackers-used-adulterated-software-and-social-engineering-to-gain-access-to-billions-in-assets",
    "domain": "AI 算力 / 半导体",
    "title": "Binance heist began with fake job interviews and a malicious Homebrew download",
    "url": "https://www.tomshardware.com/tech-industry/cryptocurrency/binance-heist-began-with-fake-job-interviews-and-a-malicious-homebrew-download-attackers-used-adulterated-software-and-social-engineering-to-gain-access-to-billions-in-assets",
    "source": "Newton Gitonga",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T13:00:00+00:00",
    "summary": "Binance has revealed how Norh Korean attackers spent months compromising systems and employees with malicious developer software and a fake recruitment process. The intrusions eventually gave hackers "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/php-vulnerability-post-mortem-reveals-bug-was-known-two-years-ago-small-team-of-maintainers-knew-of-the-issue-before-it-was-made-public-as-new-php2shell-chained-exploit-ravages-servers",
    "domain": "AI 算力 / 半导体",
    "title": "PHP vulnerability post-mortem reveals bug was known two years ago — Small team of maintainers knew of the issue before it was made public, as new PHP2Shell chained exploit ravages servers",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/php-vulnerability-post-mortem-reveals-bug-was-known-two-years-ago-small-team-of-maintainers-knew-of-the-issue-before-it-was-made-public-as-new-php2shell-chained-exploit-ravages-servers",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T12:30:00+00:00",
    "summary": "PHP has a harvest season to remember — AI-automated bug hunting reaps what years of technical debt have sown."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-can-only-fulfill-1-percent-of-chinas-massive-usd70-billion-gpu-order-for-ai-chips-report-claims-supply-constraints-choke-export-friendly-rtx-pro-5500-deliveries-despite-huge-demand",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia can only fulfill 1% of China’s massive $70 billion GPU order for AI chips, report claims — supply constraints choke export-friendly RTX Pro 5500 deliveries despite huge demand",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-can-only-fulfill-1-percent-of-chinas-massive-usd70-billion-gpu-order-for-ai-chips-report-claims-supply-constraints-choke-export-friendly-rtx-pro-5500-deliveries-despite-huge-demand",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T12:15:00+00:00",
    "summary": "Just 1% of chips promised to major Chinese companies to power their AI ambitions will be delivered, according to reports."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpu-drivers/open-source-project-renders-your-windows-11-desktop-using-the-npu-rather-than-the-gpu-npu-driver-can-only-run-at-2-to-3-hz-targets-30-hz-performance",
    "domain": "AI 算力 / 半导体",
    "title": "Open source project renders your Windows 11 desktop using the NPU rather than the GPU — ‘npu-driver’ can only run at 2 to 3 Hz, targets 30 Hz performance",
    "url": "https://www.tomshardware.com/pc-components/gpu-drivers/open-source-project-renders-your-windows-11-desktop-using-the-npu-rather-than-the-gpu-npu-driver-can-only-run-at-2-to-3-hz-targets-30-hz-performance",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T12:00:00+00:00",
    "summary": "Open source developers have released a prototype driver for Windows 11 that renders the desktop using an NPU instead of the system’s (i)GPU."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/cloudflare-engineers-optimize-dns-build-services-for-twice-the-speed-and-85-percent-lower-ram-usage-finer-grained-processes-only-do-work-and-data-movement-thats-needed",
    "domain": "AI 算力 / 半导体",
    "title": "Cloudflare engineers optimize DNS build services for twice the speed and 85% lower RAM usage",
    "url": "https://www.tomshardware.com/networking/cloudflare-engineers-optimize-dns-build-services-for-twice-the-speed-and-85-percent-lower-ram-usage-finer-grained-processes-only-do-work-and-data-movement-thats-needed",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T12:00:00+00:00",
    "summary": "Cloudflare engineers are at it again, optimizing DNS-building services for twice the speed and 85% less RAM usage"
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/upgrade-to-an-oled-display-for-only-usd269-at-walmart-acers-27-inch-nitro-gaming-monitor-has-a-superfast-240hz-refresh-rate-and-crisp-wqhd-resolution",
    "domain": "AI 算力 / 半导体",
    "title": "Upgrade to an OLED display for only $269 at Walmart — Acer's 27-inch Nitro gaming monitor has a superfast 240Hz refresh rate and crisp WQHD resolution",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/upgrade-to-an-oled-display-for-only-usd269-at-walmart-acers-27-inch-nitro-gaming-monitor-has-a-superfast-240hz-refresh-rate-and-crisp-wqhd-resolution",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T11:51:07+00:00",
    "summary": "Switch to a QD-OLED gaming monitor for just $269. This Walmart bargain nets you a 27-inch QHD display with a super-fast 240Hz refresh rate."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/applications/disgruntled-software-developers-start-ambitious-open-source-revolt-using-ai-to-clone-common-services-occupysaas-ai-powered-project-wants-to-kick-auth0-salesforce-and-other-pricy-service-as-software-to-the-curb",
    "domain": "AI 算力 / 半导体",
    "title": "Disgruntled software developers start ambitious open-source revolt, using AI to clone common services",
    "url": "https://www.tomshardware.com/software/applications/disgruntled-software-developers-start-ambitious-open-source-revolt-using-ai-to-clone-common-services-occupysaas-ai-powered-project-wants-to-kick-auth0-salesforce-and-other-pricy-service-as-software-to-the-curb",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T11:30:00+00:00",
    "summary": "OccupySaaS AI-powered project wants to kick Auth0, Salesforce, and other pricy service-as-software to the curb"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-usd300-on-this-1440p-gaming-pc-with-a-9800x3d-and-rtx-5070-right-now-pre-built-cyberpowerpc-machine-ships-with-32gb-ddr5-and-a-2tb-ssd-for-just-usd2-199-99",
    "domain": "AI 算力 / 半导体",
    "title": "Save $300 on this 1440p gaming PC with a 9800X3D and RTX 5070 right now",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-usd300-on-this-1440p-gaming-pc-with-a-9800x3d-and-rtx-5070-right-now-pre-built-cyberpowerpc-machine-ships-with-32gb-ddr5-and-a-2tb-ssd-for-just-usd2-199-99",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T11:26:04+00:00",
    "summary": "Grab a CyberPowerPC machine wtih an RTX 5070, 9800X3D, 32GB DDR5 and a 2TB SSD for $2,199."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-expects-to-outsell-intel-in-q4-for-the-first-time-in-history-usd17b-guidance-would-exceed-intels-projections",
    "domain": "AI 算力 / 半导体",
    "title": "AMD expects to outsell Intel in Q4 for the first time in history",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-expects-to-outsell-intel-in-q4-for-the-first-time-in-history-usd17b-guidance-would-exceed-intels-projections",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T11:15:00+00:00",
    "summary": "AMD's data center business surges as strong demand for Epyc processors and Instinct accelerators continues and sales of client hardware declines only slightly."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/certified-android-tv-manufacturer-put-unauthorized-backdoor-in-set-top-boxes-google-reveals-oem-sold-access-to-criminal-affiliates-for-1-3-million-devices-used-massive-network-as-botnet-for-ad-fraud-residential-proxy",
    "domain": "AI 算力 / 半导体",
    "title": "Certified Android TV manufacturer put unauthorized backdoor in 1.3 million set-top boxes, Google reveals",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/certified-android-tv-manufacturer-put-unauthorized-backdoor-in-set-top-boxes-google-reveals-oem-sold-access-to-criminal-affiliates-for-1-3-million-devices-used-massive-network-as-botnet-for-ad-fraud-residential-proxy",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T11:00:00+00:00",
    "summary": "Google discovered and shut down a backdoor built into millions of Google TV and Android TV set-top boxes built by Videostrong Technology Co."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/us-army-successfully-flies-a-hybrid-electric-drone-with-3d-printed-heavy-fuel-rotary-engine-400v-motor-generator-uses-advanced-engineering-to-ditch-a-bulky-liquid-cooling-system",
    "domain": "AI 算力 / 半导体",
    "title": "US Army successfully flies a hybrid electric drone with 3D-printed heavy-fuel rotary engine — uses advanced engineering to ditch a bulky liquid cooling system",
    "url": "https://www.tomshardware.com/tech-industry/drones/us-army-successfully-flies-a-hybrid-electric-drone-with-3d-printed-heavy-fuel-rotary-engine-400v-motor-generator-uses-advanced-engineering-to-ditch-a-bulky-liquid-cooling-system",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T10:30:00+00:00",
    "summary": "The US Army VICTOR drone uses an optimized heavy-fuel rotary engine developed with metal 3D printing for rapid prototyping."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/windows-11-8gb-ram-configurations-get-a-performance-boost-as-ai-demand-keeps-pushing-prices-up-microsoft-says-windows-is-now-20-percent-more-responsive-multitasking-40-percent-faster-on-memory-constrained-machines",
    "domain": "AI 算力 / 半导体",
    "title": "Windows 11 8GB RAM configurations get a performance boost",
    "url": "https://www.tomshardware.com/software/windows/windows-11-8gb-ram-configurations-get-a-performance-boost-as-ai-demand-keeps-pushing-prices-up-microsoft-says-windows-is-now-20-percent-more-responsive-multitasking-40-percent-faster-on-memory-constrained-machines",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T17:00:00+00:00",
    "summary": "Microsoft claims that it has made drastic improvements to the performance of Windows 11 while using 8GB of RAM."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/openai-introduces-program-to-reduce-ai-data-center-energy-demand-during-peak-hours-company-testing-grid-protectors-program-system-in-georgia",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI introduces program to reduce AI data center energy demand during peak hours",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/openai-introduces-program-to-reduce-ai-data-center-energy-demand-during-peak-hours-company-testing-grid-protectors-program-system-in-georgia",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T15:56:51+00:00",
    "summary": "The Grid Protectors Program applies load shedding, a technique in use since the 1970s, to data centers."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/intel-14a-moves-closer-to-production-as-pdk-0-9-becomes-available-process-design-kit-gives-developers-important-production-milestone-ahead-of-1-0-in-2027",
    "domain": "AI 算力 / 半导体",
    "title": "Intel 14A moves closer to production as PDK 0.9 becomes available",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/intel-14a-moves-closer-to-production-as-pdk-0-9-becomes-available-process-design-kit-gives-developers-important-production-milestone-ahead-of-1-0-in-2027",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T15:20:27+00:00",
    "summary": "Intel says its next-generation process technology is reaching expected performance and yield maturity."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/elon-musks-xai-installs-eight-converted-jet-engines-to-power-mississippi-data-center-permits-allow-25-percent-higher-limit-for-pollutants-concerns-raised-over-carbon-monoxide",
    "domain": "AI 算力 / 半导体",
    "title": "8 converted jet engines are powering xAI data centers as companies look for new energy sources",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/elon-musks-xai-installs-eight-converted-jet-engines-to-power-mississippi-data-center-permits-allow-25-percent-higher-limit-for-pollutants-concerns-raised-over-carbon-monoxide",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T15:02:09+00:00",
    "summary": "A Mississippi xAI data center is using eight converted jet engine turbines as a power source despite the known health risks of the carbon monoxide and volatile organic compounds they produce."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/apple-faces-unprecedented-memory-cost-increases-as-ram-prices-continue-to-surge-manufacturing-bill-climbs-by-usd33-billion-rising-component-expenses-threaten-margins-through-the-holiday-quarter-and-into-2027",
    "domain": "AI 算力 / 半导体",
    "title": "Apple faces unprecedented memory cost increases as RAM prices continue to surge, manufacturing bill climbs by $33 billion",
    "url": "https://www.tomshardware.com/pc-components/dram/apple-faces-unprecedented-memory-cost-increases-as-ram-prices-continue-to-surge-manufacturing-bill-climbs-by-usd33-billion-rising-component-expenses-threaten-margins-through-the-holiday-quarter-and-into-2027",
    "source": "Newton Gitonga",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T14:28:59+00:00",
    "summary": "Samsung, SK hynix, and Micron are facing strong demand for memory from AI data centers, prompting manufacturers to prioritize higher-margin server products and high-bandwidth memory. That shift is tig"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/docking-stations-hubs/hands-on-with-the-dockcase-mount-ling-2-pro-handheld-dock-with-a-built-in-capture-card-and-space-for-up-to-4tb-of-nvme-storage",
    "domain": "AI 算力 / 半导体",
    "title": "Hands-on with the DockCase Mount Ling 2 Pro",
    "url": "https://www.tomshardware.com/peripherals/docking-stations-hubs/hands-on-with-the-dockcase-mount-ling-2-pro-handheld-dock-with-a-built-in-capture-card-and-space-for-up-to-4tb-of-nvme-storage",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T14:20:22+00:00",
    "summary": "The Mount Ling 2 Pro is a dock for Nintendo Switch 2, Steam Deck, or other PC handhelds that doubles as a capture card and a vehicle for up to 4TB of NVMe SSD storage."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/bambu-lab-h3c-3d-printer-review",
    "domain": "AI 算力 / 半导体",
    "title": "Bambu Lab H3C 3D printer review: A nine-tool monster",
    "url": "https://www.tomshardware.com/3d-printing/bambu-lab-h3c-3d-printer-review",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T14:00:00+00:00",
    "summary": "The Bambu Lab H3C is a massive tool changer that handles TPU like nobody’s business."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/nvidia-tells-data-center-operators-to-limit-business-from-chinese-customers-with-new-global-restrictions-report-claims-allegedly-restricted-to-49-percent-of-the-total-ensuring-51-percent-are-non-chinese-outfits",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia tells data center operators to limit business from Chinese customers with new global restrictions, report claims",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/nvidia-tells-data-center-operators-to-limit-business-from-chinese-customers-with-new-global-restrictions-report-claims-allegedly-restricted-to-49-percent-of-the-total-ensuring-51-percent-are-non-chinese-outfits",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T13:31:11+00:00",
    "summary": "Nvidia has told cloud providers who use its data center products that they must sell less than half of their services to Chinese companies as part of a new policy that will further impact China's abil"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/corsair-has-slashed-usd180-off-its-blistering-mp700-se-gen-5-ssd-now-14-cents-per-gb-get-4tb-of-ssd-storage-for-usd579-the-cheapest-drive-on-the-market",
    "domain": "AI 算力 / 半导体",
    "title": "Corsair has slashed $180 off its blistering MP700 SE Gen 5 SSD",
    "url": "https://www.tomshardware.com/pc-components/ssds/corsair-has-slashed-usd180-off-its-blistering-mp700-se-gen-5-ssd-now-14-cents-per-gb-get-4tb-of-ssd-storage-for-usd579-the-cheapest-drive-on-the-market",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T13:25:30+00:00",
    "summary": "The 4TB Corsair MP 700 Pro SE is $180 off, the cheapest 4TB Gen 5 SSD you can buy right now."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/google-reveals-new-gemini-4-carbon-ai-model-narrowly-beating-claude-opus-5-5-frontier-ai-model-is-also-the-least-likely-to-hallucinate-benchmarks-claim",
    "domain": "AI 算力 / 半导体",
    "title": "Google reveals new Gemini 4 Carbon AI model, narrowly beating Claude Opus 5.5",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/google-reveals-new-gemini-4-carbon-ai-model-narrowly-beating-claude-opus-5-5-frontier-ai-model-is-also-the-least-likely-to-hallucinate-benchmarks-claim",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T13:00:00+00:00",
    "summary": "Last week, Google released its latest AI model, Gemini 4 Carbon, topping intelligence rankings charts."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/china-deploys-worlds-first-800-volt-dc-power-system-for-massive-ai-data-center-seeks-to-quench-power-needs-with-higher-conversion-and-efficiency-inside-a-smaller-footprint",
    "domain": "AI 算力 / 半导体",
    "title": "China deploys 'world's first' 800-volt DC power system for massive AI data center",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/china-deploys-worlds-first-800-volt-dc-power-system-for-massive-ai-data-center-seeks-to-quench-power-needs-with-higher-conversion-and-efficiency-inside-a-smaller-footprint",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T12:40:09+00:00",
    "summary": "Firm says it has completed the world’s first commercial data center deployment of an integrated 800-volt DC power system."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/chinese-survey-ship-loitering-near-undersea-cable-ignores-philippine-demands-to-withdraw-evasive-action-point-to-growing-prc-threats-to-data-lines-in-the-pacific",
    "domain": "AI 算力 / 半导体",
    "title": "Chinese survey ship loitering near undersea cable ignores Philippine demands to withdraw",
    "url": "https://www.tomshardware.com/tech-industry/chinese-survey-ship-loitering-near-undersea-cable-ignores-philippine-demands-to-withdraw-evasive-action-point-to-growing-prc-threats-to-data-lines-in-the-pacific",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T12:31:11+00:00",
    "summary": "A Chinese research vessel ignored the Philippine coast guard's attempts to move it as it loitered over an undersea cable near its coast as the PRC continues to use civilian vessels as \"gray-zone\" warf"
  },
  {
    "id": "hn:50247677",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia discusses $2k-per-GPU annual fee for software",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-discusses-usd2-000-per-gpu-annual-software-fee-for-running-agents-on-ai-infrastructure-firm-already-charges-more-than-twice-that-amount-for-its-ai-enterprise-software-platform",
    "source": "gscott",
    "platform": "hackernews",
    "points": 41,
    "published_at": "2026-10-26T17:34:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:50128597",
    "domain": "AI 算力 / 半导体",
    "title": "EU negotiates sanctions swap with China to rescue critical ASML supplier",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/eu-negotiates-sanction-swap-with-china-to-rescue-critical-asml-supplier-german-coatings-firm-faces-shutdown-without-chinese-rare-earths",
    "source": "anigbrowl",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-10-17T06:49:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:50073879",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon",
    "url": "https://deepmind.google/models/gemini/",
    "source": "737max",
    "platform": "hackernews",
    "points": 1467,
    "published_at": "2026-10-13T16:03:16+00:00",
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
    "id": "hn:50363461",
    "domain": "大厂 AI 动态",
    "title": "Tell HN: Gemini trains on chat history, even for subscribers (personal accounts)",
    "url": "https://news.ycombinator.com/item?id=50363461",
    "source": "jameslk",
    "platform": "hackernews",
    "points": 670,
    "published_at": "2026-11-04T10:10:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:50288019",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Carbon is the new #1 on the Artificial Analysis Intelligence Index v5",
    "url": "https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1",
    "source": "theHocineSaad",
    "platform": "hackernews",
    "points": 338,
    "published_at": "2026-10-29T12:41:56+00:00",
    "summary": ""
  },
  {
    "id": "hn:50122431",
    "domain": "大厂 AI 动态",
    "title": "Llama.cpp on a jailbroken PS5: run any GGUF model natively on the console",
    "url": "https://github.com/cobanov/PS5LM",
    "source": "Anon84",
    "platform": "hackernews",
    "points": 375,
    "published_at": "2026-10-16T18:32:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:50118688",
    "domain": "大厂 AI 动态",
    "title": "Show HN: Gemini 4 Argon plays StarCraft",
    "url": "https://starskirmish.com/bench/v0-2/",
    "source": "__cayenne__",
    "platform": "hackernews",
    "points": 254,
    "published_at": "2026-10-16T14:18:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:50074869",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon for Robotics",
    "url": "https://developers.googleblog.com/gemini-4-argon-for-robotics/",
    "source": "xnx",
    "platform": "hackernews",
    "points": 235,
    "published_at": "2026-10-13T16:55:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:50355504",
    "domain": "大厂 AI 动态",
    "title": "Google researchers demand freedom to tell the world what they know about AI",
    "url": "https://www.washingtonpost.com/technology/2026/11/03/google-deepmind-staff-protest-lifetime-ban-criticizing-company/",
    "source": "nsagent",
    "platform": "hackernews",
    "points": 91,
    "published_at": "2026-11-03T17:55:26+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/games/1026380/zelda-ocarina-of-time-interview-eiji-aonuma-hidemaro-fujibayashi",
    "domain": "大厂 AI 动态",
    "title": "Nintendo’s designers strove for ‘elegance’ when remaking Ocarina of Time",
    "url": "https://www.theverge.com/games/1026380/zelda-ocarina-of-time-interview-eiji-aonuma-hidemaro-fujibayashi",
    "source": "Andrew Webster",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T05:00:00+00:00",
    "summary": "The Ocarina of Time remake on the Switch 2 smashes together the past and present. The game retains much of the original N64 experience while updating it with modern graphics and gameplay that make it "
  },
  {
    "id": "rss:https://www.theverge.com/tech/1027113/x-says-its-updated-web-app-is-way-faster",
    "domain": "大厂 AI 动态",
    "title": "X says its updated web app is way faster",
    "url": "https://www.theverge.com/tech/1027113/x-says-its-updated-web-app-is-way-faster",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T00:25:12+00:00",
    "summary": "X is introducing a new version of its web app that it says is much faster than before, and it's now rolling out the updated app \"one country at a time\" for signed-in users. \"Open a profile on X.com ov"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1026867/qualcomm-earnings-data-centers",
    "domain": "大厂 AI 动态",
    "title": "Qualcomm is betting big on data centers as smartphone sales sink",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1026867/qualcomm-earnings-data-centers",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T22:42:15+00:00",
    "summary": "With smartphone sales tanking by around 20 percent compared to 2025, Qualcomm is looking to data centers to help boost its bottom line. During its Q4 2026 earnings call, the company laid out its plans"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1026878/not-even-good-at-being-rich",
    "domain": "大厂 AI 动态",
    "title": "17 better ways Elon Musk could have wasted $446 million",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1026878/not-even-good-at-being-rich",
    "source": "Elizabeth Lopatto",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T21:45:00+00:00",
    "summary": "One of the basic problems of spending too much time on social media is that you are cooking your brain by reading posts from a pack of attention-seeking lunatics. If your social media of choice is the"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1026743/bright-colorful-phone-grip-case",
    "domain": "大厂 AI 动态",
    "title": "How I learned to love an obnoxious phone grip",
    "url": "https://www.theverge.com/tech/1026743/bright-colorful-phone-grip-case",
    "source": "Allison Johnson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T21:30:00+00:00",
    "summary": "Much like a great recipe, it started with a stick of butter. This wasn't real butter; it was a friend's new phone grip, complemented by a phone case with bold stripes. Butter is in vogue now, or at le"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1026807/bose-quietcomfort-headphones-wireless-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Bose’s QuietComfort Headphones are more than half off",
    "url": "https://www.theverge.com/gadgets/1026807/bose-quietcomfort-headphones-wireless-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T21:13:11+00:00",
    "summary": "It’s not often that some of the best noise-canceling headphones you can buy are over half off. But right now, the first-gen Bose QuietComfort Headphones are on sale for $169.99 ($190 off) at Amazon, B"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1026787/att-gemini-for-home-connected-life-security-system",
    "domain": "大厂 AI 动态",
    "title": "Gemini for Home now plugs into AT&#038;T’s smart security system",
    "url": "https://www.theverge.com/tech/1026787/att-gemini-for-home-connected-life-security-system",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T20:23:24+00:00",
    "summary": "AT&#38;T's smart home security system now integrates with Gemini for Home. The company says its Connected Life system is the \"first\" home security product to integrate with Google Home Premium, enabli"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1025370/google-pixel-11-pro-phone-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Google’s Pixel 11 phones are up to 27 percent off",
    "url": "https://www.theverge.com/gadgets/1025370/google-pixel-11-pro-phone-deal-sale",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T19:00:00+00:00",
    "summary": "You can save a heck of lot of money on Google’s Pixel 11 phones through November 8th, whether you want the best-for-the-least Pixel 11, or the slightly pricier Pixel 11 Pro that takes better photos. E"
  },
  {
    "id": "rss:https://www.theverge.com/news/1026455/xbox-nano-direct-cloud-wifi-connection-xbox-cloud-gaming-phone-controller",
    "domain": "大厂 AI 动态",
    "title": "Xbox previews two new ways to control cloud games",
    "url": "https://www.theverge.com/news/1026455/xbox-nano-direct-cloud-wifi-connection-xbox-cloud-gaming-phone-controller",
    "source": "Tom Warren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T19:00:00+00:00",
    "summary": "I revealed yesterday that the new Xbox Nano controller supports a Wi-Fi connection directly to Xbox Cloud Gaming, and now Microsoft is making it official today. Two new Xbox previews will let players "
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1026586/nothing-screen-free-ai-device-carl-pei",
    "domain": "大厂 AI 动态",
    "title": "Nothing teases a screen-free AI device ahead of launch next month",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1026586/nothing-screen-free-ai-device-carl-pei",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T18:26:07+00:00",
    "summary": "Nothing CEO Carl Pei said in a post on X that the company's launching its first AI device in December. That's just a little over a year after Pei announced plans for \"AI-native\" devices and an AI oper"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/04/apple-is-reportedly-cutting-budgets-for-its-internal-ai-usage/",
    "domain": "大厂 AI 动态",
    "title": "Apple is reportedly cutting budgets for its internal AI usage",
    "url": "https://techcrunch.com/2026/11/04/apple-is-reportedly-cutting-budgets-for-its-internal-ai-usage/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T01:26:22+00:00",
    "summary": "The company is said to be significantly dropping the amount it's spending on AI for its engineering teams."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/04/after-the-midterms-a-bigger-clash-over-data-centers-could-be-coming/",
    "domain": "大厂 AI 动态",
    "title": "After the midterms, a bigger clash over data centers could be coming",
    "url": "https://techcrunch.com/2026/11/04/after-the-midterms-a-bigger-clash-over-data-centers-could-be-coming/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T01:02:14+00:00",
    "summary": "Data center opposition crossed party lines in Tuesday’s midterms."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/04/ai-pacs-spent-millions-trying-to-shape-congress-heres-how-they-fared/",
    "domain": "大厂 AI 动态",
    "title": "AI PACs spent millions trying to shape Congress — here’s how they fared",
    "url": "https://techcrunch.com/2026/11/04/ai-pacs-spent-millions-trying-to-shape-congress-heres-how-they-fared/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T22:45:09+00:00",
    "summary": "AI industry PACs spent millions influencing the 2026 midterms, with mixed results. Political groups are already looking toward the next election cycle."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/04/nothing-ceo-says-companys-mysterious-ai-first-device-is-dropping-next-month/",
    "domain": "大厂 AI 动态",
    "title": "Nothing CEO says company’s mysterious AI-first device is dropping next month",
    "url": "https://techcrunch.com/2026/11/04/nothing-ceo-says-companys-mysterious-ai-first-device-is-dropping-next-month/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T22:13:16+00:00",
    "summary": "While it's not yet clear what kind of product the smartphone startup is cooking up, Nothing's CEO said the product is designed to leverage AI for productivity gains."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/04/almost-no-one-uses-ai-agents-to-book-their-uber-company-says/",
    "domain": "大厂 AI 动态",
    "title": "Almost no one uses AI agents to book their Uber, company says",
    "url": "https://techcrunch.com/2026/11/04/almost-no-one-uses-ai-agents-to-book-their-uber-company-says/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T21:56:01+00:00",
    "summary": "During its busiest week last quarter, Uber said only four people booked a ride using an AI agent."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/04/snapchat-surpasses-30m-paid-subscribers/",
    "domain": "大厂 AI 动态",
    "title": "Snapchat surpasses 30M paid subscribers",
    "url": "https://techcrunch.com/2026/11/04/snapchat-surpasses-30m-paid-subscribers/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T21:49:29+00:00",
    "summary": "The milestone comes a year after Snapchat announced a controversial limit on free storage for its Memories feature and informed users it would start requiring users to pay $1.99 per month for addition"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/04/openai-is-already-trying-to-shape-the-2028-election/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI is already trying to shape the 2028 election",
    "url": "https://techcrunch.com/2026/11/04/openai-is-already-trying-to-shape-the-2028-election/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T21:25:44+00:00",
    "summary": "OpenAI’s Chris Lehane wants AI to define the 2028 election, proposing a new social contract that could benefit Americans while also advancing the AI giant’s own business interests."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/04/meta-acquires-ai-coding-startup-conductor/",
    "domain": "大厂 AI 动态",
    "title": "Meta acquires AI coding startup Conductor",
    "url": "https://techcrunch.com/2026/11/04/meta-acquires-ai-coding-startup-conductor/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T21:10:56+00:00",
    "summary": "The startup allows software engineers to deploy teams of agents to work on various aspects of a project simultaneously."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/04/hackers-stole-dreamhost-customer-files-and-inboxes-during-months-long-attack/",
    "domain": "大厂 AI 动态",
    "title": "Hackers stole DreamHost customer files and inboxes during months-long attack",
    "url": "https://techcrunch.com/2026/11/04/hackers-stole-dreamhost-customer-files-and-inboxes-during-months-long-attack/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T20:36:57+00:00",
    "summary": "The web host said hackers exploited a vulnerability to access customer emails and files during a \"deliberate attack.\""
  },
  {
    "id": "rss:https://techcrunch.com/video/open-source-ai-is-booming-hugging-face-explains-who-profits/",
    "domain": "大厂 AI 动态",
    "title": "Open source AI is booming. Hugging Face explains who profits.",
    "url": "https://techcrunch.com/video/open-source-ai-is-booming-hugging-face-explains-who-profits/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T19:30:04+00:00",
    "summary": "Open source models are becoming more mainstream as enterprises, governments and startups alike rely on the promise of lower costs, more control, and more flexibility. But as increasingly capable model"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/04/duckduckgo-pitches-itself-to-schools-amid-backlash-over-googles-ai-policy/",
    "domain": "大厂 AI 动态",
    "title": "DuckDuckGo pitches itself to schools amid backlash over Google’s AI policy",
    "url": "https://techcrunch.com/2026/11/04/duckduckgo-pitches-itself-to-schools-amid-backlash-over-googles-ai-policy/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T19:29:52+00:00",
    "summary": "DuckDuckGo is courting schools frustrated by Google's AI restrictions, pointing educators to its search engine and options to disable AI features."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/04/waymo-confirms-its-shaking-up-its-uber-relationship-in-january-2028/",
    "domain": "大厂 AI 动态",
    "title": "Waymo confirms it’s shaking up its Uber relationship in January 2028",
    "url": "https://techcrunch.com/2026/11/04/waymo-confirms-its-shaking-up-its-uber-relationship-in-january-2028/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T18:12:30+00:00",
    "summary": "The change will set up direct competition in those markets, as Uber has many other autonomous vehicle partners on its network."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/04/you-can-see-everything-is-getting-an-outer-space-release-and-it-hasnt-even-come-out-in-europe-yet/",
    "domain": "大厂 AI 动态",
    "title": "‘You Can See Everything’ is getting an outer space release and it hasn’t even come out in Europe yet",
    "url": "https://techcrunch.com/2026/11/04/you-can-see-everything-is-getting-an-outer-space-release-and-it-hasnt-even-come-out-in-europe-yet/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T18:10:11+00:00",
    "summary": "It is easier to watch the Elizabeth Holmes documentary \"You Can See Everything\" in low Earth orbit than in London."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/04/sequoia-hits-rewind-undoing-20-years-of-expansion/",
    "domain": "大厂 AI 动态",
    "title": "Sequoia hits rewind, undoing 20 years of expansion",
    "url": "https://techcrunch.com/2026/11/04/sequoia-hits-rewind-undoing-20-years-of-expansion/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T17:11:15+00:00",
    "summary": "Sequoia is consolidating into a smaller, Bay Area–centered firm, shutting down the programs and offices it built during a 20-year expansion while announcing roughly $10 billion in new funds."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/04/i-tried-apples-siri-recaps-theyre-surprisingly-useful-and-a-little-unsettling/",
    "domain": "大厂 AI 动态",
    "title": "I tried Apple’s Siri Recaps. They’re surprisingly useful — and a little unsettling",
    "url": "https://techcrunch.com/2026/11/04/i-tried-apples-siri-recaps-theyre-surprisingly-useful-and-a-little-unsettling/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T16:51:35+00:00",
    "summary": "Apple's AI-powered Siri Recaps won me over in just one day, despite my privacy reservations. But there's still room for improvement."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/04/google-faces-backlash-for-plan-that-would-turn-off-search-for-schools-that-restrict-ai/",
    "domain": "大厂 AI 动态",
    "title": "Google faces backlash for plan that would turn off Search for schools that restrict AI",
    "url": "https://techcrunch.com/2026/11/04/google-faces-backlash-for-plan-that-would-turn-off-search-for-schools-that-restrict-ai/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T16:17:22+00:00",
    "summary": "Politicians on the left, like NYC mayor Zohran Mamdani and former FTC chair Lina Khan, accused Google of acting as an unregulated monopoly."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/04/titan-os-raises-46-million-to-expand-its-smart-tv-os-internationally/",
    "domain": "大厂 AI 动态",
    "title": "Titan OS raises $46 million to expand its smart TV OS internationally",
    "url": "https://techcrunch.com/2026/11/04/titan-os-raises-46-million-to-expand-its-smart-tv-os-internationally/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T15:00:00+00:00",
    "summary": "Titan OS has raised $110 million in funding to date."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/04/revoluts-valuation-jumps-53-to-115b-in-new-share-sale-as-it-prepares-to-launch-us-bank/",
    "domain": "大厂 AI 动态",
    "title": "Revolut’s valuation jumps 53% to $115B in new share sale as it prepares to launch US bank",
    "url": "https://techcrunch.com/2026/11/04/revoluts-valuation-jumps-53-to-115b-in-new-share-sale-as-it-prepares-to-launch-us-bank/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T14:10:10+00:00",
    "summary": "Glade Brook, Coatue, and T. Rowe Price were among the investors that led the share sale."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/04/techcrunch-founder-summit-2026-todays-the-day/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Founder Summit 2026: Doors open at 9 a.m. ET in Boston",
    "url": "https://techcrunch.com/2026/11/04/techcrunch-founder-summit-2026-todays-the-day/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T13:00:00+00:00",
    "summary": "Today is the day to join TechCrunch Founder Summit 2026 in Boston's SoWa Power Station. Register now to join this founder-focused conference today."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/04/canva-lays-off-over-1200-people-amid-slowing-growth/",
    "domain": "大厂 AI 动态",
    "title": "Canva lays off over 1,200 people amid slowing growth",
    "url": "https://techcrunch.com/2026/11/04/canva-lays-off-over-1200-people-amid-slowing-growth/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T11:59:00+00:00",
    "summary": "Canva is cutting 22% of its staff as it faces its 'hardest year' yet."
  },
  {
    "id": "rss:https://stratechery.com/2026/ai-on-the-ballot/",
    "domain": "大厂 AI 动态",
    "title": "AI on the Ballot",
    "url": "https://stratechery.com/2026/ai-on-the-ballot/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T11:00:00+00:00",
    "summary": "Data Centers were on the ballot, and they lost in a major way; what does it mean if American opposition to building is permanent?"
  },
  {
    "id": "rss:https://stratechery.com/2026/apple-earnings-memory-problems-the-hardware-company-regression/",
    "domain": "大厂 AI 动态",
    "title": "Apple Earnings, Memory Problems, The Hardware Company Regression",
    "url": "https://stratechery.com/2026/apple-earnings-memory-problems-the-hardware-company-regression/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T11:00:00+00:00",
    "summary": "Apple's earnings suggest that the company's hardware business is doing better than ever, even in the face of memory challenges. Does the software story help or hurt?"
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/11/mercedes-amg-gt-4-door-coupe-first-drive-where-tech-and-fun-collide/",
    "domain": "大厂 AI 动态",
    "title": "Mercedes-AMG GT 4-Door Coupe first drive: Where tech and fun collide",
    "url": "https://arstechnica.com/cars/2026/11/mercedes-amg-gt-4-door-coupe-first-drive-where-tech-and-fun-collide/",
    "source": "Roberto Baldwin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T09:00:13+00:00",
    "summary": "The spirit of AMG is alive via three axial flux electric motors."
  },
  {
    "id": "rss:https://arstechnica.com/gaming/2026/11/the-tech-memory-shortage-comes-for-nintendos-cartridge-supply-chain/",
    "domain": "大厂 AI 动态",
    "title": "Nintendo's biggest ROM chip supplier is bowing out of the business",
    "url": "https://arstechnica.com/gaming/2026/11/the-tech-memory-shortage-comes-for-nintendos-cartridge-supply-chain/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T22:47:51+00:00",
    "summary": "And what that could mean for physical Switch game costs."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/11/hackers-exploited-ios-and-android-flaws-to-infect-phones/",
    "domain": "大厂 AI 动态",
    "title": "Hackers exploited iOS and Android flaws to infect phones",
    "url": "https://arstechnica.com/security/2026/11/hackers-exploited-ios-and-android-flaws-to-infect-phones/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T22:26:49+00:00",
    "summary": "Researchers say group may have been Kremlin-sponsored in search of diplomatic targets."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/11/uranium-cubes-reveal-why-the-german-nuclear-project-failed/",
    "domain": "大厂 AI 动态",
    "title": "Uranium cubes reveal why the German nuclear project failed",
    "url": "https://arstechnica.com/science/2026/11/uranium-cubes-reveal-why-the-german-nuclear-project-failed/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T21:56:29+00:00",
    "summary": "\"Our calculations suggest Heisenberg significantly underestimated the materials required.\""
  },
  {
    "id": "rss:https://arstechnica.com/information-technology/2026/11/vmware-releases-vsphere-express-for-virtualization-on-up-to-128-cores/",
    "domain": "大厂 AI 动态",
    "title": "VMware releases vSphere Express for virtualization on up to 128 cores",
    "url": "https://arstechnica.com/information-technology/2026/11/vmware-releases-vsphere-express-for-virtualization-on-up-to-128-cores/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T21:38:49+00:00",
    "summary": "“We started listening to a lot of our lower-end customers,\" VMware exec says."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/11/amds-record-quarter-data-center-business-doubles-while-gaming-craters/",
    "domain": "大厂 AI 动态",
    "title": "AMD's record quarter: Data center business doubles, while gaming craters",
    "url": "https://arstechnica.com/gadgets/2026/11/amds-record-quarter-data-center-business-doubles-while-gaming-craters/",
    "source": "Nick Indge",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T21:29:46+00:00",
    "summary": "AMD's gaming revenue fell 40 percent in an otherwise record $13.4 billion quarter."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/11/big-tech-claims-voters-ai-backlash-is-anti-trump-not-anti-tech/",
    "domain": "大厂 AI 动态",
    "title": "Big Tech claims voters’ AI backlash is “anti-Trump” not “anti-tech”",
    "url": "https://arstechnica.com/tech-policy/2026/11/big-tech-claims-voters-ai-backlash-is-anti-trump-not-anti-tech/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T20:55:50+00:00",
    "summary": "Tech industry in denial as US overwhelmingly votes to restrict AI, data centers."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/11/elon-musk-moved-spacex-to-red-texas-now-its-blue-what-happens-next/",
    "domain": "大厂 AI 动态",
    "title": "After Texas' blue wave, what happens to Elon Musk and SpaceX?",
    "url": "https://arstechnica.com/space/2026/11/elon-musk-moved-spacex-to-red-texas-now-its-blue-what-happens-next/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T20:36:05+00:00",
    "summary": "\"Data centers in space looking pretty appealing right now.\""
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/11/ted-cruz-aims-to-put-another-republican-on-fcc-in-senates-lame-duck-session/",
    "domain": "大厂 AI 动态",
    "title": "Ted Cruz aims to stack FCC with Republicans before Democrats take Senate control",
    "url": "https://arstechnica.com/tech-policy/2026/11/ted-cruz-aims-to-put-another-republican-on-fcc-in-senates-lame-duck-session/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T19:08:23+00:00",
    "summary": "Cruz and Trump seem to have no plans to fill FCC's empty Democratic seat."
  },
  {
    "id": "hn:50306008",
    "domain": "股票",
    "title": "US tech stocks see sharp falls over AI cost fears",
    "url": "https://www.bbc.co.uk/news/articles/cvwy72e0n72yo",
    "source": "mindracer",
    "platform": "hackernews",
    "points": 270,
    "published_at": "2026-10-30T16:13:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:50346153",
    "domain": "股票",
    "title": "Intel stock collapse worsens as $3.5T chip rout spreads",
    "url": "https://finance.yahoo.com/markets/article/the-intel-stock-collapse-is-getting-worse--and-the-37-trillion-chip-rout-is-spreading-212154947.html",
    "source": "entryleveljobsc",
    "platform": "hackernews",
    "points": 234,
    "published_at": "2026-11-03T00:08:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:50342284",
    "domain": "股票",
    "title": "Oracle files to sell $20B in new stock, bonds to finance AI buildout",
    "url": "https://www.cnbc.com/2026/11/02/oracle-files-to-sell-20-billion-in-new-stock-bonds-to-finance-ai-buildout.html",
    "source": "smartmic",
    "platform": "hackernews",
    "points": 199,
    "published_at": "2026-11-02T19:27:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:50051583",
    "domain": "股票",
    "title": "Research Firm Calls Anthropic's IPO 'Unprecedented Test of Investor Gullibity'",
    "url": "https://www.cnbc.com/2026/10/07/anthropic-will-be-most-ridiculous-ipo-of-year-analyst-says.html",
    "source": "m463",
    "platform": "hackernews",
    "points": 244,
    "published_at": "2026-10-12T05:03:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:50362274",
    "domain": "股票",
    "title": "AI stocks slide as Texas governor result raises data center risks",
    "url": "https://www.cnbc.com/2026/11/04/ai-stocks-texas-governor-data-centers.html",
    "source": "1659447091",
    "platform": "hackernews",
    "points": 54,
    "published_at": "2026-11-04T07:00:20+00:00",
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
    "id": "hn:50352405",
    "domain": "股票",
    "title": "US Hedge Funds Just Sold Every AI Stock They Bought Since 2025",
    "url": "https://finance.yahoo.com/markets/stocks/articles/us-hedge-funds-just-sold-113114644.html",
    "source": "robin_reala",
    "platform": "hackernews",
    "points": 38,
    "published_at": "2026-11-03T14:27:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:50351712",
    "domain": "股票",
    "title": "Anthropic's IPO Filing Warns It May Be 'Imminently' Close to RSI",
    "url": "https://epyhia.com/anthropic-s-ipo-filing-warns-it-may-be-imminently-close-to-recursive",
    "source": "arbuge",
    "platform": "hackernews",
    "points": 31,
    "published_at": "2026-11-03T13:26:43+00:00",
    "summary": ""
  },
  {
    "id": "hn:50280197",
    "domain": "股票",
    "title": "Alphabet Announces Third Quarter 2026 Results [pdf]",
    "url": "https://s206.q4cdn.com/479360582/files/doc_financials/2026/q3/2026q3-alphabet-earnings-release.pdf",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 82,
    "published_at": "2026-10-28T20:11:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:50232604",
    "domain": "股票",
    "title": "Microsoft and others tell crypto platform not to tokenize their stocks",
    "url": "https://gizmodo.com/microsoft-mcdonalds-verizon-and-others-tell-crypto-platform-not-to-tokenize-their-stocks-2000830368",
    "source": "gumby",
    "platform": "hackernews",
    "points": 100,
    "published_at": "2026-10-25T15:28:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:50348591",
    "domain": "股票",
    "title": "How AI is creating a lopsided US economy",
    "url": "https://www.abc.net.au/news/2026-10-19/ai-stock-market-concentration-data/107261078",
    "source": "gmays",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-11-03T05:58:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:50325107",
    "domain": "股票",
    "title": "The question we should all be asking about AI",
    "url": "https://www.cnn.com/2026/10/30/business/ai-stocks-bonds-debt",
    "source": "heresie-dabord",
    "platform": "hackernews",
    "points": 23,
    "published_at": "2026-11-01T12:44:36+00:00",
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
    "id": "hn:50274706",
    "domain": "金融",
    "title": "Tesla Semi catches fire on I-880",
    "url": "https://electrek.co/2026/10/28/tesla-semi-fire-i-880-hayward-no-crash/",
    "source": "metadat",
    "platform": "hackernews",
    "points": 96,
    "published_at": "2026-10-28T14:54:07+00:00",
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
    "id": "hn:50372038",
    "domain": "金融",
    "title": "Harmony: Chat like Discord. Federated like email",
    "url": "https://mony.lol/",
    "source": "FinalDestiny",
    "platform": "hackernews",
    "points": 29,
    "published_at": "2026-11-04T21:49:40+00:00",
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
    "id": "hn:50080275",
    "domain": "金融",
    "title": "Show HN: Pulse Local, a Mac budgeting app whose AI models run on your machine",
    "url": "https://pulseos.finance",
    "source": "niztk",
    "platform": "hackernews",
    "points": 122,
    "published_at": "2026-10-13T23:13:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:50239430",
    "domain": "金融",
    "title": "Tesla cancels Cybertruck in Australia and NZ after 7 years of deposits",
    "url": "https://electrek.co/2026/10/23/tesla-cancels-cybertruck-australia-new-zealand/",
    "source": "MilnerRoute",
    "platform": "hackernews",
    "points": 98,
    "published_at": "2026-10-26T05:13:15+00:00",
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
    "id": "rss:https://arxiv.org/abs/2611.05553",
    "domain": "金融",
    "title": "Decision Models as Scalable Economic Surrogates that Capture Human Variation",
    "url": "https://arxiv.org/abs/2611.05553",
    "source": "Maxime Saxena, Fabio Caccioli, R. Maria del Rio-Chanona",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T05:00:00+00:00",
    "summary": "arXiv:2611.05553v1 Announce Type: new Abstract: Decision Models (DMs), a new class of AI models, give fast responses and return a probability distribution over a fixed set of options. These properties"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.05640",
    "domain": "金融",
    "title": "Economic Policy Uncertainty Index for Poland: Data, Construction, and Validation",
    "url": "https://arxiv.org/abs/2611.05640",
    "source": "Alina M. Landowska, Robert A. K{\\l}opotek, He Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T05:00:00+00:00",
    "summary": "arXiv:2611.05640v1 Announce Type: new Abstract: We construct a continuous monthly Economic Policy Uncertainty (EPU) index for Poland spanning January 2000 to June 2026, following the newspaper-based B"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.05714",
    "domain": "金融",
    "title": "The potential impact of fiscal rule changes on digital products trade",
    "url": "https://arxiv.org/abs/2611.05714",
    "source": "Sonja Mitikj, Viktor Stojkoski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T05:00:00+00:00",
    "summary": "arXiv:2611.05714v1 Announce Type: new Abstract: The WTO moratorium on customs duties on electronic transmissions lapsed in March 2026, allowing governments to impose tariffs on cross-border digital pr"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.05767",
    "domain": "金融",
    "title": "Priced In or Bet On? Cram-School Lessons, Jeonse Leases, and Expected Appreciation in Seoul",
    "url": "https://arxiv.org/abs/2611.05767",
    "source": "Samiha Tariq",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T05:00:00+00:00",
    "summary": "arXiv:2611.05767v1 Announce Type: new Abstract: South Korean families spend heavily on hagwons, private cram schools that prepare students for the university entrance exam. This paper asks what access"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.06459",
    "domain": "金融",
    "title": "A general technique for explicit quantile representations",
    "url": "https://arxiv.org/abs/2611.06459",
    "source": "Wolfgang Schadner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T05:00:00+00:00",
    "summary": "arXiv:2611.06459v1 Announce Type: new Abstract: This work proves existence of contours independent of probability level for exact quantile integrals of strictly positive real-analytic densities. Expli"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.06495",
    "domain": "金融",
    "title": "Constrained defined-contribution pension management: A reparameterized neural network approach",
    "url": "https://arxiv.org/abs/2611.06495",
    "source": "Yueman Feng, Wenyuan Li",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T05:00:00+00:00",
    "summary": "arXiv:2611.06495v1 Announce Type: new Abstract: This paper studies constrained defined contribution (DC) pension management under a two-factor financial market model. The pension participant is allowe"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.06607",
    "domain": "金融",
    "title": "Hard to Fool: A Bounded LLM Research Loop for Quantitative Finance, and What Two Dozen Campaigns Found",
    "url": "https://arxiv.org/abs/2611.06607",
    "source": "Henry Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T05:00:00+00:00",
    "summary": "arXiv:2611.06607v1 Announce Type: new Abstract: Agentic research loops that let a language model propose a change, run a fixed experiment and keep whatever improves the metric work well in machine lea"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.06629",
    "domain": "金融",
    "title": "Does Frontier AI Strengthen Cyber Defense? Evidence from Project Glasswing",
    "url": "https://arxiv.org/abs/2611.06629",
    "source": "Thomas Mosk",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T05:00:00+00:00",
    "summary": "arXiv:2611.06629v1 Announce Type: new Abstract: Defenders and attackers race to find the same software flaws. I use the launch of Project Glasswing, which gave a small group of large US tech firms ear"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.06126",
    "domain": "金融",
    "title": "Exponential Seniority Weighting Chain-Ladder Reserving",
    "url": "https://arxiv.org/abs/2611.06126",
    "source": "Mario V. W\\\"uthrich",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T05:00:00+00:00",
    "summary": "arXiv:2611.06126v1 Announce Type: cross Abstract: We develop a tractable state-space version of the chain-ladder model. The state-space dynamics acts on the accident year axis which, in contrast to th"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.06696",
    "domain": "金融",
    "title": "You Know What You Will Like: People Predict Their Own Ratings Better Than Recommender Systems",
    "url": "https://arxiv.org/abs/2611.06696",
    "source": "Zihan Chen, Lei Nico Zheng, Di Zhu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T05:00:00+00:00",
    "summary": "arXiv:2611.06696v1 Announce Type: cross Abstract: Recommender systems usually learn what people want from what they have done. Platforms could also ask people directly, but asking is costly: 98.8% of "
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.06888",
    "domain": "金融",
    "title": "Dull, Dirty, Dangerous? Working Conditions and the Limits of Occupational AI Exposure",
    "url": "https://arxiv.org/abs/2611.06888",
    "source": "Siyi Yu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T05:00:00+00:00",
    "summary": "arXiv:2611.06888v1 Announce Type: cross Abstract: Automation is often justified as relief from dull, dirty, and dangerous work. I examine how these conditions relate to occupational AI exposure using "
  },
  {
    "id": "rss:https://arxiv.org/abs/2507.20410",
    "domain": "金融",
    "title": "Pay and Beyond: The Evolving Rewards for AI Skills",
    "url": "https://arxiv.org/abs/2507.20410",
    "source": "Alejandra Castaneda, Matthew Bone, Fabian Stephany",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T05:00:00+00:00",
    "summary": "arXiv:2507.20410v4 Announce Type: replace Abstract: This study examines the monetary and non-monetary rewards advertised in job vacancies requiring artificial intelligence skills in the U.S. labor mar"
  },
  {
    "id": "rss:https://arxiv.org/abs/2508.21285",
    "domain": "金融",
    "title": "A Financial Brain Scan of the LLM",
    "url": "https://arxiv.org/abs/2508.21285",
    "source": "Hui Chen, Antoine Didisheim, Mo Pourmohammadi, Luciano Somoza, Hanqing Tian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T05:00:00+00:00",
    "summary": "arXiv:2508.21285v4 Announce Type: replace Abstract: We use sparse autoencoders (SAEs) to \"brain scan\" large language models, mapping internal activations to interpretable concepts and enabling targete"
  },
  {
    "id": "rss:https://arxiv.org/abs/2512.10672",
    "domain": "金融",
    "title": "The Dynamic Theory of Economic Complexity",
    "url": "https://arxiv.org/abs/2512.10672",
    "source": "Cesar A. Hidalgo, Viktor Stojkoski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T05:00:00+00:00",
    "summary": "arXiv:2512.10672v2 Announce Type: replace Abstract: Why do some activities grow faster in some economies than others? We develop a dynamic model of economic complexity in which output is determined by"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.17117",
    "domain": "金融",
    "title": "Geometric Observables for Financial Regime Detection",
    "url": "https://arxiv.org/abs/2605.17117",
    "source": "Will Hammond",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T05:00:00+00:00",
    "summary": "arXiv:2605.17117v3 Announce Type: replace Abstract: We extract four geometric observables -- Berry Phase Rate, Spectral Entropy, Reduced State Purity, and Hamiltonian Sensitivity -- from a learned spe"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.29572",
    "domain": "金融",
    "title": "Valuation Reveals Uncertainty",
    "url": "https://arxiv.org/abs/2606.29572",
    "source": "Jongjin Park, David Criens, Hyungbin Park",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T05:00:00+00:00",
    "summary": "arXiv:2606.29572v2 Announce Type: replace Abstract: This paper studies the recovery of uncertainty from dynamic sublinear valuation rules. Robust valuation assigns each payoff its worst-case expected "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.15452",
    "domain": "金融",
    "title": "Computing Endogenous Transformations in Processing Networks: A Dynamic Calibration Approach",
    "url": "https://arxiv.org/abs/2609.15452",
    "source": "Satoshi Nakano, Kazuhiko Nishimura",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T05:00:00+00:00",
    "summary": "arXiv:2609.15452v5 Announce Type: replace Abstract: Understanding how production networks endogenously transform requires a parametric model with non-neutral substitution elasticities. While the Casca"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.01540",
    "domain": "金融",
    "title": "Social Networks and the Propagation of Household Shocks to Asset Prices",
    "url": "https://arxiv.org/abs/2611.01540",
    "source": "Faisal Quaiyyum",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T05:00:00+00:00",
    "summary": "arXiv:2611.01540v2 Announce Type: replace Abstract: When can local household disturbances move credit prices? I develop a financially weighted propagation operator on the social network. In a conditio"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.01656",
    "domain": "金融",
    "title": "AIDA: An AI Outage Registry with Evidence from On-Chain MEV",
    "url": "https://arxiv.org/abs/2611.01656",
    "source": "Wenbin Wu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T05:00:00+00:00",
    "summary": "arXiv:2611.01656v2 Announce Type: replace Abstract: Generative AI coding tools have lowered the cost of writing trading software, but no systematic dataset records when these services fail. We introdu"
  },
  {
    "id": "rss:https://arxiv.org/abs/2307.04754",
    "domain": "金融",
    "title": "Dynamic Strategy Selection",
    "url": "https://arxiv.org/abs/2307.04754",
    "source": "Francesco Cordoni, Alessio Sancetta, Yuqian Zhao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T05:00:00+00:00",
    "summary": "arXiv:2307.04754v4 Announce Type: replace-cross Abstract: We consider the problem of dynamically selecting among competing strategies using observable predictors. To mitigate estimation noise and exce"
  },
  {
    "id": "rss:https://arxiv.org/abs/2502.02352",
    "domain": "金融",
    "title": "Stochastic Optimal Control with Measurable Coefficients and Applications",
    "url": "https://arxiv.org/abs/2502.02352",
    "source": "Filippo de Feo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T05:00:00+00:00",
    "summary": "arXiv:2502.02352v4 Announce Type: replace-cross Abstract: We consider fully non-linear stochastic optimal control problems with measurable coefficients and (local) uniformly elliptic diffusion. Using "
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
    "id": "hn:50295332",
    "domain": "金融",
    "title": "Tesla caught altering specs following rear suspension collapse reports",
    "url": "https://carnewschina.com/2026/09/17/tesla-caught-quietly-altering-model-y-l-manual-specs-following-rear-suspension-collapse-reports/",
    "source": "Alien1Being",
    "platform": "hackernews",
    "points": 26,
    "published_at": "2026-10-29T20:24:13+00:00",
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
    "id": "hn:50074739",
    "domain": "金融",
    "title": "Americans Trust in Federal Government Sinks to New Depths",
    "url": "https://news.gallup.com/poll/715361/trust-federal-government-sinks-new-depths.aspx",
    "source": "giuliomagnifico",
    "platform": "hackernews",
    "points": 49,
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
  }
]
```
