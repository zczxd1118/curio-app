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

- 今日日期：`2026-09-17`
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
  "date": "2026-09-17",
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
    "points": 2817996,
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
    "points": 1942983,
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
    "points": 1874335,
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
    "points": 1301785,
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
    "points": 1230978,
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
    "points": 886969,
    "published_at": "2025-05-01T09:00:00+00:00",
    "summary": "up的科学星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 881959,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1GsY76dEqW",
    "domain": "AI",
    "title": "一口气搞懂Agent到底怎么用！",
    "url": "http://www.bilibili.com/video/av117252103997988",
    "source": "GenJi是真想教会你",
    "platform": "bilibili",
    "points": 807286,
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
    "points": 781871,
    "published_at": "2026-07-01T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260701\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\nAI大模型开发热门教程：\nAI大模型开发：BV1h1"
  },
  {
    "id": "bvid:BV1ZHYy6rEpG",
    "domain": "AI",
    "title": "豆包大升级！Agent 干活新姿势～",
    "url": "http://www.bilibili.com/video/av117269703167491",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 665259,
    "published_at": "2026-09-14T14:34:55+00:00",
    "summary": "豆包大升级，一秒化身你的老同事～\n感谢朋友们的3连+关注～"
  },
  {
    "id": "bvid:BV1rBRQBSEwB",
    "domain": "AI",
    "title": "Claude Code+DeepSeek V4 Pro安装教程｜3步从零装好开始用 | Mac Windows",
    "url": "http://www.bilibili.com/video/av116543199385810",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 393725,
    "published_at": "2026-05-09T10:10:00+00:00",
    "summary": "上期vibe coding零基础教程10万多人看了，私信和评论里问最多的居然不是怎么写需求。\n 而是Claude Code怎么装？DeepSeek怎么接进去？🫣\n\n所以这期作为补丁教程，专门帮大家搞定这3件事：\n 1️⃣ 安装Claude Code\n 2️⃣ 把DeepSeek V4 Pro百万上下文满血版接入Claude Code\n 3️⃣ 在VS Code里正式用起来\n\nMac和Windows"
  },
  {
    "id": "bvid:BV1ia9UBPESQ",
    "domain": "AI",
    "title": "在VScode中配置Claude Code并接入DeepSeek V4 Pro【oo唠嗑教程】",
    "url": "http://www.bilibili.com/video/av116487012549813",
    "source": "沉默的羔丸ovo",
    "platform": "bilibili",
    "points": 336832,
    "published_at": "2026-04-29T08:23:29+00:00",
    "summary": "配置方法如下：\n(想用真心换取你的关注...蟹蟹泥...)\nsetting.json添加：\n{ &quot;name&quot;: &quot;ANTHROPIC_BASE_URL&quot;, &quot;value&quot;: &quot;https://xxxx&quot; }, \n{ &quot;name&quot;: &quot;ANTHROPIC_AUTH_TOKEN&quot;, "
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 325084,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 290965,
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
    "points": 285256,
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
    "points": 262651,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1DLYC6oEKT",
    "domain": "AI",
    "title": "为了让所有人都用好AI，我做了这个……",
    "url": "http://www.bilibili.com/video/av117268008733524",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 209594,
    "published_at": "2026-09-14T06:39:37+00:00",
    "summary": "炉子，给普通人的 AI 能力网络~\n官网/申请入口：luzi.ai\n感谢大家三连 + 关注和支持，大家一起“能力满满”！"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 200767,
    "published_at": "2026-04-27T08:51:41+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n   喜欢视频课程的同学一键三连多多支持一下，长按点赞五秒=lv6大佬 可以的发送彩色弹幕哦。\n配套源码项目已打包评论区回复up"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 181516,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1ExV36wEsE",
    "domain": "AI",
    "title": "VS Code 安装 Claude Code 并接入 DeepSeek！Claude Code for VS Code！VSCode使用ClaudeCode插件",
    "url": "http://www.bilibili.com/video/av116662871268177",
    "source": "FutureAI实验室",
    "platform": "bilibili",
    "points": 179225,
    "published_at": "2026-05-30T09:44:52+00:00",
    "summary": "本节视频编号71，评论区自助领取配套文档，记得一键三连哦！"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 177378,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1Teec6BEti",
    "domain": "AI",
    "title": "保姆级教程！教你在本地搭建DeepsSeek Harness多Agent工作流！",
    "url": "http://www.bilibili.com/video/av117280474137774",
    "source": "我是阿众",
    "platform": "bilibili",
    "points": 174060,
    "published_at": "2026-09-16T11:41:14+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1RNTtzMENj",
    "domain": "AI",
    "title": "从零编写MCP并发布上线，超简单！手把手教程",
    "url": "http://www.bilibili.com/video/av114630814862349",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 156599,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 118115,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1jSe76aEG9",
    "domain": "AI",
    "title": "Agent到底能做什么？千问办公全面上手+8大玩法",
    "url": "http://www.bilibili.com/video/av117273830363327",
    "source": "Xuan_酱",
    "platform": "bilibili",
    "points": 110195,
    "published_at": "2026-09-15T07:27:33+00:00",
    "summary": "全网最全、最详细的千问办公教程\n我会从安装下载，到界面功能，\n再用日常工作案例\n带你从零跑通八个千问办公的使用技巧\n帮你省下大把时间去做更有意义的事情\n看完保证你从小白变成Agent办公高手"
  },
  {
    "id": "bvid:BV1kGo6BdEsT",
    "domain": "AI",
    "title": "如何用Claude Skill 做高质量 PPT（附完整教程）",
    "url": "http://www.bilibili.com/video/av116474832361424",
    "source": "阿西_出海",
    "platform": "bilibili",
    "points": 99957,
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
    "points": 93723,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1K6YM69ESq",
    "domain": "AI",
    "title": "AI+网络安全实战：从Agent入门到AI智能体挖漏洞教程！网络安全|信息安全|黑客技术|渗透测试|SRC漏洞挖掘|AI审计|HVV护网行动|靶场练习-码士集团",
    "url": "http://www.bilibili.com/video/av117247037213495",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 73390,
    "published_at": "2026-09-10T13:47:24+00:00",
    "summary": "这套课程围绕「AI+网络安全」展开，从AI智能体基础入门，到WorkBuddy、Trae等主流Agent工具的实际应用，再到API-Key接入、Skill使用等核心能力，逐步进入AI漏洞挖掘、代码审计、CTF题目分析等安全实战场景。同时结合SRC漏洞挖掘、HVV护网、安全竞赛以及网络安全就业方向，帮助你系统了解AI在网络安全学习、开发与实战中的应用方式。适合网络安全初学者、安全从业者以及希望利用A"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 55169,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1VL3F6pE9K",
    "domain": "AI",
    "title": "0基础入门智能体agent测试：AI测试基础+AI智能体(Agent)测试从零入门全攻略，2026最新版！",
    "url": "http://www.bilibili.com/video/av116991151113881",
    "source": "黑马测试",
    "platform": "bilibili",
    "points": 50050,
    "published_at": "2026-07-27T09:19:37+00:00",
    "summary": "还在卷传统软件测试？2026年必学的AI智能体(Agent)测试来了！本期视频专为0基础小白打造，从软件测试基础讲起...若要本视频配套资源笔记可加up主企微（请看置顶留言最后一句话）。"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 48163,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1XiD5BQEAj",
    "domain": "AI",
    "title": "Claude Code 接入微信、一行命令把Claude Code装进微信、保姆级教程、微信支持Claude Code（cc-connect）远程开发",
    "url": "http://www.bilibili.com/video/av116350093694897",
    "source": "下班学AI",
    "platform": "bilibili",
    "points": 39911,
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
    "points": 34332,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1ApYD6KEkD",
    "domain": "AI",
    "title": "马斯克收购Cursor后，Cursor的性价比现在已经爆表",
    "url": "http://www.bilibili.com/video/av117254955993228",
    "source": "jopatk",
    "platform": "bilibili",
    "points": 31033,
    "published_at": "2026-09-11T23:19:58+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 30671,
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
    "points": 29758,
    "published_at": "2025-07-16T13:10:54+00:00",
    "summary": "Cursor用不了？三款AI编程工具完美代替Cursor\naugmentCode\nTrae\nKiro"
  },
  {
    "id": "bvid:BV1WtoTBiEuR",
    "domain": "AI",
    "title": "Claude Code多Agent模式实战分享",
    "url": "http://www.bilibili.com/video/av116454666012312",
    "source": "Simon林_",
    "platform": "bilibili",
    "points": 25848,
    "published_at": "2026-04-23T15:18:08+00:00",
    "summary": "Claude Code有2种多Agent模式：多个subagents模式和多个独立agent模式"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22785,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 22311,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1oc4m6wEoD",
    "domain": "AI",
    "title": "【江科大】如何用AI全流程开发STM32",
    "url": "http://www.bilibili.com/video/av117180431736152",
    "source": "拉咯比哩",
    "platform": "bilibili",
    "points": 19609,
    "published_at": "2026-08-30T02:00:00+00:00",
    "summary": "江科大老学长带你 FreeRTOS 项目实践 STM32F103 + Cube MX + FreeRTOS + 面向对象 + 项目框架\n这是AI入门篇，前置章节请见之前的视频\n此篇章将从零开始，用AI实现一套简单的系统\n感谢大家支持"
  },
  {
    "id": "bvid:BV18TZYY8EuJ",
    "domain": "AI",
    "title": "微软最新AI Agent入门课程 • 中英",
    "url": "http://www.bilibili.com/video/av114246130076146",
    "source": "Mindofuture",
    "platform": "bilibili",
    "points": 16400,
    "published_at": "2025-03-30T02:06:00+00:00",
    "summary": "在这门包含10节课的课程中，我们将带你从概念到代码，全面覆盖构建AI代理的基础知识。在这里找到完整的“AI代理入门”课程及代码示例\nhttps://github.com/microsoft/ai-agents-for-beginners\n\nP01 什么是AI代理\nP02 使用哪种AI代理框架\nP03 如何设计优秀的AI代理\nP04 什么是代理工具使用设计模式\nP05 什么是代理式RAG\nP06 如"
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 14408,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1AJen6SEVQ",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Agent智能体】教程！大模型入门到进阶，一套全解决！Agentic AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av117274400790619",
    "source": "吴恩达Agent",
    "platform": "bilibili",
    "points": 12625,
    "published_at": "2026-09-15T09:48:26+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n1. 构建智能体设计模式：反射、工具使用、规划与多智能体工作流；\n2. 将人工智能与外部工具集成：数据库、API、网络搜索与代码执行；\n3. 评估并优化人工智能系统：性能指标、错误分析与生产部署\n4、使用开放标准格式和最佳实践创建可重复使用的技能，并组合以创建复杂的工作流程。\n5、建立定制代码生成技能，审核你的代"
  },
  {
    "id": "bvid:BV1EReW6pEfv",
    "domain": "AI",
    "title": "14K Star Claude Code 开源桌面端，5个AI自己分工干活了！",
    "url": "http://www.bilibili.com/video/av117276346946735",
    "source": "程序员阿江-Relakkes",
    "platform": "bilibili",
    "points": 12379,
    "published_at": "2026-09-16T03:30:00+00:00",
    "summary": "上一期让 cc-haha 自动操作电脑，这一期，我让 5 个 AI Agent 一起做开发。\n\n用的还是我一直在维护的开源 Claude Code 桌面端：cc-haha。这次重点演示 Agent Teams：我给出一个开发需求，队长拆任务，前端、后端、测试和 Code Review 分工推进。成员做完手上的工作，还能继续领取可执行的任务，直接给队友发消息。\n\n这期用一个真实任务，从组队、共享任务"
  },
  {
    "id": "bvid:BV1pfuR69EoF",
    "domain": "AI",
    "title": "【全80集】零基础Vibe Coding教程，Vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av117070675118277",
    "source": "暴龙Boy",
    "platform": "bilibili",
    "points": 11097,
    "published_at": "2026-08-10T10:45:04+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 10820,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
  },
  {
    "id": "bvid:BV1MNeE6HEUn",
    "domain": "AI",
    "title": "穷鬼大学生开发套装：VSCode + Claude Code + DeepSeek",
    "url": "http://www.bilibili.com/video/av117273998136745",
    "source": "AI实验中心",
    "platform": "bilibili",
    "points": 10229,
    "published_at": "2026-09-15T08:03:31+00:00",
    "summary": "如果你是新手小白想尝试为AI编程入门建立编程环境，那么这个视频会帮助到你，如果你有任何问题，请评论区留言。"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 9534,
    "published_at": "2025-04-14T02:30:00+00:00",
    "summary": "MCP服务网站：https://smithery.ai/\nCherry Studio官方网站：https://cherry-ai.com/"
  },
  {
    "id": "bvid:BV1GD7qzREVA",
    "domain": "AI",
    "title": "【MCP部署实战】手把手教你把MCP接入各大热门工具，保姆级教学，我奶听了都能学会，CherryStudio配置MCP",
    "url": "http://www.bilibili.com/video/av114623818763366",
    "source": "亿点点大模型",
    "platform": "bilibili",
    "points": 9188,
    "published_at": "2025-06-04T07:08:58+00:00",
    "summary": "全程干货无废话！MCP最新实战教程，从环境部署、原理详解到项目实战，带你彻底吃透MCP！MCPServer开发，mcp开发，mcp教程，mcp项目 完整视频教程+讲解课件+学习笔记+AI大模型知识库已打包可分享！"
  },
  {
    "id": "bvid:BV1aSR4BKESW",
    "domain": "AI",
    "title": "安卓手机部署Claude Code",
    "url": "http://www.bilibili.com/video/av116526891993752",
    "source": "中国小骑士",
    "platform": "bilibili",
    "points": 7159,
    "published_at": "2026-05-06T09:24:14+00:00",
    "summary": "通过Termux安装Claude Code并且接入国内大模型"
  },
  {
    "id": "hn:49724881",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia announces native GPU programming in Rust",
    "url": "https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/",
    "source": "nonmaskable",
    "platform": "hackernews",
    "points": 643,
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
    "points": 582,
    "published_at": "2026-09-12T15:08:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:49548952",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia to acquire Hugging Face",
    "url": "https://www.cnbc.com/2026/09/03/nvidia-agrees-to-buy-hugging-face-for-almost-13-billion-ai-expansion.html",
    "source": "tosh",
    "platform": "hackernews",
    "points": 329,
    "published_at": "2026-09-03T12:10:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:49682319",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia dismisses \"circular financing\", says every $1 it invests brings back $100",
    "url": "https://invezz.com/news/2026/09/11/nvidia-says-every-1-it-invests-brings-back-100-so-why-does-the-stock-keep-falling/",
    "source": "mgh2",
    "platform": "hackernews",
    "points": 137,
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
    "points": 20,
    "published_at": "2026-09-15T15:31:55+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/no-summer-lull-for-semiconductors/",
    "domain": "AI 算力 / 半导体",
    "title": "No Summer Lull for Semiconductors",
    "url": "https://www.eetimes.com/no-summer-lull-for-semiconductors/",
    "source": "Anne-Françoise Pelé",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T08:03:34+00:00",
    "summary": "There was a time when summer slowed the semiconductor news cycle. Not this year. The post No Summer Lull for Semiconductors appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/smarter-cameras-need-more-than-edge-ai-to-protect-privacy/",
    "domain": "AI 算力 / 半导体",
    "title": "Smarter Cameras Need More Than Edge AI to Protect Privacy",
    "url": "https://www.eetimes.com/smarter-cameras-need-more-than-edge-ai-to-protect-privacy/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T18:00:00+00:00",
    "summary": "Axis Communications and Pimloc show how masking, encryption, anonymization, and governance can protect privacy without destroying useful evidence. The post Smarter Cameras Need More Than Edge AI to Pr"
  },
  {
    "id": "rss:https://www.eetimes.com/ramxeed-ultimate-feram-guarantees-10-year-data-retention-under-continuous-125c-exposure/",
    "domain": "AI 算力 / 半导体",
    "title": "RAMXEED ULTIMATE FeRAM Guarantees 10-Year Data Retention under Continuous 125°C Exposure",
    "url": "https://www.eetimes.com/ramxeed-ultimate-feram-guarantees-10-year-data-retention-under-continuous-125c-exposure/",
    "source": "RAMXEED",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T16:00:00+00:00",
    "summary": "RAMXEED launches RAMXEED ULTIMATE, a new FeRAM line with memory products guaranteeing 10 years of data retention at 125°C. The post RAMXEED ULTIMATE FeRAM Guarantees 10-Year Data Retention under Conti"
  },
  {
    "id": "rss:https://www.eetimes.com/edge-first-architectures-for-building-and-campus-safety-and-security/",
    "domain": "AI 算力 / 半导体",
    "title": "Edge-first Architectures for Building and Campus Safety and Security",
    "url": "https://www.eetimes.com/edge-first-architectures-for-building-and-campus-safety-and-security/",
    "source": "Qualcomm, Arrow Electronics",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T15:53:12+00:00",
    "summary": "Join us to explore how Qualcomm Technologies edge-first architecture is built to bring AI processing directly to cameras, gateways, and on-premises systems. The post Edge-first Architectures for Build"
  },
  {
    "id": "rss:https://www.eetimes.com/z-wave-long-range-extends-iot-reach-beyond-mesh-networks/",
    "domain": "AI 算力 / 半导体",
    "title": "Z-Wave Long Range Extends IoT Reach Beyond Mesh Networks",
    "url": "https://www.eetimes.com/z-wave-long-range-extends-iot-reach-beyond-mesh-networks/",
    "source": "Abitzen Xavier",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T14:51:54+00:00",
    "summary": "Z-Wave Long Range blasts past mesh limits with 1.5-mile IoT reach and open security. The post Z-Wave Long Range Extends IoT Reach Beyond Mesh Networks appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/pasqal-nasdaq-debut-meets-a-risk-reckoning/",
    "domain": "AI 算力 / 半导体",
    "title": "Pasqal’s Nasdaq Debut Meets a Risk Reckoning",
    "url": "https://www.eetimes.com/pasqal-nasdaq-debut-meets-a-risk-reckoning/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T08:03:27+00:00",
    "summary": "A sharp share price drop exposes the challenge of valuing quantum companies before commercial demand is proven. The post Pasqal’s Nasdaq Debut Meets a Risk Reckoning appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/aircraft-actuator-electrification-redefines-system-level-architecture/",
    "domain": "AI 算力 / 半导体",
    "title": "Aircraft Actuator Electrification Redefines System-Level Architecture",
    "url": "https://www.eetimes.com/aircraft-actuator-electrification-redefines-system-level-architecture/",
    "source": "Bill Schweber",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T19:00:00+00:00",
    "summary": "The transition from hydraulic to electric-motor aircraft actuators also encompasses many system-level issues and opportunities. The post Aircraft Actuator Electrification Redefines System-Level Archit"
  },
  {
    "id": "rss:https://www.eetimes.com/reduce-risk-cut-costs-and-speed-time-to-market-with-certified-wifi-ble-modules/",
    "domain": "AI 算力 / 半导体",
    "title": "Reduce Risk, Cut Costs, and Speed Time-to-Market with Certified WiFi & BLE Modules",
    "url": "https://www.eetimes.com/reduce-risk-cut-costs-and-speed-time-to-market-with-certified-wifi-ble-modules/",
    "source": "GigaDevice",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T17:23:09+00:00",
    "summary": "Join this webinar and learn how a certified WiFi and BLE combination module can simplify your next connected device design. The post Reduce Risk, Cut Costs, and Speed Time-to-Market with Certified WiF"
  },
  {
    "id": "rss:https://www.eetimes.com/empowering-the-future-of-robotics/",
    "domain": "AI 算力 / 半导体",
    "title": "Empowering the Future of Robotics",
    "url": "https://www.eetimes.com/empowering-the-future-of-robotics/",
    "source": "Analog Devices",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T14:00:07+00:00",
    "summary": "See how autonomous mobile robots are transforming manufacturing, warehousing, and logistics. Explore the technologies driving smarter navigation, safer operations, and greater automation. The post Emp"
  },
  {
    "id": "rss:https://www.eetimes.com/leo-satellites/",
    "domain": "AI 算力 / 半导体",
    "title": "Designing Passive Components for LEO Satellite Systems",
    "url": "https://www.eetimes.com/leo-satellites/",
    "source": "YAGEO Group",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T14:00:00+00:00",
    "summary": "Selecting passive components for LEO satellite systems is becoming increasingly complex as spacecraft architectures evolve and constellation deployments scale. Engineers must determine when commercial"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/overclocking/developer-vibe-codes-a-tool-to-let-nvidia-rtx-50-series-laptop-owners-crank-up-their-power-limits-can-juice-rtx-5090-mobile-gpu-to-225w",
    "domain": "AI 算力 / 半导体",
    "title": "Developer vibe codes a tool to let Nvidia RTX 50-series laptop owners crank up their power limits — can juice RTX 5090 mobile GPU to 225W",
    "url": "https://www.tomshardware.com/pc-components/overclocking/developer-vibe-codes-a-tool-to-let-nvidia-rtx-50-series-laptop-owners-crank-up-their-power-limits-can-juice-rtx-5090-mobile-gpu-to-225w",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T15:19:42+00:00",
    "summary": "A developer has created a fully vibe-coded tool that seems to work to allow some GeForce RTX 50-series laptops to crank their power limits by as much as 28%."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/piecemakers-bets-edge-ai-devices-will-diverge-from-reliance-on-hbm-custom-designed-memory-fuses-dram-stack-directly-to-the-processor-using-hybrid-bonding",
    "domain": "AI 算力 / 半导体",
    "title": "Piecemakers bets edge AI devices will diverge from reliance on HBM — custom-designed memory fuses DRAM stack directly to the processor using hybrid bonding",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/piecemakers-bets-edge-ai-devices-will-diverge-from-reliance-on-hbm-custom-designed-memory-fuses-dram-stack-directly-to-the-processor-using-hybrid-bonding",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T14:36:48+00:00",
    "summary": "Nanya-backed DRAM designer PieceMakers began trading in Taipei on Sept. 16 on a bet that AI inference memory won’t be HBM."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/denuvo-sues-anonymous-game-cracker-voices38-over-alleged-drm-circumvention-seeks-damages-after-anti-tamper-protections-bypassed-in-26-games",
    "domain": "AI 算力 / 半导体",
    "title": "Denuvo sues anonymous game cracker ‘voices38’ over alleged DRM circumvention — seeks damages after Anti-Tamper protections bypassed in 26 games",
    "url": "https://www.tomshardware.com/video-games/denuvo-sues-anonymous-game-cracker-voices38-over-alleged-drm-circumvention-seeks-damages-after-anti-tamper-protections-bypassed-in-26-games",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T14:22:54+00:00",
    "summary": "Instead of pursuing traditional copyright infringement, Denuvo's case relies on the DMCA's anti-circumvention provisions, targeting the alleged bypassing of its digital protections."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/micron-announces-512gb-ddr5-9200-memory-modules-with-16w-power-draw-up-to-12tb-per-server-claims-60-percent-less-energy-intensive-than-four-128gb-modules",
    "domain": "AI 算力 / 半导体",
    "title": "Micron announces 512GB DDR5-9200 memory modules with 16W power draw — up to 12TB per server, claims 60% less energy-intensive than four 128GB modules",
    "url": "https://www.tomshardware.com/pc-components/dram/micron-announces-512gb-ddr5-9200-memory-modules-with-16w-power-draw-up-to-12tb-per-server-claims-60-percent-less-energy-intensive-than-four-128gb-modules",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T14:07:31+00:00",
    "summary": "After five years, Samsung's 512GB DDR5 memory modules get their first direct rival from Micron, which also promises to offer speed bins up to 9200 MT/s. But their prices could be way too high even for"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/ai-induced-memory-shortage-is-changing-how-devices-are-built-fairphone-says-memory-now-60-percent-of-materials-cost-smaller-laptop-and-phone-makers-are-redesigning-products-and-have-to-test-for-fake-chips",
    "domain": "AI 算力 / 半导体",
    "title": "AI-induced memory shortage is changing how devices are built, Fairphone says memory now 60% of materials cost — smaller laptop and phone makers are redesigning products and have to test for fake chips",
    "url": "https://www.tomshardware.com/pc-components/ram/ai-induced-memory-shortage-is-changing-how-devices-are-built-fairphone-says-memory-now-60-percent-of-materials-cost-smaller-laptop-and-phone-makers-are-redesigning-products-and-have-to-test-for-fake-chips",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T12:15:42+00:00",
    "summary": "For smaller device manufacturers, rising memory prices are only part of the problem as limited availability forces companies to rethink everything from motherboard designs to procurement strategies."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/policy/chinese-state-media-counters-dario-amodeis-call-to-put-brakes-on-ai-development-paper-says-move-is-a-response-to-chinese-competition",
    "domain": "AI 算力 / 半导体",
    "title": "Chinese state media counters Anthropic's call to put brakes on AI development — paper says move is ‘a response to Chinese competition’",
    "url": "https://www.tomshardware.com/tech-industry/policy/chinese-state-media-counters-dario-amodeis-call-to-put-brakes-on-ai-development-paper-says-move-is-a-response-to-chinese-competition",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T12:00:00+00:00",
    "summary": "State media outlet China Daily posits that Anthropic's Dario Amodei made the call to limit frontier AI development because Chinese AI models are catching up with American AI labs."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/pick-up-a-giant-18-inch-rtx-5080-powered-asus-gaming-laptop-from-best-buy-and-save-usd600-the-rog-strix-g18-also-comes-with-32gb-of-memory-and-a-2tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Pick up a giant 18-inch RTX 5080-powered Asus gaming laptop from Best Buy and save $600 — the ROG Strix G18 also comes with 32GB of memory and a 2TB SSD",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/pick-up-a-giant-18-inch-rtx-5080-powered-asus-gaming-laptop-from-best-buy-and-save-usd600-the-rog-strix-g18-also-comes-with-32gb-of-memory-and-a-2tb-ssd",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T11:40:28+00:00",
    "summary": "Go big with an 18-inch gaming laptop monster. Save $600 on the RTX-5080-powered Asus ROG Strix G18 gaming laptop at Best Buy."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/jensen-huang-thinks-china-will-develop-its-own-advanced-lithography-systems-by-2030-nvidia-ceo-says-achievement-of-that-capability-is-just-a-matter-of-time",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang thinks China will develop its own advanced lithography chipmaking tools by 2030 — Nvidia CEO says achievement of that capability 'is just a matter of time'",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/jensen-huang-thinks-china-will-develop-its-own-advanced-lithography-systems-by-2030-nvidia-ceo-says-achievement-of-that-capability-is-just-a-matter-of-time",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T11:30:00+00:00",
    "summary": "Nvidia CEO thinks that in light of his view of a three- to four-year timeline for Chinese development of advanced semi tooling, the country is \"already there.\""
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/sk-hynix-reportedly-discussing-us-memory-chip-manufacturing-with-intel-options-include-leasing-ohio-plant-or-forming-joint-venture-with-other-ai-hyperscalers",
    "domain": "AI 算力 / 半导体",
    "title": "SK hynix reportedly discussing US memory chip manufacturing with Intel — options include leasing Ohio plant or forming joint venture with other AI hyperscalers",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/sk-hynix-reportedly-discussing-us-memory-chip-manufacturing-with-intel-options-include-leasing-ohio-plant-or-forming-joint-venture-with-other-ai-hyperscalers",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T11:20:00+00:00",
    "summary": "Sources say SK hynix and Intel are in talks to start HBM manufacturing in the United States. Both companies refused to confirm the rumors, though, as SK hynix could potentially be put in a precarious "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/defeated-gpt-6-astra-model-spent-several-hours-just-farming-potatoes-after-being-blown-up-by-a-creeper-in-minecraft-openai-offering-gets-further-than-any-other-ai-system-in-141-hour-test",
    "domain": "AI 算力 / 半导体",
    "title": "'Defeated' GPT-6 Astra model spent several hours just farming potatoes after being blown up by a Creeper in Minecraft — OpenAI offering gets further than any other AI system in 141-hour test",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/defeated-gpt-6-astra-model-spent-several-hours-just-farming-potatoes-after-being-blown-up-by-a-creeper-in-minecraft-openai-offering-gets-further-than-any-other-ai-system-in-141-hour-test",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T11:15:00+00:00",
    "summary": "OpenAI's GPT-6 Astra spent hours just farming potatoes after dying and losing all of its gear during a Minecraft test."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/amazon-reportedly-tells-customers-in-abu-dhabi-and-bahrain-to-find-safer-harbors-for-their-data-aws-has-no-timeline-for-resuming-operations-six-months-after-drone-strikes-damaged-data-centers-in-the-region",
    "domain": "AI 算力 / 半导体",
    "title": "AWS tells clients to quit Middle East data centers six months after Iranian drone strikes — Amazon offers no recovery timeline as UAE mulls underground data centers [Updated]",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/amazon-reportedly-tells-customers-in-abu-dhabi-and-bahrain-to-find-safer-harbors-for-their-data-aws-has-no-timeline-for-resuming-operations-six-months-after-drone-strikes-damaged-data-centers-in-the-region",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T11:00:00+00:00",
    "summary": "Amazon Web Services' data centers in Abu Dhabi and Bahrain were struck by drone attacks more than six months ago. Now, the company has told customers to move their data to other regions, and it has no"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-reportedly-denies-rtx-5090-warranty-over-faded-serial-number-usd6-500-gpu-blemish-not-an-isolated-incident-according-to-customers",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia reportedly denies RTX 5090 warranty over faded serial number — $6,500 GPU blemish not an isolated incident, according to customers",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-reportedly-denies-rtx-5090-warranty-over-faded-serial-number-usd6-500-gpu-blemish-not-an-isolated-incident-according-to-customers",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T10:45:00+00:00",
    "summary": "Redditor reported that Nvidia allegedly rejected their warranty claims for GeForce RTX 5090 Founders Edition graphics cards because the serial number on the bracket was unreadable."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-usd270-on-this-solid-1080p-gaming-pc-with-an-rtx-5060-from-msi-now-under-usd1-430-codex-r2-rig-packs-32gb-ddr5-ram-a-2tb-ssd-and-a-10-core-intel-cpu",
    "domain": "AI 算力 / 半导体",
    "title": "Save $270 on this solid 1080p gaming PC with an RTX 5060 from MSI, now under $1,430 — Codex R2 rig packs 32GB DDR5 RAM, a 2TB SSD, and a 10-core Intel CPU",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-usd270-on-this-solid-1080p-gaming-pc-with-an-rtx-5060-from-msi-now-under-usd1-430-codex-r2-rig-packs-32gb-ddr5-ram-a-2tb-ssd-and-a-10-core-intel-cpu",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T10:43:01+00:00",
    "summary": "Save $270 on this MSI gaming PC with a Intel Core i5-14400F, Nvidia GeForce RTX 5060, 32GB DDR5 and a 2TB SSD, all for $1,429."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/26-year-old-sony-ps2-security-chip-broken-wide-open-after-four-years-of-effort-reverse-engineering-enthusiast-successfully-unlocks-cxp102064-mechacon-chip",
    "domain": "AI 算力 / 半导体",
    "title": "Original Sony PlayStation 2 security chip ‘broken wide open’ after 26 years — chemical decapping and four years of reverse engineering unlocks MechaCon secrets",
    "url": "https://www.tomshardware.com/video-games/playstation/26-year-old-sony-ps2-security-chip-broken-wide-open-after-four-years-of-effort-reverse-engineering-enthusiast-successfully-unlocks-cxp102064-mechacon-chip",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T10:30:00+00:00",
    "summary": "The ‘magic security chip’ inside the original PlayStation 2 has been successfully reverse engineered and dumped after four years of effort."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/chinas-open-weight-ai-models-are-now-just-4-months-behind-frontier-us-offerings-mozilla-report-claims-models-still-lag-in-some-benchmarks-but-are-drastically-cheaper-to-use",
    "domain": "AI 算力 / 半导体",
    "title": "China's open-weight AI models are now just 4 months behind frontier US offerings, Mozilla report claims — models still lag in some benchmarks but are drastically cheaper to use",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/chinas-open-weight-ai-models-are-now-just-4-months-behind-frontier-us-offerings-mozilla-report-claims-models-still-lag-in-some-benchmarks-but-are-drastically-cheaper-to-use",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T10:15:00+00:00",
    "summary": "Mozilla’s State of Open Source AI report puts Kimi K3 about four months behind closed frontier models at 30% of the price."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/devastated-father-says-his-9-year-old-son-spent-usd118-000-on-youtube-ad-campaigns-for-his-minecraft-channel-using-a-company-credit-card-bill-racked-up-in-just-three-weeks-was-supposed-to-be-one-usd20-promotion",
    "domain": "AI 算力 / 半导体",
    "title": "Devastated father says his 9-year-old son spent $118,000 on YouTube ad campaigns for his Minecraft channel using a company credit card — bill racked up in just three weeks was supposed to be one $20 p",
    "url": "https://www.tomshardware.com/video-games/devastated-father-says-his-9-year-old-son-spent-usd118-000-on-youtube-ad-campaigns-for-his-minecraft-channel-using-a-company-credit-card-bill-racked-up-in-just-three-weeks-was-supposed-to-be-one-usd20-promotion",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T10:15:00+00:00",
    "summary": "A father says his 9-year-old son spent $118,000 of his employer's money on YouTube ads for Minecraft and Roblox videos in three weeks."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-enthusiast-builds-gpt-6-astra-powered-bot-to-take-on-balatros-gold-stake-black-deck-bot-leverages-python-for-numerical-tools-beats-hardest-difficulty-repeatedly",
    "domain": "AI 算力 / 半导体",
    "title": "AI enthusiast builds GPT-6 Astra-powered bot to take on Balatro's Gold Stake Black Deck — bot leverages Python for numerical tools, beats hardest difficulty repeatedly",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-enthusiast-builds-gpt-6-astra-powered-bot-to-take-on-balatros-gold-stake-black-deck-bot-leverages-python-for-numerical-tools-beats-hardest-difficulty-repeatedly",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T10:00:00+00:00",
    "summary": "A Reddit user has shared details of a new Balatro-playing AI bot that took on the infamous Gold Stake Black Deck with aplomb."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-leaders-clash-over-safety-fears-after-anthropic-whistleblower-says-ai-could-kill-us-all-by-2030-openai-anthropic-and-xai-figureheads-call-for-external-governance-while-jensen-huang-says-worries-are-made-up",
    "domain": "AI 算力 / 半导体",
    "title": "AI leaders clash over safety fears after Anthropic whistleblower says AI could 'kill us all' by 2030 — OpenAI, Anthropic and xAI figureheads call for external governance, while Jensen Huang says worri",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-leaders-clash-over-safety-fears-after-anthropic-whistleblower-says-ai-could-kill-us-all-by-2030-openai-anthropic-and-xai-figureheads-call-for-external-governance-while-jensen-huang-says-worries-are-made-up",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T17:19:36+00:00",
    "summary": "The CEOs of OpenAI and Anthropic, as well as other industry leaders, are calling for a general slowdown in AI development over safety fears. On the flip side, Chinese authorities, the U.S. President, "
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/asus-ludicrous-20th-anniversary-bundle-is-now-the-cheapest-way-to-buy-an-rtx-5090-nvidias-flagship-gpu-stock-is-so-limited-that-this-usd10-850-bundle-with-a-3000w-psu-x870e-board-and-open-frame-case-is-actually-cheaper-than-some-scalper-listings",
    "domain": "AI 算力 / 半导体",
    "title": "Asus' ludicrous $10,850 20th-anniversary bundle is now the cheapest way to buy an RTX 5090 — Nvidia's flagship GPU stock is so limited that this bundle with a 3000W PSU, X870E board, and open-frame ca",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/asus-ludicrous-20th-anniversary-bundle-is-now-the-cheapest-way-to-buy-an-rtx-5090-nvidias-flagship-gpu-stock-is-so-limited-that-this-usd10-850-bundle-with-a-3000w-psu-x870e-board-and-open-frame-case-is-actually-cheaper-than-some-scalper-listings",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T15:13:16+00:00",
    "summary": "This ultra-premium Asus ROG Edition 20th Anniversary Combo set at Newegg is super expensive at $10,849.96, but ironically, it's the 'cheapest' way to pick up an RTX 5090 right now."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-reportedly-cans-12xe-option-for-nova-lake-s-desktop-gaming-apu-design-said-to-resurface-with-razor-lake",
    "domain": "AI 算力 / 半导体",
    "title": "Intel reportedly cans 12Xe option for Nova Lake-S desktop — gaming APU design said to resurface with Razor Lake",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-reportedly-cans-12xe-option-for-nova-lake-s-desktop-gaming-apu-design-said-to-resurface-with-razor-lake",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T14:17:06+00:00",
    "summary": "Following rumors of a Nova Lake desktop SKU with 12 Xe3P cores, tipster Jaykihn suggests that Intel has canned the design and moved the target to next-gen Razor Lake instead."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/us-ai-data-centers-projected-to-become-the-fifth-largest-natural-gas-consumer-in-the-world-by-2035-consumption-to-grow-by-15-billion-cubic-feet-per-day-as-demand-for-compute-increases",
    "domain": "AI 算力 / 半导体",
    "title": "US AI data centers projected to become the fifth-largest natural gas consumer in the world by 2035 — consumption to grow by 15 billion cubic feet per day as demand for compute increases",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/us-ai-data-centers-projected-to-become-the-fifth-largest-natural-gas-consumer-in-the-world-by-2035-consumption-to-grow-by-15-billion-cubic-feet-per-day-as-demand-for-compute-increases",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T13:57:36+00:00",
    "summary": "Data centers in the U.S. are projected to use up more natural gas than most of the rest of the world to generate the electricity they need. Estimates suggest that 15 billion cubic feet per day are nee"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/bill-gates-compares-ai-to-alien-intelligence-in-movies-where-magically-the-us-and-china-solves-the-problem-together-warns-world-governments-that-theyre-not-ready-for-ai",
    "domain": "AI 算力 / 半导体",
    "title": "Bill Gates compares AI to alien intelligence in movies where ‘magically the US and China’ solve the problem together — warns world governments that they’re not ready for AI",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/bill-gates-compares-ai-to-alien-intelligence-in-movies-where-magically-the-us-and-china-solves-the-problem-together-warns-world-governments-that-theyre-not-ready-for-ai",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T12:52:53+00:00",
    "summary": "The billionaire philanthropist says that governments across the world need to work together to ensure that the people are ready for upcoming upheaval brought about by AI. He even compared the technolo"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/chatgpt-transcripts-are-reportedly-read-by-humans-to-improve-responses-including-those-with-personal-information-project-lilly-has-seen-openai-hire-hundreds-of-contractors-to-manually-review-logs",
    "domain": "AI 算力 / 半导体",
    "title": "ChatGPT transcripts are reportedly read by humans to improve responses, including those with personal information — 'Project Lilly' has seen OpenAI hire hundreds of contractors to manually review logs",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/chatgpt-transcripts-are-reportedly-read-by-humans-to-improve-responses-including-those-with-personal-information-project-lilly-has-seen-openai-hire-hundreds-of-contractors-to-manually-review-logs",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T11:30:00+00:00",
    "summary": "404 Media reports that OpenAI has hired hundreds of contractors to evaluate ChatGPT responses manually."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/windows-september-2026-update-brings-many-long-requested-features-but-also-surfaces-fresh-bugs-windows-11-update-causes-crashes-on-amd-graphics-explorer-hang-ups-and-broken-third-party-integrations",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft rolls out emergency update for Windows 11's latest patch — recent update causes crashes on AMD graphics, Explorer hang-ups, and broken third-party integrations",
    "url": "https://www.tomshardware.com/software/windows/windows-september-2026-update-brings-many-long-requested-features-but-also-surfaces-fresh-bugs-windows-11-update-causes-crashes-on-amd-graphics-explorer-hang-ups-and-broken-third-party-integrations",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T11:00:00+00:00",
    "summary": "Windows September 2026 update brings many long-requested features, but also surfaces fresh bugs — new code crashing AMD, HP, and Lenovo systems and surfaces audio, Explorer, and Remote Desktop problem"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/grab-a-usd560-saving-on-this-1440p-ready-gaming-pc-with-a-9800x3d-and-rtx-5060-ti-16gb-now-usd1-859-all-white-cyberpowerpc-desktop-ships-with-one-of-amds-best-x3d-chips-along-with-32gb-ddr5-and-a-2tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Grab a $560 saving on this 1440p-ready gaming PC with a 9800X3D and RTX 5060 Ti 16GB, now $1,859 — all-white CyberPowerPC desktop ships with one of AMD's best X3D chips, along with 32GB DDR5 and a 2TB",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/grab-a-usd560-saving-on-this-1440p-ready-gaming-pc-with-a-9800x3d-and-rtx-5060-ti-16gb-now-usd1-859-all-white-cyberpowerpc-desktop-ships-with-one-of-amds-best-x3d-chips-along-with-32gb-ddr5-and-a-2tb-ssd",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T10:36:40+00:00",
    "summary": "Save nearly $600 on this CyberPowerPC gaming PC with a 9800X3D, RTX 5060 Ti 16GB, 32GB DDR5, and a 2TB SSD."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/minecraft-legacy-gets-re-written-in-c-for-ps2-and-wii-ports-code-is-tuned-so-it-works-well-even-on-the-ps2s-meager-32mb-of-ram",
    "domain": "AI 算力 / 半导体",
    "title": "Minecraft Legacy gets rewritten in C++ for PS2 and Wii ports — code is tuned so it works well even on the PS2’s meager 32MB of RAM",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/minecraft-legacy-gets-re-written-in-c-for-ps2-and-wii-ports-code-is-tuned-so-it-works-well-even-on-the-ps2s-meager-32mb-of-ram",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T10:30:00+00:00",
    "summary": "Games optimization specialist OptiProjects (AKA OptiJeugos) has released a new port of Minecraft Legacy for the Sony PlayStation 2 and Nintendo Wii consoles."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/developer-builds-viral-3d-source-code-visualizer-that-consumes-21gb-of-ram-flies-around-2-5-million-lines-of-code-at-over-120-frames-per-second",
    "domain": "AI 算力 / 半导体",
    "title": "Developer builds viral 3D source code visualizer that consumes 21GB of RAM — flies around 2.5 million lines of code at over 120 frames per second",
    "url": "https://www.tomshardware.com/tech-industry/developer-builds-viral-3d-source-code-visualizer-that-consumes-21gb-of-ram-flies-around-2-5-million-lines-of-code-at-over-120-frames-per-second",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T10:00:00+00:00",
    "summary": "A developer has built a 3D code visualizer."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/amds-radeon-rx-9070-gre-graphics-card-returns-to-its-lowest-ever-price-of-usd499-rare-deal-places-this-current-generation-12gb-gpu-below-its-msrp-launch-price",
    "domain": "AI 算力 / 半导体",
    "title": "AMD's Radeon RX 9070 GRE graphics card returns to its lowest-ever price of $499 — rare deal places this current-generation 12GB GPU below its MSRP launch price",
    "url": "https://www.tomshardware.com/pc-components/gpus/amds-radeon-rx-9070-gre-graphics-card-returns-to-its-lowest-ever-price-of-usd499-rare-deal-places-this-current-generation-12gb-gpu-below-its-msrp-launch-price",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T09:50:21+00:00",
    "summary": "Grab a new 12GB GPU for less than the MSRP launch price."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/perplexitys-local-ai-agent-comes-to-windows-but-only-for-rtx-gpus-with-at-least-24gb-of-vram-portable-computer-brings-ai-for-multistep-tasks-to-compatible-pcs",
    "domain": "AI 算力 / 半导体",
    "title": "Perplexity’s local AI agent comes to Windows, but only for RTX GPUs with at least 24GB of VRAM — Portable Computer brings AI for multistep tasks to compatible PCs",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/perplexitys-local-ai-agent-comes-to-windows-but-only-for-rtx-gpus-with-at-least-24gb-of-vram-portable-computer-brings-ai-for-multistep-tasks-to-compatible-pcs",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T09:24:32+00:00",
    "summary": "Perplexity and Nvidia released Portable Computer for Windows on Sept. 14, bringing the local-first AI agent to GeForce RTX and RTX PRO GPUs with 24GB or more of VRAM."
  },
  {
    "id": "hn:49567357",
    "domain": "AI 算力 / 半导体",
    "title": "Georgi Gerganov on llama.cpp/ggml future after Nvidia acquisition of HuggingFace",
    "url": "https://twitter.com/ggerganov/status/2095897173376618881",
    "source": "theanonymousone",
    "platform": "hackernews",
    "points": 76,
    "published_at": "2026-09-04T17:12:22+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-says-ai-can-boost-u-s-gdp-by-32-percent-up-to-usd44-4-trillion-in-four-years-economics-model-predicts-that-displaced-employees-may-have-to-switch-to-jobs-like-electrician-and-nurse",
    "domain": "AI 算力 / 半导体",
    "title": "Anthropic says AI can boost U.S. GDP by 32%, up to $44.4 trillion in four years — economics model predicts that displaced employees 'may have to switch to jobs like electrician and nurse'",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-says-ai-can-boost-u-s-gdp-by-32-percent-up-to-usd44-4-trillion-in-four-years-economics-model-predicts-that-displaced-employees-may-have-to-switch-to-jobs-like-electrician-and-nurse",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T18:50:36+00:00",
    "summary": "Anthropic has published a paper wherein it envisions a future for the economy where AI is deeply ingrained. In the most extreme scenarios, U.S. GDP is up, but unemployment simmers as others are put ou"
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
    "id": "hn:49557813",
    "domain": "AI 算力 / 半导体",
    "title": "Tell HN: NVIDIA's Acquisition of HuggingFace was for $HuggingFace",
    "url": "https://news.ycombinator.com/item?id=49557813",
    "source": "MontagFTB",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-09-03T22:08:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:49594189",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's Jensen Huang says 'AGI has arrived' and congratulates OpenAI",
    "url": "https://www.businessinsider.com/nvidia-jensen-huang-agi-openai-astra-ai-2026-9",
    "source": "vinni2",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-09-07T05:23:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:49552375",
    "domain": "AI 算力 / 半导体",
    "title": "Texas Data Center Map: See where data centers are operating or planned",
    "url": "https://www.kxan.com/news/texas/texas-data-center-tracker-see-where-600-projects-are-operating-or-planned-across-state-in-interactive-map/",
    "source": "simonpure",
    "platform": "hackernews",
    "points": 34,
    "published_at": "2026-09-03T16:10:12+00:00",
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
    "id": "hn:49611251",
    "domain": "大厂 AI 动态",
    "title": "AlphaGenome Atlas: a high-resolution map of human DNA",
    "url": "https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphagenome-atlas/",
    "source": "utiiiD",
    "platform": "hackernews",
    "points": 605,
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
    "points": 482,
    "published_at": "2026-09-15T17:38:18+00:00",
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
    "id": "hn:49727659",
    "domain": "大厂 AI 动态",
    "title": "The DeepMind Institute",
    "url": "https://institute.deepmind.com/",
    "source": "vertigoruntime",
    "platform": "hackernews",
    "points": 170,
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
    "id": "hn:49383326",
    "domain": "大厂 AI 动态",
    "title": "Codex on AWS bedrock bug causing 10x charges",
    "url": "https://github.com/openai/codex/issues/37674",
    "source": "TheP1000",
    "platform": "hackernews",
    "points": 148,
    "published_at": "2026-08-21T03:17:43+00:00",
    "summary": ""
  },
  {
    "id": "hn:49704226",
    "domain": "大厂 AI 动态",
    "title": "Tell HN: iOS 27 does not allow Apple Intelligence to be disabled",
    "url": "https://news.ycombinator.com/item?id=49704226",
    "source": "nunez",
    "platform": "hackernews",
    "points": 73,
    "published_at": "2026-09-14T21:21:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:49735238",
    "domain": "大厂 AI 动态",
    "title": "Migrating the GitHub Copilot Runtime to Rust, Using Copilot",
    "url": "https://github.blog/ai-and-ml/generative-ai/migrating-the-github-copilot-runtime-to-rust-using-copilot/",
    "source": "abraham",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-09-17T01:12:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:49610641",
    "domain": "大厂 AI 动态",
    "title": "AlphaGenome Atlas predictive map of every DNA letter change in the human genome",
    "url": "https://deepmind.google/blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/",
    "source": "fady0",
    "platform": "hackernews",
    "points": 91,
    "published_at": "2026-09-08T14:14:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:49706941",
    "domain": "大厂 AI 动态",
    "title": "I worked at Google DeepMind. You should listen to the warnings about AI",
    "url": "https://www.theguardian.com/technology/2026/sep/14/google-deepmind-ai-warnings",
    "source": "gibspaulding",
    "platform": "hackernews",
    "points": 40,
    "published_at": "2026-09-15T02:25:41+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/996314/tiff-2026-halloween-streaming-below-crystal-lake-yaga-carrie",
    "domain": "大厂 AI 动态",
    "title": "The streamers are fighting over Halloween",
    "url": "https://www.theverge.com/entertainment/996314/tiff-2026-halloween-streaming-below-crystal-lake-yaga-carrie",
    "source": "Andrew Webster",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T03:00:00+00:00",
    "summary": "The Toronto International Film Festival is a place to go to see the future of film, but this year it also provided a glimpse at what is coming very soon in the realm of streaming. Four different strea"
  },
  {
    "id": "rss:https://www.theverge.com/tech/996078/snap-specs-intelligence-ai-agent-ios-mac",
    "domain": "大厂 AI 动态",
    "title": "Snap is launching a new Specs AI tool, and it’s coming to iOS and Mac",
    "url": "https://www.theverge.com/tech/996078/snap-specs-intelligence-ai-agent-ios-mac",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T23:40:00+00:00",
    "summary": "Snap is introducing \"Specs Intelligence,\" a new AI assistant that can connect other digital accounts to help you with things like work tasks and keeping track of travel information. It seems similar t"
  },
  {
    "id": "rss:https://www.theverge.com/tech/996422/snap-specs-hands-on-ar-glasses",
    "domain": "大厂 AI 动态",
    "title": "I wore Snap’s $2,200 smart glasses",
    "url": "https://www.theverge.com/tech/996422/snap-specs-hands-on-ar-glasses",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T23:40:00+00:00",
    "summary": "My favorite part of wearing the Specs, Snap's new augmented reality glasses, was playing dominoes. Sitting across the table from a Snap employee wearing the same pair of chunky glasses, I could select"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/996499/ai-odyssey-movie-review",
    "domain": "大厂 AI 动态",
    "title": "The 2.5-hour AI-generated Odyssey movie is 2.5 hours too long",
    "url": "https://www.theverge.com/entertainment/996499/ai-odyssey-movie-review",
    "source": "Andrew Webster",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T20:59:13+00:00",
    "summary": "Christopher Nolan's engrossing take on The Odyssey dominated at the box office and spurred a newfound interest in classic literature among filmgoers. But a new retelling of the story made entirely wit"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/996470/ai-data-center-e-waste-ban",
    "domain": "大厂 AI 动态",
    "title": "The AI data center e-waste problem is huge — and getting bigger",
    "url": "https://www.theverge.com/ai-artificial-intelligence/996470/ai-data-center-e-waste-ban",
    "source": "Justine Calma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T20:40:46+00:00",
    "summary": "E-waste from the AI boom has been vastly underestimated, a new report warns. By 2050, it could become enough trash to fill 23 million shipping containers - roughly enough 40-foot containers to circle "
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/996416/resident-zach-cregger-review",
    "domain": "大厂 AI 动态",
    "title": "Resident Evil is a comedy first and a thrilling nightmare second",
    "url": "https://www.theverge.com/entertainment/996416/resident-zach-cregger-review",
    "source": "Charles Pulliam-Moore",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T18:45:35+00:00",
    "summary": "When Paul W.S. Anderson's Resident Evil hit theaters in 2002, video game movies were largely seen as a niche. Films like Mortal Kombat and Tomb Raider had proven that big-screen game adaptations could"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/996379/metroid-ravenous-preorder-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Walmart takes a bite off the cost of Metroid Ravenous physical preorders",
    "url": "https://www.theverge.com/gadgets/996379/metroid-ravenous-preorder-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T18:20:38+00:00",
    "summary": "The Metroid series is going back to its 2D roots again with Metroid Ravenous for the Nintendo Switch 2, the first side-scrolling game in the series since 2021’s Metroid Dread for the Nintendo Switch. "
  },
  {
    "id": "rss:https://www.theverge.com/tech/996321/apple-servers-ai-nvidia",
    "domain": "大厂 AI 动态",
    "title": "Apple might make servers again to cash in on the AI rush",
    "url": "https://www.theverge.com/tech/996321/apple-servers-ai-nvidia",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T17:20:29+00:00",
    "summary": "According to The Information, Apple is planning to get back into the server game and might just pair up with Nvidia to make it happen. Apple retired its Xserve line in 2011 and has largely left enterp"
  },
  {
    "id": "rss:https://www.theverge.com/column/995939/optimizer-health-age-wearables-longevity",
    "domain": "大厂 AI 动态",
    "title": "Your ‘health age’ is fake",
    "url": "https://www.theverge.com/column/995939/optimizer-health-age-wearables-longevity",
    "source": "Victoria Song",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T17:00:00+00:00",
    "summary": "This is Optimizer, a weekly newsletter sent from Verge senior reviewer Victoria Song that dissects and discusses the latest gizmos and potions that swear they're going to change your life. Opt in for "
  },
  {
    "id": "rss:https://www.theverge.com/tech/996310/google-home-mcp-integration-agentic-ai-smart-home-price-release-date",
    "domain": "大厂 AI 动态",
    "title": "Google will now let any AI agent run your smart home",
    "url": "https://www.theverge.com/tech/996310/google-home-mcp-integration-agentic-ai-smart-home-price-release-date",
    "source": "Jennifer Pattison Tuohy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T17:00:00+00:00",
    "summary": "Google is opening up its smart home to AI agents, letting tools like Claude and Open Claw access and control your connected devices and analyze your home's data using the standardized Model Context Pr"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/16/iceland-based-treble-raises-18-million-for-its-voice-simulation-platform/",
    "domain": "大厂 AI 动态",
    "title": "Iceland-based Treble raises $18 million for its voice simulation platform",
    "url": "https://techcrunch.com/2026/09/16/iceland-based-treble-raises-18-million-for-its-voice-simulation-platform/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T05:00:00+00:00",
    "summary": "Treble's voice simulation platform is used by voice AI model developers, AI wearable, and robotics companies"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/16/your-startups-next-teammate-might-be-an-ai-agent-gusto-insight-partners-and-leland-explain-what-that-changes-at-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "Your startup’s next teammate might be an AI agent: Gusto, Insight Partners, and Leland explain what that changes at TechCrunch Disrupt 2026",
    "url": "https://techcrunch.com/2026/09/16/your-startups-next-teammate-might-be-an-ai-agent-gusto-insight-partners-and-leland-explain-what-that-changes-at-techcrunch-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T03:30:00+00:00",
    "summary": "This session will explore how early-stage companies are building teams where humans and AI agents work alongside each other — and how founders can do that without sacrificing speed, accountability, or"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/16/snap-tries-to-make-the-case-again-for-its-2200-smart-glasses/",
    "domain": "大厂 AI 动态",
    "title": "Snap tries to make the case again for its $2,200 smart glasses",
    "url": "https://techcrunch.com/2026/09/16/snap-tries-to-make-the-case-again-for-its-2200-smart-glasses/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T00:58:49+00:00",
    "summary": "Since Specs' debut earlier this year, Snap has clearly been looking for an opportunity to explain why the smart glasses deserve to exist."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/16/musks-long-time-backer-is-giving-spacex-stock-to-its-investors/",
    "domain": "大厂 AI 动态",
    "title": "Musk’s long-time backer is giving SpaceX stock to its investors",
    "url": "https://techcrunch.com/2026/09/16/musks-long-time-backer-is-giving-spacex-stock-to-its-investors/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T23:50:07+00:00",
    "summary": "Valor Equity Partners is handing out stock to its LPs instead of cash returns."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/16/al-gore-has-a-surprisingly-calm-take-on-the-ai-data-center-backlash/",
    "domain": "大厂 AI 动态",
    "title": "Al Gore says the real AI risk isn’t data centers",
    "url": "https://techcrunch.com/2026/09/16/al-gore-has-a-surprisingly-calm-take-on-the-ai-data-center-backlash/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T23:43:09+00:00",
    "summary": "In an interview with TechCrunch, Al Gore suggested he isn't losing sleep over AI data center emissions — he's more worried about the AI industry's own warnings about where the technology is headed."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/16/us-automakers-could-soon-be-forced-to-include-am-radio-for-free/",
    "domain": "大厂 AI 动态",
    "title": "US automakers could soon be forced to include AM radio for free",
    "url": "https://techcrunch.com/2026/09/16/us-automakers-could-soon-be-forced-to-include-am-radio-for-free/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T22:37:08+00:00",
    "summary": "The House of Representatives, in rare bipartisan support, overwhelmingly approved legislation that would require new vehicles to include AM radio."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/16/noise-wants-to-help-everyday-people-become-paid-content-creators/",
    "domain": "大厂 AI 动态",
    "title": "Noise wants to help everyday people become paid content creators",
    "url": "https://techcrunch.com/2026/09/16/noise-wants-to-help-everyday-people-become-paid-content-creators/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T21:35:00+00:00",
    "summary": "Marketing platform Noise is on a mission to help anyone with a smart phone make money from their content."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/16/pulley-a-carta-rival-is-shutting-down/",
    "domain": "大厂 AI 动态",
    "title": "Pulley, a Carta rival, is shutting down",
    "url": "https://techcrunch.com/2026/09/16/pulley-a-carta-rival-is-shutting-down/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T21:23:19+00:00",
    "summary": "Cap table management platform Pulley, backed by General Catalyst, Stripe, and Founders Fund, announced that it's closing shop in December."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/16/anthropic-and-openai-want-to-embed-safety-evaluators-will-they-really-be-independent/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic and OpenAI want to embed safety evaluators. Will they really be independent?",
    "url": "https://techcrunch.com/2026/09/16/anthropic-and-openai-want-to-embed-safety-evaluators-will-they-really-be-independent/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T21:07:24+00:00",
    "summary": "Anthropic and OpenAI want to embed independent safety evaluators inside their AI labs. Researchers welcome the unprecedented access, but warn meaningful oversight requires transparency, independence, "
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/16/after-accusations-of-selling-perv-glasses-meta-prepares-to-sell-a-pair-without-a-camera/",
    "domain": "大厂 AI 动态",
    "title": "After accusations of selling ‘perv glasses,’ Meta prepares to sell a pair without a camera",
    "url": "https://techcrunch.com/2026/09/16/after-accusations-of-selling-perv-glasses-meta-prepares-to-sell-a-pair-without-a-camera/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T20:12:00+00:00",
    "summary": "Can Meta dodge the \"pervert glasses\" accusations with a new camera-free product?"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/16/x-will-now-let-u-s-users-trade-via-cashtags/",
    "domain": "大厂 AI 动态",
    "title": "X will now let US users trade via Cashtags",
    "url": "https://techcrunch.com/2026/09/16/x-will-now-let-u-s-users-trade-via-cashtags/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T19:57:22+00:00",
    "summary": "The move closes the gap between the market discussions taking place on the timeline, and the market itself."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/16/automattics-interim-ceo-and-legal-chief-signed-reciprocal-severance-deals-during-mullenwegs-brief-ouster/",
    "domain": "大厂 AI 动态",
    "title": "Automattic’s interim CEO and legal chief signed reciprocal severance deals during Mullenweg’s brief ouster",
    "url": "https://techcrunch.com/2026/09/16/automattics-interim-ceo-and-legal-chief-signed-reciprocal-severance-deals-during-mullenwegs-brief-ouster/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T19:35:29+00:00",
    "summary": "CFO Mark Davies and legal chief Andy Missan signed each other’s severance agreements while Matt Mullenweg was on leave, providing a year of salary and additional equity vesting if their departures qua"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/16/former-waymo-cfo-jumps-to-self-driving-startup-wayve/",
    "domain": "大厂 AI 动态",
    "title": "Former Waymo CFO jumps to self-driving startup Wayve",
    "url": "https://techcrunch.com/2026/09/16/former-waymo-cfo-jumps-to-self-driving-startup-wayve/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T19:02:49+00:00",
    "summary": "Elisa de Martel, who left her position as chief financial officer at Alphabet's autonomous vehicle company Waymo in January, will be based out of Silicon Valley."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/16/hear-why-science-corp-ceo-max-hodak-says-the-screen-era-is-ending-at-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "Hear why Science Corp CEO Max Hodak says the screen era is ending at TechCrunch Disrupt 2026",
    "url": "https://techcrunch.com/2026/09/16/hear-why-science-corp-ceo-max-hodak-says-the-screen-era-is-ending-at-techcrunch-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T18:45:35+00:00",
    "summary": "At this year's Disrupt, Science Corp CEO Max Hodak will present a vision for screen-free interfaces that can even offer medical help. Register before September 25 to save up to $200 on your pass."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/16/ai-labs-want-in-house-auditors-but-maybe-they-should-shut-the-front-door-first/",
    "domain": "大厂 AI 动态",
    "title": "AI labs want in-house auditors — but maybe they should shut the front door first",
    "url": "https://techcrunch.com/2026/09/16/ai-labs-want-in-house-auditors-but-maybe-they-should-shut-the-front-door-first/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T18:25:25+00:00",
    "summary": "There may be a simpler and more effective fix for rogue agents, hiding in plain sight."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/16/hackers-publish-thousands-of-drivers-data-after-breaching-florida-motor-vehicle-database/",
    "domain": "大厂 AI 动态",
    "title": "Hackers publish thousands of drivers’ data after breaching Florida motor vehicle database",
    "url": "https://techcrunch.com/2026/09/16/hackers-publish-thousands-of-drivers-data-after-breaching-florida-motor-vehicle-database/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T18:00:54+00:00",
    "summary": "The ShinyHunters gang leaked the files online after saying the Florida state agency did not pay their ransom demand."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/16/your-ai-agents-can-now-control-your-google-home-devices/",
    "domain": "大厂 AI 动态",
    "title": "Your AI agents can now control your Google Home devices",
    "url": "https://techcrunch.com/2026/09/16/your-ai-agents-can-now-control-your-google-home-devices/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T17:00:00+00:00",
    "summary": "Google is launching early access to a new MCP server for Google Home, allowing AI agents like Claude, ChatGPT, and others to control connected devices, review camera summaries, and access smart home a"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/16/anthropic-merges-claude-chat-and-cowork-in-one-interface/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic merges Claude chat and Cowork in one interface",
    "url": "https://techcrunch.com/2026/09/16/anthropic-merges-claude-chat-and-cowork-in-one-interface/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T16:30:00+00:00",
    "summary": "Anthropic is initially releasing these features to Pro and Max plan subscribers."
  },
  {
    "id": "rss:https://techcrunch.com/video/how-fortell-is-using-ai-and-163m-to-crack-a-hearing-aid-monopoly/",
    "domain": "大厂 AI 动态",
    "title": "How Fortell is using AI (and $163M) to crack a hearing aid monopoly",
    "url": "https://techcrunch.com/video/how-fortell-is-using-ai-and-163m-to-crack-a-hearing-aid-monopoly/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T16:00:00+00:00",
    "summary": "“Why do I have to beg my grandparents to put on their hearing aids, but no one has ever needed to ask me to put on my glasses?”&#160; That’s&#160;the question that drove&#160;Matthew de Jonge&#160;to "
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/16/may-mobility-is-going-public-in-a-1-4b-spac-deal/",
    "domain": "大厂 AI 动态",
    "title": "May Mobility is going public in a $1.4B SPAC deal",
    "url": "https://techcrunch.com/2026/09/16/may-mobility-is-going-public-in-a-1-4b-spac-deal/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T15:27:13+00:00",
    "summary": "The deal could net the asset-light robotaxi company more than $300 million in funding."
  },
  {
    "id": "rss:https://stratechery.com/2026/salesforce-ai-force-agents-as-ui-the-race-to-headless/",
    "domain": "大厂 AI 动态",
    "title": "Salesforce AI Force, Agents as UI, The Race to Headless",
    "url": "https://stratechery.com/2026/salesforce-ai-force-agents-as-ui-the-race-to-headless/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T10:18:04+00:00",
    "summary": "Salesforce is abandoning UI as a moat, which is a very smart move because it's disappearing for everyone."
  },
  {
    "id": "rss:https://stratechery.com/2026/openai-ads-amazon-ads-in-chatgpt-walmart-to-accept-apple-pay/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI Ads, Amazon Ads in ChatGPT, Walmart to Accept Apple Pay",
    "url": "https://stratechery.com/2026/openai-ads-amazon-ads-in-chatgpt-walmart-to-accept-apple-pay/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T10:00:00+00:00",
    "summary": "ChatGPT ads are working, and solve Amazon's biggest problem with chatbots. Then, Walmart finally gives in to Apple Pay, because fighting the status quo is hard."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/09/apple-reportedly-building-server-packed-with-m-series-ultra-chips-for-ai/",
    "domain": "大厂 AI 动态",
    "title": "Apple reportedly building server packed with M-series Ultra chips for AI",
    "url": "https://arstechnica.com/ai/2026/09/apple-reportedly-building-server-packed-with-m-series-ultra-chips-for-ai/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T22:02:46+00:00",
    "summary": "Planned 2029 debut could make this Apple’s first enterprise server in decades."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/09/lawsuit-trump-doj-notified-very-few-victims-in-epsteins-stash-of-child-sex-images/",
    "domain": "大厂 AI 动态",
    "title": "Epstein had huge cache of child sex pics; victims sue to find out who's in them",
    "url": "https://arstechnica.com/tech-policy/2026/09/lawsuit-trump-doj-notified-very-few-victims-in-epsteins-stash-of-child-sex-images/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T21:42:09+00:00",
    "summary": "Survivors appalled nobody will tell them if they’re in Epstein’s CSAM collection."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/09/nonprofit-that-tracks-meteors-taken-down-by-critical-blow-from-a-cyberattack/",
    "domain": "大厂 AI 动态",
    "title": "Nonprofit that tracks meteors taken down by \"critical blow\" from a cyberattack",
    "url": "https://arstechnica.com/security/2026/09/nonprofit-that-tracks-meteors-taken-down-by-critical-blow-from-a-cyberattack/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T21:08:14+00:00",
    "summary": "Group plans to be largely out of commission for several weeks."
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/09/haymitch-gets-a-backstory-in-sunrise-on-the-reaping-trailer/",
    "domain": "大厂 AI 动态",
    "title": "Lionsgate releases a new trailer for Sunrise on the Reaping",
    "url": "https://arstechnica.com/culture/2026/09/haymitch-gets-a-backstory-in-sunrise-on-the-reaping-trailer/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T20:44:41+00:00",
    "summary": "Also: Laika Studios debuts a stunning full-length trailer for its stop-motion feature, Wildwood."
  },
  {
    "id": "rss:https://arstechnica.com/gaming/2026/09/not-just-proton-getting-to-know-valves-new-steamos-compatibility-layers/",
    "domain": "大厂 AI 动态",
    "title": "Not just Proton: Getting to know Valve's new SteamOS compatibility layers",
    "url": "https://arstechnica.com/gaming/2026/09/not-just-proton-getting-to-know-valves-new-steamos-compatibility-layers/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T20:23:16+00:00",
    "summary": "New system-level tools bring Arm chipsets, Android APKs into the Steam ecosystem."
  },
  {
    "id": "hn:49691343",
    "domain": "股票",
    "title": "Nike exits the S&P 100 after 18 years and a $200B market-cap wipeout",
    "url": "https://fortune.com/2026/09/08/nike-stock-plummets-sp500-market-cap-index/",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 314,
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
    "points": 287,
    "published_at": "2026-09-09T01:57:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:49599992",
    "domain": "股票",
    "title": "Stockfish 19",
    "url": "https://stockfishchess.org/blog/2026/stockfish-19/",
    "source": "atiedebee",
    "platform": "hackernews",
    "points": 277,
    "published_at": "2026-09-07T16:17:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:49712746",
    "domain": "股票",
    "title": "Global bond yields hit 2008 highs, raising stakes for big borrowers",
    "url": "https://www.reuters.com/world/asia-pacific/bond-selloff-drives-us-benchmark-beyond-5-stocks-rattled-2026-09-15/",
    "source": "kaycebasques",
    "platform": "hackernews",
    "points": 165,
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
    "points": 161,
    "published_at": "2026-09-08T14:54:57+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3781953",
    "domain": "股票",
    "title": "A股三大股指集体收跌，农业种植掀涨停潮，航运、创新药逆势大涨，贵金属齐跌，港股AI大模型股双雄集体反弹",
    "url": "https://wallstreetcn.com/articles/3781953",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T08:25:58+00:00",
    "summary": "盘面上，个股涨跌互现，全市场超2800只个股下跌。今日成交1.84万亿。沪深两市成交额1.82万亿，较上一个交易日缩量160亿。板块方面，覆铜板、黄金、稀土、电力、石化板块表现低迷，创新药、农业股全天强势，炒作资金午后流向海运、发电设备、汽车板块。"
  },
  {
    "id": "wscn:3781982",
    "domain": "股票",
    "title": "理想i9搭载自研电池，李想称把产品的决定权握在自己手里",
    "url": "https://wallstreetcn.com/articles/3781982",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T08:08:26+00:00",
    "summary": "理想i9售价36.98万元，是理想汽车第二代纯电平台的首发旗舰，首次集中实现自研电池、电驱、智驾芯片和智驾模型四项核心技术量产搭载。新车首批搭载宁德时代电池，后续将切换为理想自研电池。随着整车厂与供应商关系重构，理想正通过核心部件自研自制，进一步强化对产品和供应链的掌控。"
  },
  {
    "id": "wscn:3781981",
    "domain": "股票",
    "title": "“木头姐”预测SpaceX星舰发射将创造10万亿美元收入，马斯克回应：并非不可能",
    "url": "https://wallstreetcn.com/articles/3781981",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T08:01:58+00:00",
    "summary": "“木头姐”Cathie Wood预测，星舰单次发射或对应约10亿美元年收入，若按马斯克2030年年发射1万次的目标推算，年收入规模可能达10万亿美元，马斯克回应“并非不可能”。这一测算基于Starlink V3的带宽变现潜力，星舰第14次飞行将搭载量产版V3卫星，并成为首次产生收入的飞行。"
  },
  {
    "id": "wscn:3781983",
    "domain": "股票",
    "title": "日央行周五若“鸽派加息”：日元恐失守158、再试160",
    "url": "https://wallstreetcn.com/articles/3781983",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T08:01:20+00:00",
    "summary": "美联储鹰派加息推升美元，日元下挫至155.98附近。尽管日本央行周五预计加息25个基点，但市场已充分定价，难抵美日高利差压制。分析认为，若植田和男后续未能给出明确的连续紧缩路径，日元汇率恐面临即时走弱压力，跌破158关口并再次下探160。"
  },
  {
    "id": "wscn:3781980",
    "domain": "股票",
    "title": "美联储释放鹰派信号后，高盛改口：10月预计再加25基点",
    "url": "https://wallstreetcn.com/articles/3781980",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T07:47:33+00:00",
    "summary": "高盛将10月加息纳入基准的核心逻辑在于：美联储既已将本次加息定性为支持\"更及时回归\"2%目标的举措，在连续会议上跟进比隔次加息更为自然。不过，高盛认为超出两次的追加加息并非基准情景，主要依据是其自身对通胀的预测低于美联储委员中值。"
  },
  {
    "id": "wscn:3781977",
    "domain": "股票",
    "title": "华为全联接大会：昇腾960超节点正式发布！新款AI芯片将提前9个月推出",
    "url": "https://wallstreetcn.com/articles/3781977",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T07:34:26+00:00",
    "summary": "华为轮值董事长汪涛在华为全联接大会2026宣布：昇腾960DT提前三个季度至2027年Q1发布，性能翻番；业界首个量产NPO形态光互联产品Hi-ONE亮相，单引擎传输容量达7.2T，替代4.8万颗光模块、降低550千瓦功耗；昇腾950超节点已规模商用超1000套。"
  },
  {
    "id": "wscn:3781978",
    "domain": "股票",
    "title": "Kimi金融行业方案来了！中信、中金等数十家机构已落地",
    "url": "https://wallstreetcn.com/articles/3781978",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T07:26:46+00:00",
    "summary": "月之暗面发布Kimi金融行业解决方案。该方案一站式接入10余个权威数据源，内置9项金融专业技能与5项安全合规措施，具备机构级数据建模与报告交付能力。工商银行、中信建投、中金公司、易方达基金等数十家金融机构已在实际业务中落地该金融行业解决方案。"
  },
  {
    "id": "wscn:3781974",
    "domain": "股票",
    "title": "“AI交易”还能继续吗？",
    "url": "https://wallstreetcn.com/articles/3781974",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T07:06:25+00:00",
    "summary": "科技股全年涨15%，但驱动逻辑正在收窄。Altimeter Capital创始人Brad Gerstner警告，Anthropic、OpenAI和SpaceX年化营收年底须从目前的1000亿增至1800亿美元，“AI交易”才能自洽。前沿实验室的“月度营收”已成决定市场生死的绝对核心。他直言：2026年，跟着事实走，拒绝杠杠押注。"
  },
  {
    "id": "wscn:3781975",
    "domain": "股票",
    "title": "华为“韬定律”新进展：提前9个月，昇腾960完成“从0到1”",
    "url": "https://wallstreetcn.com/articles/3781975",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T06:40:30+00:00",
    "summary": "华为昇腾960DT宣布提前9个月、于2027年Q1发布，性能实现翻番；昇腾950超节点已规模商用，部署超1000套。IDC数据显示，2025年中国AI加速卡市场，华为以81.2万张居国内首位。华为明确战略边界：不押注自研大模型，而是让百模高效跑在昇腾硬件上，以\"超节点+集群\"路径加速交付。"
  },
  {
    "id": "wscn:3781972",
    "domain": "股票",
    "title": "诺和诺德、礼来、字节系落子AI制药，A股创新药、CRO板块嗨了",
    "url": "https://wallstreetcn.com/articles/3781972",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T06:26:00+00:00",
    "summary": "诺和诺德与Anthropic达成AI合作，金斯瑞携手礼来TuneLab平台提供湿实验验证，字节拆分的Anew Labs亦获2.9亿美元融资。多重重磅合作与融资密集落地，显现AI制药协作热潮，带动A股创新药、CRO板块大涨。"
  },
  {
    "id": "wscn:3781970",
    "domain": "股票",
    "title": "SpaceX是防御性AI股吗？",
    "url": "https://wallstreetcn.com/articles/3781970",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T06:20:48+00:00",
    "summary": "AI股承压之际，大摩力挺SpaceX具备最强防御属性，维持300美元目标价。分析师认为其航天与星链业务筑起现金流护城河，而“轨道AI”等长期潜能几乎被市场零估值。叠加马斯克卓越的危机执行力，当下正是低位押注天基AI巨头的绝佳窗口。"
  },
  {
    "id": "wscn:3781896",
    "domain": "股票",
    "title": "49:50倒在60票门槛前：美国加密立法真空还要多久？",
    "url": "https://wallstreetcn.com/premium/articles/3781896?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T05:43:52+00:00",
    "summary": "CLARITY 法案未达60票，加密监管真空延长，市场抛售，年内立法窗口显著收窄，行政监管仍可补位。"
  },
  {
    "id": "wscn:3781965",
    "domain": "股票",
    "title": "张忆东：快则本周，慢则九月底，中国股市有望获得向上转机",
    "url": "https://wallstreetcn.com/articles/3781965",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T05:20:54+00:00",
    "summary": "九月是逢低布局中国资产和全球AI牛市的好时机。"
  },
  {
    "id": "wscn:3781968",
    "domain": "股票",
    "title": "核心是算力！华为轮值董事长谈AI战略",
    "url": "https://wallstreetcn.com/articles/3781968",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T05:20:31+00:00",
    "summary": "华为副董事长、轮值董事长汪涛表示：“华为AI战略的核心是算力，将坚持硬件变现；将通过‘超节点+集群’，为国家打造坚实的算力底座，为世界构建新的选择。”华为将提供线下+线上的灵活算力方案，加速千行万业智能化发展；还将通过创新推出多样性算力，推进AI入端、上车，让智能无所不及。"
  },
  {
    "id": "wscn:3781969",
    "domain": "股票",
    "title": "美联储鹰派加息落地 黄金走弱 科技股表现相对坚挺",
    "url": "https://wallstreetcn.com/articles/3781969",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T04:54:41+00:00",
    "summary": "美联储三年来首次加息且暗示未来货币政策将继续收紧。利率决议过后，美元升至五周高点，黄金短线急跌，但科..."
  },
  {
    "id": "wscn:3781946",
    "domain": "股票",
    "title": "付鹏点评9月美联储加息：沃什释放鹰派信号，能源裂解价差成为通胀关注点，美债熊平确认【付鹏说图表】",
    "url": "https://wallstreetcn.com/premium/articles/3781946?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T04:06:09+00:00",
    "summary": "凯文沃什对于通胀的关注排在了首位，态度非常的坚决，加息被他表述成“去掉一剂宽松”"
  },
  {
    "id": "wscn:3781962",
    "domain": "股票",
    "title": "GPU云服务掀涨价潮：Nebius再提价20%，算力供给侧迎议价权反转",
    "url": "https://wallstreetcn.com/articles/3781962",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T04:05:30+00:00",
    "summary": "Nebius10月1日起GPU云服务全线提价约20%，H100至B300多款芯片悉数上调，这已是数月内第二轮涨价，B300累计涨幅高达56%。需求能见度超24个月、客户抢购Blackwell算力甚至愿意溢价竞拍。AI算力供需失衡正在重塑整个行业谈判格局，议价权正悄然向供给侧转移。"
  },
  {
    "id": "wscn:3781943",
    "domain": "股票",
    "title": "摩根大通全球宏观大会：央行可能比预期“更快更大幅度加息”，但“股票与债券收益率”可能“齐涨”",
    "url": "https://wallstreetcn.com/articles/3781943",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T03:57:44+00:00",
    "summary": "摩根大通全球宏观大会核心判断，美联储等央行加息节奏将远超市场预期，均衡利率还需上行约100bp，风险明显偏向\"更快更大\"，但该行仍看高标普500至8000点，因AI巨额资本支出，以及实体经济对利率敏感度骤降。市场对美债收益率的“恐惧阈值”已大幅上移至5.5%-6.0%，只要升息有序便无碍股市。同时，长端利率飙升的本质是全球财政扩张与40万亿巨额美债驱动。"
  },
  {
    "id": "wscn:3781964",
    "domain": "股票",
    "title": "大批AI影视剧即将抵达战场，谁会拿到新入场券",
    "url": "https://wallstreetcn.com/articles/3781964",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T03:47:26+00:00",
    "summary": "谁能分到钱？"
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
    "id": "hn:49401229",
    "domain": "股票",
    "title": "Anthropic IPO filing will show AI backlash as a risk factor, sources say",
    "url": "https://www.cnbc.com/2026/08/21/-anthropic-ipo-filing-will-show-ai-backlash-as-risk-sources-say.html",
    "source": "newsomix9xl",
    "platform": "hackernews",
    "points": 37,
    "published_at": "2026-08-22T16:23:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:49593962",
    "domain": "股票",
    "title": "HPE Gives Oracle Right to Buy 4.2M Shares for 1 Cent Each",
    "url": "https://www.forbes.com/sites/antoniopequenoiv/2026/09/03/hewlett-packard-enterprise-gives-oracle-right-to-buy-205-million-in-stock-at-slashed-rate/",
    "source": "gurjeet",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-09-07T04:38:32+00:00",
    "summary": ""
  },
  {
    "id": "hn:49596033",
    "domain": "股票",
    "title": "Show HN: Forget Rigid Stock Screeners – A Universal Query API for Financial Data",
    "url": "https://financialdata.net/universal-query",
    "source": "_FDN_",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-09-07T09:24:17+00:00",
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
    "id": "hn:49355142",
    "domain": "金融",
    "title": "Sticky wage norms and the real wage cost of unexpected inflation",
    "url": "https://bfi.uchicago.edu/wp-content/uploads/2026/08/BFI_WP_2026-108-1.pdf",
    "source": "jplusequalt",
    "platform": "hackernews",
    "points": 392,
    "published_at": "2026-08-19T00:53:51+00:00",
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
    "id": "hn:49704008",
    "domain": "金融",
    "title": "Amazon vs. Perplexity – U.S. Court of Appeals for the Ninth Circuit",
    "url": "https://law.justia.com/cases/federal/appellate-courts/ca9/26-1444/26-1444-2026-08-04.html",
    "source": "neom",
    "platform": "hackernews",
    "points": 216,
    "published_at": "2026-09-14T21:05:22+00:00",
    "summary": ""
  },
  {
    "id": "hn:49731356",
    "domain": "金融",
    "title": "Fed hikes rates as inflation worries push up bond yields",
    "url": "https://www.reuters.com/live/live-fed-rate-hike-expected-inflation-worries-push-up-bond-yields-2026-09-16/",
    "source": "wslh",
    "platform": "hackernews",
    "points": 168,
    "published_at": "2026-09-16T18:55:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:49602582",
    "domain": "金融",
    "title": "A Tesla ran a stop sign and killed a man, Full Self-Driving/Autopilot was on",
    "url": "https://electrek.co/2026/09/07/tesla-driver-assist-stop-sign-buena-vista/",
    "source": "FabHK",
    "platform": "hackernews",
    "points": 169,
    "published_at": "2026-09-07T20:21:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:49694840",
    "domain": "金融",
    "title": "How Much Has Trump Made from Crypto? ($1.4B from 2025 Federal Disclosure)",
    "url": "https://www.thepricer.org/how-much-has-trump-made-from-crypto/",
    "source": "cinderelacinder",
    "platform": "hackernews",
    "points": 112,
    "published_at": "2026-09-14T10:56:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:49601846",
    "domain": "金融",
    "title": "Tesla killing Solar Roof is leaving installers with six-figure losses",
    "url": "https://electrek.co/2026/09/01/tesla-solar-roof-exit-installers-losses/",
    "source": "voxadam",
    "platform": "hackernews",
    "points": 135,
    "published_at": "2026-09-07T19:08:47+00:00",
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
    "id": "hn:49700413",
    "domain": "金融",
    "title": "US 10-Year Breaches 5% as Inflation, Supply Worries Mount",
    "url": "https://www.bloomberg.com/news/articles/2026-09-14/us-10-year-yield-breaches-5-as-inflation-supply-worries-mount",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 71,
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
    "points": 33,
    "published_at": "2026-09-16T18:09:36+00:00",
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
    "id": "hn:49596610",
    "domain": "金融",
    "title": "Initial effects of AI technology on employment look positive",
    "url": "https://www.economist.com/finance-and-economics/2026/09/04/the-jobs-apocalypse-is-postponed-an-ai-jobs-boom-is-here",
    "source": "MrBuddyCasino",
    "platform": "hackernews",
    "points": 101,
    "published_at": "2026-09-07T10:38:32+00:00",
    "summary": ""
  },
  {
    "id": "hn:49730731",
    "domain": "金融",
    "title": "Fed Raises Rates as Warsh Bucks Trump to Contain Inflation",
    "url": "https://www.bloomberg.com/news/articles/2026-09-16/fed-raises-rates-as-warsh-bucks-trump-to-contain-inflation",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-09-16T18:05:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:49599058",
    "domain": "金融",
    "title": "If a Tesla Cybercab fleet were profitable, Tesla wouldn't sell you one",
    "url": "https://electrek.co/2026/09/07/tesla-cybercab-fleet-profitable-wouldnt-sell/",
    "source": "jijojv",
    "platform": "hackernews",
    "points": 99,
    "published_at": "2026-09-07T14:49:43+00:00",
    "summary": ""
  },
  {
    "id": "hn:49730841",
    "domain": "金融",
    "title": "Fed approves interest rate hike, signals one more to come this year",
    "url": "https://www.cnbc.com/2026/09/16/fed-rate-decision-september-2026.html",
    "source": "rawgabbit",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-09-16T18:14:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:49626052",
    "domain": "金融",
    "title": "One woman's Tesla was remotely controlled by an abusive ex-partner",
    "url": "https://www.theguardian.com/australia-news/2026/sep/09/how-one-womans-tesla-was-remotely-controlled-and-harass-by-her-abusive-ex-partner-ntwnfb",
    "source": "gradschool",
    "platform": "hackernews",
    "points": 74,
    "published_at": "2026-09-09T13:16:45+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.17609",
    "domain": "金融",
    "title": "Separated Signal Libraries: Packing, Saturation, and Joint Spectral Limits",
    "url": "https://arxiv.org/abs/2609.17609",
    "source": "Marc da Costa Nunes",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T04:00:00+00:00",
    "summary": "arXiv:2609.17609v1 Announce Type: new Abstract: We study libraries of cross-sectional signals: at each date, a forecast vector over $d$ assets intended to predict the next period's cross-sectional ret"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.17788",
    "domain": "金融",
    "title": "SAiFE-gym: Model-based Environments for Automated Market Making with Concentrated Liquidity",
    "url": "https://arxiv.org/abs/2609.17788",
    "source": "Georgios Chionas, Charalampos Kleitsikas, Stefanos Leonardos, Leandro S\\'anchez-Betancourt, Carmine Ventre",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T04:00:00+00:00",
    "summary": "arXiv:2609.17788v1 Announce Type: new Abstract: We present SAiFE_gym, a Python module that provides a collection of simulation environments for studying trading problems in Constant Product Markets (C"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.17869",
    "domain": "金融",
    "title": "Demystifying the Bergomi-Guyon expansion",
    "url": "https://arxiv.org/abs/2609.17869",
    "source": "Florian Bourgey, Jim Gatheral",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T04:00:00+00:00",
    "summary": "arXiv:2609.17869v1 Announce Type: new Abstract: Al\\`os, Gatheral and Radoi\\v{c}i\\'c derived the Bergomi-Guyon expansion of the implied variance smile from the forest expansion of the cumulant generati"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.17989",
    "domain": "金融",
    "title": "Whom Do AI Agents Work For? Role Assignment Induces Sponsorship Bias in LLM Recommenders",
    "url": "https://arxiv.org/abs/2609.17989",
    "source": "Davood Wadi, Yu Ma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T04:00:00+00:00",
    "summary": "arXiv:2609.17989v1 Announce Type: new Abstract: Large language models (LLMs) now serve as conversational shopping assistants on platforms that also sell advertising. These AI agents face a conflict of"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.18019",
    "domain": "金融",
    "title": "Model-Free Passive Execution via Order-Level Shadowing",
    "url": "https://arxiv.org/abs/2609.18019",
    "source": "Vincent Maciejewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T04:00:00+00:00",
    "summary": "arXiv:2609.18019v1 Announce Type: new Abstract: Automated execution algorithms are organized into schedule-based and liquidity-seeking families. This paper concerns the first, whose members -- Time-We"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.18161",
    "domain": "金融",
    "title": "Why a Non-Discriminatory Royalty Surcharge Is Not Chip-Neutral: The Error in FTC v. Qualcomm",
    "url": "https://arxiv.org/abs/2609.18161",
    "source": "Sang-Seung Yi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T04:00:00+00:00",
    "summary": "arXiv:2609.18161v1 Announce Type: new Abstract: Qualcomm's No License, No Chips policy let it levy a royalty surcharge on every handset, whether or not it used a Qualcomm modem chip. In FTC v. Qualcom"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.18441",
    "domain": "金融",
    "title": "Multitask Reinforcement Learning for Assisting Choice Model Specification",
    "url": "https://arxiv.org/abs/2609.18441",
    "source": "Gabriel Nova, Stephane Hess, Sander Van Cranenburgh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T04:00:00+00:00",
    "summary": "arXiv:2609.18441v1 Announce Type: new Abstract: Discrete choice model specification is a time-consuming task in which modellers often specify and estimate multiple models while balancing goodness-of-f"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.18750",
    "domain": "金融",
    "title": "PPML and Heavy-Tailed Trade and Factor Flows: Why Standard Inference Fails and How to Fix It",
    "url": "https://arxiv.org/abs/2609.18750",
    "source": "Peter H. Egger, Ting Ji, Yulong Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T04:00:00+00:00",
    "summary": "arXiv:2609.18750v1 Announce Type: new Abstract: The Poisson pseudo-maximum likelihood (PPML) estimator is widely used for estimating bilateral gravity equations. Its consistency requires only a correc"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.18975",
    "domain": "金融",
    "title": "Sniper Cohorts and Algorithmic Filter Rejections in Solana Memecoin Markets: Two-Window Replication of Lifecycle-Stage Population Separation",
    "url": "https://arxiv.org/abs/2609.18975",
    "source": "Arati Uday Kamat",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T04:00:00+00:00",
    "summary": "arXiv:2609.18975v1 Announce Type: new Abstract: Prior empirical work on Solana memecoin markets has often conflated pre-graduation (bonding-curve) and post-graduation (open-market) token populations. "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.19032",
    "domain": "金融",
    "title": "A Tale of Two Cities: The Announcement Effect of Northern Metropolis Plan",
    "url": "https://arxiv.org/abs/2609.19032",
    "source": "Yi Fan, Chongyu Wang, Ke Xu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T04:00:00+00:00",
    "summary": "arXiv:2609.19032v1 Announce Type: new Abstract: Using the October 2021 announcement of Hong Kong's Northern Metropolis Plan as a quasi-natural experiment, we examine its impacts on households, firms, "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.19033",
    "domain": "金融",
    "title": "Intergenerational Mobility in China",
    "url": "https://arxiv.org/abs/2609.19033",
    "source": "Yi Fan, Junjian Yi, Junsen Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T04:00:00+00:00",
    "summary": "arXiv:2609.19033v1 Announce Type: new Abstract: In this chapter, we provide a synthesis of empirical work on the intergenerational mobility in China, examining how much a child's success depends on th"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.19034",
    "domain": "金融",
    "title": "Power Up Consumption: Impact of Electric Vehicle Infrastructure on Household Finance",
    "url": "https://arxiv.org/abs/2609.19034",
    "source": "Sumit Agarwal, Yi Fan, Qiuxia Gao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T04:00:00+00:00",
    "summary": "arXiv:2609.19034v1 Announce Type: new Abstract: To achieve carbon neutrality, electrifying vehicles in a cleaner electricity grid has become a key pathway for global cities. While extensive research h"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.19094",
    "domain": "金融",
    "title": "Quadratic G-BSDEs for bond pricing with endogenous short-rate feedback",
    "url": "https://arxiv.org/abs/2609.19094",
    "source": "Jaehyun Kim, Hyungbin Park",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T04:00:00+00:00",
    "summary": "arXiv:2609.19094v1 Announce Type: new Abstract: We study robust bond valuation with endogenous short-rate feedback under volatility uncertainty. Within the $G$-expectation framework, the dependence of"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.19102",
    "domain": "金融",
    "title": "Optimal entry and exit for variance swaps: closed-form rules for the perpetual contract",
    "url": "https://arxiv.org/abs/2609.19102",
    "source": "Jun Maeda",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T04:00:00+00:00",
    "summary": "arXiv:2609.19102v1 Announce Type: new Abstract: Variance swaps are a convenient instrument for trading vega and convexity, and a listed contract now trades on Cboe. We ask when a trader should put suc"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.17608",
    "domain": "金融",
    "title": "Equilibrium Selection in Coordination Games with Planned Actions and Scouting",
    "url": "https://arxiv.org/abs/2609.17608",
    "source": "Wolfgang Kuhle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T04:00:00+00:00",
    "summary": "arXiv:2609.17608v1 Announce Type: cross Abstract: We study coordination games in which every action requires planning and preparation. Before players act, they can revise their plans based on partiall"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.17610",
    "domain": "金融",
    "title": "On-Demand Combinatorial Event Markets on Kalshi: Instantiation, Concentration, and Effective Market Breadth",
    "url": "https://arxiv.org/abs/2609.17610",
    "source": "Maksym Nechepurenko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T04:00:00+00:00",
    "summary": "arXiv:2609.17610v1 Announce Type: cross Abstract: Kalshi's multivariate-event architecture produces market objects on demand from exact selected legs. Across a registered seven-day interval, 190 indep"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.18287",
    "domain": "金融",
    "title": "A continuous-time dynamic contracting problem with limited liability and finite horizon",
    "url": "https://arxiv.org/abs/2609.18287",
    "source": "Andrea Bovo, Tiziano De Angelis, St\\'{e}phane Villeneuve",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T04:00:00+00:00",
    "summary": "arXiv:2609.18287v1 Announce Type: cross Abstract: We perform a detailed study of a principal--agent problem in a continuous time version of the celebrated Holmstr\\\"om--Milgrom model (Econometrica 55 ("
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.18591",
    "domain": "金融",
    "title": "Recursive Reasoning or Statistical Extrapolation? In-Context Learning in Multi-Agent Interdependent Decision-Making",
    "url": "https://arxiv.org/abs/2609.18591",
    "source": "Yu Liu, Wenwen Li, Yifan Dou, Guangnan Ye",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T04:00:00+00:00",
    "summary": "arXiv:2609.18591v1 Announce Type: cross Abstract: In-context learning (ICL) enables large language model (LLM) agents to improve decisions using interaction history, yet it remains unclear whether suc"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.18770",
    "domain": "金融",
    "title": "Regularity of a Multidimensional Principal-Agent Problem with Separable Effort Costs",
    "url": "https://arxiv.org/abs/2609.18770",
    "source": "Shuaijie Qian, Guan Qiao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T04:00:00+00:00",
    "summary": "arXiv:2609.18770v1 Announce Type: cross Abstract: This paper studies the regularity of the value function arising from a multidimensional continuous-time principal-agent model with separable, nonquadr"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.19013",
    "domain": "金融",
    "title": "Policy-Selected Transaction Tapes in Automated Market Makers: Ranking Certification under Hidden Opportunities",
    "url": "https://arxiv.org/abs/2609.19013",
    "source": "Wen-Ting Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T04:00:00+00:00",
    "summary": "arXiv:2609.19013v1 Announce Type: cross Abstract: Programmable matching mechanisms decide which orders become data. A loss metric computed from a mechanism's own transaction tape therefore mixes execu"
  },
  {
    "id": "rss:https://arxiv.org/abs/2312.17375",
    "domain": "金融",
    "title": "Causal Discovery in Financial Markets: A Framework for Nonstationary Time-Series Data",
    "url": "https://arxiv.org/abs/2312.17375",
    "source": "Agathe Sadeghi, Achintya Gopal, Mohammad Fesanghary",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T04:00:00+00:00",
    "summary": "arXiv:2312.17375v4 Announce Type: replace Abstract: This paper introduces a new causal structure learning method for nonstationary time series data, a common data type found in fields such as finance,"
  },
  {
    "id": "rss:https://arxiv.org/abs/2407.15536",
    "domain": "金融",
    "title": "Calibrating the Heston model with deep differential networks",
    "url": "https://arxiv.org/abs/2407.15536",
    "source": "Chen Zhang, Giovanni Amici, Marco Morandotti",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T04:00:00+00:00",
    "summary": "arXiv:2407.15536v4 Announce Type: replace Abstract: We propose a gradient-based deep learning framework to calibrate the Heston option pricing model (Heston, 1993). Our neural network, henceforth deep"
  },
  {
    "id": "rss:https://arxiv.org/abs/2502.17731",
    "domain": "金融",
    "title": "Confidence intervals for empirical convergence rates of randomised quasi-Monte Carlo, with applications to option pricing",
    "url": "https://arxiv.org/abs/2502.17731",
    "source": "Giacomo Case",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T04:00:00+00:00",
    "summary": "arXiv:2502.17731v2 Announce Type: replace Abstract: Empirical comparisons of quasi-Monte Carlo rules often report fitted convergence exponents without intervals. We estimate the root mean square error"
  },
  {
    "id": "rss:https://arxiv.org/abs/2503.01716",
    "domain": "金融",
    "title": "The Volterra Stein-Stein model with stochastic interest rates",
    "url": "https://arxiv.org/abs/2503.01716",
    "source": "Eduardo Abi Jaber, Donatien Hainaut, Edouard Motte",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T04:00:00+00:00",
    "summary": "arXiv:2503.01716v3 Announce Type: replace Abstract: We introduce the Volterra Stein-Stein model with stochastic interest rates, where both volatility and interest rates are driven by correlated Gaussi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2602.11992",
    "domain": "金融",
    "title": "Labor Supply among Homeless Street-Paper Sellers: Evidence from a Randomized Wage Increase",
    "url": "https://arxiv.org/abs/2602.11992",
    "source": "Mats Ekman, Niklas Jakobsson, Andreas Kotsadam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T04:00:00+00:00",
    "summary": "arXiv:2602.11992v3 Announce Type: replace Abstract: We conduct a pre-registered randomized controlled trial to test for income targeting in labor-supply decisions among sellers of a Swedish street pap"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.04004",
    "domain": "金融",
    "title": "Structural Limits of OHLCV-Based Intraday Momentum Signals in MNQ Futures: A Systematic Falsification Study",
    "url": "https://arxiv.org/abs/2605.04004",
    "source": "Mathias Mesfin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T04:00:00+00:00",
    "summary": "arXiv:2605.04004v3 Announce Type: replace Abstract: This paper tests whether common intraday momentum signals built from OHLCV data generate a tradable edge in Micro E-Mini Nasdaq 100 (MNQ) futures af"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.27845",
    "domain": "金融",
    "title": "LLM Agents as Static Level-k Players in Behavioural Games",
    "url": "https://arxiv.org/abs/2606.27845",
    "source": "Po Han Teo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T04:00:00+00:00",
    "summary": "arXiv:2606.27845v2 Announce Type: replace Abstract: Large Language Models (LLMs) are increasingly used as stand-ins in behavioural games. These stand-ins rely on the assumption that the LLM's distribu"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.15452",
    "domain": "金融",
    "title": "Computing Endogenous Transformations in Processing Networks: A Dynamic Calibration Approach",
    "url": "https://arxiv.org/abs/2609.15452",
    "source": "Satoshi Nakano, Kazuhiko Nishimura",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T04:00:00+00:00",
    "summary": "arXiv:2609.15452v2 Announce Type: replace Abstract: Understanding how supply chains endogenously transform requires a parametric model of processing networks with non-neutral substitution elasticities"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.12114",
    "domain": "金融",
    "title": "A Decomposition Method for LQ Conditional McKean-Vlasov Control Problems with Random Coefficients",
    "url": "https://arxiv.org/abs/2604.12114",
    "source": "On\\'esime Hounkpe, Dena Firoozi, Shuang Gao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T04:00:00+00:00",
    "summary": "arXiv:2604.12114v2 Announce Type: replace-cross Abstract: We propose a decomposition method for solving a general class of linear-quadratic (LQ) McKean-Vlasov control problems involving conditional ex"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.12802",
    "domain": "金融",
    "title": "Strategically Analogous Mechanisms",
    "url": "https://arxiv.org/abs/2605.12802",
    "source": "Joseph Feffer, Filip Tokarski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T04:00:00+00:00",
    "summary": "arXiv:2605.12802v2 Announce Type: replace-cross Abstract: This paper studies when strategic understanding acquired in one mechanism can be transferred to another. It introduces a framework in which ag"
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
    "id": "hn:49633640",
    "domain": "金融",
    "title": "DHS Program Analyzes Americans' Finances to Flag Drivers for Traffic Stops",
    "url": "https://www.military.com/dhs-program-analyzes-americans-finances-to-flag-drivers-for-traffic-stops-report",
    "source": "randycupertino",
    "platform": "hackernews",
    "points": 35,
    "published_at": "2026-09-09T20:22:20+00:00",
    "summary": ""
  }
]
```
