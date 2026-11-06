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

- 今日日期：`2026-11-06`
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
  "date": "2026-11-06",
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
    "points": 2213254,
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
    "points": 2087005,
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
    "points": 2073079,
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
    "points": 1472732,
    "published_at": "2026-06-09T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“VibeCoding”免费获取\n【课程简介】从零开始，用自然语言指挥AI开发真实软件项目！"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 1442020,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV11NNAz5EKn",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！",
    "url": "http://www.bilibili.com/video/av116187623069851",
    "source": "AI-智能体搭建教程",
    "platform": "bilibili",
    "points": 1437402,
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
    "points": 910022,
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
    "points": 892375,
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
    "points": 744217,
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
    "points": 675358,
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
    "points": 595690,
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
    "points": 462184,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1AnQNYxEsy",
    "domain": "AI",
    "title": "MCP是啥？技术原理是什么？一个视频搞懂MCP的一切。Windows系统配置MCP，Cursor Cline使用MCP",
    "url": "http://www.bilibili.com/video/av114155298228756",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 427243,
    "published_at": "2025-03-13T13:18:09+00:00",
    "summary": "MCP是近期的AI领域的热点，特别是在海外社区获得热烈讨论，每天都有大量MCP工具诞生。本期视频我们从MCP的概念，技术原理，到多场景实战，一个视频看懂MCP的全部内容。\n\n\nMCP官方开源仓库：https://github.com/modelcontextprotocol/servers\nMCP合集网站：  https://smithery.ai/\nVscode下载：https://code.v"
  },
  {
    "id": "bvid:BV1vG8QzcE5X",
    "domain": "AI",
    "title": "Claude使用指南，claude code零基础教程，claude code安装配置到实战",
    "url": "http://www.bilibili.com/video/av114933744272468",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 358074,
    "published_at": "2025-07-30T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从概念到安装，再到Claude Code的具体使用，开发效率原地起飞！"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 347862,
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
    "points": 322019,
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
    "points": 294337,
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
    "points": 226932,
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
    "points": 200476,
    "published_at": "2026-04-13T09:00:00+00:00",
    "summary": "opencodeopencode使用全攻略opencode教程opencode和claudecodeopencode使用技巧opencode实战opencode coworkopencode安装opencode开发opencode使用教程opencode教程opencode安装教程opencode使用全攻略opencode和claudecodeopencode skillsopencode插件op"
  },
  {
    "id": "bvid:BV1kr4h6fExw",
    "domain": "AI",
    "title": "DeepSeek 新出的 Super Agent 是什么？真有用么？",
    "url": "http://www.bilibili.com/video/av117564076202051",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 196588,
    "published_at": "2026-11-05T13:35:56+00:00",
    "summary": "DeepSeek Harness 团队最新开源的 Super-agent 是什么？和传统 Agent 有什么区别？它是怎么工作的？真的能提升 AI 工作的效率么？一期视频带你掌握 Super-agent 智能体，对 AI 小白、AI 编程爱好者、前端和后端程序员、AI 应用开发求职者都有帮助\n编程学习教程+实战项目+简历模板：codefather.cn\n免费 AI 编程教程：github.com/"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 185938,
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
    "points": 164888,
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
    "points": 162281,
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
    "points": 161753,
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
    "points": 158039,
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
    "points": 151762,
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
    "points": 150307,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1dpdZYBE9q",
    "domain": "AI",
    "title": "零代码让AI秒接海量MCP工具！最适合小白的MCP集合平台",
    "url": "http://www.bilibili.com/video/av114340703243255",
    "source": "AI研究室-帆哥",
    "platform": "bilibili",
    "points": 103449,
    "published_at": "2025-04-15T11:00:00+00:00",
    "summary": "最近MCP太火了，阿里直接跟进把MCP整合到百炼平台里面了，做了一个MCP的“应用商店”。\n之前不管是在cursor还是Claude上还是需要配置一下MCP服务器，现在在百炼上就可以直接无脑添加MCP工具，非常方便。\n而且因为在平台上一体化，和大模型可以打包配置，让后端的运维部署变得更轻松。\n这个视频教你怎么用阿里云百炼的MCP工具创建一个agent应用。"
  },
  {
    "id": "bvid:BV1K6YM69ESq",
    "domain": "AI",
    "title": "AI+网络安全实战：从Agent入门到AI智能体挖漏洞教程！网络安全|信息安全|黑客技术|渗透测试|SRC漏洞挖掘|AI审计|HVV护网行动|靶场练习-码士集团",
    "url": "http://www.bilibili.com/video/av117247037213495",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 95892,
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
    "points": 94255,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operit教程：入门安卓最强大ai平台operitAI",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 75828,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1woHQ6kEtv",
    "domain": "AI",
    "title": "【2026最新版】Workbuddy财务自动化办公实战教程，搭建数字员工，能够秒做账、报税、报销、出报表、做财务分析、编制预算、处理合并报表",
    "url": "http://www.bilibili.com/video/av117404038466491",
    "source": "Max极客菌",
    "platform": "bilibili",
    "points": 61436,
    "published_at": "2026-10-08T07:22:21+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1JY4w6kEAe",
    "domain": "AI",
    "title": "【全网首发】Claude防封号独家指南！前后花了5万元！小白保姆级教程【包含对话铺垫/IP DNS/订阅方式/历史记录清除】",
    "url": "http://www.bilibili.com/video/av117546107800312",
    "source": "Gemini3-",
    "platform": "bilibili",
    "points": 55196,
    "published_at": "2026-11-02T09:26:34+00:00",
    "summary": "视频内已经将所有的网站进行打码，没有吐露任何网址，也没有推广违规AI服务\n简介无推广内容\n视频中演示网站有正规ICP备案与ICP许可"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 50166,
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
    "points": 49557,
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
    "points": 47802,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV17Lap6VEUr",
    "domain": "AI",
    "title": "【全80集】Vibe Coding 零基础入门到实战教程，由浅入深（全程干货）",
    "url": "http://www.bilibili.com/video/av117353572468721",
    "source": "数据拾光屋",
    "platform": "bilibili",
    "points": 43718,
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
    "points": 41229,
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
    "points": 37166,
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
    "points": 34645,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1Nu3M6bEXE",
    "domain": "AI",
    "title": "【上海交大张倬胜】大模型系列课程从入门到精通，手把手教学，保姆级教程！涵盖预训练模型微调与部署、提示学习与思维链、模型水印、多模态大模型，比啃书效果好多了",
    "url": "http://www.bilibili.com/video/av116979859984479",
    "source": "Agent开发教程",
    "platform": "bilibili",
    "points": 32708,
    "published_at": "2026-07-25T09:34:49+00:00",
    "summary": "【上海交大张倬胜】大模型系列课程从入门到精通，手把手教学，保姆级教程！涵盖预训练模型微调与部署、提示学习与思维链、模型水印、多模态大模型，比啃书效果好多了，草履虫都能学会！"
  },
  {
    "id": "bvid:BV1sQaL6vEkb",
    "domain": "AI",
    "title": "小白向，ai入门第一课：agent的部署和使用！",
    "url": "http://www.bilibili.com/video/av117349378166797",
    "source": "沈三殊",
    "platform": "bilibili",
    "points": 31837,
    "published_at": "2026-09-28T15:30:36+00:00",
    "summary": "详细的agent部署介绍：https://pan.quark.cn/s/3846914c6da7\n欢迎来到ai的世界！！\n有疑问欢迎私信。"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29931,
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
    "points": 29040,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1vwXPYkEGx",
    "domain": "AI",
    "title": "Cursor+mcp配置，手把手教你配置任意MCP服务，学不会你打我，小白保姆级教程~MCP服务配置指南 - 提升AI编程助手能力",
    "url": "http://www.bilibili.com/video/av114193181183930",
    "source": "三少科技",
    "platform": "bilibili",
    "points": 27448,
    "published_at": "2025-03-20T05:51:23+00:00",
    "summary": "我的知识星球，https://t.zsxq.com/jVAk9\n\n📌 本期教程通过实战演示，教你在Cursor中配置和使用MCP服务器，特别是filesystem MCP服务，解决Cursor无法写入文件的常见问题。\n⏱️ 内容概要：\n00:00 介绍MCP及其重要性\n02:00 Cursor抽风问题与MCP解决方案\n04:00 配置第一个MCP服务器（filesystem）\n07:00 Wind"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 26307,
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
    "points": 25854,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1wpxq6VEXx",
    "domain": "AI",
    "title": "【AI时代的STM32教程】AI Agent 初体验",
    "url": "http://www.bilibili.com/video/av117529699682124",
    "source": "keysking",
    "platform": "bilibili",
    "points": 23997,
    "published_at": "2026-10-30T11:52:06+00:00",
    "summary": "一句话，让 AI 帮我们完成第一个 STM32C5 程序！🚀\n本期我们一起认识 AI Agent，学习如何描述开发需求，并借助开源的 STM32C5DevSkills，让 AI 完成工程创建、芯片配置、代码编写和编译烧录，让律动小板上的小灯闪烁起来！\n也特别感谢 @意法半导体中国   对本系列教程的支持～下期我们再亲手走一遍开发流程，把 Agent 替我们完成的工作，一步步搞明白！"
  },
  {
    "id": "bvid:BV1ixxM6mE5T",
    "domain": "AI",
    "title": "vibe coding破防瞬间",
    "url": "http://www.bilibili.com/video/av117511798395204",
    "source": "程序员牛牛学长",
    "platform": "bilibili",
    "points": 20426,
    "published_at": "2026-10-29T10:55:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1f57C6YErb",
    "domain": "AI",
    "title": "手把手教你Codex安装和使用MCP！新手必备~",
    "url": "http://www.bilibili.com/video/av116696861907147",
    "source": "Raina测试",
    "platform": "bilibili",
    "points": 18820,
    "published_at": "2026-06-06T11:29:00+00:00",
    "summary": "这一期给大家分享下在codex里面如何配置和使用MCP，和skill一样，MCP也是我们平时用得比较多的，所以建议大家也可以学一下它的基础配置和使用~\n步骤都不难，跟着操作就可以了"
  },
  {
    "id": "hn:50362905",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia RTX Spark encrypted firmware slows inference speed to 35% on Linux",
    "url": "https://www.mindstudio.ai/blog/linux-nvidia-rtx-spark-laptop",
    "source": "novaRom",
    "platform": "hackernews",
    "points": 614,
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
    "points": 289,
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
    "points": 195,
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
    "id": "hn:50387738",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Kubernetes Engine (NVKE)",
    "url": "https://github.com/dsx-ai-factory/nvke",
    "source": "gkapur",
    "platform": "hackernews",
    "points": 81,
    "published_at": "2026-11-06T03:16:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:50363861",
    "domain": "AI 算力 / 半导体",
    "title": "RTX 5090 Street Prices Top $9k as Nvidia GPU Costs Climb",
    "url": "https://aroundprague.cz/en/news/us/rtx-5090-street-prices-top-9-000-as-nvidia-gpu-costs-climb",
    "source": "teleforce",
    "platform": "hackernews",
    "points": 73,
    "published_at": "2026-11-04T11:02:23+00:00",
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
    "id": "hn:50372759",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia store pulls RTX 5080 following RTX 5090 removal, prices rise to 2.2X MSRP",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-store-quietly-pulls-the-rtx-5080-following-rtx-5090-removal-street-prices-climb-to-2-2x-over-msrp",
    "source": "akyuu",
    "platform": "hackernews",
    "points": 31,
    "published_at": "2026-11-04T23:12:29+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/europe-chip-industry-perfect-storm-or-perfect-timing/",
    "domain": "AI 算力 / 半导体",
    "title": "Europe’s Chip Industry: Perfect Storm or Perfect Timing?",
    "url": "https://www.eetimes.com/europe-chip-industry-perfect-storm-or-perfect-timing/",
    "source": "Anne-Françoise Pelé",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T09:53:05+00:00",
    "summary": "At SEMICON Europa 2026, Europe’s chip industry will confront a “perfect storm” of geopolitical, technological, and competitive pressures. The post Europe’s Chip Industry: Perfect Storm or Perfect Timi"
  },
  {
    "id": "rss:https://www.eetimes.com/ee-times-magazine-november-2026/",
    "domain": "AI 算力 / 半导体",
    "title": "EE Times Magazine – November 2026",
    "url": "https://www.eetimes.com/ee-times-magazine-november-2026/",
    "source": "Anne-Françoise Pelé",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T22:30:00+00:00",
    "summary": "This edition of EE Times Magazine explores advances in semiconductor manufacturing and packaging, farm autonomy, and Canada’s efforts to commercialize emerging technologies. The post EE Times Magazine"
  },
  {
    "id": "rss:https://www.eetimes.com/infineon-leaders-andreas-urschitz-and-maher-matta-on-a-decade-of-oktobertech/",
    "domain": "AI 算力 / 半导体",
    "title": "Infineon Leaders Andreas Urschitz and Maher Matta on a Decade of OktoberTech",
    "url": "https://www.eetimes.com/infineon-leaders-andreas-urschitz-and-maher-matta-on-a-decade-of-oktobertech/",
    "source": "EE Times",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T19:30:52+00:00",
    "summary": "Sponsored: Infineon’s Andreas Urschitz and Maher Matta talk to EE Times at OktoberTech Silicon Valley 2026, looking back on a decade of innovation and growth. The post Infineon Leaders Andreas Urschit"
  },
  {
    "id": "rss:https://www.eetimes.com/infineons-johannes-schoiswohl-on-the-gan-market-at-oktobertech/",
    "domain": "AI 算力 / 半导体",
    "title": "Infineon’s Johannes Schoiswohl on the GaN Market at OktoberTech",
    "url": "https://www.eetimes.com/infineons-johannes-schoiswohl-on-the-gan-market-at-oktobertech/",
    "source": "EE Times",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T19:15:17+00:00",
    "summary": "Sponsored: PEN’s Aalyia Shaukat talks to Infineon’s Johannes Schoiswohl about the GaN market at OktoberTech Silicon Valley 2026, the event’s 10th anniversary. The post Infineon’s Johannes Schoiswohl o"
  },
  {
    "id": "rss:https://www.eetimes.com/infineons-steve-tateosian-talks-iot-consumer-and-industrial-mcus-at-oktobertech/",
    "domain": "AI 算力 / 半导体",
    "title": "Infineon’s Steve Tateosian Talks IoT, Consumer, and Industrial MCUs at OktoberTech",
    "url": "https://www.eetimes.com/infineons-steve-tateosian-talks-iot-consumer-and-industrial-mcus-at-oktobertech/",
    "source": "EE Times",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T18:59:48+00:00",
    "summary": "Sponsored: EDN's Majeed Ahmad talks to Infineon's Steve Tateosian on edge systems, application examples, and the growth of the market. The post Infineon’s Steve Tateosian Talks IoT, Consumer, and Indu"
  },
  {
    "id": "rss:https://www.eetimes.com/from-pytorch-to-product-accelerating-edge-ai-through-open-ecosystems/",
    "domain": "AI 算力 / 半导体",
    "title": "From PyTorch to Product: Accelerating Edge AI Through Open Ecosystems",
    "url": "https://www.eetimes.com/from-pytorch-to-product-accelerating-edge-ai-through-open-ecosystems/",
    "source": "Renesas",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T18:12:42+00:00",
    "summary": "In this 30-Minute BitCast, discover how open-source technologies are helping developers accelerate AI deployment on resource-constrained embedded devices. The post From PyTorch to Product: Acceleratin"
  },
  {
    "id": "rss:https://www.eetimes.com/accelerate-analog-design-with-flexible-ai-native-workflows/",
    "domain": "AI 算力 / 半导体",
    "title": "Accelerate Analog Design with Flexible, AI-Native Workflows",
    "url": "https://www.eetimes.com/accelerate-analog-design-with-flexible-ai-native-workflows/",
    "source": "ChipsAgents",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T17:40:24+00:00",
    "summary": "Join this webinar to learn how ChipAgents’ IC-star chip neural engine automates analog design, simulation, and verification in one unified, flexible agentic loop. The post Accelerate Analog Design wit"
  },
  {
    "id": "rss:https://www.eetimes.com/nvidia-municipal-leaders-frame-ai-as-critical-urban-infrastructure/",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia, Municipal Leaders Frame AI as Critical Urban Infrastructure",
    "url": "https://www.eetimes.com/nvidia-municipal-leaders-frame-ai-as-critical-urban-infrastructure/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T16:09:46+00:00",
    "summary": "City officials are moving beyond isolated pilot projects toward local computing infrastructure and AI. The post Nvidia, Municipal Leaders Frame AI as Critical Urban Infrastructure appeared first on EE"
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
    "id": "rss:https://www.tomshardware.com/video-games/handheld-gaming/grab-a-nintendo-switch-2-controller-upgrade-from-usd49-just-in-time-for-zelda-ocarina-of-times-remaster-secure-the-tools-to-defeat-ganondorf-with-these-top-wireless-gamepads-from-8bitdo-gamesir-and-others",
    "domain": "AI 算力 / 半导体",
    "title": "Grab a Nintendo Switch 2 controller upgrade from $49, just in time for Zelda: Ocarina of Time's remaster",
    "url": "https://www.tomshardware.com/video-games/handheld-gaming/grab-a-nintendo-switch-2-controller-upgrade-from-usd49-just-in-time-for-zelda-ocarina-of-times-remaster-secure-the-tools-to-defeat-ganondorf-with-these-top-wireless-gamepads-from-8bitdo-gamesir-and-others",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T21:00:00+00:00",
    "summary": "A selection of the best Switch 2 controllers for getting your best Zelda game on."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/combined-flaws-let-anyone-into-alpine-linux-and-other-distros-by-typing-anything-over-256-characters-as-a-password-emergency-fixes-for-openssh-and-musl-libc-issued-for-millions-of-systems-patch-immediately",
    "domain": "AI 算力 / 半导体",
    "title": "Combined OpenSSH and musl-libc flaws let anyone into Alpine Linux and other distros by typing anything over 256 characters as a password",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/combined-flaws-let-anyone-into-alpine-linux-and-other-distros-by-typing-anything-over-256-characters-as-a-password-emergency-fixes-for-openssh-and-musl-libc-issued-for-millions-of-systems-patch-immediately",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T18:14:56+00:00",
    "summary": "Combined OpenSSH and musl-libc flaws let anyone into Alpine Linux and other distros by typing anything over 256 characters as a password"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/india-targets-creating-homegrown-gpus-within-2-years-and-plans-to-commercialize-indigenous-shakti-and-vega-risc-v-processors-sees-ai-boom-as-a-potential-repeat-of-the-y2k-opportunity-for-its-it-industry",
    "domain": "AI 算力 / 半导体",
    "title": "India targets creating homegrown GPUs within 2 years and plans to commercialize indigenous SHAKTI and VEGA processors",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/india-targets-creating-homegrown-gpus-within-2-years-and-plans-to-commercialize-indigenous-shakti-and-vega-risc-v-processors-sees-ai-boom-as-a-potential-repeat-of-the-y2k-opportunity-for-its-it-industry",
    "source": "Newton Gitonga",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T18:00:00+00:00",
    "summary": "MeitY Secretary S. Krishnan says India plans to develop its own GPU under Semiconductor Mission 2.0, with a target of approximately two years. The country is also looking to commercialize its SHAKTI a"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/policy/chinese-ai-lab-moonshot-reportedly-looked-at-european-data-centers-to-access-nvidia-chips-report-claims-kimi-maker-primarily-interested-in-inferencing-capacity-but-also-asked-about-training-clusters",
    "domain": "AI 算力 / 半导体",
    "title": "Chinese AI lab Moonshot reportedly looked at European data centers to access Nvidia chips, report claims",
    "url": "https://www.tomshardware.com/tech-industry/policy/chinese-ai-lab-moonshot-reportedly-looked-at-european-data-centers-to-access-nvidia-chips-report-claims-kimi-maker-primarily-interested-in-inferencing-capacity-but-also-asked-about-training-clusters",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T16:48:30+00:00",
    "summary": "The lab is reportedly interested in renting at least 8,000 Nvidia Blackwell GPUs."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/nintendo/nintendo-switch-2-sales-dropped-by-41-percent-from-last-year-due-to-consoles-price-increase-pressure-to-release-more-big-games-to-make-up-for-shortfall",
    "domain": "AI 算力 / 半导体",
    "title": "Nintendo Switch 2 sales dropped by 41% from last year due to console's price increase",
    "url": "https://www.tomshardware.com/video-games/nintendo/nintendo-switch-2-sales-dropped-by-41-percent-from-last-year-due-to-consoles-price-increase-pressure-to-release-more-big-games-to-make-up-for-shortfall",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T16:27:28+00:00",
    "summary": "Nintendo's Switch 2 sales decreased by 41% compared to the same time frame last year due to an increase in the console's price. Investors are pressuring Nintendo to release more big games to attract m"
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/portable-monitors/uperfect-gr14bu-portable-monitor-review",
    "domain": "AI 算力 / 半导体",
    "title": "UPERFECT GR14BU portable monitor review: A 120 Hz 3K OLED touch display at a killer price",
    "url": "https://www.tomshardware.com/monitors/portable-monitors/uperfect-gr14bu-portable-monitor-review",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T15:00:00+00:00",
    "summary": "With a 3K OLED panel and a 120 Hz refresh rate, the GR14BU comes out swinging."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-leaker-claims-nova-lake-desktop-chips-have-5-1-ghz-clock-limit-beyond-90-c-high-clock-speeds-could-demand-significant-cooling-for-next-gen-chips",
    "domain": "AI 算力 / 半导体",
    "title": "Intel leaker claims Nova Lake desktop chips have 5.1 GHz clock limit beyond 90°C",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-leaker-claims-nova-lake-desktop-chips-have-5-1-ghz-clock-limit-beyond-90-c-high-clock-speeds-could-demand-significant-cooling-for-next-gen-chips",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T14:57:51+00:00",
    "summary": "A known Intel leaker claims that Intel's next-generation processors will top out at 5.1 GHz if the CPU core temperatures aren't kept below 90°C."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/microns-usd4-5-billion-taoyuan-plant-construction-halted-amidst-labor-dispute-company-and-union-still-havent-reached-agreement-as-latter-asks-for-clearer-profit-sharing-terms",
    "domain": "AI 算力 / 半导体",
    "title": "Micron's $4.5 billion Taoyuan plant construction halted amidst labor dispute",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/microns-usd4-5-billion-taoyuan-plant-construction-halted-amidst-labor-dispute-company-and-union-still-havent-reached-agreement-as-latter-asks-for-clearer-profit-sharing-terms",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T14:28:30+00:00",
    "summary": "Micron and the Taoyuan labor union is set to meet again on November 6 as the two parties engage in a protracted labor dispute regarding profit-sharing."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/macbooks/apple-macbook-pro-14-inch-m6-review",
    "domain": "AI 算力 / 半导体",
    "title": "Apple MacBook Pro (14-inch, M6) review: Speedy M6 chip slips into comfortable shoes",
    "url": "https://www.tomshardware.com/laptops/macbooks/apple-macbook-pro-14-inch-m6-review",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T14:00:00+00:00",
    "summary": "Apple’s brings its powerful M6 chip and N1 Wi-Fi 7 chip to the MacBook Pro."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/macbooks/apple-macbook-pro-with-proled-xdr-display-review",
    "domain": "AI 算力 / 半导体",
    "title": "Apple MacBook Pro with PROLED XDR Display review: The screen that every Mac deserves",
    "url": "https://www.tomshardware.com/laptops/macbooks/apple-macbook-pro-with-proled-xdr-display-review",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T14:00:00+00:00",
    "summary": "Apple's MacBook Pro with PROLED Display has lots of small tweaks that make it a major upgrade, including a lighter weight and touch functionality, but it's exceptionally expensive and out of reach for"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/microsd-cards/boost-your-nintendo-switch-2s-storage-for-zelda-ocarina-of-time-with-these-microsd-express-deals-starting-at-usd48-make-room-for-hyrule-with-these-high-speed-cards-that-double-or-triple-your-game-storage",
    "domain": "AI 算力 / 半导体",
    "title": "Boost your Nintendo Switch 2's storage for Zelda: Ocarina of Time with these microSD Express deals, starting at $48",
    "url": "https://www.tomshardware.com/pc-components/microsd-cards/boost-your-nintendo-switch-2s-storage-for-zelda-ocarina-of-time-with-these-microsd-express-deals-starting-at-usd48-make-room-for-hyrule-with-these-high-speed-cards-that-double-or-triple-your-game-storage",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T14:00:00+00:00",
    "summary": "With the Legend of Zelda: Ocarina of Time remake now available for the Nintendo Switch 2, you're going to need enough storage to install it. Here are some Switch 2 microSD Express card deals to help y"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/congresswoman-calls-for-artificial-superintelligence-ban-after-democrats-seismic-midterm-sweep-demands-regulation-of-out-of-control-industry-and-pause-on-advanced-ai",
    "domain": "AI 算力 / 半导体",
    "title": "Congresswoman calls for artificial superintelligence ban after Democrats' seismic midterm sweep",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/congresswoman-calls-for-artificial-superintelligence-ban-after-democrats-seismic-midterm-sweep-demands-regulation-of-out-of-control-industry-and-pause-on-advanced-ai",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T13:30:16+00:00",
    "summary": "Rep. Yassamin Ansari of Arizona is asking her party to focus on AI issues."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/routers/this-usd79-98-tp-link-wireless-router-with-wi-fi-7-tech-is-back-down-to-its-lowest-ever-price-archer-be3600-unlocks-multi-gigabit-networking-ideal-for-gaming-or-4k-streaming-with-33-percent-off",
    "domain": "AI 算力 / 半导体",
    "title": "This $79.98 TP-Link wireless router with Wi-Fi 7 tech is back down to its lowest-ever price",
    "url": "https://www.tomshardware.com/networking/routers/this-usd79-98-tp-link-wireless-router-with-wi-fi-7-tech-is-back-down-to-its-lowest-ever-price-archer-be3600-unlocks-multi-gigabit-networking-ideal-for-gaming-or-4k-streaming-with-33-percent-off",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T13:00:00+00:00",
    "summary": "You can pick up a TP-Link Archer BE3600 wireless router at its lowest ever price on Amazon for just $79.98."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/two-dead-five-injured-in-taiwan-pcb-factory-explosion-panasonic-industrial-devices-materials-facility-fire-prompts-emergency-response",
    "domain": "AI 算力 / 半导体",
    "title": "Two dead, five injured in Taiwan PCB factory explosion",
    "url": "https://www.tomshardware.com/tech-industry/two-dead-five-injured-in-taiwan-pcb-factory-explosion-panasonic-industrial-devices-materials-facility-fire-prompts-emergency-response",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T12:31:33+00:00",
    "summary": "An explosion and fire at a PCB factory situated in Taiwan’s Silicon Valley has left two people dead and five injured."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/blood-banks-in-france-hit-by-temperature-raising-attacks-on-fridges-purported-hackers-claim-attacks-are-about-cybersecurity-not-malice",
    "domain": "AI 算力 / 半导体",
    "title": "Hackers target French blood service fridges following supermarket attacks",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/blood-banks-in-france-hit-by-temperature-raising-attacks-on-fridges-purported-hackers-claim-attacks-are-about-cybersecurity-not-malice",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T12:00:00+00:00",
    "summary": "Following the string of cyberattacks on supermarket freezers, blood banks in France were recently attacked. Luckily, no biomaterial was lost as the attack triggered the EFS' alerts."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/marvell-to-buy-lumentum-in-usd115-billion-all-stock-deal-combined-company-to-supply-scale-up-and-scale-in-optics-for-ai-data-centers",
    "domain": "AI 算力 / 半导体",
    "title": "Marvell to buy Lumentum in $115 billion all-stock deal",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/marvell-to-buy-lumentum-in-usd115-billion-all-stock-deal-combined-company-to-supply-scale-up-and-scale-in-optics-for-ai-data-centers",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T12:00:00+00:00",
    "summary": "Marvell has agreed to acquire Lumentum for $115 billion, combining its optical DSPs, SerDes, silicon photonics, and networking silicon with Lumentum’s lasers, transceivers, optical switches, and InP m"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/spacex-plans-to-build-more-data-center-compute-than-googles-entire-lifetime-capacity-in-just-1-5-years-analysts-say-target-is-realistic-spacex-to-build-staggering-10-gigawatts-of-compute-in-2027-alone",
    "domain": "AI 算力 / 半导体",
    "title": "SpaceX's plan to build more data center compute than Google's entire lifetime capacity in just 1.5 years is possible, say analysts",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/spacex-plans-to-build-more-data-center-compute-than-googles-entire-lifetime-capacity-in-just-1-5-years-analysts-say-target-is-realistic-spacex-to-build-staggering-10-gigawatts-of-compute-in-2027-alone",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T11:30:00+00:00",
    "summary": "SpaceX's bold claim that it's capable of building 10 GW of compute in 2027 may be plausible — analysts dig through the breakneck speed of Colossus buildouts as evidence"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-loosens-game-restrictions-claude-will-now-offer-to-build-original-game-in-same-genre-if-asked-to-copy",
    "domain": "AI 算力 / 半导体",
    "title": "Anthropic loosens Claude's game cloning ban",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-loosens-game-restrictions-claude-will-now-offer-to-build-original-game-in-same-genre-if-asked-to-copy",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T11:00:00+00:00",
    "summary": "The update is expected to reduce false positives and allow game developers to use the tool for their own legitimate projects without getting blocked."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/grab-a-huge-44-percent-saving-on-a-4k-43-inch-samsung-smart-monitor-now-under-usd280-limited-time-woot-discount-on-dual-use-display-thatll-work-as-a-home-office-screen-or-standalone-smart-tv",
    "domain": "AI 算力 / 半导体",
    "title": "Grab a huge 44% saving on a 4K 43-inch Samsung smart monitor, now under $280",
    "url": "https://www.tomshardware.com/monitors/grab-a-huge-44-percent-saving-on-a-4k-43-inch-samsung-smart-monitor-now-under-usd280-limited-time-woot-discount-on-dual-use-display-thatll-work-as-a-home-office-screen-or-standalone-smart-tv",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T10:52:49+00:00",
    "summary": "Grab a cheap upgrade from a top brand with this Samsung 43-inch M7 M70F 4K UHD monitor, down to just $279.99, giving you a smart display for TV, movies, and productivity."
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
    "title": "Team Group CEO warns memory crisis could reach point where 'even money can't buy goods'",
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
    "title": "Thermal Grizzly launches PhaseSheet PTM Pro with improved thermal conductivity",
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
    "title": "AI data centers comprehensively defeated at US midterm elections",
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
    "title": "PHP vulnerability post-mortem reveals bug was known two years ago",
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
    "title": "Nvidia can only fulfill 1% of China’s massive $70 billion GPU order for AI chips, report claims",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-can-only-fulfill-1-percent-of-chinas-massive-usd70-billion-gpu-order-for-ai-chips-report-claims-supply-constraints-choke-export-friendly-rtx-pro-5500-deliveries-despite-huge-demand",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T12:15:00+00:00",
    "summary": "Just 1% of chips promised to major Chinese companies to power their AI ambitions will be delivered, according to reports."
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
    "points": 717,
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
    "points": 92,
    "published_at": "2026-11-03T17:55:26+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1028454/openai-data-center-nda",
    "domain": "大厂 AI 动态",
    "title": "OpenAI is stepping back from NDAs for data center projects",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1028454/openai-data-center-nda",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T00:37:56+00:00",
    "summary": "Following this week's midterms where voters resoundingly voiced their opposition to data center expansion, OpenAI today announced new commitments to communities where it is working on data center proj"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1028412/airbnb-ai-travel-agent-q3-2026-earnings",
    "domain": "大厂 AI 动态",
    "title": "Airbnb is working on an AI travel agent",
    "url": "https://www.theverge.com/tech/1028412/airbnb-ai-travel-agent-q3-2026-earnings",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T00:06:12+00:00",
    "summary": "Airbnb plans to roll out an AI agent in the first half of 2027 that will help users plan and book travel, the company said in its Q3 2026 earnings shareholder letter released today. \"Today's AI agents"
  },
  {
    "id": "rss:https://www.theverge.com/news/1028375/the-new-york-times-letterboxd-acquisition-report",
    "domain": "大厂 AI 动态",
    "title": "The New York Times is in talks to buy Letterboxd for around $330 million",
    "url": "https://www.theverge.com/news/1028375/the-new-york-times-letterboxd-acquisition-report",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T23:45:10+00:00",
    "summary": "The New York Times Company is in talks\"exclusive negotations\" to acquire Letterboxd, the social network for film lovers, for around $330 million, The New York Times reports. The Times Company, Sony Pi"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1028346/t-mobile-deutsche-telecom-spacex-starlink-mobile",
    "domain": "大厂 AI 动态",
    "title": "T-Mobile owner on Elon Musk launching a wireless carrier: &#8216;Welcome to the party&#8217;",
    "url": "https://www.theverge.com/tech/1028346/t-mobile-deutsche-telecom-spacex-starlink-mobile",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T23:17:10+00:00",
    "summary": "The head of T-Mobile's parent company is casting doubt on SpaceX's plans to make Starlink Mobile a \"major\" carrier in the US. During an earnings call on Thursday, Deutsche Telekom CEO Tim H&#246;ttges"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1028302/perplexity-teammates-ai-agents-work",
    "domain": "大厂 AI 动态",
    "title": "Perplexity launches its own take on AI agents for work",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1028302/perplexity-teammates-ai-agents-work",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T22:26:50+00:00",
    "summary": "Perplexity is taking on OpenAI and Anthropic with its own work-focused AI agents. The startup's new always-on \"Teammates\" can take on multiple roles within a workspace, while pulling existing projects"
  },
  {
    "id": "rss:https://www.theverge.com/news/1028281/salon-dot-com-shuts-down",
    "domain": "大厂 AI 动态",
    "title": "Salon is shutting down after 31 years",
    "url": "https://www.theverge.com/news/1028281/salon-dot-com-shuts-down",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T22:08:14+00:00",
    "summary": "Salon launched 31 years ago as one of the first online-only news magazine outlets, and it announced today in an unsigned post that it's ceasing publication. The company said that the \"business realiti"
  },
  {
    "id": "rss:https://www.theverge.com/policy/1028253/midterm-elections-x-right-wing-memes",
    "domain": "大厂 AI 动态",
    "title": "The midterms proved once and for all that X is not real life",
    "url": "https://www.theverge.com/policy/1028253/midterm-elections-x-right-wing-memes",
    "source": "Gaby Del Valle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T21:55:00+00:00",
    "summary": "A week before the midterm elections, Vice President JD Vance hosted a town hall in Texas with Fox News host Jesse Watters. It was a friendly event with a friendly audience in what should have been a f"
  },
  {
    "id": "rss:https://www.theverge.com/science/1028178/blue-origins-next-launch-now-wont-happen-until-2027",
    "domain": "大厂 AI 动态",
    "title": "Blue Origin’s next launch now won’t happen until 2027",
    "url": "https://www.theverge.com/science/1028178/blue-origins-next-launch-now-wont-happen-until-2027",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T20:47:14+00:00",
    "summary": "Blue Origin plans to do its next New Glenn rocket launch in January 2027, according to CNBC and the Financial Times, which cite a memo from CEO Dave Limp sent to staff. The new timeline follows a May "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1027659/samsung-galaxy-z-fold-8-beats-pill-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Samsung’s Galaxy Z Fold 8 is $300 off ahead of Black Friday",
    "url": "https://www.theverge.com/gadgets/1027659/samsung-galaxy-z-fold-8-beats-pill-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T19:12:58+00:00",
    "summary": "Android fans with a bit of iPhone Duo envy, take note: The Samsung Galaxy Z Fold 8 is discounted to $1,599.99 at both Amazon and Best Buy, a hefty $300 markdown from its usual price, and just $50 high"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1028015/meta-muse-ai-voice-mode-expressive-avatar",
    "domain": "大厂 AI 动态",
    "title": "Muse has a voice mode now",
    "url": "https://www.theverge.com/tech/1028015/meta-muse-ai-voice-mode-expressive-avatar",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T19:03:04+00:00",
    "summary": "Meta now lets you have voice conversations with your Muse AI agent in real time, CEO Mark Zuckerberg announced today. The feature has been rolled out to me, and I gave it a spin on the iOS app while w"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/05/at-least-10-local-governments-have-moved-to-drop-flocks-surveillance-cameras-since-summer/",
    "domain": "大厂 AI 动态",
    "title": "At least 10 local governments have moved to drop Flock’s surveillance cameras since summer",
    "url": "https://techcrunch.com/2026/11/05/at-least-10-local-governments-have-moved-to-drop-flocks-surveillance-cameras-since-summer/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T07:18:44+00:00",
    "summary": "The concerns range from privacy to how data is shared (and with whom) to procurement concerns."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/05/palo-alto-networks-in-talks-to-buy-ai-agent-security-startup-clutch-for-500m/",
    "domain": "大厂 AI 动态",
    "title": "Palo Alto Networks in talks to buy AI agent security startup Clutch for $500M",
    "url": "https://techcrunch.com/2026/11/05/palo-alto-networks-in-talks-to-buy-ai-agent-security-startup-clutch-for-500m/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T06:28:32+00:00",
    "summary": "Clutch, backed by Lightspeed and SignalFire, was last valued at $85 million, according to a source."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/05/the-new-york-times-reportedly-in-talks-to-buy-letterboxd-for-330-million/",
    "domain": "大厂 AI 动态",
    "title": "The New York Times reportedly in talks to buy Letterboxd for $330 million",
    "url": "https://techcrunch.com/2026/11/05/the-new-york-times-reportedly-in-talks-to-buy-letterboxd-for-330-million/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T00:07:18+00:00",
    "summary": "Letterboxd, an online platform for movie lovers, has grown dramatically in recent years."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/05/meta-google-and-tiktok-sue-california-ag-over-teen-social-media-law/",
    "domain": "大厂 AI 动态",
    "title": "Meta, Google, and TikTok sue California AG over teen social media law",
    "url": "https://techcrunch.com/2026/11/05/meta-google-and-tiktok-sue-california-ag-over-teen-social-media-law/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T00:01:38+00:00",
    "summary": "If it goes into effect next year, this California law would restrict social media access for children under 16."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/05/airbnb-says-its-launching-an-ai-travel-agent-in-the-first-half-of-2027/",
    "domain": "大厂 AI 动态",
    "title": "Airbnb says it’s launching an AI travel agent in the first half of 2027",
    "url": "https://techcrunch.com/2026/11/05/airbnb-says-its-launching-an-ai-travel-agent-in-the-first-half-of-2027/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T22:40:55+00:00",
    "summary": "Airbnb says its upcoming AI agent will help travelers plan trips, compare options, manage bookings, and get assistance throughout their stay."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/05/serve-robotics-launches-new-business-to-become-the-aws-for-robots/",
    "domain": "大厂 AI 动态",
    "title": "Serve Robotics launches new business to become the AWS for robots",
    "url": "https://techcrunch.com/2026/11/05/serve-robotics-launches-new-business-to-become-the-aws-for-robots/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T21:15:00+00:00",
    "summary": "Serve Robotics announced alonsgside its third-quarter earnings that it will launch a new business line called Physical AI Services to offer customers its connectivity and data tools."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/05/meta-says-us-users-can-now-video-chat-with-their-muse-ai-avatar/",
    "domain": "大厂 AI 动态",
    "title": "Meta says US users can now video chat with their Muse AI avatar",
    "url": "https://techcrunch.com/2026/11/05/meta-says-us-users-can-now-video-chat-with-their-muse-ai-avatar/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T19:48:28+00:00",
    "summary": "Meta's AI agent can now take calls as a customizable animated avatar, ahead of the launch of a Tamagotchi-like wearable designed to bring Muse to life."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/05/metas-warns-that-election-backlash-against-data-centers-could-make-ai-expansion-harder/",
    "domain": "大厂 AI 动态",
    "title": "Meta warns that election backlash against data centers could make AI expansion harder",
    "url": "https://techcrunch.com/2026/11/05/metas-warns-that-election-backlash-against-data-centers-could-make-ai-expansion-harder/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T19:12:39+00:00",
    "summary": "Meta warns that growing political opposition to data centers could threaten future AI investments, as communities push back against massive infrastructure projects."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/05/openai-released-a-new-cybersecurity-model-is-that-enough/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI released a new cybersecurity model. Is that enough?",
    "url": "https://techcrunch.com/2026/11/05/openai-released-a-new-cybersecurity-model-is-that-enough/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T19:06:12+00:00",
    "summary": "OpenAI's newest cybersecurity model comes out as AI labs face scrutiny of their work to protect digital infrastructure."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/05/u-s-government-warns-of-ongoing-cyber-threat-amid-mass-hacks-of-industrial-retail-and-military-freezers/",
    "domain": "大厂 AI 动态",
    "title": "US government warns of ‘ongoing cyber threat’ amid mass hacks of industrial retail and military freezers",
    "url": "https://techcrunch.com/2026/11/05/u-s-government-warns-of-ongoing-cyber-threat-amid-mass-hacks-of-industrial-retail-and-military-freezers/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T18:48:34+00:00",
    "summary": "A joint U.S. government statement says the hacks are affecting the food, transportation, and healthcare industries after reports of global mass hacks."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/05/openai-president-greg-brockman-says-company-could-be-ipo-ready-in-2027/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI president Greg Brockman says company could be IPO ready in 2027",
    "url": "https://techcrunch.com/2026/11/05/openai-president-greg-brockman-says-company-could-be-ipo-ready-in-2027/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T18:02:27+00:00",
    "summary": "Speaking at a Wall Street Journal tech conference on Wednesday, the executive touted how the company had been gaining ground in the enterprise market, where rival Anthropic had already successfully ma"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/05/the-ex-secret-service-agent-who-flipped-a-hacker-is-now-raising-a-second-250m-cybersecurity-fund/",
    "domain": "大厂 AI 动态",
    "title": "The ex-Secret Service agent who flipped a hacker is now raising a second $250M cybersecurity fund",
    "url": "https://techcrunch.com/2026/11/05/the-ex-secret-service-agent-who-flipped-a-hacker-is-now-raising-a-second-250m-cybersecurity-fund/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T18:00:00+00:00",
    "summary": "Stephen Ward, a former Secret Service agent and Home Depot CISO, is preparing a second fund of roughly $250 million for Brightmind Partners."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/05/claude-can-now-analyze-your-spending-with-its-new-personal-finance-tool/",
    "domain": "大厂 AI 动态",
    "title": "Claude can now analyze your spending with its new Personal Finance tool",
    "url": "https://techcrunch.com/2026/11/05/claude-can-now-analyze-your-spending-with-its-new-personal-finance-tool/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T18:00:00+00:00",
    "summary": "With Personal Finance in Claude, users can connect their bank and card accounts through Plaid and ask questions about their finances."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/05/harbinger-raises-240m-after-expanding-into-defense/",
    "domain": "大厂 AI 动态",
    "title": "Harbinger raises $240M after expanding into defense",
    "url": "https://techcrunch.com/2026/11/05/harbinger-raises-240m-after-expanding-into-defense/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T17:52:44+00:00",
    "summary": "The Los Angeles-based startup has now raised more than $650 million, and is working on electric trucks, emergency vehicles, and a driverless platform for the military."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/05/food-delivery-startup-wonder-files-for-ipo-as-it-explores-its-next-big-bite/",
    "domain": "大厂 AI 动态",
    "title": "Food delivery startup Wonder files for IPO as it explores its next big bite",
    "url": "https://techcrunch.com/2026/11/05/food-delivery-startup-wonder-files-for-ipo-as-it-explores-its-next-big-bite/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T17:11:48+00:00",
    "summary": "Following years of fundraising, acquisitions, and expansion, food delivery startup Wonder is moving closer to becoming a publicly traded company."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/05/axiom-math-wants-to-keep-ai-slop-out-of-mathematics/",
    "domain": "大厂 AI 动态",
    "title": "Axiom Math wants to keep AI slop out of mathematics",
    "url": "https://techcrunch.com/2026/11/05/axiom-math-wants-to-keep-ai-slop-out-of-mathematics/",
    "source": "Aditya Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T16:16:45+00:00",
    "summary": "As AI floods math with unchecked proofs, Axiom Math is betting on verification. The startup’s AI agents just formally verified the Stacks Project, one of the field’s biggest libraries."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/05/bluesky-hit-peak-usage-for-the-year-on-election-night/",
    "domain": "大厂 AI 动态",
    "title": "Bluesky hit peak usage for the year on election night",
    "url": "https://techcrunch.com/2026/11/05/bluesky-hit-peak-usage-for-the-year-on-election-night/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T15:44:58+00:00",
    "summary": "Bluesky CEO Toni Schneider said posts and likes doubled during to the U.S. midterm elections on Tuesday."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/05/zipline-hits-21-5b-valuation-as-walmart-expands-bet-on-drone-delivery/",
    "domain": "大厂 AI 动态",
    "title": "Zipline hits $21.5B valuation as Walmart expands bet on drone delivery",
    "url": "https://techcrunch.com/2026/11/05/zipline-hits-21-5b-valuation-as-walmart-expands-bet-on-drone-delivery/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T15:40:34+00:00",
    "summary": "Zipline raised $1.5 billion and ramped up its partnership with Walmart."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/05/tiktok-quietly-launches-a-standalone-tiktok-shop-app/",
    "domain": "大厂 AI 动态",
    "title": "TikTok quietly launches a stand-alone TikTok Shop app",
    "url": "https://techcrunch.com/2026/11/05/tiktok-quietly-launches-a-standalone-tiktok-shop-app/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T15:33:58+00:00",
    "summary": "The app will offer personalized product recommendations, shopping through livestreams and short-form videos, app-exclusive deals, in-app checkout, order tracking, and customer support."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/05/dropbox-acquires-tigris-data-for-350m-to-bolster-its-ai-iinfrastructure/",
    "domain": "大厂 AI 动态",
    "title": "Dropbox acquires Tigris Data for $350M to bolster its AI infrastructure",
    "url": "https://techcrunch.com/2026/11/05/dropbox-acquires-tigris-data-for-350m-to-bolster-its-ai-iinfrastructure/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T15:19:05+00:00",
    "summary": "The deal is expected to support the development of DBX Agent Cloud, a new storage platform aimed at developers building AI models and agents."
  },
  {
    "id": "rss:https://stratechery.com/2026/an-interview-with-intuit-ceo-sasan-goodarzi-about-accounting-and-ai/",
    "domain": "大厂 AI 动态",
    "title": "An Interview With Intuit CEO Sasan Goodarzi About Accounting and AI",
    "url": "https://stratechery.com/2026/an-interview-with-intuit-ceo-sasan-goodarzi-about-accounting-and-ai/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T11:00:00+00:00",
    "summary": "An interview with Intuit CEO Sasan Goodarzi about the working for one of tech's oldest software companies, and how Intuit is leaning into the AI paradigm shift."
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
    "id": "rss:https://arstechnica.com/space/2026/11/blue-origin-announces-rocket-upgrades-aimed-at-lower-costs-more-performance/",
    "domain": "大厂 AI 动态",
    "title": "Blue Origin says it is building a higher-performing rocket engine at 1/4 the cost",
    "url": "https://arstechnica.com/space/2026/11/blue-origin-announces-rocket-upgrades-aimed-at-lower-costs-more-performance/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T00:17:06+00:00",
    "summary": "\"This is going to be a game-changer.\""
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/11/vulnerability-allows-attackers-to-log-into-some-linux-devices-sans-password/",
    "domain": "大厂 AI 动态",
    "title": "Meet *sshole, the vulnerability that lets hackers SSH into Linux devices",
    "url": "https://arstechnica.com/security/2026/11/vulnerability-allows-attackers-to-log-into-some-linux-devices-sans-password/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T23:09:36+00:00",
    "summary": "Certain configurations of Alpine are affected. Other distros may be as well."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/11/nasas-experimental-x-70-aircraft-is-a-big-question-mark/",
    "domain": "大厂 AI 动态",
    "title": "NASA unveils mysterious X-70 experimental aircraft using AI-generated image",
    "url": "https://arstechnica.com/gadgets/2026/11/nasas-experimental-x-70-aircraft-is-a-big-question-mark/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T22:49:03+00:00",
    "summary": "NASA’s X-70 Fractal announcement comes as agency aims to grow X-plane fleet."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/11/sony-adds-usb-c-to-its-70s-era-mdr-3-walkman-headphones/",
    "domain": "大厂 AI 动态",
    "title": "Sony revives the original Walkman headphones, adds USB-C",
    "url": "https://arstechnica.com/gadgets/2026/11/sony-adds-usb-c-to-its-70s-era-mdr-3-walkman-headphones/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T21:56:36+00:00",
    "summary": "Orange ear cushions included."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/11/google-schools-can-keep-search-while-skipping-gemini-but-ai-search-is-non-negotiable/",
    "domain": "大厂 AI 动态",
    "title": "Google: Schools can keep search while skipping Gemini, but AI search is non-negotiable",
    "url": "https://arstechnica.com/ai/2026/11/google-schools-can-keep-search-while-skipping-gemini-but-ai-search-is-non-negotiable/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T21:40:36+00:00",
    "summary": "Google is technically offering schools more choice but not the choices anyone wants."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/11/lawsuit-man-introduced-his-wife-to-chatgpt-she-used-it-to-plan-his-murder/",
    "domain": "大厂 AI 动态",
    "title": "Lawsuit: Man introduced his wife to ChatGPT. She used it to plan his murder.",
    "url": "https://arstechnica.com/tech-policy/2026/11/lawsuit-man-introduced-his-wife-to-chatgpt-she-used-it-to-plan-his-murder/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T21:39:40+00:00",
    "summary": "Bitter energy drinks turned out to be ChatGPT-steered poisoning, lawsuit says."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/11/bmw-bumps-battery-for-the-better-the-2027-i7-60-xdrive-driven/",
    "domain": "大厂 AI 动态",
    "title": "BMW bumps battery for the better: The 2027 i7 60 xDrive, driven",
    "url": "https://arstechnica.com/cars/2026/11/bmw-bumps-battery-for-the-better-the-2027-i7-60-xdrive-driven/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T20:45:50+00:00",
    "summary": "BMW has updated its flagship sedan with the newest EV and infotainment tech."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/11/getting-software-to-help-block-out-a-star-so-we-can-see-exoplanets/",
    "domain": "大厂 AI 动态",
    "title": "Software squeezes more data out of Webb Telescope for imaging exoplanets",
    "url": "https://arstechnica.com/science/2026/11/getting-software-to-help-block-out-a-star-so-we-can-see-exoplanets/",
    "source": "John Timmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T19:59:22+00:00",
    "summary": "Software optimizes a physical model of the telescope to reduce noise."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/11/kalshi-court-losses-pile-up-as-judges-refuse-to-block-state-gambling-laws/",
    "domain": "大厂 AI 动态",
    "title": "Kalshi court losses pile up as judges refuse to block state gambling laws",
    "url": "https://arstechnica.com/tech-policy/2026/11/kalshi-court-losses-pile-up-as-judges-refuse-to-block-state-gambling-laws/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T19:46:37+00:00",
    "summary": "Kalshi can't avoid gambling law by claiming it doesn't offer gambling, state AG says."
  },
  {
    "id": "hn:50381623",
    "domain": "股票",
    "title": "Nasdaq plummets 4% into correction territory",
    "url": "https://www.cnbc.com/2026/11/04/stock-market-today-live-updates.html",
    "source": "kristianp",
    "platform": "hackernews",
    "points": 218,
    "published_at": "2026-11-05T17:11:15+00:00",
    "summary": ""
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
    "id": "hn:50382179",
    "domain": "股票",
    "title": "Nasdaq Sinks 5% as Investors Retreat from AI Trade After Election",
    "url": "https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-11-05-2026",
    "source": "armcat",
    "platform": "hackernews",
    "points": 160,
    "published_at": "2026-11-05T18:00:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:50384822",
    "domain": "股票",
    "title": "$2.5T has been wiped from US stocks",
    "url": "https://finlaws.substack.com/p/25t-has-been-wiped-from-us-stocks",
    "source": "madihaa",
    "platform": "hackernews",
    "points": 154,
    "published_at": "2026-11-05T21:39:26+00:00",
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
    "id": "hn:50386909",
    "domain": "股票",
    "title": "Investors wipe $2.5T off Nasdaq as blue tsunami prompts AI fears",
    "url": "https://www.reuters.com/legal/transactional/ai-data-center-stocks-slip-democratic-sweep-clouds-expansion-plans-2026-11-05/",
    "source": "lilerjee",
    "platform": "hackernews",
    "points": 44,
    "published_at": "2026-11-06T01:11:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:50389401",
    "domain": "股票",
    "title": "Global stocks tumble as AI panic grips markets after Democrats' midterm success",
    "url": "https://www.theguardian.com/business/live/2026/nov/06/global-stocks-tumble-ai-panic-markets-democrats-midterms-success-jobs-oil-dollar-latest-news-updates",
    "source": "drayfield",
    "platform": "hackernews",
    "points": 29,
    "published_at": "2026-11-06T07:52:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:50384382",
    "domain": "股票",
    "title": "Chip stocks get slaughtered as Wall Street in worst post-midterm day since 1896",
    "url": "https://finance.yahoo.com/markets/article/chip-stocks-get-slaughtered-as-wall-street-heads-for-its-worst-post-midterm-day-since-1896-163413900.html",
    "source": "novaRom",
    "platform": "hackernews",
    "points": 29,
    "published_at": "2026-11-05T20:58:36+00:00",
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
    "id": "hn:50383675",
    "domain": "股票",
    "title": "Wipeout for AI stocks sends Wall Street reeling and S&P 500 tumbles more than 3%",
    "url": "https://apnews.com/article/stocks-markets-ai-midterm-oil-trump-7ee9c212805aa5e70cf34d25aab7a36e",
    "source": "jethronethro",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-11-05T19:58:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:50385642",
    "domain": "股票",
    "title": "Michael Burry says Anthropic is 'betting its existence' on optimism",
    "url": "https://www.businessinsider.com/michael-burry-anthropic-ipo-outlook-ant-big-short-2026-11",
    "source": "mgh2",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-11-05T22:49:47+00:00",
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
    "points": 32,
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
    "id": "hn:50385870",
    "domain": "金融",
    "title": "Cuban: Facebook knowingly runs AI deepfake scam ads; docs say $16B fraud revenue",
    "url": "https://finance.yahoo.com/technology/ai/articles/mark-cuban-says-facebook-knowingly-213000020.html",
    "source": "randycupertino",
    "platform": "hackernews",
    "points": 344,
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
    "id": "hn:50387406",
    "domain": "金融",
    "title": "Tesla and SpaceX lose over $420B in combined market cap in the two days",
    "url": "https://techlaws.pages.dev/tesla-and-spacex-lose-over-420b-in-combined-market-cap-in-the-two-days/",
    "source": "Pepitobombito",
    "platform": "hackernews",
    "points": 76,
    "published_at": "2026-11-06T02:30:25+00:00",
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
    "id": "hn:50372038",
    "domain": "金融",
    "title": "Harmony: Chat like Discord. Federated like email",
    "url": "https://mony.lol/",
    "source": "FinalDestiny",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-11-04T21:49:40+00:00",
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
    "id": "rss:https://arxiv.org/abs/2611.06919",
    "domain": "金融",
    "title": "Return Decomposition of Hybrid Strategies in the Brazilian Market: Evidence of Genuine Alpha and Factor Exposure",
    "url": "https://arxiv.org/abs/2611.06919",
    "source": "Francisco Robson do Nascimento de Freitas, Felipe Macedo Zumba, Lucio Marassi, Jian Vingthor Souza Luna de Azevedo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T05:00:00+00:00",
    "summary": "arXiv:2611.06919v1 Announce Type: new Abstract: This paper decomposes the return sources of a hybrid portfolio combining a fundamentalist screen - based on P/E, ROE, Net Margin, Current Ratio, and P/B"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.07110",
    "domain": "金融",
    "title": "Credibility Clustering for Experience Rating: An Automated Approach to Risk Group Allocation in Group Life Insurance",
    "url": "https://arxiv.org/abs/2611.07110",
    "source": "Thom van Rijn, Frank Weber, Michael Merz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T05:00:00+00:00",
    "summary": "arXiv:2611.07110v1 Announce Type: new Abstract: In insurance, experience rating plays a crucial role in mitigating adverse selection by adjusting premiums according to historical claims experience. A "
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.07120",
    "domain": "金融",
    "title": "A Rough Instantaneous Squared VIX Model for Term Structure and Option Pricing",
    "url": "https://arxiv.org/abs/2611.07120",
    "source": "Tianfeng Yang, Wen Su, Blanka Horvath",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T05:00:00+00:00",
    "summary": "arXiv:2611.07120v1 Announce Type: new Abstract: The VIX term structure provides forward-looking measures of market uncertainty across horizons, while VIX options allow investors to hedge volatility ri"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.07287",
    "domain": "金融",
    "title": "Neural Realized Measures: Forecast-Supervised Intraday Aggregation for Volatility Forecasting",
    "url": "https://arxiv.org/abs/2611.07287",
    "source": "Brian Sing Fan Chan, Jennifer So Kuen Chan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T05:00:00+00:00",
    "summary": "arXiv:2611.07287v1 Announce Type: new Abstract: High-frequency volatility forecasting typically separates measurement from prediction: intraday observations are first compressed into a daily realized "
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.07457",
    "domain": "金融",
    "title": "Information-Theoretic Model for the Growth Optimal Portfolio of Stocks",
    "url": "https://arxiv.org/abs/2611.07457",
    "source": "Eckhard Platen, Kevin Fergusson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T05:00:00+00:00",
    "summary": "arXiv:2611.07457v1 Announce Type: new Abstract: Drawing on information-theoretic principles and empirical evidence, a proxy for the growth-optimal portfolio of stocks (the benchmark) is constructed an"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.08031",
    "domain": "金融",
    "title": "Economies of scale and the equity-efficiency trade-off: Evidence from a piped water network in rural Bangladesh",
    "url": "https://arxiv.org/abs/2611.08031",
    "source": "Md. Ahasan Habib, Anna Tompsett",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T05:00:00+00:00",
    "summary": "arXiv:2611.08031v1 Announce Type: new Abstract: Policymakers who set prices for public infrastructure often anticipate an equity-efficiency trade-off: while higher prices could increase revenues from "
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.08430",
    "domain": "金融",
    "title": "Cross-Border Ownership and Input Access: Evidence from the Lithium Supply Chain",
    "url": "https://arxiv.org/abs/2611.08430",
    "source": "Kei Irizawa",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T05:00:00+00:00",
    "summary": "arXiv:2611.08430v1 Announce Type: new Abstract: How does cross-border ownership shape the lithium supply chain? Using global data on mines and refineries, I estimate a model in which ownership can low"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.07083",
    "domain": "金融",
    "title": "Necessary and sufficient conditions for the martingale property of stochastic exponentials driven by multi-dimensional diffusions",
    "url": "https://arxiv.org/abs/2611.07083",
    "source": "Erhan Bayraktar, Hao Xing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T05:00:00+00:00",
    "summary": "arXiv:2611.07083v1 Announce Type: cross Abstract: We give necessary and sufficient coefficient conditions for stochastic exponentials driven by multidimensional diffusions to be true martingales. The "
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.07699",
    "domain": "金融",
    "title": "Stay, Reposition, or Recharge: Battery-Aware Operation of Robotaxi Fleets",
    "url": "https://arxiv.org/abs/2611.07699",
    "source": "Philipp Af\\`eche (Kamessi), Saif Benjaafar (Kamessi), Jiayu (Kamessi), Zhao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T05:00:00+00:00",
    "summary": "arXiv:2611.07699v1 Announce Type: cross Abstract: Electric robotaxis are rapidly expanding from pilots to scaled commercial deployment; unlike traditional human-driven ride-hailing vehicles, they requ"
  },
  {
    "id": "rss:https://arxiv.org/abs/2501.01748",
    "domain": "金融",
    "title": "On consistency of optimal portfolio choice for state-dependent exponential utilities",
    "url": "https://arxiv.org/abs/2501.01748",
    "source": "Edoardo Berton, Marzia De Donno, Marco Maggis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T05:00:00+00:00",
    "summary": "arXiv:2501.01748v2 Announce Type: replace Abstract: In a complete Brownian market, we characterize consistency across investment horizons for state-dependent exponential utilities. We show that consis"
  },
  {
    "id": "rss:https://arxiv.org/abs/2502.17906",
    "domain": "金融",
    "title": "Why financial prices exhibit Brownian motion despite predictable order flow: An exactly solvable nonlinear price impact model",
    "url": "https://arxiv.org/abs/2502.17906",
    "source": "Yuki Sato, Shunta Fujiwara, Kiyoshi Kanazawa",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T05:00:00+00:00",
    "summary": "arXiv:2502.17906v5 Announce Type: replace Abstract: In econophysics, there are two enigmatic empirical laws of financial market microstructure: (i) the market-order flow has predictable persistence du"
  },
  {
    "id": "rss:https://arxiv.org/abs/2510.02906",
    "domain": "金融",
    "title": "FinMultiHopQA: A KG-Grounded Multi-Hop Financial QA Benchmark for Evidence-Driven Reasoning",
    "url": "https://arxiv.org/abs/2510.02906",
    "source": "Abhinav Arun, Reetu Raj Harsh, Bhaskarjit Sarmah, Stefano Pasquali",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T05:00:00+00:00",
    "summary": "arXiv:2510.02906v2 Announce Type: replace Abstract: Multi-hop financial question answering often requires composing evidence distributed across filing sections, fiscal years, and peer companies. Prior"
  },
  {
    "id": "rss:https://arxiv.org/abs/2512.16587",
    "domain": "金融",
    "title": "Did a feedback mechanism between propositional and prescriptive knowledge create modern growth?",
    "url": "https://arxiv.org/abs/2512.16587",
    "source": "Julius Koschnick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T05:00:00+00:00",
    "summary": "arXiv:2512.16587v3 Announce Type: replace Abstract: Joel Mokyr has argued that self-sustained modern growth originated from a feedback loop between propositional (theoretical) and prescriptive (applie"
  },
  {
    "id": "rss:https://arxiv.org/abs/2602.07688",
    "domain": "金融",
    "title": "Could It Have Fit Anything? Restrictiveness of Economic Models, LLMs, and AI Workflows",
    "url": "https://arxiv.org/abs/2602.07688",
    "source": "Drew Fudenberg, Wayne Yuan Gao, Zhiheng You",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T05:00:00+00:00",
    "summary": "arXiv:2602.07688v4 Announce Type: replace Abstract: How much does a prediction procedure rule out when its model class is unspecified? We extend restrictiveness from economic models to black-box proce"
  },
  {
    "id": "rss:https://arxiv.org/abs/2603.22569",
    "domain": "金融",
    "title": "Proxy-Reliance Control in Conformal Recalibration of One-Sided Value-at-Risk",
    "url": "https://arxiv.org/abs/2603.22569",
    "source": "Tenghan Zhong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T05:00:00+00:00",
    "summary": "arXiv:2603.22569v2 Announce Type: replace Abstract: We introduce a proxy-reliance-controlled conformal recalibration framework for one-sided Value-at-Risk (VaR), and study a question that existing sta"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.05011",
    "domain": "金融",
    "title": "Reaction-boundary variance and adjoint-consistent local-volatility projection",
    "url": "https://arxiv.org/abs/2607.05011",
    "source": "Christopher Angstmann, Tim Gebbie",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T05:00:00+00:00",
    "summary": "arXiv:2607.05011v4 Announce Type: replace Abstract: We derive an operational-time variance kernel for a latent-order-book reaction boundary and use it to separate three objects usually collapsed in ca"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.37820",
    "domain": "金融",
    "title": "Information Games: Strategic Crowding and Firm Repositioning in Language-Model Space",
    "url": "https://arxiv.org/abs/2609.37820",
    "source": "Marcus Gawronsky, Chun-Sung Huang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T05:00:00+00:00",
    "summary": "arXiv:2609.37820v2 Announce Type: replace Abstract: When firms respond to new market opportunities, their capacity choices alter the future discounted free cash flows available to both competitors and"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.11093",
    "domain": "金融",
    "title": "Risk Ceilings and Development Deadlines: Pacing AI under Uncertain Safety Productivity",
    "url": "https://arxiv.org/abs/2610.11093",
    "source": "Li Gan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T05:00:00+00:00",
    "summary": "arXiv:2610.11093v3 Announce Type: replace Abstract: Can a regulator promise both a risk ceiling and a development deadline when safety productivity is unknown? A ceiling below the final model's unprot"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.14305",
    "domain": "金融",
    "title": "Safety Research and the Allocation of Frontier Compute",
    "url": "https://arxiv.org/abs/2610.14305",
    "source": "Li Gan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T05:00:00+00:00",
    "summary": "arXiv:2610.14305v2 Announce Type: replace Abstract: During a frontier takeoff period, an AI lab splits a committed stock of compute among capability research, safety research, and customers, and a reg"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.00958",
    "domain": "金融",
    "title": "Quantifying Repair Risk in Crypto Option Surfaces",
    "url": "https://arxiv.org/abs/2611.00958",
    "source": "Tenghan Zhong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T05:00:00+00:00",
    "summary": "arXiv:2611.00958v2 Announce Type: replace Abstract: Option desks adjust crypto option quotes into price surfaces that remain within bid-ask intervals and satisfy standard no-arbitrage restrictions acr"
  },
  {
    "id": "rss:https://arxiv.org/abs/2401.16754",
    "domain": "金融",
    "title": "Human Responses to Algorithmic Correction: Evidence from Centre Court",
    "url": "https://arxiv.org/abs/2401.16754",
    "source": "David Almog, Romain Gauriot, Lionel Page, Daniel Martin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T05:00:00+00:00",
    "summary": "arXiv:2401.16754v5 Announce Type: replace-cross Abstract: We study how algorithmic review changes error composition using Hawk-Eye records from professional tennis. Within 20 mm of the line, mistaken "
  },
  {
    "id": "rss:https://arxiv.org/abs/2511.07235",
    "domain": "金融",
    "title": "Deep Neural Operator Learning for Probabilistic Models",
    "url": "https://arxiv.org/abs/2511.07235",
    "source": "Erhan Bayraktar, Qi Feng, Zecheng Zhang, Zhaoyu Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T05:00:00+00:00",
    "summary": "arXiv:2511.07235v2 Announce Type: replace-cross Abstract: We propose a deep neural-operator framework for a general class of probabilistic models. Under global Lipschitz conditions on the operator ove"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.21042",
    "domain": "金融",
    "title": "Absolute Continuity of Monotone Aggregations under Positive Regression Dependence",
    "url": "https://arxiv.org/abs/2606.21042",
    "source": "Ben Goldys, Max Nendel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T05:00:00+00:00",
    "summary": "arXiv:2606.21042v2 Announce Type: replace-cross Abstract: In this paper, we provide sufficient conditions for the absolute continuity of one-dimensional push-forwards of dependent random vectors. Supp"
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
  }
]
```
