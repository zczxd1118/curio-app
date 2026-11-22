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

- 今日日期：`2026-11-22`
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
  "date": "2026-11-22",
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
    "points": 2278223,
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
    "points": 2145353,
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
    "points": 1571683,
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
    "points": 1510786,
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
    "points": 1485139,
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
    "points": 916240,
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
    "points": 907983,
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
    "points": 760812,
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
    "points": 597463,
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
    "points": 486181,
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
    "points": 434476,
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
    "points": 428729,
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
    "points": 365254,
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
    "points": 331554,
    "published_at": "2025-04-15T00:59:13+00:00",
    "summary": "MCP终极指南 - 带你深入掌握MCP（基础篇）\n\n时间轴：\n01:05 MCP简要介绍\n02:47 安装 MCP Host（Cline）\n03:15 配置 Cline 用的 API Key\n06:01 第一个 MCP 问题\n06:31 概念解释：MCP Server 和 Tool\n09:13 配置 MCP Server\n14:19 使用 MCP Server\n15:24 MCP 交互流程详解\n1"
  },
  {
    "id": "bvid:BV1h3W76wEem",
    "domain": "AI",
    "title": "Claude(Code)桌面APP，保姆级全攻略，一期视频精通，顶级Agent软件长什么样？",
    "url": "http://www.bilibili.com/video/av117580048108571",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 330303,
    "published_at": "2026-11-08T09:14:07+00:00",
    "summary": "最近Claude桌面端（Claude Desktop） 有了一大波功能更新。随着一步步的迭代，它已经把 Claude Code 的编程、Claude Design 的设计，以及 Claude Cowork 的办公等核心能力，全部收入了同一个桌面客户端，特别是Claude Code已经从原本黑乎乎的命令行工具，进化成了桌面客户端的完全体形态。再搭配上超强的Opus5.5 模型，已经能称得上是地表顶级"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 303550,
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
    "points": 238755,
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
    "points": 211400,
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
    "points": 187539,
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
    "points": 166586,
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
    "points": 164279,
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
    "points": 162219,
    "published_at": "2025-02-18T13:13:51+00:00",
    "summary": "我试用了几十种AI编程辅助工具，找到了其中三个免费，并且效果最好的方案。 本期视频就来跟大家分享一下。视频中间会穿插很多AI编程工具的使用技巧，还有看待AI编程的一些个人思考。本期视频没有广告都是个人的经验干货，废话不多说我们直接开始。"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 158118,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1VL3F6pE9K",
    "domain": "AI",
    "title": "0基础入门智能体agent测试：AI测试基础+AI智能体(Agent)测试从零入门全攻略，2026最新版！",
    "url": "http://www.bilibili.com/video/av116991151113881",
    "source": "黑马测试",
    "platform": "bilibili",
    "points": 119130,
    "published_at": "2026-07-27T09:19:37+00:00",
    "summary": "还在卷传统软件测试？2026年必学的AI智能体(Agent)测试来了！本期视频专为0基础小白打造，从软件测试基础讲起...若要本视频配套资源笔记可加up主企微（请看置顶留言最后一句话）。"
  },
  {
    "id": "bvid:BV1dpdZYBE9q",
    "domain": "AI",
    "title": "零代码让AI秒接海量MCP工具！最适合小白的MCP集合平台",
    "url": "http://www.bilibili.com/video/av114340703243255",
    "source": "AI研究室-帆哥",
    "platform": "bilibili",
    "points": 103516,
    "published_at": "2025-04-15T11:00:00+00:00",
    "summary": "最近MCP太火了，阿里直接跟进把MCP整合到百炼平台里面了，做了一个MCP的“应用商店”。\n之前不管是在cursor还是Claude上还是需要配置一下MCP服务器，现在在百炼上就可以直接无脑添加MCP工具，非常方便。\n而且因为在平台上一体化，和大模型可以打包配置，让后端的运维部署变得更轻松。\n这个视频教你怎么用阿里云百炼的MCP工具创建一个agent应用。"
  },
  {
    "id": "bvid:BV1NBx46pEL4",
    "domain": "AI",
    "title": "DeepSeek Harness 手机端来了，还能自动操控手机！",
    "url": "http://www.bilibili.com/video/av117540386835759",
    "source": "AI博士嗨嗨",
    "platform": "bilibili",
    "points": 101538,
    "published_at": "2026-11-01T09:07:14+00:00",
    "summary": "在手机上运行 DeepSeek Harness，出门也能连上电脑里的 DSH 接着干活，还能让 AI 自己打开 App、搜索、点按和输入。这期带大家上手社区开源的安卓客户端 DSH Go，从下载安装、本机模型配置，到电脑 Remote 插件安装和手机远程连接，再用美团点螺蛳粉的实际过程，看看它能做哪些步骤、什么时候需要我们接手。最后再聊聊插话、分享回放、桌宠和插件这些日常用得上的功能。"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 94382,
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
    "points": 91688,
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
    "points": 89823,
    "published_at": "2026-10-08T07:22:21+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operit教程：入门安卓最强大ai平台operitAI",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 81198,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV17Lap6VEUr",
    "domain": "AI",
    "title": "【全80集】Vibe Coding 零基础入门到实战教程，由浅入深（全程干货）",
    "url": "http://www.bilibili.com/video/av117353572468721",
    "source": "数据拾光屋",
    "platform": "bilibili",
    "points": 64252,
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
    "points": 50691,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1hMYj6mEVn",
    "domain": "AI",
    "title": "TeleAgent 零基础操作指南来啦！",
    "url": "http://www.bilibili.com/video/av117250728204981",
    "source": "天翼AI",
    "platform": "bilibili",
    "points": 47992,
    "published_at": "2026-09-11T05:27:19+00:00",
    "summary": "TeleAgent星辰超级智能体 零基础操作指南来啦！\n官网下载、注册登录，两步即用。\n不论是桌面整理、C 盘瘦身这种电子家务，还是 PPT撰写、Excel 整理、定时任务这些复杂工作，只需说清需求，就能直接拿结果；\n面试模拟、旅行攻略……更多生活日常，TA都能搞定，安全靠谱。\n技能广场还有办公、生活、娱乐等海量技能按需选择。\nAI搭子就选TA，即刻上手吧！"
  },
  {
    "id": "bvid:BV1uVSUBkEfZ",
    "domain": "AI",
    "title": "Microsoft Copilot完整教程(上) 从入门到Agent 一站式掌握AI办公",
    "url": "http://www.bilibili.com/video/av116351721084069",
    "source": "星小脉",
    "platform": "bilibili",
    "points": 47588,
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
    "points": 43788,
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
    "points": 42165,
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
    "points": 41558,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV1mvyYzeEus",
    "domain": "AI",
    "title": "0基础 5分钟学会DeepSeek Harness新手教程-01｜认识AI Agent，让AI替你干活",
    "url": "http://www.bilibili.com/video/av117654841137017",
    "source": "DurianPaul",
    "platform": "bilibili",
    "points": 37962,
    "published_at": "2026-11-21T14:16:06+00:00",
    "summary": "全系列资料（练习素材、提示词）：\n链接：https://share.weiyun.com/9ydbX2n9  密码：kmtjgc\n\n零基础也能听懂的 AI Agent 入门！这期用大白话和游戏比喻，讲清楚：\n• Agent 和聊天 AI 到底有什么不一样\n• DeepSeek Harness 是什么、能帮你干什么\n• 客户端怎么装、工作区怎么建、模型和推理等级怎么选\n• 插件、Skill、MCP、"
  },
  {
    "id": "bvid:BV1sQaL6vEkb",
    "domain": "AI",
    "title": "小白向，ai入门第一课：agent的部署和使用！",
    "url": "http://www.bilibili.com/video/av117349378166797",
    "source": "沈三殊",
    "platform": "bilibili",
    "points": 34704,
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
    "points": 32548,
    "published_at": "2026-10-27T16:09:19+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29994,
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
    "points": 27110,
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
    "points": 22867,
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
    "points": 19874,
    "published_at": "2026-06-06T11:29:00+00:00",
    "summary": "这一期给大家分享下在codex里面如何配置和使用MCP，和skill一样，MCP也是我们平时用得比较多的，所以建议大家也可以学一下它的基础配置和使用~\n步骤都不难，跟着操作就可以了"
  },
  {
    "id": "bvid:BV18VWb68EDF",
    "domain": "AI",
    "title": "1:1复刻视频？火爆github，这个ai逆向视频的工具太强了！手把手教你使用 rea video",
    "url": "http://www.bilibili.com/video/av117585685319069",
    "source": "IT一哥们",
    "platform": "bilibili",
    "points": 19582,
    "published_at": "2026-11-09T09:10:54+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1xLtS6WEVG",
    "domain": "AI",
    "title": "DeepSeek Harness的MCP应用教程、MCP安装、MCP迁移、MCP删除与卸载",
    "url": "http://www.bilibili.com/video/av117201218635665",
    "source": "eogee",
    "platform": "bilibili",
    "points": 18181,
    "published_at": "2026-09-02T11:33:53+00:00",
    "summary": "MCP 是扩展 Agent 能力的主要方式：接入一个 MCP 服务器，Agent 就能获得一整套现成的外部工具。DeepSeek Harness（命令名 `dsh`，简称 DSH）内置了 MCP 客户端桥插件，配置即可接入社区海量 MCP 服务。本教程以实战为主线，介绍在 dsh 中接入现成 MCP 服务、接入自定义 MCP 服务的完整流程，给出从 Claude Code、Codex 迁移配置的对"
  },
  {
    "id": "bvid:BV1Uwj863EPS",
    "domain": "AI",
    "title": "IDEA中集成claudecode和codex，全程无废话，提升编程效率",
    "url": "http://www.bilibili.com/video/av116788633340919",
    "source": "阿秀_love",
    "platform": "bilibili",
    "points": 15948,
    "published_at": "2026-06-22T01:00:00+00:00",
    "summary": "IDEA中集成claudecode和codex，全程无废话，提升编程效率，先看上一个视频下载安装claudecode和codex，关注后自动获取安装包。"
  },
  {
    "id": "bvid:BV1AFxf6BEpK",
    "domain": "AI",
    "title": "【5分钟搞定】Claude账号注册登录保姆级教程！没有邮箱、注册不了、要手机号验证、弹KYC认证？这一条全讲清",
    "url": "http://www.bilibili.com/video/av117561526059085",
    "source": "团子讲Ai",
    "platform": "bilibili",
    "points": 15843,
    "published_at": "2026-11-05T02:47:11+00:00",
    "summary": "本视频由 Claude Code 剪辑创作完成。不懂网络配置可以看我主页置顶视频\n最近很多人卡在 Claude 注册第一步，我用微软邮箱亲手从头注册了两个号，每一步和会卡住的地方都录了下来：\n1. 用微软邮箱注册 Claude：不用手机，只要一个辅助邮箱验证；QQ、163 邮箱别拿去注册。\n2. 手机号验证跳不过：要能收短信的美国号码，虚拟号不收，一个号码只能验证一次。\n3. 弹 KYC 身份认证"
  },
  {
    "id": "bvid:BV1yyQEBdEkm",
    "domain": "AI",
    "title": "【2026B站最全】Claude Code+软件测试实操教程!看完我直接删了收藏夹所有测试教程,从账号注册到Plan驱动测试项目,小白3天上手！",
    "url": "http://www.bilibili.com/video/av116408092525631",
    "source": "软件测试大神",
    "platform": "bilibili",
    "points": 15660,
    "published_at": "2026-04-15T09:55:02+00:00",
    "summary": "配套资料👉：https://b23.tv/qvhxmaQ\n包括:AI测试网站，几十个AI场景测试完整流程，skil文档，测试八股文，项目源码，测试用例模板，工具安装包，学习计划表，学习路线，100g测试新人资料包等等，资料百分百免费，放心领取~"
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
    "points": 1116,
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
    "id": "hn:50581438",
    "domain": "AI 算力 / 半导体",
    "title": "US SEC's Nvidia probe is examining potential accounting issues – sources",
    "url": "https://www.marketscreener.com/news/us-sec-s-nvidia-probe-is-examining-potential-accounting-issues-sources-say-ce785ed3dd8ff627",
    "source": "ftchd",
    "platform": "hackernews",
    "points": 303,
    "published_at": "2026-11-20T20:22:41+00:00",
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
    "points": 290,
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
    "id": "hn:50497155",
    "domain": "AI 算力 / 半导体",
    "title": "Serving GLM-5.3 at 607.8 tok/s across two Nvidia DGX stations with vLLM",
    "url": "https://developer.nvidia.com/blog/when-one-gpu-isnt-enough-serving-glm-5-3-across-two-nvidia-dgx-stations-with-vllm/",
    "source": "wondersky",
    "platform": "hackernews",
    "points": 150,
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
    "id": "rss:https://www.tomshardware.com/pc-components/nas/ditch-cloud-subscriptions-with-a-usd132-discount-on-a-4-bay-ugreen-dxp4800-gt-nas-enclosure-in-amazon-black-friday-deal-offers-dual-10gbe-ports-and-supports-up-to-144tb-of-storage",
    "domain": "AI 算力 / 半导体",
    "title": "Ditch cloud subscriptions with a $132 discount on a 4-Bay UGreen DXP4800 GT NAS enclosure in Amazon Black Friday deal — offers dual 10GbE ports and supports up to 144TB of storage",
    "url": "https://www.tomshardware.com/pc-components/nas/ditch-cloud-subscriptions-with-a-usd132-discount-on-a-4-bay-ugreen-dxp4800-gt-nas-enclosure-in-amazon-black-friday-deal-offers-dual-10gbe-ports-and-supports-up-to-144tb-of-storage",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T09:45:44+00:00",
    "summary": "For those looking to ditch cloud storage this Black Friday, UGreen's DXP4800 GT 4-bay NAS enclosure has gone on sale with a lovely 20% discount at Amazon, marking the second time it's returned to its "
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/msis-magnificent-32-inch-4k-qd-oled-gaming-monitor-tumbles-to-just-usd569-save-usd130-at-b-and-h-photo-with-this-black-friday-mag-321up-deal-the-perfect-gaming-upgrade-for-your-pc",
    "domain": "AI 算力 / 半导体",
    "title": "MSI's magnificent 32-inch 4K QD-OLED gaming monitor tumbles to just $569 — save $130 at B&H Photo with this Black Friday MAG 321UP deal, the perfect gaming upgrade for your PC",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/msis-magnificent-32-inch-4k-qd-oled-gaming-monitor-tumbles-to-just-usd569-save-usd130-at-b-and-h-photo-with-this-black-friday-mag-321up-deal-the-perfect-gaming-upgrade-for-your-pc",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T09:14:51+00:00",
    "summary": "Save $130 on this gorgeous 32-inch QD-OLED gaming monitor from MSI and experience crisp visuals in 4K."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/oled-gaming-laptop-with-rtx-5060-and-intel-core-ultra-7-cpu-price-crashes-by-usd650-in-black-friday-offer-lenovo-legion-5i-laptop-drops-to-usd1-349-with-free-games-at-b-and-h",
    "domain": "AI 算力 / 半导体",
    "title": "OLED gaming laptop with RTX 5060 and Intel Core Ultra 7 CPU price crashes by $650 in Black Friday offer — Lenovo Legion 5i laptop drops to $1,349 with free games at B&H",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/oled-gaming-laptop-with-rtx-5060-and-intel-core-ultra-7-cpu-price-crashes-by-usd650-in-black-friday-offer-lenovo-legion-5i-laptop-drops-to-usd1-349-with-free-games-at-b-and-h",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T09:05:40+00:00",
    "summary": "Getting a gaming laptop this holiday season doesn't have to mean spending thousands of dollars, as this modestly priced Lenovo Legion 5i OLED gaming laptop has dropped to just $1,349 at B&amp;H."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/alienware-aurora-pc-with-rtx-5070-32gb-of-ram-drops-to-usd1-899-in-amazon-black-friday-offer-core-ultra-7-equipped-pc-is-one-of-the-best-value-prebuilt-deals-weve-seen-so-far",
    "domain": "AI 算力 / 半导体",
    "title": "Alienware Aurora PC with RTX 5070, 32GB of RAM drops to $1,899 in Amazon Black Friday offer — Core Ultra 7 equipped PC is one of the best value prebuilt deals we’ve seen so far",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/alienware-aurora-pc-with-rtx-5070-32gb-of-ram-drops-to-usd1-899-in-amazon-black-friday-offer-core-ultra-7-equipped-pc-is-one-of-the-best-value-prebuilt-deals-weve-seen-so-far",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T08:08:15+00:00",
    "summary": "Pick up a gaming PC bargain this Black Friday with this RTX 5070-powered Alienware Aurora rig, which also comes with 32GB of DDR5 memory for only $1.899."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/act-fast-to-score-intels-core-i7-14700k-for-its-lowest-price-ever-at-usd249-99-raptor-lake-refresh-cpu-is-a-bargain-that-supports-ddr5-and-ddr4-motherboards",
    "domain": "AI 算力 / 半导体",
    "title": "Act fast to score Intel's Core i7-14700K for its lowest price ever at $249.99",
    "url": "https://www.tomshardware.com/pc-components/cpus/act-fast-to-score-intels-core-i7-14700k-for-its-lowest-price-ever-at-usd249-99-raptor-lake-refresh-cpu-is-a-bargain-that-supports-ddr5-and-ddr4-motherboards",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-21T20:00:22+00:00",
    "summary": "After months of inconsistent pricing, Intel's Core i7-14700K is down to its lowest price ever at $249.99, with support for LGA 1700 motherboards that come with either DDR4 or DDR5 memory support."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/pc-cases/save-usd78-on-corsairs-triple-chamber-air-5400-rs-r-midtower-pc-case-at-new-all-time-low-price-chassis-includes-three-pre-installed-rs-r-argb-fans-and-back-connector-motherboard-support",
    "domain": "AI 算力 / 半导体",
    "title": "Save $78 on Corsair's triple-chamber AIR 5400 RS-R midtower PC case at new all-time low price",
    "url": "https://www.tomshardware.com/pc-components/pc-cases/save-usd78-on-corsairs-triple-chamber-air-5400-rs-r-midtower-pc-case-at-new-all-time-low-price-chassis-includes-three-pre-installed-rs-r-argb-fans-and-back-connector-motherboard-support",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-21T18:49:39+00:00",
    "summary": "Corsair's triple-chamber AIR 5400 RS-R is down to its lowest price ever in a run-up Black Friday sale, saving you nearly $80 off list price."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-chairs/best-gaming-chair-deals-secretlab-razer-and-more",
    "domain": "AI 算力 / 半导体",
    "title": "Best Black Friday gaming chair deals 2026",
    "url": "https://www.tomshardware.com/peripherals/gaming-chairs/best-gaming-chair-deals-secretlab-razer-and-more",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-21T16:38:40+00:00",
    "summary": "The best Black Friday deals on gaming chairs for every budget, style, and comfort level. Upgrade your gaming chair with something high-quality."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/trump-wants-to-ban-us-companies-from-building-overseas-data-centers-as-bans-slow-development-also-considers-putting-a-tremendous-tax-in-lieu-of-prohibition",
    "domain": "AI 算力 / 半导体",
    "title": "Trump wants to ban US companies from building overseas data centers as bans slow development",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/trump-wants-to-ban-us-companies-from-building-overseas-data-centers-as-bans-slow-development-also-considers-putting-a-tremendous-tax-in-lieu-of-prohibition",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-21T16:29:39+00:00",
    "summary": "The president wants U.S. data center companies to stay within U.S. borders or pay a hefty fee if they want to build in foreign countries."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/supercomputers/this-week-on-toms-hardware-premium-21-november-2026-amd-nvidia-and-more-show-off-the-future-of-high-performance-computing-at-sc26",
    "domain": "AI 算力 / 半导体",
    "title": "This week on Tom's Hardware Premium: 21 November 2026",
    "url": "https://www.tomshardware.com/tech-industry/supercomputers/this-week-on-toms-hardware-premium-21-november-2026-amd-nvidia-and-more-show-off-the-future-of-high-performance-computing-at-sc26",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-21T16:00:00+00:00",
    "summary": "We go through an exhaustive list of everything we covered at SC26, which includes brand-new devices and developments from AMD, Nvidia, Intel and many more."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/air-cooling/laptop-cooled-by-bounce-house-blower-gets-35-degree-drop-in-temperatures-modder-compares-laptop-cooler-with-increasingly-powerful-fan-setups",
    "domain": "AI 算力 / 半导体",
    "title": "Modder cools gaming laptop with a bounce house blower for a 35-degree drop",
    "url": "https://www.tomshardware.com/pc-components/air-cooling/laptop-cooled-by-bounce-house-blower-gets-35-degree-drop-in-temperatures-modder-compares-laptop-cooler-with-increasingly-powerful-fan-setups",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-21T15:31:48+00:00",
    "summary": "A PC cooling enthusiast attached a bounce house blower to the bottom of his laptop, bringing temperatures below 50 degrees Celsius."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/rapidus-reportedly-struggles-to-produce-working-sram-on-its-2nm-node-putting-2027-mass-production-at-risk-company-faces-significant-challenges-using-euv-to-develop-gaa-transistors",
    "domain": "AI 算力 / 半导体",
    "title": "Rapidus reportedly struggles to produce working SRAM on its 2nm node, putting 2027 mass production at risk",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/rapidus-reportedly-struggles-to-produce-working-sram-on-its-2nm-node-putting-2027-mass-production-at-risk-company-faces-significant-challenges-using-euv-to-develop-gaa-transistors",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-21T15:30:00+00:00",
    "summary": "Japan's semiconductor startup has demonstrated functioning GAA transistors, but integrating them into working memory cells appears to be a considerably greater challenge."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/35-year-old-snes-runs-chatgpt-accelerated-with-a-super-fx-2-chip-21-mhz-of-risc-muscle-speeds-2-2m-parameter-chatbot-replies",
    "domain": "AI 算力 / 半导体",
    "title": "35-year-old SNES runs ChatGPT, accelerated with a Super FX 2 chip — 21 MHz of RISC muscle speeds 2.2M parameter chatbot replies",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/35-year-old-snes-runs-chatgpt-accelerated-with-a-super-fx-2-chip-21-mhz-of-risc-muscle-speeds-2-2m-parameter-chatbot-replies",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-21T15:02:17+00:00",
    "summary": "Nintendo’s classic SNES console now has its own ChatGPT client, and it's accelerated by the Super FX 2 chip."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/gigabyte-mo27q2a-27-inch-qhd-280-hz-qd-oled-gaming-monitor-review",
    "domain": "AI 算力 / 半导体",
    "title": "Gigabyte MO27Q2A 27-inch QHD 280 Hz QD-OLED gaming monitor review: Another price buster from Gigabyte",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/gigabyte-mo27q2a-27-inch-qhd-280-hz-qd-oled-gaming-monitor-review",
    "source": "Christian Eberle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-21T14:30:00+00:00",
    "summary": "Gigabyte brings excellent value while delivering premium performance and build quality with its MO27Q2A. This QD-OLED panel sports QHD resolution, 280 Hz, Adaptive-Sync, DisplayHDR 400, and wide-gamut"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/knoxvilles-police-department-will-send-semi-autonomous-drones-on-911-calls-eyes-in-the-sky-to-aid-situational-awareness-for-officers",
    "domain": "AI 算力 / 半导体",
    "title": "New semi-autonomous 911 drones will reach nearly all of Knoxville in 90 seconds or less",
    "url": "https://www.tomshardware.com/tech-industry/drones/knoxvilles-police-department-will-send-semi-autonomous-drones-on-911-calls-eyes-in-the-sky-to-aid-situational-awareness-for-officers",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-21T14:00:00+00:00",
    "summary": "The Knoxville Police Department has launched its Drone as First Responder program, with drones being dispatched to the scene following a 911 call to increase real-time situational awareness."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/defense-firms-emp-dragon-weapon-fries-51-jam-proof-drones-simultaneously-high-power-electromagnetic-system-relies-on-120-year-old-vacuum-tube-tech-to-defeat-fiber-optic-uavs",
    "domain": "AI 算力 / 半导体",
    "title": "Defense firm’s EMP ‘Dragon’ weapon fries 51 jam-proof drones simultaneously",
    "url": "https://www.tomshardware.com/tech-industry/drones/defense-firms-emp-dragon-weapon-fries-51-jam-proof-drones-simultaneously-high-power-electromagnetic-system-relies-on-120-year-old-vacuum-tube-tech-to-defeat-fiber-optic-uavs",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-21T13:54:41+00:00",
    "summary": "Aselsan developed the Ejderha, which translates to 'Dragon' in English, as a defensive weapon designed to combat drone swarms."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/msi-crosshair-a16-hx-rtx-5070-ryzen-9-equipped-gaming-laptop-gets-usd400-discount-at-amazon-system-comes-with-a-free-game-in-early-black-friday-offer",
    "domain": "AI 算力 / 半导体",
    "title": "MSI Crosshair A16 HX RTX 5070, Ryzen 9-equipped gaming laptop gets $400 discount at Amazon",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/msi-crosshair-a16-hx-rtx-5070-ryzen-9-equipped-gaming-laptop-gets-usd400-discount-at-amazon-system-comes-with-a-free-game-in-early-black-friday-offer",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-21T13:09:06+00:00",
    "summary": "Save over $400 on this AMD Ryzen 9-equipped gaming laptop from MSI as a part of their early Black Friday deals, which also comes with a free copy of Onimusha: The Way of the Sword."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/homelabbers-second-gen-optane-build-runs-2-8-trillion-parameter-kimi-k3-at-3-11-tokens-per-second-after-adding-two-rtx-3090s-moving-nearly-half-the-model-into-a-ram-drive-boosted-performance-by-41-percent",
    "domain": "AI 算力 / 半导体",
    "title": "Homelabber’s second-gen Optane build uses two RTX 3090s to run 2.8-trillion-parameter Kimi AI model at 3.11 tokens per second",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/homelabbers-second-gen-optane-build-runs-2-8-trillion-parameter-kimi-k3-at-3-11-tokens-per-second-after-adding-two-rtx-3090s-moving-nearly-half-the-model-into-a-ram-drive-boosted-performance-by-41-percent",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-21T12:00:00+00:00",
    "summary": "A Reddit homelabber’s Optane PMem 200 server now runs Moonshot AI’s Kimi K3 at 3.11 tokens/s with two RTX 3090s and a RAM drive."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/external-hdds/get-38-percent-off-this-20tb-wd-elements-external-hdd-in-amazon-black-friday-offer-pay-just-2-75-cents-per-gb-as-drive-drops-to-usd549",
    "domain": "AI 算力 / 半导体",
    "title": "Get 38% off this 20TB WD Elements external HDD in Amazon Black Friday offer — pay just 2.75 cents per GB as drive drops to $549",
    "url": "https://www.tomshardware.com/pc-components/external-hdds/get-38-percent-off-this-20tb-wd-elements-external-hdd-in-amazon-black-friday-offer-pay-just-2-75-cents-per-gb-as-drive-drops-to-usd549",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-21T11:41:10+00:00",
    "summary": "Pay just 2.75 cents per gigabyte with this 20TB external HDD offer, as the WD Elements set has dropped to just $549.99 in this Black Friday deal."
  },
  {
    "id": "rss:https://www.tomshardware.com/gift-guides-seasonal-sales/netgear-black-friday-deals-save-you-up-to-33-percent-on-full-home-wifi-coverage-upgrade-your-gaming-router-mesh-wifi-setup-or-wireless-extenders",
    "domain": "AI 算力 / 半导体",
    "title": "Netgear Black Friday deals save you up to 33% on full home WiFi coverage — upgrade your gaming router, mesh WiFi setup, or wireless extenders",
    "url": "https://www.tomshardware.com/gift-guides-seasonal-sales/netgear-black-friday-deals-save-you-up-to-33-percent-on-full-home-wifi-coverage-upgrade-your-gaming-router-mesh-wifi-setup-or-wireless-extenders",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-21T11:33:43+00:00",
    "summary": "We've rounded up some of the best deals on Netgear network solutions for your home, from complete mesh networks to gaming routers and WiFi extenders."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/one-gigabyte-of-wikipedia-losslessly-compressed-to-105-39mb-with-self-learning-ai-transformer-model-tufazip-needs-two-nvidia-b200-gpus-and-about-a-week-to-compress-or-decompress",
    "domain": "AI 算力 / 半导体",
    "title": "One gigabyte of Wikipedia losslessly compressed to 105.39MB with self-learning AI transformer model",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/one-gigabyte-of-wikipedia-losslessly-compressed-to-105-39mb-with-self-learning-ai-transformer-model-tufazip-needs-two-nvidia-b200-gpus-and-about-a-week-to-compress-or-decompress",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-21T11:30:00+00:00",
    "summary": "Tufa Labs’ tufazip compresses 1GB of Wikipedia to 105.39MB with a 163M-parameter Transformer as its only predictor, on two Nvidia B200s."
  },
  {
    "id": "rss:https://www.tomshardware.com/maker-stem/hardware-hacker-builds-open-source-portable-3-5-inch-floppy-wi-fi-nas-reads-and-shares-old-school-floppies-wirelessly-or-through-direct-connection",
    "domain": "AI 算力 / 半导体",
    "title": "Hardware hacker builds open-source portable 3.5-inch floppy Wi-Fi NAS",
    "url": "https://www.tomshardware.com/maker-stem/hardware-hacker-builds-open-source-portable-3-5-inch-floppy-wi-fi-nas-reads-and-shares-old-school-floppies-wirelessly-or-through-direct-connection",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-21T11:00:00+00:00",
    "summary": "Techie designs a portable Wi-Fi NAS to read and transfer digital camera floppy disks — device does double duty for easy floppy archival"
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
    "id": "hn:50552424",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Neon",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/",
    "source": "yigitdemirag",
    "platform": "hackernews",
    "points": 1059,
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
    "points": 576,
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
    "points": 375,
    "published_at": "2026-11-19T23:35:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:50577901",
    "domain": "大厂 AI 动态",
    "title": "Google workers tell their employer not to punish schools that don't want AI",
    "url": "https://www.motherjones.com/politics/2026/11/google-alphabet-union-school-ai-protest-gemini-workers-petition/",
    "source": "cdrnsf",
    "platform": "hackernews",
    "points": 282,
    "published_at": "2026-11-20T16:59:27+00:00",
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
    "points": 293,
    "published_at": "2026-11-18T18:49:51+00:00",
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
    "id": "hn:50541790",
    "domain": "大厂 AI 动态",
    "title": "Why is Gemini 4 Carbon taking so long?",
    "url": "https://kernel.dev/blog/why-is-gemini-4-carbon-taking-so-long/",
    "source": "deenadz",
    "platform": "hackernews",
    "points": 286,
    "published_at": "2026-11-18T04:14:04+00:00",
    "summary": ""
  },
  {
    "id": "hn:50554374",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Neon looks like an Opus 5.5 competitor",
    "url": "https://micjm.com/blog/gemini-4-neon-looks-like-a-top-model/",
    "source": "seizethecheese",
    "platform": "hackernews",
    "points": 256,
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
    "points": 174,
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
    "points": 124,
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
    "points": 46,
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
    "id": "rss:https://www.theverge.com/tech/1039564/amazon-nyc-council-packages-shipping-label",
    "domain": "大厂 AI 动态",
    "title": "Amazon is complaining about NYC Council on shipping labels, too",
    "url": "https://www.theverge.com/tech/1039564/amazon-nyc-council-packages-shipping-label",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-21T21:59:31+00:00",
    "summary": "Amazon is leaving no venue unexplored in its fight against the New York City Council and the Delivery Protection Act. The company is now putting labels on shipments claiming that the Council could add"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1039554/un-regulations-killer-robots",
    "domain": "大厂 AI 动态",
    "title": "The UN fails to agree on rules regulating ‘killer robots’",
    "url": "https://www.theverge.com/tech/1039554/un-regulations-killer-robots",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-21T20:03:37+00:00",
    "summary": "One of the items on the agenda for UN diplomats meeting in Geneva this week was working towards rules regarding the use of autonomous weapons, or so-called \"killer robots.\" Eventually, representatives"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1039543/fbi-usda-hacked",
    "domain": "大厂 AI 动态",
    "title": "The FBI and USDA were reportedly hacked",
    "url": "https://www.theverge.com/tech/1039543/fbi-usda-hacked",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-21T17:42:27+00:00",
    "summary": "Friday, it was reported that both the US Department of Agriculture (USDA) and the FBI were hacked. In reporting on the FBI hack, CNN noted that this is the second such attack on the agency in the last"
  },
  {
    "id": "rss:https://www.theverge.com/report/1038463/john-roberts-linda-belcher-bobs-burgers-interview",
    "domain": "大厂 AI 动态",
    "title": "John Roberts, the voice of Linda Belcher, is just happy to finish a thing",
    "url": "https://www.theverge.com/report/1038463/john-roberts-linda-belcher-bobs-burgers-interview",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-21T16:00:00+00:00",
    "summary": "You probably know John Roberts best as the voice of Linda Belcher on Bob's Burgers. The show just wrapped up its 16th season and shows no signs of slowing down anytime soon. The show remains a reliabl"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1038762/amazon-alexa-photo-frame-black-friday-2026-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Amazon’s first digital photo frame is up to 50 percent off for Black Friday",
    "url": "https://www.theverge.com/gadgets/1038762/amazon-alexa-photo-frame-black-friday-2026-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-21T16:00:00+00:00",
    "summary": "Amazon only announced its first digital photo frame less than a month ago, but it&#8217;s already getting a sizable discount for Black Friday. You can currently grab the Alexa Photo Frame at Amazon an"
  },
  {
    "id": "rss:https://www.theverge.com/podcast/1038701/anthropic-ipo-ai-safety-openai-nvidia-structure",
    "domain": "大厂 AI 动态",
    "title": "Can Anthropic afford to put safety first?",
    "url": "https://www.theverge.com/podcast/1038701/anthropic-ipo-ai-safety-openai-nvidia-structure",
    "source": "Nilay Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-21T15:00:00+00:00",
    "summary": "Today, I’m talking with Hayden Field, The Verge’s senior AI reporter, about the Anthropic IPO for the third and final episode in our series about AI in real life. The AI lab behind Claude went public "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1039160/anker-soundcore-liberty-5-pro-black-friday-2026-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Our go-to earbuds for taking calls have fallen to their lowest price to date",
    "url": "https://www.theverge.com/gadgets/1039160/anker-soundcore-liberty-5-pro-black-friday-2026-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-21T14:55:28+00:00",
    "summary": "If you’re looking for a new pair of earbuds, the Soundcore Liberty 5 Pro are on sale for $129.99 at Amazon, Best Buy, and Walmart right now. That’s the lowest price we’ve seen for Anker’s excellent wi"
  },
  {
    "id": "rss:https://www.theverge.com/games/1038099/chess-classic-games-expansion-ai",
    "domain": "大厂 AI 动态",
    "title": "Chess.com’s next move is a new hub for classic games, from mahjong to sudoku",
    "url": "https://www.theverge.com/games/1038099/chess-classic-games-expansion-ai",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-21T14:00:00+00:00",
    "summary": "Chess.com is ready to go a lot bigger than chess. After launching Gambit, a gambling-free poker site, earlier this year, the company is now adding 10 more games: backgammon, checkers, go, hearts, mahj"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1038562/xiaomi-18-pro-max-review",
    "domain": "大厂 AI 动态",
    "title": "The Xiaomi 18 Pro proves two screens aren’t better than one",
    "url": "https://www.theverge.com/tech/1038562/xiaomi-18-pro-max-review",
    "source": "Dominic Preston",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-21T13:00:00+00:00",
    "summary": "Xiaomi introduced a second screen to its flagship phones with last year's 17 Pros, but didn't release them outside China. That means the new 18 Pro and Pro Max are the first chance I've had to find ou"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1039433/gta-vi-alfred-6-clockwisetv-installer",
    "domain": "大厂 AI 动态",
    "title": "The game of the year is finally here",
    "url": "https://www.theverge.com/tech/1039433/gta-vi-alfred-6-clockwisetv-installer",
    "source": "David Pierce",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-21T13:00:00+00:00",
    "summary": "Hi, friends! Welcome to Installer No. 153, your guide to the best and Verge-iest stuff in the world. (If you're new here, welcome, thank you for tearing yourself away from GTA to be here, and also you"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/21/signal-restricts-mobile-screenshots-as-it-confronts-existential-threat-of-ai-surveillance/",
    "domain": "大厂 AI 动态",
    "title": "Signal restricts mobile screenshots as it confronts ‘existential threat’ of AI surveillance",
    "url": "https://techcrunch.com/2026/11/21/signal-restricts-mobile-screenshots-as-it-confronts-existential-threat-of-ai-surveillance/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-21T21:37:10+00:00",
    "summary": "Signal is limiting users' ability to take screenshots in both its Android and iOS apps."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/21/a-tale-of-two-nvidias/",
    "domain": "大厂 AI 动态",
    "title": "A tale of two Nvidias",
    "url": "https://techcrunch.com/2026/11/21/a-tale-of-two-nvidias/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-21T21:07:42+00:00",
    "summary": "We got two very different pictures of Nvidia — the company’s latest earnings report vs. the tech executives loudly calling for Jensen Huang’s return."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/21/trump-says-reported-fbi-database-hack-is-not-good/",
    "domain": "大厂 AI 动态",
    "title": "Trump says reported FBI database hack is ‘not good’",
    "url": "https://techcrunch.com/2026/11/21/trump-says-reported-fbi-database-hack-is-not-good/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-21T18:44:53+00:00",
    "summary": "The FBI is reportedly investigating a hack of the National Crime Information Center."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/21/all-the-ai-agents-that-can-live-in-your-text-messages/",
    "domain": "大厂 AI 动态",
    "title": "Here are the top AI agents that can live in your text messages",
    "url": "https://techcrunch.com/2026/11/21/all-the-ai-agents-that-can-live-in-your-text-messages/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-21T17:00:00+00:00",
    "summary": "We created a list of the most notable AI agents that can live in your text messages, from general assistants to agents designed for families, travel, and work."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/21/is-selling-an-ai-version-of-your-face-to-this-microdrama-startup-the-future-of-hollywood/",
    "domain": "大厂 AI 动态",
    "title": "Is selling an AI version of your face to this microdrama startup the future of Hollywood?",
    "url": "https://techcrunch.com/2026/11/21/is-selling-an-ai-version-of-your-face-to-this-microdrama-startup-the-future-of-hollywood/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-21T16:00:00+00:00",
    "summary": "An actor has licensed his face to a microdrama startup — in a trend that's already popular in China. Experts question the long-term consequences if this becomes a trend in Hollywood, too."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/21/alaska-your-next-governor-is-a-wikipedia-nerd/",
    "domain": "大厂 AI 动态",
    "title": "Alaska, your next governor is a Wikipedia nerd",
    "url": "https://techcrunch.com/2026/11/21/alaska-your-next-governor-is-a-wikipedia-nerd/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-21T15:18:29+00:00",
    "summary": "Jonathan Kreiss-Tomkins, Alaska's governor-elect, has made more than 13,000 WIkipedia edits."
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
    "id": "hn:50556287",
    "domain": "股票",
    "title": "Ruby2ßhell: Pre-authentication RCE on stock Rails",
    "url": "https://verialabs.com/ruby2shell/",
    "source": "jdns",
    "platform": "hackernews",
    "points": 405,
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
    "id": "hn:50588647",
    "domain": "股票",
    "title": "Anthropic's IPO bank closed position meant to stabilize stock",
    "url": "https://www.reuters.com/markets/us/anthropics-ipo-bank-closed-position-meant-stabilize-stock-removing-source-2026-11-20",
    "source": "anon373839",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-11-21T12:43:24+00:00",
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
    "id": "hn:50532613",
    "domain": "金融",
    "title": "Brazil's tax authority open-sources its tax calculator on GitHub under MIT",
    "url": "https://www.gov.br/receitafederal/pt-br/assuntos/noticias/2026/novembro/receita-federal-publica-primeiro-codigo-fonte-aberto-no-github-e-amplia-transparencia-da-reforma-tributaria",
    "source": "dvaplima",
    "platform": "hackernews",
    "points": 776,
    "published_at": "2026-11-17T15:22:57+00:00",
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
    "points": 196,
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
    "id": "hn:50594937",
    "domain": "金融",
    "title": "Tesla launches FSD v15, targets its biggest weaknesses, from signs to potholes",
    "url": "https://electrek.co/2026/11/21/tesla-fsd-v15-rollout-25x-safety-reality-view/",
    "source": "m348e912",
    "platform": "hackernews",
    "points": 26,
    "published_at": "2026-11-22T00:14:05+00:00",
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
    "id": "hn:50528073",
    "domain": "金融",
    "title": "Elderly people are buying Teslas for the 'full self-driving.' This is a problem",
    "url": "https://www.fastcompany.com/91641371/elderly-people-are-buying-tesla-for-full-self-driving-this-is-a-problem",
    "source": "watermelon0",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-11-17T06:20:11+00:00",
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
