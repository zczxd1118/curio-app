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

- 今日日期：`2026-09-12`
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
  "date": "2026-09-12",
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
    "id": "bvid:BV1rpWjevEip",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的Python零基础全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！",
    "url": "http://www.bilibili.com/video/av113006243481679",
    "source": "Python官方课程",
    "platform": "bilibili",
    "points": 19730954,
    "published_at": "2024-08-22T14:59:18+00:00",
    "summary": "【视频配套籽料、开发环境搭建安装包教程、电子书+问题解答请看 ”置顶平论” 自取哦】\r\n本套教程从零开始讲解，手把手教学，包含基础语法、进阶语法、爬虫、自动化办公、数据分析\r\n无论是新手小白，还是有一定编码经验的选手，皆可学习\r\n如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！"
  },
  {
    "id": "bvid:BV1BVEs6LENZ",
    "domain": "AI",
    "title": "【2026最新Codex】Codex保姆级完整教程-Codex新手保姆级教程-最强AI助手！从入门到进阶，22分钟速通Codex！【附教程文档安装包】",
    "url": "http://www.bilibili.com/video/av116707129561197",
    "source": "编程大佬陈悠秀",
    "platform": "bilibili",
    "points": 2681832,
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
    "points": 1901775,
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
    "points": 1850600,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1j9MP6wEV9",
    "domain": "AI",
    "title": "从零开始，学会让桌面Agent帮你干活！【小白教程】",
    "url": "http://www.bilibili.com/video/av116861865887789",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 1355118,
    "published_at": "2026-07-05T02:00:00+00:00",
    "summary": "用不上codex的朋友们！新的国产Agent直接上手，来跑通8大用法～\n感谢朋友们的三连+关注～"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 1278063,
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
    "points": 1200608,
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
    "points": 884635,
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
    "points": 807360,
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
    "points": 751578,
    "published_at": "2026-07-01T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260701\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\nAI大模型开发热门教程：\nAI大模型开发：BV1h1"
  },
  {
    "id": "bvid:BV1ABu96JEAR",
    "domain": "AI",
    "title": "【保姆级教程】WorkBuddy彻底玩明白！只看这一期就够了！10节付费课内容全公开，完整工作流+实战技巧全揭秘，零基础一小时从入门到精通【附完整资料】",
    "url": "http://www.bilibili.com/video/av117069685262348",
    "source": "workbuddy应用实战",
    "platform": "bilibili",
    "points": 616844,
    "published_at": "2026-08-10T06:05:50+00:00",
    "summary": "这可能是B站最全的WorkBuddy免费教程。咱们把付费课程做成了免费课程，感谢观众大老爷的两币奉上，有喜欢的也可以一键三连。 评论“蓝皮书”领取全套资料\n我花了整整一周，从安装到实战到管理思维，把WorkBuddy这个腾讯云AI桌面工作台拆成了10步，每一步都带实操。你不需要任何基础，跟着点就行。"
  },
  {
    "id": "bvid:BV1ia9UBPESQ",
    "domain": "AI",
    "title": "在VScode中配置Claude Code并接入DeepSeek V4 Pro【oo唠嗑教程】",
    "url": "http://www.bilibili.com/video/av116487012549813",
    "source": "沉默的羔丸ovo",
    "platform": "bilibili",
    "points": 331905,
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
    "points": 286909,
    "published_at": "2025-04-15T00:59:13+00:00",
    "summary": "MCP终极指南 - 带你深入掌握MCP（基础篇）\n\n时间轴：\n01:05 MCP简要介绍\n02:47 安装 MCP Host（Cline）\n03:15 配置 Cline 用的 API Key\n06:01 第一个 MCP 问题\n06:31 概念解释：MCP Server 和 Tool\n09:13 配置 MCP Server\n14:19 使用 MCP Server\n15:24 MCP 交互流程详解\n1"
  },
  {
    "id": "bvid:BV1Zgud6LEoh",
    "domain": "AI",
    "title": "【最新版】小白速通 Codex 教程（含 DeepSeek 接入，无需 ChatGPT 订阅）",
    "url": "http://www.bilibili.com/video/av117070826047031",
    "source": "林粒粒呀",
    "platform": "bilibili",
    "points": 281951,
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
    "points": 278119,
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
    "points": 259485,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1ssN16HEkq",
    "domain": "AI",
    "title": "【2026最新版】ChatGPT+Codex 零基础全套教程｜从入门到 AI 开发实战全流程",
    "url": "http://www.bilibili.com/video/av116911476115725",
    "source": "马士兵长沙中心",
    "platform": "bilibili",
    "points": 240697,
    "published_at": "2026-07-13T07:51:43+00:00",
    "summary": "2026 新版 OpenAI ChatGPT+Codex 完整实战课，零基础也能学，从基础指令到 AI 项目开发全流程教学，配套可落地实战案例，学完直接做简历项目。"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 192019,
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
    "points": 181124,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1ExV36wEsE",
    "domain": "AI",
    "title": "VS Code 安装 Claude Code 并接入 DeepSeek！Claude Code for VS Code！VSCode使用ClaudeCode插件",
    "url": "http://www.bilibili.com/video/av116662871268177",
    "source": "FutureAI实验室",
    "platform": "bilibili",
    "points": 177030,
    "published_at": "2026-05-30T09:44:52+00:00",
    "summary": "本节视频编号71，评论区自助领取配套文档，记得一键三连哦！"
  },
  {
    "id": "bvid:BV1Ypbs6vEuJ",
    "domain": "AI",
    "title": "全程无废话！从零用上chatGPT6！保姆级安装/注册/使用ChatGPT+Codex最详细保姆级教程",
    "url": "http://www.bilibili.com/video/av117223716817942",
    "source": "Gemini3-",
    "platform": "bilibili",
    "points": 173926,
    "published_at": "2026-09-06T10:54:39+00:00",
    "summary": "你好审核大人，改下简介"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 170598,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1RNTtzMENj",
    "domain": "AI",
    "title": "从零编写MCP并发布上线，超简单！手把手教程",
    "url": "http://www.bilibili.com/video/av114630814862349",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 155945,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1ZRbe6eENh",
    "domain": "AI",
    "title": "DeepSeek Harness安装和使用教程【最新完整版】零基础小白速通deepseek harness入门教程怎么下载插件如何安装如何使用全搞定！",
    "url": "http://www.bilibili.com/video/av117110286062691",
    "source": "鹏哥C语言",
    "platform": "bilibili",
    "points": 153328,
    "published_at": "2026-08-17T10:10:51+00:00",
    "summary": "欢迎大家来到鹏哥课堂！这份DeepSeek Harness教程专为零基础小白打造，全程手把手演示安装、启动Web界面、模型接入、基础任务实操。 很多小白卡在环境配置、命令报错、参数设置，本教程能让你避开各种坑，跟着操作就能成功运行。 搞懂 Agent = 模型 + Harness，让 AI 读写文件、执行命令、自主完成项目任务。本教程适合程序员、AI 爱好者及想上手本地智能体的同学等。希望大家把视"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 114009,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1PTTs6cEwi",
    "domain": "AI",
    "title": "不写一行代码！0基础用AI开发修仙游戏【全流程教程】",
    "url": "http://www.bilibili.com/video/av116855104668708",
    "source": "黑鲸同学",
    "platform": "bilibili",
    "points": 98581,
    "published_at": "2026-07-03T11:00:00+00:00",
    "summary": "本期视频长达90分钟，全程无废话，建议先收藏后观看。涵盖Vibe Coding理念、Cursor使用、AI绘图与视频生成、游戏系统开发全流程。"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 93660,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1XnuGzfEp7",
    "domain": "AI",
    "title": "让你手中的AI好用10倍！5个好玩实用的MCP推荐，让你不只会用AI搜索",
    "url": "http://www.bilibili.com/video/av114835262018810",
    "source": "田同学Tino",
    "platform": "bilibili",
    "points": 74537,
    "published_at": "2025-07-12T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1A24y1J7Dt",
    "domain": "AI",
    "title": "如何在VS Code中使用Cursor自动生成代码",
    "url": "http://www.bilibili.com/video/av781409810",
    "source": "许你再少年",
    "platform": "bilibili",
    "points": 74351,
    "published_at": "2023-03-23T11:32:23+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1MJXZBgE32",
    "domain": "AI",
    "title": "AI Coding 进阶：从 Vibe/Plan/Spec 到 Harness Engineering 与 Agent Teams",
    "url": "http://www.bilibili.com/video/av116334289491216",
    "source": "Qoder",
    "platform": "bilibili",
    "points": 72185,
    "published_at": "2026-04-02T09:00:33+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1sZMq6qEko",
    "domain": "AI",
    "title": "从0做出你的第一个App ｜ 零基础AI编程保姆教程",
    "url": "http://www.bilibili.com/video/av117038647352026",
    "source": "木子不写代码",
    "platform": "bilibili",
    "points": 68502,
    "published_at": "2026-08-07T12:15:00+00:00",
    "summary": "这期视频，我会手把手带你，用 AI 做出你的第一个 App。\n全程假设你没有任何编程和AI的基础，\n我们从如何写需求提示词开始，\n到确定页面结构和设计，\n产品需求文档，\n开发计划，\n第一版APP验收，\ngit代码存档，\n二次开发，\n界面美化，\n做好的APP也会开源给到大家，\n我也会演示如何获取这个项目源代码并且用AI继续定制开发，\n视频到最后，\n你会收获一个为自己的工作和生活定制的专属APP！\n和"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 55023,
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
    "points": 47917,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1YJ336EEBk",
    "domain": "AI",
    "title": "【AI陪玩】开袋即食的AI接入我的世界教程！",
    "url": "http://www.bilibili.com/video/av116981806143216",
    "source": "万昇Dwin",
    "platform": "bilibili",
    "points": 47890,
    "published_at": "2026-07-26T01:30:00+00:00",
    "summary": "模组：Numen\n项目地址：https://github.com/Dwinovo/minecraft-numen"
  },
  {
    "id": "bvid:BV1vYFQzQE4P",
    "domain": "AI",
    "title": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！Claude Code Hooks回调+Agent Teams全自动开发零轮询",
    "url": "http://www.bilibili.com/video/av116046157647899",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 47690,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operitAI教程：入门安卓最强大ai平台",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 43418,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1VL3F6pE9K",
    "domain": "AI",
    "title": "0基础入门智能体agent测试：AI测试基础+AI智能体(Agent)测试从零入门全攻略，2026最新版！",
    "url": "http://www.bilibili.com/video/av116991151113881",
    "source": "黑马测试",
    "platform": "bilibili",
    "points": 42476,
    "published_at": "2026-07-27T09:19:37+00:00",
    "summary": "还在卷传统软件测试？2026年必学的AI智能体(Agent)测试来了！本期视频专为0基础小白打造，从软件测试基础讲起...若要本视频配套资源笔记可加up主企微（请看置顶留言最后一句话）。"
  },
  {
    "id": "bvid:BV1XiD5BQEAj",
    "domain": "AI",
    "title": "Claude Code 接入微信、一行命令把Claude Code装进微信、保姆级教程、微信支持Claude Code（cc-connect）远程开发",
    "url": "http://www.bilibili.com/video/av116350093694897",
    "source": "下班学AI",
    "platform": "bilibili",
    "points": 39787,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV1LXhc6yEkc",
    "domain": "AI",
    "title": "昔涟/Cyrene-Agent 安装配置/演示教程",
    "url": "http://www.bilibili.com/video/av117164694570292",
    "source": "Playa0",
    "platform": "bilibili",
    "points": 37850,
    "published_at": "2026-08-27T00:43:58+00:00",
    "summary": "v1.1.6安装包：\n夸克网盘：\n链接：https://pan.quark.cn/s/43ff3db459f4?pwd=SD2k\n提取码：SD2k\ngithub仓库：\nPlaya-0v0/Cyrene-Agent: An open-source AI desktop companion inspired by Cyrene, combining immersive Chat, personaliz"
  },
  {
    "id": "bvid:BV1K6Te6bET4",
    "domain": "AI",
    "title": "超火AI编程工作流mattpocock-skills，保姆级教程详细讲解",
    "url": "http://www.bilibili.com/video/av116842588800995",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 34602,
    "published_at": "2026-07-01T03:33:49+00:00",
    "summary": "🔥 本期视频来实战一下最近 GitHub 上很火的 mattpocock-skills！\n很多人可能听过 Claude Code Skills，但真正用的时候会有一个问题：\n这些技能到底应该放在 AI 编程流程的哪一步？🤔\n这期我会用一个完整的「秒杀系统 Demo」带你跑一遍：\n✅ 初始化项目\n✅ 需求访谈\n✅ 生成 PRD\n✅ 页面原型设计\n✅ 进入开发流程\n✅ 代码 Review\n✅ Bug "
  },
  {
    "id": "bvid:BV1z7YJ6MERc",
    "domain": "AI",
    "title": "2026国赛AI一键式全流程解题+论文写作保姆级教程！含AIGC痕迹检测+降重方法+解题过程+论文生成+图表优化等等全覆盖！2026国赛应用AI获奖必看教程！",
    "url": "http://www.bilibili.com/video/av117235779637712",
    "source": "数学建模老哥",
    "platform": "bilibili",
    "points": 31883,
    "published_at": "2026-09-08T14:04:35+00:00",
    "summary": "2026国赛AI一键式全流程解题+论文写作保姆级教程！含AIGC痕迹检测+降重方法+解题过程+论文生成+图表优化等等全覆盖！2026国赛应用AI获奖必看教程！"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 30567,
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
    "points": 29731,
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
    "points": 28930,
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
    "points": 27204,
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
    "points": 25641,
    "published_at": "2026-04-23T15:18:08+00:00",
    "summary": "Claude Code有2种多Agent模式：多个subagents模式和多个独立agent模式"
  },
  {
    "id": "bvid:BV15RPpzSEJM",
    "domain": "AI",
    "title": "斯坦福大学:Vibe Coding(AI编程最新课程)",
    "url": "http://www.bilibili.com/video/av116180459389189",
    "source": "世界课程精选站",
    "platform": "bilibili",
    "points": 22821,
    "published_at": "2026-03-06T05:00:15+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22773,
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
    "points": 21866,
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
    "points": 21856,
    "published_at": "2026-08-15T16:01:38+00:00",
    "summary": "这期用同一个 DeepSeek Pro 0813 模型，分别在 Claude Code 和 DeepSeek Harness 里完成同样的任务，对比工具链对最终效果的影响。\n实测内容包括：\nFPS 游戏 Demo、灯塔预警沙盘、手枪组装动画、显示器组装动画，以及 DeepSeek Harness 的插件化源码流程。\n整体看下来，模型本身当然重要，但 Harness 在插件化、流程记录、缓存命中和任"
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
    "id": "hn:49657991",
    "domain": "AI 算力 / 半导体",
    "title": "How to Build a $20B Semiconductor Fab (2024)",
    "url": "https://www.construction-physics.com/p/how-to-build-a-20-billion-semiconductor",
    "source": "Bluestein",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-09-11T13:22:01+00:00",
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
    "id": "rss:https://www.eetimes.com/inside-architect-labs-two-week-chip-design/",
    "domain": "AI 算力 / 半导体",
    "title": "Inside Architect Labs’ Two-Week Chip Design",
    "url": "https://www.eetimes.com/inside-architect-labs-two-week-chip-design/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T02:00:00+00:00",
    "summary": "Architect Labs says its AI can drag custom chip design from years to weeks with Redwood. The post Inside Architect Labs’ Two-Week Chip Design appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/fabships-aim-to-exploit-free-space-vacuum-for-compound-semiconductor-substrates/",
    "domain": "AI 算力 / 半导体",
    "title": "Fabships Aim to Exploit ‘Free’ Space Vacuum for Compound Semiconductor Substrates",
    "url": "https://www.eetimes.com/fabships-aim-to-exploit-free-space-vacuum-for-compound-semiconductor-substrates/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T21:00:00+00:00",
    "summary": "Space is the next frontier for semiconductor manufacturing, as startup Besxar, founded by an ex-OpenAI technical director, completed its first SpaceX flight and recovered wafer samples without contami"
  },
  {
    "id": "rss:https://www.eetimes.com/soc-planner-a-new-generation-of-automated-soc-design-exploration-managing-cost-effectiveness-and-sustainability/",
    "domain": "AI 算力 / 半导体",
    "title": "SoC PLANNER: A New Generation of Automated SoC Design Exploration Managing Cost-Effectiveness and Sustainability",
    "url": "https://www.eetimes.com/soc-planner-a-new-generation-of-automated-soc-design-exploration-managing-cost-effectiveness-and-sustainability/",
    "source": "Defacto Technologies",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T14:36:58+00:00",
    "summary": "GRENOBLE, France &#8211; [2026, September 8th] CEA, Defacto Technologies, and Innova Advanced Technologies today announced the completion of SoC PLANNER, a three-years project funded by BPI France, as"
  },
  {
    "id": "rss:https://www.eetimes.com/should-standards-trump-innovation/",
    "domain": "AI 算力 / 半导体",
    "title": "Should Standards Trump Innovation?",
    "url": "https://www.eetimes.com/should-standards-trump-innovation/",
    "source": "Prakash Sangam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T13:52:31+00:00",
    "summary": "Standards shouldn’t muzzle RFID’s next leap: Gen2X keeps Gen2 compatibility while boosting range, speed, and reliability. The post Should Standards Trump Innovation? appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/indian-researchers-look-beyond-gpus-to-neuromorphic-ai-hardware/",
    "domain": "AI 算力 / 半导体",
    "title": "Indian Researchers Look Beyond GPUs to Neuromorphic AI Hardware",
    "url": "https://www.eetimes.com/indian-researchers-look-beyond-gpus-to-neuromorphic-ai-hardware/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T07:31:15+00:00",
    "summary": "As AI workloads become more computationally demanding, Indian researchers argue that the next advance may come from rethinking computing architecture itself. The post Indian Researchers Look Beyond GP"
  },
  {
    "id": "rss:https://www.eetimes.com/from-ai-assisted-eda-to-ai-mediated-engineering/",
    "domain": "AI 算力 / 半导体",
    "title": "From AI-Assisted EDA to AI-Mediated Engineering",
    "url": "https://www.eetimes.com/from-ai-assisted-eda-to-ai-mediated-engineering/",
    "source": "Simon Davidmann",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T20:23:10+00:00",
    "summary": "What DAC 2026 revealed about agents, engines, trust—and why the industry should be optimistic. The post From AI-Assisted EDA to AI-Mediated Engineering appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/proven-actions-technologys-end-to-end-audio-architecture-tames-sounds-black-magic/",
    "domain": "AI 算力 / 半导体",
    "title": "Proven: Actions Technology’s End-to-End Audio Architecture Tames Sound’s “Black Magic”",
    "url": "https://www.eetimes.com/proven-actions-technologys-end-to-end-audio-architecture-tames-sounds-black-magic/",
    "source": "Franklin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T13:00:00+00:00",
    "summary": "Whether in the mass consumer market or the high-end professional audio segment, sound quality remains the defining factor that separates one product from another. Consumers’ appetite for better audio "
  },
  {
    "id": "rss:https://www.eetimes.com/adi-snaps-alif-semiconductor-to-push-ai-into-physical-systems/",
    "domain": "AI 算力 / 半导体",
    "title": "ADI Snaps Alif Semiconductor to Push AI into Physical Systems",
    "url": "https://www.eetimes.com/adi-snaps-alif-semiconductor-to-push-ai-into-physical-systems/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T11:00:00+00:00",
    "summary": "The $1.35 billion deal marks another edge AI leap of faith, combining analog sensing with low-power AI processors. The post ADI Snaps Alif Semiconductor to Push AI into Physical Systems appeared first"
  },
  {
    "id": "rss:https://www.eetimes.com/what-six-hours-on-the-runway-told-me-about-air-traffic-control-resilience-and-ai/",
    "domain": "AI 算力 / 半导体",
    "title": "What Six Hours on the Runway Told Me About Air Traffic Control, Resilience, and AI",
    "url": "https://www.eetimes.com/what-six-hours-on-the-runway-told-me-about-air-traffic-control-resilience-and-ai/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T08:09:30+00:00",
    "summary": "A U.K. air traffic control glitch stranded flights for hours, prompting reflections on resilience, redundancy, legacy systems, and AI. The post What Six Hours on the Runway Told Me About Air Traffic C"
  },
  {
    "id": "rss:https://www.eetimes.com/cincon-high-performance-power-modules-for-edge-ai-ipcs/",
    "domain": "AI 算力 / 半导体",
    "title": "Cincon High-Performance Power Modules for Edge AI & IPCs",
    "url": "https://www.eetimes.com/cincon-high-performance-power-modules-for-edge-ai-ipcs/",
    "source": "Cincon Elctronics Co., Ltd.",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T08:00:00+00:00",
    "summary": "As AI moves to the edge, IPCs demand compact, rugged power. Cincon offers baseplate-cooled DC-DC &#038; AC-DC solutions for fanless, harsh AIoT environments. The post Cincon High-Performance Power Mod"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/china-modified-nvidia-rtx-5090-with-massive-96gb-of-memory-appears-on-alibaba-for-less-than-usd4-000-3x-more-vram-at-65-percent-the-cost-of-the-original",
    "domain": "AI 算力 / 半导体",
    "title": "China-modified Nvidia RTX 5090 with massive 96GB of memory appears on Alibaba for less than $4,000 — 3x more VRAM at 65% the cost of the original",
    "url": "https://www.tomshardware.com/pc-components/gpus/china-modified-nvidia-rtx-5090-with-massive-96gb-of-memory-appears-on-alibaba-for-less-than-usd4-000-3x-more-vram-at-65-percent-the-cost-of-the-original",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T16:32:36+00:00",
    "summary": "An alleged Nvidia GeForce RTX 5090 96GB with 96GB of modded VRAM surfaces on Alibaba for $3888."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/supercomputers/sanctioned-chinese-supercomputer-maker-stripped-of-io500-benchmark-crown-intel-powered-aurora-retakes-the-lead-record-breaking-parastor-f9000-storage-system-doesnt-meet-reproducibility-requirements",
    "domain": "AI 算力 / 半导体",
    "title": "Sanctioned Chinese supercomputer maker stripped of IO500 benchmark crown, Intel-powered Aurora retakes the lead — record-breaking ParaStor F9000 storage system doesn't meet reproducibility requirement",
    "url": "https://www.tomshardware.com/tech-industry/supercomputers/sanctioned-chinese-supercomputer-maker-stripped-of-io500-benchmark-crown-intel-powered-aurora-retakes-the-lead-record-breaking-parastor-f9000-storage-system-doesnt-meet-reproducibility-requirements",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T16:26:12+00:00",
    "summary": "Sugon's record-breaking ParaStor F9000 storage systems have lost their IO500 Production crowns and have been moved to the Research list after failing to meet the benchmark's highest reproducibility re"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/pc-building/save-20-percent-on-this-144-in-1-screwdriver-set-perfect-for-hobbyists-and-pc-builders-under-usd40-epic-starter-toolkit-ships-with-electric-and-precision-drivers-along-with-120-magnetic-bits-and-22-maintenance-tools",
    "domain": "AI 算力 / 半导体",
    "title": "Save 20% on this 144-in-1 screwdriver set, perfect for hobbyists and PC builders under $40 — epic starter toolkit ships with electric and precision drivers, along with 120 magnetic bits and 22 mainten",
    "url": "https://www.tomshardware.com/desktops/pc-building/save-20-percent-on-this-144-in-1-screwdriver-set-perfect-for-hobbyists-and-pc-builders-under-usd40-epic-starter-toolkit-ships-with-electric-and-precision-drivers-along-with-120-magnetic-bits-and-22-maintenance-tools",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T15:32:15+00:00",
    "summary": "This 144-in-1 repair toolkit from Strebito is on sale, with 120 bits and a number of other tools for less than $40."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/gamestop-is-reopening-recently-closed-stores-despite-massive-retail-cuts-select-locations-return-nationwide-starting-september-11",
    "domain": "AI 算力 / 半导体",
    "title": "GameStop is reopening recently closed stores despite massive retail cuts — select locations return nationwide starting September 11",
    "url": "https://www.tomshardware.com/tech-industry/gamestop-is-reopening-recently-closed-stores-despite-massive-retail-cuts-select-locations-return-nationwide-starting-september-11",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T12:50:35+00:00",
    "summary": "After shutting down hundreds of locations and dramatically shrinking its physical retail footprint, GameStop is bringing select stores back as its business continues to evolve beyond physical games."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/at-ifa-2026-computing-chased-the-high-and-low-ends-ai-and-budget-focused-machines-left-little-for-the-rest-of-us",
    "domain": "AI 算力 / 半导体",
    "title": "At IFA 2026, computing chased the high and low ends — AI and budget-focused machines left little for the rest of us",
    "url": "https://www.tomshardware.com/laptops/at-ifa-2026-computing-chased-the-high-and-low-ends-ai-and-budget-focused-machines-left-little-for-the-rest-of-us",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T12:44:08+00:00",
    "summary": "At IFA 2026, a bifurcated computing landscape widened as more companies chased Apple's MacBook Neo while also keeping one foot firmly planted in the AI space."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/neogeo-aes-console-remake-delayed-for-nearly-a-year-decision-driven-by-ram-shortage-and-unexpected-popularity",
    "domain": "AI 算力 / 半导体",
    "title": "Hardware-accurate NeoGeo AES+ delayed to late 2027 due to memory shortage — decision driven by surging demand and AI-driven RAM crunch",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/neogeo-aes-console-remake-delayed-for-nearly-a-year-decision-driven-by-ram-shortage-and-unexpected-popularity",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T11:30:00+00:00",
    "summary": "NeoGeo AES+ console remake delayed for nearly a year — decision driven by RAM shortage and unexpected popularity"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/power-supplies/thermalright-tr-kg750-750w-power-supply-review",
    "domain": "AI 算力 / 半导体",
    "title": "Thermalright TR-KG750 750W power supply review: HKC-built KG unit with a Thermalright badge for $91",
    "url": "https://www.tomshardware.com/pc-components/power-supplies/thermalright-tr-kg750-750w-power-supply-review",
    "source": "E. Fylladitakis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T11:05:00+00:00",
    "summary": "Thermalright's HKC-built KG series brings ATX 3.1, a native 12V-2x6 connector and a five-year warranty at a low price point, with the compromises visible inside."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/external-ssds/hands-on-sharges-disk-pro-2-ultra",
    "domain": "AI 算力 / 半导体",
    "title": "Hands On: Sharge's Disk Pro 2 Ultra is a compact, magnetic DIY SSD dock with active cooling, 80W passthrough charging, and HDMI 2.1, supporting up to 8TB drives",
    "url": "https://www.tomshardware.com/pc-components/external-ssds/hands-on-sharges-disk-pro-2-ultra",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T11:05:00+00:00",
    "summary": "One of our favorite external SSDs gets an upgrade as a compact DIY hub with an M.2 slot, active cooling, USB ports, up to HDMI 2.1, and a removable cable."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/desktop-graphics-card-shipments-hit-four-year-high-of-12-5-million-despite-increasing-prices-nvidia-takes-90-percent-share-as-gamers-rush-to-beat-looming-price-spikes",
    "domain": "AI 算力 / 半导体",
    "title": "Desktop graphics card shipments hit four-year high of 12.5 million despite increasing prices — Nvidia takes 90% share as gamers rush to beat looming price spikes",
    "url": "https://www.tomshardware.com/pc-components/gpus/desktop-graphics-card-shipments-hit-four-year-high-of-12-5-million-despite-increasing-prices-nvidia-takes-90-percent-share-as-gamers-rush-to-beat-looming-price-spikes",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T11:00:00+00:00",
    "summary": "Shipments of desktop add-in-boards in Q2 were the highest since Q1 2022 despite rising prices and dropping sales of desktop PCs, according to new numbers from Jon Peddie Research."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/snag-a-huge-usd1-000-saving-on-this-rtx-5090-oled-gaming-laptop-from-hp-now-usd3-699-16-inch-hyperx-rig-delivers-1600p-gaming-with-ultra-fast-240hz-refresh-rate-coupled-with-32gb-ddr5-ram-and-a-2tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Snag a huge $1,000 saving on this RTX 5090 OLED gaming laptop from HP, now $3,699 — 16-inch HyperX rig delivers 1600p gaming with ultra-fast 240Hz refresh rate, coupled with 32GB DDR5 RAM and a 2TB SS",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/snag-a-huge-usd1-000-saving-on-this-rtx-5090-oled-gaming-laptop-from-hp-now-usd3-699-16-inch-hyperx-rig-delivers-1600p-gaming-with-ultra-fast-240hz-refresh-rate-coupled-with-32gb-ddr5-ram-and-a-2tb-ssd",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T10:50:59+00:00",
    "summary": "The HyperX Omen Max 16, featuring the powerful Nvidia GeForce RTX 5090 GPU, is down to $3,699.99 right now, saving you $1,000."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/windows-11-can-now-reinstall-itself-from-the-cloud-cloud-rebuild-revives-dead-systems-without-secondary-boot-media-wipes-broken-installation-and-downloads-a-fresh-copy-of-the-os",
    "domain": "AI 算力 / 半导体",
    "title": "Windows 11 can now reinstall itself from the cloud — Cloud Rebuild revives dead systems without secondary boot media, wipes broken installation and downloads a fresh copy of the OS",
    "url": "https://www.tomshardware.com/software/windows/windows-11-can-now-reinstall-itself-from-the-cloud-cloud-rebuild-revives-dead-systems-without-secondary-boot-media-wipes-broken-installation-and-downloads-a-fresh-copy-of-the-os",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T10:30:00+00:00",
    "summary": "Windows 11 users can soon recover from serious installation problems without relying on a USB drive or a custom recovery image."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-says-claude-thwarted-bioweapon-research-from-state-sponsored-actors-covert-accounts-used-u-s-proxies-to-attempt-to-engineer-deadlier-viruses-tried-to-evade-identification-and-regional-blocks",
    "domain": "AI 算力 / 半导体",
    "title": "Anthropic says Claude thwarted bioweapon research from state-sponsored actors — covert accounts used U.S. proxies to attempt to engineer deadlier viruses, tried to evade identification and regional bl",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-says-claude-thwarted-bioweapon-research-from-state-sponsored-actors-covert-accounts-used-u-s-proxies-to-attempt-to-engineer-deadlier-viruses-tried-to-evade-identification-and-regional-blocks",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T10:00:00+00:00",
    "summary": "Anthropic claims Claude refused instructions to potentially develop biological weapons — alleged state-linked accounts tried to evade identification and regional blocks"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/russian-plot-to-sabotage-undersea-cables-with-secret-weapon-foiled-by-nato-clandestine-op-uncovers-training-exercise-simulating-deployment-against-infrastructure-in-norway",
    "domain": "AI 算力 / 半导体",
    "title": "Russian plot to sabotage undersea cables with 'secret weapon' foiled by NATO — clandestine op uncovers training exercise simulating deployment against infrastructure in Norway",
    "url": "https://www.tomshardware.com/tech-industry/russian-plot-to-sabotage-undersea-cables-with-secret-weapon-foiled-by-nato-clandestine-op-uncovers-training-exercise-simulating-deployment-against-infrastructure-in-norway",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T09:26:43+00:00",
    "summary": "NATO foiled a Russian training exercise simulating the deployment of a secret weapon against Norwegian undersea cables."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/nintendo/nintendo-of-america-puts-tariff-refunds-towards-customer-appreciation-sale-but-no-refunds-to-switch-2-buyers-offers-30-percent-off-games-and-accessories-from-september-13-to-26",
    "domain": "AI 算力 / 半导体",
    "title": "Nintendo of America puts tariff refunds towards 'customer appreciation' sale, but no refunds to Switch 2 buyers — offers 30% off games and accessories from September 13 to 26",
    "url": "https://www.tomshardware.com/video-games/nintendo/nintendo-of-america-puts-tariff-refunds-towards-customer-appreciation-sale-but-no-refunds-to-switch-2-buyers-offers-30-percent-off-games-and-accessories-from-september-13-to-26",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T19:35:00+00:00",
    "summary": "Nintendo is offering a 30% sale with its tariff refunds, as opposed as returning the money directly to customers."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/routers/asus-routers-gain-fccs-conditional-approval-for-sale-in-the-us-as-tp-link-remains-locked-out-asuss-wi-fi-8-ambitions-remain-intact",
    "domain": "AI 算力 / 半导体",
    "title": "Asus routers gain FCC's 'Conditional Approval' for sale in the US as TP-Link remains locked out — Asus's Wi-Fi 8 ambitions remain intact",
    "url": "https://www.tomshardware.com/networking/routers/asus-routers-gain-fccs-conditional-approval-for-sale-in-the-us-as-tp-link-remains-locked-out-asuss-wi-fi-8-ambitions-remain-intact",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T19:13:21+00:00",
    "summary": "Asus gets conditional approval from the FCC for US router sales, while rival TP-Link continues to wait"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-releases-new-ryzen-5-5500f-and-ryzen-5-7500-to-save-budget-pc-building-new-budget-zen-3-and-zen-4-cpus-to-soften-the-blow-from-high-ram-prices",
    "domain": "AI 算力 / 半导体",
    "title": "AMD releases new Ryzen 5 5500F and Ryzen 5 7500 for budget PC builders — new budget Zen 3 and Zen 4 CPUs soften the blow from high RAM prices",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-releases-new-ryzen-5-5500f-and-ryzen-5-7500-to-save-budget-pc-building-new-budget-zen-3-and-zen-4-cpus-to-soften-the-blow-from-high-ram-prices",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T17:54:53+00:00",
    "summary": "AMD has officially launched the Ryzen 5 5500F and Ryzen 5 7500 processors with six Zen 3 and Zen 4 cores, respectively."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/apples-new-a20-pro-smartphone-chip-around-25-percent-faster-than-its-predecessor-in-leaked-benchmark-the-2nm-cpu-in-the-iphone-duo-and-18-pro-hits-nearly-5-ghz-clocks",
    "domain": "AI 算力 / 半导体",
    "title": "Apple’s new A20 Pro smartphone chip around 25% faster than its predecessor in leaked benchmark — the 2nm CPU in the iPhone Duo and 18 Pro hits nearly 5 GHz clocks",
    "url": "https://www.tomshardware.com/pc-components/cpus/apples-new-a20-pro-smartphone-chip-around-25-percent-faster-than-its-predecessor-in-leaked-benchmark-the-2nm-cpu-in-the-iphone-duo-and-18-pro-hits-nearly-5-ghz-clocks",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T16:04:10+00:00",
    "summary": "The first Apple A20 Geekbench 6 benchmark results are starting to pop up online and the single-core score is very impressive."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/this-usd399-elegoo-centauri-carbon-2-combo-deal-with-usd1-filament-is-the-perfect-3d-printer-deal-for-beginners-flash-sale-discount-nets-you-a-core-xy-printer-with-four-color-system-and-auto-bed-leveling",
    "domain": "AI 算力 / 半导体",
    "title": "This $399 Elegoo Centauri Carbon 2 Combo with $1 filament is the perfect 3D printer deal for beginners — flash sale discount nets you a Core XY printer with four-color system and auto bed leveling",
    "url": "https://www.tomshardware.com/3d-printing/this-usd399-elegoo-centauri-carbon-2-combo-deal-with-usd1-filament-is-the-perfect-3d-printer-deal-for-beginners-flash-sale-discount-nets-you-a-core-xy-printer-with-four-color-system-and-auto-bed-leveling",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T15:00:00+00:00",
    "summary": "Grab this budget-friendly 3D printer from Elegoo, the Centauri Carbon 2 Combo, for $399, and pay just $1 extra for 1KG of filament."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cryptocurrency/minecraft-spawned-crypto-kingpin-faces-20-years-for-usd245-million-heist-masterminds-role-in-hacking-campaign-fueled-their-supercar-bodyguards-and-private-jet-habit",
    "domain": "AI 算力 / 半导体",
    "title": "Minecraft-spawned crypto kingpin faces 20 years for $245 million heist — mastermind's role in hacking campaign fueled their supercar, bodyguards, and private jet habit",
    "url": "https://www.tomshardware.com/tech-industry/cryptocurrency/minecraft-spawned-crypto-kingpin-faces-20-years-for-usd245-million-heist-masterminds-role-in-hacking-campaign-fueled-their-supercar-bodyguards-and-private-jet-habit",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T14:25:28+00:00",
    "summary": "The ringleader of a cybercrime gang, which reportedly formed after meetups in Minecraft online, has plead guilty to a racketeering charge and now faces up to 20 years in jail."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/openais-rogue-ai-agents-accessed-more-websites-to-communicate-than-originally-believed-defiant-llms-accessed-old-wikis-and-abandoned-websites-to-co-ordinate-in-a-bid-to-dupe-assessors",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI's rogue AI agents accessed more websites to communicate than originally believed — defiant LLMs accessed old wikis and abandoned websites to co-ordinate in a bid to dupe assessors",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/openais-rogue-ai-agents-accessed-more-websites-to-communicate-than-originally-believed-defiant-llms-accessed-old-wikis-and-abandoned-websites-to-co-ordinate-in-a-bid-to-dupe-assessors",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T13:20:00+00:00",
    "summary": "Rogue OpenAI agents used dozens of website to exchange information, new investigations have found. However, the real impact is yet to be determined."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-chairs/libernovo-omni-pro-review",
    "domain": "AI 算力 / 半导体",
    "title": "Libernovo Omni Pro Review: Cooler than you think",
    "url": "https://www.tomshardware.com/peripherals/gaming-chairs/libernovo-omni-pro-review",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T13:06:32+00:00",
    "summary": "Libernovo's Omni Pro is a dynamic, ergonomic gaming chair with motorized lumbar support and a ventilation fan that works surprisingly well."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/old-macbook-uses-a-mirror-webcam-and-ai-agent-to-code-its-own-amd-gpu-drivers-agent-first-omarchy-linux-debugs-itself-ai-can-check-its-own-progress-on-screen-in-real-time",
    "domain": "AI 算力 / 半导体",
    "title": "Old MacBook uses a mirror, webcam, and AI agent to code its own AMD GPU drivers — 'agent-first' Omarchy Linux debugs itself, AI can check its own progress on screen in real-time",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/old-macbook-uses-a-mirror-webcam-and-ai-agent-to-code-its-own-amd-gpu-drivers-agent-first-omarchy-linux-debugs-itself-ai-can-check-its-own-progress-on-screen-in-real-time",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T13:00:00+00:00",
    "summary": "Using an 'age of agents' Linux distro a 'MacBook is using its webcam to look at its screen in a mirror to improve AMD Radeon chip support.'"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/chinas-ai-accelerator-supplier-biren-posts-2-000-percent-year-over-year-revenue-growth-export-controls-benefit-homegrown-chips-as-nvidia-and-amd-exit-market",
    "domain": "AI 算力 / 半导体",
    "title": "China's AI accelerator supplier Biren posts 2,000% year-over-year revenue growth — US export controls benefit homegrown chips as Nvidia and AMD exit market",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/chinas-ai-accelerator-supplier-biren-posts-2-000-percent-year-over-year-revenue-growth-export-controls-benefit-homegrown-chips-as-nvidia-and-amd-exit-market",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T12:40:00+00:00",
    "summary": "Biren Technology shows unprecedented shipments growth in 1H 2026 as competition from AMD and Nvidia vanishes (at least officially)."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/chinese-quartz-approved-for-semiconductor-equipment-and-dram-manufacturing-but-it-still-cant-break-americas-monopoly-china-secures-domestic-supply-for-chipmaking-components-but-spruce-pine-still-holds-the-crucible-monopoly",
    "domain": "AI 算力 / 半导体",
    "title": "Chinese quartz approved for semiconductor equipment and DRAM manufacturing, but it still can't break America's monopoly — China secures domestic supply for chipmaking components, but Spruce Pine still",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/chinese-quartz-approved-for-semiconductor-equipment-and-dram-manufacturing-but-it-still-cant-break-americas-monopoly-china-secures-domestic-supply-for-chipmaking-components-but-spruce-pine-still-holds-the-crucible-monopoly",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T12:20:00+00:00",
    "summary": "Pacific Quartz gets its high-purity quartz qualified for semiconductor equipment and DRAM manufacturing."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/the-state-of-abf-substrates-in-data-center-silicon-in-2026-solving-the-supply-crunch-and-material-wall-beneath-every-ai-accelerator",
    "domain": "AI 算力 / 半导体",
    "title": "The state of ABF substrates in data center silicon in 2026 — solving the supply crunch and material wall beneath every AI accelerator",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/the-state-of-abf-substrates-in-data-center-silicon-in-2026-solving-the-supply-crunch-and-material-wall-beneath-every-ai-accelerator",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T12:00:00+00:00",
    "summary": "ABF substrates underpin today’s most advanced AI chips, but soaring demand and expanding accelerator packages are creating new supply and technical bottlenecks that the industry is currently racing to"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/modded-rtx-5090-ditches-16-pin-power-for-triple-8-pin-connectors-draws-up-to-900w-and-hits-3-400-mhz",
    "domain": "AI 算力 / 半导体",
    "title": "Modded RTX 5090 ditches 16-pin power for triple 8-pin connectors — draws up to 900W and hits 3,400 MHz",
    "url": "https://www.tomshardware.com/pc-components/gpus/modded-rtx-5090-ditches-16-pin-power-for-triple-8-pin-connectors-draws-up-to-900w-and-hits-3-400-mhz",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T11:40:00+00:00",
    "summary": "TecLab’s experiment puts the humble 8-pin connector to an extreme test, with the modified RTX 5090 pulling more than 120A while avoiding the newer 12V-2x6 design altogether."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/tsmc-samsung-and-intel-shore-up-support-with-asml-to-deploy-larger-high-na-euv-photomasks-6-12-inch-photomask-transition-may-take-years-despite-unified-effort",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC, Samsung, and Intel shore up support with ASML to deploy larger High-NA EUV photomasks — 6×12-inch photomask transition may take years despite unified effort",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/tsmc-samsung-and-intel-shore-up-support-with-asml-to-deploy-larger-high-na-euv-photomasks-6-12-inch-photomask-transition-may-take-years-despite-unified-effort",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T11:20:00+00:00",
    "summary": "ASML, Intel, Samsung, and TSMC back development of 6×12-inch to build large processors using High-NA EUV lithography systems without stitching."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/developer-uses-claude-to-vibe-code-a-windows-3-1-shell-in-an-hour-reanimated-12mb-retro-launcher-runs-on-both-windows-11-and-apple-silicon",
    "domain": "AI 算力 / 半导体",
    "title": "Developer uses Claude to vibe code a Windows 3.1 shell in an hour — reanimated 12MB retro launcher runs on both Windows 11 and Apple Silicon",
    "url": "https://www.tomshardware.com/software/windows/developer-uses-claude-to-vibe-code-a-windows-3-1-shell-in-an-hour-reanimated-12mb-retro-launcher-runs-on-both-windows-11-and-apple-silicon",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T11:00:00+00:00",
    "summary": "There’s a new vibe-coded clone of the Windows 3.1 Program Manager that runs on modern Windows 11 or macOS systems."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/save-usd250-on-this-1080p-ready-gaming-laptop-with-an-rtx-5060-now-just-usd1049-msi-cyborg-15-rig-ships-with-a-15-6-inch-144hz-display-16gb-ddr5-ram-and-an-eight-core-intel-cpu",
    "domain": "AI 算力 / 半导体",
    "title": "Save $250 on this 1080p-ready gaming laptop with an RTX 5060, now just $1049 — MSI Cyborg 15 rig ships with a 15.6-inch 144Hz display, 16GB DDR5 RAM, and an eight-core Intel CPU",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/save-usd250-on-this-1080p-ready-gaming-laptop-with-an-rtx-5060-now-just-usd1049-msi-cyborg-15-rig-ships-with-a-15-6-inch-144hz-display-16gb-ddr5-ram-and-an-eight-core-intel-cpu",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T10:53:35+00:00",
    "summary": "This MSI gaming laptop is fit for 1080p gaming, thanks to an RTX 5060, with $250 off knocking the price down to just $1049.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/steam-enforces-australian-age-verification-via-credit-cards-debit-card-glitches-and-low-credit-adoption-alienate-core-gamers-privacy-first-mindset-leads-to-dearth-of-options-that-may-hinder-consumers",
    "domain": "AI 算力 / 半导体",
    "title": "Steam enforces Australian age verification via credit cards — debit card glitches and low credit adoption alienate core gamers, privacy-first mindset leads to dearth of options that may hinder consume",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/steam-enforces-australian-age-verification-via-credit-cards-debit-card-glitches-and-low-credit-adoption-alienate-core-gamers-privacy-first-mindset-leads-to-dearth-of-options-that-may-hinder-consumers",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T10:30:00+00:00",
    "summary": "Valve starts enforcing Australian age verification law, but its privacy-minded choice of bank card as the only verification method is causing issues with many consumers."
  },
  {
    "id": "hn:49638022",
    "domain": "AI 算力 / 半导体",
    "title": "CUDA Rust: Two Tracks for Writing GPU Kernels",
    "url": "https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/",
    "source": "xiaoyu2006",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-09-10T03:25:49+00:00",
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
    "id": "hn:49497235",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's AI advantage is moving beyond the GPU",
    "url": "https://techcrunch.com/2026/08/29/nvidias-ai-advantage-is-moving-beyond-the-gpu/",
    "source": "01-_-",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-08-30T09:57:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:49558584",
    "domain": "AI 算力 / 半导体",
    "title": "Hugging Face is too important to fall into Nvidia's hands",
    "url": "https://www.theregister.com/ai-and-ml/2026/09/03/hugging-face-is-too-important-to-fall-into-nvidias-hands/5294363",
    "source": "mdp2021",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-09-03T23:33:42+00:00",
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
    "points": 601,
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
    "points": 406,
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
    "id": "hn:49610641",
    "domain": "大厂 AI 动态",
    "title": "AlphaGenome Atlas predictive map of every DNA letter change in the human genome",
    "url": "https://deepmind.google/blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/",
    "source": "fady0",
    "platform": "hackernews",
    "points": 91,
    "published_at": "2026-09-08T14:14:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:49653699",
    "domain": "大厂 AI 动态",
    "title": "The Gemini app is now available for Windows",
    "url": "https://blog.google/innovation-and-ai/products/gemini-app/gemini-app-now-on-windows/",
    "source": "quysala12",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-09-11T04:52:20+00:00",
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
    "id": "hn:49652122",
    "domain": "大厂 AI 动态",
    "title": "Setting up OpenCode with Ollama and sbx on Mac",
    "url": "https://tensorsandtokens.com/posts/opencode-ollama/",
    "source": "etoxin",
    "platform": "hackernews",
    "points": 30,
    "published_at": "2026-09-11T00:45:26+00:00",
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
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/994207/chatgpt-new-mexico-lawyer-fined-murder-appeal",
    "domain": "大厂 AI 动态",
    "title": "Lawyer fined $5K over AI-hallucinated witnesses in a murder case",
    "url": "https://www.theverge.com/ai-artificial-intelligence/994207/chatgpt-new-mexico-lawyer-fined-murder-appeal",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T20:44:02+00:00",
    "summary": "New Mexico's Supreme Court is punishing a lawyer for including AI-fabricated witnesses and fake police testimony in an appeal for his client's murder conviction, according to a report from Reuters. In"
  },
  {
    "id": "rss:https://www.theverge.com/tech/994087/matt-mullenweg-automattic-ceo-return",
    "domain": "大厂 AI 动态",
    "title": "Matt Mullenweg returns as Automattic CEO two days after getting booted",
    "url": "https://www.theverge.com/tech/994087/matt-mullenweg-automattic-ceo-return",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T17:16:59+00:00",
    "summary": "Two days after being placed on a paid leave of absence, Matt Mullenweg says he has been reinstated as CEO of Automattic, according to a Slack message seen by TechCrunch. WordPress Executive Director M"
  },
  {
    "id": "rss:https://www.theverge.com/podcast/994016/iphone-duo-vergecast-apple-watch-mac-llms",
    "domain": "大厂 AI 动态",
    "title": "We unfolded the iPhone Duo",
    "url": "https://www.theverge.com/podcast/994016/iphone-duo-vergecast-apple-watch-mac-llms",
    "source": "Jacob Kastrenakes",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T16:22:24+00:00",
    "summary": "You only get one chance at a first impression, and getting to introduce Apple's first folding phone is certainly a strong way to start things off as Apple's CEO. On The Vergecast today, we're talking "
  },
  {
    "id": "rss:https://www.theverge.com/policy/994072/white-house-truth-social-popular-powerful",
    "domain": "大厂 AI 动态",
    "title": "The White House says Truth Social is the ‘most powerful and popular social media platform in the world’",
    "url": "https://www.theverge.com/policy/994072/white-house-truth-social-popular-powerful",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T16:21:19+00:00",
    "summary": "The White House claims the Donald Trump-owned Truth Social is the \"most powerful and popular social media platform in the world.\" The statement, provided to The New York Times by White House spokesper"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/994064/anthropic-spent-this-week-in-hot-water-over-cybersecurity",
    "domain": "大厂 AI 动态",
    "title": "Anthropic spent this week in hot water over cybersecurity",
    "url": "https://www.theverge.com/ai-artificial-intelligence/994064/anthropic-spent-this-week-in-hot-water-over-cybersecurity",
    "source": "Hayden Field",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T16:09:14+00:00",
    "summary": "After admitting earlier this year that its AI models had hacked other companies' systems on a handful of occasions, Anthropic released a new report on Wednesday detailing the attacks. It reveals a str"
  },
  {
    "id": "rss:https://www.theverge.com/news/993791/microsoft-frank-shaw-leaving-head-of-comms",
    "domain": "大厂 AI 动态",
    "title": "Microsoft’s head of comms is leaving after almost 20 years",
    "url": "https://www.theverge.com/news/993791/microsoft-frank-shaw-leaving-head-of-comms",
    "source": "Tom Warren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T16:01:34+00:00",
    "summary": "Frank Shaw is leaving Microsoft after 17 years as chief communications officer. In an internal note to his team, Shaw says he's \"decided it is time for me to move on and try new things,\" after support"
  },
  {
    "id": "rss:https://www.theverge.com/tech/994055/meta-project-phoenix-headset-leak",
    "domain": "大厂 AI 动态",
    "title": "Meta may have leaked the first look at its slim &#8216;Project Phoenix&#8217; headset",
    "url": "https://www.theverge.com/tech/994055/meta-project-phoenix-headset-leak",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T15:38:31+00:00",
    "summary": "Just a couple of weeks before Meta Connect starts on September 23rd, UploadVR posted images seemingly revealing the design for Meta's \"Project Phoenix\" headset. The images, which UploadVR says were \"f"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/993637/apple-airpods-5-anc-wireless-charging-preorder-buy",
    "domain": "大厂 AI 动态",
    "title": "Where to preorder the Apple AirPods 5",
    "url": "https://www.theverge.com/gadgets/993637/apple-airpods-5-anc-wireless-charging-preorder-buy",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T15:31:00+00:00",
    "summary": "The Apple AirPods 5 are bringing active noise cancellation to the masses, and they're now available for preorder at a variety of retailers. They'll officially launch on September 18th, the same day as"
  },
  {
    "id": "rss:https://www.theverge.com/tech/993898/nicholaslighttv-remove-your-media-youtube-crunchyroll-viz-media",
    "domain": "大厂 AI 动态",
    "title": "Anime reaction YouTubers are at war with copyright enforcers",
    "url": "https://www.theverge.com/tech/993898/nicholaslighttv-remove-your-media-youtube-crunchyroll-viz-media",
    "source": "Charles Pulliam-Moore",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T15:12:58+00:00",
    "summary": "On September 6th, YouTuber Nicholas Light posted a video to one of his channels that made it seem like all of his content was about to be removed from the platform. In the video - ominously titled \"My"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/993929/soundcore-liberty-5-pro-earbuds-control-resonant-ring-doorbell-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "The wireless earbuds with unbeatable call quality got their first discount",
    "url": "https://www.theverge.com/gadgets/993929/soundcore-liberty-5-pro-earbuds-control-resonant-ring-doorbell-deal-sale",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T14:43:26+00:00",
    "summary": "Anker’s Soundcore Liberty 5 Pro came out swinging in May with incredible call quality, something that competing ear buds have struggled to get right. They’ve become part of our reviewer John Higgins’ "
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/11/mecka-ai-nears-500m-valuation-in-sequoia-led-deal-amid-rush-for-robot-training-data/",
    "domain": "大厂 AI 动态",
    "title": "Mecka AI nears $500M valuation in Sequoia-led deal amid rush for robot training data",
    "url": "https://techcrunch.com/2026/09/11/mecka-ai-nears-500m-valuation-in-sequoia-led-deal-amid-rush-for-robot-training-data/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T22:58:17+00:00",
    "summary": "The round for the two-year-old startup is coming together months after Mecka announced its Series A."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/11/khosla-ventures-is-opening-a-new-york-office-this-fall-its-first-outpost-outside-sand-hill-road/",
    "domain": "大厂 AI 动态",
    "title": "Khosla Ventures is opening a New York office this fall — its first outpost outside Sand Hill Road",
    "url": "https://techcrunch.com/2026/09/11/khosla-ventures-is-opening-a-new-york-office-this-fall-its-first-outpost-outside-sand-hill-road/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T21:19:05+00:00",
    "summary": "\"It's actually allegedly being built out now,\" said Rabois, who has clearly dealt with a missed construction timeline or two."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/11/y-combinators-garry-tan-wants-u-s-open-weight-ai-labs-to-distill-frontier-models-too/",
    "domain": "大厂 AI 动态",
    "title": "Y Combinator’s Garry Tan wants US open-weight AI labs to ‘distill’ frontier models, too",
    "url": "https://techcrunch.com/2026/09/11/y-combinators-garry-tan-wants-u-s-open-weight-ai-labs-to-distill-frontier-models-too/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T20:59:47+00:00",
    "summary": "Tan wants smaller, American open-weight AI labs to use the same kind of training techniques on American frontier AI labs, giving the U.S. a more robust set of open-weight options that aren’t Chinese."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/11/openais-feud-with-mathematicians-is-only-escalating/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI’s feud with mathematicians is only escalating",
    "url": "https://techcrunch.com/2026/09/11/openais-feud-with-mathematicians-is-only-escalating/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T20:57:36+00:00",
    "summary": "Twenty-five leading mathematicians signed an open letter arguing that AI labs are threatening their intellectual work."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/11/one-week-left-to-book-your-exhibit-table-at-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "One week left to book your exhibit table at TechCrunch Disrupt 2026",
    "url": "https://techcrunch.com/2026/09/11/one-week-left-to-book-your-exhibit-table-at-techcrunch-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T20:33:18+00:00",
    "summary": "Only one week left to secure your exhibit table. Tables are limited and can sell out before the September 18 deadline."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/11/final-final-final-call-for-techcrunch-disrupt-2026-side-events/",
    "domain": "大厂 AI 动态",
    "title": "Final, final, final call for TechCrunch Disrupt 2026 Side Events",
    "url": "https://techcrunch.com/2026/09/11/final-final-final-call-for-techcrunch-disrupt-2026-side-events/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T20:30:17+00:00",
    "summary": "The absolute last chance to apply to host an official Side Event during TechCrunch Disrupt 2026 is tonight, September 11, at 11:59 p.m. PT."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/11/kimi-maker-moonshot-ai-targets-2-billion-in-annual-revenue/",
    "domain": "大厂 AI 动态",
    "title": "Kimi-maker Moonshot AI targets $2B in annual revenue",
    "url": "https://techcrunch.com/2026/09/11/kimi-maker-moonshot-ai-targets-2-billion-in-annual-revenue/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T19:35:54+00:00",
    "summary": "While K3's usage figures have declined slightly in recent months, OpenRouter data currently shows as many as 300 billion tokens being generated each day by K3 models on the system."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/11/roblox-is-making-it-easier-to-build-games-with-ai-and-play-them-outside-roblox/",
    "domain": "大厂 AI 动态",
    "title": "Roblox is making it easier to build games with AI — and play them outside Roblox",
    "url": "https://techcrunch.com/2026/09/11/roblox-is-making-it-easier-to-build-games-with-ai-and-play-them-outside-roblox/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T19:00:00+00:00",
    "summary": "At its annual Roblox Developer Conference (RDC), the company announced several new features, including new game-creation tools, expanded NPC capabilities, and the ability to make games available acros"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/11/central-eurasia-names-its-2026-road-to-battlefield-winners-cerberus-weglobal-ai-and-looq/",
    "domain": "大厂 AI 动态",
    "title": "Central Eurasia names its 2026 Road to Battlefield winners: Cerberus, WeGlobal AI, and LOOQ",
    "url": "https://techcrunch.com/2026/09/11/central-eurasia-names-its-2026-road-to-battlefield-winners-cerberus-weglobal-ai-and-looq/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T18:58:01+00:00",
    "summary": "Cerberus, WeGlobal AI, and LOOQ took the top three spots at the regional final of Road to TechCrunch Startup Battlefield 2026 and will represent Central Eurasia in the Startup Battlefield 200 at TechC"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/11/nscale-adds-former-openai-exec-fidji-simo-to-its-board-ahead-of-potential-ipo/",
    "domain": "大厂 AI 动态",
    "title": "Nscale adds former OpenAI exec Fidji Simo to its board ahead of potential IPO",
    "url": "https://techcrunch.com/2026/09/11/nscale-adds-former-openai-exec-fidji-simo-to-its-board-ahead-of-potential-ipo/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T16:46:25+00:00",
    "summary": "The No. 2 exec at OpenAI also led Instacart through its IPO in 2023."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/11/matt-mullenweg-tells-automattic-staff-in-slack-hes-back-in-control-after-ceo-ouster/",
    "domain": "大厂 AI 动态",
    "title": "Matt Mullenweg tells (trolls?) Automattic staff, saying he’s back in control after CEO ouster",
    "url": "https://techcrunch.com/2026/09/11/matt-mullenweg-tells-automattic-staff-in-slack-hes-back-in-control-after-ceo-ouster/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T15:19:00+00:00",
    "summary": "In a Slack message seen by TechCrunch, Matt Mullenweg told Automattic employees he’s back in control of the company, days after its board put him on leave. Automattic has not yet confirmed the apparen"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/11/scammers-target-hundreds-of-thousands-of-crypto-owners-after-trezor-confirms-data-breach-of-email-provider/",
    "domain": "大厂 AI 动态",
    "title": "Scammers target hundreds of thousands of crypto owners after Trezor confirms data breach of email provider",
    "url": "https://techcrunch.com/2026/09/11/scammers-target-hundreds-of-thousands-of-crypto-owners-after-trezor-confirms-data-breach-of-email-provider/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T13:32:54+00:00",
    "summary": "This is the second data breach affecting a company that hardware crypto wallet maker Trezor relies on."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/10/thrive-capital-showed-vcs-the-way-into-pro-sports-ownership-collaborative-fund-is-now-trying-its-own-version-of-the-same-play/",
    "domain": "大厂 AI 动态",
    "title": "Thrive Capital led VCs into pro sports ownership; Collaborative Fund just upped that play",
    "url": "https://techcrunch.com/2026/09/10/thrive-capital-showed-vcs-the-way-into-pro-sports-ownership-collaborative-fund-is-now-trying-its-own-version-of-the-same-play/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T22:30:00+00:00",
    "summary": "Collaborative Fund just bought into D.C. United and its stadium, with firm founder Craig Shapiro pitching it as a way to showcase for the firm's startups."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/10/jensen-huang-explains-why-nvidia-will-grow-an-astounding-70-next-year/",
    "domain": "大厂 AI 动态",
    "title": "Jensen Huang explains why Nvidia will grow an astounding 70% next year",
    "url": "https://techcrunch.com/2026/09/10/jensen-huang-explains-why-nvidia-will-grow-an-astounding-70-next-year/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T21:51:59+00:00",
    "summary": "Nvidia has its finger in every pie, and sees another year of plenty in its future, Jensen Huang says. But, he insists, its deals are not circular."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/10/mark-wahlberg-is-coming-to-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "Mark Wahlberg is coming to TechCrunch Disrupt 2026, and he wants to talk about your work, not his",
    "url": "https://techcrunch.com/2026/09/10/mark-wahlberg-is-coming-to-techcrunch-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T21:35:00+00:00",
    "summary": "Mark Wahlberg joins Bruce K. Lee at Disrupt to discuss investing, entrepreneurship, healthcare, wellness, and building businesses."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/10/openai-puts-pro-subscriptions-on-hold-due-to-astra-demand/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI puts Pro subscriptions on hold due to Astra demand",
    "url": "https://techcrunch.com/2026/09/10/openai-puts-pro-subscriptions-on-hold-due-to-astra-demand/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T20:59:51+00:00",
    "summary": "The company said Pro subscriptions put the most strain on its systems, so it's pausing sign-ups while adding more capacity."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/10/anthropic-details-distillation-campaigns-from-alibaba-moonshot-ai-and-deepseek/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic details distillation campaigns from Alibaba, Moonshot AI, and DeepSeek",
    "url": "https://techcrunch.com/2026/09/10/anthropic-details-distillation-campaigns-from-alibaba-moonshot-ai-and-deepseek/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T20:57:30+00:00",
    "summary": "A new report released Thursday by Anthropic alleges persistent distillation attacks by China-based AI companies, which have escalated in recent months as competition in the space has intensified."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/10/furos-founders-left-silicon-valley-and-its-paying-off/",
    "domain": "大厂 AI 动态",
    "title": "Furo’s founders left Silicon Valley — and it’s paying off",
    "url": "https://techcrunch.com/2026/09/10/furos-founders-left-silicon-valley-and-its-paying-off/",
    "source": "Anna Heim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T20:48:00+00:00",
    "summary": "The three 28-year-old founders behind energy startup Furo moved from Silicon Valley and back to Germany, and yet secured $4 million in funding from mostly U.S. backers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/10/metas-ai-agent-muse-is-now-the-no-2-app-in-the-us/",
    "domain": "大厂 AI 动态",
    "title": "Meta’s AI agent Muse is now the No. 2 app in the US",
    "url": "https://techcrunch.com/2026/09/10/metas-ai-agent-muse-is-now-the-no-2-app-in-the-us/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T19:50:04+00:00",
    "summary": "Meta's newest app Muse is off to a slower start than the company's other apps, like Meta AI or Threads."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/10/proxima-fusion-bets-e140m-on-a-critical-fusion-ingredient-dominated-by-asian-suppliers/",
    "domain": "大厂 AI 动态",
    "title": "Proxima Fusion bets €140M on a critical fusion ingredient dominated by Asian suppliers",
    "url": "https://techcrunch.com/2026/09/10/proxima-fusion-bets-e140m-on-a-critical-fusion-ingredient-dominated-by-asian-suppliers/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T18:38:00+00:00",
    "summary": "Proxima Fusion said Wednesday it plans to build a €140 million ($162.6 million) factory to produce fusion-grade high-temperature superconducting (HTS) tape, which will provide the startup with key com"
  },
  {
    "id": "rss:https://stratechery.com/2026/duo-threats/",
    "domain": "大厂 AI 动态",
    "title": "2026.37: Duo Threats",
    "url": "https://stratechery.com/2026/duo-threats/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T17:00:00+00:00",
    "summary": "The best Stratechery content from the week of September 7, 2026, including the arrival of the Duo, AI that benefits humanity, and closing the book on a catastrophe."
  },
  {
    "id": "rss:https://stratechery.com/2026/the-iphone-duo-the-intelligent-personal-hub-apple-watch-audio-intelligence/",
    "domain": "大厂 AI 动态",
    "title": "The iPhone Duo, The Intelligent Personal Hub, Apple Watch Audio Intelligence",
    "url": "https://stratechery.com/2026/the-iphone-duo-the-intelligent-personal-hub-apple-watch-audio-intelligence/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T10:00:00+00:00",
    "summary": "Apple once again demonstrated the power of integrating hardware and software, but it's biggest AI blindspot might be its belief in the primacy of apps."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/09/some-satellite-companies-still-have-an-appetite-for-boutique-launch-services/",
    "domain": "大厂 AI 动态",
    "title": "Some satellite companies still have an appetite for boutique launch services",
    "url": "https://arstechnica.com/space/2026/09/some-satellite-companies-still-have-an-appetite-for-boutique-launch-services/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T23:34:45+00:00",
    "summary": "\"Dedicated launch is pretty essential for us for most of our missions.\""
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/09/random-rewards-enrich-classic-game-theory-contests/",
    "domain": "大厂 AI 动态",
    "title": "Random rewards enrich classic game-theory insights",
    "url": "https://arstechnica.com/science/2026/09/random-rewards-enrich-classic-game-theory-contests/",
    "source": "Chris Lee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T21:41:16+00:00",
    "summary": "Simple games gain rich strategies in the face of noise."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/09/bouncy-castle-launches-horrifying-mrsa-outbreak-striking-48-kids-in-ireland/",
    "domain": "大厂 AI 动态",
    "title": "Bouncy castle launches horrifying MRSA outbreak, striking 48 kids in Ireland",
    "url": "https://arstechnica.com/health/2026/09/bouncy-castle-launches-horrifying-mrsa-outbreak-striking-48-kids-in-ireland/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T21:14:26+00:00",
    "summary": "The strain lurking in the inflatable structure was hypervirulent."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/09/court-rejects-governments-energy-emergency-that-kept-coal-plant-open/",
    "domain": "大厂 AI 动态",
    "title": "Trump's forced coal plant extensions thrown out by judge",
    "url": "https://arstechnica.com/science/2026/09/court-rejects-governments-energy-emergency-that-kept-coal-plant-open/",
    "source": "John Timmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T20:32:59+00:00",
    "summary": "The Department of Energy declared an \"emergency\" when none existed."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/09/chatgpt-using-lawyer-punished-for-citing-fake-testimony-from-made-up-witnesses/",
    "domain": "大厂 AI 动态",
    "title": "ChatGPT-using lawyer punished for citing fake testimony from made-up witnesses",
    "url": "https://arstechnica.com/tech-policy/2026/09/chatgpt-using-lawyer-punished-for-citing-fake-testimony-from-made-up-witnesses/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T19:34:09+00:00",
    "summary": "\"I didn't know that AI could hallucinate facts,\" New Mexico defense lawyer says."
  },
  {
    "id": "hn:49599992",
    "domain": "股票",
    "title": "Stockfish 19",
    "url": "https://stockfishchess.org/blog/2026/stockfish-19/",
    "source": "atiedebee",
    "platform": "hackernews",
    "points": 276,
    "published_at": "2026-09-07T16:17:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:49611240",
    "domain": "股票",
    "title": "iPod Classic 6G in QEMU",
    "url": "https://www.reddit.com/r/emulation/s/VL4Au2HGxq",
    "source": "dmonterocrespo",
    "platform": "hackernews",
    "points": 148,
    "published_at": "2026-09-08T14:54:57+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3780023",
    "domain": "股票",
    "title": "华源期货孙伏鲲带你用衍生品工具重塑交易体系：从波段结构到期权增强的四维交易系统",
    "url": "https://wallstreetcn.com/articles/3780023",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T07:38:24+00:00",
    "summary": "2026年9月19日，华源期货副总经理孙伏鲲投研框架大分享：四维一体，构建你的交易\"操作系统\""
  },
  {
    "id": "wscn:3781629",
    "domain": "股票",
    "title": "美股长牛背后有大小熊",
    "url": "https://wallstreetcn.com/articles/3781629",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T07:38:03+00:00",
    "summary": "美债利率重返2007年高位，美股长牛会否终结？百年复盘显示，1982年后产业升级与养老金入市造就牛长熊短；真正大熊需基本面恶化引发盈利估值双杀，小熊多由事件冲击，平均跌23.5%、仅3.4个月。"
  },
  {
    "id": "wscn:3781627",
    "domain": "股票",
    "title": "直击光博会！芯片、光引擎、设备密集上新",
    "url": "https://wallstreetcn.com/articles/3781627",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T06:13:51+00:00",
    "summary": "从单波200G光通信电芯片、6.4T CPO光引擎，到纳秒级光路交换产品、面向铜材料加工的绿光激光器，多家公司带来了面向下一代光互连及其应用场景的新产品。这些新品尚处于不同阶段：有的已经量产，有的正在送样验证，也有的在等待下游市场启动。产品发布的节奏背后，光通信产业链正在为1.6T、NPO、CPO等技术路线提前准备。"
  },
  {
    "id": "wscn:3781625",
    "domain": "股票",
    "title": "交易员警惕线上移：10年期美债收益率破6%，才是个人投资组合的真正红线",
    "url": "https://wallstreetcn.com/articles/3781625",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T04:50:24+00:00",
    "summary": "本周10年期美债收益率一度逼近5%，但彭博调查显示，交易员在个人持仓上能忍受6%以上的收益率。其核心逻辑在于：操作自有资金没有“被解雇”的问责压力，因此风险容忍度远高于管理他人资产的机构行为。此外，相较于美债收益率的绝对水平，其上涨速度对市场的冲击力更大。"
  },
  {
    "id": "wscn:3781573",
    "domain": "股票",
    "title": "10年美债冲向5%！贝森特回购是否被低估？",
    "url": "https://wallstreetcn.com/premium/articles/3781573?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T04:33:52+00:00",
    "summary": "10年美债或破5%，强劲配置需求与贝森特Put将约束上行空间。多空拉锯中贝森特Put短期被高估、中期不应低估。"
  },
  {
    "id": "wscn:3781624",
    "domain": "股票",
    "title": "又见存储巨头“天量奖金”：美光最高发68个月奖金",
    "url": "https://wallstreetcn.com/articles/3781624",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T04:33:12+00:00",
    "summary": "美光科技宣布向中国台湾员工发放35至68个月薪酬的创纪录奖励，最低现金补偿170万新台币。然而，代表中国台湾约三分之二员工的桃园工会拒绝接受，坚持要求将15%营业利润纳入奖金分配，并维持罢工威胁。"
  },
  {
    "id": "wscn:3781623",
    "domain": "股票",
    "title": "柴油价格历史性突破6美元！美国会放“出口管制”大招吗？",
    "url": "https://wallstreetcn.com/articles/3781623",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T04:02:17+00:00",
    "summary": "地缘冲突叠加供应链断裂是柴油价格大涨主因，特朗普政府政策工具已近告罄，\"禁止成品油出口\"被迫提上议程，落地概率被机构评估为35%。但专家几乎一致警告：禁令不仅无法压价，反将适得其反，并重创欧亚能源市场，更与特朗普\"能源主导\"战略背道而驰。"
  },
  {
    "id": "wscn:3781626",
    "domain": "股票",
    "title": "京东健康，可能是最难复制的医疗AI公司",
    "url": "https://wallstreetcn.com/articles/3781626",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T03:46:19+00:00",
    "summary": "一位慢阻肺合并心梗的高龄老人出院回家，血氧指数在90%，老人行动不便，家属通过京东互联网医院联系到一..."
  },
  {
    "id": "wscn:3781622",
    "domain": "股票",
    "title": "一支拖鞋军，正在改写中东格局",
    "url": "https://wallstreetcn.com/articles/3781622",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T03:36:37+00:00",
    "summary": "也门胡塞武装近期发动猛烈攻势，一周内占领六个地区、控制曼德海峡，令装备精良的政府军溃败。其胜因在于指挥统一、战斗意志坚定，而政府军派系林立、依赖外援却得不到及时支援。此役对伊朗是重大战略胜利，对沙特和美国则是严重挫败。随着霍尔木兹与曼德两大能源通道同时告急，中东局势持续动荡，更大风暴或在后头。"
  },
  {
    "id": "wscn:3781555",
    "domain": "股票",
    "title": "付鹏：能源市场成品油的紧张终于传导到了上游，警惕上下游左脚踩右脚【付鹏说4】",
    "url": "https://wallstreetcn.com/premium/articles/3781555?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T02:56:10+00:00",
    "summary": "美国炼厂开工率已达98%，柴油价格创历史新高，出口创新高、库存降至极低水平，表明下游已紧张到极限。随着检修季和冬季临近，炼厂一旦检修或出现故障，柴油价格将急剧上涨并反向拉动原油；叠加交易员已将地缘政治风险溢价转移至下游，上下游可能形成相互推升的“左脚踩右脚”循环。"
  },
  {
    "id": "wscn:3781521",
    "domain": "股票",
    "title": "OpenAI推出Agents API公测版，将Codex背后的harness与基础设施向开发者开放",
    "url": "https://wallstreetcn.com/articles/3781521",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T02:53:56+00:00",
    "summary": "OpenAI正式向外部开发者开放Agents API公测，该API将支撑Codex及企业版ChatGPT的代理框架以编程接口形式提供，仅按token及工具调用量计费。核心能力在于强大的harness机制，包括上下文自动压缩、工具并行调用及多代理协同，支持单次API调用创建生产级代理。"
  },
  {
    "id": "wscn:3781615",
    "domain": "股票",
    "title": "戴尔单日暴涨12%创新高！被甲骨文点名为千亿资本支出“核心供货商”",
    "url": "https://wallstreetcn.com/articles/3781615",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T02:53:05+00:00",
    "summary": "甲骨文管理层点名戴尔，将其列为公司AI资本开支（950亿美元）的直接受益供应商。叠加RBC Capital首次覆盖给予\"跑赢大盘\"评级，分析师强调其AI基础设施供应链护城河，戴尔股价单日飙涨11.98%创历史新高，市值突破3600亿美元，年内累计涨幅近350%。"
  },
  {
    "id": "wscn:3781620",
    "domain": "股票",
    "title": "油价是特朗普的“大麻烦”，而日元是所有人的",
    "url": "https://wallstreetcn.com/articles/3781620",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T02:32:06+00:00",
    "summary": "油价逼近110美元/桶，距中期选举仅剩七周半，民主党重夺参议院概率已突破50%，政治与经济压力正迫使白宫寻求缓和。与此同时，日元结构性升值才是更深层的全球风险——美日利差背离修正、日本资本大规模回流、套息交易被迫平仓，将同步推升欧美债券收益率并唤醒VIX，一场跨资产波动率风暴或已在酝酿之中。"
  },
  {
    "id": "wscn:3781619",
    "domain": "股票",
    "title": "本轮AI牛市两大“网红”合并！SemiAnalysis收购Citrini",
    "url": "https://wallstreetcn.com/articles/3781619",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T01:46:24+00:00",
    "summary": "此次收购将SemiAnalysis在芯片供应链与AI硬件领域的深度技术研究，与Citrini在公开市场投资分析方面的影响力相结合。两者合并，被市场视为一个明确信号：将AI硬件建设与公开市场股票表现相连接的综合性研究，正成为稀缺且高价值的资产。"
  },
  {
    "id": "wscn:3781600",
    "domain": "股票",
    "title": "“AI股神”杀回来了：重建此前“爆仓仓位”，但降低杠杆",
    "url": "https://wallstreetcn.com/articles/3781600",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T01:42:55+00:00",
    "summary": "\"AI股神\"Leopold Aschenbrenner在创下对冲基金史上最大单笔亏损后，正借助弹性看涨期权卷土重来，重建AMD、英特尔、SK海力士等AI半导体核心头寸。此次改用全额付款期权替代总收益互换，理论上规避爆仓风险，但策略逻辑未变，仍依赖触发轧空策略推动动量。"
  },
  {
    "id": "wscn:3781618",
    "domain": "股票",
    "title": "美联储一旦开启加息周期，“连加3次”是合理预期？",
    "url": "https://wallstreetcn.com/articles/3781618",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T01:16:30+00:00",
    "summary": "BMO预计10月、12月将连续跟进，三次合计加息或抹去2025年全部降息成果；先锋集团认为\"连加三次\"是合理起点，但实际次数可能高达六次。历史上存在例外：1997年美联储仅加息一次，此后18个月内未再行动。与此同时，AI巨头万亿级债务融资、保险业私人信贷敞口，及10年期美债收益率逼近5%，为本轮加息周期最危险的压力点。"
  },
  {
    "id": "wscn:3781616",
    "domain": "股票",
    "title": "高盛也“改口”了：下周美联储会加息！",
    "url": "https://wallstreetcn.com/articles/3781616",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T00:59:29+00:00",
    "summary": "高盛从预测按兵不动到押注下周加息25基点，并表示这次转向并非因为通胀数据有多糟糕——8月CPI虽称不上完美，但也未令人警觉。真正的关键在于：沃什鹰派发言已引导市场预期\"若通胀数据不够完美则加息\"，美联储若此时退缩，公信力将遭重创，长端利率恐即刻剧烈反应。"
  },
  {
    "id": "wscn:3781614",
    "domain": "股票",
    "title": "美国赤字逼近2万亿，利息账单首破1万亿，长端美债为债务螺旋定价",
    "url": "https://wallstreetcn.com/articles/3781614",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T00:43:43+00:00",
    "summary": "美国2026财年前11个月联邦赤字达1.97万亿美元，创历史次高，净利息支出突破1万亿美元，首超国防支出。市场正将长端美债从\"无风险基准\"重新定价为\"财政风险资产\"，债务螺旋自我强化迹象日趋明显。"
  },
  {
    "id": "wscn:3781613",
    "domain": "股票",
    "title": "报道：英伟达洽谈在Anthropic IPO中投资高达100亿美元",
    "url": "https://wallstreetcn.com/articles/3781613",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T00:36:56+00:00",
    "summary": "9月11日据路透社报道，Anthropic正与英伟达洽谈，寻求将这家芯片巨头引入其IPO作为基石投资者。英伟达正考虑向Anthropic的IPO投入最多100亿美元。基石投资者通常是在IPO向市场公开发行前承诺认购特定份额的机构投资者，为上市提供早期背书。"
  },
  {
    "id": "wscn:3781612",
    "domain": "股票",
    "title": "伦巴德：GPIF超配日债或引发全球套息平仓，西班牙国际银行：GPIF或抛售620亿美元美债！",
    "url": "https://wallstreetcn.com/articles/3781612",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T23:15:05+00:00",
    "summary": "伦巴德全球宏观研究指出，GPIF正在或即将加速回流日本国内债券，这一结构性资金回流将推动USD/JPY跌破150，并指向130至140的公允价值区间，而全球套息交易的被动去杠杆风险尚未被市场充分定价。西班牙国际银行指出，由于日本本土资产吸引力的提升，在现行政策框架下，GPIF或减持高达620亿美元美债。"
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
    "id": "hn:49594251",
    "domain": "金融",
    "title": "Switzerland's Federal Government Is Replacing Microsoft on 3k Computers",
    "url": "https://itsfoss.com/news/switzerland-replace-microssoft-pilot/",
    "source": "ivell",
    "platform": "hackernews",
    "points": 370,
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
    "points": 169,
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
    "id": "hn:49626052",
    "domain": "金融",
    "title": "One woman's Tesla was remotely controlled by an abusive ex-partner",
    "url": "https://www.theguardian.com/australia-news/2026/sep/09/how-one-womans-tesla-was-remotely-controlled-and-harass-by-her-abusive-ex-partner-ntwnfb",
    "source": "gradschool",
    "platform": "hackernews",
    "points": 73,
    "published_at": "2026-09-09T13:16:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:49596610",
    "domain": "金融",
    "title": "Initial effects of AI technology on employment look positive",
    "url": "https://www.economist.com/finance-and-economics/2026/09/04/the-jobs-apocalypse-is-postponed-an-ai-jobs-boom-is-here",
    "source": "MrBuddyCasino",
    "platform": "hackernews",
    "points": 100,
    "published_at": "2026-09-07T10:38:32+00:00",
    "summary": ""
  },
  {
    "id": "hn:49599058",
    "domain": "金融",
    "title": "If a Tesla Cybercab fleet were profitable, Tesla wouldn't sell you one",
    "url": "https://electrek.co/2026/09/07/tesla-cybercab-fleet-profitable-wouldnt-sell/",
    "source": "jijojv",
    "platform": "hackernews",
    "points": 99,
    "published_at": "2026-09-07T14:49:43+00:00",
    "summary": ""
  },
  {
    "id": "hn:49612981",
    "domain": "金融",
    "title": "DOJ Blocked ICE Agent Shooting Charge over Federal Prosecutor's Objections",
    "url": "https://www.propublica.org/article/doj-blocks-charges-ice-agent-minneapolis-julio-cesar-sosa-celis",
    "source": "paimapi",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-09-08T16:54:03+00:00",
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
