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

- 今日日期：`2026-09-27`
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
  "date": "2026-09-27",
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
    "id": "bvid:BV1E7wtzaEdq",
    "domain": "AI",
    "title": "从 LLM 到 Agent Skill，一期视频带你打通底层逻辑！",
    "url": "http://www.bilibili.com/video/av116227955497963",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 2004903,
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
    "points": 1909069,
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
    "points": 1337506,
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
    "points": 1284920,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1o19aBJEAo",
    "domain": "AI",
    "title": "【全100集】吊打付费！目前B站最全最细的AI真人短剧制作保姆级教程！2026最新版AI视频生成全流程教学！七天就能从小白到大神！带你从入门到精通实现商业变现！",
    "url": "http://www.bilibili.com/video/av116492733518306",
    "source": "AI绘画学习教程",
    "platform": "bilibili",
    "points": 1245698,
    "published_at": "2026-05-04T08:11:00+00:00",
    "summary": "持续更新中！资料和工具在评论区哦"
  },
  {
    "id": "bvid:BV1kX546QEjG",
    "domain": "AI",
    "title": "保姆级Claude Code速成，必学！简单！【附完整文档】",
    "url": "http://www.bilibili.com/video/av116554859545963",
    "source": "数字游牧人",
    "platform": "bilibili",
    "points": 1099885,
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
    "points": 999211,
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
    "points": 891740,
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
    "points": 812628,
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
    "points": 694960,
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
    "points": 590537,
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
    "points": 443438,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1rBRQBSEwB",
    "domain": "AI",
    "title": "Claude Code+DeepSeek V4 Pro安装教程｜3步从零装好开始用 | Mac Windows",
    "url": "http://www.bilibili.com/video/av116543199385810",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 406385,
    "published_at": "2026-05-09T10:10:00+00:00",
    "summary": "上期vibe coding零基础教程10万多人看了，私信和评论里问最多的居然不是怎么写需求。\n 而是Claude Code怎么装？DeepSeek怎么接进去？🫣\n\n所以这期作为补丁教程，专门帮大家搞定这3件事：\n 1️⃣ 安装Claude Code\n 2️⃣ 把DeepSeek V4 Pro百万上下文满血版接入Claude Code\n 3️⃣ 在VS Code里正式用起来\n\nMac和Windows"
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 394414,
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
    "points": 359482,
    "published_at": "2026-08-10T10:54:20+00:00",
    "summary": "Codex 安装 + 上手速通，保姆级教程！\n无需 ChatGPT 订阅，国内直连 DeepSeek"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 298058,
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
    "points": 297300,
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
    "points": 217970,
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
    "points": 188342,
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
    "points": 182181,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1wDhj6wEa8",
    "domain": "AI",
    "title": "全网刷屏的 Jev 模型正式开放！保姆级教程 + 实战测评",
    "url": "http://www.bilibili.com/video/av117313592367632",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 160914,
    "published_at": "2026-09-22T07:50:41+00:00",
    "summary": "全网爆火的 Jev 模型是什么？有什么用？怎么使用？怎么接入 AI 编程工具（比如 Codex）？效果真的好么？跟 DeepSeek V4 Flash 比速度如何？傻子可懂的 Jev 保姆级实战教程 + 实战测评来啦。\n编程学习教程+实战项目+简历模板：codefather.cn\n免费 AI 编程教程：github.com/liyupi/ai-guide\n记得三连支持、关注鱼皮，让更多朋友学到知识"
  },
  {
    "id": "bvid:BV1iH8Y6wE5s",
    "domain": "AI",
    "title": "【Re:从零开始的AI学习】安装你的第一个 Agent",
    "url": "http://www.bilibili.com/video/av117148403893835",
    "source": "卡普迪姆",
    "platform": "bilibili",
    "points": 137740,
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
    "points": 124445,
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
    "points": 93800,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1H1eH6DExE",
    "domain": "AI",
    "title": "零基础入门vibe coding！如何搭建自己的工作台？附指令模版",
    "url": "http://www.bilibili.com/video/av117275877184803",
    "source": "Iris学姐",
    "platform": "bilibili",
    "points": 88352,
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
    "points": 80315,
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
    "points": 75347,
    "published_at": "2025-07-12T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1VL3F6pE9K",
    "domain": "AI",
    "title": "0基础入门智能体agent测试：AI测试基础+AI智能体(Agent)测试从零入门全攻略，2026最新版！",
    "url": "http://www.bilibili.com/video/av116991151113881",
    "source": "黑马测试",
    "platform": "bilibili",
    "points": 61035,
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
    "points": 55501,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operit教程：入门安卓最强大ai平台operitAI",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 54506,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1W2Ts6YEXW",
    "domain": "AI",
    "title": "AI大模型+网络安全零基础入门全套教程：从Agent选型到AI挖洞全流程！AI挖洞提示词|AI解CTF题|AI审计代码|SRC挖洞|CS渗透|kali-码士集团",
    "url": "http://www.bilibili.com/video/av116854601286698",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 53441,
    "published_at": "2026-07-03T06:28:48+00:00",
    "summary": "迈入AI赋能的网络安全新时代！\n\n本课程带你打通大模型与安全实战的底层逻辑。从大模型演进到安全智能体（Agent）构建，硬核实战拉满！手把手教你利用大模型API自动化搞定信息收集、黑盒挖洞、代码审计、解CTF题目及报告编写。深度破解AI挖洞的高效提示词秘籍，攻克复杂场景下的Agent架构与成本选型。\n\n2026安全防线全面升级，带你用AI武装自己，成为驾驭大模型的稀缺AI安全专家！"
  },
  {
    "id": "bvid:BV1LXhc6yEkc",
    "domain": "AI",
    "title": "昔涟/Cyrene-Agent 安装配置/演示教程",
    "url": "http://www.bilibili.com/video/av117164694570292",
    "source": "Playa0",
    "platform": "bilibili",
    "points": 50932,
    "published_at": "2026-08-27T00:43:58+00:00",
    "summary": "v1.1.6安装包：\n夸克网盘：\n链接：https://pan.quark.cn/s/43ff3db459f4?pwd=SD2k\n提取码：SD2k\ngithub仓库：\nPlaya-0v0/Cyrene-Agent: An open-source AI desktop companion inspired by Cyrene, combining immersive Chat, personaliz"
  },
  {
    "id": "bvid:BV1AJen6SEVQ",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Agent智能体】教程！大模型入门到进阶，一套全解决！Agentic AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av117274400790619",
    "source": "吴恩达Agent",
    "platform": "bilibili",
    "points": 49565,
    "published_at": "2026-09-15T09:48:26+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n1. 构建智能体设计模式：反射、工具使用、规划与多智能体工作流；\n2. 将人工智能与外部工具集成：数据库、API、网络搜索与代码执行；\n3. 评估并优化人工智能系统：性能指标、错误分析与生产部署\n4、使用开放标准格式和最佳实践创建可重复使用的技能，并组合以创建复杂的工作流程。\n5、建立定制代码生成技能，审核你的代"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 48647,
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
    "points": 40154,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV17ve36mEnr",
    "domain": "AI",
    "title": "恭喜你打败了99%的985学生，只要你会用Agent。",
    "url": "http://www.bilibili.com/video/av117286513940447",
    "source": "小毛毛熊丶",
    "platform": "bilibili",
    "points": 38653,
    "published_at": "2026-09-17T13:08:15+00:00",
    "summary": "当我通过对话框和 AI 聊天时，我庆幸自己站在了新一轮工业革命的窗口；\n但等我用过 Agent 类工具后，才发现工业革命这个比喻还是肤浅了，应该提高到人类学会用火的高度。\n连数学家都快已经被 AI 干失业了…"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 34404,
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
    "points": 29779,
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
    "points": 28960,
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
    "points": 23225,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1wqeb6gEDY",
    "domain": "AI",
    "title": "Claude Code 百分百不封号",
    "url": "http://www.bilibili.com/video/av117297150694473",
    "source": "DUNHKPcc",
    "platform": "bilibili",
    "points": 22994,
    "published_at": "2026-09-19T10:14:15+00:00",
    "summary": "如果需要文档，私信主播，主页送免费的token，文件在群里 Q群1124987353"
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
    "id": "bvid:BV1EReW6pEfv",
    "domain": "AI",
    "title": "14K Star Claude Code 开源桌面端，5个AI自己分工干活了！",
    "url": "http://www.bilibili.com/video/av117276346946735",
    "source": "程序员阿江-Relakkes",
    "platform": "bilibili",
    "points": 19488,
    "published_at": "2026-09-16T03:30:00+00:00",
    "summary": "上一期让 cc-haha 自动操作电脑，这一期，我让 5 个 AI Agent 一起做开发。\n\n用的还是我一直在维护的开源 Claude Code 桌面端：cc-haha。这次重点演示 Agent Teams：我给出一个开发需求，队长拆任务，前端、后端、测试和 Code Review 分工推进。成员做完手上的工作，还能继续领取可执行的任务，直接给队友发消息。\n\n这期用一个真实任务，从组队、共享任务"
  },
  {
    "id": "bvid:BV1f5hq6jEG5",
    "domain": "AI",
    "title": "为什么我会感觉vibe coding让程序员越来越浮躁了？",
    "url": "http://www.bilibili.com/video/av117307502302833",
    "source": "AAA话题批发",
    "platform": "bilibili",
    "points": 17662,
    "published_at": "2026-09-21T07:45:00+00:00",
    "summary": "随着 AI 编程工具 vibe coding 逐步在开发团队落地，在带来效率提升的同时，也滋生出程序员群体心态浮躁的现象，这篇文章结合团队实际使用经历，对这一矛盾现象展开剖析。\n文章先客观列举该工具带来的实际增益。它可以快速完成功能编码，辅助梳理陌生工程，自动处理部分 bug，也能降低跨领域任务的上手门槛，就连过去难以推动的编辑器迁移，也因为工具良好的使用体验顺利落地，一线开发人员对工具的依赖程度"
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 17596,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1XGaA6CEwe",
    "domain": "AI",
    "title": "【2026最新】Claude Code保姆级完整教程-最强AI助手！从入门到进阶，速通Claude Code！一个方法教你规避封号风险！【附教程文档安装包】",
    "url": "http://www.bilibili.com/video/av117325537810666",
    "source": "大模型小阳",
    "platform": "bilibili",
    "points": 16049,
    "published_at": "2026-09-24T10:36:14+00:00",
    "summary": "整理制作不易，大家记得点个关注，一键三连呀【点赞、收藏、转发】感谢支持~"
  },
  {
    "id": "bvid:BV1yyQEBdEkm",
    "domain": "AI",
    "title": "【2026B站最全】Claude Code+软件测试实操教程!看完我直接删了收藏夹所有测试教程,从账号注册到Plan驱动测试项目,小白3天上手！",
    "url": "http://www.bilibili.com/video/av116408092525631",
    "source": "软件测试大神",
    "platform": "bilibili",
    "points": 15240,
    "published_at": "2026-04-15T09:55:02+00:00",
    "summary": "配套资料👉：https://b23.tv/qvhxmaQ\n包括:AI测试网站，几十个AI场景测试完整流程，skil文档，测试八股文，项目源码，测试用例模板，工具安装包，学习计划表，学习路线，100g测试新人资料包等等，资料百分百免费，放心领取~"
  },
  {
    "id": "bvid:BV1MAYd6sEZh",
    "domain": "AI",
    "title": "效率翻倍， 一次讲透AI Agent的用法和技巧",
    "url": "http://www.bilibili.com/video/av117258059847877",
    "source": "数码旭",
    "platform": "bilibili",
    "points": 14301,
    "published_at": "2026-09-12T12:33:07+00:00",
    "summary": "AI Agent作为今年AI应用方式最大的变化，会给普通人带来突破性的效率提升，当然也给我带来的特别大的帮助。我希望通过这期长视频，能帮助你提升工作效率。"
  },
  {
    "id": "bvid:BV1pfuR69EoF",
    "domain": "AI",
    "title": "【全80集】零基础Vibe Coding教程，Vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av117070675118277",
    "source": "暴龙Boy",
    "platform": "bilibili",
    "points": 14210,
    "published_at": "2026-08-10T10:45:04+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1xh3C6cEGv",
    "domain": "AI",
    "title": "两周完成一篇SCI论文，用claude code帮你干",
    "url": "http://www.bilibili.com/video/av117002408559933",
    "source": "博士大师兄木水",
    "platform": "bilibili",
    "points": 12065,
    "published_at": "2026-07-29T08:53:04+00:00",
    "summary": "大师兄八股文SCI速成模板已制作成skill，手把手带你实现一键生成SCI论文初稿"
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
    "id": "hn:49844663",
    "domain": "AI 算力 / 半导体",
    "title": "ASML says it sold 'absolutely nothing' in Europe in 2026",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/asml-says-its-sells-absolutely-nothing-in-europe-calls-on-eu-to-help-create-demand",
    "source": "MC995",
    "platform": "hackernews",
    "points": 269,
    "published_at": "2026-09-25T13:49:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:49824864",
    "domain": "AI 算力 / 半导体",
    "title": "Virtio-nvgpu: Near-native Nvidia GPU access inside a KVM guest",
    "url": "https://github.com/nestrilabs/virtio-nvgpu",
    "source": "WanjohiRyan",
    "platform": "hackernews",
    "points": 154,
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
    "id": "rss:https://www.eetimes.com/huaweis-tau-law-takes-commercial-form/",
    "domain": "AI 算力 / 半导体",
    "title": "Huawei’s Tau Law Takes Commercial Form",
    "url": "https://www.eetimes.com/huaweis-tau-law-takes-commercial-form/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T14:18:57+00:00",
    "summary": "Kirin 9050 Pro rests on the Tau (τ) Scaling Law, marking a major change in chip architecture designed to bypass EUV lithography limits. The post Huawei’s Tau Law Takes Commercial Form appeared first o"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/27-year-old-gta-2-gets-full-path-tracing-and-60-fps-frame-generation-via-rtx-remix-custom-direct3d-9-wrapper-modernizes-classic-with-custom-direct3d-9-bridge-unlocks-dynamic-lighting",
    "domain": "AI 算力 / 半导体",
    "title": "27-year-old GTA 2 gets full path tracing and 60 FPS frame generation via RTX Remix",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/27-year-old-gta-2-gets-full-path-tracing-and-60-fps-frame-generation-via-rtx-remix-custom-direct3d-9-wrapper-modernizes-classic-with-custom-direct3d-9-bridge-unlocks-dynamic-lighting",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T15:10:00+00:00",
    "summary": "Modder releases GTA2 RTX Remix, a mod that adds path tracing and a dynamic time of day to the 27-year-old Grand Theft Auto 2."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/russia-bombs-ukrainian-data-centers-in-latest-escalation-100-000-households-lose-connectivity-as-firms-migrate-data-abroad-zelensky-says-ordinary-life-is-simply-a-target",
    "domain": "AI 算力 / 半导体",
    "title": "Russia bombs Ukrainian data centers in latest escalation",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/russia-bombs-ukrainian-data-centers-in-latest-escalation-100-000-households-lose-connectivity-as-firms-migrate-data-abroad-zelensky-says-ordinary-life-is-simply-a-target",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T14:30:59+00:00",
    "summary": "Russia has begun targeting data centers and internet infrastructure in its latest attacks, disrupting critical services for Ukrainian civilians. The attacks have left 100,000 households in the area wi"
  },
  {
    "id": "rss:https://www.tomshardware.com/tablets/microsoft-surface/microsoft-quietly-drops-copilot-branding-from-its-new-laptops-surface-cvp-confirms-new-devices-meet-hardware-requirements-but-lack-controversial-branding",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft quietly drops Copilot+ branding from new laptops",
    "url": "https://www.tomshardware.com/tablets/microsoft-surface/microsoft-quietly-drops-copilot-branding-from-its-new-laptops-surface-cvp-confirms-new-devices-meet-hardware-requirements-but-lack-controversial-branding",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T14:00:00+00:00",
    "summary": "Microsoft's latest Surface laptops dropped the Copilot+ PC branding despite hitting the minimum requirements. Even high-end AI devices like the Nvidia RTX Spark and Microsoft's own Project Zenith are "
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/open-source-anyps5-dumps-emulation-to-run-playstation-5-console-games-natively-on-pc-amd-zen-2-architecture-enables-proton-like-binary-translation-for-windows-and-linux",
    "domain": "AI 算力 / 半导体",
    "title": "Open-source AnyPS5 dumps emulation to run PlayStation 5 console games natively on PC",
    "url": "https://www.tomshardware.com/video-games/playstation/open-source-anyps5-dumps-emulation-to-run-playstation-5-console-games-natively-on-pc-amd-zen-2-architecture-enables-proton-like-binary-translation-for-windows-and-linux",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T13:59:04+00:00",
    "summary": "Traditional PS5 emulators attempt to recreate the console's hardware and software environment, but AnyPS5 is experimenting with a compatibility layer that translates PlayStation 5 executables into for"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/an-nvidia-chatbot-could-one-day-help-developers-better-optimize-their-games-patent-filing-show-requests-can-be-made-in-plain-english",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia patents AI chatbot to streamline PC game optimization",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/an-nvidia-chatbot-could-one-day-help-developers-better-optimize-their-games-patent-filing-show-requests-can-be-made-in-plain-english",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T13:00:00+00:00",
    "summary": "An Nvidia patent suggests the company could push developers to use a new chatbot as a way to get guidance on how to optimize their new games before release."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/sandisk-optimus-gx-pro-850p-2tb-ssd-review",
    "domain": "AI 算力 / 半导体",
    "title": "Sandisk Optimus GX Pro 850P 2TB SSD review: A PS5 SSD you recognize at a price you don’t",
    "url": "https://www.tomshardware.com/pc-components/ssds/sandisk-optimus-gx-pro-850p-2tb-ssd-review",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T13:00:00+00:00",
    "summary": "The Sandisk Optimus GX Pro 850P is a WD Black SN850P by another name. It’s a great PS5 SSD with good performance in a mature package, but with a stiff premium."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidias-rtx-mega-geometry-2-0-streams-ray-tracing-geometry-into-vram-on-demand-nanite-inspired-design-drops-detail-instead-of-dropping-out",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia’s RTX Mega Geometry 2.0 streams ray-tracing geometry into VRAM on demand",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidias-rtx-mega-geometry-2-0-streams-ray-tracing-geometry-into-vram-on-demand-nanite-inspired-design-drops-detail-instead-of-dropping-out",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T12:30:00+00:00",
    "summary": "Nvidia’s RTX Mega Geometry 2.0 SDK arrives alongside RTX Kit 2026.3 with on-demand ray-tracing geometry streaming."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/novel-attack-on-rsa-cryptography-might-bring-computation-requirements-for-cracking-down-to-manageable-levels",
    "domain": "AI 算力 / 半导体",
    "title": "Novel attack slashes computing power needed to crack textbook RSA cryptography",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/novel-attack-on-rsa-cryptography-might-bring-computation-requirements-for-cracking-down-to-manageable-levels",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T12:00:00+00:00",
    "summary": "Not very practical yet, but could serve as the basis for future improvements."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/pny-allegedly-refuses-to-cover-melted-rtx-5090-powered-by-native-power-supply-cable-company-closes-users-ticket-when-questioned-on-policy",
    "domain": "AI 算力 / 半导体",
    "title": "PNY allegedly refuses to cover melted RTX 5090 powered by native power supply cable",
    "url": "https://www.tomshardware.com/pc-components/gpus/pny-allegedly-refuses-to-cover-melted-rtx-5090-powered-by-native-power-supply-cable-company-closes-users-ticket-when-questioned-on-policy",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T11:30:00+00:00",
    "summary": "A user's GeForce RTX 5090 died when his 12V-2x6 connector melted, and then PNY denied his warranty claim based on technicalities that aren't even present in the warranty policy."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/liquid-cooling/enthusiast-cooled-iphone-18-pro-with-cold-can-of-la-croix-sparkling-water-benchmarks-show-25-percent-higher-sustained-performance-liquid-cooling-surprisingly-reduced-thermal-throttling",
    "domain": "AI 算力 / 半导体",
    "title": "Enthusiast cooled iPhone 18 Pro with cold can of La Croix sparkling water; benchmarks show 25% higher sustained performance",
    "url": "https://www.tomshardware.com/pc-components/liquid-cooling/enthusiast-cooled-iphone-18-pro-with-cold-can-of-la-croix-sparkling-water-benchmarks-show-25-percent-higher-sustained-performance-liquid-cooling-surprisingly-reduced-thermal-throttling",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T11:00:00+00:00",
    "summary": "Matt Birchler put a cold drink can on the back of an iPhone 18 Pro to see how much performance uplift it would get in a prolonged benchmarking session. The results showed up to 25% higher sustained pe"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/vpn/federal-bill-would-force-vpn-providers-isps-and-dns-services-to-block-foreign-piracy-sites-yet-fuzzy-location-rules-could-trigger-heavy-handed-bans",
    "domain": "AI 算力 / 半导体",
    "title": "Federal bill would force VPN providers, ISPs, and DNS services to block foreign piracy sites",
    "url": "https://www.tomshardware.com/software/vpn/federal-bill-would-force-vpn-providers-isps-and-dns-services-to-block-foreign-piracy-sites-yet-fuzzy-location-rules-could-trigger-heavy-handed-bans",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T10:30:00+00:00",
    "summary": "Proposed federal bill would force ISPs, DNS services, and VPN providers to block foreign piracy sites — yet the definition of \"from the United states\" gets murky"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/chatgpt-6-astra-cracks-1941-enigma-coded-message-in-two-days-autonomous-ai-coded-its-own-simulator-to-crack-code-that-was-unsolved-since-it-was-shared-online-back-in-2005",
    "domain": "AI 算力 / 半导体",
    "title": "ChatGPT-6 Astra cracks 85-year-old 1941 Enigma-coded message in two days",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/chatgpt-6-astra-cracks-1941-enigma-coded-message-in-two-days-autonomous-ai-coded-its-own-simulator-to-crack-code-that-was-unsolved-since-it-was-shared-online-back-in-2005",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T10:00:00+00:00",
    "summary": "A German Army Enigma transmission from 85 years ago, known as the MVUEH message, has been cracked by GTP-Astra in just two days."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/elon-musks-spacexai-to-add-another-660-000-ai-gpus-this-year-nearing-a-total-of-1-44-million-in-operation-firm-is-building-1-2-gigawatt-power-plant-to-bring-systems-fully-online",
    "domain": "AI 算力 / 半导体",
    "title": "Elon Musk's SpaceXAI to add another 660,000 AI GPUs this year, nearing a total of 1.44 million in operation",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/elon-musks-spacexai-to-add-another-660-000-ai-gpus-this-year-nearing-a-total-of-1-44-million-in-operation-firm-is-building-1-2-gigawatt-power-plant-to-bring-systems-fully-online",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T15:40:00+00:00",
    "summary": "Elon Musk says that the Colossus 2 will receive 220,000 GB300 GPUs by next week, with another two tranches of the same amount expected to arrive later this year. This will put the site at over a milli"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/photonics/tower-semiconductor-to-invest-usd4-billion-in-japanese-ops-to-set-up-massive-optical-connectivity-hub-dual-track-expansion-aims-to-increase-output-by-40-times-by-2029",
    "domain": "AI 算力 / 半导体",
    "title": "Tower Semiconductor to invest $4 billion in Japanese ops to set up massive optical connectivity hub",
    "url": "https://www.tomshardware.com/tech-industry/photonics/tower-semiconductor-to-invest-usd4-billion-in-japanese-ops-to-set-up-massive-optical-connectivity-hub-dual-track-expansion-aims-to-increase-output-by-40-times-by-2029",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T15:00:22+00:00",
    "summary": "Tower's new optical connectivity hub in Japan will increase its output by 40 times in 2029 compared to 2025 level."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/meta-muse-runs-agents-on-amd-epyc-turin-hosts-with-two-cores-and-8gb-of-memory-ai-agent-can-pass-terminal-commands-to-ubuntu-host-system",
    "domain": "AI 算力 / 半导体",
    "title": "Meta Muse runs agents on AMD EPYC Turin hosts with two cores and 8GB of memory",
    "url": "https://www.tomshardware.com/pc-components/cpus/meta-muse-runs-agents-on-amd-epyc-turin-hosts-with-two-cores-and-8gb-of-memory-ai-agent-can-pass-terminal-commands-to-ubuntu-host-system",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T14:56:36+00:00",
    "summary": "Meta's new Muse AI agent is powered by AMD EPYC Turin hosts, with each user getting a private sandbox with two vCPUs and 8GB of memory."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/air-cooling/noctua-explores-2-000w-micro-channel-air-cooling-partners-with-forced-physics-to-develop-vacuum-pump-level-airflow-for-desktop-pcs",
    "domain": "AI 算力 / 半导体",
    "title": "Noctua explores 2,000W micro-channel air cooling",
    "url": "https://www.tomshardware.com/pc-components/air-cooling/noctua-explores-2-000w-micro-channel-air-cooling-partners-with-forced-physics-to-develop-vacuum-pump-level-airflow-for-desktop-pcs",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T14:42:58+00:00",
    "summary": "Noctua and Forced Physics are exploring whether densely packed micro-channels can provide extreme cooling performance without the noise associated with high-pressure airflow"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/save-usd250-on-this-award-winning-elegoo-resin-3d-printer-with-an-integrated-heater-and-16k-resolution-39-percent-discount-on-the-saturn-4-ultra-16k-gets-you-a-hugely-accurate-printer-with-fast-speeds-and-a-tilt-release-vat",
    "domain": "AI 算力 / 半导体",
    "title": "Save $250 on this award-winning Elegoo resin 3D printer with an integrated heater and 16K resolution",
    "url": "https://www.tomshardware.com/3d-printing/save-usd250-on-this-award-winning-elegoo-resin-3d-printer-with-an-integrated-heater-and-16k-resolution-39-percent-discount-on-the-saturn-4-ultra-16k-gets-you-a-hugely-accurate-printer-with-fast-speeds-and-a-tilt-release-vat",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T13:33:16+00:00",
    "summary": "This Elegoo Saturn 4 Ultra, one of the best resin 3D printers you can buy, is on sale for $359 right now, saving you 40% on its usual price."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/laptop-maker-says-ddr5-so-dimms-are-6x-pricier-than-last-year-schenker-says-other-component-costs-are-rising-too-announces-price-hikes",
    "domain": "AI 算力 / 半导体",
    "title": "DDR5 laptop memory prices surge 6X in 12 months",
    "url": "https://www.tomshardware.com/laptops/laptop-maker-says-ddr5-so-dimms-are-6x-pricier-than-last-year-schenker-says-other-component-costs-are-rising-too-announces-price-hikes",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T13:00:00+00:00",
    "summary": "XMG noted that SO-DIMM prices have jumped 6x, with other components like PCBs, CPUs, and GPUs also facing increasing costs. This has forced the niche laptop manufacturer to bump their SRPs between $11"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/power-supplies/gamemax-rgb-pro-750g-power-supply-review",
    "domain": "AI 算力 / 半导体",
    "title": "Gamemax RGB PRO 750G power supply review: Efficient, but pricey for an average unit with pretty lights",
    "url": "https://www.tomshardware.com/pc-components/power-supplies/gamemax-rgb-pro-750g-power-supply-review",
    "source": "E. Fylladitakis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T13:00:00+00:00",
    "summary": "Gamemax charges $105 for an average power supply with RGB lighting. The Sohoo platform underneath measures well enough, but the fan, the capacitors, and the warranty all sit below what the price shoul"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/nintendo/nintendo-wins-usd4-5-million-lawsuit-against-switch-pirate-by-default-defendant-allegedly-moderated-r-switchpirates-and-sold-pirated-switch-games",
    "domain": "AI 算力 / 半导体",
    "title": "Nintendo wins $4.5 million lawsuit against Switch pirate by default",
    "url": "https://www.tomshardware.com/video-games/nintendo/nintendo-wins-usd4-5-million-lawsuit-against-switch-pirate-by-default-defendant-allegedly-moderated-r-switchpirates-and-sold-pirated-switch-games",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T12:26:21+00:00",
    "summary": "A Washington court granted Nintendo of America a $4.5 million default judgment after the defendant failed to appear in court and respond to the allegations. The company claimed that it sent a cease-an"
  },
  {
    "id": "rss:https://www.tomshardware.com/tablets/microsoft-surface/microsoft-revamps-copilot-with-new-tools-support-for-frontier-models-available-now-through-frontier-program",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft revamps Copilot with new tools, support for frontier models",
    "url": "https://www.tomshardware.com/tablets/microsoft-surface/microsoft-revamps-copilot-with-new-tools-support-for-frontier-models-available-now-through-frontier-program",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T12:00:00+00:00",
    "summary": "Microsoft is revamping Copilot into a singular AI workspace, mixing your projects and agents together. It will also be able to support third-party frontier models."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/intel-expects-14a-to-be-within-5-percent-the-performance-of-tsmcs-a14-conservative-forecast-clashes-with-18as-frequency-lead-and-promised-20-percent-gains",
    "domain": "AI 算力 / 半导体",
    "title": "Intel expects 14A to be 'within 5%' the performance of TSMC's A14",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/intel-expects-14a-to-be-within-5-percent-the-performance-of-tsmcs-a14-conservative-forecast-clashes-with-18as-frequency-lead-and-promised-20-percent-gains",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T12:00:00+00:00",
    "summary": "Intel's Naga Chandrasekaran now claims that Intel 14A node will deliver performance 'within 5%' of TSMC's A14 technology, a claim that requires a closer examination."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/asus-online-store-hit-by-data-breach-customer-contact-details-and-order-information-revealed",
    "domain": "AI 算力 / 半导体",
    "title": "Asus confirms eShop data breach exposed customer order records and contact details",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/asus-online-store-hit-by-data-breach-customer-contact-details-and-order-information-revealed",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T11:30:00+00:00",
    "summary": "Asus eShop hit by data breach — customer contact details and order information revealed"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/new-jersey-fines-data-center-for-using-unpermitted-power-generators-microsoft-linked-site-also-in-trouble-with-community-for-noise-pollution-other-issues",
    "domain": "AI 算力 / 半导体",
    "title": "New Jersey hits Microsoft-linked AI data center with record fine for 62 unpermitted power generators, issues 45-day shutdown deadline",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/new-jersey-fines-data-center-for-using-unpermitted-power-generators-microsoft-linked-site-also-in-trouble-with-community-for-noise-pollution-other-issues",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T11:00:00+00:00",
    "summary": "The DataOne data center is facing a record fine of $1.07 million for operating portable turbine generators without permission. Residents say that the penalty is a drop in the bucket for these big tech"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/grab-this-4k-ready-rtx-5070-ti-gaming-pc-from-hp-for-under-usd1-900-right-now-powerful-omen-35l-machine-is-a-serious-bargain-with-a-20-core-intel-cpu-32gb-ddr5-ram-and-a-1tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Grab this 4K-ready RTX 5070 Ti gaming PC from HP for under $1,900 right now",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/grab-this-4k-ready-rtx-5070-ti-gaming-pc-from-hp-for-under-usd1-900-right-now-powerful-omen-35l-machine-is-a-serious-bargain-with-a-20-core-intel-cpu-32gb-ddr5-ram-and-a-1tb-ssd",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T10:51:36+00:00",
    "summary": "This epic HP Omen 45L gaming rig is one of the cheapest RTX 5070 Ti PC you can buy right now, fitted with a Intel Core i7-14700F, 32GB of DDR RAM, and a 1TB SSD for just $1,899.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-dlss-5-upscales-frame-rates-and-flame-temps-on-16-pin-power-connector-ai-gaming-tech-pushes-connector-to-uncomfortable-thermal-and-power-limits",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia DLSS 5 power draw hits 647W as power connector runs hotter than the GPU die, upscales frame rates and flame temps on 16-pin",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-dlss-5-upscales-frame-rates-and-flame-temps-on-16-pin-power-connector-ai-gaming-tech-pushes-connector-to-uncomfortable-thermal-and-power-limits",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T10:30:00+00:00",
    "summary": "QuasarZone tests show the 16-pin power connector on a GeForce RTX 5090 reaches temperatures above 90 degrees Celsius at peak power consumption near 650W."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/google-is-blasting-an-experimental-ai-data-center-into-orbit-first-satellite-will-feature-just-four-tensor-processing-units",
    "domain": "AI 算力 / 半导体",
    "title": "Google's orbital AI data center test packs four TPUs and 1,000W of solar power",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/google-is-blasting-an-experimental-ai-data-center-into-orbit-first-satellite-will-feature-just-four-tensor-processing-units",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T10:00:00+00:00",
    "summary": "Google will launch an experimental satellite into orbit on October 1, taking four tensor processing units with it."
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
    "points": 877,
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
    "points": 590,
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
    "points": 492,
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
    "id": "hn:49817615",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.8 text-to-speech",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/",
    "source": "swolpers",
    "platform": "hackernews",
    "points": 330,
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
    "id": "hn:49844896",
    "domain": "大厂 AI 动态",
    "title": "Microsoft abandons personal AI chatbot race with Copilot reboot",
    "url": "https://www.bloomberg.com/news/articles/2026-09-25/microsoft-abandons-personal-ai-chatbot-race-with-copilot-reboot",
    "source": "sbulaev",
    "platform": "hackernews",
    "points": 148,
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
    "points": 142,
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
    "id": "hn:49854945",
    "domain": "大厂 AI 动态",
    "title": "The Copilot+ PC brand is dead",
    "url": "https://www.windowscentral.com/microsoft/windows-11/the-copilot-pc-brand-is-dead-microsoft-and-pc-makers-quietly-pull-back-on-tarnished-windows-11-ai-pc-branding",
    "source": "bj-rn",
    "platform": "hackernews",
    "points": 104,
    "published_at": "2026-09-26T09:55:38+00:00",
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
    "id": "hn:49829472",
    "domain": "大厂 AI 动态",
    "title": "Fourier Analysis: Drawing Llamas with Circles",
    "url": "https://adekau.github.io/posts/2020/llamas.html",
    "source": "cebert",
    "platform": "hackernews",
    "points": 76,
    "published_at": "2026-09-24T12:03:35+00:00",
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
    "id": "rss:https://www.theverge.com/tech/1001118/apple-hit-with-5-7-billion-in-damages-over-haptic-patents",
    "domain": "大厂 AI 动态",
    "title": "Apple hit with $5.7 billion in damages over haptic patents",
    "url": "https://www.theverge.com/tech/1001118/apple-hit-with-5-7-billion-in-damages-over-haptic-patents",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T21:30:01+00:00",
    "summary": "Haptics tech company Taction sued Apple in 2021, alleging it infringed two of its patents. Now a federal jury in San Diego has awarded Taction over $5.7 billion in damages. According to CNBC, \"The law"
  },
  {
    "id": "rss:https://www.theverge.com/report/1000994/decap-drums-that-knock-interview",
    "domain": "大厂 AI 动态",
    "title": "Decap is the man behind the drums behind your favorite song",
    "url": "https://www.theverge.com/report/1000994/decap-drums-that-knock-interview",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T19:30:00+00:00",
    "summary": "I don't think I'm going to hurt anyone's feelings by pointing out that Decap doesn't have the name recognition of Kendrick Lamar, Olivia Rodrigo, or Charli XCX. But his fingerprints are all over track"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/1001056/this-american-life-npr-kids-group-chat-comment-section",
    "domain": "大厂 AI 动态",
    "title": "Kids turned the comment section of an NPR podcast into a group chat",
    "url": "https://www.theverge.com/entertainment/1001056/this-american-life-npr-kids-group-chat-comment-section",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T17:32:35+00:00",
    "summary": "Middle schoolers, likely blocked from other apps and social networks, apparently turned the Spotify comment section under an episode of NPR's Wild Card into an impromptu group chat. In a new episode o"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1001049/openai-training-pause",
    "domain": "大厂 AI 动态",
    "title": "OpenAI pauses training of its ‘most capable models’",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1001049/openai-training-pause",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T16:34:59+00:00",
    "summary": "As reports of OpenAI's models breaking containment, hacking sites, and generally getting out of control pile up, the company has made the decision to pause training of its most powerful models. The de"
  },
  {
    "id": "rss:https://www.theverge.com/podcast/1000344/cloudflare-matthew-prince-google-zero-ai-web-advertising",
    "domain": "大厂 AI 动态",
    "title": "Can Cloudflare CEO Matthew Prince save the web from AI?",
    "url": "https://www.theverge.com/podcast/1000344/cloudflare-matthew-prince-google-zero-ai-web-advertising",
    "source": "Nilay Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T14:00:00+00:00",
    "summary": "Today, I’m talking with Matthew Prince, who is CEO of Cloudflare. This episode is part of a two-part series on the future of business. Matthew last joined us on the show about two and a half years ago"
  },
  {
    "id": "rss:https://www.theverge.com/games/1000818/control-resonant-reading-collectibles-documents-logs",
    "domain": "大厂 AI 动态",
    "title": "Control Resonant is a great game — it’s even better when you read everything",
    "url": "https://www.theverge.com/games/1000818/control-resonant-reading-collectibles-documents-logs",
    "source": "Kallie Plagge",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T13:00:00+00:00",
    "summary": "In Control Resonant, the entire world is at stake. But that didn't stop the diligent employees of the Federal Bureau of Control from filing reams of paperwork, and it didn't stop me from reading every"
  },
  {
    "id": "rss:https://www.theverge.com/games/1001002/pokemon-30th-celebration-scalping-resellers",
    "domain": "大厂 AI 动态",
    "title": "Pokémon card resellers have turned collecting into an online blood sport",
    "url": "https://www.theverge.com/games/1001002/pokemon-30th-celebration-scalping-resellers",
    "source": "Charles Pulliam-Moore",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T12:00:00+00:00",
    "summary": "Earlier this month, Pok&#233;mon card content creator Natalie Roush posted a video to her YouTube and Instagram pages that enraged the larger collection community. In the now-deleted video, Roush show"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/999785/amflow-tl-review-avinox-esuv-e-bike-avinox",
    "domain": "大厂 AI 动态",
    "title": "Can &#8216;eSUV&#8217; e-bikes really go from trail to town?",
    "url": "https://www.theverge.com/transportation/999785/amflow-tl-review-avinox-esuv-e-bike-avinox",
    "source": "Thomas Ricker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T07:00:00+00:00",
    "summary": "Have you ever wanted an electric bike that easily transitions from the drudgery of urban asphalt to adventures in gravel and dirt? That's what a subclass of so-called \"electric SUV\" (eSUV) e-bikes cla"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1000859/roku-pro-series-oled-nothing-phone-4a-pro-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Roku&#8217;s first OLED TVs are up to $400 off, starting at $699",
    "url": "https://www.theverge.com/gadgets/1000859/roku-pro-series-oled-nothing-phone-4a-pro-deal-sale",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T18:18:57+00:00",
    "summary": "Roku recently launched its first-ever OLED TVs. The $999 starting price was already impressive for the 55-inch Pro Series model that has a 120Hz refresh rate OLED panel (with four HDMI 2.1 ports and s"
  },
  {
    "id": "rss:https://www.theverge.com/podcast/1000751/vergecast-meta-connect-muse-googlebooks",
    "domain": "大厂 AI 动态",
    "title": "Phones don’t have lights",
    "url": "https://www.theverge.com/podcast/1000751/vergecast-meta-connect-muse-googlebooks",
    "source": "Jacob Kastrenakes",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T17:42:59+00:00",
    "summary": "Mark Zuckerberg has a new defense of the Ray-Ban Meta glasses: They're actually doing more to signal they're taking a photo than phones do. He's brought this up in at least two recent interviews, noti"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/26/pnoes-new-face-mask-wants-to-make-lab-grade-breath-testing-a-self-serve-affair/",
    "domain": "大厂 AI 动态",
    "title": "PNOE’s new face mask wants to make lab-grade breath testing a self-serve affair",
    "url": "https://techcrunch.com/2026/09/26/pnoes-new-face-mask-wants-to-make-lab-grade-breath-testing-a-self-serve-affair/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-27T01:40:30+00:00",
    "summary": "PNOĒ, the Malden, Mass.-based startup whose breath-analyzing mask used to bear an unfortunate resemblance to Bane's, is launching a sleeker self-serve version on October 1 that lets gym-goers measure "
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/26/google-tests-buying-from-walmart-owned-flipkart-through-gemini-and-ai-mode-in-india/",
    "domain": "大厂 AI 动态",
    "title": "Google tests buying from Walmart-owned Flipkart through Gemini and AI Mode in India",
    "url": "https://techcrunch.com/2026/09/26/google-tests-buying-from-walmart-owned-flipkart-through-gemini-and-ai-mode-in-india/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-27T01:30:00+00:00",
    "summary": "The limited test covers select products and users, with a broader rollout planned for later in October."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/26/insurers-claim-ai-is-already-increasing-healthcare-costs/",
    "domain": "大厂 AI 动态",
    "title": "Insurers claim AI is already increasing healthcare costs",
    "url": "https://techcrunch.com/2026/09/26/insurers-claim-ai-is-already-increasing-healthcare-costs/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T21:02:06+00:00",
    "summary": "Blue Cross Blue Shield says hospital use of AI tools led to an additional $942M in healthcare spending over a two-year period."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/26/tiktok-agrees-to-pay-at-least-100m-in-alabama-settlement/",
    "domain": "大厂 AI 动态",
    "title": "TikTok agrees to pay at least $100M in Alabama settlement",
    "url": "https://techcrunch.com/2026/09/26/tiktok-agrees-to-pay-at-least-100m-in-alabama-settlement/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T20:24:45+00:00",
    "summary": "TikTok will pay Alabama at least $100 million in a settlement tied to allegations that the short-form video platform misled users about safety and was designed to addict children."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/26/meta-says-it-will-run-ads-for-musk-documentary-after-all/",
    "domain": "大厂 AI 动态",
    "title": "Meta and YouTube say they will run ads for ‘Musk’ documentary after all",
    "url": "https://techcrunch.com/2026/09/26/meta-says-it-will-run-ads-for-musk-documentary-after-all/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T17:44:00+00:00",
    "summary": "Two companies now say they will accept advertising for director Alex Gibney’s upcoming documentary about Elon Musk, following earlier reporting that a number of social media platforms had rejected the"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/26/levoits-new-air-purifier-is-for-the-pet-odors-that-have-taken-over-your-apartment/",
    "domain": "大厂 AI 动态",
    "title": "Levoit’s new air purifier is for the pet odors that have taken over your apartment",
    "url": "https://techcrunch.com/2026/09/26/levoits-new-air-purifier-is-for-the-pet-odors-that-have-taken-over-your-apartment/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T17:00:00+00:00",
    "summary": "This $189.99 air purifier is specifically designed to tackle pet odors, removing up to 70% in one hour."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/26/i-created-an-interactive-digital-avatar-of-myself-and-you-can-talk-to-it/",
    "domain": "大厂 AI 动态",
    "title": "I created an interactive digital avatar of myself — and you can talk to it",
    "url": "https://techcrunch.com/2026/09/26/i-created-an-interactive-digital-avatar-of-myself-and-you-can-talk-to-it/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T14:00:00+00:00",
    "summary": "After obtaining an interactive avatar and training it to discuss venture fraud, I have mixed feelings about making AI clones of ourselves."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/25/at-meta-connect-the-companys-smart-glasses-were-everywhere/",
    "domain": "大厂 AI 动态",
    "title": "At Meta Connect, the company’s smart glasses were everywhere",
    "url": "https://techcrunch.com/2026/09/25/at-meta-connect-the-companys-smart-glasses-were-everywhere/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T01:08:57+00:00",
    "summary": "The company behind Facebook and Instagram wants to keep consumers connected to the digital world via its ever-growing line of smart glasses."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/25/crusoe-abandons-1-25b-plan-to-use-boom-turbines-at-ai-data-centers/",
    "domain": "大厂 AI 动态",
    "title": "Crusoe abandons $1.25B plan to use Boom turbines at AI data centers",
    "url": "https://techcrunch.com/2026/09/25/crusoe-abandons-1-25b-plan-to-use-boom-turbines-at-ai-data-centers/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T23:11:10+00:00",
    "summary": "Boom Supersonic CEO Blake Scholl said the company's new stationary power plants were no longer in Crusoe's near-term plans."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/25/automattic-has-a-new-board-after-failed-attempt-to-put-ceo-on-leave/",
    "domain": "大厂 AI 动态",
    "title": "Automattic has a new board after failed attempt to put CEO on leave",
    "url": "https://techcrunch.com/2026/09/25/automattic-has-a-new-board-after-failed-attempt-to-put-ceo-on-leave/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T23:04:34+00:00",
    "summary": "After days of upheaval at Automattic, following a failed attempt to remove CEO Matt Mullenweg, the company has a new board."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/25/unsecured-openai-agents-posted-53-user-images-on-the-internet-without-the-labs-knowledge/",
    "domain": "大厂 AI 动态",
    "title": "Unsecured OpenAI agents posted 53 user images on the internet without the lab’s knowledge",
    "url": "https://techcrunch.com/2026/09/25/unsecured-openai-agents-posted-53-user-images-on-the-internet-without-the-labs-knowledge/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T22:20:47+00:00",
    "summary": "AI agents operating in OpenAI's research environment posted user images on public image-hosting sites without the lab's knowledge."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/25/meta-opens-early-access-program-for-new-muse-features/",
    "domain": "大厂 AI 动态",
    "title": "Meta opens early access program for new Muse features",
    "url": "https://techcrunch.com/2026/09/25/meta-opens-early-access-program-for-new-muse-features/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T20:34:53+00:00",
    "summary": "Anyone interested in joining has to ask Muse to put them on the list."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/25/the-hottest-new-hangout-for-middle-schoolers-is-nprs-comment-section/",
    "domain": "大厂 AI 动态",
    "title": "The hottest new hangout for middle schoolers is NPR’s comment section?",
    "url": "https://techcrunch.com/2026/09/25/the-hottest-new-hangout-for-middle-schoolers-is-nprs-comment-section/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T20:33:58+00:00",
    "summary": "When NPR staffers flagged strange comments under their podcasts on Spotify as bots, it took a Gen Z colleague to (immediately) figure out the mystery."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/25/anthropic-to-pay-akamai-11-6-billion-over-seven-years-in-cloud-deal/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic to pay Akamai $11.6 billion over seven years in cloud deal",
    "url": "https://techcrunch.com/2026/09/25/anthropic-to-pay-akamai-11-6-billion-over-seven-years-in-cloud-deal/",
    "source": "Aditya Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T19:13:38+00:00",
    "summary": "Anthropic has committed $11.6 billion over seven years to Akamai's cloud infrastructure, a bet on CPUs that could grow to about $20 billion, and in an unusual arrangement, Akamai is giving Anthropic a"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/25/mark-wahlberg-is-coming-to-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "Mark Wahlberg is coming to TechCrunch Disrupt 2026, and he wants to talk about your work, not his",
    "url": "https://techcrunch.com/2026/09/25/mark-wahlberg-is-coming-to-techcrunch-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T18:48:33+00:00",
    "summary": "Mark Wahlberg joins Bruce K. Lee at Disrupt to discuss investing, entrepreneurship, healthcare, wellness, and building businesses."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/25/ahead-of-u-s-ipo-british-ai-neocloud-nscale-secures-3-36b-in-convertible-finacing/",
    "domain": "大厂 AI 动态",
    "title": "Ahead of US IPO, British AI neocloud Nscale secures $3.36B in convertible financing",
    "url": "https://techcrunch.com/2026/09/25/ahead-of-u-s-ipo-british-ai-neocloud-nscale-secures-3-36b-in-convertible-finacing/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T18:33:59+00:00",
    "summary": "The funding, which comes from Third Point, Nvidia, and others, will fuel the company's massive AI data center buildout."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/25/the-aeropod-automates-soil-aeration-without-robotics-see-it-at-techcrunch-disrupt/",
    "domain": "大厂 AI 动态",
    "title": "The Aeropod automates soil aeration without robotics — see it at TechCrunch Disrupt",
    "url": "https://techcrunch.com/2026/09/25/the-aeropod-automates-soil-aeration-without-robotics-see-it-at-techcrunch-disrupt/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T17:30:00+00:00",
    "summary": "Muju Earth Technologies has developed a deceptively simply pod that can save farmers money while improving crop yields."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/25/some-supabase-customers-are-publicly-exposing-reams-of-peoples-data-to-the-web/",
    "domain": "大厂 AI 动态",
    "title": "Some Supabase customers are publicly exposing reams of people’s data to the web",
    "url": "https://techcrunch.com/2026/09/25/some-supabase-customers-are-publicly-exposing-reams-of-peoples-data-to-the-web/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T17:29:46+00:00",
    "summary": "The findings highlight how AI-generated and vibe-coded apps can spill and expose users' data when not configured or secured properly."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/25/astra-and-opus-just-passed-turings-other-test/",
    "domain": "大厂 AI 动态",
    "title": "Astra and Opus just passed Turing’s other test",
    "url": "https://techcrunch.com/2026/09/25/astra-and-opus-just-passed-turings-other-test/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T17:24:36+00:00",
    "summary": "Frontier AI models are finishing Alan Turing's World War II codebreaking work."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/25/meta-is-putting-its-muscle-behind-muse-as-the-ai-app-takes-off/",
    "domain": "大厂 AI 动态",
    "title": "Meta is putting its muscle behind Muse as the AI app takes off",
    "url": "https://techcrunch.com/2026/09/25/meta-is-putting-its-muscle-behind-muse-as-the-ai-app-takes-off/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T16:16:52+00:00",
    "summary": "Muse is topping the app store charts and adding users at a rapid clip, while Meta ramps up the personal AI agent's promotion across its own apps and beyond."
  },
  {
    "id": "rss:https://stratechery.com/2026/begun-the-aggregator-wars-have/",
    "domain": "大厂 AI 动态",
    "title": "2026.39: Begun, the Aggregator Wars Have",
    "url": "https://stratechery.com/2026/begun-the-aggregator-wars-have/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T17:00:00+00:00",
    "summary": "The best Stratechery content from the week of September 21, 2026, including Meta vs. Amazon, GM bending the knee to CarPlay, and profiling the profiler."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/09/teslas-big-electric-truck-faces-an-even-bigger-infrastructure-challenge/",
    "domain": "大厂 AI 动态",
    "title": "Tesla’s big electric truck faces an even bigger infrastructure challenge",
    "url": "https://arstechnica.com/cars/2026/09/teslas-big-electric-truck-faces-an-even-bigger-infrastructure-challenge/",
    "source": "Aarian Marshall, wired.com",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T10:45:09+00:00",
    "summary": "The 500-mile Semi arrives as charging gaps still limit electric trucking."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/09/can-trump-ever-be-wrong-his-pick-to-lead-fda-refused-to-say/",
    "domain": "大厂 AI 动态",
    "title": "Can Trump ever be wrong? His pick to lead FDA refused to say.",
    "url": "https://arstechnica.com/health/2026/09/can-trump-ever-be-wrong-his-pick-to-lead-fda-refused-to-say/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T23:00:26+00:00",
    "summary": "Heidi Overton faced questions focused on vaccines, birth control, and vapes."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/09/court-rules-trump-can-blacklist-anthropic-for-refusing-to-enable-claude-features/",
    "domain": "大厂 AI 动态",
    "title": "Court rules Pentagon can blacklist Anthropic for refusing to enable Claude features",
    "url": "https://arstechnica.com/tech-policy/2026/09/court-rules-trump-can-blacklist-anthropic-for-refusing-to-enable-claude-features/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T21:36:20+00:00",
    "summary": "\"Overly constrained AI models\" could cause military operations to fail, judges say."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/09/tesla-workers-balk-at-training-optimus-humanoid-robots-as-replacements/",
    "domain": "大厂 AI 动态",
    "title": "Tesla workers balk at training Optimus humanoid robots as replacements",
    "url": "https://arstechnica.com/ai/2026/09/tesla-workers-balk-at-training-optimus-humanoid-robots-as-replacements/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T21:10:51+00:00",
    "summary": "Despite challenges, Tesla aims for 1,000 Optimus robots per week by end of 2026."
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
    "id": "hn:49826087",
    "domain": "股票",
    "title": "16GB iPod Nano 3G Upgrade",
    "url": "https://tuckerosman.com/projects/16gb-ipod-nano",
    "source": "Ivoah",
    "platform": "hackernews",
    "points": 154,
    "published_at": "2026-09-24T03:58:54+00:00",
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
    "id": "rss:https://www.netinterest.co/p/the-agents-revolt",
    "domain": "股票",
    "title": "The Agents Revolt",
    "url": "https://www.netinterest.co/p/the-agents-revolt",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T17:33:27+00:00",
    "summary": "What happens to finance when customers start paying attention"
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
    "id": "hn:49778029",
    "domain": "金融",
    "title": "Samsung is expected to more than double output of its HBM4 and HBM4E DRAM",
    "url": "https://en.sedaily.com/finance/2026/09/20/samsung-to-double-hbm4-output-next-year-sources-say",
    "source": "giuliomagnifico",
    "platform": "hackernews",
    "points": 561,
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
    "points": 255,
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
    "id": "hn:49832844",
    "domain": "金融",
    "title": "Federal judge orders Texas to air condition all prisons by the end of 2029",
    "url": "https://www.texastribune.org/2026/09/22/texas-prison-air-conditioning-lawsuit-ruling/",
    "source": "bonefishgrill",
    "platform": "hackernews",
    "points": 117,
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
    "id": "hn:49849986",
    "domain": "金融",
    "title": "Show HN: Ekselio – Loveable for finance workflows (local first)",
    "url": "https://www.gptbeyond.com/try?home=1",
    "source": "kdautaj",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-09-25T21:09:28+00:00",
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
    "id": "hn:49828019",
    "domain": "金融",
    "title": "Show HN: Trader News – Hacker News for Finance",
    "url": "https://news.ycombinator.com/item?id=49828019",
    "source": "FailMore",
    "platform": "hackernews",
    "points": 25,
    "published_at": "2026-09-24T08:54:57+00:00",
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
