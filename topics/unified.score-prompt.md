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

- 今日日期：`2026-08-26`
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
  "date": "2026-08-26",
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
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 1188537,
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
    "points": 1105518,
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
    "points": 878035,
    "published_at": "2025-05-01T09:00:00+00:00",
    "summary": "up的科学星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV1ZzvUBXEoL",
    "domain": "AI",
    "title": "【2026最新版】保姆级AI Agent智能体系统教程，手把手带你从0基础开始搭建企业级AI Agent智能体！全程干货无废话！让你少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av115818910194374",
    "source": "极客教学",
    "platform": "bilibili",
    "points": 860758,
    "published_at": "2026-01-01T08:40:14+00:00",
    "summary": "【2026最新版】保姆级AI Agent智能体系统教程，手把手带你从0基础开始搭建企业级AI Agent智能体！全程干货无废话！让你少走99%的弯路！"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 637219,
    "published_at": "2026-07-01T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260701\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\nAI大模型开发热门教程：\nAI大模型开发：BV1h1"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 599922,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1aDMezREUj",
    "domain": "AI",
    "title": "Cursor使用教程，2小时玩转cursor，cursor无限续杯",
    "url": "http://www.bilibili.com/video/av114691716154833",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 585456,
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
    "points": 440023,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1AnQNYxEsy",
    "domain": "AI",
    "title": "MCP是啥？技术原理是什么？一个视频搞懂MCP的一切。Windows系统配置MCP，Cursor Cline使用MCP",
    "url": "http://www.bilibili.com/video/av114155298228756",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 421329,
    "published_at": "2025-03-13T13:18:09+00:00",
    "summary": "MCP是近期的AI领域的热点，特别是在海外社区获得热烈讨论，每天都有大量MCP工具诞生。本期视频我们从MCP的概念，技术原理，到多场景实战，一个视频看懂MCP的全部内容。\n\n\nMCP官方开源仓库：https://github.com/modelcontextprotocol/servers\nMCP合集网站：  https://smithery.ai/\nVscode下载：https://code.v"
  },
  {
    "id": "bvid:BV1vG8QzcE5X",
    "domain": "AI",
    "title": "Claude使用指南，claude code零基础教程，claude code安装配置到实战",
    "url": "http://www.bilibili.com/video/av114933744272468",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 352709,
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
    "points": 273723,
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
    "points": 254606,
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
    "points": 247142,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV16Luq6FEmP",
    "domain": "AI",
    "title": "当不懂代码的老婆，第一次接触vibe coding……",
    "url": "http://www.bilibili.com/video/av117076211536327",
    "source": "糖果果的未来要发光",
    "platform": "bilibili",
    "points": 180966,
    "published_at": "2026-08-11T09:50:27+00:00",
    "summary": "当不懂代码的老婆，第一次接触vibe coding……"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 179900,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 170422,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 161299,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 145105,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 99627,
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
    "points": 93369,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1A24y1J7Dt",
    "domain": "AI",
    "title": "如何在VS Code中使用Cursor自动生成代码",
    "url": "http://www.bilibili.com/video/av781409810",
    "source": "许你再少年",
    "platform": "bilibili",
    "points": 74197,
    "published_at": "2023-03-23T11:32:23+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1myM96nETU",
    "domain": "AI",
    "title": "AI 赛博女友！本地部署教程，无需 API、完全免费，8G显存就能跑！实时语音聊天，几乎零延迟，太上头了！| 零度解说",
    "url": "http://www.bilibili.com/video/av117032322339286",
    "source": "零度解说",
    "platform": "bilibili",
    "points": 58207,
    "published_at": "2026-08-04T12:00:00+00:00",
    "summary": "AI 赛博女友一键安装包下载：https://www.freedidi.com/24984.html"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 54474,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1vYFQzQE4P",
    "domain": "AI",
    "title": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！Claude Code Hooks回调+Agent Teams全自动开发零轮询",
    "url": "http://www.bilibili.com/video/av116046157647899",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 47650,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 46885,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 41051,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1AeeJzhEgg",
    "domain": "AI",
    "title": "如何选择一家靠谱的Claude Code中转站",
    "url": "http://www.bilibili.com/video/av115082692403009",
    "source": "野码AI",
    "platform": "bilibili",
    "points": 37604,
    "published_at": "2025-08-25T03:25:00+00:00",
    "summary": "在用了超过5个不同的中转站后，我总结了如何选择一家靠谱的中转站的几点分享给大家，供大家参考，如果对你有帮助，记得三连+关注，需要相关资料的私信领取，谢谢。"
  },
  {
    "id": "bvid:BV1cCj2ztEf5",
    "domain": "AI",
    "title": "Cursor+Claude Code+Claude 4终极组合！仅用10分钟为开源项目Magentic-UI完美集成JWT用户认证系统，编程效率提升300%",
    "url": "http://www.bilibili.com/video/av114574527307727",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 35167,
    "published_at": "2025-05-26T14:20:15+00:00",
    "summary": "Cursor+Claude Code+Claude 4终极组合！仅用10分钟为开源项目Magentic-UI完美集成JWT用户认证系统，编程效率提升300%，告别传统开发模式！小白也能轻松开发商业项目\n\n🚀🚀🚀视频简介：\n✅【保姆级教程】从技术栈分析到功能实现：Claude Code完整开发流程深度解析！从零开始为微软开源智能体项目添加完整用户认证功能，支持注册登录退出，让你的AI应用瞬间变身多用"
  },
  {
    "id": "bvid:BV1AGRtBnE3S",
    "domain": "AI",
    "title": "别手动写测试用例了!2026最新Claude Code+Skills实现需求文档生成全量用例|全流程AI驱动软件测试落地方案,测试效率翻10倍！",
    "url": "http://www.bilibili.com/video/av116528787756865",
    "source": "清风说测试开发",
    "platform": "bilibili",
    "points": 32511,
    "published_at": "2026-05-07T00:00:00+00:00",
    "summary": "全栈课一共分为6大块内容\n第一块：AI智能体开发基础(AI大模型、工具、记忆、MCP、中间件、Skills等核心内容)\n第二块：Claude Code,Trea+skills实现基于需求文档生成用例，基于OpenClaw实现接口自动化落地，基于hermes Agent实现web自动化落地\n第三块：功能测试的智能体开发(项目RAG知识库搭建+Agent搭建+skills开发，实现用例生成的Agent"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operitAI教程：入门安卓最强大ai平台",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 32347,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29666,
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
    "points": 28890,
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
    "points": 26771,
    "published_at": "2026-04-03T16:14:43+00:00",
    "summary": "每个参数都是干什么的，如何修改提示词的教程。\n不知道这是什么？请看合集内的视频~\n我做了一个 AI 的杀戮尖塔2MOD！\n可以和怪物对话，策反怪物，带着怪物爬塔（重写了几乎每一个怪物在友方时候的行为），还能给怪物打防御，带个沙虫全吃了！\n可以和上古之民对话，聊嗨了会给你 1～2 个额外赐福，还能帮你指示为未来\n可以让偷窃草蜢偷队友的 key 卡，想无限？偷了！\n可以和商人讨价还价，甚至白嫖\n多人的"
  },
  {
    "id": "bvid:BV1WtoTBiEuR",
    "domain": "AI",
    "title": "Claude Code多Agent模式实战分享",
    "url": "http://www.bilibili.com/video/av116454666012312",
    "source": "Simon林_",
    "platform": "bilibili",
    "points": 25049,
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
    "points": 22742,
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
    "points": 20172,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1ofSSBfEC1",
    "domain": "AI",
    "title": "小白也会的trae里安装 claude code 教程",
    "url": "http://www.bilibili.com/video/av116352710870207",
    "source": "长留-AIGC",
    "platform": "bilibili",
    "points": 18638,
    "published_at": "2026-04-05T15:08:17+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV14erKYuEaE",
    "domain": "AI",
    "title": "最强编程AI Cursor+Unity制作一个史诗游戏(详细)",
    "url": "http://www.bilibili.com/video/av113774908413987",
    "source": "多西杰克",
    "platform": "bilibili",
    "points": 17750,
    "published_at": "2025-01-05T09:01:00+00:00",
    "summary": "网上惊呼Cursor AI厉害的内容很多，但结合Unity做游戏的不多，我就来实测一下，做一个AAA大作......"
  },
  {
    "id": "bvid:BV1rEJ8znEoj",
    "domain": "AI",
    "title": "Cursor+Stagewise插件，给ＡI装上眼睛，前端可视化编程，开发效率提升10倍！",
    "url": "http://www.bilibili.com/video/av114540016572317",
    "source": "为梦想的旅途助力",
    "platform": "bilibili",
    "points": 11390,
    "published_at": "2025-05-20T11:55:43+00:00",
    "summary": "想象一下，您可以将浏览器环境变成轻量级的可视化编辑器，以便您可以直接在浏览器中与 AI 聊天来修改屏幕上的任何 UI，并且它会立即在您的 Cursor 中完成工作。\n\nStagewise能够将您的浏览器用户界面与代码编辑器相连接，为您的 AI 代理提供实时上下文。\n\n大白话就是你可以在网页上任意地方选择，然后一键发送需要修改或者完善的内容给AI编辑器，Cursor这类编辑器就收到了指令，然后开始工"
  },
  {
    "id": "bvid:BV1GvmzBUEfj",
    "domain": "AI",
    "title": "【AI杂谈】3 claude code概念讲解与配置",
    "url": "http://www.bilibili.com/video/av115718414668601",
    "source": "左-岚",
    "platform": "bilibili",
    "points": 9595,
    "published_at": "2025-12-14T14:38:05+00:00",
    "summary": "飞书的ai杂谈目录下\nhttps://my.feishu.cn/wiki/space/7600816265116011716\n\n米醋工作室 AI 开发环境配置完整指南https://www.micu.wiki/t/topic/571\nClaude Code 常见问题与故障排查https://www.micu.wiki/t/topic/570\nClaude Code 核心概念详解\nhttps://w"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 9420,
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
    "points": 8839,
    "published_at": "2026-06-08T10:17:31+00:00",
    "summary": "手把手教你如何使用最新乐鑫文档知识库，帮你在 Claude / Cursor 等平台解答问题、生成代码、迁移 ESP-IDF 版本、烧录固件。 MCP 服务器现已支持微信扫码一键登录，快来一试！\n\n视频重点内容包括👇：\n\n- 如何将 MCP 服务器添加到 VS Code\n- 让 Copilot 基于乐鑫文档对比旧版和最新版 I2C 驱动\n- 驱动迁移\n- Copilot 编译代码、烧录代码并监控输"
  },
  {
    "id": "bvid:BV1Tz8g6HErC",
    "domain": "AI",
    "title": "【全748集】B站最全最细的AI Agent零基础入门教程，2026最新版，教学通俗易懂，小白适用！普通人也能抓住的AI风口！手把手教会你agent智能体搭建~",
    "url": "http://www.bilibili.com/video/av117115201789701",
    "source": "AI全栈开发",
    "platform": "bilibili",
    "points": 8278,
    "published_at": "2026-08-18T11:27:05+00:00",
    "summary": "【2026最新版AI Agent智能体零基础全套教程 | 配套源码+学习路线+项目案例，看置顶评论自取】\n本套教程专为零基础设计，从Agent原理到独立打造智能体，手把手带你系统掌握AI Agent智能体搭建。\n✅ Agent基础：什么是Agent、三大核心能力（规划/工具/记忆）\n✅ 主流框架：Langchain、LangGraph主流框架\n✅ 多Agent协作：A2A协议、任务编排与调度\n✅ "
  },
  {
    "id": "bvid:BV1xh3C6cEGv",
    "domain": "AI",
    "title": "两周完成一篇SCI论文，用claude code帮你干",
    "url": "http://www.bilibili.com/video/av117002408559933",
    "source": "博士大师兄木水",
    "platform": "bilibili",
    "points": 7694,
    "published_at": "2026-07-29T08:53:04+00:00",
    "summary": "大师兄八股文SCI速成模板已制作成skill，手把手带你实现一键生成SCI论文初稿"
  },
  {
    "id": "bvid:BV1zcTTznEL8",
    "domain": "AI",
    "title": "MCP应用：为小智增加在线点歌服务",
    "url": "http://www.bilibili.com/video/av114635462156272",
    "source": "无敌哥-AI治理架构师",
    "platform": "bilibili",
    "points": 7406,
    "published_at": "2025-06-06T08:30:10+00:00",
    "summary": "除了对话、人脸识别、摄像头识别场景多模态交互外！其实，听音乐是我们的刚需，今天就给小智加上！背后利用了MCP ，话说MCP 真实为小智增加了无线可能！大家有啥想法，可以尽管提哈！"
  },
  {
    "id": "bvid:BV1Y1bv68Eq9",
    "domain": "AI",
    "title": "DeepSeek Harness 多 Agent 协作插件开源！一条指令拉起 Agent Teams",
    "url": "http://www.bilibili.com/video/av117111879898943",
    "source": "程序员阿江-Relakkes",
    "platform": "bilibili",
    "points": 6989,
    "published_at": "2026-08-18T10:30:00+00:00",
    "summary": "这期分享我在 DeepSeek Harness 内测期间开发的开源插件 `dsh-agent-teams`。\n\n当你明确指定使用 Agent Teams 后，插件会自动完成：\n\n- 创建队长与多个成员 Agent；\n- 分析任务并生成依赖 DAG；\n- 无依赖任务并行执行；\n- 通过共享任务池原子领取任务，避免成员冲突；\n- 通过本地数据协议完成队长、成员之间的通信与状态同步；\n- 为不同成员配置"
  },
  {
    "id": "bvid:BV1QU6GYFEio",
    "domain": "AI",
    "title": "[课程4] 用Cursor开发数据库真的很简单 | Agent应用 | 用Codebase解决跨文件错误",
    "url": "http://www.bilibili.com/video/av113742109021318",
    "source": "Zhu的AI日记",
    "platform": "bilibili",
    "points": 7024,
    "published_at": "2024-12-31T12:30:00+00:00",
    "summary": "***这是全网最完整的分享如何在不懂编程的情况下，利用结构化思维，用Cursor开发商业app的系列课程。\n《懒人记单词》是基于艾宾浩斯遗忘曲线设计的记单词神器，它可以对每一个单词进行人性化的解读，并在每一个遗忘周期到来时及时提醒，并通过单词释义选择，拼写和造句进行全方位的巩固，同时AI还能对你的句子进行多维度的评估，确保你对每一个单词不仅会认，而且会用。\n\n***你将在本视频中学到：\n1.数据库"
  },
  {
    "id": "bvid:BV1u4G9zmEte",
    "domain": "AI",
    "title": "什么是MCP？VS Code中使用MCP Server",
    "url": "http://www.bilibili.com/video/av114426032168712",
    "source": "AI落地派",
    "platform": "bilibili",
    "points": 6918,
    "published_at": "2025-04-30T08:51:30+00:00",
    "summary": "什么是MCP，怎么样使用MCP Server，不用写SQL语句就可以查询数据库。\n\nMCP Servers\nhttps://smithery.ai/\nhttps://github.com/punkpeye/awesome-mcp-servers\nhttps://github.com/modelcontextprotocol/servers\n\nMCP Server for MySQL based o"
  },
  {
    "id": "bvid:BV1fNs9eiEm9",
    "domain": "AI",
    "title": "Cursor AI编程结合cocos3.8游戏开发教程-01",
    "url": "http://www.bilibili.com/video/av113187471105975",
    "source": "太阳8800",
    "platform": "bilibili",
    "points": 6702,
    "published_at": "2024-09-23T15:15:13+00:00",
    "summary": "开源源码仓库\nhttps://gitee.com/gamepublic/chess-cards"
  },
  {
    "id": "bvid:BV1aSR4BKESW",
    "domain": "AI",
    "title": "安卓手机部署Claude Code",
    "url": "http://www.bilibili.com/video/av116526891993752",
    "source": "中国小骑士",
    "platform": "bilibili",
    "points": 6662,
    "published_at": "2026-05-06T09:24:14+00:00",
    "summary": "通过Termux安装Claude Code并且接入国内大模型"
  },
  {
    "id": "hn:49434378",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI Jalapeño: Better than Nvidia Blackwell",
    "url": "https://newsletter.semianalysis.com/p/openai-jalapeno-better-than-nvidia",
    "source": "bmulholland",
    "platform": "hackernews",
    "points": 376,
    "published_at": "2026-08-25T14:06:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:49323686",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia dramatically reduces amount of OpenAI infra financing it may guarantee",
    "url": "https://www.reuters.com/business/nvidia-scales-back-250-billion-openai-data-center-guarantee-wsj-reports-2026-08-14/",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 254,
    "published_at": "2026-08-16T21:07:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:49417669",
    "domain": "AI 算力 / 半导体",
    "title": "Some of Russia's A.I. Drones Are Powered by Nvidia",
    "url": "https://www.nytimes.com/2026/08/24/world/europe/ukraine-war-nvidia-ai-autonomous-drones.html",
    "source": "reaperducer",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-08-24T10:16:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:49436796",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI claims its new chips can outperform Nvidia processors in tests",
    "url": "https://www.bloomberg.com/news/articles/2026-08-25/openai-claims-its-new-chips-can-outperform-nvidia-processors-in-tests",
    "source": "TravisJamison",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-08-25T16:35:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:49423067",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Groq 3 LPX Unlocks Ultrafast Interactivity at Long Context",
    "url": "https://developer.nvidia.com/blog/how-nvidia-groq-3-lpx-unlocks-ultrafast-interactivity-at-long-context-on-nvidia-vera-rubin/",
    "source": "frozenport",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-08-24T17:22:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:49424444",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia customers notified about AI-related price hikes above 15%",
    "url": "https://www.reuters.com/business/nvidia-customers-notified-about-ai-related-price-hikes-above-15-bloomberg-news-2026-08-22/",
    "source": "dgellow",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-08-24T19:06:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:49387755",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia AVO scores 100% on the ARC-AGI-3 interactive reasoning benchmark",
    "url": "https://twitter.com/NVIDIAAI/status/2090786258981466231",
    "source": "dsrtslnd23",
    "platform": "hackernews",
    "points": 71,
    "published_at": "2026-08-21T13:26:03+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/the-complete-iot-mesh-solution-making-wi-sun-deployments-simple/",
    "domain": "AI 算力 / 半导体",
    "title": "The Complete IoT Mesh Solution: Making Wi-SUN Deployments Simple",
    "url": "https://www.eetimes.com/the-complete-iot-mesh-solution-making-wi-sun-deployments-simple/",
    "source": "Digi, Silicon Labs, Arrow Electronics",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T16:31:04+00:00",
    "summary": "Join us for a technical walkthrough of the Digi XBee for Wi-SUN platform and a live demo showing how quickly you can go from development kit to a fully managed, self-healing mesh network ready for pro"
  },
  {
    "id": "rss:https://www.eetimes.com/engineering-fiber-optic-solutions-for-next-generation-space-applications/",
    "domain": "AI 算力 / 半导体",
    "title": "Engineering Fiber Optic Solutions for Next-Generation Space Applications",
    "url": "https://www.eetimes.com/engineering-fiber-optic-solutions-for-next-generation-space-applications/",
    "source": "TE Connectivity",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T14:00:00+00:00",
    "summary": "As satellite systems demand greater bandwidth, lower weight, and higher reliability, engineers face significant challenges when integrating fiber optics into space-qualified platforms. This case study"
  },
  {
    "id": "rss:https://www.eetimes.com/yokogawa-releases-ct500sa-and-ct200sa-ac-dc-split-core-current-sensors/",
    "domain": "AI 算力 / 半导体",
    "title": "Yokogawa Releases CT500SA and CT200SA AC/DC Split Core Current Sensors",
    "url": "https://www.eetimes.com/yokogawa-releases-ct500sa-and-ct200sa-ac-dc-split-core-current-sensors/",
    "source": "Yokogawa Test and Measurement Corporation",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T13:50:53+00:00",
    "summary": "(Tokyo, Japan – August 19, 2026) Yokogawa Test &#38; Measurement Corporation today announces the release of its second-generation of AC/DC split core current sensors, the CT500SA and CT200SA. Designed"
  },
  {
    "id": "rss:https://www.eetimes.com/tsmcs-hbm-packaging-yield-issues-help-intel-analysts-say/",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC’s HBM-Packaging Yield Issues Help Intel, Analysts Say",
    "url": "https://www.eetimes.com/tsmcs-hbm-packaging-yield-issues-help-intel-analysts-say/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T07:00:00+00:00",
    "summary": "TSMC’s CoWoS bottlenecks could hand Intel a foundry opening as AI chipmakers eye EMIB and new memory tech. The post TSMC’s HBM-Packaging Yield Issues Help Intel, Analysts Say appeared first on EE Time"
  },
  {
    "id": "rss:https://www.eetimes.com/nxp-expands-industrial-endpoint-access-with-mcu-topology-discovery/",
    "domain": "AI 算力 / 半导体",
    "title": "NXP Expands Industrial Endpoint Access with MCU Topology Discovery",
    "url": "https://www.eetimes.com/nxp-expands-industrial-endpoint-access-with-mcu-topology-discovery/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T17:00:00+00:00",
    "summary": "NXP’s MCX A5 identifies and maps connected devices to improve network visibility, turning endpoints into accessible sources of real-time data for analytics, automation, and industrial edge AI. The pos"
  },
  {
    "id": "rss:https://www.eetimes.com/radiation-tolerance-of-tantalum-polymer-capacitors/",
    "domain": "AI 算力 / 半导体",
    "title": "Radiation Tolerance of Tantalum Polymer Capacitors",
    "url": "https://www.eetimes.com/radiation-tolerance-of-tantalum-polymer-capacitors/",
    "source": "Krystof Adamek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T14:00:00+00:00",
    "summary": "Environments rich in ionizing radiation create a particularly difficult functional challenge for electronic components. Spacecraft, nuclear reactors, particle accelerators, and hardened military equip"
  },
  {
    "id": "rss:https://www.eetimes.com/welcome-to-the-era-of-trustworthy-ai-for-ic-signoff-and-manufacturing/",
    "domain": "AI 算力 / 半导体",
    "title": "Welcome to the Era of Trustworthy AI for IC Signoff and Manufacturing",
    "url": "https://www.eetimes.com/welcome-to-the-era-of-trustworthy-ai-for-ic-signoff-and-manufacturing/",
    "source": "Juan Rey, Senior Vice President, General Manager and CTO of the Calibre segment, Siemens EDA",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T13:00:00+00:00",
    "summary": "Trust is the key to AI adoption in chip design. See how deterministic EDA engines and explainable AI can accelerate signoff and manufacturing. The post Welcome to the Era of Trustworthy AI for IC Sign"
  },
  {
    "id": "rss:https://www.eetimes.com/hp1800-the-magic-of-single-stage-48v-to-ultra-low-voltage/",
    "domain": "AI 算力 / 半导体",
    "title": "HP1800: The Magic of Single-Stage 48V to Ultra-Low Voltage",
    "url": "https://www.eetimes.com/hp1800-the-magic-of-single-stage-48v-to-ultra-low-voltage/",
    "source": "Hynetek Semiconductor Co., Ltd.",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T13:00:00+00:00",
    "summary": "HP1800 PWM phase-doubler turns 1 tri-state PWM input to four 180° interleaved complementary outputs. It enables 90–92% efficient single-stage 48V-to-1V AI PoL conversion (vs ~86% two-stage), cutting P"
  },
  {
    "id": "rss:https://www.eetimes.com/nvidia-inference-pivot-reaches-rebellions-in-korea/",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia’s Inference Pivot Reaches Rebellions in Korea",
    "url": "https://www.eetimes.com/nvidia-inference-pivot-reaches-rebellions-in-korea/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T08:07:18+00:00",
    "summary": "Nvidia is reportedly in talks with Korean inference upstart Rebellions about a technical partnership, investment, or acquisition. The post Nvidia’s Inference Pivot Reaches Rebellions in Korea appeared"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/nda-5pm-et-tuesday-commodore-77-special-edition-c64u-uses-more-powerful-amd-artix-xc7a100t-processor-preorders-for-cyberpunk-2077-inspired-design-open-today-at-usd377",
    "domain": "AI 算力 / 半导体",
    "title": "Commodore unveils striking Cyberpunk 2077 version of its C64U made in partnership with CD Projekt Red — Commodore 77 special edition uses more powerful AMD Artix XC7A100T processor",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/nda-5pm-et-tuesday-commodore-77-special-edition-c64u-uses-more-powerful-amd-artix-xc7a100t-processor-preorders-for-cyberpunk-2077-inspired-design-open-today-at-usd377",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T21:00:00+00:00",
    "summary": "A special edition of the Commodore 64 Ultimate made in collaboration with CD Projekt Red has been announced today. The new Commodore 77 takes its stylish inspiration from Cyberpunk 77, and is skillful"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/hot-chips-2026-samsung-makes-lpddr5x-smart-with-logic-unit-in-memory-lpddr5x-pim-is-3-01x-faster-than-lpddr5x-in-ai-inference-with-8x-the-bandwidth",
    "domain": "AI 算力 / 半导体",
    "title": "Hot Chips 2026: Samsung makes LPDDR5X smart with logic unit in memory — LPDDR5X-PIM is 3.01x faster than LPDDR5X in AI inference with 8x the bandwidth",
    "url": "https://www.tomshardware.com/pc-components/dram/hot-chips-2026-samsung-makes-lpddr5x-smart-with-logic-unit-in-memory-lpddr5x-pim-is-3-01x-faster-than-lpddr5x-in-ai-inference-with-8x-the-bandwidth",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T18:31:37+00:00",
    "summary": "Samsung detailed the industry's first LPDDR5X-PIM at Hot Chips 2026, adding logic directly to memory to speed up data-intensive workloads like AI inference."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/openai-says-its-jalapeno-chip-beats-nvidias-gb300-in-first-published-benchmarks",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI’s 700W Jalapeño ASIC outpaces 1,400W Nvidia flagship GPU — claims up to 1.9x throughput per kilowatt and 3.6x lower latency, co-developed with Broadcom",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/openai-says-its-jalapeno-chip-beats-nvidias-gb300-in-first-published-benchmarks",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T18:05:23+00:00",
    "summary": "OpenAI arrived at Hot Chips on Tuesday with benchmarks claiming its first in-house chip beats Nvidia's GB300."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/pc-cases/hands-on-with-hytes-y50-rgb-case-premium-looks-at-an-affordable-price",
    "domain": "AI 算力 / 半导体",
    "title": "Hands-on with Hyte’s Y50 RGB case: Premium looks at an affordable price",
    "url": "https://www.tomshardware.com/pc-components/pc-cases/hands-on-with-hytes-y50-rgb-case-premium-looks-at-an-affordable-price",
    "source": "Myles Goldman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T17:00:00+00:00",
    "summary": "Hyte’s Y50 RGB is an affordable option for anyone looking to get a glass chassis with included ARGB fans."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/get-16gb-of-ddr5-ram-for-usd70-and-start-your-am5-gaming-rig-with-this-bundle-usd568-for-ryzen-7-7700x3d-16gb-g-skill-ddr5-ram-asus-tuf-b650-e-motherboard-and-free-aio",
    "domain": "AI 算力 / 半导体",
    "title": "Get 16GB of DDR5 RAM for $70 and start your AM5 gaming rig with this bundle — $568 for Ryzen 7 7700X3D, 16GB G.Skill DDR5 RAM, Asus TUF B650-E motherboard, and free AIO",
    "url": "https://www.tomshardware.com/pc-components/get-16gb-of-ddr5-ram-for-usd70-and-start-your-am5-gaming-rig-with-this-bundle-usd568-for-ryzen-7-7700x3d-16gb-g-skill-ddr5-ram-asus-tuf-b650-e-motherboard-and-free-aio",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T15:59:08+00:00",
    "summary": "568.99 ($200/26% off) gets you a 3-item Newegg combo: a Ryzen 7 7700X3D, Asus B650 board, 16GB of G.Skill DDR5-6000, and a free 240mm AIO thrown in — a inexpensive avenue into AM5."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/hot-chips-2026-intel-details-cutting-edge-tech-in-entry-level-wildcat-lake-value-focused-18a-chips-necessitated-ucie-integration",
    "domain": "AI 算力 / 半导体",
    "title": "Hot Chips 2026: Intel details cutting-edge tech in entry-level Wildcat Lake — value-focused 18A chips necessitated UCIe integration",
    "url": "https://www.tomshardware.com/pc-components/cpus/hot-chips-2026-intel-details-cutting-edge-tech-in-entry-level-wildcat-lake-value-focused-18a-chips-necessitated-ucie-integration",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T15:45:08+00:00",
    "summary": "Intel's Wildcat Lake is competing in the budget laptop market, but it takes a very different approach, leveraging a UCIe interconnect and Intel's latest 18A node."
  },
  {
    "id": "rss:https://www.tomshardware.com/gift-guides-seasonal-sales/best-ram-memory-deals-ddr5-ddr4",
    "domain": "AI 算力 / 半导体",
    "title": "Best RAM deals 2026 — discounts on DDR5 and DDR4 to beat the memory price crunch",
    "url": "https://www.tomshardware.com/gift-guides-seasonal-sales/best-ram-memory-deals-ddr5-ddr4",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T15:14:44+00:00",
    "summary": "We're rounding up the best RAM deals from retailers across the U.S here."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/hot-chips-2026-intel-dives-deep-on-crescent-island-ai-accelerator-larger-caches-and-deeper-xmx-engines-target-maximum-ai-flops-per-watt",
    "domain": "AI 算力 / 半导体",
    "title": "Hot Chips 2026: Intel dives deep on Crescent Island AI accelerator — larger caches and deeper XMX engines target maximum AI FLOPS per watt",
    "url": "https://www.tomshardware.com/pc-components/gpus/hot-chips-2026-intel-dives-deep-on-crescent-island-ai-accelerator-larger-caches-and-deeper-xmx-engines-target-maximum-ai-flops-per-watt",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T15:12:44+00:00",
    "summary": "At Hot Chips 2026, Intel detailed more about its Crescent Island AI accelerator, which uses the Xe3P architecture. The accelerator will use liquid-cooled chips and HBM4 memory to serve inference workl"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/mini-pcs/apple-price-hikes-continue-as-mac-mini-with-16gb-ram-and-256gb-is-now-usd899-1tb-storage-option-adds-usd500-to-entry-level-headless-system",
    "domain": "AI 算力 / 半导体",
    "title": "Apple price hikes continue as Mac mini with 16GB RAM and 256GB is now $899 — 1TB storage option adds $500 to entry-level headless system",
    "url": "https://www.tomshardware.com/desktops/mini-pcs/apple-price-hikes-continue-as-mac-mini-with-16gb-ram-and-256gb-is-now-usd899-1tb-storage-option-adds-usd500-to-entry-level-headless-system",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T14:37:55+00:00",
    "summary": "Apple's Mac mini and Mac Studio see price hikes, while memory and storage upgrades get even more expensive"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/apple-launches-new-m6-and-m5-ultra-apple-silicon-chips-debuting-in-new-mac-mini-and-mac-studio",
    "domain": "AI 算力 / 半导体",
    "title": "Apple launches new M6 and M5 Ultra Apple silicon chips — debuting in new Mac Mini and Mac Studio",
    "url": "https://www.tomshardware.com/pc-components/cpus/apple-launches-new-m6-and-m5-ultra-apple-silicon-chips-debuting-in-new-mac-mini-and-mac-studio",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T13:26:19+00:00",
    "summary": "Apple has announced new M6 and M5 Ultra chips, a new Mac mini, and a new Mac Studio."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/china-strategically-slows-exports-of-critical-materials-used-in-semiconductor-fabrication-to-taiwan-germanium-and-quartz-exports-to-the-region-also-threaten-optical-and-robotics-supply-chain",
    "domain": "AI 算力 / 半导体",
    "title": "China strategically slows exports of critical materials used in semiconductor fabrication to Taiwan — germanium and quartz exports to the region also threaten optical and robotics supply chain",
    "url": "https://www.tomshardware.com/tech-industry/china-strategically-slows-exports-of-critical-materials-used-in-semiconductor-fabrication-to-taiwan-germanium-and-quartz-exports-to-the-region-also-threaten-optical-and-robotics-supply-chain",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T13:00:00+00:00",
    "summary": "China slows exports of germanium, quartz-based materials, and magnets. The move potentially disrupts the optical connectivity, semiconductor, and robotics industries."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/nvidia-jetson-orin-guided-the-russian-ai-drone-that-killed-three-civilians-in-ukraine-forensic-teams-say",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Jetson Orin-guided Russian AI drone killed three civilians in Ukraine, forensic teams say — first documented case of civilian deaths caused by a Russian drone using fully autonomous targeting",
    "url": "https://www.tomshardware.com/tech-industry/drones/nvidia-jetson-orin-guided-the-russian-ai-drone-that-killed-three-civilians-in-ukraine-forensic-teams-say",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T12:40:22+00:00",
    "summary": "A Russian Molniya drone carrying an Nvidia Jetson Orin module killed three civilians at a gas station in Zaporizhzhia last month."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/handheld-gaming/asus-rog-xbox-ally-x20-with-oled-screen-available-october-15-pre-orders-start-now-standalone-system-for-usd1-299-99-or-an-ar-bundle-for-usd2-499-99",
    "domain": "AI 算力 / 半导体",
    "title": "Asus ROG Xbox Ally X20 with OLED screen available October 15, pre-orders start now — standalone system for $1,299.99, or an AR bundle for $2,499.99",
    "url": "https://www.tomshardware.com/video-games/handheld-gaming/asus-rog-xbox-ally-x20-with-oled-screen-available-october-15-pre-orders-start-now-standalone-system-for-usd1-299-99-or-an-ar-bundle-for-usd2-499-99",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T12:30:00+00:00",
    "summary": "At gamescom, Asus finally announced the pricing for the Asus ROG Xbox Ally X20, either as a standalone handheld or a bundle with AR glasses."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/linux/linux-was-announced-by-linus-torvalds-35-years-ago-today-humble-os-started-with-10-000-lines-of-code-but-has-now-grown-to-40-million-dominates-global-infrastructure",
    "domain": "AI 算力 / 半导体",
    "title": "Linux was announced by Linus Torvalds 35 years ago today — humble OS started with 10,000 lines of code but has now grown to 40 million, dominates global infrastructure",
    "url": "https://www.tomshardware.com/software/linux/linux-was-announced-by-linus-torvalds-35-years-ago-today-humble-os-started-with-10-000-lines-of-code-but-has-now-grown-to-40-million-dominates-global-infrastructure",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T12:28:05+00:00",
    "summary": "The development of Linux, a free ‘hobby’ operating system, was announced by Linus Torvalds 35 years ago today."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/micron-says-the-silicon-gap-between-hbm-and-ddr5-is-widening-with-every-generation",
    "domain": "AI 算力 / 半导体",
    "title": "Hot Chips 2026: Micron warns HBM wafer penalty is widening with every generation — AI memory uses 3x more silicon than DDR5, company says memory wall is 'getting worse' as prices rise",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/micron-says-the-silicon-gap-between-hbm-and-ddr5-is-widening-with-every-generation",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T12:19:38+00:00",
    "summary": "Micron Fellow Raghu Sreeramaneni told the Hot Chips 2026 conference that the silicon penalty HBM carries against DDR5 is growing with every generation."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/hot-chips-2026-nvidia-breaks-down-88-core-vera-cpu-spatial-multithreading-benchmarked-1-2-tb-s-socamm2-memory-agentic-workloads-detailed-and-more",
    "domain": "AI 算力 / 半导体",
    "title": "Hot Chips 2026: Nvidia breaks down 88-core Vera CPU — spatial multithreading benchmarked, 1.2 TB/s SOCAMM2 memory, agentic workloads detailed, and more",
    "url": "https://www.tomshardware.com/pc-components/cpus/hot-chips-2026-nvidia-breaks-down-88-core-vera-cpu-spatial-multithreading-benchmarked-1-2-tb-s-socamm2-memory-agentic-workloads-detailed-and-more",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T11:53:48+00:00",
    "summary": "Nvidia has provided more color on its Vera CPU for agentic data centers at Hot Chips 2026, showcasing the benefits of spatial multithreading and the power benefits of the LPDDR5X memory system."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/hdds/stack-up-on-seagate-hard-drives-with-usd30-off-the-8tb-barracuda-hdd-its-lowest-price-at-best-buy-since-april",
    "domain": "AI 算力 / 半导体",
    "title": "Stock up on Seagate hard drives with $30 off the 8TB Barracuda HDD — Its lowest price at Best Buy since April",
    "url": "https://www.tomshardware.com/pc-components/hdds/stack-up-on-seagate-hard-drives-with-usd30-off-the-8tb-barracuda-hdd-its-lowest-price-at-best-buy-since-april",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T11:16:58+00:00",
    "summary": "Save $30 on an 8TB Seagate Barracuda HDD at Best Buy. The lowest price since April."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-coder-gets-doom-running-on-a-custom-cpu-designed-by-gpt-5-6-sol-game-viewport-is-overlaid-on-a-pulsing-schematic-of-the-cpu-in-turing-completes-sandbox-environment",
    "domain": "AI 算力 / 半导体",
    "title": "AI coder gets Doom running on a custom CPU designed by GPT-5.6 Sol — game viewport is overlaid on a pulsing schematic of the CPU in Turing Complete's sandbox environment",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-coder-gets-doom-running-on-a-custom-cpu-designed-by-gpt-5-6-sol-game-viewport-is-overlaid-on-a-pulsing-schematic-of-the-cpu-in-turing-completes-sandbox-environment",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T11:09:49+00:00",
    "summary": "An AI computing enthusiast has demonstrated Doom running on a custom CPU designed by GPT-5.6 Sol."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/motherboards/asus-rog-strix-b850-f-gaming-wifi-neo-motherboard-review",
    "domain": "AI 算力 / 半导体",
    "title": "Asus ROG Strix B850-F Gaming Wifi Neo motherboard review: Pricey proposition for B850, but packed with features",
    "url": "https://www.tomshardware.com/pc-components/motherboards/asus-rog-strix-b850-f-gaming-wifi-neo-motherboard-review",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T11:05:00+00:00",
    "summary": "Maxsun’s Terminator B850M Pro II is a decent budget option in the Micro ATX form factor, but only if you can find it for the $199.99 MSRP."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/one-gigabyte-of-ram-cost-as-much-as-a-house-back-in-1995-pcs-were-brutally-expensive-back-then-and-were-heading-back-in-that-direction",
    "domain": "AI 算力 / 半导体",
    "title": "One gigabyte of RAM cost as much as a house back in 1995 — $64,000 price tag resurfaced in 31-year-old press release, equivalent to $140,000 today",
    "url": "https://www.tomshardware.com/pc-components/ram/one-gigabyte-of-ram-cost-as-much-as-a-house-back-in-1995-pcs-were-brutally-expensive-back-then-and-were-heading-back-in-that-direction",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T11:00:00+00:00",
    "summary": "One gigabyte of RAM could cost you a house back in 1995 — PCs were brutally expensive were back then, and we're heading back in that direction"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-usd500-on-this-1440p-ready-gaming-pc-with-an-nvidia-geforce-rtx-5070-right-now-msi-codex-r2-pre-built-drops-below-usd1-500-with-a-20-core-intel-cpu-16gb-ddr5-and-a-1tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Save $500 on this 1440p-ready gaming PC with an Nvidia GeForce RTX 5070 right now — MSI Codex R2 pre-built drops below $1,500 with a 20-core Intel CPU, 16GB DDR5, and a 1TB SSD",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-usd500-on-this-1440p-ready-gaming-pc-with-an-nvidia-geforce-rtx-5070-right-now-msi-codex-r2-pre-built-drops-below-usd1-500-with-a-20-core-intel-cpu-16gb-ddr5-and-a-1tb-ssd",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T10:47:19+00:00",
    "summary": "This $1,499 MSI Codex R2 gaming PC comes with a $500 saving for a PC with an Nvidia GeForce RTX 5070, 16GB of DDR5 RAM, and a 1TB SSD."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/spacexai-will-deploy-standalone-nvidia-vera-cpus-for-groks-agentic-workloads",
    "domain": "AI 算力 / 半导体",
    "title": "SpaceXAI will deploy standalone Nvidia Vera CPUs for Grok's agentic workloads — will use optimized Vera Rubin NVL72 in space with Starmind satellite",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/spacexai-will-deploy-standalone-nvidia-vera-cpus-for-groks-agentic-workloads",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T10:41:54+00:00",
    "summary": "Nvidia claims the chip completes agentic, reinforcement learning, and data processing tasks up to 1.8 times faster than x86 processors."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/windows-veterans-vibe-coded-task-manager-now-also-runs-on-mac-and-linux-downloadable-app-is-the-result-of-a-107-page-spec-fed-to-claude-code",
    "domain": "AI 算力 / 半导体",
    "title": "Windows veteran's vibe-coded Task Manager now also runs on Mac and Linux — downloadable app is the result of a 107-page spec fed to Claude Code",
    "url": "https://www.tomshardware.com/software/windows/windows-veterans-vibe-coded-task-manager-now-also-runs-on-mac-and-linux-downloadable-app-is-the-result-of-a-107-page-spec-fed-to-claude-code",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T10:30:00+00:00",
    "summary": "Legendary Windows developer Dave Plummer has been busy finessing his revamped Task Manager, now dubbed TMOG."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/linux/decades-long-linux-ownership-dispute-effectively-dead-after-xinuos-appeal-rejected-us-court-of-appeals-halts-the-legal-wrangling-over-ibms-and-red-hats-use-of-project-monterey-unix-code",
    "domain": "AI 算力 / 半导体",
    "title": "Decades-long Linux ownership dispute effectively dead after Xinuos appeal rejected — US Court of Appeals halts the legal wrangling over IBM’s and Red Hat’s use of Project Monterey UNIX code",
    "url": "https://www.tomshardware.com/software/linux/decades-long-linux-ownership-dispute-effectively-dead-after-xinuos-appeal-rejected-us-court-of-appeals-halts-the-legal-wrangling-over-ibms-and-red-hats-use-of-project-monterey-unix-code",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T10:00:00+00:00",
    "summary": "A decades-long dispute over the ownership of Linux looks like it is over. Earlier this month the United States Court of Appeals for the Second Circuit rejected Xinuos’ continued claims that IBM and Re"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/aliexpress-allegedly-uses-your-browsers-audio-system-to-fingerprint-your-pc-hidden-code-runs-even-when-no-sound-is-playing",
    "domain": "AI 算力 / 半导体",
    "title": "AliExpress allegedly uses your browser's audio system to fingerprint your PC — hidden code runs even when no sound is playing",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/aliexpress-allegedly-uses-your-browsers-audio-system-to-fingerprint-your-pc-hidden-code-runs-even-when-no-sound-is-playing",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T09:44:53+00:00",
    "summary": "A developer's investigation into a Bluetooth headphone issue uncovered hidden Web Audio processing on AliExpress that allegedly fingerprints browsers and collects detailed device information."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-xeon-7-diamond-rapids-comes-with-up-to-256-p-cores-1-28-gb-of-last-level-cache-next-gen-18a-p-cpu-also-brings-avx-10-2-and-uses-ucie-s-instead-of-emib",
    "domain": "AI 算力 / 半导体",
    "title": "Hot Chips 2026: Intel Xeon 7 'Diamond Rapids' comes with up to 256 P-cores, 1.28 GB of last-level cache — next-gen 18A-P CPU also brings AVX 10.2 and uses UCIe-S instead of EMIB",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-xeon-7-diamond-rapids-comes-with-up-to-256-p-cores-1-28-gb-of-last-level-cache-next-gen-18a-p-cpu-also-brings-avx-10-2-and-uses-ucie-s-instead-of-emib",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T21:07:45+00:00",
    "summary": "Intel has pulled back the curtain on its next-gen Diamond Rapids Xeon CPUs, packing up to 256 P-cores and 1.28 TB of last-level cache."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/sk-hynix-says-hybrid-bonding-wont-be-ready-for-hbm4e-as-ai-memory-runs-into-a-775-micron-ceiling",
    "domain": "AI 算力 / 半导体",
    "title": "Hot Chips 2026: SK hynix pushes hybrid bonding to HBM5 as AI memory hits 775-micron ceiling — firm extends MR-MUF through Nvidia Rubin",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/sk-hynix-says-hybrid-bonding-wont-be-ready-for-hbm4e-as-ai-memory-runs-into-a-775-micron-ceiling",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T17:55:45+00:00",
    "summary": "The problem, per SK, is that HBM cubes are capped at a total thickness of 775 microns, the standard thickness of a 300mm logic wafer."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/ibms-first-dual-isa-core-natively-executes-arm-and-z-architecture-in-the-same-core-all-cores-run-at-5-7-ghz-base-frequency-next-gen-mainframe-ai-processor-is-built-on-2nm-node-with-11-cores",
    "domain": "AI 算力 / 半导体",
    "title": "Hot Chips 2026: IBM's first dual-ISA core natively executes ARM and z/Architecture in the same core; all cores run at 5.7 GHz base frequency — next-gen mainframe AI processor is built on 2nm node with",
    "url": "https://www.tomshardware.com/pc-components/cpus/ibms-first-dual-isa-core-natively-executes-arm-and-z-architecture-in-the-same-core-all-cores-run-at-5-7-ghz-base-frequency-next-gen-mainframe-ai-processor-is-built-on-2nm-node-with-11-cores",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T17:42:34+00:00",
    "summary": "IBM is vastly expanding softwarte support on its mainframes with its first dual-ISA CPU core that natively supports z/Architecture and ARM instructions."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/lgs-native-1-000-hz-1080p-gaming-monitor-has-a-matching-usd1-000-price-tag-preorders-open-for-the-25-inch-ultragear-25g590b",
    "domain": "AI 算力 / 半导体",
    "title": "LG's native 1,000 Hz 1080p gaming monitor has a matching $1,000 price tag — preorders open for the 25-inch UltraGear 25G590B",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/lgs-native-1-000-hz-1080p-gaming-monitor-has-a-matching-usd1-000-price-tag-preorders-open-for-the-25-inch-ultragear-25g590b",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T17:21:51+00:00",
    "summary": "The UltraGear 25G590B is the first 1,000 Hz gaming monitor with a native 1080p resolution"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/pc-cases/cooler-master-q300l-v3-microatx-case-review",
    "domain": "AI 算力 / 半导体",
    "title": "Cooler Master Q300L v3 MicroATX case review: Sub-$45 MSRP offers incredible value for MicroATX chassis with included fans",
    "url": "https://www.tomshardware.com/pc-components/pc-cases/cooler-master-q300l-v3-microatx-case-review",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T17:07:15+00:00",
    "summary": "Cooler Master’s Q300L V3 offers more airflow, bigger clearances, and a 20 Gbps USB-C for under $45"
  },
  {
    "id": "hn:49411178",
    "domain": "AI 算力 / 半导体",
    "title": "Etched Sohu vs. Nvidia: Transformer ASIC vs. GPU (2026)",
    "url": "https://www.spheron.network/blog/etched-ai-sohu-vs-nvidia-transformer-asic-inference/",
    "source": "rbanffy",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-08-23T18:27:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:49342314",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia discloses $21B stake in SpaceX",
    "url": "https://arstechnica.com/information-technology/2026/08/nvidia-discloses-21b-stake-in-spacex/",
    "source": "joozio",
    "platform": "hackernews",
    "points": 31,
    "published_at": "2026-08-18T07:02:04+00:00",
    "summary": ""
  },
  {
    "id": "hn:49322519",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia discloses $21B stake in SpaceX at end of second quarter",
    "url": "https://www.cnbc.com/2026/08/14/nvidia-discloses-21-billion-stake-in-spacex-at-end-of-second-quarter.html",
    "source": "johnbarron",
    "platform": "hackernews",
    "points": 47,
    "published_at": "2026-08-16T18:40:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:49282762",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia doubles RTX PRO 6000 Blackwell's MSRP to a staggering $16,000",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-doubles-rtx-pro-6000-blackwells-msrp-to-a-staggering-usd16-000-96gb-card-started-pre-orders-below-usd8-000-last-year",
    "source": "jacquesm",
    "platform": "hackernews",
    "points": 37,
    "published_at": "2026-08-13T07:28:54+00:00",
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
    "id": "hn:49184755",
    "domain": "大厂 AI 动态",
    "title": "Changes at Google DeepMind: Demis Hassabis from CEO to Chair, Jeff Dean departs",
    "url": "https://blog.google/company-news/inside-google/message-ceo/next-chapter-ai-momentum/",
    "source": "colesantiago",
    "platform": "hackernews",
    "points": 867,
    "published_at": "2026-08-05T16:05:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:49111237",
    "domain": "大厂 AI 动态",
    "title": "Gemini Robotics 2 brings whole body intelligence to robots",
    "url": "https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/",
    "source": "ai2027",
    "platform": "hackernews",
    "points": 620,
    "published_at": "2026-07-30T15:15:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:49220126",
    "domain": "大厂 AI 动态",
    "title": "DeepMind's WeatherNext model achieves breakthrough forecasting cyclones",
    "url": "https://deepmind.google/blog/weathernext-ai-model-achieves-breakthrough-in-forecasting-cyclones/",
    "source": "bhavansig",
    "platform": "hackernews",
    "points": 449,
    "published_at": "2026-08-08T09:18:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:49096188",
    "domain": "大厂 AI 动态",
    "title": "Document-borne AI worms can self-propagate through Copilot for Word",
    "url": "https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/",
    "source": "Canopy9560",
    "platform": "hackernews",
    "points": 384,
    "published_at": "2026-07-29T11:44:33+00:00",
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
    "id": "hn:49184757",
    "domain": "大厂 AI 动态",
    "title": "Demis Hassabis is moving from CEO to Chairman at Google DeepMind",
    "url": "https://www.axios.com/2026/08/05/google-deepmind-demis-hassabis-ai",
    "source": "ot",
    "platform": "hackernews",
    "points": 371,
    "published_at": "2026-08-05T16:05:37+00:00",
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
    "id": "hn:49067285",
    "domain": "大厂 AI 动态",
    "title": "Why I Left Google DeepMind",
    "url": "https://www.lesswrong.com/posts/iKm2FhpWkuuBojm82/why-i-left-google-deepmind",
    "source": "eatitraw",
    "platform": "hackernews",
    "points": 200,
    "published_at": "2026-07-27T09:56:37+00:00",
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
    "id": "hn:49198583",
    "domain": "大厂 AI 动态",
    "title": "Show HN: The Channels SDK – Bring Any Agent to Any Channel (Slack, MS Teams)",
    "url": "https://github.com/CopilotKit/channels-sdk",
    "source": "davidmckayv",
    "platform": "hackernews",
    "points": 121,
    "published_at": "2026-08-06T16:05:51+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/984753/garmin-fenix-9-smartwatch-launch",
    "domain": "大厂 AI 动态",
    "title": "Garmin’s new Fenix 9 adds brighter screens and smoother map panning",
    "url": "https://www.theverge.com/gadgets/984753/garmin-fenix-9-smartwatch-launch",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T22:20:17+00:00",
    "summary": "Garmin just took the wraps off its new line of rugged Fenix 9 smartwatches, with the base model featuring an OLED display with a brightness of up to 3,000 nits, making it twice as bright as its predec"
  },
  {
    "id": "rss:https://www.theverge.com/policy/984723/trump-h1b-fee-asylum-legal-immigration",
    "domain": "大厂 AI 动态",
    "title": "Trump is upping the price of Big Tech’s favorite visa",
    "url": "https://www.theverge.com/policy/984723/trump-h1b-fee-asylum-legal-immigration",
    "source": "Gaby Del Valle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T21:45:00+00:00",
    "summary": "In the span of a few hours on Monday, the Department of Homeland Security announced that it would be implementing a fee of over $103,000 on H-1B visas, and news broke that the State Department plans o"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/984677/inscryption-humble-daniel-mullins-pony-island-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "At just $8, you owe it to yourself to grab Inscryption",
    "url": "https://www.theverge.com/gadgets/984677/inscryption-humble-daniel-mullins-pony-island-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T20:38:37+00:00",
    "summary": "If you watched the Gamescom 2026 announcements, you might have caught a trailer for the bizarre, frenetic Pony Island 2: Panda Circus, a game from Daniel Mullins. In case you haven’t heard of him, get"
  },
  {
    "id": "rss:https://www.theverge.com/games/984680/the-witcher-3-wild-hunt-remastered-launch-date-trailer",
    "domain": "大厂 AI 动态",
    "title": "The Witcher 3 is getting a remaster",
    "url": "https://www.theverge.com/games/984680/the-witcher-3-wild-hunt-remastered-launch-date-trailer",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T20:24:24+00:00",
    "summary": "CD Projekt Red is remastering The Witcher 3: Wild Hunt, the hit RPG that first launched in 2015, and the updated game will be available starting September 29th. The Witcher 3: Wild Hunt - Remastered w"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/984485/dreame-rocket-car-shut-down",
    "domain": "大厂 AI 动态",
    "title": "Dreame’s dream of a rocket-powered car is dead",
    "url": "https://www.theverge.com/transportation/984485/dreame-rocket-car-shut-down",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T18:52:53+00:00",
    "summary": "Dreame, the Chinese vacuum company that aspires to be a global technology giant, is reportedly shutting down its automotive project after funding from the government dried up. According to CarNewsChin"
  },
  {
    "id": "rss:https://www.theverge.com/games/984530/microsoft-xbox-25th-anniversary-accessories",
    "domain": "大厂 AI 动态",
    "title": "Take a look at Microsoft&#8217;s new 25th anniversary Halo accessories",
    "url": "https://www.theverge.com/games/984530/microsoft-xbox-25th-anniversary-accessories",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T18:16:29+00:00",
    "summary": "The new Designed for Xbox 25th Anniversary collection features a handful of limited edition gadgets available for pre-order today. Paying homage to the Halo special edition of the original Xbox, almos"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/984414/bose-soundlink-micro-seagate-game-drive-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Bose’s smallest Bluetooth speaker is a great deal at 35 percent off",
    "url": "https://www.theverge.com/gadgets/984414/bose-soundlink-micro-seagate-game-drive-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T17:39:20+00:00",
    "summary": "Bose may be best known for its QuietComfort headphones, but the brand’s Bluetooth speakers have earned a great reputation for featuring great sound and build quality. The compact Bose SoundLink Micro "
  },
  {
    "id": "rss:https://www.theverge.com/games/983891/gamescom-opening-night-live-2026-geoff-keighley",
    "domain": "大厂 AI 动态",
    "title": "Gamescom Opening Night Live 2026: The biggest announcements and trailers",
    "url": "https://www.theverge.com/games/983891/gamescom-opening-night-live-2026-geoff-keighley",
    "source": "Verge Staff",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T17:20:00+00:00",
    "summary": "The Geoff Keighley-hosted Opening Night Live event at Gamescom just wrapped up. Arguably the biggest announcement was the closer: a remastered version of The Witcher 3: Wild Hunt from CD Projekt Red t"
  },
  {
    "id": "rss:https://www.theverge.com/tech/984463/instagram-first-draft-edit-reels",
    "domain": "大厂 AI 动态",
    "title": "Instagram’s ‘First Draft’ trims your Reels clips for you",
    "url": "https://www.theverge.com/tech/984463/instagram-first-draft-edit-reels",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T17:12:31+00:00",
    "summary": "Instagram is launching a new Reels-editing feature that automatically trims your video clips to focus on the highlights. The feature, called First Draft, is rolling out to Instagram's iPhone app and p"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/984430/nothing-os-5-launch-android-17",
    "domain": "大厂 AI 动态",
    "title": "Nothing OS 5.0 brings a new Glyph Interface app and a more customizable homescreen",
    "url": "https://www.theverge.com/gadgets/984430/nothing-os-5-launch-android-17",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T16:58:53+00:00",
    "summary": "With the new design of Nothing OS 5.0, app icons and widgets can use adaptive color to get color tints pulled from your wallpaper, which update whenever your wallpaper changes. Alongside Android's bui"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/25/indias-ringg-gets-backing-from-peak-xv-as-it-pushes-voice-ai-past-the-phone-call/",
    "domain": "大厂 AI 动态",
    "title": "India’s Ringg gets backing from Peak XV as it pushes voice AI past the phone call",
    "url": "https://techcrunch.com/2026/08/25/indias-ringg-gets-backing-from-peak-xv-as-it-pushes-voice-ai-past-the-phone-call/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T03:30:00+00:00",
    "summary": "Ringg has raised $10 million from Peak XV as a part of its Series A extension."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/25/robotics-startup-generalist-reaches-3b-valuation-sources-say/",
    "domain": "大厂 AI 动态",
    "title": "Robotics startup Generalist reaches $3B valuation, sources say",
    "url": "https://techcrunch.com/2026/08/25/robotics-startup-generalist-reaches-3b-valuation-sources-say/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T00:40:59+00:00",
    "summary": "The $200 million extension comes just months after the physical AI startup reached a $2 billion valuation."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/25/openai-loses-a-top-data-center-exec-as-stream-of-high-profile-departures-continues/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI loses a top data center exec, as stream of high-profile departures continues",
    "url": "https://techcrunch.com/2026/08/25/openai-loses-a-top-data-center-exec-as-stream-of-high-profile-departures-continues/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T00:06:20+00:00",
    "summary": "Before Malone left, OpenAI had already reshuffled its infrastructure org, shifting his reporting line away from President Greg Brockman and putting Vice President Sachin Katti in charge of the group."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/25/x-sends-cease-and-desist-to-open-source-project-nitter-over-alleged-scraping/",
    "domain": "大厂 AI 动态",
    "title": "X sends cease-and-desist to open source project Nitter over alleged scraping",
    "url": "https://techcrunch.com/2026/08/25/x-sends-cease-and-desist-to-open-source-project-nitter-over-alleged-scraping/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T20:44:12+00:00",
    "summary": "X has sent cease-and-desist letters to Nitter, the open source project behind privacy-friendly X front ends, demanding its instances and code repository be taken down over alleged scraping."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/25/instagrams-first-draft-feature-aims-to-make-editing-reels-less-tedious/",
    "domain": "大厂 AI 动态",
    "title": "Instagram’s ‘First Draft’ feature aims to make editing Reels less tedious",
    "url": "https://techcrunch.com/2026/08/25/instagrams-first-draft-feature-aims-to-make-editing-reels-less-tedious/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T19:22:52+00:00",
    "summary": "Instagram says the process can produce a first pass in under 10 seconds, potentially saving creators significant editing time while making video creation more approachable for people who don't have mu"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/25/stability-ai-maker-of-image-generator-stable-diffusion-raises-76-million-in-fresh-funding/",
    "domain": "大厂 AI 动态",
    "title": "Stability AI, maker of image generator Stable Diffusion, raises $76 million in fresh funding",
    "url": "https://techcrunch.com/2026/08/25/stability-ai-maker-of-image-generator-stable-diffusion-raises-76-million-in-fresh-funding/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T19:03:47+00:00",
    "summary": "The company's new fundraising total now stands at $232 million."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/25/spacex-will-build-a-second-100b-starbase-spaceport-in-louisiana/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX will build a second, $100B ‘Starbase’ spaceport in Louisiana",
    "url": "https://techcrunch.com/2026/08/25/spacex-will-build-a-second-100b-starbase-spaceport-in-louisiana/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T18:26:55+00:00",
    "summary": "The company says it will start construction in 2027 and that a Starship rocket could take flight as soon as 2029."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/25/your-vote-matters-decide-which-audience-choice-sessions-will-make-it-to-techcrunch-founder-summit/",
    "domain": "大厂 AI 动态",
    "title": "Your vote matters! Decide which Audience Choice sessions will make it to TechCrunch Founder Summit",
    "url": "https://techcrunch.com/2026/08/25/your-vote-matters-decide-which-audience-choice-sessions-will-make-it-to-techcrunch-founder-summit/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T18:22:50+00:00",
    "summary": "Each year, we get a huge influx of applicants to speak at TechCrunch’s events, and this year’s Founder Summit in Boston on November 4 will be no different!"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/25/tonight-marks-your-last-chance-to-save-up-to-300-on-a-techcrunch-disrupt-2026-pass/",
    "domain": "大厂 AI 动态",
    "title": "Tonight marks your last chance to save up to $300 on a TechCrunch Disrupt 2026 pass",
    "url": "https://techcrunch.com/2026/08/25/tonight-marks-your-last-chance-to-save-up-to-300-on-a-techcrunch-disrupt-2026-pass/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T18:01:30+00:00",
    "summary": "If you’ve been circling around Disrupt, then now’s the best time to lock in your pass and start getting ready to join the rest of the startup community gathering in San Francisco from October 13-15 at"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/25/claude-cowork-finally-remembers-what-you-told-the-app-in-chat/",
    "domain": "大厂 AI 动态",
    "title": "Claude Cowork finally remembers what you told the app in chat",
    "url": "https://techcrunch.com/2026/08/25/claude-cowork-finally-remembers-what-you-told-the-app-in-chat/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T17:50:33+00:00",
    "summary": "Anthropic is giving Claude a shared memory across chat and Cowork, so users no longer have to repeatedly brief the AI on projects, preferences, and other context."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/25/waymo-robotaxis-are-headed-to-munich/",
    "domain": "大厂 AI 动态",
    "title": "Waymo robotaxis are headed to Munich",
    "url": "https://techcrunch.com/2026/08/25/waymo-robotaxis-are-headed-to-munich/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T17:32:03+00:00",
    "summary": "Germany's autonomous vehicle regulations have made it a hotspot for autonomous vehicle testing and eventual commercial robotaxi deployment."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/25/life360-expands-pet-tracking-with-new-8-scannable-tags-and-zoomie-alerts/",
    "domain": "大厂 AI 动态",
    "title": "Life360 expands pet tracking with new $8 scannable tags and zoomie alerts",
    "url": "https://techcrunch.com/2026/08/25/life360-expands-pet-tracking-with-new-8-scannable-tags-and-zoomie-alerts/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T16:35:00+00:00",
    "summary": "Life360’s new $7.99 scannable pet tags alert families when a lost pet is found and share its last known location, while new care-tracking features help households keep tabs on feeding, walks, medicati"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/25/that-fake-grand-theft-auto-vi-demo-is-actually-just-malware/",
    "domain": "大厂 AI 动态",
    "title": "That fake Grand Theft Auto VI demo is actually just malware",
    "url": "https://techcrunch.com/2026/08/25/that-fake-grand-theft-auto-vi-demo-is-actually-just-malware/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T15:48:38+00:00",
    "summary": "Grand Theft Auto fans, eager for news about one of the most anticipated video games of all time, appear especially vulnerable to this new cyberattack."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/25/pacific-fusion-next-fusion-machine-could-clear-key-hurdle-to-commercial-power/",
    "domain": "大厂 AI 动态",
    "title": "Pacific Fusion’s next fusion machine could clear a key hurdle to commercial power",
    "url": "https://techcrunch.com/2026/08/25/pacific-fusion-next-fusion-machine-could-clear-key-hurdle-to-commercial-power/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T15:30:00+00:00",
    "summary": "Fusion startup Pacific Fusion broke ground on a demonstration facility in New Mexico that it says will generate enough energy to power itself."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/25/gamma-acquires-accel-backed-design-startup-lica/",
    "domain": "大厂 AI 动态",
    "title": "Gamma acquires Accel-backed design startup Lica",
    "url": "https://techcrunch.com/2026/08/25/gamma-acquires-accel-backed-design-startup-lica/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T15:00:00+00:00",
    "summary": "Lica co-founders are going to work on Gamma's new research team."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/25/apple-rescues-hide-my-email-feature-from-the-privacy-scrap-heap/",
    "domain": "大厂 AI 动态",
    "title": "Apple rescues Hide My Email feature from the privacy scrap heap",
    "url": "https://techcrunch.com/2026/08/25/apple-rescues-hide-my-email-feature-from-the-privacy-scrap-heap/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T14:46:32+00:00",
    "summary": "Apple says it will no longer ditch using its icloud.com domain for hiding people's email addresses."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/25/openais-jalapeno-chip-is-built-for-fast-inference-at-scale-benchmarks-show/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI’s Jalapeño chip is built for fast inference at scale, benchmarks show",
    "url": "https://techcrunch.com/2026/08/25/openais-jalapeno-chip-is-built-for-fast-inference-at-scale-benchmarks-show/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T14:22:04+00:00",
    "summary": "Tested on SemiAnalysis’ InferenceX benchmark, Jalapeño registered both more tokens per user and more throughput per kilowatt than the currently available state-of-the art."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/25/apple-debuts-its-most-powerful-chip-ever-in-m5-ultra-and-m6/",
    "domain": "大厂 AI 动态",
    "title": "Apple debuts its ‘most powerful chip ever’ in M5 Ultra and M6",
    "url": "https://techcrunch.com/2026/08/25/apple-debuts-its-most-powerful-chip-ever-in-m5-ultra-and-m6/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T14:10:36+00:00",
    "summary": "Apple unveils these new processors alongside an updated Mac Mini and Mac Studio."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/25/self-driving-truck-startup-gatik-raises-200m-following-pepsico-deal/",
    "domain": "大厂 AI 动态",
    "title": "Self-driving truck startup Gatik raises $200M following PepsiCo deal",
    "url": "https://techcrunch.com/2026/08/25/self-driving-truck-startup-gatik-raises-200m-following-pepsico-deal/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T14:00:00+00:00",
    "summary": "The funding, Gatik's largest so far, was led by Qatar Investment Authority and Koch Disruptive Technologies."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/25/apples-latest-mac-mini-runs-on-a-new-m6-chip-and-starts-at-899/",
    "domain": "大厂 AI 动态",
    "title": "Apple’s latest Mac Mini runs on a new M6 chip, and starts at $899",
    "url": "https://techcrunch.com/2026/08/25/apples-latest-mac-mini-runs-on-a-new-m6-chip-and-starts-at-899/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T13:55:06+00:00",
    "summary": "The base model of the Mac Mini comes with 256GB of storage, 16GB of RAM, and costs $899."
  },
  {
    "id": "rss:https://stratechery.com/2026/netflix-to-sell-streaming-services-streamers-as-aggregators-revisiting-roku/",
    "domain": "大厂 AI 动态",
    "title": "Netflix to Sell Streaming Services?, Streamers as Aggregators, Revisiting Roku",
    "url": "https://stratechery.com/2026/netflix-to-sell-streaming-services-streamers-as-aggregators-revisiting-roku/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T10:00:00+00:00",
    "summary": "Netflix is considering selling other streaming services, and I think it's a good idea; it's also a let-down for Netflix's original goals and potential pivots."
  },
  {
    "id": "rss:https://stratechery.com/2026/autonomy-and-innovation/",
    "domain": "大厂 AI 动态",
    "title": "Autonomy and Innovation",
    "url": "https://stratechery.com/2026/autonomy-and-innovation/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T10:00:00+00:00",
    "summary": "Incentives favor offense when it comes to agentic cybersecurity; it's the same dynamic that will limit incumbents and fuel startups in the long run."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/08/the-worlds-busiest-spaceport-is-about-to-get-a-lot-quieter-at-least-for-now/",
    "domain": "大厂 AI 动态",
    "title": "The world's busiest spaceport is about to get a lot quieter, at least for now",
    "url": "https://arstechnica.com/space/2026/08/the-worlds-busiest-spaceport-is-about-to-get-a-lot-quieter-at-least-for-now/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T22:21:06+00:00",
    "summary": "SpaceX aims to launch Starship from Florida by the end of the year. 2027 seems more likely."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/08/world-humanoid-robot-games-show-runners-breaking-records-bursting-into-flames/",
    "domain": "大厂 AI 动态",
    "title": "World humanoid robot games show runners breaking records, bursting into flames",
    "url": "https://arstechnica.com/ai/2026/08/world-humanoid-robot-games-show-runners-breaking-records-bursting-into-flames/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T20:59:03+00:00",
    "summary": "Record-breaking robot races are less substantial than household chore challenges."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/08/how-chemistry-can-keep-glow-in-the-dark-pigments-from-fading/",
    "domain": "大厂 AI 动态",
    "title": "Preserving glow-in-the-dark art and fashion for future generations",
    "url": "https://arstechnica.com/science/2026/08/how-chemistry-can-keep-glow-in-the-dark-pigments-from-fading/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T18:59:12+00:00",
    "summary": "Understanding unique photochemistry of such materials will help in conservation, storage, and exhibition."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/08/google-begins-rolling-out-anti-motion-sickness-feature-on-android-17/",
    "domain": "大厂 AI 动态",
    "title": "Google's anti-nausea Motion Assist dots finally rolling out on Android",
    "url": "https://arstechnica.com/gadgets/2026/08/google-begins-rolling-out-anti-motion-sickness-feature-on-android-17/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T18:32:30+00:00",
    "summary": "It's currently only appearing on Pixels running Android 17."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/08/two-unvaccinated-people-die-from-measles-in-pennsylvania-officials-confirm/",
    "domain": "大厂 AI 动态",
    "title": "Two unvaccinated people die from measles in Pennsylvania, officials confirm",
    "url": "https://arstechnica.com/health/2026/08/two-unvaccinated-people-die-from-measles-in-pennsylvania-officials-confirm/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T17:39:38+00:00",
    "summary": "\"[P]eople are not familiar with this disease and don’t fully understand the potential severity.\""
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/08/spacex-intends-to-invest-up-to-100-billion-in-massive-louisiana-spaceport/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX intends to invest up to $100 billion in massive Louisiana spaceport",
    "url": "https://arstechnica.com/space/2026/08/spacex-intends-to-invest-up-to-100-billion-in-massive-louisiana-spaceport/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T17:26:15+00:00",
    "summary": "\"This will be a project like no other.\""
  },
  {
    "id": "hn:49166182",
    "domain": "股票",
    "title": "Bending Spoons makes first post-IPO acquisition with $1.3B Airtable deal",
    "url": "https://live.euronext.com/en/financial-news/bending-spoons-makes-first-post-ipo-acquisition-13-billion-airtable-deal",
    "source": "riffraff",
    "platform": "hackernews",
    "points": 118,
    "published_at": "2026-08-04T09:27:47+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3780130",
    "domain": "股票",
    "title": "37万亿险资换锚：一条100%重磅监管红线落地，能把多少资金推向红利？",
    "url": "https://wallstreetcn.com/premium/articles/3780130?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T03:51:06+00:00",
    "summary": "《保险公司资产负债管理办法》正式落地，最受市场关注的变化，是人身险净投资收益覆盖率被纳入硬性监管指标，并要求不低于100%。在长端利率下行、存量高收益资产持续到期的背景下，股息红利作为稳定净投资收益来源，其监管价值明显上升。按照不同假设测算，未来数年险资对高股息资产的潜在增配规模可能达到数千亿元至万亿元级，这会不会成为红利资产下一阶段最重要的长期买方力量？"
  },
  {
    "id": "wscn:3780314",
    "domain": "股票",
    "title": "地缘冲突+极端天气双重冲击，全球粮食危机警报拉响！",
    "url": "https://wallstreetcn.com/articles/3780314",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T03:17:14+00:00",
    "summary": "战争、极端天气双重冲击正将全球粮食推向危机边缘。汇丰最新警告：2026/27年度全球谷物供需缺口将是2006年以来最大；超强厄尔尼诺概率超90%，8月谷物价格同比暴涨30%。此外，乌克兰出口近乎停滞，芝加哥小麦期货飙至两年高位——一场系统性粮食危机正在成形。"
  },
  {
    "id": "wscn:3780306",
    "domain": "股票",
    "title": "高盛也相信：为了救日元，日本9月将加息",
    "url": "https://wallstreetcn.com/articles/3780306",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T03:11:09+00:00",
    "summary": "高盛将日本央行加息预期大幅前移至9月，此前预期为2027年1月，终端利率预测同步上调至1.75%。核心逻辑在于：中长期通胀预期已逼近2%，日元贬值压力取代工资数据成为最紧迫变量——美元兑日元若突破160关口，按兵不动将被市场解读为央行默许汇率走弱，反而推高通胀预期。"
  },
  {
    "id": "wscn:3780298",
    "domain": "股票",
    "title": "美国保险业爆出大雷：210亿美金遭暗箱操作，华尔街大鳄的体育帝国摇摇欲坠",
    "url": "https://wallstreetcn.com/articles/3780298",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T03:06:17+00:00",
    "summary": "千亿金融帝国古根海姆（Guggenheim）CEO马克·沃尔特正面临FBI的严厉调查。高达210亿美元的保险资金涉嫌违规“左手倒右手”，美国保险业背后高达1.1万亿美元的“私募吸血”模式正面临崩盘危机。"
  },
  {
    "id": "wscn:3780296",
    "domain": "股票",
    "title": "IMF总裁警告财政风险上升，呼吁各国推进整合、央行坚守抗通胀立场",
    "url": "https://wallstreetcn.com/articles/3780296",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T03:04:34+00:00",
    "summary": "IMF总裁Georgieva警告全球财政与货币压力同步累积，敦促各国制定可信债务整合计划，要求央行坚守价格稳定职责。她指出，中东能源冲击与AI需求增长形成拉锯，债券收益率攀升和通胀降温迟滞反映高度不确定性，强调\"没有理由自满\"。"
  },
  {
    "id": "wscn:3780307",
    "domain": "股票",
    "title": "超级厄尔尼诺+俄乌/美伊战事=未来半年的农产品涨价周期",
    "url": "https://wallstreetcn.com/articles/3780307",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T02:42:56+00:00",
    "summary": "花旗首席分析师团队最新报告维持谷物及油籽看涨立场，全面上调玉米、小麦、大豆价格目标。报告指出，超级厄尔尼诺概率超90%、黑海航运中断、生物燃料需求扩张及化肥能源成本高企四重因素共振，将在未来6至12个月持续收紧全球农业供需。"
  },
  {
    "id": "wscn:3780308",
    "domain": "股票",
    "title": "知名风投a16z：过去75年的“创新方法论”，AI已经彻底改写",
    "url": "https://wallstreetcn.com/articles/3780308",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T02:33:16+00:00",
    "summary": "a16z合伙人认为，AI正在改写创新的底层经济逻辑：从工程约束转向资本约束，20人团队如今能有效部署10亿美元。这一判断直接影响对初创公司vs大厂竞争格局、风险投资逻辑乃至AI能力边界的判断。三人同时坦承，面对百亿美元规模的模型训练，没人真正知道会产生什么，“这是人类从未创造过的数字产物”。"
  },
  {
    "id": "wscn:3780304",
    "domain": "股票",
    "title": "被低估的金矿板块？金价飙升破4500美元后，金矿采选行业能否迎来春天",
    "url": "https://wallstreetcn.com/premium/articles/3780304?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T02:32:31+00:00",
    "summary": "中国金矿采选行业正处于资源接续、产能扩张与估值修复的三重窗口：一方面，全球金矿产金增速显著落后于需求，2025年矿产金仅3300吨，而投资与央行购金合计占比已升至60.8%；另一方面，中国金矿企业借助深部开采技术突破、全球化并购与在建工程放量，正在将金价上行转化为可量化的盈利弹性。"
  },
  {
    "id": "wscn:3780305",
    "domain": "股票",
    "title": "大摩启动英伟达信用评级：财务实力转化为AI融资工具，负债规模或达2000亿美元",
    "url": "https://wallstreetcn.com/articles/3780305",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T02:30:31+00:00",
    "summary": "英伟达正将5000亿美元量级的AI基础设施融资野心，悄然转化为其资产负债表上的隐性风险敞口。摩根士丹利最新报告揭示，若将租赁担保、剩余价值支持及收入分成等或有义务悉数纳入，英伟达全口径信用敞口至2028年底或触及2000亿美元——其中高达1700亿美元游离于表外，透明度缺口与尾部风险仍存。"
  },
  {
    "id": "wscn:3780309",
    "domain": "股票",
    "title": "A股三大股指早盘震荡上涨，有色金属、券商活跃，光模块调整，恒指、恒科指均涨超1%，生物医药爆发",
    "url": "https://wallstreetcn.com/articles/3780309",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T02:30:05+00:00",
    "summary": "早盘有色板块震荡反弹，铜方向领涨，金诚信涨停，江西铜业触及涨停，云南铜业、西部矿业、北方铜业、铜陵有色、洛阳钼业涨幅靠前。港股恒生生物科技指数涨超3%，信达生物涨超12%，康方生物涨超8%。"
  },
  {
    "id": "wscn:3780311",
    "domain": "股票",
    "title": "库克清空弹夹！2nm，韬定律，最强AI电脑",
    "url": "https://wallstreetcn.com/articles/3780311",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T02:21:06+00:00",
    "summary": "库克退休前火力全开！苹果一口气发布首款2nm芯片M6与史上最强M系芯片M5 Ultra——前者AI性能暴涨4倍，Mac mini悄然向\"桌面Agent服务器\"转型；后者四Die堆叠、512GB统一内存、1.2TB/s带宽，直接把桌面机干成了AI机房。价格也跟着算力一路飞涨，512GB版Mac Studio更已排货至10月底。"
  },
  {
    "id": "wscn:3780312",
    "domain": "股票",
    "title": "BOSS直聘二季度MAU首次突破7000万，AI服务向招聘全流程延伸",
    "url": "https://wallstreetcn.com/articles/3780312",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T02:20:08+00:00",
    "summary": "8月25日，BOSS直聘发布2026年二季度业绩。公司实现营收23.99亿元，同比增长14.1%，增..."
  },
  {
    "id": "wscn:3780315",
    "domain": "股票",
    "title": "上半年归母净利增长40.21%，这家地方实力券商进入“利润爬坡期”，",
    "url": "https://wallstreetcn.com/articles/3780315",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T01:14:05+00:00",
    "summary": "浙商证券自营投资收益大幅增加"
  },
  {
    "id": "wscn:3780301",
    "domain": "股票",
    "title": "一石激起千层浪！短短9个月，OpenAI自研ASIC芯片已超越英伟达Blackwell？",
    "url": "https://wallstreetcn.com/articles/3780301",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T01:10:22+00:00",
    "summary": "OpenAI首颗自研推理芯片Jalapeño在能效、吞吐量等核心指标上实测超越英伟达Blackwell，且开发周期远低于行业均值。更深远的意义在于：AI工具深度介入芯片设计本身，形成\"AI造芯片、芯片跑AI\"的正向飞轮，CUDA的软件护城河正面临结构性挑战。"
  },
  {
    "id": "wscn:3780302",
    "domain": "股票",
    "title": "“AI存储税”！Trendforce称：2027年，存储将占主要云厂资本开支的68%",
    "url": "https://wallstreetcn.com/articles/3780302",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T00:31:40+00:00",
    "summary": "TrendForce最新报告显示，受存储合同价格大幅上涨驱动，DRAM与NAND Flash在主要云服务商资本开支中的占比将从2026年的47%跃升至2027年的68%。服务器DRAM价格2026年预计累计涨幅约270%，HBM 2027年仍可能再涨70%至140%。"
  },
  {
    "id": "wscn:3780300",
    "domain": "股票",
    "title": "“国会山股神”首度建仓“AI能源”，Bloom应声走高",
    "url": "https://wallstreetcn.com/articles/3780300",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T00:30:33+00:00",
    "summary": "美国\"国会山股神\"佩洛西家族最新交易曝光：斥资数百万美元首度建仓AI能源股Bloom Energy，并同步加仓英特尔。受此提振，Bloom Energy单日涨逾4%。消息迅速引爆跟单热潮，逾两万名投资者闻风而动，押注规模达4400万美元，国会议员炒股合规争议再度升温。"
  },
  {
    "id": "wscn:3780290",
    "domain": "股票",
    "title": "停火谈判重大进展！美伊传就霍尔木兹自由通航达成共识、伊朗与阿曼拟设临时安全通道，布油一度跌6%",
    "url": "https://wallstreetcn.com/articles/3780290",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T00:11:11+00:00",
    "summary": "据俄媒，巴基斯坦和伊朗的消息人士称，美伊已就停火协议条款达成共识，其中包括霍尔木兹海峡自由通航，双方预计未来几天公布相关消息，并根据此前由巴基斯坦斡旋达成的谅解备忘录，启动谈判及技术性会议。伊朗副外长称，伊朗告知谈判代表，若美国希望海峡重开，必须纠错并重回所作承诺。伊媒称，巴基斯坦陆军元帅最近访伊是为谈判创造空间，并向美转达伊方条件和立场。"
  },
  {
    "id": "wscn:3780225",
    "domain": "股票",
    "title": "AI债务的“次贷时刻”会来吗？真正危险的环节可能还没出现",
    "url": "https://wallstreetcn.com/premium/articles/3780225?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T00:10:06+00:00",
    "summary": "AI基础设施正从科技公司的资本开支，快速演变为资本市场共同参与的信用扩张。Hyperscaler今年资本开支已逼近7000亿美元，Private Credit、SPV和资产证券化加速进入算力产业。尽管债务增长迅速，但核心借款人质量、银行渗透率和居民财富效应仍与2008年前夕存在明显差距，即使未来发生出清，其系统性破坏力大概率也难企及次贷危机。真正需要追踪的是，算力金融化会否继续向银行体系和短期融资"
  },
  {
    "id": "wscn:3780297",
    "domain": "股票",
    "title": "持续“恐吓”美债空头！“贝森特看跌期权”开始生效？",
    "url": "https://wallstreetcn.com/articles/3780297",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T00:07:54+00:00",
    "summary": "美财长贝森特\"翻倍\"长期美债回购计划正在重塑利率市场：30年期互换利差收窄至2月新低，期权市场出现明显看涨倾斜，交易员不敢轻易做空长端。花旗策略师将其定义为\"贝森特看跌期权\"开始发挥作用，但Pimco警告结构性财政赤字问题短期无解，Druckenmiller更直言此举是“错误”。"
  },
  {
    "id": "wscn:3780295",
    "domain": "股票",
    "title": "油价大跌5%，为贝森特提供债券收益率喘息空间，但结构性压力未解",
    "url": "https://wallstreetcn.com/articles/3780295",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T23:21:33+00:00",
    "summary": "油价大跌逾5%，带动10年期美债收益率回落6个基点至4.64%，但整体仍在近五周区间内震荡，属技术性调整而非结构性下行。通胀高于目标、国债供给持续偏大及名义增长强劲，共同制约长端收益率下行空间，令财长贝森特期望的实质性重新定价难以实现。"
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
    "id": "hn:49397022",
    "domain": "股票",
    "title": "Ask HN: What is the evidence for a stock market bubble in AI?",
    "url": "https://news.ycombinator.com/item?id=49397022",
    "source": "roschdal",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-08-22T06:07:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:49396088",
    "domain": "股票",
    "title": "S&P 500 CEO median pay hits $17.3M, widening CEO-worker ratio to 312-to-1",
    "url": "https://finance.yahoo.com/markets/stocks/articles/p-500-ceo-median-pay-234900518.html",
    "source": "newsomix9xl",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-08-22T02:38:14+00:00",
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
    "id": "hn:49305685",
    "domain": "股票",
    "title": "Backtesting Congress members stock trades by the disclosure date",
    "url": "https://investingpaths.com/tools/congress",
    "source": "ProdRatSuperior",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-08-14T23:08:56+00:00",
    "summary": ""
  },
  {
    "id": "hn:49322233",
    "domain": "股票",
    "title": "AI is not just one bubble, strategist says – but a 'rolling sequence of bubbles'",
    "url": "https://fortune.com/2026/08/16/ai-bubble-sequence-saas-software-stocks-silver-prices-chipmakers/",
    "source": "pessimizer",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-08-16T18:05:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:49338121",
    "domain": "股票",
    "title": "US tech stock correction likely, warn ECB economists",
    "url": "https://www.ft.com/content/cb4b22ab-4183-4d19-be60-6d2fab86d86d",
    "source": "aanet",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-08-17T21:46:22+00:00",
    "summary": ""
  },
  {
    "id": "hn:49195657",
    "domain": "股票",
    "title": "The Investors Whose SpaceX Shares Vanished Before They Could Cash In",
    "url": "https://www.wsj.com/finance/stocks/spacex-ipo-spv-investors-2698a174",
    "source": "doener",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-08-06T12:19:44+00:00",
    "summary": ""
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
    "id": "rss:https://www.netinterest.co/p/apple-turnover",
    "domain": "股票",
    "title": "Apple Turnover",
    "url": "https://www.netinterest.co/p/apple-turnover",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-04-24T16:38:20+00:00",
    "summary": "How Tim Cook reshaped payments &#8211; and what he leaves behind"
  },
  {
    "id": "hn:49355142",
    "domain": "金融",
    "title": "Sticky wage norms and the real wage cost of unexpected inflation",
    "url": "https://bfi.uchicago.edu/wp-content/uploads/2026/08/BFI_WP_2026-108-1.pdf",
    "source": "jplusequalt",
    "platform": "hackernews",
    "points": 391,
    "published_at": "2026-08-19T00:53:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:49175192",
    "domain": "金融",
    "title": "Thanks FedEx, This Is Why We Keep Getting Phished (2024)",
    "url": "https://www.troyhunt.com/thanks-fedex-this-is-why-we-keep-getting-phished/",
    "source": "stymaar",
    "platform": "hackernews",
    "points": 338,
    "published_at": "2026-08-04T21:09:39+00:00",
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
    "id": "hn:49415187",
    "domain": "金融",
    "title": "Nearly 3M Teslas recalled in China over hidden door handles",
    "url": "https://www.bbc.com/news/articles/c4g6ggdg030o",
    "source": "chicken-stew",
    "platform": "hackernews",
    "points": 119,
    "published_at": "2026-08-24T04:27:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:49200390",
    "domain": "金融",
    "title": "Federal Communications Commission scraps limit on broadcast TV ownership",
    "url": "https://www.nbcnews.com/business/media/federal-communications-commission-scraps-limit-broadcast-tv-ownership-rcna587641",
    "source": "pseudolus",
    "platform": "hackernews",
    "points": 179,
    "published_at": "2026-08-06T18:22:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:49082695",
    "domain": "金融",
    "title": "Mondragon Corporation – a federation of co-operatives",
    "url": "https://en.wikipedia.org/wiki/Mondragon_Corporation",
    "source": "brnt",
    "platform": "hackernews",
    "points": 174,
    "published_at": "2026-07-28T12:19:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:49122994",
    "domain": "金融",
    "title": "Situational Awareness down 67% in July in AI stock rout",
    "url": "https://www.wsj.com/finance/investing/situational-awareness-down-67-in-july-in-ai-stock-rout-cd19901f",
    "source": "pondsider",
    "platform": "hackernews",
    "points": 157,
    "published_at": "2026-07-31T13:37:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:49432102",
    "domain": "金融",
    "title": "Nostr vs. Fediverse vs. Bluesky: A Comparison of Decentralized Social Protocols",
    "url": "https://soapbox.pub/blog/comparing-protocols",
    "source": "Bluestein",
    "platform": "hackernews",
    "points": 54,
    "published_at": "2026-08-25T11:27:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:49439296",
    "domain": "金融",
    "title": "A brief history of federal lift ticket regulation",
    "url": "https://zakpodmore.substack.com/p/a-brief-history-of-federal-lift-ticket",
    "source": "CGMthrowaway",
    "platform": "hackernews",
    "points": 49,
    "published_at": "2026-08-25T19:25:43+00:00",
    "summary": ""
  },
  {
    "id": "hn:49118696",
    "domain": "金融",
    "title": "The bond market isn’t buying what Fed Chair Warsh is selling",
    "url": "https://www.reuters.com/commentary/reuters-open-interest/bond-market-isnt-buying-what-fed-chair-warsh-is-selling-2026-07-30/",
    "source": "kaycebasques",
    "platform": "hackernews",
    "points": 139,
    "published_at": "2026-07-31T03:32:21+00:00",
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
    "id": "rss:https://arxiv.org/abs/2608.21498",
    "domain": "金融",
    "title": "Beyond Lognormal Sums: A Four-Moment Probability Framework for Basket and Spread Option Pricing",
    "url": "https://arxiv.org/abs/2608.21498",
    "source": "Dongdong Hu, Hasanjan Sayit, Steve Tchoneteck, Frederi Viens",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T04:00:00+00:00",
    "summary": "arXiv:2608.21498v1 Announce Type: new Abstract: Basket options are difficult to value under correlated lognormal dynamics because weighted sums and differences of lognormal variables have no tractable"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.21506",
    "domain": "金融",
    "title": "What Quantitative Risk Modellers Can Learn from Durkheim's Study of Suicide",
    "url": "https://arxiv.org/abs/2608.21506",
    "source": "Mahmood Alaghmandan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T04:00:00+00:00",
    "summary": "arXiv:2608.21506v1 Announce Type: new Abstract: Emile Durkheim's Suicide: A Study in Sociology (1897) predates much of the statistical machinery that quantitative modellers now take for granted. Yet, "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.21691",
    "domain": "金融",
    "title": "Contextual Visual Distinctiveness in Online Product Search",
    "url": "https://arxiv.org/abs/2608.21691",
    "source": "Felicia Nguyen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T04:00:00+00:00",
    "summary": "arXiv:2608.21691v1 Announce Type: new Abstract: In online product search, returned alternatives often look alike. We investigate when a product's visual separation from its closest look-alike in a ret"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.21843",
    "domain": "金融",
    "title": "Debt relief and remittances can offset foreign aid cuts for most countries, but some remain locked out",
    "url": "https://arxiv.org/abs/2608.21843",
    "source": "Andrea Vismara, Rafael Prieto-Curiel, Rosie Hayward",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T04:00:00+00:00",
    "summary": "arXiv:2608.21843v1 Announce Type: new Abstract: In 2025, bilateral foreign aid was reduced by 23%, affecting more than 130 aid recipient countries. We assess whether debt service relief or remittance "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.21873",
    "domain": "金融",
    "title": "Discrete asset pricing under transaction costs and model uncertainty with and without short-sale constraints",
    "url": "https://arxiv.org/abs/2608.21873",
    "source": "Wenqing Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T04:00:00+00:00",
    "summary": "arXiv:2608.21873v1 Announce Type: new Abstract: We study discrete-time asset pricing with bid-ask spreads and model uncertainty. The family of probability measures enters the no-arbitrage condition th"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.21888",
    "domain": "金融",
    "title": "Short-horizon mean reversion in cryptocurrency markets: a matched cross-market measurement",
    "url": "https://arxiv.org/abs/2608.21888",
    "source": "Nadav A. Kitron, Jonathan M. Wengrowicz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T04:00:00+00:00",
    "summary": "arXiv:2608.21888v1 Announce Type: new Abstract: At 15-minute horizons, directional mean reversion is far stronger and more pervasive in cryptocurrency markets than in US equities: scored under one mat"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.22478",
    "domain": "金融",
    "title": "Arbitrage-Aware Multi-Step Forecasting of Implied Volatility Surfaces: Modelling Surface Trajectories Using Latent Diffusion",
    "url": "https://arxiv.org/abs/2608.22478",
    "source": "Dominik Manuel Buchegger, Lukas Gonon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T04:00:00+00:00",
    "summary": "arXiv:2608.22478v1 Announce Type: new Abstract: Implied volatility surfaces summarise the option market and are central to many financial applications. Forecasting their future evolution requires mode"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.22620",
    "domain": "金融",
    "title": "WSVI: A Dimensionless Shape Family for Implied Volatility and Its Static No-Arbitrage Structure",
    "url": "https://arxiv.org/abs/2608.22620",
    "source": "Charles Clevenger, Xiang Wan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T04:00:00+00:00",
    "summary": "arXiv:2608.22620v1 Announce Type: new Abstract: W-shaped smiles appear in near-expiry options around binary events such as earnings, and have been associated with bimodal risk-neutral densities. The t"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.22864",
    "domain": "金融",
    "title": "From Exponential to Polynomial: An Exact Filter for High-Dimensional MSM Models",
    "url": "https://arxiv.org/abs/2608.22864",
    "source": "Daniyal Ali Hameedi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T04:00:00+00:00",
    "summary": "arXiv:2608.22864v1 Announce Type: new Abstract: In this paper we propose a new formulation of the Bayesian Filter as used in the discrete-time Markov-Switching-Multifractal (MSM) model of volatility b"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.23051",
    "domain": "金融",
    "title": "Female Nomination and Party Vote Share in US Gubernatorial Elections",
    "url": "https://arxiv.org/abs/2608.23051",
    "source": "Paolo Verme",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T04:00:00+00:00",
    "summary": "arXiv:2608.23051v1 Announce Type: new Abstract: What happens to a party's vote share when it nominates a woman for executive office? The evidence on female candidates is dominated by legislative races"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.23053",
    "domain": "金融",
    "title": "tse_tick: A Python Library for Parsing and Querying Nikkei NEEDS Tick Data from the Tokyo Stock Exchange",
    "url": "https://arxiv.org/abs/2608.23053",
    "source": "Kazumi Li, Masataka Hayashi, Teruo Nakatsuma, Peter Romero",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T04:00:00+00:00",
    "summary": "arXiv:2608.23053v1 Announce Type: new Abstract: Tick-level trade-and-quote data for the Tokyo Stock Exchange is distributed through the Nikkei NEEDS service as thousands of zipped CSV archives spannin"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.23274",
    "domain": "金融",
    "title": "The Physical Crash Frontier: What Finite Option Quotes Can and Cannot Reveal",
    "url": "https://arxiv.org/abs/2608.23274",
    "source": "Jirong Zhuang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T04:00:00+00:00",
    "summary": "arXiv:2608.23274v1 Announce Type: new Abstract: Option prices are prices of insurance, so the risk-neutral probabilities they imply overstate physical crash risk. A power utility pricing kernel undoes"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.23369",
    "domain": "金融",
    "title": "Culture and constitutional compliance",
    "url": "https://arxiv.org/abs/2608.23369",
    "source": "Jerg Gutmann, Anna Lewczuk-Czerwi\\'nska, Jacek Lewkowicz, Stefan Voigt",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T04:00:00+00:00",
    "summary": "arXiv:2608.23369v1 Announce Type: new Abstract: Constitutions as the formal foundation of a country's legal and political system have important economic and political effects. Yet, we still know littl"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.23393",
    "domain": "金融",
    "title": "KellyBoost: Growth-Optimal Portfolio Construction with Gradient-Boosted Trees",
    "url": "https://arxiv.org/abs/2608.23393",
    "source": "Jiayu Li",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T04:00:00+00:00",
    "summary": "arXiv:2608.23393v1 Announce Type: new Abstract: KellyBoost is a single multi-output XGBoost model whose softmax output is the portfolio: with y the vector of per-asset holding-period returns, the trai"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.23524",
    "domain": "金融",
    "title": "The Measurement Revolution? Credible Measurement and Inference in the Age of AI",
    "url": "https://arxiv.org/abs/2608.23524",
    "source": "Melissa Dell, Ashesh Rambachan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T04:00:00+00:00",
    "summary": "arXiv:2608.23524v1 Announce Type: new Abstract: Artificial intelligence (AI) is transforming measurement in economics. AI models convert unstructured data, such as text and images, into structured var"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.04432",
    "domain": "金融",
    "title": "The Price of Isolation: Estimating the Ecosystem Cost of Symmetric Two-Sided A/B Testing",
    "url": "https://arxiv.org/abs/2608.04432",
    "source": "Yuanyuan Shen, Yiren Yan, Wenjie Li, Chunhui Zhu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T04:00:00+00:00",
    "summary": "arXiv:2608.04432v1 Announce Type: cross Abstract: On two-sided content platforms, symmetric two-sided isolation (assigning matched fractions of creators and viewers to isolated treatment and control s"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.22497",
    "domain": "金融",
    "title": "Reflexivity from Hierarchical Causality",
    "url": "https://arxiv.org/abs/2608.22497",
    "source": "Tim Gebbie",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T04:00:00+00:00",
    "summary": "arXiv:2608.22497v1 Announce Type: cross Abstract: We consider reflexivity in hierarchical causal systems in which higher-level states constrain the lower-level dynamics that remain admissible [Wilcox "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.22697",
    "domain": "金融",
    "title": "Does Rank Still Matter? Position Bias When AI Agents Shop on Our Behalf",
    "url": "https://arxiv.org/abs/2608.22697",
    "source": "Davood Wadi, Yu Ma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T04:00:00+00:00",
    "summary": "arXiv:2608.22697v1 Announce Type: cross Abstract: Search rankings are valuable because human attention is scarce and sequential. Higher-placed alternatives are easier to find, so they are examined and"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.22703",
    "domain": "金融",
    "title": "Diagonal Frog meets ADI: trading matrix exponentials for rational maps in the Fokker--Planck equation",
    "url": "https://arxiv.org/abs/2608.22703",
    "source": "Andrey Itkin, Rakhymzhan Kazbek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T04:00:00+00:00",
    "summary": "arXiv:2608.22703v1 Announce Type: cross Abstract: A companion paper \\cite{ItkinDF2026} introduced the Diagonal Frog (DF) positivity-preserving schemes for anisotropic Fokker--Planck equations, advanci"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.22768",
    "domain": "金融",
    "title": "The Loop-Gain Matrix: Coupled Rebalancing Feedback and the Blind Spots of Scalar Stability Monitoring",
    "url": "https://arxiv.org/abs/2608.22768",
    "source": "Jihwan Woo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T04:00:00+00:00",
    "summary": "arXiv:2608.22768v1 Announce Type: cross Abstract: The stability of markets hosting leveraged exchange-traded products is governed not by any single product's loop gain but by the spectral radius of a "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.22852",
    "domain": "金融",
    "title": "Your AI, On a Dial: Controlling Investment Bias in LLMs with a Single Neuron",
    "url": "https://arxiv.org/abs/2608.22852",
    "source": "Sahong Park, Suhwan Park, Hoyoung Lee, Gakyung Kwon, Wonbin Ahn, Jaewon Choi, Alejandro Lopez-Lira, Yoon Kim, Chanyeol Choi, Hyeongwoo Kong, Yongjae Lee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T04:00:00+00:00",
    "summary": "arXiv:2608.22852v1 Announce Type: cross Abstract: Large language models (LLMs) are increasingly used in investment decision-making, yet prior work shows that they exhibit systematic, model-specific in"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.23416",
    "domain": "金融",
    "title": "The Axiomatic Trader: Latent Regularity, Information Budgets, and the Canonical Form of a Quantitative Investment System",
    "url": "https://arxiv.org/abs/2608.23416",
    "source": "Jiayu Li",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T04:00:00+00:00",
    "summary": "arXiv:2608.23416v1 Announce Type: cross Abstract: Systematic trading rests on one article of faith: that regularities found in the past persist. We state it as a time-invariant mechanism driven by an "
  },
  {
    "id": "rss:https://arxiv.org/abs/2108.02283",
    "domain": "金融",
    "title": "Machine Learning Classification and Portfolio Construction: Does the Loss Function Matter?",
    "url": "https://arxiv.org/abs/2108.02283",
    "source": "Yang Bai, Kuntara Pukthuanthong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T04:00:00+00:00",
    "summary": "arXiv:2108.02283v4 Announce Type: replace Abstract: Classification outperforms regression across matched machine learning models in portfolio construction. A stacking ensemble of gradient boosted tree"
  },
  {
    "id": "rss:https://arxiv.org/abs/2206.08401",
    "domain": "金融",
    "title": "Is Decentralized Finance Actually Decentralized? An Interdisciplinary Framework Integrating Network Theory, Agent-Based Simulation, and Longitudinal Evidence from Aave, GHO Issuance, and Cross-Chain E",
    "url": "https://arxiv.org/abs/2206.08401",
    "source": "Ziqiao Ao, Lin William Cong, Gergely Horvath, Luyao Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T04:00:00+00:00",
    "summary": "arXiv:2206.08401v5 Announce Type: replace Abstract: Decentralized finance (DeFi) can broaden access while leaving activity, network position, and infrastructure concentrated. We develop a four-dimensi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2409.17035",
    "domain": "金融",
    "title": "Scaling up to the cloud: Cloud technology use and growth rates in small and large firms",
    "url": "https://arxiv.org/abs/2409.17035",
    "source": "Bernardo Caldarola, Luca Fontanelli",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T04:00:00+00:00",
    "summary": "arXiv:2409.17035v5 Announce Type: replace Abstract: Using a unique combination of micro-level data sources on French firms, this paper explores the relationship between cloud technologies and firm gro"
  },
  {
    "id": "rss:https://arxiv.org/abs/2410.13100",
    "domain": "金融",
    "title": "Quantifying socio-temporal effects of loan delinquency drivers in microfinance",
    "url": "https://arxiv.org/abs/2410.13100",
    "source": "Cedric H. A. Koffi, Viani Biatat Djeundje, Olivier Menoukeu Pamen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T04:00:00+00:00",
    "summary": "arXiv:2410.13100v3 Announce Type: replace Abstract: We develop and evaluate a family of discrete-time logit-link (LLink) models, including fixed-effects and frailty extensions, to quantify association"
  },
  {
    "id": "rss:https://arxiv.org/abs/2502.19862",
    "domain": "金融",
    "title": "Optimal risk-aware interest rates for decentralized lending protocols",
    "url": "https://arxiv.org/abs/2502.19862",
    "source": "Bastien Baude, Damien Challet, Ioane Muni Toke",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T04:00:00+00:00",
    "summary": "arXiv:2502.19862v2 Announce Type: replace Abstract: Interest rates in decentralized lending protocols are set algorithmically and adjust to supply and demand for liquidity. In this study, we propose a"
  },
  {
    "id": "rss:https://arxiv.org/abs/2509.01310",
    "domain": "金融",
    "title": "Gender Differences in Healthcare Utilisation: Causal Evidence from Unexpected Adverse Health Shocks",
    "url": "https://arxiv.org/abs/2509.01310",
    "source": "Nadja van 't Hoff, Giovanni Mellace, Seetha Menon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T04:00:00+00:00",
    "summary": "arXiv:2509.01310v2 Announce Type: replace Abstract: Women live longer than men yet report worse health. One common reading of this male-female health-survival paradox is that women also engage more wi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2511.02016",
    "domain": "金融",
    "title": "ABIDES-MARL: A Multi-Agent Reinforcement Learning Environment for Optimal Execution with Endogenous Liquidity",
    "url": "https://arxiv.org/abs/2511.02016",
    "source": "Patrick Cheridito, Jean-Loup Dupret, Zhexin Wu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T04:00:00+00:00",
    "summary": "arXiv:2511.02016v2 Announce Type: replace Abstract: Classical optimal execution models treat market impact as a pre-specified, exogenous process. However, when market makers adapt strategically, this "
  },
  {
    "id": "rss:https://arxiv.org/abs/2601.03799",
    "domain": "金融",
    "title": "Optimal execution on Uniswap v2/v3 under transient price impact",
    "url": "https://arxiv.org/abs/2601.03799",
    "source": "Bastien Baude, Damien Challet, Ioane Muni Toke",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T04:00:00+00:00",
    "summary": "arXiv:2601.03799v2 Announce Type: replace Abstract: We study the optimal liquidation of a large position on Uniswap v2 and Uniswap v3 in discrete time. The instantaneous price impact is derived from t"
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
    "id": "hn:49414279",
    "domain": "金融",
    "title": "Tesla discontinues its Solar Roof tiles, not economically viable",
    "url": "https://electrek.co/2026/08/20/tesla-discontinues-solar-roof-panels-only/",
    "source": "MilnerRoute",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-08-24T01:21:56+00:00",
    "summary": ""
  },
  {
    "id": "hn:49304409",
    "domain": "金融",
    "title": "Make a 6-Tesla-class high-temperature superconducting dipole magnet at 4.2 K",
    "url": "https://journals.aps.org/prab/abstract/10.1103/4nhs-bkwh",
    "source": "supermagnet",
    "platform": "hackernews",
    "points": 48,
    "published_at": "2026-08-14T20:49:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:49206115",
    "domain": "金融",
    "title": "Anthropic CEO reportedly worried new hires only care about money",
    "url": "https://finance.yahoo.com/technology/ai/articles/anthropic-ceo-reportedly-worried-hires-160000647.html",
    "source": "frays",
    "platform": "hackernews",
    "points": 65,
    "published_at": "2026-08-07T05:15:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:49391382",
    "domain": "金融",
    "title": "Tesla sunsets its Solar Roof tiles",
    "url": "https://www.theverge.com/tech/983167/tesla-solar-roof-tiles-discontinued",
    "source": "doener",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-08-21T17:32:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:49097833",
    "domain": "金融",
    "title": "Show HN: The Federalist Papers, typeset as the 1787 newspapers they ran in",
    "url": "https://federalistreader.org/",
    "source": "vhwalke",
    "platform": "hackernews",
    "points": 58,
    "published_at": "2026-07-29T14:13:54+00:00",
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
  }
]
```
