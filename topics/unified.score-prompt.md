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

- 今日日期：`2026-10-27`
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
  "date": "2026-10-27",
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
    "points": 2162297,
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
    "points": 2037882,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 1441692,
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
    "points": 1397248,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1VZWc6dECG",
    "domain": "AI",
    "title": "【Re:从零开始的AI学习】第一季总集篇｜从入门到用好 AI",
    "url": "http://www.bilibili.com/video/av117430848391663",
    "source": "卡普迪姆",
    "platform": "bilibili",
    "points": 1023829,
    "published_at": "2026-10-13T00:57:21+00:00",
    "summary": "这次，我把【Re：从零开始的 AI 学习】第一季全 13 期完整连在一起啦！\n新来的朋友或者想要查漏补缺的伙伴，现在可以一口气通关！从 AI 入门与提示词技巧，到 Agent 玩法、主流模型对比与使用成本……跟着走一遍就能彻底搞懂。\n希望这个系列能给你带来哪怕一点点启发，欢迎点赞、投币、收藏一键三连支持！也超级欢迎转发安利给身边的朋友～\n\n【目录】\n00:00 导语\n00:32 AI 这三年发生了"
  },
  {
    "id": "bvid:BV1aeLqzUE6L",
    "domain": "AI",
    "title": "10分钟讲清楚 Prompt, Agent, MCP 是什么",
    "url": "http://www.bilibili.com/video/av114410228025650",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 905448,
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
    "points": 877403,
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
    "points": 731887,
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
    "points": 675041,
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
    "points": 594339,
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
    "points": 426126,
    "published_at": "2025-03-13T13:18:09+00:00",
    "summary": "MCP是近期的AI领域的热点，特别是在海外社区获得热烈讨论，每天都有大量MCP工具诞生。本期视频我们从MCP的概念，技术原理，到多场景实战，一个视频看懂MCP的全部内容。\n\n\nMCP官方开源仓库：https://github.com/modelcontextprotocol/servers\nMCP合集网站：  https://smithery.ai/\nVscode下载：https://code.v"
  },
  {
    "id": "bvid:BV1ia9UBPESQ",
    "domain": "AI",
    "title": "在VScode中配置Claude Code并接入DeepSeek V4 Pro【oo唠嗑教程】",
    "url": "http://www.bilibili.com/video/av116487012549813",
    "source": "沉默的羔丸ovo",
    "platform": "bilibili",
    "points": 362888,
    "published_at": "2026-04-29T08:23:29+00:00",
    "summary": "配置方法如下：\n(想用真心换取你的关注...蟹蟹泥...)\nsetting.json添加：\n{ &quot;name&quot;: &quot;ANTHROPIC_BASE_URL&quot;, &quot;value&quot;: &quot;https://xxxx&quot; }, \n{ &quot;name&quot;: &quot;ANTHROPIC_AUTH_TOKEN&quot;, "
  },
  {
    "id": "bvid:BV1vG8QzcE5X",
    "domain": "AI",
    "title": "Claude使用指南，claude code零基础教程，claude code安装配置到实战",
    "url": "http://www.bilibili.com/video/av114933744272468",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 357388,
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
    "points": 336393,
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
    "points": 315179,
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
    "points": 287453,
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
    "points": 217454,
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
    "points": 184884,
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
    "points": 163631,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV1eYPpeWEnT",
    "domain": "AI",
    "title": "Cursor + MCP = 王炸！彻底颠覆我的Cursor工作流，效率直接起飞",
    "url": "http://www.bilibili.com/video/av114073660301264",
    "source": "御风大世界",
    "platform": "bilibili",
    "points": 151701,
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
    "points": 143904,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1PgCmY9EKu",
    "domain": "AI",
    "title": "Cursor教程：实现自动化写文章，让AI 7*24小时为你打工｜ChatGPT｜AI进化论-花生",
    "url": "http://www.bilibili.com/video/av113328902905646",
    "source": "花叔v",
    "platform": "bilibili",
    "points": 135372,
    "published_at": "2024-10-18T14:35:55+00:00",
    "summary": "👏 欢迎加入我的知识星球「AI编程：从入门到精通」：https://t.zsxq.com/BFTPI\n🤖 OpenAI API充值入口：https://platform.openai.com/settings/organization/billing/overview\n\n这期视频主要是像你介绍如何使用Cursor写自动化脚本，实现让ChatGPT为你自动化写作的目的。以小红书读书博主为例，演示了使"
  },
  {
    "id": "bvid:BV1dpdZYBE9q",
    "domain": "AI",
    "title": "零代码让AI秒接海量MCP工具！最适合小白的MCP集合平台",
    "url": "http://www.bilibili.com/video/av114340703243255",
    "source": "AI研究室-帆哥",
    "platform": "bilibili",
    "points": 103383,
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
    "points": 92578,
    "published_at": "2026-09-10T13:47:24+00:00",
    "summary": "这套课程围绕「AI+网络安全」展开，从AI智能体基础入门，到WorkBuddy、Trae等主流Agent工具的实际应用，再到API-Key接入、Skill使用等核心能力，逐步进入AI漏洞挖掘、代码审计、CTF题目分析等安全实战场景。同时结合SRC漏洞挖掘、HVV护网、安全竞赛以及网络安全就业方向，帮助你系统了解AI在网络安全学习、开发与实战中的应用方式。适合网络安全初学者、安全从业者以及希望利用A"
  },
  {
    "id": "bvid:BV1VL3F6pE9K",
    "domain": "AI",
    "title": "0基础入门智能体agent测试：AI测试基础+AI智能体(Agent)测试从零入门全攻略，2026最新版！",
    "url": "http://www.bilibili.com/video/av116991151113881",
    "source": "黑马测试",
    "platform": "bilibili",
    "points": 91174,
    "published_at": "2026-07-27T09:19:37+00:00",
    "summary": "还在卷传统软件测试？2026年必学的AI智能体(Agent)测试来了！本期视频专为0基础小白打造，从软件测试基础讲起...若要本视频配套资源笔记可加up主企微（请看置顶留言最后一句话）。"
  },
  {
    "id": "bvid:BV1XnuGzfEp7",
    "domain": "AI",
    "title": "让你手中的AI好用10倍！5个好玩实用的MCP推荐，让你不只会用AI搜索",
    "url": "http://www.bilibili.com/video/av114835262018810",
    "source": "田同学Tino",
    "platform": "bilibili",
    "points": 77086,
    "published_at": "2025-07-12T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV143wwz6E8F",
    "domain": "AI",
    "title": "Claude code科研使用展示与思路分享（提速就靠Ai）",
    "url": "http://www.bilibili.com/video/av116211882920985",
    "source": "科研推土机",
    "platform": "bilibili",
    "points": 76617,
    "published_at": "2026-03-11T18:12:00+00:00",
    "summary": "本期给大家带来的是Claude在Vscode的科研应用演示与我最近的一些心得使用心得，科研速度嘎嘎提升。论文复现画图、数据分析就靠Claude code。这个课程也是科研推土机「系统管理文献课程2.0」学员催我更新的内容，希望能帮助到大家～，这个视频重点讲两个事情：\n1️⃣ 资料获取，free不用怀疑，我是良心可言博主，，关注我(GZTSHNR)～\n2️⃣ 展示如何在VS code实操应用clau"
  },
  {
    "id": "bvid:BV1renJ6VEuZ",
    "domain": "AI",
    "title": "DeepSeekHarness装进手机",
    "url": "http://www.bilibili.com/video/av117467271666305",
    "source": "文大师啵啵",
    "platform": "bilibili",
    "points": 68229,
    "published_at": "2026-10-19T11:14:25+00:00",
    "summary": "如果把 DeepSeek Harness 完整搬进 Android，手机会变成什么？\n\n它不是又一个聊天助手，而是一台随身 AI 工作站：有自己的工作区、Linux 环境、终端、文件管理系统、插件系统，也能通过无障碍或者 Shizuku 操作手机，并通过内置浏览器实现网页自动化。\n\n这个项目叫 DSHBox，让 DeepSeek Harness 运行在手机上。\n\n本视频展示从首页进入、选择工作区、"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 56412,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1Y6uC6TE1m",
    "domain": "AI",
    "title": "疯狂Vibe Coding一周，我烧了近100亿Token，做了5个项目！",
    "url": "http://www.bilibili.com/video/av117080321957877",
    "source": "神烦老狗",
    "platform": "bilibili",
    "points": 53548,
    "published_at": "2026-08-12T03:12:41+00:00",
    "summary": "项目地址：\nlocal-ops — 本地服务指挥台（零依赖 Python + 原生前端）：https://github.com/laogou717/local-ops\nmd-wechat — 公众号排版工具：https://github.com/laogou717/md-wechat\ndaydream-room — 白日梦陈列室：https://github.com/laogou717/daydr"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 49717,
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
    "points": 48777,
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
    "points": 47766,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1XiD5BQEAj",
    "domain": "AI",
    "title": "Claude Code 接入微信、一行命令把Claude Code装进微信、保姆级教程、微信支持Claude Code（cc-connect）远程开发",
    "url": "http://www.bilibili.com/video/av116350093694897",
    "source": "下班学AI",
    "platform": "bilibili",
    "points": 40954,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV1gwcAzkEhw",
    "domain": "AI",
    "title": "Claude Code Agent Teams上手指南+项目实测",
    "url": "http://www.bilibili.com/video/av116037064331269",
    "source": "程序员阿江-Relakkes",
    "platform": "bilibili",
    "points": 36030,
    "published_at": "2026-02-08T23:30:00+00:00",
    "summary": "用Claude Code干复杂任务总碰到三个问题：\n\n上下文越来越长开始遗忘、任务只能串行效率低、单Agent视角单一容易漏检。\n\nClaude官方发布的Agent Teams功能正好解决这些痛点\n\n一个Team Lead拆任务，多个Teammate并行执行，还能互相通信协调。\n\n本期视频从核心概念、使用场景、底层架构到真实项目实战，带你完整搞懂Agent Teams的正确打开方式。"
  },
  {
    "id": "bvid:BV1hmb26ZEws",
    "domain": "AI",
    "title": "DeepSeek Harness 实测  Claude Code 对比后，梁神我错了 差距比我想的大",
    "url": "http://www.bilibili.com/video/av117100337236191",
    "source": "程序员晓刘",
    "platform": "bilibili",
    "points": 33370,
    "published_at": "2026-08-15T16:01:38+00:00",
    "summary": "这期用同一个 DeepSeek Pro 0813 模型，分别在 Claude Code 和 DeepSeek Harness 里完成同样的任务，对比工具链对最终效果的影响。\n实测内容包括：\nFPS 游戏 Demo、灯塔预警沙盘、手枪组装动画、显示器组装动画，以及 DeepSeek Harness 的插件化源码流程。\n整体看下来，模型本身当然重要，但 Harness 在插件化、流程记录、缓存命中和任"
  },
  {
    "id": "bvid:BV1g5nM6tEBf",
    "domain": "AI",
    "title": "DeepSeek V4.1 Flash 接入指南｜六大 Agent 工具一次配好",
    "url": "http://www.bilibili.com/video/av117459403150912",
    "source": "跟着小陈玩AI",
    "platform": "bilibili",
    "points": 32292,
    "published_at": "2026-10-18T02:13:56+00:00",
    "summary": "DeepSeek 发布 V4.1 Flash，跑分反超一众旗舰。本期实测把它接进 DeepSeek Harness、WorkBuddy、Kimi Code、小米 MIMO、ZCode、Codex、Claude Code 等工具，两种配置方法、模型名怎么填、哪里要避坑，一条视频全部讲清。"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29874,
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
    "points": 29019,
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
    "points": 28529,
    "published_at": "2026-04-03T16:14:43+00:00",
    "summary": "每个参数都是干什么的，如何修改提示词的教程。\n不知道这是什么？请看合集内的视频~\n我做了一个 AI 的杀戮尖塔2MOD！\n可以和怪物对话，策反怪物，带着怪物爬塔（重写了几乎每一个怪物在友方时候的行为），还能给怪物打防御，带个沙虫全吃了！\n可以和上古之民对话，聊嗨了会给你 1～2 个额外赐福，还能帮你指示为未来\n可以让偷窃草蜢偷队友的 key 卡，想无限？偷了！\n可以和商人讨价还价，甚至白嫖\n多人的"
  },
  {
    "id": "bvid:BV1sQaL6vEkb",
    "domain": "AI",
    "title": "小白向，ai入门第一课：agent的部署和使用！",
    "url": "http://www.bilibili.com/video/av117349378166797",
    "source": "沈三殊",
    "platform": "bilibili",
    "points": 28229,
    "published_at": "2026-09-28T15:30:36+00:00",
    "summary": "详细的agent部署介绍：https://pan.quark.cn/s/3846914c6da7\n欢迎来到ai的世界！！\n有疑问欢迎私信。"
  },
  {
    "id": "bvid:BV17Lap6VEUr",
    "domain": "AI",
    "title": "【全80集】Vibe Coding 零基础入门到实战教程，由浅入深（全程干货）",
    "url": "http://www.bilibili.com/video/av117353572468721",
    "source": "数据拾光屋",
    "platform": "bilibili",
    "points": 28087,
    "published_at": "2026-10-02T09:25:00+00:00",
    "summary": "本套教程专门为零基础学员而制，全程干货无废话，喜欢的小伙伴记得点赞三连喔 ~"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 25555,
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
    "points": 24006,
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
    "points": 22827,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1xFJ26tEoG",
    "domain": "AI",
    "title": "AI产品经理作品集：Vibe Coding实操 ChatBI落地写进简历",
    "url": "http://www.bilibili.com/video/av117445360618053",
    "source": "AI产品经理PMGao",
    "platform": "bilibili",
    "points": 16752,
    "published_at": "2026-10-15T14:22:53+00:00",
    "summary": "有很多同学用过codex、claude code等就觉得有vibecoding经验了，很多同学其实站在一个使用AI的普通用户跟AI交流而已，还远远达不到作为AI产品经理的能力。所以这个实操案例系统化的讲解了企业级项目是如何通过vibecoding落地的详细步骤，这里面包括了产品规划+竞品分析+SDD开发规范+Harness+测试用例+测评+skill设计等等。\n\n这个实操结合企业级案例深度讲解，完"
  },
  {
    "id": "bvid:BV1yyQEBdEkm",
    "domain": "AI",
    "title": "【2026B站最全】Claude Code+软件测试实操教程!看完我直接删了收藏夹所有测试教程,从账号注册到Plan驱动测试项目,小白3天上手！",
    "url": "http://www.bilibili.com/video/av116408092525631",
    "source": "软件测试大神",
    "platform": "bilibili",
    "points": 15414,
    "published_at": "2026-04-15T09:55:02+00:00",
    "summary": "配套资料👉：https://b23.tv/qvhxmaQ\n包括:AI测试网站，几十个AI场景测试完整流程，skil文档，测试八股文，项目源码，测试用例模板，工具安装包，学习计划表，学习路线，100g测试新人资料包等等，资料百分百免费，放心领取~"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 13194,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
  },
  {
    "id": "bvid:BV12iHF6PEb7",
    "domain": "AI",
    "title": "【Living World】一个会回应你的 MC 服务器｜开发中概念演示",
    "url": "http://www.bilibili.com/video/av117510036789910",
    "source": "Seventick",
    "platform": "bilibili",
    "points": 11276,
    "published_at": "2026-10-27T00:34:44+00:00",
    "summary": "在大多数服务器，世界是一块背景板：怪刷了又刷，NPC 一百天说同一句话，你做了什么它都不会记得。\n\nTIMES 想做的是 Living World——一个会回应你的世界。\n村子缺铁，铁匠铺就熄火；你送去一车铁，炉火重新亮起，铁匠记住你的名字。\n北矿挖得太深，惊动了幽匿；守不住，矿口被封，镇上的炉火又灭了。\n全服一起夺回北矿，新矿道开通，你的名字刻在铁匠铺门口的木牌上。\n你下线以后，世界依然在运行；"
  },
  {
    "id": "bvid:BV1rhdgBMEK2",
    "domain": "AI",
    "title": "Claude Code + Figma MCP：传统 UI 开发流程已死？",
    "url": "http://www.bilibili.com/video/av116538183124050",
    "source": "犬哥网站",
    "platform": "bilibili",
    "points": 10749,
    "published_at": "2026-05-08T12:00:00+00:00",
    "summary": "▬▬▬▬▬ 🏆️ 犬哥专业服务 🏆️ ▬▬▬▬▬\n网页设计＆数位行销服务 ➜ https://frankknow.com\nWordPress 优质主机：https://frankknow.com/wordpress-hosting/\n\n▬▬▬▬▬ 🏆️ 精选架站系列 🏆️ ▬▬▬▬▬\n新手自学架站（网域＋主机＋WordPress 架站，一次学会）➜ https://frankknow.com/wp"
  },
  {
    "id": "hn:49970667",
    "domain": "AI 算力 / 半导体",
    "title": "Opus 5.5 agents discover two room-temperature magnetic semiconductor candidates",
    "url": "https://www.vals.ai/blogs/room-temperature-magnetic-semiconductors",
    "source": "outlier99",
    "platform": "hackernews",
    "points": 495,
    "published_at": "2026-10-05T21:00:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:50219700",
    "domain": "AI 算力 / 半导体",
    "title": "GPU-unlock: FP/BF16 instruction issue rate on Nvidia 3000's cards",
    "url": "https://github.com/Zagitta/gpu-unlock",
    "source": "fragebogen",
    "platform": "hackernews",
    "points": 349,
    "published_at": "2026-10-24T09:58:27+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/using-a-single-image-to-optimize-urban-solar-panel-orientation/",
    "domain": "AI 算力 / 半导体",
    "title": "Using a Single Image to Optimize Urban Solar-Panel Orientation",
    "url": "https://www.eetimes.com/using-a-single-image-to-optimize-urban-solar-panel-orientation/",
    "source": "Bill Schweber",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T22:00:00+00:00",
    "summary": "Getting the most power from an urban-sited panel requires deep understanding of its surroundings. The post Using a Single Image to Optimize Urban Solar-Panel Orientation appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/automakers-reconsider-in-cabin-sensing-for-euro-ncap-ratings/",
    "domain": "AI 算力 / 半导体",
    "title": "Automakers Reconsider In-Cabin Sensing for Euro NCAP Ratings",
    "url": "https://www.eetimes.com/automakers-reconsider-in-cabin-sensing-for-euro-ncap-ratings/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T17:00:11+00:00",
    "summary": "Stricter European safety assessment criteria are prompting car companies to replace steering-wheel sensors with consolidated in-cabin systems. The post Automakers Reconsider In-Cabin Sensing for Euro "
  },
  {
    "id": "rss:https://www.eetimes.com/framing-the-shift-to-48v/",
    "domain": "AI 算力 / 半导体",
    "title": "Framing the Shift to 48V",
    "url": "https://www.eetimes.com/framing-the-shift-to-48v/",
    "source": "Vasanth Sista, Field Application Engineer, TE Connectivity",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T13:00:00+00:00",
    "summary": "From lighter wiring to automated assembly, 48V architectures are reshaping vehicle connectivity and laying the groundwork for next generation mobility. The post Framing the Shift to 48V appeared first"
  },
  {
    "id": "rss:https://www.eetimes.com/the-ai-packaging-challenge-5-reasons-panels-are-gaining-momentum/",
    "domain": "AI 算力 / 半导体",
    "title": "The AI Packaging Challenge: 5 Reasons Panels Are Gaining Momentum",
    "url": "https://www.eetimes.com/the-ai-packaging-challenge-5-reasons-panels-are-gaining-momentum/",
    "source": "Aaron Fellis, corporate vice president and general manager, Wet Equipment Technology Systems, Lam Research",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T13:00:00+00:00",
    "summary": "As AI pushes chip packages beyond traditional wafer limits, panel-level processing is emerging as a critical path to scale advanced packaging. The post The AI Packaging Challenge: 5 Reasons Panels Are"
  },
  {
    "id": "rss:https://www.eetimes.com/in-orbit-useful-life-becomes-a-performance-metric/",
    "domain": "AI 算力 / 半导体",
    "title": "In Orbit, Useful Life Becomes a Performance Metric",
    "url": "https://www.eetimes.com/in-orbit-useful-life-becomes-a-performance-metric/",
    "source": "Ron Honig",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T08:25:36+00:00",
    "summary": "Google’s Project Suncatcher is testing AI hardware in space, where radiation, cooling, power, and hardware lifetime determine the economics of computing. The post In Orbit, Useful Life Becomes a Perfo"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-quietly-confirms-raptor-lake-next-cpus-through-internal-driver-publication-lga-1700-chips-also-appear-in-shipping-manifests-dating-back-to-august",
    "domain": "AI 算力 / 半导体",
    "title": "Intel quietly confirms Raptor Lake Next CPUs through internal driver publication",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-quietly-confirms-raptor-lake-next-cpus-through-internal-driver-publication-lga-1700-chips-also-appear-in-shipping-manifests-dating-back-to-august",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T18:50:28+00:00",
    "summary": "An internal driver and a shipping manifest reveal that Intel's desktop Raptor Lake Next parts may be on the way right now."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/portable-monitors/jsaux-flipgo-dual-screen-portable-monitor-review",
    "domain": "AI 算力 / 半导体",
    "title": "JSAUX FlipGo dual-screen portable monitor review: Gorgeous displays with touch support and a built-in USB hub",
    "url": "https://www.tomshardware.com/monitors/portable-monitors/jsaux-flipgo-dual-screen-portable-monitor-review",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T16:33:31+00:00",
    "summary": "The JSAUX FlipGo features dual 16-inch touch displays and a built-in hub."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/hdds/save-usd134-on-this-wd-red-plus-10tb-hdd-bundle-at-newegg-this-double-drive-deal-lands-you-with-20tb-of-total-capacity-for-your-nas",
    "domain": "AI 算力 / 半导体",
    "title": "Save $134 on this WD Red Plus 10TB HDD bundle at Newegg",
    "url": "https://www.tomshardware.com/pc-components/hdds/save-usd134-on-this-wd-red-plus-10tb-hdd-bundle-at-newegg-this-double-drive-deal-lands-you-with-20tb-of-total-capacity-for-your-nas",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T16:00:00+00:00",
    "summary": "Grab two 10TB NAS Hard Disk Drives and save $134 — this two-pack WD Red Plus bundle is the best deal for adding capacity to your NAS"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/handheld-gaming/asus-rog-xbox-ally-x20-tested-same-performance-more-comfortable-and-a-glorious-oled-screen",
    "domain": "AI 算力 / 半导体",
    "title": "Asus ROG Xbox Ally X20 tested: Same performance, more comfortable, and a glorious OLED screen",
    "url": "https://www.tomshardware.com/video-games/handheld-gaming/asus-rog-xbox-ally-x20-tested-same-performance-more-comfortable-and-a-glorious-oled-screen",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T15:00:00+00:00",
    "summary": "Asus adds an OLED screen, TMR sticks, and more comfortable grips to its AMD-powered gaming handheld."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/3-2-pb-s-real-time-optical-fiber-transfer-speed-world-record-claimed-by-chinese-team-speed-fast-enough-to-download-more-than-20-000-4k-movies-in-one-second",
    "domain": "AI 算力 / 半导体",
    "title": "3.2 Petabits per second real-time optical fiber transfer speed world record claimed by Chinese team",
    "url": "https://www.tomshardware.com/networking/3-2-pb-s-real-time-optical-fiber-transfer-speed-world-record-claimed-by-chinese-team-speed-fast-enough-to-download-more-than-20-000-4k-movies-in-one-second",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T14:43:37+00:00",
    "summary": "A Chinese team has claimed a new world record for real-time transfer speeds across a 24-core optical fiber cable."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/leaked-256-core-zen-6c-epyc-cpu-destroys-zen-5-in-early-single-threaded-benchmarks-hints-at-24-percent-ipc-gain-early-single-threaded-benchmarks-point-to-huge-amd-zen-6-improvements",
    "domain": "AI 算力 / 半导体",
    "title": "Leaked 256-core Zen 6c EPYC CPU destroys Zen 5 in early single-threaded benchmarks hints at 24% IPC gain",
    "url": "https://www.tomshardware.com/pc-components/cpus/leaked-256-core-zen-6c-epyc-cpu-destroys-zen-5-in-early-single-threaded-benchmarks-hints-at-24-percent-ipc-gain-early-single-threaded-benchmarks-point-to-huge-amd-zen-6-improvements",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T14:31:43+00:00",
    "summary": "A benchmark leak and a direct clock-matched comparison from an enthusiast seed the idea that Zen 6 may come with a decent IPC bump as well as increased clocks."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/micron-plans-to-use-wafer-bonding-and-high-na-euv-for-next-gen-dram-company-also-developing-vertical-high-bandwidth-memory-and-vertical-edge-inference-memory-integrated-directly-on-top-of-processors",
    "domain": "AI 算力 / 半导体",
    "title": "Micron plans to use wafer bonding and High-NA EUV for next-gen DRAM",
    "url": "https://www.tomshardware.com/pc-components/dram/micron-plans-to-use-wafer-bonding-and-high-na-euv-for-next-gen-dram-company-also-developing-vertical-high-bandwidth-memory-and-vertical-edge-inference-memory-integrated-directly-on-top-of-processors",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T14:00:00+00:00",
    "summary": "Micron rejects 4F2, intends to use wafer bonding and High-NA EUV before going 3D NAND over the next few years."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/windows-11s-whole-iso-squeezed-into-a-cd-rom-sub-700mb-disk-boots-to-the-desktop-runs-apps-just-like-the-microsoft-original",
    "domain": "AI 算力 / 半导体",
    "title": "Windows 11’s ‘whole ISO’ squeezed into a CD-ROM",
    "url": "https://www.tomshardware.com/software/windows/windows-11s-whole-iso-squeezed-into-a-cd-rom-sub-700mb-disk-boots-to-the-desktop-runs-apps-just-like-the-microsoft-original",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T13:40:00+00:00",
    "summary": "Professional Windows crusher NTDEV has showcased their next-generation tool for compressing Windows 11 with a video of an install that fits on a single CD-ROM."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/cadence-reveals-maestro-fine-tuned-ai-models-built-to-run-specialized-chip-design-agents-with-early-access-coming-for-select-customers-in-q4-2026-claims-up-to-30-percent-higher-quality-results-and-up-to-5x-token-efficiency-over-a-general-purpose-ai-model",
    "domain": "AI 算力 / 半导体",
    "title": "Cadence reveals Maestro, fine-tuned AI models built to run specialized chip design agents, with early access coming for 'select customers' in Q4 2026",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/cadence-reveals-maestro-fine-tuned-ai-models-built-to-run-specialized-chip-design-agents-with-early-access-coming-for-select-customers-in-q4-2026-claims-up-to-30-percent-higher-quality-results-and-up-to-5x-token-efficiency-over-a-general-purpose-ai-model",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T13:20:00+00:00",
    "summary": "Cadence unveiled Maestro, domain-specialized AI models for its chip design agents, with early access for select customers in Q4 2026."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/chinese-research-vessels-loiter-near-pacific-undersea-cables-more-than-any-other-nation-report-finds-civilian-fleet-using-lawnmower-patterns-may-be-mapping-seafloor-for-future-sabotage",
    "domain": "AI 算力 / 半导体",
    "title": "Chinese research vessels loiter near Pacific undersea cables more than any other nation, report finds",
    "url": "https://www.tomshardware.com/tech-industry/chinese-research-vessels-loiter-near-pacific-undersea-cables-more-than-any-other-nation-report-finds-civilian-fleet-using-lawnmower-patterns-may-be-mapping-seafloor-for-future-sabotage",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T13:00:00+00:00",
    "summary": "Chinese vessels are spending more time near undersea cables in the Pacific than nearly 50 other nations, according to a new report by the Center for Strategic and International Studies."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/intel-explores-potential-collaboration-with-amd-as-lip-bu-tan-pushes-customer-focused-turnaround-ceo-targets-custom-chips-advanced-packaging-and-stronger-foundry-business",
    "domain": "AI 算力 / 半导体",
    "title": "Intel's Lip-Bu Tan has spoken with Lisa Su about potential collaboration with AMD",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/intel-explores-potential-collaboration-with-amd-as-lip-bu-tan-pushes-customer-focused-turnaround-ceo-targets-custom-chips-advanced-packaging-and-stronger-foundry-business",
    "source": "Newton Gitonga",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T12:40:00+00:00",
    "summary": "Intel CEO Lip-Bu Tan has reportedly discussed potential areas of cooperation with AMD chief Lisa Su as Intel works to rebuild its CPU business and expand its foundry operations. The companies have alr"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-over-usd1-000-on-this-alienware-gaming-pc-with-an-rtx-5070-and-32gb-ddr5-unlock-1440p-and-4k-gameplay-with-this-aurora-act1250-rig-with-a-20-core-intel-cpu-and-a-1tb-ssd-for-usd2-199-99",
    "domain": "AI 算力 / 半导体",
    "title": "Save over $1,000 on this Alienware gaming PC with an RTX 5070 and 32GB DDR5",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-over-usd1-000-on-this-alienware-gaming-pc-with-an-rtx-5070-and-32gb-ddr5-unlock-1440p-and-4k-gameplay-with-this-aurora-act1250-rig-with-a-20-core-intel-cpu-and-a-1tb-ssd-for-usd2-199-99",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T12:20:00+00:00",
    "summary": "Newegg have cut this Alienware Aurora gaming PC by over $1,000, netting yo ua 4K-ready machine with an RTX 5070 and 32GB of DDR5 RAM for $2,199.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/lack-of-funding-likely-led-to-the-recent-php-security-snafu-but-thats-just-the-tip-of-the-iceberg-a-dreary-situation-caused-by-services-running-old-versions-with-no-support",
    "domain": "AI 算力 / 半导体",
    "title": "Lack of staff and funding likely led to the recent PHP security snafu; project has only one full-time employee, but that's just the tip of the iceberg",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/lack-of-funding-likely-led-to-the-recent-php-security-snafu-but-thats-just-the-tip-of-the-iceberg-a-dreary-situation-caused-by-services-running-old-versions-with-no-support",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T11:50:00+00:00",
    "summary": "Lack of funding likely led to the recent PHP security snafu, but that's just the tip of the iceberg — dreary situation caused by services running old versions with no support"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/modder-turns-nes-into-a-windows-like-desktop-with-original-hardware-emulates-a-full-retro-experience-with-a-cd-drive-and-slow-internet",
    "domain": "AI 算力 / 半导体",
    "title": "Modder turns NES into a Windows-like desktop with original hardware",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/modder-turns-nes-into-a-windows-like-desktop-with-original-hardware-emulates-a-full-retro-experience-with-a-cd-drive-and-slow-internet",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T11:20:00+00:00",
    "summary": "Throaty Mumbo turns his NES into a Windows-like desktop using an FPGA cartridge emulating an old Intel CPU, complete with a CD drive and internet capabilities, all without tearing the NES apart."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-20-30-and-40-series-gpus-hacked-to-remove-a-half-speed-ai-throttle-firmware-exploit-doubles-rtx-4090s-peak-tensor-rate-lifts-rtx-3090-ti-matrix-math-up-to-80-percent",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia RTX 20, 30, and 40-series GPUs hacked to remove a half-speed AI throttle",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-20-30-and-40-series-gpus-hacked-to-remove-a-half-speed-ai-throttle-firmware-exploit-doubles-rtx-4090s-peak-tensor-rate-lifts-rtx-3090-ti-matrix-math-up-to-80-percent",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T11:00:00+00:00",
    "summary": "Linux kernel modules lift Nvidia’s half-rate AI tensor limit on GeForce RTX 20, 30, and 40-series GPUs."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cryptomining/hacker-offers-bitcoin-reward-to-anyone-who-can-break-into-an-unpatched-server-running-php-still-remains-unhacked-php2shell-challenge-tests-claims-that-ai-makes-exploiting-vulnerabilities-easy",
    "domain": "AI 算力 / 半导体",
    "title": "Bitcoin reward offered to anyone who could break into an unpatched server running PHP, hacker cracks site and claims bounty",
    "url": "https://www.tomshardware.com/tech-industry/cryptomining/hacker-offers-bitcoin-reward-to-anyone-who-can-break-into-an-unpatched-server-running-php-still-remains-unhacked-php2shell-challenge-tests-claims-that-ai-makes-exploiting-vulnerabilities-easy",
    "source": "Newton Gitonga",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T10:30:00+00:00",
    "summary": "The “Steal My Bitcoin” challenge offers a bounty to anyone who can breach a deliberately vulnerable PHP website using the recently disclosed PHP2Shell flaws. The challenge follows previous recoveries "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/reddits-r-opensource-bans-ai-made-and-ai-focused-projects-also-bans-non-english-speakers-sweeping-new-rules-spark-backlash-over-linux-kernel-contributions-and-solo-developers",
    "domain": "AI 算力 / 半导体",
    "title": "Reddit’s r/opensource bans AI-made and AI-focused projects, also bans non-English speakers",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/reddits-r-opensource-bans-ai-made-and-ai-focused-projects-also-bans-non-english-speakers-sweeping-new-rules-spark-backlash-over-linux-kernel-contributions-and-solo-developers",
    "source": "Newton Gitonga",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T10:00:00+00:00",
    "summary": "Reddit’s r/opensource has barred AI-built, AI-focused, and AI-using projects under new rules announced October 24. The crackdown also imposes strict requirements on project age and contributors, while"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/microsoft-office/denmarks-bid-to-ditch-microsoft-office-for-open-source-alternative-collabora-collapses-in-under-six-months-employees-cite-issues-with-style-formatting-and-tracking-changes",
    "domain": "AI 算力 / 半导体",
    "title": "Denmark’s bid to ditch Microsoft Office for open-source alternative Collabora collapses in under six months",
    "url": "https://www.tomshardware.com/software/microsoft-office/denmarks-bid-to-ditch-microsoft-office-for-open-source-alternative-collabora-collapses-in-under-six-months-employees-cite-issues-with-style-formatting-and-tracking-changes",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T09:30:00+00:00",
    "summary": "The Danish digitization ministry experimented with Collabora as an alternative to Microsoft Office, but employees who used them were frequently frustrated with style and paragraph formatting challenge"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/big-tech-is-cashing-in-on-ai-while-the-rest-of-corporate-america-sees-no-financial-returns-report-outlines-how-rising-token-costs-threaten-to-squeeze-corporate-profit-margins",
    "domain": "AI 算力 / 半导体",
    "title": "Big Tech is cashing in on AI while the rest of corporate America sees no financial returns",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/big-tech-is-cashing-in-on-ai-while-the-rest-of-corporate-america-sees-no-financial-returns-report-outlines-how-rising-token-costs-threaten-to-squeeze-corporate-profit-margins",
    "source": "Newton Gitonga",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-25T15:25:40+00:00",
    "summary": "Revenue per employee at the Magnificent Seven has outpaced the S&amp;P 493, and a new comparison highlights the growing divide in fortunes between America’s largest technology companies and the rest o"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/mechanical-keyboards/iqunix-mq80-low-profile-mechanical-keyboard-review",
    "domain": "AI 算力 / 半导体",
    "title": "IQUNIX MQ80 low profile mechanical keyboard review",
    "url": "https://www.tomshardware.com/peripherals/mechanical-keyboards/iqunix-mq80-low-profile-mechanical-keyboard-review",
    "source": "Christopher Coke",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-25T15:08:23+00:00",
    "summary": "The IQUNIX MQ80 is well-made and super stylish, but it’s not quite the instant sell it used to be. Catch this one if you don’t like magnetic switches, but otherwise wait for a sale."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/ukrainian-drone-attacks-hammer-russias-finance-ministry-data-center-damaged-facility-reportedly-holds-tax-databases-facility-also-holds-other-important-state-registry-data",
    "domain": "AI 算力 / 半导体",
    "title": "Ukrainian drone attacks hammer Russia's finance ministry data center, damaged facility reportedly holds tax databases",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/ukrainian-drone-attacks-hammer-russias-finance-ministry-data-center-damaged-facility-reportedly-holds-tax-databases-facility-also-holds-other-important-state-registry-data",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-25T14:05:00+00:00",
    "summary": "Reports say that this is one of three data centers that the Russian finance ministry operated."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/samsungs-new-2tb-990-ssd-is-38-percent-off-at-amazon-today-get-usd200-off-this-pcie-4-0-all-rounder-drive-for-a-limited-time",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung's new 2TB 990 SSD is 38% off at Amazon today",
    "url": "https://www.tomshardware.com/pc-components/ssds/samsungs-new-2tb-990-ssd-is-38-percent-off-at-amazon-today-get-usd200-off-this-pcie-4-0-all-rounder-drive-for-a-limited-time",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-25T13:43:37+00:00",
    "summary": "Get 38% off the new Samsung 990 2TB SSD, a $200 saving."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/jailbroken-ps5s-can-now-run-steam-pc-games-you-can-now-sign-in-with-your-steam-account-and-install-games-from-your-library-directly-to-the-console",
    "domain": "AI 算力 / 半导体",
    "title": "Jailbroken PS5s can now run Steam PC games",
    "url": "https://www.tomshardware.com/video-games/playstation/jailbroken-ps5s-can-now-run-steam-pc-games-you-can-now-sign-in-with-your-steam-account-and-install-games-from-your-library-directly-to-the-console",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-25T12:40:11+00:00",
    "summary": "Playden for PS5 creates an app for each Steam game that it downloads, allowing it to appear as a separate tile on the console's home screen."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/windows-xp-debuted-25-years-ago-today-microsofts-biggest-launch-since-95-was-its-first-consumer-os-to-remove-the-dos-underpinnings",
    "domain": "AI 算力 / 半导体",
    "title": "Windows XP debuted 25 years ago today",
    "url": "https://www.tomshardware.com/software/windows/windows-xp-debuted-25-years-ago-today-microsofts-biggest-launch-since-95-was-its-first-consumer-os-to-remove-the-dos-underpinnings",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-25T12:20:00+00:00",
    "summary": "Windows XP became available at retailers for the first time on this day back in 2001."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/new-cd-players-keep-launching-but-a-drive-shortage-could-make-them-unfixable-almost-nobody-makes-the-drives-anymore",
    "domain": "AI 算力 / 半导体",
    "title": "New CD players keep launching, but a drive shortage could make them unfixable",
    "url": "https://www.tomshardware.com/peripherals/new-cd-players-keep-launching-but-a-drive-shortage-could-make-them-unfixable-almost-nobody-makes-the-drives-anymore",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-25T12:00:00+00:00",
    "summary": "The lack of optical drive manufacturers is raising questions about the repairability and longevity of new CD players that are coming out on the market today."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/openais-isolated-red-team-ai-agents-built-a-hidden-cpu-cache-channel-to-talk-with-no-network-or-shared-files-exploited-cpu-cache-timing-to-bypass-microvm-sandboxes",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI's isolated red-team agents built a hidden CPU cache channel to talk with no network or shared files",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/openais-isolated-red-team-ai-agents-built-a-hidden-cpu-cache-channel-to-talk-with-no-network-or-shared-files-exploited-cpu-cache-timing-to-bypass-microvm-sandboxes",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-25T11:30:00+00:00",
    "summary": "OpenAI’s red-team agents passed hidden messages through the CPU cache, a covert trick already shown to move data between cloud VMs."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-ceo-lisa-su-proposed-bringing-back-the-ryzen-7-5800x3d-set-plan-in-motion-before-ddr5-shortages-am4-cpu-considered-a-final-gift-to-loyal-fans-of-the-decade-old-socket",
    "domain": "AI 算力 / 半导体",
    "title": "AMD CEO Lisa Su proposed bringing back the Ryzen 7 5800X3D, set plan in motion before DDR5 shortages",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-ceo-lisa-su-proposed-bringing-back-the-ryzen-7-5800x3d-set-plan-in-motion-before-ddr5-shortages-am4-cpu-considered-a-final-gift-to-loyal-fans-of-the-decade-old-socket",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-25T11:00:00+00:00",
    "summary": "AMD Director Travis Kirsch confirmed the rationale for relaunching the first X3D chip and explained why the company no longer offers many Ryzen 3 SKUs."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/nvidia-eyes-converting-old-nuclear-plants-into-massive-ai-data-centers-reusing-shut-down-german-energy-sites-could-reduce-the-cost-and-timeline-of-building-from-scratch",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia eyes converting old nuclear plants into massive AI data centers",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/nvidia-eyes-converting-old-nuclear-plants-into-massive-ai-data-centers-reusing-shut-down-german-energy-sites-could-reduce-the-cost-and-timeline-of-building-from-scratch",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-25T10:30:00+00:00",
    "summary": "Nvidia and PreussenElektra are studying whether decommissioned sites of German nuclear power plants can be repurposed as AI data centers, potentially cutting development time by reusing existing grid "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/hacker-finds-own-samsung-tv-collecting-scary-amounts-of-user-information-and-gets-banned-by-openai-for-cyber-abuse-tv-runs-an-ai-model-that-collects-audio-screenshots-and-plenty-of-other-user-data-for-ad-targeting",
    "domain": "AI 算力 / 半导体",
    "title": "Cybersecurity bounty hunter says Samsung TVs use AI to record audio and screenshots for ads",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/hacker-finds-own-samsung-tv-collecting-scary-amounts-of-user-information-and-gets-banned-by-openai-for-cyber-abuse-tv-runs-an-ai-model-that-collects-audio-screenshots-and-plenty-of-other-user-data-for-ad-targeting",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-25T10:00:00+00:00",
    "summary": "A hacker reverse-engineered his own Samsung TV and found alarming spying activity, including code that used connected devices' microphones to listen to users."
  },
  {
    "id": "hn:50086363",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's first GPU: GeForce 256",
    "url": "https://dfarq.homeip.net/nvidias-first-gpu-geforce-256/",
    "source": "ibobev",
    "platform": "hackernews",
    "points": 79,
    "published_at": "2026-10-14T12:05:44+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/arm-comments-on-jury-decision-in-qualcomm-trial/",
    "domain": "AI 算力 / 半导体",
    "title": "Arm Comments on Jury Decision in Qualcomm Trial",
    "url": "https://www.eetimes.com/arm-comments-on-jury-decision-in-qualcomm-trial/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-24T00:00:00+00:00",
    "summary": "Arm's Ami Badani cites the $2 nominal damages award as validation, while chip design experts point to open architectures such as RISC-V as the long-term alternative for AI workload flexibility. The po"
  },
  {
    "id": "rss:https://www.eetimes.com/two-dollars-and-a-test-suite/",
    "domain": "AI 算力 / 半导体",
    "title": "Two Dollars and a Test Suite",
    "url": "https://www.eetimes.com/two-dollars-and-a-test-suite/",
    "source": "Moshe Zalcberg",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T08:03:27+00:00",
    "summary": "The $2 damages award grabbed headlines, but the Arm-Qualcomm verdict’s bigger implication concerns who controls the compliance tests that custom chips must pass before shipping. The post Two Dollars a"
  },
  {
    "id": "rss:https://www.eetimes.com/from-cloud-ai-to-edge-ai-how-biwin-enables-the-next-generation-of-storage-and-memory-solutions/",
    "domain": "AI 算力 / 半导体",
    "title": "From Cloud AI to Edge AI: How BIWIN Enables the Next Generation of Storage and Memory Solutions",
    "url": "https://www.eetimes.com/from-cloud-ai-to-edge-ai-how-biwin-enables-the-next-generation-of-storage-and-memory-solutions/",
    "source": "EE Times",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T18:24:39+00:00",
    "summary": "See how BIWIN’s SSD, embedded storage, and memory portfolio supports faster, efficient AI from cloud data centers to edge wearables. The post From Cloud AI to Edge AI: How BIWIN Enables the Next Gener"
  },
  {
    "id": "rss:https://www.eetimes.com/deepx-building-open-software-ecosystem-to-scale-physical-ai-beyond-the-data-center/",
    "domain": "AI 算力 / 半导体",
    "title": "Deepx Building Open Software Ecosystem to Scale Physical AI Beyond the Data Center",
    "url": "https://www.eetimes.com/deepx-building-open-software-ecosystem-to-scale-physical-ai-beyond-the-data-center/",
    "source": "Stephen Las Marias",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T18:14:49+00:00",
    "summary": "Deepx is combining low-power AI accelerators and portable software with industry partnerships to bring physical AI into production. The post Deepx Building Open Software Ecosystem to Scale Physical AI"
  },
  {
    "id": "rss:https://www.eetimes.com/how-goodram-validates-dram-and-ssd-reliability-in-europe/",
    "domain": "AI 算力 / 半导体",
    "title": "How Goodram Validates DRAM and SSD Reliability in Europe",
    "url": "https://www.eetimes.com/how-goodram-validates-dram-and-ssd-reliability-in-europe/",
    "source": "GOODRAM",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T13:00:00+00:00",
    "summary": "Explore Goodram’s European approach to DRAM and SSD testing, from burn-in to platform validation, for reliable industrial and embedded systems. The post How Goodram Validates DRAM and SSD Reliability "
  },
  {
    "id": "hn:50081435",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Reportedly Ending the RTX 5090, Reserves GB202 for Workstation GPUs",
    "url": "https://www.techpowerup.com/353578/nvidia-reportedly-ending-the-rtx-5090-reserves-gb202-silicon-for-workstation-gpus",
    "source": "kristianp",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-10-14T01:52:56+00:00",
    "summary": ""
  },
  {
    "id": "hn:50110301",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia, Apple, Google, Microsoft, Amazon, Meta gave Trump $92M for his ballroom",
    "url": "https://www.theverge.com/policy/1012047/nvidia-apple-google-microsoft-amazon-meta-trump-ballroom",
    "source": "jacquesm",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-10-15T21:11:05+00:00",
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
    "id": "rss:https://semianalysis.com/2025/09/16/xais-colossus-2-first-gigawatt-datacenter/",
    "domain": "AI 算力 / 半导体",
    "title": "xAI’s Colossus 2 – First Gigawatt Datacenter In The World, Unique RL Methodology, Capital Raise",
    "url": "https://semianalysis.com/2025/09/16/xais-colossus-2-first-gigawatt-datacenter/",
    "source": "Jeremie Eliahou Ontiveros",
    "platform": "rss",
    "points": null,
    "published_at": "2025-09-16T17:38:01+00:00",
    "summary": "Much has been written about xAI’s Colossus 1. The Memphis build belongs in the history books: the largest AI training cluster, erected from scratch in 122 days. With roughly 200,000 H100/H200s and ~30"
  },
  {
    "id": "rss:https://semianalysis.com/2025/09/10/another-giant-leap-the-rubin-cpx-specialized-accelerator-rack/",
    "domain": "AI 算力 / 半导体",
    "title": "Another Giant Leap: The Rubin CPX Specialized Accelerator & Rack",
    "url": "https://semianalysis.com/2025/09/10/another-giant-leap-the-rubin-cpx-specialized-accelerator-rack/",
    "source": "Dylan Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2025-09-10T19:57:18+00:00",
    "summary": "Nvidia announced the Rubin CPX, a solution that is specifically designed to be optimized for the prefill phase, with the single-die Rubin CPX heavily emphasizing compute FLOPS over memory bandwidth. T"
  },
  {
    "id": "rss:https://semianalysis.com/2025/09/08/huawei-ascend-production-ramp/",
    "domain": "AI 算力 / 半导体",
    "title": "Huawei Ascend Production Ramp: Die Banks, TSMC Continued Production, HBM is The Bottleneck",
    "url": "https://semianalysis.com/2025/09/08/huawei-ascend-production-ramp/",
    "source": "Dylan Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2025-09-08T09:54:57+00:00",
    "summary": "Compute is the lifeblood of AI. He who controls the spice controls the universe the compute will control the production of tokens and reap the benefits of AI. Without compute you do not have a seat at"
  },
  {
    "id": "rss:https://semianalysis.com/2025/09/03/amazons-ai-resurgence-aws-anthropics-multi-gigawatt-trainium-expansion/",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon’s AI Resurgence: AWS & Anthropic’s Multi-Gigawatt Trainium Expansion",
    "url": "https://semianalysis.com/2025/09/03/amazons-ai-resurgence-aws-anthropics-multi-gigawatt-trainium-expansion/",
    "source": "Jeremie Eliahou Ontiveros",
    "platform": "rss",
    "points": null,
    "published_at": "2025-09-03T20:55:46+00:00",
    "summary": "Two-and-a-half years ago, we flagged a looming “cloud crisis” at AWS. Today, the evidence has mounted. AWS is the crown jewel of the Amazon empire, generating ~60% of group profits, and dominating the"
  },
  {
    "id": "rss:https://semianalysis.com/2025/08/20/h100-vs-gb200-nvl72-training-benchmarks/",
    "domain": "AI 算力 / 半导体",
    "title": "H100 vs GB200 NVL72 Training Benchmarks – Power, TCO, and Reliability Analysis, Software Improvement Over Time",
    "url": "https://semianalysis.com/2025/08/20/h100-vs-gb200-nvl72-training-benchmarks/",
    "source": "Dylan Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2025-08-20T04:56:35+00:00",
    "summary": "Frontier model training has pushed GPUs and AI systems to their absolute limits, making cost, efficiency, power, performance per TCO, and reliability central to the discussion on effective training. T"
  },
  {
    "id": "hn:49913571",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/",
    "source": "bradleyg223",
    "platform": "hackernews",
    "points": 1705,
    "published_at": "2026-09-30T20:04:37+00:00",
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
    "id": "hn:49957116",
    "domain": "大厂 AI 动态",
    "title": "Turn off Apple Intelligence on macOS 27 and get its disk space back",
    "url": "https://github.com/omlahore/RemoveMacAI",
    "source": "privacyisntdead",
    "platform": "hackernews",
    "points": 775,
    "published_at": "2026-10-04T19:42:25+00:00",
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
    "id": "hn:49914236",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon (High): Intelligence, Performance and Price Analysis",
    "url": "https://artificialanalysis.ai/models/gemini-4-argon",
    "source": "theanonymousone",
    "platform": "hackernews",
    "points": 113,
    "published_at": "2026-09-30T20:50:28+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1019143/openai-eth-kaseya-science-math-physics",
    "domain": "大厂 AI 动态",
    "title": "OpenAI announces three big science discoveries and a new way to work with academics",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1019143/openai-eth-kaseya-science-math-physics",
    "source": "Richard Lawler",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T23:34:58+00:00",
    "summary": "Less than a month after its mass release of hundreds of manuscripts that it said contained solutions to long-standing mathematics questions, OpenAI is back with three more \"major\" discoveries in math,"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1018962/samsung-p9-256gb-microsd-express-card-switch-2-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Samsung’s Switch 2-ready MicroSD Express card is on sale for less than $50",
    "url": "https://www.theverge.com/gadgets/1018962/samsung-p9-256gb-microsd-express-card-switch-2-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T21:56:36+00:00",
    "summary": "Running out of space on your Nintendo Switch 2? Thankfully, Samsung’s P9 MicroSD Express card is discounted at multiple retailers, with the 256GB version going for $47.99 (Amazon, B&#38;H Photo) and t"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1018994/anthropic-ipo-ai-data-center-energy-climate-risk",
    "domain": "大厂 AI 动态",
    "title": "Anthropic is burning gas to feed the AI boom",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1018994/anthropic-ipo-ai-data-center-energy-climate-risk",
    "source": "Justine Calma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T21:45:31+00:00",
    "summary": "As it prepares to go public, Anthropic's S-1 filing makes generative AI's methane dependency glaringly obvious. \"Competition for access to electrical supply and data center locations with adequate pow"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1018827/ios-27-2-iphone-duo-apple-pencil",
    "domain": "大厂 AI 动态",
    "title": "iPhone Duo now supports Apple Pencil with iOS 27.2",
    "url": "https://www.theverge.com/tech/1018827/ios-27-2-iphone-duo-apple-pencil",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T18:51:06+00:00",
    "summary": "Apple has just released iOS 27.2, bringing Apple Pencil support to the iPhone Duo. The software update also includes an \"Edge Light\" feature for the iPhone Duo that's intended to illuminate your face "
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/1018818/nba-kalshi-polymarket",
    "domain": "大厂 AI 动态",
    "title": "The NBA’s response to gambling scandals is to add more gambling partnerships",
    "url": "https://www.theverge.com/entertainment/1018818/nba-kalshi-polymarket",
    "source": "Richard Lawler",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T18:22:06+00:00",
    "summary": "From the bright minds that brought you FTX Arena and NBA Top Shot NFT maketplace (where sales last month dropped to $762,781, which is a 99.66 percent decrease compared to the February 2021 peak of $2"
  },
  {
    "id": "rss:https://www.theverge.com/news/1018713/meta-muse-agentic-shopping-ai-the-realreal",
    "domain": "大厂 AI 动态",
    "title": "The RealReal won’t let AI agents hog designer clothing",
    "url": "https://www.theverge.com/news/1018713/meta-muse-agentic-shopping-ai-the-realreal",
    "source": "Mia Sato",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T17:30:55+00:00",
    "summary": "The RealReal, a secondhand luxury fashion consignment retailer, said it's updating its bot defense system, effectively making it harder for AI agents to shop on its site. The change comes days after T"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1018760/iphone-duo-crackgate-inside-screen-hinge-crack",
    "domain": "大厂 AI 动态",
    "title": "Apple acknowledges iPhone Duo display &#8216;issue&#8217; after reports of cracked screens",
    "url": "https://www.theverge.com/tech/1018760/iphone-duo-crackgate-inside-screen-hinge-crack",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T17:28:07+00:00",
    "summary": "Following reports of iPhone Duos with cracked and broken inside screens, often showing a bright line running from the center to the right side, Apple says in a statement to Bloomberg and 9to5Mac that "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1018612/nothing-ear-3a-noise-canceling-earbuds-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Nothing&#8217;s eye-catching Ear 3A earbuds are matching their best price to date",
    "url": "https://www.theverge.com/gadgets/1018612/nothing-ear-3a-noise-canceling-earbuds-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T17:25:34+00:00",
    "summary": "If you want a decent pair of noise-canceling earbuds without spending a fortune, Nothing’s Ear 3A are worth considering. The wireless earbuds offer a lot of features for the price, and they’re an even"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1018738/anthropic-ipo-s1-filing-weird-details",
    "domain": "大厂 AI 动态",
    "title": "Five weird details from Anthropic’s IPO filing",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1018738/anthropic-ipo-s1-filing-weird-details",
    "source": "Robert Hart",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T17:10:23+00:00",
    "summary": "Anthropic has finally filed its S-1 prospectus with the SEC, a document designed to give investors a look under the hood of its business, from how much its executives are making and plans for spending"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1018621/fitbit-edge-review-fitness-tracker-wearables-health",
    "domain": "大厂 AI 动态",
    "title": "Everything old is new again with the Fitbit Edge",
    "url": "https://www.theverge.com/tech/1018621/fitbit-edge-review-fitness-tracker-wearables-health",
    "source": "Victoria Song",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T17:00:00+00:00",
    "summary": "Last week, I sank into my living room couch and watched a bedraggled, nihilistic Matthew McConaughey take a drag of a cigarette in season 1 of True Detective. \"You know, someone once told me time is a"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/26/x-is-nudging-users-to-promote-their-posts-with-a-pointing-hand-and-people-are-confused/",
    "domain": "大厂 AI 动态",
    "title": "X is nudging users to promote their posts with a pointing hand, and people are confused",
    "url": "https://techcrunch.com/2026/10/26/x-is-nudging-users-to-promote-their-posts-with-a-pointing-hand-and-people-are-confused/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T06:34:44+00:00",
    "summary": "Whose hand is behind this travesty?"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/26/how-openai-turned-its-coding-tools-into-dots-an-always-on-personal-assistant/",
    "domain": "大厂 AI 动态",
    "title": "How OpenAI turned its coding tools into dots, an always-on personal assistant",
    "url": "https://techcrunch.com/2026/10/26/how-openai-turned-its-coding-tools-into-dots-an-always-on-personal-assistant/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T02:00:00+00:00",
    "summary": "Alexander Embiricos, the OpenAI executive responsible for dots, never wants to have a meeting with someone else's AI agent."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/26/cohere-says-alibabas-qwen-model-tried-to-send-a-file-to-beijing/",
    "domain": "大厂 AI 动态",
    "title": "Cohere says Alibaba’s Qwen model tried to send a file to Beijing",
    "url": "https://techcrunch.com/2026/10/26/cohere-says-alibabas-qwen-model-tried-to-send-a-file-to-beijing/",
    "source": "Aditya Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T01:12:21+00:00",
    "summary": "An AI model said it wouldn’t use any tools, then tried to send something to a server in Beijing anyway, and while researchers say it’s probably a training quirk and not espionage, the whole thing has "
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/26/databricks-co-founder-shares-his-secrets-for-winning-big-enterprises-customers/",
    "domain": "大厂 AI 动态",
    "title": "Databricks co-founder shares his secrets for winning big enterprise customers",
    "url": "https://techcrunch.com/2026/10/26/databricks-co-founder-shares-his-secrets-for-winning-big-enterprises-customers/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T22:00:00+00:00",
    "summary": "Turns out selling to big companies isn’t about having the shiniest tech: It’s about hitching a ride on a giant’s sales team."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/26/watch-out-youtube-instagram-goes-from-short-form-to-90-minute-videos/",
    "domain": "大厂 AI 动态",
    "title": "Watch out, YouTube — Instagram goes from short-form to 90-minute videos",
    "url": "https://techcrunch.com/2026/10/26/watch-out-youtube-instagram-goes-from-short-form-to-90-minute-videos/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T21:05:11+00:00",
    "summary": "After years in which every social platform (even LinkedIn!) aggressively pursued short-form video, this is a notable shift in strategy for Instagram."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/26/uh-oh-it-sounds-like-the-iphone-duo-keeps-cracking-and-users-arent-happy-about-it/",
    "domain": "大厂 AI 动态",
    "title": "Uh-oh, it sounds like the iPhone Duo keeps cracking and users aren’t happy about it",
    "url": "https://techcrunch.com/2026/10/26/uh-oh-it-sounds-like-the-iphone-duo-keeps-cracking-and-users-arent-happy-about-it/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T19:22:40+00:00",
    "summary": "A small number of early adopters of the much-hyped new foldable phone from Apple have complained of screens cracking."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/26/fusion-startups-are-giving-the-government-shares-in-exchange-for-awards-is-it-worth-it/",
    "domain": "大厂 AI 动态",
    "title": "Fusion startups are giving the government shares in exchange for awards. Is it worth it?",
    "url": "https://techcrunch.com/2026/10/26/fusion-startups-are-giving-the-government-shares-in-exchange-for-awards-is-it-worth-it/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T18:59:52+00:00",
    "summary": "Fusion startups face a new challenge, one unrelated to plasma physics: Give the government shares in exchange for funding awards or go it alone?"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/26/this-startups-self-driving-excavators-help-dig-up-600m-in-new-funding/",
    "domain": "大厂 AI 动态",
    "title": "This startup’s self-driving excavators help dig up $600M in new funding",
    "url": "https://techcrunch.com/2026/10/26/this-startups-self-driving-excavators-help-dig-up-600m-in-new-funding/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T17:45:00+00:00",
    "summary": "Bedrock Robotics, which is now valued at $4.1 billion, is particularly focused on autonomous excavators, in part because of a growing shortage of skilled operators."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/26/anthropics-ipo-filing-reveals-its-strategy-for-keeping-enterprise-customers-hooked/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic’s IPO filing reveals its strategy for keeping enterprise customers hooked",
    "url": "https://techcrunch.com/2026/10/26/anthropics-ipo-filing-reveals-its-strategy-for-keeping-enterprise-customers-hooked/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T16:49:42+00:00",
    "summary": "Anthropic’s S-1 shows more than half of its $100,000-plus customers now use both the Claude Platform and a first-party app, a cross-selling playbook reminiscent of Amazon that’s making enterprise cust"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/26/spacex-locks-in-40b-gpu-financing-deal-with-apollo/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX locks in $40B GPU financing deal with Apollo",
    "url": "https://techcrunch.com/2026/10/26/spacex-locks-in-40b-gpu-financing-deal-with-apollo/",
    "source": "Aditya Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T16:46:36+00:00",
    "summary": "The financing gives SpaceX another way to fund its rapidly expanding AI ambitions without relying solely on traditional debt markets."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/26/microsoft-offers-buyouts-to-around-60000-employees-reports-say/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft offers buyouts to around 60,000 employees",
    "url": "https://techcrunch.com/2026/10/26/microsoft-offers-buyouts-to-around-60000-employees-reports-say/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T15:58:25+00:00",
    "summary": "The buyout offers mark Microsoft's latest efforts to cut costs and rework its workforce."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/26/anthropic-officially-files-for-its-public-debut/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic officially files for its public debut",
    "url": "https://techcrunch.com/2026/10/26/anthropic-officially-files-for-its-public-debut/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T14:35:22+00:00",
    "summary": "Anthropic has officially filed for an IPO, revealing soaring revenue, mounting losses, major enterprise adoption, and an unusual governance structure designed to preserve founder control and its AI sa"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/26/apple-unveils-new-ipad-mini-with-oled-display-and-faster-a20-pro-chip/",
    "domain": "大厂 AI 动态",
    "title": "Apple unveils new iPad mini with OLED display and faster A20 Pro chip",
    "url": "https://techcrunch.com/2026/10/26/apple-unveils-new-ipad-mini-with-oled-display-and-faster-a20-pro-chip/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T14:25:43+00:00",
    "summary": "The new iPad mini features a thinner and lighter design than its predecessor."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/26/matiks-raises-10m-to-expand-its-math-and-puzzle-gaming-platform/",
    "domain": "大厂 AI 动态",
    "title": "Matiks raises $10M to expand its math and puzzle gaming platform",
    "url": "https://techcrunch.com/2026/10/26/matiks-raises-10m-to-expand-its-math-and-puzzle-gaming-platform/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T14:08:04+00:00",
    "summary": "Matiks has introduced a new platform for users to create games using AI."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/26/tesla-turns-to-turo-to-boost-adoption-of-full-self-driving-supervised/",
    "domain": "大厂 AI 动态",
    "title": "Tesla turns to Turo to boost adoption of Full Self-Driving (Supervised)",
    "url": "https://techcrunch.com/2026/10/26/tesla-turns-to-turo-to-boost-adoption-of-full-self-driving-supervised/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T12:58:40+00:00",
    "summary": "Eligible Turo hosts will also get a one-month free trial of Tesla's FSD software."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/25/5-best-apps-track-reading-discover-new-books/",
    "domain": "大厂 AI 动态",
    "title": "The best apps for tracking your reading and discovering new books",
    "url": "https://techcrunch.com/2026/10/25/5-best-apps-track-reading-discover-new-books/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T01:10:00+00:00",
    "summary": "There are numerous apps on the market that promise to do just that, so we’ve compiled a list of some of the best ones to help you pick the right one for you."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/25/grok-releases-the-first-seven-minutes-of-its-ai-generated-odyssey/",
    "domain": "大厂 AI 动态",
    "title": "Grok releases the first seven minutes of its AI-generated ‘Odyssey’",
    "url": "https://techcrunch.com/2026/10/25/grok-releases-the-first-seven-minutes-of-its-ai-generated-odyssey/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-25T21:31:16+00:00",
    "summary": "The footage looks okay, as long as you're not seeking artistry, inspiration, or human interest."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/25/cyberselfish-author-takes-aim-at-techno-libertarianism-as-her-book-returns-from-the-dead/",
    "domain": "大厂 AI 动态",
    "title": "‘Cyberselfish’ author takes aim at techno-libertarianism as her book returns from the dead",
    "url": "https://techcrunch.com/2026/10/25/cyberselfish-author-takes-aim-at-techno-libertarianism-as-her-book-returns-from-the-dead/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-25T20:20:08+00:00",
    "summary": "\"That's a 12-year-old view of the world.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/25/ai-delivers-zero-financial-payoff-to-most-companies-according-to-apollo-economist/",
    "domain": "大厂 AI 动态",
    "title": "AI delivers ‘zero financial payoff’ to most companies, Apollo economist says",
    "url": "https://techcrunch.com/2026/10/25/ai-delivers-zero-financial-payoff-to-most-companies-according-to-apollo-economist/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-25T16:57:32+00:00",
    "summary": "\"Despite massive investments and widespread hype around artificial intelligence, the technology has delivered zero financial payoff to corporate America outside of tech.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/25/techcrunch-mobility-blue-green-is-the-color-of-autonomy/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Mobility: Blue-green is the color of autonomy",
    "url": "https://techcrunch.com/2026/10/25/techcrunch-mobility-blue-green-is-the-color-of-autonomy/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-25T16:05:00+00:00",
    "summary": "Welcome back to TechCrunch Mobility, your hub for the future of transportation and now, more than ever, the role AI is playing in it."
  },
  {
    "id": "rss:https://stratechery.com/2026/the-end-of-the-internet/",
    "domain": "大厂 AI 动态",
    "title": "The End of the Internet",
    "url": "https://stratechery.com/2026/the-end-of-the-internet/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T10:00:00+00:00",
    "summary": "The old Internet, where anyone could host a server is over, but it's just the final blow in an ending that has been coming for years. The future, though, is brighter than it appears."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/10/microsoft-offers-voluntary-buyouts-to-60000-employees/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft offers to buy out a quarter of its workforce",
    "url": "https://arstechnica.com/gadgets/2026/10/microsoft-offers-voluntary-buyouts-to-60000-employees/",
    "source": "Nick Indge",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T22:36:06+00:00",
    "summary": "Employees in the US, Canada, India, and the UK may receive offers to leave MS today."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/10/whats-worse-than-having-eye-worms-having-eye-worms-with-babies/",
    "domain": "大厂 AI 动态",
    "title": "Worms mate in man's eyes, get plucked out right before larvae burst out",
    "url": "https://arstechnica.com/health/2026/10/whats-worse-than-having-eye-worms-having-eye-worms-with-babies/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T20:27:00+00:00",
    "summary": "Case study gives a whole new meaning to \"bedroom eyes.\""
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/10/meet-the-real-life-scottish-surgeon-who-inspired-sherlock-holmes/",
    "domain": "大厂 AI 动态",
    "title": "Meet the real-life Scottish surgeon who inspired Sherlock Holmes",
    "url": "https://arstechnica.com/science/2026/10/meet-the-real-life-scottish-surgeon-who-inspired-sherlock-holmes/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T20:15:07+00:00",
    "summary": "Lindsey Fitzharris chats with Ars about her new book, Sleuth-Hound: The Case of the Real Sherlock Holmes."
  },
  {
    "id": "rss:https://arstechnica.com/apple/2026/10/apple-releases-ios-and-macos-27-2-with-new-siri-ai-features-new-music-logo/",
    "domain": "大厂 AI 动态",
    "title": "Apple releases iOS and macOS 27.2 with new Siri AI features, new Music logo",
    "url": "https://arstechnica.com/apple/2026/10/apple-releases-ios-and-macos-27-2-with-new-siri-ai-features-new-music-logo/",
    "source": "Samuel Axon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T20:04:16+00:00",
    "summary": "Included is the ability to limit which applications Siri can directly access."
  },
  {
    "id": "rss:https://arstechnica.com/apple/2026/10/apple-reveals-updated-ipad-mini-with-a-bigger-oled-screen-for-700/",
    "domain": "大厂 AI 动态",
    "title": "Apple reveals updated iPad mini with a bigger OLED screen for $700",
    "url": "https://arstechnica.com/apple/2026/10/apple-reveals-updated-ipad-mini-with-a-bigger-oled-screen-for-700/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T19:04:40+00:00",
    "summary": "Apple claims this is the most significant update ever for the iPad mini line."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/10/boston-dynamics-employees-want-to-block-sale-of-robot-dogs-to-ice/",
    "domain": "大厂 AI 动态",
    "title": "ICE plan to buy robot dogs spurs protest from hundreds of Boston Dynamics employees",
    "url": "https://arstechnica.com/ai/2026/10/boston-dynamics-employees-want-to-block-sale-of-robot-dogs-to-ice/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T18:50:41+00:00",
    "summary": "US robotics company stands by ICE deal as more than 300 employees warn of risk."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/10/musk-accuses-ukraine-of-violating-starlink-terms-with-deadly-drone-strikes/",
    "domain": "大厂 AI 动态",
    "title": "Musk accuses Ukraine of violating Starlink terms with deadly drone strikes",
    "url": "https://arstechnica.com/tech-policy/2026/10/musk-accuses-ukraine-of-violating-starlink-terms-with-deadly-drone-strikes/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T18:09:08+00:00",
    "summary": "Ukraine says Starshield back to normal, denies misuse of Starlink commercial service."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/10/highway-thieves-are-spoofing-gps-to-steal-millions-in-data-center-bound-cargo/",
    "domain": "大厂 AI 动态",
    "title": "Highway thieves are spoofing GPS to steal millions in data center-bound cargo",
    "url": "https://arstechnica.com/tech-policy/2026/10/highway-thieves-are-spoofing-gps-to-steal-millions-in-data-center-bound-cargo/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T17:26:36+00:00",
    "summary": "Investigators explain how highway thieves stole $100M in data center equipment."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/10/some-iphone-duo-screens-are-already-failing/",
    "domain": "大厂 AI 动态",
    "title": "Some iPhone Duo screens are already failing",
    "url": "https://arstechnica.com/gadgets/2026/10/some-iphone-duo-screens-are-already-failing/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T16:51:49+00:00",
    "summary": "Apple's \"precision-engineered\" hinge is apparently damaging some iPhone Duo screens."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/10/f1-in-texas-one-more-race-and-well-have-a-new-champion/",
    "domain": "大厂 AI 动态",
    "title": "F1 in Texas: The American race that fans love to attend",
    "url": "https://arstechnica.com/cars/2026/10/f1-in-texas-one-more-race-and-well-have-a-new-champion/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T14:48:24+00:00",
    "summary": "Ars spends the weekend with the Audi Revolut F1 team at the Circuit of the Americas."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/10/tesla-wants-ai-and-software-to-be-its-next-profit-engine/",
    "domain": "大厂 AI 动态",
    "title": "Tesla gave up the EV crown. Now it wants to win the autonomy race.",
    "url": "https://arstechnica.com/cars/2026/10/tesla-wants-ai-and-software-to-be-its-next-profit-engine/",
    "source": "Kana Inagaki, Financial Times",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T14:30:27+00:00",
    "summary": "Tesla hopes autonomy subscriptions can deliver the margins car sales cannot."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/10/from-impulse-purchase-to-pocket-studio-the-m-vave-fm-1/",
    "domain": "大厂 AI 动态",
    "title": "From impulse purchase to pocket studio: The M-Vave FM-1",
    "url": "https://arstechnica.com/gadgets/2026/10/from-impulse-purchase-to-pocket-studio-the-m-vave-fm-1/",
    "source": "Nick Indge",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T11:00:15+00:00",
    "summary": "M-Vave's cheap FM-1 pocket synth has exploded as a community firmware playground."
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
    "id": "hn:49886005",
    "domain": "股票",
    "title": "Anthropic's IPO prospectus shows AI vision, surging costs",
    "url": "https://www.reuters.com/business/finance/anthropics-ipo-prospectus-shows-sweeping-ai-vision-surging-costs-2026-09-28/",
    "source": "6thbit",
    "platform": "hackernews",
    "points": 145,
    "published_at": "2026-09-28T23:40:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:50162431",
    "domain": "股票",
    "title": "The Secret Life of Circuits is now in stock everywhere",
    "url": "https://blog.coredump.cx/p/the-secret-life-of-circuits-is-now",
    "source": "surprisetalk",
    "platform": "hackernews",
    "points": 102,
    "published_at": "2026-10-20T07:15:12+00:00",
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
    "id": "hn:50254255",
    "domain": "股票",
    "title": "Pentagon orders bases to plan for 90 days without the grid",
    "url": "https://fortune.com/2026/10/26/pentagon-fortress-bases-90-days-off-grid-uk-be-ready-stockpile/",
    "source": "russfink",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-10-27T03:02:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:50210325",
    "domain": "股票",
    "title": "Built a site that teaches investing using the live market as the examples",
    "url": "https://www.stocksightfinance.com",
    "source": "kshitik",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-10-23T15:07:06+00:00",
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
    "id": "hn:49914149",
    "domain": "股票",
    "title": "Anthropic's IPO Prospectus Is a Fucking Doozy",
    "url": "https://daringfireball.net/linked/2026/09/30/reuters-anthropic-ipo-prospectus",
    "source": "danaris",
    "platform": "hackernews",
    "points": 71,
    "published_at": "2026-09-30T20:44:19+00:00",
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
    "id": "hn:50193524",
    "domain": "股票",
    "title": "Chinese stocks turn biggest losers as global AI trade stumbles",
    "url": "https://theedgemalaysia.com/node/822195",
    "source": "miohtama",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-10-22T10:32:13+00:00",
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
    "id": "hn:50098423",
    "domain": "股票",
    "title": "Asia chip stocks fall, AI funding worries",
    "url": "https://www.cnbc.com/2026/10/15/sk-hynix-samsung-softbank-stocks-asia-tech-rout-ai-funding-worries.html",
    "source": "kristianp",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-10-15T02:29:41+00:00",
    "summary": ""
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
    "id": "hn:50113666",
    "domain": "股票",
    "title": "South Korea's stock market down, president telling people not to commit suicide",
    "url": "https://twitter.com/litcapital/status/2110752546415382699",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-10-16T03:26:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:50086344",
    "domain": "股票",
    "title": "Humxn Commits $50M to Buy Skilled Trades Data for Robotics Training",
    "url": "https://markets.businessinsider.com/news/stocks/humxn-research-labs-wants-to-buy-50-million-worth-of-skilled-trades-farming-and-manufacturing-data-for-ai-robotics-training-1036622854",
    "source": "howdoweknowit",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-10-14T12:04:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:50113735",
    "domain": "股票",
    "title": "CoreWeave Founders Shield Fortunes with $3.3B Stock Sales",
    "url": "https://www.bloomberg.com/news/articles/2026-10-15/coreweave-founders-shield-fortunes-with-3-3-billion-stock-sales",
    "source": "qlte",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-10-16T03:34:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:50122366",
    "domain": "股票",
    "title": "Anthropic's Valuation Collapsed by $500B",
    "url": "https://www.telegraph.co.uk/business/2026/10/16/anthropic-valuation-ipo-ai-stock-listing/",
    "source": "novaRom",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-10-16T18:27:58+00:00",
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
    "id": "hn:50112657",
    "domain": "金融",
    "title": "Tesla Roadster",
    "url": "https://www.tesla.com/roadster",
    "source": "shekhar101",
    "platform": "hackernews",
    "points": 1644,
    "published_at": "2026-10-16T01:32:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:49948254",
    "domain": "金融",
    "title": "Federal judge calls Flock 'indiscriminate mass surveillance'",
    "url": "https://techcrunch.com/2026/10/03/federal-judge-calls-flock-indiscriminate-mass-surveillance/",
    "source": "sbulaev",
    "platform": "hackernews",
    "points": 503,
    "published_at": "2026-10-03T22:07:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:49875913",
    "domain": "金融",
    "title": "Parley: Federated, decentralised chat that speaks plain IRC",
    "url": "https://git.mills.io/prologic/parley",
    "source": "davidcollantes",
    "platform": "hackernews",
    "points": 330,
    "published_at": "2026-09-28T10:30:54+00:00",
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
    "id": "hn:49921118",
    "domain": "金融",
    "title": "Meta Uses A.I. Data Centers to Avoid Billions in Federal Taxes",
    "url": "https://www.nytimes.com/2026/09/30/technology/meta-ai-data-centers-taxes.html",
    "source": "gmays",
    "platform": "hackernews",
    "points": 259,
    "published_at": "2026-10-01T13:05:51+00:00",
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
    "id": "hn:50239430",
    "domain": "金融",
    "title": "Tesla cancels Cybertruck in Australia and NZ after 7 years of deposits",
    "url": "https://electrek.co/2026/10/23/tesla-cancels-cybertruck-australia-new-zealand/",
    "source": "MilnerRoute",
    "platform": "hackernews",
    "points": 93,
    "published_at": "2026-10-26T05:13:15+00:00",
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
    "id": "hn:50090662",
    "domain": "金融",
    "title": "Tesla's Robotaxis Blow Through School Zones, NHTSA Petition Alleges",
    "url": "https://www.extremetech.com/cars/teslas-robotaxis-blow-through-school-zones-nhtsa-petition-alleges",
    "source": "speckx",
    "platform": "hackernews",
    "points": 146,
    "published_at": "2026-10-14T16:45:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:50253630",
    "domain": "金融",
    "title": "The 'Buy, Borrow and Die' Wealth Strategy Has Become a $5T Market",
    "url": "https://www.wsj.com/finance/the-buy-borrow-and-die-wealth-strategy-has-become-a-5-trillion-market-d9149a9d",
    "source": "tysone",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-10-27T01:30:08+00:00",
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
    "id": "hn:50141295",
    "domain": "金融",
    "title": "Tesla 'Cannot Guarantee' Roadster Reservation Holders Will Ever Get a Car",
    "url": "https://www.thedrive.com/news/tesla-cannot-guarantee-roadster-reservation-holders-will-ever-get-a-car",
    "source": "healsdata",
    "platform": "hackernews",
    "points": 121,
    "published_at": "2026-10-18T14:16:41+00:00",
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
    "id": "hn:50236506",
    "domain": "金融",
    "title": "F45 (Fedora 45) Final Is No-Go",
    "url": "https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/EWDOYT6TOMFY4XPL5MJC2QWCDJBOR6MU/",
    "source": "gnabgib",
    "platform": "hackernews",
    "points": 31,
    "published_at": "2026-10-25T22:09:09+00:00",
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
    "id": "hn:50189801",
    "domain": "金融",
    "title": "Tesla profits drop 43% in Q3",
    "url": "https://arstechnica.com/cars/2026/10/tesla-profits-drop-43-in-q3/",
    "source": "throw0101a",
    "platform": "hackernews",
    "points": 87,
    "published_at": "2026-10-22T01:02:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:49916668",
    "domain": "金融",
    "title": "10-year Treasury yield climbs above 5.3% to a level not seen in 24 years",
    "url": "https://www.wsj.com/finance/investing/surging-yields-bring-the-bond-market-back-to-the-turn-of-the-century-2b74773f",
    "source": "kaycebasques",
    "platform": "hackernews",
    "points": 125,
    "published_at": "2026-10-01T01:40:50+00:00",
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
    "id": "rss:https://arxiv.org/abs/2610.33102",
    "domain": "金融",
    "title": "The Capability Transfer: Cohort Reversal, Codified Expertise, and the Adaptability Tax of AI Transformation",
    "url": "https://arxiv.org/abs/2610.33102",
    "source": "Ina Catrinescu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T04:00:00+00:00",
    "summary": "arXiv:2610.33102v1 Announce Type: new Abstract: Most analyses of AI and employment ask which jobs are exposed. This paper asks what happens to the pipeline that produces experts. It extends the model "
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.33109",
    "domain": "金融",
    "title": "Uncertainty Quantification for Financial Foundation Models: A Survey",
    "url": "https://arxiv.org/abs/2610.33109",
    "source": "Zijie Zhao, Mingjun Sun, Shenbo Xu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T04:00:00+00:00",
    "summary": "arXiv:2610.33109v1 Announce Type: new Abstract: Financial foundation models increasingly support workflows spanning financial question answering, disclosure analysis, forecasting, and decision-making."
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.33400",
    "domain": "金融",
    "title": "Tracking High-Frequency Trading Activity in China and Its Effects on Market Quality",
    "url": "https://arxiv.org/abs/2610.33400",
    "source": "Li Guo, Frank Weikai Li, Ding Qi, Lijian Sun",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T04:00:00+00:00",
    "summary": "arXiv:2610.33400v1 Announce Type: new Abstract: We develop a new order-level proxy for high-frequency trading (HFT) activity based on precise order placement and study its effects on market quality. W"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.33447",
    "domain": "金融",
    "title": "Efficiency vs Capability in the Intelligence Explosion",
    "url": "https://arxiv.org/abs/2610.33447",
    "source": "Karthik Tadepalli",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T04:00:00+00:00",
    "summary": "arXiv:2610.33447v1 Announce Type: new Abstract: AI progress can feed back into AI research in two ways. Capability improvements allow AIs to perform a larger share of AI research tasks, while efficien"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.33453",
    "domain": "金融",
    "title": "Cross-Bond Panel Learning for Next-Day Price Forecasting of Chinese Convertible Bonds: A Reality Check",
    "url": "https://arxiv.org/abs/2610.33453",
    "source": "Derun Zhong, Guolian Wang, Shiqing Wang, Hongjie Feng",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T04:00:00+00:00",
    "summary": "arXiv:2610.33453v1 Announce Type: new Abstract: Recent advances in financial machine learning have prompted growing interest in applying deep neural networks to convertible bond valuation and forecast"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.33597",
    "domain": "金融",
    "title": "Optimal portfolio choice under green transition timing risk",
    "url": "https://arxiv.org/abs/2610.33597",
    "source": "Emma Kroell, Mogens Steffensen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T04:00:00+00:00",
    "summary": "arXiv:2610.33597v1 Announce Type: new Abstract: We study an investor's optimal portfolio choice problem when they account for the impact of a possible future green transition, whose timing is uncertai"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.33604",
    "domain": "金融",
    "title": "What FLARE's Published Numbers Actually Measure",
    "url": "https://arxiv.org/abs/2610.33604",
    "source": "Dung Cao, Palaash Gang, Arjun Veluri",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T04:00:00+00:00",
    "summary": "arXiv:2610.33604v1 Announce Type: new Abstract: We audit the scoring pipeline of FLARE, the financial task suite behind PIXIU and FinBen, and find that in a decisive fraction of cells the score is a p"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.33785",
    "domain": "金融",
    "title": "Geoeconomic Stress and European Defence Readiness",
    "url": "https://arxiv.org/abs/2610.33785",
    "source": "d'Artis Kancs",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T04:00:00+00:00",
    "summary": "arXiv:2610.33785v1 Announce Type: new Abstract: This study develops a country-level measure of the economic-industrial capacity of European NATO Allies to mobilise, replenish, maintain, and sustain mi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.33786",
    "domain": "金融",
    "title": "Jensen gaps and the decomposition principle",
    "url": "https://arxiv.org/abs/2610.33786",
    "source": "Lilian Hu, Ruodu Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T04:00:00+00:00",
    "summary": "arXiv:2610.33786v1 Announce Type: new Abstract: We provide axiomatic characterizations of Jensen-gap functionals, which have the form $\\rho(X)=\\mathbb{E}[f(X)]-f(\\mathbb{E}[X])$ for some real-valued f"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.34133",
    "domain": "金融",
    "title": "Smart charging without rebound peaks: Wholesale price feedback limits distribution grid peaks from price-responsive electric vehicles",
    "url": "https://arxiv.org/abs/2610.34133",
    "source": "Lion Hirth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T04:00:00+00:00",
    "summary": "arXiv:2610.34133v1 Announce Type: new Abstract: Studies on price-optimized EV charging consistently find that the common price signal synchronizes charging of the entire fleet of cars in the cheapest "
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.34153",
    "domain": "金融",
    "title": "Certifying Reward Alignment in Portfolio Reinforcement Learning",
    "url": "https://arxiv.org/abs/2610.34153",
    "source": "Matin Tavakoli, Seyedreza Tavakoli, Faezeh Salmani, Amir Amini, Mohammad Hosein Rohban, Gholamali Aminian, Ali Habibnia Rohban",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T04:00:00+00:00",
    "summary": "arXiv:2610.34153v1 Announce Type: new Abstract: Financial reinforcement learning often translates an investment objective into an additive risk-adjusted reward. An agent can optimise that reward accur"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.34348",
    "domain": "金融",
    "title": "Optimal ratcheting dividend policies with resets",
    "url": "https://arxiv.org/abs/2610.34348",
    "source": "Alexandre Roch, Simone Scotti",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T04:00:00+00:00",
    "summary": "arXiv:2610.34348v1 Announce Type: new Abstract: We study an optimal dividend policy problem under ratcheting and bankruptcy constraints. Firms face a tradeoff between the negative signal of a dividend"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.34787",
    "domain": "金融",
    "title": "Do Round Numbers Hold Prices? Occupation Densities and Depth-Conditioned Hazards in the Limit Order Book",
    "url": "https://arxiv.org/abs/2610.34787",
    "source": "Jiwon Jung, Kiseop Lee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T04:00:00+00:00",
    "summary": "arXiv:2610.34787v1 Announce Type: new Abstract: Prices cluster at round numbers, a pattern often interpreted as evidence that these levels act as price barriers. This pattern also admits a mechanical "
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.34936",
    "domain": "金融",
    "title": "Det-MASO: Diversity-Regularized Multi-Agent Sequential Optimization for Factor Generation",
    "url": "https://arxiv.org/abs/2610.34936",
    "source": "Tiantian Wu, Peng Yang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T04:00:00+00:00",
    "summary": "arXiv:2610.34936v1 Announce Type: new Abstract: Quantitative investment requires alpha factors that are both predictive and diverse. However, existing factor generation methods, including formulaic mi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.35022",
    "domain": "金融",
    "title": "Martingality in EFM Signature Volatility Models",
    "url": "https://arxiv.org/abs/2610.35022",
    "source": "Dimitri Sotnikov, Adeline Viot",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T04:00:00+00:00",
    "summary": "arXiv:2610.35022v1 Announce Type: new Abstract: We establish a martingality criterion for the Exponentially Fading Memory (EFM) signature volatility model, extending the recent result of Abi Jaber, Ga"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.35118",
    "domain": "金融",
    "title": "Scenario Matching for Credit Dependence Stress Tests: Temporal correlation constraints and empirical risk bounds",
    "url": "https://arxiv.org/abs/2610.35118",
    "source": "Naoufal Nifa",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T04:00:00+00:00",
    "summary": "arXiv:2610.35118v1 Announce Type: new Abstract: We couple two sets of simulated market and credit paths by minimizing absolute temporal-correlation error relative to a prescribed target. Each market p"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.35702",
    "domain": "金融",
    "title": "Weekend Crypto Volatility and Monday Market Risk",
    "url": "https://arxiv.org/abs/2610.35702",
    "source": "Pedram Ebadollahyvahed, Nneka Umeorah",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T04:00:00+00:00",
    "summary": "arXiv:2610.35702v1 Announce Type: new Abstract: Cryptocurrencies trade continuously while major traditional markets close over the weekend. We examine whether weekend cryptocurrency volatility predict"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.33098",
    "domain": "金融",
    "title": "Identifying level-$k$ reasoning in repeated games: Strategies, beliefs, and cognitive ability",
    "url": "https://arxiv.org/abs/2610.33098",
    "source": "David Gill, Yaroslav Rosokha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T04:00:00+00:00",
    "summary": "arXiv:2610.33098v1 Announce Type: cross Abstract: In this paper, we identify level-$k$ reasoning in repeated games that operates at the level of a supergame strategy. First, we develop a model of leve"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.33122",
    "domain": "金融",
    "title": "The Digital-Energy Recomposition of the Kitchin Cycle: Exploratory Evidence from U.S. IT and Irish Data-Centre Series (1995-2025)",
    "url": "https://arxiv.org/abs/2610.33122",
    "source": "Bartosz Ziollko, Adam Niedzialkowski, Bartosz Szyma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T04:00:00+00:00",
    "summary": "arXiv:2610.33122v1 Announce Type: cross Abstract: Using quarterly FRED and CSO Ireland data over 1995Q1-2025Q4, we examine whether U.S.\\ IT investment and Irish data-centre electricity are recomposing"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.33132",
    "domain": "金融",
    "title": "A Stationary Mean-Field Model for Carbon Market Stability Reserve",
    "url": "https://arxiv.org/abs/2610.33132",
    "source": "Ren\\'e A\\\"id, Federico Cannerozzi, Giorgio Ferrari",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T04:00:00+00:00",
    "summary": "arXiv:2610.33132v1 Announce Type: cross Abstract: We formulate the design of a market stability reserve as a stationary mean-field singular control problem. The allowance balance follows a regime-swit"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.33438",
    "domain": "金融",
    "title": "Compiling and forecasting implied volatility surfaces via survey sampling, tempered inverse-probability sequence learning, and causal activity clocks",
    "url": "https://arxiv.org/abs/2610.33438",
    "source": "Deepak Bastola, Eli Prushansky",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T04:00:00+00:00",
    "summary": "arXiv:2610.33438v1 Announce Type: cross Abstract: Compiling implied volatility (IV) surfaces and forecasting derivative risk from high-frequency equity and options feeds requires addressing contract h"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.33538",
    "domain": "金融",
    "title": "Tokenised Sukuk: A Verifiable Architecture for Asset Evidence and Programmable Shariah Compliance",
    "url": "https://arxiv.org/abs/2610.33538",
    "source": "Rischan Mafrur, Khadijah, Gun Gun Febrianza",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T04:00:00+00:00",
    "summary": "arXiv:2610.33538v1 Announce Type: cross Abstract: Security-token standards such as ERC-3643 decide who may hold a token, not what stands behind it. For a sukuk this gap matters: whether a certificate "
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.35476",
    "domain": "金融",
    "title": "Differentiability and Convexity of the Solution Maps for Fully Non-linear Parabolic HJB Equations",
    "url": "https://arxiv.org/abs/2610.35476",
    "source": "Jean-Fran\\c{c}ois Chassagneux, St\\'ephane Cr\\'epey, Gr\\'egoire Loeper, Justin Ruelland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T04:00:00+00:00",
    "summary": "arXiv:2610.35476v1 Announce Type: cross Abstract: We study the dependence on the terminal condition of solutions to a fully nonlinear parabolic Hamilton--Jacobi--Bellman (HJB) equation, when the termi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.35738",
    "domain": "金融",
    "title": "Fuji: The Shape, Composition, and Spread of Demand Bursts on Robinhood Chain",
    "url": "https://arxiv.org/abs/2610.35738",
    "source": "Pranay Anchuri (Offchain Labs)",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T04:00:00+00:00",
    "summary": "arXiv:2610.35738v1 Announce Type: cross Abstract: Demand on blockchain-based marketplaces arrives in bursts and at a high rate. On these platforms the data are completely visible, which makes it feasi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2405.02170",
    "domain": "金融",
    "title": "Fourier-Laplace transforms in polynomial Ornstein-Uhlenbeck volatility models",
    "url": "https://arxiv.org/abs/2405.02170",
    "source": "Eduardo Abi Jaber (Xiaoyuan), Shaun (Xiaoyuan), Li, Xuyang Lin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T04:00:00+00:00",
    "summary": "arXiv:2405.02170v2 Announce Type: replace Abstract: We consider the Fourier-Laplace transforms of a broad class of polynomial Ornstein-Uhlenbeck (OU) volatility models, including the well-known Stein-"
  },
  {
    "id": "rss:https://arxiv.org/abs/2501.00058",
    "domain": "金融",
    "title": "European Defence Readiness",
    "url": "https://arxiv.org/abs/2501.00058",
    "source": "d'Artis Kancs",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T04:00:00+00:00",
    "summary": "arXiv:2501.00058v4 Announce Type: replace Abstract: Europe's defence readiness is being tested by a deteriorating security environment, prolonged war on the continent and growing uncertainty over the "
  },
  {
    "id": "rss:https://arxiv.org/abs/2512.07867",
    "domain": "金融",
    "title": "LLM-Generated Counterfactual Stress Scenarios for Portfolio Risk Simulation via Hybrid Prompt-RAG Pipeline",
    "url": "https://arxiv.org/abs/2512.07867",
    "source": "Masoud Soleimani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T04:00:00+00:00",
    "summary": "arXiv:2512.07867v2 Announce Type: replace Abstract: We develop a transparent, auditable large language model (LLM) pipeline for macro-financial stress testing. Structured prompting, with optional retr"
  },
  {
    "id": "rss:https://arxiv.org/abs/2601.11305",
    "domain": "金融",
    "title": "Multiscaling in the Rough Bergomi Model: A Tale of Tails",
    "url": "https://arxiv.org/abs/2601.11305",
    "source": "Giuseppe Brandi, Tiziana Di Matteo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T04:00:00+00:00",
    "summary": "arXiv:2601.11305v2 Announce Type: replace Abstract: The rough Bergomi (rBergomi) model, characterised by its roughness parameter $H$, has been shown to exhibit multiscaling behaviour as $H$ approaches"
  }
]
```
