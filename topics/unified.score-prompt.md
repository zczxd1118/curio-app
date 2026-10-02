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

- 今日日期：`2026-10-02`
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
  "date": "2026-10-02",
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
    "points": 1922682,
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
    "points": 1600419,
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
    "points": 1353539,
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
    "points": 1301986,
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
    "points": 1104486,
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
    "points": 1046394,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1yorUYWEGD",
    "domain": "AI",
    "title": "普通人也可以看的 AI 编程指南 | Cursor 教程｜Cursor 使用技巧和思路｜如何免费使用 Cursor｜AI 编程",
    "url": "http://www.bilibili.com/video/av113786467981446",
    "source": "不正经的前端啊",
    "platform": "bilibili",
    "points": 945883,
    "published_at": "2025-01-07T10:01:48+00:00",
    "summary": "普通人也可以看的 AI 编程指南\n全网最详细的 Cursor 教程\nCursor 核心功能、使用技巧和思路\n如何免费白嫖 Cursor"
  },
  {
    "id": "bvid:BV1aeLqzUE6L",
    "domain": "AI",
    "title": "10分钟讲清楚 Prompt, Agent, MCP 是什么",
    "url": "http://www.bilibili.com/video/av114410228025650",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 893806,
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
    "points": 823760,
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
    "points": 700212,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1WBG9zgECp",
    "domain": "AI",
    "title": "史上最强 AI 编程工具免费啦！Cursor 保姆级使用教程！新手友好！看到就是赚到！｜ 集成 MCP ！",
    "url": "http://www.bilibili.com/video/av114426116120045",
    "source": "AfterShip",
    "platform": "bilibili",
    "points": 674213,
    "published_at": "2025-05-01T04:00:00+00:00",
    "summary": "相信你已经在网上刷到过不少的 AI 工具，但如果你让我推荐最值得我们每个人学习的一款 AI 工具，那绝对就是史上最强的 AI 编程工具 —— Cursor。为此，我们录制了一个保姆级的 Cursor 新手教程，在这里免费分享给大家。即使你是一个对 AI 完全 0 基础的新手小白，看完这个视频后，你也可以彻底了解 Cursor 这个软件，并知道如何从 0 到 1 用 Cursor 做出入门级的 AI"
  },
  {
    "id": "bvid:BV1aDMezREUj",
    "domain": "AI",
    "title": "Cursor使用教程，2小时玩转cursor，cursor无限续杯",
    "url": "http://www.bilibili.com/video/av114691716154833",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 591109,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV1ia9UBPESQ",
    "domain": "AI",
    "title": "在VScode中配置Claude Code并接入DeepSeek V4 Pro【oo唠嗑教程】",
    "url": "http://www.bilibili.com/video/av116487012549813",
    "source": "沉默的羔丸ovo",
    "platform": "bilibili",
    "points": 346640,
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
    "points": 303262,
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
    "points": 299732,
    "published_at": "2025-04-15T00:59:13+00:00",
    "summary": "MCP终极指南 - 带你深入掌握MCP（基础篇）\n\n时间轴：\n01:05 MCP简要介绍\n02:47 安装 MCP Host（Cline）\n03:15 配置 Cline 用的 API Key\n06:01 第一个 MCP 问题\n06:31 概念解释：MCP Server 和 Tool\n09:13 配置 MCP Server\n14:19 使用 MCP Server\n15:24 MCP 交互流程详解\n1"
  },
  {
    "id": "bvid:BV1X8oKBLEdj",
    "domain": "AI",
    "title": "一口气学会AI编程！3个月10万字超详细教学！【项目实操】【0基础教学】【自学教程】【AI编程】【vibecoding】",
    "url": "http://www.bilibili.com/video/av116436177523067",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 229725,
    "published_at": "2026-04-21T03:15:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料，领取方式：关注后 私信“ 1 ”就好！\n\n后面还会出【一口气学会AI漫剧 】【一口气学会AI Agent 】等系列！大家可以蹲蹲！"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 225027,
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
    "points": 192124,
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
    "points": 182490,
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
    "points": 158245,
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
    "points": 126990,
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
    "points": 100012,
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
    "points": 93877,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV143wwz6E8F",
    "domain": "AI",
    "title": "Claude code科研使用展示与思路分享（提速就靠Ai）",
    "url": "http://www.bilibili.com/video/av116211882920985",
    "source": "科研推土机",
    "platform": "bilibili",
    "points": 75862,
    "published_at": "2026-03-11T18:12:00+00:00",
    "summary": "本期给大家带来的是Claude在Vscode的科研应用演示与我最近的一些心得使用心得，科研速度嘎嘎提升。论文复现画图、数据分析就靠Claude code。这个课程也是科研推土机「系统管理文献课程2.0」学员催我更新的内容，希望能帮助到大家～，这个视频重点讲两个事情：\n1️⃣ 资料获取，free不用怀疑，我是良心可言博主，，关注我(GZTSHNR)～\n2️⃣ 展示如何在VS code实操应用clau"
  },
  {
    "id": "bvid:BV1XnuGzfEp7",
    "domain": "AI",
    "title": "让你手中的AI好用10倍！5个好玩实用的MCP推荐，让你不只会用AI搜索",
    "url": "http://www.bilibili.com/video/av114835262018810",
    "source": "田同学Tino",
    "platform": "bilibili",
    "points": 75579,
    "published_at": "2025-07-12T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1468g6DEWs",
    "domain": "AI",
    "title": "【全100集】(允许白嫖) 2026最全最细的AI教程零基础入门到精通，一周带你小白变大神！全程干货无废话！存下吧，少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av117115386404821",
    "source": "AI产品经理入门教程-",
    "platform": "bilibili",
    "points": 74677,
    "published_at": "2026-08-18T13:11:45+00:00",
    "summary": "【2026最新版AI教程零基础入门到精通｜配套学习路线+工具包+实战项目，看置顶评论自取】\n 本套教程专为零基础设计，从AI是什么到独立用AI解决实际问题，手把手带你系统走完从入门到精通的完整路径。 ✅ AI认知入门：什么是AI/大模型、它们能做什么不能做什么、别被营销话术忽悠\n✅ 核心技能掌握：提示词工程、多轮对话技巧、让AI稳定输出的方法论\n✅ 进阶能力突破：AI工作流搭建、智能体开发、多工具"
  },
  {
    "id": "bvid:BV1U8d8BzEUK",
    "domain": "AI",
    "title": "建议收藏 | 51万行源码真相，ClaudeCode架构深度解读，深度复盘四大约束架构与8大设计模式，揭秘工业级Agent如何解决上下文爆炸与成本失控",
    "url": "http://www.bilibili.com/video/av116413847044339",
    "source": "赋范课堂",
    "platform": "bilibili",
    "points": 71294,
    "published_at": "2026-04-16T10:20:18+00:00",
    "summary": "ClaudeCode源码深度解读，揭秘Agent真正的秘密武器：拆解51万行工程源码，解析四大约束架构与8种设计模式，掌握工业级Agent从Demo到可靠产品的核心演进路径，助你重塑AI开发底层思维。"
  },
  {
    "id": "bvid:BV1ApYD6KEkD",
    "domain": "AI",
    "title": "马斯克收购Cursor后，Cursor的性价比现在已经爆表",
    "url": "http://www.bilibili.com/video/av117254955993228",
    "source": "jopatk",
    "platform": "bilibili",
    "points": 57161,
    "published_at": "2026-09-11T23:19:58+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1YJ336EEBk",
    "domain": "AI",
    "title": "【AI陪玩】开袋即食的AI接入我的世界教程！",
    "url": "http://www.bilibili.com/video/av116981806143216",
    "source": "万昇Dwin",
    "platform": "bilibili",
    "points": 55925,
    "published_at": "2026-07-26T01:30:00+00:00",
    "summary": "模组：Numen\n项目地址：https://github.com/Dwinovo/minecraft-numen"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 55641,
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
    "points": 52207,
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
    "points": 48849,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1wqeb6gEDY",
    "domain": "AI",
    "title": "Claude Code 百分百不封号",
    "url": "http://www.bilibili.com/video/av117297150694473",
    "source": "DUNHKPcc",
    "platform": "bilibili",
    "points": 46935,
    "published_at": "2026-09-19T10:14:15+00:00",
    "summary": "如果需要文档，私信主播，主页送免费的token，文件在群里 Q群1124987353"
  },
  {
    "id": "bvid:BV1z2Yw6sEgB",
    "domain": "AI",
    "title": "这就是最强性能的MC服务器！Mac Mini M6！",
    "url": "http://www.bilibili.com/video/av117362917382346",
    "source": "脏小豆",
    "platform": "bilibili",
    "points": 46361,
    "published_at": "2026-10-01T02:00:00+00:00",
    "summary": "无广！无广！无广！\n是性能最强的MC服务器，但是性价比不高！"
  },
  {
    "id": "bvid:BV1xra169EjN",
    "domain": "AI",
    "title": "GPT-6.1 Sol 扩容；Claude Code 推出 Mods 支持【AI 早报 2026-10-02】",
    "url": "http://www.bilibili.com/video/av117368839735122",
    "source": "橘鸦Juya",
    "platform": "bilibili",
    "points": 37277,
    "published_at": "2026-10-02T02:08:48+00:00",
    "summary": "文字版及相关链接请看：https://daily.juya.uk/issues/2026-10-02/"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 30834,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV1kRW3zmEv8",
    "domain": "AI",
    "title": "【即梦AI】即梦Agent杀疯了！8种玩法带你速通即梦Agent智能体模式，赶紧来学！",
    "url": "http://www.bilibili.com/video/av115229962798190",
    "source": "WorkBuddy教程丶",
    "platform": "bilibili",
    "points": 30575,
    "published_at": "2025-09-19T08:17:20+00:00",
    "summary": "即梦手册、AI绘画资料、系统学习AIGC请戳：https://www.bilibili.com/read/cv41224312"
  },
  {
    "id": "bvid:BV15wRwBwE79",
    "domain": "AI",
    "title": "小白AI做产品的唯一正确姿势！VS Code + Claude Code 王炸组合！",
    "url": "http://www.bilibili.com/video/av116510752250797",
    "source": "PM刘搞定",
    "platform": "bilibili",
    "points": 28251,
    "published_at": "2026-05-04T01:10:00+00:00",
    "summary": "你是不是也被网上铺天盖地的 “Vibecoding” 爽文给骗了？\n\n以为只要随便跟 AI 许个愿，它就能帮你直接写出一个爆款应用？\n\n现实却是：一顿操作猛如虎，一看代码原地杵。AI 瞎改一通，越改 Bug 越多，几百个文件堆在一起像个垃圾场，折腾两天最后只能无奈烂尾。🤦‍♂️\n\n其实，Vibecoding 绝对不是凭感觉瞎聊，它的底层仍然是严谨的工程化思维！\n\n本期视频，搞定带你彻底摒弃“抽卡式"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 23547,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1XGaA6CEwe",
    "domain": "AI",
    "title": "【2026最新】Claude Code保姆级完整教程-最强AI助手！从入门到进阶，速通Claude Code！一个方法教你规避封号风险！【附教程文档安装包】",
    "url": "http://www.bilibili.com/video/av117325537810666",
    "source": "大模型小阳",
    "platform": "bilibili",
    "points": 23190,
    "published_at": "2026-09-24T10:36:14+00:00",
    "summary": "整理制作不易，大家记得点个关注，一键三连呀【点赞、收藏、转发】感谢支持~"
  },
  {
    "id": "bvid:BV1k73y6fEDx",
    "domain": "AI",
    "title": "【ClaudeCode】这绝对是b站讲的最好的Claude Code保姆级全套教程，2026最新版，包含所有干货！七天就能从小白到大神！学完即就业，玩转AI技术",
    "url": "http://www.bilibili.com/video/av117001821488596",
    "source": "爬虫逆向",
    "platform": "bilibili",
    "points": 21257,
    "published_at": "2026-07-29T07:25:00+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！"
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 19119,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1MAYd6sEZh",
    "domain": "AI",
    "title": "效率翻倍， 一次讲透AI Agent的用法和技巧",
    "url": "http://www.bilibili.com/video/av117258059847877",
    "source": "数码旭",
    "platform": "bilibili",
    "points": 18348,
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
    "points": 15448,
    "published_at": "2026-08-10T10:45:04+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1WCan6jEhS",
    "domain": "AI",
    "title": "Vps Claude 极低的封号风险",
    "url": "http://www.bilibili.com/video/av117352700122819",
    "source": "DUNHKPcc",
    "platform": "bilibili",
    "points": 12192,
    "published_at": "2026-09-29T05:39:03+00:00",
    "summary": "如果需要文档，私信主播，主页送免费的token，文件在群里 Q群1124987353"
  },
  {
    "id": "bvid:BV1Zka56QEsv",
    "domain": "AI",
    "title": "为了用上Claude，我被封了10个号｜网络、代充、KYC、苹果美区踩坑全记录",
    "url": "http://www.bilibili.com/video/av117349864708105",
    "source": "一唯光明故",
    "platform": "bilibili",
    "points": 11965,
    "published_at": "2026-09-28T17:34:14+00:00",
    "summary": "重度 AI 用户，工作全靠它：写报告、做 PPT、处理数据、写 Python 跑内网分析、写前端网页。\n为了用上 Claude，前前后后被封了不下 10 个号，这期把我踩过的坑一次讲清楚。"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 11760,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
  },
  {
    "id": "bvid:BV1TJh666Eua",
    "domain": "AI",
    "title": "【直播回放】2026唯一需要掌握的AI软件：Codex全流程实操教学",
    "url": "http://www.bilibili.com/video/av117309565831190",
    "source": "立得AI-阿真",
    "platform": "bilibili",
    "points": 11296,
    "published_at": "2026-09-22T03:00:00+00:00",
    "summary": "整理不易，需要知识库的小伙伴，三连后给后台回复“知识库”，看到了会第一时间发你哦"
  },
  {
    "id": "bvid:BV1EEM96uEPP",
    "domain": "AI",
    "title": "【逆向】掌握MCP功能使用修改分析，成为逆向高手！",
    "url": "http://www.bilibili.com/video/av117030460131623",
    "source": "009安乐",
    "platform": "bilibili",
    "points": 10811,
    "published_at": "2026-08-03T07:47:28+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV12MEg6pE9o",
    "domain": "AI",
    "title": "【乐鑫教程】乐鑫文档 MCP 服务器上线，现已支持微信登录！",
    "url": "http://www.bilibili.com/video/av116713957956440",
    "source": "乐鑫信息科技",
    "platform": "bilibili",
    "points": 9506,
    "published_at": "2026-06-08T10:17:31+00:00",
    "summary": "手把手教你如何使用最新乐鑫文档知识库，帮你在 Claude / Cursor 等平台解答问题、生成代码、迁移 ESP-IDF 版本、烧录固件。 MCP 服务器现已支持微信扫码一键登录，快来一试！\n\n视频重点内容包括👇：\n\n- 如何将 MCP 服务器添加到 VS Code\n- 让 Copilot 基于乐鑫文档对比旧版和最新版 I2C 驱动\n- 驱动迁移\n- Copilot 编译代码、烧录代码并监控输"
  },
  {
    "id": "hn:49872723",
    "domain": "AI 算力 / 半导体",
    "title": "Owed a billion dollars in Nvidia stock",
    "url": "https://colo.to/nvidia-stock-narrative.html",
    "source": "Eric_Gullichsen",
    "platform": "hackernews",
    "points": 1089,
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
    "points": 401,
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
    "points": 254,
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
    "points": 74,
    "published_at": "2026-10-01T20:36:47+00:00",
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
    "id": "rss:https://www.eetimes.com/manufacturing-intelligence-turning-eda-data-into-trusted-action/",
    "domain": "AI 算力 / 半导体",
    "title": "Manufacturing Intelligence: Turning EDA Data into Trusted Action",
    "url": "https://www.eetimes.com/manufacturing-intelligence-turning-eda-data-into-trusted-action/",
    "source": "Dr. Jim Shiely, Technical and strategic advisor, Siemens EDA",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T13:00:00+00:00",
    "summary": "Manufacturing intelligence connects EDA, TCAD and metrology to turn manufacturing evidence into trusted action, faster. The post Manufacturing Intelligence: Turning EDA Data into Trusted Action appear"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/mini-pcs/first-intel-panther-lake-mini-pc-cooled-with-solid-state-airjet-tech-operates-at-less-than-21-dba-aaeon-claims-its-fanless-up-xtreme-ptl-edge-air-is-also-slimmer-lighter-than-actively-cooled-rivals",
    "domain": "AI 算力 / 半导体",
    "title": "First Intel Panther Lake mini PC cooled with solid-state AirJet tech operates at less than 21 dBA",
    "url": "https://www.tomshardware.com/desktops/mini-pcs/first-intel-panther-lake-mini-pc-cooled-with-solid-state-airjet-tech-operates-at-less-than-21-dba-aaeon-claims-its-fanless-up-xtreme-ptl-edge-air-is-also-slimmer-lighter-than-actively-cooled-rivals",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T15:27:09+00:00",
    "summary": "Aaeon's UP Xtreme PTL Edge Air is the first Panther Lake mini PC we've seen with AirJet technology for ultra-low-noise active cooling."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-launches-open-agent-safety-platform-to-restrain-rogue-ai-agents-new-hardware-and-software-security-stack-can-quarantine-agents-in-milliseconds",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia launches Open Agent Safety Platform to physically restrain rogue AI agents",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-launches-open-agent-safety-platform-to-restrain-rogue-ai-agents-new-hardware-and-software-security-stack-can-quarantine-agents-in-milliseconds",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T14:30:00+00:00",
    "summary": "Nvidia’s new Open Agent Safety Platform combines OpenShell sandboxing with BlueField-powered Sentry hardware to monitor and rapidly quarantine rogue AI agents"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/ais-chipmaking-frontier-may-face-patent-infringement-hurdles-as-autonomous-tools-take-over-ai-can-spread-a-copied-design-or-infringed-patent-across-thousands-of-chips-before-anyone-notices-says-expert",
    "domain": "AI 算力 / 半导体",
    "title": "AI's chipmaking frontier may face patent infringement hurdles as autonomous tools take over",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/ais-chipmaking-frontier-may-face-patent-infringement-hurdles-as-autonomous-tools-take-over-ai-can-spread-a-copied-design-or-infringed-patent-across-thousands-of-chips-before-anyone-notices-says-expert",
    "source": "Chris Stokel-Walker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T14:20:00+00:00",
    "summary": "Can AI outsmart the ingenuity of human thinking and design? If so, what does that mean for proprietary IP? We explore the tools, and the potential pitfalls."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/deepseek-and-huawei-release-open-source-ascend-ai-programming-tools-to-reduce-reliance-on-nvidia-ecosystem-tools-include-compute-and-communication-libraries-as-well-as-ascend-support-for-tilelang",
    "domain": "AI 算力 / 半导体",
    "title": "DeepSeek and Huawei release open-source Ascend AI programming tools to reduce reliance on Nvidia ecosystem",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/deepseek-and-huawei-release-open-source-ascend-ai-programming-tools-to-reduce-reliance-on-nvidia-ecosystem-tools-include-compute-and-communication-libraries-as-well-as-ascend-support-for-tilelang",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T14:00:00+00:00",
    "summary": "DeepSeek and Huawei have released open-source programming tools for Ascend 950 AI chips, including compute and communication libraries, aimed at making Huawei hardware easier to program and optimize."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/maingears-new-program-offers-instant-trade-ins-for-gaming-pc-buyers-delivers-quotes-for-old-laptops-phones-tablets-smartwatches-headphones-cameras-lenses-and-microphones-in-minutes",
    "domain": "AI 算力 / 半导体",
    "title": "Maingear’s new program offers instant trade-ins for gaming PC buyers",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/maingears-new-program-offers-instant-trade-ins-for-gaming-pc-buyers-delivers-quotes-for-old-laptops-phones-tablets-smartwatches-headphones-cameras-lenses-and-microphones-in-minutes",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T13:45:00+00:00",
    "summary": "American custom and prebuilt computer seller Maingear has launched a new instant trade-in scheme through SELLIT9."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/get-over-70-percent-off-this-cherry-xtrfy-mx-3-1-wired-mechanical-gaming-keyboard-just-usd34-buys-a-quality-full-size-keeb-with-cherry-mx2a-switches",
    "domain": "AI 算力 / 半导体",
    "title": "Get over 70% off this Cherry Xtrfy MX 3.1 wired mechanical gaming keyboard",
    "url": "https://www.tomshardware.com/pc-components/get-over-70-percent-off-this-cherry-xtrfy-mx-3-1-wired-mechanical-gaming-keyboard-just-usd34-buys-a-quality-full-size-keeb-with-cherry-mx2a-switches",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T13:20:00+00:00",
    "summary": "Buy the full-size Cherry Xtrfy MX 3.1 mechanical gaming keyboard for only $34 with promo code WOOTCHERRY. That’s over 70% off, an all-time low, and new Woot customers can drop it $29"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/gears-of-war-e-day-is-an-uncharacteristically-cpu-heavy-unreal-engine-5-game-benchmarking-25-cpus-from-intel-and-amd-and-investigating-low-core-mode",
    "domain": "AI 算力 / 半导体",
    "title": "Gears of War E-Day is an uncharacteristically CPU-heavy Unreal Engine 5 game",
    "url": "https://www.tomshardware.com/pc-components/cpus/gears-of-war-e-day-is-an-uncharacteristically-cpu-heavy-unreal-engine-5-game-benchmarking-25-cpus-from-intel-and-amd-and-investigating-low-core-mode",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T13:00:00+00:00",
    "summary": "Gears of War E-Day is a surprisingly heavy Unreal Engine 5 game on the CPU. We benchmarked the game with 25 processors, as well as investigated what the “low core mode” actually does."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/gears-of-war-e-day-pc-graphics-performance-tested-43-gpus-take-us-back-to-the-start-of-an-iconic-saga",
    "domain": "AI 算力 / 半导体",
    "title": "Gears of War: E-Day PC graphics performance tested",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/gears-of-war-e-day-pc-graphics-performance-tested-43-gpus-take-us-back-to-the-start-of-an-iconic-saga",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T13:00:00+00:00",
    "summary": "Gears of War: E-Day is the first game to implement Unreal Engine's MegaLights technology, allowing for hundreds of dynamic ray-traced light sources in a scene. We put it to the test on 43 graphics car"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/hp-boards-the-macbook-neo-competitor-train-omnibook-5-comes-in-four-colors-with-wildcat-lake-and-starts-at-usd699-99",
    "domain": "AI 算力 / 半导体",
    "title": "HP boards the MacBook Neo competitor train",
    "url": "https://www.tomshardware.com/laptops/hp-boards-the-macbook-neo-competitor-train-omnibook-5-comes-in-four-colors-with-wildcat-lake-and-starts-at-usd699-99",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T13:00:00+00:00",
    "summary": "The new HP OmniBook 5 (14-inch) uses Wildcat Lake and a variety of colors to compete with the MacBook Neo."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/micron-projects-tightening-ram-shortages-through-2028-as-it-generates-record-profit-record-86-25-percent-gross-margin-drives-over-usd53-billion-in-quarterly-profit",
    "domain": "AI 算力 / 半导体",
    "title": "Micron projects tightening RAM shortages through 2028 as it generates record profit",
    "url": "https://www.tomshardware.com/pc-components/dram/micron-projects-tightening-ram-shortages-through-2028-as-it-generates-record-profit-record-86-25-percent-gross-margin-drives-over-usd53-billion-in-quarterly-profit",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T12:50:00+00:00",
    "summary": "Micron makes big money amid the NAND and DRAM shortage. Company expects supply crunch to continue through 2028."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/ps3-emulator-devs-warn-of-fake-blu-ray-drives-on-newegg-and-aliexpress-beware-of-fake-blu-ray-drives-devs-warn-retrogamers-scammers-use-spoofed-firmware-to-disguise-older-mechanisms-in-high-end-shells",
    "domain": "AI 算力 / 半导体",
    "title": "PS3 emulator devs warn of fake Blu-ray drives on Newegg and AliExpress",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/ps3-emulator-devs-warn-of-fake-blu-ray-drives-on-newegg-and-aliexpress-beware-of-fake-blu-ray-drives-devs-warn-retrogamers-scammers-use-spoofed-firmware-to-disguise-older-mechanisms-in-high-end-shells",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T12:30:00+00:00",
    "summary": "The developers of a leading PlayStation 3 emulator warn of 'a recent influx of fake Blu-ray drives.'"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-says-actors-linked-to-moonshot-ai-spearheaded-a-campaign-to-extract-its-models-hidden-reasoning-logged-attempts-peaked-at-16-000-users-over-two-days",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI says actors linked to China-based Moonshot AI spearheaded a campaign to extract its models’ hidden reasoning",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-says-actors-linked-to-moonshot-ai-spearheaded-a-campaign-to-extract-its-models-hidden-reasoning-logged-attempts-peaked-at-16-000-users-over-two-days",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T12:00:00+00:00",
    "summary": "OpenAI says operators copied its models’ encrypted reasoning and asked a model in a separate conversation to decrypt it."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/grab-a-huge-usd520-saving-on-this-rtx-5090-gaming-laptop-from-msi-with-64gb-ddr5-and-a-2tb-ssd-stealth-a18-ai-rig-ships-with-12-core-amd-ryzen-ai-9-cpu-along-with-an-18-inch-uhd-display-with-a-120hz-refresh-rate",
    "domain": "AI 算力 / 半导体",
    "title": "Grab a huge $520 saving on this RTX 5090 gaming laptop from MSI with 64GB DDR5 and a 2TB SSD",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/grab-a-huge-usd520-saving-on-this-rtx-5090-gaming-laptop-from-msi-with-64gb-ddr5-and-a-2tb-ssd-stealth-a18-ai-rig-ships-with-12-core-amd-ryzen-ai-9-cpu-along-with-an-18-inch-uhd-display-with-a-120hz-refresh-rate",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T11:40:00+00:00",
    "summary": "Pick up a $720 saving on this RTX 5090 MSI gaming laptop, featuring 64GB DDR5 RAM, 2TB SSD, and an AMD Ryzen AI 9 HX 370 CPU, now just $3,779."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/ai-agents-inadvertently-leak-13-000-internal-screenshots-from-organizations-list-of-companies-includes-fortune-500-and-a-frontier-ai-lab",
    "domain": "AI 算力 / 半导体",
    "title": "AI agents inadvertently leak 13,000+ internal screenshots from organizations",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/ai-agents-inadvertently-leak-13-000-internal-screenshots-from-organizations-list-of-companies-includes-fortune-500-and-a-frontier-ai-lab",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T11:30:00+00:00",
    "summary": "AI agents have been quietly uploading internal screenshots from over 300 companies to public GitHub repos, some of which contain sensitive information."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/micron-lawsuit-claims-chinese-memory-maker-ymtc-poached-its-engineers-then-sued-it-using-its-own-stolen-tech-ex-employees-hid-roles-on-linkedin-patented-micron-tech-and-won-a-german-injunction",
    "domain": "AI 算力 / 半导体",
    "title": "Micron lawsuit claims Chinese memory maker YMTC poached its engineers, then sued it using its own stolen tech",
    "url": "https://www.tomshardware.com/pc-components/ssds/micron-lawsuit-claims-chinese-memory-maker-ymtc-poached-its-engineers-then-sued-it-using-its-own-stolen-tech-ex-employees-hid-roles-on-linkedin-patented-micron-tech-and-won-a-german-injunction",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T11:00:00+00:00",
    "summary": "Micron files a lawsuit against Yangtze Memory, claims that some of the patents which YMTC uses against Micron in various courts were granted to former YMTC engineers who took crucial know-how from Mic"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/firm-rents-four-nvidia-h200s-to-test-80x-cheaper-deepseek-claim-usd13-200-monthly-gpu-rental-doubles-claude-bill-while-security-flaws-keep-code-offline",
    "domain": "AI 算力 / 半导体",
    "title": "Firm rents four Nvidia H200s to test '80x cheaper' DeepSeek claim",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/firm-rents-four-nvidia-h200s-to-test-80x-cheaper-deepseek-claim-usd13-200-monthly-gpu-rental-doubles-claude-bill-while-security-flaws-keep-code-offline",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T10:30:00+00:00",
    "summary": "A call center consultancy rented four Nvidia H200s to run DeepSeek V4.1 Flash for Claude Code and found DeepSeek's API cheaper."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/storage/sony-released-the-first-cd-audio-player-on-this-day-in-1982-player-cost-usd3-700-when-adjusted-for-inflation-but-it-would-be-another-decade-before-the-cd-rom-driven-multimedia-pc-era-began",
    "domain": "AI 算力 / 半导体",
    "title": "Sony released the first CD audio player on this day in 1982",
    "url": "https://www.tomshardware.com/pc-components/storage/sony-released-the-first-cd-audio-player-on-this-day-in-1982-player-cost-usd3-700-when-adjusted-for-inflation-but-it-would-be-another-decade-before-the-cd-rom-driven-multimedia-pc-era-began",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T10:22:30+00:00",
    "summary": "Sony launched the world’s first CD player on this day in 1982, kickstarting the compact disc digital audio era."
  },
  {
    "id": "rss:https://www.tomshardware.com/service-providers/web-hosting/kyiv-missile-strikes-take-out-popular-torrent-trackers-russo-ukrainian-war-temporarily-achieves-what-lawmakers-cant",
    "domain": "AI 算力 / 半导体",
    "title": "Russian missile strikes take out popular piracy websites",
    "url": "https://www.tomshardware.com/service-providers/web-hosting/kyiv-missile-strikes-take-out-popular-torrent-trackers-russo-ukrainian-war-temporarily-achieves-what-lawmakers-cant",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T10:00:00+00:00",
    "summary": "Over the last week, there have been reports that the Russian military has started targeting Ukraine's datacenters. As one commenter put it, \"DDoS now means Direct Destruction of Servers.\""
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/geekbench-7-results-suggest-openais-dots-agent-runs-on-nine-core-amd-epyc-vms-with-nearly-10gb-of-memory-newest-runs-score-about-six-times-meta-muse-in-multi-core",
    "domain": "AI 算力 / 半导体",
    "title": "Geekbench 7 results suggest OpenAI's dots run on nine-core AMD EPYC VMs",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/geekbench-7-results-suggest-openais-dots-agent-runs-on-nine-core-amd-epyc-vms-with-nearly-10gb-of-memory-newest-runs-score-about-six-times-meta-muse-in-multi-core",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T18:00:39+00:00",
    "summary": "Post-launch Geekbench 7 runs show Debian Linux instead of the leak's Ubuntu."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/policy/top-ai-tech-executives-promise-to-self-police-ai-development-nvidia-anthropic-openai-and-more-pledge-ai-labs-will-take-steps-to-build-a-positive-future",
    "domain": "AI 算力 / 半导体",
    "title": "Top AI tech executives promise to ‘self-police’ AI development",
    "url": "https://www.tomshardware.com/tech-industry/policy/top-ai-tech-executives-promise-to-self-police-ai-development-nvidia-anthropic-openai-and-more-pledge-ai-labs-will-take-steps-to-build-a-positive-future",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T17:27:37+00:00",
    "summary": "The heads of the biggest AI labs — Google, Anthropic, Meta, OpenAI, SpaceXAI, and Nvidia — went to Washington and signed the 'Joint Commitment on Frontier Responsibilities,' promising to develop their"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/marvels-wolverine-reaches-gameplay-with-kytyps5-emulator-ps5-exclusive-joins-ghost-of-yotei-in-reaching-gameplay-performance-still-in-single-digits",
    "domain": "AI 算力 / 半导体",
    "title": "Marvel's Wolverine reaches gameplay with KytyPS5 emulator",
    "url": "https://www.tomshardware.com/video-games/playstation/marvels-wolverine-reaches-gameplay-with-kytyps5-emulator-ps5-exclusive-joins-ghost-of-yotei-in-reaching-gameplay-performance-still-in-single-digits",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T17:00:00+00:00",
    "summary": "An experimental PS5 emulator has been shown running the brand-new Marvel's Wolverine game on a PC, with gameplay working for the first time."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/xbox/xbox-disc-to-digital-feature-rolls-out-to-all-xbox-players-to-enable-playing-disc-free-but-selling-your-media-revokes-access-hybrid-physical-media-plan-lands-as-sony-phases-out-discs-by-2028",
    "domain": "AI 算力 / 半导体",
    "title": "Xbox Disc to Digital feature rolls out to all Xbox players to enable playing disc-free, but selling your media revokes access",
    "url": "https://www.tomshardware.com/video-games/xbox/xbox-disc-to-digital-feature-rolls-out-to-all-xbox-players-to-enable-playing-disc-free-but-selling-your-media-revokes-access-hybrid-physical-media-plan-lands-as-sony-phases-out-discs-by-2028",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T16:40:00+00:00",
    "summary": "Xbox gamers can now get a digital license tied to their physical game discs associated with their Xbox profile for select titles, allowing them to play the game without needing to insert it into the c"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/new-ps5-relapse-jailbreak-enables-homebrew-and-switch-emulation-but-is-hamstrung-by-rapidly-changing-firmware-revisions-jailbreak-unlocks-firmware-13-60-but-newer-games-already-demand-firmware-14-00",
    "domain": "AI 算力 / 半导体",
    "title": "New PS5 Relapse jailbreak enables homebrew and Switch emulation but is hamstrung by rapidly-changing firmware revisions",
    "url": "https://www.tomshardware.com/video-games/playstation/new-ps5-relapse-jailbreak-enables-homebrew-and-switch-emulation-but-is-hamstrung-by-rapidly-changing-firmware-revisions-jailbreak-unlocks-firmware-13-60-but-newer-games-already-demand-firmware-14-00",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T16:20:00+00:00",
    "summary": "A new jailbreak supports firmware 7.00 through 13.60, including on the PS5 Pro. But some game updates may already require a newer firmware, breaking the jailbreak."
  },
  {
    "id": "rss:https://www.tomshardware.com/tag/ai-chip-design-week",
    "domain": "AI 算力 / 半导体",
    "title": "AI Chip Design Week",
    "url": "https://www.tomshardware.com/tag/ai-chip-design-week",
    "source": "The Editors of Tom&#039;s Hardware",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T16:02:34+00:00",
    "summary": "AI Chip Design Week"
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/routers/tp-link-opens-global-preorders-for-its-first-wi-fi-8-router-but-ban-keeps-it-out-of-us-market-us-left-off-launch-list-as-fcc-freeze-refuses-to-thaw",
    "domain": "AI 算力 / 半导体",
    "title": "TP-Link opens global preorders for its first Wi-Fi 8 router, but ban keeps it out of US market",
    "url": "https://www.tomshardware.com/networking/routers/tp-link-opens-global-preorders-for-its-first-wi-fi-8-router-but-ban-keeps-it-out-of-us-market-us-left-off-launch-list-as-fcc-freeze-refuses-to-thaw",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T15:43:47+00:00",
    "summary": "TP-Link's first Wi-Fi 8 product, the Archer 8 Ultra, is off limits in the U.S."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/save-60-percent-on-your-first-month-of-meshy-7-ai-streamline-your-3d-printing-workflow-for-less",
    "domain": "AI 算力 / 半导体",
    "title": "Save 60% on your first month of Meshy 7 AI — streamline your 3D printing workflow for less",
    "url": "https://www.tomshardware.com/3d-printing/save-60-percent-on-your-first-month-of-meshy-7-ai-streamline-your-3d-printing-workflow-for-less",
    "source": "Sponsored",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T15:00:00+00:00",
    "summary": "Use the exclusive TOMESHY60 discount code to slash 60% off your first month of Meshy 7."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-claims-popular-chinese-ai-model-has-mythos-class-hacking-abilities-frontier-red-teaming-report-details-weak-safeguards-on-open-weight-ai",
    "domain": "AI 算力 / 半导体",
    "title": "Anthropic claims popular Chinese AI model has Mythos-class hacking abilities",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-claims-popular-chinese-ai-model-has-mythos-class-hacking-abilities-frontier-red-teaming-report-details-weak-safeguards-on-open-weight-ai",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T14:40:00+00:00",
    "summary": "Anthropic has released a frontier red teaming report, claiming that Zhipu AI's GLM-5.3 has weak safeguarding, and can easily be used to generate harmful content."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/metas-muse-ai-agent-accused-of-accessing-sensitive-user-data-on-iphone-and-mac-without-permission-agent-shocks-reporter-by-referring-to-confidential-messages-it-wasnt-granted-access-to",
    "domain": "AI 算力 / 半导体",
    "title": "Meta's Muse AI agent accused of ignoring user permissions and accessing forbidden personal user data",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/metas-muse-ai-agent-accused-of-accessing-sensitive-user-data-on-iphone-and-mac-without-permission-agent-shocks-reporter-by-referring-to-confidential-messages-it-wasnt-granted-access-to",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T14:00:00+00:00",
    "summary": "Meta's Muse AI agent has been accused of ignoring user permissions and accessing forbidden personal user data on an iPhone and Mac, including iMessages."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/ibuypower-slate-gaming-desktop-review",
    "domain": "AI 算力 / 半导体",
    "title": "iBuyPower Slate Gaming Desktop review: Strong gaming value and extras",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/ibuypower-slate-gaming-desktop-review",
    "source": "Charles Jefferies",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T13:50:00+00:00",
    "summary": "The iBuyPower Slate pairs a Ryzen 7 7700X3D and RTX 5070 in a stylish RGB-equipped chassis, delivering strong gaming performance and surprising extras, though productivity performance trails some simi"
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/network-switches/grab-this-10-port-gigabit-poe-switch-with-up-to-60w-of-power-for-under-usd38-a-new-record-low-ugreen-switch-upgrades-your-home-network-with-eight-power-delivery-ports-for-cameras-and-wi-fi-extenders",
    "domain": "AI 算力 / 半导体",
    "title": "Grab this 10-port gigabit PoE+ switch with up to 60W of power for under $38, a new record low",
    "url": "https://www.tomshardware.com/networking/network-switches/grab-this-10-port-gigabit-poe-switch-with-up-to-60w-of-power-for-under-usd38-a-new-record-low-ugreen-switch-upgrades-your-home-network-with-eight-power-delivery-ports-for-cameras-and-wi-fi-extenders",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T13:40:00+00:00",
    "summary": "This Ugreen 10-port unmanaged Ethernet switch has hit record-low pricing of $37.79, unlocking eight PoE+ ports for up to 60W of power delivery for cameras and WiFi extenders, along with two extra port"
  },
  {
    "id": "rss:https://www.eetimes.com/ai-drives-larger-denser-packaging-raising-new-challenges-for-equipment-makers/",
    "domain": "AI 算力 / 半导体",
    "title": "AI Drives Larger, Denser Packaging, Raising New Challenges for Equipment Makers",
    "url": "https://www.eetimes.com/ai-drives-larger-denser-packaging-raising-new-challenges-for-equipment-makers/",
    "source": "Susan Hong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T08:55:36+00:00",
    "summary": "At A*STAR’s Innovate Together 2026, industry experts explored packaging, hybrid bonding, optical interconnects, and process control for AI. The post AI Drives Larger, Denser Packaging, Raising New Cha"
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
    "points": 1654,
    "published_at": "2026-09-30T20:04:37+00:00",
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
    "points": 616,
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
    "id": "hn:49829472",
    "domain": "大厂 AI 动态",
    "title": "Fourier Analysis: Drawing Llamas with Circles",
    "url": "https://adekau.github.io/posts/2020/llamas.html",
    "source": "cebert",
    "platform": "hackernews",
    "points": 79,
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
    "id": "rss:https://www.theverge.com/tech/1003877/apple-security-camera-no-video",
    "domain": "大厂 AI 动态",
    "title": "Apple’s reportedly developing a smart home camera that doesn’t record video",
    "url": "https://www.theverge.com/tech/1003877/apple-security-camera-no-video",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T22:51:36+00:00",
    "summary": "Apple's rumored push into smart home tech could include a smart home security camera that only gives users text event descriptions instead of video footage. Mark Gurman said in the first episode of th"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1003756/google-gemini-live-guided-vision",
    "domain": "大厂 AI 动态",
    "title": "Google’s new Guided Vision feature can help you read the fine print",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1003756/google-gemini-live-guided-vision",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T19:47:51+00:00",
    "summary": "Guided Vision is launching in Gemini Live on compatible Android devices today to use AI to give real-time audio descriptions of anything you point your phone's camera at. By sharing your camera in Gem"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1003735/android-central-layoffs",
    "domain": "大厂 AI 动态",
    "title": "Android Central &#8216;will continue&#8217; despite laying off its staff",
    "url": "https://www.theverge.com/tech/1003735/android-central-layoffs",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T19:20:29+00:00",
    "summary": "Android Central, a blog focused on the Android ecosystem, laid off its staff yesterday, but owner Future confirms to The Verge that the site will continue publishing. Yesterday, four of the six staffe"
  },
  {
    "id": "rss:https://www.theverge.com/games/1003593/steam-deck-2-is-amd-gainsborough-the-chip-valves-been-waiting-for",
    "domain": "大厂 AI 动态",
    "title": "Steam Deck 2: Is AMD Gainsborough the chip Valve’s been waiting for?",
    "url": "https://www.theverge.com/games/1003593/steam-deck-2-is-amd-gainsborough-the-chip-valves-been-waiting-for",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T18:52:58+00:00",
    "summary": "The Steam Deck is four and a half years old, and handheld gamers are eagerly awaiting a Steam Deck 2 - but Valve has consistently said it needs a new chip with a \"generational leap\" in performance and"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1003589/google-ai-overviews-chegg-penske-lawsuits-dismissed",
    "domain": "大厂 AI 动态",
    "title": "Judge dismisses antitrust lawsuits over Google’s AI Overviews",
    "url": "https://www.theverge.com/tech/1003589/google-ai-overviews-chegg-penske-lawsuits-dismissed",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T17:12:21+00:00",
    "summary": "A federal judge has dismissed a pair of antitrust lawsuits filed by Chegg and Rolling Stone parent company Penske Media Corporation, which accused Google of driving away web traffic with its AI-powere"
  },
  {
    "id": "rss:https://www.theverge.com/games/1003549/sony-ps5-quick-spectral-super-resolution-qssr",
    "domain": "大厂 AI 动态",
    "title": "Sony brings AI graphics upscaling to the regular PS5",
    "url": "https://www.theverge.com/games/1003549/sony-ps5-quick-spectral-super-resolution-qssr",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T16:53:39+00:00",
    "summary": "Sony is launching a new AI upscaling technology specifically for the regular PS5. The new tech, called Quick Spectral Super Resolution (QSSR), is a \"new performance tier of AI upscaling\" that's a resu"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1003034/meta-vr-glasses-vs-augmented-reality",
    "domain": "大厂 AI 动态",
    "title": "Can VR glasses save VR?",
    "url": "https://www.theverge.com/tech/1003034/meta-vr-glasses-vs-augmented-reality",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T16:10:32+00:00",
    "summary": "I'm pretty sure I won't be buying the $1,299 Meta VR Glasses. That's too rich for my blood in today's economy, and my feelings about Meta are… conflicted. But I want you to understand that Meta just c"
  },
  {
    "id": "rss:https://www.theverge.com/news/1003515/microsoft-ryan-roslansky-office-teams-linkedin-leaving",
    "domain": "大厂 AI 动态",
    "title": "Microsoft’s Office and Teams chief is leaving",
    "url": "https://www.theverge.com/news/1003515/microsoft-ryan-roslansky-office-teams-linkedin-leaving",
    "source": "Tom Warren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T16:02:37+00:00",
    "summary": "After nearly 18 years at LinkedIn and Microsoft, Ryan Roslansky is leaving the company. Roslansky, who until recently was the CEO of LinkedIn, was promoted to the head of Office last year and then too"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1003365/microsoft-copilot-os-for-work-notepad",
    "domain": "大厂 AI 动态",
    "title": "Inside Microsoft’s big Copilot rethink",
    "url": "https://www.theverge.com/tech/1003365/microsoft-copilot-os-for-work-notepad",
    "source": "Tom Warren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T16:00:00+00:00",
    "summary": "Last week, Microsoft CEO Satya Nadella hosted an intimate, invite-only event for leaders from some of its key enterprise customers. Instead of a flashy media event, Nadella outlined the future of Copi"
  },
  {
    "id": "rss:https://www.theverge.com/policy/1003426/nyc-click-to-cancel-subscriptions-rule",
    "domain": "大厂 AI 动态",
    "title": "NYC is now the first city in America that bans sketchy subscriptions",
    "url": "https://www.theverge.com/policy/1003426/nyc-click-to-cancel-subscriptions-rule",
    "source": "Lauren Feiner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T14:49:25+00:00",
    "summary": "New York City residents struggling to get out of recurring subscription fees can now submit complaints to the city government. As of Thursday, the city's click-to-cancel rule has taken effect, which r"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/01/robotaxi-operators-will-face-fines-for-blocking-first-responders/",
    "domain": "大厂 AI 动态",
    "title": "Robotaxi operators will face fines for blocking first responders",
    "url": "https://techcrunch.com/2026/10/01/robotaxi-operators-will-face-fines-for-blocking-first-responders/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T00:57:57+00:00",
    "summary": "A new California law places new rules on autonomous vehicles operators"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/01/the-founders-guide-to-techcrunch-disrupt-2026-everything-you-need-to-know/",
    "domain": "大厂 AI 动态",
    "title": "The founder’s guide to TechCrunch Disrupt 2026: Everything you need to know",
    "url": "https://techcrunch.com/2026/10/01/the-founders-guide-to-techcrunch-disrupt-2026-everything-you-need-to-know/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T00:03:23+00:00",
    "summary": "TechCrunch Disrupt 2026 is built around one question: How do you build an enduring company in the AI era? Our programming and speaker lineup reflect that."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/01/lyft-is-paying-272-5m-to-settle-lawsuit-over-how-it-classified-drivers/",
    "domain": "大厂 AI 动态",
    "title": "Lyft is paying $272.5M to settle lawsuit over how it classified drivers",
    "url": "https://techcrunch.com/2026/10/01/lyft-is-paying-272-5m-to-settle-lawsuit-over-how-it-classified-drivers/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T21:57:08+00:00",
    "summary": "Today, gig economy drivers are classified as contractors. This settlement clears up a lingering lawsuit from 2020 when that was still an unanswered issue."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/01/kevin-mandias-new-agent-swarm-security-startup-armadin-raises-255-5m-at-2-5b-valuation/",
    "domain": "大厂 AI 动态",
    "title": "Kevin Mandia’s new ‘agent swarm’ security startup Armadin raises $255.5M at $2.5B valuation",
    "url": "https://techcrunch.com/2026/10/01/kevin-mandias-new-agent-swarm-security-startup-armadin-raises-255-5m-at-2-5b-valuation/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T21:55:22+00:00",
    "summary": "Kevin Mandia, best known as the founder of Mandiant, has a new startup that is using agent swarms to test and protect enterprises."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/01/musks-ai-chatbot-grok-reportedly-encouraged-trump-to-capture-venezuelas-president/",
    "domain": "大厂 AI 动态",
    "title": "Musk’s AI chatbot Grok reportedly encouraged Trump to capture Venezuela’s president",
    "url": "https://techcrunch.com/2026/10/01/musks-ai-chatbot-grok-reportedly-encouraged-trump-to-capture-venezuelas-president/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T21:08:11+00:00",
    "summary": "President Trump reportedly asked for Grok's opinion before invading Venezuela and capturing Nicolás Maduro."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/01/chatgpt-can-now-virtually-try-on-clothes-for-you/",
    "domain": "大厂 AI 动态",
    "title": "ChatGPT can now virtually try on clothes for you",
    "url": "https://techcrunch.com/2026/10/01/chatgpt-can-now-virtually-try-on-clothes-for-you/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T19:21:53+00:00",
    "summary": "OpenAI is rolling out new shopping features for ChatGPT that let users virtually try on clothing and accessories using their own photos and save products they like to a Favorites library."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/01/google-thinks-spacexs-starship-has-to-launch-1600-times-before-space-data-centers-get-off-the-ground/",
    "domain": "大厂 AI 动态",
    "title": "Google thinks SpaceX’s Starship has to launch 1,800 times before space data centers get off the ground",
    "url": "https://techcrunch.com/2026/10/01/google-thinks-spacexs-starship-has-to-launch-1600-times-before-space-data-centers-get-off-the-ground/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T19:18:03+00:00",
    "summary": "Google launched its first advanced chip into orbit to pave the way for space data centers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/01/worlds-first-enhanced-geothermal-power-plant-completed-in-just-23-months/",
    "domain": "大厂 AI 动态",
    "title": "World’s first enhanced geothermal power plant completed in just 23 months",
    "url": "https://techcrunch.com/2026/10/01/worlds-first-enhanced-geothermal-power-plant-completed-in-just-23-months/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T18:35:55+00:00",
    "summary": "Fervo Energy completed its first power plant in less than two years. The next phases promise to connect to the grid even quicker."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/01/openai-cuts-ties-with-three-safety-researchers-wsj-reports/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI cuts ties with 3 safety researchers, WSJ reports",
    "url": "https://techcrunch.com/2026/10/01/openai-cuts-ties-with-three-safety-researchers-wsj-reports/",
    "source": "Aditya Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T18:14:42+00:00",
    "summary": "OpenAI has parted ways with three safety researchers after an internal investigation found they mishandled sensitive company information, report says."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/01/opus-5-5-loves-to-tell-you-this-matters-and-other-ai-writing-tells/",
    "domain": "大厂 AI 动态",
    "title": "Opus 5.5 loves to tell you ‘this matters’ (and other AI writing tells)",
    "url": "https://techcrunch.com/2026/10/01/opus-5-5-loves-to-tell-you-this-matters-and-other-ai-writing-tells/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T17:50:19+00:00",
    "summary": "Opus 5.5’s biggest tell is the word “dependable,” which pops up 23 times more often than in human samples."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/01/this-startup-wants-to-turn-idle-car-inventory-into-rental-revenue/",
    "domain": "大厂 AI 动态",
    "title": "This startup wants to turn idle car inventory into rental revenue",
    "url": "https://techcrunch.com/2026/10/01/this-startup-wants-to-turn-idle-car-inventory-into-rental-revenue/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T17:09:00+00:00",
    "summary": "When Igor Dobrianskyi looks at a car dealership lot, he doesn't see rows of cars — he sees millions of dollars just sitting there, depreciating. Come see MyMonthlyCar in the Startup Battlefield 200 at"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/01/amazon-releases-its-own-jev-clone-as-decision-models-flood-the-web/",
    "domain": "大厂 AI 动态",
    "title": "Amazon releases its own Jev clone as decision models flood the web",
    "url": "https://techcrunch.com/2026/10/01/amazon-releases-its-own-jev-clone-as-decision-models-flood-the-web/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T16:49:22+00:00",
    "summary": "Amazon Web Services' Strand Labs has released the latest Jevalike decision model, Strands Decider 2B."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/01/shopify-debuts-canvas-a-way-to-build-online-stores-by-chatting-with-ai/",
    "domain": "大厂 AI 动态",
    "title": "Shopify debuts Canvas, a way to build online stores by chatting with AI",
    "url": "https://techcrunch.com/2026/10/01/shopify-debuts-canvas-a-way-to-build-online-stores-by-chatting-with-ai/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T16:44:35+00:00",
    "summary": "Shopify’s new Canvas site builder lets merchants create and customize their online stores by chatting with its AI agent Sidekick, while watching the changes happen in real time."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/01/california-governor-vetoes-bill-banning-use-of-pervert-glasses-to-secretly-record-people/",
    "domain": "大厂 AI 动态",
    "title": "California governor vetoes bill banning use of ‘pervert glasses’ to secretly record people",
    "url": "https://techcrunch.com/2026/10/01/california-governor-vetoes-bill-banning-use-of-pervert-glasses-to-secretly-record-people/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T16:35:25+00:00",
    "summary": "The California state bill would have penalized people who secretly recorded people in public with wearables equipped with cameras and microphones."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/01/one-year-later-tesla-and-musk-are-still-dont-have-a-good-definition-of-abundance/",
    "domain": "大厂 AI 动态",
    "title": "One year later, Tesla and Musk still don’t have a good definition of ‘abundance’",
    "url": "https://techcrunch.com/2026/10/01/one-year-later-tesla-and-musk-are-still-dont-have-a-good-definition-of-abundance/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T15:50:10+00:00",
    "summary": "The CEO promised to get more specific about his vision. But the details are still absent."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/01/brian-chesky-interview-ai-agents-need-their-own-operating-system/",
    "domain": "大厂 AI 动态",
    "title": "Brian Chesky interview: AI agents need their own operating system",
    "url": "https://techcrunch.com/2026/10/01/brian-chesky-interview-ai-agents-need-their-own-operating-system/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T15:12:00+00:00",
    "summary": "Brian Chesky on making Airbnb agent-friendly, the state of consumer AI, and why the world needs an AI-native operating system."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/01/photon-held-a-funeral-for-mobile-apps-now-it-has-4-5m-to-help-replace-them-with-agents/",
    "domain": "大厂 AI 动态",
    "title": "Photon held a funeral for mobile apps. Now it has $4.5M to help replace them with agents.",
    "url": "https://techcrunch.com/2026/10/01/photon-held-a-funeral-for-mobile-apps-now-it-has-4-5m-to-help-replace-them-with-agents/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T14:00:00+00:00",
    "summary": "The startup helps developers build AI agents that work over iMessage, SMS/RCS, email, and other messaging platforms. It's a bet that consumers will increasingly use agents instead of downloading apps."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/01/hearing-tech-startup-legato-launches-its-ai-hearing-glasses/",
    "domain": "大厂 AI 动态",
    "title": "Hearing tech startup Legato launches its AI hearing glasses",
    "url": "https://techcrunch.com/2026/10/01/hearing-tech-startup-legato-launches-its-ai-hearing-glasses/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T13:00:00+00:00",
    "summary": "The glasses stem from the startup’s goal of making hearing care more accessible by addressing the cost, comfort, and stigma associated with traditional hearing aids."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/01/audibles-new-features-let-you-explore-book-worlds-and-even-talk-to-characters/",
    "domain": "大厂 AI 动态",
    "title": "Audible’s new features let you explore book worlds — and use AI to talk to characters",
    "url": "https://techcrunch.com/2026/10/01/audibles-new-features-let-you-explore-book-worlds-and-even-talk-to-characters/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T13:00:00+00:00",
    "summary": "Audible is rolling out new features that help listeners keep track of characters, explore places and imagery mentioned in books, and even interact with characters using generative AI."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/01/the-new-kindle-ditches-the-bezel-in-a-push-toward-a-smaller-lighter-e-reader/",
    "domain": "大厂 AI 动态",
    "title": "The new Kindle ditches the raised bezel in a push toward a smaller, lighter e-reader",
    "url": "https://techcrunch.com/2026/10/01/the-new-kindle-ditches-the-bezel-in-a-push-toward-a-smaller-lighter-e-reader/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T13:00:00+00:00",
    "summary": "The new Kindle lineup features its lightest and thinnest designs yet, with a sleek, front-flush display that eliminates bezels for good."
  },
  {
    "id": "rss:https://stratechery.com/2026/an-interview-with-jason-del-rey-about-muse-amazon-and-walmart/",
    "domain": "大厂 AI 动态",
    "title": "An Interview with Jason Del Rey About Muse, Amazon, and Walmart",
    "url": "https://stratechery.com/2026/an-interview-with-jason-del-rey-about-muse-amazon-and-walmart/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T10:00:00+00:00",
    "summary": "An interview with Jason Del Rey about Amazon versus Meta, which is a continuation of the oldest battle in retail between Amazon and Walmart."
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
    "points": 53,
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
    "id": "hn:49875913",
    "domain": "金融",
    "title": "Parley: Federated, decentralised chat that speaks plain IRC",
    "url": "https://git.mills.io/prologic/parley",
    "source": "davidcollantes",
    "platform": "hackernews",
    "points": 327,
    "published_at": "2026-09-28T10:30:54+00:00",
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
    "id": "hn:49921118",
    "domain": "金融",
    "title": "Meta Uses A.I. Data Centers to Avoid Billions in Federal Taxes",
    "url": "https://www.nytimes.com/2026/09/30/technology/meta-ai-data-centers-taxes.html",
    "source": "gmays",
    "platform": "hackernews",
    "points": 252,
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
    "id": "hn:49904408",
    "domain": "金融",
    "title": "Tesla takes on $30B in credit as it approaches unprofitability",
    "url": "https://electrek.co/2026/09/29/tesla-takes-on-30-billion-in-credit-as-it-approaches-unprofitability/",
    "source": "ciconia",
    "platform": "hackernews",
    "points": 158,
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
    "points": 120,
    "published_at": "2026-10-01T01:40:50+00:00",
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
    "id": "rss:https://arxiv.org/abs/2610.00005",
    "domain": "金融",
    "title": "A Multi-Venue Solana/DeFi Microstructure Data Corpus: The RED-2400 Family v2",
    "url": "https://arxiv.org/abs/2610.00005",
    "source": "Arati Uday Kamat",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T04:00:00+00:00",
    "summary": "arXiv:2610.00005v1 Announce Type: new Abstract: Empirical research on decentralized and Solana-native market microstructure is constrained less by method than by data: the strongest results in the fie"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.00023",
    "domain": "金融",
    "title": "Market, Ethics, and Morality",
    "url": "https://arxiv.org/abs/2610.00023",
    "source": "Ali Zeytoon-Nejad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T04:00:00+00:00",
    "summary": "arXiv:2610.00023v1 Announce Type: new Abstract: This paper provides a clear philosophy on codes of human conduct within economic and social institutions like markets and government. It categorizes the"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.00051",
    "domain": "金融",
    "title": "Climate aware lending allocation under NGFS scenarios - A Monte Carlo approach",
    "url": "https://arxiv.org/abs/2610.00051",
    "source": "Marina Palaisti",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T04:00:00+00:00",
    "summary": "arXiv:2610.00051v1 Announce Type: new Abstract: This paper develops a framework to assess loan portfolio budget in credit portfolios exposed to climate risk over a 3-5 year horizon. Using short-term s"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.00104",
    "domain": "金融",
    "title": "Modelling Robust Lending Decisions under Climate Scenario Ambiguity: A Minimax-Regret Framework with NGFS Short-Term Scenarios",
    "url": "https://arxiv.org/abs/2610.00104",
    "source": "Marina Palaisti",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T04:00:00+00:00",
    "summary": "arXiv:2610.00104v1 Announce Type: new Abstract: This paper develops a public-data framework for evaluating incremental bank lending when plausible climate scenarios imply different sector credit outco"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.00147",
    "domain": "金融",
    "title": "Admissible Portfolio Optimization: Information Constraints, Conditional Efficient Frontiers, and the Price of Causal Identification",
    "url": "https://arxiv.org/abs/2610.00147",
    "source": "Alejandro Rodriguez Dominguez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T04:00:00+00:00",
    "summary": "arXiv:2610.00147v1 Announce Type: new Abstract: Mean--variance portfolio choice takes the conditioning information as given and optimizes over weights, so two errors about that information pass into t"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.00158",
    "domain": "金融",
    "title": "Causal Price-of-Risk Mandates under Overlapping Information",
    "url": "https://arxiv.org/abs/2610.00158",
    "source": "Alejandro Rodriguez Dominguez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T04:00:00+00:00",
    "summary": "arXiv:2610.00158v1 Announce Type: new Abstract: We study whether causal risk mandates constructed from overlapping information blocks can be implemented by one self-financing portfolio that is optimal"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.00165",
    "domain": "金融",
    "title": "Outcome Determination and Settlement Finality on Kalshi: Public State Paths, Prospective Measurement, and Empirical Identification",
    "url": "https://arxiv.org/abs/2610.00165",
    "source": "Maksym Nechepurenko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T04:00:00+00:00",
    "summary": "arXiv:2610.00165v1 Announce Type: new Abstract: Event-contract settlement is a state path rather than a universal timestamp. Using a registered seven-day enrollment and seven-day administrative follow"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.00173",
    "domain": "金融",
    "title": "Price Discovery at the Boundary of Contractual Decidability: Terminal-Value Gaps, Trading Availability, and Venue Finality on Kalshi",
    "url": "https://arxiv.org/abs/2610.00173",
    "source": "Maksym Nechepurenko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T04:00:00+00:00",
    "summary": "arXiv:2610.00173v1 Announce Type: new Abstract: This paper studies price discovery around contractual decidability rather than an arbitrary venue label. Its upstream lifecycle and decidability clocks "
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.00183",
    "domain": "金融",
    "title": "Two Models of Event Finality: Functional Alignment, Contestability, and Empirical Comparability on Polymarket and Kalshi",
    "url": "https://arxiv.org/abs/2610.00183",
    "source": "Maksym Nechepurenko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T04:00:00+00:00",
    "summary": "arXiv:2610.00183v1 Announce Type: new Abstract: Event contracts reach economic finality through different institutional paths. Polymarket distinguishes oracle adjudication, adapter consumption, Condit"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.00287",
    "domain": "金融",
    "title": "Multi-Jurisdictional Legal Identity Assurance for Capability Gating: A Design-Science Proposal for Tiered, Reusable Identity Assurance of Natural, Juridical, and Machine Entities",
    "url": "https://arxiv.org/abs/2610.00287",
    "source": "Walter Kurz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T04:00:00+00:00",
    "summary": "arXiv:2610.00287v1 Announce Type: new Abstract: Identity assurance is the cost a digital system pays for dishonesty and uncertainty: it exists to make acts attributable when not everyone can be truste"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.00340",
    "domain": "金融",
    "title": "Short-term barrier option price expansion",
    "url": "https://arxiv.org/abs/2610.00340",
    "source": "Masaaki Fukasawa",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T04:00:00+00:00",
    "summary": "arXiv:2610.00340v1 Announce Type: new Abstract: We derive a short-maturity expansion for up-and-out put barrier option prices under continuous stochastic volatility when the strike and the barrier app"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.00619",
    "domain": "金融",
    "title": "Beyond Supra-Competitive Outcomes: Collusive Behaviour in Deep Reinforcement Learning for Optimal Execution Games",
    "url": "https://arxiv.org/abs/2610.00619",
    "source": "Christos Spyridon Koulouris, Carlo Campajola",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T04:00:00+00:00",
    "summary": "arXiv:2610.00619v1 Announce Type: new Abstract: In this paper, we extend earlier findings of supra-competitive outcomes in optimal-execution games by identifying a learned punitive mechanism that dete"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.00951",
    "domain": "金融",
    "title": "Negative Oil & Nickel Squeeze: A Feedback Model for Extreme Commodity Futures Prices",
    "url": "https://arxiv.org/abs/2610.00951",
    "source": "Iosif Zimbidis, Ronnie Sircar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T04:00:00+00:00",
    "summary": "arXiv:2610.00951v1 Announce Type: new Abstract: On April 20, 2020, the May front-month WTI oil futures contract, one day before its expiration date, opened near $\\$17/$barrel and dropped far below zer"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.00998",
    "domain": "金融",
    "title": "Portfolio Choice under General Utility with Transaction Costs and Search Frictions",
    "url": "https://arxiv.org/abs/2610.00998",
    "source": "Tae Ung Gang, Donghan Kim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T04:00:00+00:00",
    "summary": "arXiv:2610.00998v1 Announce Type: new Abstract: We study finite-horizon portfolio optimization with proportional transaction costs and trading opportunities arriving at the jump times of a Cox process"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.01008",
    "domain": "金融",
    "title": "Modeling Shipping Emissions: Machine Learning, Engineering, and Policy Counterfactuals",
    "url": "https://arxiv.org/abs/2610.01008",
    "source": "Hiroyuki Kasahara, Allen Peters, Oliver Xu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T04:00:00+00:00",
    "summary": "arXiv:2610.01008v1 Announce Type: new Abstract: Machine learning predicts outcomes well, but predictive accuracy does not ensure reliable counterfactual responses. We examine how to combine machine le"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.01187",
    "domain": "金融",
    "title": "On the Pricing of American Options under Stochastic Local Volatility and Stochastic Correlation via the RBSDE Framework",
    "url": "https://arxiv.org/abs/2610.01187",
    "source": "Long Teng",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T04:00:00+00:00",
    "summary": "arXiv:2610.01187v1 Announce Type: new Abstract: In this work, we study the pricing of American options under stochastic local volatility (SLV) models extended by including stochastic correlation drive"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.01264",
    "domain": "金融",
    "title": "Strategic Optimization of Bus Systems with Stochastic Ridership",
    "url": "https://arxiv.org/abs/2610.01264",
    "source": "Haoran Zhao, Andres Fielbaum",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T04:00:00+00:00",
    "summary": "arXiv:2610.01264v1 Announce Type: new Abstract: In global metropolitan areas, public transport benefits from bus systems. Bus design widely applies theoretical models, which typically assume static ri"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.01562",
    "domain": "金融",
    "title": "Social welfare and price discovery in double auction markets",
    "url": "https://arxiv.org/abs/2610.01562",
    "source": "Teemu Pennanen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T04:00:00+00:00",
    "summary": "arXiv:2610.01562v1 Announce Type: new Abstract: The tendency of the double auction mechanism to drive prices to competitive equilibrium has been well documented in laboratory experiments, but the phen"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.01897",
    "domain": "金融",
    "title": "Shared Models, Selective Trading, and Order Flow",
    "url": "https://arxiv.org/abs/2610.01897",
    "source": "Victoria Ruojie Li, Arka Prava Bandyopadhyay",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T04:00:00+00:00",
    "summary": "arXiv:2610.01897v1 Announce Type: new Abstract: We study whether model diversity survives selection into trading. In synthetic markets with a fixed mixture of three language-model families, news prese"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.00782",
    "domain": "金融",
    "title": "Can we create a `race to the top' for weather forecasts to inform smallholder farmer decisions?",
    "url": "https://arxiv.org/abs/2610.00782",
    "source": "Colin Aitken, Michael K. Tippett, Pedram Hassanzadeh, Katherine Kowal, Rendani Mbuvha, John H. Marsham, Shruti Nath, Ousmane Ndiaye, Douglas J. Parker, Caroline M Wainwright, Michael Kremer, William R. Boos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T04:00:00+00:00",
    "summary": "arXiv:2610.00782v1 Announce Type: cross Abstract: Artificial-intelligence weather prediction (AIWP) models have made it possible to produce high-quality tailored forecasts with limited computational r"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.01115",
    "domain": "金融",
    "title": "Certified Alpha Capacity: Statistical Evidence, Economic Lifetime, and Arbitrage under Decay",
    "url": "https://arxiv.org/abs/2610.01115",
    "source": "Nicol\\`o Bonacorsi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T04:00:00+00:00",
    "summary": "arXiv:2610.01115v1 Announce Type: cross Abstract: In this paper we study whether a trading signal can accumulate enough statistical evidence for reliable deployment before its economic value decays. W"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.01325",
    "domain": "金融",
    "title": "PPO-HRAP: Proximal Policy Optimization with a Hybrid Regime-Aware Policy for Risk-Controlled Trading",
    "url": "https://arxiv.org/abs/2610.01325",
    "source": "Duong Hien Chi Kien, Thanh Trung Huynh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T04:00:00+00:00",
    "summary": "arXiv:2610.01325v1 Announce Type: cross Abstract: Reinforcement learning for trading often struggles to balance upside participation with drawdown control. Profit-only policies can collapse toward pas"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.01348",
    "domain": "金融",
    "title": "Verify Claims, Not Scores: Evidence-Based Verification of Modular Agents",
    "url": "https://arxiv.org/abs/2610.01348",
    "source": "Ali Atiah Alzahrani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T04:00:00+00:00",
    "summary": "arXiv:2610.01348v1 Announce Type: cross Abstract: When developers change one component of an agent, such as its controller, a learned model or its verifier, they usually judge the change by an aggrega"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.01585",
    "domain": "金融",
    "title": "Distribution-constrained maximum stopping of maximum type",
    "url": "https://arxiv.org/abs/2610.01585",
    "source": "Shuoqing Deng, Xin Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T04:00:00+00:00",
    "summary": "arXiv:2610.01585v1 Announce Type: cross Abstract: We consider the distribution-constrained optimal stopping problem $\\sup_{\\tau\\sim \\mu} \\mathbb E[B^*_\\tau]$, where $\\mu$ is a probability distribution"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.02106",
    "domain": "金融",
    "title": "Densities for scalar-valued BSDEs via unique continuation and backward uniqueness",
    "url": "https://arxiv.org/abs/2610.02106",
    "source": "Solesne Bourguin, Daniel C. Schwarz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T04:00:00+00:00",
    "summary": "arXiv:2610.02106v1 Announce Type: cross Abstract: We give sufficient conditions ensuring that, at every fixed positive time, the scalar backward component of a Markovian forward-backward stochastic di"
  },
  {
    "id": "rss:https://arxiv.org/abs/2505.12269",
    "domain": "金融",
    "title": "Hardening Soft Information: Evidence on Analyst Integration Costs",
    "url": "https://arxiv.org/abs/2505.12269",
    "source": "Kerry Xiao, Amy Zang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T04:00:00+00:00",
    "summary": "arXiv:2505.12269v4 Announce Type: replace Abstract: We examine how the cost of transforming qualitative information into precise numerical estimates--a form of integration cost--creates a structural f"
  },
  {
    "id": "rss:https://arxiv.org/abs/2602.16078",
    "domain": "金融",
    "title": "AI as Coordination-Compressing Capital: Task Reallocation, Organizational Redesign, and the Regime Fork",
    "url": "https://arxiv.org/abs/2602.16078",
    "source": "Alex Farach (Microsoft)",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T04:00:00+00:00",
    "summary": "arXiv:2602.16078v4 Announce Type: replace Abstract: Task-based models of AI hold organizational structure fixed. We model AI as agent capital that compresses managers' per-link coordination costs towa"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.13597",
    "domain": "金融",
    "title": "Daycare Matching with Siblings: Social Implementation and Welfare Evaluation",
    "url": "https://arxiv.org/abs/2604.13597",
    "source": "Kan Kuno, Daisuke Moriwaki, Yoshihiro Takenami",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T04:00:00+00:00",
    "summary": "arXiv:2604.13597v3 Announce Type: replace Abstract: In centralized matching markets, agents may value joint assignment, as with siblings or couples. Standard preference estimation ignores such complem"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.15825",
    "domain": "金融",
    "title": "Convergence to collusion in algorithmic pricing",
    "url": "https://arxiv.org/abs/2604.15825",
    "source": "Kevin Michael Frick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T04:00:00+00:00",
    "summary": "arXiv:2604.15825v2 Announce Type: replace Abstract: Artificial intelligence algorithms are increasingly used by firms to set prices. Previous research shows that they can learn to collude, but how qui"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.27837",
    "domain": "金融",
    "title": "Distributionally Robust Insurance under Bregman-Wasserstein Divergence",
    "url": "https://arxiv.org/abs/2604.27837",
    "source": "Wenjun Jiang, Qingqing Zhang, Yiying Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T04:00:00+00:00",
    "summary": "arXiv:2604.27837v2 Announce Type: replace Abstract: This paper investigates two optimal insurance contracting problems under distributional uncertainty from the perspective of a potential policyholder"
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
  }
]
```
