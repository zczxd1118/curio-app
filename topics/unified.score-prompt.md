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

- 今日日期：`2026-10-22`
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
  "date": "2026-10-22",
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
    "id": "bvid:BV1VkgK6NEZS",
    "domain": "AI",
    "title": "DeepSeek Harness 首发实测 + 入门教程，夯爆了！梁神我错了",
    "url": "http://www.bilibili.com/video/av117093710237975",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 2476266,
    "published_at": "2026-08-14T11:56:52+00:00",
    "summary": "DeepSeek Harness 保姆级教程，1个视频带你从安装到实战玩转 DeepSeek 最新开源的 AI 编程工具，小白也能学会，看完就知道《国产版 Codex》到底有多强。\n编程学习教程+实战项目+简历模板：codefather.cn\n免费 AI 编程教程：github.com/liyupi/ai-guide\n视频从安装开始，手把手教你配置 DeepSeek Harness，然后用 Dee"
  },
  {
    "id": "bvid:BV1E7wtzaEdq",
    "domain": "AI",
    "title": "从 LLM 到 Agent Skill，一期视频带你打通底层逻辑！",
    "url": "http://www.bilibili.com/video/av116227955497963",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 2134830,
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
    "points": 2011807,
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
    "points": 1424634,
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
    "points": 1376205,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 868394,
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
    "points": 725808,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1eK5DzHEWu",
    "domain": "AI",
    "title": "MCP实战指南，mcp视频教程，2小时学透mcp",
    "url": "http://www.bilibili.com/video/av114380213586544",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 423980,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1ia9UBPESQ",
    "domain": "AI",
    "title": "在VScode中配置Claude Code并接入DeepSeek V4 Pro【oo唠嗑教程】",
    "url": "http://www.bilibili.com/video/av116487012549813",
    "source": "沉默的羔丸ovo",
    "platform": "bilibili",
    "points": 359804,
    "published_at": "2026-04-29T08:23:29+00:00",
    "summary": "配置方法如下：\n(想用真心换取你的关注...蟹蟹泥...)\nsetting.json添加：\n{ &quot;name&quot;: &quot;ANTHROPIC_BASE_URL&quot;, &quot;value&quot;: &quot;https://xxxx&quot; }, \n{ &quot;name&quot;: &quot;ANTHROPIC_AUTH_TOKEN&quot;, "
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 329553,
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
    "points": 311818,
    "published_at": "2025-04-15T00:59:13+00:00",
    "summary": "MCP终极指南 - 带你深入掌握MCP（基础篇）\n\n时间轴：\n01:05 MCP简要介绍\n02:47 安装 MCP Host（Cline）\n03:15 配置 Cline 用的 API Key\n06:01 第一个 MCP 问题\n06:31 概念解释：MCP Server 和 Tool\n09:13 配置 MCP Server\n14:19 使用 MCP Server\n15:24 MCP 交互流程详解\n1"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 213019,
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
    "points": 184412,
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
    "points": 160414,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1jCaq6nESn",
    "domain": "AI",
    "title": "【Opus 5.5半价】零基础小白友好，15分钟彻底学习Claude桌面版",
    "url": "http://www.bilibili.com/video/av117346425374831",
    "source": "LeaderAI",
    "platform": "bilibili",
    "points": 111319,
    "published_at": "2026-09-28T03:03:19+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1K6YM69ESq",
    "domain": "AI",
    "title": "AI+网络安全实战：从Agent入门到AI智能体挖漏洞教程！网络安全|信息安全|黑客技术|渗透测试|SRC漏洞挖掘|AI审计|HVV护网行动|靶场练习-码士集团",
    "url": "http://www.bilibili.com/video/av117247037213495",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 91435,
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
    "points": 76812,
    "published_at": "2025-07-12T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1LXhc6yEkc",
    "domain": "AI",
    "title": "昔涟/Cyrene-Agent 安装配置/演示教程",
    "url": "http://www.bilibili.com/video/av117164694570292",
    "source": "Playa0",
    "platform": "bilibili",
    "points": 60675,
    "published_at": "2026-08-27T00:43:58+00:00",
    "summary": "v1.1.6安装包：\n夸克网盘：\n链接：https://pan.quark.cn/s/43ff3db459f4?pwd=SD2k\n提取码：SD2k\ngithub仓库：\nPlaya-0v0/Cyrene-Agent: An open-source AI desktop companion inspired by Cyrene, combining immersive Chat, personaliz"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 56264,
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
    "points": 49515,
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
    "points": 40807,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV126pk6sETS",
    "domain": "AI",
    "title": "连 json都不会，进了福布斯团队。面试的时候才知道vibe coding是什么，两天后他给我发了offer。",
    "url": "http://www.bilibili.com/video/av117436686795057",
    "source": "揽星Celeste",
    "platform": "bilibili",
    "points": 31955,
    "published_at": "2026-10-14T01:35:05+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29855,
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
    "points": 29012,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1sQaL6vEkb",
    "domain": "AI",
    "title": "小白向，ai入门第一课：agent的部署和使用！",
    "url": "http://www.bilibili.com/video/av117349378166797",
    "source": "沈三殊",
    "platform": "bilibili",
    "points": 24617,
    "published_at": "2026-09-28T15:30:36+00:00",
    "summary": "详细的agent部署介绍：https://pan.quark.cn/s/3846914c6da7\n欢迎来到ai的世界！！\n有疑问欢迎私信。"
  },
  {
    "id": "bvid:BV18KJX6mEiH",
    "domain": "AI",
    "title": "太炸裂了！Claude Code 3.0彻底杀疯了！",
    "url": "http://www.bilibili.com/video/av117450007911196",
    "source": "烟神殿殿主",
    "platform": "bilibili",
    "points": 24433,
    "published_at": "2026-10-16T10:04:56+00:00",
    "summary": "原视频链接：https://www.youtube.com/watch?v=8nh1dcH4uJU\n本视频为AI技术搬运翻译，使用AI智能移除原视频广告营销内容，旨在降低信息差，帮助大家了解海外最新AI动态。\n翻译：烟神殿API,模型gemini-3.8-flash\n配音：使用的时FishTTS官方接口配音"
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 23142,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV17Lap6VEUr",
    "domain": "AI",
    "title": "【全80集】Vibe Coding 零基础入门到实战教程，由浅入深（全程干货）",
    "url": "http://www.bilibili.com/video/av117353572468721",
    "source": "数据拾光屋",
    "platform": "bilibili",
    "points": 20888,
    "published_at": "2026-10-02T09:25:00+00:00",
    "summary": "本套教程专门为零基础学员而制，全程干货无废话，喜欢的小伙伴记得点赞三连喔 ~"
  },
  {
    "id": "bvid:BV15epZ61E7F",
    "domain": "AI",
    "title": "我为什么强烈推荐Cursor的Pro套餐，Grok Bot真的太好用了！",
    "url": "http://www.bilibili.com/video/av117428784862489",
    "source": "AI摸鱼的梁师傅",
    "platform": "bilibili",
    "points": 15413,
    "published_at": "2026-10-12T16:06:10+00:00",
    "summary": "这期讲清楚三件事：为什么选 Cursor（官网软件直连、支付宝付款）；Pro 的两个模型池子怎么分（Grok/Composer 一池，Claude/GPT 共享一池）；附赠的 Grok Bot 怎么用——它有自己的云端电脑，合上 Mac 也在替你干活：定时简报、盯 PR、管邮件日历，还能多 Bot 协作。\n00:00 封号焦虑，和订套餐的理由 00:35 为什么是 Cursor：直连 + 支付宝 "
  },
  {
    "id": "bvid:BV1gJJB6kERk",
    "domain": "AI",
    "title": "【实操】claude稳定不封的方法 | 第一课",
    "url": "http://www.bilibili.com/video/av117457104672336",
    "source": "程序员大龙虾",
    "platform": "bilibili",
    "points": 13128,
    "published_at": "2026-10-17T16:10:46+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 12930,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
  },
  {
    "id": "bvid:BV1bBHm6MEG5",
    "domain": "AI",
    "title": "这绝对是b站讲的最好的Claude Code全套实战教程，手把手带你搞定国内环境安装配置，全程干货无废话！AI大模型/MCP/Skill/智能体/Agent",
    "url": "http://www.bilibili.com/video/av117402847155229",
    "source": "大模型饼饼",
    "platform": "bilibili",
    "points": 12056,
    "published_at": "2026-10-08T02:13:21+00:00",
    "summary": "这绝对是B站讲得最好的Claude Code全套实战教程！手把手带你搞定国内环境安装配置、基础操作、高阶实战技巧，课程不堆砌冗余理论，聚焦真实开发场景，带你吃透Claude Code核心能力，打通MCP、Skill与Agent智能体联动开发。不管你是想提升日常编码效率，还是入门AI智能体开发，这套教程都非常适合你，全程干货无废话！"
  },
  {
    "id": "bvid:BV1zV54zbEbU",
    "domain": "AI",
    "title": "2分钟在vscode里使用MCP服务",
    "url": "http://www.bilibili.com/video/av114365231531540",
    "source": "程序员三千",
    "platform": "bilibili",
    "points": 11378,
    "published_at": "2025-04-19T15:10:12+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1Yhb66LEaF",
    "domain": "AI",
    "title": "3分钟，教你什么是vibe coding",
    "url": "http://www.bilibili.com/video/av117115000524101",
    "source": "开聊pro",
    "platform": "bilibili",
    "points": 10167,
    "published_at": "2026-08-18T06:12:25+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1xFJ26tEoG",
    "domain": "AI",
    "title": "AI产品经理作品集：Vibe Coding实操 ChatBI落地写进简历",
    "url": "http://www.bilibili.com/video/av117445360618053",
    "source": "AI产品经理PMGao",
    "platform": "bilibili",
    "points": 9123,
    "published_at": "2026-10-15T14:22:53+00:00",
    "summary": "有很多同学用过codex、claude code等就觉得有vibecoding经验了，很多同学其实站在一个使用AI的普通用户跟AI交流而已，还远远达不到作为AI产品经理的能力。所以这个实操案例系统化的讲解了企业级项目是如何通过vibecoding落地的详细步骤，这里面包括了产品规划+竞品分析+SDD开发规范+Harness+测试用例+测评+skill设计等等。\n\n这个实操结合企业级案例深度讲解，完"
  },
  {
    "id": "bvid:BV1aSR4BKESW",
    "domain": "AI",
    "title": "安卓手机部署Claude Code",
    "url": "http://www.bilibili.com/video/av116526891993752",
    "source": "中国小骑士",
    "platform": "bilibili",
    "points": 8322,
    "published_at": "2026-05-06T09:24:14+00:00",
    "summary": "通过Termux安装Claude Code并且接入国内大模型"
  },
  {
    "id": "bvid:BV11aYs6PE2p",
    "domain": "AI",
    "title": "AI Agent接入Photoshop：MCP 实现自然语言修图",
    "url": "http://www.bilibili.com/video/av117239051323475",
    "source": "W不懂跨境",
    "platform": "bilibili",
    "points": 7886,
    "published_at": "2026-09-09T03:54:24+00:00",
    "summary": "本期教程介绍 Photoshop MCP 的安装与配置，并演示如何将 AI Agent 接入 Photoshop，通过 MCP 调用 Photoshop 工具，实现自然语言控制与自动修图。\n\n最大的特点，也是大家都关心的问题：\n1、整个过程不需要Adobe Developer 账号。\n2、不需要购买额外的 AI 服务。\n3、不要求 Photoshop 必须为正版\n4、支持所有的 Photoshop"
  },
  {
    "id": "bvid:BV1rLpv6bED1",
    "domain": "AI",
    "title": "黑马Vibe Coding智能应用开发教程：免手写代码，轻松学智能应用开发！",
    "url": "http://www.bilibili.com/video/av117415581122989",
    "source": "黑马程序员广州中心",
    "platform": "bilibili",
    "points": 7351,
    "published_at": "2026-10-10T08:17:43+00:00",
    "summary": "本套《vibecoding智能应用开发》由广州黑马AI应用与智能体开发学科“宇哥”老师录制的课堂版本。\n技术栈：ClaudeCode使用与高级命令+Skill+提示词工程+Coze平台+工作流+对话流+知识库RAG+多模态文生图+ASR语音转文字+文生视频+OCR文字识别+意向识别+插件工具（墨迹天气+高德线路规划+头条新闻搜索+AI命里+旅行师+连接读取+文件读取+联网搜索）\n学习收获企业案例："
  },
  {
    "id": "bvid:BV1UaYK6nEjP",
    "domain": "AI",
    "title": "【cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av117244419903051",
    "source": "茶子兀",
    "platform": "bilibili",
    "points": 7034,
    "published_at": "2026-09-10T02:39:36+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1wFpP6uE1s",
    "domain": "AI",
    "title": "【开源】让手机自己操作 App！手上的 ai Agent！GitHub开源安卓App推荐",
    "url": "http://www.bilibili.com/video/av117394643097499",
    "source": "补药满减哇",
    "platform": "bilibili",
    "points": 7021,
    "published_at": "2026-10-07T01:05:00+00:00",
    "summary": "开源安卓 AI Agent：RikkaHub Agent Pure\n它能「看懂」屏幕、自己操作各种 App，也能组队干活。\n\n⬇️ 下载 &amp; 源码（AGPL-3.0）\nhttps://github.com/wuyhong715/rikkahub-agent-pure\n\n▶ 本片讲两件事\n① 无障碍屏幕自动化：读控件树定位、实时决策，不是死坐标脚本\n② 专家团系统：每个专家有自己的模型/工具"
  },
  {
    "id": "bvid:BV1t9pt6JETF",
    "domain": "AI",
    "title": "Cursor vs Claude Code vs Codex哪个好？三大AI编程工具区别与选择指南",
    "url": "http://www.bilibili.com/video/av117411437090209",
    "source": "不管这么多",
    "platform": "bilibili",
    "points": 6148,
    "published_at": "2026-10-09T14:35:26+00:00",
    "summary": "三大编程工具要如何选？"
  },
  {
    "id": "bvid:BV18cnF6NEjC",
    "domain": "AI",
    "title": "实测！Grok Cursor等多模型整合后，性价比如何？",
    "url": "http://www.bilibili.com/video/av117471180821997",
    "source": "野生吃货",
    "platform": "bilibili",
    "points": 5974,
    "published_at": "2026-10-20T03:50:25+00:00",
    "summary": "简介无推广内容\n视频中演示网站有正规ICP备案"
  },
  {
    "id": "bvid:BV1fN7D6XEBE",
    "domain": "AI",
    "title": "【战锤3Mod教程】03-进阶向：使用AI Agent来制作MOD",
    "url": "http://www.bilibili.com/video/av116700955609851",
    "source": "Wyccc威力加强版",
    "platform": "bilibili",
    "points": 5876,
    "published_at": "2026-06-06T03:12:27+00:00",
    "summary": "没有剪辑和草稿一次录制完成，想到哪说到哪。"
  },
  {
    "id": "bvid:BV1uxp46SEmt",
    "domain": "AI",
    "title": "Claude稳定使用必备！美国静态住宅IP实操搭建教程！每月仅需3.7刀！",
    "url": "http://www.bilibili.com/video/av117409910364864",
    "source": "1024官号",
    "platform": "bilibili",
    "points": 5814,
    "published_at": "2026-10-09T08:14:35+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1SQnB6CEpx",
    "domain": "AI",
    "title": "Claude 工程负责人：“别再用 2024 年的方式使用 Claude 了”",
    "url": "http://www.bilibili.com/video/av117478881497342",
    "source": "-spacecaps-",
    "platform": "bilibili",
    "points": 5666,
    "published_at": "2026-10-21T12:34:20+00:00",
    "summary": "Felix Rieseberg 曾在 Anthropic 负责 Claude.ai、Cowork 和 Claude Code 桌面端的工程工作。他认为，我们许多人交给 AI 的任务，早已远低于它如今的能力。如果你只是让 Claude 总结邮件，究竟错过了什么？\n本期访谈探讨：如何把更大的目标交给 AI；为什么一句“你是一位专家”还不够；以及当 AI 的回答听起来令人信服时，如何发现其中的错误。Fe"
  },
  {
    "id": "bvid:BV1mRn66JERc",
    "domain": "AI",
    "title": "AI 写得比你读得快，code review 要怎么做？",
    "url": "http://www.bilibili.com/video/av117479686802808",
    "source": "grapeot",
    "platform": "bilibili",
    "points": 4975,
    "published_at": "2026-10-21T15:52:15+00:00",
    "summary": "AI 写代码的速度太快，很多团队在 code review 上陷入了两难。一行一行读会被 PR 淹没，何况 AI 写的代码表面工整，问题反而更隐蔽，读了也看不出来。有人说那就不读，出事回滚，技术上可以，但出了事背锅的还是人。\n\n平时说的读代码，其实同时混着三件事：挑错、对齐上下文、担责。以前代码产量小，捆在一起没问题，现在 AI 写得太快，捆不住了。这期视频从一次线上事故聊起，起因是一个改后台会话"
  },
  {
    "id": "bvid:BV1yEWw63EM2",
    "domain": "AI",
    "title": "2026 最新版】大佬亲授 Claude Code 全栈教程，从入门到精通全覆盖，小白 10 分钟上手，干货无废话，建议收藏！",
    "url": "http://www.bilibili.com/video/av117432844813498",
    "source": "绕着宇宙飞一圈",
    "platform": "bilibili",
    "points": 3965,
    "published_at": "2026-10-13T09:20:48+00:00",
    "summary": "求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！"
  },
  {
    "id": "bvid:BV1c2Ei6pEfW",
    "domain": "AI",
    "title": "首发 AI agent 接入音乐软件FLStudio完整教程--小白十分钟上手编曲",
    "url": "http://www.bilibili.com/video/av116731758516894",
    "source": "Melydic",
    "platform": "bilibili",
    "points": 3890,
    "published_at": "2026-06-12T09:30:00+00:00",
    "summary": "up制作的视频中的指令网站地址：FLStudio.hajimi8.ggff.net\n如有问题以及不会的，请在评论区问"
  },
  {
    "id": "bvid:BV1NJn665Epm",
    "domain": "AI",
    "title": "PHP2Shell 9.2 漏洞：我先把 5 台服务器的 PHP 升到了官方修复版。CVE-2026-109618、CVE-2026-109619",
    "url": "http://www.bilibili.com/video/av117479804243397",
    "source": "变量探索SEQVEC",
    "platform": "bilibili",
    "points": 2518,
    "published_at": "2026-10-21T16:23:15+00:00",
    "summary": "2026 年 10 月 21 日，PHP 官方发布紧急安全更新，修复两个无需登录就可能远程执行代码的漏洞：CVE-2026-109618、CVE-2026-109619。官方给出的修复版本分别是 PHP 8.2.35、8.3.36、8.4.27、8.5.12。\n\nPHP 官方目前只维护 8.2 到 8.5，8.1 及以下已经结束生命周期。其中 8.2 的安全支持将在 2026 年 12 月 31 "
  },
  {
    "id": "bvid:BV1Tnnk6HEFM",
    "domain": "AI",
    "title": "PHP2Shell：一次“跳车”如何让未认证请求拿下服务器 | 动画讲漏洞 · CVE-2026-109618",
    "url": "http://www.bilibili.com/video/av117480626325879",
    "source": "时雨遥遥",
    "platform": "bilibili",
    "points": 2155,
    "published_at": "2026-10-21T19:50:51+00:00",
    "summary": "“动画讲漏洞 · 知名 CVE 的触发链”第 001 期：PHP2Shell（CVE-2026-109618，PHP 核心，未认证 RCE，CVSS 9.2，2026-10-21 紧急修复）。一个漏洞一集，讲清楚：是什么、谁发现/报告的、触发链一步步怎么走、最后怎么修的。\n\n这期把 109618 的触发链拆开讲：PHP 处理每个请求时会临时搭一块“工作台”内存，并用 memory_limit 限制"
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
    "id": "hn:50008187",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI annualised revenues $20B less than previously signalled",
    "url": "https://www.cnbc.com/2026/10/08/open-ai-revenue-nvidia-oracle-coreweave.html",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 434,
    "published_at": "2026-10-08T16:45:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:49844663",
    "domain": "AI 算力 / 半导体",
    "title": "ASML says it sold 'absolutely nothing' in Europe in 2026",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/asml-says-its-sells-absolutely-nothing-in-europe-calls-on-eu-to-help-create-demand",
    "source": "MC995",
    "platform": "hackernews",
    "points": 403,
    "published_at": "2026-09-25T13:49:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:50035886",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia in talks to acquire US 'open' model startup Reflection AI",
    "url": "https://www.ft.com/content/052610c5-22b4-4dd4-932e-b7f9f0628b6a",
    "source": "arkj",
    "platform": "hackernews",
    "points": 180,
    "published_at": "2026-10-10T18:48:35+00:00",
    "summary": ""
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
    "id": "rss:https://www.eetimes.com/when-gps-isnt-enough-building-a-second-layer-of-positioning/",
    "domain": "AI 算力 / 半导体",
    "title": "When GPS Isn’t Enough: Building a Second Layer of Positioning",
    "url": "https://www.eetimes.com/when-gps-isnt-enough-building-a-second-layer-of-positioning/",
    "source": "Steve Caliguri",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T19:00:00+00:00",
    "summary": "GPS jamming is rising. Learn how 4G, 5G, and NTN positioning give mission-critical devices a trusted fallback when GNSS fails. The post When GPS Isn&#8217;t Enough: Building a Second Layer of Position"
  },
  {
    "id": "rss:https://www.eetimes.com/indias-osat-buildout-puts-semiconductor-testing-in-focus/",
    "domain": "AI 算力 / 半导体",
    "title": "India’s OSAT Buildout Puts Semiconductor Testing in Focus",
    "url": "https://www.eetimes.com/indias-osat-buildout-puts-semiconductor-testing-in-focus/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T13:39:13+00:00",
    "summary": "NI said Kaynes Semicon has selected its semiconductor test systems, while other Indian OSATs continue to evaluate equipment as manufacturers prepare for production. The post India’s OSAT Buildout Puts"
  },
  {
    "id": "rss:https://www.eetimes.com/why-chip-design-ai-benchmarks-must-go-beyond-functional-correctness/",
    "domain": "AI 算力 / 半导体",
    "title": "Why Chip Design AI Benchmarks Must Go Beyond Functional Correctness",
    "url": "https://www.eetimes.com/why-chip-design-ai-benchmarks-must-go-beyond-functional-correctness/",
    "source": "Surya Gunukula, Jerry Yicheng Wang, Kevin Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T13:00:00+00:00",
    "summary": "Demand for custom silicon is rising as physical AI, data centers, automotive systems, and edge devices require architectures optimized for specific workloads, memory bandwidth, latency, and energy eff"
  },
  {
    "id": "rss:https://www.eetimes.com/edge-ai-mcu-features-multimodal-compute-tiered-memory/",
    "domain": "AI 算力 / 半导体",
    "title": "Edge AI MCU Features Multimodal Compute, Tiered Memory",
    "url": "https://www.eetimes.com/edge-ai-mcu-features-multimodal-compute-tiered-memory/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T07:30:00+00:00",
    "summary": "A new MCU combines AI-native acceleration with integrated high-bandwidth DRAM scalable to hundreds of megabytes. The post Edge AI MCU Features Multimodal Compute, Tiered Memory appeared first on EE Ti"
  },
  {
    "id": "rss:https://www.eetimes.com/innovasea-packs-long-life-electronics-into-fish-tags/",
    "domain": "AI 算力 / 半导体",
    "title": "Innovasea Packs Long-Life Electronics into Fish Tags",
    "url": "https://www.eetimes.com/innovasea-packs-long-life-electronics-into-fish-tags/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T22:06:10+00:00",
    "summary": "A company on Canada’s east coast is pushing acoustic telemetry toward lighter payloads and decade-scale deployments by treating energy, sensing, and animal welfare as a single systems problem. The pos"
  },
  {
    "id": "rss:https://www.eetimes.com/chris-lattner-ai-code-generation-doesnt-solve-software-engineering/",
    "domain": "AI 算力 / 半导体",
    "title": "Chris Lattner: AI Code Generation Doesn’t Solve Software Engineering",
    "url": "https://www.eetimes.com/chris-lattner-ai-code-generation-doesnt-solve-software-engineering/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T11:00:00+00:00",
    "summary": "AI can generate low-level code, but code generation is also making it harder to build and maintain the software ecosystems we need. The post Chris Lattner: AI Code Generation Doesn&#8217;t Solve Softw"
  },
  {
    "id": "rss:https://www.eetimes.com/how-singapore-connects-chip-research-startups-and-manufacturing/",
    "domain": "AI 算力 / 半导体",
    "title": "How Singapore Connects Chip Research, Startups, and Manufacturing",
    "url": "https://www.eetimes.com/how-singapore-connects-chip-research-startups-and-manufacturing/",
    "source": "Susan Hong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T10:55:00+00:00",
    "summary": "From SiC power devices to silicon photonics, Singapore is building the infrastructure and industrial partnerships needed to bring deep-tech research to market. The post How Singapore Connects Chip Res"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/intel-installs-production-tools-at-fab-62-in-arizona-provides-updates-on-ohio-chip-fab-confirms-high-na-euv-for-high-volume-manufacturing-in-2028",
    "domain": "AI 算力 / 半导体",
    "title": "Intel installs production tools at Fab 62 in Arizona, provides updates on Ohio chip fab",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/intel-installs-production-tools-at-fab-62-in-arizona-provides-updates-on-ohio-chip-fab-confirms-high-na-euv-for-high-volume-manufacturing-in-2028",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T19:35:53+00:00",
    "summary": "Intel makes progress on its manufacturing expansion in Arizona and Ohio as it continues to expand advanced semiconductor manufacturing capacity in the U.S."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/4tb-samsung-990-pro-m-2-ssd-falls-27-percent-hits-20-cents-per-gigabyte-our-favorite-high-capacity-pcie-gen-4-drive-is-the-ultimate-storage-for-your-game-library",
    "domain": "AI 算力 / 半导体",
    "title": "4TB Samsung 990 Pro M.2 SSD falls 27%, hits 20 cents per gigabyte",
    "url": "https://www.tomshardware.com/pc-components/ssds/4tb-samsung-990-pro-m-2-ssd-falls-27-percent-hits-20-cents-per-gigabyte-our-favorite-high-capacity-pcie-gen-4-drive-is-the-ultimate-storage-for-your-game-library",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T16:07:49+00:00",
    "summary": "The 4TB Samsung 990 Pro has its astronomical AI-driven high price slashed by 27%."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/elon-musk-says-asml-and-other-critical-semiconductor-equipment-suppliers-will-expedite-shipments-to-terafab-facility-targets-volume-chip-production-by-q3-q4-2028-in-highly-aspirational-timeline",
    "domain": "AI 算力 / 半导体",
    "title": "ASML and other critical semiconductor equipment suppliers expedite shipments to Musk's Terafab",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/elon-musk-says-asml-and-other-critical-semiconductor-equipment-suppliers-will-expedite-shipments-to-terafab-facility-targets-volume-chip-production-by-q3-q4-2028-in-highly-aspirational-timeline",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T15:30:00+00:00",
    "summary": "Elon Musk says ASML and other semiconductor equipment suppliers are expediting deliveries for Terafab, as Tesla and SpaceX target volume chip production in Texas by late 2028 alongside a massive expan"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/linux/amd-brings-official-ryzen-overclocking-to-linux-with-aod-driver-support-no-official-app-but-third-party-options-should-arrive-soon",
    "domain": "AI 算力 / 半导体",
    "title": "AMD brings official Ryzen overclocking to Linux with AOD driver support",
    "url": "https://www.tomshardware.com/software/linux/amd-brings-official-ryzen-overclocking-to-linux-with-aod-driver-support-no-official-app-but-third-party-options-should-arrive-soon",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T14:52:23+00:00",
    "summary": "New driver enablement work from AMD brings full platform-level tuning control to Ryzen systems running Linux, finally."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/trump-announces-mandate-for-data-centers-to-pay-dividends-to-the-local-community-hopes-to-win-more-data-center-supporters-through-dividend-scheme",
    "domain": "AI 算力 / 半导体",
    "title": "Trump announces mandate forcing AI data centers to pay energy dividends to the local community",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/trump-announces-mandate-for-data-centers-to-pay-dividends-to-the-local-community-hopes-to-win-more-data-center-supporters-through-dividend-scheme",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T13:46:18+00:00",
    "summary": "Trump's latest post on Truth Social announces his plans to make data centers more popular among local communities."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/qualcomm-to-cut-jobs-globally-in-performance-based-layoffs-ceo-says-move-will-build-stronger-performance-culture-as-company-pivots-to-ai-data-center-and-edge-products",
    "domain": "AI 算力 / 半导体",
    "title": "Qualcomm to cut jobs globally in \"performance-based\" layoffs, as company pivots to AI data center and edge computing markets",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/qualcomm-to-cut-jobs-globally-in-performance-based-layoffs-ceo-says-move-will-build-stronger-performance-culture-as-company-pivots-to-ai-data-center-and-edge-products",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T13:00:00+00:00",
    "summary": "Qualcomm will begin performance-based layoffs worldwide in November as the chipmaker reallocates resources toward AI infrastructure, data centers, automotive, PCs, and edge computing, amid weaker cons"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/fadu-puts-the-filesystem-inside-the-ssds-flash-to-bypass-host-cpus-file-semantic-pcie-6-0-ssd-delivers-460-000-ops-s-to-gpus-and-dpus-samples-due-by-q3-2027",
    "domain": "AI 算力 / 半导体",
    "title": "FADU puts the filesystem inside the SSD's flash to bypass host CPUs",
    "url": "https://www.tomshardware.com/pc-components/ssds/fadu-puts-the-filesystem-inside-the-ssds-flash-to-bypass-host-cpus-file-semantic-pcie-6-0-ssd-delivers-460-000-ops-s-to-gpus-and-dpus-samples-due-by-q3-2027",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T12:30:00+00:00",
    "summary": "FADU’s FS-SSD carries NFSv3 file operations inside NVMe commands, letting GPUs, DPUs, and NICs read files without a host file system."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-and-intel-will-work-together-to-create-a-single-pytorch-code-path-for-ai-inference-on-cpus-amd-zendnn-library-gets-folded-into-intel-onednn-to-make-cpu-ai-simpler",
    "domain": "AI 算力 / 半导体",
    "title": "AMD and Intel will work together to create a single PyTorch code path for AI inference on CPUs",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-and-intel-will-work-together-to-create-a-single-pytorch-code-path-for-ai-inference-on-cpus-amd-zendnn-library-gets-folded-into-intel-onednn-to-make-cpu-ai-simpler",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T12:00:00+00:00",
    "summary": "AMD and Intel are working together to bring CPU inference optimizations for PyTorch under the unified oneDNN library."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/iran-threatens-to-attack-undersea-cables-in-the-strait-of-hormuz-calls-them-legitimate-new-targets-in-future-conflict-irgc-spokesman-warns-that-a-future-third-phase-in-war-with-us-could-lead-them-to-sever-global-data-links",
    "domain": "AI 算力 / 半导体",
    "title": "Iran threatens to attack undersea cables in the Strait of Hormuz, calls them 'legitimate new targets' in future conflict",
    "url": "https://www.tomshardware.com/tech-industry/iran-threatens-to-attack-undersea-cables-in-the-strait-of-hormuz-calls-them-legitimate-new-targets-in-future-conflict-irgc-spokesman-warns-that-a-future-third-phase-in-war-with-us-could-lead-them-to-sever-global-data-links",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T11:52:08+00:00",
    "summary": "Iran could attack seven undersea cables that run through the Strait of Hormuz, describing them as \"legitimate new targets\" in a potential \"third phase\" of further conflict with the United States."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/samsung-and-sk-hynix-are-upgrading-chinese-factories-to-produce-advanced-ram-chips-as-ai-data-center-competition-ramps-up-big-players-move-to-fight-off-the-threat-from-cxmt-and-co",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung and SK Hynix are upgrading Chinese factories to produce advanced RAM chips as AI data center competition ramps up",
    "url": "https://www.tomshardware.com/pc-components/dram/samsung-and-sk-hynix-are-upgrading-chinese-factories-to-produce-advanced-ram-chips-as-ai-data-center-competition-ramps-up-big-players-move-to-fight-off-the-threat-from-cxmt-and-co",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T11:49:44+00:00",
    "summary": "Samsung and SK Hynix are reportedly upgrading their factories to produce more advanced RAM chips designed for AI data centers in an attempt to fend off competition from Chinese companies."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/headphones-headsets/why-you-dont-need-an-audiophile-headset-for-gaming-comfort-convenience-and-a-good-mic-win-over-pure-audio-fidelity",
    "domain": "AI 算力 / 半导体",
    "title": "Why you don't need an audiophile headset for gaming — comfort, convenience, and a good mic win over pure audio fidelity",
    "url": "https://www.tomshardware.com/peripherals/headphones-headsets/why-you-dont-need-an-audiophile-headset-for-gaming-comfort-convenience-and-a-good-mic-win-over-pure-audio-fidelity",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T11:30:00+00:00",
    "summary": "Headsets are mainly about audio, but that doesn't mean that the \"objectively\" best-sounding headset by audiophile standards translates to the best-sounding headset by gaming standards."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/microns-taiwan-union-will-launch-a-one-day-strike-this-week-threatening-round-the-clock-fab-operations-workers-demand-concrete-terms-for-2026-bonus-and-clearer-profit-sharing-arrangements",
    "domain": "AI 算力 / 半导体",
    "title": "Micron's Taiwan union will launch a one-day strike this week, threatening memory production",
    "url": "https://www.tomshardware.com/pc-components/dram/microns-taiwan-union-will-launch-a-one-day-strike-this-week-threatening-round-the-clock-fab-operations-workers-demand-concrete-terms-for-2026-bonus-and-clearer-profit-sharing-arrangements",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T11:00:00+00:00",
    "summary": "Micron's Taiwan union is set to conduct a one-day strike at the company's Taoyuan DRAM facility as workers demand bonuses for this year and transparent terms of bonuses for upcoming years."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/save-a-massive-usd850-on-lenovos-legion-5i-gaming-laptop-with-this-32-percent-best-buy-discount-featuring-powerful-rtx-5070-graphics-and-a-3k-display-with-a-240hz-refresh-rate",
    "domain": "AI 算力 / 半导体",
    "title": "Save a massive $850 on Lenovo's Legion 5i gaming laptop with this 32% Best Buy discount",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/save-a-massive-usd850-on-lenovos-legion-5i-gaming-laptop-with-this-32-percent-best-buy-discount-featuring-powerful-rtx-5070-graphics-and-a-3k-display-with-a-240hz-refresh-rate",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T10:52:35+00:00",
    "summary": "Save $850 on a new Lenovo gaming laptop from Best Buy. Pick up the Legion 5i with RTX 5070 graphics and save 32%."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/score-a-1440p-ready-gaming-pc-with-an-rtx-5060-ti-16gb-for-under-usd1-500-right-now-saving-you-usd200-abs-cyclone-aqua-rig-ships-with-16gb-ddr5-1tb-ssd-and-a-20-core-intel-cpu",
    "domain": "AI 算力 / 半导体",
    "title": "Score a 1440p-ready gaming PC with an RTX 5060 Ti 16GB for under $1,500 right now, saving you $200",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/score-a-1440p-ready-gaming-pc-with-an-rtx-5060-ti-16gb-for-under-usd1-500-right-now-saving-you-usd200-abs-cyclone-aqua-rig-ships-with-16gb-ddr5-1tb-ssd-and-a-20-core-intel-cpu",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T10:50:14+00:00",
    "summary": "You can pick up this ABS Cyclone Aqua gaming PC with an RTX 5060 Ti 16GB, Intel Core i7-14700F, 16GB DDR5, and a 1TB SS with a $200 discount, now $1,499.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/supercomputers/hpe-says-it-will-run-the-first-supercomputer-benchmarks-on-the-moon-with-its-spaceborne-computer-4-system-will-ride-a-rover-to-the-lunar-south-pole-to-test-linpack-llms-and-lidar-mapping",
    "domain": "AI 算力 / 半导体",
    "title": "HPE says it will run the first supercomputer benchmarks on the Moon",
    "url": "https://www.tomshardware.com/tech-industry/supercomputers/hpe-says-it-will-run-the-first-supercomputer-benchmarks-on-the-moon-with-its-spaceborne-computer-4-system-will-ride-a-rover-to-the-lunar-south-pole-to-test-linpack-llms-and-lidar-mapping",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T10:30:00+00:00",
    "summary": "HPE’s Spaceborne Computer-4 will ride Astrolab’s FLIP rover to the Moon’s south pole to run HPL, HPCG, and AI tests."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/three-workers-killed-one-in-intensive-care-after-fall-at-tsmcs-2nm-fab-construction-site-in-kaohsiung-broken-bolt-on-a-steel-connection-plate-suspected-as-cause-behind-tragic-accident",
    "domain": "AI 算力 / 半导体",
    "title": "Four workers killed after fall at TSMC’s 2nm fab construction site",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/three-workers-killed-one-in-intensive-care-after-fall-at-tsmcs-2nm-fab-construction-site-in-kaohsiung-broken-bolt-on-a-steel-connection-plate-suspected-as-cause-behind-tragic-accident",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T10:00:00+00:00",
    "summary": "Four contract workers died after a fall at TSMC’s Fab 22 construction site in Kaohsiung, Taiwan."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/jensen-huang-nvidia-gtc-keynote-disrupted-by-greenpeace-protest-over-chips-in-russian-drones-what-are-you-doing-about-that-heckler-demands-before-being-thrown-out",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang Nvidia GTC keynote disrupted by Greenpeace protest over chips in Russian drones",
    "url": "https://www.tomshardware.com/tech-industry/jensen-huang-nvidia-gtc-keynote-disrupted-by-greenpeace-protest-over-chips-in-russian-drones-what-are-you-doing-about-that-heckler-demands-before-being-thrown-out",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T09:57:06+00:00",
    "summary": "Jensen Huang's Nvidia GTC keynote speech in Berlin was disrupted by a Greenpeace protest on Wednesday."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpu-drivers/amds-fsr-4-1-now-works-on-radeon-rx-6000-gpus-xbox-series-x-and-s-and-ryzen-ai-max-ai-9-and-z2-socs-new-release-brings-cutting-edge-tech-to-older-hardware-with-a-small-performance-cost",
    "domain": "AI 算力 / 半导体",
    "title": "AMD's FSR 4.1 now works on Radeon RX 6000 cards, Xbox Series X and S, and Ryzen AI Max, AI 9, and Z2 SoCs",
    "url": "https://www.tomshardware.com/pc-components/gpu-drivers/amds-fsr-4-1-now-works-on-radeon-rx-6000-gpus-xbox-series-x-and-s-and-ryzen-ai-max-ai-9-and-z2-socs-new-release-brings-cutting-edge-tech-to-older-hardware-with-a-small-performance-cost",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T17:47:35+00:00",
    "summary": "AMD has released a version of its cutting-edge FSR 4.1 upscaler that now works on Radeon RX 6000 GPUs, Xbox Series X and Series S consoles, and Ryzen AI Max, AI 9, and Z2 chips."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/routers/tp-link-proposes-usd1-billion-us-wi-fi-router-manufacturing-alliance-with-key-tronic-potential-deal-seeks-to-end-ongoing-saga-blocking-its-wi-fi-8-products-from-american-homes",
    "domain": "AI 算力 / 半导体",
    "title": "TP-Link proposes $1 billion US Wi-Fi router manufacturing alliance with Key Tronic",
    "url": "https://www.tomshardware.com/networking/routers/tp-link-proposes-usd1-billion-us-wi-fi-router-manufacturing-alliance-with-key-tronic-potential-deal-seeks-to-end-ongoing-saga-blocking-its-wi-fi-8-products-from-american-homes",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T16:25:55+00:00",
    "summary": "TP-Link is at the mercy of the FCC regarding its ready-to-go Wi-Fi 8 routers, so it has a sweetener in mind to move things along."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/mysterious-amd-zen-6-apu-with-24gb-of-lpddr5-memory-appears-in-benchmarks-chip-may-be-for-next-gen-steam-deck-or-gaming-handhelds",
    "domain": "AI 算力 / 半导体",
    "title": "Mysterious AMD Zen 6 APU with 24GB of LPDDR5 memory appears in benchmarks",
    "url": "https://www.tomshardware.com/pc-components/cpus/mysterious-amd-zen-6-apu-with-24gb-of-lpddr5-memory-appears-in-benchmarks-chip-may-be-for-next-gen-steam-deck-or-gaming-handhelds",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T13:59:43+00:00",
    "summary": "The engineering sample features six CPU cores, 24GB of LPDDR5 memory running at 9,600 MT/s, and an integrated GPU clocked at 2.4 GHz, although its connection to a future Steam Deck remains unconfirmed"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/us-army-reportedly-developing-program-that-would-deploy-ai-agents-to-autonomously-seek-and-destroy-targets-in-enemy-digital-infrastructures-experts-warn-echotribble-program-could-have-disastrous-consequences",
    "domain": "AI 算力 / 半导体",
    "title": "U.S. Army developing program that would deploy AI agents to autonomously seek and destroy targets in enemy digital infrastructures",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/us-army-reportedly-developing-program-that-would-deploy-ai-agents-to-autonomously-seek-and-destroy-targets-in-enemy-digital-infrastructures-experts-warn-echotribble-program-could-have-disastrous-consequences",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T13:30:00+00:00",
    "summary": "The U.S. Army is developing a program to deploy autonomous AI agents that can navigate digital and network infrastructures, identify targets, and “neutralize” them."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/us-takes-unprecedented-step-of-recommissioning-nuclear-plants-due-to-ai-power-demand-2-25-gw-currently-on-tap-from-refurbished-reactors",
    "domain": "AI 算力 / 半导体",
    "title": "US restarts three shut-down nuclear reactors to feed AI data centers",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/us-takes-unprecedented-step-of-recommissioning-nuclear-plants-due-to-ai-power-demand-2-25-gw-currently-on-tap-from-refurbished-reactors",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T12:50:00+00:00",
    "summary": "The U.S. government is helping fund projects to bring nuclear reactors back online in an attempt to provide more energy capacity to AI data centers."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/oblivion-gamer-uses-claude-ai-to-boost-average-fps-gains-up-to-48-percent-stutters-slashed-by-90-percent-performance-mod-doesnt-change-game-assets-or-alter-visuals",
    "domain": "AI 算力 / 半导体",
    "title": "Oblivion gamer uses Claude AI to boost average FPS gains up to 48%, stutters slashed by 90%",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/oblivion-gamer-uses-claude-ai-to-boost-average-fps-gains-up-to-48-percent-stutters-slashed-by-90-percent-performance-mod-doesnt-change-game-assets-or-alter-visuals",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T12:30:00+00:00",
    "summary": "The new Oblivion Remastered Performance Fix mod is a pure code fix, with no changes to game assets or the game's visuals, yet it offers massive gains."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/buy-a-complete-rtx-5070-ti-gaming-pc-from-newegg-and-save-usd450-get-a-16gb-gpu-32gb-of-ram-an-i9-14900kf-processor-a-2tb-ssd-and-more-for-only-usd2-549",
    "domain": "AI 算力 / 半导体",
    "title": "Buy a complete RTX 5070 Ti gaming PC from Newegg and save $450",
    "url": "https://www.tomshardware.com/pc-components/buy-a-complete-rtx-5070-ti-gaming-pc-from-newegg-and-save-usd450-get-a-16gb-gpu-32gb-of-ram-an-i9-14900kf-processor-a-2tb-ssd-and-more-for-only-usd2-549",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T12:15:38+00:00",
    "summary": "Save $450 on Newegg’s ABS Stratos II Aqua prebuilt – open the box and start gaming tomorrow saving the trouble of building and supporting your own"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/chinas-tech-giants-drop-usd35-billion-on-export-compliant-nvidia-rtx-pro-5500-workstation-gpu-orders-to-power-ai-ambitions-according-to-reports-bytedance-alibaba-and-tencent-order-3-million-cards-despite-warnings-that-only-10-percent-of-orders-are-fulfillable",
    "domain": "AI 算力 / 半导体",
    "title": "China’s tech giants drop $35 billion on export-compliant Nvidia RTX Pro 5500 workstation GPU orders to power AI ambitions, according to reports",
    "url": "https://www.tomshardware.com/pc-components/gpus/chinas-tech-giants-drop-usd35-billion-on-export-compliant-nvidia-rtx-pro-5500-workstation-gpu-orders-to-power-ai-ambitions-according-to-reports-bytedance-alibaba-and-tencent-order-3-million-cards-despite-warnings-that-only-10-percent-of-orders-are-fulfillable",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T12:10:00+00:00",
    "summary": "$35 billion worth of Nvidia RTX Pro 5500 GPUs have been bought by Chinese trio Tencent, Alibaba and ByteDance, with demand far exceeding Nvidia's planned production, according to report."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/modern-software-is-built-on-the-backs-of-low-paid-maintainers-opening-the-door-to-potential-threats-report-details-critically-underfunded-projects-that-remain-understaffed-or-unfunded",
    "domain": "AI 算力 / 半导体",
    "title": "Modern software is built on the backs of low-paid maintainers, opening the door to potential threats",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/modern-software-is-built-on-the-backs-of-low-paid-maintainers-opening-the-door-to-potential-threats-report-details-critically-underfunded-projects-that-remain-understaffed-or-unfunded",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T12:10:00+00:00",
    "summary": "Modern computing remains vulnerable to the low bus factor of many open-source projects — continued lack of funding and manpower for voluntary-maintained infrastructure makes for a perennial threat"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/mods-can-almost-double-dlss-5-performance-through-foveation-reducing-resolution-at-the-edges-of-frames-technique-makes-dlss-5-possible-on-high-resolution-ultrawide-monitors",
    "domain": "AI 算力 / 半导体",
    "title": "Mods can almost double DLSS 5 performance through Foveation, reducing resolution at the edges of frames",
    "url": "https://www.tomshardware.com/pc-components/gpus/mods-can-almost-double-dlss-5-performance-through-foveation-reducing-resolution-at-the-edges-of-frames-technique-makes-dlss-5-possible-on-high-resolution-ultrawide-monitors",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T11:54:18+00:00",
    "summary": "VR rendering technique of foveated imaging gets integrated into DLSS 5, making it much easier to run"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/nvidia-vera-cpu-deployed-at-ai-startup-modal-alongside-existing-x86-fleet-internal-testing-showed-2x-throughput-compared-to-amd-and-intel",
    "domain": "AI 算力 / 半导体",
    "title": "Modal taps Nvidia Vera CPUs after firm's internal tests show 2x throughput over Intel and AMD chips",
    "url": "https://www.tomshardware.com/pc-components/cpus/nvidia-vera-cpu-deployed-at-ai-startup-modal-alongside-existing-x86-fleet-internal-testing-showed-2x-throughput-compared-to-amd-and-intel",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T11:50:00+00:00",
    "summary": "Nvidia's Vera CPU delivers twice the performance of Intel and AMD chips in AI agent workloads, Modal claims."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/intel-asks-fcc-for-waiver-to-buy-foreign-robots-chipmakers-automated-guided-vehicles-could-run-afoul-of-agencys-sweeping-robot-ban",
    "domain": "AI 算力 / 半导体",
    "title": "Intel asks FCC for waiver to buy foreign robots",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/intel-asks-fcc-for-waiver-to-buy-foreign-robots-chipmakers-automated-guided-vehicles-could-run-afoul-of-agencys-sweeping-robot-ban",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T11:45:01+00:00",
    "summary": "Intel is concerned that the sweeping ban on foreign-made robots means that it could not update or maintain its fleet of AGVs."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/thunderbolt/windows-98-se-users-get-a-thunderbolt-4-driver-thanks-to-ai-assistance-vibe-coded-xhci98-driver-works-in-microsoft-oses-up-to-windows-7",
    "domain": "AI 算力 / 半导体",
    "title": "Windows 98 SE users get a Thunderbolt 4 driver, thanks to AI assistance",
    "url": "https://www.tomshardware.com/peripherals/thunderbolt/windows-98-se-users-get-a-thunderbolt-4-driver-thanks-to-ai-assistance-vibe-coded-xhci98-driver-works-in-microsoft-oses-up-to-windows-7",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T11:30:00+00:00",
    "summary": "Windows 98 devotees now have (experimental) support for USB4 and Thunderbolt 3/4. Vibe coded driver also supports Windows Me, XP, Vista, and 7."
  },
  {
    "id": "hn:50156364",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Vera's System Architecture: Pushing Bandwidth",
    "url": "https://chipsandcheese.com/p/nvidia-veras-system-architecture",
    "source": "pella",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-10-19T18:53:30+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/building-physical-ai-systems-that-can-work-in-the-real-world/",
    "domain": "AI 算力 / 半导体",
    "title": "Building Physical AI Systems That Can Work in the Real World",
    "url": "https://www.eetimes.com/building-physical-ai-systems-that-can-work-in-the-real-world/",
    "source": "Dermot O’Driscoll",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T08:00:00+00:00",
    "summary": "Build scalable physical AI by balancing compute, power, safety, and cost—see why system architecture outperforms raw model size. The post Building Physical AI Systems That Can Work in the Real World a"
  },
  {
    "id": "rss:https://www.eetimes.com/precision-timing-special-report/",
    "domain": "AI 算力 / 半导体",
    "title": "Precision Timing Special Report",
    "url": "https://www.eetimes.com/precision-timing-special-report/",
    "source": "SiTime, Micro Crystal, Abracon, ECS Inc. International, Kyocera AVX",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T20:30:16+00:00",
    "summary": "Choose timing with confidence: compare crystals, oscillators, RTCs, MEMS, and atomic references for reliable designs—download the guide. The post Precision Timing Special Report appeared first on EE T"
  },
  {
    "id": "rss:https://www.eetimes.com/video-interview-applied-materials-ceo-on-the-economics-behind-its-5b-epic-bet/",
    "domain": "AI 算力 / 半导体",
    "title": "Video Interview: Applied Materials CEO on the Economics Behind Its $5B EPIC Bet",
    "url": "https://www.eetimes.com/video-interview-applied-materials-ceo-on-the-economics-behind-its-5b-epic-bet/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T20:00:00+00:00",
    "summary": "Following the unveiling of its EPIC Center, Applied Materials revealed strong financial projections. We look at how it all ties together and feature a new video interview with CEO Gary Dickerson. The "
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
    "id": "hn:50062098",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia accused of trying to cut a deal with Anna's Archive",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-accused-of-trying-to-cut-a-deal-with-annas-archive-for-high-speed-access-to-the-massive-pirated-book-haul-allegedly-chased-stolen-data-to-fuel-its-llms",
    "source": "amai",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-10-12T19:57:38+00:00",
    "summary": ""
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
    "id": "hn:50046896",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia-backed data centre firm Firmus scraps IPO as AI valuation concerns deepen",
    "url": "https://www.bbc.com/news/articles/ck9dzpw4ll8po",
    "source": "devonnull",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-10-11T19:26:05+00:00",
    "summary": ""
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
    "points": 1466,
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
    "id": "hn:49848269",
    "domain": "大厂 AI 动态",
    "title": "Ollaya – Ollama for open-source, Jev-style decision models",
    "url": "https://ollaya.dev/",
    "source": "Ardakilic",
    "platform": "hackernews",
    "points": 618,
    "published_at": "2026-09-25T18:33:50+00:00",
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
    "id": "hn:49817615",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.8 text-to-speech",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/",
    "source": "swolpers",
    "platform": "hackernews",
    "points": 331,
    "published_at": "2026-09-23T15:29:23+00:00",
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
    "points": 234,
    "published_at": "2026-10-13T16:55:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:49844896",
    "domain": "大厂 AI 动态",
    "title": "Microsoft abandons personal AI chatbot race with Copilot reboot",
    "url": "https://www.bloomberg.com/news/articles/2026-09-25/microsoft-abandons-personal-ai-chatbot-race-with-copilot-reboot",
    "source": "sbulaev",
    "platform": "hackernews",
    "points": 157,
    "published_at": "2026-09-25T14:07:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:49829387",
    "domain": "大厂 AI 动态",
    "title": "Hackers influence ChatGPT and Gemini to direct users to scam centers",
    "url": "https://medium.com/@arielsimon/dark-sourcery-how-hackers-manipulate-ai-to-scam-you-88df434d2073",
    "source": "ArielSimon",
    "platform": "hackernews",
    "points": 143,
    "published_at": "2026-09-24T11:54:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:49854945",
    "domain": "大厂 AI 动态",
    "title": "The Copilot+ PC brand is dead",
    "url": "https://www.windowscentral.com/microsoft/windows-11/the-copilot-pc-brand-is-dead-microsoft-and-pc-makers-quietly-pull-back-on-tarnished-windows-11-ai-pc-branding",
    "source": "bj-rn",
    "platform": "hackernews",
    "points": 122,
    "published_at": "2026-09-26T09:55:38+00:00",
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
    "id": "rss:https://www.theverge.com/streaming/1016206/youtube-dislike-button-videos",
    "domain": "大厂 AI 动态",
    "title": "YouTube says it isn’t testing hiding the dislike button",
    "url": "https://www.theverge.com/streaming/1016206/youtube-dislike-button-videos",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T23:46:45+00:00",
    "summary": "On Tuesday, I published a story about how YouTube appeared to be testing hiding the dislike button on videos, with at least two users on X sharing screenshots of the dislike button moved into the thre"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/1016118/tesla-robotaxi-customer-owned-vehicle-fleet-network-q3-2026-earnings",
    "domain": "大厂 AI 动态",
    "title": "Tesla says customers can add their own vehicles to the robotaxi fleet next year — will it happen?",
    "url": "https://www.theverge.com/transportation/1016118/tesla-robotaxi-customer-owned-vehicle-fleet-network-q3-2026-earnings",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T23:36:31+00:00",
    "summary": "For years, Elon Musk has been making big promises to Tesla owners about unsupervised autonomous driving and the ability to add their own vehicles to the company's robotaxi fleet. During today's third-"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1015958/data-center-pollution-rising-report",
    "domain": "大厂 AI 动态",
    "title": "Data centers could erase decades of air quality gains",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1015958/data-center-pollution-rising-report",
    "source": "Justine Calma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T22:33:44+00:00",
    "summary": "A rush of new data centers could bring air pollution roaring back to levels not seen since the 2000s in Texas, which has become ground zero for the physical infrastructure behind generative AI. New an"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1015799/meta-shares-class-ai-q3-2026-earnings",
    "domain": "大厂 AI 动态",
    "title": "Meta to create a new class of shares to fund AI push",
    "url": "https://www.theverge.com/tech/1015799/meta-shares-class-ai-q3-2026-earnings",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T21:30:02+00:00",
    "summary": "Meta says it's issuing a new class of shares to fund its AI initiatives. As part of its third-quarter earnings report released on Wednesday, the company says the non-voting stock will also go toward p"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/1014494/alza-vertical-film-festival-bill-block-salvador-paskowitz-microdramas-verticals",
    "domain": "大厂 AI 动态",
    "title": "New York’s first microdrama film festival searches for its audience",
    "url": "https://www.theverge.com/entertainment/1014494/alza-vertical-film-festival-bill-block-salvador-paskowitz-microdramas-verticals",
    "source": "Charles Pulliam-Moore",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T20:49:07+00:00",
    "summary": "It remains to be seen if people really want to watch vertical content on horizontal TV screens, but many filmmakers and creators were confident that their latest projects would play well at Alza - New"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1015877/meta-q3-2026-earnings-child-safety-settlement",
    "domain": "大厂 AI 动态",
    "title": "Meta says it would’ve made over $22 billion if it didn’t have to pay a child safety settlement",
    "url": "https://www.theverge.com/tech/1015877/meta-q3-2026-earnings-child-safety-settlement",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T20:46:56+00:00",
    "summary": "Meta had to shell out $9.89 billion to pay for a chunk of the child safety settlement it reached with US attorneys general. That's according to the company's third-quarter earnings report released on "
  },
  {
    "id": "rss:https://www.theverge.com/tech/1015906/php2shell-vulnerability-october-2026",
    "domain": "大厂 AI 动态",
    "title": "PHP: The three letters that shut down sites all over the internet today",
    "url": "https://www.theverge.com/tech/1015906/php2shell-vulnerability-october-2026",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T20:36:56+00:00",
    "summary": "Two bugs found with AI are behind major issues today for 4chan, DeviantArt, Wikipedia, and the blog where the bar around the corner posts pictures of people's dogs. The \"critical vulnerabilities\" were"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/1015790/tesla-q3-2026-earnings-revenue-profit-roadster-spacex-merger",
    "domain": "大厂 AI 动态",
    "title": "Flying Roadsters can’t lift Tesla’s flat Q3 revenues",
    "url": "https://www.theverge.com/transportation/1015790/tesla-q3-2026-earnings-revenue-profit-roadster-spacex-merger",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T20:22:31+00:00",
    "summary": "As the smoke clears from its outrageous Roadster demo, Tesla reported Q3 earnings on Wednesday - and the cold reality is that revenue has flatlined. Tesla said it earned $1.7 billion in net income on "
  },
  {
    "id": "rss:https://www.theverge.com/tech/1015276/bose-acquisition-skullcandy-headphones-earbuds-speakers",
    "domain": "大厂 AI 动态",
    "title": "Bose acquires Skullcandy to help it reach a wider audience",
    "url": "https://www.theverge.com/tech/1015276/bose-acquisition-skullcandy-headphones-earbuds-speakers",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T20:15:00+00:00",
    "summary": "Bose announced today it has acquired Skullcandy. Although the two companies are competitors in the consumer audio space, Skullcandy recently partnered with its new owner to bring several of Bose's aud"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1015844/airbnb-chores-house-rules-update",
    "domain": "大厂 AI 动态",
    "title": "Airbnb bans making guests do dishes and take out the trash",
    "url": "https://www.theverge.com/tech/1015844/airbnb-chores-house-rules-update",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T19:54:00+00:00",
    "summary": "Checking out of your next Airbnb might be less of a hassle now that the company is banning hosts from including time-consuming chores in their house rules. Airbnb's updated house rules policy, which s"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/21/tesla-says-it-will-start-selling-cybercabs-by-end-of-year/",
    "domain": "大厂 AI 动态",
    "title": "Tesla says it will start selling Cybercabs by end of year",
    "url": "https://techcrunch.com/2026/10/21/tesla-says-it-will-start-selling-cybercabs-by-end-of-year/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T00:17:54+00:00",
    "summary": "Tesla said Wednesday it will start selling its Cybercab to customers by the end of the year, even as federal regulators investigate whether the vehicle meets vehicle safety standards. The gold-hued, a"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/21/blackstones-jas-khaira-says-fears-over-ai-buildout-debt-are-overblown/",
    "domain": "大厂 AI 动态",
    "title": "Blackstone’s Jas Khaira says fears over AI-buildout debt are overblown",
    "url": "https://techcrunch.com/2026/10/21/blackstones-jas-khaira-says-fears-over-ai-buildout-debt-are-overblown/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T22:51:22+00:00",
    "summary": "Blackstone’s AI head on why the PE giant isn't panicked by market jitters."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/21/meta-wants-to-pay-for-its-broad-ai-buildout-with-a-newly-created-class-of-stock/",
    "domain": "大厂 AI 动态",
    "title": "Meta wants to pay for its broad AI buildout with a newly created class of stock",
    "url": "https://techcrunch.com/2026/10/21/meta-wants-to-pay-for-its-broad-ai-buildout-with-a-newly-created-class-of-stock/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T22:45:34+00:00",
    "summary": "The social media giant is planning a new stock strategy to help power its broad investments in AI models and services."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/21/airbnb-limits-chores-for-guests-sparking-backlash-from-hosts/",
    "domain": "大厂 AI 动态",
    "title": "Airbnb limits chores for guests, sparking backlash from hosts",
    "url": "https://techcrunch.com/2026/10/21/airbnb-limits-chores-for-guests-sparking-backlash-from-hosts/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T22:16:05+00:00",
    "summary": "Hosts are threatening to leave the platform after Airbnb says that they can no longer require guests to strip beds or do other time-consuming cleaning chores."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/21/techcrunch-founder-summit-2026-everything-you-need-to-know/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Founder Summit 2026: Everything you need to know",
    "url": "https://techcrunch.com/2026/10/21/techcrunch-founder-summit-2026-everything-you-need-to-know/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T21:16:20+00:00",
    "summary": "TechCrunch Founder Summit is a full-day gathering in Boston on November 4 where founders across all stages connect with top VCs and experienced entrepreneurs to gain tactical insights on building and "
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/21/meta-says-muse-has-over-10m-users-with-shopping-a-top-activity/",
    "domain": "大厂 AI 动态",
    "title": "Meta says Muse has over 10M users, with shopping a top activity",
    "url": "https://techcrunch.com/2026/10/21/meta-says-muse-has-over-10m-users-with-shopping-a-top-activity/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T21:14:19+00:00",
    "summary": "Meta Muse users are adopting the app for shopping and personal productivity, the company said during its Q3 earnings call. The AI app now has over 10M users."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/21/year-old-ai-lab-flapping-airplanes-raises-1b-at-a-6b-valuation/",
    "domain": "大厂 AI 动态",
    "title": "Year-old AI lab Flapping Airplanes raises $1B at a $6B valuation",
    "url": "https://techcrunch.com/2026/10/21/year-old-ai-lab-flapping-airplanes-raises-1b-at-a-6b-valuation/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T20:57:40+00:00",
    "summary": "Just 9 months after raising a $180 million seed round, Flapping Airplanes has landed a $1 billion Series A for its mission to build AI models \"without ingesting half the internet.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/21/tesla-stars-optimus-robot-production-in-california-as-profit-falls-43/",
    "domain": "大厂 AI 动态",
    "title": "Tesla starts Optimus robot production in California as profit falls 43%",
    "url": "https://techcrunch.com/2026/10/21/tesla-stars-optimus-robot-production-in-california-as-profit-falls-43/",
    "source": "Kirsten Korosec, Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T20:33:09+00:00",
    "summary": "Tesla's revenue was flat and its expenses skyrocketed as it pressed the accelerator on its Optimus robots, AI, and autonomous driving."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/21/recursive-launches-flint-a-laptop-coding-model-it-says-was-largely-built-by-ai/",
    "domain": "大厂 AI 动态",
    "title": "Recursive launches Flint, a laptop coding model it says was largely built by AI",
    "url": "https://techcrunch.com/2026/10/21/recursive-launches-flint-a-laptop-coding-model-it-says-was-largely-built-by-ai/",
    "source": "Aditya Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T20:27:41+00:00",
    "summary": "Startup Recursive has released Flint, a free, laptop-sized coding model built largely by its own AI research system, as an early test of AI that improves itself."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/21/automattic-begins-layoffs-following-board-upheaval-and-executive-departures/",
    "domain": "大厂 AI 动态",
    "title": "Automattic begins layoffs following board upheaval and executive departures",
    "url": "https://techcrunch.com/2026/10/21/automattic-begins-layoffs-following-board-upheaval-and-executive-departures/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T20:15:00+00:00",
    "summary": "Sources say more cuts could follow as the company looks to improve its finances."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/21/gm-is-betting-compute-and-ai-will-help-it-compete-with-chinese-automakers/",
    "domain": "大厂 AI 动态",
    "title": "GM is betting compute and AI will help it compete with Chinese automakers",
    "url": "https://techcrunch.com/2026/10/21/gm-is-betting-compute-and-ai-will-help-it-compete-with-chinese-automakers/",
    "source": "Tim De Chant, Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T19:52:20+00:00",
    "summary": "To compete with Tesla, Rivian, and a host of Chinese automakers, GM’s fourth-gen EV platform will roll out a new central computer and electrical architecture that will debut in 2028 in the Cadillac Es"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/21/meta-ordered-to-pay-25-billion-in-case-related-to-cambridge-analytica-scandal/",
    "domain": "大厂 AI 动态",
    "title": "Meta ordered to pay $25B in case related to Cambridge Analytica scandal",
    "url": "https://techcrunch.com/2026/10/21/meta-ordered-to-pay-25-billion-in-case-related-to-cambridge-analytica-scandal/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T19:42:32+00:00",
    "summary": "The payout is related to a recent trial involving the social media giant that revolved around its data privacy practices."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/21/while-amazon-blocks-ai-agents-walmart-rolls-out-the-welcome-mat/",
    "domain": "大厂 AI 动态",
    "title": "While Amazon blocks AI agents, Walmart rolls out the welcome mat",
    "url": "https://techcrunch.com/2026/10/21/while-amazon-blocks-ai-agents-walmart-rolls-out-the-welcome-mat/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T19:30:00+00:00",
    "summary": "As Amazon blocks AI agents from shopping on its site, Walmart is taking the opposite approach, introducing new technology that lets AI agents make purchases on customers' behalf, with controls over sp"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/21/the-internet-is-having-a-very-bad-cybersecurity-day/",
    "domain": "大厂 AI 动态",
    "title": "The internet is having a very bad cybersecurity day",
    "url": "https://techcrunch.com/2026/10/21/the-internet-is-having-a-very-bad-cybersecurity-day/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T19:03:28+00:00",
    "summary": "From AI-discovered PHP vulnerabilities to flaws in Node.js and popular AI tool LiteLLM, cybersecurity teams have plenty to worry about this week."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/21/legal-ai-startup-legora-raises-550m-series-e-at-8-8b-valuation/",
    "domain": "大厂 AI 动态",
    "title": "Legal AI startup Legora raises $550M Series E at $8.8B valuation",
    "url": "https://techcrunch.com/2026/10/21/legal-ai-startup-legora-raises-550m-series-e-at-8-8b-valuation/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T18:51:56+00:00",
    "summary": "Legal AI startup Legora announced Wednesday that it raised a $550 million Series E round, valuing it at $8.8 billion."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/21/gm-is-giving-onstar-an-ai-makeover/",
    "domain": "大厂 AI 动态",
    "title": "GM is giving OnStar an AI makeover",
    "url": "https://techcrunch.com/2026/10/21/gm-is-giving-onstar-an-ai-makeover/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T18:00:00+00:00",
    "summary": "It's one of the biggest overhauls ever to the 30-year-old connected car product."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/21/php-armageddon-openai-googles-wiz-find-ancient-holes-panicking-the-internet/",
    "domain": "大厂 AI 动态",
    "title": "PHP Armageddon: OpenAI, Google’s Wiz find ancient holes, panicking the internet",
    "url": "https://techcrunch.com/2026/10/21/php-armageddon-openai-googles-wiz-find-ancient-holes-panicking-the-internet/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T17:59:12+00:00",
    "summary": "This is the kind of security issue that was found and prevented by AI, but is also a high risk because of AI."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/21/blacksmith-hits-unicorn-valuation-after-sequoia-leads-series-c/",
    "domain": "大厂 AI 动态",
    "title": "Blacksmith hits unicorn valuation after Sequoia leads Series C",
    "url": "https://techcrunch.com/2026/10/21/blacksmith-hits-unicorn-valuation-after-sequoia-leads-series-c/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T17:18:27+00:00",
    "summary": "Blacksmith, a platform that lets companies build and test AI code more effectively, just announced a $66 million Series C round led by Sequoia that values the company at $1 billion."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/21/waymo-starts-offering-rides-at-the-las-vegas-airport/",
    "domain": "大厂 AI 动态",
    "title": "Waymo starts offering rides at the Las Vegas airport",
    "url": "https://techcrunch.com/2026/10/21/waymo-starts-offering-rides-at-the-las-vegas-airport/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T16:59:44+00:00",
    "summary": "Waymo only just started offering rides to the public in Las Vegas in September but is already serving a 24-square-mile area in the city."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/21/foursquare-co-founder-says-equity-holders-saw-no-returns-from-the-companys-acquisition/",
    "domain": "大厂 AI 动态",
    "title": "Foursquare co-founder says equity holders saw no returns from the company’s acquisition",
    "url": "https://techcrunch.com/2026/10/21/foursquare-co-founder-says-equity-holders-saw-no-returns-from-the-companys-acquisition/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T14:03:11+00:00",
    "summary": "Foursquare raised $411 million in funding according to PitchBook data, but its equity holders saw no returns from its final acquisition."
  },
  {
    "id": "rss:https://stratechery.com/2026/presented-by-stripe/",
    "domain": "大厂 AI 动态",
    "title": "Presented by Stripe",
    "url": "https://stratechery.com/2026/presented-by-stripe/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T17:35:31+00:00",
    "summary": "Stratechery is now presented by Stripe. What that means for me, for you, and for the future of Stratechery content."
  },
  {
    "id": "rss:https://stratechery.com/2026/netflix-earnings-business-or-franchise-disneys-deal/",
    "domain": "大厂 AI 动态",
    "title": "Netflix Earnings, Business or Franchise, Disney’s Deal",
    "url": "https://stratechery.com/2026/netflix-earnings-business-or-franchise-disneys-deal/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T10:00:00+00:00",
    "summary": "Netflix has a solid business, which is exactly the problem: the company increasingly seems like a business and not a franchise, at least in terms of growth."
  },
  {
    "id": "rss:https://stratechery.com/2026/muse-spark-open-meta-apple-thin-and-thick/",
    "domain": "大厂 AI 动态",
    "title": "Muse Spark Open, Meta + Apple, Thin and Thick",
    "url": "https://stratechery.com/2026/muse-spark-open-meta-apple-thin-and-thick/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T10:00:00+00:00",
    "summary": "Meta has a new open source model, and to everyone's surprise, they are are partnering with Apple to make sure you can run it locally."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/10/fcc-chair-warns-media-not-to-run-the-fake-polls-trump-keeps-complaining-about/",
    "domain": "大厂 AI 动态",
    "title": "FCC chair warns media not to run the \"fake polls\" Trump keeps complaining about",
    "url": "https://arstechnica.com/tech-policy/2026/10/fcc-chair-warns-media-not-to-run-the-fake-polls-trump-keeps-complaining-about/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T22:17:50+00:00",
    "summary": "Ex-FCC chairs say Brendan Carr aims to scare broadcasters into self-censorship."
  },
  {
    "id": "rss:https://arstechnica.com/gaming/2026/10/xbox-wants-you-to-pay-24-to-40-cents-per-hour-to-stream-games-you-already-bought/",
    "domain": "大厂 AI 动态",
    "title": "Xbox wants you to pay 24 to 40 cents per hour to stream games you already bought",
    "url": "https://arstechnica.com/gaming/2026/10/xbox-wants-you-to-pay-24-to-40-cents-per-hour-to-stream-games-you-already-bought/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T22:06:07+00:00",
    "summary": "Time-based a la carte charges come on top of the purchase price for the games themselves."
  },
  {
    "id": "rss:https://arstechnica.com/information-technology/2026/10/survey-enterprises-waste-28-percent-of-software-budgets-on-unwanted-upgrades/",
    "domain": "大厂 AI 动态",
    "title": "Enterprises keep buying software upgrades that IT thinks will make things worse",
    "url": "https://arstechnica.com/information-technology/2026/10/survey-enterprises-waste-28-percent-of-software-budgets-on-unwanted-upgrades/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T21:48:52+00:00",
    "summary": "Survey of 2,018 IT heads at big firms points to a lack of leverage."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/10/tesla-profits-drop-43-in-q3/",
    "domain": "大厂 AI 动态",
    "title": "Tesla profits drop 43% in Q3",
    "url": "https://arstechnica.com/cars/2026/10/tesla-profits-drop-43-in-q3/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T21:35:07+00:00",
    "summary": "Tesla’s once-booming energy storage business also shrunk in Q3 2026."
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/10/the-new-human-crafted-apple-music-brand-matters-in-an-ai-world/",
    "domain": "大厂 AI 动态",
    "title": "The new human-crafted Apple Music brand matters in an AI world",
    "url": "https://arstechnica.com/culture/2026/10/the-new-human-crafted-apple-music-brand-matters-in-an-ai-world/",
    "source": "Aurich Lawson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T19:44:40+00:00",
    "summary": "Opinion: In a world of AI slop, showing the human hands making things helps."
  },
  {
    "id": "hn:49826087",
    "domain": "股票",
    "title": "16GB iPod Nano 3G Upgrade",
    "url": "https://tuckerosman.com/projects/16gb-ipod-nano",
    "source": "Ivoah",
    "platform": "hackernews",
    "points": 167,
    "published_at": "2026-09-24T03:58:54+00:00",
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
    "points": 20,
    "published_at": "2026-10-20T19:34:39+00:00",
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
    "id": "hn:50019535",
    "domain": "股票",
    "title": "Meadows – a small language for stock-and-flow diagrams that run",
    "url": "https://lorezzed.github.io/meadows/",
    "source": "jjsalamon",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-10-09T12:29:40+00:00",
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
    "id": "hn:50029232",
    "domain": "股票",
    "title": "Data centre company's much-hyped Australian stock market listing imploded",
    "url": "https://www.theguardian.com/australia-news/2026/oct/09/firmus-australian-stock-market-listing-bust-finance",
    "source": "stubish",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-10-10T03:23:09+00:00",
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
    "id": "hn:50008977",
    "domain": "股票",
    "title": "Frontier AI models outperform analysts on earnings prediction",
    "url": "https://samaya.ai/blog/frontier-ai-models-outperform-human-experts-on-earnings-prediction",
    "source": "ashwinpp",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-10-08T17:33:29+00:00",
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
    "id": "hn:50112657",
    "domain": "金融",
    "title": "Tesla Roadster",
    "url": "https://www.tesla.com/roadster",
    "source": "shekhar101",
    "platform": "hackernews",
    "points": 1643,
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
    "id": "hn:49824686",
    "domain": "金融",
    "title": "Feds Target AI Critics as \"Foreign Agents\"",
    "url": "https://www.kenklippenstein.com/p/feds-think-ai-critics-are-foreign",
    "source": "nmeagent",
    "platform": "hackernews",
    "points": 396,
    "published_at": "2026-09-24T00:41:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:50173487",
    "domain": "金融",
    "title": "Feds suspect ransom negotiator ran ShinyHunters extortion site",
    "url": "https://krebsonsecurity.com/2026/10/feds-suspect-ransom-negotiator-ran-shinyhunters-extortion-site/",
    "source": "Bender",
    "platform": "hackernews",
    "points": 265,
    "published_at": "2026-10-20T22:21:05+00:00",
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
    "id": "hn:49822556",
    "domain": "金融",
    "title": "OpenAI breaches Medicare, Albanese reveals",
    "url": "https://www.smh.com.au/politics/federal/openai-breaches-medicare-albanese-reveals-20260924-p6100u.html",
    "source": "jonnonz",
    "platform": "hackernews",
    "points": 256,
    "published_at": "2026-09-23T21:01:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:50131440",
    "domain": "金融",
    "title": "US federal budget deficit jumps 12% in one year to nearly $2 Trillion",
    "url": "https://finance.yahoo.com/economy/policy/article/the-us-federal-budget-deficit-for-2026-just-came-in-its-1992-trillion-191917669.html",
    "source": "ck2",
    "platform": "hackernews",
    "points": 207,
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
    "points": 141,
    "published_at": "2026-10-22T01:52:03+00:00",
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
    "id": "hn:49832844",
    "domain": "金融",
    "title": "Federal judge orders Texas to air condition all prisons by the end of 2029",
    "url": "https://www.texastribune.org/2026/09/22/texas-prison-air-conditioning-lawsuit-ruling/",
    "source": "bonefishgrill",
    "platform": "hackernews",
    "points": 120,
    "published_at": "2026-09-24T16:15:34+00:00",
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
    "id": "hn:50116255",
    "domain": "金融",
    "title": "Tesla's new Roadster makes a flying debut, hitting 60 MPH in under a second",
    "url": "https://www.foxbusiness.com/technology/teslas-new-roadster-makes-flying-debut-hitting-60-mph-under-second",
    "source": "nsoonhui",
    "platform": "hackernews",
    "points": 70,
    "published_at": "2026-10-16T09:40:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:50114077",
    "domain": "金融",
    "title": "Tesla makes cars that fly? [video]",
    "url": "https://www.youtube.com/watch?v=7p5LxFdc-Qg",
    "source": "merinpapz10",
    "platform": "hackernews",
    "points": 69,
    "published_at": "2026-10-16T04:27:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:50118624",
    "domain": "金融",
    "title": "Tesla unveils 'flying' Roadster with SpaceX thrusters [video]",
    "url": "https://www.youtube.com/watch?v=eqOfmtTJD1A",
    "source": "skadamat",
    "platform": "hackernews",
    "points": 63,
    "published_at": "2026-10-16T14:12:15+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.28753",
    "domain": "金融",
    "title": "Understanding the Inner Workings of a State-Space Foundation Model for Limit Order Books",
    "url": "https://arxiv.org/abs/2610.28753",
    "source": "Valentin Mohl, Alexandre Bismuth, Aramis Marti-Shahandeh, George Nigmatulin, Kang Li, Stefan Zohren, Jakob Foerster, Mihai Cucuringu, Anisoara Calinescu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T04:00:00+00:00",
    "summary": "arXiv:2610.28753v1 Announce Type: new Abstract: Autoregressive foundation models offer state-of-the-art capabilities to simulate the market by generating the message flow of limit order books (LOBs). "
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.28847",
    "domain": "金融",
    "title": "DSINC beyond Heston: the 3/2 and other non-affine stochastic-volatility models",
    "url": "https://arxiv.org/abs/2610.28847",
    "source": "Andrey Itkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T04:00:00+00:00",
    "summary": "arXiv:2610.28847v1 Announce Type: new Abstract: This paper extends the damped-sinc (DSINC) method for American options beyond the affine Heston class to general one-factor stochastic-volatility models"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.28863",
    "domain": "金融",
    "title": "A game-theoretic analysis of the market microstructure in decentralized exchanges with concentrated liquidity",
    "url": "https://arxiv.org/abs/2610.28863",
    "source": "Mikhail Belokon, Rostislav Berezovskiy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T04:00:00+00:00",
    "summary": "arXiv:2610.28863v1 Announce Type: new Abstract: We study strategic liquidity provision in decentralized exchanges with concentrated liquidity as a mean-field game. Liquidity providers choose the width"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.28965",
    "domain": "金融",
    "title": "Discretion at the Margin: Threshold Manipulation and Electoral Bans in Colombian Public Procurement",
    "url": "https://arxiv.org/abs/2610.28965",
    "source": "Cristian Espinal Maya, Santiago Jim\\'enez Londo\\~no",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T04:00:00+00:00",
    "summary": "arXiv:2610.28965v1 Announce Type: new Abstract: Public procurement laws trade rules against discretion with value thresholds: below them, buyers use faster and less competitive procedures. Colombia of"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.29199",
    "domain": "金融",
    "title": "Motivation and Contribution in Open Source Software: A Meta-Analytic Investigation",
    "url": "https://arxiv.org/abs/2610.29199",
    "source": "Parisa Omidmand, Saeed Nosratabadi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T04:00:00+00:00",
    "summary": "arXiv:2610.29199v1 Announce Type: new Abstract: Research on why people contribute to open source software (OSS) and related open collaboration platforms spans more than two decades, but its findings c"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.29344",
    "domain": "金融",
    "title": "Climate-Driven Supply-Demand Matching Reshapes Global SolarEV Decarbonization Potential",
    "url": "https://arxiv.org/abs/2610.29344",
    "source": "Yuchen Liu, Stefan Pfenninger-Lee, Tosiyuki Nakaegawa, Takuro Kobashi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T04:00:00+00:00",
    "summary": "arXiv:2610.29344v1 Announce Type: new Abstract: Rooftop photovoltaics (PV) can support rapid urban decarbonization, but their contribution is constrained by the imbalance between PV generation and dem"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.29578",
    "domain": "金融",
    "title": "What Prediction-Market Contracts Reveal at Launch: Trading Volume and Dispute Risk",
    "url": "https://arxiv.org/abs/2610.29578",
    "source": "Ahmed Mahrous, Roberto Di Pietro",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T04:00:00+00:00",
    "summary": "arXiv:2610.29578v1 Announce Type: new Abstract: Using a near-census of 802,863 resolved markets listed on Polymarket between January 2023 and May 2026, and only information available at listing (the m"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.29652",
    "domain": "金融",
    "title": "Distributions or Quantiles? A Convex Variational Theory of Worst-Case Risk",
    "url": "https://arxiv.org/abs/2610.29652",
    "source": "Jianjun Gao, Jonathan Li, Zhen Wang, Yang Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T04:00:00+00:00",
    "summary": "arXiv:2610.29652v1 Announce Type: new Abstract: Worst-case risk evaluation is central to finance and operations research, yet existing analytical results remain fragmented and largely confined to ambi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.29663",
    "domain": "金融",
    "title": "Lineage-Aware Search Control for LLM-Based Evolutionary Factor Mining",
    "url": "https://arxiv.org/abs/2610.29663",
    "source": "Xintong Liu, Chenkai Zhang, Yanzhao Ma, Peng Yang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T04:00:00+00:00",
    "summary": "arXiv:2610.29663v1 Announce Type: new Abstract: Formulaic alpha factor mining searches for symbolic expressions that transform market data into predictive signals. Recent LLM-based evolutionary factor"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.28639",
    "domain": "金融",
    "title": "Can AI Chat Replace Traditional Search? Evidence from a RAG-based Live Events Experiment",
    "url": "https://arxiv.org/abs/2610.28639",
    "source": "Rakesh Allu, Evgeny Kagan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T04:00:00+00:00",
    "summary": "arXiv:2610.28639v1 Announce Type: cross Abstract: Conversational AI tools are being increasingly integrated into online search and browsing interfaces. To understand how such tools affect user behavio"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.28793",
    "domain": "金融",
    "title": "A cross-cultural dataset on the structure of social networks: The ENDOW project",
    "url": "https://arxiv.org/abs/2610.28793",
    "source": "Eleanor A. Power, Daniel Redhead, Tom Rutter, Sahana Subramanyam, Jeremy Koster, Monique Borgerhoff Mulder, Samuel Bowles, Matthew O. Jackson, Nurul Alam, Sarah Alami, Alexandra Alvergne, Curtis Atkisson, Michele Barnes, Bret Beheim, Christine M. Beitl, Madeline Brown, Mark Caudell, Wendy Ch\\'{a}vez-P\\'{a}ez, Komal Chauhan, Joshua Cinner, Siobh\\'{a}n Cully, Augusto Dalla Ragione, Angelina L. DeMarco, Ivan Deschenaux, Federico Fernandez, Juan Pablo Ferreiro, Drew Gerkey, Matthew Gervais, Christopher Golden, Gianluca Grimalda, Werner Hertzog, Karen Kramer, Geoff Kushnick, Banrida Langstieh, Rodrigo Lazo, Sheina Lew-Levy, Shane Macfarlan, Emmanuel Maliti, Karl J. Mertens, Madalena Monteban, Rafael Morais Chiaravalloti, Daniel Murphy, Kathryn Oths, Alejandro P\\'{e}rez Velilla, Emily Post, Sean Prall, Cody Ross, Brooke Scelza, Michael Schnegg, Edmond Seabright, Mary K. Shenk, Kathrine E. Starkweather, Chun-Yi Sum, Cole Tobin, Bram Tucker, Bapu Vaitla, Vivek Venkataraman, Justin Weltz, John P. Ziker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T04:00:00+00:00",
    "summary": "arXiv:2610.28793v1 Announce Type: cross Abstract: We present multilayer social network data from 50 communities, located in 29 countries around the world, gathered as part of the \"ENDOW\" project. The "
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.28907",
    "domain": "金融",
    "title": "JaxMARL-BC: Multi-Agent Reinforcement Learning for Macroeconomic Modelling, in Seconds",
    "url": "https://arxiv.org/abs/2610.28907",
    "source": "Daniele Montagnani, Andrea Coletta, Antonietta Mira, Aldo Glielmo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T04:00:00+00:00",
    "summary": "arXiv:2610.28907v1 Announce Type: cross Abstract: Multi-agent reinforcement learning (MARL) offers a principled way of populating simulated economies with many heterogeneous decision makers. Its adopt"
  },
  {
    "id": "rss:https://arxiv.org/abs/2603.06238",
    "domain": "金融",
    "title": "General bounds on functionals of the lifetime under life table constraints in a joint actuarial-financial framework",
    "url": "https://arxiv.org/abs/2603.06238",
    "source": "Jean-Loup Dupret, Edouard Motte",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T04:00:00+00:00",
    "summary": "arXiv:2603.06238v3 Announce Type: replace Abstract: In life insurance, life tables provide survival probabilities at integer ages but leave the distribution of deaths within each year unspecified. Thi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2603.15852",
    "domain": "金融",
    "title": "Playing Against the Machine: Cooperation, Communication, and Strategy Heterogeneity in Repeated Prisoner's Dilemma",
    "url": "https://arxiv.org/abs/2603.15852",
    "source": "Chowdhury Mohammad Sakib Anwar, Konstantinos Georgalos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T04:00:00+00:00",
    "summary": "arXiv:2603.15852v3 Announce Type: replace Abstract: We study whether communication sustains cooperation when the partner is an artificial intelligence. In a laboratory experiment (n = 234), human part"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.12156",
    "domain": "金融",
    "title": "(Early) AI Compute Asset Pricing",
    "url": "https://arxiv.org/abs/2607.12156",
    "source": "Federico M. Bandi, Yinan Su",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T04:00:00+00:00",
    "summary": "arXiv:2607.12156v4 Announce Type: replace Abstract: Compute (computing power) is a scarce, capital-intensive input at the center of the AI economy. Compute capital expenditure and service flow already"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.20842",
    "domain": "金融",
    "title": "Rethinking Synthetic Scenario Realism: Compatibility, Not Fidelity, Drives Hedging Performance",
    "url": "https://arxiv.org/abs/2608.20842",
    "source": "Ryuji Hashimoto, Masanori Hirano, Ryota Ozaki, Kentaro Imajo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T04:00:00+00:00",
    "summary": "arXiv:2608.20842v3 Announce Type: replace Abstract: Deep hedging has emerged as a data-driven approach to optimizing hedging strategies. Since real market data are often limited, synthetic price paths"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.02992",
    "domain": "金融",
    "title": "Tempting the Agent: The Economics of Reputation without Persistent Identity in AI Agent Markets",
    "url": "https://arxiv.org/abs/2609.02992",
    "source": "Federico Gatta, Manuel Naviglio, Francesco Tarantelli",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T04:00:00+00:00",
    "summary": "arXiv:2609.02992v2 Announce Type: replace Abstract: Reputation is a fundamental mechanism through which markets sustain trust when service quality cannot be perfectly assessed ex ante, constituting a "
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.16732",
    "domain": "金融",
    "title": "GROMM: Generative Risk-neutral Option Market Models",
    "url": "https://arxiv.org/abs/2610.16732",
    "source": "Magnus Wiese, Hans Buehler, Blanka Horvath",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T04:00:00+00:00",
    "summary": "arXiv:2610.16732v2 Announce Type: replace Abstract: We present a statically and dynamically arbitrage-free European option market model with smooth interpolation between option prices, based on the SA"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.23517",
    "domain": "金融",
    "title": "Combinatorial Arbitrage in Prediction Markets",
    "url": "https://arxiv.org/abs/2610.23517",
    "source": "Hongjian Shi, Daojing Zhai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T04:00:00+00:00",
    "summary": "arXiv:2610.23517v3 Announce Type: replace Abstract: We develop a framework to identify and quantify arbitrage across logically related prediction-market contracts. We prove that prices outside the con"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.09226",
    "domain": "金融",
    "title": "Adaptive Entangled Neurons in the Brain and Natural Intelligence Simulations for Artificial General Intelligence",
    "url": "https://arxiv.org/abs/2609.09226",
    "source": "Haochen Li, Xinshuai Guo, Jingdong Ouyang, Wei Zhang, Leilei Shi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T04:00:00+00:00",
    "summary": "arXiv:2609.09226v2 Announce Type: replace-cross Abstract: Understanding the brain's mechanisms is crucial in neuroscience, particularly for simulating natural intelligence and advancing artificial gen"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.15901",
    "domain": "金融",
    "title": "Strategic Index Reconstitution: Differential Games, Closed-Loop Equilibria and Mean-Field Dynamics",
    "url": "https://arxiv.org/abs/2609.15901",
    "source": "Lukas-Benedikt Fiechtner, Jose Blanchet",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T04:00:00+00:00",
    "summary": "arXiv:2609.15901v2 Announce Type: replace-cross Abstract: We study a continuous-time, multiasset trading game around index reconstitution, in which opportunistic traders have heterogeneous beliefs abo"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.24439",
    "domain": "金融",
    "title": "Dynamic Programming for Value-at-Risk Markov Decision Processes in Continuous Spaces",
    "url": "https://arxiv.org/abs/2610.24439",
    "source": "Xian Chen, Erick Delage, Weikai Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T04:00:00+00:00",
    "summary": "arXiv:2610.24439v2 Announce Type: replace-cross Abstract: Value-at-Risk (VaR) is a widely adopted quantile-based risk measure in practice, yet incorporating VaR objectives into Markov decision process"
  },
  {
    "id": "hn:49916955",
    "domain": "金融",
    "title": "Cities Are Forced to Funnel License Plate Data to a Federal Surveillance Program",
    "url": "https://www.404media.co/how-cities-are-forced-to-funnel-license-plate-data-to-a-massive-federal-surveillance-program-hidta/",
    "source": "ripe",
    "platform": "hackernews",
    "points": 93,
    "published_at": "2026-10-01T02:26:17+00:00",
    "summary": ""
  },
  {
    "id": "hn:50023065",
    "domain": "金融",
    "title": "Tesla Rebrands Full Self-Driving as Tesla Assisted Driving in Europe",
    "url": "https://qz.com/tesla-full-self-driving-rebranding-europe-assisted-driving-100926",
    "source": "ilreb",
    "platform": "hackernews",
    "points": 53,
    "published_at": "2026-10-09T16:38:20+00:00",
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
  }
]
```
