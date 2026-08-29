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

- 今日日期：`2026-08-29`
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
  "date": "2026-08-29",
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
    "title": "9分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 1769315,
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
    "points": 1206139,
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
    "points": 1121769,
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
    "points": 1064820,
    "published_at": "2026-05-11T09:02:15+00:00",
    "summary": "文档链接：https://lcnaoyjp4e3z.feishu.cn/wiki/MtJlwX0B5iy6y9k5GZTcdjSknTd"
  },
  {
    "id": "bvid:BV1WBG9zgECp",
    "domain": "AI",
    "title": "史上最强 AI 编程工具免费啦！Cursor 保姆级使用教程！新手友好！看到就是赚到！｜ 集成 MCP ！",
    "url": "http://www.bilibili.com/video/av114426116120045",
    "source": "AfterShip",
    "platform": "bilibili",
    "points": 672397,
    "published_at": "2025-05-01T04:00:00+00:00",
    "summary": "相信你已经在网上刷到过不少的 AI 工具，但如果你让我推荐最值得我们每个人学习的一款 AI 工具，那绝对就是史上最强的 AI 编程工具 —— Cursor。为此，我们录制了一个保姆级的 Cursor 新手教程，在这里免费分享给大家。即使你是一个对 AI 完全 0 基础的新手小白，看完这个视频后，你也可以彻底了解 Cursor 这个软件，并知道如何从 0 到 1 用 Cursor 做出入门级的 AI"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 658049,
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
    "points": 648032,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 632391,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1Krpfe8EfU",
    "domain": "AI",
    "title": "我的世界【国内离线服务器推荐】2024离线服务器 小游戏 生存 RPG 无政府 星露谷 粘液科技",
    "url": "http://www.bilibili.com/video/av112978611474242",
    "source": "一只呱呱捏",
    "platform": "bilibili",
    "points": 300706,
    "published_at": "2024-08-17T17:51:07+00:00",
    "summary": "视频制作不易还请一键三连加关注(≧ω≦)/\n1.mc.163mc.cn\n2.wdsj.net\n3.mc.remiaft.com\n4.2b2t.xin\n5.CHAOS SMP 白名单：624324072\n6.方块传说服务器群：458742218\n7.魔法小镇服务器群：925055004\n8.缘木方舍服务器群：1006141418"
  },
  {
    "id": "bvid:BV1qGc7zwEX6",
    "domain": "AI",
    "title": "史上最强 AI 编程工具Cursor来啦！Cursor保姆级使用教程！新手友好！看到就是赚到！！！",
    "url": "http://www.bilibili.com/video/av116061928226926",
    "source": "知名的阿呆同学",
    "platform": "bilibili",
    "points": 278409,
    "published_at": "2026-02-19T07:34:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 258848,
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
    "points": 249462,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1e3t4etExj",
    "domain": "AI",
    "title": "手摸手的AI编程cursor实战【小白教程】",
    "url": "http://www.bilibili.com/video/av113148447169565",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 234990,
    "published_at": "2024-09-17T01:00:00+00:00",
    "summary": "喜欢的朋友可以三连+关注～这对我真的很重要"
  },
  {
    "id": "bvid:BV1Pk4d6KEvZ",
    "domain": "AI",
    "title": "服 务 器 又 来 新 人【服务器生存指南】",
    "url": "http://www.bilibili.com/video/av117168553329255",
    "source": "不风采的琴",
    "platform": "bilibili",
    "points": 227255,
    "published_at": "2026-08-28T04:00:00+00:00",
    "summary": "为什么床可以复活\n部分BGM：坏蛋联盟原声、我的世界原声、我的世界故事模式原声、That Man、Asc.Scorpio等"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 180150,
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
    "points": 149469,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1bk4y1m79S",
    "domain": "AI",
    "title": "【白话科普】服务器是什么 ｜能做什么  | 和电脑有什么区别 | 什么是云服务器 | 网站上线系列分享",
    "url": "http://www.bilibili.com/video/av754075347",
    "source": "好奇代码的三木",
    "platform": "bilibili",
    "points": 148407,
    "published_at": "2020-07-27T11:55:35+00:00",
    "summary": "我的JavaScript + Nodejs高手之路全栈课，就在B站课堂！课程地址 → https://www.bilibili.com/cheese/play/ss1226\n\n在买服务器之前\n我们要先来了解下服务器是什么\n\n全集系列在此  BV18a4y1Y7e9"
  },
  {
    "id": "bvid:BV1FV4xz9EPt",
    "domain": "AI",
    "title": "使用云服务器搭建内网穿透！纵享独属于个人的丝滑体验！",
    "url": "http://www.bilibili.com/video/av115353979983816",
    "source": "在下莫老师",
    "platform": "bilibili",
    "points": 119832,
    "published_at": "2025-10-11T09:00:00+00:00",
    "summary": "本期编号：EP268\n\n莫老师的附件表（快捷键Crtl+F搜索视频标题）：\n\n推荐：www.在下莫老师.com\n备用：www.zxmls.lol"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 102201,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1dpdZYBE9q",
    "domain": "AI",
    "title": "零代码让AI秒接海量MCP工具！最适合小白的MCP集合平台",
    "url": "http://www.bilibili.com/video/av114340703243255",
    "source": "AI研究室-帆哥",
    "platform": "bilibili",
    "points": 99866,
    "published_at": "2025-04-15T11:00:00+00:00",
    "summary": "最近MCP太火了，阿里直接跟进把MCP整合到百炼平台里面了，做了一个MCP的“应用商店”。\n之前不管是在cursor还是Claude上还是需要配置一下MCP服务器，现在在百炼上就可以直接无脑添加MCP工具，非常方便。\n而且因为在平台上一体化，和大模型可以打包配置，让后端的运维部署变得更轻松。\n这个视频教你怎么用阿里云百炼的MCP工具创建一个agent应用。"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 93426,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1ZRbe6eENh",
    "domain": "AI",
    "title": "DeepSeek Harness安装和使用教程【最新完整版】零基础小白速通deepseek harness入门教程怎么下载插件如何安装如何使用全搞定！",
    "url": "http://www.bilibili.com/video/av117110286062691",
    "source": "鹏哥C语言",
    "platform": "bilibili",
    "points": 87650,
    "published_at": "2026-08-17T10:10:51+00:00",
    "summary": "欢迎大家来到鹏哥课堂！这份DeepSeek Harness教程专为零基础小白打造，全程手把手演示安装、启动Web界面、模型接入、基础任务实操。 很多小白卡在环境配置、命令报错、参数设置，本教程能让你避开各种坑，跟着操作就能成功运行。 搞懂 Agent = 模型 + Harness，让 AI 读写文件、执行命令、自主完成项目任务。本教程适合程序员、AI 爱好者及想上手本地智能体的同学等。希望大家把视"
  },
  {
    "id": "bvid:BV1vYFQzQE4P",
    "domain": "AI",
    "title": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！Claude Code Hooks回调+Agent Teams全自动开发零轮询",
    "url": "http://www.bilibili.com/video/av116046157647899",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 47659,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1sZMq6qEko",
    "domain": "AI",
    "title": "从0做出你的第一个App ｜ 零基础AI编程保姆教程",
    "url": "http://www.bilibili.com/video/av117038647352026",
    "source": "木子不写代码",
    "platform": "bilibili",
    "points": 41688,
    "published_at": "2026-08-07T12:15:00+00:00",
    "summary": "这期视频，我会手把手带你，用 AI 做出你的第一个 App。\n全程假设你没有任何编程和AI的基础，\n我们从如何写需求提示词开始，\n到确定页面结构和设计，\n产品需求文档，\n开发计划，\n第一版APP验收，\ngit代码存档，\n二次开发，\n界面美化，\n做好的APP也会开源给到大家，\n我也会演示如何获取这个项目源代码并且用AI继续定制开发，\n视频到最后，\n你会收获一个为自己的工作和生活定制的专属APP！\n和"
  },
  {
    "id": "bvid:BV18Zu76fEoH",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent零基础全套教程，2026最新版，全程干货无废话！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI",
    "url": "http://www.bilibili.com/video/av117047069509564",
    "source": "Agent智能体搭建-",
    "platform": "bilibili",
    "points": 34102,
    "published_at": "2026-08-06T08:03:07+00:00",
    "summary": "【系统学习、最新学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本合集从零基础开始，手把手带你走完一条完整的AI Agent 学习路径：\n→ 大模型认知与API调用（不用懂原理也能上手）\n→ Python速成（学AI够用的部分，不浪费）\n→ 提示词工程（让大模型听懂你的话）\n→ RAG检索增强（解决AI胡说八道的问题）\n→ LangChain框架（Agent开"
  },
  {
    "id": "bvid:BV1cdbB6nEhs",
    "domain": "AI",
    "title": "我的世界中国版不稳定SMP服务器教程",
    "url": "http://www.bilibili.com/video/av117113826056179",
    "source": "晚渡_神焀",
    "platform": "bilibili",
    "points": 33884,
    "published_at": "2026-08-18T01:10:31+00:00",
    "summary": "我的世界SMP服务器教学，温布同款"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 30394,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV1dZud6VE5G",
    "domain": "AI",
    "title": "【AI实战】AI Agent智能教务排课与教学质量分析系统，基于SpringAI+Springboot+Agent的教务排课系统，教学质量分析系统",
    "url": "http://www.bilibili.com/video/av117070104692483",
    "source": "武哥聊编程",
    "platform": "bilibili",
    "points": 24530,
    "published_at": "2026-08-10T07:48:01+00:00",
    "summary": "完整资料：https://aigcbaba.com/course/98"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 20469,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1PZhw6cEfR",
    "domain": "AI",
    "title": "【全92集】吊打付费！目前B站最全最细《AI Agent开发》系统教程，2026最新版，含所有干货！7天就能从小白到大神！少走99%湾路！存下吧！很难找全的！",
    "url": "http://www.bilibili.com/video/av117165936149836",
    "source": "coming-AI",
    "platform": "bilibili",
    "points": 15307,
    "published_at": "2026-08-27T06:02:14+00:00",
    "summary": "整理制作不易，大家记得点个关注，一键三连呀【点赞、收藏、转发】感谢支持~"
  },
  {
    "id": "bvid:BV1Tz8g6HErC",
    "domain": "AI",
    "title": "【全748集】B站最全最细的AI Agent零基础入门教程，2026最新版，教学通俗易懂，小白适用！普通人也能抓住的AI风口！手把手教会你agent智能体搭建~",
    "url": "http://www.bilibili.com/video/av117115201789701",
    "source": "AI全栈开发",
    "platform": "bilibili",
    "points": 10728,
    "published_at": "2026-08-18T11:27:05+00:00",
    "summary": "【2026最新版AI Agent智能体零基础全套教程 | 配套源码+学习路线+项目案例，看置顶评论自取】\n本套教程专为零基础设计，从Agent原理到独立打造智能体，手把手带你系统掌握AI Agent智能体搭建。\n✅ Agent基础：什么是Agent、三大核心能力（规划/工具/记忆）\n✅ 主流框架：Langchain、LangGraph主流框架\n✅ 多Agent协作：A2A协议、任务编排与调度\n✅ "
  },
  {
    "id": "bvid:BV1eMgG6QEeG",
    "domain": "AI",
    "title": "【吴恩达】这绝对是把《Vibe Coding》讲得最通透的一套课！手把手教你构建自己的企业级AI工作流，学完直接落地！——附带课件代码",
    "url": "http://www.bilibili.com/video/av117081815189025",
    "source": "吴恩达Agents",
    "platform": "bilibili",
    "points": 9746,
    "published_at": "2026-08-12T09:29:57+00:00",
    "summary": "Vibe Coding火了，但你会发现——AI写的代码像开盲盒，今天能跑明天崩，项目一大就乱套。\n规范驱动开发（SDD） 就是来解决这个问题的。它的核心理念很简单：在让AI写代码之前，先和AI在统一的规范文档里对齐需求，把开发变成可预测、可追溯、可控制的过程。"
  },
  {
    "id": "bvid:BV1itb667EXd",
    "domain": "AI",
    "title": "【全749集】吊打付费！目前B站最全最细《AI Agent开发》系统教程，2026最新版，含所有干货！7天就能从小白到大神！少走99%湾路！存下吧！很难找全的！",
    "url": "http://www.bilibili.com/video/av117114966971955",
    "source": "AI-Agent开发",
    "platform": "bilibili",
    "points": 8829,
    "published_at": "2026-08-18T05:59:59+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1JTV26wEYV",
    "domain": "AI",
    "title": "Cursor vs Codex：AI编程工具真实体验对比，200刀该充给谁？",
    "url": "http://www.bilibili.com/video/av116684044179010",
    "source": "现场敲代码",
    "platform": "bilibili",
    "points": 8379,
    "published_at": "2026-06-03T03:29:24+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1As1HB1EGs",
    "domain": "AI",
    "title": "Cursor 2.0 - 多智能体协同，Composer编程模型",
    "url": "http://www.bilibili.com/video/av115494103359207",
    "source": "五里墩茶社",
    "platform": "bilibili",
    "points": 7419,
    "published_at": "2025-11-04T23:58:14+00:00",
    "summary": "一个key用全球大模型🔴 https://DMXAPI.cn 🚀 国内直连OpenAI、Claude、Gemini，💰￥1元起充！\n推荐一个目前全网价格最实惠的合租平台，ChatGPT，MidJourney，奈飞，迪士尼，苹果TV等热门软件应有尽有 - https://dub.sh/unibus ，首单9折优惠 - 优惠码 01Coder\n\n- 加入我的知识星球：https://t.zsxq.co"
  },
  {
    "id": "bvid:BV1aSR4BKESW",
    "domain": "AI",
    "title": "安卓手机部署Claude Code",
    "url": "http://www.bilibili.com/video/av116526891993752",
    "source": "中国小骑士",
    "platform": "bilibili",
    "points": 6769,
    "published_at": "2026-05-06T09:24:14+00:00",
    "summary": "通过Termux安装Claude Code并且接入国内大模型"
  },
  {
    "id": "bvid:BV1tBuq65Epg",
    "domain": "AI",
    "title": "【前端必看】B站最细最全的前端转AI Agent开发教程，7天带你从入门到精通，2026最新版，包含所有干货！比付费强10倍，学完既可就业！",
    "url": "http://www.bilibili.com/video/av117075959876425",
    "source": "AI开发应用",
    "platform": "bilibili",
    "points": 5928,
    "published_at": "2026-08-11T09:21:12+00:00",
    "summary": "【前端必看】B站最细最全的前端转AI Agent开发教程，7天带你从入门到精通，2026最新版，包含所有干货！比付费强10倍，学完既可就业！"
  },
  {
    "id": "bvid:BV13cmnBFEP9",
    "domain": "AI",
    "title": "Claude Code教程9：Claude Code与GitHub的高效联动",
    "url": "http://www.bilibili.com/video/av115689541077475",
    "source": "木乐乐的异想世界",
    "platform": "bilibili",
    "points": 5508,
    "published_at": "2025-12-09T12:17:23+00:00",
    "summary": "【Claude Code教程第9集中文翻译】Net Ninja带你解锁Claude Code与GitHub的高效联动！本集聚焦实用核心功能：无需复杂配置，在Claude聊天会话中即可设置GitHub集成——安装后自动创建两个关键GitHub Action：①自动审查拉取请求（PR）并给出精准反馈；②当仓库问题提及Claude时，自动在新功能分支处理该问题。注意：需先安装GitHub CLI（附官方"
  },
  {
    "id": "bvid:BV1aMAczmEmf",
    "domain": "AI",
    "title": "[MoonPack]在布吉岛里注入模组-mcp",
    "url": "http://www.bilibili.com/video/av116264966163402",
    "source": "DanciestZebra70",
    "platform": "bilibili",
    "points": 5207,
    "published_at": "2026-03-21T03:13:25+00:00",
    "summary": "交流群\n①1051043310\n②365233792"
  },
  {
    "id": "bvid:BV16xdBBLEtR",
    "domain": "AI",
    "title": "手把手教你搭建Claude MCP服务：从本地到远程，大厂已落地",
    "url": "http://www.bilibili.com/video/av116417437503756",
    "source": "下班学AI",
    "platform": "bilibili",
    "points": 4769,
    "published_at": "2026-04-17T01:25:49+00:00",
    "summary": "🔥 MCP（模型上下文协议）到底是什么？为什么阿里、腾讯都在抢着布局？\n\n本期视频带你从零上手MCP——从常见的开源服务（Playwright自动化、Figma设计转代码、GitHub操作），到手写一个自己的MCP服务器（时间查询、数字相加、商品价格查询），并成功接入Claude CLI实现本地调用。\n\n随后，我会演示如何将MCP服务从本地部署到云端，让它真正变成可远程调用的AI能力。\n\n最后，拆"
  },
  {
    "id": "bvid:BV1TZ8X6gEJp",
    "domain": "AI",
    "title": "我发现了这个服务器的遗产...",
    "url": "http://www.bilibili.com/video/av117161104448971",
    "source": "Natko物语",
    "platform": "bilibili",
    "points": 4163,
    "published_at": "2026-08-26T11:40:46+00:00",
    "summary": "这是BrokenLandSMP的第二季第二集！\n你看 我们简直是拖更传奇\n\n“这个服务器的历史中还埋藏着许多我们不知道的故事，关于覆灭的文明，关于污染的来历。\n我会继续探究，直到世界的尽头。”\n\n感谢参演：@余忧Yuyo  @棒棒糖麦当果  @litanbo暮色哥  @Ange_FC  \n\n你可以加入qq群聊664184185以了解服务器！ \n另外 如果你对BrokenLand感兴趣 请关注@煅灼"
  },
  {
    "id": "bvid:BV1bzg36rEfP",
    "domain": "AI",
    "title": "【2026年8月最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av117096964953989",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 3765,
    "published_at": "2026-08-15T01:49:32+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1Rutc6AEKW",
    "domain": "AI",
    "title": "【Agent开发教程】这绝对是你看过讲的最好的AI Agent智能体教程，包含Agent+RAG+MCP+LangChain+LangGraph+企业级项目实战",
    "url": "http://www.bilibili.com/video/av117172009437972",
    "source": "图灵学院官方",
    "platform": "bilibili",
    "points": 3488,
    "published_at": "2026-08-28T07:52:39+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n【本视频笔记代码、大模型最新学习路线、系统学习课程、实战案例、电子书+问题解答等戳这里获取→https://www.bilibili.com/read/cv39576966/?jump_opus=1】"
  },
  {
    "id": "bvid:BV1anhG6KEYc",
    "domain": "AI",
    "title": "3分钟搞定Claude桌面版安装+汉化+自由接入大模型",
    "url": "http://www.bilibili.com/video/av117155483944854",
    "source": "大海资源",
    "platform": "bilibili",
    "points": 3142,
    "published_at": "2026-08-25T09:44:19+00:00",
    "summary": "Claude命令版安装教程：https://www.bilibili.com/video/BV1iTbX6JEyy/\ncodex安装教程：https://www.bilibili.com/video/BV1PkGg6BEBz/\n桌面版文字教程：https://www.dhzyw.com/archives/11528.html"
  },
  {
    "id": "bvid:BV1jqMD6bEyi",
    "domain": "AI",
    "title": "史上最强AI编程工具免费啦！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av117030275515194",
    "source": "千川-Pro",
    "platform": "bilibili",
    "points": 2812,
    "published_at": "2026-08-03T07:00:12+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1zu4k6nEVU",
    "domain": "AI",
    "title": "2026测试新方向：AI Agent测试零基础教程，从基础到智能体测试实战（DeepSeek决策+Playwright执行）",
    "url": "http://www.bilibili.com/video/av117177378150162",
    "source": "软件测试零基础入门",
    "platform": "bilibili",
    "points": 2673,
    "published_at": "2026-08-29T06:32:04+00:00",
    "summary": "勉费领取视频全套资料/文档/学习笔记点旁边这个链接哦→https://www.bilibili.com/opus/918700823271178265?spm_id_from=333.1387.0.0"
  },
  {
    "id": "bvid:BV1W26PYbEdK",
    "domain": "AI",
    "title": "AI编程IDE-Cursor的R语言配置",
    "url": "http://www.bilibili.com/video/av113582222082613",
    "source": "灵活胖子的进步之路",
    "platform": "bilibili",
    "points": 2687,
    "published_at": "2024-12-04T13:11:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1PM8y6rEE3",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Vibe Coding】教程！从环境搭建到工作流完整闭环，一套全解决！DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av117137096185556",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 2356,
    "published_at": "2026-08-22T03:48:16+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1d6bZ6wE8W",
    "domain": "AI",
    "title": "【cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av117125217787738",
    "source": "一月还会远吗",
    "platform": "bilibili",
    "points": 2355,
    "published_at": "2026-08-20T01:27:02+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1kt62YrEYP",
    "domain": "AI",
    "title": "AI神助力REAPER的脚本编程，Cursor让小白变身脚本达人，脚本达人升职产品经理",
    "url": "http://www.bilibili.com/video/av113763550238467",
    "source": "音乐人侯吕健",
    "platform": "bilibili",
    "points": 2247,
    "published_at": "2025-01-03T08:47:16+00:00",
    "summary": "自从解锁了使用Cursor的AI助手来助力REAPER的脚本编程这项技能后，感觉就像开了挂，以前确实自己的编程能力有限，很多奇思妙想无法实现，现在可能逐步让它们变成现实，并投入实际应用了。小白也能成为脚本达人，再也不用去学习那些艰深晦涩的代码了。“码农”的工作交给AI，自己当好设计师或产品经理就行了。\n\n视频中脚本的下载地址：\n下载:https://wwty.lanzouu.com/iMOji2j"
  },
  {
    "id": "hn:49458161",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia agrees to acquire Hugging Face for $13B",
    "url": "https://www.businessinsider.com/nvidia-in-talks-to-buy-hugging-face-13-billion-dollars-2026-8",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 1953,
    "published_at": "2026-08-27T01:12:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:49434378",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI Jalapeño: Better than Nvidia Blackwell",
    "url": "https://newsletter.semianalysis.com/p/openai-jalapeno-better-than-nvidia",
    "source": "bmulholland",
    "platform": "hackernews",
    "points": 584,
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
    "id": "hn:49480449",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Insists It Can Keep Printing Money to Fund the AI Boom",
    "url": "https://www.wsj.com/tech/ai/nvidia-insists-it-can-keep-printing-money-to-fund-the-ai-boom-195e7d5e",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 45,
    "published_at": "2026-08-28T15:57:40+00:00",
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
    "id": "hn:49464837",
    "domain": "AI 算力 / 半导体",
    "title": "U.S. considers fresh round of tariffs on semiconductors, report says",
    "url": "https://www.cnbc.com/2026/08/27/trump-semiconductor-tech-tariffs.html",
    "source": "mikhael",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-08-27T13:45:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:49447878",
    "domain": "AI 算力 / 半导体",
    "title": "Who bears the risk in Nvidia's $500B financing platform?",
    "url": "https://www.sascha-steffen.de/updates/nvidia-500bn-ai-financing-credit-risk",
    "source": "rwmj",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-08-26T12:32:31+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/googles-marvell-deal-shows-custom-silicon-spreading-beyond-the-tpu/",
    "domain": "AI 算力 / 半导体",
    "title": "Google’s Marvell Deal Shows Custom Silicon Spreading Beyond the TPU",
    "url": "https://www.eetimes.com/googles-marvell-deal-shows-custom-silicon-spreading-beyond-the-tpu/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T21:59:13+00:00",
    "summary": "Google’s expanded relationship with Marvell suggests that memory, networking, storage, and data movement are candidates for specialization too. The post Google’s Marvell Deal Shows Custom Silicon Spre"
  },
  {
    "id": "rss:https://www.eetimes.com/microscale-power-management-starts-with-microflow-heat-measurement/",
    "domain": "AI 算力 / 半导体",
    "title": "Microscale Power Management Starts with Microflow Heat Measurement",
    "url": "https://www.eetimes.com/microscale-power-management-starts-with-microflow-heat-measurement/",
    "source": "Bill Schweber",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T07:00:00+00:00",
    "summary": "Laser pulses and X-ray imaging reveal the surprising impact of micron-scale material defects on heat dissipation. The post Microscale Power Management Starts with Microflow Heat Measurement appeared f"
  },
  {
    "id": "rss:https://www.eetimes.com/first-benchmarks-revealed-for-jalapeno-openais-clean-sheet-general-purpose-ai-accelerator-asic/",
    "domain": "AI 算力 / 半导体",
    "title": "First Benchmarks Revealed for Jalapeño, OpenAI’s Clean-Sheet General Purpose AI Accelerator ASIC",
    "url": "https://www.eetimes.com/first-benchmarks-revealed-for-jalapeno-openais-clean-sheet-general-purpose-ai-accelerator-asic/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T22:14:16+00:00",
    "summary": "At Hot Chips 2026, Richard Ho, says OpenAI isn't just repurposing a GPU to suit AI: Jalapeño is a purpose built AI accelerator built from scratch for AI workloads. The post First Benchmarks Revealed f"
  },
  {
    "id": "rss:https://www.eetimes.com/qualcomm-bets-open-source-ai-software-can-break-nvidias-lock-in/",
    "domain": "AI 算力 / 半导体",
    "title": "Qualcomm Bets Open-Source AI Software Can Break Nvidia’s Lock-In",
    "url": "https://www.eetimes.com/qualcomm-bets-open-source-ai-software-can-break-nvidias-lock-in/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T18:09:20+00:00",
    "summary": "Modular aims to separate AI software from silicon choice, giving Qualcomm and other challengers a shot at Nvidia-dominated workloads. The post Qualcomm Bets Open-Source AI Software Can Break Nvidia’s "
  },
  {
    "id": "rss:https://www.eetimes.com/newpower-worldwide-expands-credit-facility-to-750-million-to-support-global-growth-and-customer-demand/",
    "domain": "AI 算力 / 半导体",
    "title": "NewPower Worldwide Expands Credit Facility to $750 Million to Support Global Growth and Customer Demand",
    "url": "https://www.eetimes.com/newpower-worldwide-expands-credit-facility-to-750-million-to-support-global-growth-and-customer-demand/",
    "source": "Stefani Munoz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T14:44:16+00:00",
    "summary": "NASHUA, New Hampshire – NewPower Worldwide, one of the electronics industry’s fastest-growing distributors, today announced it has expanded its committed credit facility to $750 million, further enhan"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ddr4/msi-brings-ddr4-back-to-gaming-laptops-amidst-dram-crisis-katana-15-hx-c14-available-with-up-to-core-i9-14900hx-and-rtx-5070",
    "domain": "AI 算力 / 半导体",
    "title": "MSI brings DDR4 back to gaming laptops amidst DRAM crisis — Katana 15 HX C14 available with up to Core i9-14900HX and RTX 5070",
    "url": "https://www.tomshardware.com/pc-components/ddr4/msi-brings-ddr4-back-to-gaming-laptops-amidst-dram-crisis-katana-15-hx-c14-available-with-up-to-core-i9-14900hx-and-rtx-5070",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T15:55:43+00:00",
    "summary": "With 32GB DDR4 SO-DIMM memory kits costing roughly half as much as comparable DDR5 kits, MSI’s new Katana 15 HX C14 could help reduce the impact of soaring memory prices."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/policy/new-us-export-controls-reportedly-target-chinese-access-to-remote-ai-servers-trump-admins-cut-down-ai-diffusion-rule-could-be-shared-with-industry-as-soon-as-september",
    "domain": "AI 算力 / 半导体",
    "title": "New US export controls reportedly target Chinese access to remote AI servers — Trump admin's cut-down AI diffusion rule could be shared with industry as soon as September",
    "url": "https://www.tomshardware.com/tech-industry/policy/new-us-export-controls-reportedly-target-chinese-access-to-remote-ai-servers-trump-admins-cut-down-ai-diffusion-rule-could-be-shared-with-industry-as-soon-as-september",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T15:47:46+00:00",
    "summary": "The Trump administration is reportedly drafting a rule to close a loophole around remote access to advanced AI compute, and it could be shared with trade groups as early as September."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/nvidia-gears-up-its-influence-in-washington-forming-pac-tells-employees-that-decisions-congress-makes-over-the-coming-years-could-have-substantial-consequences-for-the-ai-industry-according-to-report",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia gears up its influence in Washington, forming PAC — tells employees that decisions Congress makes over the coming years could have substantial consequences for the AI industry, according to rep",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/nvidia-gears-up-its-influence-in-washington-forming-pac-tells-employees-that-decisions-congress-makes-over-the-coming-years-could-have-substantial-consequences-for-the-ai-industry-according-to-report",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T15:19:27+00:00",
    "summary": "Nvidia establishes its employees federal political action committee (PAC) to fund politicians whose positions are favorable to Nvidia's interests."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/security-researchers-find-surveillance-implants-in-chinese-made-routers-sold-worldwide-three-different-backdoor-like-implants-hidden-in-firmware",
    "domain": "AI 算力 / 半导体",
    "title": "Security researchers find surveillance implants in Chinese-made routers sold worldwide — three different backdoor-like implants hidden in firmware",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/security-researchers-find-surveillance-implants-in-chinese-made-routers-sold-worldwide-three-different-backdoor-like-implants-hidden-in-firmware",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T14:13:12+00:00",
    "summary": "Security researchers at Vulncheck discovered intentionally masked surveillance implants embedded in the firmware of numerous devices from Shenzhen Zhibotong Electronics."
  },
  {
    "id": "rss:https://www.tomshardware.com/gift-guides-seasonal-sales/save-up-to-usd600-on-ibuypower-gaming-pcs-in-its-labor-day-sale-beat-the-component-crisis-with-big-bundles-and-coupons",
    "domain": "AI 算力 / 半导体",
    "title": "Save up to $600 on iBuyPower gaming PCs in its Labor Day sale — beat the component crisis with big bundles and coupons",
    "url": "https://www.tomshardware.com/gift-guides-seasonal-sales/save-up-to-usd600-on-ibuypower-gaming-pcs-in-its-labor-day-sale-beat-the-component-crisis-with-big-bundles-and-coupons",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T14:00:00+00:00",
    "summary": "iBuypower is hosting a Labor Day sale with up to 65% off our favorite tech products."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/exclusive-dlss-5-has-already-been-ported-to-work-on-rtx-4000-series-graphics-cards-incompatible-cuda-instructions-get-patched-to-work-on-previous-gen-hardware",
    "domain": "AI 算力 / 半导体",
    "title": "DLSS 5 has already been ported to work on RTX 4000 Series graphics cards — incompatible CUDA instructions get patched to work on previous-gen hardware",
    "url": "https://www.tomshardware.com/pc-components/gpus/exclusive-dlss-5-has-already-been-ported-to-work-on-rtx-4000-series-graphics-cards-incompatible-cuda-instructions-get-patched-to-work-on-previous-gen-hardware",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T13:57:35+00:00",
    "summary": "One modder has reverse-engineered DLSS 5 to function on RTX 4000 series Ada Lovelace-based GPUs, porting incompatible CUDA instructions within the Neural Rendering DLL, enabling them to be read on pre"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/cloudflare-frees-100tb-of-ram-by-shrinking-dns-cache-entries",
    "domain": "AI 算力 / 半导体",
    "title": "Cloudflare frees up 100TB of RAM by shrinking 1.1.1.1's DNS cache entries — 250 billion cached DNS entries at any given time means one wasted byte costs 250GB",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/cloudflare-frees-100tb-of-ram-by-shrinking-dns-cache-entries",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T13:14:41+00:00",
    "summary": "Cloudflare says that it has freed up roughly 100TB of RAM across its global fleet without reconfiguring any physical RAM modules in its servers."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-denies-pausing-ai-cloud-commitments-initiative-after-reported-partner-backlash-report-claims-company-told-cloud-providers-it-could-only-lease-its-gpus-to-nvidia-approved-customers",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia denies pausing AI cloud commitments initiative after reported partner backlash — report claims company told cloud providers it could only lease its GPUs to Nvidia-approved customers",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-denies-pausing-ai-cloud-commitments-initiative-after-reported-partner-backlash-report-claims-company-told-cloud-providers-it-could-only-lease-its-gpus-to-nvidia-approved-customers",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T13:13:58+00:00",
    "summary": "Nvidia denies putting AI cloud commitments initiative on hold despite reports that some deals were paused amid partner pushback over customer controls and concerns about potential antitrust scrutiny."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/micron-workers-increasingly-support-strike-over-bonus-pay-labor-union-wants-profit-sharing-scheme-as-employees-at-samsung-sk-hynix-enjoy-bonuses-worth-hundreds-of-thousands-of-dollars",
    "domain": "AI 算力 / 半导体",
    "title": "Micron workers increasingly support strike over bonus pay — labor union wants profit-sharing scheme, as employees at Samsung, SK hynix enjoy bonuses worth hundreds of thousands of dollars",
    "url": "https://www.tomshardware.com/tech-industry/micron-workers-increasingly-support-strike-over-bonus-pay-labor-union-wants-profit-sharing-scheme-as-employees-at-samsung-sk-hynix-enjoy-bonuses-worth-hundreds-of-thousands-of-dollars",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T13:07:55+00:00",
    "summary": "80% of Micron workers in Taiwan have signaled that they're willing to go on strike if the company does not strike a deal over bonuses. The employees want to replace the current bonus system with a pro"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/docking-stations-hubs/save-a-ridiculous-76-percent-on-this-7-in-1-hyper-dual-monitor-thunderbolt-4-dock-just-usd24-buys-a-dual-4k60hz-hyperdrive-docking-station-for-pennies-on-the-dollar",
    "domain": "AI 算力 / 半导体",
    "title": "Save a ridiculous 76% on this 7-in-1 Hyper Dual Monitor Thunderbolt 4 Dock — just $24 buys a dual 4K60Hz HyperDrive docking station for pennies on the dollar",
    "url": "https://www.tomshardware.com/peripherals/docking-stations-hubs/save-a-ridiculous-76-percent-on-this-7-in-1-hyper-dual-monitor-thunderbolt-4-dock-just-usd24-buys-a-dual-4k60hz-hyperdrive-docking-station-for-pennies-on-the-dollar",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T11:59:37+00:00",
    "summary": "Grab the HyperDrive Thunderbolt 4 7-in-1 dock for under $25 with code WOOTDOCK (76% off) - run two 4K60Hz monitors or one 8K30Hz display and additional connectivity for a pittance"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/policy/x-busts-200-000-strong-chinese-bot-farm-including-accounts-making-claims-about-ai-data-centers-and-electricity-suspect-accounts-posted-claims-about-pricing-and-grid-strain-to-manipulate-debate",
    "domain": "AI 算力 / 半导体",
    "title": "X busts 200,000-strong Chinese bot farm, including accounts making claims about AI data centers and electricity — suspect accounts posted claims about pricing and grid strain to 'manipulate' debate",
    "url": "https://www.tomshardware.com/tech-industry/policy/x-busts-200-000-strong-chinese-bot-farm-including-accounts-making-claims-about-ai-data-centers-and-electricity-suspect-accounts-posted-claims-about-pricing-and-grid-strain-to-manipulate-debate",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T11:07:22+00:00",
    "summary": "The X Safety Team said that at least 200 bot accounts have been making posts to influence public opinion data centers and energy policy. The accounts share links to legitimate news stories and then ad"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/power-supplies/msi-mpg-ai1600ts-pcie5-1600w-power-supply-review",
    "domain": "AI 算力 / 半导体",
    "title": "MSI MPG Ai1600TS PCIE5 1600W power supply review: GPU Safeguard+ protection with Titanium effeciency",
    "url": "https://www.tomshardware.com/pc-components/power-supplies/msi-mpg-ai1600ts-pcie5-1600w-power-supply-review",
    "source": "E. Fylladitakis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T11:05:00+00:00",
    "summary": "MSI's flagship 1600W unit delivers confirmed Titanium efficiency, an all-Japanese component selection, and a genuinely novel approach to GPU power management, but the price tag demands serious justifi"
  },
  {
    "id": "rss:https://www.tomshardware.com/phones/android/google-clamps-down-on-android-app-ram-usage-amid-ai-memory-crisis-developers-have-until-february-2027-to-adapt-to-new-memory-optimizing-rules",
    "domain": "AI 算力 / 半导体",
    "title": "Google clamps down on Android app RAM usage amid AI memory crisis — developers have until February 2027 to adapt to new memory-optimizing rules",
    "url": "https://www.tomshardware.com/phones/android/google-clamps-down-on-android-app-ram-usage-amid-ai-memory-crisis-developers-have-until-february-2027-to-adapt-to-new-memory-optimizing-rules",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T11:00:00+00:00",
    "summary": "Google implements stricter memory limits and introduces new performance standards for Android apps."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/samsungs-new-2tb-990-ssd-is-36-percent-off-at-amazon-nearly-usd200-off-this-gen-4-all-rounder",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung's new 2TB 990 SSD is 36% off at Amazon — nearly $200 off this Gen 4 all-rounder",
    "url": "https://www.tomshardware.com/pc-components/ssds/samsungs-new-2tb-990-ssd-is-36-percent-off-at-amazon-nearly-usd200-off-this-gen-4-all-rounder",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T10:37:21+00:00",
    "summary": "Get 36% off the new Samsung 990 2TB SSD, a $190 saving."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/intel-14a-defect-density-is-dropping-faster-than-the-company-expected-we-have-not-seen-this-performance-since-22nm-says-cfo",
    "domain": "AI 算力 / 半导体",
    "title": "Intel 14A defect density is dropping faster than the company expected — 'we have not seen this performance since 22nm,' says CFO",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/intel-14a-defect-density-is-dropping-faster-than-the-company-expected-we-have-not-seen-this-performance-since-22nm-says-cfo",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T10:30:00+00:00",
    "summary": "Intel says defect density of 14A process technology is declining rapidly as internal teams are already developing 14A-based products, while external clients are now wondering about capacity that Intel"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/modders-get-leaked-dlss-5-running-in-control-early-blackwell-test-drops-rtx-5070-ti-from-71-to-35-fps-at-4k",
    "domain": "AI 算力 / 半导体",
    "title": "Modders get leaked DLSS 5 running in Control — early Blackwell test drops RTX 5070 Ti from 71 to 35 FPS at 4K",
    "url": "https://www.tomshardware.com/pc-components/gpus/modders-get-leaked-dlss-5-running-in-control-early-blackwell-test-drops-rtx-5070-ti-from-71-to-35-fps-at-4k",
    "source": "Dan Mateescu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T10:00:00+00:00",
    "summary": "DLSS 5 has apparently leaked, originating from inside a new game."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/sk-hynix-breaks-ground-on-the-first-hbm-plant-in-the-us-bringing-key-ai-component-production-to-the-states-says-production-starts-in-2029",
    "domain": "AI 算力 / 半导体",
    "title": "SK hynix breaks ground on the first HBM plant in the US, bringing key AI component production to the States — says production starts in 2029",
    "url": "https://www.tomshardware.com/pc-components/dram/sk-hynix-breaks-ground-on-the-first-hbm-plant-in-the-us-bringing-key-ai-component-production-to-the-states-says-production-starts-in-2029",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T09:58:37+00:00",
    "summary": "SK hynix breaks ground on HBM assembly plant in the U.S. that will form a connection between DRAM wafers produced in South Korea and their consumers among AI companies in the U.S."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/indiana-power-provider-proposes-usd59-million-rate-cut-for-state-says-data-centers-and-other-large-customers-are-driving-increased-revenue-move-could-potentially-save-residential-users-usd100-annually",
    "domain": "AI 算力 / 半导体",
    "title": "Indiana power provider proposes $59 million rate cut for state, says data centers and other large customers are driving increased revenue — move could potentially save residential users $100 annually",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/indiana-power-provider-proposes-usd59-million-rate-cut-for-state-says-data-centers-and-other-large-customers-are-driving-increased-revenue-move-could-potentially-save-residential-users-usd100-annually",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T09:37:11+00:00",
    "summary": "I&amp;M, which serves part of Indiana, says that it plans to cut electricity prices for the state, resulting in savings of about $59 million for residential users. This translates to about $100 a year"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/claude-nukes-a-developers-700-gb-home-directory-while-testing-a-script-to-ensure-it-wouldnt-do-so-automatic-model-downgrade-may-have-contributed-to-the-screw-up",
    "domain": "AI 算力 / 半导体",
    "title": "Claude nukes a developer's 700 GB home directory while testing deletion safeguards; automatic model safety downgrade may have contributed to the screw-up — Anthropic safety harness downgraded model to",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/claude-nukes-a-developers-700-gb-home-directory-while-testing-a-script-to-ensure-it-wouldnt-do-so-automatic-model-downgrade-may-have-contributed-to-the-screw-up",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T09:30:00+00:00",
    "summary": "Claude nuked a developer's 700 GB home directory while testing a script to ensure that wouldn't happen, and it's possible that an automatic model downgrade likely contributed to the screw-up"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/chinas-ymtc-aims-to-become-the-worlds-largest-nand-maker-by-the-end-of-2027",
    "domain": "AI 算力 / 半导体",
    "title": "China's YMTC aims to become the world's largest NAND maker by the end of 2027, report says — company plans to overtake Samsung and SK hynix",
    "url": "https://www.tomshardware.com/pc-components/dram/chinas-ymtc-aims-to-become-the-worlds-largest-nand-maker-by-the-end-of-2027",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T16:54:24+00:00",
    "summary": "The target would require YMTC to nearly double its market share in 16 months."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/policy/trump-administration-weighs-expanding-chip-tariffs-to-laptops-consoles-and-servers",
    "domain": "AI 算力 / 半导体",
    "title": "Trump administration weighs expanding chip tariffs to laptops, consoles, and servers, report claims — January's data center exemptions may be scrapped",
    "url": "https://www.tomshardware.com/tech-industry/policy/trump-administration-weighs-expanding-chip-tariffs-to-laptops-consoles-and-servers",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T16:13:27+00:00",
    "summary": "The Trump administration is weighing a second round of semiconductor tariffs that would extend duties beyond chips to products built with them."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/hot-chips-2026-cerebras-lays-out-the-future-of-wafer-scale-ai-nexus-system-architecture-triples-rack-scale-performance-cs-6-wafer-to-incorporate-stacked-dram",
    "domain": "AI 算力 / 半导体",
    "title": "Hot Chips 2026: Cerebras lays out the future of wafer-scale AI — Nexus system architecture triples rack-scale performance, CS-6 wafer to incorporate stacked DRAM",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/hot-chips-2026-cerebras-lays-out-the-future-of-wafer-scale-ai-nexus-system-architecture-triples-rack-scale-performance-cs-6-wafer-to-incorporate-stacked-dram",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T15:59:18+00:00",
    "summary": "At Hot Chips 2026, Cerebras revealed the next two generations of its wafer-scale accelerator roadmap. It also discussed the benefits of its new Nexus rack design for the CS-4 rack-scale accelerator an"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/manufacturing/glass-substrate-roadmap-examined",
    "domain": "AI 算力 / 半导体",
    "title": "Glass substrate roadmaps examined — Absolics in final qualification and a first product that keeps slipping",
    "url": "https://www.tomshardware.com/tech-industry/manufacturing/glass-substrate-roadmap-examined",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T15:40:11+00:00",
    "summary": "Glass-core substrates, the replacement for organic chip packaging that Intel promised in September 2023, are now in final qualification but still not in a single commercial product"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-expects-to-sell-usd20-billion-worth-of-vera-rubin-hardware-this-quarter-would-account-for-20-percent-of-data-center-revenue-its-fastest-ramp-in-company-history",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia expects to sell $20 billion of Vera Rubin systems in Q3 as shipments begin — figure would account for 20% of its data center revenue mix, marks fastest ramp in company history",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-expects-to-sell-usd20-billion-worth-of-vera-rubin-hardware-this-quarter-would-account-for-20-percent-of-data-center-revenue-its-fastest-ramp-in-company-history",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T15:33:14+00:00",
    "summary": "Nvidia expects Vera Rubin to become its fastest-ramping data center AI platform as it projects sales of Vera Rubin hardware to hit 20% of data center revenue in its third fiscal quarter."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/samsungs-new-odyssey-g6-monitor-hits-a-ridiculous-1-100hz-refresh-rate-at-720p-displays-each-frame-for-less-than-a-millisecond",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung's new Odyssey G6 monitor hits a ridiculous 1,100Hz refresh rate at 720p — displays each frame for less than a millisecond",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/samsungs-new-odyssey-g6-monitor-hits-a-ridiculous-1-100hz-refresh-rate-at-720p-displays-each-frame-for-less-than-a-millisecond",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T15:29:53+00:00",
    "summary": "Ironically, the display with the four-digit refresh rate is actually the bottom of the display stack Samsung is showing off at Gamescom 2026."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/many-talks-between-data-center-developers-and-local-governments-are-under-nda-residents-question-the-needs-for-secrecy-but-developer-argues-its-important-to-avoid-running-afoul-of-insider-trading-rules",
    "domain": "AI 算力 / 半导体",
    "title": "Many talks between data center developers and local governments are wrapped in secrecy behind non-disclosure agreements — residents question the need for NDAs, but developers argue it’s important to a",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/many-talks-between-data-center-developers-and-local-governments-are-under-nda-residents-question-the-needs-for-secrecy-but-developer-argues-its-important-to-avoid-running-afoul-of-insider-trading-rules",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T15:06:53+00:00",
    "summary": "Researchers discovered that most negotiations between data centers and local governments are protected by NDAs. These documents keep details in secret, with residents having a difficult time finding i"
  },
  {
    "id": "rss:https://www.tomshardware.com/gift-guides-seasonal-sales/save-up-to-61-percent-on-gaming-pcs-laptops-and-more-in-hps-labor-day-2026-sale-huge-discounts-on-a-range-of-hardware-monitors-and-peripherals",
    "domain": "AI 算力 / 半导体",
    "title": "Save up to 61% on gaming PCs, laptops, and more in HP's Labor Day 2026 sale — huge discounts on a range of hardware, monitors, and peripherals",
    "url": "https://www.tomshardware.com/gift-guides-seasonal-sales/save-up-to-61-percent-on-gaming-pcs-laptops-and-more-in-hps-labor-day-2026-sale-huge-discounts-on-a-range-of-hardware-monitors-and-peripherals",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T14:24:56+00:00",
    "summary": "HP is hosting a Labor Day sale with up to 65% off our favorite tech products."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/macbooks/ingenious-indie-hacker-funds-usd3-000-macbook-purchase-by-selling-advertising-space-on-the-lid-sticker-space-auction-has-already-raised-111-percent-of-the-price-of-the-laptop",
    "domain": "AI 算力 / 半导体",
    "title": "Ingenious indie hacker funds $3,000 MacBook purchase by selling advertising space on the lid — sticker space auction has already raised 111% of the price of the laptop",
    "url": "https://www.tomshardware.com/laptops/macbooks/ingenious-indie-hacker-funds-usd3-000-macbook-purchase-by-selling-advertising-space-on-the-lid-sticker-space-auction-has-already-raised-111-percent-of-the-price-of-the-laptop",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T13:29:23+00:00",
    "summary": "An enterprising individual has successfully pre-sold enough advertisement sticker space on their dream MacBook’s lid to raise 111% of the laptop’s retail price."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/epa-faces-lawsuit-over-claims-it-fast-tracked-approval-of-toxic-data-center-chemicals-exposure-to-photoacid-generators-used-for-semiconductor-manufacturing-could-result-in-sudden-death-also-appear-to-be-long-lasting-pfas",
    "domain": "AI 算力 / 半导体",
    "title": "EPA faces lawsuit over claims it fast-tracked approval of toxic 'data center chemicals' — exposure to photoacid generators used for semiconductor manufacturing could result in ‘sudden death,’ also app",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/epa-faces-lawsuit-over-claims-it-fast-tracked-approval-of-toxic-data-center-chemicals-exposure-to-photoacid-generators-used-for-semiconductor-manufacturing-could-result-in-sudden-death-also-appear-to-be-long-lasting-pfas",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T13:10:57+00:00",
    "summary": "An environmental group said that two new chemicals approved by the EPA for semiconductor manufacturing do not come with enough safeguards, so they're suing the agency for 'turning the new chemical rev"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-to-buy-hugging-face-for-usd12-9-billion-report-claims-could-strengthen-nvidias-open-model-strategy-and-shore-up-position-against-rivals",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia to buy Hugging Face for $12.9 billion, report claims — could strengthen Nvidia's open-model strategy and shore up position against rivals",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-to-buy-hugging-face-for-usd12-9-billion-report-claims-could-strengthen-nvidias-open-model-strategy-and-shore-up-position-against-rivals",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T13:00:51+00:00",
    "summary": "Nvidia reportedly plans to buy Hugging Face at a price that exceeds its revenue by over 80 times, making it a major strategic investment in AI ecosystem."
  },
  {
    "id": "hn:49455507",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Announces Financial Results for Second Quarter Fiscal 2027",
    "url": "https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027",
    "source": "NewCzech",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-08-26T20:35:48+00:00",
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
    "id": "rss:https://www.eetimes.com/why-connectivity-has-become-an-edge-ai-design-decision/",
    "domain": "AI 算力 / 半导体",
    "title": "Why Connectivity Has Become an Edge AI Design Decision",
    "url": "https://www.eetimes.com/why-connectivity-has-become-an-edge-ai-design-decision/",
    "source": "Neeta Shenoy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T07:00:00+00:00",
    "summary": "Edge AI isn’t smart if its wireless link chokes; design compute, security, and Wi‑Fi 7 handoffs together from day one. The post Why Connectivity Has Become an Edge AI Design Decision appeared first on"
  },
  {
    "id": "rss:https://www.eetimes.com/nvme-2-4-update-adds-post-quantum-security-power-controls/",
    "domain": "AI 算力 / 半导体",
    "title": "NVMe 2.4 Update Adds Post-Quantum Security, Power Controls",
    "url": "https://www.eetimes.com/nvme-2-4-update-adds-post-quantum-security-power-controls/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T22:00:00+00:00",
    "summary": "NVMe 2.4 enhances security, power, virtualization, and management across cloud, AI, and enterprise workloads. The post NVMe 2.4 Update Adds Post-Quantum Security, Power Controls appeared first on EE T"
  },
  {
    "id": "rss:https://www.eetimes.com/reliable-power-path-design-integrating-mosfets-diodes-tvs-devices-and-capacitors/",
    "domain": "AI 算力 / 半导体",
    "title": "Reliable Power-Path Design: Integrating MOSFETs, Diodes, TVS Devices, and Capacitors",
    "url": "https://www.eetimes.com/reliable-power-path-design-integrating-mosfets-diodes-tvs-devices-and-capacitors/",
    "source": "Unikeyic.",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T13:00:00+00:00",
    "summary": "Design a reliable 24V power path, pick the right MOSFET, diode, TVS, and capacitor to handle surges, reverse polarity, and inrush current The post Reliable Power-Path Design: Integrating MOSFETs, Diod"
  },
  {
    "id": "rss:https://www.eetimes.com/why-automation-is-essential-to-achieve-eu-cra-compliance/",
    "domain": "AI 算力 / 半导体",
    "title": "Why Automation Is Essential to Achieve EU CRA Compliance",
    "url": "https://www.eetimes.com/why-automation-is-essential-to-achieve-eu-cra-compliance/",
    "source": "Colin Duggan, CEO and co-founder, BG Networks",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T13:00:00+00:00",
    "summary": "Discover how automation streamlines product-level conformity workflows to help manufacturers achieve EU Cyber Resilience Act compliance. The post Why Automation Is Essential to Achieve EU CRA Complian"
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
    "id": "hn:49468818",
    "domain": "大厂 AI 动态",
    "title": "Gemini-3.5-Transcribe",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/",
    "source": "k9294",
    "platform": "hackernews",
    "points": 356,
    "published_at": "2026-08-27T18:03:42+00:00",
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
    "id": "hn:49467922",
    "domain": "大厂 AI 动态",
    "title": "Gemini Omni 1.1 Flash",
    "url": "https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/",
    "source": "saretup",
    "platform": "hackernews",
    "points": 296,
    "published_at": "2026-08-27T17:06:32+00:00",
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
    "id": "rss:https://www.theverge.com/tech/986364/google-search-ai-overviews-auto-expand",
    "domain": "大厂 AI 动态",
    "title": "Google further buries search results under AI mode",
    "url": "https://www.theverge.com/tech/986364/google-search-ai-overviews-auto-expand",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T22:48:11+00:00",
    "summary": "Google is now automatically expanding its AI search summaries at the top of the results page for some searches, as reported by Search Engine Roundtable. The change, when it kicks in, pushes the typica"
  },
  {
    "id": "rss:https://www.theverge.com/games/986337/xbox-ceo-asha-sharma-project-helix-family-of-devices",
    "domain": "大厂 AI 动态",
    "title": "Xbox CEO calls Project Helix a ‘family of devices’",
    "url": "https://www.theverge.com/games/986337/xbox-ceo-asha-sharma-project-helix-family-of-devices",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T22:03:13+00:00",
    "summary": "According to Xbox CEO Asha Sharma, Project Helix, which she announced in March as a codename for Microsoft's \"next generation console\" - phrasing that seemingly implied a singular device - will actual"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/985741/tcl-qm7l-belkin-thunderbolt-dock-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Save hundreds on a TCL mini-LED TV with quantum dots and high refresh rate",
    "url": "https://www.theverge.com/gadgets/985741/tcl-qm7l-belkin-thunderbolt-dock-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T17:03:07+00:00",
    "summary": "Amazon and Best Buy have the TCL QM7L mini-LED TV on sale for as low as $797.99 for the 55-inch model, a $200 discount from the usual price. We spotted scaling discounts on larger sizes as well, altho"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/986176/data-center-pollution-epa-rule-change-air-permit",
    "domain": "大厂 AI 动态",
    "title": "Trump’s EPA wants to let data centers hide their air pollution",
    "url": "https://www.theverge.com/ai-artificial-intelligence/986176/data-center-pollution-epa-rule-change-air-permit",
    "source": "Justine Calma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T16:28:40+00:00",
    "summary": "Just as new data centers face growing backlash from neighboring communities, the US Environmental Protection Agency (EPA) is about to make it harder for people to weigh in on any pollution those cente"
  },
  {
    "id": "rss:https://www.theverge.com/games/986197/nvidia-dlss-5-leak-ai",
    "domain": "大厂 AI 动态",
    "title": "DLSS 5 leaked and modders are putting Nvidia&#8217;s AI effects on everything",
    "url": "https://www.theverge.com/games/986197/nvidia-dlss-5-leak-ai",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T16:22:16+00:00",
    "summary": "Modders are trying out an unofficial version of Nvidia's DLSS 5 on Skyrim, Cyberpunk 2077, GTA V, and a bunch of other games after code for the AI upscaling tech appeared in an early-access build of N"
  },
  {
    "id": "rss:https://www.theverge.com/podcast/986145/m6-mac-mini-meta-settlement-gta-6-vergecast",
    "domain": "大厂 AI 动态",
    "title": "The iPhone Fold could make concerts even worse",
    "url": "https://www.theverge.com/podcast/986145/m6-mac-mini-meta-settlement-gta-6-vergecast",
    "source": "Jacob Kastrenakes",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T15:26:19+00:00",
    "summary": "You know the person blocking your view of the concert because their phone is swaying in the air, recording the entire thing? Get ready for the unfolded version of it. This week on The Vergecast, we di"
  },
  {
    "id": "rss:https://www.theverge.com/tech/986130/apple-tv-plus-price-hike",
    "domain": "大厂 AI 动态",
    "title": "Apple TV now costs $14.99 a month after its fourth price hike in four years",
    "url": "https://www.theverge.com/tech/986130/apple-tv-plus-price-hike",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T13:47:36+00:00",
    "summary": "Apple raised the price of its streaming service for new and current subscribers on Friday, bumping it up from $12.99 per month to $14.99, Deadline and Variety are reporting. An annual subscription now"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/983263/dark-matter-season-2-review-apple-tv",
    "domain": "大厂 AI 动态",
    "title": "Apple TV’s sci-fi thriller Dark Matter gets even trippier in season 2",
    "url": "https://www.theverge.com/entertainment/983263/dark-matter-season-2-review-apple-tv",
    "source": "Andrew Webster",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T12:00:00+00:00",
    "summary": "Confusion is a generally accepted side effect of mystery box shows. They slather on secrets with the promise of a satisfying payoff in the end, and sometimes the cast and crew even have a hard time fo"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/985947/anthropic-supply-chain-risk-lawsuit-judge-ruling",
    "domain": "大厂 AI 动态",
    "title": "Anthropic was illegally blacklisted by the Trump administration, court rules",
    "url": "https://www.theverge.com/ai-artificial-intelligence/985947/anthropic-supply-chain-risk-lawsuit-judge-ruling",
    "source": "Hayden Field",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T03:14:06+00:00",
    "summary": "On Thursday, a judge ruled that the Pentagon's blacklisting of Anthropic earlier this year was unconstitutional, delivering the AI lab a win in a monthslong rollercoaster of a battle with the Trump ad"
  },
  {
    "id": "rss:https://www.theverge.com/games/985910/grand-theft-auto-gta-vi-extended-look-youtube-netflix-stream",
    "domain": "大厂 AI 动态",
    "title": "The GTA VI ‘extended look’ is now streaming on YouTube",
    "url": "https://www.theverge.com/games/985910/grand-theft-auto-gta-vi-extended-look-youtube-netflix-stream",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T01:05:18+00:00",
    "summary": "Rockstar has officially published its \"extended look\" at Grand Theft Auto VI on YouTube and on its website, as promised. The in-depth preview, which \"entirely\" features footage captured from the PS5 v"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/28/chinese-automakers-are-following-teslas-bet-that-robots-are-the-next-big-profit-machine/",
    "domain": "大厂 AI 动态",
    "title": "Chinese automakers are following Tesla’s bet that robots are the next big profit machine",
    "url": "https://techcrunch.com/2026/08/28/chinese-automakers-are-following-teslas-bet-that-robots-are-the-next-big-profit-machine/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T23:24:27+00:00",
    "summary": "Technical progress has encouraged a new batch of companies to jump in on the promise of profits from humanoid robots. And they're all Chinese automakers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/28/is-the-best-way-to-watch-a-movie-on-a-pair-of-sunglasses/",
    "domain": "大厂 AI 动态",
    "title": "Is the best way to watch a movie on a pair of sunglasses?",
    "url": "https://techcrunch.com/2026/08/28/is-the-best-way-to-watch-a-movie-on-a-pair-of-sunglasses/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T22:42:48+00:00",
    "summary": "Are XREAL's smart glasses the way of the future for home entertainment?"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/28/neocloud-lambda-secures-1b-in-debt-to-buy-more-chips/",
    "domain": "大厂 AI 动态",
    "title": "Neocloud Lambda secures $1B in debt to buy more chips",
    "url": "https://techcrunch.com/2026/08/28/neocloud-lambda-secures-1b-in-debt-to-buy-more-chips/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T20:24:11+00:00",
    "summary": "Neocloud Lambda has raised $1B in private debt to buy Nvidia AI chips and lease them to Microsoft. It's the latest in a string of loans, underscoring the high cost of the AI boom."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/28/an-anthropic-researcher-just-gave-us-a-peek-at-self-improving-ai/",
    "domain": "大厂 AI 动态",
    "title": "An Anthropic researcher just gave us a peek at self-improving AI",
    "url": "https://techcrunch.com/2026/08/28/an-anthropic-researcher-just-gave-us-a-peek-at-self-improving-ai/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T19:30:38+00:00",
    "summary": "Given 10 benchmarks for specific misaligned behaviors, the automated systems were able to improve performance on every single one without degrading overall performance."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/28/braves-browser-one-ups-chrome-with-its-new-support-for-email-aliases/",
    "domain": "大厂 AI 动态",
    "title": "Brave’s browser one-ups Chrome with its new support for email aliases",
    "url": "https://techcrunch.com/2026/08/28/braves-browser-one-ups-chrome-with-its-new-support-for-email-aliases/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T18:50:00+00:00",
    "summary": "The feature, announced this week, allows Brave's users to sign up for websites and other online services without having to share their personal email addresses."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/28/open-weight-ai-companies-are-the-valleys-hottest-acquisition-targets/",
    "domain": "大厂 AI 动态",
    "title": "Open-weight AI companies are the Valley’s hottest acquisition targets",
    "url": "https://techcrunch.com/2026/08/28/open-weight-ai-companies-are-the-valleys-hottest-acquisition-targets/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T18:19:40+00:00",
    "summary": "There's a lot of capital pouring into the business of giving models away."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/28/how-sweden-built-one-of-europes-hottest-startup-ecosystems/",
    "domain": "大厂 AI 动态",
    "title": "How Sweden built one of Europe’s hottest startup ecosystems",
    "url": "https://techcrunch.com/2026/08/28/how-sweden-built-one-of-europes-hottest-startup-ecosystems/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T17:09:05+00:00",
    "summary": "Sophia Bendz, general partner at Cherry Ventures, stopped by Equity to break down the latest in the Swedish tech ecosystem."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/28/more-americans-oppose-police-license-plate-cameras-than-support-them-survey/",
    "domain": "大厂 AI 动态",
    "title": "More Americans oppose police license plate cameras than support them: survey",
    "url": "https://techcrunch.com/2026/08/28/more-americans-oppose-police-license-plate-cameras-than-support-them-survey/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T15:57:58+00:00",
    "summary": "The backlash against license plate readers comes amid a wave of police abuses of surveillance cameras."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/28/friend-focused-photo-sharing-app-retro-snags-21m/",
    "domain": "大厂 AI 动态",
    "title": "Friend-focused photo-sharing app Retro snags $21M",
    "url": "https://techcrunch.com/2026/08/28/friend-focused-photo-sharing-app-retro-snags-21m/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T15:35:03+00:00",
    "summary": "Retro, a friend-focused photo-sharing app built by former Instagram employees, has raised more than $21 million in Series A funding."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/28/apple-tv-is-raising-its-subscription-prices-again/",
    "domain": "大厂 AI 动态",
    "title": "Apple TV is raising its subscription prices again",
    "url": "https://techcrunch.com/2026/08/28/apple-tv-is-raising-its-subscription-prices-again/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T14:36:48+00:00",
    "summary": "Now, Apple TV subscriptions will cost $14.99 per month, up from its previous price of $12.99 per month."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/28/a16z-creates-a-1-1b-machine-age-fund-to-accelerate-the-physical-buildout-of-ai/",
    "domain": "大厂 AI 动态",
    "title": "a16z creates a $1.1B ‘Machine Age’ fund to ‘accelerate the physical buildout of AI’",
    "url": "https://techcrunch.com/2026/08/28/a16z-creates-a-1-1b-machine-age-fund-to-accelerate-the-physical-buildout-of-ai/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T13:24:43+00:00",
    "summary": "The firm, known for its focus on software, is going to start throwing more money at the hardware behind AI."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/28/anthropic-gets-its-first-court-win-over-the-pentagons-supply-chain-risk-label/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic gets its first court win over the Pentagon’s supply-chain risk label",
    "url": "https://techcrunch.com/2026/08/28/anthropic-gets-its-first-court-win-over-the-pentagons-supply-chain-risk-label/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T12:46:12+00:00",
    "summary": "A federal judge ruled the Trump administration illegally labeled Anthropic a supply-chain risk, handing the AI company a victory as its second Pentagon lawsuit continues in Washington."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/28/meta-executive-leaves-for-openai-as-the-social-media-giant-faces-growing-scrutiny-in-india/",
    "domain": "大厂 AI 动态",
    "title": "Meta executive leaves for OpenAI as the social media giant faces growing scrutiny in India",
    "url": "https://techcrunch.com/2026/08/28/meta-executive-leaves-for-openai-as-the-social-media-giant-faces-growing-scrutiny-in-india/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T12:21:06+00:00",
    "summary": "Sandhya Devanathan will oversee some OpenAI operations across Southeast Asia and Australia in her new role."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/28/as-electric-two-wheelers-gain-a-foothold-belgian-startup-any-bets-on-cargo-space/",
    "domain": "大厂 AI 动态",
    "title": "As electric two-wheelers gain a foothold, Belgian startup Any bets on cargo space",
    "url": "https://techcrunch.com/2026/08/28/as-electric-two-wheelers-gain-a-foothold-belgian-startup-any-bets-on-cargo-space/",
    "source": "Anna Heim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T09:33:00+00:00",
    "summary": "Launched by Belgian startup Any, LUV1 is a modular electric motorcycle with 120 liters of cargo space that can be used to carry bags, work equipment, or even pets."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/27/ai-athletes-and-keith-rabois-strictlyvc-is-back-in-new-york-on-september-10/",
    "domain": "大厂 AI 动态",
    "title": "AI, athletes, and Keith Rabois: StrictlyVC is back in New York on September 10",
    "url": "https://techcrunch.com/2026/08/27/ai-athletes-and-keith-rabois-strictlyvc-is-back-in-new-york-on-september-10/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T02:02:44+00:00",
    "summary": "A boutique StrictlyVC evening returns to New York's West Village on September 10 with Keith Rabois, Craig Shapiro, Jason Levien, Tristan Walker, Brynn Putnam, and Deven Parekh — covering AI, sports in"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/27/anthropic-and-openai-are-joining-the-ai-stage-at-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic and OpenAI are joining the AI stage at TechCrunch Disrupt 2026",
    "url": "https://techcrunch.com/2026/08/27/anthropic-and-openai-are-joining-the-ai-stage-at-techcrunch-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T23:16:45+00:00",
    "summary": "At TechCrunch Disrupt 2026, the AI Stage is back to dig into the single hottest topic in the community for the past few years, presented by Google for Startups."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/27/rivians-cfo-is-leaving-the-company/",
    "domain": "大厂 AI 动态",
    "title": "Rivian’s CFO is leaving the company",
    "url": "https://techcrunch.com/2026/08/27/rivians-cfo-is-leaving-the-company/",
    "source": "Sean O'Kane, Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T20:23:10+00:00",
    "summary": "Claire McDonough is stepping down on October 30 to pursue a new opportunity, the company said in a filing on Thursday."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/27/bluesky-adds-an-algorithmic-opt-out-feature-for-those-who-dont-want-to-go-viral/",
    "domain": "大厂 AI 动态",
    "title": "Bluesky adds an ‘algorithmic opt-out’ feature for those who don’t want to go viral",
    "url": "https://techcrunch.com/2026/08/27/bluesky-adds-an-algorithmic-opt-out-feature-for-those-who-dont-want-to-go-viral/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T20:15:26+00:00",
    "summary": "Sometimes people just want to post to their followers, Bluesky says."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/27/buried-in-metas-18b-settlement-is-a-legal-pass-on-kids-data/",
    "domain": "大厂 AI 动态",
    "title": "Buried in Meta’s $18B settlement is a legal pass on kids’ data",
    "url": "https://techcrunch.com/2026/08/27/buried-in-metas-18b-settlement-is-a-legal-pass-on-kids-data/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T20:04:26+00:00",
    "summary": "Meta’s settlement with 29 states allows it to retain certain data from children under 13 to train and test age-detection models, highlighting a privacy trade-off built into the deal."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/27/youtube-now-lets-creators-tag-amazon-products-and-earn-commissions-from-purchases/",
    "domain": "大厂 AI 动态",
    "title": "YouTube now lets creators tag Amazon products and earn commissions from purchases",
    "url": "https://techcrunch.com/2026/08/27/youtube-now-lets-creators-tag-amazon-products-and-earn-commissions-from-purchases/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T19:54:28+00:00",
    "summary": "The update turns product recommendations into a more direct revenue stream for creators, and for Amazon, the move puts its massive online marketplace inside one of the most popular video platforms."
  },
  {
    "id": "rss:https://stratechery.com/2026/internet-hype-and-real-world-change/",
    "domain": "大厂 AI 动态",
    "title": "2026.35: Internet Hype and Real World Change",
    "url": "https://stratechery.com/2026/internet-hype-and-real-world-change/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T17:00:00+00:00",
    "summary": "The best Stratechery content from the week of August 24, 2026 including the breaker's advantage, the new battle for HDMI1, and how data center discourse ends."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/08/kalshi-cant-evade-nevada-gambling-laws-by-calling-bets-swaps-court-rules/",
    "domain": "大厂 AI 动态",
    "title": "Court rules Kalshi sports bets aren't \"swaps,\" just gambling with a different name",
    "url": "https://arstechnica.com/tech-policy/2026/08/kalshi-cant-evade-nevada-gambling-laws-by-calling-bets-swaps-court-rules/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T22:14:52+00:00",
    "summary": "Kalshi can't evade Nevada gambling laws by calling bets \"swaps,\" judges rule."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/08/cities-terminate-flock-contracts-at-record-pace-in-august/",
    "domain": "大厂 AI 动态",
    "title": "Cities terminate Flock contracts at record pace in August",
    "url": "https://arstechnica.com/tech-policy/2026/08/cities-terminate-flock-contracts-at-record-pace-in-august/",
    "source": "Cyrus Farivar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T21:33:54+00:00",
    "summary": "Cancellations have accelerated."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/08/rfk-jr-has-lied-to-the-senate-lawmakers-call-for-criminal-probe-ouster/",
    "domain": "大厂 AI 动态",
    "title": "\"RFK Jr. has lied to the Senate\": Lawmakers call for criminal probe, ouster",
    "url": "https://arstechnica.com/health/2026/08/rfk-jr-has-lied-to-the-senate-lawmakers-call-for-criminal-probe-ouster/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T21:17:38+00:00",
    "summary": "RFK Jr. went to Samoa to spread vaccine fears. The measles outbreak after killed 83."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/08/trump-blacklisting-of-woke-anthropic-deemed-illegal-by-federal-judge/",
    "domain": "大厂 AI 动态",
    "title": "Trump blacklisting of \"woke\" Anthropic deemed illegal by federal judge",
    "url": "https://arstechnica.com/tech-policy/2026/08/trump-blacklisting-of-woke-anthropic-deemed-illegal-by-federal-judge/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T18:07:55+00:00",
    "summary": "Anthropic refused to support lethal autonomous warfare and mass surveillance."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/08/trump-calls-for-creation-of-a-space-academy-to-train-future-nasa-leaders/",
    "domain": "大厂 AI 动态",
    "title": "Here's what we know about the \"space academy\" Trump just announced",
    "url": "https://arstechnica.com/space/2026/08/trump-calls-for-creation-of-a-space-academy-to-train-future-nasa-leaders/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T17:36:30+00:00",
    "summary": "\"It's called the US Space Academy. That's a big deal.\""
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/08/apple-one-and-apple-tv-subscription-prices-increase-by-up-to-20-percent/",
    "domain": "大厂 AI 动态",
    "title": "Apple One and Apple TV subscription prices increase by up to 20 percent",
    "url": "https://arstechnica.com/gadgets/2026/08/apple-one-and-apple-tv-subscription-prices-increase-by-up-to-20-percent/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T17:23:53+00:00",
    "summary": "Annual Apple TV subscriptions get the biggest bump."
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/08/our-10-favorite-scenes-from-t2-judgment-day/",
    "domain": "大厂 AI 动态",
    "title": "Our 10 favorite scenes from T2: Judgment Day",
    "url": "https://arstechnica.com/culture/2026/08/our-10-favorite-scenes-from-t2-judgment-day/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T16:44:47+00:00",
    "summary": "James Cameron's 1991 sci-fi blockbuster returns to theaters this weekend for its 35th anniversary."
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
    "id": "hn:49468651",
    "domain": "股票",
    "title": "US Patriot missile stocks in Europe are 'beyond critical' due to Iran war",
    "url": "https://apnews.com/article/patriot-missiles-iran-war-russia-ukraine-trump-09c7d8030a2e11fbd8ee3f7176b3f2d4",
    "source": "hn_acker",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-08-27T17:54:03+00:00",
    "summary": ""
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
    "id": "wscn:3780635",
    "domain": "股票",
    "title": "存款降本红利渐薄 齐鲁银行对公「压舱石」迎战零售风险出清",
    "url": "https://wallstreetcn.com/articles/3780635",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T08:59:10+00:00",
    "summary": "8月28日，齐鲁银行公布的2026年半年度报告显示，公司期内实现营业收入74.97亿元，同比增长10..."
  },
  {
    "id": "wscn:3780634",
    "domain": "股票",
    "title": "井英科技吴高明：AI视频，终局是编剧中心制",
    "url": "https://wallstreetcn.com/articles/3780634",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T08:51:57+00:00",
    "summary": "今年一季度中国新上线12.8万部微短剧，AI占比超95%，月活7.18亿、人均日刷129分钟。井英科技联合创始人吴高明认为，后期、表演、导演会被AI逐步接管，但编剧依赖的隐性知识——对人心的直觉和对世界的体验——未被结构化，模型学不到。"
  },
  {
    "id": "wscn:3780632",
    "domain": "股票",
    "title": "AI利润格局：模型公司每100美元收入，35-40美元流向云厂，为其带来10-20美元营业利润",
    "url": "https://wallstreetcn.com/articles/3780632",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T08:51:47+00:00",
    "summary": "巴克莱拆解AI行业利润链条：AI实验室付费推理利润率从2025年的十几个百分点飙升至50%-65%以上，API利润率或超80%，企业级需求和agentic工作流是主因。业务组合差异（API vs 订阅为主）可导致不同实验室毛利率相差17个百分点。行业收入预计从2024年70亿美元增至2028年6900亿美元，训练成本占比将从96%降至30%，2028年后自建基础设施项目或将削弱三大云厂商的市场份额"
  },
  {
    "id": "wscn:3780633",
    "domain": "股票",
    "title": "付息负债成本压降39BP，民生银行的存量风险消化与息差重构",
    "url": "https://wallstreetcn.com/articles/3780633",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T08:22:17+00:00",
    "summary": "在银行业普遍面临息差收窄压力的背景下，民生银行交出了一份资产负债结构调整的半年报。\n数据显示，202..."
  },
  {
    "id": "wscn:3780623",
    "domain": "股票",
    "title": "“竞争格局缓和”下的美团：本地商业利润率远超预期，新业务亏损收窄",
    "url": "https://wallstreetcn.com/articles/3780623",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T07:16:40+00:00",
    "summary": "外卖是利润改善的主要来源。高盛分析认为，外卖UE恢复、配送补贴正常化和营销效率提升共同推动了利润改善。"
  },
  {
    "id": "wscn:3780631",
    "domain": "股票",
    "title": "存款降本撑起息差回升，华夏银行半年减值计提大增58%拖累利润",
    "url": "https://wallstreetcn.com/articles/3780631",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T06:42:12+00:00",
    "summary": "在商业银行普遍面临盈利压力的背景下，华夏银行最新披露的2026年半年度报告呈现出较为复杂的损益结构。..."
  },
  {
    "id": "wscn:3780464",
    "domain": "股票",
    "title": "如果mRNA腾飞，未来哪些上游需求会爆发增长？",
    "url": "https://wallstreetcn.com/premium/articles/3780464?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T06:21:19+00:00",
    "summary": "单患者全流程测序及检测支出约2.33万美元，其中治疗后MRD监测1.75万美元为最大增量来源。"
  },
  {
    "id": "wscn:3780629",
    "domain": "股票",
    "title": "沃什“放鹰”，高盛依旧不信“9月加息”、摩根大通称“还是要看8月非农和CPI”",
    "url": "https://wallstreetcn.com/articles/3780629",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T05:21:40+00:00",
    "summary": "摩根大通维持12月加息的基准预测，经济学家Michael Feroli称，决定9月会议结果的\"更重要的消息\"是即将公布的8月非农就业和CPI报告。高盛预计8月核心CPI和核心PCE环比涨幅均在0.2%左右，按此路径FOMC将按兵不动。"
  },
  {
    "id": "wscn:3780628",
    "domain": "股票",
    "title": "半年核销处置逼近去年全年，光大银行上半年净利下滑24%",
    "url": "https://wallstreetcn.com/articles/3780628",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T04:37:58+00:00",
    "summary": "光大银行于8月28日晚间披露了2026年半年度报告。\n在商业银行普遍面临经营压力的背景下，这份中报呈..."
  },
  {
    "id": "wscn:3780626",
    "domain": "股票",
    "title": "付鹏点评杰克逊霍尔会议：上有本森特，下有凯文沃什【付鹏说图表】",
    "url": "https://wallstreetcn.com/premium/articles/3780626?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T04:16:29+00:00",
    "summary": "美联储管通胀和短端，财政部管融资和长端"
  },
  {
    "id": "wscn:3780625",
    "domain": "股票",
    "title": "全球首发，雷军点赞！长鑫官宣LPDDR6内存量产",
    "url": "https://wallstreetcn.com/articles/3780625",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T04:02:43+00:00",
    "summary": "长鑫率先量产落地LPDDR6，意味着中国存储企业首次在高端内存标准上，打破海外厂商长期垄断产品先发的局面，实现全球首发量产的历史性跨越。"
  },
  {
    "id": "wscn:3780624",
    "domain": "股票",
    "title": "瑞银详解宇树科技：人形机器人整机先行者，“小脑”与本体技术领先",
    "url": "https://wallstreetcn.com/articles/3780624",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T03:36:03+00:00",
    "summary": "现在，宇树已证明自己能造出最好的\"身体\"。接下来的问题只有一个——这副身体能不能装上一颗真正聪明的\"大脑\"。"
  },
  {
    "id": "wscn:3780487",
    "domain": "股票",
    "title": "连续两次加息！AI繁荣逼韩国央行抢跑，10月步伐是否放缓？",
    "url": "https://wallstreetcn.com/premium/articles/3780487?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T02:05:45+00:00",
    "summary": "AI繁荣推动韩国经济超预期复苏，连续加息以抑制AI驱动的需求通胀，10月或将暂停，但本轮紧缩尚未结束。"
  },
  {
    "id": "wscn:3780621",
    "domain": "股票",
    "title": "“世纪运河”开通在即，江海联运如何改变中国与东盟",
    "url": "https://wallstreetcn.com/articles/3780621",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T02:03:19+00:00",
    "summary": "平陆运河的建设开通，将让世界进一步分享中国发展机遇：首先，各国商品将以更便利的物流方式进入中国大市场；其次，运河将极大提升区域内互联互通，加快贸易投资便利化，促进中国与东盟、中国与世界的一体化；最后，作为向新、向绿、向智的样板工程，这条运河将为中国与新兴经济体注入发展新动能。"
  },
  {
    "id": "wscn:3780616",
    "domain": "股票",
    "title": "伊朗总统称“若霍尔木兹海峡重开，美国必须履行其义务”，军方强调“船只未经协调不得通过”",
    "url": "https://wallstreetcn.com/articles/3780616",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T01:47:37+00:00",
    "summary": "伊朗总统强调，伊朗目前正在努力确保，如果该航道在特定框架下重新开放，美国也必须履行其义务。另外伊朗已下令，所有未经伊朗协调而试图通过霍尔木兹海峡的船只均不得通行。革命卫队海军表示，这一行动将持续进行，直至美国对伊朗的军事行动彻底终结并履行其应尽的义务。"
  },
  {
    "id": "wscn:3780604",
    "domain": "股票",
    "title": "1个月960亿美元创纪录干预后，日元跌破160“回到干预前水平”",
    "url": "https://wallstreetcn.com/articles/3780604",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T01:45:22+00:00",
    "summary": "沃什周五表态将坚定实现通胀目标，提振美元走强，日元一度下跌0.5%至160.16。分析指出，160失守将推高再度干预预期，但鉴于原因是美元走强及美国利率上行，当局或将保持一定观望。贝森特回函民主党参议员Warren，为上月日元干预辩护，指出日元失序可能引发日本被迫抛售美债，最终推高美国家庭和企业的借贷成本。"
  },
  {
    "id": "wscn:3780619",
    "domain": "股票",
    "title": "沃什“杰克逊霍尔”讲完，美联储9月“不加也得加”？",
    "url": "https://wallstreetcn.com/articles/3780619",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T01:29:57+00:00",
    "summary": "市场迅速计入加息预期。两年期美债收益率跳升12个基点至4.35%，为6月首场新闻发布会以来最大单日涨幅，也是2010年以来杰克逊霍尔期间最大波动；美元走强，黄金回落。联邦基金期货显示9月加息概率从讲话前约35%升破50%，年内至少一次加息几乎被完全定价。巴克莱和法国兴业银行当日调整预测，预计9月和12月各加息25个基点。"
  },
  {
    "id": "wscn:3780618",
    "domain": "股票",
    "title": "特朗普宣布与委内瑞拉达成石油协议，称获逾650亿桶储量\"多数控制权\"",
    "url": "https://wallstreetcn.com/articles/3780618",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T00:58:30+00:00",
    "summary": "特朗普将该协议称为\"世界历史上最大的石油交易\"，并强调协议对美国纳税人\"零成本\"。"
  },
  {
    "id": "wscn:3780620",
    "domain": "股票",
    "title": "“三箭齐发”，中国住房金融制度迎来划时代变革",
    "url": "https://wallstreetcn.com/articles/3780620",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T00:57:53+00:00",
    "summary": "未来能在桌上继续玩下去的，只有两类主体：一类是融资成本足够低、能扛住长周期的央国企；另一类是能在产品力、资产运营、资本化退出上建立壁垒的专业化房企。至于那套靠“卖楼花”滚雪球的高周转模式，它已经成为了历史。"
  },
  {
    "id": "wscn:3780614",
    "domain": "股票",
    "title": "美众议院下周二表决临时拨款法案，需获三分之二多数支持",
    "url": "https://wallstreetcn.com/articles/3780614",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T23:55:05+00:00",
    "summary": "此次表决的背景是美国联邦政府面临的资金到期压力。当前财年的联邦拨款将于9月30日到期，若国会未能在此前通过新的拨款法案或临时决议，联邦政府将面临部分停摆的风险。"
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
    "id": "hn:49415187",
    "domain": "金融",
    "title": "Nearly 3M Teslas recalled in China over hidden door handles",
    "url": "https://www.bbc.com/news/articles/c4g6ggdg030o",
    "source": "chicken-stew",
    "platform": "hackernews",
    "points": 120,
    "published_at": "2026-08-24T04:27:57+00:00",
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
    "id": "hn:49111879",
    "domain": "金融",
    "title": "Citadel Buys Situational Awareness's Stock Portfolio After Big Losses in AI",
    "url": "https://www.wsj.com/finance/citadel-buys-situational-awarenesss-stock-portfolio-after-big-losses-in-ai-5117159b",
    "source": "mudil",
    "platform": "hackernews",
    "points": 54,
    "published_at": "2026-07-30T16:00:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:49197127",
    "domain": "金融",
    "title": "Former Federal Prosecutors to Senate: Stop Confirming Election Deniers as Judges",
    "url": "https://abovethelaw.com/2026/08/former-federal-prosecutors-to-senate-stop-confirming-election-deniers-to-the-federal-bench/",
    "source": "hn_acker",
    "platform": "hackernews",
    "points": 49,
    "published_at": "2026-08-06T14:25:07+00:00",
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
    "id": "hn:49173576",
    "domain": "金融",
    "title": "Investors in Situational Awareness deserved to lose their shirts",
    "url": "https://www.economist.com/finance-and-economics/2026/08/04/investors-in-situational-awareness-deserved-to-lose-their-shirts",
    "source": "Anon84",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-08-04T19:18:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:49184251",
    "domain": "金融",
    "title": "Fed's Kashkari says 'now is the time to start slowly moving' rates up",
    "url": "https://www.cnbc.com/2026/08/05/feds-kashkari-says-now-is-the-time-to-start-slowly-moving-rates-up.html",
    "source": "mapping365",
    "platform": "hackernews",
    "points": 42,
    "published_at": "2026-08-05T15:24:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:49215292",
    "domain": "金融",
    "title": "Mykhailo Fedorov reveals struggle to secure Patriot missiles and Western support",
    "url": "https://www.uawire.org/former-ukrainian-defense-minister-mykhailo-fedorov-reveals-struggles-to-secure-patriot-missiles-and-western-support",
    "source": "greedo",
    "platform": "hackernews",
    "points": 38,
    "published_at": "2026-08-07T19:38:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:49157782",
    "domain": "金融",
    "title": "US Schools Are Ditching Chromebooks for MacBooks by the Thousands",
    "url": "https://finance.yahoo.com/technology/articles/us-schools-ditching-chromebooks-macbooks-233015401.html",
    "source": "thunderbong",
    "platform": "hackernews",
    "points": 36,
    "published_at": "2026-08-03T16:16:19+00:00",
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
    "id": "hn:49182971",
    "domain": "金融",
    "title": "OpenAI settles claims of discrimination against US workers for $3.2M",
    "url": "https://finance.yahoo.com/technology/ai/articles/openai-settles-claims-discrimination-against-221429616.html",
    "source": "declan_roberts",
    "platform": "hackernews",
    "points": 27,
    "published_at": "2026-08-05T13:57:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:49189030",
    "domain": "金融",
    "title": "A Fed official is asking whether AI is becoming 'too big to fail'",
    "url": "https://thenextweb.com/news/a-fed-official-is-asking-whether-ai-is-becoming-too-big-to-fail",
    "source": "cdrnsf",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-08-05T21:08:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:49214813",
    "domain": "金融",
    "title": "US Sold Euros to Save the Yen, Europe Found Out After",
    "url": "https://finance.yahoo.com/markets/currencies/articles/us-sold-euros-save-yen-033819315.html",
    "source": "amarcheschi",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-08-07T18:54:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:49114620",
    "domain": "金融",
    "title": "'Talk Is Cheap': Wall Street Delivers Harsh Verdict on Warsh Fed",
    "url": "https://www.bloomberg.com/news/articles/2026-07-30/-talk-is-cheap-wall-street-delivers-harsh-verdict-on-warsh-fed",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-07-30T19:33:17+00:00",
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
  }
]
```
