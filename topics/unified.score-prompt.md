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

- 今日日期：`2026-10-07`
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
  "date": "2026-10-07",
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
    "points": 3100783,
    "published_at": "2026-06-07T05:32:32+00:00",
    "summary": "最近Codex的能力越来越全面，变成了Codex四大形态里最强一个。 Codex APP 比起 Claude Code，额度更高，功能更全，免费账户也能用。而且不会出现限速、封号、降智等问题，用过的小伙伴直呼真香。本期视频带来一个Codex APP的完整教程"
  },
  {
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "8分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 1934573,
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
    "points": 1367456,
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
    "points": 1313409,
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
    "points": 1109244,
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
    "points": 1079322,
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
    "points": 895669,
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
    "points": 832130,
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
    "points": 704898,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 447888,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 308461,
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
    "points": 301602,
    "published_at": "2025-04-15T00:59:13+00:00",
    "summary": "MCP终极指南 - 带你深入掌握MCP（基础篇）\n\n时间轴：\n01:05 MCP简要介绍\n02:47 安装 MCP Host（Cline）\n03:15 配置 Cline 用的 API Key\n06:01 第一个 MCP 问题\n06:31 概念解释：MCP Server 和 Tool\n09:13 配置 MCP Server\n14:19 使用 MCP Server\n15:24 MCP 交互流程详解\n1"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 230545,
    "published_at": "2026-04-27T08:51:41+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n   喜欢视频课程的同学一键三连多多支持一下，长按点赞五秒=lv6大佬 可以的发送彩色弹幕哦。\n配套源码项目已打包评论区回复up"
  },
  {
    "id": "bvid:BV1WWYE6LEzx",
    "domain": "AI",
    "title": "黑马程序员2026全网最夯VibeCoding零基础入门到实战项目开发全套视频教程，AI辅助编程从入门到实战，涵盖Claude Code、DeepSeek等内容",
    "url": "http://www.bilibili.com/video/av117251667724450",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 206398,
    "published_at": "2026-09-14T01:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260914\n2026黑马程序员AI智能应用开发学习路线图\nhttps://www.bilibili.com/opus/1156896913511940102\n如何下载资料\nhttps://www.bilibili.com/read/cv7881295/\n学习+球球群625260577，告别孤单，共同进步！\n\n【AI智能"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 195191,
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
    "points": 182845,
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
    "points": 158633,
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
    "points": 129568,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1K6YM69ESq",
    "domain": "AI",
    "title": "AI+网络安全实战：从Agent入门到AI智能体挖漏洞教程！网络安全|信息安全|黑客技术|渗透测试|SRC漏洞挖掘|AI审计|HVV护网行动|靶场练习-码士集团",
    "url": "http://www.bilibili.com/video/av117247037213495",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 86816,
    "published_at": "2026-09-10T13:47:24+00:00",
    "summary": "这套课程围绕「AI+网络安全」展开，从AI智能体基础入门，到WorkBuddy、Trae等主流Agent工具的实际应用，再到API-Key接入、Skill使用等核心能力，逐步进入AI漏洞挖掘、代码审计、CTF题目分析等安全实战场景。同时结合SRC漏洞挖掘、HVV护网、安全竞赛以及网络安全就业方向，帮助你系统了解AI在网络安全学习、开发与实战中的应用方式。适合网络安全初学者、安全从业者以及希望利用A"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operit教程：入门安卓最强大ai平台operitAI",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 60898,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 55747,
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
    "points": 54083,
    "published_at": "2026-08-27T00:43:58+00:00",
    "summary": "v1.1.6安装包：\n夸克网盘：\n链接：https://pan.quark.cn/s/43ff3db459f4?pwd=SD2k\n提取码：SD2k\ngithub仓库：\nPlaya-0v0/Cyrene-Agent: An open-source AI desktop companion inspired by Cyrene, combining immersive Chat, personaliz"
  },
  {
    "id": "bvid:BV1jCaq6nESn",
    "domain": "AI",
    "title": "【Opus 5.5半价】零基础小白友好，15分钟彻底学习Claude桌面版",
    "url": "http://www.bilibili.com/video/av117346425374831",
    "source": "LeaderAI",
    "platform": "bilibili",
    "points": 49470,
    "published_at": "2026-09-28T03:03:19+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 48971,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1hxMbzqEzU",
    "domain": "AI",
    "title": "小智MCP自由了！我开源了个命令行神器实现多MCP聚合",
    "url": "http://www.bilibili.com/video/av114686414625640",
    "source": "闪电蘑菇",
    "platform": "bilibili",
    "points": 42132,
    "published_at": "2025-06-15T08:31:55+00:00",
    "summary": "- 我写的小智客户端命令行工具\n - github: https://github.com/shenjingnan/xiaozhi-client\n - gitee: https://gitee.com/shenjingnan/xiaozhi-client\n\n- 小智官方MCP示例代码仓库：\n - github: https://github.com/78/mcp-calculator\n - git"
  },
  {
    "id": "bvid:BV1XiD5BQEAj",
    "domain": "AI",
    "title": "Claude Code 接入微信、一行命令把Claude Code装进微信、保姆级教程、微信支持Claude Code（cc-connect）远程开发",
    "url": "http://www.bilibili.com/video/av116350093694897",
    "source": "下班学AI",
    "platform": "bilibili",
    "points": 40325,
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
    "points": 34470,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1CmAGegEpa",
    "domain": "AI",
    "title": "使用Cursor实战Java项目（Cursor写Java代码）",
    "url": "http://www.bilibili.com/video/av114012708733672",
    "source": "小道仙97",
    "platform": "bilibili",
    "points": 33048,
    "published_at": "2025-02-16T09:02:42+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29805,
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
    "points": 28976,
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
    "points": 27977,
    "published_at": "2026-04-03T16:14:43+00:00",
    "summary": "每个参数都是干什么的，如何修改提示词的教程。\n不知道这是什么？请看合集内的视频~\n我做了一个 AI 的杀戮尖塔2MOD！\n可以和怪物对话，策反怪物，带着怪物爬塔（重写了几乎每一个怪物在友方时候的行为），还能给怪物打防御，带个沙虫全吃了！\n可以和上古之民对话，聊嗨了会给你 1～2 个额外赐福，还能帮你指示为未来\n可以让偷窃草蜢偷队友的 key 卡，想无限？偷了！\n可以和商人讨价还价，甚至白嫖\n多人的"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 23820,
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
    "points": 22805,
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
    "points": 19929,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1PdhR6GEsa",
    "domain": "AI",
    "title": "vibe coding现况",
    "url": "http://www.bilibili.com/video/av117336426158756",
    "source": "程序员牛牛学长",
    "platform": "bilibili",
    "points": 19532,
    "published_at": "2026-10-04T10:55:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV18TZYY8EuJ",
    "domain": "AI",
    "title": "微软最新AI Agent入门课程 • 中英",
    "url": "http://www.bilibili.com/video/av114246130076146",
    "source": "Mindofuture",
    "platform": "bilibili",
    "points": 17136,
    "published_at": "2025-03-30T02:06:00+00:00",
    "summary": "在这门包含10节课的课程中，我们将带你从概念到代码，全面覆盖构建AI代理的基础知识。在这里找到完整的“AI代理入门”课程及代码示例\nhttps://github.com/microsoft/ai-agents-for-beginners\n\nP01 什么是AI代理\nP02 使用哪种AI代理框架\nP03 如何设计优秀的AI代理\nP04 什么是代理工具使用设计模式\nP05 什么是代理式RAG\nP06 如"
  },
  {
    "id": "bvid:BV1xh3C6cEGv",
    "domain": "AI",
    "title": "两周完成一篇SCI论文，用claude code帮你干",
    "url": "http://www.bilibili.com/video/av117002408559933",
    "source": "博士大师兄木水",
    "platform": "bilibili",
    "points": 13048,
    "published_at": "2026-07-29T08:53:04+00:00",
    "summary": "大师兄八股文SCI速成模板已制作成skill，手把手带你实现一键生成SCI论文初稿"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 12117,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
  },
  {
    "id": "bvid:BV1Cvpw6iEwS",
    "domain": "AI",
    "title": "【10月Agent大横评】Deepseek用什么AI Agent不烧心，从夯到拉？",
    "url": "http://www.bilibili.com/video/av117393351251135",
    "source": "xx滴热茶",
    "platform": "bilibili",
    "points": 11974,
    "published_at": "2026-10-06T09:56:33+00:00",
    "summary": "Deepseek用什么agent不烧心，从夯到拉？穷鬼实测到底哪个agent和deepseek搭配做的又快又好还省钱？【8个Agent大横评】"
  },
  {
    "id": "bvid:BV1zbduYgEBH",
    "domain": "AI",
    "title": "Cursor新手教程⑤：Cursor降智真相+解决办法",
    "url": "http://www.bilibili.com/video/av114311359891940",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 10961,
    "published_at": "2025-04-10T02:53:27+00:00",
    "summary": "你是不是经常碰到这种情况：\n你试图修复一个小错误\n人工智能给出一个看似合理的更改建议\n这个修复导致其他地方出错\n你要求人工智能修复新出现的问题\n这又产生了另外两个问题\n如此反复\n本视频带你拆解Cursor降智的真相以及解决办法"
  },
  {
    "id": "bvid:BV1sQaL6vEkb",
    "domain": "AI",
    "title": "小白向，ai入门第一课：agent的部署和使用！",
    "url": "http://www.bilibili.com/video/av117349378166797",
    "source": "沈三殊",
    "platform": "bilibili",
    "points": 10532,
    "published_at": "2026-09-28T15:30:36+00:00",
    "summary": "详细的agent部署介绍：https://pan.quark.cn/s/3846914c6da7\n欢迎来到ai的世界！！\n有疑问欢迎私信。"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 9601,
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
    "points": 9278,
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
    "points": 7748,
    "published_at": "2026-05-06T09:24:14+00:00",
    "summary": "通过Termux安装Claude Code并且接入国内大模型"
  },
  {
    "id": "bvid:BV1u4G9zmEte",
    "domain": "AI",
    "title": "什么是MCP？VS Code中使用MCP Server",
    "url": "http://www.bilibili.com/video/av114426032168712",
    "source": "AI落地派",
    "platform": "bilibili",
    "points": 7114,
    "published_at": "2025-04-30T08:51:30+00:00",
    "summary": "什么是MCP，怎么样使用MCP Server，不用写SQL语句就可以查询数据库。\n\nMCP Servers\nhttps://smithery.ai/\nhttps://github.com/punkpeye/awesome-mcp-servers\nhttps://github.com/modelcontextprotocol/servers\n\nMCP Server for MySQL based o"
  },
  {
    "id": "bvid:BV1snhi6WE5P",
    "domain": "AI",
    "title": "【Cursor使用教程】史上最强AI编程工具Cursor！Cursor入门到精通保姆级教程！安装搭建/高阶技巧使用/开发小游戏/应用场景案例实战",
    "url": "http://www.bilibili.com/video/av117308156614035",
    "source": "图灵课堂",
    "platform": "bilibili",
    "points": 7042,
    "published_at": "2026-09-21T08:55:13+00:00",
    "summary": "整理制作不易，大家记得点个关注，一键三连呀【点赞、收藏、转发】感谢支持~\n全套AI大模型笔记/学习大纲/面试真题自取：https://www.bilibili.com/read/cv39638062/?spm_id_from=333.1387.0.0&amp;jump_opus=1"
  },
  {
    "id": "bvid:BV1QU6GYFEio",
    "domain": "AI",
    "title": "[课程4] 用Cursor开发数据库真的很简单 | Agent应用 | 用Codebase解决跨文件错误",
    "url": "http://www.bilibili.com/video/av113742109021318",
    "source": "Zhu的AI日记",
    "platform": "bilibili",
    "points": 7036,
    "published_at": "2024-12-31T12:30:00+00:00",
    "summary": "***这是全网最完整的分享如何在不懂编程的情况下，利用结构化思维，用Cursor开发商业app的系列课程。\n《懒人记单词》是基于艾宾浩斯遗忘曲线设计的记单词神器，它可以对每一个单词进行人性化的解读，并在每一个遗忘周期到来时及时提醒，并通过单词释义选择，拼写和造句进行全方位的巩固，同时AI还能对你的句子进行多维度的评估，确保你对每一个单词不仅会认，而且会用。\n\n***你将在本视频中学到：\n1.数据库"
  },
  {
    "id": "bvid:BV1aMAczmEmf",
    "domain": "AI",
    "title": "[MoonPack]在布吉岛里注入模组-mcp",
    "url": "http://www.bilibili.com/video/av116264966163402",
    "source": "DanciestZebra70",
    "platform": "bilibili",
    "points": 7003,
    "published_at": "2026-03-21T03:13:25+00:00",
    "summary": "交流群\n①1051043310\n②365233792"
  },
  {
    "id": "bvid:BV1auHq67Eja",
    "domain": "AI",
    "title": "【附链接】全局加载MCP教程",
    "url": "http://www.bilibili.com/video/av117377178012232",
    "source": "XiaozhumIOvO",
    "platform": "bilibili",
    "points": 6893,
    "published_at": "2026-10-03T13:21:35+00:00",
    "summary": "下载在https://wwbhw.lanzouq.com/b01gicrceh\n密码:三连\n里面的py.zip"
  },
  {
    "id": "bvid:BV1fNs9eiEm9",
    "domain": "AI",
    "title": "Cursor AI编程结合cocos3.8游戏开发教程-01",
    "url": "http://www.bilibili.com/video/av113187471105975",
    "source": "太阳8800",
    "platform": "bilibili",
    "points": 6852,
    "published_at": "2024-09-23T15:15:13+00:00",
    "summary": "开源源码仓库\nhttps://gitee.com/gamepublic/chess-cards"
  },
  {
    "id": "hn:49872723",
    "domain": "AI 算力 / 半导体",
    "title": "Owed a billion dollars in Nvidia stock",
    "url": "https://colo.to/nvidia-stock-narrative.html",
    "source": "Eric_Gullichsen",
    "platform": "hackernews",
    "points": 1091,
    "published_at": "2026-09-28T02:05:13+00:00",
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
    "id": "hn:49906100",
    "domain": "AI 算力 / 半导体",
    "title": "OpenDLSS: A Vulkan Reimplementation of Nvidia's DLSS 5 Neural Rendering Network",
    "url": "https://github.com/maanHimself/OpenDLSS-NR",
    "source": "sagacity",
    "platform": "hackernews",
    "points": 278,
    "published_at": "2026-09-30T08:43:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:49824864",
    "domain": "AI 算力 / 半导体",
    "title": "Virtio-nvgpu: Near-native Nvidia GPU access inside a KVM guest",
    "url": "https://github.com/nestrilabs/virtio-nvgpu",
    "source": "WanjohiRyan",
    "platform": "hackernews",
    "points": 155,
    "published_at": "2026-09-24T01:02:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:49926773",
    "domain": "AI 算力 / 半导体",
    "title": "Show HN: Janus – Go binary that runs GGUF models via Vulkan on AMD/Intel/Nvidia",
    "url": "https://github.com/Vibra-Ingenn/Janus",
    "source": "Maverick617",
    "platform": "hackernews",
    "points": 106,
    "published_at": "2026-10-01T20:36:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:49714096",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC revealing details about next gen A14 node",
    "url": "https://iedm26.mapyourshow.com/8_0/sessions/session-details.cfm?scheduleid=331",
    "source": "osnium123",
    "platform": "hackernews",
    "points": 129,
    "published_at": "2026-09-15T15:31:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:49933958",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon seeks to offload $8B of Nvidia chips to investors",
    "url": "https://www.reuters.com/business/retail-consumer/amazon-seeks-offload-8-billion-nvidia-chips-investors-ft-reports-2026-10-02/",
    "source": "wslh",
    "platform": "hackernews",
    "points": 82,
    "published_at": "2026-10-02T14:30:32+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/the-ai-boom-has-a-gigawatt-accounting-problem/",
    "domain": "AI 算力 / 半导体",
    "title": "The AI Boom Has a Gigawatt Accounting Problem",
    "url": "https://www.eetimes.com/the-ai-boom-has-a-gigawatt-accounting-problem/",
    "source": "Ron Honig",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T21:57:47+00:00",
    "summary": "Track energized compute, not gigawatts, as AI data centers face delays in memory, networking, cooling, and power. The post The AI Boom Has a Gigawatt Accounting Problem appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/axelera-ai-data-center-inference-performance-in-the-power-envelope-of-embedded-systems/",
    "domain": "AI 算力 / 半导体",
    "title": "Axelera AI: Data Center Inference Performance in the Power Envelope of Embedded Systems",
    "url": "https://www.eetimes.com/axelera-ai-data-center-inference-performance-in-the-power-envelope-of-embedded-systems/",
    "source": "EE Times",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T18:03:14+00:00",
    "summary": "Axelera’s Europa brings 629 TOPS inference to 35W edge systems while Voyager cuts toolchain lock-in. The post Axelera AI: Data Center Inference Performance in the Power Envelope of Embedded Systems ap"
  },
  {
    "id": "rss:https://www.eetimes.com/solving-the-five-hard-problems-of-nfc-antenna-integration-at-13-56-mhz/",
    "domain": "AI 算力 / 半导体",
    "title": "Solving the Five Hard Problems of NFC Antenna Integration at 13.56 MHz",
    "url": "https://www.eetimes.com/solving-the-five-hard-problems-of-nfc-antenna-integration-at-13-56-mhz/",
    "source": "Chris Zhong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T15:34:21+00:00",
    "summary": "Avoid NFC failures: plan ferrite shielding, flexible placement, robust connectors, and chipset validation before prototyping. The post Solving the Five Hard Problems of NFC Antenna Integration at 13.5"
  },
  {
    "id": "rss:https://www.eetimes.com/cxl-connected-mram-address-ai-storage-latency/",
    "domain": "AI 算力 / 半导体",
    "title": "CXL-Connected MRAM Address AI Storage Latency",
    "url": "https://www.eetimes.com/cxl-connected-mram-address-ai-storage-latency/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T10:24:22+00:00",
    "summary": "Everspin’s demo shows how a 4-GB pool of persistent MRAM can serve as a new tier of storage between DRAM and NAND flash. The post CXL-Connected MRAM Address AI Storage Latency appeared first on EE Tim"
  },
  {
    "id": "rss:https://www.eetimes.com/kepler-aims-to-launch-energy-saving-replacement-for-hbm-in-2027/",
    "domain": "AI 算力 / 半导体",
    "title": "Kepler Aims to Launch Energy-Saving Replacement for HBM in 2027",
    "url": "https://www.eetimes.com/kepler-aims-to-launch-energy-saving-replacement-for-hbm-in-2027/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T20:00:00+00:00",
    "summary": "Kepler targets 2027 production for 3D ferroelectric memory promising 5–10× better bandwidth per watt than HBM. The post Kepler Aims to Launch Energy-Saving Replacement for HBM in 2027 appeared first o"
  },
  {
    "id": "rss:https://www.eetimes.com/trusted-ai-why-intelligence-alone-isnt-enough/",
    "domain": "AI 算力 / 半导体",
    "title": "Trusted AI: Why Intelligence Alone Isn’t Enough",
    "url": "https://www.eetimes.com/trusted-ai-why-intelligence-alone-isnt-enough/",
    "source": "EE Times",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T17:48:56+00:00",
    "summary": "See how trusted AI combines intelligence, domain expertise, and deterministic verification to boost confidence in semiconductor design. The post Trusted AI: Why Intelligence Alone Isn’t Enough appeare"
  },
  {
    "id": "rss:https://www.eetimes.com/access-granted-unlocking-building-safety-and-security-controls-with-audio/",
    "domain": "AI 算力 / 半导体",
    "title": "ACCESS GRANTED – Unlocking Building Safety and Security Controls with Audio",
    "url": "https://www.eetimes.com/access-granted-unlocking-building-safety-and-security-controls-with-audio/",
    "source": "Same Sky and Arrow",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T16:08:24+00:00",
    "summary": "This webinar will cover current controls, modern technology selection, application considerations, and tailored audio component choices. The post ACCESS GRANTED – Unlocking Building Safety and Securit"
  },
  {
    "id": "rss:https://www.eetimes.com/gpt-synopsys-combines-ic-design-eda-with-agentic-ai/",
    "domain": "AI 算力 / 半导体",
    "title": "GPT-Synopsys Combines IC Design EDA with Agentic AI",
    "url": "https://www.eetimes.com/gpt-synopsys-combines-ic-design-eda-with-agentic-ai/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T12:00:00+00:00",
    "summary": "Synopsys joins OpenAI for a leap of faith in AI-native IC design by augmenting frontier models with EDA tools. The post GPT-Synopsys Combines IC Design EDA with Agentic AI appeared first on EE Times."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/mini-pcs/geekom-fall-tech-week-deals-offer-up-to-usd730-on-a-new-mini-pc-prices-start-at-just-usd284-both-amd-and-intel-options-on-sale",
    "domain": "AI 算力 / 半导体",
    "title": "Geekom Fall tech week deals offer up to $730 on a new mini PC",
    "url": "https://www.tomshardware.com/desktops/mini-pcs/geekom-fall-tech-week-deals-offer-up-to-usd730-on-a-new-mini-pc-prices-start-at-just-usd284-both-amd-and-intel-options-on-sale",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T10:00:00+00:00",
    "summary": "Mini PC specialist Geekom has more than a dozen mini PCs on sale across its website and Amazon, shaving as much as $730 off the price."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/samsung-9100-pro-ssd-gets-another-price-cut-up-to-51-percent-off-1tb-falls-below-usd200-4tb-below-usd750",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung 9100 Pro SSD gets another price cut, up to 51% off",
    "url": "https://www.tomshardware.com/pc-components/samsung-9100-pro-ssd-gets-another-price-cut-up-to-51-percent-off-1tb-falls-below-usd200-4tb-below-usd750",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T09:15:32+00:00",
    "summary": "Another huge price drop brings the Samsung 9100 Pro down even further, with the 1TB model now below $200, and the 4TB model dropping by nearly $400 since yesterday."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ddr5/corsair-has-slashed-usd103-off-this-32gb-vengeance-ram-the-cheapest-kit-on-the-market-at-this-speed",
    "domain": "AI 算力 / 半导体",
    "title": "Corsair has slashed $103 off this 32GB Vengeance RAM — the cheapest kit on the market at this speed",
    "url": "https://www.tomshardware.com/pc-components/ddr5/corsair-has-slashed-usd103-off-this-32gb-vengeance-ram-the-cheapest-kit-on-the-market-at-this-speed",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T09:00:00+00:00",
    "summary": "Get Corsair Vengeance DDR5 for $410."
  },
  {
    "id": "rss:https://www.tomshardware.com/live/news/amazon-prime-big-deal-days-2026-day-two",
    "domain": "AI 算力 / 半导体",
    "title": "Best Amazon Prime Day tech deals live",
    "url": "https://www.tomshardware.com/live/news/amazon-prime-big-deal-days-2026-day-two",
    "source": "The Editors of Tom&#039;s Hardware",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T06:21:39+00:00",
    "summary": "It's the final day of the Amazon Prime sale."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/get-usd500-off-this-sweet-ryzen-7-7800x3d-and-rtx-5070-powered-gaming-pc-at-just-usd1799-32gb-of-ddr5-6000-comes-standard-too-at-a-22-percent-discount",
    "domain": "AI 算力 / 半导体",
    "title": "Get 22% off this sweet Ryzen 7 7800X3D and RTX 5070-powered gaming PC at just $1799",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/get-usd500-off-this-sweet-ryzen-7-7800x3d-and-rtx-5070-powered-gaming-pc-at-just-usd1799-32gb-of-ddr5-6000-comes-standard-too-at-a-22-percent-discount",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T00:42:54+00:00",
    "summary": "Get $500 off this prebuilt gaming PC with a sweet Ryzen 7 7800X3D CPU, a powerful RTX 5070 graphics card, and 32GB of memory at just $1799."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/controllers-gamepads/grab-some-of-our-favorite-controllers-for-pc-gaming-for-less-than-the-cost-of-a-dualsense-get-a-quality-controller-with-more-features-during-prime-day",
    "domain": "AI 算力 / 半导体",
    "title": "Grab some of our favorite controllers for PC gaming for less than the cost of a DualSense",
    "url": "https://www.tomshardware.com/peripherals/controllers-gamepads/grab-some-of-our-favorite-controllers-for-pc-gaming-for-less-than-the-cost-of-a-dualsense-get-a-quality-controller-with-more-features-during-prime-day",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T21:53:18+00:00",
    "summary": "Sony's PC game controllers are on sale."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/get-a-1440p-qd-oled-monitor-for-just-usd280-entry-level-aoc-display-comes-with-144hz-refresh-rate-and-0-03ms-response-time",
    "domain": "AI 算力 / 半导体",
    "title": "Get a 1440p QD-OLED monitor for just $280 — entry-level AOC display comes with 144Hz refresh rate and 0.03ms response time",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/get-a-1440p-qd-oled-monitor-for-just-usd280-entry-level-aoc-display-comes-with-144hz-refresh-rate-and-0-03ms-response-time",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T20:15:40+00:00",
    "summary": "At $280, AOC's 27-inch 1440p QD-OLED monitor with a 144Hz refresh rate is one of the cheapest OLED displays we've seen."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/hp-takes-usd2200-off-a-ryzen-7-9800x3d-and-rtx-5080-prebuilt-at-usd2-799-sale-slashes-44-percent-off-an-omen-system-thats-ready-to-game-however-you-want",
    "domain": "AI 算力 / 半导体",
    "title": "HP takes $2200 off a Ryzen 7 9800X3D and RTX 5080 prebuilt at $2,799",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/hp-takes-usd2200-off-a-ryzen-7-9800x3d-and-rtx-5080-prebuilt-at-usd2-799-sale-slashes-44-percent-off-an-omen-system-thats-ready-to-game-however-you-want",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T18:47:37+00:00",
    "summary": "HP is selling its Omen 35L with an Nvidia RTX 5080 and Ryzen 7 9800X3D for $2,799, or $2200 off. This system has 32GB of RAM and a 2TB SSD for strong supporting performance, too."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/black-friday-laptop-deals-what-should-small-and-medium-sized-businesses-be-looking-for",
    "domain": "AI 算力 / 半导体",
    "title": "Black Friday laptop deals: What should small and medium-sized businesses be looking for?",
    "url": "https://www.tomshardware.com/laptops/black-friday-laptop-deals-what-should-small-and-medium-sized-businesses-be-looking-for",
    "source": "Sponsored",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T18:30:51+00:00",
    "summary": "Dell Pro 3, 5, and 7 laptops offer excellent options for small and medium-sized businesses this Black Friday. Here's how to find the best deal on the right laptop for your business."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/docking-stations-hubs/mac-mini-docks-add-more-ports-and-storage-get-more-out-of-your-headless-server-ai-machine-or-apple-workstation",
    "domain": "AI 算力 / 半导体",
    "title": "Mac Mini docks add more ports and storage — get more out of your headless server, AI machine, or Apple workstation",
    "url": "https://www.tomshardware.com/peripherals/docking-stations-hubs/mac-mini-docks-add-more-ports-and-storage-get-more-out-of-your-headless-server-ai-machine-or-apple-workstation",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T17:50:00+00:00",
    "summary": "Mac Mini docks add more ports and allow for further internal storage. Many of them are molded to fit directly beneath Apple's popular mini PC."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/award-winning-anycubic-3d-printers-on-sale-with-up-to-47-percent-off-massive-discounts-available-on-the-most-popular-models",
    "domain": "AI 算力 / 半导体",
    "title": "Award-winning Anycubic 3D Printers on sale with up to 47% off",
    "url": "https://www.tomshardware.com/3d-printing/award-winning-anycubic-3d-printers-on-sale-with-up-to-47-percent-off-massive-discounts-available-on-the-most-popular-models",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T17:30:00+00:00",
    "summary": "Anycubic's range of 3D printers sees large discounts in the Amazon Prime Big Deal Days sale"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/save-up-to-43-percent-on-these-handy-hoto-tools-for-pc-builders-and-hobbyists-starting-from-usd14-limited-time-deals-on-electric-screwdrivers-air-blowers-flashlights-cordless-drills-and-more",
    "domain": "AI 算力 / 半导体",
    "title": "Save up to 43% on these handy Hoto tools for PC builders and hobbyists, starting from $14",
    "url": "https://www.tomshardware.com/peripherals/save-up-to-43-percent-on-these-handy-hoto-tools-for-pc-builders-and-hobbyists-starting-from-usd14-limited-time-deals-on-electric-screwdrivers-air-blowers-flashlights-cordless-drills-and-more",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T16:50:00+00:00",
    "summary": "Amazon's big discount event means that now is the perfect time to stock up on Hoto's tools for hobbyists and PC builders, with deals running until October 7."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/controllers-gamepads/grab-this-epic-razer-wolverine-v3-controller-for-a-great-52-percent-off-now-just-usd94-99-for-this-competitive-wireless-gamepad-with-tmr-sticks-and-8k-polling-rate",
    "domain": "AI 算力 / 半导体",
    "title": "Grab this epic Razer Wolverine V3 controller for a great 53% off",
    "url": "https://www.tomshardware.com/peripherals/controllers-gamepads/grab-this-epic-razer-wolverine-v3-controller-for-a-great-52-percent-off-now-just-usd94-99-for-this-competitive-wireless-gamepad-with-tmr-sticks-and-8k-polling-rate",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T16:40:00+00:00",
    "summary": "This esports pro-friendly Razer Wolverine V3 Tournament Edition controller is on sale for a record-low Amazon Price, now just $94.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/storage/the-swiss-army-knife-of-usb-docking-dvd-drives-is-on-sale-also-available-with-built-in-m-2-ssd-slot-or-sata-hard-drive-dock-usd28-for-dvd-writer-and-hub-usd33-gets-an-added-sata-dock-or-pay-usd39-for-the-m-2-version",
    "domain": "AI 算力 / 半导体",
    "title": "The Swiss army knife of USB DVD drives is on sale, also features a built-in M.2 SSD slot, USB hub, and SATA hard drive dock",
    "url": "https://www.tomshardware.com/pc-components/storage/the-swiss-army-knife-of-usb-docking-dvd-drives-is-on-sale-also-available-with-built-in-m-2-ssd-slot-or-sata-hard-drive-dock-usd28-for-dvd-writer-and-hub-usd33-gets-an-added-sata-dock-or-pay-usd39-for-the-m-2-version",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T16:20:00+00:00",
    "summary": "Portable DVD writers with flash media reading, M.2, and SATA drive docking abilities are great Prime Day Deals."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-core-ultra-5-250k-plus-falls-to-its-lowest-price-ever-at-usd145-grab-an-18-core-midrange-cpu-with-5-3-ghz-boost-at-an-entry-level-price",
    "domain": "AI 算力 / 半导体",
    "title": "Intel's Core Ultra 5 250K Plus is down to its lowest price ever at $145",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-core-ultra-5-250k-plus-falls-to-its-lowest-price-ever-at-usd145-grab-an-18-core-midrange-cpu-with-5-3-ghz-boost-at-an-entry-level-price",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T15:50:00+00:00",
    "summary": "Intel's 18-core Core Ultra 5 250K Plus is down to its lowest price ever on Amazon, selling for just $145 on sale."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/buy-an-nvidia-rtx-5070-ti-16gb-for-only-usd1099-extra-discount-on-newegg-drops-the-price-on-the-triple-fan-gigabyte-windforce-to-the-lowest-price-weve-seen-in-months",
    "domain": "AI 算力 / 半导体",
    "title": "Buy an Nvidia RTX 5070 Ti 16GB for only $1099",
    "url": "https://www.tomshardware.com/pc-components/buy-an-nvidia-rtx-5070-ti-16gb-for-only-usd1099-extra-discount-on-newegg-drops-the-price-on-the-triple-fan-gigabyte-windforce-to-the-lowest-price-weve-seen-in-months",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T15:25:00+00:00",
    "summary": "Prices have been sky-high forever, but you can find a bit of a reprieve from Newegg as the Gigabyte Windforce 5070 Ti is on sale for only $1,099."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/this-cool-usd11-desktop-pc-power-switch-is-the-perfect-upgrade-for-your-desk-lets-you-stop-your-rig-without-bending-down-ultimate-impulse-buy-ships-with-durable-mechanical-keys-and-rgb-lighting",
    "domain": "AI 算力 / 半导体",
    "title": "This brilliant $11 power button gadget lets you switch your PC on from your desk with ease",
    "url": "https://www.tomshardware.com/pc-components/this-cool-usd11-desktop-pc-power-switch-is-the-perfect-upgrade-for-your-desk-lets-you-stop-your-rig-without-bending-down-ultimate-impulse-buy-ships-with-durable-mechanical-keys-and-rgb-lighting",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T14:56:51+00:00",
    "summary": "This fun, practical power button for your desk is just $11. As desk gadgets go, this is unbeatable. Grab it while you can."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/amds-radeon-rx-9070-gre-graphics-card-crashes-below-original-msrp-at-usd529-the-best-value-12gb-gpu-is-a-hot-deal",
    "domain": "AI 算力 / 半导体",
    "title": "AMD's Radeon RX 9070 GRE graphics card crashes to $529, below original MSRP",
    "url": "https://www.tomshardware.com/pc-components/gpus/amds-radeon-rx-9070-gre-graphics-card-crashes-below-original-msrp-at-usd529-the-best-value-12gb-gpu-is-a-hot-deal",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T14:44:56+00:00",
    "summary": "Grab a new 12GB GPU for less than the MSRP launch price."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/gta-v-playable-in-browser-immediately-nuked-unofficial-webassembly-port-built-with-ai-gets-taken-down-within-hours-of-going-live",
    "domain": "AI 算力 / 半导体",
    "title": "GTA V playable in browser immediately nuked",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/gta-v-playable-in-browser-immediately-nuked-unofficial-webassembly-port-built-with-ai-gets-taken-down-within-hours-of-going-live",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T13:50:55+00:00",
    "summary": "It's unclear who took down PlayGTA5.com but Take-Two would likely have taken quick action if it saw the website."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/cd-players-are-back-with-modern-interesting-features-starting-as-low-as-usd89-here-are-some-of-the-best-and-most-interesting-new-models",
    "domain": "AI 算力 / 半导体",
    "title": "CD players are back, and offering up modern, interesting features",
    "url": "https://www.tomshardware.com/peripherals/cd-players-are-back-with-modern-interesting-features-starting-as-low-as-usd89-here-are-some-of-the-best-and-most-interesting-new-models",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T13:28:44+00:00",
    "summary": "CD sales were up nearly 60% in the past year, outpacing vinyl and ushering in plenty of new and interesting hardware. If you’re looking to snag a new drive to play your old discs, there are quite a fe"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/gigaphoton-debuts-neon-recycling-system-with-claimed-50-percent-recovery-rate-systems-throw-a-lifeline-to-chipmakers-that-utilize-70-percent-of-global-neon-supply-in-duv-lithography",
    "domain": "AI 算力 / 半导体",
    "title": "Gigaphoton debuts neon recycling system with claimed 50% recovery rate",
    "url": "https://www.tomshardware.com/tech-industry/gigaphoton-debuts-neon-recycling-system-with-claimed-50-percent-recovery-rate-systems-throw-a-lifeline-to-chipmakers-that-utilize-70-percent-of-global-neon-supply-in-duv-lithography",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T13:20:00+00:00",
    "summary": "New neon gas recycling systems promise to reduce the demand for the noble gas at major chip manufacturers using DUV lithography. But as that technology is supplanted, this much-needed fix may only be "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/ev-charging-company-plans-to-deploy-100-000-nvidia-gpus-in-pods-at-its-roadside-sites-across-the-us-aims-to-offer-worlds-first-edge-inference-compute-network-using-idle-ev-charging-capacity",
    "domain": "AI 算力 / 半导体",
    "title": "EV charging company plans to deploy 100,000 Nvidia GPUs in pods at sites across the US",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/ev-charging-company-plans-to-deploy-100-000-nvidia-gpus-in-pods-at-its-roadside-sites-across-the-us-aims-to-offer-worlds-first-edge-inference-compute-network-using-idle-ev-charging-capacity",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T12:45:00+00:00",
    "summary": "EV charging firm Xeal plans to use its existing U.S. network to deploy the 'world’s first edge inference compute network using idle EV charging capacity.'"
  },
  {
    "id": "rss:https://www.tomshardware.com/speakers/trettires-retro-ambient-audio-system-offers-a-full-hi-fi-system-with-no-wires-wall-mountable-vinyl-cd-and-cassette-players-serve-as-functional-decor",
    "domain": "AI 算力 / 半导体",
    "title": "Wall-mountable record, CD, and cassette players combo is a full hi-fi system with no wires",
    "url": "https://www.tomshardware.com/speakers/trettires-retro-ambient-audio-system-offers-a-full-hi-fi-system-with-no-wires-wall-mountable-vinyl-cd-and-cassette-players-serve-as-functional-decor",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T12:30:00+00:00",
    "summary": "Trettire's Retro Ambient Audio System offers a full hi-fi system with no wires — wall-mountable vinyl, CD, and cassette players serve as functional decor"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/hackers-suspected-of-using-ai-agents-for-cyberattacks-on-south-korean-banks-exposing-data-from-about-25-000-customers-officials-believe-ai-models-enable-actors-to-hack-with-ease-even-without-specialized-skills",
    "domain": "AI 算力 / 半导体",
    "title": "Hackers suspected of using AI agents for cyberattacks on South Korean banks, exposing data from about 25,000 customers",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/hackers-suspected-of-using-ai-agents-for-cyberattacks-on-south-korean-banks-exposing-data-from-about-25-000-customers-officials-believe-ai-models-enable-actors-to-hack-with-ease-even-without-specialized-skills",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T12:15:00+00:00",
    "summary": "South Korean president Lee Jae Myung told his cabinet that there were signs that hackers used AI to execute the attacks on the banks."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/spending-on-u-s-data-center-buildings-hits-record-usd85-billion-annual-pace-up-73-percent-in-a-year-and-census-doesnt-count-the-servers-and-racks-inside",
    "domain": "AI 算力 / 半导体",
    "title": "Data center construction spending hits record $85 billion annual pace",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/spending-on-u-s-data-center-buildings-hits-record-usd85-billion-annual-pace-up-73-percent-in-a-year-and-census-doesnt-count-the-servers-and-racks-inside",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T12:00:00+00:00",
    "summary": "Census Bureau data shows U.S. data center construction spending hit a record $85 billion annual rate in August, up 73% in a year."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/two-of-alienwares-best-qd-oled-gaming-monitors-plummet-to-record-low-prices-34-inch-aw3426dw-ultrawide-360-hz-27-inch-aw2725df-are-up-to-28-percent-off",
    "domain": "AI 算力 / 半导体",
    "title": "Two of Alienware's best QD-OLED gaming monitors plummet to record-low prices",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/two-of-alienwares-best-qd-oled-gaming-monitors-plummet-to-record-low-prices-34-inch-aw3426dw-ultrawide-360-hz-27-inch-aw2725df-are-up-to-28-percent-off",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T11:47:59+00:00",
    "summary": "Ultrawide 280 Hz, or 16:9 at 360 Hz. Both won our Editors' Choice for their excellent performance."
  },
  {
    "id": "rss:https://www.tomshardware.com/live/news/amazon-prime-day-monitors-2026",
    "domain": "AI 算力 / 半导体",
    "title": "Prime Day gaming monitor deals live 2026",
    "url": "https://www.tomshardware.com/live/news/amazon-prime-day-monitors-2026",
    "source": "The Editors of Tom&#039;s Hardware",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T11:45:31+00:00",
    "summary": "The best Amazon Prime Day 2026 monitor sales, live round-the-clock coverage of all the best deals."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/qualcomm-will-pay-huawei-to-license-its-patents-for-the-first-time-in-historic-turnaround-reversal-in-a-5g-and-ai-cross-licensing-deal-comes-25-years-after-huawei-first-paid-qualcomm",
    "domain": "AI 算力 / 半导体",
    "title": "Qualcomm will pay Huawei to license its patents for the first time in historic turnaround",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/qualcomm-will-pay-huawei-to-license-its-patents-for-the-first-time-in-historic-turnaround-reversal-in-a-5g-and-ai-cross-licensing-deal-comes-25-years-after-huawei-first-paid-qualcomm",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T11:30:00+00:00",
    "summary": "Huawei and Qualcomm sign a multi-year patent cross-license covering 5G and AI, with Qualcomm buying some Huawei US patents."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/madlad-applies-dlss-5-to-the-original-duke-nukem-and-pong-tens-of-games-tested-with-outcomes-ranging-from-trippy-to-genuinely-interesting",
    "domain": "AI 算力 / 半导体",
    "title": "Madlad applies DLSS 5 to the original Duke Nukem and Pong",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/madlad-applies-dlss-5-to-the-original-duke-nukem-and-pong-tens-of-games-tested-with-outcomes-ranging-from-trippy-to-genuinely-interesting",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T11:00:00+00:00",
    "summary": "Madlad applies DLSS 5 to the original Duke Nukem and Pong — 50 games tested with outcomes ranging from trippy to genuinely interesting"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-and-synopsys-partner-to-build-gpt-synopsys-for-autonomous-chip-design-specialized-ai-model-will-operate-eda-tools-allowing-engineers-to-deliver-more-sophisticated-chips-faster",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI and Synopsys partner to build \"GPT-Synopsys\" for autonomous chip design",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-and-synopsys-partner-to-build-gpt-synopsys-for-autonomous-chip-design-specialized-ai-model-will-operate-eda-tools-allowing-engineers-to-deliver-more-sophisticated-chips-faster",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T11:00:00+00:00",
    "summary": "OpenAI and Synopsys are developing GPT-Synopsys, a specialized semiconductor-design model that will directly operate Synopsys EDA tools"
  },
  {
    "id": "hn:49879032",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang says AI distillation is 'competition.'",
    "url": "https://www.cnbc.com/2026/09/28/nvidias-jensen-huang-ai-distillation-china.html",
    "source": "cramer4next",
    "platform": "hackernews",
    "points": 73,
    "published_at": "2026-09-28T14:55:34+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/electric-car-makers-need-to-appeal-to-the-other-90/",
    "domain": "AI 算力 / 半导体",
    "title": "Electric Car Makers Need to Appeal to the ‘Other 90%’",
    "url": "https://www.eetimes.com/electric-car-makers-need-to-appeal-to-the-other-90/",
    "source": "Charles Murray",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T05:30:55+00:00",
    "summary": "Broader appeal for the electric car is a big challenge. Innovation is still the best solution. The post Electric Car Makers Need to Appeal to the ‘Other 90%’ appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/autosens-2026-regulations-drive-automotive-sensing-architectures/",
    "domain": "AI 算力 / 半导体",
    "title": "AutoSens 2026: Regulation Drives Automotive Sensing Architectures",
    "url": "https://www.eetimes.com/autosens-2026-regulations-drive-automotive-sensing-architectures/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T15:58:50+00:00",
    "summary": "At AutoSens Europe, automotive sensing designs reflected tighter safety standards, advances in AI processing, and growing cybersecurity requirements. The post AutoSens 2026: Regulation Drives Automoti"
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
    "id": "hn:49346906",
    "domain": "AI 算力 / 半导体",
    "title": "Ask HN: Do you feel comfortable admitting that you use AI?",
    "url": "https://news.ycombinator.com/item?id=49346906",
    "source": "var0xyz",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-08-18T15:16:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:49913571",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/",
    "source": "bradleyg223",
    "platform": "hackernews",
    "points": 1702,
    "published_at": "2026-09-30T20:04:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:49797982",
    "domain": "大厂 AI 动态",
    "title": "I said no and Apple said yes",
    "url": "https://dbushell.com/2026/09/22/apple-intelligence/",
    "source": "thatslast",
    "platform": "hackernews",
    "points": 886,
    "published_at": "2026-09-22T08:04:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:49957116",
    "domain": "大厂 AI 动态",
    "title": "Turn off Apple Intelligence on macOS 27 and get its disk space back",
    "url": "https://github.com/omlahore/RemoveMacAI",
    "source": "privacyisntdead",
    "platform": "hackernews",
    "points": 767,
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
    "points": 493,
    "published_at": "2026-09-15T17:38:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:49790409",
    "domain": "大厂 AI 动态",
    "title": "Turn off and restrict access to Apple Intelligence features on Mac",
    "url": "https://support.apple.com/guide/mac-help/turn-restrict-access-apple-intelligence-mchlb2e44f94/mac",
    "source": "alwillis",
    "platform": "hackernews",
    "points": 354,
    "published_at": "2026-09-21T17:30:21+00:00",
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
    "id": "hn:49914236",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon (High): Intelligence, Performance and Price Analysis",
    "url": "https://artificialanalysis.ai/models/gemini-4-argon",
    "source": "theanonymousone",
    "platform": "hackernews",
    "points": 112,
    "published_at": "2026-09-30T20:50:28+00:00",
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
    "id": "hn:49697014",
    "domain": "大厂 AI 动态",
    "title": "Notes on gotchas while migrating 35kb preprompts from Opus to self-hosted Ollama",
    "url": "https://patrickmccanna.net/notes-on-migrating-large-prompts-away-from-anthropic-openai-to-self-hosted-llms/",
    "source": "0o_MrPatrick_o0",
    "platform": "hackernews",
    "points": 140,
    "published_at": "2026-09-14T13:59:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:49859982",
    "domain": "大厂 AI 动态",
    "title": "Faster prompt lookup drafting in llama.cpp",
    "url": "https://jadidbourbaki.github.io/blog/prompt-lookup-llama-cpp/",
    "source": "pptadversary",
    "platform": "hackernews",
    "points": 89,
    "published_at": "2026-09-26T19:57:24+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1006355/openai-chatgpt-for-teens-common-sense-media",
    "domain": "大厂 AI 动态",
    "title": "ChatGPT for Teens is an ‘unacceptable risk,’ says Common Sense Media",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1006355/openai-chatgpt-for-teens-common-sense-media",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T09:00:00+00:00",
    "summary": "Common Sense Media, a nonprofit that offers reviews of apps, services, and entertainment with a focus on youth safety, today said that OpenAI's ChatGPT for Teens is an \"unacceptable risk.\" ChatGPT for"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1005004/openai-math-release-github",
    "domain": "大厂 AI 动态",
    "title": "OpenAI drops another batch of mathematical breakthroughs",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1005004/openai-math-release-github",
    "source": "Robert Hart",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T23:26:38+00:00",
    "summary": "OpenAI has revealed solutions to a number of long-standing mathematics problems produced by an unreleased frontier model in a batch of 722 manuscripts, covering 372 result families that group related "
  },
  {
    "id": "rss:https://www.theverge.com/report/1005859/microsoft-xbox-gta-6-streaming-rights",
    "domain": "大厂 AI 动态",
    "title": "Xbox has secured GTA 6 streaming rights",
    "url": "https://www.theverge.com/report/1005859/microsoft-xbox-gta-6-streaming-rights",
    "source": "Tom Warren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T22:12:27+00:00",
    "summary": "Xbox CEO Asha Sharma told employees that Microsoft is getting ready to do something around Grand Theft Auto VI that \"no other platform holder is doing\" during an employee all-hands this morning. Accor"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1006059/robot-vacuum-mop-roborock-qrevo-prime-day-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "The best robot vacuum and mop deals during October Prime Day",
    "url": "https://www.theverge.com/gadgets/1006059/robot-vacuum-mop-roborock-qrevo-prime-day-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T22:00:00+00:00",
    "summary": "Spending too much time constantly sweeping and mopping? If you have the money to delegate those chores to a robot cleaner, you could save a lot of personal time. Thankfully, it’s cheaper than usual to"
  },
  {
    "id": "rss:https://www.theverge.com/news/1006238/apple-lg-homekit-rumor-fcc",
    "domain": "大厂 AI 动态",
    "title": "Apple and LG team up on new smart home gear, starting with a lock, doorbell, and thermostat",
    "url": "https://www.theverge.com/news/1006238/apple-lg-homekit-rumor-fcc",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T21:39:53+00:00",
    "summary": "Apple is collaborating with LG on a new lineup of smart home devices, including a video doorbell, thermostat, indoor camera, and more, according to a report from Bloomberg. The products will reportedl"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/1006221/sebastian-maniscalco-siriusxm-channel-controversy",
    "domain": "大厂 AI 动态",
    "title": "Sebastian Maniscalco’s SiriusXM channel is hurting up-and-coming talent, comics say",
    "url": "https://www.theverge.com/entertainment/1006221/sebastian-maniscalco-siriusxm-channel-controversy",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T21:10:13+00:00",
    "summary": "Comedian Sebastian Maniscalco is facing backlash from fellow comics who claim his takeover of SiriusXM's Raw Comedy channel is harming up-and-coming talent, as reported earlier by Deadline. Many estab"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/1006193/tesla-model-3-model-y-powershare-home-backup",
    "domain": "大厂 AI 动态",
    "title": "Tesla&#8217;s Model 3 and Model Y can be a backup battery for your house",
    "url": "https://www.theverge.com/transportation/1006193/tesla-model-3-model-y-powershare-home-backup",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T20:37:54+00:00",
    "summary": "Some Tesla Model 3 and Model Y owners can use their EV battery to keep the lights on longer during a power outage, now that Tesla's expanding the Powershare Home Backup feature. It was previously only"
  },
  {
    "id": "rss:https://www.theverge.com/science/1006082/google-nuclear-energy-power-purchase-agreement-constellation",
    "domain": "大厂 AI 动态",
    "title": "Google’s power-hungry data centers crave nuclear energy",
    "url": "https://www.theverge.com/science/1006082/google-nuclear-energy-power-purchase-agreement-constellation",
    "source": "Justine Calma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T20:32:10+00:00",
    "summary": "Google announced a new agreement to update six nuclear power plant sites across the US as the tech giant seeks to generate more electricity for its power-hungry data centers. Google signed the 20-year"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1006020/amazon-kindle-paperwhite-prime-day-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Amazon’s last-gen Kindle Paperwhite is 30 percent off",
    "url": "https://www.theverge.com/gadgets/1006020/amazon-kindle-paperwhite-prime-day-deal-sale",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T20:00:00+00:00",
    "summary": "Calling something “last-gen” usually means it comes with big compromises compared to the latest version. That’s not as true for the last-gen Kindle Paperwhite as it is with some other tech. The newer "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1005662/apple-ipad-macbook-airpod-prime-day-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Save on MacBooks, iPads and Apple Watches during October Prime Day",
    "url": "https://www.theverge.com/gadgets/1005662/apple-ipad-macbook-airpod-prime-day-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T19:30:00+00:00",
    "summary": "Amazon’s October Big Deal Days are underway (lasting through tomorrow night), and we spotted a ton of Apple products and accessories in the sale, ranging from laptops and headphones to desktops and mo"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/07/spotify-expands-audiobooks-to-over-180-markets/",
    "domain": "大厂 AI 动态",
    "title": "Spotify expands audiobooks to over 180 markets",
    "url": "https://techcrunch.com/2026/10/07/spotify-expands-audiobooks-to-over-180-markets/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T07:00:00+00:00",
    "summary": "Spotify will make 350,000 titles available in over 120 languages for this expansion"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/06/how-to-find-out-if-amazon-thinks-you-have-flat-buttocks/",
    "domain": "大厂 AI 动态",
    "title": "How to find out if Amazon thinks you have ‘flat buttocks’",
    "url": "https://techcrunch.com/2026/10/06/how-to-find-out-if-amazon-thinks-you-have-flat-buttocks/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T22:55:39+00:00",
    "summary": "\"I stumbled upon a page of assumptions that Amazon has made about me based on my purchases and I’m literally speechless,\" one shopper wrote on Threads."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/06/apple-is-reportedly-partnering-with-lg-to-launch-a-smart-lock-thermostat-and-doorbell/",
    "domain": "大厂 AI 动态",
    "title": "Apple is reportedly partnering with LG to launch a smart lock, thermostat, and doorbell",
    "url": "https://techcrunch.com/2026/10/06/apple-is-reportedly-partnering-with-lg-to-launch-a-smart-lock-thermostat-and-doorbell/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T22:53:09+00:00",
    "summary": "Apple appears poised to push into the smart home market with a slate of new devices and a key partner."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/06/ex-ramp-engineers-raise-20m-for-platform-melius-after-scrapping-their-first-product/",
    "domain": "大厂 AI 动态",
    "title": "Ex-Ramp engineers raise $20M for platform Melius after scrapping their first product",
    "url": "https://techcrunch.com/2026/10/06/ex-ramp-engineers-raise-20m-for-platform-melius-after-scrapping-their-first-product/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T22:34:03+00:00",
    "summary": "Instead of helping marketers manage and optimize ad spend, the company is focusing on building the tools that generate the creative assets and campaigns."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/06/silicon-valleys-ai-wunderkind-launches-underdog-the-most-private-instinct-muse-competitor-yet/",
    "domain": "大厂 AI 动态",
    "title": "Silicon Valley’s AI wunderkind launches Underdog, the most private Instinct/Muse competitor yet",
    "url": "https://techcrunch.com/2026/10/06/silicon-valleys-ai-wunderkind-launches-underdog-the-most-private-instinct-muse-competitor-yet/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T20:47:01+00:00",
    "summary": "Sigil Wen, backed by a Silicon Valley who's who, has built an on-device AI assistant that promises to be free, fully private, and capable for everyday tasks."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/06/how-ai-decision-models-could-change-content-moderation/",
    "domain": "大厂 AI 动态",
    "title": "How AI decision models could change content moderation",
    "url": "https://techcrunch.com/2026/10/06/how-ai-decision-models-could-change-content-moderation/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T20:35:20+00:00",
    "summary": "On Tuesday, Musubi announced a lightweight decision model made for real-time moderation called PolicyLM-1.7B, released with open weights."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/06/ai-computing-startup-lambda-to-raise-4b-ahead-of-planned-ipo/",
    "domain": "大厂 AI 动态",
    "title": "AI computing startup Lambda to raise $4B ahead of planned IPO",
    "url": "https://techcrunch.com/2026/10/06/ai-computing-startup-lambda-to-raise-4b-ahead-of-planned-ipo/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T20:00:30+00:00",
    "summary": "Nvidia-backed Lambda is raising up to $4 billion at a $14.5 billion pre-money valuation ahead of a planned 2027 IPO, led by Coatue and Blackstone."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/06/the-next-hurdle-for-ai-agents-getting-websites-to-let-them-in/",
    "domain": "大厂 AI 动态",
    "title": "The next hurdle for AI agents: getting websites to let them in",
    "url": "https://techcrunch.com/2026/10/06/the-next-hurdle-for-ai-agents-getting-websites-to-let-them-in/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T19:56:50+00:00",
    "summary": "Personal AI agents promise to shop, book flights, and make reservations for you. But deliberate blocks and anti-bot defenses are getting in the way, leaving consumers caught in the middle. A new stand"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/06/hark-releases-an-ai-personal-assistant-with-a-focus-on-privacy/",
    "domain": "大厂 AI 动态",
    "title": "Hark releases an AI personal assistant with a focus on privacy",
    "url": "https://techcrunch.com/2026/10/06/hark-releases-an-ai-personal-assistant-with-a-focus-on-privacy/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T18:22:45+00:00",
    "summary": "The AI lab's personal assistant is an operating system from the future designed to compete with Muse, Dots, and Instinct."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/06/indias-jiohotstar-takes-partnership-route-for-middle-east-expansion/",
    "domain": "大厂 AI 动态",
    "title": "India’s JioHotstar takes partnership route for Middle East expansion",
    "url": "https://techcrunch.com/2026/10/06/indias-jiohotstar-takes-partnership-route-for-middle-east-expansion/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T17:14:07+00:00",
    "summary": "JioHotstar will be offered inside Starzplay rather than through a stand-alone service."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/06/mirror-particle-is-building-a-world-model-of-human-behavior/",
    "domain": "大厂 AI 动态",
    "title": "Mirror Particle is building a ‘world model’ of human behavior",
    "url": "https://techcrunch.com/2026/10/06/mirror-particle-is-building-a-world-model-of-human-behavior/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T16:35:00+00:00",
    "summary": "Mirror Particle will launch at TechCrunch Disrupt's Startup Battlefield 200 with a world model built from scratch to predict human behavior, arguing that LLM role-play falls short for market research "
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/06/furientis-lands-25m-from-benchmark-to-mass-produce-low-cost-missile-interceptors/",
    "domain": "大厂 AI 动态",
    "title": "Furientis lands $25M from Benchmark to mass-produce low-cost missile interceptors",
    "url": "https://techcrunch.com/2026/10/06/furientis-lands-25m-from-benchmark-to-mass-produce-low-cost-missile-interceptors/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T16:29:12+00:00",
    "summary": "The storied Silicon Valley firm makes its first pure defense investment."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/06/learn-all-about-scaling-fundraising-founder-how-tos-and-more-at-techcrunch-founder-summit-november-4/",
    "domain": "大厂 AI 动态",
    "title": "Learn all about scaling, fundraising, founder how-tos, and more at TechCrunch Founder Summit, November 4",
    "url": "https://techcrunch.com/2026/10/06/learn-all-about-scaling-fundraising-founder-how-tos-and-more-at-techcrunch-founder-summit-november-4/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T16:18:45+00:00",
    "summary": "There isn’t a single manual to read or prompt to give an LLM that can equip you with the skills and knowledge to build a company. But on November 4, TechCrunch Founder Summit gives founders the next-b"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/06/anthropic-gives-startups-a-free-year-of-enterprise-service-and-1000-in-token-credits/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic is giving startups a free year of Claude Team and $1,000 in credits",
    "url": "https://techcrunch.com/2026/10/06/anthropic-gives-startups-a-free-year-of-enterprise-service-and-1000-in-token-credits/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T16:00:00+00:00",
    "summary": "\"We created this program because we believe the benefits of AI will reach most people through the companies that build on top of models, rather than through the models alone.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/06/libreoffice-says-no-ai-is-now-a-software-feature/",
    "domain": "大厂 AI 动态",
    "title": "LibreOffice says ‘no AI’ is now a software feature",
    "url": "https://techcrunch.com/2026/10/06/libreoffice-says-no-ai-is-now-a-software-feature/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T15:25:00+00:00",
    "summary": "The maker of the open source document editor says it has no plans to add AI to its software's default configuration, citing user privacy."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/06/vinod-khosla-believes-ex-deepmind-engineers-wajo-will-win-agent-market-on-trust/",
    "domain": "大厂 AI 动态",
    "title": "Vinod Khosla believes ex-DeepMind engineer’s Wajo will win agent market on trust",
    "url": "https://techcrunch.com/2026/10/06/vinod-khosla-believes-ex-deepmind-engineers-wajo-will-win-agent-market-on-trust/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T15:15:00+00:00",
    "summary": "Wajo's Fo agent can hire humans to complete a task."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/06/bluesky-wants-to-give-you-your-own-domain-on-the-open-web/",
    "domain": "大厂 AI 动态",
    "title": "Bluesky wants to give you your own domain on the open web",
    "url": "https://techcrunch.com/2026/10/06/bluesky-wants-to-give-you-your-own-domain-on-the-open-web/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T14:41:52+00:00",
    "summary": "Bluesky says the process will still take 18-24 months, so don't expect your new, shortened 'bsky' handle any time soon."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/06/emmys-will-move-from-broadcast-tv-to-prime-video-in-2027/",
    "domain": "大厂 AI 动态",
    "title": "Emmys will move from broadcast TV to Prime Video in 2027",
    "url": "https://techcrunch.com/2026/10/06/emmys-will-move-from-broadcast-tv-to-prime-video-in-2027/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T14:37:31+00:00",
    "summary": "Non-Amazon Prime subscribers will be able to watch the awards show on the platform."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/06/mistrals-new-1t-model-aims-to-leapfrog-closed-and-open-rivals/",
    "domain": "大厂 AI 动态",
    "title": "Mistral’s new 1T model aims to leapfrog closed and open rivals",
    "url": "https://techcrunch.com/2026/10/06/mistrals-new-1t-model-aims-to-leapfrog-closed-and-open-rivals/",
    "source": "Anna Heim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T14:33:16+00:00",
    "summary": "French AI lab Mistral AI has released Mistral Large 4, a new large multimodal model aiming to leapfrog both American and Chinese rivals."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/06/pinterests-ai-now-turns-beauty-pins-into-action-plans/",
    "domain": "大厂 AI 动态",
    "title": "Pinterest’s AI now turns beauty Pins into action plans",
    "url": "https://techcrunch.com/2026/10/06/pinterests-ai-now-turns-beauty-pins-into-action-plans/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T14:00:49+00:00",
    "summary": "Pinterest’s new AI-powered Beauty Guides translate hair and nail Pins into salon terminology, with estimated costs, appointment times, and maintenance needs."
  },
  {
    "id": "rss:https://stratechery.com/2026/apple-and-lg-the-house-for-everyone-else-agent-standards-and-amazon/",
    "domain": "大厂 AI 动态",
    "title": "Apple and LG, The House For Everyone Else, Agent Standards and Amazon",
    "url": "https://stratechery.com/2026/apple-and-lg-the-house-for-everyone-else-agent-standards-and-amazon/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T10:01:39+00:00",
    "summary": "Apple is taking a smarter approach to the home than I expected, leaning into integration (with partners); then, what Amazon should do about agents."
  },
  {
    "id": "rss:https://stratechery.com/2026/game-decompilation-is-this-legal-a-well-trodden-path/",
    "domain": "大厂 AI 动态",
    "title": "Game Decompilation, Is This Legal?, A Well-Trodden Path",
    "url": "https://stratechery.com/2026/game-decompilation-is-this-legal-a-well-trodden-path/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T10:07:36+00:00",
    "summary": "Games are being decompiled, but the real risk to gaming is new games and increased personalization."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/10/drone-strikes-likely-russian-sink-ships-in-nato-countries-economic-zones/",
    "domain": "大厂 AI 动态",
    "title": "Drones sink ships near NATO countries in “unacceptable” attacks, EU says",
    "url": "https://arstechnica.com/gadgets/2026/10/drone-strikes-likely-russian-sink-ships-in-nato-countries-economic-zones/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T21:31:10+00:00",
    "summary": "Two cargo ships have sunk, one ship was afire, and sailors are dead or missing."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/10/openai-will-watermark-chatgpt-outputs-by-default-but-only-in-the-eu/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI will watermark ChatGPT outputs by default—but only in the EU",
    "url": "https://arstechnica.com/ai/2026/10/openai-will-watermark-chatgpt-outputs-by-default-but-only-in-the-eu/",
    "source": "Samuel Axon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T20:50:32+00:00",
    "summary": "Like other solutions, it is not especially reliable, and it's easy to circumvent."
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
    "id": "hn:49930086",
    "domain": "股票",
    "title": "US tells France and Germany to release diesel stocks or face US export ban",
    "url": "https://www.reuters.com/business/energy/us-tells-france-germany-release-diesel-stocks-or-face-us-export-ban-sources-say-2026-10-01/",
    "source": "geox",
    "platform": "hackernews",
    "points": 99,
    "published_at": "2026-10-02T05:22:20+00:00",
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
    "id": "hn:49948254",
    "domain": "金融",
    "title": "Federal judge calls Flock 'indiscriminate mass surveillance'",
    "url": "https://techcrunch.com/2026/10/03/federal-judge-calls-flock-indiscriminate-mass-surveillance/",
    "source": "sbulaev",
    "platform": "hackernews",
    "points": 497,
    "published_at": "2026-10-03T22:07:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:49778029",
    "domain": "金融",
    "title": "Samsung is expected to more than double output of its HBM4 and HBM4E DRAM",
    "url": "https://en.sedaily.com/finance/2026/09/20/samsung-to-double-hbm4-output-next-year-sources-say",
    "source": "giuliomagnifico",
    "platform": "hackernews",
    "points": 562,
    "published_at": "2026-09-20T17:38:50+00:00",
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
    "points": 257,
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
    "id": "hn:49981063",
    "domain": "金融",
    "title": "Former German spy chief arrested for attempted treason",
    "url": "https://www.reuters.com/business/finance/former-german-spy-chief-detained-suspicion-espionage-treason-bild-reports-2026-10-06/",
    "source": "semiquaver",
    "platform": "hackernews",
    "points": 120,
    "published_at": "2026-10-06T16:51:50+00:00",
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
    "id": "hn:49904408",
    "domain": "金融",
    "title": "Tesla takes on $30B in credit as it approaches unprofitability",
    "url": "https://electrek.co/2026/09/29/tesla-takes-on-30-billion-in-credit-as-it-approaches-unprofitability/",
    "source": "ciconia",
    "platform": "hackernews",
    "points": 161,
    "published_at": "2026-09-30T04:37:37+00:00",
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
    "id": "hn:49916668",
    "domain": "金融",
    "title": "10-year Treasury yield climbs above 5.3% to a level not seen in 24 years",
    "url": "https://www.wsj.com/finance/investing/surging-yields-bring-the-bond-market-back-to-the-turn-of-the-century-2b74773f",
    "source": "kaycebasques",
    "platform": "hackernews",
    "points": 123,
    "published_at": "2026-10-01T01:40:50+00:00",
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
    "id": "rss:https://arxiv.org/abs/2610.06856",
    "domain": "金融",
    "title": "The Agentic ETF: How Agentic Trading Becomes an Asset Class",
    "url": "https://arxiv.org/abs/2610.06856",
    "source": "Amandeep Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T04:00:00+00:00",
    "summary": "arXiv:2610.06856v1 Announce Type: new Abstract: Three structural trends are converging in public markets: the exchange-traded fund (ETF) has become the dominant fund wrapper, actively managed ETFs are"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.06947",
    "domain": "金融",
    "title": "FactorBench: A Portfolio-Aware Benchmark for Automated Factor Mining",
    "url": "https://arxiv.org/abs/2610.06947",
    "source": "Zhuohan Wang, Carmine Ventre",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T04:00:00+00:00",
    "summary": "arXiv:2610.06947v1 Announce Type: new Abstract: Factor mining seeks to discover signals from financial data that predict future asset returns and guide portfolio construction. Automated factor mining "
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.07003",
    "domain": "金融",
    "title": "Reliability of AI Agents: Rater Effects, Drift, and the Return to an Evaluation Program",
    "url": "https://arxiv.org/abs/2610.07003",
    "source": "Liu Zhang, Mark Esposito",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T04:00:00+00:00",
    "summary": "arXiv:2610.07003v1 Announce Type: new Abstract: Firms increasingly evaluate deployed AI agents using repeated human ratings, yet observed score changes may reflect the measurement process as much as c"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.07239",
    "domain": "金融",
    "title": "Optimal Retirement of European Fossil Fuel Power Plants and the Cost of Delay",
    "url": "https://arxiv.org/abs/2610.07239",
    "source": "Imke Rhoden",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T04:00:00+00:00",
    "summary": "arXiv:2610.07239v1 Announce Type: new Abstract: Mitigation pathways require fossil power plants to retire well before the end of their technical lives, yet retirement decisions are typically derived f"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.07888",
    "domain": "金融",
    "title": "A Functional Representation of Credit Behavior for Probability of Default Modeling",
    "url": "https://arxiv.org/abs/2610.07888",
    "source": "Jonas Brunholm, Bjarne H{\\o}jgaard, Thomas D. Nielsen, Orimar Sauri",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T04:00:00+00:00",
    "summary": "arXiv:2610.07888v1 Announce Type: new Abstract: This paper proposes a framework for modeling probability of default via functional data analysis. By representing a series of credit variables as functi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.07974",
    "domain": "金融",
    "title": "Configurations, not thresholds: the middle-income trap in the CEE members of the OECD",
    "url": "https://arxiv.org/abs/2610.07974",
    "source": "Zoltan Bartha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T04:00:00+00:00",
    "summary": "arXiv:2610.07974v1 Announce Type: new Abstract: The middle-income trap is usually identified by comparing a country's income to a threshold. This reveals that convergence has stalled but not where the"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.07985",
    "domain": "金融",
    "title": "A Finite Bid--Ask Spread from Replenishment Displaced from the Quote",
    "url": "https://arxiv.org/abs/2610.07985",
    "source": "Christopher Angstmann, Derick Diana, Tim Gebbie",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T04:00:00+00:00",
    "summary": "arXiv:2610.07985v1 Announce Type: new Abstract: We give a unified analytic account of a finite bid--ask spread in a two-field reaction--diffusion order book. The model retains separate bid and ask den"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.08004",
    "domain": "金融",
    "title": "University as catalyst of public R&D expenditures? An empirical assessment on EU NUTS 3 regions",
    "url": "https://arxiv.org/abs/2610.08004",
    "source": "Silvia Iossa, Saverio Barabuffi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T04:00:00+00:00",
    "summary": "arXiv:2610.08004v1 Announce Type: new Abstract: This study examines whether universities shape the regional innovation effects of public R&amp;D expenditure and whether this role varies across regiona"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.08169",
    "domain": "金融",
    "title": "Modelling Regime Shifts in Continuous Intraday Electricity Markets with State-dependent Hawkes Processes",
    "url": "https://arxiv.org/abs/2610.08169",
    "source": "Ayoub Jhabli, Tarek AlSkaif, Kwabena E. Bennin, Bedir Tekinerdogan, Axel Naumann, Joost M. E. Pennings",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T04:00:00+00:00",
    "summary": "arXiv:2610.08169v1 Announce Type: new Abstract: The growing importance of intraday trading in Europe, driven by the increasing penetration of renewable energy sources, has led to higher volatility and"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.08302",
    "domain": "金融",
    "title": "A Theory of Value Growth",
    "url": "https://arxiv.org/abs/2610.08302",
    "source": "Zhuo Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T04:00:00+00:00",
    "summary": "arXiv:2610.08302v1 Announce Type: new Abstract: Classical growth theory places physical productivity at the center of economic growth. In modern service-based economies, however, growth increasingly m"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.08447",
    "domain": "金融",
    "title": "Organizational Lifespan as Commitment: The Case of Foundations",
    "url": "https://arxiv.org/abs/2610.08447",
    "source": "Christian Jaag",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T04:00:00+00:00",
    "summary": "arXiv:2610.08447v1 Announce Type: new Abstract: An organization may bind future decision makers through a commitment over its own lifespan. This paper studies that choice for philanthropic foundations"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.08455",
    "domain": "金融",
    "title": "Competition with a Common Purpose",
    "url": "https://arxiv.org/abs/2610.08455",
    "source": "Christian Jaag",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T04:00:00+00:00",
    "summary": "arXiv:2610.08455v1 Announce Type: new Abstract: Non-governmental organizations often compete for funding while valuing similar social outcomes. Fundraising may expand total giving to a cause or redire"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.08467",
    "domain": "金融",
    "title": "Scalable Nonparametric Demand Estimation in Differentiated Product Markets",
    "url": "https://arxiv.org/abs/2610.08467",
    "source": "Julien Monardo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T04:00:00+00:00",
    "summary": "arXiv:2610.08467v1 Announce Type: new Abstract: The answers to many economic questions depend on the slope and curvature of demand. Estimating demand for differentiated products entails a trade-off be"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.08631",
    "domain": "金融",
    "title": "Exponential investors with weakly mean-reverting prices",
    "url": "https://arxiv.org/abs/2610.08631",
    "source": "Balazs Hoffmann, Miklos Rasonyi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T04:00:00+00:00",
    "summary": "arXiv:2610.08631v1 Announce Type: new Abstract: We investigate a continuous-time financial market where the asset price exhibits weak (sublinear) mean reversion and has a nonzero drift. Complementing "
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.08729",
    "domain": "金融",
    "title": "Ownership and Non-Neutral Technological Change: Evidence from China's State-Owned Enterprise Privatization",
    "url": "https://arxiv.org/abs/2610.08729",
    "source": "Ziyao Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T04:00:00+00:00",
    "summary": "arXiv:2610.08729v1 Announce Type: new Abstract: I estimate firm-level capital-, labor-, and material-augmenting productivity for Chinese manufacturing, 1998--2008, and the effect of state-owned enterp"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.07162",
    "domain": "金融",
    "title": "Adversarial Training for Deep Hedging in Nonstationary Markets",
    "url": "https://arxiv.org/abs/2610.07162",
    "source": "Philipp J. Schneider, Lukas Looser, Antoine Garin, Shuhan Liu, Daniel Kuhn",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T04:00:00+00:00",
    "summary": "arXiv:2610.07162v1 Announce Type: cross Abstract: Deep hedging learns trading policies from historical or simulated market trajectories, yet under nonstationarity these training paths may not represen"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.07404",
    "domain": "金融",
    "title": "Convex Order Beyond Dimension One: Projection Tests, Counterexamples and Gaussian Mixtures",
    "url": "https://arxiv.org/abs/2610.07404",
    "source": "Olivier Gu\\'eant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T04:00:00+00:00",
    "summary": "arXiv:2610.07404v1 Announce Type: cross Abstract: In actuarial science and quantitative finance, convex order provides a natural way to compare risks with the same mean. In dimension one, convex order"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.08194",
    "domain": "金融",
    "title": "The Noise Is the Signal: Correlated Sampling Error Is Rank-Informative for Proxy Metric Selection",
    "url": "https://arxiv.org/abs/2610.08194",
    "source": "Sandro Provenzano",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T04:00:00+00:00",
    "summary": "arXiv:2610.08194v1 Announce Type: cross Abstract: North-star metrics such as customer lifetime value are often too slow and noisy to decide a short A/B test. Teams therefore rely on a proxy metric, co"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.08264",
    "domain": "金融",
    "title": "Understanding Interfirm AI Talent Flow Networks through Online Professional Profiles",
    "url": "https://arxiv.org/abs/2610.08264",
    "source": "Donghang Li, Yunhan Zheng, Alok Prakash, Shenhao Wang, Jinhua Zhao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T04:00:00+00:00",
    "summary": "arXiv:2610.08264v1 Announce Type: cross Abstract: Artificial intelligence capabilities are often measured as resources accumulated within firms, yet they also circulate across organizational boundarie"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.08275",
    "domain": "金融",
    "title": "Personalized Recommendations Without Inducing Congestion: Mitigating Disparities in the NYC High School Match",
    "url": "https://arxiv.org/abs/2610.08275",
    "source": "Erica Chiang, Kenny Peng, Rebecca Lichtenstein, Brielle McDaniel, Kristen O'Neil, Deja Thomas, Lianna Wright, Jon Kleinberg, Eva Tardos, Nikhil Garg",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T04:00:00+00:00",
    "summary": "arXiv:2610.08275v1 Announce Type: cross Abstract: Algorithmic recommendations can help participants navigate large matching markets. For example, recommendations for school and college choices may red"
  },
  {
    "id": "rss:https://arxiv.org/abs/2405.08101",
    "domain": "金融",
    "title": "Data-driven measures of high-frequency trading",
    "url": "https://arxiv.org/abs/2405.08101",
    "source": "G. Ibikunle, B. Moews, D. Muravyev, K. Rzayev",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T04:00:00+00:00",
    "summary": "arXiv:2405.08101v4 Announce Type: replace Abstract: Public data do not identify high-frequency trading (HFT), and standard proxies do not separate liquidity-supplying from liquidity-demanding strategi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2601.12414",
    "domain": "金融",
    "title": "When Is the Gini Loading More Prudent? Tail Structure and the Ordering of the Standard Deviation and the Gini Mean Difference",
    "url": "https://arxiv.org/abs/2601.12414",
    "source": "Nawaf Mohammed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T04:00:00+00:00",
    "summary": "arXiv:2601.12414v4 Announce Type: replace Abstract: The standard deviation (SD) and the Gini mean difference (GMD) are the two canonical measures of variability used to load premiums, set risk margins"
  },
  {
    "id": "rss:https://arxiv.org/abs/2601.22167",
    "domain": "金融",
    "title": "The Evolution of Technology Portfolios and Firm Profitability in the European Power Sector",
    "url": "https://arxiv.org/abs/2601.22167",
    "source": "Robin Fischer, Anton Pichler",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T04:00:00+00:00",
    "summary": "arXiv:2601.22167v2 Announce Type: replace Abstract: Power firms' generation portfolios are long-lived and change slowly. We study how this inertia shapes profitability as market conditions shift. Link"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.02795",
    "domain": "金融",
    "title": "Coordinated Sniper Cohorts on Pump.fun: Detection of 1,012 Persistent Wallet Rings and a Contamination-Adjusted Estimate of Coordination-Specific First-Hour Buyer-Flow Lift",
    "url": "https://arxiv.org/abs/2607.02795",
    "source": "Arati Uday Kamat",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T04:00:00+00:00",
    "summary": "arXiv:2607.02795v4 Announce Type: replace Abstract: CORRECTION (Oct 2026): buyer records include sells and miss many buys; all numerical results below are withdrawn pending a corrected analysis. Motiv"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.20405",
    "domain": "金融",
    "title": "An Arbitrarily Precise Global Closed Form Approximation for the Neoclassical Growth Model",
    "url": "https://arxiv.org/abs/2609.20405",
    "source": "Jordan Roulleau-Pasdeloup",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T04:00:00+00:00",
    "summary": "arXiv:2609.20405v2 Announce Type: replace Abstract: I consider a neoclassical growth model with a constant absolute risk aversion (CARA) utility function and derive a global closed form approximation "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.37741",
    "domain": "金融",
    "title": "Dyson-Schwinger Effective-Action Methods for Rough Volatility: A Correlation-Response Architecture for Calibration, Exotics and Risk",
    "url": "https://arxiv.org/abs/2609.37741",
    "source": "Fr\\'ed\\'eric Pauquay",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T04:00:00+00:00",
    "summary": "arXiv:2609.37741v2 Announce Type: replace Abstract: We develop a non-perturbative framework for stochastic-volatility option pricing built on the two-particle-irreducible (2PI) effective action and th"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.37963",
    "domain": "金融",
    "title": "Not All LPs Are Equal: The Active-Passive Gap in Automated Market Maker Liquidity Provision",
    "url": "https://arxiv.org/abs/2609.37963",
    "source": "Agathe Sadeghi, Dingyue Liu, Ciamac Moallemi, Xin Wan, Brian Zhu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T04:00:00+00:00",
    "summary": "arXiv:2609.37963v2 Announce Type: replace Abstract: Liquidity provision in automated market makers is typically analyzed at the pool level, implicitly assuming LP homogeneity. This aggregate view can "
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.05740",
    "domain": "金融",
    "title": "Latent Continuum of Regimes in Limit Order Book Dynamics",
    "url": "https://arxiv.org/abs/2610.05740",
    "source": "Anjali Thawait",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T04:00:00+00:00",
    "summary": "arXiv:2610.05740v2 Announce Type: replace Abstract: Market-regime models typically assume a finite set of discrete latent states. We examine whether high frequency limit-order-book dynamics exhibit di"
  },
  {
    "id": "rss:https://arxiv.org/abs/2011.00520",
    "domain": "金融",
    "title": "Social networks, confirmation bias and shock elections",
    "url": "https://arxiv.org/abs/2011.00520",
    "source": "Edoardo Gallo, Alastair Langtry",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T04:00:00+00:00",
    "summary": "arXiv:2011.00520v2 Announce Type: replace-cross Abstract: This paper links the increasing prominence of social networks in politics to recent shock election outcomes. In our setup, agents learning on "
  },
  {
    "id": "hn:49930690",
    "domain": "金融",
    "title": "Quantitative Finance with OCaml",
    "url": "https://qcaml.com/index.html",
    "source": "leonry",
    "platform": "hackernews",
    "points": 54,
    "published_at": "2026-10-02T07:14:34+00:00",
    "summary": ""
  },
  {
    "id": "hn:49938815",
    "domain": "金融",
    "title": "Federal Judge Rules a Flock Search Was Unconstitutional",
    "url": "https://www.404media.co/federal-judge-rules-a-flock-search-was-indiscriminate-mass-surveillance-and-unconstitutional/",
    "source": "pavel_lishin",
    "platform": "hackernews",
    "points": 54,
    "published_at": "2026-10-02T21:28:59+00:00",
    "summary": ""
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
    "id": "hn:49849986",
    "domain": "金融",
    "title": "Show HN: Ekselio – Loveable for finance workflows (local first)",
    "url": "https://www.gptbeyond.com/try?home=1",
    "source": "kdautaj",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-09-25T21:09:28+00:00",
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
    "id": "hn:49924299",
    "domain": "金融",
    "title": "Sony released the first CD audio player on this day in 1982",
    "url": "https://www.tomshardware.com/pc-components/storage/sony-released-the-first-cd-audio-player-on-this-day-in-1982-player-cost-usd3-700-when-adjusted-for-inflation-but-it-would-be-another-decade-before-the-cd-rom-driven-multimedia-pc-era-began",
    "source": "Brajeshwar",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-10-01T17:07:39+00:00",
    "summary": ""
  }
]
```
