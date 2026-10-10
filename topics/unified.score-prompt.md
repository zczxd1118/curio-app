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

- 今日日期：`2026-10-10`
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
  "date": "2026-10-10",
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
    "points": 3160104,
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
    "points": 2063431,
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
    "points": 1946891,
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
    "points": 1608175,
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
    "points": 1379485,
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
    "points": 1325333,
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
    "points": 1120480,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1kX546QEjG",
    "domain": "AI",
    "title": "保姆级Claude Code速成，必学！简单！【附完整文档】",
    "url": "http://www.bilibili.com/video/av116554859545963",
    "source": "数字游牧人",
    "platform": "bilibili",
    "points": 1113808,
    "published_at": "2026-05-11T09:02:15+00:00",
    "summary": "文档链接：https://lcnaoyjp4e3z.feishu.cn/wiki/MtJlwX0B5iy6y9k5GZTcdjSknTd"
  },
  {
    "id": "bvid:BV1yorUYWEGD",
    "domain": "AI",
    "title": "普通人也可以看的 AI 编程指南 | Cursor 教程｜Cursor 使用技巧和思路｜如何免费使用 Cursor｜AI 编程",
    "url": "http://www.bilibili.com/video/av113786467981446",
    "source": "不正经的前端啊",
    "platform": "bilibili",
    "points": 946162,
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
    "points": 897226,
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
    "points": 839940,
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
    "points": 709002,
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
    "points": 591863,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 476171,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 444973,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1ia9UBPESQ",
    "domain": "AI",
    "title": "在VScode中配置Claude Code并接入DeepSeek V4 Pro【oo唠嗑教程】",
    "url": "http://www.bilibili.com/video/av116487012549813",
    "source": "沉默的羔丸ovo",
    "platform": "bilibili",
    "points": 350872,
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
    "points": 312706,
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
    "points": 303490,
    "published_at": "2025-04-15T00:59:13+00:00",
    "summary": "MCP终极指南 - 带你深入掌握MCP（基础篇）\n\n时间轴：\n01:05 MCP简要介绍\n02:47 安装 MCP Host（Cline）\n03:15 配置 Cline 用的 API Key\n06:01 第一个 MCP 问题\n06:31 概念解释：MCP Server 和 Tool\n09:13 配置 MCP Server\n14:19 使用 MCP Server\n15:24 MCP 交互流程详解\n1"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 274722,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 235026,
    "published_at": "2026-04-27T08:51:41+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n   喜欢视频课程的同学一键三连多多支持一下，长按点赞五秒=lv6大佬 可以的发送彩色弹幕哦。\n配套源码项目已打包评论区回复up"
  },
  {
    "id": "bvid:BV1X8oKBLEdj",
    "domain": "AI",
    "title": "一口气学会AI编程！3个月10万字超详细教学！【项目实操】【0基础教学】【自学教程】【AI编程】【vibecoding】",
    "url": "http://www.bilibili.com/video/av116436177523067",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 232840,
    "published_at": "2026-04-21T03:15:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料，领取方式：关注后 私信“ 1 ”就好！\n\n后面还会出【一口气学会AI漫剧 】【一口气学会AI Agent 】等系列！大家可以蹲蹲！"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 198728,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1TTR8BaEnL",
    "domain": "AI",
    "title": "Claude Code 零基础终极教程：安装、换模型、插件、Hooks、Skills、Subagents、实战项目一次讲透！",
    "url": "http://www.bilibili.com/video/av116529475622752",
    "source": "木子不写代码",
    "platform": "bilibili",
    "points": 188682,
    "published_at": "2026-05-07T08:00:00+00:00",
    "summary": "这是你能看到的最完整的 Claude Code 零基础系统教程。\n\n\n我们将深度拆解：\n\n1️⃣ 基础入门：安装、第三方模型接入、权限系统。\n\n2️⃣ 核心进阶：Tools、Hooks、Skills、Subagents 及自动化流程。\n\n3️⃣ 项目实战：从零构建一个真实可用的 AI 网页 App。\n\n\n视频跟到最后，你不只是学会写代码，而是掌握 AI 智能体的工作逻辑。我是木子，只提供 AI 时"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 183123,
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
    "points": 158963,
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
    "points": 131692,
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
    "points": 93952,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1d2pF6nEqZ",
    "domain": "AI",
    "title": "当你团队都在vibe coding",
    "url": "http://www.bilibili.com/video/av117392663450931",
    "source": "程序员牛牛学长",
    "platform": "bilibili",
    "points": 90725,
    "published_at": "2026-10-08T10:55:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1XnuGzfEp7",
    "domain": "AI",
    "title": "让你手中的AI好用10倍！5个好玩实用的MCP推荐，让你不只会用AI搜索",
    "url": "http://www.bilibili.com/video/av114835262018810",
    "source": "田同学Tino",
    "platform": "bilibili",
    "points": 76067,
    "published_at": "2025-07-12T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV143wwz6E8F",
    "domain": "AI",
    "title": "Claude code科研使用展示与思路分享（提速就靠Ai）",
    "url": "http://www.bilibili.com/video/av116211882920985",
    "source": "科研推土机",
    "platform": "bilibili",
    "points": 76038,
    "published_at": "2026-03-11T18:12:00+00:00",
    "summary": "本期给大家带来的是Claude在Vscode的科研应用演示与我最近的一些心得使用心得，科研速度嘎嘎提升。论文复现画图、数据分析就靠Claude code。这个课程也是科研推土机「系统管理文献课程2.0」学员催我更新的内容，希望能帮助到大家～，这个视频重点讲两个事情：\n1️⃣ 资料获取，free不用怀疑，我是良心可言博主，，关注我(GZTSHNR)～\n2️⃣ 展示如何在VS code实操应用clau"
  },
  {
    "id": "bvid:BV1VL3F6pE9K",
    "domain": "AI",
    "title": "0基础入门智能体agent测试：AI测试基础+AI智能体(Agent)测试从零入门全攻略，2026最新版！",
    "url": "http://www.bilibili.com/video/av116991151113881",
    "source": "黑马测试",
    "platform": "bilibili",
    "points": 71640,
    "published_at": "2026-07-27T09:19:37+00:00",
    "summary": "还在卷传统软件测试？2026年必学的AI智能体(Agent)测试来了！本期视频专为0基础小白打造，从软件测试基础讲起...若要本视频配套资源笔记可加up主企微（请看置顶留言最后一句话）。"
  },
  {
    "id": "bvid:BV1ApYD6KEkD",
    "domain": "AI",
    "title": "马斯克收购Cursor后，Cursor的性价比现在已经爆表",
    "url": "http://www.bilibili.com/video/av117254955993228",
    "source": "jopatk",
    "platform": "bilibili",
    "points": 67225,
    "published_at": "2026-09-11T23:19:58+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1e8dmBYEms",
    "domain": "AI",
    "title": "国内零门槛安装Claude Code(Win/Mac都支持｜新手友好｜建议收藏)",
    "url": "http://www.bilibili.com/video/av116441546230371",
    "source": "栗氪聊AI",
    "platform": "bilibili",
    "points": 66286,
    "published_at": "2026-04-21T07:38:25+00:00",
    "summary": "喜欢的朋友可以三连+关注支持一下，这对我帮助很大，感谢～"
  },
  {
    "id": "bvid:BV1jCaq6nESn",
    "domain": "AI",
    "title": "【Opus 5.5半价】零基础小白友好，15分钟彻底学习Claude桌面版",
    "url": "http://www.bilibili.com/video/av117346425374831",
    "source": "LeaderAI",
    "platform": "bilibili",
    "points": 63901,
    "published_at": "2026-09-28T03:03:19+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operit教程：入门安卓最强大ai平台operitAI",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 62367,
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
    "points": 55844,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1EfY76YEwp",
    "domain": "AI",
    "title": "14k Star Claude Code 开源桌面端，能自动操作电脑了！",
    "url": "http://www.bilibili.com/video/av117251936293145",
    "source": "程序员阿江-Relakkes",
    "platform": "bilibili",
    "points": 46898,
    "published_at": "2026-09-11T10:30:01+00:00",
    "summary": "基于此前泄露的 Claude Code 源代码，我做了一个开源桌面端 cc-haha，并持续迭代。\n这次重构了 Computer Use 电脑操控功能：AI 能自己看屏幕、操作 APP，在 Mac 后台搭建小镇，也不占用我的鼠标键盘。\n本期从下载安装、模型配置到权限授权，带你一步步用起来。支持自选模型，不需要 Claude 账号。"
  },
  {
    "id": "bvid:BV1x6Vt6dEef",
    "domain": "AI",
    "title": "100 小时测试 Claude Code vs Codex（真实结果）",
    "url": "http://www.bilibili.com/video/av116656495925868",
    "source": "设计之道",
    "platform": "bilibili",
    "points": 39841,
    "published_at": "2026-05-29T06:44:49+00:00",
    "summary": "【海外 AI 订阅】\n国内直连，支付宝付款，不用代理，\n一站订阅 ChatGPT / Codex / Claude Code / X\n订阅链接：https://bewild.ai?code=SJZD\n订阅时请填优惠邀请码：SJZD，具体优惠金额以官网为准。\n\n【视频介绍】\n我花了 100 个小时测试 Claude Code 和 Codex，结果真的让我非常意外。\n相同的提示词、相同的项目构建、两个"
  },
  {
    "id": "bvid:BV1Cvpw6iEwS",
    "domain": "AI",
    "title": "【10月Agent大横评】Deepseek用什么AI Agent不烧心，从夯到拉？",
    "url": "http://www.bilibili.com/video/av117393351251135",
    "source": "xx滴热茶",
    "platform": "bilibili",
    "points": 35945,
    "published_at": "2026-10-06T09:56:33+00:00",
    "summary": "Deepseek用什么agent不烧心，从夯到拉？穷鬼实测到底哪个agent和deepseek搭配做的又快又好还省钱？【8个Agent大横评】"
  },
  {
    "id": "bvid:BV1oQYL64EJV",
    "domain": "AI",
    "title": "【SRC漏洞挖掘】2026最适合新手的AI+自动化挖漏洞教程，从环境搭建到漏洞验证，手把手带你挖到第一个SRC漏洞！",
    "url": "http://www.bilibili.com/video/av117251248490748",
    "source": "阿盾聊安全",
    "platform": "bilibili",
    "points": 32963,
    "published_at": "2026-09-11T07:39:16+00:00",
    "summary": "这套 18 节教程带你从零跑通 AI 自动化挖漏洞全流程：环境搭建、Hermes部署、Burp/Nuclei 集成、资产侦察、漏洞发现到报告验证，一套打通。\n适合有 Web 安全基础、想从手动挖洞升级到自动化的同学。\n资料和工具包见评论区，三连不迷路。"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 24076,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV15Vhy6cEhd",
    "domain": "AI",
    "title": "通俗易懂地讲解什么是Agent？",
    "url": "http://www.bilibili.com/video/av117330906449673",
    "source": "洪涛同学LovTech",
    "platform": "bilibili",
    "points": 22209,
    "published_at": "2026-09-25T09:12:59+00:00",
    "summary": "从0到1搭建一个简易Agent，从小白的角度出发解释Agent是如何运行的？"
  },
  {
    "id": "bvid:BV1Jnti6kE1C",
    "domain": "AI",
    "title": "【AI➕生信分析】目前B站最全最细的巧用Agent零代码完成一篇生信分析全套教程，一周从AI分析工作站的搭建到自动数据的获取，看完这一套生信分析教程就够了！",
    "url": "http://www.bilibili.com/video/av117211637222989",
    "source": "生信学不会1",
    "platform": "bilibili",
    "points": 21256,
    "published_at": "2026-09-04T07:43:34+00:00",
    "summary": "本套教程适合想学习生信分析的同学，生信分析+AI，巧用Agent零代码完成一篇生信分析，零基础教学\n如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！！！"
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 20537,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1pfuR69EoF",
    "domain": "AI",
    "title": "【全80集】零基础Vibe Coding教程，Vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av117070675118277",
    "source": "暴龙Boy",
    "platform": "bilibili",
    "points": 17114,
    "published_at": "2026-08-10T10:45:04+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1ZBT2ztEwp",
    "domain": "AI",
    "title": "一条视频讲清楚 到底什么是MCP！#MCP #Cursor #AI #编程",
    "url": "http://www.bilibili.com/video/av114642592469769",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 14437,
    "published_at": "2025-06-07T14:53:38+00:00",
    "summary": "一条视频讲清楚 到底什么是MCP！#MCP #Cursor #AI #编程"
  },
  {
    "id": "bvid:BV1sQaL6vEkb",
    "domain": "AI",
    "title": "小白向，ai入门第一课：agent的部署和使用！",
    "url": "http://www.bilibili.com/video/av117349378166797",
    "source": "沈三殊",
    "platform": "bilibili",
    "points": 13614,
    "published_at": "2026-09-28T15:30:36+00:00",
    "summary": "详细的agent部署介绍：https://pan.quark.cn/s/3846914c6da7\n欢迎来到ai的世界！！\n有疑问欢迎私信。"
  },
  {
    "id": "bvid:BV1xh3C6cEGv",
    "domain": "AI",
    "title": "两周完成一篇SCI论文，用claude code帮你干",
    "url": "http://www.bilibili.com/video/av117002408559933",
    "source": "博士大师兄木水",
    "platform": "bilibili",
    "points": 13468,
    "published_at": "2026-07-29T08:53:04+00:00",
    "summary": "大师兄八股文SCI速成模板已制作成skill，手把手带你实现一键生成SCI论文初稿"
  },
  {
    "id": "bvid:BV1cyVv6TEG6",
    "domain": "AI",
    "title": "Claude Code CLI 小白极简入门 - 装了之后必会的命令与快捷键",
    "url": "http://www.bilibili.com/video/av116677635217424",
    "source": "五里墩茶社",
    "platform": "bilibili",
    "points": 13361,
    "published_at": "2026-06-02T00:20:19+00:00",
    "summary": "一个key用全球大模型🔴 https://DMXAPI.cn 🚀 国内直连OpenAI、Claude、Gemini,💰￥1元起充!\n\n加入我的知识星球:https://t.zsxq.com/W5Oj7\n\n本期视频面向已经装好 Claude Code、想真正用起来的新手。\n\n装了 Claude Code、却只会跟它对话？这一期按一次真实会话的顺序，把每天都会用到的命令和快捷键过一遍 - 怎么发现命令"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 12235,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
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
    "id": "hn:50008187",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI annualised revenues $20B less than previously signalled",
    "url": "https://www.cnbc.com/2026/10/08/open-ai-revenue-nvidia-oracle-coreweave.html",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 424,
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
    "id": "hn:49906100",
    "domain": "AI 算力 / 半导体",
    "title": "OpenDLSS: A Vulkan Reimplementation of Nvidia's DLSS 5 Neural Rendering Network",
    "url": "https://github.com/maanHimself/OpenDLSS-NR",
    "source": "sagacity",
    "platform": "hackernews",
    "points": 279,
    "published_at": "2026-09-30T08:43:21+00:00",
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
    "id": "rss:https://www.eetimes.com/manfred-horstmann-globalfoundries-bets-on-fdx-fusion-for-physical-ai/",
    "domain": "AI 算力 / 半导体",
    "title": "Manfred Horstmann: GlobalFoundries Bets on FDX Fusion for Physical AI",
    "url": "https://www.eetimes.com/manfred-horstmann-globalfoundries-bets-on-fdx-fusion-for-physical-ai/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T22:00:00+00:00",
    "summary": "GlobalFoundries said strained-silicon FD-SOI can deliver 7-nm-class performance without EUV and open a new market for Europe. The post Manfred Horstmann: GlobalFoundries Bets on FDX Fusion for Physica"
  },
  {
    "id": "rss:https://www.eetimes.com/solid-state-transformers-accelerate-your-sst-design/",
    "domain": "AI 算力 / 半导体",
    "title": "Solid-State Transformers: Accelerate Your SST Design",
    "url": "https://www.eetimes.com/solid-state-transformers-accelerate-your-sst-design/",
    "source": "Infineon Technologies, Arrow Electronics",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T15:38:47+00:00",
    "summary": "Join our expert-led webinar to explore Infineon's comprehensive portfolio for Solid-State Transformers (SSTs). The post Solid-State Transformers: Accelerate Your SST Design appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/connecting-chiplets-isnt-enough-solving-the-data-movement-challenge-in-multi-die-systems/",
    "domain": "AI 算力 / 半导体",
    "title": "Connecting Chiplets Isn’t Enough – Solving the Data Movement Challenge in Multi-Die Systems",
    "url": "https://www.eetimes.com/connecting-chiplets-isnt-enough-solving-the-data-movement-challenge-in-multi-die-systems/",
    "source": "Arteris",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T14:21:07+00:00",
    "summary": "Join this BitCast and explore how extending NoC connectivity across die boundaries enables engineering teams to scale from monolithic SoCs to multi-die architectures. The post Connecting Chiplets Isn’"
  },
  {
    "id": "rss:https://www.eetimes.com/u-s-manufacturing-activity-sustains-growth-in-september-as-backlogs-surge/",
    "domain": "AI 算力 / 半导体",
    "title": "U.S. Manufacturing Activity Sustains Growth in September as Backlogs Surge",
    "url": "https://www.eetimes.com/u-s-manufacturing-activity-sustains-growth-in-september-as-backlogs-surge/",
    "source": "News Desk",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T12:11:04+00:00",
    "summary": "Manufacturing maintains nine-month growth streak despite soaring costs and trade barriers. The post U.S. Manufacturing Activity Sustains Growth in September as Backlogs Surge appeared first on EE Time"
  },
  {
    "id": "rss:https://www.eetimes.com/physical-ai-needs-a-neuromorphic-path-from-sensor-to-silicon/",
    "domain": "AI 算力 / 半导体",
    "title": "Physical AI Needs a Neuromorphic Path from Sensor to Silicon",
    "url": "https://www.eetimes.com/physical-ai-needs-a-neuromorphic-path-from-sensor-to-silicon/",
    "source": "Xabier Iturbe",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T08:39:41+00:00",
    "summary": "Physical AI will be limited in the real world if we keep pretending that physical data comes packaged like the digital world. The post Physical AI Needs a Neuromorphic Path from Sensor to Silicon appe"
  },
  {
    "id": "rss:https://www.eetimes.com/worlds-first-single-chip-multiturn-position-sensor-in-smaller-form-factor/",
    "domain": "AI 算力 / 半导体",
    "title": "Worlds First Single Chip Multiturn Position Sensor in Smaller Form Factor",
    "url": "https://www.eetimes.com/worlds-first-single-chip-multiturn-position-sensor-in-smaller-form-factor/",
    "source": "Analog Devices",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T08:08:26+00:00",
    "summary": "Join this webinar, where our expert will explore the technology behind the ADMT4000 and how its ability to track multiple rotations and angular movement without power is transforming the design of bot"
  },
  {
    "id": "rss:https://www.eetimes.com/scaling-3d-ic-design-trends-challenges-and-practical-workflows/",
    "domain": "AI 算力 / 半导体",
    "title": "Scaling 3D IC design: Trends, Challenges and Practical Workflows",
    "url": "https://www.eetimes.com/scaling-3d-ic-design-trends-challenges-and-practical-workflows/",
    "source": "Siemens EDA",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T07:32:29+00:00",
    "summary": "Join us to discover how Siemens Innovator3D IC streamlines 3D IC design from planning to implementation! The post Scaling 3D IC design: Trends, Challenges and Practical Workflows appeared first on EE "
  },
  {
    "id": "rss:https://www.eetimes.com/why-custom-silicon-matters-in-ai-data-centers/",
    "domain": "AI 算力 / 半导体",
    "title": "Why Custom Silicon Matters in AI Data Centers",
    "url": "https://www.eetimes.com/why-custom-silicon-matters-in-ai-data-centers/",
    "source": "Scott Seal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T19:16:44+00:00",
    "summary": "Custom silicon lets AI data centers cut power, latency and data movement while improving economics at scale. The post Why Custom Silicon Matters in AI Data Centers appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/schiederwerk-showcases-novel-power-supply-solutions-for-mission-critical-applications-at-electronica-2026/",
    "domain": "AI 算力 / 半导体",
    "title": "SCHIEDERWERK Showcases Novel Power Supply Solutions for Mission-Critical Applications at electronica 2026",
    "url": "https://www.eetimes.com/schiederwerk-showcases-novel-power-supply-solutions-for-mission-critical-applications-at-electronica-2026/",
    "source": "SCHIEDERWERK",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T14:23:33+00:00",
    "summary": "Nuremberg / Munich, Germany, 2026 — SCHIEDERWERK GmbH, a specialist in custom power electronics solutions engineered and manufactured in Germany, will showcase its latest platform-based power supplies"
  },
  {
    "id": "rss:https://www.eetimes.com/nvidia-jetson-to-sima-ai-modalix-mlsoc-migration-guide/",
    "domain": "AI 算力 / 半导体",
    "title": "NVIDIA Jetson to SiMa.ai Modalix MLSoC Migration Guide",
    "url": "https://www.eetimes.com/nvidia-jetson-to-sima-ai-modalix-mlsoc-migration-guide/",
    "source": "SiMa Technologies, Inc.",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T14:00:00+00:00",
    "summary": "This technical guide provides a practical framework for migrating machine learning models and applications from an NVIDIA/CUDA-based environment to the SiMa.ai Physical AI platform. It explains the ke"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/gigabytes-latest-bios-update-hints-at-intels-raptor-lake-next-launch-in-2027-new-cpus-may-support-both-ddr4-and-ddr5-memory",
    "domain": "AI 算力 / 半导体",
    "title": "Gigabyte's latest BIOS update hints at Intel's Raptor Lake Next Launch in 2027",
    "url": "https://www.tomshardware.com/pc-components/cpus/gigabytes-latest-bios-update-hints-at-intels-raptor-lake-next-launch-in-2027-new-cpus-may-support-both-ddr4-and-ddr5-memory",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T13:43:01+00:00",
    "summary": "Gigabyte confirms BIOS support for upcoming Intel LGA 1700 processors on B760 and H610 motherboards, with the rumored Raptor Lake Next lineup expected in early 2027 to support both DDR4 and DDR5 memor"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/cloud-storage/microsoft-365-slashes-storage-capacity-for-shared-accounts-amid-industry-wide-shortages-2tb-limit-to-take-effect-after-april-2027",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft 365 slashes storage capacity for shared accounts amid industry-wide shortages",
    "url": "https://www.tomshardware.com/software/cloud-storage/microsoft-365-slashes-storage-capacity-for-shared-accounts-amid-industry-wide-shortages-2tb-limit-to-take-effect-after-april-2027",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T12:51:59+00:00",
    "summary": "This effectively increases the costs for large users, although it may benefit those who have family members that don't take up much cloud storage space."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/pc-shipments-tumble-over-20-percent-in-3q26-as-chip-shortages-bite-top-three-pc-vendors-ship-11-6-million-fewer-units-year-over-year",
    "domain": "AI 算力 / 半导体",
    "title": "PC shipments tumble over 20% in 3Q26 as chip shortages bite",
    "url": "https://www.tomshardware.com/tech-industry/pc-shipments-tumble-over-20-percent-in-3q26-as-chip-shortages-bite-top-three-pc-vendors-ship-11-6-million-fewer-units-year-over-year",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T11:10:05+00:00",
    "summary": "PC shipments for the third quarter of 2026 drop by 15.8 million units, with Lenovo, HP, and Dell being hit the hardest. Memory chip manufacturers estimate that the situation will not improve until 202"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/independent-tests-rank-mistrals-new-trillion-parameter-large-4-the-best-ai-model-outside-the-u-s-and-china-but-chinese-open-weights-still-overcome-europes-best-efforts",
    "domain": "AI 算力 / 半导体",
    "title": "Mistral’s new Large 4 trails some Chinese open models in independent tests",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/independent-tests-rank-mistrals-new-trillion-parameter-large-4-the-best-ai-model-outside-the-u-s-and-china-but-chinese-open-weights-still-overcome-europes-best-efforts",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T11:00:00+00:00",
    "summary": "Artificial Analysis scores Mistral’s new Large 4 at 38, behind open models from Xiaomi, Z.ai, Moonshot, and DeepSeek."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/grab-this-32-inch-4k-oled-gaming-monitor-from-asrock-for-the-super-low-price-of-usd596-dual-mode-refresh-rates-and-resolutions-let-you-switch-between-high-fidelity-and-esports-gaming",
    "domain": "AI 算力 / 半导体",
    "title": "Grab this 32-inch 4K OLED gaming monitor from ASRock for the super low price of $596",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/grab-this-32-inch-4k-oled-gaming-monitor-from-asrock-for-the-super-low-price-of-usd596-dual-mode-refresh-rates-and-resolutions-let-you-switch-between-high-fidelity-and-esports-gaming",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T10:56:13+00:00",
    "summary": "Save 33% on the 32-inch ASRock Phantom Gaming 4K OLED gaming monitor at Newegg."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/macbooks/save-usd200-on-the-2026-m5-macbook-air-right-now-undoing-apples-june-price-hike-with-prices-starting-from-usd1-099-amazon-deal-nets-you-current-gen-models-with-16gb-or-24gb-ram-and-up-to-1tb-storage",
    "domain": "AI 算力 / 半导体",
    "title": "Save $200 on the 2026 M5 MacBook Air right now, undoing Apple's June price hike with prices starting from $1,099",
    "url": "https://www.tomshardware.com/laptops/macbooks/save-usd200-on-the-2026-m5-macbook-air-right-now-undoing-apples-june-price-hike-with-prices-starting-from-usd1-099-amazon-deal-nets-you-current-gen-models-with-16gb-or-24gb-ram-and-up-to-1tb-storage",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T10:47:15+00:00",
    "summary": "Grab Apple's 2026 MacBook Air with M5 chip for $1,099 right now, a $200 price drop that knocks it back to its early 2026 pricing."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/kioxia-unveils-e1-l-ssds-for-hyperscalers-with-up-to-122-88tb-capacity-extreme-density-meets-compact-form-factor",
    "domain": "AI 算力 / 半导体",
    "title": "Kioxia unveils E1.L SSDs for hyperscalers with up to 122.88TB capacity",
    "url": "https://www.tomshardware.com/pc-components/ssds/kioxia-unveils-e1-l-ssds-for-hyperscalers-with-up-to-122-88tb-capacity-extreme-density-meets-compact-form-factor",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T10:30:00+00:00",
    "summary": "Kioxia's LD4-series SSDs can store up to 122.88TB of data in a compact form-factor, but its performance remains a mystery."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/arc-raiders-developer-uses-ai-to-detect-cheating-embark-cracks-down-on-cheaters-deploys-harsh-penalties-including-permaban-on-first-time-offenders",
    "domain": "AI 算力 / 半导体",
    "title": "Arc Raiders publisher developing AI anti-cheat stack in escalating war with cheaters",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/arc-raiders-developer-uses-ai-to-detect-cheating-embark-cracks-down-on-cheaters-deploys-harsh-penalties-including-permaban-on-first-time-offenders",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T10:00:00+00:00",
    "summary": "These strict measures are designed to deter players from cheating. Those caught will get a permaban that span accounts and even hardware in the future."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-tried-to-crush-the-megahertz-myth-25-years-ago-today-debuting-its-performance-rating-system-athlon-xp-chips-introduced-the-scheme-which-endured-until-intel-lost-its-clock-speed-advantage-with-pentium-m",
    "domain": "AI 算力 / 半导体",
    "title": "AMD attempted to crush the 'Megahertz myth' with its Performance Rating system on this day 25 years ago",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-tried-to-crush-the-megahertz-myth-25-years-ago-today-debuting-its-performance-rating-system-athlon-xp-chips-introduced-the-scheme-which-endured-until-intel-lost-its-clock-speed-advantage-with-pentium-m",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T09:30:00+00:00",
    "summary": "Today, a quarter of a century ago, AMD launched its AMD Athlon XP processor family and its Performance Rating (PR) naming scheme."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/globalfoundries-to-produce-silicon-interposers-for-tsmcs-cowos-in-the-us-five-year-agreement-valued-at-usd2-billion",
    "domain": "AI 算力 / 半导体",
    "title": "GlobalFoundries to produce silicon interposers for TSMC's CoWoS in the US",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/globalfoundries-to-produce-silicon-interposers-for-tsmcs-cowos-in-the-us-five-year-agreement-valued-at-usd2-billion",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T18:23:28+00:00",
    "summary": "GlobalFoundries becomes a part of TSMC's CoWoS supply chain in the U.S.: set to participate in production of leading-edge AI and HPC accelerators without investing in leading-edge process technologies"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/policy/u-s-suspends-green-card-path-for-h-1b-workers-at-microsoft-and-adobe-labor-certification-program-blocked-due-to-alleged-fraud",
    "domain": "AI 算力 / 半导体",
    "title": "U.S. suspends green card path for H-1B workers at Microsoft and Adobe",
    "url": "https://www.tomshardware.com/tech-industry/policy/u-s-suspends-green-card-path-for-h-1b-workers-at-microsoft-and-adobe-labor-certification-program-blocked-due-to-alleged-fraud",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T17:26:07+00:00",
    "summary": "U.S. suspends green card path for H-1B workers at Microsoft, Adobe, and IT outsourcing companies — PERM program blocked due to alleged fraud"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/the-atari-800xl-returns-with-a-faithful-but-modern-retro-games-ltd-redesign-classic-8-bit-home-computer-revamp-sports-mechanical-keyboard-and-hdmi-connectivity",
    "domain": "AI 算力 / 半导体",
    "title": "The Atari 800XL returns with a 'faithful' but modern Retro Games Ltd redesign",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/the-atari-800xl-returns-with-a-faithful-but-modern-retro-games-ltd-redesign-classic-8-bit-home-computer-revamp-sports-mechanical-keyboard-and-hdmi-connectivity",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T16:37:20+00:00",
    "summary": "Pre-orders for the Atari-licensed THE 800XL began today. This is a modernized yet claimed to be faithful recreation of the classic 8-bit home computer, popular in the early 1980s."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/department-of-war-dishes-out-usd1-5-billion-loan-commitment-to-boost-semiconductor-supply-chain-wolfspeed-to-focus-on-national-security-applications-as-part-of-30-year-agreement",
    "domain": "AI 算力 / 半导体",
    "title": "Department of War dishes out $1.5 billion loan commitment to boost semiconductor supply chain",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/department-of-war-dishes-out-usd1-5-billion-loan-commitment-to-boost-semiconductor-supply-chain-wolfspeed-to-focus-on-national-security-applications-as-part-of-30-year-agreement",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T16:24:54+00:00",
    "summary": "Wolfspeed has secured a conditional $1.5 billion, 30-year loan commitment from the U.S. Department of War to expand GaN epitaxy and radiation-hardened SiC and GaN technologies for U.S. national securi"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/finland-orders-google-to-stop-work-on-two-ai-data-centers-over-alleged-deforestation-company-admits-it-has-fallen-short-of-our-own-high-standards-in-this-instance",
    "domain": "AI 算力 / 半导体",
    "title": "Finland orders Google to stop work on two AI data centers over alleged deforestation",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/finland-orders-google-to-stop-work-on-two-ai-data-centers-over-alleged-deforestation-company-admits-it-has-fallen-short-of-our-own-high-standards-in-this-instance",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T15:52:45+00:00",
    "summary": "Finnish authorities say they cannot conduct a proper environmental assessment after the site has already been changed."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/bambu-labs-3d-printing-patent-application-for-a-new-heatbed-design-may-improve-peeling-issues-replacement-costs-could-possibly-rise-as-a-consequence",
    "domain": "AI 算力 / 半导体",
    "title": "Bambu Lab’s 3D printing patent application for a new heatbed design may improve peeling issues",
    "url": "https://www.tomshardware.com/3d-printing/bambu-labs-3d-printing-patent-application-for-a-new-heatbed-design-may-improve-peeling-issues-replacement-costs-could-possibly-rise-as-a-consequence",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T14:11:49+00:00",
    "summary": "Bambu Lab applied to patent its new heatbed design that might finally solve bed adhesion problems for large prints."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/software-could-be-the-easiest-fix-for-hyperscalers-ai-power-squeeze-researchers-say-data-center-demand-is-expected-to-rival-japans-electricity-usage-by-2030",
    "domain": "AI 算力 / 半导体",
    "title": "Software could be the easiest fix for hyperscalers' AI power squeeze, researchers say",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/software-could-be-the-easiest-fix-for-hyperscalers-ai-power-squeeze-researchers-say-data-center-demand-is-expected-to-rival-japans-electricity-usage-by-2030",
    "source": "Chris Stokel-Walker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T14:00:00+00:00",
    "summary": "The industry is spending billions on more efficient chips, cooling, and grid connections. But what about making computers do less work – or doing it at a better time?"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/ukrainian-drones-hit-russias-yandex-data-centers-housing-two-top-supercomputers-major-outage-follows-retaliatory-strike",
    "domain": "AI 算力 / 半导体",
    "title": "Ukrainian drones hit Russia's Yandex data centers housing two top supercomputers",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/ukrainian-drones-hit-russias-yandex-data-centers-housing-two-top-supercomputers-major-outage-follows-retaliatory-strike",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T13:46:56+00:00",
    "summary": "No more AI training in Russia? Destiny of two Nvidia-powered Russian supercomputers is unknown as drones hit Yandex data center in Sasovo."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/amd-seeks-broader-partnership-with-samsung-as-it-looks-to-secure-memory-supply-samsung-reportedly-hopes-to-turn-its-memory-supply-relationship-with-amd-into-foundry-orders-for-logic-chips",
    "domain": "AI 算力 / 半导体",
    "title": "AMD seeks 'broader partnership' with Samsung as it looks to secure memory supply",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/amd-seeks-broader-partnership-with-samsung-as-it-looks-to-secure-memory-supply-samsung-reportedly-hopes-to-turn-its-memory-supply-relationship-with-amd-into-foundry-orders-for-logic-chips",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T12:30:00+00:00",
    "summary": "AMD is pursuing a 'broader partnership' with Samsung as memory company wants to tie advanced memory supply to its orders at its foundry unit."
  },
  {
    "id": "rss:https://www.tomshardware.com/service-providers/streaming/american-jailed-for-commanding-10-000-bots-to-stream-his-own-ai-generated-songs-and-earn-millions-in-fraudulent-royalty-payments-beating-taylor-swift-is-the-first-person-to-end-up-in-prison-for-ai-assisted-music-streaming-crime",
    "domain": "AI 算力 / 半导体",
    "title": "American jailed for commanding 10,000 bots to stream his own AI-generated songs",
    "url": "https://www.tomshardware.com/service-providers/streaming/american-jailed-for-commanding-10-000-bots-to-stream-his-own-ai-generated-songs-and-earn-millions-in-fraudulent-royalty-payments-beating-taylor-swift-is-the-first-person-to-end-up-in-prison-for-ai-assisted-music-streaming-crime",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T12:19:45+00:00",
    "summary": "The first-ever criminal case involving AI-assisted music streaming fraud has concluded, with an American citizen facing 18 months behind bars and an $8M fine."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/researcher-develops-method-for-fingerprinting-cheaters-using-counter-strike-mouse-and-keyboard-input-patterns-says-technique-can-be-used-so-bans-follow-users-even-if-they-make-new-accounts",
    "domain": "AI 算力 / 半导体",
    "title": "Researcher develops method for fingerprinting cheaters using Counter-Strike mouse and keyboard input patterns",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/researcher-develops-method-for-fingerprinting-cheaters-using-counter-strike-mouse-and-keyboard-input-patterns-says-technique-can-be-used-so-bans-follow-users-even-if-they-make-new-accounts",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T12:10:58+00:00",
    "summary": "u/Magga_ built a method that identified players by looking at how they use their mouse and keyboard. They can then use this to ensure that bans follow cheaters, even if they make new accounts from ano"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amds-epyc-verano-ai-host-cpu-will-reportedly-use-a-special-sb1-socket-zen-6-chip-pairs-72-cores-with-a-24-channel-lpddr5x-memory-subsystem",
    "domain": "AI 算力 / 半导体",
    "title": "AMD's EPYC Verano AI host CPU will reportedly use a special SB1 socket",
    "url": "https://www.tomshardware.com/pc-components/cpus/amds-epyc-verano-ai-host-cpu-will-reportedly-use-a-special-sb1-socket-zen-6-chip-pairs-72-cores-with-a-24-channel-lpddr5x-memory-subsystem",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T12:00:00+00:00",
    "summary": "Dynatron quietly unveils air cooler for AMD's EPYC 'Verano' CPUs aimed at AI servers."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/applications/spotifast-lets-you-enjoy-spotify-tracks-while-lowering-ram-usage-by-5x-or-more-open-source-app-cuts-ram-usage-down-to-150-mb-and-brings-back-classic-winamp-skins",
    "domain": "AI 算力 / 半导体",
    "title": "Spotifast lets you enjoy Spotify tracks while lowering RAM usage by 5x or more",
    "url": "https://www.tomshardware.com/software/applications/spotifast-lets-you-enjoy-spotify-tracks-while-lowering-ram-usage-by-5x-or-more-open-source-app-cuts-ram-usage-down-to-150-mb-and-brings-back-classic-winamp-skins",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T11:30:00+00:00",
    "summary": "Spotifast lets you enjoy Spotify tracks while lowering RAM usage by 5x or more — alternative client also packs Winamp skins and Milkdrop visualizations."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/china-allegedly-intercepted-ups-shipped-f-35-parts-after-employee-missed-email-warning-worker-decided-to-divert-through-hong-kong-to-speed-up-delivery",
    "domain": "AI 算力 / 半导体",
    "title": "China allegedly intercepted UPS-shipped F-35 parts after employee missed email warning",
    "url": "https://www.tomshardware.com/tech-industry/china-allegedly-intercepted-ups-shipped-f-35-parts-after-employee-missed-email-warning-worker-decided-to-divert-through-hong-kong-to-speed-up-delivery",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T11:06:12+00:00",
    "summary": "A UPS worker missed an important email about securely routing top-secret F-35 parts so mistakenly opted for a Hong Kong transit for faster shipping."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/spacex-reportedly-seeking-usd40-billion-debt-package-for-nvidia-ai-hardware-massive-raise-could-fund-roughly-360-000-vera-rubin-gpus-across-5-000-nvl72-racks",
    "domain": "AI 算力 / 半导体",
    "title": "SpaceX reportedly seeking $40 billion debt package for Nvidia AI hardware",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/spacex-reportedly-seeking-usd40-billion-debt-package-for-nvidia-ai-hardware-massive-raise-could-fund-roughly-360-000-vera-rubin-gpus-across-5-000-nvl72-racks",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T11:00:00+00:00",
    "summary": "SpaceX reportedly intends to borrow $40 billion to procure 360,000 Nvidia Rubin AI accelerators, infrastructure."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/former-groq-engineers-sue-board-over-usd20-billion-nvidia-deal-saying-it-handed-nvidia-the-lpu-and-the-team-that-built-it-plaintiffs-allege-the-board-kept-billions-from-other-shareholders",
    "domain": "AI 算力 / 半导体",
    "title": "Former Groq engineers sue board over $20 billion Nvidia deal",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/former-groq-engineers-sue-board-over-usd20-billion-nvidia-deal-saying-it-handed-nvidia-the-lpu-and-the-team-that-built-it-plaintiffs-allege-the-board-kept-billions-from-other-shareholders",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T11:00:00+00:00",
    "summary": "Two former Groq engineers sued Groq’s board in Delaware over the Nvidia licensing deal behind the Groq 3 LPU."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/score-a-1080p-gaming-pc-for-less-than-usd1-000-right-now-fitted-with-nvidia-or-amd-gpus-save-up-to-usd350-to-secure-rigs-with-rtx-5060-or-rx-9060-gpus-at-low-prices",
    "domain": "AI 算力 / 半导体",
    "title": "Score a 1080p gaming PC for less than $1,000 right now, fitted with Nvidia or AMD GPUs",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/score-a-1080p-gaming-pc-for-less-than-usd1-000-right-now-fitted-with-nvidia-or-amd-gpus-save-up-to-usd350-to-secure-rigs-with-rtx-5060-or-rx-9060-gpus-at-low-prices",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T10:57:45+00:00",
    "summary": "Two gaming PCs capable of 1080p gameplay have dropped below $1,000, a price that's hard to beat in the current market, thanks to sales at Best Buy and Walmart."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/make-the-jump-to-an-oled-gaming-monitor-and-save-48-percent-lgs-massive-45-inch-ultragear-screen-hits-its-lowest-price",
    "domain": "AI 算力 / 半导体",
    "title": "Make the jump to an OLED gaming monitor and save 48%",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/make-the-jump-to-an-oled-gaming-monitor-and-save-48-percent-lgs-massive-45-inch-ultragear-screen-hits-its-lowest-price",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T10:46:50+00:00",
    "summary": "Save 48% on the 45-inch LG 45GX900A-B OLED gaming monitor at Amazon."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/taiwan-indicts-10-for-smuggling-us-military-grade-chips-to-china-parts-routed-to-missile-and-radar-programs-using-forged-taiwan-defense-institute-orders-texas-instruments-and-analog-devices-hardware-passed-off-as-made-in-taiwan",
    "domain": "AI 算力 / 半导体",
    "title": "Taiwan indicts 10 for smuggling US military-grade chips to China, parts routed to missile and radar programs using forged Taiwan defense institute orders",
    "url": "https://www.tomshardware.com/tech-industry/taiwan-indicts-10-for-smuggling-us-military-grade-chips-to-china-parts-routed-to-missile-and-radar-programs-using-forged-taiwan-defense-institute-orders-texas-instruments-and-analog-devices-hardware-passed-off-as-made-in-taiwan",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T10:30:00+00:00",
    "summary": "Taiwanese prosecutors indicted 10 company heads over Texas Instruments and Analog Devices chips allegedly resold to China."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/video-editing-graphic-design/solo-developer-rebuilds-adobe-creative-suite-in-rust-using-claude-releases-it-free-to-all-targets-100-percent-parity-in-one-month-despite-piracy-claims-and-safety-warnings",
    "domain": "AI 算力 / 半导体",
    "title": "Solo developer rebuilds Adobe Creative Suite in Rust using Claude, releases it free to all",
    "url": "https://www.tomshardware.com/software/video-editing-graphic-design/solo-developer-rebuilds-adobe-creative-suite-in-rust-using-claude-releases-it-free-to-all-targets-100-percent-parity-in-one-month-despite-piracy-claims-and-safety-warnings",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T10:00:00+00:00",
    "summary": "Multiple Adobe creative tools were recreated using Claude and made open-source by one person."
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
    "id": "rss:https://www.tomshardware.com/networking/it-pro-says-his-parents-keurig-smart-coffee-maker-sent-1tb-of-data-over-their-wi-fi-in-10-days-it-saturated-an-access-point-on-its-own-but-he-says-most-of-the-traffic-never-left-the-home-network",
    "domain": "AI 算力 / 半导体",
    "title": "IT pro says his parents’ Keurig smart coffee maker sent 1TB of data over their Wi-Fi in 10 days",
    "url": "https://www.tomshardware.com/networking/it-pro-says-his-parents-keurig-smart-coffee-maker-sent-1tb-of-data-over-their-wi-fi-in-10-days-it-saturated-an-access-point-on-its-own-but-he-says-most-of-the-traffic-never-left-the-home-network",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T09:30:00+00:00",
    "summary": "A Keurig K-Supreme SMART coffee maker sent about 1TB over a family’s home Wi-Fi in 10 days, saturating an access point."
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
    "points": 1704,
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
    "points": 771,
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
    "id": "hn:49996713",
    "domain": "大厂 AI 动态",
    "title": "I'm not paying $20 for ChatGPT or Claude because a free local LLM does",
    "url": "https://www.xda-developers.com/im-not-paying-20-for-chatgpt-claude-or-gemini-because-a-free-local-llm-does-everything-i-need/",
    "source": "hsnewman",
    "platform": "hackernews",
    "points": 52,
    "published_at": "2026-10-07T18:19:03+00:00",
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
    "id": "hn:49993338",
    "domain": "大厂 AI 动态",
    "title": "Tell HN: Apple not letting removal of AI models on macOS 27 is outrageous",
    "url": "https://news.ycombinator.com/item?id=49993338",
    "source": "busymom0",
    "platform": "hackernews",
    "points": 37,
    "published_at": "2026-10-07T14:26:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:50000431",
    "domain": "大厂 AI 动态",
    "title": "100 days later: Microsoft still steers Windows and Copilot users to Edge",
    "url": "https://blog.mozilla.org/en/mozilla/over-the-edge-2-100-days-later/",
    "source": "thimabi",
    "platform": "hackernews",
    "points": 34,
    "published_at": "2026-10-08T00:06:27+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1007674/smart-bird-feeders-attact-pests-too",
    "domain": "大厂 AI 动态",
    "title": "My brief romance with an AI bird feeder",
    "url": "https://www.theverge.com/gadgets/1007674/smart-bird-feeders-attact-pests-too",
    "source": "Thomas Ricker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-10T07:00:00+00:00",
    "summary": "It started off promising enough. Dozens of tiny, colorful birds were drawn to my garden just a few weeks after I mounted a $350 $269 Kiwibit Bird Feeder 2 Pro. \"Looks like Great Tit!\" read the first A"
  },
  {
    "id": "rss:https://www.theverge.com/games/1009140/ram-shortage-intel-amd-ddr4-comeback",
    "domain": "大厂 AI 动态",
    "title": "Decade-old RAM is making a comeback",
    "url": "https://www.theverge.com/games/1009140/ram-shortage-intel-amd-ddr4-comeback",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T21:50:00+00:00",
    "summary": "CPU makers have noticed that the seemingly unending RAM price hikes are making it tough for a lot of us to upgrade our PCs. Their solution? A return to last-gen DDR4 RAM. Intel and AMD are making new "
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1009090/anthropic-fake-homicide-information-philadelphia-pd-tip",
    "domain": "大厂 AI 动态",
    "title": "Anthropic’s AI gave Philadelphia police a fake tip about an unsolved homicide",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1009090/anthropic-fake-homicide-information-philadelphia-pd-tip",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T21:15:38+00:00",
    "summary": "An Anthropic AI model provided false information about an unsolved homicide to a Philadelphia Police Department (PPD) tipline, according to a report from 6abc. In a statement released on Friday, the P"
  },
  {
    "id": "rss:https://www.theverge.com/policy/1008991/ohio-blogger-harassment-shrek-nude",
    "domain": "大厂 AI 动态",
    "title": "Ohio blogger found guilty of harassment for sending Shrek nude to senator",
    "url": "https://www.theverge.com/policy/1008991/ohio-blogger-harassment-shrek-nude",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T19:41:11+00:00",
    "summary": "A jury found an Ohio political blogger guilty of telecommunications harassment after he sent an explicit image of Shrek to a Republican state senator. On Friday, a judge ordered DJ Byrnes, owner of po"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1008726/openai-mathematics-solutions-chaos",
    "domain": "大厂 AI 动态",
    "title": "&#8216;Pure insanity&#8217;: Mathematicians will need years to make sense of OpenAI&#8217;s latest drop",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1008726/openai-mathematics-solutions-chaos",
    "source": "Robert Hart",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T19:09:44+00:00",
    "summary": "\"Staggering.\" \"Overwhelming.\" \"Unprecedented.\" \"Surreal.\" \"Pure insanity.\" Those were among the descriptions more than three dozen mathematicians reached for in conversations with The Verge as they tr"
  },
  {
    "id": "rss:https://www.theverge.com/policy/1008950/fcc-brendan-carr-pete-hegseth-execution-tv-networks-air",
    "domain": "大厂 AI 动态",
    "title": "Brendan Carr says he&#8217;ll let Pete Hegseth decide whether TV networks can air the public execution",
    "url": "https://www.theverge.com/policy/1008950/fcc-brendan-carr-pete-hegseth-execution-tv-networks-air",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T18:30:48+00:00",
    "summary": "FCC chairman Brendan Carr said he will defer to Secretary of Defense Pete Hegseth on whether TV networks can air the planned execution of convicted Fort Hood shooter Nidal Hasan by firing squad. The P"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1008930/nikon-small-world-in-motion-winner-ai",
    "domain": "大厂 AI 动态",
    "title": "Nikon microscopic video competition winner disqualified for using generative AI",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1008930/nikon-small-world-in-motion-winner-ai",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T18:06:57+00:00",
    "summary": "Nikon says the video that originally won first place in its Small World in Motion contest \"did not comply with the competition rules regarding generative AI.\" BBC reports that the original first place"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1008918/google-fitbit-edge-launch-next-week",
    "domain": "大厂 AI 动态",
    "title": "Google teases Fitbit Edge launch next week",
    "url": "https://www.theverge.com/tech/1008918/google-fitbit-edge-launch-next-week",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T18:05:55+00:00",
    "summary": "It looks like Google is getting ready to take the wraps off its rumored Fitbit Edge next Monday. In a post on X, Google posted a picture of what appears to be the side of the fitness tracker, with the"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1008857/samsung-galaxy-s26-ultra-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "The Samsung Galaxy S26 Ultra is down to $950 after Prime Day",
    "url": "https://www.theverge.com/gadgets/1008857/samsung-galaxy-s26-ultra-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T17:41:24+00:00",
    "summary": "Amazon has the Samsung Galaxy S26 Ultra in black with 256GB of storage discounted to $949.99, a healthy discount from its usual price of $1,399.99. This phone’s standout feature is the adjustable priv"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1008833/amazon-kindle-light-leak",
    "domain": "大厂 AI 动态",
    "title": "Amazon’s new Kindles appear to have a light leak problem",
    "url": "https://www.theverge.com/tech/1008833/amazon-kindle-light-leak",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T17:25:39+00:00",
    "summary": "Some users are reporting that the new Kindles have a light leak issue that is especially apparent when using dark mode. The latest base-model Kindles have a flush bezel that gives them a sleek appeara"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/09/elon-musk-intensifies-attack-on-ambani-over-starlink-india-launch-delay/",
    "domain": "大厂 AI 动态",
    "title": "Elon Musk intensifies attack on Ambani over Starlink India launch delay",
    "url": "https://techcrunch.com/2026/10/09/elon-musk-intensifies-attack-on-ambani-over-starlink-india-launch-delay/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-10T03:10:06+00:00",
    "summary": "Elon Musk has accused Indian billionaire Mukesh Ambani of blocking competition."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/09/anthropic-cant-reliably-control-its-ai-agents-its-cutting-off-its-internal-evals-from-the-live-internet-instead/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic can’t reliably control its AI agents. It’s cutting off its internal evals from the live internet instead",
    "url": "https://techcrunch.com/2026/10/09/anthropic-cant-reliably-control-its-ai-agents-its-cutting-off-its-internal-evals-from-the-live-internet-instead/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-10T00:18:32+00:00",
    "summary": "Anthropic said it \"turned off live internet access\" for \"all our internal evaluations\" until further notice."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/09/long-live-the-mechanical-keyboard/",
    "domain": "大厂 AI 动态",
    "title": "Long live the mechanical keyboard",
    "url": "https://techcrunch.com/2026/10/09/long-live-the-mechanical-keyboard/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T22:08:24+00:00",
    "summary": "Keychron made a name for itself after launching on Kickstarter in 2017. Today, it offers the value K2 model as well as a variety of other versions, including one with an all-wood body."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/09/the-maker-of-non-text-ai-model-jev-valued-at-7-5b-just-weeks-after-launch/",
    "domain": "大厂 AI 动态",
    "title": "The maker of non-text AI model Jev valued at $7.5B just weeks after launch",
    "url": "https://techcrunch.com/2026/10/09/the-maker-of-non-text-ai-model-jev-valued-at-7-5b-just-weeks-after-launch/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T21:41:29+00:00",
    "summary": "What has users and large corporations so excited about Jev is TypeSafe’s claim that it works significantly faster and uses far fewer tokens than LLMs."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/09/an-anthropic-ai-model-sent-a-false-homicide-tip-to-philadelphia-police/",
    "domain": "大厂 AI 动态",
    "title": "An Anthropic AI model sent a false homicide tip to Philadelphia police",
    "url": "https://techcrunch.com/2026/10/09/an-anthropic-ai-model-sent-a-false-homicide-tip-to-philadelphia-police/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T19:36:56+00:00",
    "summary": "Anthropic did not discover this behavior until over two months after its AI submitted the false tip."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/09/batteries-are-now-cheaper-than-natural-gas-turbines-used-at-many-data-centers/",
    "domain": "大厂 AI 动态",
    "title": "Batteries are now cheaper than natural gas turbines used at many data centers",
    "url": "https://techcrunch.com/2026/10/09/batteries-are-now-cheaper-than-natural-gas-turbines-used-at-many-data-centers/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T18:57:58+00:00",
    "summary": "Batteries are now cheaper than natural gas turbines as the data center boom pushes prices up."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/09/techcrunch-disrupt-2026-gammas-grant-lee-engines-elia-wallen-and-gvs-crystal-huang-on-landing-your-first-1000-customers/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Disrupt 2026: Gamma’s Grant Lee, Engine’s Elia Wallen, and GV’s Crystal Huang on landing your first 1,000 customers",
    "url": "https://techcrunch.com/2026/10/09/techcrunch-disrupt-2026-gammas-grant-lee-engines-elia-wallen-and-gvs-crystal-huang-on-landing-your-first-1000-customers/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T18:57:06+00:00",
    "summary": "Leaders from Gamma, Engine, and Google Ventures join TechCrunch Disrupt 2026 to talk how to get your first customers. Register now to save up to $100. Grab a second pass at 50% off."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/09/lumenus-helps-automate-tedious-paperwork-in-times-of-grief/",
    "domain": "大厂 AI 动态",
    "title": "LumenUs helps automate tedious paperwork in times of grief",
    "url": "https://techcrunch.com/2026/10/09/lumenus-helps-automate-tedious-paperwork-in-times-of-grief/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T17:00:00+00:00",
    "summary": "\"The day your loved one passes away, you also get this honorary badge of a project manager for a project you had no idea about,\" said founder Sara Tashakorinia."
  },
  {
    "id": "rss:https://techcrunch.com/video/amazon-and-others-are-done-keeping-data-center-deals-secret-is-it-enough-to-build-trust/",
    "domain": "大厂 AI 动态",
    "title": "Amazon and others are done keeping data center deals secret. Is it enough to build trust?",
    "url": "https://techcrunch.com/video/amazon-and-others-are-done-keeping-data-center-deals-secret-is-it-enough-to-build-trust/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T16:56:42+00:00",
    "summary": "Amazon says it will&#160;stop using NDAs&#160;when negotiating data center deals with local governments, following&#160;a&#160;similar move from Microsoft&#160;earlier this year. Secrecy has fueled co"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/09/danu-robotics-fight-to-build-a-better-recycling-robot/",
    "domain": "大厂 AI 动态",
    "title": "Danu Robotics’ fight to build a better recycling robot",
    "url": "https://techcrunch.com/2026/10/09/danu-robotics-fight-to-build-a-better-recycling-robot/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T16:45:00+00:00",
    "summary": "For six years, Danu founder Amy Ma has been working on a better way to sort recyclable waste."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/09/we-cant-help-treating-ai-like-its-human-but-should-we/",
    "domain": "大厂 AI 动态",
    "title": "We can’t help treating AI like it’s human. But should we?",
    "url": "https://techcrunch.com/2026/10/09/we-cant-help-treating-ai-like-its-human-but-should-we/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T16:40:14+00:00",
    "summary": "\"When we are drawn into even the most primitive exchanges with a relational artifact, we believe it cares for us,\" Dr. Sherry Turkle writes. \"And we are wired to care for it in return.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/09/tesla-renames-full-self-driving-to-tesla-assisted-driving-in-europe/",
    "domain": "大厂 AI 动态",
    "title": "Tesla renames ‘Full Self-Driving’ to ‘Tesla Assisted Driving’ in Europe",
    "url": "https://techcrunch.com/2026/10/09/tesla-renames-full-self-driving-to-tesla-assisted-driving-in-europe/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T16:07:26+00:00",
    "summary": "The name change is enough for Germany's transport minister to start advocating for Europe-wide adoption of the driver assistance software."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/09/remember-orkut-its-founder-wants-to-bring-it-back/",
    "domain": "大厂 AI 动态",
    "title": "Remember Orkut? Its founder wants to bring it back",
    "url": "https://techcrunch.com/2026/10/09/remember-orkut-its-founder-wants-to-bring-it-back/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T15:56:15+00:00",
    "summary": "Orkut's founder is now taking aim at algorithms and AI-generated content."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/09/a16zs-olivia-moore-on-the-state-of-consumer-ai/",
    "domain": "大厂 AI 动态",
    "title": "a16z’s Olivia Moore on the state of consumer AI",
    "url": "https://techcrunch.com/2026/10/09/a16zs-olivia-moore-on-the-state-of-consumer-ai/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T15:43:33+00:00",
    "summary": "Moore sees a huge opportunity in consumer AI, particularly if the industry can tap into revenue streams beyond just subscriptions and API charges."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/09/automattic-loses-its-interim-cfo-just-weeks-after-boardroom-shakeup/",
    "domain": "大厂 AI 动态",
    "title": "Automattic interim CFO resigns just weeks after boardroom shakeup",
    "url": "https://techcrunch.com/2026/10/09/automattic-loses-its-interim-cfo-just-weeks-after-boardroom-shakeup/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T15:02:30+00:00",
    "summary": "Automattic's interim chief financial officer Jeremy Klaperman has left the company less than a month after taking the role, TechCrunch has learned. Sources say his departure followed a demotion back t"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/09/beyond-techcrunch-disrupt-2026-the-side-events-parties-networking-you-cant-miss/",
    "domain": "大厂 AI 动态",
    "title": "Beyond TechCrunch Disrupt 2026: The Side Events, Parties & Networking You Can’t Miss",
    "url": "https://techcrunch.com/2026/10/09/beyond-techcrunch-disrupt-2026-the-side-events-parties-networking-you-cant-miss/",
    "source": "Jean Bradley, TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T14:42:34+00:00",
    "summary": "TechCrunch Disrupt 2026 is just the beginning. From exclusive networking events and startup showcases to happy hours, dinners, and after-hours meetups, discover what’s happening across San Francisco d"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/09/techcrunch-disrupt-2026-starts-in-4-days-lock-in-your-pass-savings-of-up-to-100-before-prices-rise/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Disrupt 2026 starts in 4 days — lock in your pass savings of up to $100 before prices rise",
    "url": "https://techcrunch.com/2026/10/09/techcrunch-disrupt-2026-starts-in-4-days-lock-in-your-pass-savings-of-up-to-100-before-prices-rise/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T14:00:00+00:00",
    "summary": "Four days until TechCrunch Disrupt 2026 starts, when 10,000 founders, investors, and tech leaders gather in San Francisco's Moscone West on October 13-15. Save up to $100 on your price. Plus, save 50%"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/09/surveillance-company-flock-cuts-staff-as-privacy-backlash-grows/",
    "domain": "大厂 AI 动态",
    "title": "Surveillance company Flock cuts staff as privacy backlash grows",
    "url": "https://techcrunch.com/2026/10/09/surveillance-company-flock-cuts-staff-as-privacy-backlash-grows/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T13:40:36+00:00",
    "summary": "Flock would not say if CEO Garrett Langley would take a pay cut following the reduction in workforce."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/09/xonas-commercial-gps-alternative-is-about-to-go-live/",
    "domain": "大厂 AI 动态",
    "title": "Xona’s commercial GPS alternative is about to go live",
    "url": "https://techcrunch.com/2026/10/09/xonas-commercial-gps-alternative-is-about-to-go-live/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T12:00:00+00:00",
    "summary": "Xona's precision timing and navigation service will enter beta testing after SpaceX launches six satellites designed by the company."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/08/president-trump-awards-big-tech-donors-with-nations-highest-science-prizes/",
    "domain": "大厂 AI 动态",
    "title": "President Trump awards Big Tech donors with nation’s highest science prizes",
    "url": "https://techcrunch.com/2026/10/08/president-trump-awards-big-tech-donors-with-nations-highest-science-prizes/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T22:33:59+00:00",
    "summary": "Together, the awardees have donated nearly $6 billion to efforts tied to Trump and his administration."
  },
  {
    "id": "rss:https://stratechery.com/2026/its-not-you-its-me/",
    "domain": "大厂 AI 动态",
    "title": "2026.41: It’s Not You, It’s Me",
    "url": "https://stratechery.com/2026/its-not-you-its-me/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T17:00:00+00:00",
    "summary": "The best Stratechery content from the week of October 5, 2026, including drifting apart from Apple, Facebook complications, and the delightful absurdity of U.S.-China dynamics."
  },
  {
    "id": "rss:https://stratechery.com/2026/an-interview-with-katie-harbath-about-disrupting-politics-at-facebook/",
    "domain": "大厂 AI 动态",
    "title": "An Interview with Katie Harbath About Disrupting Politics at Facebook",
    "url": "https://stratechery.com/2026/an-interview-with-katie-harbath-about-disrupting-politics-at-facebook/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T10:00:00+00:00",
    "summary": "An interview with former Facebook Head of Global Elections Katie Harbath about her new book Disrupting Politics, and how things change for the company in the 2010s."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/10/neanderthal-wooden-tools-from-spain-found-preserved-in-stone/",
    "domain": "大厂 AI 动态",
    "title": "Neanderthal wooden tools from Spain found preserved in stone",
    "url": "https://arstechnica.com/science/2026/10/neanderthal-wooden-tools-from-spain-found-preserved-in-stone/",
    "source": "Jacek Krywko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T22:34:03+00:00",
    "summary": "Dissolved rock precipitated around the tools, which then decayed."
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
    "id": "hn:50029452",
    "domain": "股票",
    "title": "Data Center Darling's $30B IPO Dream Crushed in 48 Hours",
    "url": "https://www.bloomberg.com/news/articles/2026-10-09/data-center-darling-s-30-billion-ipo-dream-crushed-in-48-hours",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 37,
    "published_at": "2026-10-10T04:04:17+00:00",
    "summary": ""
  },
  {
    "id": "hn:50019535",
    "domain": "股票",
    "title": "Meadows – a small language for stock-and-flow diagrams that run",
    "url": "https://lorezzed.github.io/meadows/",
    "source": "jjsalamon",
    "platform": "hackernews",
    "points": 30,
    "published_at": "2026-10-09T12:29:40+00:00",
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
    "points": 502,
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
    "id": "hn:50023065",
    "domain": "金融",
    "title": "Tesla Rebrands Full Self-Driving as Tesla Assisted Driving in Europe",
    "url": "https://qz.com/tesla-full-self-driving-rebranding-europe-assisted-driving-100926",
    "source": "ilreb",
    "platform": "hackernews",
    "points": 50,
    "published_at": "2026-10-09T16:38:20+00:00",
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
    "id": "hn:50029232",
    "domain": "金融",
    "title": "Data centre company's much-hyped Australian stock market listing imploded",
    "url": "https://www.theguardian.com/australia-news/2026/oct/09/firmus-australian-stock-market-listing-bust-finance",
    "source": "stubish",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-10-10T03:23:09+00:00",
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
    "id": "hn:49938815",
    "domain": "金融",
    "title": "Federal Judge Rules a Flock Search Was Unconstitutional",
    "url": "https://www.404media.co/federal-judge-rules-a-flock-search-was-indiscriminate-mass-surveillance-and-unconstitutional/",
    "source": "pavel_lishin",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-10-02T21:28:59+00:00",
    "summary": ""
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
    "id": "hn:49908455",
    "domain": "金融",
    "title": "European Network for Payments – An EU Alternative to Visa/Mastercard",
    "url": "https://www.reuters.com/business/finance/european-payments-groups-join-forces-lessen-us-reliance-2026-09-30/",
    "source": "monegator",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-09-30T13:11:29+00:00",
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
  }
]
```
