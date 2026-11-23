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

- 今日日期：`2026-11-23`
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
  "date": "2026-11-23",
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
    "points": 2282870,
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
    "points": 2150272,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1onb6zwEkk",
    "domain": "AI",
    "title": "【Ai教程】100集（全）从零开始学illustrator软件基础 (Ai2025新手入门实用版)Ai2025零基础入门教程！！！",
    "url": "http://www.bilibili.com/video/av115025985412548",
    "source": "天才AI设计鲨",
    "platform": "bilibili",
    "points": 1584613,
    "published_at": "2025-08-14T11:00:00+00:00",
    "summary": "设计行业5年 是一名资深设计师~PS学习交流 （南极有什么→ 动物 群 ：211582457）\n你的三连是我最大的动力！！你的三连是我最大的动力！！你的三连是我最大的动力！！"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 1580428,
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
    "points": 1513191,
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
    "points": 1488460,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1ojfDBSEPv",
    "domain": "AI",
    "title": "【闪客】一口气拆穿Skill/MCP/RAG/Agent/OpenClaw底层逻辑",
    "url": "http://www.bilibili.com/video/av116007418988157",
    "source": "飞天闪客",
    "platform": "bilibili",
    "points": 946949,
    "published_at": "2026-02-03T15:37:23+00:00",
    "summary": "被人负责造词，我负责帮大家吃词"
  },
  {
    "id": "bvid:BV1aeLqzUE6L",
    "domain": "AI",
    "title": "10分钟讲清楚 Prompt, Agent, MCP 是什么",
    "url": "http://www.bilibili.com/video/av114410228025650",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 916621,
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
    "points": 761874,
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
    "points": 597553,
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
    "points": 487636,
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
    "points": 437568,
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
    "points": 434914,
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
    "points": 428820,
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
    "points": 374435,
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
    "points": 366791,
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
    "points": 359007,
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
    "points": 332269,
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
    "points": 304374,
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
    "points": 292038,
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
    "points": 239558,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1468g6DEWs",
    "domain": "AI",
    "title": "【全100集】(允许白嫖) 2026最全最细的AI教程零基础入门到精通，一周带你小白变大神！全程干货无废话！存下吧，少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av117115386404821",
    "source": "AI产品经理入门教程-",
    "platform": "bilibili",
    "points": 232299,
    "published_at": "2026-08-18T13:11:45+00:00",
    "summary": "【2026最新版AI教程零基础入门到精通｜配套学习路线+工具包+实战项目，看置顶评论自取】\n 本套教程专为零基础设计，从AI是什么到独立用AI解决实际问题，手把手带你系统走完从入门到精通的完整路径。 ✅ AI认知入门：什么是AI/大模型、它们能做什么不能做什么、别被营销话术忽悠\n✅ 核心技能掌握：提示词工程、多轮对话技巧、让AI稳定输出的方法论\n✅ 进阶能力突破：AI工作流搭建、智能体开发、多工具"
  },
  {
    "id": "bvid:BV1qJs16WEJj",
    "domain": "AI",
    "title": "今天体验的人生副本是:沉迷vibe coding走火入魔的AI嘉豪",
    "url": "http://www.bilibili.com/video/av117635899524333",
    "source": "vibe睦头人",
    "platform": "bilibili",
    "points": 230576,
    "published_at": "2026-11-18T06:01:48+00:00",
    "summary": "ai生成，仅供娱乐，如有雷同，纯属巧合（（"
  },
  {
    "id": "bvid:BV15XDfBSE2t",
    "domain": "AI",
    "title": "ClaudeCode平替:OpenCode详细使用教程看这一个就够了（内含超详细安装文档+软件安装包）",
    "url": "http://www.bilibili.com/video/av116379604881806",
    "source": "鹏哥C语言",
    "platform": "bilibili",
    "points": 211925,
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
    "points": 187622,
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
    "points": 166652,
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
    "points": 164439,
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
    "points": 162257,
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
    "points": 158660,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1Qcg6zgEhU",
    "domain": "AI",
    "title": "【AI Agent实战】从零开始教你搭建Agent智能体，小白也能学会的保姆级教程！让你少走99%弯路！",
    "url": "http://www.bilibili.com/video/av114771105945944",
    "source": "讲AI的小坛",
    "platform": "bilibili",
    "points": 128150,
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
    "points": 120284,
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
    "points": 105064,
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
    "points": 94389,
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
    "points": 91989,
    "published_at": "2026-07-26T01:30:00+00:00",
    "summary": "模组：Numen\n项目地址：https://github.com/Dwinovo/minecraft-numen"
  },
  {
    "id": "bvid:BV1cVW86JE2e",
    "domain": "AI",
    "title": "Vibe Coding 完不会获客？我用 AI 做了一个「营销数据库」！【B站AI创造公开赛】",
    "url": "http://www.bilibili.com/video/av117587245599812",
    "source": "熠辉IndieDev",
    "platform": "bilibili",
    "points": 76624,
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
    "points": 65644,
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
    "points": 50720,
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
    "points": 47892,
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
    "points": 45607,
    "published_at": "2026-10-30T11:52:06+00:00",
    "summary": "一句话，让 AI 帮我们完成第一个 STM32C5 程序！🚀\n本期我们一起认识 AI Agent，学习如何描述开发需求，并借助开源的 STM32C5DevSkills，让 AI 完成工程创建、芯片配置、代码编写和编译烧录，让律动小板上的小灯闪烁起来！\n也特别感谢 @意法半导体中国   对本系列教程的支持～下期我们再亲手走一遍开发流程，把 Agent 替我们完成的工作，一步步搞明白！"
  },
  {
    "id": "bvid:BV1mvyYzeEus",
    "domain": "AI",
    "title": "0基础 5分钟学会DeepSeek Harness新手教程-01｜认识AI Agent，让AI替你干活",
    "url": "http://www.bilibili.com/video/av117654841137017",
    "source": "DurianPaul",
    "platform": "bilibili",
    "points": 45245,
    "published_at": "2026-11-21T14:16:06+00:00",
    "summary": "全系列资料（练习素材、提示词）：\n链接：https://share.weiyun.com/9ydbX2n9  密码：kmtjgc\n\n零基础也能听懂的 AI Agent 入门！这期用大白话和游戏比喻，讲清楚：\n• Agent 和聊天 AI 到底有什么不一样\n• DeepSeek Harness 是什么、能帮你干什么\n• 客户端怎么装、工作区怎么建、模型和推理等级怎么选\n• 插件、Skill、MCP、"
  },
  {
    "id": "bvid:BV1hmb26ZEws",
    "domain": "AI",
    "title": "DeepSeek Harness 实测  Claude Code 对比后，梁神我错了 差距比我想的大",
    "url": "http://www.bilibili.com/video/av117100337236191",
    "source": "程序员晓刘",
    "platform": "bilibili",
    "points": 42550,
    "published_at": "2026-08-15T16:01:38+00:00",
    "summary": "这期用同一个 DeepSeek Pro 0813 模型，分别在 Claude Code 和 DeepSeek Harness 里完成同样的任务，对比工具链对最终效果的影响。\n实测内容包括：\nFPS 游戏 Demo、灯塔预警沙盘、手枪组装动画、显示器组装动画，以及 DeepSeek Harness 的插件化源码流程。\n整体看下来，模型本身当然重要，但 Harness 在插件化、流程记录、缓存命中和任"
  },
  {
    "id": "bvid:BV1NddKBvEsY",
    "domain": "AI",
    "title": "claude code 桌面端安装并且配置第三方api使用教程，想体验的尽早吧，因为这公司可能不知道哪天抽风就会禁用了！#claude #ai #人工智能",
    "url": "http://www.bilibili.com/video/av116535968466799",
    "source": "菜鸡的老黎",
    "platform": "bilibili",
    "points": 42452,
    "published_at": "2026-05-07T23:56:28+00:00",
    "summary": "claude code 桌面端安装并且配置第三方api使用教程，想体验的尽早吧，因为这公司可能不知道哪天抽风就会禁用了！#claude #ai #人工智能 #agent"
  },
  {
    "id": "bvid:BV1XiD5BQEAj",
    "domain": "AI",
    "title": "Claude Code 接入微信、一行命令把Claude Code装进微信、保姆级教程、微信支持Claude Code（cc-connect）远程开发",
    "url": "http://www.bilibili.com/video/av116350093694897",
    "source": "下班学AI",
    "platform": "bilibili",
    "points": 41585,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV1sQaL6vEkb",
    "domain": "AI",
    "title": "小白向，ai入门第一课：agent的部署和使用！",
    "url": "http://www.bilibili.com/video/av117349378166797",
    "source": "沈三殊",
    "platform": "bilibili",
    "points": 34868,
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
    "points": 30002,
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
    "points": 29076,
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
    "points": 27164,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1XPWm6EEZt",
    "domain": "AI",
    "title": "生而为卒，不朽于年——安卓claude code开发工作台cccodroid v0.6.16长期稳定版宣传mv",
    "url": "http://www.bilibili.com/video/av117597395818716",
    "source": "Grey-Oak",
    "platform": "bilibili",
    "points": 19685,
    "published_at": "2026-11-11T10:48:29+00:00",
    "summary": "七七八八，八八七七，这次也不想让ai替我编什么肉麻的小作文了，干脆直白点把这个项目诞生之前一直到现在为止的零零散散的记忆片段拼凑起来，勉强讲点什么。\n用harness的最直观需求——方便，还是方便，因此各大厂商都推出了自己的远程控制，但稳定性不尽如人意，所以早先我把目光投向了vps中转实现稳定远控，效果好一些，但上手成本不低。这个时候我第一次接触到了woaiys3（账号已停用，新用户名为yimen"
  },
  {
    "id": "bvid:BV1xLtS6WEVG",
    "domain": "AI",
    "title": "DeepSeek Harness的MCP应用教程、MCP安装、MCP迁移、MCP删除与卸载",
    "url": "http://www.bilibili.com/video/av117201218635665",
    "source": "eogee",
    "platform": "bilibili",
    "points": 18437,
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
    "points": 17023,
    "published_at": "2026-11-19T09:13:50+00:00",
    "summary": "这个合集用大白话讲清 Claude Code，先说清楚它到底是什么、能帮你做什么，再带你装好并配好环境；接着讲权限与控制模式、内置命令的用法，让它按你的规矩干活；然后一步步接上 MCP 用外部工具、写 Skill 复用常用能力、配 Hooks 做自动化、拆子智能体分工，最后用 SDD 规范把需求到代码的流程固定下来。全程按真实操作演示，每集都能跟着做，遇到坑也能提前避开，建议先收藏慢慢看。"
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
    "points": 307,
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
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/president-trump-says-nvidia-board-rehiring-jensen-huang-would-be-best-for-the-company-and-the-us-treasury-sec-bessent-walks-back-outsider-ceo-comments-claims-huang-is-technically-an-outsider-now",
    "domain": "AI 算力 / 半导体",
    "title": "President Trump says Nvidia board rehiring Jensen Huang would be best for the company and US",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/president-trump-says-nvidia-board-rehiring-jensen-huang-would-be-best-for-the-company-and-the-us-treasury-sec-bessent-walks-back-outsider-ceo-comments-claims-huang-is-technically-an-outsider-now",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T11:59:00+00:00",
    "summary": "After saying that Nvidia's new CEO should come \"outside the company,\" U.S. Treasury Secretary Scott Bessent now argues that former chief Jensen Huang \"is on the outside,\" paving the way for a return f"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-usd730-on-this-rtx-5070-ti-gaming-pc-from-cyberpower-32gb-of-ram-16gb-of-vram-and-a-2tb-ssd-make-for-an-impressive-spec-sheet-for-only-usd2-479",
    "domain": "AI 算力 / 半导体",
    "title": "Save $730 on this RTX 5070 Ti gaming PC from Cyberpower",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-usd730-on-this-rtx-5070-ti-gaming-pc-from-cyberpower-32gb-of-ram-16gb-of-vram-and-a-2tb-ssd-make-for-an-impressive-spec-sheet-for-only-usd2-479",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T11:39:43+00:00",
    "summary": "An impressive gaming PC prebuilt with an RTX 5070 TI 16GB powering the graphics. All for just $2.479 in Walmart's Black Friday deal."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-mice/weird-finger-wearable-gaming-mouse-kickstarter-breaks-8x-its-crowdfunding-goal-but-it-potentially-has-major-design-flaws-and-is-kind-of-sketchy",
    "domain": "AI 算力 / 半导体",
    "title": "Weird finger-wearable gaming mouse raises $43,000 on Kickstarter, a staggering 8x its crowdfunding goal",
    "url": "https://www.tomshardware.com/peripherals/gaming-mice/weird-finger-wearable-gaming-mouse-kickstarter-breaks-8x-its-crowdfunding-goal-but-it-potentially-has-major-design-flaws-and-is-kind-of-sketchy",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T11:30:00+00:00",
    "summary": "The Borslon finger-worn gaming mouse is the first of its kind, reaching $43,000 in its Kickstarter campaign and shattering its $5,000 goal. However, it may have some major design flaws."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/homelabbers-usd3-500-build-straps-four-32gb-nvidia-v100s-to-a-lenovo-mini-pc-for-128gb-of-vram-coreboot-oculink-docks-and-a-solder-bridge-unlock-285-tokens-sec-in-qwen3-8-27b",
    "domain": "AI 算力 / 半导体",
    "title": "Homelabber's $3,500 build straps four 32GB Nvidia V100s to a Lenovo mini PC for 128GB of VRAM",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/homelabbers-usd3-500-build-straps-four-32gb-nvidia-v100s-to-a-lenovo-mini-pc-for-128gb-of-vram-coreboot-oculink-docks-and-a-solder-bridge-unlock-285-tokens-sec-in-qwen3-8-27b",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T11:00:00+00:00",
    "summary": "A homelab builder runs four used Nvidia Tesla V100 32GB GPUs off a Lenovo ThinkCentre M720q Tiny over OCuLink for 128GB of VRAM."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/canadian-scalper-places-40-nvidia-rtx-5090s-on-facebook-marketplace-for-over-usd6-600-apiece-ironically-still-cheaper-than-memory-expresss-10-000-cad-retail-price-purportedly-selling-every-unit-quite-quickly",
    "domain": "AI 算力 / 半导体",
    "title": "Canadian scalper places 40+ Nvidia RTX 5090s on Facebook Marketplace for over $6,600 apiece",
    "url": "https://www.tomshardware.com/pc-components/gpus/canadian-scalper-places-40-nvidia-rtx-5090s-on-facebook-marketplace-for-over-usd6-600-apiece-ironically-still-cheaper-than-memory-expresss-10-000-cad-retail-price-purportedly-selling-every-unit-quite-quickly",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T10:30:00+00:00",
    "summary": "Canadian scalper places 40+ Nvidia RTX 5090s on Facebook Marketplace for over 6,600 USD a piece — purportedly sold every unit quite quickly"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/anthropic-researcher-tunes-chess-software-to-turn-a-200-mhz-pentium-pro-into-a-behemoth-that-would-handily-defeat-kasparov-and-carlsen-1995-pc-with-64-mb-of-ram-would-crush-kasparov-9-times-out-of-10",
    "domain": "AI 算力 / 半导体",
    "title": "Anthropic researcher tunes chess software to turn a 200 MHz Pentium Pro into a behemoth that would handily defeat Kasparov and Carlsen",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/anthropic-researcher-tunes-chess-software-to-turn-a-200-mhz-pentium-pro-into-a-behemoth-that-would-handily-defeat-kasparov-and-carlsen-1995-pc-with-64-mb-of-ram-would-crush-kasparov-9-times-out-of-10",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T10:00:00+00:00",
    "summary": "Anthropic researcher tunes chess software to turn a lone Pentium Pro into a behemoth that would handily defeat Kasparov and Carlsen — 1995 challenge would have a different outcome with today's softwar"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/corsairs-tiny-xeneon-edge-pc-touchscreen-discounted-by-usd50-in-all-five-colors-14-5-inch-lcd-touchscreen-drops-to-usd199-99-comes-with-a-built-in-stand",
    "domain": "AI 算力 / 半导体",
    "title": "Corsair's tiny Xeneon Edge PC touchscreen discounted by $50 in all five colors",
    "url": "https://www.tomshardware.com/pc-components/corsairs-tiny-xeneon-edge-pc-touchscreen-discounted-by-usd50-in-all-five-colors-14-5-inch-lcd-touchscreen-drops-to-usd199-99-comes-with-a-built-in-stand",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T21:32:16+00:00",
    "summary": "Corsair has all five colors of its 14.5-inch Xeneon Edge touchscreen on sale for Black Friday for $50 off."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/17-year-old-windows-7-gets-unofficial-directx-12-and-vulkan-1-4-support-enthusiasts-bring-nvidia-rtx-50-amd-rx-9000-and-intel-arc-gpus-to-the-aging-os",
    "domain": "AI 算力 / 半导体",
    "title": "17-year-old Windows 7 gets unofficial DirectX 12 and Vulkan 1.4 support",
    "url": "https://www.tomshardware.com/software/windows/17-year-old-windows-7-gets-unofficial-directx-12-and-vulkan-1-4-support-enthusiasts-bring-nvidia-rtx-50-amd-rx-9000-and-intel-arc-gpus-to-the-aging-os",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T20:03:52+00:00",
    "summary": "A community-developed project brings DirectX 12 and Vulkan 1.4 support to Microsoft's retired operating system, allowing modern Nvidia, AMD, and Intel graphics cards to work with Windows 7."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/usb/under-desk-headphone-hanger-with-three-charging-ports-drops-below-usd10-cozoos-20w-combo-device-has-been-a-useful-addition-to-my-standing-desk-since-2023",
    "domain": "AI 算力 / 半导体",
    "title": "An under-desk headphone hanger with three charging ports (up to 20W) for less than $10",
    "url": "https://www.tomshardware.com/peripherals/usb/under-desk-headphone-hanger-with-three-charging-ports-drops-below-usd10-cozoos-20w-combo-device-has-been-a-useful-addition-to-my-standing-desk-since-2023",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T19:34:47+00:00",
    "summary": "With two hanging hooks, notches for six cables and 20W of charging, Cozoo's quirky combo device has been a useful addition to my standing desk since 2023."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/handheld-gaming/nintendo-switch-2-bundles-drop-to-pre-hike-pricing-in-black-friday-run-up-sale-get-a-switch-2-along-with-mario-kart-world-and-nintendo-switch-online-for-usd50-off",
    "domain": "AI 算力 / 半导体",
    "title": "Nintendo Switch 2 bundles drop to pre-hike pricing in Black Friday run-up sale",
    "url": "https://www.tomshardware.com/video-games/handheld-gaming/nintendo-switch-2-bundles-drop-to-pre-hike-pricing-in-black-friday-run-up-sale-get-a-switch-2-along-with-mario-kart-world-and-nintendo-switch-online-for-usd50-off",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T19:00:00+00:00",
    "summary": "The Nintendo Switch 2 is down to its pre-hike pricing in a Black Friday run-up sale, knocking a rare $50 off a bundle that includes the console and Mario Kart World."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/give-your-gaming-setup-a-serious-upgrade-with-the-razer-basilisk-v3-for-half-price-for-just-usd32-99-you-get-26-000-dpi-sensitivity-programmable-buttons-and-plenty-of-rgb",
    "domain": "AI 算力 / 半导体",
    "title": "Give your gaming setup a serious upgrade with the Razer Basilisk V3 for half price",
    "url": "https://www.tomshardware.com/pc-components/give-your-gaming-setup-a-serious-upgrade-with-the-razer-basilisk-v3-for-half-price-for-just-usd32-99-you-get-26-000-dpi-sensitivity-programmable-buttons-and-plenty-of-rgb",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T18:17:53+00:00",
    "summary": "Whether you play competitive shooters, racing games, or RPGs, the Basilisk V3 offers customizable controls and an adjustable scroll wheel to suit different gaming preferences."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/mice/grab-keychrons-full-sized-low-profile-k5-v2-wireless-mechanical-keyboard-for-its-lowest-ever-price-of-just-usd56-108-key-low-profile-clacker-supports-qmk-sports-three-layers-of-foam",
    "domain": "AI 算力 / 半导体",
    "title": "Grab Keychron's full-sized low-profile K5 V2 wireless mechanical keyboard for its lowest-ever price of just $56",
    "url": "https://www.tomshardware.com/peripherals/mice/grab-keychrons-full-sized-low-profile-k5-v2-wireless-mechanical-keyboard-for-its-lowest-ever-price-of-just-usd56-108-key-low-profile-clacker-supports-qmk-sports-three-layers-of-foam",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T18:15:16+00:00",
    "summary": "If you're after a full-sized mechanical keyboard on a budget, this is one of the best deals around during early Black Friday. It has a white backlight and supports either Bluteooth or wired connectivi"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/case-fans/maker-builds-mad-max-inspired-wall-of-100-noctua-pc-fans-stress-tests-usd2-355-open-source-openfan-xl-controller",
    "domain": "AI 算力 / 半导体",
    "title": "Maker builds Mad Max-inspired wall of 100 Noctua PC fans",
    "url": "https://www.tomshardware.com/pc-components/case-fans/maker-builds-mad-max-inspired-wall-of-100-noctua-pc-fans-stress-tests-usd2-355-open-source-openfan-xl-controller",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T16:00:46+00:00",
    "summary": "A wall of 100 Noctua PC fans was built by maker Sasa Karanovic because \"why not\" and to demo his new OpenFAN XL fan controller."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/lenovo-pro-9n-review",
    "domain": "AI 算力 / 半导体",
    "title": "Lenovo Pro 9n review: 18-core RTX Spark in a fancy chassis",
    "url": "https://www.tomshardware.com/laptops/lenovo-pro-9n-review",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T16:00:00+00:00",
    "summary": "The Lenovo Pro 9n is a lighter alternative to the Surface Laptop Ultra, offering a vivid OLED panel and lots of ports, though it shares similar weaknesses, like battery life."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/arm-yourself-against-online-threats-with-30-percent-off-yubikey-5c-nfc-bundles-at-best-buy-at-usd37-per-key-this-deal-could-save-you-more-than-just-cash",
    "domain": "AI 算力 / 半导体",
    "title": "Arm yourself against online threats with 30% off YubiKey 5C NFC bundles at Best Buy",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/arm-yourself-against-online-threats-with-30-percent-off-yubikey-5c-nfc-bundles-at-best-buy-at-usd37-per-key-this-deal-could-save-you-more-than-just-cash",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T15:45:00+00:00",
    "summary": "The YubiKey 5 NFC security key has dropped to an effective $ 37 per key at Best Buy when purchasing a bundle of two. Sporting both Type-A and Type-C flavors, this Black Friday deal could save you more"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/wearable-tech/neuralink-trial-participant-ditches-mouth-stick-to-play-gta-6-with-his-mind-brain-computer-interface-maps-imagined-ring-finger-taps-and-hand-slides-to-a-playstation-5-controller",
    "domain": "AI 算力 / 半导体",
    "title": "Neuralink trial participant ditches mouth stick to play GTA 6 with his mind",
    "url": "https://www.tomshardware.com/peripherals/wearable-tech/neuralink-trial-participant-ditches-mouth-stick-to-play-gta-6-with-his-mind-brain-computer-interface-maps-imagined-ring-finger-taps-and-hand-slides-to-a-playstation-5-controller",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T14:49:48+00:00",
    "summary": "This is one of the most complicated games yet to be played using Neuralink, with the patient using imagined movements like tapping a finger or sliding a hand to simulate commands on the PS5 controller"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/kfc-offers-disc-shaped-fried-chicken-to-sad-disc-less-gta-vi-fans-kfc-spains-the-replacement-disc-campaign-delivers-where-rockstar-disappoints-after-selling-usd3-79-billion-of-gta-vi-without-a-physical-disc",
    "domain": "AI 算力 / 半导体",
    "title": "KFC offers disc-shaped fried chicken to sad disc-less GTA VI fans",
    "url": "https://www.tomshardware.com/video-games/kfc-offers-disc-shaped-fried-chicken-to-sad-disc-less-gta-vi-fans-kfc-spains-the-replacement-disc-campaign-delivers-where-rockstar-disappoints-after-selling-usd3-79-billion-of-gta-vi-without-a-physical-disc",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T14:18:22+00:00",
    "summary": "KFC Spain is offering free fried chicken discs to GTA 6 game owners bringing in their empty game cases as part of its 'The Replacement Disc' campaign."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/ukraine-revives-its-grounded-fleet-of-500-us-made-puma-drones-with-homegrown-anti-jamming-tech-anti-jamming-upgrade-triples-range-to-31-miles",
    "domain": "AI 算力 / 半导体",
    "title": "Ukraine revives its grounded fleet of 500+ US-made Puma drones with homegrown anti-jamming tech",
    "url": "https://www.tomshardware.com/tech-industry/drones/ukraine-revives-its-grounded-fleet-of-500-us-made-puma-drones-with-homegrown-anti-jamming-tech-anti-jamming-upgrade-triples-range-to-31-miles",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T13:51:18+00:00",
    "summary": "The Puma AE reconnaissance drones had been grounded by electromagnetic warfare until they received this upgrade."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/policy/tsmc-reportedly-pauses-shipments-to-chinese-designers-after-u-s-export-rules-flag-decade-old-16nm-and-14nm-nodes-new-bis-controls-threaten-smartphone-tv-and-automotive-chips",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC reportedly pauses shipments to Chinese designers after U.S. export rules flag decade-old 16nm and 14nm nodes",
    "url": "https://www.tomshardware.com/tech-industry/policy/tsmc-reportedly-pauses-shipments-to-chinese-designers-after-u-s-export-rules-flag-decade-old-16nm-and-14nm-nodes-new-bis-controls-threaten-smartphone-tv-and-automotive-chips",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T13:30:00+00:00",
    "summary": "The BIS's IFR says that chip fabs can no longer assume a design's performance based on the specifications provided by their customer."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/mice/logitechs-accomplished-mx-master-3s-productivity-mouse-gets-24-percent-discount-usd75-buys-you-a-tried-and-tested-workhorse-with-killer-features",
    "domain": "AI 算力 / 半导体",
    "title": "Logitech's accomplished MX Master 3S productivity mouse gets 24% discount",
    "url": "https://www.tomshardware.com/peripherals/mice/logitechs-accomplished-mx-master-3s-productivity-mouse-gets-24-percent-discount-usd75-buys-you-a-tried-and-tested-workhorse-with-killer-features",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T13:20:00+00:00",
    "summary": "You can pick up the Logitech MX Master 3S for just $75 at Amazon, just in time for Black Friday. With its signature MagSpeed scrolling, this deal is unmissable for anyone who wants to pick up a mouse "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/ai-agents-design-an-entirely-new-cpu-architecture-from-scratch-startup-claims-frostbite-posts-4-59x-the-performance-per-watt-of-an-in-order-core-in-pre-silicon-tests",
    "domain": "AI 算力 / 半导体",
    "title": "AI agents design an entirely new CPU architecture from scratch, startup claims",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/ai-agents-design-an-entirely-new-cpu-architecture-from-scratch-startup-claims-frostbite-posts-4-59x-the-performance-per-watt-of-an-in-order-core-in-pre-silicon-tests",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T13:00:00+00:00",
    "summary": "Architect Labs says its AI agents designed Frostbite, an interaction-net CPU with 4.59x the performance per watt of an in-order core."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/moore-threads-next-lushan-gaming-gpu-could-pack-a-record-64gb-of-vram-doubles-the-rtx-5090s-32gb-lofty-claims-of-15x-gaming-and-50x-ray-tracing-over-mtt-s80",
    "domain": "AI 算力 / 半导体",
    "title": "Moore Threads' next 'Lushan' gaming GPU could pack a record 64GB of VRAM",
    "url": "https://www.tomshardware.com/pc-components/gpus/moore-threads-next-lushan-gaming-gpu-could-pack-a-record-64gb-of-vram-doubles-the-rtx-5090s-32gb-lofty-claims-of-15x-gaming-and-50x-ray-tracing-over-mtt-s80",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T12:30:00+00:00",
    "summary": "Moore Threads teased its Lushan gaming GPU ahead of MDC 2026, with a product manager claiming record VRAM for a consumer graphics card."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-headsets/one-of-the-best-gaming-headsets-plummets-to-just-usd78-at-amazon-in-unmissable-black-friday-deal-razer-blackshark-v2-pro-outshines-its-successor-at-less-than-half-the-price",
    "domain": "AI 算力 / 半导体",
    "title": "One of the best gaming headsets plummets to just $78 at Amazon in unmissable Black Friday deal",
    "url": "https://www.tomshardware.com/peripherals/gaming-headsets/one-of-the-best-gaming-headsets-plummets-to-just-usd78-at-amazon-in-unmissable-black-friday-deal-razer-blackshark-v2-pro-outshines-its-successor-at-less-than-half-the-price",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T12:20:00+00:00",
    "summary": "One of our favorite gaming headsets just got a killer discount in time for the Holiday season. The PS5 version Razer Blackshark V2 Pro, has been discounted to just $78 at Amazon, meaning that you can "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/lenders-back-spacexs-usd43-billion-nvidia-gpu-deal-but-worry-the-collateral-could-end-up-in-orbit-making-it-impossible-to-reclaim-if-musk-defaults-five-year-hell-or-high-water-lease-may-lack-a-written-earth-only-guarantee",
    "domain": "AI 算力 / 半导体",
    "title": "Lenders back SpaceX's $43 billion Nvidia GPU deal but worry the collateral could end up in orbit, making them impossible to reclaim if Musk defaults",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/lenders-back-spacexs-usd43-billion-nvidia-gpu-deal-but-worry-the-collateral-could-end-up-in-orbit-making-it-impossible-to-reclaim-if-musk-defaults-five-year-hell-or-high-water-lease-may-lack-a-written-earth-only-guarantee",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T12:00:00+00:00",
    "summary": "The $43 billion loan is structured as a unique arrangement in which a different company buys the Nvidia chips, while SpaceX makes quarterly payments to use them."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/energy-companies-deploy-drones-that-can-be-recharged-by-straddling-power-lines-nomad-quadcopter-drones-can-monitor-the-grid-without-ever-returning-home",
    "domain": "AI 算力 / 半导体",
    "title": "Energy companies deploy drones that can be recharged by straddling power lines",
    "url": "https://www.tomshardware.com/tech-industry/drones/energy-companies-deploy-drones-that-can-be-recharged-by-straddling-power-lines-nomad-quadcopter-drones-can-monitor-the-grid-without-ever-returning-home",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T11:30:00+00:00",
    "summary": "NOMADs are drones that can land on live high-voltage lines, charge from the line itself and relocate ready for their next task."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/dev-squeezes-an-ai-language-model-onto-a-floppy-for-486dx-and-pentium-pc-stalwarts-tiny-2-1-needs-540kb-of-memory-and-speaks-via-pc-speaker-is-a-question-answering-transformer-with-367k-parameters",
    "domain": "AI 算力 / 半导体",
    "title": "Dev squeezes an AI language model onto a floppy for 486DX and Pentium PC stalwarts",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/dev-squeezes-an-ai-language-model-onto-a-floppy-for-486dx-and-pentium-pc-stalwarts-tiny-2-1-needs-540kb-of-memory-and-speaks-via-pc-speaker-is-a-question-answering-transformer-with-367k-parameters",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T11:00:00+00:00",
    "summary": "An inspired developer has shoehorned a language model onto a floppy disk created especially for 486DX and Pentium PC users running DOS."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/nas/ditch-cloud-subscriptions-with-a-usd132-discount-on-a-4-bay-ugreen-dxp4800-gt-nas-enclosure-in-amazon-black-friday-deal-offers-dual-10gbe-ports-and-supports-up-to-144tb-of-storage",
    "domain": "AI 算力 / 半导体",
    "title": "Ditch cloud subscriptions with a $132 discount on a 4-Bay NAS enclosure in Amazon Black Friday deal",
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
    "title": "MSI's magnificent 32-inch 4K QD-OLED gaming monitor tumbles to just $569",
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
    "title": "OLED gaming laptop with RTX 5060 and Intel Core Ultra 7 CPU price crashes by $650 in Black Friday offer",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/oled-gaming-laptop-with-rtx-5060-and-intel-core-ultra-7-cpu-price-crashes-by-usd650-in-black-friday-offer-lenovo-legion-5i-laptop-drops-to-usd1-349-with-free-games-at-b-and-h",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T09:05:40+00:00",
    "summary": "Getting a gaming laptop this holiday season doesn't have to mean spending thousands of dollars, as this modestly priced Lenovo Legion 5i OLED gaming laptop has dropped to just $1,349 at B&amp;H."
  },
  {
    "id": "hn:50552424",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Neon",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/",
    "source": "yigitdemirag",
    "platform": "hackernews",
    "points": 1066,
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
    "points": 287,
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
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1039874/walmart-agent-gateway-meta-muse-black-friday",
    "domain": "大厂 AI 动态",
    "title": "Meta Muse can do your Black Friday shopping at Walmart",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1039874/walmart-agent-gateway-meta-muse-black-friday",
    "source": "Jess Weatherbed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T11:00:00+00:00",
    "summary": "Walmart will let Meta's Muse shop on its website on your behalf, allowing the AI agent to find and purchase Black Friday deals. Tomorrow, on Tuesday November 24th, the retail giant will roll out a liv"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1038650/kodak-slidetag-keychain-photo-display-tracker-find-my-hub-google-apple-e-ink",
    "domain": "大厂 AI 动态",
    "title": "Kodak’s next collectible is a tiny digital photo frame that doubles as a tracker",
    "url": "https://www.theverge.com/tech/1038650/kodak-slidetag-keychain-photo-display-tracker-find-my-hub-google-apple-e-ink",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T03:00:00+00:00",
    "summary": "After expanding its Charmera collection with a Millennium Edition featuring Y2K-inspired designs earlier this year, Reto's follow-up to its tiny Kodak camera is an equally small digital photo frame yo"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1039851/major-tech-outages",
    "domain": "大厂 AI 动态",
    "title": "We haven’t seen the last of the major tech outages",
    "url": "https://www.theverge.com/tech/1039851/major-tech-outages",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T22:48:02+00:00",
    "summary": "Over the last week or so, we have seen a nationwide FAA ground stop, a multi-day Outlook outage that brought entire companies to a standstill, and a banking outage at JPMorgan Chase. But the consensus"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/1039779/delta-flights-delayed-system-outage",
    "domain": "大厂 AI 动态",
    "title": "Delta flights in and out of Atlanta delayed due to system outage",
    "url": "https://www.theverge.com/transportation/1039779/delta-flights-delayed-system-outage",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T17:46:44+00:00",
    "summary": "All Delta flights in and out of Atlanta are facing significant delays on Sunday due to a problem with the system that calculates a plane's weight and balance. Hartsfield-Jackson Atlanta International "
  },
  {
    "id": "rss:https://www.theverge.com/games/1039770/binding-of-isaac-ai-music",
    "domain": "大厂 AI 动态",
    "title": "Binding of Isaac developer removes AI music from Repentance Plus",
    "url": "https://www.theverge.com/games/1039770/binding-of-isaac-ai-music",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T17:25:20+00:00",
    "summary": "The Binding of Isaac: Repentance Plus has spent the last few days getting review-bombed on Steam after it was discovered that a particular segment of the game used AI music. Reddit user ShweetsStuff d"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1037313/nintendo-switch-2-game-black-friday-cyber-monday-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Some of our favorite Switch 2 games are cheaper through Black Friday",
    "url": "https://www.theverge.com/gadgets/1037313/nintendo-switch-2-game-black-friday-cyber-monday-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T17:00:00+00:00",
    "summary": "Black Friday is a great time to expand your game library because it’s a chance to catch deals that aren’t normally happening throughout the year. That’s true for Nintendo Switch 2 games, as well. In a"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/1039762/sheherazaad-khudgarzi-review",
    "domain": "大厂 AI 动态",
    "title": "Sheherazaad’s Khudgarzi is gorgeous, ‘genre-chaotic’ South Asian folk",
    "url": "https://www.theverge.com/entertainment/1039762/sheherazaad-khudgarzi-review",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T16:33:29+00:00",
    "summary": "Sheherazaad started making ripples in the music world a few years ago with her EP Qasr, which was produced by Grammy Award winner Arooj Aftab. Now she's back with Khudgarzi, her reverb-drenched folk-n"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1039732/protesters-storm-meta-offices-in-india",
    "domain": "大厂 AI 动态",
    "title": "Protesters storm Meta offices in India",
    "url": "https://www.theverge.com/tech/1039732/protesters-storm-meta-offices-in-india",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T15:15:07+00:00",
    "summary": "Members of the opposition Congress party protested outside Meta's offices in Delhi on Friday and appear to have entered the building in a video shared by CNN. Members of the party's youth wing are dem"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1038181/nintendo-switch-2-black-friday-deal-mario-kart-world-bundle-2026-sale",
    "domain": "大厂 AI 动态",
    "title": "Nintendo’s Switch 2 console is $50 off for Black Friday",
    "url": "https://www.theverge.com/gadgets/1038181/nintendo-switch-2-black-friday-deal-mario-kart-world-bundle-2026-sale",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T14:00:00+00:00",
    "summary": "Those hoping to save some cash on a Nintendo Switch 2 can do so starting today, November 22nd, through Saturday, December 5th, giving you plenty of time to think about it after Cyber Monday has passed"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1038879/off-broadway-love-me-auracast",
    "domain": "大厂 AI 动态",
    "title": "‘The show is starting soon. Please turn on your headphones.’",
    "url": "https://www.theverge.com/tech/1038879/off-broadway-love-me-auracast",
    "source": "John Higgins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T14:00:00+00:00",
    "summary": "Up a few concrete steps and through the front door of a 200-year-old row house in New York City, I follow a crowd of people into the 178-seat SoHo Playhouse. As we filter to our seats, ushers hand eac"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/22/how-notable-capital-gic-and-baillie-gifford-bet-big-on-anthropic-before-its-ipo/",
    "domain": "大厂 AI 动态",
    "title": "How Notable Capital, GIC, and Baillie Gifford bet big on Anthropic before its IPO",
    "url": "https://techcrunch.com/2026/11/22/how-notable-capital-gic-and-baillie-gifford-bet-big-on-anthropic-before-its-ipo/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T01:25:53+00:00",
    "summary": "Three significant backers share what gave them conviction to bet billions on Anthropic."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/22/you-can-see-everything-has-made-more-than-100m-worldwide/",
    "domain": "大厂 AI 动态",
    "title": "‘You Can See Everything’ has made more than $100M worldwide",
    "url": "https://techcrunch.com/2026/11/22/you-can-see-everything-has-made-more-than-100m-worldwide/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T21:42:48+00:00",
    "summary": "The new Elizabeth Holmes documentary is just beginning to roll out internationally."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/22/openais-chief-scientist-has-thoughts-on-how-to-limit-ai-development/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI’s chief scientist has thoughts on how to limit AI development",
    "url": "https://techcrunch.com/2026/11/22/openais-chief-scientist-has-thoughts-on-how-to-limit-ai-development/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T21:14:07+00:00",
    "summary": "To establish a speed limit on AI development, you need to agree on how to measure speed."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/22/as-people-look-for-ways-to-make-new-friends-here-are-the-apps-promising-to-help/",
    "domain": "大厂 AI 动态",
    "title": "The best apps to make new friends right now",
    "url": "https://techcrunch.com/2026/11/22/as-people-look-for-ways-to-make-new-friends-here-are-the-apps-promising-to-help/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T21:00:00+00:00",
    "summary": "We've compiled a list of friendship apps, from friend discovery platforms like BFF to event-focused ones like Timeleft."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/22/why-data-centers-are-at-the-center-of-the-big-tech-backlash/",
    "domain": "大厂 AI 动态",
    "title": "Why data centers are at the center of the Big Tech backlash",
    "url": "https://techcrunch.com/2026/11/22/why-data-centers-are-at-the-center-of-the-big-tech-backlash/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T18:08:43+00:00",
    "summary": "Journalist Paris Marx unpacks his new book \"Hyperscale.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/22/techcrunch-mobility-a-b-testing-robots-vs-humans/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Mobility: A/B testing robots vs. humans",
    "url": "https://techcrunch.com/2026/11/22/techcrunch-mobility-a-b-testing-robots-vs-humans/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T17:06:00+00:00",
    "summary": "Welcome back to TechCrunch Mobility, your hub for the future of transportation and, now more than ever, the role AI is playing in it."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/22/can-a-tv-be-too-large-an-investigation/",
    "domain": "大厂 AI 动态",
    "title": "Can a TV be too large? An investigation",
    "url": "https://techcrunch.com/2026/11/22/can-a-tv-be-too-large-an-investigation/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T15:00:00+00:00",
    "summary": "Can a TV be too large? This writer's recent upgrade to a 65-inch OLED came with some unexpected challenges."
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
    "id": "rss:https://stratechery.com/2026/amazon-earnings-the-chip-question-about-agents/",
    "domain": "大厂 AI 动态",
    "title": "Amazon Earnings, The Chip Question, About Agents",
    "url": "https://stratechery.com/2026/amazon-earnings-the-chip-question-about-agents/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T11:00:00+00:00",
    "summary": "Amazon makes the case they are not like other compute providers, even as they signal the willingness to give up margin to serve the frontier."
  },
  {
    "id": "rss:https://arstechnica.com/reviews/2026/11/review-the-asus-proart-p16-offers-a-glimpse-of-a-future-powered-by-local-ai/",
    "domain": "大厂 AI 动态",
    "title": "Review: The Asus ProArt P16 offers a glimpse of a future powered by local AI",
    "url": "https://arstechnica.com/reviews/2026/11/review-the-asus-proart-p16-offers-a-glimpse-of-a-future-powered-by-local-ai/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T12:00:00+00:00",
    "summary": "The new Asus ProArt laptop costs up to $7,000, but it can run a gaggle of local AI agents."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/11/glp-1-drugs-could-have-a-surprisingly-large-environmental-payoff/",
    "domain": "大厂 AI 动态",
    "title": "GLP-1 drugs could have a surprisingly large environmental payoff",
    "url": "https://arstechnica.com/health/2026/11/glp-1-drugs-could-have-a-surprisingly-large-environmental-payoff/",
    "source": "Roslyn Henry and Peter Alexander, The Conversation",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T12:07:41+00:00",
    "summary": "GLP-1 drugs could cut food demand enough to free farmland larger than Italy."
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/11/review-godzilla-minus-zero-is-everything-we-could-want-in-a-sequel/",
    "domain": "大厂 AI 动态",
    "title": "Review: Godzilla Minus Zero joins the list of truly stellar sequels",
    "url": "https://arstechnica.com/culture/2026/11/review-godzilla-minus-zero-is-everything-we-could-want-in-a-sequel/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-21T22:12:41+00:00",
    "summary": "Director Takashi Yamazaki ups the ante by pitting Godzilla against one of the monster's greatest foes"
  },
  {
    "id": "rss:https://www.producthunt.com/products/visitors",
    "domain": "大厂 AI 动态",
    "title": "Letter Visitors",
    "url": "https://www.producthunt.com/products/visitors",
    "source": "Garry Tan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-22T07:39:42+00:00",
    "summary": "See website visitors on your website itself Discussion | Link"
  },
  {
    "id": "hn:50556287",
    "domain": "股票",
    "title": "Ruby2ßhell: Pre-authentication RCE on stock Rails",
    "url": "https://verialabs.com/ruby2shell/",
    "source": "jdns",
    "platform": "hackernews",
    "points": 407,
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
    "points": 35,
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
    "points": 22,
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
    "points": 787,
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
    "points": 197,
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
    "points": 123,
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
    "id": "hn:50605699",
    "domain": "金融",
    "title": "'It's greed': Zohran Mamdani blasts Amazon over new $5 fee hike in NYC",
    "url": "https://finance.yahoo.com/economy/policy/articles/greed-zohran-mamdani-blasts-amazon-121000124.html",
    "source": "madihaa",
    "platform": "hackernews",
    "points": 51,
    "published_at": "2026-11-23T00:23:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:50594937",
    "domain": "金融",
    "title": "Tesla launches FSD v15, targets its biggest weaknesses, from signs to potholes",
    "url": "https://electrek.co/2026/11/21/tesla-fsd-v15-rollout-25x-safety-reality-view/",
    "source": "m348e912",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-11-22T00:14:05+00:00",
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
    "id": "rss:https://arxiv.org/abs/2611.26649",
    "domain": "金融",
    "title": "VerifiQuant: Governance-by-Execution for Financial LLM Workflows",
    "url": "https://arxiv.org/abs/2611.26649",
    "source": "Yu-Chi Ko, Mi-Yen Yeh, Shou-De Lin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T05:00:00+00:00",
    "summary": "arXiv:2611.26649v1 Announce Type: new Abstract: Large language models embedded in financial workflows fail most dangerously by emitting confident, well-formatted but wrong numbers with no signal disti"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.26652",
    "domain": "金融",
    "title": "Distributional Deep Hedging",
    "url": "https://arxiv.org/abs/2611.26652",
    "source": "El-Amine Cherrat, Skander Kazdaghli, Iordanis Kerenidis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T05:00:00+00:00",
    "summary": "arXiv:2611.26652v1 Announce Type: new Abstract: Deep hedging learns a hedging strategy by optimising a risk preference over a neural-network policy. The preference is fixed before training, so each ne"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.26670",
    "domain": "金融",
    "title": "A Solvency II-Based Framework for Pricing Structural Longevity Risk under an Affine Mortality Model",
    "url": "https://arxiv.org/abs/2611.26670",
    "source": "Madiha Bouhouche (INSEA), Said Khalil (TREE, INSEA), Fadoua Badaoui (INSEA)",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T05:00:00+00:00",
    "summary": "arXiv:2611.26670v1 Announce Type: new Abstract: This paper develops a Solvency II-based pricing framework for structural longevity risk in incomplete longevity markets. The valuation scheme relies on "
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.26673",
    "domain": "金融",
    "title": "Error analysis for the numerical approximation of the quantile hedging problem",
    "url": "https://arxiv.org/abs/2611.26673",
    "source": "Cyril B\\'en\\'ezet, Cyril Nefzaoui-Blanchard, Sergio Pulido",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T05:00:00+00:00",
    "summary": "arXiv:2611.26673v1 Announce Type: new Abstract: We analyse numerical approximations of quantile hedging in complete linear markets with Markovian diffusion dynamics. The problem is formulated as stoch"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.26700",
    "domain": "金融",
    "title": "Held-to-Maturity Accounting: Hidden Losses and Systemic Fragility",
    "url": "https://arxiv.org/abs/2611.26700",
    "source": "Dongxu Li, Steve Y. Yang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T05:00:00+00:00",
    "summary": "arXiv:2611.26700v1 Announce Type: new Abstract: This paper studies how accounting-induced opacity affects systemic risk in the banking system. Motivated by the buildup of unrealized losses during rece"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.26716",
    "domain": "金融",
    "title": "Are Calibrated Decision Models Calibrated on Markets? Geolocated News, Markov Switching and a System One Model for Nasdaq-100 Allocation",
    "url": "https://arxiv.org/abs/2611.26716",
    "source": "Jakub Zaj\\k{a}c, Micha{\\l} Dyrek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T05:00:00+00:00",
    "summary": "arXiv:2611.26716v1 Announce Type: new Abstract: Portfolio allocation is driven by probabilities of losses, not only by forecasts of the direction (up/down) of the market. A decision model such as Jev "
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.26882",
    "domain": "金融",
    "title": "The Rural Margin of Territorial Peace: Within-Municipality Evidence from Colombia",
    "url": "https://arxiv.org/abs/2611.26882",
    "source": "Hector Galindo-Silva",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T05:00:00+00:00",
    "summary": "arXiv:2611.26882v1 Announce Type: new Abstract: Colombia's peace agreement introduced participatory development programs and congressional constituencies reserved for conflict victims with a rural ele"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.27020",
    "domain": "金融",
    "title": "Trust and Lottery-Related Anomalies",
    "url": "https://arxiv.org/abs/2611.27020",
    "source": "Reza Bradrania, Ya Gao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T05:00:00+00:00",
    "summary": "arXiv:2611.27020v1 Announce Type: new Abstract: We examine whether social trust shapes the pricing of lottery-like stocks by influencing investors' beliefs regarding optimistic information associated "
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.27210",
    "domain": "金融",
    "title": "The Rise of Agents and the Human Labor Market",
    "url": "https://arxiv.org/abs/2611.27210",
    "source": "Nicola Borri, Anton Cheremukhin, Yukun Liu, Aleh Tsyvinski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T05:00:00+00:00",
    "summary": "arXiv:2611.27210v1 Announce Type: new Abstract: We provide the first economy-wide and cross-AI model evidence on the effects of agentic AI on labor demand. We combine proprietary OpenRouter data cover"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.27274",
    "domain": "金融",
    "title": "Nonlinear Shrinkage for Higher Moments Estimation in Large Portfolios",
    "url": "https://arxiv.org/abs/2611.27274",
    "source": "Paul Ruelloux, Christian Bongiorno, Damien Challet",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T05:00:00+00:00",
    "summary": "arXiv:2611.27274v1 Announce Type: new Abstract: Portfolio risk is not limited to the variance of returns. The moments of portfolio returns depend directly on the covariance matrix and higher-order co-"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.27485",
    "domain": "金融",
    "title": "Risk sharing for background risk models with infinite mean",
    "url": "https://arxiv.org/abs/2611.27485",
    "source": "Ziting Miao, Yuyu Chen, Han Li",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T05:00:00+00:00",
    "summary": "arXiv:2611.27485v1 Announce Type: new Abstract: Risk sharing is usually viewed as beneficial for risk-averse agents facing independent risks with finite means, but this situation can be reversed for i"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.27505",
    "domain": "金融",
    "title": "Accountable AI Delegation in Banking: Identity, Commitment Controls, Decision Evidence and Recovery",
    "url": "https://arxiv.org/abs/2611.27505",
    "source": "Walter Kurz, Besnik Alidemi, Marco Schmidt",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T05:00:00+00:00",
    "summary": "arXiv:2611.27505v1 Announce Type: new Abstract: An AI-assisted payment can pass assessment and lose release authority before commitment. We specify a banking delegation contract that checks current au"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.27616",
    "domain": "金融",
    "title": "Do Econophysics-Inspired Inputs Improve Neural Covariance Forecasting? A Leakage-Free Walk-Forward Study of Intraday DJIA Data",
    "url": "https://arxiv.org/abs/2611.27616",
    "source": "Gabriele Ranco",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T05:00:00+00:00",
    "summary": "arXiv:2611.27616v1 Announce Type: new Abstract: Tools from econophysics, including Random Matrix Theory (RMT), Tsallis q-Gaussian tails, Hawkes self-excitation and diffusion-inspired regularization, a"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.27692",
    "domain": "金融",
    "title": "Reconstructing risk preferences from data",
    "url": "https://arxiv.org/abs/2611.27692",
    "source": "Anastasis Kratsios, Silvana M. Pesenti, Philipp Zimmermann",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T05:00:00+00:00",
    "summary": "arXiv:2611.27692v1 Announce Type: new Abstract: We consider the problem of reconstructing risk preferences from data. Specifically, for a finite dataset consisting of contingent claims and their evalu"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.26948",
    "domain": "金融",
    "title": "Bottlenecked: The Capital Cost of Protected DeFi Lending",
    "url": "https://arxiv.org/abs/2611.26948",
    "source": "Tarun Chitra, Manvir Schneider, Nagu Thogiti",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T05:00:00+00:00",
    "summary": "arXiv:2611.26948v1 Announce Type: cross Abstract: Securing hundreds of billions of dollars in decentralized finance (DeFi) requires both cryptographically secured collateral and economic capital to ab"
  },
  {
    "id": "rss:https://arxiv.org/abs/2505.14548",
    "domain": "金融",
    "title": "Keeping in Place After the Storm-Emergency Assistance and Evictions",
    "url": "https://arxiv.org/abs/2505.14548",
    "source": "Bilal Islah, Ahmed Zoulati",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T05:00:00+00:00",
    "summary": "arXiv:2505.14548v4 Announce Type: replace Abstract: We offer evidence that federal emergency assistance (FEMA) in the days following natural disasters mitigate evictions in comparison to similar emerg"
  },
  {
    "id": "rss:https://arxiv.org/abs/2507.08244",
    "domain": "金融",
    "title": "Advancing AI Capabilities and Evolving Labor Outcomes",
    "url": "https://arxiv.org/abs/2507.08244",
    "source": "Jacob Dominski, Tyler Boes, Yong Suk Lee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T05:00:00+00:00",
    "summary": "arXiv:2507.08244v4 Announce Type: replace Abstract: This paper examines how labor market outcomes changed across occupations as AI capabilities advanced from chatbots to reasoning models and AI agents"
  },
  {
    "id": "rss:https://arxiv.org/abs/2603.14024",
    "domain": "金融",
    "title": "Capturing cash non-additivity and horizon risk via BSDEs and generalized shortfall",
    "url": "https://arxiv.org/abs/2603.14024",
    "source": "Giulia Di Nunno, Emanuela Rosazza Gianin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T05:00:00+00:00",
    "summary": "arXiv:2603.14024v2 Announce Type: replace Abstract: Whenever dealing with horizons of different times scales, risk evaluation of losses may incur in both interest rate uncertainty and horizon risk as "
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.05291",
    "domain": "金融",
    "title": "Forecasting Realized Volatility with Time Series Foundation Models: A Comparison with Econometric Benchmarks",
    "url": "https://arxiv.org/abs/2607.05291",
    "source": "Alessio Brini",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T05:00:00+00:00",
    "summary": "arXiv:2607.05291v2 Announce Type: replace Abstract: Time series foundation models (TSFMs) are pretrained on large collections of series and forecast a new series without being trained on it. We compar"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.14164",
    "domain": "金融",
    "title": "Science under Threat? A Natural Experiment in Economics",
    "url": "https://arxiv.org/abs/2608.14164",
    "source": "Dominic Rohner, Oliver Vanden Eynde, Philine Widmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T05:00:00+00:00",
    "summary": "arXiv:2608.14164v2 Announce Type: replace Abstract: Academic freedom is under strain worldwide. To study how scholars respond to (perceived) political pressure, we exploit a natural experiment in the "
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.20242",
    "domain": "金融",
    "title": "Markets for Compute and Inference: Structure, Financing, and Risk Transfer",
    "url": "https://arxiv.org/abs/2611.20242",
    "source": "Dr Gabriel Borrageiro",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T05:00:00+00:00",
    "summary": "arXiv:2611.20242v3 Announce Type: replace Abstract: Capacity to run large language models is rented by the accelerator-hour, and their output is sold by the million tokens. Both goods now have publish"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.23354",
    "domain": "金融",
    "title": "AI, Specialization, and the Organization of Knowledge Work: Evidence from Legal Services",
    "url": "https://arxiv.org/abs/2611.23354",
    "source": "Liu Zhang, Mark Esposito, Isabel Yang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T05:00:00+00:00",
    "summary": "arXiv:2611.23354v2 Announce Type: replace Abstract: Artificial intelligence makes specialized knowledge cheaper to use, but its effects on professional-service firms depend on how clients reallocate w"
  },
  {
    "id": "rss:https://arxiv.org/abs/2510.16003",
    "domain": "金融",
    "title": "Rethinking Arrow--Debreu: A New Framework for Exchange",
    "url": "https://arxiv.org/abs/2510.16003",
    "source": "Nizar Riane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T05:00:00+00:00",
    "summary": "arXiv:2510.16003v3 Announce Type: replace-cross Abstract: This paper revisits the Arrow--Debreu general equilibrium framework through the lens of effective trade, emphasizing the distinction between t"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.14325",
    "domain": "金融",
    "title": "Point-in-Time Encoders for Earnings Calls",
    "url": "https://arxiv.org/abs/2611.14325",
    "source": "Alessio Brini",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T05:00:00+00:00",
    "summary": "arXiv:2611.14325v2 Announce Type: replace-cross Abstract: Text encoders turn earnings calls into vectors for search, for language models that answer from retrieved passages, and for forecasting models"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.18531",
    "domain": "金融",
    "title": "Alignment by Socialization: Learning Tradeoffs Under Selection",
    "url": "https://arxiv.org/abs/2611.18531",
    "source": "Thomas Brennan, Andrew W. Lo, Chaoyi Zhao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T05:00:00+00:00",
    "summary": "arXiv:2611.18531v2 Announce Type: replace-cross Abstract: Artificial intelligence (AI) agents are expected to complete tasks while following rules of conduct, but these objectives can conflict. We stu"
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
    "id": "hn:50467087",
    "domain": "电子信息与芯片",
    "title": "Jensen Huang resigns",
    "url": "https://apnews.com/article/nvidia-megaspeed-china-singapore-huang-5403f152a601cf82ce939f1d24fffa0f",
    "source": "lldb",
    "platform": "hackernews",
    "points": 4060,
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
    "id": "hn:50534044",
    "domain": "电子信息与芯片",
    "title": "Jensen Huang says he’s open to returning in first statement since resignation",
    "url": "https://www.cnbc.com/2026/11/17/nvidia-jensen-huang-statement.html",
    "source": "theanonymousone",
    "platform": "hackernews",
    "points": 100,
    "published_at": "2026-11-17T16:40:38+00:00",
    "summary": ""
  }
]
```
