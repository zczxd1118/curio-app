# Curio · 趋势雷达 · 跨域 Top 选稿

> 一次跑完整份简报：从所有领域的合并候选池里，选出 4-5 条跨域 Top 头条 + 备选池。
> 借鉴 Starfan 趋势雷达形态，每条头条含"二维表 + 主编点评"。

---

## 角色

你是 Curio 的**总编辑**——读者把"看全网"的工作交给你，你的责任是：

1. 从今天的所有候选（覆盖 AI / 金融 / 半导体 / 大厂讯息 4 个域）里**精选 4-5 条头条**
2. 每条头条按 **Starfan 二维表式**写：标题 + 引子段 + 已确认/尚属判断 + 主编点评
3. 列一份"备选池"（10-15 条标题级简单解释）

**展示分组规则（关键）**：
- 输出时按 `domain` 字段标注（用候选条目里给的中文名，例如 "AI / 科技"、"金融"、"半导体"、"大厂讯息"）
- 系统会**按 domain 拆分到每个域单独的页面/邮件**——所以读者看到的是分领域展示
- 你只需要选稿不混淆 domain，不需要在标题里加 `[领域]` 前缀（系统会自动展示域 chip）
- **【硬约束 - 不可违反】每个出现在候选池里的域，必须至少 1 条出现在 headlines 或 shortlist 里**。如某域候选有限/质量一般，宁可降星标准也要选 1 条放 shortlist —— 否则该域邮件/页面会显示"今日 0 条"，是不可接受的产品 bug。

---

## 输入（变量替换）

- 今日日期：`2026-09-25`
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
  "date": "2026-09-25",
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
- **跨域均衡**：4 个域里至少覆盖 3 个域。如果某域今天没有"够 4 星"的，可以不选。
- **新颖度优先**：选今天/本周首发的、有数字的、有未来动作的。避免"已知信息再拼装"。
- **跨平台同事件去重**：同一个事件（如某公司 IPO）在 HN + RSS 都出现，**选英文原版/最深度的源**。
- **反偏好**：保留 0-1 条用户可能不爱看但应该看的（标 `is_diverse: true`，可选）。
- **历史反馈优先**：如果用户最近一次反馈说"想多看 X"，至少 1 条头条契合。

### 备选池（10-15 条）
- 不上头条但仍值得知晓的。
- 每条 30-60 字一句话。
- 按 domain 自然分组，先 AI、金融，再 半导体、大厂。

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
    "id": "bvid:BV1BVEs6LENZ",
    "domain": "AI",
    "title": "【2026最新Codex】Codex保姆级完整教程-Codex新手保姆级教程-最强AI助手！从入门到进阶，22分钟速通Codex！【附教程文档安装包】",
    "url": "http://www.bilibili.com/video/av116707129561197",
    "source": "编程大佬陈悠秀",
    "platform": "bilibili",
    "points": 2969106,
    "published_at": "2026-06-07T05:32:32+00:00",
    "summary": "最近Codex的能力越来越全面，变成了Codex四大形态里最强一个。 Codex APP 比起 Claude Code，额度更高，功能更全，免费账户也能用。而且不会出现限速、封号、降智等问题，用过的小伙伴直呼真香。本期视频带来一个Codex APP的完整教程"
  },
  {
    "id": "bvid:BV1E7wtzaEdq",
    "domain": "AI",
    "title": "从 LLM 到 Agent Skill，一期视频带你打通底层逻辑！",
    "url": "http://www.bilibili.com/video/av116227955497963",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 1995951,
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
    "points": 1903974,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1NvRyBzEhq",
    "domain": "AI",
    "title": "全网最全！60分钟全面掌握Claude Code～【附完整文档】",
    "url": "http://www.bilibili.com/video/av116522328524431",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 1594253,
    "published_at": "2026-05-05T14:08:25+00:00",
    "summary": "Claude Code保姆级教学【收藏起来不会错！】\n从上手安装，到高级用法，这期一次讲全～\n花了三周做教程，希望能帮到你嘻嘻，感谢朋友们的三连+关注啦～"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 1331862,
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
    "points": 1277942,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1kX546QEjG",
    "domain": "AI",
    "title": "保姆级Claude Code速成，必学！简单！【附完整文档】",
    "url": "http://www.bilibili.com/video/av116554859545963",
    "source": "数字游牧人",
    "platform": "bilibili",
    "points": 1098207,
    "published_at": "2026-05-11T09:02:15+00:00",
    "summary": "文档链接：https://lcnaoyjp4e3z.feishu.cn/wiki/MtJlwX0B5iy6y9k5GZTcdjSknTd"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 984317,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1aeLqzUE6L",
    "domain": "AI",
    "title": "10分钟讲清楚 Prompt, Agent, MCP 是什么",
    "url": "http://www.bilibili.com/video/av114410228025650",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 891003,
    "published_at": "2025-05-01T09:00:00+00:00",
    "summary": "up的科学星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV1GsY76dEqW",
    "domain": "AI",
    "title": "一口气搞懂Agent到底怎么用！",
    "url": "http://www.bilibili.com/video/av117252103997988",
    "source": "GenJi是真想教会你",
    "platform": "bilibili",
    "points": 814424,
    "published_at": "2026-09-11T11:30:00+00:00",
    "summary": "AI Agent这两年大家都听麻了，但真到上手，claude、codex这些又是注册、又是命令行，人还没踏进Agent大门，就先被劝退了。这期视频我用0门槛的国产Agent——字节旗下的TraeWork，用六个超真实的案例，手把手带你玩转Agent！完整的文字教程和GitHub神级Skill清单，打包放置顶评论了。教程制作不易，觉得有一点点帮助的话，记得一键三连～"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 808640,
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
    "points": 692818,
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
    "points": 590322,
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
    "points": 423696,
    "published_at": "2025-03-13T13:18:09+00:00",
    "summary": "MCP是近期的AI领域的热点，特别是在海外社区获得热烈讨论，每天都有大量MCP工具诞生。本期视频我们从MCP的概念，技术原理，到多场景实战，一个视频看懂MCP的全部内容。\n\n\nMCP官方开源仓库：https://github.com/modelcontextprotocol/servers\nMCP合集网站：  https://smithery.ai/\nVscode下载：https://code.v"
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 384112,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1Zgud6LEoh",
    "domain": "AI",
    "title": "【最新版】小白速通 Codex 教程（含 DeepSeek 接入，无需 ChatGPT 订阅）",
    "url": "http://www.bilibili.com/video/av117070826047031",
    "source": "林粒粒呀",
    "platform": "bilibili",
    "points": 354522,
    "published_at": "2026-08-10T10:54:20+00:00",
    "summary": "Codex 安装 + 上手速通，保姆级教程！\n无需 ChatGPT 订阅，国内直连 DeepSeek"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 296398,
    "published_at": "2025-04-15T00:59:13+00:00",
    "summary": "MCP终极指南 - 带你深入掌握MCP（基础篇）\n\n时间轴：\n01:05 MCP简要介绍\n02:47 安装 MCP Host（Cline）\n03:15 配置 Cline 用的 API Key\n06:01 第一个 MCP 问题\n06:31 概念解释：MCP Server 和 Tool\n09:13 配置 MCP Server\n14:19 使用 MCP Server\n15:24 MCP 交互流程详解\n1"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 295911,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 267386,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 215380,
    "published_at": "2026-04-27T08:51:41+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n   喜欢视频课程的同学一键三连多多支持一下，长按点赞五秒=lv6大佬 可以的发送彩色弹幕哦。\n配套源码项目已打包评论区回复up"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 186867,
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
    "points": 182068,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1RNTtzMENj",
    "domain": "AI",
    "title": "从零编写MCP并发布上线，超简单！手把手教程",
    "url": "http://www.bilibili.com/video/av114630814862349",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 157542,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1fVhx67EgU",
    "domain": "AI",
    "title": "Opus 5.5、GPT-6 Sol首发实测，Claude再次统治世界？！",
    "url": "http://www.bilibili.com/video/av117319095293268",
    "source": "GenJi是真想教会你",
    "platform": "bilibili",
    "points": 155771,
    "published_at": "2026-09-23T13:48:37+00:00",
    "summary": "北京时间9月23日凌晨，Anthropic和OpenAI前后脚放大招：Claude Opus 5.5、GPT-6 Sol、GPT-6 Luna同夜发布，主打更快更强更便宜，GPT-6 Luna的输入输出价格甚至比DeepSeek还低！是新王登基，还是参数游戏？我们连夜用5个硬核案例当场实测！本期不含任何广告。全部案例的提示词、工具清单都打包成了文档，放在置顶评论区，三连后免费自取。点赞过2万，就再"
  },
  {
    "id": "bvid:BV1WWYE6LEzx",
    "domain": "AI",
    "title": "黑马程序员2026全网最夯VibeCoding零基础入门到实战项目开发全套视频教程，AI辅助编程从入门到实战，涵盖Claude Code、DeepSeek等内容",
    "url": "http://www.bilibili.com/video/av117251667724450",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 137802,
    "published_at": "2026-09-14T01:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260914\n2026黑马程序员AI智能应用开发学习路线图\nhttps://www.bilibili.com/opus/1156896913511940102\n如何下载资料\nhttps://www.bilibili.com/read/cv7881295/\n学习+球球群625260577，告别孤单，共同进步！\n\n【AI智能"
  },
  {
    "id": "bvid:BV1iH8Y6wE5s",
    "domain": "AI",
    "title": "【Re:从零开始的AI学习】安装你的第一个 Agent",
    "url": "http://www.bilibili.com/video/av117148403893835",
    "source": "卡普迪姆",
    "platform": "bilibili",
    "points": 134692,
    "published_at": "2026-08-24T03:43:53+00:00",
    "summary": "毕业论文还有 4 天 DDL 没写完怎么办？我选择更一期 Re0 AI！\n重要的事情说三遍，这期真的没有广告，当然 Workbuddy 官方看到觉得做得好的话，给我赞助一下也不是不行哈～\n\n下一期，让我们写出第一个程序！欢迎三连催更！\n\n▷ 下一期「程序，才是 AI 最趁手的工具」\nBV1dQtx66E9K\n\n━━━━━━━━━━━━━━━━\n【关于这个系列】\n现在的 AI 相关话题很多都脱离现实"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 123343,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 93787,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1uEK96HEWQ",
    "domain": "AI",
    "title": "claude code最舒适的图形化软件？给你codex一般的体验感",
    "url": "http://www.bilibili.com/video/av116834065976655",
    "source": "树雨自莺莺",
    "platform": "bilibili",
    "points": 82972,
    "published_at": "2026-06-29T15:21:05+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1H1eH6DExE",
    "domain": "AI",
    "title": "零基础入门vibe coding！如何搭建自己的工作台？附指令模版",
    "url": "http://www.bilibili.com/video/av117275877184803",
    "source": "Iris学姐",
    "platform": "bilibili",
    "points": 79965,
    "published_at": "2026-09-16T10:00:00+00:00",
    "summary": "零基础如何入门vibe coding？手把手教你用豆包工作搭建你的专属AI工作台！全程不用写一行代码，零基础的同学也完全能跟上~"
  },
  {
    "id": "bvid:BV1K6YM69ESq",
    "domain": "AI",
    "title": "AI+网络安全实战：从Agent入门到AI智能体挖漏洞教程！网络安全|信息安全|黑客技术|渗透测试|SRC漏洞挖掘|AI审计|HVV护网行动|靶场练习-码士集团",
    "url": "http://www.bilibili.com/video/av117247037213495",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 79048,
    "published_at": "2026-09-10T13:47:24+00:00",
    "summary": "这套课程围绕「AI+网络安全」展开，从AI智能体基础入门，到WorkBuddy、Trae等主流Agent工具的实际应用，再到API-Key接入、Skill使用等核心能力，逐步进入AI漏洞挖掘、代码审计、CTF题目分析等安全实战场景。同时结合SRC漏洞挖掘、HVV护网、安全竞赛以及网络安全就业方向，帮助你系统了解AI在网络安全学习、开发与实战中的应用方式。适合网络安全初学者、安全从业者以及希望利用A"
  },
  {
    "id": "bvid:BV1XnuGzfEp7",
    "domain": "AI",
    "title": "让你手中的AI好用10倍！5个好玩实用的MCP推荐，让你不只会用AI搜索",
    "url": "http://www.bilibili.com/video/av114835262018810",
    "source": "田同学Tino",
    "platform": "bilibili",
    "points": 75248,
    "published_at": "2025-07-12T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1U8d8BzEUK",
    "domain": "AI",
    "title": "建议收藏 | 51万行源码真相，ClaudeCode架构深度解读，深度复盘四大约束架构与8大设计模式，揭秘工业级Agent如何解决上下文爆炸与成本失控",
    "url": "http://www.bilibili.com/video/av116413847044339",
    "source": "赋范课堂",
    "platform": "bilibili",
    "points": 70439,
    "published_at": "2026-04-16T10:20:18+00:00",
    "summary": "ClaudeCode源码深度解读，揭秘Agent真正的秘密武器：拆解51万行工程源码，解析四大约束架构与8种设计模式，掌握工业级Agent从Demo到可靠产品的核心演进路径，助你重塑AI开发底层思维。"
  },
  {
    "id": "bvid:BV1VL3F6pE9K",
    "domain": "AI",
    "title": "0基础入门智能体agent测试：AI测试基础+AI智能体(Agent)测试从零入门全攻略，2026最新版！",
    "url": "http://www.bilibili.com/video/av116991151113881",
    "source": "黑马测试",
    "platform": "bilibili",
    "points": 59681,
    "published_at": "2026-07-27T09:19:37+00:00",
    "summary": "还在卷传统软件测试？2026年必学的AI智能体(Agent)测试来了！本期视频专为0基础小白打造，从软件测试基础讲起...若要本视频配套资源笔记可加up主企微（请看置顶留言最后一句话）。"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 55448,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1LXhc6yEkc",
    "domain": "AI",
    "title": "昔涟/Cyrene-Agent 安装配置/演示教程",
    "url": "http://www.bilibili.com/video/av117164694570292",
    "source": "Playa0",
    "platform": "bilibili",
    "points": 50087,
    "published_at": "2026-08-27T00:43:58+00:00",
    "summary": "v1.1.6安装包：\n夸克网盘：\n链接：https://pan.quark.cn/s/43ff3db459f4?pwd=SD2k\n提取码：SD2k\ngithub仓库：\nPlaya-0v0/Cyrene-Agent: An open-source AI desktop companion inspired by Cyrene, combining immersive Chat, personaliz"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 48579,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1AJen6SEVQ",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Agent智能体】教程！大模型入门到进阶，一套全解决！Agentic AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av117274400790619",
    "source": "吴恩达Agent",
    "platform": "bilibili",
    "points": 44962,
    "published_at": "2026-09-15T09:48:26+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n1. 构建智能体设计模式：反射、工具使用、规划与多智能体工作流；\n2. 将人工智能与外部工具集成：数据库、API、网络搜索与代码执行；\n3. 评估并优化人工智能系统：性能指标、错误分析与生产部署\n4、使用开放标准格式和最佳实践创建可重复使用的技能，并组合以创建复杂的工作流程。\n5、建立定制代码生成技能，审核你的代"
  },
  {
    "id": "bvid:BV1ApYD6KEkD",
    "domain": "AI",
    "title": "马斯克收购Cursor后，Cursor的性价比现在已经爆表",
    "url": "http://www.bilibili.com/video/av117254955993228",
    "source": "jopatk",
    "platform": "bilibili",
    "points": 44642,
    "published_at": "2026-09-11T23:19:58+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1uVSUBkEfZ",
    "domain": "AI",
    "title": "Microsoft Copilot完整教程(上) 从入门到Agent 一站式掌握AI办公",
    "url": "http://www.bilibili.com/video/av116351721084069",
    "source": "星小脉",
    "platform": "bilibili",
    "points": 34742,
    "published_at": "2026-04-05T11:00:20+00:00",
    "summary": "2026年最全面的Microsoft Copilot教程上半部分。从Copilot首页入门到Agent深度解析，涵盖搜索、资料库、AI视频生成、Copilot Pages、PowerPoint智能幻灯片等全部功能。由培训了6万人的AI顾问Cherie Brock与Sabrina Ramonov联合讲解。"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 34391,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29777,
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
    "points": 28957,
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
    "points": 23097,
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
    "points": 22797,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 16999,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV12vhx6AEBJ",
    "domain": "AI",
    "title": "Vibe Coding全套教程（Claude Code+Codex+Hermes Agent+Dify+Coze）带你手把手使用AI快速做项目！让你彻底解放双手",
    "url": "http://www.bilibili.com/video/av117318793300698",
    "source": "AI大模型技术",
    "platform": "bilibili",
    "points": 15370,
    "published_at": "2026-09-23T06:10:42+00:00",
    "summary": "学会使用AI编程工具，让你彻底解放双手！"
  },
  {
    "id": "bvid:BV1oQYL64EJV",
    "domain": "AI",
    "title": "【SRC漏洞挖掘】2026最适合新手的AI+自动化挖漏洞教程，从环境搭建到漏洞验证，手把手带你挖到第一个SRC漏洞！",
    "url": "http://www.bilibili.com/video/av117251248490748",
    "source": "阿盾聊安全",
    "platform": "bilibili",
    "points": 15337,
    "published_at": "2026-09-11T07:39:16+00:00",
    "summary": "这套 18 节教程带你从零跑通 AI 自动化挖漏洞全流程：环境搭建、Hermes部署、Burp/Nuclei 集成、资产侦察、漏洞发现到报告验证，一套打通。\n适合有 Web 安全基础、想从手动挖洞升级到自动化的同学。\n资料和工具包见评论区，三连不迷路。"
  },
  {
    "id": "bvid:BV1wqeb6gEDY",
    "domain": "AI",
    "title": "Claude Code 百分百不封号",
    "url": "http://www.bilibili.com/video/av117297150694473",
    "source": "DUNHKPcc",
    "platform": "bilibili",
    "points": 15192,
    "published_at": "2026-09-19T10:14:15+00:00",
    "summary": "如果需要文档，私信主播，主页送免费的token"
  },
  {
    "id": "bvid:BV1MAYd6sEZh",
    "domain": "AI",
    "title": "效率翻倍， 一次讲透AI Agent的用法和技巧",
    "url": "http://www.bilibili.com/video/av117258059847877",
    "source": "数码旭",
    "platform": "bilibili",
    "points": 12251,
    "published_at": "2026-09-12T12:33:07+00:00",
    "summary": "AI Agent作为今年AI应用方式最大的变化，会给普通人带来突破性的效率提升，当然也给我带来的特别大的帮助。我希望通过这期长视频，能帮助你提升工作效率。"
  },
  {
    "id": "hn:49724881",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia announces native GPU programming in Rust",
    "url": "https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/",
    "source": "nonmaskable",
    "platform": "hackernews",
    "points": 970,
    "published_at": "2026-09-16T11:15:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:49673098",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia is the central bank of AI",
    "url": "https://www.economist.com/interactive/briefing/2026/09/03/nvidia-is-the-central-bank-of-ai",
    "source": "tolugenius",
    "platform": "hackernews",
    "points": 584,
    "published_at": "2026-09-12T15:08:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:49824864",
    "domain": "AI 算力 / 半导体",
    "title": "Virtio-nvgpu: Near-native Nvidia GPU access inside a KVM guest",
    "url": "https://github.com/nestrilabs/virtio-nvgpu",
    "source": "WanjohiRyan",
    "platform": "hackernews",
    "points": 151,
    "published_at": "2026-09-24T01:02:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:49682319",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia dismisses \"circular financing\", says every $1 it invests brings back $100",
    "url": "https://invezz.com/news/2026/09/11/nvidia-says-every-1-it-invests-brings-back-100-so-why-does-the-stock-keep-falling/",
    "source": "mgh2",
    "platform": "hackernews",
    "points": 138,
    "published_at": "2026-09-13T10:29:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:49714096",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC revealing details about next gen A14 node",
    "url": "https://iedm26.mapyourshow.com/8_0/sessions/session-details.cfm?scheduleid=331",
    "source": "osnium123",
    "platform": "hackernews",
    "points": 128,
    "published_at": "2026-09-15T15:31:55+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/balancing-bandwidth-range-and-power-in-intelligent-buildings/",
    "domain": "AI 算力 / 半导体",
    "title": "Balancing Bandwidth, Range, and Power in Intelligent Buildings",
    "url": "https://www.eetimes.com/balancing-bandwidth-range-and-power-in-intelligent-buildings/",
    "source": "Andy McFarlane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T08:00:34+00:00",
    "summary": "As edge AI transforms smart buildings, Wi-Fi HaLow bridges the gap between bandwidth, long range, and low power. The post Balancing Bandwidth, Range, and Power in Intelligent Buildings appeared first "
  },
  {
    "id": "rss:https://www.eetimes.com/delos-data-targets-heterogeneous-ai-with-data-interface/",
    "domain": "AI 算力 / 半导体",
    "title": "Delos Data Targets Heterogeneous AI with Data Interface",
    "url": "https://www.eetimes.com/delos-data-targets-heterogeneous-ai-with-data-interface/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T18:43:38+00:00",
    "summary": "Delos’s Apollo chiplet is designed to bridge different endpoint semantics and interconnects, creating a low-latency domain spanning GPUs, accelerators, CPUs and memory The post Delos Data Targets Hete"
  },
  {
    "id": "rss:https://www.eetimes.com/inside-tsmcs-evolving-design-ecosystem-shaping-the-future-of-ai-with-ai/",
    "domain": "AI 算力 / 半导体",
    "title": "Inside TSMC’s Evolving Design Ecosystem: Shaping the Future of AI, with AI",
    "url": "https://www.eetimes.com/inside-tsmcs-evolving-design-ecosystem-shaping-the-future-of-ai-with-ai/",
    "source": "Aveek Sarkar, Director, Ecosystem and Alliance Management Division, TSMC",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T14:10:55+00:00",
    "summary": "TSMC shares updates about the Open Innovation Platform Ecosystem and vision for enabling AI-driven agentic workflows using TSMC AI Design Kit The post Inside TSMC’s Evolving Design Ecosystem: Shaping "
  },
  {
    "id": "rss:https://www.eetimes.com/after-ionq-buyout-skywater-reiterates-role-as-quantum-foundry/",
    "domain": "AI 算力 / 半导体",
    "title": "After IonQ Buyout, SkyWater Reiterates Role as Quantum Foundry",
    "url": "https://www.eetimes.com/after-ionq-buyout-skywater-reiterates-role-as-quantum-foundry/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T14:08:18+00:00",
    "summary": "As SkyWater scales its 200-mm and 300-mm manufacturing platforms to support diverse quantum modalities, leadership emphasizes that protecting customer IP remains its top priority. The post After IonQ "
  },
  {
    "id": "rss:https://www.eetimes.com/tis-october-price-hike-how-to-secure-adi-ti-stock-without-the-panic/",
    "domain": "AI 算力 / 半导体",
    "title": "TI’s October Price Hike: How to Secure ADI/TI Stock Without the Panic",
    "url": "https://www.eetimes.com/tis-october-price-hike-how-to-secure-adi-ti-stock-without-the-panic/",
    "source": "Skyeast International Group Limited",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T10:23:24+00:00",
    "summary": "acing TI's October price hike? SKYEAST offers $30M+ ADI/TI spot stock, 2-hour quotes, and 7×24 support across time zones. Lock in supply now. The post TI&#8217;s October Price Hike: How to Secure ADI/"
  },
  {
    "id": "rss:https://www.eetimes.com/semicon-india-2026-startup-mitra-sheds-light-on-early-stage-silicon-startup-funding/",
    "domain": "AI 算力 / 半导体",
    "title": "SEMICON India 2026: Startup Mitra Sheds Light on Early-Stage Silicon Startup Funding",
    "url": "https://www.eetimes.com/semicon-india-2026-startup-mitra-sheds-light-on-early-stage-silicon-startup-funding/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T08:15:06+00:00",
    "summary": "Indian semiconductor startups are seeking capital beyond seed rounds as they advance from prototypes and tape-out toward volume production. The post SEMICON India 2026: Startup Mitra Sheds Light on Ea"
  },
  {
    "id": "rss:https://www.eetimes.com/from-qubits-to-workflows-rethinking-quantum-computing/",
    "domain": "AI 算力 / 半导体",
    "title": "From Qubits to Workflows: Rethinking Quantum Computing",
    "url": "https://www.eetimes.com/from-qubits-to-workflows-rethinking-quantum-computing/",
    "source": "Kevin Hein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T19:00:00+00:00",
    "summary": "IBM’s quantum-centric push makes QPUs another accelerator in hybrid AI-HPC workflows. The post From Qubits to Workflows: Rethinking Quantum Computing appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/semicon-india-2026-india-starts-packaging-chips-as-ecosystem-takes-shape/",
    "domain": "AI 算力 / 半导体",
    "title": "SEMICON India 2026: India Starts Packaging Chips as Ecosystem Takes Shape",
    "url": "https://www.eetimes.com/semicon-india-2026-india-starts-packaging-chips-as-ecosystem-takes-shape/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T10:56:15+00:00",
    "summary": "India moves five chip packaging plants into production as $13.5 billion ISM 2.0 expands manufacturing, design, and engineering capabilities. The post SEMICON India 2026: India Starts Packaging Chips a"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/australian-pm-says-openai-took-84-days-to-email-agency-after-agent-hacked-its-national-health-care-portal-incident-is-believed-to-be-the-first-known-case-of-ai-breaching-a-government-site",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI agent got into Australia's Medicare stats portal with 84-day notification delay",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/australian-pm-says-openai-took-84-days-to-email-agency-after-agent-hacked-its-national-health-care-portal-incident-is-believed-to-be-the-first-known-case-of-ai-breaching-a-government-site",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T20:34:31+00:00",
    "summary": "Australia says an OpenAI agent got past blocks on a Medicare statistics portal in June. OpenAI's notification arrived in September."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/console-gaming/sony-patent-could-turn-playstation-controllers-into-tap-to-pay-credit-card-terminals-nfc-and-bluetooth-also-support-phones-and-gift-cards-for-instant-purchases",
    "domain": "AI 算力 / 半导体",
    "title": "Sony patent could turn PlayStation controllers into tap-to-pay credit card terminals",
    "url": "https://www.tomshardware.com/video-games/console-gaming/sony-patent-could-turn-playstation-controllers-into-tap-to-pay-credit-card-terminals-nfc-and-bluetooth-also-support-phones-and-gift-cards-for-instant-purchases",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T17:09:31+00:00",
    "summary": "A new patent application details the potential for a future PlayStation controller to accept payments via credit cards and gift cards."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/nvidia-ceo-says-we-have-to-shut-the-labs-down-if-ai-experiments-are-unsafe-jensen-huang-says-frontier-ai-lab-fears-are-a-distraction-not-a-call-for-regulation",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia CEO says 'we have to shut the labs down' if AI experiments are unsafe",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/nvidia-ceo-says-we-have-to-shut-the-labs-down-if-ai-experiments-are-unsafe-jensen-huang-says-frontier-ai-lab-fears-are-a-distraction-not-a-call-for-regulation",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T15:24:49+00:00",
    "summary": "In a recent interview, Nvidia CEO Jensen Huang said that if frontier labs have unsafe models, they should shut the labs down, calling the current calls for regulation a \"distraction.\""
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/japanese-used-bookstores-see-5x-sales-surge-as-books-are-being-bought-by-the-ton-one-50-ton-order-sent-to-the-us-for-ai-scanning-and-destruction-multitude-of-suspicious-bulk-buys-thought-to-end-up-in-foreign-ai-scan-and-shred-facilities",
    "domain": "AI 算力 / 半导体",
    "title": "Japanese used bookstores see 5x sales surge as books are being bought by the ton, one 50-ton order sent to the US for AI scanning and destruction",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/japanese-used-bookstores-see-5x-sales-surge-as-books-are-being-bought-by-the-ton-one-50-ton-order-sent-to-the-us-for-ai-scanning-and-destruction-multitude-of-suspicious-bulk-buys-thought-to-end-up-in-foreign-ai-scan-and-shred-facilities",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T14:35:12+00:00",
    "summary": "Investigators reckon Japan's used bookstore boom is likely due to the written-word harvesting of foreign AI giants."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/microphones/logitech-refreshes-legendary-blue-yeti-microphone-with-3d-voice-tracking-and-ai-denoising-usd160-blue-yeti-2-sequel-features-real-time-auto-gain-and-color-mascot-screen",
    "domain": "AI 算力 / 半导体",
    "title": "Logitech refreshes legendary Blue Yeti microphone with 3D voice tracking and AI denoising",
    "url": "https://www.tomshardware.com/peripherals/microphones/logitech-refreshes-legendary-blue-yeti-microphone-with-3d-voice-tracking-and-ai-denoising-usd160-blue-yeti-2-sequel-features-real-time-auto-gain-and-color-mascot-screen",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T14:00:00+00:00",
    "summary": "After years without a major successor, Logitech’s Yeti 2 arrives with new features designed to simplify microphone setup and audio adjustments."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/the-three-pronged-future-of-custom-pc-building-from-repurposing-forgotten-parts-to-ultra-premium-works-of-gaming-art",
    "domain": "AI 算力 / 半导体",
    "title": "The three-pronged future of custom PC building — from repurposing forgotten parts to ultra-premium works of gaming art",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/the-three-pronged-future-of-custom-pc-building-from-repurposing-forgotten-parts-to-ultra-premium-works-of-gaming-art",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T13:30:00+00:00",
    "summary": "This is probably the worst time ever for PC building. Here’s how and why I think the hobby (and the market) still have a future to look forward to."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/leading-semiconductor-analyst-accuses-amd-of-treason-over-restricted-chips-availability-in-china-amd-blames-diversion-of-export-controlled-rfsoc-usd36-000-radar-silicon-allegedly-quoted-at-usd1-000-for-crowdfunding-project",
    "domain": "AI 算力 / 半导体",
    "title": "Leading semiconductor analyst says AMD should be investigated for 'treason' over availability of restricted chips in China",
    "url": "https://www.tomshardware.com/tech-industry/leading-semiconductor-analyst-accuses-amd-of-treason-over-restricted-chips-availability-in-china-amd-blames-diversion-of-export-controlled-rfsoc-usd36-000-radar-silicon-allegedly-quoted-at-usd1-000-for-crowdfunding-project",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T13:00:44+00:00",
    "summary": "Top semiconductor analysis firm accuses AMD of treason, AMD says it could have been 'diversion' of an export-controlled adaptable radio platform."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/air-cooling/deepcool-ak620-and-ak400-g2-review",
    "domain": "AI 算力 / 半导体",
    "title": "GMKtec Evo-X3 review: Strix Halo in a brand new suit",
    "url": "https://www.tomshardware.com/pc-components/air-cooling/deepcool-ak620-and-ak400-g2-review",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T13:00:00+00:00",
    "summary": "GMKtec has radically remodeled its AMD Strix Halo flagship AI mini PC. The statuesque redesign looks more premium and stays cool and quiet, but the Evo-X3 is around twice the price of the Evo-X2, with"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/save-usd149-on-this-3-item-gaming-combo-from-newegg-usd1-050-buys-a-ryzen-7-9800x3d-32gb-of-corsair-ddr5-ram-asus-tuf-gaming-x870e-plus-motherboard-and-a-free-240mm-aio-and-amd-game-bundle",
    "domain": "AI 算力 / 半导体",
    "title": "Save $149 on this 3-item gaming combo from Newegg",
    "url": "https://www.tomshardware.com/pc-components/save-usd149-on-this-3-item-gaming-combo-from-newegg-usd1-050-buys-a-ryzen-7-9800x3d-32gb-of-corsair-ddr5-ram-asus-tuf-gaming-x870e-plus-motherboard-and-a-free-240mm-aio-and-amd-game-bundle",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T12:45:00+00:00",
    "summary": "Fight back against the RAMpocolypse with this 3-item Newegg combo that features the Ryzen 7 9800X3D, 32GB Corsair Vengeance RAM, and Asus TUF X870E motherboard for only $1,050, a $149 savings"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/micron-discontinues-2gb-gddr7-chips-for-gaming-gpus-as-it-pivots-toward-higher-density-memory-for-ai-chipmaker-reportedly-pivots-to-high-margin-3gb-silicon-for-ai-gpus",
    "domain": "AI 算力 / 半导体",
    "title": "Micron discontinues 2GB GDDR7 chips for gaming GPUs as it pivots toward higher-density memory for AI",
    "url": "https://www.tomshardware.com/pc-components/ram/micron-discontinues-2gb-gddr7-chips-for-gaming-gpus-as-it-pivots-toward-higher-density-memory-for-ai-chipmaker-reportedly-pivots-to-high-margin-3gb-silicon-for-ai-gpus",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T12:30:00+00:00",
    "summary": "Micron is reportedly ending production of its 2GB GDDR7 chips, shifting attention toward higher-density 3GB parts used in more lucrative professional and AI-focused GPUs."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/asml-says-its-sells-absolutely-nothing-in-europe-calls-on-eu-to-help-create-demand",
    "domain": "AI 算力 / 半导体",
    "title": "ASML says it sold 'absolutely nothing' in Europe in 2026",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/asml-says-its-sells-absolutely-nothing-in-europe-calls-on-eu-to-help-create-demand",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T12:10:00+00:00",
    "summary": "ASML calls EU authorities to help create demand for European chips as Europe's share in its revenue drops to 0% in 2026."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/lucky-3d-artist-scores-jensen-huang-signed-rtx-5090-from-used-marketplace-unused-asus-rog-astra-white-oc-expected-to-fetch-usd10-000-to-usd15-000-at-auction",
    "domain": "AI 算力 / 半导体",
    "title": "Lucky 3D artist scores Jensen Huang-signed RTX 5090 from used marketplace that's worth up to $15,000",
    "url": "https://www.tomshardware.com/pc-components/gpus/lucky-3d-artist-scores-jensen-huang-signed-rtx-5090-from-used-marketplace-unused-asus-rog-astra-white-oc-expected-to-fetch-usd10-000-to-usd15-000-at-auction",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T11:50:00+00:00",
    "summary": "A 3D artist looking to build a new workstation bought this RTX 5090 off of a used marketplace expecting a unit autographed by an Asus executive. But when they opened the box of the GPU, they were surp"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/china-swiped-f-35-stealth-fighter-parts-that-were-diverted-through-hong-kong-rerouted-ups-cargo-triggers-military-investigation-stealth-coating-recipe-feared-compromised-despite-pentagon-downplaying-mishap",
    "domain": "AI 算力 / 半导体",
    "title": "China swiped classified F-35 stealth fighter parts that were diverted through Hong Kong",
    "url": "https://www.tomshardware.com/tech-industry/china-swiped-f-35-stealth-fighter-parts-that-were-diverted-through-hong-kong-rerouted-ups-cargo-triggers-military-investigation-stealth-coating-recipe-feared-compromised-despite-pentagon-downplaying-mishap",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T11:40:00+00:00",
    "summary": "Components from the one of the free world’s most advanced fighter jets are now in the possession of the Chinese, say reports."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/wici-one-unveils-wireless-wi-fi-7-egpu-with-built-in-4tb-ssd-for-local-ai-usd1-999-box-leverages-wifi-7-to-present-a-remote-card-as-local",
    "domain": "AI 算力 / 半导体",
    "title": "New wireless Wi-Fi 7 external GPU box comes with a built-in 4TB SSD for local AI",
    "url": "https://www.tomshardware.com/pc-components/gpus/wici-one-unveils-wireless-wi-fi-7-egpu-with-built-in-4tb-ssd-for-local-ai-usd1-999-box-leverages-wifi-7-to-present-a-remote-card-as-local",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T11:25:00+00:00",
    "summary": "WiCi wireless external GPU with onboard storage puts AI workloads reach of local machines via WiFi 7."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/chinas-ultimate-gaming-gpu-hits-a-performance-wall-lx-7g100-barely-crawls-past-amds-nine-year-old-rx-580",
    "domain": "AI 算力 / 半导体",
    "title": "China’s ultimate gaming GPU hits a performance wall",
    "url": "https://www.tomshardware.com/pc-components/gpus/chinas-ultimate-gaming-gpu-hits-a-performance-wall-lx-7g100-barely-crawls-past-amds-nine-year-old-rx-580",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T11:00:00+00:00",
    "summary": "The latest review of the Lisuan Tech LX 7G100 shows performance comparable to AMD's Radeon RX 580 but trails the GeForce RTX 2060."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/british-columbia-sues-openai-to-pay-for-new-school-after-tumbler-ridge-shooting-lawsuit-says-openai-identified-shooters-chatgpt-account-eight-months-prior-but-didnt-warn-police",
    "domain": "AI 算力 / 半导体",
    "title": "British Columbia sues OpenAI and Sam Altman for 'aiding and abetting' school shooter",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/british-columbia-sues-openai-to-pay-for-new-school-after-tumbler-ridge-shooting-lawsuit-says-openai-identified-shooters-chatgpt-account-eight-months-prior-but-didnt-warn-police",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T10:30:00+00:00",
    "summary": "B.C. is demanding compensation after it says OpenAI's reviewers wanted to call police about the Tumbler Ridge shooter before the attack."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/save-a-solid-usd150-on-this-vivid-27-inch-msi-oled-monitor-with-fast-240hz-refresh-rate-now-usd359-this-mag-qd-oled-model-is-close-to-its-lowest-price-ever-on-newegg",
    "domain": "AI 算力 / 半导体",
    "title": "Save big on this vivid 27-inch OLED monitor with fast 240Hz refresh rate",
    "url": "https://www.tomshardware.com/pc-components/save-a-solid-usd150-on-this-vivid-27-inch-msi-oled-monitor-with-fast-240hz-refresh-rate-now-usd359-this-mag-qd-oled-model-is-close-to-its-lowest-price-ever-on-newegg",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T10:20:00+00:00",
    "summary": "Get this MSI 27-inch 4K QD-OLED monitor for just $359. Enjoy vibrant colors, true blacks, a 240Hz refresh rate, and ultra-fast response time —perfect for gaming and productivity, and one of the best d"
  },
  {
    "id": "rss:https://www.tomshardware.com/service-providers/samsungs-disastrous-firmware-update-breaks-refrigerators-ahead-of-south-korean-holiday-customers-complain-of-non-functioning-units-food-spoilage-ahead-of-three-day-celebration",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung's disastrous firmware update bricks refrigerators ahead of South Korean holiday",
    "url": "https://www.tomshardware.com/service-providers/samsungs-disastrous-firmware-update-breaks-refrigerators-ahead-of-south-korean-holiday-customers-complain-of-non-functioning-units-food-spoilage-ahead-of-three-day-celebration",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T10:00:00+00:00",
    "summary": "A broken Samsung update left many refrigerators stuck and non-functional. The incident, which happened right before a major holiday, has many users complaining of spoiled food and a ruined holiday."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/cyberpowerpc-lands-rare-rtx-50-series-founders-edition-cards-in-discounted-walmart-rigs-complete-rtx-5090-pc-costs-usd2-400-less-than-a-standalone-gpu",
    "domain": "AI 算力 / 半导体",
    "title": "CyberPowerPC lands rare RTX 50-series Founders Edition cards in discounted Walmart rigs",
    "url": "https://www.tomshardware.com/pc-components/gpus/cyberpowerpc-lands-rare-rtx-50-series-founders-edition-cards-in-discounted-walmart-rigs-complete-rtx-5090-pc-costs-usd2-400-less-than-a-standalone-gpu",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T09:30:00+00:00",
    "summary": "CyberPowerPC is offering five different pre-built gaming PCs with either an RTX 5070, 5080, or 5090 Founders Edition GPUs paired with either an Intel or AMD X3D CPU. They also come with 32GB of DDR5 R"
  },
  {
    "id": "rss:https://www.tomshardware.com/tablets/microsoft-surface/microsoft-brings-snapdragon-x2-plus-to-13-inch-surface-laptop-12-inch-surface-pro-low-end-systems-finally-get-upgrades",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft brings Snapdragon X2 Plus to 13-inch Surface Laptop, 12-inch Surface Pro",
    "url": "https://www.tomshardware.com/tablets/microsoft-surface/microsoft-brings-snapdragon-x2-plus-to-13-inch-surface-laptop-12-inch-surface-pro-low-end-systems-finally-get-upgrades",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T20:30:00+00:00",
    "summary": "Microsoft's lowest-end systems are getting upgrades to Qualcomm's latest Snapdragon X2 Plus processors."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/storage/chinas-ymtc-wins-patent-battle-against-micron-in-ongoing-3-year-legal-war-over-memory-patents-new-injunctions-could-restrict-microns-supply-into-germany",
    "domain": "AI 算力 / 半导体",
    "title": "China's YMTC wins patent battle against Micron in ongoing 3-year legal war over memory patents",
    "url": "https://www.tomshardware.com/pc-components/storage/chinas-ymtc-wins-patent-battle-against-micron-in-ongoing-3-year-legal-war-over-memory-patents-new-injunctions-could-restrict-microns-supply-into-germany",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T15:56:02+00:00",
    "summary": "A Munich court has granted YMTC two injunctions against Micron over 3D NAND patents, the latest development in a years-long cross-border legal battle between the memory rivals."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/alibaba-claims-new-qwen-image-2-1-ai-model-beats-google-nano-banana-2-0-with-minuscule-7b-parameter-model-benchmarks-show-open-weight-contender-is-competitive-with-openai-and-meta-image-models",
    "domain": "AI 算力 / 半导体",
    "title": "Alibaba claims new Qwen Image 2.1 AI model beats Google Nano Banana 2.0 with minuscule 7B parameter model",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/alibaba-claims-new-qwen-image-2-1-ai-model-beats-google-nano-banana-2-0-with-minuscule-7b-parameter-model-benchmarks-show-open-weight-contender-is-competitive-with-openai-and-meta-image-models",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T15:34:36+00:00",
    "summary": "Alibaba Group's AI division has released Qwen 2.1 Image, an ultra-lightweight image generation model with just 7B parameters, able to run on local hardware like the RTX 3090."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/case-mods/usd14-000-gaming-pc-features-70-handcrafted-titanium-cherry-blossoms-which-unfurl-as-temperatures-rise-zotac-designed-rtx-5080-system-features-impressive-sculpture-and-an-eye-watering-price-tag-to-match",
    "domain": "AI 算力 / 半导体",
    "title": "$14,000 gaming PC features 70 handcrafted titanium cherry blossoms which unfurl as temperatures rise",
    "url": "https://www.tomshardware.com/pc-components/case-mods/usd14-000-gaming-pc-features-70-handcrafted-titanium-cherry-blossoms-which-unfurl-as-temperatures-rise-zotac-designed-rtx-5080-system-features-impressive-sculpture-and-an-eye-watering-price-tag-to-match",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T13:14:43+00:00",
    "summary": "The Aftershock PC Cherry Bloom includes 70 hand-crafted cherry blossoms made of titanium alloy that open and close with the heat generated by the PC."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/sony-inzone-m10s-ii-27-inch-540-hz-qhd-oled-gaming-monitor-review",
    "domain": "AI 算力 / 半导体",
    "title": "Sony INZONE M10S II 27-inch 540 Hz QHD OLED gaming monitor review: A major player in a crowded field",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/sony-inzone-m10s-ii-27-inch-540-hz-qhd-oled-gaming-monitor-review",
    "source": "Christian Eberle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T13:00:00+00:00",
    "summary": "Sony brings saturated color and speedy gameplay to the OLED genre with its INZONE M10S II 27-inch QHD monitor. It boasts a 540 Hz refresh rate, 720 Hz at HD resolution, Adaptive-Sync, HDR, and wide-ga"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/filing-reveals-how-bytedance-gained-access-to-over-2-000-nvidia-b200-chips-through-nscales-norway-data-center-singaporean-subsidiary-spring-contributed-73-percent-of-uk-neoclouds-2025-revenue",
    "domain": "AI 算力 / 半导体",
    "title": "China's ByteDance gained access to over 2,000 Nvidia B200 chips through Norway data center",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/filing-reveals-how-bytedance-gained-access-to-over-2-000-nvidia-b200-chips-through-nscales-norway-data-center-singaporean-subsidiary-spring-contributed-73-percent-of-uk-neoclouds-2025-revenue",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T12:00:43+00:00",
    "summary": "UK-based Nscale signed a deal with Spring (SG) Pte Ltd, which is a subsidiary of Chinese tech giant ByteDance. The company did not make any direct mention of the TikTok parent in its filings for a U.S"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/alibaba-unveils-zhenwu-v900-ai-accelerator-claims-its-the-most-powerful-ai-chip-in-china-accelerator-supports-500-000-chip-supercluster-with-a-10t-parameter-qwen-model-on-the-roadmap",
    "domain": "AI 算力 / 半导体",
    "title": "Alibaba unveils Zhenwu V900 AI accelerator, claims it's 'the most powerful AI chip in China'",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/alibaba-unveils-zhenwu-v900-ai-accelerator-claims-its-the-most-powerful-ai-chip-in-china-accelerator-supports-500-000-chip-supercluster-with-a-10t-parameter-qwen-model-on-the-roadmap",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T12:00:00+00:00",
    "summary": "Alibaba’s T-Head Zhenwu V900 claims three times the M890’s performance with 216GB of memory as Alibaba targets 10T-parameter Qwen"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/upgrade-your-gaming-experience-with-this-27-inch-acer-1440p-270hz-panel-thats-an-incredible-45-percent-off-just-usd179-buys-an-awesome-ips-monitor-with-amd-freesync-premium-and-1ms-response-time",
    "domain": "AI 算力 / 半导体",
    "title": "Upgrade your gaming experience with this 27-inch Acer 1440p 270Hz panel that’s an incredible 45% off",
    "url": "https://www.tomshardware.com/pc-components/upgrade-your-gaming-experience-with-this-27-inch-acer-1440p-270hz-panel-thats-an-incredible-45-percent-off-just-usd179-buys-an-awesome-ips-monitor-with-amd-freesync-premium-and-1ms-response-time",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T11:45:00+00:00",
    "summary": "Jump into high-refresh-rate 1440p gaming without breaking the bank: Acer's 27-inch 1440p 270Hz IPS gaming monitor is just $179, a whopping 45% off"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/amd-begins-to-add-gddr7-support-to-its-linux-gpu-drivers-changes-could-herald-use-of-advanced-memory-standard-with-next-gen-radeon-gpus",
    "domain": "AI 算力 / 半导体",
    "title": "AMD begins to add GDDR7 support to its Linux GPU drivers",
    "url": "https://www.tomshardware.com/pc-components/gpus/amd-begins-to-add-gddr7-support-to-its-linux-gpu-drivers-changes-could-herald-use-of-advanced-memory-standard-with-next-gen-radeon-gpus",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T11:30:00+00:00",
    "summary": "Recent changes to AMD's Linux drivers to enable GDDR7 memory and other graphics IP blocks could indicate that that enablement work on its RDNA 5 GPUs is under way."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/metas-new-transoceanic-undersea-cable-boasts-a-whopping-petabit-of-bandwidth-petal-link-between-us-and-france-will-be-twice-as-fast-as-the-last",
    "domain": "AI 算力 / 半导体",
    "title": "Meta's new transoceanic undersea cable boasts a whopping petabit of bandwidth",
    "url": "https://www.tomshardware.com/networking/metas-new-transoceanic-undersea-cable-boasts-a-whopping-petabit-of-bandwidth-petal-link-between-us-and-france-will-be-twice-as-fast-as-the-last",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T11:00:00+00:00",
    "summary": "Meta has announced Petal, a new subsea cable that will carry a petabit of raw bandwidth across the 4,300 miles between the USA and France."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/this-32gb-corsair-vengeance-ddr5-6000-memory-is-the-cheapest-kit-available-discount-plus-usd40-promo-code-offers-the-least-expensive-ddr5-6000-kit-available-today",
    "domain": "AI 算力 / 半导体",
    "title": "This 32GB Corsair Vengeance DDR5-6000 memory is the cheapest kit available",
    "url": "https://www.tomshardware.com/pc-components/this-32gb-corsair-vengeance-ddr5-6000-memory-is-the-cheapest-kit-available-discount-plus-usd40-promo-code-offers-the-least-expensive-ddr5-6000-kit-available-today",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T10:45:00+00:00",
    "summary": "Get a great deal on 32GB Corsair Vengeance DDR5-6000 RAM. Just $439 after promo code SSF73844 yields one of the lowest priced 32GB kits available today"
  },
  {
    "id": "hn:49773511",
    "domain": "AI 算力 / 半导体",
    "title": "Every Nvidia GPU has 10 to 30 RISC-V cores inside it",
    "url": "https://www.xda-developers.com/your-nvidia-gpu-dozens-risc-v-cores-one-took-over-graphics-driver/",
    "source": "giuliomagnifico",
    "platform": "hackernews",
    "points": 50,
    "published_at": "2026-09-20T07:50:58+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/smarter-buildings-safer-occupants-intelligence-meets-privacy/",
    "domain": "AI 算力 / 半导体",
    "title": "Smarter Buildings, Safer Occupants: Intelligence Meets Privacy",
    "url": "https://www.eetimes.com/smarter-buildings-safer-occupants-intelligence-meets-privacy/",
    "source": "Anne-Françoise Pelé",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T08:05:07+00:00",
    "summary": "Modern building automation systems are designed to optimize energy efficiency while safeguarding the health, safety, and security of occupants. The post Smarter Buildings, Safer Occupants: Intelligenc"
  },
  {
    "id": "rss:https://www.eetimes.com/canadian-startup-sees-success-in-space-qualification/",
    "domain": "AI 算力 / 半导体",
    "title": "Canadian Startup Sees Success in Space Qualification",
    "url": "https://www.eetimes.com/canadian-startup-sees-success-in-space-qualification/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T16:21:10+00:00",
    "summary": "Novigrad is forging a pathway for faster, more accessible radiation testing as a growing wave of space missions drives demand for reliable, resilient electronics. The post Canadian Startup Sees Succes"
  },
  {
    "id": "hn:49777694",
    "domain": "AI 算力 / 半导体",
    "title": "Autonomous strike drone uses Nvidia Jetson Orin Nano to pick and bomb targets",
    "url": "https://www.tomshardware.com/tech-industry/drones/autonomous-strike-drone-uses-nvidia-jetson-orin-nano-to-independently-pick-and-bomb-targets-swedish-startups-attack-drones-run-small-ai-model-require-no-human-input-and-zero-external-comms",
    "source": "sbulaev",
    "platform": "hackernews",
    "points": 29,
    "published_at": "2026-09-20T17:07:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:49745610",
    "domain": "AI 算力 / 半导体",
    "title": "Run QWEN3.8 27B on 16gb Nvidia GPUs",
    "url": "https://github.com/MiaAI-Lab/Qwen3.8-27B-16gb-NVIDIA-GPUs-one-click-install",
    "source": "Pragmata",
    "platform": "hackernews",
    "points": 28,
    "published_at": "2026-09-17T19:46:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:49657991",
    "domain": "AI 算力 / 半导体",
    "title": "How to Build a $20B Semiconductor Fab (2024)",
    "url": "https://www.construction-physics.com/p/how-to-build-a-20-billion-semiconductor",
    "source": "Bluestein",
    "platform": "hackernews",
    "points": 25,
    "published_at": "2026-09-11T13:22:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:49727093",
    "domain": "AI 算力 / 半导体",
    "title": "Apple May Return to Server Market with Nvidia Technology",
    "url": "https://www.macrumors.com/2026/09/16/apple-may-return-to-server-market/",
    "source": "tosh",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-09-16T13:54:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:49537553",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.8 Flash and 3.8 Flash Cyber",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/",
    "source": "bratao",
    "platform": "hackernews",
    "points": 1160,
    "published_at": "2026-09-02T15:12:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:49797982",
    "domain": "大厂 AI 动态",
    "title": "I said no and Apple said yes",
    "url": "https://dbushell.com/2026/09/22/apple-intelligence/",
    "source": "thatslast",
    "platform": "hackernews",
    "points": 871,
    "published_at": "2026-09-22T08:04:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:49611251",
    "domain": "大厂 AI 动态",
    "title": "AlphaGenome Atlas: a high-resolution map of human DNA",
    "url": "https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphagenome-atlas/",
    "source": "utiiiD",
    "platform": "hackernews",
    "points": 607,
    "published_at": "2026-09-08T14:55:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:49715947",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.8 Live and 3.8 Live Extended Thinking",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/",
    "source": "leumon",
    "platform": "hackernews",
    "points": 492,
    "published_at": "2026-09-15T17:38:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:49817615",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.8 text-to-speech",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/",
    "source": "swolpers",
    "platform": "hackernews",
    "points": 329,
    "published_at": "2026-09-23T15:29:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:49790409",
    "domain": "大厂 AI 动态",
    "title": "Turn off and restrict access to Apple Intelligence features on Mac",
    "url": "https://support.apple.com/guide/mac-help/turn-restrict-access-apple-intelligence-mchlb2e44f94/mac",
    "source": "alwillis",
    "platform": "hackernews",
    "points": 353,
    "published_at": "2026-09-21T17:30:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:49552299",
    "domain": "大厂 AI 动态",
    "title": "WeatherNext 3",
    "url": "https://deepmind.google/science/weathernext/",
    "source": "matthieu_bl",
    "platform": "hackernews",
    "points": 406,
    "published_at": "2026-09-03T16:06:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:49468818",
    "domain": "大厂 AI 动态",
    "title": "Gemini-3.5-Transcribe",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/",
    "source": "k9294",
    "platform": "hackernews",
    "points": 363,
    "published_at": "2026-08-27T18:03:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:49467922",
    "domain": "大厂 AI 动态",
    "title": "Gemini Omni 1.1 Flash",
    "url": "https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/",
    "source": "saretup",
    "platform": "hackernews",
    "points": 297,
    "published_at": "2026-08-27T17:06:32+00:00",
    "summary": ""
  },
  {
    "id": "hn:49829387",
    "domain": "大厂 AI 动态",
    "title": "Hackers influence ChatGPT and Gemini to direct users to scam centers",
    "url": "https://medium.com/@arielsimon/dark-sourcery-how-hackers-manipulate-ai-to-scam-you-88df434d2073",
    "source": "ArielSimon",
    "platform": "hackernews",
    "points": 136,
    "published_at": "2026-09-24T11:54:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:49727659",
    "domain": "大厂 AI 动态",
    "title": "The DeepMind Institute",
    "url": "https://institute.deepmind.com/",
    "source": "vertigoruntime",
    "platform": "hackernews",
    "points": 186,
    "published_at": "2026-09-16T14:32:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:49602490",
    "domain": "大厂 AI 动态",
    "title": "Emacs Bedrock 2.0",
    "url": "https://lambdaland.org/posts/2026-09-06-bedrock-v2/",
    "source": "ashton314",
    "platform": "hackernews",
    "points": 191,
    "published_at": "2026-09-07T20:12:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:49740330",
    "domain": "大厂 AI 动态",
    "title": "I had Gemini train its own replacement for $9",
    "url": "https://www.petervijeh.com/projects/reddit-ner",
    "source": "p-s-v",
    "platform": "hackernews",
    "points": 88,
    "published_at": "2026-09-17T13:17:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:49762493",
    "domain": "大厂 AI 动态",
    "title": "Gemini hacked three companies in first known breakout by Google's AI",
    "url": "https://www.reuters.com/business/gemini-hacked-three-companies-first-known-breakout-by-google-ai-wsj-reports-2026-09-18/",
    "source": "usernomdeguerre",
    "platform": "hackernews",
    "points": 77,
    "published_at": "2026-09-19T01:40:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:49743685",
    "domain": "大厂 AI 动态",
    "title": "Economic policy for AGI",
    "url": "https://institute.deepmind.com/essays/economic-policy-for-agi/",
    "source": "alphabetatango",
    "platform": "hackernews",
    "points": 66,
    "published_at": "2026-09-17T17:12:51+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/transportation/1000317/tesla-semi-launch-customer-delivery-freight-battery-engineer",
    "domain": "大厂 AI 动态",
    "title": "Here’s the Tesla Semi… again",
    "url": "https://www.theverge.com/transportation/1000317/tesla-semi-launch-customer-delivery-freight-battery-engineer",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T02:12:57+00:00",
    "summary": "Remember the Tesla Semi? The long-gestating, heavy-duty truck first introduced in concept form in 2017 is finally in volume production as of April 2026 - nearly a decade after its initial introduction"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1000495/microsoft-is-killing-off-the-copilot-plus-pc-brand",
    "domain": "大厂 AI 动态",
    "title": "Microsoft is killing off the ‘Copilot Plus PC’ brand",
    "url": "https://www.theverge.com/tech/1000495/microsoft-is-killing-off-the-copilot-plus-pc-brand",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T01:25:53+00:00",
    "summary": "Remember when Microsoft wanted everyone to know that \"Copilot Plus PCs\" were the ones to get, because those were the PCs that that'd have enough built-in AI muscle to get things done? Two and a half y"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1000370/meta-instagram-attorney-client-privilege-hats",
    "domain": "大厂 AI 动态",
    "title": "Meta employees ordered ‘attorney/client privilege’ hats while fighting child safety disclosures",
    "url": "https://www.theverge.com/tech/1000370/meta-instagram-attorney-client-privilege-hats",
    "source": "Richard Lawler",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T23:50:55+00:00",
    "summary": "Meta's lawyers have argued that certain evidence should be withheld from public view on the grounds of attorney-client privilege in the ongoing lawsuits over alleged harm to teens' safety and mental h"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1000443/qualcomms-new-elite-sound-chip-might-finally-deliver-the-wi-fi-earbud-dream",
    "domain": "大厂 AI 动态",
    "title": "Qualcomm’s new ‘Elite’ sound chip might finally deliver the Wi-Fi earbud dream",
    "url": "https://www.theverge.com/tech/1000443/qualcomms-new-elite-sound-chip-might-finally-deliver-the-wi-fi-earbud-dream",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T23:42:39+00:00",
    "summary": "What if your wireless earbuds - or audio glasses - could stream high-quality lossless audio that doesn't cut out when you leave your phone on the bedside charger or buried in the couch? Qualcomm's new"
  },
  {
    "id": "rss:https://www.theverge.com/news/1000374/microsoft-comms-pr-brad-smith-cela",
    "domain": "大厂 AI 动态",
    "title": "Microsoft puts Brad Smith in charge of communications",
    "url": "https://www.theverge.com/news/1000374/microsoft-comms-pr-brad-smith-cela",
    "source": "Tom Warren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T22:08:22+00:00",
    "summary": "Microsoft is moving its communications group out of marketing and into its Corporate, External, and Legal Affairs (CELA) organization. The surprise change will see Microsoft vice chair and president B"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1000328/google-gemini-ai-live-avatar-face",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.8 Live with Live Avatar gives Google&#8217;s AI a face",
    "url": "https://www.theverge.com/tech/1000328/google-gemini-ai-live-avatar-face",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T19:59:26+00:00",
    "summary": "Google's new Gemini 3.8 Live update lets users have conversations with the model while watching an animated AI persona respond in real time. The \"Live Avatar\" will lip-sync and show different facial e"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1000122/cyberpowerpc-gaming-prebuilt-rtx-5070-core-i7-asrock-oled-monitor-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Sadly, this $1,549 RTX 5070-equipped gaming PC is a very good deal",
    "url": "https://www.theverge.com/gadgets/1000122/cyberpowerpc-gaming-prebuilt-rtx-5070-core-i7-asrock-oled-monitor-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T18:19:23+00:00",
    "summary": "While PC component prices remain high, you can save a good bit of money on a system by purchasing a prebuilt desktop. Walmart has a well-equipped CyberPowerPC gaming PC on sale for $1,549, almost $600"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1000140/jensen-huang-nvidia-ai-energy-climate-change-supervillain",
    "domain": "大厂 AI 动态",
    "title": "Jensen Huang talks about AI and climate change like a supervillain",
    "url": "https://www.theverge.com/tech/1000140/jensen-huang-nvidia-ai-energy-climate-change-supervillain",
    "source": "Justine Calma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T18:04:44+00:00",
    "summary": "As Jensen Huang puts it, AI can help fight climate change - but only if it inflicts \"an enormous amount of pain and suffering\" first. The Nvidia CEO discussed the future of energy and AI's impact on o"
  },
  {
    "id": "rss:https://www.theverge.com/games/999972/meta-horizon-create-studio-ai-games",
    "domain": "大厂 AI 动态",
    "title": "Meta is going to let you build games with AI right on your phone",
    "url": "https://www.theverge.com/games/999972/meta-horizon-create-studio-ai-games",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T17:52:29+00:00",
    "summary": "Meta has a new plan to get people to make games for its Horizon social platform. The company today announced two new development tools that will let you create games with AI prompts: Horizon Create, a"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1000222/meta-muse-ai-filesystem",
    "domain": "大厂 AI 动态",
    "title": "Muse will apparently let you download its entire filesystem",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1000222/meta-muse-ai-filesystem",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T17:14:12+00:00",
    "summary": "A pair of developers say that with very little prompting, Meta's Muse will share its entire filesystem with you. Peter James and Jonny L. Saunders have said they both independently coaxed Muse into zi"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/24/lightspeed-targets-250m-for-new-india-fund-focusing-on-early-stage-ai/",
    "domain": "大厂 AI 动态",
    "title": "Lightspeed targets $250M for new India fund, focusing on early-stage AI",
    "url": "https://techcrunch.com/2026/09/24/lightspeed-targets-250m-for-new-india-fund-focusing-on-early-stage-ai/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T05:00:00+00:00",
    "summary": "The venture firm is aligning its India fundraising cycle with its global funds for the first time, as it shifts to a shorter investment period."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/24/waymo-is-scaling-fast-heres-what-the-fleet-data-shows/",
    "domain": "大厂 AI 动态",
    "title": "Waymo is scaling fast: Here’s what the fleet data shows",
    "url": "https://techcrunch.com/2026/09/24/waymo-is-scaling-fast-heres-what-the-fleet-data-shows/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T23:24:33+00:00",
    "summary": "In the past month, Waymo has expanded its fleet in Texas by 49%. There are other hot spots as well."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/24/nexterity-wants-to-automate-the-hard-dangerous-part-of-pipefitting/",
    "domain": "大厂 AI 动态",
    "title": "Nexterity wants to automate the hard, dangerous part of pipefitting",
    "url": "https://techcrunch.com/2026/09/24/nexterity-wants-to-automate-the-hard-dangerous-part-of-pipefitting/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T20:45:00+00:00",
    "summary": "The startup's robot can tighten or loosen four bolts at a time, and it fits in a Pelican case."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/24/bring-your-co-founder-partner-or-colleague-and-get-50-off-a-second-techcrunch-disrupt-2026-pass/",
    "domain": "大厂 AI 动态",
    "title": "Bring your co-founder, partner, or colleague and get 50% off a second TechCrunch Disrupt 2026 pass",
    "url": "https://techcrunch.com/2026/09/24/bring-your-co-founder-partner-or-colleague-and-get-50-off-a-second-techcrunch-disrupt-2026-pass/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T19:15:00+00:00",
    "summary": "Buy one pass to TechCrunch Disrupt 2026 and get 50% off a second of the same ticket type. Register before event starts on October 13 at 8 a.m. PT."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/24/prismml-brings-its-tiny-llms-to-qualcomm-powered-smart-glasses/",
    "domain": "大厂 AI 动态",
    "title": "PrismML brings its tiny LLMs to Qualcomm-powered smart glasses",
    "url": "https://techcrunch.com/2026/09/24/prismml-brings-its-tiny-llms-to-qualcomm-powered-smart-glasses/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T19:00:42+00:00",
    "summary": "Prism's larger goal is open-weight AI that runs on devices and makes better use of the computing power they already have."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/24/meet-feather-the-startup-building-the-android-of-robotics-for-developers/",
    "domain": "大厂 AI 动态",
    "title": "Meet Feather, the startup building the ‘Android of robotics’ for developers",
    "url": "https://techcrunch.com/2026/09/24/meet-feather-the-startup-building-the-android-of-robotics-for-developers/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T18:52:38+00:00",
    "summary": "Feather is betting on a customizable, $30,000 platform built for software developers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/24/oracle-sends-force-majeure-notice-on-its-new-mexico-stargate-data-center/",
    "domain": "大厂 AI 动态",
    "title": "Oracle sends force majeure notice on its New Mexico Stargate data center",
    "url": "https://techcrunch.com/2026/09/24/oracle-sends-force-majeure-notice-on-its-new-mexico-stargate-data-center/",
    "source": "Aditya Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T18:11:44+00:00",
    "summary": "The notice would allow Oracle to delay payments should the facility miss its 2028 target to come online."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/24/metas-muse-charm-looks-like-a-tamagotchi-but-its-tapping-into-a-much-newer-trend/",
    "domain": "大厂 AI 动态",
    "title": "Meta’s Muse Charm looks like a Tamagotchi, but it’s tapping into a much newer trend",
    "url": "https://techcrunch.com/2026/09/24/metas-muse-charm-looks-like-a-tamagotchi-but-its-tapping-into-a-much-newer-trend/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T17:39:24+00:00",
    "summary": "Meta’s new AI gadget may look like a Tamagotchi, but its dangling form factor taps into a much broader Gen Z trend around bag charms, retro tech, and turning gadgets into fashion accessories."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/24/databricks-buys-row-zero-and-is-scouting-for-more-startups-to-acquire/",
    "domain": "大厂 AI 动态",
    "title": "Databricks buys Row Zero and is scouting for more startups to acquire",
    "url": "https://techcrunch.com/2026/09/24/databricks-buys-row-zero-and-is-scouting-for-more-startups-to-acquire/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T17:07:55+00:00",
    "summary": "Databricks has bought cloud spreadsheet startup Row Zero, adding yet another acquisition to its 2026 shopping spree."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/24/google-photos-clueless-inspired-virtual-closet-is-now-available-on-android-and-ios/",
    "domain": "大厂 AI 动态",
    "title": "Google Photos ‘Clueless’-inspired virtual closet is now available on Android and iOS",
    "url": "https://techcrunch.com/2026/09/24/google-photos-clueless-inspired-virtual-closet-is-now-available-on-android-and-ios/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T17:00:00+00:00",
    "summary": "The AI-powered feature builds a virtual wardrobe from your photos, and is now broadly available after first rolling out to Android users in June."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/24/techcrunch-founder-summit-2026-everything-you-need-to-know/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Founder Summit 2026: Everything you need to know",
    "url": "https://techcrunch.com/2026/09/24/techcrunch-founder-summit-2026-everything-you-need-to-know/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T16:46:47+00:00",
    "summary": "TechCrunch Founder Summit is a full-day gathering in Boston on November 4 where founders across all stages connect with top VCs and experienced entrepreneurs to gain tactical insights on building and "
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/24/twenty-minutes-with-the-ceo-of-elevenlabs-now-reportedly-valued-at-22-billion/",
    "domain": "大厂 AI 动态",
    "title": "ElevenLabs’ CEO on margins, IPO timing, and telling customers they’re talking to a bot",
    "url": "https://techcrunch.com/2026/09/24/twenty-minutes-with-the-ceo-of-elevenlabs-now-reportedly-valued-at-22-billion/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T16:35:13+00:00",
    "summary": "ElevenLabs powers the AI voice on the other end of a lot of customer service calls, and its CEO told me this week that businesses should probably tell you that — at least until getting a machine is wh"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/24/meet-the-next-wave-of-vcs-judging-startup-battlefield-200-at-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "Meet the next wave of VCs judging Startup Battlefield 200 at TechCrunch Disrupt 2026",
    "url": "https://techcrunch.com/2026/09/24/meet-the-next-wave-of-vcs-judging-startup-battlefield-200-at-techcrunch-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T16:03:36+00:00",
    "summary": "Meet the next wave of VCs judging the Startup Battlefield 200 contenders on the main stage at TechCrunch Disrupt 2026. Register by September 25 at 11:59 p.m. PT, to save up to $200 and to get a front-"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/24/google-tests-letting-gemini-make-phone-calls-initially-for-us-pixel-owners/",
    "domain": "大厂 AI 动态",
    "title": "Google tests letting Gemini call businesses for you",
    "url": "https://techcrunch.com/2026/09/24/google-tests-letting-gemini-make-phone-calls-initially-for-us-pixel-owners/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T16:00:00+00:00",
    "summary": "Google says the AI-calling feature will first be available to Pixel 11 owners in the U.S. who pay for a Gemini subscription."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/24/shield-ai-waabi-and-general-motors-on-building-ai-when-failure-is-not-an-option-at-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "Shield AI, Waabi, and General Motors on building AI when failure is not an option at TechCrunch Disrupt 2026",
    "url": "https://techcrunch.com/2026/09/24/shield-ai-waabi-and-general-motors-on-building-ai-when-failure-is-not-an-option-at-techcrunch-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T15:00:00+00:00",
    "summary": "Leaders from Waabi, Shield AI, and General Motors join the Real World AI Stage at TechCrunch Disrupt 2026 to talk building AI. Save up to $200 by September 25 at 11:59 p.m. PT. Get a second pass at 50"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/24/lovables-annualized-revenue-crosses-600m-as-vibe-coding-takes-off/",
    "domain": "大厂 AI 动态",
    "title": "Lovable’s annualized revenue crosses $600M as vibe coding takes off",
    "url": "https://techcrunch.com/2026/09/24/lovables-annualized-revenue-crosses-600m-as-vibe-coding-takes-off/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T14:43:25+00:00",
    "summary": "Lovable co-founder Fabian Hedin said that apps created on the platform are getting nearly a billion monthly views each month."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/24/ando-eyes-slack-as-it-builds-team-messaging-platform-for-humans-and-agents-to-work-together/",
    "domain": "大厂 AI 动态",
    "title": "Ando wants to take on Slack with a team messaging app that lets humans and agents work together",
    "url": "https://techcrunch.com/2026/09/24/ando-eyes-slack-as-it-builds-team-messaging-platform-for-humans-and-agents-to-work-together/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T14:31:00+00:00",
    "summary": "The app gives agents their own identities and inboxes and lets them partake in conversations as naturally as people can."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/24/techcrunch-disrupt-2026-cal-ais-zach-yadegari-on-how-to-create-viral-growth-and-capitalize-on-it/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Disrupt 2026: Cal AI’s Zach Yadegari on how to create viral growth and capitalize on it",
    "url": "https://techcrunch.com/2026/09/24/techcrunch-disrupt-2026-cal-ais-zach-yadegari-on-how-to-create-viral-growth-and-capitalize-on-it/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T14:30:00+00:00",
    "summary": "Zach Yadegari joins the Builders Stage at TechCrunch Disrupt 2026 to share how he capitalized on viral growth. Save up to $200 before September 25. Save 50% on a second pass."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/24/2-days-left-to-save-up-to-200-on-techcrunch-disrupt-2026-reason-5-7-to-attend/",
    "domain": "大厂 AI 动态",
    "title": "2 days left to save up to $200 on a TechCrunch Disrupt 2026 pass — reason 4 of 5 to attend",
    "url": "https://techcrunch.com/2026/09/24/2-days-left-to-save-up-to-200-on-techcrunch-disrupt-2026-reason-5-7-to-attend/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T14:00:00+00:00",
    "summary": "Reason 4 of 5 to attend TechCrunch Disrupt 2026: Practical answers. Two days left to save up to $200 on your pass. Savings disappear after September 25 at 11:59 p.m. PT. Bring a second guest at 50% of"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/24/australia-to-investigate-if-openai-hack-of-government-health-website-broke-the-law/",
    "domain": "大厂 AI 动态",
    "title": "Australia to investigate if OpenAI hack of government health website broke the law",
    "url": "https://techcrunch.com/2026/09/24/australia-to-investigate-if-openai-hack-of-government-health-website-broke-the-law/",
    "source": "Aditya Mehta, Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T12:54:19+00:00",
    "summary": "The incident is the first known breach to affect a government agency, and Australia's prime minister has vowed to hold OpenAI accountable."
  },
  {
    "id": "rss:https://stratechery.com/2026/an-interview-with-colossus-eic-jeremy-stern-about-profiling-mark-zuckerberg/",
    "domain": "大厂 AI 动态",
    "title": "An Interview with Colossus EIC Jeremy Stern About Profiling Mark Zuckerberg",
    "url": "https://stratechery.com/2026/an-interview-with-colossus-eic-jeremy-stern-about-profiling-mark-zuckerberg/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T10:00:00+00:00",
    "summary": "An interview with Colossus EIC Jeremy Stern about profiling Mark Zuckerberg and other prominent tech figures."
  },
  {
    "id": "rss:https://stratechery.com/2026/more-on-muse-amazon-and-walmart-muse-and-expedia-whither-google/",
    "domain": "大厂 AI 动态",
    "title": "More on Muse, Amazon, and Walmart; Muse and Expedia; Whither Google?",
    "url": "https://stratechery.com/2026/more-on-muse-amazon-and-walmart-muse-and-expedia-whither-google/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T10:00:00+00:00",
    "summary": "Meta needs Walmart to wait out Amazon; Expedia seeks to keep its middleware position; meanwhile, where is Google?"
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/09/cdc-opens-state-ordering-for-covid-19-vaccines-after-unexplained-delay/",
    "domain": "大厂 AI 动态",
    "title": "CDC opens state ordering for COVID-19 vaccines after unexplained delay",
    "url": "https://arstechnica.com/health/2026/09/cdc-opens-state-ordering-for-covid-19-vaccines-after-unexplained-delay/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T22:29:48+00:00",
    "summary": "Health department previously blamed delay on \"not yet finalized procurement decisions.\""
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/09/disneys-ludwig-von-drake-was-inspired-by-rocket-scientists-65-years-ago/",
    "domain": "大厂 AI 动态",
    "title": "Donald Duck's uncle was partly based on Wernher von Braun",
    "url": "https://arstechnica.com/space/2026/09/disneys-ludwig-von-drake-was-inspired-by-rocket-scientists-65-years-ago/",
    "source": "Robert Pearlman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T21:40:07+00:00",
    "summary": "Introducing the \"world-famous authority on outer space...\""
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/09/f-droid-gets-its-biggest-update-in-a-decade-with-new-ui-and-smoother-app-installs/",
    "domain": "大厂 AI 动态",
    "title": "F-Droid gets its biggest update in a decade with new UI and smoother app installs",
    "url": "https://arstechnica.com/gadgets/2026/09/f-droid-gets-its-biggest-update-in-a-decade-with-new-ui-and-smoother-app-installs/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T19:30:42+00:00",
    "summary": "F-Droid's Android app store has been rebuilt from the ground up."
  },
  {
    "id": "hn:49691343",
    "domain": "股票",
    "title": "Nike exits the S&P 100 after 18 years and a $200B market-cap wipeout",
    "url": "https://fortune.com/2026/09/08/nike-stock-plummets-sp500-market-cap-index/",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 316,
    "published_at": "2026-09-14T02:50:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:49619848",
    "domain": "股票",
    "title": "Apple iPod Engraver (2019)",
    "url": "https://dunstanorchard.com/apple-ipod-engraver/",
    "source": "NaOH",
    "platform": "hackernews",
    "points": 288,
    "published_at": "2026-09-09T01:57:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:49712746",
    "domain": "股票",
    "title": "Global bond yields hit 2008 highs, raising stakes for big borrowers",
    "url": "https://www.reuters.com/world/asia-pacific/bond-selloff-drives-us-benchmark-beyond-5-stocks-rattled-2026-09-15/",
    "source": "kaycebasques",
    "platform": "hackernews",
    "points": 167,
    "published_at": "2026-09-15T14:07:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:49611240",
    "domain": "股票",
    "title": "iPod Classic 6G in QEMU",
    "url": "https://www.reddit.com/r/emulation/s/VL4Au2HGxq",
    "source": "dmonterocrespo",
    "platform": "hackernews",
    "points": 162,
    "published_at": "2026-09-08T14:54:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:49791944",
    "domain": "股票",
    "title": "Wall Street is growing skeptical of the data center boom",
    "url": "https://www.nytimes.com/2026/09/21/business/ai-data-center-ipos.html",
    "source": "mikhael",
    "platform": "hackernews",
    "points": 72,
    "published_at": "2026-09-21T19:14:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:49816810",
    "domain": "股票",
    "title": "Trump's 1,156 July Stock Trades Involved AI, Big Oil, Weapons-Makers, and More",
    "url": "https://www.commondreams.org/news/donald-trump-stock-trades",
    "source": "cirelli94",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-09-23T14:33:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:49819274",
    "domain": "股票",
    "title": "Morgan Stanley Investment-Bank Deal List Leaked in Email Misfire",
    "url": "https://finance.yahoo.com/markets/stocks/articles/morgan-stanley-investment-bank-deal-124657863.html",
    "source": "wslh",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-09-23T17:08:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:49796292",
    "domain": "股票",
    "title": "Smart Ring Maker Oura, Backers Seek $2.2B in US IPO",
    "url": "https://www.bloomberg.com/news/articles/2026-09-21/smart-ring-maker-oura-backers-seek-2-2-billion-in-us-ipo",
    "source": "elo2000",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-09-22T02:53:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:49810905",
    "domain": "股票",
    "title": "In 2025, 49 percent of adults under age 30 lived with a parent [pdf]",
    "url": "https://www.federalreserve.gov/publications/files/2025-report-economic-well-being-us-households-202605.pdf",
    "source": "gscott",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-09-23T02:26:49+00:00",
    "summary": ""
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
    "id": "hn:49682946",
    "domain": "股票",
    "title": "Show HN: Analyst Index – analysts who make money telling you good stock calls",
    "url": "https://www.analystidx.com/",
    "source": "haichuan",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-09-13T11:50:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:49672197",
    "domain": "股票",
    "title": "Larry Ellison to sell up to $7.5B worth of Oracle stock",
    "url": "https://www.ft.com/content/25b1abb0-790f-4315-9b0c-530d959a086f",
    "source": "potatobox",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-09-12T13:37:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:49594296",
    "domain": "股票",
    "title": "OpenAI 2025 financials $38.5B loss ahead of IPO",
    "url": "https://qz.com/openai-leaked-financials-losses-revenue-ipo-061626",
    "source": "u1hcw9nx",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-09-07T05:41:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:49696420",
    "domain": "股票",
    "title": "Global AI stocks fall as industry chiefs call for slowing development",
    "url": "https://www.reuters.com/world/china/ai-linked-asian-stocks-slump-after-top-lab-ceos-call-slowing-down-technologys-2026-09-14/",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-09-14T13:21:51+00:00",
    "summary": ""
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
    "id": "hn:49451482",
    "domain": "股票",
    "title": "Hackers Broke into Justice Department, NASA, Federal Reserve, Senate",
    "url": "https://www.justice.gov/opa/pr/justice-department-and-fbi-seize-platforms-operated-and-used-china-state-sponsored-hackers",
    "source": "2OEH8eoCRo0",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-08-26T16:05:32+00:00",
    "summary": ""
  },
  {
    "id": "hn:49450370",
    "domain": "股票",
    "title": "Chinese Hackers Broke into Justice Department, NASA, Federal Reserve, Senate",
    "url": "https://www.reuters.com/world/china/china-sponsored-hacking-platforms-seized-by-us-justice-department-says-2026-08-26/",
    "source": "thisisauserid",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-08-26T14:59:43+00:00",
    "summary": ""
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
    "id": "rss:https://www.netinterest.co/p/strategy-follows-structure",
    "domain": "股票",
    "title": "Strategy Follows Structure",
    "url": "https://www.netinterest.co/p/strategy-follows-structure",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-29T16:47:05+00:00",
    "summary": "Fidelity, Capital, Vanguard and the Ownership Structures That Made Them"
  },
  {
    "id": "rss:https://www.netinterest.co/p/griffins-doors",
    "domain": "股票",
    "title": "Griffin’s Doors",
    "url": "https://www.netinterest.co/p/griffins-doors",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-22T16:22:17+00:00",
    "summary": "Inside Citadel&#8217;s Talent Machine"
  },
  {
    "id": "rss:https://www.netinterest.co/p/the-future-of-ir",
    "domain": "股票",
    "title": "The Future of IR",
    "url": "https://www.netinterest.co/p/the-future-of-ir",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-15T15:38:49+00:00",
    "summary": "What the Changing Shape of Markets Means for Investor Relations"
  },
  {
    "id": "rss:https://www.netinterest.co/p/bye-the-index",
    "domain": "股票",
    "title": "Bye the Index",
    "url": "https://www.netinterest.co/p/bye-the-index",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-08T16:07:09+00:00",
    "summary": "How Nasdaq learned to run its flywheel in reverse"
  },
  {
    "id": "rss:https://www.netinterest.co/p/money-for-nothing",
    "domain": "股票",
    "title": "Money for Nothing",
    "url": "https://www.netinterest.co/p/money-for-nothing",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-01T16:28:45+00:00",
    "summary": "The Golden Age of Arbitrage?"
  },
  {
    "id": "hn:49778029",
    "domain": "金融",
    "title": "Samsung is expected to more than double output of its HBM4 and HBM4E DRAM",
    "url": "https://en.sedaily.com/finance/2026/09/20/samsung-to-double-hbm4-output-next-year-sources-say",
    "source": "giuliomagnifico",
    "platform": "hackernews",
    "points": 560,
    "published_at": "2026-09-20T17:38:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:49686766",
    "domain": "金融",
    "title": "I'm being cyberattacked by Tesla, Inc",
    "url": "https://dreamstation.systems/personal/tesla.html",
    "source": "robinpie",
    "platform": "hackernews",
    "points": 458,
    "published_at": "2026-09-13T18:03:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:49594251",
    "domain": "金融",
    "title": "Switzerland's Federal Government Is Replacing Microsoft on 3k Computers",
    "url": "https://itsfoss.com/news/switzerland-replace-microssoft-pilot/",
    "source": "ivell",
    "platform": "hackernews",
    "points": 371,
    "published_at": "2026-09-07T05:33:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:49822556",
    "domain": "金融",
    "title": "OpenAI breaches Medicare, Albanese reveals",
    "url": "https://www.smh.com.au/politics/federal/openai-breaches-medicare-albanese-reveals-20260924-p6100u.html",
    "source": "jonnonz",
    "platform": "hackernews",
    "points": 252,
    "published_at": "2026-09-23T21:01:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:49704008",
    "domain": "金融",
    "title": "Amazon vs. Perplexity – U.S. Court of Appeals for the Ninth Circuit",
    "url": "https://law.justia.com/cases/federal/appellate-courts/ca9/26-1444/26-1444-2026-08-04.html",
    "source": "neom",
    "platform": "hackernews",
    "points": 219,
    "published_at": "2026-09-14T21:05:22+00:00",
    "summary": ""
  },
  {
    "id": "hn:49832844",
    "domain": "金融",
    "title": "Federal judge orders Texas to air condition all prisons by the end of 2029",
    "url": "https://www.texastribune.org/2026/09/22/texas-prison-air-conditioning-lawsuit-ruling/",
    "source": "bonefishgrill",
    "platform": "hackernews",
    "points": 105,
    "published_at": "2026-09-24T16:15:34+00:00",
    "summary": ""
  },
  {
    "id": "hn:49731356",
    "domain": "金融",
    "title": "Fed hikes rates as inflation worries push up bond yields",
    "url": "https://www.reuters.com/live/live-fed-rate-hike-expected-inflation-worries-push-up-bond-yields-2026-09-16/",
    "source": "wslh",
    "platform": "hackernews",
    "points": 184,
    "published_at": "2026-09-16T18:55:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:49600997",
    "domain": "金融",
    "title": "No constitutional right to clean water, federal court finds",
    "url": "https://www.usatoday.com/story/news/nation/2026/09/07/court-constitution-right-clean-water/91649488007/",
    "source": "measurablefunc",
    "platform": "hackernews",
    "points": 135,
    "published_at": "2026-09-07T17:52:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:49694840",
    "domain": "金融",
    "title": "How Much Has Trump Made from Crypto? ($1.4B from 2025 Federal Disclosure)",
    "url": "https://www.thepricer.org/how-much-has-trump-made-from-crypto/",
    "source": "cinderelacinder",
    "platform": "hackernews",
    "points": 114,
    "published_at": "2026-09-14T10:56:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:49591672",
    "domain": "金融",
    "title": "Hackers have withdrawn ~4k BTC (~$320M) from the Liquid Federation wallet",
    "url": "https://twitter.com/Liquid_BTC/status/2096696272447218108",
    "source": "felipelalli",
    "platform": "hackernews",
    "points": 126,
    "published_at": "2026-09-06T22:43:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:49828019",
    "domain": "金融",
    "title": "Show HN: Trader News – Hacker News for Finance",
    "url": "https://news.ycombinator.com/item?id=49828019",
    "source": "FailMore",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-09-24T08:54:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:49596610",
    "domain": "金融",
    "title": "Initial effects of AI technology on employment look positive",
    "url": "https://www.economist.com/finance-and-economics/2026/09/04/the-jobs-apocalypse-is-postponed-an-ai-jobs-boom-is-here",
    "source": "MrBuddyCasino",
    "platform": "hackernews",
    "points": 103,
    "published_at": "2026-09-07T10:38:32+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.28504",
    "domain": "金融",
    "title": "AI in Science: Early Insights",
    "url": "https://arxiv.org/abs/2609.28504",
    "source": "Mihai Codreanu, Alex Imas, Juan Mateos-Garcia, Joseph Emmens, Evalyne Muiruri, Arthur Turrell, Julian Jacobs, Atoosa Kasirzadeh, Ana Trisovic, Yiyuan Chen, Tanya Rodchenko, Catherine Pollard, Scott Strand, Daniel Rock, Zanna Iscenko, Fabien Curto Millet, Neil Thompson, James Manyika",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T04:00:00+00:00",
    "summary": "arXiv:2609.28504v1 Announce Type: new Abstract: Scientific progress is a key driver of economic growth and prosperity. There is great excitement - but also concerns - about the impacts of AI on scienc"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.28549",
    "domain": "金融",
    "title": "Do Female Directors Raise ESG Ratings? A Meta-Analysis",
    "url": "https://arxiv.org/abs/2609.28549",
    "source": "Karolina Hozova, Tomas Havranek, Zuzana Irsova",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T04:00:00+00:00",
    "summary": "arXiv:2609.28549v1 Announce Type: new Abstract: Appointing more women to corporate boards is widely expected to also raise firms' environmental, social, and governance (ESG) performance. We provide th"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.28675",
    "domain": "金融",
    "title": "From Individual to Social Imitation: How Communities Expand Organizational Search",
    "url": "https://arxiv.org/abs/2609.28675",
    "source": "Esteve Almirall, Christopher Tucci",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T04:00:00+00:00",
    "summary": "arXiv:2609.28675v1 Announce Type: new Abstract: Generative artificial intelligence illustrates a broader organizational puzzle: young, resource-constrained firms can build on knowledge produced across"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.28681",
    "domain": "金融",
    "title": "Improving Today, Narrowing Tomorrow: Collective Learning, Diversity, and Generativity",
    "url": "https://arxiv.org/abs/2609.28681",
    "source": "Esteve Almirall, Chris Tucci",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T04:00:00+00:00",
    "summary": "arXiv:2609.28681v1 Announce Type: new Abstract: Generative AI makes a paradox newly visible: learning from a common source can improve what each firm does today while narrowing the variety available f"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.28863",
    "domain": "金融",
    "title": "Affine Pricing Models from Group Quantization and Holonomy",
    "url": "https://arxiv.org/abs/2609.28863",
    "source": "Santiago Garcia",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T04:00:00+00:00",
    "summary": "arXiv:2609.28863v1 Announce Type: new Abstract: The analytic tractability of affine pricing models is usually expressed through two complementary formulations: a coordinate-space pricing operator and "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.29080",
    "domain": "金融",
    "title": "Don't Fake It If You Can't Make It: Driver Misconduct in Last-Mile Delivery",
    "url": "https://arxiv.org/abs/2609.29080",
    "source": "Srishti Arora, Vivek Choudhary, Pavel Kireyev",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T04:00:00+00:00",
    "summary": "arXiv:2609.29080v1 Announce Type: new Abstract: In the last two decades, last-mile delivery (LMD) firms have seen immense growth fueled by the success of e-commerce, leading to faster and cheaper deli"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.29700",
    "domain": "金融",
    "title": "Storage Options and Endogenous Commodity Prices in Continuous Time",
    "url": "https://arxiv.org/abs/2609.29700",
    "source": "Nader Karimi, Erfan Salavati, Hojatollah Adibi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T04:00:00+00:00",
    "summary": "arXiv:2609.29700v1 Announce Type: new Abstract: We study the price formation of a storable commodity when the decision to sell or keep the commodity is treated as an embedded storage option. The price"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.29905",
    "domain": "金融",
    "title": "Decision-Relevant Information in Partially Observed Production Networks",
    "url": "https://arxiv.org/abs/2609.29905",
    "source": "Shaowen Luo, Kwok Ping Tsang, Zichao Yang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T04:00:00+00:00",
    "summary": "arXiv:2609.29905v1 Announce Type: new Abstract: A production network can remain largely unidentified even when the economic decision it supports is identified. We characterize sufficient measurements "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.28947",
    "domain": "金融",
    "title": "Why Does Misinformation Propagate Faster? An Algorithmic Perspective on X",
    "url": "https://arxiv.org/abs/2609.28947",
    "source": "Pan Li, Shuang Gao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T04:00:00+00:00",
    "summary": "arXiv:2609.28947v1 Announce Type: cross Abstract: Misinformation is widely reported to propagate faster on engagement-based platforms, yet prior work largely focused on empirical analysis, without ide"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.29530",
    "domain": "金融",
    "title": "The Impossible Trinity of Time-Series Validation: A Conservation Law among Training Sufficiency, Test Coverage, and Temporal Causality",
    "url": "https://arxiv.org/abs/2609.29530",
    "source": "Jiayu Li",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T04:00:00+00:00",
    "summary": "arXiv:2609.29530v1 Announce Type: cross Abstract: Validating a model on a time series asks for three things at once: each training run should use most of the sample (sufficiency), the test sets should"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.29887",
    "domain": "金融",
    "title": "Cost-Sensitive Online Window Size Selection for Portfolio Management",
    "url": "https://arxiv.org/abs/2609.29887",
    "source": "Yi-Chen Liu, Chung-Han Hsieh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T04:00:00+00:00",
    "summary": "arXiv:2609.29887v1 Announce Type: cross Abstract: This paper investigates cost-sensitive online window size selection for portfolio management under changing market conditions. Specifically, we propos"
  },
  {
    "id": "rss:https://arxiv.org/abs/2411.05938",
    "domain": "金融",
    "title": "Uncertain and Asymmetric Forecasts",
    "url": "https://arxiv.org/abs/2411.05938",
    "source": "Eric Vansteenberghe",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T04:00:00+00:00",
    "summary": "arXiv:2411.05938v4 Announce Type: replace Abstract: Survey density forecasts are summarized by their second and third moments, read as uncertainty and as the balance of risks. Neither can be read on i"
  },
  {
    "id": "rss:https://arxiv.org/abs/2502.06015",
    "domain": "金融",
    "title": "Critical Mathematical Economics and Progressive Computer Science",
    "url": "https://arxiv.org/abs/2502.06015",
    "source": "Johannes Buchner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T04:00:00+00:00",
    "summary": "arXiv:2502.06015v5 Announce Type: replace Abstract: The aim of this article is to present elements and discuss the potential of a research program at the intersection between mathematics and heterodox"
  },
  {
    "id": "rss:https://arxiv.org/abs/2602.06198",
    "domain": "金融",
    "title": "Insider Purchases Far Below the 52-Week High: Decomposing the Disclosure Reaction in Microcap Equities",
    "url": "https://arxiv.org/abs/2602.06198",
    "source": "Hangyi Zhao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T04:00:00+00:00",
    "summary": "arXiv:2602.06198v2 Announce Type: replace Abstract: Purchases reported under transaction code P on SEC Form 4 by insiders of U.S. equities with an estimated filing-date capitalization of USD 30 millio"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.02791",
    "domain": "金融",
    "title": "Capitalizing Risk, Regulation, and Revised Perceptions: Sequential Shocks in Florida's Condominium Market",
    "url": "https://arxiv.org/abs/2607.02791",
    "source": "Shaoming Cheng",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T04:00:00+00:00",
    "summary": "arXiv:2607.02791v2 Announce Type: replace Abstract: Housing markets capitalize new information about future risks and ownership costs, yet less is known about how capitalization evolves when closely s"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.18975",
    "domain": "金融",
    "title": "Do Two On-Chain Observation Pipelines See the Same Tokens? Cross-Pipeline Coverage on the Solana pump.fun Launchpad",
    "url": "https://arxiv.org/abs/2609.18975",
    "source": "Arati Uday Kamat",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T04:00:00+00:00",
    "summary": "arXiv:2609.18975v2 Announce Type: replace Abstract: On-chain studies of memecoin launchpads usually rely on one data-collection pipeline, yet whether differently configured pipelines observe the same "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.27727",
    "domain": "金融",
    "title": "Sovereign Grassroots Currencies: A CBDC Architecture for Credit and Monetary Policy (Full Version)",
    "url": "https://arxiv.org/abs/2609.27727",
    "source": "Ehud Shapiro",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T04:00:00+00:00",
    "summary": "arXiv:2609.27727v2 Announce Type: replace Abstract: A Central Bank Digital Currency (CBDC) is central-bank money in digital form, held by the public. Leading designs have two limitations: conversion f"
  },
  {
    "id": "rss:https://arxiv.org/abs/2310.19992",
    "domain": "金融",
    "title": "Robust Estimation of Realized Correlation: New Insights about Intraday Fluctuations in Market Betas",
    "url": "https://arxiv.org/abs/2310.19992",
    "source": "Peter Reinhard Hansen, Yiyao Luo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T04:00:00+00:00",
    "summary": "arXiv:2310.19992v2 Announce Type: replace-cross Abstract: Time-varying volatility is an inherent feature of economic time series and complicates correlation measurement at high frequencies. While the "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.30583",
    "domain": "金融",
    "title": "The Cross-Section of Stock Returns and AI Exposure",
    "url": "https://arxiv.org/abs/2606.30583",
    "source": "Nicola Borri, Yukun Liu, Aleh Tsyvinski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T04:00:00+00:00",
    "summary": "arXiv:2606.30583v3 Announce Type: replace-cross Abstract: We study 380 trillion tokens of realized AI consumption across more than four hundred LLMs. We build a high-frequency AI factor and show that "
  },
  {
    "id": "hn:49700413",
    "domain": "金融",
    "title": "US 10-Year Breaches 5% as Inflation, Supply Worries Mount",
    "url": "https://www.bloomberg.com/news/articles/2026-09-14/us-10-year-yield-breaches-5-as-inflation-supply-worries-mount",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 72,
    "published_at": "2026-09-14T17:11:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:49730769",
    "domain": "金融",
    "title": "Feds Want California to Give Up 14 Years of Broadband Protections. It Should Sue",
    "url": "https://cyberlaw.stanford.edu/blog/2026/09/california-is-being-asked-to-give-up-14-years-of-broadband-protections-it-doesnt-have-to/",
    "source": "rsingel",
    "platform": "hackernews",
    "points": 38,
    "published_at": "2026-09-16T18:09:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:49762617",
    "domain": "金融",
    "title": "Elon Musk and Tesla Forged a New EV Path",
    "url": "https://spectrum.ieee.org/elon-musk-tesla",
    "source": "vinhnx",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-09-19T02:08:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:49612981",
    "domain": "金融",
    "title": "DOJ Blocked ICE Agent Shooting Charge over Federal Prosecutor's Objections",
    "url": "https://www.propublica.org/article/doj-blocks-charges-ice-agent-minneapolis-julio-cesar-sosa-celis",
    "source": "paimapi",
    "platform": "hackernews",
    "points": 56,
    "published_at": "2026-09-08T16:54:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:49564189",
    "domain": "金融",
    "title": "Norway's Oil Fund Proposes Selling Roughly $80B in U.S. Treasurys",
    "url": "https://www.wsj.com/finance/investing/norways-oil-fund-proposes-cut-to-government-bond-holdings-d930893f",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 48,
    "published_at": "2026-09-04T13:15:24+00:00",
    "summary": ""
  },
  {
    "id": "hn:49731515",
    "domain": "金融",
    "title": "Fed Raises Rates for First Time in Three Years",
    "url": "https://www.wsj.com/economy/central-banking/fed-raises-rates-for-first-time-in-three-years-08539fbe",
    "source": "kaycebasques",
    "platform": "hackernews",
    "points": 25,
    "published_at": "2026-09-16T19:09:22+00:00",
    "summary": ""
  },
  {
    "id": "hn:49625461",
    "domain": "金融",
    "title": "Teen reading slumps to worst this century due to surge in screen time",
    "url": "https://finance.yahoo.com/news/teen-reading-slumps-worst-century-111013754.html",
    "source": "pseudolus",
    "platform": "hackernews",
    "points": 42,
    "published_at": "2026-09-09T12:29:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:49730731",
    "domain": "金融",
    "title": "Fed Raises Rates as Warsh Bucks Trump to Contain Inflation",
    "url": "https://www.bloomberg.com/news/articles/2026-09-16/fed-raises-rates-as-warsh-bucks-trump-to-contain-inflation",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-09-16T18:05:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:49667360",
    "domain": "金融",
    "title": "A Decade of Hype, 3k Roofs, and One Redirect URL: Tesla Kills the Solar Roof",
    "url": "https://www.gadgetreview.com/a-decade-of-hype-3000-roofs-and-one-redirect-url-tesla-kills-the-solar-roof",
    "source": "upofadown",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-09-12T00:38:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:49514224",
    "domain": "金融",
    "title": "Monero Inflation Checker – FCMP++",
    "url": "https://www.reddit.com/r/Monero/comments/1w3hcos/monero_inflation_checker_fcmp/",
    "source": "Cider9986",
    "platform": "hackernews",
    "points": 36,
    "published_at": "2026-08-31T20:00:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:49633640",
    "domain": "金融",
    "title": "DHS Program Analyzes Americans' Finances to Flag Drivers for Traffic Stops",
    "url": "https://www.military.com/dhs-program-analyzes-americans-finances-to-flag-drivers-for-traffic-stops-report",
    "source": "randycupertino",
    "platform": "hackernews",
    "points": 35,
    "published_at": "2026-09-09T20:22:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:49548497",
    "domain": "金融",
    "title": "Mark Cuban: Why US hospitals \"don't know their costs\"",
    "url": "https://www.beckershospitalreview.com/finance/mark-cuban-why-us-hospitals-dont-know-their-costs/",
    "source": "elo2000",
    "platform": "hackernews",
    "points": 30,
    "published_at": "2026-09-03T11:07:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:49515596",
    "domain": "金融",
    "title": "Congress to vote on denying federal funding to universities that boycott Israel",
    "url": "https://twitter.com/dylanotes/status/2094229210889965634",
    "source": "slowin",
    "platform": "hackernews",
    "points": 28,
    "published_at": "2026-08-31T22:24:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:49551601",
    "domain": "金融",
    "title": "Inside Google’s $200bn Wall Street finance machine for Anthropic",
    "url": "https://www.ft.com/content/549f2e23-5aa2-49c7-9ea6-a9784ab7087c",
    "source": "porridgeraisin",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-09-03T15:26:27+00:00",
    "summary": ""
  }
]
```
