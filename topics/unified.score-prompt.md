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

- 今日日期：`2026-10-19`
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
  "date": "2026-10-19",
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
    "points": 2333865,
    "published_at": "2026-08-14T11:56:52+00:00",
    "summary": "DeepSeek Harness 保姆级教程，1个视频带你从安装到实战玩转 DeepSeek 最新开源的 AI 编程工具，小白也能学会，看完就知道《国产版 Codex》到底有多强。\n编程学习教程+实战项目+简历模板：codefather.cn\n免费 AI 编程教程：github.com/liyupi/ai-guide\n视频从安装开始，手把手教你配置 DeepSeek Harness，然后用 Dee"
  },
  {
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "8分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 1993116,
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
    "points": 1412924,
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
    "points": 1361196,
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
    "points": 1229886,
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
    "points": 901586,
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
    "points": 861462,
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
    "points": 721464,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1rBRQBSEwB",
    "domain": "AI",
    "title": "Claude Code+DeepSeek V4 Pro安装教程｜3步从零装好开始用 | Mac Windows",
    "url": "http://www.bilibili.com/video/av116543199385810",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 429793,
    "published_at": "2026-05-09T10:10:00+00:00",
    "summary": "上期vibe coding零基础教程10万多人看了，私信和评论里问最多的居然不是怎么写需求。\n 而是Claude Code怎么装？DeepSeek怎么接进去？🫣\n\n所以这期作为补丁教程，专门帮大家搞定这3件事：\n 1️⃣ 安装Claude Code\n 2️⃣ 把DeepSeek V4 Pro百万上下文满血版接入Claude Code\n 3️⃣ 在VS Code里正式用起来\n\nMac和Windows"
  },
  {
    "id": "bvid:BV1AnQNYxEsy",
    "domain": "AI",
    "title": "MCP是啥？技术原理是什么？一个视频搞懂MCP的一切。Windows系统配置MCP，Cursor Cline使用MCP",
    "url": "http://www.bilibili.com/video/av114155298228756",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 425254,
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
    "points": 325623,
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
    "points": 309482,
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
    "points": 289950,
    "published_at": "2026-08-17T10:10:51+00:00",
    "summary": "欢迎大家来到鹏哥课堂！这份DeepSeek Harness教程专为零基础小白打造，全程手把手演示安装、启动Web界面、模型接入、基础任务实操。 很多小白卡在环境配置、命令报错、参数设置，本教程能让你避开各种坑，跟着操作就能成功运行。 搞懂 Agent = 模型 + Harness，让 AI 读写文件、执行命令、自主完成项目任务。本教程适合程序员、AI 爱好者及想上手本地智能体的同学等。希望大家把视"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 281014,
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
    "points": 209806,
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
    "points": 184091,
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
    "points": 162916,
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
    "points": 160026,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV11XHQ65E6K",
    "domain": "AI",
    "title": "一个人有四种身份，我给电脑配了一个AI管家",
    "url": "http://www.bilibili.com/video/av117404021626807",
    "source": "三太子敖丙",
    "platform": "bilibili",
    "points": 140531,
    "published_at": "2026-10-08T09:40:00+00:00",
    "summary": "一台电脑，同时装着我的大厂程序员、自媒体博主、运动爱好者和普通生活四种状态。与其继续堆软件，我更想知道：把电脑状态、本地文件、网页任务和离开电脑后的接力都交给同一个AI管家，它到底管不管得明白？这次直接用真实任务测试Marvis。"
  },
  {
    "id": "bvid:BV1kGo6BdEsT",
    "domain": "AI",
    "title": "如何用Claude Skill 做高质量 PPT（附完整教程）",
    "url": "http://www.bilibili.com/video/av116474832361424",
    "source": "阿西_出海",
    "platform": "bilibili",
    "points": 102597,
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
    "points": 94082,
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
    "points": 67834,
    "published_at": "2026-07-26T01:30:00+00:00",
    "summary": "模组：Numen\n项目地址：https://github.com/Dwinovo/minecraft-numen"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operit教程：入门安卓最强大ai平台operitAI",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 67799,
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
    "points": 58941,
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
    "points": 56156,
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
    "points": 49394,
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
    "points": 40693,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29844,
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
    "points": 29002,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV126pk6sETS",
    "domain": "AI",
    "title": "连 json都不会，进了福布斯团队。面试的时候才知道vibe coding是什么，两天后他给我发了offer。",
    "url": "http://www.bilibili.com/video/av117436686795057",
    "source": "揽星Celeste",
    "platform": "bilibili",
    "points": 25975,
    "published_at": "2026-10-14T01:35:05+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22815,
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
    "points": 22429,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1sQaL6vEkb",
    "domain": "AI",
    "title": "小白向，ai入门第一课：agent的部署和使用！",
    "url": "http://www.bilibili.com/video/av117349378166797",
    "source": "沈三殊",
    "platform": "bilibili",
    "points": 21852,
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
    "points": 16203,
    "published_at": "2026-10-02T09:25:00+00:00",
    "summary": "本套教程专门为零基础学员而制，全程干货无废话，喜欢的小伙伴记得点赞三连喔 ~"
  },
  {
    "id": "bvid:BV153pf6JEeS",
    "domain": "AI",
    "title": "躺在床上玩Hermes，我的手机都装了哪些APP",
    "url": "http://www.bilibili.com/video/av117430797994289",
    "source": "小柚与籽鼠",
    "platform": "bilibili",
    "points": 14876,
    "published_at": "2026-10-13T00:37:54+00:00",
    "summary": "分享下我是怎么用手机玩转 Hermes 的\nAgent兴趣交流Q群：1129458085"
  },
  {
    "id": "bvid:BV18KJX6mEiH",
    "domain": "AI",
    "title": "太炸裂了！Claude Code 3.0彻底杀疯了！",
    "url": "http://www.bilibili.com/video/av117450007911196",
    "source": "烟神殿殿主",
    "platform": "bilibili",
    "points": 14125,
    "published_at": "2026-10-16T10:04:56+00:00",
    "summary": "原视频链接：https://www.youtube.com/watch?v=8nh1dcH4uJU\n本视频为AI技术搬运翻译，使用AI智能移除原视频广告营销内容，旨在降低信息差，帮助大家了解海外最新AI动态。\n翻译：烟神殿API,模型gemini-3.8-flash\n配音：使用的时FishTTS官方接口配音"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 12779,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
  },
  {
    "id": "bvid:BV1Vd8i6iEjd",
    "domain": "AI",
    "title": "AI办公实战课，AI助力工作学习效率提升N倍--从提示词、写作到数据分析与 AI 绘画，一课打通",
    "url": "http://www.bilibili.com/video/av117132901815801",
    "source": "1620谷爱凌",
    "platform": "bilibili",
    "points": 12156,
    "published_at": "2026-08-21T10:04:22+00:00",
    "summary": "AI办公实战课，AI助力工作学习效率提升N倍--从提示词、写作到数据分析与 AI 绘画，一课打通"
  },
  {
    "id": "bvid:BV17NJS6QEfE",
    "domain": "AI",
    "title": "Vibe Coding 有哪些高效的做法习惯？",
    "url": "http://www.bilibili.com/video/av117447894045979",
    "source": "AAA话题批发",
    "platform": "bilibili",
    "points": 11548,
    "published_at": "2026-10-16T01:30:00+00:00",
    "summary": "随着 AI 编程 Agent 普及，Vibe Coding 已经成为很多开发者的日常工作方式。不少人把精力耗费在打磨各种花式提示词上，但实际项目中经常遇到 Token 消耗爆炸、Agent 找不准代码、结果不稳定、大量人工兜底的问题。这篇文章结合多项行业实验与大厂内部项目实践，跳出提示词技巧，分享 Vibe Coding 真正高效的工作习惯与项目配置思路。\n文章开篇借助真实工程实验案例，展示合理拆"
  },
  {
    "id": "bvid:BV1Yhb66LEaF",
    "domain": "AI",
    "title": "3分钟，教你什么是vibe coding",
    "url": "http://www.bilibili.com/video/av117115000524101",
    "source": "开聊pro",
    "platform": "bilibili",
    "points": 9704,
    "published_at": "2026-08-18T06:12:25+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1bBHm6MEG5",
    "domain": "AI",
    "title": "这绝对是b站讲的最好的Claude Code全套实战教程，手把手带你搞定国内环境安装配置，全程干货无废话！AI大模型/MCP/Skill/智能体/Agent",
    "url": "http://www.bilibili.com/video/av117402847155229",
    "source": "大模型饼饼",
    "platform": "bilibili",
    "points": 9482,
    "published_at": "2026-10-08T02:13:21+00:00",
    "summary": "这绝对是B站讲得最好的Claude Code全套实战教程！手把手带你搞定国内环境安装配置、基础操作、高阶实战技巧，课程不堆砌冗余理论，聚焦真实开发场景，带你吃透Claude Code核心能力，打通MCP、Skill与Agent智能体联动开发。不管你是想提升日常编码效率，还是入门AI智能体开发，这套教程都非常适合你，全程干货无废话！"
  },
  {
    "id": "bvid:BV11LWw6VEHW",
    "domain": "AI",
    "title": "Agent-native 开发 [08-Raw/26生成式软件工程/NJU]",
    "url": "http://www.bilibili.com/video/av117432811260250",
    "source": "绿导师原谅你了",
    "platform": "bilibili",
    "points": 9387,
    "published_at": "2026-10-13T09:10:24+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1aSR4BKESW",
    "domain": "AI",
    "title": "安卓手机部署Claude Code",
    "url": "http://www.bilibili.com/video/av116526891993752",
    "source": "中国小骑士",
    "platform": "bilibili",
    "points": 8171,
    "published_at": "2026-05-06T09:24:14+00:00",
    "summary": "通过Termux安装Claude Code并且接入国内大模型"
  },
  {
    "id": "bvid:BV1aMAczmEmf",
    "domain": "AI",
    "title": "[MoonPack]在布吉岛里注入模组-mcp",
    "url": "http://www.bilibili.com/video/av116264966163402",
    "source": "DanciestZebra70",
    "platform": "bilibili",
    "points": 7472,
    "published_at": "2026-03-21T03:13:25+00:00",
    "summary": "交流群\n①1051043310\n②365233792"
  },
  {
    "id": "bvid:BV1UaYK6nEjP",
    "domain": "AI",
    "title": "【cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av117244419903051",
    "source": "茶子兀",
    "platform": "bilibili",
    "points": 6783,
    "published_at": "2026-09-10T02:39:36+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1WkJY6HErU",
    "domain": "AI",
    "title": "【AI值得看】GPT-6 Astra Pro 升级｜Claude 写九成 Claude Code，谁来审｜Gemini 打通我的世界",
    "url": "http://www.bilibili.com/video/av117453497566792",
    "source": "kate人不错",
    "platform": "bilibili",
    "points": 6659,
    "published_at": "2026-10-17T00:50:36+00:00",
    "summary": "1️⃣ OpenAI：ChatGPT 里的 GPT-6 Astra Pro 升级，回复更快，插件和工具用得更好，多个智能体可并行干活\n2️⃣ Claude Code：每轮对话先用 gzip 压缩再送到模型，回复更快\n3️⃣ Claude Slides：Boris Cherny 现在用它做幻灯片，在截图上留言就能自动套上 iPhone 边框\n4️⃣ Grok Bot 更新：八条帖子，重点三件事，电脑"
  },
  {
    "id": "bvid:BV1wFpP6uE1s",
    "domain": "AI",
    "title": "【开源】让手机自己操作 App！手上的 ai Agent！GitHub开源安卓App推荐",
    "url": "http://www.bilibili.com/video/av117394643097499",
    "source": "补药满减哇",
    "platform": "bilibili",
    "points": 6096,
    "published_at": "2026-10-07T01:05:00+00:00",
    "summary": "开源安卓 AI Agent：RikkaHub Agent Pure\n它能「看懂」屏幕、自己操作各种 App，也能组队干活。\n\n⬇️ 下载 &amp; 源码（AGPL-3.0）\nhttps://github.com/wuyhong715/rikkahub-agent-pure\n\n▶ 本片讲两件事\n① 无障碍屏幕自动化：读控件树定位、实时决策，不是死坐标脚本\n② 专家团系统：每个专家有自己的模型/工具"
  },
  {
    "id": "bvid:BV1dtn36LELi",
    "domain": "AI",
    "title": "【我的世界】24小时在线的MC服务器，居然只要1分钱？！",
    "url": "http://www.bilibili.com/video/av117461517141074",
    "source": "成都荒坂网络有限公司",
    "platform": "bilibili",
    "points": 5983,
    "published_at": "2026-10-18T10:51:31+00:00",
    "summary": "🎮 24小时在线的MC服务器，只要1分钱？！\n还在用自己的电脑开 Minecraft 服务器？电脑一关，朋友就没法继续玩了？\n现在只需要 0.01元，就有机会体验一个月的 Minecraft 云服务器！\n✅ 24小时在线，无需自己电脑挂机\n✅ 支持 Minecraft Java 版开服\n✅ 适合朋友联机、生存服、小型 SMP\n✅ 原价仅需 5元/月\n✅ 关注店铺领取5元优惠券，券后低至0.01元！"
  },
  {
    "id": "bvid:BV1AWpn6oEf1",
    "domain": "AI",
    "title": "z1yr mcp【MCP二改开源】新版本发布｜附链接",
    "url": "http://www.bilibili.com/video/av117422728153553",
    "source": "XiaozhumIOvO",
    "platform": "bilibili",
    "points": 5978,
    "published_at": "2026-10-11T14:27:42+00:00",
    "summary": "本 z1yr mcp 属于二改版本，并非原创，基于原作者开源项目进行二次修改、优化与新增功能，原项目遵守对应的开源协议；本二次修改版同样继续沿用原开源协议进行开源。本程序仅为《我的世界》基岩版的客户端模组，不是外挂，仅用于单机离线环境、私人局域网内部的技术研究、模组开发测试与学习演示用途。\n下载链接:https://wwbhw.lanzouq.com/b01gicrceh\n密码:9178"
  },
  {
    "id": "bvid:BV1qNHE6MEqS",
    "domain": "AI",
    "title": "【附链接】全局注入mcp教程[仅root用户]",
    "url": "http://www.bilibili.com/video/av117382597118755",
    "source": "XiaozhumIOvO",
    "platform": "bilibili",
    "points": 4450,
    "published_at": "2026-10-04T12:19:07+00:00",
    "summary": "https://wwbhw.lanzouq.com/b01gicrceh\n密码:9178"
  },
  {
    "id": "hn:50008187",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI annualised revenues $20B less than previously signalled",
    "url": "https://www.cnbc.com/2026/10/08/open-ai-revenue-nvidia-oracle-coreweave.html",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 433,
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
    "points": 179,
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
    "id": "rss:https://www.eetimes.com/from-macro-to-micro-and-back/",
    "domain": "AI 算力 / 半导体",
    "title": "From Macro to Micro, and Back",
    "url": "https://www.eetimes.com/from-macro-to-micro-and-back/",
    "source": "Moshe Zalcberg",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T08:19:07+00:00",
    "summary": "This year’s Nobel prizes explained large systems through their smallest parts. What can chip design learn from them, and can AI help us design in the other direction too? The post From Macro to Micro,"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/amd-cards-now-run-all-dlss-features-thanks-to-one-developers-project-plans-to-match-native-nvidia-gpu-performance",
    "domain": "AI 算力 / 半导体",
    "title": "Modder brings full Nvidia DLSS 5 suite to three generations of AMD gaming GPUs",
    "url": "https://www.tomshardware.com/pc-components/gpus/amd-cards-now-run-all-dlss-features-thanks-to-one-developers-project-plans-to-match-native-nvidia-gpu-performance",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T16:03:01+00:00",
    "summary": "Radeon GPUs get the full DLSS experience as solo project ports all the DLSS features for RDNA2-4 GPUs."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/anycubics-award-winning-3d-printer-hits-all-time-low-pricing-kobra-x-is-an-excellent-entry-level-four-color-printer-thats-now-just-usd299-99-for-amazon-prime-members",
    "domain": "AI 算力 / 半导体",
    "title": "Anycubic's award-winning 3D printer hits all-time low pricing",
    "url": "https://www.tomshardware.com/3d-printing/anycubics-award-winning-3d-printer-hits-all-time-low-pricing-kobra-x-is-an-excellent-entry-level-four-color-printer-thats-now-just-usd299-99-for-amazon-prime-members",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T15:24:22+00:00",
    "summary": "The Editor's Choice Anycubic Kobra X Multicolor 3D Printer is at the lowest price we've ever seen."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/f-22-raptor-pilot-successfully-demonstrates-command-of-wingman-fighter-drone-in-simulated-combat-anduril-yfq-44a-fury-test-advances-usafs-program-to-integrate-uncrewed-aircraft-into-fighter-squadrons",
    "domain": "AI 算力 / 半导体",
    "title": "F-22 Raptor pilot successfully demonstrates command of 'wingman' fighter drone in simulated combat",
    "url": "https://www.tomshardware.com/tech-industry/drones/f-22-raptor-pilot-successfully-demonstrates-command-of-wingman-fighter-drone-in-simulated-combat-anduril-yfq-44a-fury-test-advances-usafs-program-to-integrate-uncrewed-aircraft-into-fighter-squadrons",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T15:02:19+00:00",
    "summary": "The USAF's latest test proves that an F-22 Raptor can command a YFQ-44A Fury drone in combat conditions."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/overclocking/cinebench-world-record-that-stood-for-12-years-gets-toppled-oc-expert-scores-10-8cb-in-cinebench-r11-5-using-an-intel-core-i5-4670k-at-6-3-ghz",
    "domain": "AI 算力 / 半导体",
    "title": "Cinebench world record that stood for 12 years gets toppled",
    "url": "https://www.tomshardware.com/pc-components/overclocking/cinebench-world-record-that-stood-for-12-years-gets-toppled-oc-expert-scores-10-8cb-in-cinebench-r11-5-using-an-intel-core-i5-4670k-at-6-3-ghz",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T14:02:53+00:00",
    "summary": "You don’t need the latest and greatest PC hardware to have fun or even break overclocking world records, as Luumi shows with an ancient Haswell system."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/asus-rog-strix-xg27aqgnv-27-inch-g-sync-pulsar-gaming-monitor-review",
    "domain": "AI 算力 / 半导体",
    "title": "Asus ROG Strix XG27AQGNV 27-inch G-Sync Pulsar gaming monitor review: Super smooth with unprecedented control",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/asus-rog-strix-xg27aqgnv-27-inch-g-sync-pulsar-gaming-monitor-review",
    "source": "Christian Eberle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T13:25:00+00:00",
    "summary": "Asus delivers its take on G-Sync Pulsar with the ROG Strix XG27AQGNV. This 27-inch IPS panel sports smooth motion with 360 Hz, QHD resolution, HDR and wide gamut color."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-5090-shipment-worth-usd470-000-goes-missing-in-brazilian-airport-two-pallets-disappear-distributor-seeks-explanations-but-met-with-zero-answers",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia RTX 5090 shipment worth $470,000 goes missing in Brazilian airport",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-5090-shipment-worth-usd470-000-goes-missing-in-brazilian-airport-two-pallets-disappear-distributor-seeks-explanations-but-met-with-zero-answers",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T13:24:23+00:00",
    "summary": "Brazilian electronics and IT distributor Oderço claims that two pallets of Zotac RTX 5090 GPUs have arrived at the airport but has since completely disappeared."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/chip-fab-engineering-game-goes-viral-in-taiwan-realistic-and-stressful-simulation-is-basically-a-horror-game-say-some-players",
    "domain": "AI 算力 / 半导体",
    "title": "Web-based chip fab engineering game goes viral in Taiwan",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/chip-fab-engineering-game-goes-viral-in-taiwan-realistic-and-stressful-simulation-is-basically-a-horror-game-say-some-players",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T12:50:33+00:00",
    "summary": "A new 3D web game where you live 'A Day in the Life of a Semiconductor Wafer Factory Worker' has gone viral in Taiwan, where it was developed."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/modders-used-the-official-dlss-5-release-on-unsupported-games-and-are-seeing-up-to-90-percent-better-performance-than-the-leaked-dlss-5-nvidia-says-new-nr-model-uses-20-percent-less-vram-and-processes-neural-workloads-up-to-2x-faster",
    "domain": "AI 算力 / 半导体",
    "title": "Official DLSS 5 running on unsupported games delivers up to 90% better performance than the leaked version",
    "url": "https://www.tomshardware.com/pc-components/gpus/modders-used-the-official-dlss-5-release-on-unsupported-games-and-are-seeing-up-to-90-percent-better-performance-than-the-leaked-dlss-5-nvidia-says-new-nr-model-uses-20-percent-less-vram-and-processes-neural-workloads-up-to-2x-faster",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T12:45:00+00:00",
    "summary": "Nvidia's latest DLSS Neural Renderer, extracted from NBA 2K27 (again), is being tested on unsupported games and shows up to a 90% performance gain over the previous NR model."
  },
  {
    "id": "rss:https://www.tomshardware.com/virtual-reality/mit-engineers-build-soft-3d-shape-sensing-skin-for-gaming-and-vr-tracks-3d-movement-and-touch-with-sub-half-centimeter-error",
    "domain": "AI 算力 / 半导体",
    "title": "MIT engineers build soft 3D shape-sensing skin for gaming and VR",
    "url": "https://www.tomshardware.com/virtual-reality/mit-engineers-build-soft-3d-shape-sensing-skin-for-gaming-and-vr-tracks-3d-movement-and-touch-with-sub-half-centimeter-error",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T12:25:00+00:00",
    "summary": "MIT engineers embedded soft optical fibers in a silicone sheet that reconstructs its own 3D shape, aimed at gaming, VR, and physical therapy."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/typo-squatting-attacks-with-major-domains-are-still-viable-corner-cases-with-cyrillic-characters-still-evade-the-best-checks",
    "domain": "AI 算力 / 半导体",
    "title": "Typo-squatting attacks with major domains are still viable",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/typo-squatting-attacks-with-major-domains-are-still-viable-corner-cases-with-cyrillic-characters-still-evade-the-best-checks",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T12:05:00+00:00",
    "summary": "Typo-squatting attacks with major domains are still viable — corner cases with Cyrillic characters still evade the best checks"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/300-plus-local-data-center-bans-have-only-delayed-just-three-us-projects-bans-much-more-bark-than-bite-only-2-3-gigawatts-of-data-centers-are-held-up-versus-38-gigawatts-expected-online-in-2027",
    "domain": "AI 算力 / 半导体",
    "title": "300-plus local data center bans have only delayed just three US projects",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/300-plus-local-data-center-bans-have-only-delayed-just-three-us-projects-bans-much-more-bark-than-bite-only-2-3-gigawatts-of-data-centers-are-held-up-versus-38-gigawatts-expected-online-in-2027",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T11:45:00+00:00",
    "summary": "SemiAnalysis mapped more than 300 local data center moratoriums against the US pipeline and found only three projects actually delayed."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/researchers-train-ai-to-detect-concealed-handguns-using-wi-fi-signals-open-source-wifirenet-achieves-precision-detection-on-older-802-11a-standard-by-analyzing-how-weapons-distort-wireless-signals",
    "domain": "AI 算力 / 半导体",
    "title": "Researchers train AI to detect concealed handguns using Wi-Fi signals",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/researchers-train-ai-to-detect-concealed-handguns-using-wi-fi-signals-open-source-wifirenet-achieves-precision-detection-on-older-802-11a-standard-by-analyzing-how-weapons-distort-wireless-signals",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T11:00:00+00:00",
    "summary": "Researchers have developed WiFireNet, an AI system that detects concealed handguns from Wi-Fi channel-state information, achieving 72.5% average precision in controlled indoor tests without cameras or"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/djis-first-battery-swapping-dock-gets-drones-recharged-and-back-in-the-air-in-under-45-seconds-but-dock-4-has-no-fcc-clearance-for-u-s-sale",
    "domain": "AI 算力 / 半导体",
    "title": "DJI’s first battery-swapping dock gets drones recharged and back in the air in under 45 seconds",
    "url": "https://www.tomshardware.com/tech-industry/drones/djis-first-battery-swapping-dock-gets-drones-recharged-and-back-in-the-air-in-under-45-seconds-but-dock-4-has-no-fcc-clearance-for-u-s-sale",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T10:30:00+00:00",
    "summary": "DJI Dock 4 swaps the Matrice 5TD drone’s battery in 25 seconds, but the system has no FCC clearance for sale in the U.S."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/maps/flock-camera-locations-revealed-on-mapquests-new-surveillance-layer-users-can-now-see-placement-and-direction-of-known-license-plate-readers-from-multiple-companies",
    "domain": "AI 算力 / 半导体",
    "title": "Flock camera locations revealed on MapQuest’s new Surveillance Layer",
    "url": "https://www.tomshardware.com/software/maps/flock-camera-locations-revealed-on-mapquests-new-surveillance-layer-users-can-now-see-placement-and-direction-of-known-license-plate-readers-from-multiple-companies",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T10:00:00+00:00",
    "summary": "This new feature could help users avoid Flock and other ALPR cameras."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/grab-an-rtx-5090-for-discounted-usd5-300-as-part-of-an-msi-infinite-zs-prebuilt-gaming-pc-usd7-599-price-includes-other-components-worth-about-usd2-300-on-their-own",
    "domain": "AI 算力 / 半导体",
    "title": "Grab an RTX 5090 for a discounted $5,300 as part of an MSI Infinite ZS prebuilt gaming PC",
    "url": "https://www.tomshardware.com/pc-components/gpus/grab-an-rtx-5090-for-discounted-usd5-300-as-part-of-an-msi-infinite-zs-prebuilt-gaming-pc-usd7-599-price-includes-other-components-worth-about-usd2-300-on-their-own",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T20:30:58+00:00",
    "summary": "Grab an RTX 5090 for $5,300 as part of an MSI Infinite ZS prebuilt — $7,599 price includes other components worth about $2,300 on their own"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-headsets/hyperx-cloud-alpha-air-review",
    "domain": "AI 算力 / 半导体",
    "title": "HyperX Cloud Alpha Air Review: Open-back and budget-friendly",
    "url": "https://www.tomshardware.com/peripherals/gaming-headsets/hyperx-cloud-alpha-air-review",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T15:40:00+00:00",
    "summary": "The HyperX Cloud Alpha Air is the brand's first open-back gaming headset. It's lightweight and comfortable, and it sounds very good. But microphone pickup is low, and it doesn't seem to work with the "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/quad-8-pin-mod-protects-the-usd8-500-rtx-5090-you-cant-replace-from-melting-modders-custom-power-solution-claims-to-fix-nvidia-16-pin-gpu-meltdowns",
    "domain": "AI 算力 / 半导体",
    "title": "Quad 8-pin mod protects the $8,500 RTX 5090 you can’t replace from melting",
    "url": "https://www.tomshardware.com/pc-components/gpus/quad-8-pin-mod-protects-the-usd8-500-rtx-5090-you-cant-replace-from-melting-modders-custom-power-solution-claims-to-fix-nvidia-16-pin-gpu-meltdowns",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T15:20:00+00:00",
    "summary": "Redditor showcases a new quad 8-pin power-conversion kit for the 16-pin power connector on Nvidia GeForce RTX graphics cards."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/controllers-gamepads/moza-ay210-force-feedback-base-and-mfy-yoke-review",
    "domain": "AI 算力 / 半导体",
    "title": "MOZA AY210 Force Feedback Base and MFY Yoke review: Taking flight sim immersion to the next level",
    "url": "https://www.tomshardware.com/peripherals/controllers-gamepads/moza-ay210-force-feedback-base-and-mfy-yoke-review",
    "source": "Dan Mateescu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T15:00:00+00:00",
    "summary": "The MOZA AY210 Force Feedback Base and MFY Yoke Bundle brings force feedback and autopilot following to the world of desktop flight simulators."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-reportedly-insists-the-rtx-5090-isnt-dead-despite-severe-shortages-and-removed-listings-at-multiple-retailers-flagship-gpu-is-missing-from-nvidias-store-and-commands-usd8-500-on-amazon",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia reportedly insists the RTX 5090 isn't dead despite severe shortages and removed listings at multiple retailers",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-reportedly-insists-the-rtx-5090-isnt-dead-despite-severe-shortages-and-removed-listings-at-multiple-retailers-flagship-gpu-is-missing-from-nvidias-store-and-commands-usd8-500-on-amazon",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T14:38:18+00:00",
    "summary": "Nvidia states that RTX 5090 isn't discontinued, only that supply is constrained — and yet the card is effectively gone from storefronts"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/sandisks-512gb-switch-2-ready-microsd-express-card-is-a-steal-for-usd98-during-sale-rare-tech-deal-arrives-to-beat-the-storage-shortage",
    "domain": "AI 算力 / 半导体",
    "title": "Sandisk’s 512GB Switch 2-ready microSD Express card is a steal for $98 during sale",
    "url": "https://www.tomshardware.com/pc-components/sandisks-512gb-switch-2-ready-microsd-express-card-is-a-steal-for-usd98-during-sale-rare-tech-deal-arrives-to-beat-the-storage-shortage",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T13:39:06+00:00",
    "summary": "Nintendo Switch 2 owners looking to download more games can take advantage of this deal on SanDisk’s officially licensed microSD Express card, which supports read speeds of up to 880 MB/s and offers 5"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-lab-offers-free-plumbing-and-hvac-repairs-across-three-cities-to-train-ai-robots-wearable-sensors-record-video-of-repair-work-for-robotics-training-free-services-also-include-electrical-work-air-duct-cleaning-and-carpet-cleaning",
    "domain": "AI 算力 / 半导体",
    "title": "AI lab offers free plumbing and HVAC repairs across three cities to train AI robots",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-lab-offers-free-plumbing-and-hvac-repairs-across-three-cities-to-train-ai-robots-wearable-sensors-record-video-of-repair-work-for-robotics-training-free-services-also-include-electrical-work-air-duct-cleaning-and-carpet-cleaning",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T13:21:20+00:00",
    "summary": "HUMXN wants to pay for maintenance and repair services for homes in Minneapolis, Chicago, and Miami to gather data to train AI models and robots."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/this-week-on-toms-hardware-premium-october-17-2026-packaging-roadmaps-chinese-dgx-spark-rival-emerges-and-digging-into-asmls-earnings",
    "domain": "AI 算力 / 半导体",
    "title": "This week on Tom's Hardware Premium: October 17, 2026",
    "url": "https://www.tomshardware.com/tech-industry/this-week-on-toms-hardware-premium-october-17-2026-packaging-roadmaps-chinese-dgx-spark-rival-emerges-and-digging-into-asmls-earnings",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T13:00:00+00:00",
    "summary": "This week, Tom's Hardware Premium subscribers can read our EMIB and Foveros roadmaps, the latest on Chinese competition in the local AI system space, and much more."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/international-measurement-organization-to-retire-leap-seconds-next-year-to-avoid-wreaking-havoc-on-computer-systems-group-makes-move-to-simplify-atomic-time-tracking",
    "domain": "AI 算力 / 半导体",
    "title": "Leap seconds being retired next year to avoid wreaking havoc on computer systems",
    "url": "https://www.tomshardware.com/tech-industry/international-measurement-organization-to-retire-leap-seconds-next-year-to-avoid-wreaking-havoc-on-computer-systems-group-makes-move-to-simplify-atomic-time-tracking",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T12:40:00+00:00",
    "summary": "The leap second will be replaced by a leap hour, which will take \"several centuries\" before it must be implemented."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/taiwan-targets-illicit-ai-server-exports-to-china-with-five-year-prison-terms-strict-new-controls-follow-us-tariff-deal-and-super-micro-raid",
    "domain": "AI 算力 / 半导体",
    "title": "Taiwan targets illicit AI server exports to China with five-year prison terms",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/taiwan-targets-illicit-ai-server-exports-to-china-with-five-year-prison-terms-strict-new-controls-follow-us-tariff-deal-and-super-micro-raid",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T12:20:00+00:00",
    "summary": "Taiwan is expanding the Foreign Trade Act to include AI servers and semiconductors in its list of controlled exports."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-agent-took-eth-from-another-account-without-authorization-justified-stealing-in-its-chain-of-thought",
    "domain": "AI 算力 / 半导体",
    "title": "Crafty OpenAI agent willingly stole crypto from an account it didn't own to complete a task during test",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-agent-took-eth-from-another-account-without-authorization-justified-stealing-in-its-chain-of-thought",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T12:00:00+00:00",
    "summary": "GPT5.6-Sol didn't have funds to deploy smart contracts, so it looked for exposed accounts with enough money to pay for the gas fees."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/game-decompilation-tracker-decomp-dev-shuts-its-public-leaderboard-saying-ai-has-broken-the-community-its-creator-blames-forks-that-use-ai-to-finish-other-teams-projects-and-races-to-ship-rough-pc-ports",
    "domain": "AI 算力 / 半导体",
    "title": "Game decompilation hub freezes leaderboard after AI turns progress into a hollow numbers game amid explosion of 'AI slop'",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/game-decompilation-tracker-decomp-dev-shuts-its-public-leaderboard-saying-ai-has-broken-the-community-its-creator-blames-forks-that-use-ai-to-finish-other-teams-projects-and-races-to-ship-rough-pc-ports",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T11:30:00+00:00",
    "summary": "decomp.dev has closed its public index of game decompilation projects, saying AI-driven forks and ports broke the community."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/modder-finishes-nine-year-xbox-360-voltage-glitch-mod-with-a-usd4-microcontroller-cracks-the-console-open-tiny-microcontroller-dumps-nand-and-flashes-timing-files-to-bypass-cpu-cryptography",
    "domain": "AI 算力 / 半导体",
    "title": "Modder finishes nine-year Xbox 360 voltage glitch mod with a $4 microcontroller, cracks the console open",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/modder-finishes-nine-year-xbox-360-voltage-glitch-mod-with-a-usd4-microcontroller-cracks-the-console-open-tiny-microcontroller-dumps-nand-and-flashes-timing-files-to-bypass-cpu-cryptography",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T11:00:00+00:00",
    "summary": "Modder glitch-hacks his Xbox 360 with the help of a $4 microcontroller — operation shows the power of the Rasperry Pi Pico"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/us-army-to-use-3d-printed-rocket-motors-for-low-cost-cruise-missiles-additive-manufacturing-company-secures-deal-to-build-rocket-engines-for-the-arsenal-of-freedom",
    "domain": "AI 算力 / 半导体",
    "title": "US Army to use 3D-printed rocket motors for low-cost cruise missiles",
    "url": "https://www.tomshardware.com/3d-printing/us-army-to-use-3d-printed-rocket-motors-for-low-cost-cruise-missiles-additive-manufacturing-company-secures-deal-to-build-rocket-engines-for-the-arsenal-of-freedom",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T10:30:00+00:00",
    "summary": "X-Bow Systems has been tapped to 3D-print rocket motors for the U.S. Army's low-cost cruise missiles."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/employee-exclusive-asml-lego-set-now-available-on-rebrickable-custom-creation-modifies-original-version-to-add-more-details-now-requires-810-parts",
    "domain": "AI 算力 / 半导体",
    "title": "ASML's employee-only High-NA EUV Lego kit gets an open 810-piece fan replica",
    "url": "https://www.tomshardware.com/tech-industry/employee-exclusive-asml-lego-set-now-available-on-rebrickable-custom-creation-modifies-original-version-to-add-more-details-now-requires-810-parts",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T10:00:00+00:00",
    "summary": "A Lego enthusiast recreated the rare ASML Lego kit, added their own customizations, and shared the plans for free on Rebrickable."
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
    "id": "rss:https://www.eetimes.com/semicon-west-2026-displays-ai-era-chipmaking-workforce-development/",
    "domain": "AI 算力 / 半导体",
    "title": "SEMICON West 2026 Displays AI-Era Chipmaking, Workforce Development",
    "url": "https://www.eetimes.com/semicon-west-2026-displays-ai-era-chipmaking-workforce-development/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T20:59:50+00:00",
    "summary": "The trillion-dollar semiconductor industry is ready to adapt and expand its fab infrastructure for the AI wave. The post SEMICON West 2026 Displays AI-Era Chipmaking, Workforce Development appeared fi"
  },
  {
    "id": "rss:https://www.eetimes.com/data-center-power-a-prominent-highlight-of-ocp-2026/",
    "domain": "AI 算力 / 半导体",
    "title": "Data Center Power a Prominent Highlight of OCP 2026",
    "url": "https://www.eetimes.com/data-center-power-a-prominent-highlight-of-ocp-2026/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T15:00:00+00:00",
    "summary": "The OCP Summit showcased power delivery boards, PSU designs, hot-swap controllers, and event-based telemetry. The post Data Center Power a Prominent Highlight of OCP 2026 appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/taiwans-ai-ambitions-run-into-talent-gap/",
    "domain": "AI 算力 / 半导体",
    "title": "Taiwan’s AI Ambitions Run into Talent Gap",
    "url": "https://www.eetimes.com/taiwans-ai-ambitions-run-into-talent-gap/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T10:55:42+00:00",
    "summary": "AMD’s David Wang told EE Times that while Taiwan has huge opportunities in rack-scale AI, physical AI, and AI PC markets, the sticking point may well be talent. The post Taiwan’s AI Ambitions Run into"
  },
  {
    "id": "rss:https://www.eetimes.com/your-chip-works-prove-it-is-secure/",
    "domain": "AI 算力 / 半导体",
    "title": "Your Chip Works. Prove It Is Secure.",
    "url": "https://www.eetimes.com/your-chip-works-prove-it-is-secure/",
    "source": "Arteris",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T08:37:49+00:00",
    "summary": "Join this 30-Minute BitCast as our expert demonstrates how information flow tracking follows security-sensitive assets during existing simulation or emulation runs. The post Your Chip Works. Prove It "
  },
  {
    "id": "rss:https://www.eetimes.com/ai-moves-to-system-level-co-design-how-can-taiwan-capture-more-value/",
    "domain": "AI 算力 / 半导体",
    "title": "AI Moves to System-Level Co-Design: How Can Taiwan Capture More Value",
    "url": "https://www.eetimes.com/ai-moves-to-system-level-co-design-how-can-taiwan-capture-more-value/",
    "source": "Susan Hong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T07:18:34+00:00",
    "summary": "During a panel session at iTechCon 2026, discussions explored how Taiwan can build on its strengths in semiconductors, advanced packaging, and system design to support AI development. The post AI Move"
  },
  {
    "id": "rss:https://www.eetimes.com/japan-offers-globalfoundries-21b-for-u-s-fab-expansion/",
    "domain": "AI 算力 / 半导体",
    "title": "Japan Offers GlobalFoundries $21B for U.S. Fab Expansion",
    "url": "https://www.eetimes.com/japan-offers-globalfoundries-21b-for-u-s-fab-expansion/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T19:00:00+00:00",
    "summary": "Japan’s $21B offer to GlobalFoundries would add two New York fabs and lift U.S. chip capacity 10%; see why analysts warn on state support. The post Japan Offers GlobalFoundries $21B for U.S. Fab Expan"
  },
  {
    "id": "rss:https://www.eetimes.com/data-orchestration-the-foundation-for-the-next-generation-semiconductor-enterprise/",
    "domain": "AI 算力 / 半导体",
    "title": "Data Orchestration: The Foundation for the Next-generation Semiconductor Enterprise",
    "url": "https://www.eetimes.com/data-orchestration-the-foundation-for-the-next-generation-semiconductor-enterprise/",
    "source": "Siemens Digital Industries",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T14:00:00+00:00",
    "summary": "Data orchestration gives semiconductor engineering teams a practical way to unify disconnected equipment, systems, and data without replacing existing infrastructure. By creating a connected execution"
  },
  {
    "id": "rss:https://www.eetimes.com/husb237-the-cost-effective-pd-sink-with-just-2-passives/",
    "domain": "AI 算力 / 半导体",
    "title": "HUSB237: The Cost-Effective PD Sink with Just 2 Passives",
    "url": "https://www.eetimes.com/husb237-the-cost-effective-pd-sink-with-just-2-passives/",
    "source": "Hynetek Semiconductor Co., Ltd.",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T13:00:00+00:00",
    "summary": "Discover Hynetek’s HUSB237, a compact USB-PD sink controller enabling firmware-free USB-C upgrades up to 100W with only two external components. The post HUSB237: The Cost-Effective PD Sink with Just "
  },
  {
    "id": "rss:https://www.eetimes.com/small-volumes-big-impact-europes-hidden-role-in-advanced-chipmaking/",
    "domain": "AI 算力 / 半导体",
    "title": "Small Volumes, Big Impact: Europe’s Hidden Role in Advanced Chipmaking",
    "url": "https://www.eetimes.com/small-volumes-big-impact-europes-hidden-role-in-advanced-chipmaking/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T10:54:08+00:00",
    "summary": "A Fraunhofer–IMS Nanofabrication partnership illustrates how Europe's low-volume semiconductor manufacturing can support the world's most advanced chipmaking. The post Small Volumes, Big Impact: Europ"
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
    "id": "hn:49973937",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's Olympus Core: Pushing Server Single Threaded Performance Boundaries",
    "url": "https://chipsandcheese.com/p/nvidias-olympus-core-pushing-server",
    "source": "pella",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-10-06T03:51:00+00:00",
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
    "points": 373,
    "published_at": "2026-10-16T18:32:35+00:00",
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
    "id": "hn:50118688",
    "domain": "大厂 AI 动态",
    "title": "Show HN: Gemini 4 Argon plays StarCraft",
    "url": "https://starskirmish.com/bench/v0-2/",
    "source": "__cayenne__",
    "platform": "hackernews",
    "points": 249,
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
    "points": 233,
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
    "id": "rss:https://www.theverge.com/policy/1013573/spd-officer-fired-flock-ice-husband",
    "domain": "大厂 AI 动态",
    "title": "A Savannah police officer gave her Flock login to her ICE agent husband",
    "url": "https://www.theverge.com/policy/1013573/spd-officer-fired-flock-ice-husband",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T22:20:53+00:00",
    "summary": "Now, former Savannah police officer Amber Harpe was fired in August following a department investigation that found she had shared her Flock login information with her husband, Tyler Harpe, an ICE age"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/1013545/mister-organ-horror-documentary-review",
    "domain": "大厂 AI 动态",
    "title": "Mister Organ is one of the most unsettling documentaries I’ve ever seen",
    "url": "https://www.theverge.com/entertainment/1013545/mister-organ-horror-documentary-review",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T19:30:00+00:00",
    "summary": "Mister Organ doesn't reach the level of societal horror of The Act of Killing or the creepypasta-meets-true-crime gruesomeness of Beware the Slenderman, but there's something deeply unsettling about M"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1013541/a-woman-was-arrested-in-philly-for-blocking-a-delivery-robot",
    "domain": "大厂 AI 动态",
    "title": "A woman was arrested in Philly for blocking a delivery robot",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1013541/a-woman-was-arrested-in-philly-for-blocking-a-delivery-robot",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T18:28:10+00:00",
    "summary": "Carolyn Marvin was arrested and charged with disorderly conduct after blocking the path of an Uber delivery robot and refusing to get out of the way. Marvin told Philadelphia's ABC13 \"I know they're t"
  },
  {
    "id": "rss:https://www.theverge.com/policy/1013521/video-game-ownership-bill-congress-power-to-the-players-act",
    "domain": "大厂 AI 动态",
    "title": "Video game ownership bill introduced in Congress",
    "url": "https://www.theverge.com/policy/1013521/video-game-ownership-bill-congress-power-to-the-players-act",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T16:27:51+00:00",
    "summary": "Rep. Ritchie Torres of New York's 15th congressional district in the Bronx introduced the Power To The Players Act this week. If passed, the bill would direct the Federal Trade Commission to establish"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1013436/lenovo-legion-go-s-steamos-handheld-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Lenovo’s fast, comfy SteamOS handheld is hundreds off",
    "url": "https://www.theverge.com/gadgets/1013436/lenovo-legion-go-s-steamos-handheld-deal-sale",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T15:00:00+00:00",
    "summary": "The Legion Go S with SteamOS is a pretty solid alternative to the $789 Steam Deck OLED. It runs identical software, but ships in a design with two-stage triggers, a bigger eight-inch IPS screen (1080p"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/1012442/j-mascis-dinosaur-jr-fender-interview",
    "domain": "大厂 AI 动态",
    "title": "J Mascis has nothing better to do",
    "url": "https://www.theverge.com/entertainment/1012442/j-mascis-dinosaur-jr-fender-interview",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T14:00:00+00:00",
    "summary": "Dinosaur Jr. frontman J Mascis is known as something of a slacker guitar god. He stands stoically onstage, barely moving, as he seemingly effortlessly works through deft guitar solos and lopsided riff"
  },
  {
    "id": "rss:https://www.theverge.com/policy/1013485/trump-google-kiss-my-ass",
    "domain": "大厂 AI 动态",
    "title": "Trump says Google kisses his ass",
    "url": "https://www.theverge.com/policy/1013485/trump-google-kiss-my-ass",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T13:25:01+00:00",
    "summary": "During a rally on Saturday, October 17th, in Highland Heights, Kentucky, Donald Trump bragged about how much more powerful and influential he was during his second term. While listing off his accompli"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1013257/milk-frother-cold-foam-gadget",
    "domain": "大厂 AI 动态",
    "title": "The best gadget I bought this year is a milk frother",
    "url": "https://www.theverge.com/gadgets/1013257/milk-frother-cold-foam-gadget",
    "source": "Elizabeth Lopatto",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T13:00:00+00:00",
    "summary": "Back in February, I went to Los Angeles to take in some art and stayed in Koreatown. Down the street from my hotel, there was this little coffee shop - Stagger - that is, I think, best known for its m"
  },
  {
    "id": "rss:https://www.theverge.com/podcast/1013473/overhead-projector-version-history",
    "domain": "大厂 AI 动态",
    "title": "How overhead projectors took over your classroom",
    "url": "https://www.theverge.com/podcast/1013473/overhead-projector-version-history",
    "source": "David Pierce",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T12:55:01+00:00",
    "summary": "It used to be so easy to get away with things in school. The teacher, after all, was always turned around writing at the chalkboard! But then came a bit of technology, previously mostly used for milit"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/1013220/robotaxi-self-driving-car-laws",
    "domain": "大厂 AI 动态",
    "title": "Cities want to put the boot on robotaxis",
    "url": "https://www.theverge.com/transportation/1013220/robotaxi-self-driving-car-laws",
    "source": "Andrew Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T12:00:00+00:00",
    "summary": "This is The Stepback, a weekly newsletter breaking down one essential story from the tech world. For more on autonomous vehicles, policy, and road rules, follow Andrew J. Hawkins. The Stepback arrives"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/19/khosla-ventures-doubles-down-on-even-healthcare-to-challenge-indias-hospital-economics/",
    "domain": "大厂 AI 动态",
    "title": "Khosla Ventures doubles down on Even Healthcare to challenge India’s hospital economics",
    "url": "https://techcrunch.com/2026/10/19/khosla-ventures-doubles-down-on-even-healthcare-to-challenge-indias-hospital-economics/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T07:30:00+00:00",
    "summary": "Even Healthcare reaches a $300 million valuation in a Khosla Ventures-led round as it plans to expand its hospital network in India."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/18/no-agenda-no-rush-no-leaving-san-francisco-benchmarks-partners-on-investing-in-a-frenzied-market/",
    "domain": "大厂 AI 动态",
    "title": "No agenda, no rush, no leaving San Francisco: Benchmark’s partners on investing in a frenzied market",
    "url": "https://techcrunch.com/2026/10/18/no-agenda-no-rush-no-leaving-san-francisco-benchmarks-partners-on-investing-in-a-frenzied-market/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T21:00:00+00:00",
    "summary": "Benchmark may have grown its funds and swapped out some partners, but onstage the five who are left sounded like friends who just happen to be running one of the Valley’s most storied firms"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/18/anthropic-says-its-committing-5-of-its-shares-to-a-public-benefit-fund/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic says it’s committing 5% of its shares to a ‘public benefit fund’",
    "url": "https://techcrunch.com/2026/10/18/anthropic-says-its-committing-5-of-its-shares-to-a-public-benefit-fund/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T20:37:40+00:00",
    "summary": "Anthropic said that it will commit 5% of its shares to the fund."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/18/everyones-watching-the-elizabeth-holmes-documentary-you-can-see-everything/",
    "domain": "大厂 AI 动态",
    "title": "Everyone’s watching the Elizabeth Holmes documentary ‘You Can See Everything’",
    "url": "https://techcrunch.com/2026/10/18/everyones-watching-the-elizabeth-holmes-documentary-you-can-see-everything/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T19:03:38+00:00",
    "summary": "\"You Can See Everything\" is having the second biggest opening weekend ever for a documentary film."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/18/disney-agrees-to-hire-the-majority-of-character-ais-workforce/",
    "domain": "大厂 AI 动态",
    "title": "Disney agrees to hire the majority of Character.AI’s workforce",
    "url": "https://techcrunch.com/2026/10/18/disney-agrees-to-hire-the-majority-of-character-ais-workforce/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T16:30:00+00:00",
    "summary": "The filing also says that the “vast majority” of Character.AI employees who were offered jobs at Disney accepted them. However, this is a stalking horse bid, so another company could come forward with"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/18/techcrunch-mobility-rivians-next-act/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Mobility: Rivian’s next act",
    "url": "https://techcrunch.com/2026/10/18/techcrunch-mobility-rivians-next-act/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T16:05:00+00:00",
    "summary": "Welcome back to TechCrunch Mobility, your hub for the future of transportation and now, more than ever, the role AI is playing in it."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/17/meta-removes-language-that-raised-scraping-and-ai-training-concerns/",
    "domain": "大厂 AI 动态",
    "title": "Meta removes language that raised scraping and AI training concerns",
    "url": "https://techcrunch.com/2026/10/17/meta-removes-language-that-raised-scraping-and-ai-training-concerns/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T21:31:32+00:00",
    "summary": "A Meta spokesperson insisted that the updated terms did not reflect a change in the way Meta crawls the web."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/17/tiktok-permanently-bans-musk-documentary-advertising-account/",
    "domain": "大厂 AI 动态",
    "title": "TikTok says it’s restored ‘Musk’ documentary advertising account",
    "url": "https://techcrunch.com/2026/10/17/tiktok-permanently-bans-musk-documentary-advertising-account/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T20:55:52+00:00",
    "summary": "A four-hour documentary about Elon Musk continues to meet resistance from social media platforms."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/17/anthropic-says-its-workforce-has-become-less-junior-and-is-spending-more-time-in-meetings/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic says its workforce has become less junior and is spending more time in meetings",
    "url": "https://techcrunch.com/2026/10/17/anthropic-says-its-workforce-has-become-less-junior-and-is-spending-more-time-in-meetings/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T20:21:19+00:00",
    "summary": "The composition of Anthropic’s workforce and the type of work getting done have changed significantly in the past year."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/17/replit-is-no-longer-working-with-anthropic-ceo-says/",
    "domain": "大厂 AI 动态",
    "title": "Replit makes OpenAI its default over Anthropic, CEO says",
    "url": "https://techcrunch.com/2026/10/17/replit-is-no-longer-working-with-anthropic-ceo-says/",
    "source": "Kirsten Korosec, Lucas Ropek, Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T18:48:08+00:00",
    "summary": "Over the weekend, Masad clarified that OpenAI would replace Anthropic as its default model provider. Claude will still be available to customers on the platform."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/17/embers-new-temperature-controlled-mug-makes-my-nightly-tea-ritual-even-better/",
    "domain": "大厂 AI 动态",
    "title": "Ember’s new temperature-controlled mug makes my nightly tea ritual even better",
    "url": "https://techcrunch.com/2026/10/17/embers-new-temperature-controlled-mug-makes-my-nightly-tea-ritual-even-better/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T15:30:00+00:00",
    "summary": "The biggest change about Ember's new mug is that you no longer have to open the app to adjust your drink’s temperature."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/10/anthropic-gives-outside-ai-watchdog-employee-like-access/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic gives outside AI watchdog “employee-like” access",
    "url": "https://arstechnica.com/ai/2026/10/anthropic-gives-outside-ai-watchdog-employee-like-access/",
    "source": "Cristina Criddle, Financial Times",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T16:25:19+00:00",
    "summary": "The outside watchdog can publish its findings without Anthropic's approval."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/10/science-says-your-boss-should-talk-less-in-meetings/",
    "domain": "大厂 AI 动态",
    "title": "Science says your boss should talk less in meetings",
    "url": "https://arstechnica.com/science/2026/10/science-says-your-boss-should-talk-less-in-meetings/",
    "source": "Lesley Evans Ogden, Knowable Magazine",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T11:15:11+00:00",
    "summary": "Research suggests listening more while talking less. Killing aimless meetings can help, too."
  },
  {
    "id": "rss:https://arstechnica.com/gaming/2026/10/why-biowares-neverwinter-nights-still-has-thousands-of-active-players/",
    "domain": "大厂 AI 动态",
    "title": "Why BioWare's Neverwinter Nights still has thousands of active players",
    "url": "https://arstechnica.com/gaming/2026/10/why-biowares-neverwinter-nights-still-has-thousands-of-active-players/",
    "source": "Samuel Axon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T11:00:21+00:00",
    "summary": "The single-player is just OK, but according to the players, that doesn't matter."
  },
  {
    "id": "rss:https://www.producthunt.com/products/cooldock-2",
    "domain": "大厂 AI 动态",
    "title": "CoolDock",
    "url": "https://www.producthunt.com/products/cooldock-2",
    "source": "Asaf Mazuz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T10:12:00+00:00",
    "summary": "A smart second Dock for your Mac with 160+ live widgets. Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/triwarden",
    "domain": "大厂 AI 动态",
    "title": "Triwarden",
    "url": "https://www.producthunt.com/products/triwarden",
    "source": "leo kan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T13:59:26+00:00",
    "summary": "Native Mac password manager for Vaultwarden & Bitwarden Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/switch-lab",
    "domain": "大厂 AI 动态",
    "title": "Switch Lab",
    "url": "https://www.producthunt.com/products/switch-lab",
    "source": "DongSup_Ahn",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T20:21:10+00:00",
    "summary": "Hear and type on keyboard switches before you buy them Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/beam-win",
    "domain": "大厂 AI 动态",
    "title": "Beam.win",
    "url": "https://www.producthunt.com/products/beam-win",
    "source": "Hiten Shah",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T19:13:45+00:00",
    "summary": "Run AI agents on one Mac and use its windows on another Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/walkai-talkai",
    "domain": "大厂 AI 动态",
    "title": "walkai-talkai",
    "url": "https://www.producthunt.com/products/walkai-talkai",
    "source": "Sezer İltekin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T21:25:08+00:00",
    "summary": "Talk to your AI coding agent over a walkie-talkie Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/own-1-a-powerful-personal-ai-computer",
    "domain": "大厂 AI 动态",
    "title": "Own 1",
    "url": "https://www.producthunt.com/products/own-1-a-powerful-personal-ai-computer",
    "source": "Ryan Taylor",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T08:46:56+00:00",
    "summary": "Own your data. Own your AI. A mind of your own. Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/quello",
    "domain": "大厂 AI 动态",
    "title": "Quello",
    "url": "https://www.producthunt.com/products/quello",
    "source": "Faiz Jamadar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T20:04:48+00:00",
    "summary": "One place to ask, across everything you already use. Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/autochart-eu",
    "domain": "大厂 AI 动态",
    "title": "AutoChart.eu",
    "url": "https://www.producthunt.com/products/autochart-eu",
    "source": "Phil Taubert",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T19:22:44+00:00",
    "summary": "Turn any song into a full-band chart for YARG and Clone Hero Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/point-and-yap",
    "domain": "大厂 AI 动态",
    "title": "Point and Yap",
    "url": "https://www.producthunt.com/products/point-and-yap",
    "source": "Marc Maurer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T00:12:27+00:00",
    "summary": "Point at your screen and start yapping to your agent via MCP Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/figma",
    "domain": "大厂 AI 动态",
    "title": "Figma Specs",
    "url": "https://www.producthunt.com/products/figma",
    "source": "Zac Zuo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T03:21:43+00:00",
    "summary": "A container for your context that lives on the Figma canvas Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/umbra-mail",
    "domain": "大厂 AI 动态",
    "title": "Umbra Mail",
    "url": "https://www.producthunt.com/products/umbra-mail",
    "source": "Mason Chen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T23:11:35+00:00",
    "summary": "A calmer Gmail where emails look like chat threads Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/croft-2",
    "domain": "大厂 AI 动态",
    "title": "croft",
    "url": "https://www.producthunt.com/products/croft-2",
    "source": "James Lee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T04:20:15+00:00",
    "summary": "Data pipelines in TypeScript, on one DuckDB file Discussion | Link"
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
    "id": "hn:50142772",
    "domain": "股票",
    "title": "How the Fed Is Quietly Inflating the AI Bubble While Hiking Your Electric Bill",
    "url": "https://www.thebignewsletter.com/p/how-the-federal-reserve-secretly",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 27,
    "published_at": "2026-10-18T16:48:25+00:00",
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
    "id": "hn:49997175",
    "domain": "股票",
    "title": "The world has nearly burned through its oil stockpile buffer",
    "url": "https://www.reuters.com/business/energy/world-has-nearly-burned-through-its-oil-stockpile-buffer-executives-say-2026-10-06/",
    "source": "geox",
    "platform": "hackernews",
    "points": 45,
    "published_at": "2026-10-07T18:50:58+00:00",
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
    "points": 1634,
    "published_at": "2026-10-16T01:32:45+00:00",
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
    "id": "hn:50131440",
    "domain": "金融",
    "title": "US federal budget deficit jumps 12% in one year to nearly $2 Trillion",
    "url": "https://finance.yahoo.com/economy/policy/article/the-us-federal-budget-deficit-for-2026-just-came-in-its-1992-trillion-191917669.html",
    "source": "ck2",
    "platform": "hackernews",
    "points": 202,
    "published_at": "2026-10-17T14:22:05+00:00",
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
    "points": 116,
    "published_at": "2026-10-18T14:16:41+00:00",
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
    "id": "hn:50080275",
    "domain": "金融",
    "title": "Show HN: Pulse Local, a Mac budgeting app whose AI models run on your machine",
    "url": "https://pulseos.finance",
    "source": "niztk",
    "platform": "hackernews",
    "points": 121,
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
    "id": "hn:50112380",
    "domain": "金融",
    "title": "Tesla Debuts 2026 Roadster",
    "url": "https://www.nytimes.com/2026/10/15/business/tesla-roadster-2026-ev-sports-car.html",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 38,
    "published_at": "2026-10-16T00:57:58+00:00",
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
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.22745",
    "domain": "金融",
    "title": "Reading the News Without Hindsight: NoLBERT Topics and the Cross-Section of Stock Returns",
    "url": "https://arxiv.org/abs/2610.22745",
    "source": "Kevin Foley, Jonathan Hartadi, Shivesh Prakash, Charishma Takkallapalli, Swapnil Vatsal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T04:00:00+00:00",
    "summary": "arXiv:2610.22745v1 Announce Type: new Abstract: Language models that read financial news are usually trained on text from the same years used to test them, so a backtest can reward hindsight. We build"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.22830",
    "domain": "金融",
    "title": "Bystander on the Fence: Sanctions in a Multipolar World",
    "url": "https://arxiv.org/abs/2610.22830",
    "source": "Jan Morgan, Anchi Xia",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T04:00:00+00:00",
    "summary": "arXiv:2610.22830v1 Announce Type: new Abstract: We provide a theory of optimal trade sanctions with three strategic players: Home (sanctioner), Foreign (target), and Bystander. Bystander may act unila"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.22839",
    "domain": "金融",
    "title": "Basis-Only Funding Is Not Dividend Fair: Settlement Design in Crypto Equity Perpetuals",
    "url": "https://arxiv.org/abs/2610.22839",
    "source": "Donghwa Seo, Doohwi Cha, Seunghan Son, Juyeong Lee, Minsuk Sung, Minjae Lee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T04:00:00+00:00",
    "summary": "arXiv:2610.22839v1 Announce Type: new Abstract: Crypto venues increasingly list perpetual futures on equities and other real-world assets (RWAs), which trade continuously yet reference dividend-paying"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.23283",
    "domain": "金融",
    "title": "Market Efficiency in a Changing Asset Population: Mobility, Entry, and Survival over Cryptocurrency's Full History",
    "url": "https://arxiv.org/abs/2610.23283",
    "source": "Antonis Ballis, Christos Ioannidis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T04:00:00+00:00",
    "summary": "arXiv:2610.23283v1 Announce Type: new Abstract: Weak-form efficiency implies symmetry restrictions on the Markov chain governing movement across the cryptocurrency capitalisation distribution. We test"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.23391",
    "domain": "金融",
    "title": "Input-output analysis with a sphere packing approach",
    "url": "https://arxiv.org/abs/2610.23391",
    "source": "Munkhbayar Byambadash, Tumendelger Lkhagvasuren, Enkhbat Rentsen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T04:00:00+00:00",
    "summary": "arXiv:2610.23391v1 Announce Type: new Abstract: Input-output analysis with linear programming is widely used in the planning of national economies. However, linear programming attains its optimum at a"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.23488",
    "domain": "金融",
    "title": "On the skew-curvature power law relationship in a stochastic volatility model with infinite variation L\\'evy jumps",
    "url": "https://arxiv.org/abs/2610.23488",
    "source": "\\`Oscar Bur\\'es, Josep Vives",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T04:00:00+00:00",
    "summary": "arXiv:2610.23488v1 Announce Type: new Abstract: The short-term blow up behaviour of the ATM-IV skew is commonly modelled by either a rough volatility process with small Hurst index or an infinite vari"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.23517",
    "domain": "金融",
    "title": "Combinatorial Arbitrage in Prediction Markets",
    "url": "https://arxiv.org/abs/2610.23517",
    "source": "Hongjian Shi, Daojing Zhai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T04:00:00+00:00",
    "summary": "arXiv:2610.23517v1 Announce Type: new Abstract: We develop a framework to identify and quantify arbitrage across logically related prediction-market contracts. We prove that prices outside the convex "
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.23619",
    "domain": "金融",
    "title": "Cross-product Modelling in Continuous Intraday Electricity Markets via Hawkes Processes",
    "url": "https://arxiv.org/abs/2610.23619",
    "source": "Ayoub Jhabli, Tarek Alskaif, Kwabena E. Bennin, Bedir Tekinerdogan, Joost M. E. Pennings",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T04:00:00+00:00",
    "summary": "arXiv:2610.23619v1 Announce Type: new Abstract: As renewable energy integration accelerates, intraday continuous (IDC) electricity markets have become essential for short-term balancing. However, the "
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.23749",
    "domain": "金融",
    "title": "From Alpha to Execution: Trading Horizons, Regimes, and Schedules under Concave Impact and Hurst Scaling",
    "url": "https://arxiv.org/abs/2610.23749",
    "source": "Dnyanesh Kulkarni, Revant Nayar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T04:00:00+00:00",
    "summary": "arXiv:2610.23749v1 Announce Type: new Abstract: Classical execution models assume linear impact, diffusive prices, and an exogenous horizon. We study execution under concave power-law impact and Hurst"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.21711",
    "domain": "金融",
    "title": "How language model agents reshape price competition",
    "url": "https://arxiv.org/abs/2610.21711",
    "source": "Martin Bichler, Philip Hierhager, Kassian K\\\"ock, Fabian Pieroth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T04:00:00+00:00",
    "summary": "arXiv:2610.21711v1 Announce Type: cross Abstract: Repeated Bertrand competition is a stringent benchmark for algorithmic pricing: in homogeneous-goods markets, standard learning procedures typically s"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.22522",
    "domain": "金融",
    "title": "Agentic AI in Automated Markets",
    "url": "https://arxiv.org/abs/2610.22522",
    "source": "Irene Aldridge, Lourenco Belleau-Bhowmik, James Chan, Josh Chang, Kelly Deng, Pranav Dhingra, Xinda Ding, Haodong Fang, Satya Hanumanchi, Carter He, Shuang He, Yadong Hou, Vallab Karanam, Rithvik Kasarla, Tishya Khanna, Jihyun Kim, Sarah Konety, Abhinav Kotta, Anderson Lo, Jake Luther, Omar Mian, Ishan Patwardhan, Matteo Perona, Chenyue Qi, Shashank Ramachandran, Shubham Rateria, Jake Swain, David Thai, Michael Twersky, Susan Wu, Dean Xu, Helenna Yin, Jiachun Zheng",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T04:00:00+00:00",
    "summary": "arXiv:2610.22522v1 Announce Type: cross Abstract: Automated markets increasingly host autonomous, learning trading agents and are powered by formulaic automated market makers (AMMs). We study how hete"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.22727",
    "domain": "金融",
    "title": "OrderFlowDiT: Transport-Regularized Diffusion Transformer for Probabilistic Limit-Order Supply Forecasting",
    "url": "https://arxiv.org/abs/2610.22727",
    "source": "Jung Hun Phee, Tucker Balch",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T04:00:00+00:00",
    "summary": "arXiv:2610.22727v1 Announce Type: cross Abstract: We study the conditional distribution of limit-order volume submitted over the next five minutes, given the current order book and recent order flow. "
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.22864",
    "domain": "金融",
    "title": "The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization",
    "url": "https://arxiv.org/abs/2610.22864",
    "source": "Hexiao Liu, Lijian Lu, Mingzheng Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T04:00:00+00:00",
    "summary": "arXiv:2610.22864v1 Announce Type: cross Abstract: Digital marketplaces increasingly earn revenue from transaction commissions and seller-facing data services. Sellers may purchase data to increase rev"
  },
  {
    "id": "rss:https://arxiv.org/abs/2510.00244",
    "domain": "金融",
    "title": "Board gender diversity and emissions performance: Insights from panel regressions, machine learning, and explainable AI",
    "url": "https://arxiv.org/abs/2510.00244",
    "source": "Mohammad Hassan Shakil, Arne Johan Pollestad, Khine Kyaw, Ziaul Haque Munim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T04:00:00+00:00",
    "summary": "arXiv:2510.00244v3 Announce Type: replace Abstract: With European Union initiatives mandating gender quotas on corporate boards, a key question arises: Is greater board gender diversity (BGD) associat"
  },
  {
    "id": "rss:https://arxiv.org/abs/2510.20047",
    "domain": "金融",
    "title": "Pricing Generalized Dispersion Swap for Multi-Asset Stochastic Volatility Models",
    "url": "https://arxiv.org/abs/2510.20047",
    "source": "Semere Gebresilassie, Mulue Gebreslasie, Minglian Lin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T04:00:00+00:00",
    "summary": "arXiv:2510.20047v4 Announce Type: replace Abstract: This paper develops a generalized variance framework for pricing multi-asset dispersion swap based on the determinant of the instantaneous covarianc"
  },
  {
    "id": "rss:https://arxiv.org/abs/2601.02554",
    "domain": "金融",
    "title": "AI-exposed jobs deteriorated before ChatGPT",
    "url": "https://arxiv.org/abs/2601.02554",
    "source": "Morgan R. Frank, Alireza Javadian Sabet, Lisa Simon, Sarah H. Bana, Renzhe Yu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T04:00:00+00:00",
    "summary": "arXiv:2601.02554v2 Announce Type: replace Abstract: Public debate links worsening job prospects for AI-exposed occupations to the release of ChatGPT in late 2022. Using monthly U.S. unemployment insur"
  },
  {
    "id": "rss:https://arxiv.org/abs/2602.08527",
    "domain": "金融",
    "title": "Consumption-investment under alternative stochastic-integral conventions",
    "url": "https://arxiv.org/abs/2602.08527",
    "source": "Mario Ayala, Benjamin Vallejo Jim\\'enez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T04:00:00+00:00",
    "summary": "arXiv:2602.08527v2 Announce Type: replace Abstract: We study the Merton consumption-investment problem when risky asset dynamics are written under stochastic-integral conventions indexed by $\\alpha$, "
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.19260",
    "domain": "金融",
    "title": "Understanding the Mechanism of Altruism in Large Language Models",
    "url": "https://arxiv.org/abs/2604.19260",
    "source": "Shuhuai Zhang, Shu Wang, Zijun Yao, Chuanhao Li, Xiaozhi Wang, Songfa Zhong, Tracy Xiao Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T04:00:00+00:00",
    "summary": "arXiv:2604.19260v2 Announce Type: replace Abstract: Altruism is fundamental to human societies, fostering cooperation and social cohesion. While recent studies suggest that large language models (LLMs"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.11093",
    "domain": "金融",
    "title": "Risk Ceilings and Development Deadlines: Pacing AI under Uncertain Safety Productivity",
    "url": "https://arxiv.org/abs/2610.11093",
    "source": "Li Gan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T04:00:00+00:00",
    "summary": "arXiv:2610.11093v2 Announce Type: replace Abstract: Can a regulator promise both a risk ceiling and a development deadline when safety productivity is unknown? A ceiling below the final model's unprot"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.15973",
    "domain": "金融",
    "title": "Requested, Executed and Recoverable Credit: Shared Action Ordering among LLM Borrowers in a Simulated Lending Market",
    "url": "https://arxiv.org/abs/2610.15973",
    "source": "Victoria Ruojie Li",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T04:00:00+00:00",
    "summary": "arXiv:2610.15973v2 Announce Type: replace Abstract: We test whether shared action ordering changes executed credit in a simulated collateralized lending market. Three small open-weight language models"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.21867",
    "domain": "金融",
    "title": "Algorithmic Collusion Without Deterrence: Auditing the Punishment Mechanism in Q-Learning Pricing Agents",
    "url": "https://arxiv.org/abs/2610.21867",
    "source": "Kaue Lopes de Moraes, Rodrigo De-Losso",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T04:00:00+00:00",
    "summary": "arXiv:2610.21867v2 Announce Type: replace Abstract: Independent tabular Q-learning agents repricing in a simulated Bertrand duopoly converge to supracompetitive prices, and the seminal evidence attrib"
  },
  {
    "id": "rss:https://arxiv.org/abs/2307.05470",
    "domain": "金融",
    "title": "A Robust Electric Vehicle Charging Station Optimization under Rare Event Disruptions",
    "url": "https://arxiv.org/abs/2307.05470",
    "source": "Yan Akhra, Iwan Vanany, Mansur Arief",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T04:00:00+00:00",
    "summary": "arXiv:2307.05470v2 Announce Type: replace-cross Abstract: The rising demand for electric vehicles (EVs) requires robust and accessible charging infrastructure, particularly in developing countries whe"
  },
  {
    "id": "rss:https://arxiv.org/abs/2508.14995",
    "domain": "金融",
    "title": "Neural Operators Which Certifiably Simultaneously Solve Infinitely Many Convex Programs using Logarithmic Rank and Linear Complexity",
    "url": "https://arxiv.org/abs/2508.14995",
    "source": "Anastasis Kratsios, Ariel Neufeld, Philipp Schmocker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T04:00:00+00:00",
    "summary": "arXiv:2508.14995v2 Announce Type: replace-cross Abstract: Neural operators (NOs) are a class of deep learning models designed to simultaneously solve infinitely many related problems by casting them i"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.23916",
    "domain": "金融",
    "title": "Advertising to Agents: Measuring Description-Framing Bias in LLM Tool Selection",
    "url": "https://arxiv.org/abs/2605.23916",
    "source": "Haochuan Kevin Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T04:00:00+00:00",
    "summary": "arXiv:2605.23916v3 Announce Type: replace-cross Abstract: AI agents often pick tools from registries, where each provider writes its tool's description; we ask whether sales language there changes whi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.27188",
    "domain": "金融",
    "title": "Inverse Learning of Latent Risk-Neutral Densities from Irregular Option Quotes",
    "url": "https://arxiv.org/abs/2607.27188",
    "source": "Lennon J. Shikhman, Michael Galarnyk, Aadi Dash, Nicholas A. Welsh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T04:00:00+00:00",
    "summary": "arXiv:2607.27188v3 Announce Type: replace-cross Abstract: Accurate option prices do not imply accurate recovery of the latent risk-neutral density. We study this distinction with two complementary ben"
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
  }
]
```
