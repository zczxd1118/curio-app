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

- 今日日期：`2026-11-24`
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
  "date": "2026-11-24",
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
    "points": 2155454,
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
    "points": 1589976,
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
    "points": 1515586,
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
    "points": 1492464,
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
    "points": 917012,
    "published_at": "2025-05-01T09:00:00+00:00",
    "summary": "up的科学星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 763010,
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
    "points": 597670,
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
    "points": 489164,
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
    "points": 438121,
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
    "points": 435246,
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
    "points": 428935,
    "published_at": "2025-03-13T13:18:09+00:00",
    "summary": "MCP是近期的AI领域的热点，特别是在海外社区获得热烈讨论，每天都有大量MCP工具诞生。本期视频我们从MCP的概念，技术原理，到多场景实战，一个视频看懂MCP的全部内容。\n\n\nMCP官方开源仓库：https://github.com/modelcontextprotocol/servers\nMCP合集网站：  https://smithery.ai/\nVscode下载：https://code.v"
  },
  {
    "id": "bvid:BV1h3W76wEem",
    "domain": "AI",
    "title": "Claude(Code)桌面APP，保姆级全攻略，一期视频精通，顶级Agent软件长什么样？",
    "url": "http://www.bilibili.com/video/av117580048108571",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 421487,
    "published_at": "2026-11-08T09:14:07+00:00",
    "summary": "最近Claude桌面端（Claude Desktop） 有了一大波功能更新。随着一步步的迭代，它已经把 Claude Code 的编程、Claude Design 的设计，以及 Claude Cowork 的办公等核心能力，全部收入了同一个桌面客户端，特别是Claude Code已经从原本黑乎乎的命令行工具，进化成了桌面客户端的完全体形态。再搭配上超强的Opus5.5 模型，已经能称得上是地表顶级"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 368272,
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
    "points": 333057,
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
    "points": 305131,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1RdLm6PEFF",
    "domain": "AI",
    "title": "ClaudeCode桌面版 = 中文汉化 + 免登录 + 接入DeekSeek + 安装自己的Skill",
    "url": "http://www.bilibili.com/video/av116606717919919",
    "source": "iwenwiki",
    "platform": "bilibili",
    "points": 292656,
    "published_at": "2026-05-20T11:45:46+00:00",
    "summary": "全B站最详细的 ClaudeCode 桌面版教程，从安装到免登录，中文汉化，接入DeepSeek，安装使用自己的Skill，ClaudeCode真正的AI编程工具，恐怖如斯！\nAgent Skills课程在这里：https://www.bilibili.com/video/BV1ugdgBQED4/?spm_id_from=333.1387.homepage.video_card.click&am"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 240432,
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
    "points": 187715,
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
    "points": 166720,
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
    "points": 164570,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1eYPpeWEnT",
    "domain": "AI",
    "title": "Cursor + MCP = 王炸！彻底颠覆我的Cursor工作流，效率直接起飞",
    "url": "http://www.bilibili.com/video/av114073660301264",
    "source": "御风大世界",
    "platform": "bilibili",
    "points": 151936,
    "published_at": "2025-02-27T03:19:03+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1Am9kBfEMN",
    "domain": "AI",
    "title": "AI智能体赋能课堂教学——技术很简单，难的是想法",
    "url": "http://www.bilibili.com/video/av116482180647922",
    "source": "爱可可-爱生活",
    "platform": "bilibili",
    "points": 120147,
    "published_at": "2026-04-28T11:55:25+00:00",
    "summary": "在AI迅猛发展的今天，课堂正在悄然发生变化。\n但真正的挑战，从来不是“会不会用工具”，而是——我们究竟希望学生学会什么？\n\n本讲座不教软件操作，不演示平台使用，\n而是聚焦一个更关键的问题：\n如何借助AI，让那些我们一直想实现却做不到的教学理想成为现实。\n\n通过真实课堂案例与可落地的方法模型，讲座将带领教师完成一次思维升级：\n从“让AI替你干活”，转向“用AI创造更好的学习体验”\n从“提高效率”，走"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 94392,
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
    "points": 92303,
    "published_at": "2026-07-26T01:30:00+00:00",
    "summary": "模组：Numen\n项目地址：https://github.com/Dwinovo/minecraft-numen"
  },
  {
    "id": "bvid:BV1ExyuzpEL9",
    "domain": "AI",
    "title": "时代眼泪！Cursor名字或将写进历史，招牌谢幕图标独活，Grok Build 成功寄生！",
    "url": "http://www.bilibili.com/video/av117657357584985",
    "source": "黑鸦Heya",
    "platform": "bilibili",
    "points": 78635,
    "published_at": "2026-11-22T00:56:08+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV143wwz6E8F",
    "domain": "AI",
    "title": "Claude code科研使用展示与思路分享（提速就靠Ai）",
    "url": "http://www.bilibili.com/video/av116211882920985",
    "source": "科研推土机",
    "platform": "bilibili",
    "points": 77165,
    "published_at": "2026-03-11T18:12:00+00:00",
    "summary": "本期给大家带来的是Claude在Vscode的科研应用演示与我最近的一些心得使用心得，科研速度嘎嘎提升。论文复现画图、数据分析就靠Claude code。这个课程也是科研推土机「系统管理文献课程2.0」学员催我更新的内容，希望能帮助到大家～，这个视频重点讲两个事情：\n1️⃣ 资料获取，free不用怀疑，我是良心可言博主，，关注我(GZTSHNR)～\n2️⃣ 展示如何在VS code实操应用clau"
  },
  {
    "id": "bvid:BV1U8d8BzEUK",
    "domain": "AI",
    "title": "建议收藏 | 51万行源码真相，ClaudeCode架构深度解读，深度复盘四大约束架构与8大设计模式，揭秘工业级Agent如何解决上下文爆炸与成本失控",
    "url": "http://www.bilibili.com/video/av116413847044339",
    "source": "赋范课堂",
    "platform": "bilibili",
    "points": 76585,
    "published_at": "2026-04-16T10:20:18+00:00",
    "summary": "ClaudeCode源码深度解读，揭秘Agent真正的秘密武器：拆解51万行工程源码，解析四大约束架构与8种设计模式，掌握工业级Agent从Demo到可靠产品的核心演进路径，助你重塑AI开发底层思维。"
  },
  {
    "id": "bvid:BV1xBrDB9E42",
    "domain": "AI",
    "title": "独立开发太累？Godot + Claude Code 搭建 AI 辅助工作流，效率直接起飞！ | 地块召唤师开发实战 #01",
    "url": "http://www.bilibili.com/video/av115911319100158",
    "source": "像素夹心饼干",
    "platform": "bilibili",
    "points": 70577,
    "published_at": "2026-01-18T03:25:00+00:00",
    "summary": "大家好，这里是饼干！🍪\n这是我的新坑——**《地块召唤师》**开发实战分享的第一期。\n很多朋友问独立开发如何提升效率？这期视频我不聊虚的，直接公开我从 0 到 1 搭建的 AI + Godot 高效工作流。\n从游戏引擎的选择，到 Claude Code、Copilot 等 AI 工具的实战配置，再到如何用“明确需求”的方法论（SMART原则+双钻模型）来驾驭 AI，让它不仅仅是写代码的工具，更成为"
  },
  {
    "id": "bvid:BV17Lap6VEUr",
    "domain": "AI",
    "title": "【全80集】Vibe Coding 零基础入门到实战教程，由浅入深（全程干货）",
    "url": "http://www.bilibili.com/video/av117353572468721",
    "source": "数据拾光屋",
    "platform": "bilibili",
    "points": 67184,
    "published_at": "2026-10-02T09:25:00+00:00",
    "summary": "本套教程专门为零基础学员而制，全程干货无废话，喜欢的小伙伴记得点赞三连喔 ~"
  },
  {
    "id": "bvid:BV1uTnP62Eu1",
    "domain": "AI",
    "title": "【AI开发单片机系统】不写一行代码：STM32从零到成品全流程实战",
    "url": "http://www.bilibili.com/video/av117472841697065",
    "source": "叶江航",
    "platform": "bilibili",
    "points": 57849,
    "published_at": "2026-10-20T10:50:16+00:00",
    "summary": "该教程用 AI 辅助开发，零代码编写，快速从想法到成品做出一套完整的 STM32 物联网系统。\n以STM32 智能温控风扇系统为实战案例，带你从 0 到 1 完成整个单片机系统的设计与制作。\n\n全程演示一套可复用的「AI 开发六步法」：\n需求分析 → 硬件选型 → 功能拆解 → 硬件搭建 → 模块编程 → 系统联调\n学会这套方法，你也能快速做出自己的单片机系统。"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 57156,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1SMyozuERk",
    "domain": "AI",
    "title": "AI 爆款视频复刻实操：用豆包工作实现提示词倒推 + 剧情改编 + AI 成片剪辑【ai漫剧教程】",
    "url": "http://www.bilibili.com/video/av117670041093416",
    "source": "北航90后副教授何静",
    "platform": "bilibili",
    "points": 53435,
    "published_at": "2026-11-24T06:56:28+00:00",
    "summary": "刷到喜欢的爆款视频，想做同款却不知道怎么下手？\n这期ai 漫剧教程继续用豆包工作，分享 3 种完全不一样的 AI 二创思路：\n✅ 视觉同款：保留画面效果，一键替换角色、场景\n✅ 形式同款：上传视频倒推镜头提示词，复刻运镜节奏\n✅ 创意同款：借鉴爆款冲突，重新改编原创短剧剧情\n素材生成完，还可以直接交给agent自动筛选镜头、剪辑成片、加字幕配乐。\n配套提示词模板放在视频里，截图就能直接套用。\n你平"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 50768,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1nXQEBnEBG",
    "domain": "AI",
    "title": "Claude.md:AI 编程的 “宪法”，如何编写 Claude.md 新手指南",
    "url": "http://www.bilibili.com/video/av116408008573973",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 48328,
    "published_at": "2026-04-15T09:28:16+00:00",
    "summary": "本视频介绍了 claude.md 的编写指南：\n1、了解 Claude.md\n2、如何编写 Claude.md\n3、使用/init 命令初始化 claude.md"
  },
  {
    "id": "bvid:BV1uVSUBkEfZ",
    "domain": "AI",
    "title": "Microsoft Copilot完整教程(上) 从入门到Agent 一站式掌握AI办公",
    "url": "http://www.bilibili.com/video/av116351721084069",
    "source": "星小脉",
    "platform": "bilibili",
    "points": 48245,
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
    "points": 47158,
    "published_at": "2026-10-30T11:52:06+00:00",
    "summary": "一句话，让 AI 帮我们完成第一个 STM32C5 程序！🚀\n本期我们一起认识 AI Agent，学习如何描述开发需求，并借助开源的 STM32C5DevSkills，让 AI 完成工程创建、芯片配置、代码编写和编译烧录，让律动小板上的小灯闪烁起来！\n也特别感谢 @意法半导体中国   对本系列教程的支持～下期我们再亲手走一遍开发流程，把 Agent 替我们完成的工作，一步步搞明白！"
  },
  {
    "id": "bvid:BV1thQPYfEYC",
    "domain": "AI",
    "title": "全流程演示Cursor + Blender MCP实现自动3D建模",
    "url": "http://www.bilibili.com/video/av114155835103525",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 44819,
    "published_at": "2025-03-13T15:31:17+00:00",
    "summary": "自动3D建模这个例子，是不是让大家一下子就看懂MCP的用途了。\n.\n后面会实测更多Cursor+MCP的更多玩法，欢迎继续围观\n.\n欢迎加入我的知识星球，有问必答：https://t.zsxq.com/fD4Fb\n.\nblender mcp项目：https://github.com/ahujasid/blender-mcp/tree/main"
  },
  {
    "id": "bvid:BV1BygA6KEAi",
    "domain": "AI",
    "title": "DeepSeek Harness + ComfyUI：Agent开始自己跑AI工作流了！",
    "url": "http://www.bilibili.com/video/av117093508910174",
    "source": "啦啦啦的小黄瓜",
    "platform": "bilibili",
    "points": 41789,
    "published_at": "2026-08-14T11:01:16+00:00",
    "summary": "小助理联系方式：zhuli240614\nComfyUI节点详解网址：uinodes.com，网站使用教程：\n[ComfyUI]全网最详细节点测试以及参数详解，近千节点持续更新，纯干货教程总结梳理。\n\nMiniMax Music3模型以及工作流：https://pan.quark.cn/s/f19f1109a481\n所有模型以及工作流分享：https://pan.quark.cn/s/ef8c640"
  },
  {
    "id": "bvid:BV1Nu3M6bEXE",
    "domain": "AI",
    "title": "【上海交大张倬胜】大模型系列课程从入门到精通，手把手教学，保姆级教程！涵盖预训练模型微调与部署、提示学习与思维链、模型水印、多模态大模型，比啃书效果好多了",
    "url": "http://www.bilibili.com/video/av116979859984479",
    "source": "Agent开发教程",
    "platform": "bilibili",
    "points": 38981,
    "published_at": "2026-07-25T09:34:49+00:00",
    "summary": "【上海交大张倬胜】大模型系列课程从入门到精通，手把手教学，保姆级教程！涵盖预训练模型微调与部署、提示学习与思维链、模型水印、多模态大模型，比啃书效果好多了，草履虫都能学会！"
  },
  {
    "id": "bvid:BV1gwcAzkEhw",
    "domain": "AI",
    "title": "Claude Code Agent Teams上手指南+项目实测",
    "url": "http://www.bilibili.com/video/av116037064331269",
    "source": "程序员阿江-Relakkes",
    "platform": "bilibili",
    "points": 36655,
    "published_at": "2026-02-08T23:30:00+00:00",
    "summary": "用Claude Code干复杂任务总碰到三个问题：\n\n上下文越来越长开始遗忘、任务只能串行效率低、单Agent视角单一容易漏检。\n\nClaude官方发布的Agent Teams功能正好解决这些痛点\n\n一个Team Lead拆任务，多个Teammate并行执行，还能互相通信协调。\n\n本期视频从核心概念、使用场景、底层架构到真实项目实战，带你完整搞懂Agent Teams的正确打开方式。"
  },
  {
    "id": "bvid:BV1sQaL6vEkb",
    "domain": "AI",
    "title": "小白向，ai入门第一课：agent的部署和使用！",
    "url": "http://www.bilibili.com/video/av117349378166797",
    "source": "沈三殊",
    "platform": "bilibili",
    "points": 34979,
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
    "points": 33577,
    "published_at": "2026-10-27T16:09:19+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1SwyXzoEms",
    "domain": "AI",
    "title": "狂烧上万元，我用 AI 做了 500 多个网站！",
    "url": "http://www.bilibili.com/video/av117666283002439",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 32405,
    "published_at": "2026-11-23T14:51:52+00:00",
    "summary": "我的第二个出海产品 VibeFather 来了，几百个现成的网站模板，让你快速通过 AI 编程工具做出同款网站，提供完整提示词和设计规范文档，让 Vibe Coding 又快又省 tokens。\n模板大全：vibefather.ai\n开源指路：github.com/liyupi/awesome-vibe-coding-websites\n编程学习教程+实战项目+简历模板：codefather.cn\n"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 31330,
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
    "points": 30009,
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
    "points": 29079,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22872,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1xLtS6WEVG",
    "domain": "AI",
    "title": "DeepSeek Harness的MCP应用教程、MCP安装、MCP迁移、MCP删除与卸载",
    "url": "http://www.bilibili.com/video/av117201218635665",
    "source": "eogee",
    "platform": "bilibili",
    "points": 18696,
    "published_at": "2026-09-02T11:33:53+00:00",
    "summary": "MCP 是扩展 Agent 能力的主要方式：接入一个 MCP 服务器，Agent 就能获得一整套现成的外部工具。DeepSeek Harness（命令名 `dsh`，简称 DSH）内置了 MCP 客户端桥插件，配置即可接入社区海量 MCP 服务。本教程以实战为主线，介绍在 dsh 中接入现成 MCP 服务、接入自定义 MCP 服务的完整流程，给出从 Claude Code、Codex 迁移配置的对"
  },
  {
    "id": "bvid:BV13Asb6cE17",
    "domain": "AI",
    "title": "Claude Code 从0到1全攻略：装环境、设权限、接 MCP、写可复用技能、拆子智能体、配自动钩子，全程讲透从装到用的整套流程，建议收藏慢慢看！AI大模型",
    "url": "http://www.bilibili.com/video/av117642291582518",
    "source": "大模型分享员",
    "platform": "bilibili",
    "points": 18588,
    "published_at": "2026-11-19T09:13:50+00:00",
    "summary": "这个合集用大白话讲清 Claude Code，先说清楚它到底是什么、能帮你做什么，再带你装好并配好环境；接着讲权限与控制模式、内置命令的用法，让它按你的规矩干活；然后一步步接上 MCP 用外部工具、写 Skill 复用常用能力、配 Hooks 做自动化、拆子智能体分工，最后用 SDD 规范把需求到代码的流程固定下来。全程按真实操作演示，每集都能跟着做，遇到坑也能提前避开，建议先收藏慢慢看。"
  },
  {
    "id": "bvid:BV1yyQEBdEkm",
    "domain": "AI",
    "title": "【2026B站最全】Claude Code+软件测试实操教程!看完我直接删了收藏夹所有测试教程,从账号注册到Plan驱动测试项目,小白3天上手！",
    "url": "http://www.bilibili.com/video/av116408092525631",
    "source": "软件测试大神",
    "platform": "bilibili",
    "points": 15721,
    "published_at": "2026-04-15T09:55:02+00:00",
    "summary": "配套资料👉：https://b23.tv/qvhxmaQ\n包括:AI测试网站，几十个AI场景测试完整流程，skil文档，测试八股文，项目源码，测试用例模板，工具安装包，学习计划表，学习路线，100g测试新人资料包等等，资料百分百免费，放心领取~"
  },
  {
    "id": "hn:50611576",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Reinstates Jensen Huang as CEO",
    "url": "https://www.cnbc.com/2026/11/23/nvidia-jensen-huang-ceo.html",
    "source": "jaz",
    "platform": "hackernews",
    "points": 2674,
    "published_at": "2026-11-23T14:00:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:50611588",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang Reinstated as Nvidia CEO",
    "url": "https://nvidianews.nvidia.com/news/nvidia-board-reinstates-jensen-huang-as-president-ceo-and-board-director",
    "source": "alanwong",
    "platform": "hackernews",
    "points": 1708,
    "published_at": "2026-11-23T14:01:23+00:00",
    "summary": ""
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
    "points": 671,
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
    "id": "hn:50581438",
    "domain": "AI 算力 / 半导体",
    "title": "US SEC's Nvidia probe is examining potential accounting issues – sources",
    "url": "https://www.marketscreener.com/news/us-sec-s-nvidia-probe-is-examining-potential-accounting-issues-sources-say-ce785ed3dd8ff627",
    "source": "ftchd",
    "platform": "hackernews",
    "points": 308,
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
    "points": 150,
    "published_at": "2026-11-14T14:09:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:50618490",
    "domain": "AI 算力 / 半导体",
    "title": "Congress shreds Nvidia's 'outrageous' return of Huang: 'Failure of character'",
    "url": "https://www.cnbc.com/2026/11/23/nvidia-jensen-huang-congress-trump.html",
    "source": "MilnerRoute",
    "platform": "hackernews",
    "points": 69,
    "published_at": "2026-11-23T20:13:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:50626861",
    "domain": "AI 算力 / 半导体",
    "title": "Who in Washington owns and trades Nvidia stock",
    "url": "https://www.kadoa.com/congress/insights/trump-nvidia",
    "source": "hubraumhugo",
    "platform": "hackernews",
    "points": 64,
    "published_at": "2026-11-24T11:51:05+00:00",
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
    "id": "hn:50621127",
    "domain": "AI 算力 / 半导体",
    "title": "Short Nvidia Fund Halted After 91% Wipeout",
    "url": "https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-11-23-2026/card/short-nvidia-fund-halted-after-91-wipeout-myoKEHNFkGcseucDUC48",
    "source": "devy",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-11-23T23:36:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:50616243",
    "domain": "AI 算力 / 半导体",
    "title": "Trump Is Said to Have Directed Effort to Reinstate Nvidia Chief",
    "url": "https://www.nytimes.com/2026/11/23/us/politics/trump-nvidia-huang.html",
    "source": "johnny313",
    "platform": "hackernews",
    "points": 31,
    "published_at": "2026-11-23T18:03:59+00:00",
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
    "id": "rss:https://www.eetimes.com/vehicle-to-grid-great-idea-or-unrealistic-dream-part-2/",
    "domain": "AI 算力 / 半导体",
    "title": "Vehicle-to-Grid: Great Idea or Unrealistic Dream? (Part 2)",
    "url": "https://www.eetimes.com/vehicle-to-grid-great-idea-or-unrealistic-dream-part-2/",
    "source": "Bill Schweber",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T11:53:11+00:00",
    "summary": "Vehicle-to-grid technology promises grid benefits but raises concerns over battery life, charging access, costs, and driver convenience. The post Vehicle-to-Grid: Great Idea or Unrealistic Dream? (Par"
  },
  {
    "id": "rss:https://www.eetimes.com/vehicle-to-grid-great-idea-or-unrealistic-dream/",
    "domain": "AI 算力 / 半导体",
    "title": "Vehicle-to-Grid: Great Idea or Unrealistic Dream?",
    "url": "https://www.eetimes.com/vehicle-to-grid-great-idea-or-unrealistic-dream/",
    "source": "Bill Schweber",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T08:40:49+00:00",
    "summary": "Vehicle-to-grid sounds like a partial solution for enhancing the grid, but the reality of the human factor may say otherwise. The post Vehicle-to-Grid: Great Idea or Unrealistic Dream? appeared first "
  },
  {
    "id": "rss:https://www.eetimes.com/nsing-featured-cra-ai-robotics-motor-control-and-digital-energy-at-electronica-2026/",
    "domain": "AI 算力 / 半导体",
    "title": "NSING Featured CRA, AI Robotics, Motor Control and Digital Energy at electronica 2026",
    "url": "https://www.eetimes.com/nsing-featured-cra-ai-robotics-motor-control-and-digital-energy-at-electronica-2026/",
    "source": "NSING Technologies Pte. Ltd.",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T07:41:37+00:00",
    "summary": "At electronica 2026 in Munich, NSING exhibited 35 solutions built on N32‑series MCUs, N32WB BLE SoCs and NS350 TPM, covering AI robotics, motor control and digital energy, and presented its CRA compli"
  },
  {
    "id": "rss:https://www.eetimes.com/nvidia-board-reinstates-jensen-huang-as-ceo/",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Board Reinstates Jensen Huang as CEO",
    "url": "https://www.eetimes.com/nvidia-board-reinstates-jensen-huang-as-ceo/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T18:17:02+00:00",
    "summary": "Nvidia goes back to business as usual following Huang's resignation and reinstatement after a week. The post Nvidia Board Reinstates Jensen Huang as CEO appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/the-sovereign-ai-paradox-who-controls-the-compute/",
    "domain": "AI 算力 / 半导体",
    "title": "The Sovereign AI Paradox: Who Controls the Compute?",
    "url": "https://www.eetimes.com/the-sovereign-ai-paradox-who-controls-the-compute/",
    "source": "Ron Honig",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T16:08:35+00:00",
    "summary": "U.S. restrictions on overseas AI infrastructure could accelerate sovereign computing and weaken American technology dominance. The post The Sovereign AI Paradox: Who Controls the Compute? appeared fir"
  },
  {
    "id": "rss:https://www.eetimes.com/secure-flash-a-practical-path-to-cyber-resilience-act-compliance/",
    "domain": "AI 算力 / 半导体",
    "title": "Secure Flash: A Practical Path to Cyber Resilience Act Compliance",
    "url": "https://www.eetimes.com/secure-flash-a-practical-path-to-cyber-resilience-act-compliance/",
    "source": "Winbond Electronics Corporation",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T15:00:00+00:00",
    "summary": "The EU Cyber Resilience Act (CRA) introduces cybersecurity requirements for connected products throughout their lifecycle. This white paper explores how Winbond’s TrustME® W77Q Secure Flash and CRA Co"
  },
  {
    "id": "rss:https://www.eetimes.com/the-enigma-of-softbanks-1-trillion-sk-hynix-buyout-attempt/",
    "domain": "AI 算力 / 半导体",
    "title": "The Enigma of SoftBank’s $1 Trillion SK Hynix Buyout Attempt",
    "url": "https://www.eetimes.com/the-enigma-of-softbanks-1-trillion-sk-hynix-buyout-attempt/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T08:30:00+00:00",
    "summary": "Here is why it was a non-starter and what the story reveals about memory’s strategic appeal in the AI buildup. The post The Enigma of SoftBank’s $1 Trillion SK Hynix Buyout Attempt appeared first on E"
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/samsung-just-launched-a-gaming-monitor-with-a-refresh-rate-higher-than-its-price-dual-mode-odyssey-g60h-offers-1-100-hz-in-hd",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung just launched a gaming monitor with a refresh rate higher than its price — dual-mode Odyssey G60H offers 1,100 Hz in HD",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/samsung-just-launched-a-gaming-monitor-with-a-refresh-rate-higher-than-its-price-dual-mode-odyssey-g60h-offers-1-100-hz-in-hd",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T13:12:57+00:00",
    "summary": "Samsung's newly launched Odyssey G60H display is targeted squarely at serious competitive gamers with QHD 600Hz and HD 1100HZ display modes."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/vulnerability-could-let-hacker-hijack-electric-trailer-braking-system-remotely-via-bluetooth-apply-any-amount-of-force-remotely-elecbrakes-flaw-reverse-engineered-using-claude-patched-by-manufacturer",
    "domain": "AI 算力 / 半导体",
    "title": "Vulnerability could let hacker hijack electric trailer braking system remotely via Bluetooth, apply any amount of force remotely",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/vulnerability-could-let-hacker-hijack-electric-trailer-braking-system-remotely-via-bluetooth-apply-any-amount-of-force-remotely-elecbrakes-flaw-reverse-engineered-using-claude-patched-by-manufacturer",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T12:38:32+00:00",
    "summary": "After noticing that his Elecbrakes remote had automatically paired to a stranger's trailer, Patrick Forck's cyber security spider senses tingled."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/go-ad-free-across-toms-hardware-by-subscribing-to-premium-from-usd7-a-month-or-usd29-annually-support-us-to-get-seamless-browsing-read-a-treasure-trove-of-exclusive-content-and-unlock-access-to-bench",
    "domain": "AI 算力 / 半导体",
    "title": "Go ad-free across Tom’s Hardware by subscribing to Premium from $7 a month, or $29 annually",
    "url": "https://www.tomshardware.com/tech-industry/go-ad-free-across-toms-hardware-by-subscribing-to-premium-from-usd7-a-month-or-usd29-annually-support-us-to-get-seamless-browsing-read-a-treasure-trove-of-exclusive-content-and-unlock-access-to-bench",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T12:30:00+00:00",
    "summary": "Tom’s Hardware is going ad-free, exclusively for Premium members."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/hit-this-rtx-5070-ti-powered-gaming-laptop-deal-at-best-buy-and-save-usd550-asus-rog-strix-g16-only-usd1-749-with-16gb-of-ddr5-ram-and-a-1tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Hit this RTX 5070 Ti-powered gaming laptop deal at Best Buy and save $550",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/hit-this-rtx-5070-ti-powered-gaming-laptop-deal-at-best-buy-and-save-usd550-asus-rog-strix-g16-only-usd1-749-with-16gb-of-ddr5-ram-and-a-1tb-ssd",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T12:00:00+00:00",
    "summary": "Pick up a new gaming laptop in the Black Friday sales with $550 off the Asus ROG G16 at Best Buy."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/japan-puts-chipmaking-labs-inside-trucks-with-mobilefab-trucks-pack-30-cm-lithography-gear-to-tackle-a-10-year-semiconductor-engineer-shortage",
    "domain": "AI 算力 / 半导体",
    "title": "Japan puts chipmaking labs inside trucks with mobileFab",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/japan-puts-chipmaking-labs-inside-trucks-with-mobilefab-trucks-pack-30-cm-lithography-gear-to-tackle-a-10-year-semiconductor-engineer-shortage",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T11:30:00+00:00",
    "summary": "Japan's chip-making education program goes on wheels with the mobileFab — truck-mounted lithography machines let students everywhere pattern chip wiring"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/shared-cxl-memory-pools-come-with-steep-software-tax-that-could-stall-multi-server-scaling-ut-arlington-shares-real-world-test-that-measured-four-servers-sharing-the-same-pool-at-sc26",
    "domain": "AI 算力 / 半导体",
    "title": "Shared CXL memory pools come with steep software tax that could stall multi-server scaling",
    "url": "https://www.tomshardware.com/pc-components/dram/shared-cxl-memory-pools-come-with-steep-software-tax-that-could-stall-multi-server-scaling-ut-arlington-shares-real-world-test-that-measured-four-servers-sharing-the-same-pool-at-sc26",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T11:30:00+00:00",
    "summary": "UT Arlington and Intel measured software sync costs on a real four-host shared CXL memory pool, as vendors eye CXL for AI KV cache."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/grab-a-4k-ready-cyberpowerpc-gaming-rig-with-a-7800x3d-and-rtx-5070-for-usd2-099-99-newegg-knocks-usd130-off-this-liquid-cooled-desktop-with-32gb-ddr5-and-a-1tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Grab a 4K-ready CyberPowerPC gaming rig with a 7800X3D and RTX 5070 for $2,099.99",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/grab-a-4k-ready-cyberpowerpc-gaming-rig-with-a-7800x3d-and-rtx-5070-for-usd2-099-99-newegg-knocks-usd130-off-this-liquid-cooled-desktop-with-32gb-ddr5-and-a-1tb-ssd",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T11:21:13+00:00",
    "summary": "Grab this powerful CyberPowerPC gaming rig with an AMD Ryzen 7 7800X3D and Nvidia GeForce RTX 5070 for $2,099.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/nvidia-engineer-that-quit-in-response-to-jensen-huang-resignation-welcomes-ceo-back-i-may-have-moved-too-quickly-says-robotics-engineer-who-made-viral-post",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia engineer who quit over Jensen Huang's exit says he 'may have moved too quickly'",
    "url": "https://www.tomshardware.com/tech-industry/nvidia-engineer-that-quit-in-response-to-jensen-huang-resignation-welcomes-ceo-back-i-may-have-moved-too-quickly-says-robotics-engineer-who-made-viral-post",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T11:00:00+00:00",
    "summary": "An Nvidia robotics engineer that quit in response to Jensen Huang's resignation says he \"may have moved too quickly\" now that CEO is back in charge."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/wearable-tech/gamer-hijacks-plane-in-gta-6-using-just-mind-control-and-eye-tracking-xbox-controller-mapped-to-read-brain-signals-using-eeg",
    "domain": "AI 算力 / 半导体",
    "title": "Gamer hijacks plane in GTA 6 using just mind control and eye tracking",
    "url": "https://www.tomshardware.com/peripherals/wearable-tech/gamer-hijacks-plane-in-gta-6-using-just-mind-control-and-eye-tracking-xbox-controller-mapped-to-read-brain-signals-using-eeg",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T10:30:00+00:00",
    "summary": "Perri Karyal programmed an EEG device to read her brainwaves and translate it to actions on her Xbox controller."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/enthusiast-gets-gta-v-running-on-a-2007-radeon-with-just-64mb-of-vram-config-edits-windows-8-and-an-overclock-lift-it-from-1-fps-to-20-fps-but-most-cars-stop-rendering",
    "domain": "AI 算力 / 半导体",
    "title": "Enthusiast gets GTA V running on a 2007 Radeon with just 64MB of VRAM",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/enthusiast-gets-gta-v-running-on-a-2007-radeon-with-just-64mb-of-vram-config-edits-windows-8-and-an-overclock-lift-it-from-1-fps-to-20-fps-but-most-cars-stop-rendering",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T10:00:00+00:00",
    "summary": "Budget-Builds Official ran GTA V on a 2007 ATI Radeon HD 2350 with 64MB of DDR2 VRAM at 13 to 20 FPS."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/sharges-disk-pro-2-usb-hub-and-actively-cooled-m-2-enclosure-drops-to-its-lowest-ever-price-one-of-my-favorite-products-of-2026-now-starts-at-just-usd66",
    "domain": "AI 算力 / 半导体",
    "title": "Sharge's Disk Pro 2 USB hub and actively cooled M.2 enclosure drops to its lowest-ever price",
    "url": "https://www.tomshardware.com/pc-components/sharges-disk-pro-2-usb-hub-and-actively-cooled-m-2-enclosure-drops-to-its-lowest-ever-price-one-of-my-favorite-products-of-2026-now-starts-at-just-usd66",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T09:30:00+00:00",
    "summary": "Sharge's see-through hub with the ports you need and up to 8TB of storage is now on sale for $66.51 for the Lite model, or $80.91 for the Ultra model that supports up to 8K and faster card reader spee"
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/routers/grab-a-speedy-tp-link-tri-band-wi-fi-7-router-for-less-than-usd90-archer-be9500-router-is-55-percent-off-sports-10-gbe-wan-and-two-2-5-gbe-lan-ports",
    "domain": "AI 算力 / 半导体",
    "title": "Grab a TP-Link tri-band Wi-Fi 7 router for less than $90",
    "url": "https://www.tomshardware.com/networking/routers/grab-a-speedy-tp-link-tri-band-wi-fi-7-router-for-less-than-usd90-archer-be9500-router-is-55-percent-off-sports-10-gbe-wan-and-two-2-5-gbe-lan-ports",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T22:00:00+00:00",
    "summary": "TP-Link is aiming for the value crown with a $90 tri-band Wi-Fi 7 router."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/macbook-neo-falls-to-all-time-low-usd599-in-amazon-black-friday-sale-256gb-citrus-model-price-matches-its-original-launch",
    "domain": "AI 算力 / 半导体",
    "title": "MacBook Neo falls to all-time low $599 in Amazon Black Friday sale — 256GB Citrus model price matches its original launch (Update: now $649)",
    "url": "https://www.tomshardware.com/laptops/macbook-neo-falls-to-all-time-low-usd599-in-amazon-black-friday-sale-256gb-citrus-model-price-matches-its-original-launch",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T21:09:03+00:00",
    "summary": "Apple's MacBook Neo in citrus is down to $599, its original launch price from earlier this year, at Amazon."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/jensen-huang-returns-to-applause-from-employees-at-nvidia-hq-some-employees-reportedly-disgruntled-by-return-saying-this-is-the-worst-outcome",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang returns to applause from employees at Nvidia HQ",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/jensen-huang-returns-to-applause-from-employees-at-nvidia-hq-some-employees-reportedly-disgruntled-by-return-saying-this-is-the-worst-outcome",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T21:00:00+00:00",
    "summary": "Jensen Huang returned to the office after being reinstated to CEO to cheers, according to videos spread on social media."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/grab-this-usd1199-asus-prime-rtx-5070-ti-for-a-1440p-or-4k-gaming-upgrade-best-buy-deal-gets-you-into-high-end-blackwell-for-hundreds-less",
    "domain": "AI 算力 / 半导体",
    "title": "Grab this $1199 Asus Prime RTX 5070 Ti for a 1440p or 4K gaming upgrade",
    "url": "https://www.tomshardware.com/pc-components/gpus/grab-this-usd1199-asus-prime-rtx-5070-ti-for-a-1440p-or-4k-gaming-upgrade-best-buy-deal-gets-you-into-high-end-blackwell-for-hundreds-less",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T19:58:02+00:00",
    "summary": "RTX 5070 Ti graphics cards have been selling for close to twice their MSRP of late, but you can this Asus card for $1199 at Best Buy right now — the cheapest we've seen so far in the Black Friday fren"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/electric-intel-core-ultra-7-270k-plus-deal-knocks-it-down-to-just-usd232-25-percent-discount-marks-a-new-all-time-low-for-arrow-lake-refresh",
    "domain": "AI 算力 / 半导体",
    "title": "Electric Intel Core Ultra 7 270K Plus deal knocks it down to just $232",
    "url": "https://www.tomshardware.com/pc-components/cpus/electric-intel-core-ultra-7-270k-plus-deal-knocks-it-down-to-just-usd232-25-percent-discount-marks-a-new-all-time-low-for-arrow-lake-refresh",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T19:24:52+00:00",
    "summary": "The Intel Core Ultra 7 270K Plus is back in stock at Amazon for an all-time low price of just $232, over $80 off its average selling price."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/stock-up-on-storage-with-4tb-t-force-g50-ssd-at-just-usd0-10-per-gb-entry-level-pcie-4-0-drive-offers-decent-performance-and-lots-of-capacity",
    "domain": "AI 算力 / 半导体",
    "title": "Stock up on storage with 4TB T-Force G50 SSD at just $0.10 per GB",
    "url": "https://www.tomshardware.com/pc-components/ssds/stock-up-on-storage-with-4tb-t-force-g50-ssd-at-just-usd0-10-per-gb-entry-level-pcie-4-0-drive-offers-decent-performance-and-lots-of-capacity",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T18:11:09+00:00",
    "summary": "Team Group has an excellent deal on its 4TB T-Force G50 Evo, knocking the price down to just $0.10 per GB ahead on Black Friday."
  },
  {
    "id": "hn:50552424",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Neon",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/",
    "source": "yigitdemirag",
    "platform": "hackernews",
    "points": 1070,
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
    "points": 376,
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
    "points": 284,
    "published_at": "2026-11-20T16:59:27+00:00",
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
    "id": "hn:50550415",
    "domain": "大厂 AI 动态",
    "title": "Genie 4 is now available",
    "url": "https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/",
    "source": "leumon",
    "platform": "hackernews",
    "points": 294,
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
    "points": 288,
    "published_at": "2026-11-18T04:14:04+00:00",
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
    "id": "hn:50554374",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Neon looks like an Opus 5.5 competitor",
    "url": "https://micjm.com/blog/gemini-4-neon-looks-like-a-top-model/",
    "source": "seizethecheese",
    "platform": "hackernews",
    "points": 257,
    "published_at": "2026-11-19T00:29:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:50569519",
    "domain": "大厂 AI 动态",
    "title": "What Comes After AGI?",
    "url": "https://institute.deepmind.com/essays/what-comes-after-agi/",
    "source": "jdkee",
    "platform": "hackernews",
    "points": 178,
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
    "id": "rss:https://www.theverge.com/transportation/1040676/uber-nuro-lucid-driverless-robotaxi-testing-bay-area",
    "domain": "大厂 AI 动态",
    "title": "Uber, Nuro, and Lucid kick off fully driverless robotaxi testing",
    "url": "https://www.theverge.com/transportation/1040676/uber-nuro-lucid-driverless-robotaxi-testing-bay-area",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T13:00:00+00:00",
    "summary": "Uber's high-stakes robotaxi bet is officially ditching its human safety net. Nuro, Lucid, and Uber are starting fully driverless public road testing in the San Francisco Bay Area, with employee-only r"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1041000/kagi-mail-email-google-gmail-alternative",
    "domain": "大厂 AI 动态",
    "title": "Google alternative Kagi launches an email service",
    "url": "https://www.theverge.com/tech/1041000/kagi-mail-email-google-gmail-alternative",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T00:02:52+00:00",
    "summary": "Kagi, which already offers a paid alternative to Google Search and its own Orion browser as a rival to Chrome, is taking on another Google service: Gmail. Today, Kagi announced a public beta of Kagi M"
  },
  {
    "id": "rss:https://www.theverge.com/games/1040966/arion-kurtaj-gta-vi-leaks-sentenced-released",
    "domain": "大厂 AI 动态",
    "title": "The hacker behind early GTA VI leaks has been sentenced — and released",
    "url": "https://www.theverge.com/games/1040966/arion-kurtaj-gta-vi-leaks-sentenced-released",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T23:25:01+00:00",
    "summary": "Arion Kurtaj, who pleaded guilty last week to hacking Grand Theft Auto VI developer Rockstar Games and other companies, including Uber and Revolut, was sentenced to seven years in prison but released "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1026041/holiday-gift-guide-2026",
    "domain": "大厂 AI 动态",
    "title": "The Verge’s 2026 holiday gift guide",
    "url": "https://www.theverge.com/gadgets/1026041/holiday-gift-guide-2026",
    "source": "Ryan Waniata",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T23:14:10+00:00",
    "summary": "Gift-giving isn't just about grabbing something solid under a determined spending limit. It's an expression of love, a way to show someone how well you really know them. That doesn't mean you have to "
  },
  {
    "id": "rss:https://www.theverge.com/tech/1040872/ladybird-indie-browser-engine-alpha-testing",
    "domain": "大厂 AI 动态",
    "title": "Ladybird, the first new browser engine in years, is now available to test",
    "url": "https://www.theverge.com/tech/1040872/ladybird-indie-browser-engine-alpha-testing",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T22:38:09+00:00",
    "summary": "Ladybird, an independent web browser with a built-from-scratch engine, is finally available for testing. On Monday, Ladybird developer Andreas Kling announced that the browser is launching in alpha on"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1040652/jensen-huang-nvidia-trump-reinstated",
    "domain": "大厂 AI 动态",
    "title": "Trump engineered a risky comeback for Jensen Huang",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1040652/jensen-huang-nvidia-trump-reinstated",
    "source": "Hayden Field",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T22:25:12+00:00",
    "summary": "After Nvidia's board accepted Jensen Huang's resignation as CEO, following reports that Huang had an affair with an alleged Chinese spy, President Donald Trump, too, appeared to submit to the new real"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1030422/nvidia-jensen-huang-ai-china-alice-huang",
    "domain": "大厂 AI 动态",
    "title": "Nvidia CEO Jensen Huang is back. What happens next?",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1030422/nvidia-jensen-huang-ai-china-alice-huang",
    "source": "Richard Lawler",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T22:10:32+00:00",
    "summary": "After the leather-jacketed CEO, president, and co-founder of Nvidia, Jensen Huang, acknowledged an affair with Megaspeed exec Alice Huang, his company initially announced an investigation. However, af"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1040819/welcome-to-elite-impunity-jensen-huang",
    "domain": "大厂 AI 动态",
    "title": "Welcome to elite impunity, Jensen Huang",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1040819/welcome-to-elite-impunity-jensen-huang",
    "source": "Elizabeth Lopatto",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T22:09:26+00:00",
    "summary": "I suppose I must issue a hearty congratulations to Jensen Huang. Huang is CEO of Nvidia again, to the surprise of basically everyone except President Donald Trump and Vice President JD Vance, who made"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1034512/apple-watch-series-12-black-friday-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "The Apple Watch Series 12 is cheaper than ever ahead of Black Friday",
    "url": "https://www.theverge.com/gadgets/1034512/apple-watch-series-12-black-friday-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T21:36:48+00:00",
    "summary": "If you’re still sporting an Apple Watch that launched five or so years ago, now is a good time to upgrade. Apple’s latest smartwatch, the 42mm Apple Watch Series 12 with Wi-Fi and GPS connectivity, ha"
  },
  {
    "id": "rss:https://www.theverge.com/science/1040497/ai-data-centers-electricity-un-climate-summit",
    "domain": "大厂 AI 动态",
    "title": "AI data centers throw another wrench into chaotic UN climate talks",
    "url": "https://www.theverge.com/science/1040497/ai-data-centers-electricity-un-climate-summit",
    "source": "Justine Calma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T21:09:37+00:00",
    "summary": "The clean energy revolution hinges on electrifying the entire global economy just as power-hungry data centers are surging. It's a challenge delegates from all over the world had to grapple with durin"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/23/figma-employee-sues-alleging-company-forced-her-to-confront-harassers/",
    "domain": "大厂 AI 动态",
    "title": "Figma employee sues, alleging company forced her to confront harassers",
    "url": "https://techcrunch.com/2026/11/23/figma-employee-sues-alleging-company-forced-her-to-confront-harassers/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T23:07:49+00:00",
    "summary": "Figma and its CEO are being sued by a current employee for alleged sexual harassment and discrimination."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/23/anthropic-launches-claude-ship-letting-ai-agents-review-fix-and-approve-code-changes/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic launches Claude Ship, letting AI agents review, fix, and approve code changes",
    "url": "https://techcrunch.com/2026/11/23/anthropic-launches-claude-ship-letting-ai-agents-review-fix-and-approve-code-changes/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T22:05:50+00:00",
    "summary": "As AI-generated code piles up, Anthropic's new developer tools aim to eliminate another bottleneck by letting agents handle routine approvals."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/23/supertake-raises-20m-to-let-ai-agents-turn-your-market-predictions-into-stock-portfolios/",
    "domain": "大厂 AI 动态",
    "title": "Supertake raises $20M to let AI agents turn your market predictions into stock portfolios",
    "url": "https://techcrunch.com/2026/11/23/supertake-raises-20m-to-let-ai-agents-turn-your-market-predictions-into-stock-portfolios/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T22:02:05+00:00",
    "summary": "Think you know where the market is headed? A startup called Supertake lets you put money behind your ideas without having to pick the stocks yourself."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/23/elon-musk-and-others-rejoice-as-jensen-huang-is-reinstated-at-nvidia-amid-scandal/",
    "domain": "大厂 AI 动态",
    "title": "Elon Musk and others rejoice as Jensen Huang is reinstated at Nvidia amid scandal",
    "url": "https://techcrunch.com/2026/11/23/elon-musk-and-others-rejoice-as-jensen-huang-is-reinstated-at-nvidia-amid-scandal/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T21:47:41+00:00",
    "summary": "\"The mistake has been corrected,\" Elon Musk chimed in."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/23/megaspeed-the-company-at-the-center-of-the-jensen-huang-scandal-appears-headed-for-a-u-s-blacklist/",
    "domain": "大厂 AI 动态",
    "title": "Megaspeed, the company at the center of the Jensen Huang scandal, appears headed for a US blacklist",
    "url": "https://techcrunch.com/2026/11/23/megaspeed-the-company-at-the-center-of-the-jensen-huang-scandal-appears-headed-for-a-u-s-blacklist/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T21:25:42+00:00",
    "summary": "Megaspeed, which was previously led by Alice Huang, would be barred from doing business with U.S. companies unless those companies attained a special license from the federal government."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/23/nvidia-employees-greet-jensen-huang-like-a-hero-as-he-returns-to-companys-hq/",
    "domain": "大厂 AI 动态",
    "title": "Nvidia employees greet Jensen Huang like a hero as he returns to company’s HQ",
    "url": "https://techcrunch.com/2026/11/23/nvidia-employees-greet-jensen-huang-like-a-hero-as-he-returns-to-companys-hq/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T20:38:53+00:00",
    "summary": "\"I'm going to be a better CEO the second time around,\" Huang told employees."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/23/outrageous-reckless-wow-heres-what-politicians-are-saying-about-jensen-huangs-return-to-nvidia/",
    "domain": "大厂 AI 动态",
    "title": "‘Outrageous,’ ‘reckless,’ ‘wow’: Here’s what politicians are saying about Jensen Huang’s return to Nvidia",
    "url": "https://techcrunch.com/2026/11/23/outrageous-reckless-wow-heres-what-politicians-are-saying-about-jensen-huangs-return-to-nvidia/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T19:31:41+00:00",
    "summary": "Politicians on both sides of the aisle seem angry, agitated, and nonplussed by the return of Jensen Huang to Nvidia leadership less than two weeks after his ousting."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/23/google-searchs-ai-mode-can-now-tap-into-drive-and-wallet-for-more-personalized-responses/",
    "domain": "大厂 AI 动态",
    "title": "Google Search’s AI Mode can now tap into Drive and Wallet for more personalized responses",
    "url": "https://techcrunch.com/2026/11/23/google-searchs-ai-mode-can-now-tap-into-drive-and-wallet-for-more-personalized-responses/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T19:14:46+00:00",
    "summary": "By bringing Personal Intelligence in AI Mode to Drive, Wallet, and the Gemini app, Google is leveraging the wealth of user data that's already within its ecosystem"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/23/jensen-huang-scheduled-to-testify-next-week-in-senate-following-reinstatement-as-nvidia-ceo/",
    "domain": "大厂 AI 动态",
    "title": "Jensen Huang scheduled to testify next week in Senate following reinstatement as Nvidia CEO",
    "url": "https://techcrunch.com/2026/11/23/jensen-huang-scheduled-to-testify-next-week-in-senate-following-reinstatement-as-nvidia-ceo/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T18:12:22+00:00",
    "summary": "The public hearing follows bipartisan calls for Huang to testify about the affair with the suspected Chinese spy."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/23/amazon-snaps-up-decarts-ai-optimization-tech-for-7-5b-as-it-prepares-to-sell-trainium-chips/",
    "domain": "大厂 AI 动态",
    "title": "Amazon snaps up Decart’s AI optimization tech for $7.5B as it prepares to sell Trainium chips",
    "url": "https://techcrunch.com/2026/11/23/amazon-snaps-up-decarts-ai-optimization-tech-for-7-5b-as-it-prepares-to-sell-trainium-chips/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T17:14:23+00:00",
    "summary": "Amazon is acquiring Decart’s AI optimization technology and research team in a reported $7.5 billion deal."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/23/meta-throws-out-its-net-zero-goal-its-competitors-should-be-furious/",
    "domain": "大厂 AI 动态",
    "title": "Meta throws out its net-zero goal — its competitors should be furious",
    "url": "https://techcrunch.com/2026/11/23/meta-throws-out-its-net-zero-goal-its-competitors-should-be-furious/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T17:13:45+00:00",
    "summary": "Meta walked back its 2030 net-zero goal in its 2026 sustainability report, a decision that could send ripples throughout the tech industry."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/23/jensen-huang-isnt-out-of-the-woods-yet/",
    "domain": "大厂 AI 动态",
    "title": "Jensen Huang isn’t out of the woods yet",
    "url": "https://techcrunch.com/2026/11/23/jensen-huang-isnt-out-of-the-woods-yet/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T16:57:40+00:00",
    "summary": "Tech leaders should be clear-eyed about all the problems likely to come with Huang's reinstatement."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/23/trump-reportedly-called-into-nvidia-board-meeting-to-advocate-for-huangs-return/",
    "domain": "大厂 AI 动态",
    "title": "Trump reportedly called into Nvidia board meeting to advocate for Huang’s return",
    "url": "https://techcrunch.com/2026/11/23/trump-reportedly-called-into-nvidia-board-meeting-to-advocate-for-huangs-return/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T16:39:10+00:00",
    "summary": "\"I spoke to them, let me put it that way … And I convinced them,\" the president told CNBC."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/23/crowdstrike-to-acquire-zscaler-for-44-billion/",
    "domain": "大厂 AI 动态",
    "title": "CrowdStrike to acquire Zscaler for $44 billion",
    "url": "https://techcrunch.com/2026/11/23/crowdstrike-to-acquire-zscaler-for-44-billion/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T16:20:11+00:00",
    "summary": "The cybersecurity giant said that the deal to buy Zscaler, which provides zero-trust products to large enterprises, will better equip their customers to use AI agents."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/23/dutch-privacy-authority-urges-consumers-not-to-buy-pervert-glasses/",
    "domain": "大厂 AI 动态",
    "title": "Dutch privacy authority urges consumers not to buy ‘pervert glasses’",
    "url": "https://techcrunch.com/2026/11/23/dutch-privacy-authority-urges-consumers-not-to-buy-pervert-glasses/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T15:29:49+00:00",
    "summary": "The Netherlands' data protection agency said smart wearables violate people's privacy, get information wrong, and can result in unsafe situations."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/23/trump-endorses-jensen-huangs-return-to-nvidia-says-us-has-no-evidence-of-wrongdoing/",
    "domain": "大厂 AI 动态",
    "title": "Trump endorses Jensen Huang’s return to Nvidia, says US has no evidence of wrongdoing",
    "url": "https://techcrunch.com/2026/11/23/trump-endorses-jensen-huangs-return-to-nvidia-says-us-has-no-evidence-of-wrongdoing/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T15:04:01+00:00",
    "summary": "The president cited the U.S. attorney general in defending Huang's return, while urging Nvidia to continue its export-control investigation."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/23/sierra-doubles-valuation-to-30b-within-six-months-as-demand-for-ai-in-cx-takes-off/",
    "domain": "大厂 AI 动态",
    "title": "Sierra doubles valuation to $30B within six months as demand for AI in CX takes off",
    "url": "https://techcrunch.com/2026/11/23/sierra-doubles-valuation-to-30b-within-six-months-as-demand-for-ai-in-cx-takes-off/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T14:43:03+00:00",
    "summary": "Enterprise customer experience company Sierra, co-founded by former Salesforce co-CEO Bret Taylor, said on Monday that it has raised $1.75 billion in a Series F round."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/23/nvidia-reverses-course-and-brings-jensen-huang-back-as-ceo/",
    "domain": "大厂 AI 动态",
    "title": "Nvidia reverses course and brings Jensen Huang back as CEO",
    "url": "https://techcrunch.com/2026/11/23/nvidia-reverses-course-and-brings-jensen-huang-back-as-ceo/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T14:21:59+00:00",
    "summary": "The stunning reversal was supported by senior officials in the U.S. government."
  },
  {
    "id": "hn:50556287",
    "domain": "股票",
    "title": "Ruby2ßhell: Pre-authentication RCE on stock Rails",
    "url": "https://verialabs.com/ruby2shell/",
    "source": "jdns",
    "platform": "hackernews",
    "points": 408,
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
    "id": "hn:50620721",
    "domain": "股票",
    "title": "Freeing the iPod Nano 5G",
    "url": "https://viktorkrapivin.com/blog/nano5g-priv-prvd",
    "source": "rpm_conservatio",
    "platform": "hackernews",
    "points": 127,
    "published_at": "2026-11-23T23:03:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:50583254",
    "domain": "股票",
    "title": "Nasdaq erases all 2026 gains",
    "url": "https://www.cnbc.com/2026/11/19/stock-market-today-live-updates.html",
    "source": "mv4",
    "platform": "hackernews",
    "points": 133,
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
    "id": "hn:50617640",
    "domain": "股票",
    "title": "Two \"suspicious clusters\" on Polymarket Made Over $340k on Huang Comeback",
    "url": "https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-11-23-2026/card/two-groups-of-polymarket-accounts-made-over-340-000-on-huang-comeback-Lan2T0TwbJPNsyhmQHGq",
    "source": "qlte",
    "platform": "hackernews",
    "points": 56,
    "published_at": "2026-11-23T19:25:21+00:00",
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
    "id": "hn:50581060",
    "domain": "股票",
    "title": "Army delays detonating \"catastrophically hazardous\" lead azide amid fear, anger",
    "url": "https://arstechnica.com/science/2026/11/outrage-questions-swirl-as-army-delays-blowing-up-stockpile-of-toxic-lead-azide/",
    "source": "Bender",
    "platform": "hackernews",
    "points": 34,
    "published_at": "2026-11-20T20:01:48+00:00",
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
    "id": "rss:https://www.netinterest.co/p/supply-and-demand",
    "domain": "股票",
    "title": "Supply and Demand",
    "url": "https://www.netinterest.co/p/supply-and-demand",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T15:38:25+00:00",
    "summary": "Finding Equilibrium Inside the AI Economy"
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
    "id": "hn:50439616",
    "domain": "股票",
    "title": "Anthropic to Seek $1.3T Valuation in IPO",
    "url": "https://www.wsj.com/finance/stocks/anthropic-to-seek-1-3-trillion-valuation-in-ipo-8337b669",
    "source": "sonabinu",
    "platform": "hackernews",
    "points": 60,
    "published_at": "2026-11-10T12:49:32+00:00",
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
    "id": "hn:50532613",
    "domain": "金融",
    "title": "Brazil's tax authority open-sources its tax calculator on GitHub under MIT",
    "url": "https://www.gov.br/receitafederal/pt-br/assuntos/noticias/2026/novembro/receita-federal-publica-primeiro-codigo-fonte-aberto-no-github-e-amplia-transparencia-da-reforma-tributaria",
    "source": "dvaplima",
    "platform": "hackernews",
    "points": 789,
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
    "points": 198,
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
    "id": "hn:50602847",
    "domain": "金融",
    "title": "Canada recommits to federal funding for news",
    "url": "https://www.niemanlab.org/2026/11/a-government-that-gets-it-canada-recommits-to-federal-funding-for-news/",
    "source": "DeepLogin",
    "platform": "hackernews",
    "points": 126,
    "published_at": "2026-11-22T19:10:38+00:00",
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
    "points": 152,
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
    "id": "hn:50605699",
    "domain": "金融",
    "title": "'It's greed': Zohran Mamdani blasts Amazon over new $5 fee hike in NYC",
    "url": "https://finance.yahoo.com/economy/policy/articles/greed-zohran-mamdani-blasts-amazon-121000124.html",
    "source": "madihaa",
    "platform": "hackernews",
    "points": 58,
    "published_at": "2026-11-23T00:23:37+00:00",
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
    "points": 33,
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
    "points": 37,
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
