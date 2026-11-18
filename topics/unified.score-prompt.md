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

- 今日日期：`2026-11-18`
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
  "date": "2026-11-18",
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
    "id": "bvid:BV1ABu96JEAR",
    "domain": "AI",
    "title": "【保姆级教程】WorkBuddy彻底玩明白！只看这一期就够了！10节付费课内容全公开，完整工作流+实战技巧全揭秘，零基础一小时从入门到精通【附完整资料】",
    "url": "http://www.bilibili.com/video/av117069685262348",
    "source": "workbuddy应用实战",
    "platform": "bilibili",
    "points": 2192948,
    "published_at": "2026-08-10T06:05:50+00:00",
    "summary": "这可能是B站最全的WorkBuddy免费教程。咱们把付费课程做成了免费课程，感谢观众大老爷的两币奉上，有喜欢的也可以一键三连。 评论“蓝皮书”领取全套资料\n我花了整整一周，从安装到实战到管理思维，把WorkBuddy这个腾讯云AI桌面工作台拆成了10步，每一步都带实操。你不需要任何基础，跟着点就行。"
  },
  {
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "8分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 2133440,
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
    "points": 1542283,
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
    "points": 1502006,
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
    "points": 1474655,
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
    "points": 914922,
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
    "points": 904466,
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
    "points": 757242,
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
    "points": 596975,
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
    "points": 428418,
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
    "points": 359929,
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
    "points": 329264,
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
    "points": 300975,
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
    "points": 236321,
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
    "points": 187167,
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
    "points": 179979,
    "published_at": "2026-08-07T12:15:00+00:00",
    "summary": "这期视频，我会手把手带你，用 AI 做出你的第一个 App。\n全程假设你没有任何编程和AI的基础，\n我们从如何写需求提示词开始，\n到确定页面结构和设计，\n产品需求文档，\n开发计划，\n第一版APP验收，\ngit代码存档，\n二次开发，\n界面美化，\n做好的APP也会开源给到大家，\n我也会演示如何获取这个项目源代码并且用AI继续定制开发，\n视频到最后，\n你会收获一个为自己的工作和生活定制的专属APP！\n和"
  },
  {
    "id": "bvid:BV1h3W76wEem",
    "domain": "AI",
    "title": "Claude(Code)桌面APP，保姆级全攻略，一期视频精通，顶级Agent软件长什么样？",
    "url": "http://www.bilibili.com/video/av117580048108571",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 179537,
    "published_at": "2026-11-08T09:14:07+00:00",
    "summary": "最近Claude桌面端（Claude Desktop） 有了一大波功能更新。随着一步步的迭代，它已经把 Claude Code 的编程、Claude Design 的设计，以及 Claude Cowork 的办公等核心能力，全部收入了同一个桌面客户端，特别是Claude Code已经从原本黑乎乎的命令行工具，进化成了桌面客户端的完全体形态。再搭配上超强的Opus5.5 模型，已经能称得上是地表顶级"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 166313,
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
    "points": 163761,
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
    "points": 162092,
    "published_at": "2025-02-18T13:13:51+00:00",
    "summary": "我试用了几十种AI编程辅助工具，找到了其中三个免费，并且效果最好的方案。 本期视频就来跟大家分享一下。视频中间会穿插很多AI编程工具的使用技巧，还有看待AI编程的一些个人思考。本期视频没有广告都是个人的经验干货，废话不多说我们直接开始。"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 94345,
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
    "points": 77063,
    "published_at": "2026-03-11T18:12:00+00:00",
    "summary": "本期给大家带来的是Claude在Vscode的科研应用演示与我最近的一些心得使用心得，科研速度嘎嘎提升。论文复现画图、数据分析就靠Claude code。这个课程也是科研推土机「系统管理文献课程2.0」学员催我更新的内容，希望能帮助到大家～，这个视频重点讲两个事情：\n1️⃣ 资料获取，free不用怀疑，我是良心可言博主，，关注我(GZTSHNR)～\n2️⃣ 展示如何在VS code实操应用clau"
  },
  {
    "id": "bvid:BV1cVW86JE2e",
    "domain": "AI",
    "title": "Vibe Coding 完不会获客？我用 AI 做了一个「营销数据库」！【B站AI创造公开赛】",
    "url": "http://www.bilibili.com/video/av117587245599812",
    "source": "熠辉IndieDev",
    "platform": "bilibili",
    "points": 74077,
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
    "points": 64147,
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
    "points": 58801,
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
    "points": 57026,
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
    "points": 50593,
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
    "points": 47840,
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
    "points": 46526,
    "published_at": "2026-04-05T11:00:20+00:00",
    "summary": "2026年最全面的Microsoft Copilot教程上半部分。从Copilot首页入门到Agent深度解析，涵盖搜索、资料库、AI视频生成、Copilot Pages、PowerPoint智能幻灯片等全部功能。由培训了6万人的AI顾问Cherie Brock与Sabrina Ramonov联合讲解。"
  },
  {
    "id": "bvid:BV1thQPYfEYC",
    "domain": "AI",
    "title": "全流程演示Cursor + Blender MCP实现自动3D建模",
    "url": "http://www.bilibili.com/video/av114155835103525",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 44791,
    "published_at": "2025-03-13T15:31:17+00:00",
    "summary": "自动3D建模这个例子，是不是让大家一下子就看懂MCP的用途了。\n.\n后面会实测更多Cursor+MCP的更多玩法，欢迎继续围观\n.\n欢迎加入我的知识星球，有问必答：https://t.zsxq.com/fD4Fb\n.\nblender mcp项目：https://github.com/ahujasid/blender-mcp/tree/main"
  },
  {
    "id": "bvid:BV1XiD5BQEAj",
    "domain": "AI",
    "title": "Claude Code 接入微信、一行命令把Claude Code装进微信、保姆级教程、微信支持Claude Code（cc-connect）远程开发",
    "url": "http://www.bilibili.com/video/av116350093694897",
    "source": "下班学AI",
    "platform": "bilibili",
    "points": 41489,
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
    "points": 41032,
    "published_at": "2026-08-15T16:01:38+00:00",
    "summary": "这期用同一个 DeepSeek Pro 0813 模型，分别在 Claude Code 和 DeepSeek Harness 里完成同样的任务，对比工具链对最终效果的影响。\n实测内容包括：\nFPS 游戏 Demo、灯塔预警沙盘、手枪组装动画、显示器组装动画，以及 DeepSeek Harness 的插件化源码流程。\n整体看下来，模型本身当然重要，但 Harness 在插件化、流程记录、缓存命中和任"
  },
  {
    "id": "bvid:BV1g6fdYcEes",
    "domain": "AI",
    "title": "Cursor从小白到专家-第19课：如何用Cursor开发安卓APP？",
    "url": "http://www.bilibili.com/video/av113888322524233",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 29071,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 27275,
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
    "points": 26990,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22863,
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
    "points": 19631,
    "published_at": "2026-06-06T11:29:00+00:00",
    "summary": "这一期给大家分享下在codex里面如何配置和使用MCP，和skill一样，MCP也是我们平时用得比较多的，所以建议大家也可以学一下它的基础配置和使用~\n步骤都不难，跟着操作就可以了"
  },
  {
    "id": "bvid:BV1rvW761E7x",
    "domain": "AI",
    "title": "【全748集】目前B站最细最全的AI Agent搭建零基础全套教程，2026最新版，手把手教你搭建企业级Agent智能体！学完即可就业！让你少走99%弯路！！",
    "url": "http://www.bilibili.com/video/av117579779742632",
    "source": "Agent产品",
    "platform": "bilibili",
    "points": 17877,
    "published_at": "2026-11-08T08:11:42+00:00",
    "summary": "【全748集】目前B站最细最全的AI Agent搭建零基础全套教程，2026最新版，手把手教你搭建企业级Agent智能体！学完即可就业！让你少走99%弯路！！"
  },
  {
    "id": "bvid:BV1xh3C6cEGv",
    "domain": "AI",
    "title": "两周完成一篇SCI论文，用claude code帮你干",
    "url": "http://www.bilibili.com/video/av117002408559933",
    "source": "博士大师兄木水",
    "platform": "bilibili",
    "points": 16610,
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
    "points": 15609,
    "published_at": "2026-04-15T09:55:02+00:00",
    "summary": "配套资料👉：https://b23.tv/qvhxmaQ\n包括:AI测试网站，几十个AI场景测试完整流程，skil文档，测试八股文，项目源码，测试用例模板，工具安装包，学习计划表，学习路线，100g测试新人资料包等等，资料百分百免费，放心领取~"
  },
  {
    "id": "bvid:BV17YsJ6UEnW",
    "domain": "AI",
    "title": "国内稳定使用 Claude Code 保姆级教程-3 步搞定",
    "url": "http://www.bilibili.com/video/av117619675890528",
    "source": "小杨同学-毕业辅导",
    "platform": "bilibili",
    "points": 15362,
    "published_at": "2026-11-15T09:15:58+00:00",
    "summary": "实测稳定使用半个多月、零封号（个人经验，仅供参考）。\n这期分享我在国内使用 Claude Code 的完整流程，以及用了半年 Codex 之后转到 Claude 的真实感受。"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 14167,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
  },
  {
    "id": "bvid:BV11aYs6PE2p",
    "domain": "AI",
    "title": "AI Agent接入Photoshop：MCP 实现自然语言修图",
    "url": "http://www.bilibili.com/video/av117239051323475",
    "source": "W不懂跨境",
    "platform": "bilibili",
    "points": 14048,
    "published_at": "2026-09-09T03:54:24+00:00",
    "summary": "本期教程介绍 Photoshop MCP 的安装与配置，并演示如何将 AI Agent 接入 Photoshop，通过 MCP 调用 Photoshop 工具，实现自然语言控制与自动修图。\n\n最大的特点，也是大家都关心的问题：\n1、整个过程不需要Adobe Developer 账号。\n2、不需要购买额外的 AI 服务。\n3、不要求 Photoshop 必须为正版\n4、支持所有的 Photoshop"
  },
  {
    "id": "bvid:BV1Yhb66LEaF",
    "domain": "AI",
    "title": "3分钟，教你什么是vibe coding",
    "url": "http://www.bilibili.com/video/av117115000524101",
    "source": "开聊pro",
    "platform": "bilibili",
    "points": 14046,
    "published_at": "2026-08-18T06:12:25+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1wFpP6uE1s",
    "domain": "AI",
    "title": "【开源】让手机自己操作 App！手上的 ai Agent！GitHub开源安卓App推荐",
    "url": "http://www.bilibili.com/video/av117394643097499",
    "source": "补药满减哇",
    "platform": "bilibili",
    "points": 13504,
    "published_at": "2026-10-07T01:05:00+00:00",
    "summary": "开源安卓 AI Agent：RikkaHub Agent Pure\n它能「看懂」屏幕、自己操作各种 App，也能组队干活。\n\n⬇️ 下载 &amp; 源码（AGPL-3.0）\nhttps://github.com/wuyhong715/rikkahub-agent-pure\n\n▶ 本片讲两件事\n① 无障碍屏幕自动化：读控件树定位、实时决策，不是死坐标脚本\n② 专家团系统：每个专家有自己的模型/工具"
  },
  {
    "id": "bvid:BV1VqHM6iEXn",
    "domain": "AI",
    "title": "从零实现自己的agent第十一期：多agent协作",
    "url": "http://www.bilibili.com/video/av117496514418485",
    "source": "小单说AI",
    "platform": "bilibili",
    "points": 11573,
    "published_at": "2026-10-25T02:00:00+00:00",
    "summary": "源码地址放这里了：\n📦 教学仓库：https:// github.com/TheSyart/claude-agent-examples\n⚔️ 实战项目：https://github.com/TheSyart/emperor-agent\n我会持续更新 Agent 教学与实战内容。\n觉得有用的话，帮忙点个 Star ⭐\n谢谢大家支持。"
  },
  {
    "id": "bvid:BV1t9pt6JETF",
    "domain": "AI",
    "title": "Cursor vs Claude Code vs Codex哪个好？三大AI编程工具区别与选择指南",
    "url": "http://www.bilibili.com/video/av117411437090209",
    "source": "不管这么多",
    "platform": "bilibili",
    "points": 9742,
    "published_at": "2026-10-09T14:35:26+00:00",
    "summary": "三大编程工具要如何选？"
  },
  {
    "id": "bvid:BV1UaYK6nEjP",
    "domain": "AI",
    "title": "【cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av117244419903051",
    "source": "茶子兀",
    "platform": "bilibili",
    "points": 9424,
    "published_at": "2026-09-10T02:39:36+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1Gonv6CE5u",
    "domain": "AI",
    "title": "Codex做亚马逊运营｜AI自动化从安装到MCP接入·实操合集（持续更新）",
    "url": "http://www.bilibili.com/video/av117476432022910",
    "source": "知易聊亚马逊",
    "platform": "bilibili",
    "points": 7709,
    "published_at": "2026-10-21T02:10:20+00:00",
    "summary": "亚马逊运营AI提效｜Codex教程合集（安装配置+MCP接入全流程）"
  },
  {
    "id": "bvid:BV17ZuA6YESN",
    "domain": "AI",
    "title": "AI接管CATIA建模教程：从MCP配置到三维模型自动生成",
    "url": "http://www.bilibili.com/video/av117037204505522",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 7135,
    "published_at": "2026-08-05T02:00:00+00:00",
    "summary": "只需要输入自然语言，AI Agent就能自动操作CATIA完成三维建模？\n本期视频将详细讲解AI Agent通过MCP驱动CATIA V5建模的基本原理，并完整演示CATIA MCP的安装、配置与实际建模流程。\n通过MCP协议，AI Agent可以连接CATIA当前活动会话，调用CATIA原生API，根据用户需求自动拆分建模步骤，创建草图、拉伸特征、Part零件、GSD曲面、装配体及分析任务，并根"
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
    "points": 1113,
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
    "points": 819,
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
    "points": 558,
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
    "points": 482,
    "published_at": "2026-11-15T23:55:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:50501631",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia deliberately kept GPU prices high through circular financing deals",
    "url": "https://www.techspot.com/news/114558-nvidia-deliberately-kept-gpu-prices-high-through-circular.html",
    "source": "madihaa",
    "platform": "hackernews",
    "points": 451,
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
    "points": 386,
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
    "points": 287,
    "published_at": "2026-11-16T15:24:09+00:00",
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
    "points": 177,
    "published_at": "2026-11-15T23:24:53+00:00",
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
    "points": 135,
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
    "id": "hn:50538942",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Chair Harvey Jones says board doesn't intend to reinstate Huang as CEO",
    "url": "https://www.cnbc.com/2026/11/17/nvidia-nvda-earnings-report-q3-2027.html",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 54,
    "published_at": "2026-11-17T22:08:34+00:00",
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
    "id": "hn:50513876",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's Days as an Open Checkbook for the AI Economy Are Numbered",
    "url": "https://www.wsj.com/tech/ai/nvidias-days-as-an-open-checkbook-for-the-ai-economy-are-numbered-90c7b388",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 38,
    "published_at": "2026-11-16T04:03:51+00:00",
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
    "points": 35,
    "published_at": "2026-11-15T22:53:51+00:00",
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
    "id": "rss:https://www.eetimes.com/edge-ai-moves-agricultural-intelligence-from-the-cloud-to-the-field/",
    "domain": "AI 算力 / 半导体",
    "title": "Edge AI Moves Agricultural Intelligence from the Cloud to the Field",
    "url": "https://www.eetimes.com/edge-ai-moves-agricultural-intelligence-from-the-cloud-to-the-field/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T06:59:00+00:00",
    "summary": "NXP and Nvidia tackle the challenges of delivering computing power, energy efficiency, and safety as agricultural machinery becomes autonomous. The post Edge AI Moves Agricultural Intelligence from th"
  },
  {
    "id": "rss:https://www.eetimes.com/marc-hijink-on-asmls-culture-supply-chain-and-geopolitics/",
    "domain": "AI 算力 / 半导体",
    "title": "Marc Hijink on ASML’s Culture, Supply Chain, and Geopolitics",
    "url": "https://www.eetimes.com/marc-hijink-on-asmls-culture-supply-chain-and-geopolitics/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-17T22:37:22+00:00",
    "summary": "Explore how ASML’s partner-driven culture, EUV dominance, and geopolitical pressures reshaped chipmaking in Marc Hijink’s interview. The post Marc Hijink on ASML’s Culture, Supply Chain, and Geopoliti"
  },
  {
    "id": "rss:https://www.eetimes.com/everspin-looks-to-broaden-mram-adoption-with-lpddr-standard/",
    "domain": "AI 算力 / 半导体",
    "title": "Everspin Looks to Broaden MRAM Adoption with LPDDR Standard",
    "url": "https://www.eetimes.com/everspin-looks-to-broaden-mram-adoption-with-lpddr-standard/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-17T17:26:57+00:00",
    "summary": "An exploratory JEDEC task group is weighing how controller vendors could support MRAM with hard IP to work with newer LPDDR implementations. The post Everspin Looks to Broaden MRAM Adoption with LPDDR"
  },
  {
    "id": "rss:https://www.eetimes.com/ltcc-solutions-for-next-generation-uwb-ble-devices/",
    "domain": "AI 算力 / 半导体",
    "title": "LTCC Solutions for Next Generation UWB/BLE Devices",
    "url": "https://www.eetimes.com/ltcc-solutions-for-next-generation-uwb-ble-devices/",
    "source": "TAIYO YUDEN (U.S.A.) INC.",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-17T15:00:00+00:00",
    "summary": "Discover TAIYO YUDEN’s advanced LTCC (Low Temperature Co-fired Ceramic) solutions for UWB and Bluetooth Low Energy (BLE) applications. Featuring high-performance RF components, these solutions address"
  },
  {
    "id": "rss:https://www.eetimes.com/minimising-acoustic-noise-in-space-constrained-medical-and-life-science-applications/",
    "domain": "AI 算力 / 半导体",
    "title": "Minimizing Acoustic Noise in Space-Constrained Medical and Life Science Applications",
    "url": "https://www.eetimes.com/minimising-acoustic-noise-in-space-constrained-medical-and-life-science-applications/",
    "source": "Giulio Bocciolini, Senior Product Marketing Manager EMEA, TDK-Lambda EMEA",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-17T15:00:00+00:00",
    "summary": "Design engineers and technical decision-makers working on medical and life science equipment must balance competing demands: high power density, thermal performance, compact dimensions, and low acoust"
  },
  {
    "id": "rss:https://www.eetimes.com/intesa-sanpaolo-finds-value-before-quantum-computers-are-ready/",
    "domain": "AI 算力 / 半导体",
    "title": "Intesa Sanpaolo Finds Value Before Quantum Computers Are Ready",
    "url": "https://www.eetimes.com/intesa-sanpaolo-finds-value-before-quantum-computers-are-ready/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-17T09:16:07+00:00",
    "summary": "The banking group reports double-digit cost savings from quantum-inspired optimization, but useful quantum hardware faces a tougher test than faster calculations. The post Intesa Sanpaolo Finds Value "
  },
  {
    "id": "rss:https://www.eetimes.com/taking-a-tour-of-canadas-particle-accelerator/",
    "domain": "AI 算力 / 半导体",
    "title": "Taking a Tour of Canada’s Particle Accelerator",
    "url": "https://www.eetimes.com/taking-a-tour-of-canadas-particle-accelerator/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-16T17:52:31+00:00",
    "summary": "Located on Canada’s west coast, TRIUMF’s normal-conducting cyclotron, unique materials probes, and irradiation facilities serve everything from quantum materials and radiation-hardened electronics to "
  },
  {
    "id": "rss:https://www.eetimes.com/simplifying-power-design-with-%c2%b5module-solutions/",
    "domain": "AI 算力 / 半导体",
    "title": "Simplifying Power Design with µModule Solutions",
    "url": "https://www.eetimes.com/simplifying-power-design-with-%c2%b5module-solutions/",
    "source": "Analog Devices, Arrow Electronics",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-16T17:41:23+00:00",
    "summary": "Join this webinar to learn how highly integrated power solutions can simplify design, increase power density, and much more. The post Simplifying Power Design with µModule Solutions appeared first on "
  },
  {
    "id": "rss:https://www.eetimes.com/beyond-low-energy-new-product-frontiers-for-lossless-audio-edge-ai-and-display-streaming/",
    "domain": "AI 算力 / 半导体",
    "title": "Beyond Low Energy: New Product Frontiers for Lossless Audio, Edge-AI and Display Streaming",
    "url": "https://www.eetimes.com/beyond-low-energy-new-product-frontiers-for-lossless-audio-edge-ai-and-display-streaming/",
    "source": "Telink Semiconductor",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-16T17:19:44+00:00",
    "summary": "Join our expert-led webinar to discover how the TL753X SoC leverages High Definition Technology (HDT) for innovative applications. The post Beyond Low Energy: New Product Frontiers for Lossless Audio,"
  },
  {
    "id": "rss:https://www.eetimes.com/silicon-motherboard-enables-double-sided-integration-of-ics-and-passive-components/",
    "domain": "AI 算力 / 半导体",
    "title": "Silicon Motherboard Enables Double-Sided Integration of ICs and Passive Components",
    "url": "https://www.eetimes.com/silicon-motherboard-enables-double-sided-integration-of-ics-and-passive-components/",
    "source": "Nisshinbo Micro Devices",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-16T17:00:00+00:00",
    "summary": "Nisshinbo's Silicon Motherboard integrates ICs and passives on both sides of a silicon substrate, reducing mounting area by up to 90%. The post Silicon Motherboard Enables Double-Sided Integration of "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/china-threatens-countermeasures-on-the-face-of-new-ai-gpu-rental-and-export-restrictions-beijing-threatens-retaliation-ahead-of-thursdays-xi-jinping-meeting-sino-american-trade-war-may-be-renewed-for-a-new-season",
    "domain": "AI 算力 / 半导体",
    "title": "China threatens 'countermeasures' in the face of new AI GPU rental and export restrictions — Beijing threatens retaliation ahead of Thursday's Xi Jinping meeting, Sino-American trade war may be renewe",
    "url": "https://www.tomshardware.com/pc-components/gpus/china-threatens-countermeasures-on-the-face-of-new-ai-gpu-rental-and-export-restrictions-beijing-threatens-retaliation-ahead-of-thursdays-xi-jinping-meeting-sino-american-trade-war-may-be-renewed-for-a-new-season",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T11:00:00+00:00",
    "summary": "China threatens \"countermeasures\" on the face of new Blackwell rental and export restrictions — Sino-American trade war may be renewed for a new season"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/the-downfall-of-jensen-huang-a-timeline-of-allegations-and-scandals-that-brought-down-the-king-of-ai-infrastructure",
    "domain": "AI 算力 / 半导体",
    "title": "The Downfall of Jensen Huang — a timeline of allegations and scandals that brought down the king of AI infrastructure",
    "url": "https://www.tomshardware.com/tech-industry/the-downfall-of-jensen-huang-a-timeline-of-allegations-and-scandals-that-brought-down-the-king-of-ai-infrastructure",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T10:30:00+00:00",
    "summary": "Jensen’s affairs dominated headlines, but the seeds of his downfall were planted in both the bedroom and the boardroom and stretched from Beijing to Washington, with Nvidia sitting right in the middle"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/usd3-26-million-in-spacex-ai-data-center-revenue-will-be-pumped-back-into-the-city-of-memphis-up-to-usd25-000-on-offer-to-low-income-residents-for-repairs-and-home-improvements",
    "domain": "AI 算力 / 半导体",
    "title": "$3.26 million in SpaceX AI data center revenue will be pumped back into the City of Memphis",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/usd3-26-million-in-spacex-ai-data-center-revenue-will-be-pumped-back-into-the-city-of-memphis-up-to-usd25-000-on-offer-to-low-income-residents-for-repairs-and-home-improvements",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T10:00:00+00:00",
    "summary": "The City of Memphis is making its first major investment, almost $3.3 million, through the Community Benefit Ordinance. The fund was set up to use a portion of the tax generated by SpaceX AI's Colossu"
  },
  {
    "id": "rss:https://www.tomshardware.com/gift-guides-seasonal-sales/budget-friendly-gifts-for-gamers-keyboards-mice-headsets-and-more-under-usd80",
    "domain": "AI 算力 / 半导体",
    "title": "Budget-friendly gifts for gamers — keyboards, mice, headsets, and more under $80",
    "url": "https://www.tomshardware.com/gift-guides-seasonal-sales/budget-friendly-gifts-for-gamers-keyboards-mice-headsets-and-more-under-usd80",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T00:00:00+00:00",
    "summary": "The best budget-friendly gifts for gamers — keyboards, mice, headsets, and more, all for under $80."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/nvidia-employee-warns-of-irreplaceable-talent-exodus-if-jensen-huang-not-reinstated-cautions-board-and-top-brass-that-talent-at-nvidia-is-now-contemplating-departing",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia employee warns of 'irreplaceable' talent exodus if Jensen Huang not reinstated",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/nvidia-employee-warns-of-irreplaceable-talent-exodus-if-jensen-huang-not-reinstated-cautions-board-and-top-brass-that-talent-at-nvidia-is-now-contemplating-departing",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-17T21:00:00+00:00",
    "summary": "An internal letter was sent to Nvidia's board and top executives warning that \"irreplaceable talent\" could leave if Jensen Huang isn't reinstated as CEO."
  },
  {
    "id": "rss:https://www.tomshardware.com/gift-guides-seasonal-sales/10-desk-upgrade-gifts-to-improve-pc-work-and-gaming-spaces-a-monitor-riser-with-charging-and-usb-ports-an-excellent-speaker-upgrade-modern-charging-hubs-and-more",
    "domain": "AI 算力 / 半导体",
    "title": "10 desk upgrade gifts to improve PC work and gaming spaces",
    "url": "https://www.tomshardware.com/gift-guides-seasonal-sales/10-desk-upgrade-gifts-to-improve-pc-work-and-gaming-spaces-a-monitor-riser-with-charging-and-usb-ports-an-excellent-speaker-upgrade-modern-charging-hubs-and-more",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-17T21:00:00+00:00",
    "summary": "These 10 devices can make the desk space around a PC more versatile, enjoyable, and productive experience."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/nvidia-claims-its-vera-cpu-can-gain-up-to-39-percent-performance-boost-via-software-optimization-at-sc26-architectural-fine-tuning-is-needed-to-fully-unleash-custom-olympus-cores",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia claims its Vera CPU can gain up to 39% performance boost via software optimization at SC26 — architectural fine-tuning is needed to fully unleash custom Olympus cores",
    "url": "https://www.tomshardware.com/pc-components/cpus/nvidia-claims-its-vera-cpu-can-gain-up-to-39-percent-performance-boost-via-software-optimization-at-sc26-architectural-fine-tuning-is-needed-to-fully-unleash-custom-olympus-cores",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-17T17:30:00+00:00",
    "summary": "Nvidia's Vera CPU, powered by its custom Olympus Arm cores, already offers strong performance with unoptimized code, but at SC26, the company demonstrated that further software optimizations can impro"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/jensen-huang-says-he-would-be-honored-to-return-as-nvidia-ceo-first-statement-since-resignation-follows-support-from-billionaires-investors-and-some-employees",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang says he would be ‘honored’ to return as Nvidia CEO",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/jensen-huang-says-he-would-be-honored-to-return-as-nvidia-ceo-first-statement-since-resignation-follows-support-from-billionaires-investors-and-some-employees",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-17T16:33:23+00:00",
    "summary": "In his first statement since his resignation, former Nvidia CEO Jensen Huang expressed openness to returning to his former role."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-safety-legislation-has-a-conflict-of-interest-problem-big-us-labs-are-warning-of-risk-just-as-cheaper-chinese-open-weight-models-erode-their-commercial-edge",
    "domain": "AI 算力 / 半导体",
    "title": "AI safety legislation has a conflict-of-interest problem — Big US labs are warning of risk just as cheaper Chinese open-weight models erode their commercial edge",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-safety-legislation-has-a-conflict-of-interest-problem-big-us-labs-are-warning-of-risk-just-as-cheaper-chinese-open-weight-models-erode-their-commercial-edge",
    "source": "Chris Stokel-Walker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-17T16:00:00+00:00",
    "summary": "The AI safety conversation is as much a political one as it is a real-life worry. We interview experts to find out how legislation may be a convenient way to control the AI market."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/former-nvidia-ceo-jensen-huang-will-appear-before-a-house-foreign-affairs-panel-amid-concerns-over-his-affair-with-a-suspected-chinese-spy-will-testify-behind-closed-doors-december-1-nvidia-lawyer-will-also-appear",
    "domain": "AI 算力 / 半导体",
    "title": "Former Nvidia CEO Jensen Huang will appear before a House Foreign Affairs panel amid concerns over his affair with a suspected Chinese spy",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/former-nvidia-ceo-jensen-huang-will-appear-before-a-house-foreign-affairs-panel-amid-concerns-over-his-affair-with-a-suspected-chinese-spy-will-testify-behind-closed-doors-december-1-nvidia-lawyer-will-also-appear",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-17T15:50:51+00:00",
    "summary": "Former Nvidia CEO Jensen Huang will appear before the House Foreign Affairs, Intelligence, and China Select Committees on December 1, with Nvidia's lawyer following him on December 2. The appearances "
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
    "points": 739,
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
    "points": 573,
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
    "points": 570,
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
    "points": 507,
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
    "id": "hn:50541790",
    "domain": "大厂 AI 动态",
    "title": "Why is Gemini 4 Carbon taking so long?",
    "url": "https://kernel.dev/blog/why-is-gemini-4-carbon-taking-so-long/",
    "source": "deenadz",
    "platform": "hackernews",
    "points": 110,
    "published_at": "2026-11-18T04:14:04+00:00",
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
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1036415/suno-visuals-ai-generated-video-images-feature",
    "domain": "大厂 AI 动态",
    "title": "Suno now lets you make AI videos for your AI music",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1036415/suno-visuals-ai-generated-video-images-feature",
    "source": "Jess Weatherbed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T11:16:53+00:00",
    "summary": "Suno has introduced image and video generation in its latest effort to expand beyond being an AI music platform. The new feature, called \"Visuals,\" allows users to turn Suno songs into AI-generated vi"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/1035847/grand-theft-auto-6-launch-review-news",
    "domain": "大厂 AI 动态",
    "title": "Grand Theft Auto VI has arrived",
    "url": "https://www.theverge.com/entertainment/1035847/grand-theft-auto-6-launch-review-news",
    "source": "Andrew Webster",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T11:06:16+00:00",
    "summary": "More than a decade after Grand Theft Auto V was first released, its sequel is finally launching. On November 19th, GTA VI will be available on both the PS5 and Xbox Series X / S, and it’s quite possib"
  },
  {
    "id": "rss:https://www.theverge.com/games/1035801/grand-theft-auto-6-review",
    "domain": "大厂 AI 动态",
    "title": "Grand Theft Auto VI does something impossible — it lives up to the hype",
    "url": "https://www.theverge.com/games/1035801/grand-theft-auto-6-review",
    "source": "Andrew Webster",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T11:00:00+00:00",
    "summary": "How do you follow a game like Grand Theft Auto V? Thirteen years ago, Rockstar's crime-fueled epic went on to redefine what an open-world game could be and became an enormous success, selling more tha"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/1035806/grand-theft-auto-6-rob-nelson-interview",
    "domain": "大厂 AI 动态",
    "title": "‘It’s a risk’: How Rockstar built the most detailed (and romantic) GTA yet",
    "url": "https://www.theverge.com/entertainment/1035806/grand-theft-auto-6-rob-nelson-interview",
    "source": "Andrew Webster",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T11:00:00+00:00",
    "summary": "Grand Theft Auto VI isn't just the biggest GTA game to date; it's also the most romantic. Though the series is well known for its sordid assortment of criminal leads, GTA VI switches things up by star"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1036111/satya-nadella-says-hes-agi-pilled-now",
    "domain": "大厂 AI 动态",
    "title": "Satya Nadella says he’s AGI-pilled now",
    "url": "https://www.theverge.com/tech/1036111/satya-nadella-says-hes-agi-pilled-now",
    "source": "Nilay Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-17T23:41:18+00:00",
    "summary": "Microsoft CEO Satya Nadella says he's AGI-pilled, at least when it comes to how AI might make startling changes to the structure of the economy and how politics might change because of it. \"I am AGI-p"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/1036110/jeff-bezos-james-bond-casting-amazon",
    "domain": "大厂 AI 动态",
    "title": "Jeff Bezos says he was ‘heavily involved’ in picking the new James Bond",
    "url": "https://www.theverge.com/entertainment/1036110/jeff-bezos-james-bond-casting-amazon",
    "source": "Charles Pulliam-Moore",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-17T22:38:41+00:00",
    "summary": "Robert Pattinson's casting as James Bond made enough sense given his recent work with director Denis Villeneuve, who's making the franchise's next film over at Amazon. But it turns out that Amazon fou"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1036160/nvidia-earnings-harvey-c-jones-jensen-huang",
    "domain": "大厂 AI 动态",
    "title": "Read everything that Nvidia’s board chair had to say about Jensen Huang",
    "url": "https://www.theverge.com/tech/1036160/nvidia-earnings-harvey-c-jones-jensen-huang",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-17T22:32:50+00:00",
    "summary": "Nvidia's quarterly earnings call on Tuesday was its first with CFO and interim CEO Colette Kress at the helm alongside the company's first board chair, Harvey C. Jones. The leadership change followed "
  },
  {
    "id": "rss:https://www.theverge.com/tech/1036045/ifixit-teardown-apple-homeview-smart-home-hub",
    "domain": "大厂 AI 动态",
    "title": "iFixit’s Apple HomeView teardown reveals a device that will be difficult to repair",
    "url": "https://www.theverge.com/tech/1036045/ifixit-teardown-apple-homeview-smart-home-hub",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-17T22:25:41+00:00",
    "summary": "After finding recent versions of Apple's iPads and HomePods much easier to disassemble for battery replacements or other repairs, iFixit assumed it would be the same story for Apple's new HomeView hub"
  },
  {
    "id": "rss:https://www.theverge.com/report/1035465/nvidia-says-it-will-not-reinstate-jensen-huang-as-ceo",
    "domain": "大厂 AI 动态",
    "title": "Nvidia says it does not intend to reinstate Jensen Huang as CEO",
    "url": "https://www.theverge.com/report/1035465/nvidia-says-it-will-not-reinstate-jensen-huang-as-ceo",
    "source": "Hayden Field",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-17T22:05:05+00:00",
    "summary": "Starting Nvidia's quarterly earnings call on Tuesday, new board chair Harvey Jones said that when former CEO Jensen Huang resigned, \"the Nvidia board unanimously accepted his resignation and does not "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1035932/apple-macbook-neo-black-friday-2026-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "The MacBook Neo is receiving a rare $50 discount ahead of Black Friday",
    "url": "https://www.theverge.com/gadgets/1035932/apple-macbook-neo-black-friday-2026-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-17T21:46:20+00:00",
    "summary": "If you’re looking for a new laptop or a gift for the student in your life, you can save $50 on the MacBook Neo at several retailers, in both storage sizes and all four colors. The 256GB model is curre"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/18/china-dominates-battery-graphite-but-this-startup-could-break-the-monopoly/",
    "domain": "大厂 AI 动态",
    "title": "China dominates battery graphite, but this startup could break the monopoly",
    "url": "https://techcrunch.com/2026/11/18/china-dominates-battery-graphite-but-this-startup-could-break-the-monopoly/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T11:00:00+00:00",
    "summary": "Chinese companies maintain near total dominance of the graphite industry, but Molten Industries says its new factory in Oakland could spell the end of the monopoly."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/17/nvidias-startup-stakes-ballooned-to-65b-but-huangs-exit-puts-future-deals-in-doubt/",
    "domain": "大厂 AI 动态",
    "title": "Nvidia’s startup stakes ballooned to $65B, but Huang’s exit puts future deals in doubt",
    "url": "https://techcrunch.com/2026/11/17/nvidias-startup-stakes-ballooned-to-65b-but-huangs-exit-puts-future-deals-in-doubt/",
    "source": "Dominic-Madori Davis, Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T01:44:21+00:00",
    "summary": "The value of Nvidia’s private investments has nearly tripled over the past nine months, fueled by Jensen Huang’s aggressive dealmaking and rising valuations of its existing portfolio companies."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/17/nvidia-promises-that-revenue-will-keep-soaring-for-now/",
    "domain": "大厂 AI 动态",
    "title": "Nvidia promises that revenue will keep soaring — for now",
    "url": "https://techcrunch.com/2026/11/17/nvidia-promises-that-revenue-will-keep-soaring-for-now/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T00:16:50+00:00",
    "summary": "Despite the turmoil Nvidia is in after the departure of its disgraced founder and CEO Jensen Huang, the company projected that its streak of record-breaking revenue isn't about to stop."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/17/stripe-backer-atomico-calls-for-europe-to-own-its-success-stories/",
    "domain": "大厂 AI 动态",
    "title": "Stripe backer Atomico calls for Europe to own its success stories",
    "url": "https://techcrunch.com/2026/11/17/stripe-backer-atomico-calls-for-europe-to-own-its-success-stories/",
    "source": "Anna Heim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T00:01:00+00:00",
    "summary": "Europe is home to many of the world's fastest growing companies of all time, veteran VC firm Atomico highlighted in its latest annual State of European Tech report."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/17/nvidia-is-abandoning-china-after-jensen-huangs-ouster/",
    "domain": "大厂 AI 动态",
    "title": "Nvidia is abandoning China after Jensen Huang’s ouster",
    "url": "https://techcrunch.com/2026/11/17/nvidia-is-abandoning-china-after-jensen-huangs-ouster/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-17T23:37:48+00:00",
    "summary": "Nvidia's interim CEO says the company is done selling chips to China. How much will that cost?"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/17/nvidia-says-its-open-source-ai-strategy-remains-intact-after-jensen-huangs-exit/",
    "domain": "大厂 AI 动态",
    "title": "Nvidia says its open source AI strategy remains intact after Jensen Huang’s exit",
    "url": "https://techcrunch.com/2026/11/17/nvidia-says-its-open-source-ai-strategy-remains-intact-after-jensen-huangs-exit/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-17T23:04:35+00:00",
    "summary": "Nvidia's interim CEO reaffirmed its open source AI strategy and plans to acquire Hugging Face, despite Jensen Huang's sudden departure."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/17/nvidia-says-it-doesnt-plan-to-reappoint-jensen-huang-as-ceo/",
    "domain": "大厂 AI 动态",
    "title": "Nvidia says it doesn’t plan to reappoint Jensen Huang as CEO",
    "url": "https://techcrunch.com/2026/11/17/nvidia-says-it-doesnt-plan-to-reappoint-jensen-huang-as-ceo/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-17T22:42:27+00:00",
    "summary": "The former CEO offered to return to his top role at the company after his resignation last week."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/17/amazon-and-google-will-together-own-nearly-30-of-anthropic-after-its-ipo/",
    "domain": "大厂 AI 动态",
    "title": "Amazon and Google will together own nearly 30% of Anthropic after its IPO",
    "url": "https://techcrunch.com/2026/11/17/amazon-and-google-will-together-own-nearly-30-of-anthropic-after-its-ipo/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-17T22:29:05+00:00",
    "summary": "Amazon will own just under 15% of Anthropic after the IPO, with the option to go much higher. Google is a close second with holdings of nearly 14%."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/17/sec-reportedly-investigating-nvidia-amid-huang-exit/",
    "domain": "大厂 AI 动态",
    "title": "SEC reportedly investigating Nvidia amid Huang exit",
    "url": "https://techcrunch.com/2026/11/17/sec-reportedly-investigating-nvidia-amid-huang-exit/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-17T21:48:07+00:00",
    "summary": "The SEC is opening a probe into Nvidia following the departure of CEO Jensen Huang, who admitted to an affair with an alleged Chinese spy, reports The Wall Street Journal."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/17/google-joins-the-tech-outage-trend-by-announcing-its-not-having-one/",
    "domain": "大厂 AI 动态",
    "title": "Google joins the tech outage trend by announcing it’s not having one",
    "url": "https://techcrunch.com/2026/11/17/google-joins-the-tech-outage-trend-by-announcing-its-not-having-one/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-17T21:34:50+00:00",
    "summary": "With tech outages seemingly everywhere, Google took the unusual step of announcing that Gmail is working just fine, actually."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/17/waymo-suspends-freeway-rides-nationwide-after-california-dmv-order/",
    "domain": "大厂 AI 动态",
    "title": "Waymo suspends freeway rides nationwide after California DMV order",
    "url": "https://techcrunch.com/2026/11/17/waymo-suspends-freeway-rides-nationwide-after-california-dmv-order/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-17T19:49:41+00:00",
    "summary": "The DMV said Waymo's freeway operations pose an imminent hazard to public safety. Restrictions will remain in place until Waymo can demonstrate that it has taken \"effective corrective actions\" to addr"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/17/model-ml-raises-250m-to-automate-investment-banking-grunt-work/",
    "domain": "大厂 AI 动态",
    "title": "Model ML raises $250M to automate investment banking grunt work",
    "url": "https://techcrunch.com/2026/11/17/model-ml-raises-250m-to-automate-investment-banking-grunt-work/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-17T19:32:11+00:00",
    "summary": "The startup says its agents understand the full context of deals that bankers and consultants are working on and can automatically update financial models and presentations when new developments affec"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/17/google-expands-access-to-gemini-tasks-which-can-help-with-calls-purchases/",
    "domain": "大厂 AI 动态",
    "title": "Google expands access to Gemini Tasks, which can help with calls, purchases",
    "url": "https://techcrunch.com/2026/11/17/google-expands-access-to-gemini-tasks-which-can-help-with-calls-purchases/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-17T19:02:20+00:00",
    "summary": "Gemini's Task mode can help users coordinate calls, log into websites, and even make purchases on the user's behalf."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/17/apple-services-including-icloud-app-store-and-apple-music-hit-by-outage/",
    "domain": "大厂 AI 动态",
    "title": "Apple services, including iCloud, App Store, Apple Music, and more, hit by outage",
    "url": "https://techcrunch.com/2026/11/17/apple-services-including-icloud-app-store-and-apple-music-hit-by-outage/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-17T18:55:40+00:00",
    "summary": "Apple's status page confirms its services are facing outages, but has not confirmed the cause."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/17/google-to-keep-gemini-chats-for-two-months-up-from-72-hours-even-with-history-off/",
    "domain": "大厂 AI 动态",
    "title": "Google to keep Gemini chats for 2 months, up from 72 hours, even with history off",
    "url": "https://techcrunch.com/2026/11/17/google-to-keep-gemini-chats-for-two-months-up-from-72-hours-even-with-history-off/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-17T18:48:23+00:00",
    "summary": "Google's Gemini update extending chat retention will roll out globally over the coming weeks."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/17/as-decision-model-use-skyrockets-is-customization-is-the-next-frontier/",
    "domain": "大厂 AI 动态",
    "title": "As decision model use skyrockets, is customization the next frontier?",
    "url": "https://techcrunch.com/2026/11/17/as-decision-model-use-skyrockets-is-customization-is-the-next-frontier/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-17T18:10:00+00:00",
    "summary": "Sqwish Labs has a new wrinkle on the decision model: Train it with your own data to max its capabilities."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/17/pedestal-ai-raises-4-7-million-to-agentify-the-supply-chain/",
    "domain": "大厂 AI 动态",
    "title": "Pedestal AI raises $4.7 million to agentify the supply chain",
    "url": "https://techcrunch.com/2026/11/17/pedestal-ai-raises-4-7-million-to-agentify-the-supply-chain/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-17T18:04:16+00:00",
    "summary": "The company uses agentic AI to make supply chains faster and more reliable."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/17/protons-lumo-a-privacy-focused-alternative-to-chatgpt-and-claude-arrives-on-desktop/",
    "domain": "大厂 AI 动态",
    "title": "Proton’s Lumo, a privacy-focused alternative to ChatGPT and Claude, arrives on desktop",
    "url": "https://techcrunch.com/2026/11/17/protons-lumo-a-privacy-focused-alternative-to-chatgpt-and-claude-arrives-on-desktop/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-17T17:32:25+00:00",
    "summary": "Proton's new Lumo Desktop app for Windows, Mac, and Linux lets users automate tasks across files and connected apps, with granular controls over what its AI can access."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/17/ai-models-can-be-tricked-into-identifying-civilians-as-military-targets-by-telling-them-its-a-game/",
    "domain": "大厂 AI 动态",
    "title": "AI models can be tricked into identifying civilians as military targets by telling them it’s a game",
    "url": "https://techcrunch.com/2026/11/17/ai-models-can-be-tricked-into-identifying-civilians-as-military-targets-by-telling-them-its-a-game/",
    "source": "Kirsten Korosec, Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-17T17:20:41+00:00",
    "summary": "Vals, a San Francisco-based AI evaluation startup, tested whether leading AI models could be manipulated into participating in autonomous warfare. They usually compiled."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/17/jensen-huang-says-he-would-be-honored-if-allowed-to-return-as-nvidia-ceo/",
    "domain": "大厂 AI 动态",
    "title": "Jensen Huang says he would be ‘honored’ if allowed to return as Nvidia CEO",
    "url": "https://techcrunch.com/2026/11/17/jensen-huang-says-he-would-be-honored-if-allowed-to-return-as-nvidia-ceo/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-17T16:44:15+00:00",
    "summary": "In the first public statement since his resignation, Nvidia founder Jensen Huang signaled his willingness to return as CEO."
  },
  {
    "id": "rss:https://stratechery.com/2026/nvidia-earnings-office-convergence-os-wars-ai-edition/",
    "domain": "大厂 AI 动态",
    "title": "Nvidia Earnings; Office Convergence; OS Wars, AI Edition",
    "url": "https://stratechery.com/2026/nvidia-earnings-office-convergence-os-wars-ai-edition/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T11:00:00+00:00",
    "summary": "Nvidia's earnings were boring, and also a statement as to why Jensen Huang probably isn't coming back; then, Microsoft and Anthropic ship dueling operating system updates."
  },
  {
    "id": "rss:https://stratechery.com/2026/apple-permissions-update-the-new-app-paradigm-my-iphone-duo-review/",
    "domain": "大厂 AI 动态",
    "title": "Apple Permissions Update, The New App Paradigm, My iPhone Duo Review",
    "url": "https://stratechery.com/2026/apple-permissions-update-the-new-app-paradigm-my-iphone-duo-review/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-17T11:00:00+00:00",
    "summary": "Apple doesn't ruin the Mac, but they don't fix the agent problem, raising questions if they can think outside the app paradigm. Then, my iPhone Duo review."
  },
  {
    "id": "rss:https://arstechnica.com/gaming/2026/11/grand-theft-auto-vi-the-ars-technica-review/",
    "domain": "大厂 AI 动态",
    "title": "Grand Theft Auto VI: The Ars Technica review",
    "url": "https://arstechnica.com/gaming/2026/11/grand-theft-auto-vi-the-ars-technica-review/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T11:00:27+00:00",
    "summary": "Jason and Lucia's crime-heavy love story fuels a wonder of digital urban simulation."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/11/microsoft-calls-copilot-the-new-os-for-work-at-ignite-keynote/",
    "domain": "大厂 AI 动态",
    "title": "Copilot is \"the new OS for work,\" and now Office runs inside of it",
    "url": "https://arstechnica.com/gadgets/2026/11/microsoft-calls-copilot-the-new-os-for-work-at-ignite-keynote/",
    "source": "Nick Indge",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T00:27:29+00:00",
    "summary": "Word, Excel, and PowerPoint now live inside Copilot; always-on agents are next."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/11/san-diego-dumps-both-flock-cameras-and-smart-streetlights/",
    "domain": "大厂 AI 动态",
    "title": "San Diego dumps both Flock cameras and smart streetlights",
    "url": "https://arstechnica.com/tech-policy/2026/11/san-diego-dumps-both-flock-cameras-and-smart-streetlights/",
    "source": "Cyrus Farivar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-17T23:09:09+00:00",
    "summary": "500+ cameras will go dark just 3 years after mayor urged approval."
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
    "id": "hn:50510005",
    "domain": "股票",
    "title": "Do House members' stock trades beat the market? A test of 8,900 trades",
    "url": "https://arkanumdata.com/research/house-trades",
    "source": "Bluestein",
    "platform": "hackernews",
    "points": 127,
    "published_at": "2026-11-15T19:46:02+00:00",
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
    "points": 24,
    "published_at": "2026-11-12T05:31:52+00:00",
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
    "id": "hn:50383675",
    "domain": "股票",
    "title": "Wipeout for AI stocks sends Wall Street reeling and S&P 500 tumbles more than 3%",
    "url": "https://apnews.com/article/stocks-markets-ai-midterm-oil-trump-7ee9c212805aa5e70cf34d25aab7a36e",
    "source": "jethronethro",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-11-05T19:58:06+00:00",
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
    "id": "hn:50525658",
    "domain": "金融",
    "title": "Pentagon fails ninth straight audit despite progress in organizing finances",
    "url": "https://www.reuters.com/business/aerospace-defense/pentagon-fails-ninth-straight-audit-despite-progress-organizing-finances-2026-11-16/",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 149,
    "published_at": "2026-11-17T00:23:21+00:00",
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
    "id": "hn:50532322",
    "domain": "金融",
    "title": "A US Federal Women's Prison Became a \"Rape Club\"",
    "url": "https://www.propublica.org/article/federal-womens-prison-sexual-abuse-reform-dublin-bop",
    "source": "paimapi",
    "platform": "hackernews",
    "points": 81,
    "published_at": "2026-11-17T15:03:25+00:00",
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
    "points": 65,
    "published_at": "2026-11-15T10:53:50+00:00",
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
    "id": "rss:https://arxiv.org/abs/2611.21672",
    "domain": "金融",
    "title": "Who sees the sea? Sea-view potential by fa\\c{c}ade and floor from cadastral LoD1 models on the Costa del Sol",
    "url": "https://arxiv.org/abs/2611.21672",
    "source": "Gabriel Rojo (CASAS.ES)",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T05:00:00+00:00",
    "summary": "arXiv:2611.21672v1 Announce Type: new Abstract: Views are among the most valued and least measured attributes of a home. We present an open-data method that estimates the sea-view potential of every f"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.21897",
    "domain": "金融",
    "title": "Revisiting Equity-Bond Diversification under Tail Risk and Structural Market Change: Evidence from Global ETFs and Model-Implied Option Prices",
    "url": "https://arxiv.org/abs/2611.21897",
    "source": "Farzana Afroz, Abootaleb Shirvani, Nicholas Appiah, Svetlozar T. Rachev, Frank J. Fabozzi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T05:00:00+00:00",
    "summary": "arXiv:2611.21897v1 Announce Type: new Abstract: This study examines thirty equity--bond and multi-asset exchange-traded funds (ETFs) listed in the United States, Canada, and Australia using daily U.S."
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.22119",
    "domain": "金融",
    "title": "An axiomatic foundation for optimized certainty equivalents",
    "url": "https://arxiv.org/abs/2611.22119",
    "source": "Christopher Blier-Wong, Jean-Gabriel Lauzier, Zachary Van Oosten",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T05:00:00+00:00",
    "summary": "arXiv:2611.22119v1 Announce Type: new Abstract: Optimized Certainty Equivalents (OCEs) are an important class of risk measures for optimization and risk management that includes the Mean--Variance cri"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.22277",
    "domain": "金融",
    "title": "Explaining Realized Returns: Roll's $R^2$ 40 Years Later",
    "url": "https://arxiv.org/abs/2611.22277",
    "source": "Bryan Kelly, Yinan Su, Chao Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T05:00:00+00:00",
    "summary": "arXiv:2611.22277v1 Announce Type: new Abstract: Can we explain asset price movements even with hindsight? Reinterpreting Roll's (1988) AFA Presidential Address, \"$R^2$,\" as a modern empirical exercise"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.22517",
    "domain": "金融",
    "title": "Clicks, Carbon, and Risk: Climate Attention, Persistent Financial Risk, and Real-Sector Activity",
    "url": "https://arxiv.org/abs/2611.22517",
    "source": "Giovanni Angelini, Luca De Angelis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T05:00:00+00:00",
    "summary": "arXiv:2611.22517v1 Announce Type: new Abstract: Do shifts in public climate concern alter persistent financial risk and subsequently matter for real activity? We combine daily U.S. sectoral equity ret"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.22604",
    "domain": "金融",
    "title": "Beyond Strike Remapping: Conditional-Gamma Pricing of Leveraged ETF Options under Local Volatility",
    "url": "https://arxiv.org/abs/2611.22604",
    "source": "Guolin Chen, Jiang Zhou, Richard Ma, Xia Sheng, Anson Tse, Terry Wei",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T05:00:00+00:00",
    "summary": "arXiv:2611.22604v1 Announce Type: new Abstract: Options on leveraged ETFs (LETFs) are priced and hedged off the LETF volatility surface, but path-dependent variance drag makes that surface difficult t"
  },
  {
    "id": "rss:https://arxiv.org/abs/2009.00868",
    "domain": "金融",
    "title": "Loss-Given-Default Modeling by Post-Last Passage Time Process",
    "url": "https://arxiv.org/abs/2009.00868",
    "source": "Masahiko Egami",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T05:00:00+00:00",
    "summary": "arXiv:2009.00868v5 Announce Type: replace Abstract: We bridge the dichotomy between structural and intensity-based credit models by defining default via the last passage time ($\\lambda_\\alpha$) of a l"
  },
  {
    "id": "rss:https://arxiv.org/abs/2505.04555",
    "domain": "金融",
    "title": "Just After Minimum Wage Hikes: Short-Run Labor-Demand Response and Reallocation",
    "url": "https://arxiv.org/abs/2505.04555",
    "source": "Hayato Kanayama, Sho Miyaji, Suguru Otani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T05:00:00+00:00",
    "summary": "arXiv:2505.04555v4 Announce Type: replace Abstract: How labor markets adjust immediately after minimum wage hikes remains an open, policy-relevant question. This paper studies short-run minimum-wage e"
  },
  {
    "id": "rss:https://arxiv.org/abs/2601.05274",
    "domain": "金融",
    "title": "On the use of case estimate and transactional payment data in neural networks for individual loss reserving",
    "url": "https://arxiv.org/abs/2601.05274",
    "source": "Benjamin Avanzi, Matthew Lambrianidis, Greg Taylor, Bernard Wong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T05:00:00+00:00",
    "summary": "arXiv:2601.05274v2 Announce Type: replace Abstract: The use of neural networks trained on individual claims data has become increasingly popular in the actuarial reserving literature. We consider how "
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.08920",
    "domain": "金融",
    "title": "AI Adoption in S&P 500 Firms",
    "url": "https://arxiv.org/abs/2607.08920",
    "source": "Yang Yu, Martin Fleming, Lucy Hampton, Christophe Combemale, Neil Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T05:00:00+00:00",
    "summary": "arXiv:2607.08920v2 Announce Type: replace Abstract: The adoption of artificial intelligence (AI) by large enterprises is an important potential source of aggregate productivity improvement and labor m"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.00958",
    "domain": "金融",
    "title": "Quantifying Repair Risk in Crypto Option Surfaces",
    "url": "https://arxiv.org/abs/2611.00958",
    "source": "Tenghan Zhong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T05:00:00+00:00",
    "summary": "arXiv:2611.00958v3 Announce Type: replace Abstract: Option desks adjust crypto option quotes into price surfaces that remain within bid-ask intervals and satisfy standard no-arbitrage restrictions acr"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.09751",
    "domain": "金融",
    "title": "Drift-invariant kernels for discount curve models",
    "url": "https://arxiv.org/abs/2611.09751",
    "source": "Andreas Celary, Zehra Eksi-Altay, Damir Filipovic, Paul Kr\\\"uhner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T05:00:00+00:00",
    "summary": "arXiv:2611.09751v2 Announce Type: replace Abstract: Kernel ridge regression estimates the discount curve as the minimizer of a pricing error plus a penalty given by the norm of a reproducing kernel Hi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2106.00839",
    "domain": "金融",
    "title": "Algorithmic Insurance",
    "url": "https://arxiv.org/abs/2106.00839",
    "source": "Dimitris Bertsimas, Agni Orfanoudaki",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T05:00:00+00:00",
    "summary": "arXiv:2106.00839v4 Announce Type: replace-cross Abstract: When artificial intelligence (AI) systems make errors in high-stakes domains such as medical diagnosis or autonomous driving, a single algorit"
  },
  {
    "id": "rss:https://arxiv.org/abs/2508.05022",
    "domain": "金融",
    "title": "A Multivariate Generalized Cox Model for Dependent and Simultaneous Default Times",
    "url": "https://arxiv.org/abs/2508.05022",
    "source": "Djibril Gueye, Alejandra Quintos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T05:00:00+00:00",
    "summary": "arXiv:2508.05022v2 Announce Type: replace-cross Abstract: We propose a framework for dependent default times where each name defaults when an increasing driver crosses an independent unit exponential "
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
    "points": 4059,
    "published_at": "2026-11-12T13:52:29+00:00",
    "summary": ""
  }
]
```
