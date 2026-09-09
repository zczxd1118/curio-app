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

- 今日日期：`2026-09-09`
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
  "date": "2026-09-09",
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
    "id": "bvid:BV1DfrdByE2H",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Agent智能体】教程！大模型入门到进阶，一套全解决！Agentic AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av115897075242856",
    "source": "吴恩达Agent",
    "platform": "bilibili",
    "points": 4481116,
    "published_at": "2026-01-15T03:56:12+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n1. 构建智能体设计模式：反射、工具使用、规划与多智能体工作流；\n2. 将人工智能与外部工具集成：数据库、API、网络搜索与代码执行；\n3. 评估并优化人工智能系统：性能指标、错误分析与生产部署"
  },
  {
    "id": "bvid:BV1BVEs6LENZ",
    "domain": "AI",
    "title": "【2026最新Codex】Codex保姆级完整教程-Codex新手保姆级教程-最强AI助手！从入门到进阶，22分钟速通Codex！【附教程文档安装包】",
    "url": "http://www.bilibili.com/video/av116707129561197",
    "source": "编程大佬陈悠秀",
    "platform": "bilibili",
    "points": 2593502,
    "published_at": "2026-06-07T05:32:32+00:00",
    "summary": "最近Codex的能力越来越全面，变成了Codex四大形态里最强一个。 Codex APP 比起 Claude Code，额度更高，功能更全，免费账户也能用。而且不会出现限速、封号、降智等问题，用过的小伙伴直呼真香。本期视频带来一个Codex APP的完整教程"
  },
  {
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "9分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 1832555,
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
    "points": 1263354,
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
    "points": 1183141,
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
    "points": 1080379,
    "published_at": "2026-05-11T09:02:15+00:00",
    "summary": "文档链接：https://lcnaoyjp4e3z.feishu.cn/wiki/MtJlwX0B5iy6y9k5GZTcdjSknTd"
  },
  {
    "id": "bvid:BV1aeLqzUE6L",
    "domain": "AI",
    "title": "10分钟讲清楚 Prompt, Agent, MCP 是什么",
    "url": "http://www.bilibili.com/video/av114410228025650",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 883358,
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
    "points": 765298,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 731485,
    "published_at": "2026-07-01T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260701\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\nAI大模型开发热门教程：\nAI大模型开发：BV1h1"
  },
  {
    "id": "bvid:BV1aDMezREUj",
    "domain": "AI",
    "title": "Cursor使用教程，2小时玩转cursor，cursor无限续杯",
    "url": "http://www.bilibili.com/video/av114691716154833",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 587818,
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
    "points": 442030,
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
    "points": 408180,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1rBRQBSEwB",
    "domain": "AI",
    "title": "Claude Code+DeepSeek V4 Pro安装教程｜3步从零装好开始用 | Mac Windows",
    "url": "http://www.bilibili.com/video/av116543199385810",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 379862,
    "published_at": "2026-05-09T10:10:00+00:00",
    "summary": "上期vibe coding零基础教程10万多人看了，私信和评论里问最多的居然不是怎么写需求。\n 而是Claude Code怎么装？DeepSeek怎么接进去？🫣\n\n所以这期作为补丁教程，专门帮大家搞定这3件事：\n 1️⃣ 安装Claude Code\n 2️⃣ 把DeepSeek V4 Pro百万上下文满血版接入Claude Code\n 3️⃣ 在VS Code里正式用起来\n\nMac和Windows"
  },
  {
    "id": "bvid:BV1vG8QzcE5X",
    "domain": "AI",
    "title": "Claude使用指南，claude code零基础教程，claude code安装配置到实战",
    "url": "http://www.bilibili.com/video/av114933744272468",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 353919,
    "published_at": "2025-07-30T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从概念到安装，再到Claude Code的具体使用，开发效率原地起飞！"
  },
  {
    "id": "bvid:BV1ia9UBPESQ",
    "domain": "AI",
    "title": "在VScode中配置Claude Code并接入DeepSeek V4 Pro【oo唠嗑教程】",
    "url": "http://www.bilibili.com/video/av116487012549813",
    "source": "沉默的羔丸ovo",
    "platform": "bilibili",
    "points": 328181,
    "published_at": "2026-04-29T08:23:29+00:00",
    "summary": "配置方法如下：\n(想用真心换取你的关注...蟹蟹泥...)\nsetting.json添加：\n{ &quot;name&quot;: &quot;ANTHROPIC_BASE_URL&quot;, &quot;value&quot;: &quot;https://xxxx&quot; }, \n{ &quot;name&quot;: &quot;ANTHROPIC_AUTH_TOKEN&quot;, "
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 284370,
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
    "points": 273814,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 187497,
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
    "points": 180898,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 166141,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 161870,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 111732,
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
    "points": 93615,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1oTkuBoEW5",
    "domain": "AI",
    "title": "业余程序员才Vibe Coding",
    "url": "http://www.bilibili.com/video/av115921586751411",
    "source": "晓舟报告",
    "platform": "bilibili",
    "points": 75152,
    "published_at": "2026-01-21T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1XnuGzfEp7",
    "domain": "AI",
    "title": "让你手中的AI好用10倍！5个好玩实用的MCP推荐，让你不只会用AI搜索",
    "url": "http://www.bilibili.com/video/av114835262018810",
    "source": "田同学Tino",
    "platform": "bilibili",
    "points": 74417,
    "published_at": "2025-07-12T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 54943,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 41617,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operitAI教程：入门安卓最强大ai平台",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 41453,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1XiD5BQEAj",
    "domain": "AI",
    "title": "Claude Code 接入微信、一行命令把Claude Code装进微信、保姆级教程、微信支持Claude Code（cc-connect）远程开发",
    "url": "http://www.bilibili.com/video/av116350093694897",
    "source": "下班学AI",
    "platform": "bilibili",
    "points": 39679,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV1VL3F6pE9K",
    "domain": "AI",
    "title": "0基础入门智能体agent测试：AI测试基础+AI智能体(Agent)测试从零入门全攻略，2026最新版！",
    "url": "http://www.bilibili.com/video/av116991151113881",
    "source": "黑马测试",
    "platform": "bilibili",
    "points": 38372,
    "published_at": "2026-07-27T09:19:37+00:00",
    "summary": "还在卷传统软件测试？2026年必学的AI智能体(Agent)测试来了！本期视频专为0基础小白打造，从软件测试基础讲起...若要本视频配套资源笔记可加up主企微（请看置顶留言最后一句话）。"
  },
  {
    "id": "bvid:BV1cCj2ztEf5",
    "domain": "AI",
    "title": "Cursor+Claude Code+Claude 4终极组合！仅用10分钟为开源项目Magentic-UI完美集成JWT用户认证系统，编程效率提升300%",
    "url": "http://www.bilibili.com/video/av114574527307727",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 35222,
    "published_at": "2025-05-26T14:20:15+00:00",
    "summary": "Cursor+Claude Code+Claude 4终极组合！仅用10分钟为开源项目Magentic-UI完美集成JWT用户认证系统，编程效率提升300%，告别传统开发模式！小白也能轻松开发商业项目\n\n🚀🚀🚀视频简介：\n✅【保姆级教程】从技术栈分析到功能实现：Claude Code完整开发流程深度解析！从零开始为微软开源智能体项目添加完整用户认证功能，支持注册登录退出，让你的AI应用瞬间变身多用"
  },
  {
    "id": "bvid:BV1LXhc6yEkc",
    "domain": "AI",
    "title": "昔涟/Cyrene-Agent 安装配置/演示教程",
    "url": "http://www.bilibili.com/video/av117164694570292",
    "source": "Playa0",
    "platform": "bilibili",
    "points": 33829,
    "published_at": "2026-08-27T00:43:58+00:00",
    "summary": "v1.1.6安装包：\n夸克网盘：\n链接：https://pan.quark.cn/s/43ff3db459f4?pwd=SD2k\n提取码：SD2k\ngithub仓库：\nPlaya-0v0/Cyrene-Agent: An open-source AI desktop companion inspired by Cyrene, combining immersive Chat, personaliz"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29722,
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
    "points": 28923,
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
    "points": 22766,
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
    "points": 21497,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1hmb26ZEws",
    "domain": "AI",
    "title": "DeepSeek Harness 实测  Claude Code 对比后，梁神我错了 差距比我想的大",
    "url": "http://www.bilibili.com/video/av117100337236191",
    "source": "程序员晓刘",
    "platform": "bilibili",
    "points": 21116,
    "published_at": "2026-08-15T16:01:38+00:00",
    "summary": "这期用同一个 DeepSeek Pro 0813 模型，分别在 Claude Code 和 DeepSeek Harness 里完成同样的任务，对比工具链对最终效果的影响。\n实测内容包括：\nFPS 游戏 Demo、灯塔预警沙盘、手枪组装动画、显示器组装动画，以及 DeepSeek Harness 的插件化源码流程。\n整体看下来，模型本身当然重要，但 Harness 在插件化、流程记录、缓存命中和任"
  },
  {
    "id": "bvid:BV1eMgG6QEeG",
    "domain": "AI",
    "title": "【吴恩达】这绝对是把《Vibe Coding》讲得最通透的一套课！手把手教你构建自己的企业级AI工作流，学完直接落地！——附带课件代码",
    "url": "http://www.bilibili.com/video/av117081815189025",
    "source": "吴恩达Agents",
    "platform": "bilibili",
    "points": 19673,
    "published_at": "2026-08-12T09:29:57+00:00",
    "summary": "Vibe Coding火了，但你会发现——AI写的代码像开盲盒，今天能跑明天崩，项目一大就乱套。\n规范驱动开发（SDD） 就是来解决这个问题的。它的核心理念很简单：在让AI写代码之前，先和AI在统一的规范文档里对齐需求，把开发变成可预测、可追溯、可控制的过程。"
  },
  {
    "id": "bvid:BV1iDRQBrEF6",
    "domain": "AI",
    "title": "Claude + Blender 现在太强了 —— 完整免费设置",
    "url": "http://www.bilibili.com/video/av116543333601720",
    "source": "设计之道",
    "platform": "bilibili",
    "points": 16810,
    "published_at": "2026-05-09T07:11:36+00:00",
    "summary": "【简介】\nAnthropic 刚刚发布了用于创意工具的官方 Claude Connectors —— 其中 Blender 连接器对 3D 艺术家来说最重要。在本视频中，我将展示最佳的 Claude + Blender 免费设置，以及为什么这次更新可能会改变我们构建 3D 场景的方式。\n\n【你将学到】\n01:13 步骤 1：安装 Blender MCP 和 Claude Code\n02:31 步骤"
  },
  {
    "id": "bvid:BV1zbduYgEBH",
    "domain": "AI",
    "title": "Cursor新手教程⑤：Cursor降智真相+解决办法",
    "url": "http://www.bilibili.com/video/av114311359891940",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 10930,
    "published_at": "2025-04-10T02:53:27+00:00",
    "summary": "你是不是经常碰到这种情况：\n你试图修复一个小错误\n人工智能给出一个看似合理的更改建议\n这个修复导致其他地方出错\n你要求人工智能修复新出现的问题\n这又产生了另外两个问题\n如此反复\n本视频带你拆解Cursor降智的真相以及解决办法"
  },
  {
    "id": "bvid:BV1xh3C6cEGv",
    "domain": "AI",
    "title": "两周完成一篇SCI论文，用claude code帮你干",
    "url": "http://www.bilibili.com/video/av117002408559933",
    "source": "博士大师兄木水",
    "platform": "bilibili",
    "points": 9571,
    "published_at": "2026-07-29T08:53:04+00:00",
    "summary": "大师兄八股文SCI速成模板已制作成skill，手把手带你实现一键生成SCI论文初稿"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 9497,
    "published_at": "2025-04-14T02:30:00+00:00",
    "summary": "MCP服务网站：https://smithery.ai/\nCherry Studio官方网站：https://cherry-ai.com/"
  },
  {
    "id": "bvid:BV12MEg6pE9o",
    "domain": "AI",
    "title": "【乐鑫教程】乐鑫文档 MCP 服务器上线，现已支持微信登录！",
    "url": "http://www.bilibili.com/video/av116713957956440",
    "source": "乐鑫信息科技",
    "platform": "bilibili",
    "points": 9164,
    "published_at": "2026-06-08T10:17:31+00:00",
    "summary": "手把手教你如何使用最新乐鑫文档知识库，帮你在 Claude / Cursor 等平台解答问题、生成代码、迁移 ESP-IDF 版本、烧录固件。 MCP 服务器现已支持微信扫码一键登录，快来一试！\n\n视频重点内容包括👇：\n\n- 如何将 MCP 服务器添加到 VS Code\n- 让 Copilot 基于乐鑫文档对比旧版和最新版 I2C 驱动\n- 驱动迁移\n- Copilot 编译代码、烧录代码并监控输"
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 7851,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1QU6GYFEio",
    "domain": "AI",
    "title": "[课程4] 用Cursor开发数据库真的很简单 | Agent应用 | 用Codebase解决跨文件错误",
    "url": "http://www.bilibili.com/video/av113742109021318",
    "source": "Zhu的AI日记",
    "platform": "bilibili",
    "points": 7027,
    "published_at": "2024-12-31T12:30:00+00:00",
    "summary": "***这是全网最完整的分享如何在不懂编程的情况下，利用结构化思维，用Cursor开发商业app的系列课程。\n《懒人记单词》是基于艾宾浩斯遗忘曲线设计的记单词神器，它可以对每一个单词进行人性化的解读，并在每一个遗忘周期到来时及时提醒，并通过单词释义选择，拼写和造句进行全方位的巩固，同时AI还能对你的句子进行多维度的评估，确保你对每一个单词不仅会认，而且会用。\n\n***你将在本视频中学到：\n1.数据库"
  },
  {
    "id": "bvid:BV1aSR4BKESW",
    "domain": "AI",
    "title": "安卓手机部署Claude Code",
    "url": "http://www.bilibili.com/video/av116526891993752",
    "source": "中国小骑士",
    "platform": "bilibili",
    "points": 6983,
    "published_at": "2026-05-06T09:24:14+00:00",
    "summary": "通过Termux安装Claude Code并且接入国内大模型"
  },
  {
    "id": "bvid:BV1fNs9eiEm9",
    "domain": "AI",
    "title": "Cursor AI编程结合cocos3.8游戏开发教程-01",
    "url": "http://www.bilibili.com/video/av113187471105975",
    "source": "太阳8800",
    "platform": "bilibili",
    "points": 6759,
    "published_at": "2024-09-23T15:15:13+00:00",
    "summary": "开源源码仓库\nhttps://gitee.com/gamepublic/chess-cards"
  },
  {
    "id": "bvid:BV13cmnBFEP9",
    "domain": "AI",
    "title": "Claude Code教程9：Claude Code与GitHub的高效联动",
    "url": "http://www.bilibili.com/video/av115689541077475",
    "source": "木乐乐的异想世界",
    "platform": "bilibili",
    "points": 5601,
    "published_at": "2025-12-09T12:17:23+00:00",
    "summary": "【Claude Code教程第9集中文翻译】Net Ninja带你解锁Claude Code与GitHub的高效联动！本集聚焦实用核心功能：无需复杂配置，在Claude聊天会话中即可设置GitHub集成——安装后自动创建两个关键GitHub Action：①自动审查拉取请求（PR）并给出精准反馈；②当仓库问题提及Claude时，自动在新功能分支处理该问题。注意：需先安装GitHub CLI（附官方"
  },
  {
    "id": "bvid:BV1cMtz6EEKL",
    "domain": "AI",
    "title": "【2026版】B站讲的最好的Vibe Coding企业级项目实战教程，七天入门到进阶速通Claude Code+Codex+CursorAI工程化编程开发！",
    "url": "http://www.bilibili.com/video/av117211888884484",
    "source": "图灵课堂",
    "platform": "bilibili",
    "points": 5384,
    "published_at": "2026-09-04T08:47:29+00:00",
    "summary": "整理制作不易，大家记得点个关注，一键三连呀【点赞、收藏、转发】感谢支持~\nJava+AI200万字面试宝典+场景题，简历模板，Java P 5~P8技术栈学习路线自取：https://www.bilibili.com/opus/765026283734171673?spm_id_from=333.1387.0.0"
  },
  {
    "id": "bvid:BV1jWcvzmEzc",
    "domain": "AI",
    "title": "Houdini干货|houdini自己的AI agent（agent工具推荐分享）",
    "url": "http://www.bilibili.com/video/av116057012505638",
    "source": "tinywang_",
    "platform": "bilibili",
    "points": 5326,
    "published_at": "2026-02-12T09:45:41+00:00",
    "summary": "原作者教程：https://www.bilibili.com/video/BV1pwcbzBEEh/?spm_id_from=333.1387.list.card_archive.click&amp;vd_source=da5aa377b2acefadd001ffd4902eca9b\n\nGithub download：https://github.com/Kazama-Suichiku/Houdi"
  },
  {
    "id": "hn:49458161",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia agrees to acquire Hugging Face for $13B",
    "url": "https://www.businessinsider.com/nvidia-in-talks-to-buy-hugging-face-13-billion-dollars-2026-8",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 1988,
    "published_at": "2026-08-27T01:12:55+00:00",
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
    "id": "hn:49466052",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia projects $673B in sales as AI demand widens",
    "url": "https://forgeeks.net/nvidia-673-billion-ai-growth-forecast/",
    "source": "kuuuzya",
    "platform": "hackernews",
    "points": 111,
    "published_at": "2026-08-27T15:04:16+00:00",
    "summary": ""
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
    "id": "hn:49469249",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Starts Pac as AI Chip Maker Builds DC Influence Force",
    "url": "https://news.bgov.com/bloomberg-government-news/nvidia-starts-a-pac-as-ai-chip-maker-buids-influence-force-in-dc",
    "source": "rarisma",
    "platform": "hackernews",
    "points": 91,
    "published_at": "2026-08-27T18:34:40+00:00",
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
    "id": "rss:https://www.eetimes.com/strategy-paper-urges-canada-to-add-semiconductors-to-ai-strategy/",
    "domain": "AI 算力 / 半导体",
    "title": "Strategy Paper Urges Canada to Add Semiconductors to AI Strategy",
    "url": "https://www.eetimes.com/strategy-paper-urges-canada-to-add-semiconductors-to-ai-strategy/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T19:00:00+00:00",
    "summary": "Canada’s sovereign AI ambitions will fall short unless procurement, talent, funding, and existing semiconductor strengths are aligned behind domestic hardware capability. The post Strategy Paper Urges"
  },
  {
    "id": "rss:https://www.eetimes.com/the-pragmatic-path-to-achieving-cra-compliance-and-securing-your-access-to-the-eu-market/",
    "domain": "AI 算力 / 半导体",
    "title": "The Pragmatic Path to Achieving CRA Compliance and Securing Your Access to the EU Market",
    "url": "https://www.eetimes.com/the-pragmatic-path-to-achieving-cra-compliance-and-securing-your-access-to-the-eu-market/",
    "source": "MediaTek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T14:39:23+00:00",
    "summary": "As the EU Cyber Resilience Act (CRA) approaches, IoT manufacturers face stringent cybersecurity requirements across the entire product lifecycle. MediaTek, together with our strategic partners, invite"
  },
  {
    "id": "rss:https://www.eetimes.com/the-security-ai-that-learns-the-language-of-movement/",
    "domain": "AI 算力 / 半导体",
    "title": "The Security AI That Learns the Language of Movement",
    "url": "https://www.eetimes.com/the-security-ai-that-learns-the-language-of-movement/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T13:15:17+00:00",
    "summary": "UNC Charlotte researchers use edge AI to learn normal motion, predict what comes next, and flag anomalies for human review. The post The Security AI That Learns the Language of Movement appeared first"
  },
  {
    "id": "rss:https://www.eetimes.com/powering-high-precision-lasers/",
    "domain": "AI 算力 / 半导体",
    "title": "Powering High Precision Lasers",
    "url": "https://www.eetimes.com/powering-high-precision-lasers/",
    "source": "P-DUKE",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T13:00:00+00:00",
    "summary": "Today, no one can imagine life without the vast number of laser applications, ranging from milliwatt-class lasers to high-power processing. The post Powering High Precision Lasers appeared first on EE"
  },
  {
    "id": "rss:https://www.eetimes.com/how-much-impact-will-ai-have-on-iot-software-engineering/",
    "domain": "AI 算力 / 半导体",
    "title": "How Much Impact Will AI Have on IoT Software Engineering?",
    "url": "https://www.eetimes.com/how-much-impact-will-ai-have-on-iot-software-engineering/",
    "source": "Steve Bennett",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T08:06:55+00:00",
    "summary": "In theory, AI is a surefire way to raise productivity in software engineering, but the reality may not be quite so cut-and-dried. The post How Much Impact Will AI Have on IoT Software Engineering? app"
  },
  {
    "id": "rss:https://www.eetimes.com/nvidia-acquires-huggingface-for-12-9b/",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Acquires HuggingFace for $12.9B",
    "url": "https://www.eetimes.com/nvidia-acquires-huggingface-for-12-9b/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T15:58:00+00:00",
    "summary": "The open-source model hub will be acquired by the world’s biggest compute provider. The post Nvidia Acquires HuggingFace for $12.9B appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/why-microcooling-will-be-a-critical-enabler-of-agentic-ai/",
    "domain": "AI 算力 / 半导体",
    "title": "Why Microcooling Will Be a Critical Enabler of Agentic AI",
    "url": "https://www.eetimes.com/why-microcooling-will-be-a-critical-enabler-of-agentic-ai/",
    "source": "Mike Housholder",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T13:19:14+00:00",
    "summary": "Agentic AI won’t thrive on raw compute alone; tiny devices need microcooling to beat heat and sustain intelligence. The post Why Microcooling Will Be a Critical Enabler of Agentic AI appeared first on"
  },
  {
    "id": "rss:https://www.eetimes.com/why-holistic-digital-twins-are-needed-to-accelerate-sdv-development/",
    "domain": "AI 算力 / 半导体",
    "title": "Why Holistic Digital Twins are Needed to Accelerate SDV Development",
    "url": "https://www.eetimes.com/why-holistic-digital-twins-are-needed-to-accelerate-sdv-development/",
    "source": "Heather Campbell, Marketing Director for PAVE360, Siemens EDA",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T13:00:00+00:00",
    "summary": "Discover how holistic digital twins help automakers shift left, overcome integration complexity and accelerate modern software-defined vehicle development. The post Why Holistic Digital Twins are Need"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/tsmc-to-start-using-high-na-euv-lithography-in-2030-a10-or-a11-technology-prime-candidates-for-use",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC to start using High-NA EUV lithography in 2030 — A10 or A11 technology prime candidates for use",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/tsmc-to-start-using-high-na-euv-lithography-in-2030-a10-or-a11-technology-prime-candidates-for-use",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T15:00:00+00:00",
    "summary": "TSMC discloses plans to use High-NA EUV lithography in 2030, 6×12-inch photomasks with new scanners in 2033."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-reportedly-set-to-hike-cpu-prices-by-10-percent-ahead-of-major-annual-product-launch-in-march-2027-report-says-amd-will-follow-up-between-june-and-july",
    "domain": "AI 算力 / 半导体",
    "title": "Intel reportedly set to hike CPU prices by 10% ahead of 'major annual product' launch in March 2027 — report says AMD will follow up between June and July",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-reportedly-set-to-hike-cpu-prices-by-10-percent-ahead-of-major-annual-product-launch-in-march-2027-report-says-amd-will-follow-up-between-june-and-july",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T14:18:42+00:00",
    "summary": "Intel is reportedly set to raise CPU prices by 10%, following two other price increases, as it prepares for a major product launch in March 2027."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/benchmarking-qwen-3-8-27b-on-rtx-5090-and-beyond-vram-capacity-alone-cant-overcome-severe-software-and-inference-engine-bottlenecks",
    "domain": "AI 算力 / 半导体",
    "title": "Benchmarking Qwen 3.8 27B on RTX 5090 and beyond — VRAM capacity alone can't overcome severe software and inference engine bottlenecks",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/benchmarking-qwen-3-8-27b-on-rtx-5090-and-beyond-vram-capacity-alone-cant-overcome-severe-software-and-inference-engine-bottlenecks",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T13:30:02+00:00",
    "summary": "Following the release of Qwen 3.8 27B, we put our trusty hardware to the test to see which hardware might be best suited for running this open-weight AI model."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/super-smash-bros-melee-gets-fully-decompiled-after-over-six-years-of-effort-ambitious-and-technically-impressive-project-delivers-gamecube-classic-as-c-code",
    "domain": "AI 算力 / 半导体",
    "title": "Super Smash Bros Melee gets fully decompiled after over six years of effort — ambitious and technically impressive project delivers GameCube classic as C code",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/super-smash-bros-melee-gets-fully-decompiled-after-over-six-years-of-effort-ambitious-and-technically-impressive-project-delivers-gamecube-classic-as-c-code",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T12:57:45+00:00",
    "summary": "A Super Smash Bros Melee decompilation project hit its key long-standing goal a few hours ago."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/sony-threatens-to-cut-off-customer-support-and-pursue-legal-action-over-harassment-as-backlash-to-playstations-physical-disc-phaseout-intensifies-company-to-move-forward-with-no-disc-decision-despite-several-lawsuits",
    "domain": "AI 算力 / 半导体",
    "title": "Sony threatens to cut off customer support and pursue legal action over harassment as backlash to PlayStation’s physical-disc phaseout intensifies — company to move forward with no disc decision despi",
    "url": "https://www.tomshardware.com/video-games/playstation/sony-threatens-to-cut-off-customer-support-and-pursue-legal-action-over-harassment-as-backlash-to-playstations-physical-disc-phaseout-intensifies-company-to-move-forward-with-no-disc-decision-despite-several-lawsuits",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T12:20:00+00:00",
    "summary": "Sony Japan has introduced a customer-harassment policy as anger continues over PlayStation’s plan to phase out physical game discs by 2028."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/all-in-one-dlss-unlocked-mod-brings-dlss-5-and-multi-frame-gen-to-rtx-20-30-and-40-series-hybrid-tool-taps-amd-fsr-3-1-to-boost-frame-rates-up-to-6x",
    "domain": "AI 算力 / 半导体",
    "title": "All-in-one 'DLSS Unlocked' mod brings DLSS 5 and multi-frame gen to RTX 20, 30, and 40 series — hybrid tool taps AMD FSR 3.1 to boost frame rates up to 6X",
    "url": "https://www.tomshardware.com/pc-components/gpus/all-in-one-dlss-unlocked-mod-brings-dlss-5-and-multi-frame-gen-to-rtx-20-30-and-40-series-hybrid-tool-taps-amd-fsr-3-1-to-boost-frame-rates-up-to-6x",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T12:00:00+00:00",
    "summary": "Performance for the mod remains untested but just the sheer utility of DLSS Unlocked easily puts it at the top of the RTX GPUs mod list. It combines OptiScaler_DLSSNR with DLSS Enabled to bring neural"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/quantum-computing/nec-has-quietly-quit-quantum-computing-hardware-development-report-claims-company-says-it-will-continue-to-evaluate-practical-applications-and-industrialization-of-quantum-technologies",
    "domain": "AI 算力 / 半导体",
    "title": "NEC has quietly quit quantum computing hardware development, report claims — company says it will continue to evaluate practical applications and industrialization of quantum technologies",
    "url": "https://www.tomshardware.com/tech-industry/quantum-computing/nec-has-quietly-quit-quantum-computing-hardware-development-report-claims-company-says-it-will-continue-to-evaluate-practical-applications-and-industrialization-of-quantum-technologies",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T11:45:00+00:00",
    "summary": "NEC reportedly quits development of quantum computers, but plans to explore practical applications for such systems."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/vintage-emulator-studio-recreates-44-legendary-synths-down-to-the-chip-level-free-mame-powered-component-level-emulation-should-offer-exceedingly-accurate-sound",
    "domain": "AI 算力 / 半导体",
    "title": "Vintage Emulator Studio recreates 44 legendary synths down to the chip level — free MAME-powered component-level emulation should offer exceedingly accurate sound",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/vintage-emulator-studio-recreates-44-legendary-synths-down-to-the-chip-level-free-mame-powered-component-level-emulation-should-offer-exceedingly-accurate-sound",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T11:40:00+00:00",
    "summary": "Vintage Emulator Studio brings iconic vintage synths and samplers to life — MAME-powered component-level emulation should offer exceedingly accurate sound"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cryptocurrency/hackers-drain-usd320-million-in-bitcoin-from-liquid-network-emptying-roughly-95-percent-of-federation-wallet-attackers-claim-theyre-the-good-guys-and-will-return-funds-after-the-vulnerability-is-fixed",
    "domain": "AI 算力 / 半导体",
    "title": "Hackers drain $320 million in Bitcoin from Liquid Network, emptying roughly 95% of federation wallet — attackers claim they’re the ‘good guys’ and will return funds after the vulnerability is fixed",
    "url": "https://www.tomshardware.com/tech-industry/cryptocurrency/hackers-drain-usd320-million-in-bitcoin-from-liquid-network-emptying-roughly-95-percent-of-federation-wallet-attackers-claim-theyre-the-good-guys-and-will-return-funds-after-the-vulnerability-is-fixed",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T11:20:00+00:00",
    "summary": "Hackers claiming to be white hats drained about $320 million in Bitcoin from Liquid Network’s federation wallet, promising to return the funds after the platform fixes the underlying bug"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/programming/google-maps-entire-brain-and-central-nervous-system-of-adult-male-fruit-fly-software-engineers-immediately-make-it-run-doom-ai-powered-3d-model-of-over-166-000-neurons-can-also-play-super-mario-64",
    "domain": "AI 算力 / 半导体",
    "title": "Google maps entire brain and central nervous system of adult male fruit fly, software engineers immediately make it run Doom — AI-powered 3D model of over 166,000 neurons can also play Super Mario 64",
    "url": "https://www.tomshardware.com/software/programming/google-maps-entire-brain-and-central-nervous-system-of-adult-male-fruit-fly-software-engineers-immediately-make-it-run-doom-ai-powered-3d-model-of-over-166-000-neurons-can-also-play-super-mario-64",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T11:06:26+00:00",
    "summary": "Scientists mapped the complete brain and central nervous system of an adult male fruit fly for the first time. Days later the full MaleCNS v1.0 fruit fly connectome was being trained to play Doom and "
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/get-a-32gb-ddr5-gaming-pc-for-just-usd1-379-at-newegg-usd420-discount-includes-20-core-intel-cpu-and-rtx-5060",
    "domain": "AI 算力 / 半导体",
    "title": "Get a 32GB DDR5 gaming PC for just $1,379 at Newegg — $420 discount includes 20-core Intel CPU and RTX 5060",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/get-a-32gb-ddr5-gaming-pc-for-just-usd1-379-at-newegg-usd420-discount-includes-20-core-intel-cpu-and-rtx-5060",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T11:02:34+00:00",
    "summary": "Save over $400 on this DDR5 gaming PC with RTX 5060 and Core i7-14700F."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ddr5/this-usd389-32gb-ddr5-ram-kit-is-the-cheapest-on-sale-right-now-for-a-gaming-pc-upgrade-higher-spec-ram-for-usd415-gives-pc-builders-rare-choice-as-the-ai-boom-continues-to-force-memory-prices-higher",
    "domain": "AI 算力 / 半导体",
    "title": "This $389 32GB DDR5 RAM kit is the cheapest on sale right now for a gaming PC upgrade — higher-spec RAM for $415 gives PC builders rare choice as the AI boom continues to force memory prices higher",
    "url": "https://www.tomshardware.com/pc-components/ddr5/this-usd389-32gb-ddr5-ram-kit-is-the-cheapest-on-sale-right-now-for-a-gaming-pc-upgrade-higher-spec-ram-for-usd415-gives-pc-builders-rare-choice-as-the-ai-boom-continues-to-force-memory-prices-higher",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T11:00:24+00:00",
    "summary": "These DDR5 32GB memory kits are the cheapest you'll find on sale right now, starting at $389."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/thailand-asks-datacenter-operators-to-suspend-buildouts-until-legal-framework-is-complete-new-legislation-is-supposed-to-create-airtight-requirements-for-large-scale-datacenters",
    "domain": "AI 算力 / 半导体",
    "title": "Thailand asks data center operators to suspend 49 buildouts until legal framework is complete — new legislation is supposed to create 'airtight' requirements for large-scale data centers",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/thailand-asks-datacenter-operators-to-suspend-buildouts-until-legal-framework-is-complete-new-legislation-is-supposed-to-create-airtight-requirements-for-large-scale-datacenters",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T11:00:00+00:00",
    "summary": "Thailand asks datacenter operators to suspend buildouts until legal framework is complete — new legislation is supposed to create \"airtight\" requirements for large-scale datacenters"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/german-scammer-dupes-two-different-buyers-into-spending-thousands-on-hollow-rtx-5090-gpus-stripped-out-cards-netted-fraudster-usd5-000-despite-being-worthless",
    "domain": "AI 算力 / 半导体",
    "title": "German scammer dupes two different buyers into spending thousands on hollow RTX 5090 GPUs — stripped-out cards netted fraudster $5,000 despite being worthless",
    "url": "https://www.tomshardware.com/pc-components/gpus/german-scammer-dupes-two-different-buyers-into-spending-thousands-on-hollow-rtx-5090-gpus-stripped-out-cards-netted-fraudster-usd5-000-despite-being-worthless",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T10:30:00+00:00",
    "summary": "Graphics card scams without the core and memory chips are spreading worldwide, with the latest report coming from Germany."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/one-slot-low-profile-nvidia-rtx-3060-12-gb-with-two-monitor-outputs-breaks-cover-at-newegg-for-usd496-bus-powered-model-looking-for-a-use-case-in-local-llm-work",
    "domain": "AI 算力 / 半导体",
    "title": "One-slot, low-profile Nvidia RTX 3060 12 GB with two monitor outputs breaks cover at Newegg for $496 — bus-powered model looking for a use case in local LLM work",
    "url": "https://www.tomshardware.com/pc-components/gpus/one-slot-low-profile-nvidia-rtx-3060-12-gb-with-two-monitor-outputs-breaks-cover-at-newegg-for-usd496-bus-powered-model-looking-for-a-use-case-in-local-llm-work",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T10:15:00+00:00",
    "summary": "Small-form-factor, low-profile Nvidia RTX 3060 12 GB with two monitor outputs breaks cover at Newegg for $496 — bus-powered model looking for a use case in local LLM work"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ddr4/tech-enthusiast-finds-usd12-000-stack-of-ram-in-their-garage-work-let-them-keep-an-old-server-stuffed-with-1-920gb-of-ddr4",
    "domain": "AI 算力 / 半导体",
    "title": "Tech enthusiast finds $12,000 stack of RAM in their garage — work let them keep an old server stuffed with 1,920GB of DDR4",
    "url": "https://www.tomshardware.com/pc-components/ddr4/tech-enthusiast-finds-usd12-000-stack-of-ram-in-their-garage-work-let-them-keep-an-old-server-stuffed-with-1-920gb-of-ddr4",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T10:00:00+00:00",
    "summary": "A computing enthusiast found a fat stack of DDR4 RAM sticks that might be worth $10,000 in their garage."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/belgian-chinese-semiconductor-researcher-arrested-over-alleged-gan-trade-secret-theft-prosecutors-suspect-belgan-insiders-transferred-chip-ip-to-china-before-the-company-collapsed",
    "domain": "AI 算力 / 半导体",
    "title": "Belgian-Chinese semiconductor researcher arrested over alleged GaN trade-secret theft — prosecutors suspect BelGaN insiders transferred chip IP to China before the company collapsed",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/belgian-chinese-semiconductor-researcher-arrested-over-alleged-gan-trade-secret-theft-prosecutors-suspect-belgan-insiders-transferred-chip-ip-to-china-before-the-company-collapsed",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T09:50:00+00:00",
    "summary": "Belgian authorities have arrested a former BelGaN researcher on suspicion of industrial espionage, alleging that proprietary gallium nitride semiconductor technology was transferred to a Chinese rival"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/intel-surpasses-one-million-high-na-euv-wafers-processed-outpaces-the-rest-of-the-industry-combined-company-also-trailblazing-giant-6-12-photomasks-to-speed-production-and-lower-costs1",
    "domain": "AI 算力 / 半导体",
    "title": "Intel surpasses one million High-NA EUV wafers processed, outpaces the rest of the industry combined — company also trailblazing giant 6×12 photomasks to speed production and lower costs",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/intel-surpasses-one-million-high-na-euv-wafers-processed-outpaces-the-rest-of-the-industry-combined-company-also-trailblazing-giant-6-12-photomasks-to-speed-production-and-lower-costs1",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T06:00:00+00:00",
    "summary": "Intel is leading the semiconductor industry with High-NA fleet and process-maturity milestone as it reaches 1 million wafers processed using High-NA tools, moves forward with 6×12 photomask effort."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/arm-debuts-next-gen-semi-custom-neoverse-css-n4-ranger-platform-compute-subsystem-packs-up-to-128-cores-per-die-on-tsmc-n3p",
    "domain": "AI 算力 / 半导体",
    "title": "Arm debuts next-gen semi-custom Neoverse CSS N4 ‘Falcon' platform — compute subsystem packs up to 128 cores per die on TSMC N3P",
    "url": "https://www.tomshardware.com/pc-components/cpus/arm-debuts-next-gen-semi-custom-neoverse-css-n4-ranger-platform-compute-subsystem-packs-up-to-128-cores-per-die-on-tsmc-n3p",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T02:00:00+00:00",
    "summary": "Arm’s new Neoverse CSS N4 platform can pack up to 128 cores per die and 256 MB of L3 cache, representing a large increase in support over the previous Neoverse CSS N2 platform."
  },
  {
    "id": "rss:https://www.tomshardware.com/gift-guides-seasonal-sales/save-up-to-38-percent-on-a-new-gaming-pc-before-the-labor-day-sales-end-and-beat-the-price-rises-lock-down-last-minute-savings-on-new-pre-built-rigs-from-best-buy-newegg-and-walmart",
    "domain": "AI 算力 / 半导体",
    "title": "Save up to 38% on a new gaming PC before the Labor Day sales end and beat the price rises — lock down last-minute savings on new pre-built rigs from Best Buy, Newegg, and Walmart",
    "url": "https://www.tomshardware.com/gift-guides-seasonal-sales/save-up-to-38-percent-on-a-new-gaming-pc-before-the-labor-day-sales-end-and-beat-the-price-rises-lock-down-last-minute-savings-on-new-pre-built-rigs-from-best-buy-newegg-and-walmart",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T16:00:16+00:00",
    "summary": "Labor Day is nearly over, but there's still an opportunity to save hundreds on a new gaming PC before the prices rise again."
  },
  {
    "id": "rss:https://www.tomshardware.com/maker-stem/xtool-reveals-its-next-generation-of-lasers-modular-x1-supports-co2-diode-uv-fiber-and-mopa-lasers",
    "domain": "AI 算力 / 半导体",
    "title": "xTool reveals its next generation of lasers — modular X1 supports CO2, Diode, UV, Fiber, and MOPA lasers",
    "url": "https://www.tomshardware.com/maker-stem/xtool-reveals-its-next-generation-of-lasers-modular-x1-supports-co2-diode-uv-fiber-and-mopa-lasers",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T14:05:05+00:00",
    "summary": "The X1 will combine gantry and galvo technology in one machine."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/openais-gpt-6-astra-model-autonomously-completes-portal-in-24-hours-feat-cost-just-usd571-in-tokens",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI’s GPT-6 Astra model autonomously completes Portal in 24 hours — feat cost just $571 in tokens",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/openais-gpt-6-astra-model-autonomously-completes-portal-in-24-hours-feat-cost-just-usd571-in-tokens",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T13:25:56+00:00",
    "summary": "An AI enthusiast has conducted an experiment where OpenAI's new GPT-6 Astra played through the entirety of Valve's Portal 3D puzzler game on its own."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/astonishing-mod-runs-nvidia-dlss-5-on-a-second-gpu-using-a-reshade-add-on-to-reduce-performance-impact-boosts-neural-rendered-fps-up-to-127-percent-game-renders-on-one-card-neural-post-processing-runs-on-the-other-much-like-dedicated-physx-gpus",
    "domain": "AI 算力 / 半导体",
    "title": "Astonishing mod runs DLSS 5 on a second GPU to boost neural-rendered FPS up to 127% — game renders on one card, neural post-processing runs on the other, much like dedicated PhysX GPUs",
    "url": "https://www.tomshardware.com/pc-components/gpus/astonishing-mod-runs-nvidia-dlss-5-on-a-second-gpu-using-a-reshade-add-on-to-reduce-performance-impact-boosts-neural-rendered-fps-up-to-127-percent-game-renders-on-one-card-neural-post-processing-runs-on-the-other-much-like-dedicated-physx-gpus",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T12:33:56+00:00",
    "summary": "A modder has created a ReShade add-on that runs Nvidia's DLSS 5 Neural Rendering on a second GPU, rendering the game on the first GPU to share the performance load."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/power-supplies/montech-century-ii-gold-850w-atx-3-1-power-supply-review",
    "domain": "AI 算力 / 半导体",
    "title": "Montech Century II Gold 850W power supply review: Excellent budget-friendly Gold-tier ATX 3.1 unit with Cybenetics Platinum efficiency",
    "url": "https://www.tomshardware.com/pc-components/power-supplies/montech-century-ii-gold-850w-atx-3-1-power-supply-review",
    "source": "E. Fylladitakis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T12:05:00+00:00",
    "summary": "At $90, the Montech Century II Gold 850W ATX 3.1 is a low-cost Gold-tier ATX 3.1 unit with a native 12V-2x6 connector, Cybenetics Platinum efficiency at both 115V and 230V input, and a matte silver ch"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/gta-vice-city-and-gta-iii-return-to-web-browsers-after-a-dmca-takedown-open-source-reverse-engineering-brings-the-classics-to-the-web-with-over-100-fps-performance",
    "domain": "AI 算力 / 半导体",
    "title": "GTA Vice City and GTA III return to web browsers after a DMCA takedown — Open-source reverse engineering brings the classics to the web with over 100 FPS performance",
    "url": "https://www.tomshardware.com/video-games/gta-vice-city-and-gta-iii-return-to-web-browsers-after-a-dmca-takedown-open-source-reverse-engineering-brings-the-classics-to-the-web-with-over-100-fps-performance",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T11:30:00+00:00",
    "summary": "You can play GTA: Vice City and GTA III in your browser right now across pretty much any modern device. The projects are compiled from source codes of the original games and are available on either DO"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/anycubic-photon-p1-max-review",
    "domain": "AI 算力 / 半导体",
    "title": "Anycubic Photon P1 MAX review: bigger, better, and tech-packed",
    "url": "https://www.tomshardware.com/3d-printing/anycubic-photon-p1-max-review",
    "source": "Matt Farmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T11:05:00+00:00",
    "summary": "Anycubic’s Photon P1 MAX is the latest large resin printer, with new tech alongside its little brother, the P1. It sports a heated vat, Wave Release Technology, and a large, locking build plate and va"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/this-10-inch-4-3-television-hides-your-retro-consoles-in-a-secret-rear-compartment-unicos-traveller-ulw10-trades-composite-video-for-rgb-scart-and-hdmi",
    "domain": "AI 算力 / 半导体",
    "title": "This 10-inch 4:3 television hides your retro consoles in a secret rear compartment — Unico's Traveller ULW10 trades composite video for RGB SCART and HDMI",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/this-10-inch-4-3-television-hides-your-retro-consoles-in-a-secret-rear-compartment-unicos-traveller-ulw10-trades-composite-video-for-rgb-scart-and-hdmi",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T11:00:00+00:00",
    "summary": "The ULW10 Traveller offers retro gamers a compact alternative to modern widescreen TVs, complete with a 4:3 display and CRT-style visuals"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/start-your-3d-printing-journey-for-just-usd169-with-these-elegoo-printers-before-labor-day-ends-lock-in-up-to-35-percent-off-the-easy-to-use-neptune-3-pro-or-go-large-with-the-neptune-4-plus-for-massive-model-printing",
    "domain": "AI 算力 / 半导体",
    "title": "Start your 3D printing journey for just $169 with these Elegoo printers before Labor Day ends — lock in up to 35% off the easy-to-use Neptune 3 Pro or go large with the Neptune 4 Plus for massive mode",
    "url": "https://www.tomshardware.com/3d-printing/start-your-3d-printing-journey-for-just-usd169-with-these-elegoo-printers-before-labor-day-ends-lock-in-up-to-35-percent-off-the-easy-to-use-neptune-3-pro-or-go-large-with-the-neptune-4-plus-for-massive-model-printing",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T10:50:54+00:00",
    "summary": "Grab a huge discount on two of Elegoo's most popular 3D printers right now, with a price drop of up to 35%. Both the Elegoo Neptune 3 Pro and Neptune 4 Plus offer features that both beginners and enth"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/rpcs3-emulator-can-now-run-games-on-pc-directly-from-a-disc-drive-in-landmark-development-unlocks-20-years-of-physical-ps3-games-on-windows-linux-and-macos",
    "domain": "AI 算力 / 半导体",
    "title": "RPCS3 emulator can now run PS3 games on PC directly from a disc drive in landmark development — unlocks 20 years of physical titles on Windows, Linux, and macOS",
    "url": "https://www.tomshardware.com/video-games/playstation/rpcs3-emulator-can-now-run-games-on-pc-directly-from-a-disc-drive-in-landmark-development-unlocks-20-years-of-physical-ps3-games-on-windows-linux-and-macos",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T10:47:25+00:00",
    "summary": "The developers of the Sony PlayStation 3 emulator RPCS3 have told their social media followers that it is now possible to play games straight from discs."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/flea-market-shopper-uncovers-usd1-500-worth-of-samsung-ssds-inside-a-usd30-expansion-card-three-2tb-980-pro-drives-were-hidden-beneath-an-asus-hyper-m-2-heatsink",
    "domain": "AI 算力 / 半导体",
    "title": "Flea market shopper uncovers $1,500 worth of Samsung SSDs inside a $30 expansion card — Three 2TB 980 Pro drives were hidden beneath an Asus Hyper M.2 heatsink",
    "url": "https://www.tomshardware.com/pc-components/ssds/flea-market-shopper-uncovers-usd1-500-worth-of-samsung-ssds-inside-a-usd30-expansion-card-three-2tb-980-pro-drives-were-hidden-beneath-an-asus-hyper-m-2-heatsink",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T10:30:00+00:00",
    "summary": "An extremely fortunate bargain hunter in Kuwait found three Samsung 980 Pro 2TB SSDs slotted inside a $30 PCIe expansion card. Each of those drives is worth between $400 and $500, so it's clear to say"
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
    "id": "rss:https://www.eetimes.com/kioxias-flash-for-dram-initiative-eyes-ai-workloads/",
    "domain": "AI 算力 / 半导体",
    "title": "Kioxia’s Flash-for-DRAM Initiative Eyes AI Workloads",
    "url": "https://www.eetimes.com/kioxias-flash-for-dram-initiative-eyes-ai-workloads/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T08:01:30+00:00",
    "summary": "The CXL-attached memory expansion uses NAND flash optimized for high-speed processing alongside AI compute devices. The post Kioxia&#8217;s Flash-for-DRAM Initiative Eyes AI Workloads appeared first o"
  },
  {
    "id": "hn:49552616",
    "domain": "AI 算力 / 半导体",
    "title": "Launch HN: Mireye (YC S26) – Infrastructure for Physical World AI Agents",
    "url": "https://news.ycombinator.com/item?id=49552616",
    "source": "anshchokshi",
    "platform": "hackernews",
    "points": 28,
    "published_at": "2026-09-03T16:24:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:49480449",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Insists It Can Keep Printing Money to Fund the AI Boom",
    "url": "https://www.wsj.com/tech/ai/nvidia-insists-it-can-keep-printing-money-to-fund-the-ai-boom-195e7d5e",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 46,
    "published_at": "2026-08-28T15:57:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:49447878",
    "domain": "AI 算力 / 半导体",
    "title": "Who bears the risk in Nvidia's $500B financing platform?",
    "url": "https://www.sascha-steffen.de/updates/nvidia-500bn-ai-financing-credit-risk",
    "source": "rwmj",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-08-26T12:32:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:49537553",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.8 Flash and 3.8 Flash Cyber",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/",
    "source": "bratao",
    "platform": "hackernews",
    "points": 1159,
    "published_at": "2026-09-02T15:12:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:49289112",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.7 Flash",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/",
    "source": "thisisauserid",
    "platform": "hackernews",
    "points": 968,
    "published_at": "2026-08-13T17:23:22+00:00",
    "summary": ""
  },
  {
    "id": "hn:49611251",
    "domain": "大厂 AI 动态",
    "title": "AlphaGenome Atlas: a high-resolution map of human DNA",
    "url": "https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphagenome-atlas/",
    "source": "utiiiD",
    "platform": "hackernews",
    "points": 549,
    "published_at": "2026-09-08T14:55:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:49552299",
    "domain": "大厂 AI 动态",
    "title": "WeatherNext 3",
    "url": "https://deepmind.google/science/weathernext/",
    "source": "matthieu_bl",
    "platform": "hackernews",
    "points": 404,
    "published_at": "2026-09-03T16:06:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:49331423",
    "domain": "大厂 AI 动态",
    "title": "AI-Generated GitHub Copilot “Autofix” Allowed Compromise of Snowflake's Jira",
    "url": "https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug",
    "source": "galnagli",
    "platform": "hackernews",
    "points": 424,
    "published_at": "2026-08-17T14:18:38+00:00",
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
    "id": "hn:49267928",
    "domain": "大厂 AI 动态",
    "title": "llama.cpp",
    "url": "https://llama.app",
    "source": "kristianpaul",
    "platform": "hackernews",
    "points": 364,
    "published_at": "2026-08-12T04:51:59+00:00",
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
    "id": "hn:49259339",
    "domain": "大厂 AI 动态",
    "title": "Apple Silicon and macOS VMs: Faster LLM Inference with llama.cpp",
    "url": "https://github.com/trycua/cua/blob/main/blog/gpu-passthrough-macos-vms.md",
    "source": "frabonacci",
    "platform": "hackernews",
    "points": 307,
    "published_at": "2026-08-11T14:50:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:49602490",
    "domain": "大厂 AI 动态",
    "title": "Emacs Bedrock 2.0",
    "url": "https://lambdaland.org/posts/2026-09-06-bedrock-v2/",
    "source": "ashton314",
    "platform": "hackernews",
    "points": 184,
    "published_at": "2026-09-07T20:12:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:49256057",
    "domain": "大厂 AI 动态",
    "title": "What I learned by putting GitHub Copilot behind a MitM proxy",
    "url": "https://www.lighthousenewsletter.com/p/i-put-github-copilot-behind-a-mitm",
    "source": "j0selit0",
    "platform": "hackernews",
    "points": 200,
    "published_at": "2026-08-11T10:40:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:49610641",
    "domain": "大厂 AI 动态",
    "title": "AlphaGenome Atlas predictive map of every DNA letter change in the human genome",
    "url": "https://deepmind.google/blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/",
    "source": "fady0",
    "platform": "hackernews",
    "points": 83,
    "published_at": "2026-09-08T14:14:15+00:00",
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
    "id": "hn:49566788",
    "domain": "大厂 AI 动态",
    "title": "Project HydraFusion: Frontier quality via multi-model orchestration",
    "url": "https://github.blog/ai-and-ml/github-copilot/project-hydrafusion-frontier-quality-via-multi-model-orchestration/",
    "source": "qainsights",
    "platform": "hackernews",
    "points": 79,
    "published_at": "2026-09-04T16:24:50+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/tech/991884/apple-iphone-duo-rumor-foldable",
    "domain": "大厂 AI 动态",
    "title": "Apple’s foldable ‘iPhone Duo’ will reportedly start at $2,000",
    "url": "https://www.theverge.com/tech/991884/apple-iphone-duo-rumor-foldable",
    "source": "Richard Lawler",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T05:26:53+00:00",
    "summary": "With only a few hours left until the first iPhone launch event since John Ternus took over as the CEO of Apple, Bloomberg reporter Mark Gurman says the name of the company's long-rumored folding phone"
  },
  {
    "id": "rss:https://www.theverge.com/games/991806/sony-disc-plant-90-percent-10-percent",
    "domain": "大厂 AI 动态",
    "title": "Sony isn’t phasing out discs quite as quickly as we thought",
    "url": "https://www.theverge.com/games/991806/sony-disc-plant-90-percent-10-percent",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T21:52:13+00:00",
    "summary": "Sony isn't backing away from its decision to kill the video game disc in January 2028. But Sony isn't shutting down production as quickly as we thought, either. Two months after reports that Sony's la"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/991710/openai-navier-stokes-solution",
    "domain": "大厂 AI 动态",
    "title": "Drama swirls around OpenAI’s legendary mathematical milestone",
    "url": "https://www.theverge.com/ai-artificial-intelligence/991710/openai-navier-stokes-solution",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T20:53:52+00:00",
    "summary": "OpenAI says it found a solution to a major math problem that has remained unsolved for around 90 years, as reported earlier by The New York Times and Wired. In a blog post on Tuesday, OpenAI announced"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/991707/rivian-also-tmb-ebike-delay-apology",
    "domain": "大厂 AI 动态",
    "title": "Rivian spinout Also apologizes for delays in shipping futuristic e-bikes",
    "url": "https://www.theverge.com/transportation/991707/rivian-also-tmb-ebike-delay-apology",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T20:46:56+00:00",
    "summary": "Rivian's futuristic e-bike is delayed, and customers are not happy. Last year, Rivian's micromobility spinoff Also unveiled a new, software-controlled electric bike called the TM-B that immediately se"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/991653/razer-blackshark-v3-pro-gaming-headset-anc-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Razer’s ANC-equipped gaming headset for PS5 and Xbox is almost $100 off",
    "url": "https://www.theverge.com/gadgets/991653/razer-blackshark-v3-pro-gaming-headset-anc-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T20:39:49+00:00",
    "summary": "It’s rare to find high-end features like active noise cancellation in a gaming headset under $200, so we’re thrilled that the Razer BlackShark V3 Pro on sale at Woot for $164.99. There are specific mo"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/991727/openai-chatgpt-images-2-5-sketch",
    "domain": "大厂 AI 动态",
    "title": "ChatGPT Sketch turns your bad drawings into detailed AI images",
    "url": "https://www.theverge.com/ai-artificial-intelligence/991727/openai-chatgpt-images-2-5-sketch",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T20:16:09+00:00",
    "summary": "OpenAI announced ChatGPT Images 2.5 on Tuesday and is adding a new way to tell ChatGPT what you want it to make an image of: by drawing a doodle. With a new feature called Sketch, you can just draw so"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/991216/meta-bets-on-ai-agent-muse-to-catch-up-in-ai-race",
    "domain": "大厂 AI 动态",
    "title": "Meta bets on AI agent Muse to catch up in AI race",
    "url": "https://www.theverge.com/ai-artificial-intelligence/991216/meta-bets-on-ai-agent-muse-to-catch-up-in-ai-race",
    "source": "Robert Hart",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T19:00:00+00:00",
    "summary": "Meta is making another push to bring artificial intelligence to the masses with Muse, a personal assistant it says can put AI in the hands of virtually anyone. The product is the latest step in a mult"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/990313/anthropic-class-action-lawsuit-pricing-subscription-plans",
    "domain": "大厂 AI 动态",
    "title": "AI power users claim Anthropic duped them with subscriptions, and they’re taking it to court",
    "url": "https://www.theverge.com/ai-artificial-intelligence/990313/anthropic-class-action-lawsuit-pricing-subscription-plans",
    "source": "Hayden Field",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T17:27:31+00:00",
    "summary": "Anthropic says power users are key to its business - it's prioritized them even when it means cutting off other popular applications, like OpenClaw. But some of these same customers say Anthropic misl"
  },
  {
    "id": "rss:https://www.theverge.com/games/991484/zelda-ocarina-of-time-gta-6",
    "domain": "大厂 AI 动态",
    "title": "Nintendo isn’t scared of GTA VI",
    "url": "https://www.theverge.com/games/991484/zelda-ocarina-of-time-gta-6",
    "source": "Andrew Webster",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T17:13:51+00:00",
    "summary": "There's never really been a game like Grand Theft Auto VI before, one that has completely altered the lineup of games around it. Everyone, it seems, is scared of going up against Grand Theft Auto VI. "
  },
  {
    "id": "rss:https://www.theverge.com/transportation/991400/tesla-cybercab-virtual-joystick-manual-control",
    "domain": "大厂 AI 动态",
    "title": "Tesla Cybercab doesn’t have any manual controls — but it does have a virtual joystick",
    "url": "https://www.theverge.com/transportation/991400/tesla-cybercab-virtual-joystick-manual-control",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T16:06:56+00:00",
    "summary": "The Tesla Cybercab is notable for what it lacks, namely a steering wheel and pedal. By design, there is no way for this vehicle to be manually controlled - or so we thought. Less than a week after the"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/08/google-deepmind-alumni-are-building-tools-to-accelerate-fusion-power-for-the-grid/",
    "domain": "大厂 AI 动态",
    "title": "Google DeepMind alumni are building tools to accelerate fusion power for the grid",
    "url": "https://techcrunch.com/2026/09/08/google-deepmind-alumni-are-building-tools-to-accelerate-fusion-power-for-the-grid/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T06:00:00+00:00",
    "summary": "Fusionality is developing control systems and simulation environments to help fusion power startups move faster."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/08/cloudnc-raises-20m-to-automate-manufacturings-most-pressing-bottlenecks/",
    "domain": "大厂 AI 动态",
    "title": "CloudNC raises $20M to automate manufacturing’s most pressing bottlenecks",
    "url": "https://techcrunch.com/2026/09/08/cloudnc-raises-20m-to-automate-manufacturings-most-pressing-bottlenecks/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T04:01:00+00:00",
    "summary": "UK-based manufacturing software startup CloudNC announced Wednesday a $20 million B extension round, bringing its lifetime total raised amount to $128 million."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/08/white-house-takes-down-build-the-wall-game-after-the-tetris-company-complains/",
    "domain": "大厂 AI 动态",
    "title": "White House takes down ‘Build the Wall’ game after the Tetris Company complains",
    "url": "https://techcrunch.com/2026/09/08/white-house-takes-down-build-the-wall-game-after-the-tetris-company-complains/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T23:23:23+00:00",
    "summary": "The Trump administration's short-lived arcade game \"Build the Wall\" is now nowhere to be found after the Tetris Company posted that it takes \"copyright infringement very seriously.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/08/hackers-are-stealing-claude-tokens-from-subscribers/",
    "domain": "大厂 AI 动态",
    "title": "Hackers are stealing Claude tokens from subscribers",
    "url": "https://techcrunch.com/2026/09/08/hackers-are-stealing-claude-tokens-from-subscribers/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T21:10:27+00:00",
    "summary": "Last month, a Claude user noticed his account was consuming tokens even though he wasn't working. Anthropic has since warned users about hackers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/08/cognition-hits-48b-valuation-signaling-investors-believe-ai-coding-is-far-from-a-winner-take-all-market/",
    "domain": "大厂 AI 动态",
    "title": "Cognition hits $48B valuation, signaling investors believe AI coding is far from a winner-take-all market",
    "url": "https://techcrunch.com/2026/09/08/cognition-hits-48b-valuation-signaling-investors-believe-ai-coding-is-far-from-a-winner-take-all-market/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T21:04:06+00:00",
    "summary": "Cognition's valuation multiple is higher than Cursor's was before selling to SpaceX."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/08/the-exploration-company-nabs-450-million-to-challenge-spacex/",
    "domain": "大厂 AI 动态",
    "title": "The Exploration Company nabs $450 million to challenge SpaceX",
    "url": "https://techcrunch.com/2026/09/08/the-exploration-company-nabs-450-million-to-challenge-spacex/",
    "source": "Anna Heim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T20:47:34+00:00",
    "summary": "The Exploration Company (TEC) has raised $450 million to build reusable spacecraft, in what it describes as “the largest-ever Series C by a European space company.”"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/08/meta-debuts-its-muse-ai-agent-will-consumers-trust-it/",
    "domain": "大厂 AI 动态",
    "title": "Meta debuts its Muse AI agent. Will consumers trust it?",
    "url": "https://techcrunch.com/2026/09/08/meta-debuts-its-muse-ai-agent-will-consumers-trust-it/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T19:00:00+00:00",
    "summary": "Meta's new personal AI agent Muse wants access to users' email, calendars, payments, health services, and more — making the company's biggest consumer AI bet yet a major test of whether people still t"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/08/how-to-watch-apples-foldable-iphone-announcement/",
    "domain": "大厂 AI 动态",
    "title": "How to watch Apple’s foldable iPhone announcement",
    "url": "https://techcrunch.com/2026/09/08/how-to-watch-apples-foldable-iphone-announcement/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T17:46:53+00:00",
    "summary": "Apple's annual iPhone event will stream live on September 9 at 10 a.m. PDT, and we're expecting big news."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/08/openai-fought-dirty-on-career-making-math-problem-says-nyu-mathematician/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI fought dirty on career-making math problem, says NYU mathematician",
    "url": "https://techcrunch.com/2026/09/08/openai-fought-dirty-on-career-making-math-problem-says-nyu-mathematician/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T17:32:15+00:00",
    "summary": "There is a $1 million bounty for the first person providing a solution to the Navier-Stokes existence and smoothness problem."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/08/google-cloud-races-to-catch-up-in-the-ai-deployment-wars-with-accenture-deal/",
    "domain": "大厂 AI 动态",
    "title": "Google Cloud races to catch up in the AI deployment wars with Accenture deal",
    "url": "https://techcrunch.com/2026/09/08/google-cloud-races-to-catch-up-in-the-ai-deployment-wars-with-accenture-deal/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T16:20:31+00:00",
    "summary": "Google Cloud expands its enterprise AI push with Accenture, betting on forward-deployed engineers to drive adoption and overcome deployment bottlenecks."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/08/googles-revived-nuclear-power-plant-gets-1-9b-loan-from-us-government/",
    "domain": "大厂 AI 动态",
    "title": "Google’s revived nuclear power plant gets $1.9B loan from US government",
    "url": "https://techcrunch.com/2026/09/08/googles-revived-nuclear-power-plant-gets-1-9b-loan-from-us-government/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T15:25:35+00:00",
    "summary": "Google said it would bring an Iowa nuclear power plant back from the dead. Now the plant's owner is getting a $1.9 billion loan from the U.S. Energy Department."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/08/chrome-is-now-shipping-updates-every-2-weeks-as-ai-changes-the-security-landscape/",
    "domain": "大厂 AI 动态",
    "title": "Chrome is now shipping updates every 2 weeks as AI changes the security landscape",
    "url": "https://techcrunch.com/2026/09/08/chrome-is-now-shipping-updates-every-2-weeks-as-ai-changes-the-security-landscape/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T15:04:09+00:00",
    "summary": "Google is speeding up Chrome’s release schedule to ship security patches and new features faster."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/08/mistral-raises-e3b-as-sovereign-ai-becomes-big-business/",
    "domain": "大厂 AI 动态",
    "title": "Mistral raises €3B as sovereign AI becomes big business",
    "url": "https://techcrunch.com/2026/09/08/mistral-raises-e3b-as-sovereign-ai-becomes-big-business/",
    "source": "Anna Heim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T14:17:48+00:00",
    "summary": "The French AI lab has raised €3 billion at a €21 billion valuation in a Series D round led by Samsung, Scaleup Europe, and PSG Equity."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/08/a-hacker-stole-340m-in-a-crypto-heist-then-returned-most-of-it/",
    "domain": "大厂 AI 动态",
    "title": "A hacker stole $340M in a crypto heist, then returned most of it",
    "url": "https://techcrunch.com/2026/09/08/a-hacker-stole-340m-in-a-crypto-heist-then-returned-most-of-it/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T14:11:29+00:00",
    "summary": "The latest heist is one of the largest thefts of cryptocurrency to date."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/08/nuclear-startup-bluecore-energy-raises-50m-seed-round-just-two-months-after-launch/",
    "domain": "大厂 AI 动态",
    "title": "Nuclear startup Bluecore Energy raises $50M seed round, just two months after launch",
    "url": "https://techcrunch.com/2026/09/08/nuclear-startup-bluecore-energy-raises-50m-seed-round-just-two-months-after-launch/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T14:10:17+00:00",
    "summary": "Bluecore Energy announced Tuesday an oversubscribed $50 million seed round — just months after raising a $10 million pre-seed and coming out of stealth."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/08/poseidon-aerospace-lands-60m-ahead-of-first-pilotless-test-flight/",
    "domain": "大厂 AI 动态",
    "title": "Poseidon Aerospace lands $60M ahead of first pilotless test flight",
    "url": "https://techcrunch.com/2026/09/08/poseidon-aerospace-lands-60m-ahead-of-first-pilotless-test-flight/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T13:00:00+00:00",
    "summary": "The startup is trying to rethink the economics of cargo aircraft by removing pilots from the equation entirely."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/08/stoke-space-raises-another-billion-to-rival-spacex-at-re-flying-rockets/",
    "domain": "大厂 AI 动态",
    "title": "Stoke Space raises another billion to rival SpaceX at re-flying rockets",
    "url": "https://techcrunch.com/2026/09/08/stoke-space-raises-another-billion-to-rival-spacex-at-re-flying-rockets/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T09:00:00+00:00",
    "summary": "Stoke has \"completed the initial closing\" of a $1B Series E round intended to help it reach orbit and prepare a new, larger rocket for operations."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/07/eric-wus-newest-company-out-of-stealth-since-may-is-going-after-constructions-labor-crunch/",
    "domain": "大厂 AI 动态",
    "title": "Eric Wu’s newest company, out of stealth since May, is going after construction’s labor crunch",
    "url": "https://techcrunch.com/2026/09/07/eric-wus-newest-company-out-of-stealth-since-may-is-going-after-constructions-labor-crunch/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T02:16:39+00:00",
    "summary": "Eric Wu, who built and ran Opendoor before stepping away in 2022, has had his new company, NavigateAI, out of stealth since May — building AI copilots that give construction workers real-time, hands-f"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/07/artificial-intelligence-definition-glossary-hallucinations-guide-to-common-ai-terms/",
    "domain": "大厂 AI 动态",
    "title": "Opaque recurrence, and other AI terms that you should probably know",
    "url": "https://techcrunch.com/2026/09/07/artificial-intelligence-definition-glossary-hallucinations-guide-to-common-ai-terms/",
    "source": "Natasha Lomas, Romain Dillet, Kyle Wiggers, Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T19:24:00+00:00",
    "summary": "The rise of AI has brought an avalanche of new terms and slang. Here is a glossary with definitions of some of the most important words and phrases you might encounter."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/07/a-secret-new-elizabeth-holmes-documentary-stuns-telluride/",
    "domain": "大厂 AI 动态",
    "title": "A secret new Elizabeth Holmes documentary stuns Telluride",
    "url": "https://techcrunch.com/2026/09/07/a-secret-new-elizabeth-holmes-documentary-stuns-telluride/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T18:02:29+00:00",
    "summary": "Nathan Fielder and Lance Oppenheim's secret Elizabeth Holmes documentary, \"You Can See Everything,\" stunned Telluride audiences Sunday night with its generous access to the Theranos founder."
  },
  {
    "id": "rss:https://stratechery.com/2026/write-things-down/",
    "domain": "大厂 AI 动态",
    "title": "Write Things Down",
    "url": "https://stratechery.com/2026/write-things-down/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T10:00:00+00:00",
    "summary": "Writing things down is powerful, for humans and for AI; what comes first, however, is what to write, why to do it, and actually getting things done."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/09/lg-tv-shown-capable-of-tracking-user-activity-even-when-offline/",
    "domain": "大厂 AI 动态",
    "title": "LG TV shown scanning LAN for third-party phones and other devices",
    "url": "https://arstechnica.com/gadgets/2026/09/lg-tv-shown-capable-of-tracking-user-activity-even-when-offline/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T21:52:29+00:00",
    "summary": "“It doesn’t cost a lot to store text forever.”"
  },
  {
    "id": "rss:https://arstechnica.com/gaming/2026/09/gog-brings-back-big-box-pc-games-one-printable-template-at-a-time/",
    "domain": "大厂 AI 动态",
    "title": "GOG brings back \"big box\" PC games, one printable template at a time",
    "url": "https://arstechnica.com/gaming/2026/09/gog-brings-back-big-box-pc-games-one-printable-template-at-a-time/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T21:23:13+00:00",
    "summary": "Preservation \"goodies\" also includes downloadable 3D models for desktop perusal."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/09/microsoft-patches-a-record-972-vulnerabilities-112-of-them-critical/",
    "domain": "大厂 AI 动态",
    "title": "Why this month's Microsoft patch release is a doozy",
    "url": "https://arstechnica.com/security/2026/09/microsoft-patches-a-record-972-vulnerabilities-112-of-them-critical/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T21:11:46+00:00",
    "summary": "Security gnomes are pumping out patches ahead of an expected onslaught of AI-assisted attacks."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/09/astronaut-on-iss-celebrates-60-years-of-star-trek-with-prop-badge/",
    "domain": "大厂 AI 动态",
    "title": "The universal language of space is... Star Trek? Mais oui.",
    "url": "https://arstechnica.com/space/2026/09/astronaut-on-iss-celebrates-60-years-of-star-trek-with-prop-badge/",
    "source": "Robert Pearlman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T20:20:20+00:00",
    "summary": "\"Science fiction imagines the future. We build it.\""
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/09/nih-to-use-part-of-its-budget-to-pay-for-department-of-defense-research/",
    "domain": "大厂 AI 动态",
    "title": "NIH to use part of its budget to pay for Department of Defense research",
    "url": "https://arstechnica.com/science/2026/09/nih-to-use-part-of-its-budget-to-pay-for-department-of-defense-research/",
    "source": "John Timmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T20:06:44+00:00",
    "summary": "Money would ostensibly fund research the NIH leadership said it no longer wanted."
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
    "id": "wscn:3781389",
    "domain": "股票",
    "title": "美伊军事冲突升级，布油冲破百元关口，美股欧股承压，金银齐升",
    "url": "https://wallstreetcn.com/articles/3781389",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T07:49:31+00:00",
    "summary": "布伦特原油自7月24日以来首次触及每桶100美元，日内涨幅超2%。WTI原油涨近2%，报94.73美元/桶。标普500指数期货几乎持平，欧洲斯托克600指数下跌0.4%。日元兑美元报153.40，涨幅0.4%。"
  },
  {
    "id": "wscn:3781400",
    "domain": "股票",
    "title": "OpenAI解出千禧年数学难题后，Altman下一目标：攻克室温超导？",
    "url": "https://wallstreetcn.com/articles/3781400",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T07:47:48+00:00",
    "summary": "OpenAI用约1万个并发AI智能体、历时88小时，给出了困扰数学界百年的数学难题——纳维-斯托克斯方程存在性与光滑性问题的解决方案。此外，Sam Altman暗示：下一个目标，是用同样的万级智能体协作方式寻找室温超导体。AI科研边界，正在以肉眼可见的速度向外扩张。"
  },
  {
    "id": "wscn:3781397",
    "domain": "股票",
    "title": "PPI见顶后：下半场的轨迹",
    "url": "https://wallstreetcn.com/articles/3781397",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T07:12:51+00:00",
    "summary": "国联民生宏观认为，8月PPI同比阶段性回升并非物价下行趋势反转，而是油价反弹、AI产业链高景气与基数效应共同作用的结果。预计6月4.1%已是年内高点，9月或现阶段性“小高峰”，随后四季度重回缓步回落轨道。"
  },
  {
    "id": "wscn:3781396",
    "domain": "股票",
    "title": "OpenAI高管：Astra需求太猛，新的Pro订阅或被迫暂停",
    "url": "https://wallstreetcn.com/articles/3781396",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T06:15:50+00:00",
    "summary": "OpenAI产品负责人Tibo表示，对Astra的需求真的是史无前例的。优先事项始终是为现有用户保持优质服务，但如果这种情况持续下去，我们可能不得不暂时暂停新的Pro订阅。"
  },
  {
    "id": "wscn:3781394",
    "domain": "股票",
    "title": "日元这轮反弹不靠干预靠资本回流？挪威主权基金固收配置或从美债转向日债",
    "url": "https://wallstreetcn.com/articles/3781394",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T05:58:02+00:00",
    "summary": "本轮日元升值并非源于官方干预，而是由极度拥挤的空头平仓与真实的资本回流共同驱动。在挪威主权基金调整配置及日本机构预期抛售海外资产的催化下，加上日本实际薪资转正与加息预期升温，长期主导全球的日元套息交易逻辑正在瓦解，日元升值趋势具备持续性。"
  },
  {
    "id": "wscn:3781393",
    "domain": "股票",
    "title": "日元强势引发多空分歧：对冲基金看涨至140，散户逆势加码空头",
    "url": "https://wallstreetcn.com/articles/3781393",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T05:50:46+00:00",
    "summary": "外汇市场正上演一场罕见多空对决。日元本月已升值约4%，对冲基金竞相布局看涨期权，激进者押注年内美元兑日元跌至140；而日本散户却逆势持有逾3.6万亿日元净空头，若被迫集中平仓，将形成共振效应进一步放大日元涨势。日本央行加息预期叠加美财长表态支持日元升值，这场多空博弈正进入最关键的决战窗口。"
  },
  {
    "id": "wscn:3781379",
    "domain": "股票",
    "title": "A股三大股指午后集体翻绿，煤炭、航运爆发，光通信活跃、长飞光纤一度涨停，恒科指跌1%，海底捞大跌10%",
    "url": "https://wallstreetcn.com/articles/3781379",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T05:31:16+00:00",
    "summary": "盘面上，个股跌多涨少，沪深京三市约3500股飘绿，上午半天成交1.22万亿。沪深两市半日成交额1.21万亿，较上个交易日缩量超460亿。板块方面，光通信指数冲高回落，海运、煤炭、覆铜板、培育钻石、军工板块走强，传媒、地产、医药板块调整。"
  },
  {
    "id": "wscn:3781391",
    "domain": "股票",
    "title": "欧央行9月加息已无悬念：紧缩周期是否结束？",
    "url": "https://wallstreetcn.com/premium/articles/3781391?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T04:39:11+00:00",
    "summary": "欧央行9月加息已充分定价，终端利率预期分歧加剧，能源与财政风险决定后续紧缩空间。"
  },
  {
    "id": "wscn:3781366",
    "domain": "股票",
    "title": "标普料SK海力士四季度再启最高40万亿韩元回购，叠加丰厚股息，韩国Value-up行情再获新催化",
    "url": "https://wallstreetcn.com/articles/3781366",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T04:05:17+00:00",
    "summary": "标普全球市场情报预测，SK海力士有望于今年四季度宣布20万亿至40万亿韩元新一轮股票回购计划，受此提振，其ADR周二大涨超6%，周三韩股股价一度涨5%。标普指出，结合三星电子注销库存股及巨额分红，两大巨头有望为韩国资本市场树立公司治理新标杆，助力破解长期\"韩国折价\"困局。"
  },
  {
    "id": "wscn:3781377",
    "domain": "股票",
    "title": "30万亿知识工作、30万亿消费市场--驾驭AI推理时代",
    "url": "https://wallstreetcn.com/articles/3781377",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T03:54:31+00:00",
    "summary": "摩根士丹利认为AI将重塑20-30万亿美元知识工作市场与30万亿美元消费市场，企业AI支出2027年或达8000亿美元。开源模型压低Token价格，引发需求爆炸式增长；多条变现路径回报率达25%-50%。全球算力容量将从35GW激增至145GW，但电力与监管瓶颈成为下一阶段最关键的物理约束。"
  },
  {
    "id": "wscn:3781384",
    "domain": "股票",
    "title": "Amazon牵手Qualcomm，AI算力开始告别“英伟达单中心时代”",
    "url": "https://wallstreetcn.com/premium/articles/3781384?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T03:49:32+00:00",
    "summary": "Amazon与Qualcomm达成覆盖定制芯片与高速互联的长期合作，最高600亿美元的潜在采购规模，使定制ASIC再次成为AI算力市场的焦点。\n云厂商正在主动构建多架构、多供应商的计算体系，AI数据中心由单一GPU平台向异构计算演进的趋势进一步清晰。\n对资本市场而言，下一阶段值得重估的，是GPU与ASIC并存之后，产业链价值量将向哪些环节重新分配。"
  },
  {
    "id": "wscn:3781390",
    "domain": "股票",
    "title": "摩根士丹利：日元升值不足以颠覆新兴市场套利交易",
    "url": "https://wallstreetcn.com/articles/3781390",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T03:32:46+00:00",
    "summary": "日元升至半年高位、加息预期升温，套利交易承压——但摩根士丹利并不为此动摇。策略师指出，新兴市场套利交易的真正命门在于全球增长与股市表现，而非日元单边走势；投资者已转向欧元、瑞郎分散融资来源，策略韧性显著增强。"
  },
  {
    "id": "wscn:3781388",
    "domain": "股票",
    "title": "高盛TMT大会实录：OpenAI头部客户用量是普通客户8倍，“按成果收费”将取代“按Token收费”",
    "url": "https://wallstreetcn.com/articles/3781388",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T03:03:58+00:00",
    "summary": "高盛、花旗TMT双峰会同日开幕，一线信息密集释放。OpenAI企业收入年化环比增加32%，顶级客户token消耗量已是普通客户8倍；OpenAI定价路线是订阅→按用量→按成果；AMD三大锚定客户需求超预期，制约在供给而非需求；博通CEO挺千亿AI营收路径，每吉瓦电力撬动300亿美元年化收入。"
  },
  {
    "id": "wscn:3781368",
    "domain": "股票",
    "title": "花旗TMT会议：NPO抢跑，CPO瓶颈是测试，光互联是“下一个HBM",
    "url": "https://wallstreetcn.com/articles/3781368",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T03:03:11+00:00",
    "summary": "花旗记录了Lightmatter管理层访谈要点。管理层表示，NPO（近封装光学）将于2027年入市、2028年大规模普及，CPO规模化时间线维持2028-2029年不变。管理层将激光器和光纤定性为\"下一个HBM\"，供给紧张预期支撑稀缺溢价。CPO瓶颈在于测试产能而非技术本身，相关测试设备存在被低估的投资机会。"
  },
  {
    "id": "wscn:3781387",
    "domain": "股票",
    "title": "DCI超级周期：康宁长单锁到2032年，光纤真的供不应求？",
    "url": "https://wallstreetcn.com/premium/articles/3781387?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T03:02:22+00:00",
    "summary": "从GPU机房走向“国家级骨干网”——AI光通信投资边界的第二次扩张。"
  },
  {
    "id": "wscn:3781373",
    "domain": "股票",
    "title": "9月加息，美联储最不坏的选择？",
    "url": "https://wallstreetcn.com/articles/3781373",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T02:54:31+00:00",
    "summary": "非农数据爆表推升美联储9月加息概率至60%，沃什深陷\"辜负市场\"还是\"辜负特朗普\"的两难。申银万国警告，2015年以来加息预期超40%从未落空，并且市场高加息预期在CPI数据公布后大概率难以消退。若美联储此次破例，期限溢价恐遭反噬。但若加息落地且路径不大幅上修，冲击或比市场预期温和得多。"
  },
  {
    "id": "wscn:3781383",
    "domain": "股票",
    "title": "Anthropic研究员因“失控”AI担忧辞职，安全隐忧蔓延顶级实验室",
    "url": "https://wallstreetcn.com/articles/3781383",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T02:47:28+00:00",
    "summary": "Anthropic研究员Jacob Coxon以\"AI将失控\"为由愤而辞职，警告最快明年底局面便已无法挽回。同日，OpenAI首席科学家高呼全球减速、递归自我改进里程碑数据同步公开，AI安全裂口骤然撕大。更棘手的是，这场关乎人类命运的博弈，正在监管真空中加速奔跑。"
  },
  {
    "id": "wscn:3781314",
    "domain": "股票",
    "title": "日元急涨破153：升值空间还有多大？套利交易危险吗？",
    "url": "https://wallstreetcn.com/premium/articles/3781314?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T02:45:14+00:00",
    "summary": "日元急升源于政策预期与空头平仓，套利风险升高但未必崩盘，后续升值空间看下周美日央行会议。"
  },
  {
    "id": "wscn:3781385",
    "domain": "股票",
    "title": "具身智能融资开始抢“大脑”，千诀科技三个月连融两轮",
    "url": "https://wallstreetcn.com/articles/3781385",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T02:31:53+00:00",
    "summary": "具身智能的热钱，正在从机器人本体进一步流向“大脑”。\n 日前，千诀科技宣布完成数亿元A+轮融资，元禾..."
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
    "id": "hn:49473629",
    "domain": "股票",
    "title": "Alphabet stock sheds $700B as AI bills climb",
    "url": "https://www.semafor.com/article/08/27/2026/alphabet-stock-sheds-700b-as-ai-bills-climb",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 49,
    "published_at": "2026-08-28T02:23:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:49335271",
    "domain": "股票",
    "title": "30-year Treasury yield tops 5.31%, the highest in 19 years",
    "url": "https://www.cnbc.com/2026/08/17/treasury-yields-federal-reserve-fomc-minutes.html",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 63,
    "published_at": "2026-08-17T18:14:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:49511824",
    "domain": "股票",
    "title": "Apple Is Suddenly an AI Infra Stock as OpenAI Buys 10k+ Macs",
    "url": "https://247wallst.com/investing/2026/08/31/apple-is-suddenly-an-ai-infrastructure-stock-as-openai-buys-macs-by-the-tens-of-thousands/",
    "source": "prabal97",
    "platform": "hackernews",
    "points": 41,
    "published_at": "2026-08-31T16:44:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:49323620",
    "domain": "股票",
    "title": "Anthropic IPO valuation hinges on $190-200B 2028 revenue forecast",
    "url": "https://www.reuters.com/business/anthropic-ipo-valuation-hinges-190-200-billion-2028-revenue-forecast-sources-say-2026-08-15/",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-08-16T21:00:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:49468651",
    "domain": "股票",
    "title": "US Patriot missile stocks in Europe are 'beyond critical' due to Iran war",
    "url": "https://apnews.com/article/patriot-missiles-iran-war-russia-ukraine-trump-09c7d8030a2e11fbd8ee3f7176b3f2d4",
    "source": "hn_acker",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-08-27T17:54:03+00:00",
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
    "id": "hn:49261857",
    "domain": "股票",
    "title": "The SpaceX Sham",
    "url": "https://dissentmagazine.org/online_articles/spacex-ipo-elon-musk-trillionaire/",
    "source": "cdrnsf",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-08-11T17:47:03+00:00",
    "summary": ""
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
    "id": "hn:49455629",
    "domain": "股票",
    "title": "150 Years of Global Stock Returns – The Birthplace Lottery",
    "url": "https://beyondpassive.substack.com/p/150-years-of-global-stock-returns",
    "source": "rzk",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-08-26T20:43:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:49342823",
    "domain": "股票",
    "title": "OpenAI disbanded the team that assessed catastrophic model risks",
    "url": "https://thenextweb.com/news/openai-preparedness-team-disbanded-ipo-streamlining",
    "source": "nyku",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-08-18T08:06:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:49311379",
    "domain": "股票",
    "title": "OpenAI talent exodus raises 'huge red flag' ahead of IPO",
    "url": "https://www.cnbc.com/2026/08/14/open-ai-ipo-red-flag.html",
    "source": "pseudolus",
    "platform": "hackernews",
    "points": 28,
    "published_at": "2026-08-15T15:25:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:49253785",
    "domain": "股票",
    "title": "OpenAI wraps $7B share sale ahead of potential IPO",
    "url": "https://www.cnbc.com/2026/08/10/openai-wraps-7-billion-share-sale-ahead-of-potential-ipo-.html",
    "source": "kristianp",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-08-11T05:40:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:49366252",
    "domain": "股票",
    "title": "OpenAI 'will be a public company in 2027' or sooner, CFO Friar tells employees",
    "url": "https://www.cnbc.com/2026/08/19/open-ai-ipo-timing-2027-friar.html",
    "source": "thm",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-08-19T19:42:35+00:00",
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
    "id": "hn:49594251",
    "domain": "金融",
    "title": "Switzerland's Federal Government Is Replacing Microsoft on 3k Computers",
    "url": "https://itsfoss.com/news/switzerland-replace-microssoft-pilot/",
    "source": "ivell",
    "platform": "hackernews",
    "points": 365,
    "published_at": "2026-09-07T05:33:25+00:00",
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
    "id": "hn:49325159",
    "domain": "金融",
    "title": "The federal keyword lists that canceled billions in research funding",
    "url": "https://www.highereddive.com/news/inside-the-federal-keyword-lists-that-canceled-billions-in-research-funding/826203/",
    "source": "walrus01",
    "platform": "hackernews",
    "points": 284,
    "published_at": "2026-08-17T00:14:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:49602582",
    "domain": "金融",
    "title": "A Tesla ran a stop sign and killed a man, Full Self-Driving/Autopilot was on",
    "url": "https://electrek.co/2026/09/07/tesla-driver-assist-stop-sign-buena-vista/",
    "source": "FabHK",
    "platform": "hackernews",
    "points": 167,
    "published_at": "2026-09-07T20:21:12+00:00",
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
    "id": "hn:49599058",
    "domain": "金融",
    "title": "If a Tesla Cybercab fleet were profitable, Tesla wouldn't sell you one",
    "url": "https://electrek.co/2026/09/07/tesla-cybercab-fleet-profitable-wouldnt-sell/",
    "source": "jijojv",
    "platform": "hackernews",
    "points": 98,
    "published_at": "2026-09-07T14:49:43+00:00",
    "summary": ""
  },
  {
    "id": "hn:49591672",
    "domain": "金融",
    "title": "Hackers have withdrawn ~4k BTC (~$320M) from the Liquid Federation wallet",
    "url": "https://twitter.com/Liquid_BTC/status/2096696272447218108",
    "source": "felipelalli",
    "platform": "hackernews",
    "points": 125,
    "published_at": "2026-09-06T22:43:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:49596610",
    "domain": "金融",
    "title": "Initial effects of AI technology on employment look positive",
    "url": "https://www.economist.com/finance-and-economics/2026/09/04/the-jobs-apocalypse-is-postponed-an-ai-jobs-boom-is-here",
    "source": "MrBuddyCasino",
    "platform": "hackernews",
    "points": 93,
    "published_at": "2026-09-07T10:38:32+00:00",
    "summary": ""
  },
  {
    "id": "hn:49612981",
    "domain": "金融",
    "title": "DOJ Blocked ICE Agent Shooting Charge over Federal Prosecutor's Objections",
    "url": "https://www.propublica.org/article/doj-blocks-charges-ice-agent-minneapolis-julio-cesar-sosa-celis",
    "source": "paimapi",
    "platform": "hackernews",
    "points": 54,
    "published_at": "2026-09-08T16:54:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:49245487",
    "domain": "金融",
    "title": "Study links GLP-1 drugs to bigger jump in women's employment than a degree",
    "url": "https://finance.yahoo.com/healthcare/articles/harvard-study-links-glp-1-123000637.html",
    "source": "metadat",
    "platform": "hackernews",
    "points": 131,
    "published_at": "2026-08-10T16:02:34+00:00",
    "summary": ""
  },
  {
    "id": "hn:49259043",
    "domain": "金融",
    "title": "Federal vendor with $50M in contracts leaves portal broken for a month",
    "url": "https://www.propublica.org/article/foia-requests-responses",
    "source": "ams1",
    "platform": "hackernews",
    "points": 101,
    "published_at": "2026-08-11T14:32:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:49245071",
    "domain": "金融",
    "title": "Force-Fed by ICE",
    "url": "https://www.theguardian.com/us-news/2026/aug/10/ice-force-feeding-detention-gabar-choli",
    "source": "HotGarbage",
    "platform": "hackernews",
    "points": 97,
    "published_at": "2026-08-10T15:35:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:49439296",
    "domain": "金融",
    "title": "A brief history of federal lift ticket regulation",
    "url": "https://zakpodmore.substack.com/p/a-brief-history-of-federal-lift-ticket",
    "source": "CGMthrowaway",
    "platform": "hackernews",
    "points": 69,
    "published_at": "2026-08-25T19:25:43+00:00",
    "summary": ""
  },
  {
    "id": "hn:49564189",
    "domain": "金融",
    "title": "Norway's Oil Fund Proposes Selling Roughly $80B in U.S. Treasurys",
    "url": "https://www.wsj.com/finance/investing/norways-oil-fund-proposes-cut-to-government-bond-holdings-d930893f",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 47,
    "published_at": "2026-09-04T13:15:24+00:00",
    "summary": ""
  },
  {
    "id": "hn:49335163",
    "domain": "金融",
    "title": "Meta faces 'astronomical' consequences as legal fight reaches critical moment",
    "url": "https://www.cnbc.com/2026/08/17/meta-attorneys-general-california-federal-trial-astronomical-consequences.html",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 86,
    "published_at": "2026-08-17T18:06:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:49432102",
    "domain": "金融",
    "title": "Nostr vs. Fediverse vs. Bluesky: A Comparison of Decentralized Social Protocols",
    "url": "https://soapbox.pub/blog/comparing-protocols",
    "source": "Bluestein",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-08-25T11:27:51+00:00",
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
    "id": "hn:49551601",
    "domain": "金融",
    "title": "Inside Google’s $200bn Wall Street finance machine for Anthropic",
    "url": "https://www.ft.com/content/549f2e23-5aa2-49c7-9ea6-a9784ab7087c",
    "source": "porridgeraisin",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-09-03T15:26:27+00:00",
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
    "id": "hn:49243531",
    "domain": "金融",
    "title": "China is now the world's greatest oil power",
    "url": "https://www.economist.com/finance-and-economics/2026/08/09/china-is-now-the-worlds-great-oil-power",
    "source": "bookofjoe",
    "platform": "hackernews",
    "points": 56,
    "published_at": "2026-08-10T13:40:46+00:00",
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
    "id": "hn:49444266",
    "domain": "金融",
    "title": "Running out of money': Kraft, McDonald's, Whirlpool CEOs flag consumer concern",
    "url": "https://finance.yahoo.com/economy/articles/running-money-kraft-mcdonald-whirlpool-114500035.html",
    "source": "MrJagil",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-08-26T05:14:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:49441647",
    "domain": "金融",
    "title": "Complete list of U.S. products subject to counter tariffs",
    "url": "https://www.canada.ca/en/department-finance/programs/international-trade-finance-policy/canadas-response-us-tariffs/complete-list-us-products-subject-to-counter-tariffs.html",
    "source": "jonbaer",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-08-25T22:38:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:49396088",
    "domain": "金融",
    "title": "S&P 500 CEO median pay hits $17.3M, widening CEO-worker ratio to 312-to-1",
    "url": "https://finance.yahoo.com/markets/stocks/articles/p-500-ceo-median-pay-234900518.html",
    "source": "newsomix9xl",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-08-22T02:38:14+00:00",
    "summary": ""
  },
  {
    "id": "hn:49348573",
    "domain": "金融",
    "title": "Trump 2.0 has deleted or altered nearly 400 US datasets",
    "url": "https://www.theguardian.com/us-news/ng-interactive/2026/aug/18/trump-federal-data-deleted-altered",
    "source": "_djo_",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-08-18T16:51:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:49289340",
    "domain": "金融",
    "title": "Hooray for index funds–just don't call them passive",
    "url": "https://www.economist.com/finance-and-economics/2026/08/11/hooray-for-index-funds-just-dont-call-them-passive",
    "source": "thm",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-08-13T17:37:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:49352830",
    "domain": "金融",
    "title": "The most influential economist is oddly unconvincing",
    "url": "https://www.economist.com/finance-and-economics/2026/08/17/the-worlds-most-influential-economist-is-oddly-unconvincing",
    "source": "aragonite",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-08-18T21:15:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:49404624",
    "domain": "金融",
    "title": "Jane Street took $15B hit in July tied to Situational Awareness",
    "url": "https://www.reuters.com/business/finance/jane-street-took-15-billion-hit-july-tied-situational-awareness-sources-say-2026-08-14/",
    "source": "paulpauper",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-08-22T22:50:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:49350858",
    "domain": "金融",
    "title": "AI Is Upending One of Finance's Cushiest Jobs",
    "url": "https://www.bloomberg.com/news/features/2026-06-05/ai-is-upending-traditional-financial-advisor-jobs",
    "source": "theriddlr",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-08-18T18:59:38+00:00",
    "summary": ""
  }
]
```
