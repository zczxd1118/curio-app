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

- 今日日期：`2026-11-13`
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
  "date": "2026-11-13",
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
    "points": 2114776,
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
    "points": 1502695,
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
    "points": 1490288,
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
    "points": 1459503,
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
    "points": 912794,
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
    "points": 899789,
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
    "points": 752354,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV17sAte3Exh",
    "domain": "AI",
    "title": "AI做高质量PPT从写到讲的全流程拆解，一期给你讲透！【旁门左道PPT】",
    "url": "http://www.bilibili.com/video/av114039887759711",
    "source": "旁门左道PPT",
    "platform": "bilibili",
    "points": 667523,
    "published_at": "2025-02-21T04:08:12+00:00",
    "summary": "更新一期2025年最新的Ai做PPT-全流程实操教程！&lt;不是那种一键生成通用型PPT的--！&gt;这次我帮大家把做PPT从写到说的全流程拆解出来了，极致压榨各种Ai工具在各个环节使劲儿，去帮大家做出有内容有分析长得还可以的PPT，全程高能，记得码住再看~"
  },
  {
    "id": "bvid:BV1aDMezREUj",
    "domain": "AI",
    "title": "Cursor使用教程，2小时玩转cursor，cursor无限续杯",
    "url": "http://www.bilibili.com/video/av114691716154833",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 596469,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV1vG8QzcE5X",
    "domain": "AI",
    "title": "Claude使用指南，claude code零基础教程，claude code安装配置到实战",
    "url": "http://www.bilibili.com/video/av114933744272468",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 358451,
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
    "points": 354112,
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
    "points": 326147,
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
    "points": 298054,
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
    "points": 232470,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1bHER6pEdD",
    "domain": "AI",
    "title": "【2026最新版】这绝对是B站最全面的最系统的AIGC教程，从零基础到精通（全程干货）小白必看！通俗易懂——学完即能就业",
    "url": "http://www.bilibili.com/video/av116724510951654",
    "source": "AIGC炼丹日志",
    "platform": "bilibili",
    "points": 223213,
    "published_at": "2026-06-10T10:00:00+00:00",
    "summary": "本套教程专门为零基础学员而制，全程干货无废话，喜欢的小伙伴记得点赞三连喔~\n【视频配套籽料+问题1对1解答，请看 ”置顶平论” 自取哦】"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 186623,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1468g6DEWs",
    "domain": "AI",
    "title": "【全100集】(允许白嫖) 2026最全最细的AI教程零基础入门到精通，一周带你小白变大神！全程干货无废话！存下吧，少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av117115386404821",
    "source": "AI产品经理入门教程-",
    "platform": "bilibili",
    "points": 183947,
    "published_at": "2026-08-18T13:11:45+00:00",
    "summary": "【2026最新版AI教程零基础入门到精通｜配套学习路线+工具包+实战项目，看置顶评论自取】\n 本套教程专为零基础设计，从AI是什么到独立用AI解决实际问题，手把手带你系统走完从入门到精通的完整路径。 ✅ AI认知入门：什么是AI/大模型、它们能做什么不能做什么、别被营销话术忽悠\n✅ 核心技能掌握：提示词工程、多轮对话技巧、让AI稳定输出的方法论\n✅ 进阶能力突破：AI工作流搭建、智能体开发、多工具"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 165758,
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
    "points": 163137,
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
    "points": 161941,
    "published_at": "2025-02-18T13:13:51+00:00",
    "summary": "我试用了几十种AI编程辅助工具，找到了其中三个免费，并且效果最好的方案。 本期视频就来跟大家分享一下。视频中间会穿插很多AI编程工具的使用技巧，还有看待AI编程的一些个人思考。本期视频没有广告都是个人的经验干货，废话不多说我们直接开始。"
  },
  {
    "id": "bvid:BV1nM6dBdER6",
    "domain": "AI",
    "title": "vscode如何使用AI编程",
    "url": "http://www.bilibili.com/video/av115875633960242",
    "source": "波哥的编程课",
    "platform": "bilibili",
    "points": 153895,
    "published_at": "2026-01-11T08:58:44+00:00",
    "summary": "如何在vs code中使用AI进行开发，推荐了国产AI编程助手，包括安装扩展、注册登录、选择模型、生成代码和微调代码等步骤。同时，强调AI编程还有很多复杂方面，欢迎在评论区留言。"
  },
  {
    "id": "bvid:BV1eYPpeWEnT",
    "domain": "AI",
    "title": "Cursor + MCP = 王炸！彻底颠覆我的Cursor工作流，效率直接起飞",
    "url": "http://www.bilibili.com/video/av114073660301264",
    "source": "御风大世界",
    "platform": "bilibili",
    "points": 151804,
    "published_at": "2025-02-27T03:19:03+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1kGo6BdEsT",
    "domain": "AI",
    "title": "如何用Claude Skill 做高质量 PPT（附完整教程）",
    "url": "http://www.bilibili.com/video/av116474832361424",
    "source": "阿西_出海",
    "platform": "bilibili",
    "points": 104550,
    "published_at": "2026-04-27T04:45:20+00:00",
    "summary": "很多人问我上期爆了的那条视频里，那个 PPT 是怎么做的。\n其实我是用 Anthropic 最近出的 Claude Design 做的，这个功能一发出来就在全网传疯了，一条推文就冲上了 6000 多万曝光。\n本期视频我会带你手把手从 0 到 1 把这个Skill 装好，然后一起跑一个成品效果出来。"
  },
  {
    "id": "bvid:BV1JY4w6kEAe",
    "domain": "AI",
    "title": "【全网首发】Claude防封号独家指南！前后花了5万元！小白保姆级教程【包含对话铺垫/IP DNS/订阅方式/历史记录清除】",
    "url": "http://www.bilibili.com/video/av117546107800312",
    "source": "Gemini3-",
    "platform": "bilibili",
    "points": 103741,
    "published_at": "2026-11-02T09:26:34+00:00",
    "summary": "视频内已经将所有的网站进行打码，没有吐露任何网址，也没有推广违规AI服务\n简介无推广内容\n视频中演示网站有正规ICP备案与ICP许可"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operit教程：入门安卓最强大ai平台operitAI",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 78133,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1h3W76wEem",
    "domain": "AI",
    "title": "Claude(Code)桌面APP，保姆级全攻略，一期视频精通，顶级Agent软件长什么样？",
    "url": "http://www.bilibili.com/video/av117580048108571",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 77007,
    "published_at": "2026-11-08T09:14:07+00:00",
    "summary": "最近Claude桌面端（Claude Desktop） 有了一大波功能更新。随着一步步的迭代，它已经把 Claude Code 的编程、Claude Design 的设计，以及 Claude Cowork 的办公等核心能力，全部收入了同一个桌面客户端，特别是Claude Code已经从原本黑乎乎的命令行工具，进化成了桌面客户端的完全体形态。再搭配上超强的Opus5.5 模型，已经能称得上是地表顶级"
  },
  {
    "id": "bvid:BV11XWR6ZEBu",
    "domain": "AI",
    "title": "我的第一个出海产品，亏成狗了！",
    "url": "http://www.bilibili.com/video/av117602932235824",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 57849,
    "published_at": "2026-11-12T10:14:18+00:00",
    "summary": "我搞了个新公司，利用 AI 编程做了个全球化的新产品 memecub，借助 SEO 和 GEO 很快就有自然流量了，感谢这个 Vibe Coding 时代，但是真的能盈利么？程序员第一次做出海产品，分享下感受。\n编程学习教程+实战项目+简历模板：codefather.cn\n免费 AI 编程教程：github.com/liyupi/ai-guide\n记得三连支持、关注鱼皮，让更多朋友学到知识哦~"
  },
  {
    "id": "bvid:BV1RrZHYqEvm",
    "domain": "AI",
    "title": "Cursor+Figma MCP，自动生成可编辑设计稿",
    "url": "http://www.bilibili.com/video/av114257538650701",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 52826,
    "published_at": "2025-03-31T14:36:31+00:00",
    "summary": "分享了两种Figma MCP。一种是通过获取Figma API key来实现Cursor和Figma的连接，更侧重精准控制。\n.\n因为大多数 Figma 文件都会非常大，如果你想让Cursor精准链接到文件中的特定元素，一般选择这个MCP会更合适。\n.\n另一种则是通过Figma插件形式，通过channel实现与Cursor的连接，更侧重从0到1的设计元素生成，比较适合没有太多设计基础的用户。\n.\n"
  },
  {
    "id": "bvid:BV17Lap6VEUr",
    "domain": "AI",
    "title": "【全80集】Vibe Coding 零基础入门到实战教程，由浅入深（全程干货）",
    "url": "http://www.bilibili.com/video/av117353572468721",
    "source": "数据拾光屋",
    "platform": "bilibili",
    "points": 51791,
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
    "points": 50432,
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
    "points": 45087,
    "published_at": "2026-04-05T11:00:20+00:00",
    "summary": "2026年最全面的Microsoft Copilot教程上半部分。从Copilot首页入门到Agent深度解析，涵盖搜索、资料库、AI视频生成、Copilot Pages、PowerPoint智能幻灯片等全部功能。由培训了6万人的AI顾问Cherie Brock与Sabrina Ramonov联合讲解。"
  },
  {
    "id": "bvid:BV1XiD5BQEAj",
    "domain": "AI",
    "title": "Claude Code 接入微信、一行命令把Claude Code装进微信、保姆级教程、微信支持Claude Code（cc-connect）远程开发",
    "url": "http://www.bilibili.com/video/av116350093694897",
    "source": "下班学AI",
    "platform": "bilibili",
    "points": 41397,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 34686,
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
    "points": 33252,
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
    "points": 29954,
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
    "points": 29058,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1B97868EZK",
    "domain": "AI",
    "title": "Claude Code全流程开发实战丨MCP实战、Skills+Agent多工具协作、AI编程、自动化工作流、私有化部署、转行AI岗",
    "url": "http://www.bilibili.com/video/av116810192131401",
    "source": "博学谷",
    "platform": "bilibili",
    "points": 27694,
    "published_at": "2026-06-25T10:11:09+00:00",
    "summary": "视频配套资源领取方式戳：https://www.bilibili.com/opus/1217780115004456969\n或关注【博学谷】公综号回复关键词领取：260625\n学完本课程，你将能够独立完成AI Agent 研发与落地：深度掌握 Claude Code 辅助编程、Skill 技能包编排与 MCP 协议集成打通私有系统连接的“桥梁”，并能学会私有化部署。最终凭借“AI Coding 重"
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 26813,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1uwxG6DEra",
    "domain": "AI",
    "title": "3分钟讲透：Vibe Coding如何避免💩屎山代码",
    "url": "http://www.bilibili.com/video/av117513727838880",
    "source": "鲤哥builder",
    "platform": "bilibili",
    "points": 26782,
    "published_at": "2026-10-27T16:09:19+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22857,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1f57C6YErb",
    "domain": "AI",
    "title": "手把手教你Codex安装和使用MCP！新手必备~",
    "url": "http://www.bilibili.com/video/av116696861907147",
    "source": "Raina测试",
    "platform": "bilibili",
    "points": 19335,
    "published_at": "2026-06-06T11:29:00+00:00",
    "summary": "这一期给大家分享下在codex里面如何配置和使用MCP，和skill一样，MCP也是我们平时用得比较多的，所以建议大家也可以学一下它的基础配置和使用~\n步骤都不难，跟着操作就可以了"
  },
  {
    "id": "bvid:BV18TZYY8EuJ",
    "domain": "AI",
    "title": "微软最新AI Agent入门课程 • 中英",
    "url": "http://www.bilibili.com/video/av114246130076146",
    "source": "Mindofuture",
    "platform": "bilibili",
    "points": 18864,
    "published_at": "2025-03-30T02:06:00+00:00",
    "summary": "在这门包含10节课的课程中，我们将带你从概念到代码，全面覆盖构建AI代理的基础知识。在这里找到完整的“AI代理入门”课程及代码示例\nhttps://github.com/microsoft/ai-agents-for-beginners\n\nP01 什么是AI代理\nP02 使用哪种AI代理框架\nP03 如何设计优秀的AI代理\nP04 什么是代理工具使用设计模式\nP05 什么是代理式RAG\nP06 如"
  },
  {
    "id": "bvid:BV1htCnY4ET6",
    "domain": "AI",
    "title": "用 Cursor AI 写 flutter 直接喂设计图就行 | flutter教程",
    "url": "http://www.bilibili.com/video/av113723805008238",
    "source": "独立开发者_猫哥",
    "platform": "bilibili",
    "points": 18203,
    "published_at": "2024-12-27T08:21:35+00:00",
    "summary": "✏️【关于本期视频】\n在上一篇文章《Flutter 使用 Cursor 和 Figma 快速生成界面代码》中，有同学提到他直接使用了设计稿的图片进行生成。我试了一下，效果确实很好。因此，我整理了一些文档，希望对大家有所帮助。\n下图展示了我没有手动编写任何代码实现的消息首页，支持上下滑动刷新数据。\n👉 文档 https://ducafecat.com/blog/use-cursor-ai-flutt"
  },
  {
    "id": "bvid:BV1YGKJ6tEdz",
    "domain": "AI",
    "title": "Vibe Coding我的赛博女友",
    "url": "http://www.bilibili.com/video/av116933101950817",
    "source": "天工开帧",
    "platform": "bilibili",
    "points": 17264,
    "published_at": "2026-07-17T09:50:00+00:00",
    "summary": "Vibe Coding大赏之赛博女友。总体花费100个馒头左右，由于显存限制，目前实时数字人的版本没办法跑起来。目前可以24挂着，随时对话随时打断。作用嘛，除了聊天就是在我忙的时候顺手帮我查个东西。未来开发方向接入pi-agent，让它真正干活，当然，只是得上qwen27B以上得模型才有可用性。也就是说所有模型显存开销打底得36G以上。囧。当然如果不要无限制，可以接入在线模型或在线TTS，但是，我"
  },
  {
    "id": "bvid:BV1xh3C6cEGv",
    "domain": "AI",
    "title": "两周完成一篇SCI论文，用claude code帮你干",
    "url": "http://www.bilibili.com/video/av117002408559933",
    "source": "博士大师兄木水",
    "platform": "bilibili",
    "points": 16299,
    "published_at": "2026-07-29T08:53:04+00:00",
    "summary": "大师兄八股文SCI速成模板已制作成skill，手把手带你实现一键生成SCI论文初稿"
  },
  {
    "id": "bvid:BV1PUWX69EDC",
    "domain": "AI",
    "title": "DeepSeek Harness 省 token 终极指南！8 个省钱技巧",
    "url": "http://www.bilibili.com/video/av117602210876639",
    "source": "林粒粒呀",
    "platform": "bilibili",
    "points": 15664,
    "published_at": "2026-11-12T11:05:00+00:00",
    "summary": "8 个 DeepSeek Harness 省钱\n省 Token 实用技巧！"
  },
  {
    "id": "bvid:BV1yyQEBdEkm",
    "domain": "AI",
    "title": "【2026B站最全】Claude Code+软件测试实操教程!看完我直接删了收藏夹所有测试教程,从账号注册到Plan驱动测试项目,小白3天上手！",
    "url": "http://www.bilibili.com/video/av116408092525631",
    "source": "软件测试大神",
    "platform": "bilibili",
    "points": 15571,
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
    "points": 14648,
    "published_at": "2023-04-11T11:48:41+00:00",
    "summary": "免费， VS Code + CursorCode 插件，AI 帮你编写、调试代码"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 13951,
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
    "points": 13656,
    "published_at": "2025-09-22T00:00:00+00:00",
    "summary": "AI 自动操作你的电脑，解放双手，提升工作效率。"
  },
  {
    "id": "hn:50467087",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang resigns",
    "url": "https://apnews.com/article/nvidia-megaspeed-china-singapore-huang-5403f152a601cf82ce939f1d24fffa0f",
    "source": "lldb",
    "platform": "hackernews",
    "points": 3591,
    "published_at": "2026-11-12T13:52:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:50459703",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia is preparing to oust Jensen Huang",
    "url": "https://www.wsj.com/business/nvidia-is-preparing-to-oust-nvidia-ceo-jensen-huang-30f421ad",
    "source": "jbredeche",
    "platform": "hackernews",
    "points": 1217,
    "published_at": "2026-11-11T22:31:06+00:00",
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
    "points": 610,
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
    "id": "hn:50416801",
    "domain": "AI 算力 / 半导体",
    "title": "Statement from Nvidia board of directors",
    "url": "https://nvidianews.nvidia.com/news/statement-from-nvidia-board-of-directors",
    "source": "vincentchau",
    "platform": "hackernews",
    "points": 493,
    "published_at": "2026-11-08T20:26:43+00:00",
    "summary": ""
  },
  {
    "id": "hn:50459321",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang said to have had relationship with executive who reports to him",
    "url": "https://www.nytimes.com/2026/11/11/technology/jensen-huang-nvidia-affair.html",
    "source": "louiereederson",
    "platform": "hackernews",
    "points": 408,
    "published_at": "2026-11-11T22:03:58+00:00",
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
    "id": "hn:50473190",
    "domain": "AI 算力 / 半导体",
    "title": "Former Nvidia CEO Huang had a relationship with a second employee, sources say",
    "url": "https://www.reuters.com/technology/former-nvidia-ceo-huang-had-relationship-with-second-employee-sources-say-2026-11-12/",
    "source": "jbredeche",
    "platform": "hackernews",
    "points": 287,
    "published_at": "2026-11-12T19:51:33+00:00",
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
    "id": "hn:50471621",
    "domain": "AI 算力 / 半导体",
    "title": "Singapore Says U.S. Not Helpful on Investigation into Suspected Spy's Company",
    "url": "https://www.nytimes.com/2026/11/12/business/nvidia-megaspeed-alice-huang.html",
    "source": "tedd4u",
    "platform": "hackernews",
    "points": 174,
    "published_at": "2026-11-12T18:14:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:50467139",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia CEO Jensen Huang resigns after reports of second affair deepened scandal",
    "url": "https://www.bbc.co.uk/news/live/c6zjry11v8w1t",
    "source": "cognoboffin",
    "platform": "hackernews",
    "points": 168,
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
    "id": "hn:50473868",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang Third Affair Allegations Revealed",
    "url": "https://www.forbes.com/sites/alisondurkee/2026/11/12/jensen-huang-had-a-third-affair-with-another-nvidia-employee-report-says/",
    "source": "FinnLobsien",
    "platform": "hackernews",
    "points": 58,
    "published_at": "2026-11-12T20:36:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:50479721",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC Hacked",
    "url": "https://www.sec.gov/Archives/edgar/data/1046179/000104617926000800/a20261112statementregardin.htm",
    "source": "gmays",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-11-13T07:39:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:50467593",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang Resigns as Nvidia CEO After Affairs",
    "url": "https://www.nytimes.com/live/2026/11/12/business/nvidia-jensen-huang-resigns",
    "source": "speckx",
    "platform": "hackernews",
    "points": 23,
    "published_at": "2026-11-12T14:17:39+00:00",
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
    "id": "hn:50478724",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang's Last Hours as Nvidia CEO",
    "url": "https://www.bloomberg.com/news/articles/2026-11-13/inside-jensen-huang-s-final-hours-as-the-ceo-of-nvidia",
    "source": "ex-aws-dude",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-11-13T05:26:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:50463421",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's Disappearing Singapore Sales Deepen Mystery Around Megaspeed",
    "url": "https://www.wsj.com/business/earnings/nvidias-disappearing-singapore-sales-deepen-mystery-around-megaspeed-7d483180",
    "source": "ea016",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-11-12T05:31:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:50465687",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen's (Nvidia) Adventure",
    "url": "https://www.wheresyoured.at/jensens-bizarre-adventure/",
    "source": "vitorfblima",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-11-12T11:24:22+00:00",
    "summary": ""
  },
  {
    "id": "hn:50479703",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC Has Been Hacked",
    "url": "https://mlq.ai/news/tsmc-says-employee-personal-data-was-posted-online-from-a-cloud-providers-systems/",
    "source": "pretext",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-11-13T07:37:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:50452464",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Vera CPU Review: 2TB/S Memory Bandwidth, a Real x86 Rival",
    "url": "https://www.storagereview.com/review/nvidia-vera-cpu-review",
    "source": "rbanffy",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-11-11T12:06:22+00:00",
    "summary": ""
  },
  {
    "id": "hn:50460325",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia is reportedly preparing to fire Jensen Huang",
    "url": "https://www.theverge.com/tech/1031652/jensen-huang-rumor",
    "source": "bearseascape",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-11-11T23:15:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:50474251",
    "domain": "AI 算力 / 半导体",
    "title": "Alice Huang tied to Nvidia's biggest Chinese competitor",
    "url": "https://www.cnbc.com/2026/11/12/alice-huang-jensen-huang-nvidia-huawei.html",
    "source": "Betelbuddy",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-11-12T21:03:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:50424604",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's China Problem [pdf]",
    "url": "https://culperresearch.com/wp-content/uploads/2026/05/Culper_NVDA_5-13-2026.pdf",
    "source": "Erikun",
    "platform": "hackernews",
    "points": 42,
    "published_at": "2026-11-09T12:20:45+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/how-novogenius-mcu-devices-are-reshaping-the-automotive-edge-node/",
    "domain": "AI 算力 / 半导体",
    "title": "How NovoGenius® MCU+ Devices Are Reshaping the Automotive Edge Node",
    "url": "https://www.eetimes.com/how-novogenius-mcu-devices-are-reshaping-the-automotive-edge-node/",
    "source": "Christopher McGrady",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T10:41:03+00:00",
    "summary": "NOVOSENSE NovoGenius MCU+ chips integrate analog, power, and drivers, adding intelligence to automotive edge nodes for motor control, sensing and lighting. The post How NovoGenius® MCU+ Devices Are Re"
  },
  {
    "id": "rss:https://www.eetimes.com/jensen-resigns-over-second-affair/",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Resigns Over Second Affair",
    "url": "https://www.eetimes.com/jensen-resigns-over-second-affair/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T20:48:35+00:00",
    "summary": "Nvidia CEO’s second affair scandal in a week prompted his resignation, and the board is now searching for a new leader for the company. The post Jensen Resigns Over Second Affair appeared first on EE "
  },
  {
    "id": "rss:https://www.eetimes.com/design-smarter-energy-harvesting-for-battery-free-and-low-maintenance-devices-in-safety-security-applications/",
    "domain": "AI 算力 / 半导体",
    "title": "Design Smarter – Energy Harvesting for Battery-Free and Low-Maintenance Devices in Safety & Security applications",
    "url": "https://www.eetimes.com/design-smarter-energy-harvesting-for-battery-free-and-low-maintenance-devices-in-safety-security-applications/",
    "source": "Nexperia",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T15:00:00+00:00",
    "summary": "Battery-powered sensors and detectors underpin modern safety and security systems, yet they create a constant maintenance burden. Hundreds of devices need manual battery swaps, often in hard-to-reach "
  },
  {
    "id": "rss:https://www.eetimes.com/can-machines-see-a-sick-plant-before-a-farmer-can/",
    "domain": "AI 算力 / 半导体",
    "title": "Can Machines See a Sick Plant Before a Farmer Can?",
    "url": "https://www.eetimes.com/can-machines-see-a-sick-plant-before-a-farmer-can/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T13:00:00+00:00",
    "summary": "Soybean disease research shows the promise of hyperspectral imaging, while semiconductor advances could make spectral sensing affordable for farmers. The post Can Machines See a Sick Plant Before a Fa"
  },
  {
    "id": "rss:https://www.eetimes.com/connecting-ai-to-the-physical-world/",
    "domain": "AI 算力 / 半导体",
    "title": "Connecting AI to the Physical World",
    "url": "https://www.eetimes.com/connecting-ai-to-the-physical-world/",
    "source": "Eric K. C. Tsang, CEO and founder, Vicinity Technologies Limited",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T10:20:00+00:00",
    "summary": "Why specialized wireless devices and SDR software IP matter to the next wave of intelligent machines The post Connecting AI to the Physical World appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/harari-warns-tech-leaders-against-pursuing-ai-superintelligence/",
    "domain": "AI 算力 / 半导体",
    "title": "Harari Warns Tech Leaders Against Pursuing AI Superintelligence",
    "url": "https://www.eetimes.com/harari-warns-tech-leaders-against-pursuing-ai-superintelligence/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T08:30:00+00:00",
    "summary": "At Gartner IT Symposium/Xpo 2026, philosopher Yuval Noah Harari makes an appeal to delay artificial superintelligence as it threatens to erode human agency and democratic sovereignty. The post Harari "
  },
  {
    "id": "rss:https://www.eetimes.com/automotive-tech-forum-panel-discussion-the-make-or-break-milestones-toward-level-4-autonomous-driving/",
    "domain": "AI 算力 / 半导体",
    "title": "Automotive Tech Forum: Panel Discussion the Make-or-Break Milestones Toward Level 4 Autonomous Driving",
    "url": "https://www.eetimes.com/automotive-tech-forum-panel-discussion-the-make-or-break-milestones-toward-level-4-autonomous-driving/",
    "source": "AspenCore Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T23:39:41+00:00",
    "summary": "Explore the road to Level 4 autonomy as experts tackle safety, AI, regulation, and trust—watch the Automotive Tech Forum panel. The post Automotive Tech Forum: Panel Discussion the Make-or-Break Miles"
  },
  {
    "id": "rss:https://www.eetimes.com/automotive-tech-forum-the-current-state-of-sic-in-ev-design-and-how-its-evolving/",
    "domain": "AI 算力 / 半导体",
    "title": "Automotive Tech Forum: The Current State of Sic in EV Design and How It’s Evolving",
    "url": "https://www.eetimes.com/automotive-tech-forum-the-current-state-of-sic-in-ev-design-and-how-its-evolving/",
    "source": "AspenCore Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T23:34:28+00:00",
    "summary": "Explore how 800V SiC MOSFETs boost EV range, charging, and performance—and see what next-gen designs make possible. The post Automotive Tech Forum: The Current State of Sic in EV Design and How It&#82"
  },
  {
    "id": "rss:https://www.eetimes.com/automotive-tech-forum-lidar-is-key-to-safer-adas-and-autonomous-vehicles/",
    "domain": "AI 算力 / 半导体",
    "title": "Automotive Tech Forum: Lidar is Key to Safer ADAS and Autonomous Vehicles",
    "url": "https://www.eetimes.com/automotive-tech-forum-lidar-is-key-to-safer-adas-and-autonomous-vehicles/",
    "source": "AspenCore Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T23:28:21+00:00",
    "summary": "This keynote explores how LiDAR is shaping the future of mobility by improving safety, reliability, and performance in autonomous systems. The post Automotive Tech Forum: Lidar is Key to Safer ADAS an"
  },
  {
    "id": "rss:https://www.eetimes.com/automotive-tech-forum-gan-building-blocks-in-evs-and-their-design-roadmap-in-2026-and-beyond/",
    "domain": "AI 算力 / 半导体",
    "title": "Automotive Tech Forum: GaN Building Blocks in EV’s and Their Design Roadmap in 2026 and Beyond",
    "url": "https://www.eetimes.com/automotive-tech-forum-gan-building-blocks-in-evs-and-their-design-roadmap-in-2026-and-beyond/",
    "source": "AspenCore Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T23:22:01+00:00",
    "summary": "This keynote exmines GaN reliability and present the case for GaN being not only the most efficient solution, but also a necessary step for reducing system cost The post Automotive Tech Forum: GaN Bui"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/1994-jeep-cherokee-owner-hacks-32-year-old-car-with-claude-ai-to-pass-california-smog-tests-enthusiast-reverse-engineered-the-ancient-ecu-for-diagnostics-and-control",
    "domain": "AI 算力 / 半导体",
    "title": "1994 Jeep Cherokee owner hacks 32-year-old car with Claude AI to pass California smog tests",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/1994-jeep-cherokee-owner-hacks-32-year-old-car-with-claude-ai-to-pass-california-smog-tests-enthusiast-reverse-engineered-the-ancient-ecu-for-diagnostics-and-control",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T10:30:00+00:00",
    "summary": "An AI enthusiast managed to get his old 1994 Jeep Cherokee to pass the California smog tests thanks to the help of AI, a little electronics wiring skill, and $15 of components."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/macos/macos-on-pc-becomes-possible-again-thanks-to-apple-silicon-translator-for-x86-64-hackintosh-revival-project-currently-slow-and-not-very-stable",
    "domain": "AI 算力 / 半导体",
    "title": "macOS on PC becomes possible again thanks to Apple Silicon translator for x86-64",
    "url": "https://www.tomshardware.com/software/macos/macos-on-pc-becomes-possible-again-thanks-to-apple-silicon-translator-for-x86-64-hackintosh-revival-project-currently-slow-and-not-very-stable",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T10:00:00+00:00",
    "summary": "macOS on PCs becomes possible thanks to Apple Silicon translator for x86-64 — Hackintoshes"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/russias-google-says-nearly-3-percent-of-its-data-was-lost-after-crippling-ukraine-drone-strikes-opens-secret-availability-zones-yandex-cloud-blames-lack-of-user-backups-for-lost-data-now-forcibly-applies-backup-rules-by-default",
    "domain": "AI 算力 / 半导体",
    "title": "Russia’s Google says nearly 3% of its data was lost after crippling Ukraine drone strikes, opens secret availability zones",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/russias-google-says-nearly-3-percent-of-its-data-was-lost-after-crippling-ukraine-drone-strikes-opens-secret-availability-zones-yandex-cloud-blames-lack-of-user-backups-for-lost-data-now-forcibly-applies-backup-rules-by-default",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T21:00:00+00:00",
    "summary": "Yandex Cloud boasted that it had 'restored access to more than 97% of customer data' after Ukrainian drone attack damage."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/save-usd119-on-ddr5-ram-with-this-high-end-am5-gaming-combo-from-newegg-3-item-gaming-pc-combo-includes-9800x3d-32gb-corsair-vengeance-ddr5-ram-and-premium-msi-x870e-carbon-wifi-motherboard-for-only-usd1-250",
    "domain": "AI 算力 / 半导体",
    "title": "Save $119 on DDR5 RAM with this high-end AM5 gaming combo from Newegg",
    "url": "https://www.tomshardware.com/pc-components/save-usd119-on-ddr5-ram-with-this-high-end-am5-gaming-combo-from-newegg-3-item-gaming-pc-combo-includes-9800x3d-32gb-corsair-vengeance-ddr5-ram-and-premium-msi-x870e-carbon-wifi-motherboard-for-only-usd1-250",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T17:34:56+00:00",
    "summary": "Newegg's latest combo deal pairs 32GB of Corsair Vengeance DDR5-6000 RAM, Ryzen 7 9800X3D, a MSI X870E Carbon Wifi motherboard and a free Rosewill Frostmax 360mm AIO for only $1,250, a savings of $119"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/president-trump-says-apples-tim-cook-is-the-only-man-to-replace-jensen-huang-as-nvidia-ceo-proposes-a-legend-replaces-a-legend-in-call-for-apples-executive-chairman-of-its-board",
    "domain": "AI 算力 / 半导体",
    "title": "President Trump says Apple’s Tim Cook is the only man to replace Jensen Huang as Nvidia CEO",
    "url": "https://www.tomshardware.com/tech-industry/president-trump-says-apples-tim-cook-is-the-only-man-to-replace-jensen-huang-as-nvidia-ceo-proposes-a-legend-replaces-a-legend-in-call-for-apples-executive-chairman-of-its-board",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T16:16:54+00:00",
    "summary": "President Trump says Tim Cook should replace Jensen Huang as CEO of Nvidia."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/elon-musk-says-it-would-be-an-honor-to-hire-ousted-nvidia-ceo-jensen-huang-possible-projects-could-include-terafab-spacexs-planned-gpu-manufacturing-or-teslas-ai-accelerators",
    "domain": "AI 算力 / 半导体",
    "title": "Elon Musk says it ‘would be an honor’ to hire ousted Nvidia CEO Jensen Huang",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/elon-musk-says-it-would-be-an-honor-to-hire-ousted-nvidia-ceo-jensen-huang-possible-projects-could-include-terafab-spacexs-planned-gpu-manufacturing-or-teslas-ai-accelerators",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T15:46:04+00:00",
    "summary": "A random X poster urged Elon Musk to hire Jensen Huang just hours before the former Nvidia chief resigned from his position."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/power-supplies/corsair-hx1000i-shift-crystal-power-supply-review",
    "domain": "AI 算力 / 半导体",
    "title": "Corsair HX1000i Shift Crystal power supply review: 1000W Platinum efficiency with an eye-catching transparent aesthetic",
    "url": "https://www.tomshardware.com/pc-components/power-supplies/corsair-hx1000i-shift-crystal-power-supply-review",
    "source": "E. Fylladitakis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T14:00:00+00:00",
    "summary": "Corsair puts the internals of a CWT-built, Cybenetics Platinum 1000W platform on display behind three clear panels, adding side-mounted connectors, iCUE LINK integration and per-pin 12V-2x6 protection"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/nvidia-confirms-jensen-huang-has-resigned-as-ceo-colette-kress-executive-vice-president-and-chief-financial-officer-appointed-interim-ceo",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia CEO Jensen Huang resigns in the wake of multiple affairs, Chinese spy allegations",
    "url": "https://www.tomshardware.com/tech-industry/nvidia-confirms-jensen-huang-has-resigned-as-ceo-colette-kress-executive-vice-president-and-chief-financial-officer-appointed-interim-ceo",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T13:58:41+00:00",
    "summary": "NVIDIA (NASDAQ: NVDA) Board of Directors announced today that Jensen Huang has resigned as President, Chief Executive Officer, and a member of the Board, effective immediately."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/thermal-paste/noctua-brings-space-grade-carbon-nanotube-thermal-pad-to-amd-am5-and-am4-processors-promises-years-of-maintenance-free-performance-for-usd24-95",
    "domain": "AI 算力 / 半导体",
    "title": "Noctua brings space-grade carbon nanotube thermal pad to AMD AM5 and AM4 processors",
    "url": "https://www.tomshardware.com/pc-components/thermal-paste/noctua-brings-space-grade-carbon-nanotube-thermal-pad-to-amd-am5-and-am4-processors-promises-years-of-maintenance-free-performance-for-usd24-95",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T13:04:13+00:00",
    "summary": "Noctua says the NT-CP1 uses carbon nanotubes originally developed for aerospace applications, with the material gradually adapting to microscopic surface imperfections to improve heat transfer over re"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/suspected-chinese-spy-at-center-of-jensen-huang-affair-surfaces-in-beijing-alice-huang-last-spotted-heading-to-shanghai-after-being-detained-questioned-in-singapore-in-2025-allegedly-helped-china-smuggle-hundreds-of-thousands-of-banned-chips",
    "domain": "AI 算力 / 半导体",
    "title": "Suspected Chinese spy at center of Jensen Huang affair surfaces in Beijing",
    "url": "https://www.tomshardware.com/tech-industry/suspected-chinese-spy-at-center-of-jensen-huang-affair-surfaces-in-beijing-alice-huang-last-spotted-heading-to-shanghai-after-being-detained-questioned-in-singapore-in-2025-allegedly-helped-china-smuggle-hundreds-of-thousands-of-banned-chips",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T12:53:36+00:00",
    "summary": "There are multiple speculations about Alice Huang's s history and how she built her relationship with Jensen Huang."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-usd350-on-this-all-amd-1440p-gaming-desktop-with-9800x3d-rx-9070-also-features-32gb-of-ram-and-a-1tb-ssd-for-just-usd1-949",
    "domain": "AI 算力 / 半导体",
    "title": "Save $300 on this 1440p gaming PC with a 9800X3D and RTX 5070 right now",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-usd350-on-this-all-amd-1440p-gaming-desktop-with-9800x3d-rx-9070-also-features-32gb-of-ram-and-a-1tb-ssd-for-just-usd1-949",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T11:12:26+00:00",
    "summary": "Grab a CyberPowerPC machine with an RX 9070, 9800X3D, 32GB DDR5 and a 2TB SSD for $2,199."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/google-adds-two-new-specialized-chips-for-ai-agents-and-security-to-8th-gen-tpu-lineup-tpu-8i-max-puts-two-chips-on-one-package-for-long-context-work-tpu-8tx-swaps-arm-hosts-for-amd-epyc",
    "domain": "AI 算力 / 半导体",
    "title": "Google reworks TPU silicon into specialized systems for agents and security",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/google-adds-two-new-specialized-chips-for-ai-agents-and-security-to-8th-gen-tpu-lineup-tpu-8i-max-puts-two-chips-on-one-package-for-long-context-work-tpu-8tx-swaps-arm-hosts-for-amd-epyc",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T11:00:00+00:00",
    "summary": "Google’s TPU 8i Max and TPU 8tx reuse TPU 8i and TPU 8t silicon to target long-context agents and confidential inference."
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
    "points": 869,
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
    "points": 737,
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
    "points": 676,
    "published_at": "2026-11-10T12:11:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:50456791",
    "domain": "大厂 AI 动态",
    "title": "Gemini Decisions API",
    "url": "https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/",
    "source": "iamdelirium",
    "platform": "hackernews",
    "points": 561,
    "published_at": "2026-11-11T18:32:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:50471431",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Hydrogen",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/",
    "source": "dvaplima",
    "platform": "hackernews",
    "points": 531,
    "published_at": "2026-11-12T18:01:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:50411961",
    "domain": "大厂 AI 动态",
    "title": "Llama-modchip: 284B DeepSeek on 64GB RAM, no GPU",
    "url": "https://github.com/synchopate/llama-modchip",
    "source": "joshcsimmons",
    "platform": "hackernews",
    "points": 483,
    "published_at": "2026-11-08T10:22:04+00:00",
    "summary": ""
  },
  {
    "id": "hn:50472260",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Hydrogen and Orchestrator",
    "url": "https://antigravity.google/blog/gemini-4-hydrogen-in-google-antigravity/",
    "source": "jonbaer",
    "platform": "hackernews",
    "points": 420,
    "published_at": "2026-11-12T18:52:01+00:00",
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
    "id": "hn:50454306",
    "domain": "大厂 AI 动态",
    "title": "AlphaGenome 2",
    "url": "https://deepmind.google/blog/alphagenome-2-deciphering-how-cells-read-dna-to-better-understand-disease/",
    "source": "acossta",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-11-11T15:04:24+00:00",
    "summary": ""
  },
  {
    "id": "hn:50471428",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Hydrogen",
    "url": "https://deepmind.google/models/model-cards/gemini-4-hydrogen/",
    "source": "it_works",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-11-12T18:01:37+00:00",
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
    "id": "rss:https://www.theverge.com/tech/1032774/president-donald-trump-tim-cook-nvidia-jensen-huang",
    "domain": "大厂 AI 动态",
    "title": "Donald Trump really wants Tim Cook to run Nvidia",
    "url": "https://www.theverge.com/tech/1032774/president-donald-trump-tim-cook-nvidia-jensen-huang",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T00:46:07+00:00",
    "summary": "Jensen Huang resigned this morning as Nvidia's CEO following reports of affairs, including one with an alleged Chinese spy. Right now, the company is being led by its CFO on an interim basis. But Pres"
  },
  {
    "id": "rss:https://www.theverge.com/news/1032431/xbox-bethesda-wolfenstein-3",
    "domain": "大厂 AI 动态",
    "title": "Xbox announces Wolfenstein 3",
    "url": "https://www.theverge.com/news/1032431/xbox-bethesda-wolfenstein-3",
    "source": "Tom Warren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T00:11:44+00:00",
    "summary": "It's been nearly a decade since Bethesda's MachineGames released Wolfenstein II: The New Colossus in 2017, and now Xbox is ready to announce a sequel from the studio. Wolfenstein 3 was officially anno"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1032630/whoop-humans-social-network",
    "domain": "大厂 AI 动态",
    "title": "Whoop launched a social network where every user has a ‘verified heartbeat’",
    "url": "https://www.theverge.com/gadgets/1032630/whoop-humans-social-network",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T23:43:22+00:00",
    "summary": "Starting Thursday, Whoop members can share their data from its wearables on the app's new Whoop Humans social network. Users can make their metrics, activities, and achievements visible to other Whoop"
  },
  {
    "id": "rss:https://www.theverge.com/games/1032659/humble-bundle-redesign-two-factor-verification-security-settings",
    "domain": "大厂 AI 动态",
    "title": "Humble Bundle redesign removes two-factor verification from settings",
    "url": "https://www.theverge.com/games/1032659/humble-bundle-redesign-two-factor-verification-security-settings",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T23:30:52+00:00",
    "summary": "The Humble Bundle storefront for buying games and other software recently got a new look, but on the settings page, it no longer offers a way to add or update two-factor verification methods, as repor"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1032226/microsoft-outlook-is-down",
    "domain": "大厂 AI 动态",
    "title": "Microsoft Outlook is still down",
    "url": "https://www.theverge.com/tech/1032226/microsoft-outlook-is-down",
    "source": "Richard Lawler",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T23:24:13+00:00",
    "summary": "Since just before 1PM ET on Thursday, reports have come in from around the world that people can't access their Outlook email, either through the web or apps. Microsoft quickly acknowledged the issue "
  },
  {
    "id": "rss:https://www.theverge.com/news/1032396/xbox-dashboard-guide-menu-right-side-background-shuffle-feature",
    "domain": "大厂 AI 动态",
    "title": "Xbox owners are getting more customizations for backgrounds and the Guide menu",
    "url": "https://www.theverge.com/news/1032396/xbox-dashboard-guide-menu-right-side-background-shuffle-feature",
    "source": "Tom Warren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T23:00:00+00:00",
    "summary": "Microsoft is starting to test new customization options for Xbox consoles today. Xbox Insiders will be able to start testing new rotating backgrounds, new library options for digital games, and the ab"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1032505/google-search-ai-mode-gemini-4-hydrogen",
    "domain": "大厂 AI 动态",
    "title": "Google’s new Gemini model is better at understanding complicated questions",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1032505/google-search-ai-mode-gemini-4-hydrogen",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T21:55:32+00:00",
    "summary": "Google says its new Gemini 4 Hydrogen model can give more helpful answers to complex questions, including \"questions with multiple parts, hard-to-understand typos, or highly specific requests.\" The ne"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1032434/nvidia-jensen-huang-resignation-reactions",
    "domain": "大厂 AI 动态",
    "title": "‘It’s a mistake’: reactions from tech leaders on Jensen Huang’s resignation",
    "url": "https://www.theverge.com/tech/1032434/nvidia-jensen-huang-resignation-reactions",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T21:45:00+00:00",
    "summary": "Nvidia announced this morning that Jensen Huang has resigned as CEO following reports of two affairs, including one with an alleged Chinese spy and one with a direct report. The situation surrounding "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1032311/oura-ring-4-smart-ring-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "The Oura Ring 4 is almost as good as the newer model, but $150 cheaper",
    "url": "https://www.theverge.com/gadgets/1032311/oura-ring-4-smart-ring-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T21:28:53+00:00",
    "summary": "The previous-generation Oura Ring 4 is on sale for as low as $249 at Amazon, Best Buy, and Target, $100 off the retail price, and the first big discount on the device since July. The price varies a bi"
  },
  {
    "id": "rss:https://www.theverge.com/games/1032321/microsoft-xbox-original-games-pc-backwards-compatibility",
    "domain": "大厂 AI 动态",
    "title": "Here are the 25 original Xbox games you can now play on PC",
    "url": "https://www.theverge.com/games/1032321/microsoft-xbox-original-games-pc-backwards-compatibility",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T21:00:00+00:00",
    "summary": "For the 25th anniversary of Xbox, Microsoft is beginning to make good on its paid \"next-gen game preservation\" promise. Starting today, you can play 25 different original Xbox games on your Windows PC"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/12/democrats-launch-nvidia-investigation-write-scathing-letter-on-huangs-scheme-with-trump/",
    "domain": "大厂 AI 动态",
    "title": "Democrats launch Nvidia investigation, write scathing letter on Huang’s ‘scheme’ with Trump",
    "url": "https://techcrunch.com/2026/11/12/democrats-launch-nvidia-investigation-write-scathing-letter-on-huangs-scheme-with-trump/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T22:42:51+00:00",
    "summary": "This Congressional investigation into Nvidia's China sales and its dealings with Trump is the second one, so far, since news of the alleged spy affair broke."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/12/muse-can-now-place-calls-to-u-s-businesses-if-you-pay/",
    "domain": "大厂 AI 动态",
    "title": "Muse can now place calls to US businesses — if you pay",
    "url": "https://techcrunch.com/2026/11/12/muse-can-now-place-calls-to-u-s-businesses-if-you-pay/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T22:22:28+00:00",
    "summary": "Muse's AI can now place outbound calls to U.S. businesses — but it's not free."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/12/nvidia-ceo-jensen-huangs-affair-with-alleged-chinese-spy-a-timeline/",
    "domain": "大厂 AI 动态",
    "title": "The unfolding Jensen Huang scandal: a timeline",
    "url": "https://techcrunch.com/2026/11/12/nvidia-ceo-jensen-huangs-affair-with-alleged-chinese-spy-a-timeline/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T21:35:00+00:00",
    "summary": "Jensen Huang has resigned from Nvidia following an affair, which could have ramifications for national security as the U.S. and China race to develop the most advanced AI infrastructure."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/12/nebius-tests-the-neocloud-playbook-with-40-billion-in-planned-spending/",
    "domain": "大厂 AI 动态",
    "title": "Nebius tests the neocloud playbook with $40 billion in planned spending",
    "url": "https://techcrunch.com/2026/11/12/nebius-tests-the-neocloud-playbook-with-40-billion-in-planned-spending/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T21:27:10+00:00",
    "summary": "Nebius plans to fund its $40 billion AI infrastructure expansion through customer prepayments and loans, even as delays at a Microsoft data center raise questions about its financing model."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/12/jensen-huang-was-having-a-third-affair-reuters-reports/",
    "domain": "大厂 AI 动态",
    "title": "Jensen Huang was having a third affair, Reuters reports",
    "url": "https://techcrunch.com/2026/11/12/jensen-huang-was-having-a-third-affair-reuters-reports/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T20:26:47+00:00",
    "summary": "Reuters is withholding the name of the new employee linked to Huang, but says she is an employee of Nvidia."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/12/googles-latest-search-upgrade-promises-better-answers-to-your-most-complicated-questions/",
    "domain": "大厂 AI 动态",
    "title": "Google’s latest Search upgrade promises better answers to your most complicated questions",
    "url": "https://techcrunch.com/2026/11/12/googles-latest-search-upgrade-promises-better-answers-to-your-most-complicated-questions/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T19:27:45+00:00",
    "summary": "Powered by Gemini 4 Hydrogen, Google's AI Mode is getting better at understanding complex queries, surfacing relevant links, and delivering richer visual responses."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/12/nectar-launches-an-ai-agent-to-automate-creator-discovery-and-outreach-for-brands/",
    "domain": "大厂 AI 动态",
    "title": "Nectar launches an AI agent to automate creator discovery and outreach for brands",
    "url": "https://techcrunch.com/2026/11/12/nectar-launches-an-ai-agent-to-automate-creator-discovery-and-outreach-for-brands/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T19:11:00+00:00",
    "summary": "Nectar's new AI agent automates influencer marketing, helping brands discover creators, manage outreach and partnerships, and track campaign results."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/12/microsofts-outlook-email-hit-by-new-outage/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft’s Outlook email hit by new outage",
    "url": "https://techcrunch.com/2026/11/12/microsofts-outlook-email-hit-by-new-outage/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T19:03:39+00:00",
    "summary": "Microsoft hasn't yet given a cause for the outage, which is affecting Outlook email users."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/12/jensen-huangs-exit-puts-nvidias-support-for-open-source-in-question/",
    "domain": "大厂 AI 动态",
    "title": "Jensen Huang’s exit puts Nvidia’s support for open source in question",
    "url": "https://techcrunch.com/2026/11/12/jensen-huangs-exit-puts-nvidias-support-for-open-source-in-question/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T18:39:23+00:00",
    "summary": "Jensen Huang’s resignation raises questions about Nvidia’s commitment to open source AI, including its Hugging Face acquisition, open-weight models, and advocacy against restrictions, as the company n"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/12/hugging-face-ceo-vows-to-keep-fighting-for-open-source-ai-after-jensen-huangs-exit/",
    "domain": "大厂 AI 动态",
    "title": "Hugging Face CEO vows to keep fighting for open source AI after Jensen Huang’s exit",
    "url": "https://techcrunch.com/2026/11/12/hugging-face-ceo-vows-to-keep-fighting-for-open-source-ai-after-jensen-huangs-exit/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T17:36:40+00:00",
    "summary": "Hugging Face's CEO pledged to keep fighting for open source AI after Huang's exit, raising questions about Nvidia's $12.9 billion acquisition."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/12/united-airlines-blocks-ai-agents-from-booking-flights-citing-cybersecurity-risks/",
    "domain": "大厂 AI 动态",
    "title": "United Airlines blocks AI agents from booking flights, citing cybersecurity risks",
    "url": "https://techcrunch.com/2026/11/12/united-airlines-blocks-ai-agents-from-booking-flights-citing-cybersecurity-risks/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T17:17:58+00:00",
    "summary": "The airline said it will not allow customers to use AI agents to book flights and manage reservations."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/12/softbanks-billion-dollar-loss-may-have-put-a-cap-on-ais-natural-gas-ambitions/",
    "domain": "大厂 AI 动态",
    "title": "SoftBank’s billion-dollar loss may have put a cap on AI’s natural gas ambitions",
    "url": "https://techcrunch.com/2026/11/12/softbanks-billion-dollar-loss-may-have-put-a-cap-on-ais-natural-gas-ambitions/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T17:00:52+00:00",
    "summary": "SoftBank lost over $3 billion preordering natural gas turbines to power AI data centers. Here's what the loss means to power markets."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/12/phota-labs-uses-ai-to-turn-everyday-photos-into-professional-looking-shots/",
    "domain": "大厂 AI 动态",
    "title": "Phota Labs uses AI to turn everyday photos into professional-looking shots",
    "url": "https://techcrunch.com/2026/11/12/phota-labs-uses-ai-to-turn-everyday-photos-into-professional-looking-shots/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T17:00:00+00:00",
    "summary": "Rather than giving consumers yet another photo-editing tool, Phota Labs aims to use advances in AI to automate the editing process so it’s easier for anyone to turn everyday moments into better photos"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/12/jensen-huang-agrees-to-testify-before-congress/",
    "domain": "大厂 AI 动态",
    "title": "Jensen Huang agrees to testify before Congress",
    "url": "https://techcrunch.com/2026/11/12/jensen-huang-agrees-to-testify-before-congress/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T16:36:37+00:00",
    "summary": "Huang, who was ousted as CEO following reports of an alleged affair with a woman suspected of spying for China, agreed to testify Wednesday after several senior lawmakers threatened to subpoena him."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/12/five-ways-jensen-huangs-ouster-from-nvidia-could-damage-the-ai-industry/",
    "domain": "大厂 AI 动态",
    "title": "Five ways Jensen Huang’s ouster from Nvidia could damage the AI industry",
    "url": "https://techcrunch.com/2026/11/12/five-ways-jensen-huangs-ouster-from-nvidia-could-damage-the-ai-industry/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T16:32:33+00:00",
    "summary": "Nvidia's ousted CEO Jensen Huang's downfall isn’t just your run-of-the-mill salacious billionaire sex scandal. He was using his influence to push the AI industry in some very specific ways."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/12/trump-floats-apple-chairman-tim-cook-as-jensen-huangs-successor/",
    "domain": "大厂 AI 动态",
    "title": "Trump floats Apple chairman Tim Cook as Jensen Huang’s successor",
    "url": "https://techcrunch.com/2026/11/12/trump-floats-apple-chairman-tim-cook-as-jensen-huangs-successor/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T16:12:44+00:00",
    "summary": "In a post on Truth Social, President Trump says only one man can take Jensen Huang's place as head of Nvidia: Tim Cook."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/12/whoop-just-launched-a-social-network/",
    "domain": "大厂 AI 动态",
    "title": "Whoop just launched a social network",
    "url": "https://techcrunch.com/2026/11/12/whoop-just-launched-a-social-network/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T16:00:00+00:00",
    "summary": "Whoop is launching a social network that lets members share their sleep, recovery, and workout data, but the bigger bet is on becoming more of a personal health brand, with CEO Will Ahmed hinting at a"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/12/jensen-huang-is-out-at-nvidia-who-is-colette-kress-his-interim-replacement/",
    "domain": "大厂 AI 动态",
    "title": "Jensen Huang is out at Nvidia — who is Colette Kress, his interim replacement?",
    "url": "https://techcrunch.com/2026/11/12/jensen-huang-is-out-at-nvidia-who-is-colette-kress-his-interim-replacement/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T15:37:29+00:00",
    "summary": "Nvidia CFO Colette Kress is taking over as an interim replacement for longtime CEO Jensen Huang, who is embroiled in scandal."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/12/norwest-pushes-deeper-into-ai-with-new-4b-fund/",
    "domain": "大厂 AI 动态",
    "title": "Norwest pushes deeper into AI with new $4B fund",
    "url": "https://techcrunch.com/2026/11/12/norwest-pushes-deeper-into-ai-with-new-4b-fund/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T15:18:14+00:00",
    "summary": "This is the investment firm's largest fund to date."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/12/cyberattack-on-fireworks-ai-allowed-hackers-to-access-notion-customers-chat-transcripts/",
    "domain": "大厂 AI 动态",
    "title": "Cyberattack on Fireworks AI allowed hackers to access Notion customers’ chat transcripts",
    "url": "https://techcrunch.com/2026/11/12/cyberattack-on-fireworks-ai-allowed-hackers-to-access-notion-customers-chat-transcripts/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T15:02:28+00:00",
    "summary": "This is Fireworks' second data breach in as many months."
  },
  {
    "id": "rss:https://stratechery.com/2026/sharp-tech-on-video-nvidia-after-jensen-huang-ominous-news-for-american-ai-d-c-gets-its-revenge/",
    "domain": "大厂 AI 动态",
    "title": "Sharp Tech on Video: Nvidia After Jensen Huang, Ominous News for American AI, D.C. Gets Its Revenge",
    "url": "https://stratechery.com/2026/sharp-tech-on-video-nvidia-after-jensen-huang-ominous-news-for-american-ai-d-c-gets-its-revenge/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T03:47:52+00:00",
    "summary": "Sharp Tech is, for the first time, available on video. You have three ways to consume it: YouTube, Spotify, and here on Stratechery"
  },
  {
    "id": "rss:https://stratechery.com/2026/an-interview-with-roblox-ceo-david-baszucki-about-aggregating-play/",
    "domain": "大厂 AI 动态",
    "title": "An Interview With Roblox CEO David Baszucki About Aggregating Play",
    "url": "https://stratechery.com/2026/an-interview-with-roblox-ceo-david-baszucki-about-aggregating-play/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T11:00:00+00:00",
    "summary": "An interview with Roblox CEO David Baszucki about how AI is transforming game creation, and why that opens up huge opportunities to both enable developers and make Roblox both an Aggregator and a plat"
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
    "id": "hn:50346153",
    "domain": "股票",
    "title": "Intel stock collapse worsens as $3.5T chip rout spreads",
    "url": "https://finance.yahoo.com/markets/article/the-intel-stock-collapse-is-getting-worse--and-the-37-trillion-chip-rout-is-spreading-212154947.html",
    "source": "entryleveljobsc",
    "platform": "hackernews",
    "points": 236,
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
    "points": 200,
    "published_at": "2026-11-02T19:27:37+00:00",
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
    "id": "hn:50391456",
    "domain": "金融",
    "title": "Tesla to wind down Cybertruck production",
    "url": "https://www.nbcnews.com/tech/tech-news/tesla-wind-cybertruck-production-years-poor-sales-markets-rcna607817",
    "source": "PLenz",
    "platform": "hackernews",
    "points": 1163,
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
    "points": 524,
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
    "id": "hn:50475829",
    "domain": "金融",
    "title": "Richard Posner has died",
    "url": "https://www.law.uchicago.edu/news/senior-lecturer-richard-posner-law-and-economics-pioneer-and-former-federal-appellate-judge",
    "source": "sebg",
    "platform": "hackernews",
    "points": 47,
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
    "id": "hn:50122776",
    "domain": "金融",
    "title": "Show HN: Stoke Money – Personal finance app built around a cash flow forecast",
    "url": "https://stoke.money",
    "source": "_wesley",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-10-16T18:54:47+00:00",
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
    "id": "hn:50459679",
    "domain": "电子信息与芯片",
    "title": "Jensen Huang had a second affair – with an employee",
    "url": "https://www.cnbc.com/2026/11/11/nvidia-jensen-huang-affair-employee.html",
    "source": "justswim",
    "platform": "hackernews",
    "points": 52,
    "published_at": "2026-11-11T22:29:27+00:00",
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
  }
]
```
