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

- 今日日期：`2026-10-04`
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
  "date": "2026-10-04",
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
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "8分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 1926862,
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
    "points": 1358617,
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
    "points": 1306484,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 1058417,
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
    "points": 894544,
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
    "points": 826958,
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
    "points": 701988,
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
    "points": 429915,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1eK5DzHEWu",
    "domain": "AI",
    "title": "MCP实战指南，mcp视频教程，2小时学透mcp",
    "url": "http://www.bilibili.com/video/av114380213586544",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 417799,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 305044,
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
    "points": 300447,
    "published_at": "2025-04-15T00:59:13+00:00",
    "summary": "MCP终极指南 - 带你深入掌握MCP（基础篇）\n\n时间轴：\n01:05 MCP简要介绍\n02:47 安装 MCP Host（Cline）\n03:15 配置 Cline 用的 API Key\n06:01 第一个 MCP 问题\n06:31 概念解释：MCP Server 和 Tool\n09:13 配置 MCP Server\n14:19 使用 MCP Server\n15:24 MCP 交互流程详解\n1"
  },
  {
    "id": "bvid:BV1ZRbe6eENh",
    "domain": "AI",
    "title": "DeepSeek Harness安装和使用教程【最新完整版】零基础小白速通deepseek harness入门教程怎么下载插件如何安装如何使用全搞定！",
    "url": "http://www.bilibili.com/video/av117110286062691",
    "source": "鹏哥C语言",
    "platform": "bilibili",
    "points": 237089,
    "published_at": "2026-08-17T10:10:51+00:00",
    "summary": "欢迎大家来到鹏哥课堂！这份DeepSeek Harness教程专为零基础小白打造，全程手把手演示安装、启动Web界面、模型接入、基础任务实操。 很多小白卡在环境配置、命令报错、参数设置，本教程能让你避开各种坑，跟着操作就能成功运行。 搞懂 Agent = 模型 + Harness，让 AI 读写文件、执行命令、自主完成项目任务。本教程适合程序员、AI 爱好者及想上手本地智能体的同学等。希望大家把视"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 227147,
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
    "points": 193321,
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
    "points": 182628,
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
    "points": 158403,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 93898,
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
    "points": 84643,
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
    "points": 58711,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1LXhc6yEkc",
    "domain": "AI",
    "title": "昔涟/Cyrene-Agent 安装配置/演示教程",
    "url": "http://www.bilibili.com/video/av117164694570292",
    "source": "Playa0",
    "platform": "bilibili",
    "points": 52840,
    "published_at": "2026-08-27T00:43:58+00:00",
    "summary": "v1.1.6安装包：\n夸克网盘：\n链接：https://pan.quark.cn/s/43ff3db459f4?pwd=SD2k\n提取码：SD2k\ngithub仓库：\nPlaya-0v0/Cyrene-Agent: An open-source AI desktop companion inspired by Cyrene, combining immersive Chat, personaliz"
  },
  {
    "id": "bvid:BV1wqeb6gEDY",
    "domain": "AI",
    "title": "Claude Code 百分百不封号",
    "url": "http://www.bilibili.com/video/av117297150694473",
    "source": "DUNHKPcc",
    "platform": "bilibili",
    "points": 50694,
    "published_at": "2026-09-19T10:14:15+00:00",
    "summary": "如果需要文档，私信主播，主页送免费的token，文件在群里 Q群1124987353"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 48885,
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
    "points": 40273,
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
    "points": 34452,
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
    "points": 33033,
    "published_at": "2025-02-16T09:02:42+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 30844,
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
    "points": 29799,
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
    "points": 28974,
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
    "points": 23661,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1HfYW6dEsh",
    "domain": "AI",
    "title": "vsTrader马上要关闭内地服务器了。",
    "url": "http://www.bilibili.com/video/av117239403513785",
    "source": "v1312996",
    "platform": "bilibili",
    "points": 21007,
    "published_at": "2026-09-09T05:36:24+00:00",
    "summary": "理财有风险，投资需谨慎。"
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 19433,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1Zka56QEsv",
    "domain": "AI",
    "title": "为了用上Claude，我被封了10个号｜网络、代充、KYC、苹果美区踩坑全记录",
    "url": "http://www.bilibili.com/video/av117349864708105",
    "source": "一唯光明故",
    "platform": "bilibili",
    "points": 18148,
    "published_at": "2026-09-28T17:34:14+00:00",
    "summary": "重度 AI 用户，工作全靠它：写报告、做 PPT、处理数据、写 Python 跑内网分析、写前端网页。\n为了用上 Claude，前前后后被封了不下 10 个号，这期把我踩过的坑一次讲清楚。"
  },
  {
    "id": "bvid:BV14erKYuEaE",
    "domain": "AI",
    "title": "最强编程AI Cursor+Unity制作一个史诗游戏(详细)",
    "url": "http://www.bilibili.com/video/av113774908413987",
    "source": "多西杰克",
    "platform": "bilibili",
    "points": 17858,
    "published_at": "2025-01-05T09:01:00+00:00",
    "summary": "网上惊呼Cursor AI厉害的内容很多，但结合Unity做游戏的不多，我就来实测一下，做一个AAA大作......"
  },
  {
    "id": "bvid:BV18TZYY8EuJ",
    "domain": "AI",
    "title": "微软最新AI Agent入门课程 • 中英",
    "url": "http://www.bilibili.com/video/av114246130076146",
    "source": "Mindofuture",
    "platform": "bilibili",
    "points": 17032,
    "published_at": "2025-03-30T02:06:00+00:00",
    "summary": "在这门包含10节课的课程中，我们将带你从概念到代码，全面覆盖构建AI代理的基础知识。在这里找到完整的“AI代理入门”课程及代码示例\nhttps://github.com/microsoft/ai-agents-for-beginners\n\nP01 什么是AI代理\nP02 使用哪种AI代理框架\nP03 如何设计优秀的AI代理\nP04 什么是代理工具使用设计模式\nP05 什么是代理式RAG\nP06 如"
  },
  {
    "id": "bvid:BV1pfuR69EoF",
    "domain": "AI",
    "title": "【全80集】零基础Vibe Coding教程，Vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av117070675118277",
    "source": "暴龙Boy",
    "platform": "bilibili",
    "points": 15917,
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
    "points": 11926,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
  },
  {
    "id": "bvid:BV1GD7qzREVA",
    "domain": "AI",
    "title": "【MCP部署实战】手把手教你把MCP接入各大热门工具，保姆级教学，我奶听了都能学会，CherryStudio配置MCP",
    "url": "http://www.bilibili.com/video/av114623818763366",
    "source": "亿点点大模型",
    "platform": "bilibili",
    "points": 9271,
    "published_at": "2025-06-04T07:08:58+00:00",
    "summary": "全程干货无废话！MCP最新实战教程，从环境部署、原理详解到项目实战，带你彻底吃透MCP！MCPServer开发，mcp开发，mcp教程，mcp项目 完整视频教程+讲解课件+学习笔记+AI大模型知识库已打包可分享！"
  },
  {
    "id": "bvid:BV1ebTi6yE7p",
    "domain": "AI",
    "title": "llama.cpp添加网络搜索等MCP工具 本地大模型摆脱过时数据束缚 实时获取最新数据 本地部署网络搜索MCP llama.cpp启动器添加了MCP代理选项",
    "url": "http://www.bilibili.com/video/av116845491329271",
    "source": "hsxbxq",
    "platform": "bilibili",
    "points": 7743,
    "published_at": "2026-07-01T15:49:48+00:00",
    "summary": "llama.cpp也可以添加网络搜索等MCP工具了，自此本地大模型终于可以简单的摆脱过时数据的束缚，实时获取最新数据了，相当于极简版的openclaw或Hermes了。 本期视频介绍了llama.cpp服务器图形化启动器1.4版添加了MCP代理选项，以及如何本地部署网络搜索MCP和添加百度搜索MCP方法。\nopen-webSearch介绍：https://github.com/Aas-ee/ope"
  },
  {
    "id": "bvid:BV1aSR4BKESW",
    "domain": "AI",
    "title": "安卓手机部署Claude Code",
    "url": "http://www.bilibili.com/video/av116526891993752",
    "source": "中国小骑士",
    "platform": "bilibili",
    "points": 7651,
    "published_at": "2026-05-06T09:24:14+00:00",
    "summary": "通过Termux安装Claude Code并且接入国内大模型"
  },
  {
    "id": "bvid:BV1sQaL6vEkb",
    "domain": "AI",
    "title": "小白向，ai入门第一课：agent的部署和使用！",
    "url": "http://www.bilibili.com/video/av117349378166797",
    "source": "沈三殊",
    "platform": "bilibili",
    "points": 7588,
    "published_at": "2026-09-28T15:30:36+00:00",
    "summary": "详细的agent部署介绍：https://pan.quark.cn/s/3846914c6da7\n欢迎来到ai的世界！！\n有疑问欢迎私信。"
  },
  {
    "id": "bvid:BV18Ya16FEha",
    "domain": "AI",
    "title": "【学习分享】如何让AI没有道德限制",
    "url": "http://www.bilibili.com/video/av117369275942500",
    "source": "yuppt",
    "platform": "bilibili",
    "points": 7536,
    "published_at": "2026-10-02T03:52:42+00:00",
    "summary": "代码地址：github.com/CuteCuteYu/Refusal-in-Language-Models"
  },
  {
    "id": "bvid:BV1fNs9eiEm9",
    "domain": "AI",
    "title": "Cursor AI编程结合cocos3.8游戏开发教程-01",
    "url": "http://www.bilibili.com/video/av113187471105975",
    "source": "太阳8800",
    "platform": "bilibili",
    "points": 6841,
    "published_at": "2024-09-23T15:15:13+00:00",
    "summary": "开源源码仓库\nhttps://gitee.com/gamepublic/chess-cards"
  },
  {
    "id": "bvid:BV1aMAczmEmf",
    "domain": "AI",
    "title": "[MoonPack]在布吉岛里注入模组-mcp",
    "url": "http://www.bilibili.com/video/av116264966163402",
    "source": "DanciestZebra70",
    "platform": "bilibili",
    "points": 6754,
    "published_at": "2026-03-21T03:13:25+00:00",
    "summary": "交流群\n①1051043310\n②365233792"
  },
  {
    "id": "bvid:BV1snhi6WE5P",
    "domain": "AI",
    "title": "【Cursor使用教程】史上最强AI编程工具Cursor！Cursor入门到精通保姆级教程！安装搭建/高阶技巧使用/开发小游戏/应用场景案例实战",
    "url": "http://www.bilibili.com/video/av117308156614035",
    "source": "图灵课堂",
    "platform": "bilibili",
    "points": 6720,
    "published_at": "2026-09-21T08:55:13+00:00",
    "summary": "整理制作不易，大家记得点个关注，一键三连呀【点赞、收藏、转发】感谢支持~\n全套AI大模型笔记/学习大纲/面试真题自取：https://www.bilibili.com/read/cv39638062/?spm_id_from=333.1387.0.0&amp;jump_opus=1"
  },
  {
    "id": "bvid:BV1ovuC66EuG",
    "domain": "AI",
    "title": "老 k 带你手搓 AI 交易智能体",
    "url": "http://www.bilibili.com/video/av117080372351441",
    "source": "老K聊交易系统",
    "platform": "bilibili",
    "points": 6481,
    "published_at": "2026-08-12T03:43:43+00:00",
    "summary": "这是一套使用 Codex开发 AI 交易智能体的系列课程，内容包括：智能体功能介绍到软件安装配置，再到开发自动化交易工具，策略优化与训练，实现交易 skill 稳定自动运行。\n课程资料包下载：www.jujijiaoyi.com"
  },
  {
    "id": "bvid:BV1UaYK6nEjP",
    "domain": "AI",
    "title": "【cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av117244419903051",
    "source": "茶子兀",
    "platform": "bilibili",
    "points": 5163,
    "published_at": "2026-09-10T02:39:36+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1C1ht6PEG6",
    "domain": "AI",
    "title": "【2026最新】这才是B站讲的最好的Vibe Coding系统教程，3小时带你从入门到精通，包含所有干货！让你少走99%弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av117319246286300",
    "source": "大模型学习路线",
    "platform": "bilibili",
    "points": 4963,
    "published_at": "2026-09-23T07:51:49+00:00",
    "summary": "【2026最新】这才是B站讲的最好的Vibe Coding系统教程，3小时带你从入门到精通，包含所有干货！让你少走99%弯路！学完即就业，带你玩转AI！"
  },
  {
    "id": "bvid:BV1Q8Yk6tEU6",
    "domain": "AI",
    "title": "AI 时代网安该如何入门？上手 AI 网安智能体！Agent 配置、Skill 技能、挖漏洞 + 代码审计 + CTF 完整实战",
    "url": "http://www.bilibili.com/video/av117268444876326",
    "source": "八方网域-可乐",
    "platform": "bilibili",
    "points": 3450,
    "published_at": "2026-09-14T08:30:26+00:00",
    "summary": "教程制作不易，如果视频对你有用的话，记得一键三连哦"
  },
  {
    "id": "bvid:BV1WiKG6ZEUf",
    "domain": "AI",
    "title": "Vibe Coding【渡一教育】",
    "url": "http://www.bilibili.com/video/av116928639140688",
    "source": "渡一前端教科频道",
    "platform": "bilibili",
    "points": 3098,
    "published_at": "2026-07-25T03:55:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV14JHq66EGV",
    "domain": "AI",
    "title": "Vibe Coding 做来做去，怎么全是记账 APP？",
    "url": "http://www.bilibili.com/video/av117377396115758",
    "source": "筱路luck",
    "platform": "bilibili",
    "points": 2192,
    "published_at": "2026-10-03T14:16:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:49872723",
    "domain": "AI 算力 / 半导体",
    "title": "Owed a billion dollars in Nvidia stock",
    "url": "https://colo.to/nvidia-stock-narrative.html",
    "source": "Eric_Gullichsen",
    "platform": "hackernews",
    "points": 1090,
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
    "points": 402,
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
    "points": 272,
    "published_at": "2026-09-30T08:43:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:49933958",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon seeks to offload $8B of Nvidia chips to investors",
    "url": "https://www.reuters.com/business/retail-consumer/amazon-seeks-offload-8-billion-nvidia-chips-investors-ft-reports-2026-10-02/",
    "source": "wslh",
    "platform": "hackernews",
    "points": 80,
    "published_at": "2026-10-02T14:30:32+00:00",
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
    "points": 101,
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
    "id": "rss:https://www.eetimes.com/continuous-health-monitoring-drives-integrated-wearable-system-design/",
    "domain": "AI 算力 / 半导体",
    "title": "Continuous Health Monitoring Drives Integrated Wearable System Design",
    "url": "https://www.eetimes.com/continuous-health-monitoring-drives-integrated-wearable-system-design/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T11:29:26+00:00",
    "summary": "Analog Devices India’s Praveen Jose said device miniaturization is driving higher performance and quality in smaller form factors. The post Continuous Health Monitoring Drives Integrated Wearable Syst"
  },
  {
    "id": "rss:https://www.tomshardware.com/service-providers/streaming/7-year-old-nvidia-shield-tv-pro-gets-shocking-50-percent-price-hike-driven-by-ai-memory-shortage-chipmaker-axes-entry-level-shield-tv-as-component-prices-soar",
    "domain": "AI 算力 / 半导体",
    "title": "7-year-old Nvidia Shield TV Pro gets shocking 50% price hike driven by AI memory shortage",
    "url": "https://www.tomshardware.com/service-providers/streaming/7-year-old-nvidia-shield-tv-pro-gets-shocking-50-percent-price-hike-driven-by-ai-memory-shortage-chipmaker-axes-entry-level-shield-tv-as-component-prices-soar",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T16:59:51+00:00",
    "summary": "The Shield TV Pro remains one of Nvidia’s longest-running consumer devices, but its $299.99 price tag now makes the streaming box considerably more expensive than when it launched."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/elon-musk-confirms-discussions-with-tsmc-about-terafab-chipmaking-collaboration-intel-is-the-only-other-named-partner-terafab-to-exclusively-supply-tesla-spacex-and-xai",
    "domain": "AI 算力 / 半导体",
    "title": "Elon Musk confirms discussions with TSMC about Terafab chipmaking collaboration",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/elon-musk-confirms-discussions-with-tsmc-about-terafab-chipmaking-collaboration-intel-is-the-only-other-named-partner-terafab-to-exclusively-supply-tesla-spacex-and-xai",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T14:50:50+00:00",
    "summary": "Elon Musk and TSMC reportedly discuss multiple collaboration opportunities within the Terafab project."
  },
  {
    "id": "rss:https://www.tomshardware.com/gift-guides-seasonal-sales/find-tech-deals-in-neweggs-fantastech-sale-ii-ahead-of-october-5-price-protection-guarantee-lets-you-start-shopping-now",
    "domain": "AI 算力 / 半导体",
    "title": "Find tech deals in Newegg's Fantastech Sale ahead of Amazon's Big Deals Day — early shoppers get automatic refunds if hardware prices drop lower",
    "url": "https://www.tomshardware.com/gift-guides-seasonal-sales/find-tech-deals-in-neweggs-fantastech-sale-ii-ahead-of-october-5-price-protection-guarantee-lets-you-start-shopping-now",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T14:40:00+00:00",
    "summary": "Ahead of Newegg's Fantastech Sale II launch on October 5th, you can grab some early deals and have price protection security if the product price drops lower in the sale proper."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/buying-used-cpus-can-expose-users-to-existing-bans-from-anti-cheat-engines-some-anti-cheat-engines-enforce-permanent-bans-while-others-have-an-expiration-date",
    "domain": "AI 算力 / 半导体",
    "title": "Buying used CPUs can expose users to existing bans from anti-cheat engines, and there's no way to check for violations before purchase",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/buying-used-cpus-can-expose-users-to-existing-bans-from-anti-cheat-engines-some-anti-cheat-engines-enforce-permanent-bans-while-others-have-an-expiration-date",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T14:09:00+00:00",
    "summary": "The CPU's previous owner apparently used it for cheating on Valorant, with its HWID getting flagged by Vanguard. When the Redditor bought and installed it on their PC, their Valorant account received "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/this-week-on-toms-hardware-premium-october-3-2026-ai-chip-design-week-openai-interview-and-ai-agent-safety",
    "domain": "AI 算力 / 半导体",
    "title": "This week on Tom's Hardware Premium: October 3, 2026",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/this-week-on-toms-hardware-premium-october-3-2026-ai-chip-design-week-openai-interview-and-ai-agent-safety",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T14:00:00+00:00",
    "summary": "This week on Tom's Hardware Premium, we open the floodgates with a free-to-access chip design week, including expert interviews, a sit-down with OpenAI on its custom ASIC, and much more."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/steam-revenue-hit-usd1-7-billion-in-september-2026-pc-gaming-spending-grows-despite-skyrocketing-hardware-costs",
    "domain": "AI 算力 / 半导体",
    "title": "Steam hits record $1.7 billion in September 2026 despite soaring PC hardware costs",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/steam-revenue-hit-usd1-7-billion-in-september-2026-pc-gaming-spending-grows-despite-skyrocketing-hardware-costs",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T13:35:00+00:00",
    "summary": "Steam's latest revenues highlight continued strength in PC gaming, with players continuing to spend heavily even as the cost of building and upgrading gaming PCs rises."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/futurum-ceo-says-agents-use-ai-5x-more-than-humans-number-will-eventually-hit-10x-but-agents-are-mostly-rereading-what-theyve-already-seen",
    "domain": "AI 算力 / 半导体",
    "title": "AI agents use 5x more tokens than humans as cached prompts explode, headed for 10x",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/futurum-ceo-says-agents-use-ai-5x-more-than-humans-number-will-eventually-hit-10x-but-agents-are-mostly-rereading-what-theyve-already-seen",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T13:10:00+00:00",
    "summary": "Daniel Newman’s number comes from OpenRouter data, where agents passed humans in February and grew 14x by August."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/scare-up-big-savings-in-bambu-labs-halloween-sale-right-now-with-up-to-30-percent-off-grab-usd250-off-the-dual-extruder-h2d-plus-bulk-spool-discounts-and-pumpkin-themed-bundles",
    "domain": "AI 算力 / 半导体",
    "title": "Scare up big savings in Bambu Lab's Halloween sale right now, with up to 30% off",
    "url": "https://www.tomshardware.com/3d-printing/scare-up-big-savings-in-bambu-labs-halloween-sale-right-now-with-up-to-30-percent-off-grab-usd250-off-the-dual-extruder-h2d-plus-bulk-spool-discounts-and-pumpkin-themed-bundles",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T12:50:00+00:00",
    "summary": "Don't let huge 3D printer prices scare you, because Bambu Lab's Halloween sale has knocked up to 30% off a new printer, with big bulk discounts on filament rolls, too."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/malicious-vpn-config-files-can-let-attackers-run-commands-on-asus-routers-companys-patch-also-fixes-a-bug-that-lets-a-logged-in-attacker-switch-on-telnet-with-root-access",
    "domain": "AI 算力 / 半导体",
    "title": "Malicious VPN config files can let attackers run commands on Asus routers",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/malicious-vpn-config-files-can-let-attackers-run-commands-on-asus-routers-companys-patch-also-fixes-a-bug-that-lets-a-logged-in-attacker-switch-on-telnet-with-root-access",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T12:30:00+00:00",
    "summary": "Until routers on Asus’s 3.0.0.6_102 firmware are updated, the company says not to import untrusted VPN files."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/google-suspends-part-of-the-oss-vrp-bug-bounty-program-due-to-an-influx-of-invalid-ai-submissions-product-vulnerability-submissions-ended-october-1",
    "domain": "AI 算力 / 半导体",
    "title": "Google freezes open-source bug bounty program amid flood of invalid AI slop submissions",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/google-suspends-part-of-the-oss-vrp-bug-bounty-program-due-to-an-influx-of-invalid-ai-submissions-product-vulnerability-submissions-ended-october-1",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T12:00:00+00:00",
    "summary": "Google suspends product vulnerability submissions to its Open Source Software Vulnerability Reward Program (OSS VRP) over an influx of invalid AI-driven reports."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/usd5-245-prebuilt-rtx-5090-pcs-connectors-melt-after-sitting-boxed-for-a-year-digital-storm-and-pny-deny-warranty-claims-over-expired-coverage-and-third-party-cables",
    "domain": "AI 算力 / 半导体",
    "title": "$5,245 prebuilt RTX 5090 PC's connectors melt after sitting boxed for a year",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/usd5-245-prebuilt-rtx-5090-pcs-connectors-melt-after-sitting-boxed-for-a-year-digital-storm-and-pny-deny-warranty-claims-over-expired-coverage-and-third-party-cables",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T11:40:00+00:00",
    "summary": "When one gamer's prebuilt PC had a GPU and power cables burn up, they didn't know where to turn: the system builder or the GPU manufacturer. It turned into a headache of differing policies and warrant"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/california-subpoenas-openai-as-it-investigates-huggingface-breach-doj-wants-more-information-on-cybersecurity-incidents-to-determine-developer-responsibility",
    "domain": "AI 算力 / 半导体",
    "title": "California subpoenas OpenAI over rogue AI agents conducting hacking attacks",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/california-subpoenas-openai-as-it-investigates-huggingface-breach-doj-wants-more-information-on-cybersecurity-incidents-to-determine-developer-responsibility",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T11:15:00+00:00",
    "summary": "California state Attorney General Rob Bonta issued a subpoena to OpenAI, compelling it to submit information on the hacking incidents that its models have been involved in. While the investigators hav"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/amazon-promises-to-spend-usd1-billion-on-communities-close-to-its-data-centers-but-critics-push-back-planned-spend-accounts-for-just-0-1-percent-of-its-2026-ai-infrastructure-investments",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon promises to spend $1 billion on communities close to its data centers, but critics push back",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/amazon-promises-to-spend-usd1-billion-on-communities-close-to-its-data-centers-but-critics-push-back-planned-spend-accounts-for-just-0-1-percent-of-its-2026-ai-infrastructure-investments",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T10:50:00+00:00",
    "summary": "AWS CEO Matt Garman said in a company blog post that it will allocate $1 billion over five years to key issues that data center communities raised, including education, workforce pathways, energy affo"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amds-secret-zen-3-gaming-cpu-had-128mb-of-l3-cache-but-never-saw-the-light-of-day-canceled-ryzen-9-5900x3d-breaks-free-from-the-chipmakers-vault",
    "domain": "AI 算力 / 半导体",
    "title": "AMD’s secret Zen 3 gaming CPU had 128MB of game-boosting L3 cache but never saw the light of day",
    "url": "https://www.tomshardware.com/pc-components/cpus/amds-secret-zen-3-gaming-cpu-had-128mb-of-l3-cache-but-never-saw-the-light-of-day-canceled-ryzen-9-5900x3d-breaks-free-from-the-chipmakers-vault",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T10:30:00+00:00",
    "summary": "A user from the Chinese Chiphell forums shows off AMD's unreleased Ryzen 9 5900X3D, the X3D variant of the Ryzen 9 5900X."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/gpt-6-astra-plays-world-of-warcraft-blind-and-clears-the-orc-starting-zone-in-40-minutes-with-no-deaths-ai-agent-navigates-by-server-network-traffic-with-pulled-quest-data",
    "domain": "AI 算力 / 半导体",
    "title": "ChatGPT-6 Astra plays World of Warcraft 'blind' and clears the orc starting zone in 40 minutes with no deaths",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/gpt-6-astra-plays-world-of-warcraft-blind-and-clears-the-orc-starting-zone-in-40-minutes-with-no-deaths-ai-agent-navigates-by-server-network-traffic-with-pulled-quest-data",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T10:00:00+00:00",
    "summary": "The model created its own World of Warcraft pathfinder on a private server with one prompt in OpenAI's Codex."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/hdds/toshiba-to-double-hdd-production-capacity-as-30tb-class-loom-65tb-100tb-drives-on-the-roadmap-for-2030-and-beyond",
    "domain": "AI 算力 / 半导体",
    "title": "Toshiba to double HDD production capacity amid devastating shortages",
    "url": "https://www.tomshardware.com/pc-components/hdds/toshiba-to-double-hdd-production-capacity-as-30tb-class-loom-65tb-100tb-drives-on-the-roadmap-for-2030-and-beyond",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T16:00:45+00:00",
    "summary": "Toshiba doubles HDD capacity in the Philippines in fiscal 2027, in time for 30TB-class HDD ramp in 2027."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/rumored-intel-nova-lake-table-lists-three-bfc-chips-with-up-to-144mb-of-l3-next-gen-cpu-lineup-takes-shape-with-up-to-28-cores-in-core-ultra-9-4970k-bfc",
    "domain": "AI 算力 / 半导体",
    "title": "Leaked Intel Nova Lake product list has three 'BFC' chips with up to 144MB of game-boosting L3 cache",
    "url": "https://www.tomshardware.com/pc-components/cpus/rumored-intel-nova-lake-table-lists-three-bfc-chips-with-up-to-144mb-of-l3-next-gen-cpu-lineup-takes-shape-with-up-to-28-cores-in-core-ultra-9-4970k-bfc",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T15:34:13+00:00",
    "summary": "A table rumored to hold Intel's upcoming models for Nova Lake processors as surfaced, now referring to the heavily-rumored bLLC as \"BFC.\""
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/california-tech-ceo-arrested-faces-up-to-20-years-in-prison-for-smuggling-usd300-million-in-nvidia-ai-servers-to-china-federal-prosecutors-say-chips-were-routed-through-malaysia-and-singapore-using-false-paperwork",
    "domain": "AI 算力 / 半导体",
    "title": "California tech CEO arrested, faces up to 20 years in prison for smuggling $300 million in Nvidia AI servers to China",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/california-tech-ceo-arrested-faces-up-to-20-years-in-prison-for-smuggling-usd300-million-in-nvidia-ai-servers-to-china-federal-prosecutors-say-chips-were-routed-through-malaysia-and-singapore-using-false-paperwork",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T14:53:41+00:00",
    "summary": "U.S. authorities have arrested a California man accused of smuggling more than $300 million worth of export-controlled Nvidia-powered servers to China through Malaysia and Singapore, allegedly using f"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/storage/biwins-cl-100-mini-is-a-particularly-puny-but-potent-ssd-for-portable-gaming-15-x-17-mm-in-size-and-up-to-2tb-in-capacity",
    "domain": "AI 算力 / 半导体",
    "title": "BiWin's CL 100 Mini is a particularly puny but potent SSD for portable gaming",
    "url": "https://www.tomshardware.com/pc-components/storage/biwins-cl-100-mini-is-a-particularly-puny-but-potent-ssd-for-portable-gaming-15-x-17-mm-in-size-and-up-to-2tb-in-capacity",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T14:30:00+00:00",
    "summary": "BiWin's CL 100 Mini is a particularly puny but potent SSD for portable gaming — 15 x 17mm in size and up to 2 TB in capacity"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/console-gaming/sony-brings-ai-powered-upscaling-to-the-standard-ps5-new-qssr-technology-to-deliver-a-taste-of-the-ps5-pro-experience-streamlined-neural-network-tech-built-with-amd",
    "domain": "AI 算力 / 半导体",
    "title": "Sony brings AI-powered upscaling to the standard PS5",
    "url": "https://www.tomshardware.com/video-games/console-gaming/sony-brings-ai-powered-upscaling-to-the-standard-ps5-new-qssr-technology-to-deliver-a-taste-of-the-ps5-pro-experience-streamlined-neural-network-tech-built-with-amd",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T14:10:00+00:00",
    "summary": "The base PS5 is getting an optimized version of Sony's AI-powered upscaling technology, offering developers a new way to improve image quality and stability without demanding more powerful hardware."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/amazon-and-synopsys-ink-multi-year-billion-dollar-deal-in-multi-year-ip-agreement-to-accelerate-ai-chip-design-efforts-synopsys-to-adopt-amazon-bedrock-to-deploy-ai-agents-harnessing-aws-compute-and-storage-capabilities",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon and Synopsys ink multi-year billion-dollar deal in multi-year IP agreement to accelerate AI chip design efforts",
    "url": "https://www.tomshardware.com/tech-industry/amazon-and-synopsys-ink-multi-year-billion-dollar-deal-in-multi-year-ip-agreement-to-accelerate-ai-chip-design-efforts-synopsys-to-adopt-amazon-bedrock-to-deploy-ai-agents-harnessing-aws-compute-and-storage-capabilities",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T13:50:00+00:00",
    "summary": "Amazon and chip design tool maker Synopsys have inked a multi-year partnership worth over a billion dollars. As part of the arrangement, Amazon will license Synopsys' chip designs and its design tools"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/flock-drones-with-cameras-deployed-as-first-responders-in-some-us-cities-amid-privacy-concerns-uavs-connect-to-wider-emergency-services-system-and-streams-video-to-dispatchers-officers",
    "domain": "AI 算力 / 半导体",
    "title": "Flock drones with cameras deployed as first responders in some US cities amid privacy concerns",
    "url": "https://www.tomshardware.com/tech-industry/drones/flock-drones-with-cameras-deployed-as-first-responders-in-some-us-cities-amid-privacy-concerns-uavs-connect-to-wider-emergency-services-system-and-streams-video-to-dispatchers-officers",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T13:20:00+00:00",
    "summary": "U.S. cities consider deploying Flock drones that automatically respond to emergency calls. However, other jurisdictions are pushing back against the service due to privacy and other concerns."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-introduces-64gb-dgx-spark-to-throw-local-ai-fans-a-lifeline-amid-the-rampocalypse-new-gb10-config-starts-at-usd4999-for-those-who-can-work-with-less",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia introduces 64GB DGX Spark to throw local AI fans a lifeline amid the RAMpocalypse",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-introduces-64gb-dgx-spark-to-throw-local-ai-fans-a-lifeline-amid-the-rampocalypse-new-gb10-config-starts-at-usd4999-for-those-who-can-work-with-less",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T13:00:00+00:00",
    "summary": "Nvidia is introducing a 64GB version of its DGX Spark local AI workstation that's tailored for a new generation of highly intelligent yet compact local models. Starting at $4999, the more affordable c"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/openais-jalapeno-asics-are-deployed-alongside-amd-epyc-turin-cpus-as-hosts-hardware-vp-says-nvidias-vera-standalone-is-a-little-bit-behind-on-that-maturity-level",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI’s Jalapeño ASICs are deployed alongside AMD EPYC ‘Turin’ CPUs as hosts, not Nvidia's Vera",
    "url": "https://www.tomshardware.com/pc-components/cpus/openais-jalapeno-asics-are-deployed-alongside-amd-epyc-turin-cpus-as-hosts-hardware-vp-says-nvidias-vera-standalone-is-a-little-bit-behind-on-that-maturity-level",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T12:40:00+00:00",
    "summary": "OpenAI chose to pair rack-scale deployments of its Jalapeño ASIC with AMD EPYC Turin CPUs, not the wave of high-performance agentic chips like Arm’s AGI or Nvidia’s Vera."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/routers/grab-an-usd80-discount-on-this-tp-link-wi-fi-7-router-with-five-2-5g-ethernet-ports-limited-time-deal-on-the-archer-be550-nets-a-tri-band-router-with-fast-speeds-to-upgrade-your-home-network",
    "domain": "AI 算力 / 半导体",
    "title": "Grab an $80 discount on this TP-Link Wi-Fi 7 router with five 2.5G Ethernet ports, now $169.99",
    "url": "https://www.tomshardware.com/networking/routers/grab-an-usd80-discount-on-this-tp-link-wi-fi-7-router-with-five-2-5g-ethernet-ports-limited-time-deal-on-the-archer-be550-nets-a-tri-band-router-with-fast-speeds-to-upgrade-your-home-network",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T12:20:00+00:00",
    "summary": "The TP-Link Archer BE550 Wi-Fi 7 router is on sale for a limited-time only, down to $169.99, netting you powerful kit with six antennas and five 2.5G Ethernet ports."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/save-usd50-on-elgatos-biggest-stream-deck-this-32-key-monster-macro-pad-is-now-down-to-usd199",
    "domain": "AI 算力 / 半导体",
    "title": "Save $50 on Elgato's biggest Stream Deck",
    "url": "https://www.tomshardware.com/peripherals/save-usd50-on-elgatos-biggest-stream-deck-this-32-key-monster-macro-pad-is-now-down-to-usd199",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T12:00:00+00:00",
    "summary": "Elgato's Stream Deck is enjoying a 20% discount at Amazon. Pick up the Stream Deck XL for just $199."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/micron-now-has-an-88-percent-margin-on-consumer-memory-price-hikes-drive-revenue-client-business-is-microns-only-unit-that-shipped-less-memory-this-quarter",
    "domain": "AI 算力 / 半导体",
    "title": "Micron now has an 88% margin on consumer memory as price hikes drive profits",
    "url": "https://www.tomshardware.com/pc-components/dram/micron-now-has-an-88-percent-margin-on-consumer-memory-price-hikes-drive-revenue-client-business-is-microns-only-unit-that-shipped-less-memory-this-quarter",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T11:40:00+00:00",
    "summary": "Micron's consumer business is its most profitable by margin according to the company's fiscal Q4 2026 financial report, despite shipping less memory in the quarter."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/micro-center-requires-photo-id-and-signed-no-export-pledge-to-buy-rtx-5090-gaming-gpu-buyer-forced-to-sign-declaration-disclosing-install-location-and-promise-gpu-will-remain-in-the-us",
    "domain": "AI 算力 / 半导体",
    "title": "Micro Center requires photo ID and signed no-export pledge to buy RTX 5090 gaming GPU",
    "url": "https://www.tomshardware.com/pc-components/gpus/micro-center-requires-photo-id-and-signed-no-export-pledge-to-buy-rtx-5090-gaming-gpu-buyer-forced-to-sign-declaration-disclosing-install-location-and-promise-gpu-will-remain-in-the-us",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T11:15:00+00:00",
    "summary": "The form requires RTX 5090 buyers to input their personal data before getting approved to make the purchase. However, it remains unclear how Micro Center can use this information to track illegally ex"
  },
  {
    "id": "rss:https://www.tomshardware.com/raspberry-pi/component-shortages-drive-raspberry-pi-prices-up-by-up-to-23-percent-escalating-lpddr4-lpddr5-costs-trigger-the-third-price-hike-of-the-year",
    "domain": "AI 算力 / 半导体",
    "title": "Component shortages drive Raspberry Pi prices up by up to 23%",
    "url": "https://www.tomshardware.com/raspberry-pi/component-shortages-drive-raspberry-pi-prices-up-by-up-to-23-percent-escalating-lpddr4-lpddr5-costs-trigger-the-third-price-hike-of-the-year",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T11:00:00+00:00",
    "summary": "Raspberry Pi announces price adjustments for the 2GB Raspberry Pi 4 and Raspberry Pi 5 models."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/pewdiepie-unveils-uncensored-ajax-ai-model-built-to-run-on-home-pcs-creator-says-openai-banned-him-twice-while-making-it",
    "domain": "AI 算力 / 半导体",
    "title": "PewDiePie unveils ‘uncensored’ Ajax AI model for home PCs",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/pewdiepie-unveils-uncensored-ajax-ai-model-built-to-run-on-home-pcs-creator-says-openai-banned-him-twice-while-making-it",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T10:30:00+00:00",
    "summary": "PewDiePie says OpenAI banned him twice while he made Ajax, a fine-tuned Qwen3.5-9B agent."
  },
  {
    "id": "rss:https://www.eetimes.com/qualcomm-doubles-down-on-agentic-ai-at-snapdragon-summit-2026/",
    "domain": "AI 算力 / 半导体",
    "title": "Qualcomm Doubles Down on Agentic AI at Snapdragon Summit 2026",
    "url": "https://www.eetimes.com/qualcomm-doubles-down-on-agentic-ai-at-snapdragon-summit-2026/",
    "source": "Jim McGregor, Francis Sideco",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T17:31:45+00:00",
    "summary": "Qualcomm introduced two distinct Snapdragon 8 Elite Gen 6 SoCs for high-end smartphones as it expands personal agentic AI across mobile, wearables, and PCs. The post Qualcomm Doubles Down on Agentic A"
  },
  {
    "id": "rss:https://www.eetimes.com/edge-computing-and-security-for-access-control-applications-getting-the-best-of-the-two-worlds/",
    "domain": "AI 算力 / 半导体",
    "title": "Edge Computing and Security for Access Control Applications: Getting the Best of the Two Worlds",
    "url": "https://www.eetimes.com/edge-computing-and-security-for-access-control-applications-getting-the-best-of-the-two-worlds/",
    "source": "Arrow Electronics, Microchip",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T14:01:12+00:00",
    "summary": "Join us where attendees will see how on-device processing improves resilience, reduces exposure of sensitive data, counters spoofing, and supports practical deployment across buildings, smart locks, v"
  },
  {
    "id": "rss:https://www.eetimes.com/pcba-test-strategies-how-to-select-the-right-methodology-and-tester/",
    "domain": "AI 算力 / 半导体",
    "title": "PCBA Test Strategies: How to Select the Right Methodology and Tester",
    "url": "https://www.eetimes.com/pcba-test-strategies-how-to-select-the-right-methodology-and-tester/",
    "source": "Francesca Pinto, SPEA Electronic Test Products Copywriter",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T13:00:00+00:00",
    "summary": "Are you struggling with PCBA defects? Learn how to optimize your PCBA testing strategy by combining In-Circuit Testing (ICT), Functional Testing (FCT with Bed-of-Nails or Flying Probe Testers. The pos"
  },
  {
    "id": "rss:https://www.eetimes.com/small-electronics-manufacturers-save-big-on-erp/",
    "domain": "AI 算力 / 半导体",
    "title": "Small Electronics Manufacturers Save Big on ERP",
    "url": "https://www.eetimes.com/small-electronics-manufacturers-save-big-on-erp/",
    "source": "MRPeasy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T13:00:00+00:00",
    "summary": "Instead of traditional ERP, small electronics manufacturers are finding that affordable SME-focused manufacturing software provides needed functionality. The post Small Electronics Manufacturers Save "
  },
  {
    "id": "rss:https://www.eetimes.com/europe-space-industry-seeks-greater-supply-chain-control/",
    "domain": "AI 算力 / 半导体",
    "title": "Europe’s Space Industry Seeks Greater Supply Chain Control",
    "url": "https://www.eetimes.com/europe-space-industry-seeks-greater-supply-chain-control/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T09:57:15+00:00",
    "summary": "Europe's strategic space independence will depend on semiconductor supply chains, satellite networks, and 6G communications. The post Europe’s Space Industry Seeks Greater Supply Chain Control appeare"
  },
  {
    "id": "rss:https://www.eetimes.com/emergence-ai-to-deploy-neuroformal-ai-with-fabless-chipmakers/",
    "domain": "AI 算力 / 半导体",
    "title": "Emergence AI Targets Fabless Chipmakers With Neuroformal AI",
    "url": "https://www.eetimes.com/emergence-ai-to-deploy-neuroformal-ai-with-fabless-chipmakers/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T21:31:25+00:00",
    "summary": "See how Emergence AI is deploying neuroformal AI with chipmakers to boost wafer yields and tackle fab, test, and packaging failures. The post Emergence AI Targets Fabless Chipmakers With Neuroformal A"
  },
  {
    "id": "rss:https://www.eetimes.com/tsmcs-3-nm-ramp-looks-different-in-historical-context/",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC’s 3-nm Ramp Looks Different in Historical Context",
    "url": "https://www.eetimes.com/tsmcs-3-nm-ramp-looks-different-in-historical-context/",
    "source": "Ron Honig",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T15:40:17+00:00",
    "summary": "TSMC’s 3-nm node nears the revenue lead, but history shows 7 nm ramped faster; compare the data before evaluating 2 nm. The post TSMC’s 3-nm Ramp Looks Different in Historical Context appeared first o"
  },
  {
    "id": "rss:https://www.eetimes.com/advanced-strategies-for-heat-exchanger-manufacturing-in-evs-thermal-management-systems/",
    "domain": "AI 算力 / 半导体",
    "title": "Advanced Strategies for Heat Exchanger Manufacturing in EVs & Thermal Management Systems",
    "url": "https://www.eetimes.com/advanced-strategies-for-heat-exchanger-manufacturing-in-evs-thermal-management-systems/",
    "source": "Solstice",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T13:42:54+00:00",
    "summary": "Join us to explore how Praziflux® is transforming brazing processes across the EV industry and other thermal management applications. The post Advanced Strategies for Heat Exchanger Manufacturing in E"
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
    "points": 1696,
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
    "id": "hn:49914236",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon (High): Intelligence, Performance and Price Analysis",
    "url": "https://artificialanalysis.ai/models/gemini-4-argon",
    "source": "theanonymousone",
    "platform": "hackernews",
    "points": 111,
    "published_at": "2026-09-30T20:50:28+00:00",
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
    "id": "hn:49942592",
    "domain": "大厂 AI 动态",
    "title": "Gemini ending free use of Flash and Pro models",
    "url": "https://www.reddit.com/r/GeminiAI/comments/1wwalmc/wtf_google_getting_rid_of_free_gemini_flash_and/",
    "source": "rjh29",
    "platform": "hackernews",
    "points": 57,
    "published_at": "2026-10-03T09:13:19+00:00",
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
    "id": "rss:https://www.theverge.com/games/1004418/capcom-ai-game-development",
    "domain": "大厂 AI 动态",
    "title": "Capcom is preparing for a ‘future where we create games together with AI’",
    "url": "https://www.theverge.com/games/1004418/capcom-ai-game-development",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T16:49:10+00:00",
    "summary": "Capcom's Pragmata might be all about the horrors of AI, but in practice the studio doesn't seem so down on the tech. During the Capcom Open Conference RE: 2026 programmer Satoshi Ishida gave a present"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/999447/best-early-amazon-prime-day-big-deals-sale-october",
    "domain": "大厂 AI 动态",
    "title": "The best early October Prime Day deals happening now",
    "url": "https://www.theverge.com/gadgets/999447/best-early-amazon-prime-day-big-deals-sale-october",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T16:22:40+00:00",
    "summary": "It’s not even October yet and Amazon is already offering some Prime Big Deal Day discounts on its own hardware, along with plenty of other popular products. It’s all to hype up October Prime Day, whic"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/1004162/splice-ceo-kakul-srivastava-ai-interview",
    "domain": "大厂 AI 动态",
    "title": "Splice CEO Kakul Srivastava thinks AI emails are killing conversations",
    "url": "https://www.theverge.com/entertainment/1004162/splice-ceo-kakul-srivastava-ai-interview",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T15:00:00+00:00",
    "summary": "Kakul Srivastava is the CEO of Splice, the sample platform countless producers rely on for one-shots and melodic loops. Samples pulled from the service have found their way into massive hits like Lisa"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1004408/openai-safety-quits-sounding-the-alarm",
    "domain": "大厂 AI 动态",
    "title": "An OpenAI safety employee has quit and is sounding the alarm",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1004408/openai-safety-quits-sounding-the-alarm",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T14:31:56+00:00",
    "summary": "David Robinson used to write the safety reports that accompanied every major model release at OpenAI. This week, he resigned from his position and is now speaking out in an editorial in The Atlantic. "
  },
  {
    "id": "rss:https://www.theverge.com/tech/1004131/3d-movies-are-finally-worth-watching-xreal-meta-glasses-vision-pro",
    "domain": "大厂 AI 动态",
    "title": "3D movies are finally worth watching",
    "url": "https://www.theverge.com/tech/1004131/3d-movies-are-finally-worth-watching-xreal-meta-glasses-vision-pro",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T12:00:00+00:00",
    "summary": "Why am I suddenly buying up every 3D Blu-ray I can find after 3D became one of the biggest tech flops of all time? The technology's finally ready for 3D movies to shine, more than 15 years since James"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1004330/meta-muse-ai-gadgets-home-link",
    "domain": "大厂 AI 动态",
    "title": "Meta open sources code to let you make Muse AI gadgets",
    "url": "https://www.theverge.com/tech/1004330/meta-muse-ai-gadgets-home-link",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T21:08:37+00:00",
    "summary": "Meta now lets you make your own Muse gadgets that feature the company's new AI agent with code that the company open sourced. The company suggests projects like loading Muse on a color E Ink display t"
  },
  {
    "id": "rss:https://www.theverge.com/streaming/1004323/netflix-david-fincher-shawn-levy-mike-flanagan-duffer-brothers-greta-gerwig",
    "domain": "大厂 AI 动态",
    "title": "Netflix is pivoting away from prestige",
    "url": "https://www.theverge.com/streaming/1004323/netflix-david-fincher-shawn-levy-mike-flanagan-duffer-brothers-greta-gerwig",
    "source": "Charles Pulliam-Moore",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T20:30:26+00:00",
    "summary": "Many of Netflix's biggest critically acclaimed hits have been the products of its multiyear production deals with noted directors like David Fincher and Shawn Levy. In the past few weeks, though, the "
  },
  {
    "id": "rss:https://www.theverge.com/tech/1004295/apple-limit-mac-disk-access-ai-agents",
    "domain": "大厂 AI 动态",
    "title": "Apple will limit Mac disk access as AI agents ‘substantially’ increase risk",
    "url": "https://www.theverge.com/tech/1004295/apple-limit-mac-disk-access-ai-agents",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T20:08:40+00:00",
    "summary": "Apple will add new limits for \"full disk access\" on Mac in response to risks posed by AI agents, as reported earlier by TechCrunch. In an update on Friday, Apple says it's rolling out new controls to "
  },
  {
    "id": "rss:https://www.theverge.com/streaming/1004300/sling-tv-pass-cable-drops",
    "domain": "大厂 AI 动态",
    "title": "Sling TV drops its one-day cable passes",
    "url": "https://www.theverge.com/streaming/1004300/sling-tv-pass-cable-drops",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T20:00:20+00:00",
    "summary": "Dish-owned Sling TV will no longer be offering its Sling Pass feature that allowed people to buy a single day of cable TV programming at a time, as reported by The Desk. The feature was announced last"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1004096/openai-chatgpt-dots-hands-on-agent",
    "domain": "大厂 AI 动态",
    "title": "OpenAI’s Dot agent is enterprise software that can also order your dinner",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1004096/openai-chatgpt-dots-hands-on-agent",
    "source": "Allison Johnson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T18:00:00+00:00",
    "summary": "It's a tale as old as last week: OpenAI's new agent platform, called Dots, is full of cute little guys who can do your bidding. But unlike the ultra-approachable Meta Muse, Dots feel very much like us"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/03/federal-judge-calls-flock-indiscriminate-mass-surveillance/",
    "domain": "大厂 AI 动态",
    "title": "Federal judge calls Flock ‘indiscriminate mass surveillance’",
    "url": "https://techcrunch.com/2026/10/03/federal-judge-calls-flock-indiscriminate-mass-surveillance/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T19:33:15+00:00",
    "summary": "A federal judge ruled that a sheriff’s deputy violated a woman’s Fourth Amendment rights when using Flock to search for her license plate without a warrant."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/03/amazon-responds-to-data-center-backlash-says-it-no-longer-uses-ndas/",
    "domain": "大厂 AI 动态",
    "title": "Amazon responds to data center backlash, says it no longer uses NDAs",
    "url": "https://techcrunch.com/2026/10/03/amazon-responds-to-data-center-backlash-says-it-no-longer-uses-ndas/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T18:43:57+00:00",
    "summary": "The CEO of Amazon Web Services tried to push back against widespread suspicion of data centers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/03/openai-safety-employee-resigns-claiming-the-companys-culture-is-broken/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI safety employee resigns, claiming the company’s ‘culture is broken’",
    "url": "https://techcrunch.com/2026/10/03/openai-safety-employee-resigns-claiming-the-companys-culture-is-broken/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T16:30:01+00:00",
    "summary": "By his own admission, David Robinson is “something of a cliché”: an employee at a leading AI company who issues a dire warning while resigning from their job."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/03/jack-dorseys-bitchat-disappears-from-app-stores-in-india-after-government-order/",
    "domain": "大厂 AI 动态",
    "title": "Jack Dorsey’s Bitchat disappears from app stores in India after government order",
    "url": "https://techcrunch.com/2026/10/03/jack-dorseys-bitchat-disappears-from-app-stores-in-india-after-government-order/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T15:02:01+00:00",
    "summary": "Bitchat has become largely unavailable in India as a result of the restrictions."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/03/vessev-built-an-electric-ferry-that-almost-flies/",
    "domain": "大厂 AI 动态",
    "title": "Vessev built an electric ferry that almost flies",
    "url": "https://techcrunch.com/2026/10/03/vessev-built-an-electric-ferry-that-almost-flies/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T14:42:00+00:00",
    "summary": "Vessev hopes its electric hydrofoil ferry will change the way people and cities think about boats."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/03/all-the-ai-agents-that-can-live-in-your-text-messages/",
    "domain": "大厂 AI 动态",
    "title": "All the AI agents that can live in your text messages",
    "url": "https://techcrunch.com/2026/10/03/all-the-ai-agents-that-can-live-in-your-text-messages/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T14:00:00+00:00",
    "summary": "We created a list of the most notable AI agents that can live in your text messages, from general assistants to agents designed for families, travel, and work."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/03/spotify-billionaires-body-scan-startup-has-come-to-america/",
    "domain": "大厂 AI 动态",
    "title": "Spotify billionaire’s body scan startup has come to America",
    "url": "https://techcrunch.com/2026/10/03/spotify-billionaires-body-scan-startup-has-come-to-america/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T14:00:00+00:00",
    "summary": "Farooq Abbasi, an investor in Neko Health, talked to Equity about the hot health tech company and what's next for it."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/02/meta-wants-you-to-build-your-own-muse-gadget/",
    "domain": "大厂 AI 动态",
    "title": "Meta wants your next gadget to be Muse-infused",
    "url": "https://techcrunch.com/2026/10/02/meta-wants-you-to-build-your-own-muse-gadget/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T00:45:39+00:00",
    "summary": "Meta wants Muse in your TV and your toaster, so it's giving the code away for free."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/02/sanders-introduces-bill-to-ban-the-federal-government-from-using-flock/",
    "domain": "大厂 AI 动态",
    "title": "Sanders introduces bill to ban the federal government from using Flock",
    "url": "https://techcrunch.com/2026/10/02/sanders-introduces-bill-to-ban-the-federal-government-from-using-flock/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T00:21:57+00:00",
    "summary": "The proposed legislation would extend to all automotica license plate readers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/02/sean-parker-is-rebuilding-stability-ai-around-music/",
    "domain": "大厂 AI 动态",
    "title": "Sean Parker is rebuilding Stability AI around music",
    "url": "https://techcrunch.com/2026/10/02/sean-parker-is-rebuilding-stability-ai-around-music/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T21:09:14+00:00",
    "summary": "Sean Parker, who once taught the music industry what asking for forgiveness looks like, is now back with the labels' blessing and money."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/02/disrupt-2026-layoff-expo-plus-passes-available-for-75-dollars/",
    "domain": "大厂 AI 动态",
    "title": "Affected by layoffs? Don’t miss this $75 deal for your TechCrunch Disrupt 2026 Expo+ Pass",
    "url": "https://techcrunch.com/2026/10/02/disrupt-2026-layoff-expo-plus-passes-available-for-75-dollars/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T19:15:51+00:00",
    "summary": "Your next opportunity could be one conversation away. Get your Expo+ Pass for just $75. Limited to the first 100 qualifying people."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/02/apple-says-its-tightening-macos-full-disk-access-controls-due-to-new-risks-from-ai-agents/",
    "domain": "大厂 AI 动态",
    "title": "Apple says it’s tightening macOS ‘Full Disk Access’ controls due to new risks from AI agents",
    "url": "https://techcrunch.com/2026/10/02/apple-says-its-tightening-macos-full-disk-access-controls-due-to-new-risks-from-ai-agents/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T18:11:27+00:00",
    "summary": "Apple says it will add new controls around macOS’s Full Disk Access permission, warning that increasingly capable AI agents make broad access to users’ files, messages, mail, and browsing history risk"
  },
  {
    "id": "rss:https://techcrunch.com/video/its-not-ai-anymore-its-super-intelligence-according-to-the-white-house/",
    "domain": "大厂 AI 动态",
    "title": "It’s not AI anymore, it’s ‘super intelligence’ (according to the White House)",
    "url": "https://techcrunch.com/video/its-not-ai-anymore-its-super-intelligence-according-to-the-white-house/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T17:48:16+00:00",
    "summary": "This week, the White House got&#160;nearly every&#160;major tech CEO in one room — Zuckerberg, Bezos, Musk, and Anthropic’s Dario Amodei among them —&#160;to sign an AI safety pledge&#160;that Preside"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/02/techcrunch-disrupt-2026-blackstones-jas-khaira-on-building-the-next-generation-of-ai-giants/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Disrupt 2026: Blackstone’s Jas Khaira on building the next generation of AI giants",
    "url": "https://techcrunch.com/2026/10/02/techcrunch-disrupt-2026-blackstones-jas-khaira-on-building-the-next-generation-of-ai-giants/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T17:32:05+00:00",
    "summary": "Blackstone's Jas Khaira will take the Builders Stage at TechCrunch Disrupt 2026 on building next-gen AI. Register for your pass and get 50% off a second."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/02/circuit-breaker-labs-hopes-to-make-ai-safer-for-your-kids-and-you/",
    "domain": "大厂 AI 动态",
    "title": "Circuit Breaker Labs hopes to make AI safer for your kids (and you)",
    "url": "https://techcrunch.com/2026/10/02/circuit-breaker-labs-hopes-to-make-ai-safer-for-your-kids-and-you/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T17:00:00+00:00",
    "summary": "With all the talk about how AI might one day kill us all, it's easy to forget that AI has already harmed some people psychologically. Circuit Breaker Labs has created \"crash-test dummies\" to solve tha"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/02/paramount-and-warner-bros-discovery-to-become-skydance/",
    "domain": "大厂 AI 动态",
    "title": "Paramount and Warner Bros. Discovery to become Skydance",
    "url": "https://techcrunch.com/2026/10/02/paramount-and-warner-bros-discovery-to-become-skydance/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T15:53:50+00:00",
    "summary": "The roughly $110 billion deal is expected to close October 6."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/02/pope-leo-xiv-is-not-a-fan-of-ai-generated-art/",
    "domain": "大厂 AI 动态",
    "title": "Pope Leo XIV is not a fan of AI-generated art",
    "url": "https://techcrunch.com/2026/10/02/pope-leo-xiv-is-not-a-fan-of-ai-generated-art/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T15:39:41+00:00",
    "summary": "\"There is an ontological difference, even before an aesthetic one, between art and what a machine can generate through statistical calculation based on millions of images created by others,\" the pope "
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/02/laytrs-new-app-lets-you-save-anything-you-find-online-not-just-articles-to-read/",
    "domain": "大厂 AI 动态",
    "title": "Laytr’s new app lets you save anything you find online, not just articles to read",
    "url": "https://techcrunch.com/2026/10/02/laytrs-new-app-lets-you-save-anything-you-find-online-not-just-articles-to-read/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T15:31:20+00:00",
    "summary": "Laytr lets you save articles, recipes, screenshots, videos, PDFs, and more for later, while keeping your archive private and synced across your Apple devices."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/02/slovenias-si-domain-sees-a-surge-in-registrations-after-trumps-super-intelligence-order/",
    "domain": "大厂 AI 动态",
    "title": "Slovenia’s .si domain sees a surge in registrations after Trump’s ‘super intelligence’ order",
    "url": "https://techcrunch.com/2026/10/02/slovenias-si-domain-sees-a-surge-in-registrations-after-trumps-super-intelligence-order/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T14:47:46+00:00",
    "summary": "The .si domain name is seeing unprecedented demand after President Trump's super intelligence executive order."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/02/techcrunch-disrupt-2026-clays-kareem-amin-on-the-rise-of-the-gtm-engineer/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Disrupt 2026: Clay’s Kareem Amin on the rise of the GTM engineer",
    "url": "https://techcrunch.com/2026/10/02/techcrunch-disrupt-2026-clays-kareem-amin-on-the-rise-of-the-gtm-engineer/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T14:30:00+00:00",
    "summary": "Clay Co-founder and CEO Kareem Amin joins the AI Stage to discuss the rise of GTM engineer at TechCrunch Disrupt 2026. Register for your ticket and get a second pass at 50% off."
  },
  {
    "id": "rss:https://stratechery.com/2026/dots-and-question-marks/",
    "domain": "大厂 AI 动态",
    "title": "2026.40: Dots and Question Marks",
    "url": "https://stratechery.com/2026/dots-and-question-marks/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T17:00:00+00:00",
    "summary": "The best Stratechery content from the week of September 28, 2026, including Meta's focus, what OpenAI is doing, and Mao and NBA Media Day."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/10/milt-windler-nasa-flight-director-who-helped-save-apollo-13-dies-at-94/",
    "domain": "大厂 AI 动态",
    "title": "Milt Windler, NASA flight director who helped save Apollo 13, dies at 94",
    "url": "https://arstechnica.com/space/2026/10/milt-windler-nasa-flight-director-who-helped-save-apollo-13-dies-at-94/",
    "source": "Robert Pearlman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T19:45:17+00:00",
    "summary": "\"...we were making history.\""
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/10/the-dawn-of-the-age-of-the-exoskeleton/",
    "domain": "大厂 AI 动态",
    "title": "The dawn of the age of the exoskeleton",
    "url": "https://arstechnica.com/science/2026/10/the-dawn-of-the-age-of-the-exoskeleton/",
    "source": "Ildar Farkhatdinov, The Conversation",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T11:15:33+00:00",
    "summary": "The devices continue to show noticeable benefits for users in various real-world tasks."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/10/apple-changes-full-disk-access-permissions-to-curb-abuse-from-ai-agents/",
    "domain": "大厂 AI 动态",
    "title": "Apple changes full-disk access permissions to curb abuse from AI agents",
    "url": "https://arstechnica.com/security/2026/10/apple-changes-full-disk-access-permissions-to-curb-abuse-from-ai-agents/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T23:03:16+00:00",
    "summary": "Meta says FDA isn't sufficient to Muse reading messages. Apple begs to differ."
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
    "id": "hn:49930086",
    "domain": "股票",
    "title": "US tells France and Germany to release diesel stocks or face US export ban",
    "url": "https://www.reuters.com/business/energy/us-tells-france-germany-release-diesel-stocks-or-face-us-export-ban-sources-say-2026-10-01/",
    "source": "geox",
    "platform": "hackernews",
    "points": 97,
    "published_at": "2026-10-02T05:22:20+00:00",
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
    "id": "hn:49875913",
    "domain": "金融",
    "title": "Parley: Federated, decentralised chat that speaks plain IRC",
    "url": "https://git.mills.io/prologic/parley",
    "source": "davidcollantes",
    "platform": "hackernews",
    "points": 328,
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
    "points": 255,
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
    "points": 160,
    "published_at": "2026-09-30T04:37:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:49916668",
    "domain": "金融",
    "title": "10-year Treasury yield climbs above 5.3% to a level not seen in 24 years",
    "url": "https://www.wsj.com/finance/investing/surging-yields-bring-the-bond-market-back-to-the-turn-of-the-century-2b74773f",
    "source": "kaycebasques",
    "platform": "hackernews",
    "points": 122,
    "published_at": "2026-10-01T01:40:50+00:00",
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
    "id": "hn:49916955",
    "domain": "金融",
    "title": "Cities Are Forced to Funnel License Plate Data to a Federal Surveillance Program",
    "url": "https://www.404media.co/how-cities-are-forced-to-funnel-license-plate-data-to-a-massive-federal-surveillance-program-hidta/",
    "source": "ripe",
    "platform": "hackernews",
    "points": 92,
    "published_at": "2026-10-01T02:26:17+00:00",
    "summary": ""
  },
  {
    "id": "hn:49938815",
    "domain": "金融",
    "title": "Federal Judge Rules a Flock Search Was Unconstitutional",
    "url": "https://www.404media.co/federal-judge-rules-a-flock-search-was-indiscriminate-mass-surveillance-and-unconstitutional/",
    "source": "pavel_lishin",
    "platform": "hackernews",
    "points": 51,
    "published_at": "2026-10-02T21:28:59+00:00",
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
    "id": "hn:49924299",
    "domain": "金融",
    "title": "Sony released the first CD audio player on this day in 1982",
    "url": "https://www.tomshardware.com/pc-components/storage/sony-released-the-first-cd-audio-player-on-this-day-in-1982-player-cost-usd3-700-when-adjusted-for-inflation-but-it-would-be-another-decade-before-the-cd-rom-driven-multimedia-pc-era-began",
    "source": "Brajeshwar",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-10-01T17:07:39+00:00",
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
    "id": "hn:49769668",
    "domain": "金融",
    "title": "OpenAI and Anthropic oversold AI security breaches",
    "url": "https://nypost.com/2026/09/19/us-news/openai-anthropic-oversold-security-breaches-to-pressure-feds-into-protecting-turf-insiders/",
    "source": "hei-lima",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-09-19T19:59:28+00:00",
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
    "id": "hn:49828019",
    "domain": "金融",
    "title": "Show HN: Trader News – Hacker News for Finance",
    "url": "https://news.ycombinator.com/item?id=49828019",
    "source": "FailMore",
    "platform": "hackernews",
    "points": 26,
    "published_at": "2026-09-24T08:54:57+00:00",
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
    "id": "hn:49645186",
    "domain": "金融",
    "title": "Streaming Is Raising Prices Faster Than Cable Ever Did",
    "url": "https://www.hollywoodreporter.com/business/business-news/streaming-inflation-raising-prices-cable-1236691404/",
    "source": "robtherobber",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-09-10T15:15:11+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://semianalysis.com/2025/09/16/xais-colossus-2-first-gigawatt-datacenter/",
    "domain": "电子信息与芯片",
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
    "domain": "电子信息与芯片",
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
    "domain": "电子信息与芯片",
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
    "domain": "电子信息与芯片",
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
    "domain": "电子信息与芯片",
    "title": "H100 vs GB200 NVL72 Training Benchmarks – Power, TCO, and Reliability Analysis, Software Improvement Over Time",
    "url": "https://semianalysis.com/2025/08/20/h100-vs-gb200-nvl72-training-benchmarks/",
    "source": "Dylan Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2025-08-20T04:56:35+00:00",
    "summary": "Frontier model training has pushed GPUs and AI systems to their absolute limits, making cost, efficiency, power, performance per TCO, and reliability central to the discussion on effective training. T"
  },
  {
    "id": "rss:https://semianalysis.com/2025/08/13/gpt-5-ad-monetization-and-the-superapp/",
    "domain": "电子信息与芯片",
    "title": "GPT-5 Set the Stage for Ad Monetization and the SuperApp",
    "url": "https://semianalysis.com/2025/08/13/gpt-5-ad-monetization-and-the-superapp/",
    "source": "Doug OLaughlin",
    "platform": "rss",
    "points": null,
    "published_at": "2025-08-13T00:27:14+00:00",
    "summary": "To many power users (Pro and Plus), GPT5 was a disappointing release. But with closer inspection, the real release is focused on the vast majority of ChatGPT’s users, which is the 700m+ free userbase "
  },
  {
    "id": "rss:https://semianalysis.com/2025/08/12/scaling-the-memory-wall-the-rise-and-roadmap-of-hbm/",
    "domain": "电子信息与芯片",
    "title": "Scaling the Memory Wall: The Rise and Roadmap of HBM",
    "url": "https://semianalysis.com/2025/08/12/scaling-the-memory-wall-the-rise-and-roadmap-of-hbm/",
    "source": "Dylan Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2025-08-12T01:16:06+00:00",
    "summary": "The first portion of this report will explain HBM, the manufacturing process, dynamics between vendors, KVCache offload, disaggregated prefill decode, and wide / high-rank EP. The rest of the report w"
  },
  {
    "id": "rss:https://semianalysis.com/2025/07/30/robotics-levels-of-autonomy/",
    "domain": "电子信息与芯片",
    "title": "Robotics Levels of Autonomy",
    "url": "https://semianalysis.com/2025/07/30/robotics-levels-of-autonomy/",
    "source": "Reyk Knuhtsen",
    "platform": "rss",
    "points": null,
    "published_at": "2025-07-30T17:02:25+00:00",
    "summary": "Robots have powered manufacturing for decades, yet they stayed single-purpose and thrived only in perfect settings. Previous attempts at intelligent machines overpromised and underdelivered. But they "
  },
  {
    "id": "rss:https://semianalysis.com/2025/07/21/vlsi2025/",
    "domain": "电子信息与芯片",
    "title": "Intel 18A Details & Cost, Future of DRAM 4F2 vs 3D, Backside Power Adoption (or Not), China’s FlipFET, Digital Twins from Atoms to Fabs, and More",
    "url": "https://semianalysis.com/2025/07/21/vlsi2025/",
    "source": "Dylan Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2025-07-21T14:23:37+00:00",
    "summary": "Long time readers will recall that SemiAnalysis covers more than just datacenters and AMD. Today we’re back to semiconductors with a tech-focused roundup of the best from this year’s VLSI conference, "
  },
  {
    "id": "rss:https://semianalysis.com/2025/07/11/meta-superintelligence-leadership-compute-talent-and-data/",
    "domain": "电子信息与芯片",
    "title": "Meta Superintelligence – Leadership Compute, Talent, and Data",
    "url": "https://semianalysis.com/2025/07/11/meta-superintelligence-leadership-compute-talent-and-data/",
    "source": "Dylan Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2025-07-11T20:12:19+00:00",
    "summary": "Meta’s shocking purchase of 49% of Scale AI at a ~$30B valuation shows that money is of no concern for the $100B annual cashflow ad machine. Despite seemingly unlimited resources, Meta has been fallin"
  }
]
```
