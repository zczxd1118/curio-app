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

- 今日日期：`2026-09-03`
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
  "date": "2026-09-03",
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
    "points": 4424307,
    "published_at": "2026-01-15T03:56:12+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n1. 构建智能体设计模式：反射、工具使用、规划与多智能体工作流；\n2. 将人工智能与外部工具集成：数据库、API、网络搜索与代码执行；\n3. 评估并优化人工智能系统：性能指标、错误分析与生产部署"
  },
  {
    "id": "bvid:BV1E7wtzaEdq",
    "domain": "AI",
    "title": "从 LLM 到 Agent Skill，一期视频带你打通底层逻辑！",
    "url": "http://www.bilibili.com/video/av116227955497963",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 1812233,
    "published_at": "2026-03-14T14:22:56+00:00",
    "summary": "AI 核心概念大串联：LLM, Token, Context, Context Window, Prompt, User Prompt, System Prompt, Tool, MCP, Agent, Agent Skill，一期视频带你打通 AI 底层逻辑！"
  },
  {
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "9分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 1798059,
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
    "points": 1233486,
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
    "points": 1148448,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1o4gw6ZExs",
    "domain": "AI",
    "title": "我是怎么用AI干活的？",
    "url": "http://www.bilibili.com/video/av117092535768773",
    "source": "林亦LYi",
    "platform": "bilibili",
    "points": 1082447,
    "published_at": "2026-08-14T12:00:00+00:00",
    "summary": "AI 办公到底能干些啥？它真的能颠覆我们的工作方式，以至于让大厂押上身家也要卷吗？"
  },
  {
    "id": "bvid:BV1kX546QEjG",
    "domain": "AI",
    "title": "保姆级Claude Code速成，必学！简单！【附完整文档】",
    "url": "http://www.bilibili.com/video/av116554859545963",
    "source": "数字游牧人",
    "platform": "bilibili",
    "points": 1072867,
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
    "points": 880940,
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
    "points": 866425,
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
    "points": 691557,
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
    "points": 688446,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 657095,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 441428,
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
    "points": 421922,
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
    "points": 353402,
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
    "points": 322120,
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
    "points": 279689,
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
    "points": 265214,
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
    "points": 253009,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 180490,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 178900,
    "published_at": "2026-04-27T08:51:41+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n   喜欢视频课程的同学一键三连多多支持一下，长按点赞五秒=lv6大佬 可以的发送彩色弹幕哦。\n配套源码项目已打包评论区回复up"
  },
  {
    "id": "bvid:BV16NvCBrEVs",
    "domain": "AI",
    "title": "什么是Vibe Coding，以及怎么使用？",
    "url": "http://www.bilibili.com/video/av115797133368973",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 164484,
    "published_at": "2025-12-28T12:36:33+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 161615,
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
    "points": 156873,
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
    "points": 154589,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1nM6dBdER6",
    "domain": "AI",
    "title": "vscode如何使用AI编程",
    "url": "http://www.bilibili.com/video/av115875633960242",
    "source": "波哥的编程课",
    "platform": "bilibili",
    "points": 138480,
    "published_at": "2026-01-11T08:58:44+00:00",
    "summary": "如何在vs code中使用AI进行开发，推荐了国产AI编程助手，包括安装扩展、注册登录、选择模型、生成代码和微调代码等步骤。同时，强调AI编程还有很多复杂方面，欢迎在评论区留言。"
  },
  {
    "id": "bvid:BV1wqMw6NEB6",
    "domain": "AI",
    "title": "Claude的安装并且如何配置ccswitch转接第三方API完整使用教程#codex #ai #安装#大模型#API#ccswitch#claude",
    "url": "http://www.bilibili.com/video/av116861479946306",
    "source": "老便秘了",
    "platform": "bilibili",
    "points": 121622,
    "published_at": "2026-07-04T11:32:40+00:00",
    "summary": "Claude的安装并且如何配置ccswitch转接第三方API完整使用教程#codex #ai #安装#大模型#API#ccswitch#claude"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 106194,
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
    "points": 93544,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1V6tP6zENk",
    "domain": "AI",
    "title": "我爸用 Vibe Coding 做了个“专治写作走神”的软件，治法有点狠",
    "url": "http://www.bilibili.com/video/av117173787826916",
    "source": "大不溜add小不溜",
    "platform": "bilibili",
    "points": 75619,
    "published_at": "2026-08-28T15:19:16+00:00",
    "summary": "我爸说想做一个能让人专心写东西的软件。\n结果一走神、一切屏，回来以后事情就开始不对劲了。\n这是最近做的第一个 Vibe Coding 小发明，后面准备继续把一些奇奇怪怪的产品脑洞真的做出来。"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 54742,
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
    "points": 47681,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 41337,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV15hNq6LE6V",
    "domain": "AI",
    "title": "7月最新Claude防封号最安全的！注册+订阅充值教程！A畜看到直接腿软，大喊完蛋了，随后呜呼",
    "url": "http://www.bilibili.com/video/av116923035617928",
    "source": "harness使用教程-",
    "platform": "bilibili",
    "points": 40126,
    "published_at": "2026-07-15T09:16:34+00:00",
    "summary": "AI充值站：njzqhy.top"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operitAI教程：入门安卓最强大ai平台",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 37981,
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
    "points": 30452,
    "published_at": "2026-07-27T09:19:37+00:00",
    "summary": "还在卷传统软件测试？2026年必学的AI智能体(Agent)测试来了！本期视频专为0基础小白打造，从软件测试基础讲起...若要本视频配套资源笔记可加up主企微（请看置顶留言最后一句话）。"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29695,
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
    "points": 28913,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1WtoTBiEuR",
    "domain": "AI",
    "title": "Claude Code多Agent模式实战分享",
    "url": "http://www.bilibili.com/video/av116454666012312",
    "source": "Simon林_",
    "platform": "bilibili",
    "points": 25317,
    "published_at": "2026-04-23T15:18:08+00:00",
    "summary": "Claude Code有2种多Agent模式：多个subagents模式和多个独立agent模式"
  },
  {
    "id": "bvid:BV1Z5KU6UExC",
    "domain": "AI",
    "title": "【吴恩达2026】Vibe Coding保姆级教程，手把手从环境搭建到工作流完整闭环！——DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116951003242391",
    "source": "吴恩达AIAgent",
    "platform": "bilibili",
    "points": 23374,
    "published_at": "2026-07-20T07:01:13+00:00",
    "summary": "本套课专门解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22756,
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
    "points": 20936,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV14erKYuEaE",
    "domain": "AI",
    "title": "最强编程AI Cursor+Unity制作一个史诗游戏(详细)",
    "url": "http://www.bilibili.com/video/av113774908413987",
    "source": "多西杰克",
    "platform": "bilibili",
    "points": 17784,
    "published_at": "2025-01-05T09:01:00+00:00",
    "summary": "网上惊呼Cursor AI厉害的内容很多，但结合Unity做游戏的不多，我就来实测一下，做一个AAA大作......"
  },
  {
    "id": "bvid:BV1iDRQBrEF6",
    "domain": "AI",
    "title": "Claude + Blender 现在太强了 —— 完整免费设置",
    "url": "http://www.bilibili.com/video/av116543333601720",
    "source": "设计之道",
    "platform": "bilibili",
    "points": 16623,
    "published_at": "2026-05-09T07:11:36+00:00",
    "summary": "【简介】\nAnthropic 刚刚发布了用于创意工具的官方 Claude Connectors —— 其中 Blender 连接器对 3D 艺术家来说最重要。在本视频中，我将展示最佳的 Claude + Blender 免费设置，以及为什么这次更新可能会改变我们构建 3D 场景的方式。\n\n【你将学到】\n01:13 步骤 1：安装 Blender MCP 和 Claude Code\n02:31 步骤"
  },
  {
    "id": "bvid:BV1eMgG6QEeG",
    "domain": "AI",
    "title": "【吴恩达】这绝对是把《Vibe Coding》讲得最通透的一套课！手把手教你构建自己的企业级AI工作流，学完直接落地！——附带课件代码",
    "url": "http://www.bilibili.com/video/av117081815189025",
    "source": "吴恩达Agents",
    "platform": "bilibili",
    "points": 14315,
    "published_at": "2026-08-12T09:29:57+00:00",
    "summary": "Vibe Coding火了，但你会发现——AI写的代码像开盲盒，今天能跑明天崩，项目一大就乱套。\n规范驱动开发（SDD） 就是来解决这个问题的。它的核心理念很简单：在让AI写代码之前，先和AI在统一的规范文档里对齐需求，把开发变成可预测、可追溯、可控制的过程。"
  },
  {
    "id": "bvid:BV1ZWRrBJEaQ",
    "domain": "AI",
    "title": "我是如何用Claude skills从Excel到数据分析+图表可视化",
    "url": "http://www.bilibili.com/video/av116519862340507",
    "source": "迪迪碎碎念_AI",
    "platform": "bilibili",
    "points": 13747,
    "published_at": "2026-05-05T03:36:14+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1HhGo6aEvE",
    "domain": "AI",
    "title": "本地大模型也能联网搜索！LM Studio × MCP 接入教程",
    "url": "http://www.bilibili.com/video/av116635490911881",
    "source": "aopstudio",
    "platform": "bilibili",
    "points": 12075,
    "published_at": "2026-05-25T13:41:46+00:00",
    "summary": "本视频演示如何为 LM Studio 接入 MCP 联网搜索服务，让本地运行的大模型具备实时搜索网络的能力。\nMCP（Model Context Protocol）是 Anthropic 推出的开放协议，允许模型通过标准化接口调用外部工具。本次接入的搜索服务来自 MCPWorld，底层通过 npx 调用，无需额外部署服务端，配置完成后即可在 LM Studio 的对话界面中直接发起联网搜索。\n本视"
  },
  {
    "id": "bvid:BV1zbduYgEBH",
    "domain": "AI",
    "title": "Cursor新手教程⑤：Cursor降智真相+解决办法",
    "url": "http://www.bilibili.com/video/av114311359891940",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 10919,
    "published_at": "2025-04-10T02:53:27+00:00",
    "summary": "你是不是经常碰到这种情况：\n你试图修复一个小错误\n人工智能给出一个看似合理的更改建议\n这个修复导致其他地方出错\n你要求人工智能修复新出现的问题\n这又产生了另外两个问题\n如此反复\n本视频带你拆解Cursor降智的真相以及解决办法"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 9984,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 9471,
    "published_at": "2025-04-14T02:30:00+00:00",
    "summary": "MCP服务网站：https://smithery.ai/\nCherry Studio官方网站：https://cherry-ai.com/"
  },
  {
    "id": "hn:49458161",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia agrees to acquire Hugging Face for $13B",
    "url": "https://www.businessinsider.com/nvidia-in-talks-to-buy-hugging-face-13-billion-dollars-2026-8",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 1981,
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
    "id": "rss:https://www.eetimes.com/mercedes-spinout-athos-closes-its-doors/",
    "domain": "AI 算力 / 半导体",
    "title": "Mercedes Spinout Athos Closes Its Doors",
    "url": "https://www.eetimes.com/mercedes-spinout-athos-closes-its-doors/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T17:07:04+00:00",
    "summary": "The startup was unable to secure the financing required to continue commercialising its chiplet-based technology The post Mercedes Spinout Athos Closes Its Doors appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/secure-safety-security-communications-cut-time-complexity-and-install-cost/",
    "domain": "AI 算力 / 半导体",
    "title": "Secure Safety & Security Communications: Cut Time, Complexity, and Install Cost",
    "url": "https://www.eetimes.com/secure-safety-security-communications-cut-time-complexity-and-install-cost/",
    "source": "Analog Devices",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T13:21:11+00:00",
    "summary": "Join this webinar, where we will demonstrate how to enable next-generation security and building safety networks while reducing wiring complexity, improving fault detection, and much more. The post Se"
  },
  {
    "id": "rss:https://www.eetimes.com/astella-joins-5g-acia-shanghai-to-advance-industrial-5g-and-iiot-innovation/",
    "domain": "AI 算力 / 半导体",
    "title": "Astella Joins 5G-ACIA Shanghai to Advance Industrial 5G and IIoT Innovation",
    "url": "https://www.eetimes.com/astella-joins-5g-acia-shanghai-to-advance-industrial-5g-and-iiot-innovation/",
    "source": "Astella Technologies Limited",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T13:19:21+00:00",
    "summary": "Astella announces its participation in the 5G-ACIA Industrial 5G Day in Shanghai, a dedicated industry event focused on Industrial 5G. The post Astella Joins 5G-ACIA Shanghai to Advance Industrial 5G "
  },
  {
    "id": "rss:https://www.eetimes.com/manufacturing-growth-slows-in-august-amid-supply-and-cost-strains/",
    "domain": "AI 算力 / 半导体",
    "title": "Manufacturing Growth Slows in August Amid Supply and Cost Strains",
    "url": "https://www.eetimes.com/manufacturing-growth-slows-in-august-amid-supply-and-cost-strains/",
    "source": "News Desk",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T13:00:00+00:00",
    "summary": "U.S. manufacturing growth continued for the eighth consecutive month in August, though momentum slowed due to supply chain and cost pressures. The post Manufacturing Growth Slows in August Amid Supply"
  },
  {
    "id": "rss:https://www.eetimes.com/indian-startup-hrdwyr-builds-ai-native-socs-for-the-physical-world/",
    "domain": "AI 算力 / 半导体",
    "title": "Indian Startup HrdWyr Builds AI-Native SoCs for the Physical World",
    "url": "https://www.eetimes.com/indian-startup-hrdwyr-builds-ai-native-socs-for-the-physical-world/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T08:00:00+00:00",
    "summary": "HrdWyr is developing AI-native SoCs for power management, motor control, and other applications where AI meets physical systems. The post Indian Startup HrdWyr Builds AI-Native SoCs for the Physical W"
  },
  {
    "id": "rss:https://www.eetimes.com/from-silos-to-systems-from-data-to-insight/",
    "domain": "AI 算力 / 半导体",
    "title": "From Silos to Systems, from Data to Insight: Unlocking Organizational Knowledge and Winning in the AI Era with Keysight SOS Enterprise",
    "url": "https://www.eetimes.com/from-silos-to-systems-from-data-to-insight/",
    "source": "Keysight Technologies",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T03:41:26+00:00",
    "summary": "The white paper introduces Keysight SOS Enterprise as an AI-ready engineering data and IP management platform designed to help semiconductor and electronics companies centrally manage, govern, and sec"
  },
  {
    "id": "rss:https://www.eetimes.com/exclusive-sir-robin-saxby-reflects-on-impact-of-ai-geopolitics-and-retirement/",
    "domain": "AI 算力 / 半导体",
    "title": "Exclusive: Sir Robin Saxby Reflects on Impact of AI, Geopolitics, and Retirement",
    "url": "https://www.eetimes.com/exclusive-sir-robin-saxby-reflects-on-impact-of-ai-geopolitics-and-retirement/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T22:00:00+00:00",
    "summary": "An EE Times exclusive video interview with Sir Robin Saxby, founding CEO of Arm, on industry transformation in the age of AI, geopolitics, and how retirement has allowed him to support new startups. T"
  },
  {
    "id": "rss:https://www.eetimes.com/how-ai-is-reshaping-the-global-semiconductor-patent-landscape/",
    "domain": "AI 算力 / 半导体",
    "title": "How AI Is Reshaping the Global Semiconductor Patent Landscape",
    "url": "https://www.eetimes.com/how-ai-is-reshaping-the-global-semiconductor-patent-landscape/",
    "source": "Stefani Munoz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T16:32:49+00:00",
    "summary": "AI is turning chip patents into a geopolitical battle for dominance, from Nvidia’s CUDA moat to China’s filing surge. The post How AI Is Reshaping the Global Semiconductor Patent Landscape appeared fi"
  },
  {
    "id": "rss:https://www.eetimes.com/opportunity-charging-enabled-by-fast-charging-multivoltage-batteries/",
    "domain": "AI 算力 / 半导体",
    "title": "Opportunity Charging Enabled by Fast Charging MultiVoltage Batteries",
    "url": "https://www.eetimes.com/opportunity-charging-enabled-by-fast-charging-multivoltage-batteries/",
    "source": "Green Cubes Technology",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T14:56:51+00:00",
    "summary": "While opportunity charging is a practice applicable to both Lead Acidand Lithium-ion (Li-ion) batteries for motive power systems, fast charging is a key differentiator for Lithium-ion batteries. Becau"
  },
  {
    "id": "rss:https://www.eetimes.com/the-future-of-cable-testing-why-intelligent-automation-is-replacing-manual-validation/",
    "domain": "AI 算力 / 半导体",
    "title": "The Future of Cable Testing: Why Intelligent Automation is Replacing Manual Validation",
    "url": "https://www.eetimes.com/the-future-of-cable-testing-why-intelligent-automation-is-replacing-manual-validation/",
    "source": "Vitrek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T14:39:23+00:00",
    "summary": "This whitepaper examines the limitations of manual cable validation processes and explores how automated testing strategies help address common engineering and manufacturing pain points. Topics includ"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/microsoft-will-expand-windows-11-memory-integrity-feature-to-more-pcs-starting-in-october-security-feature-reduces-gaming-performance-on-some-systems",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft will expand Windows 11 Memory Integrity feature to more PCs starting in October — security feature reduces gaming performance on some systems",
    "url": "https://www.tomshardware.com/software/windows/microsoft-will-expand-windows-11-memory-integrity-feature-to-more-pcs-starting-in-october-security-feature-reduces-gaming-performance-on-some-systems",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T16:07:29+00:00",
    "summary": "Microsoft will begin enabling Memory Integrity by default on more eligible Windows PCs through quality updates in October, expanding kernel-level protection while preserving existing opt-outs for user"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/hybrid-bonding-roadmap-examined",
    "domain": "AI 算力 / 半导体",
    "title": "The current state of Hybrid Bonding in 2026 — TSMC sits at 6 microns and the HBM delay that nobody expected",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/hybrid-bonding-roadmap-examined",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T15:05:41+00:00",
    "summary": "Hybrid bonding, the copper-to-copper joining technique that replaces solder microbumps in 3D chip stacks, is in high-volume production on logic and freshly postponed on memory."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/gopro-to-expand-into-ai-data-centers-after-usd285-million-merger-with-optical-photonics-company-move-to-solve-camera-makers-financial-woes-move-manufacturing-back-into-the-us",
    "domain": "AI 算力 / 半导体",
    "title": "GoPro to expand into AI data centers after $285 million merger with optical-photonics company — move to solve camera maker’s financial woes, move manufacturing back into the US",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/gopro-to-expand-into-ai-data-centers-after-usd285-million-merger-with-optical-photonics-company-move-to-solve-camera-makers-financial-woes-move-manufacturing-back-into-the-us",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T14:43:10+00:00",
    "summary": "GoPro is merging with optical-photonics company Starman Optical in a deal worth at least $285 million. This move will wipe out the company's $92 million outstanding debt, let it start manufacturing it"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/samsung-teases-new-hbm5-with-twice-the-performance-of-hbm4e-ambitious-data-transfer-rates-could-hint-at-4-096-bit-interface",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung teases new HBM5 with twice the performance of HBM4E —ambitious data transfer rates could hint at 4,096-bit interface",
    "url": "https://www.tomshardware.com/pc-components/dram/samsung-teases-new-hbm5-with-twice-the-performance-of-hbm4e-ambitious-data-transfer-rates-could-hint-at-4-096-bit-interface",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T14:38:20+00:00",
    "summary": "Samsung expects HBM5 to deliver 4 TB/s of bandwidth per stack by late 2020s, which will enable AI accelerators with aggregated memory bandwidth of around 100 TB/s."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/russian-hacker-faces-up-to-20-years-in-prison-following-extradition-and-indictment-over-us-phishing-campaign-that-allegedly-infected-80-000-pcs-hacker-stole-victims-data-via-remote-access",
    "domain": "AI 算力 / 半导体",
    "title": "Russian hacker faces up to 20 years in prison, following extradition and indictment over US phishing campaign that allegedly infected 80,000 PCs — hacker stole victims' data via remote access",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/russian-hacker-faces-up-to-20-years-in-prison-following-extradition-and-indictment-over-us-phishing-campaign-that-allegedly-infected-80-000-pcs-hacker-stole-victims-data-via-remote-access",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T14:22:37+00:00",
    "summary": "Russian national faces US charges over a phishing campaign that allegedly infected 80,000 PCs and stole credentials and personal data"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/storage/tape-companies-ship-160-exabytes-of-storage-in-2025-ai-data-demands-drive-unprecedented-data-growth-capacity-shipped-in-q1-2026-rose-57-percent-yoy-driven-by-ai-lto-9-momentum-and-early-lto-10-uptake",
    "domain": "AI 算力 / 半导体",
    "title": "Tape companies ship 160 exabytes of storage in 2025, AI data demands drive 'unprecedented data growth' — capacity shipped in Q1 2026 rose 57% YOY driven by AI, LTO‑9 momentum, and early LTO‑10 uptake",
    "url": "https://www.tomshardware.com/pc-components/storage/tape-companies-ship-160-exabytes-of-storage-in-2025-ai-data-demands-drive-unprecedented-data-growth-capacity-shipped-in-q1-2026-rose-57-percent-yoy-driven-by-ai-lto-9-momentum-and-early-lto-10-uptake",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T13:24:55+00:00",
    "summary": "Tape storage companies celebrate capacity shipment growth of 57% YOY for Q1 2026."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/we-explored-early-dlss-5-performance-with-community-mods-and-the-limits-of-the-12v-2x6-power-connector-may-hold-it-back-on-the-rtx-5090",
    "domain": "AI 算力 / 半导体",
    "title": "We explored early DLSS 5 performance with community mods — and the limits of the 12V-2x6 power connector may hold it back on the RTX 5090",
    "url": "https://www.tomshardware.com/pc-components/gpus/we-explored-early-dlss-5-performance-with-community-mods-and-the-limits-of-the-12v-2x6-power-connector-may-hold-it-back-on-the-rtx-5090",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T13:21:38+00:00",
    "summary": "DLSS 5 officially releases later this week, but we tested it on the RTX 5090 using community mods to see what kind of performance drop and extra power draw you can expect."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/fbi-investigating-153-million-us-and-canadian-drivers-licenses-leaked-on-russian-cybercrime-forum-including-that-of-us-secdef-pete-hegseth-data-is-suspected-to-have-come-from-an-id-authentication-service-provider",
    "domain": "AI 算力 / 半导体",
    "title": "FBI investigating 153 million US and Canadian driver’s licenses leaked on Russian cybercrime forum, including that of US SecDef Pete Hegseth — data is suspected to have come from an ID-authentication ",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/fbi-investigating-153-million-us-and-canadian-drivers-licenses-leaked-on-russian-cybercrime-forum-including-that-of-us-secdef-pete-hegseth-data-is-suspected-to-have-come-from-an-id-authentication-service-provider",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T13:14:05+00:00",
    "summary": "The leak was traced to a major ID-authentication service based in Louisiana, serving major companies like Hertz, Target, and the United States Coast Guard."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-headsets/usd30-buys-you-a-brand-new-hyperx-gaming-headset-save-40-percent-on-the-cloudx-stinger-2-with-massive-50mm-drivers",
    "domain": "AI 算力 / 半导体",
    "title": "$30 buys you a brand-new HyperX gaming headset — save 40% on the CloudX Stinger 2 with massive 50mm drivers",
    "url": "https://www.tomshardware.com/peripherals/gaming-headsets/usd30-buys-you-a-brand-new-hyperx-gaming-headset-save-40-percent-on-the-cloudx-stinger-2-with-massive-50mm-drivers",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T13:12:33+00:00",
    "summary": "With a massive 40% knocked off the list price, the HyperX CloudX Stinger 2 is only $29.99 on the HyperX store."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/pc-cases/fractal-define-one-case-review",
    "domain": "AI 算力 / 半导体",
    "title": "Fractal Define One case review: Balancing noise and thermals",
    "url": "https://www.tomshardware.com/pc-components/pc-cases/fractal-define-one-case-review",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T13:05:00+00:00",
    "summary": "Fractal’s Define One rounds off the boxy Define, while still keeping the iconic closed-front design. A focus on GPU airflow and three included Momentum 14 fans highlight this $154 mid-tower chassis."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/pc-cases/fractal-summit-case-review",
    "domain": "AI 算力 / 半导体",
    "title": "Fractal Summit case review: real wood accents scream premium, but it only stands out in white or black",
    "url": "https://www.tomshardware.com/pc-components/pc-cases/fractal-summit-case-review",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T13:00:00+00:00",
    "summary": "The Fractal Summit is a good-looking, open-face mid-tower with real wood accents that's easy to build in. But noise-normalized thermals landed a bit warmer than we expected."
  },
  {
    "id": "rss:https://www.tomshardware.com/cameras/korean-researchers-build-usd7-hidden-camera-detector-gadget-uses-led-lights-and-ai-to-separate-reflections-from-lenses",
    "domain": "AI 算力 / 半导体",
    "title": "Researchers build a $7 smartphone clip-on that spots hidden cameras — AI and dynamic LED grid deliver 94% accuracy",
    "url": "https://www.tomshardware.com/cameras/korean-researchers-build-usd7-hidden-camera-detector-gadget-uses-led-lights-and-ai-to-separate-reflections-from-lenses",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T12:20:00+00:00",
    "summary": "This gadget only costs $7 but can help your catch hidden cameras through the use of the companion AI app that installs on your phone. It works by changing the location of the LED light source to compa"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/power-supplies/questionable-pc-power-supply-explodes-bursts-into-flames-the-moment-its-plugged-into-a-socket-viral-video-captures-moment-repair-shop-worker-avoids-disaster",
    "domain": "AI 算力 / 半导体",
    "title": "Questionable PC power supply 'explodes,' bursts into flames the moment it's plugged into a socket in viral video — video captures moment repair shop worker avoids disaster",
    "url": "https://www.tomshardware.com/pc-components/power-supplies/questionable-pc-power-supply-explodes-bursts-into-flames-the-moment-its-plugged-into-a-socket-viral-video-captures-moment-repair-shop-worker-avoids-disaster",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T11:40:00+00:00",
    "summary": "Clearly, one PSU in Vietnam did not live up to this expectation, as CCTV footage from a shop shows it bursting into flames as soon as it's plugged into the socket. Even though it caught on fire, thank"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/eff-asks-california-governor-to-veto-bill-that-would-require-online-age-verification-electronic-frontier-foundation-argues-bill-would-result-in-privacy-invasive-checks-and-step-on-first-amendment",
    "domain": "AI 算力 / 半导体",
    "title": "EFF asks California governor to veto bill that would require online age verification — Electronic Frontier Foundation argues bill would result in privacy-invasive checks and step on First Amendment",
    "url": "https://www.tomshardware.com/tech-industry/eff-asks-california-governor-to-veto-bill-that-would-require-online-age-verification-electronic-frontier-foundation-argues-bill-would-result-in-privacy-invasive-checks-and-step-on-first-amendment",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T11:20:00+00:00",
    "summary": "Electronic Frontier Foundation asks California governor to veto bill that would require online age verification — EFF argues A.B. 1709 would result in privacy-invasive checks and step on First Amendme"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ddr5/this-32gb-ddr5-ram-kit-is-now-the-cheapest-on-sale-dropping-back-under-usd400-13-percent-discount-on-an-unflashy-pny-memory-kit-for-new-gaming-pc-builds-or-upgrades",
    "domain": "AI 算力 / 半导体",
    "title": "This 32GB DDR5 RAM kit is now the cheapest on sale, dropping back under $400 — 13% discount on an unflashy PNY memory kit for new gaming PC builds or upgrades",
    "url": "https://www.tomshardware.com/pc-components/ddr5/this-32gb-ddr5-ram-kit-is-now-the-cheapest-on-sale-dropping-back-under-usd400-13-percent-discount-on-an-unflashy-pny-memory-kit-for-new-gaming-pc-builds-or-upgrades",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T11:13:14+00:00",
    "summary": "This 32GB DDR5 memory kit from PNY is the cheapest you'll find on sale at the moment, now just $399.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/ai-data-center-investment-projected-to-hit-usd32-trillion-by-2050-infrastructure-spending-estimated-to-exceed-capital-requirements-for-railways-electrification-or-the-internet",
    "domain": "AI 算力 / 半导体",
    "title": "AI data center investment projected to hit $32 trillion by 2050 — infrastructure spending estimated to exceed capital requirements for railways, electrification, or the internet",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/ai-data-center-investment-projected-to-hit-usd32-trillion-by-2050-infrastructure-spending-estimated-to-exceed-capital-requirements-for-railways-electrification-or-the-internet",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T11:00:26+00:00",
    "summary": "These investments aren't massive one-time expenses — data center operators are expected to upgrade their expensive GPUs and related infrastructure every four to six years, as new semiconductor technol"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/techie-creates-a-database-of-coil-whining-graphics-cards-power-supplies-and-liquid-cooler-pumps-open-source-project-wants-community-reports-of-affected-parts",
    "domain": "AI 算力 / 半导体",
    "title": "Techie creates a database of coil-whining graphics cards, power supplies, and liquid cooler pumps — open-source project wants community reports of affected parts",
    "url": "https://www.tomshardware.com/pc-components/techie-creates-a-database-of-coil-whining-graphics-cards-power-supplies-and-liquid-cooler-pumps-open-source-project-wants-community-reports-of-affected-parts",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T11:00:00+00:00",
    "summary": "Techie creates a database of coil-whining graphics cards, PSUs, and AIO pumps — open-source project wants community reports of affected parts"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/startups-pitch-an-airbnb-for-ai-inference-that-pays-gamers-for-their-idle-pcs",
    "domain": "AI 算力 / 半导体",
    "title": "Startups want to rent your idle gaming PC for AI tasks — Startups pitch an 'Airbnb for AI inference,' but profitability remains unproven",
    "url": "https://www.tomshardware.com/pc-components/gpus/startups-pitch-an-airbnb-for-ai-inference-that-pays-gamers-for-their-idle-pcs",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T11:00:00+00:00",
    "summary": "If your gaming rig spends most of its life doing nothing, a pair of startups would be willing to pay you something close to minimum wage for its downtime"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/nintendo/you-can-now-play-gta-v-natively-on-a-nintendo-switch-thanks-to-unofficial-homebrew-port-game-runs-at-30-fps-but-requires-a-jailbroken-overclocked-switch",
    "domain": "AI 算力 / 半导体",
    "title": "You can now play GTA V natively on a Nintendo Switch thanks to unofficial Homebrew port — game runs at 30 FPS but requires a jailbroken, overclocked Switch",
    "url": "https://www.tomshardware.com/video-games/nintendo/you-can-now-play-gta-v-natively-on-a-nintendo-switch-thanks-to-unofficial-homebrew-port-game-runs-at-30-fps-but-requires-a-jailbroken-overclocked-switch",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T10:40:00+00:00",
    "summary": "A team of modders have taken leaked source code and recompiled it to run the game logic natively on the Switch's Arm-based SoC. As long as you overclock the system, you can get a relatively-stable 30 "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/researchers-easily-trick-fortune-500-companies-ai-agents-into-running-arbitrary-code-supply-chain-attack-via-llms-txt-guidance-file-illustrates-how-data-has-become-code",
    "domain": "AI 算力 / 半导体",
    "title": "Researchers easily trick Fortune-500 companies' AI agents into running arbitrary code — supply-chain attack via llms.txt guidance file illustrates how data has become code",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/researchers-easily-trick-fortune-500-companies-ai-agents-into-running-arbitrary-code-supply-chain-attack-via-llms-txt-guidance-file-illustrates-how-data-has-become-code",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T10:20:00+00:00",
    "summary": "Researchers easily trick Fortune-500 companies' AI agents into running arbitrary code. This supply-chain attack, done via using data in public llms.txt guidance files, illustrates the dangers of data "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/chinas-euv-technology-at-a-similar-stage-to-asml-in-2004-analyst-claims-beijings-semiconductor-industry-remains-well-behind-western-rivals",
    "domain": "AI 算力 / 半导体",
    "title": "China's EUV technology 'at a similar stage to ASML in 2004,' analyst claims — Beijing's semiconductor industry remains well behind Western rivals",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/chinas-euv-technology-at-a-similar-stage-to-asml-in-2004-analyst-claims-beijings-semiconductor-industry-remains-well-behind-western-rivals",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T10:15:00+00:00",
    "summary": "Despite rumors, there is no evidence that Chinese makers of lithography tools can produce immersion lithography scanners in quantity."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/space/russian-starlink-rival-flounders-after-entire-batch-of-satellites-fails-to-reach-operational-altitude-many-of-the-16-launched-hit-less-than-half-their-870km-target-and-two-are-already-falling-back-to-earth",
    "domain": "AI 算力 / 半导体",
    "title": "Russian Starlink rival flounders after entire batch of satellites fails to reach operational altitude — many of the 16 launched hit less than half their 870km target, and two are already falling back ",
    "url": "https://www.tomshardware.com/tech-industry/space/russian-starlink-rival-flounders-after-entire-batch-of-satellites-fails-to-reach-operational-altitude-many-of-the-16-launched-hit-less-than-half-their-870km-target-and-two-are-already-falling-back-to-earth",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T10:00:00+00:00",
    "summary": "The entire second batch of Russian Rassvet satellites have failed to reach their target operational altitudes, according to reports."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/oklahoma-city-tries-to-charge-farmer-arrested-at-data-center-debate-usd17-000-for-body-cam-footage-of-the-incident-accused-faces-trespassing-charge-for-going-over-allotted-speaking-time-by-30-seconds-at-a-public-debate",
    "domain": "AI 算力 / 半导体",
    "title": "Oklahoma city tries to charge farmer arrested at data center debate $17,000 for body cam footage of the incident — accused faces trespassing charge for going over allotted speaking time by 30 seconds ",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/oklahoma-city-tries-to-charge-farmer-arrested-at-data-center-debate-usd17-000-for-body-cam-footage-of-the-incident-accused-faces-trespassing-charge-for-going-over-allotted-speaking-time-by-30-seconds-at-a-public-debate",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T10:00:00+00:00",
    "summary": "Claremore admits that one of its reasons for charging so much is because it fears that the documents will be \"subject to wide distribution, including on social media.\""
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/handheld-gaming/acers-wild-project-dualplay-mini-is-a-foldable-handheld-that-doubles-as-a-netbook-concept-shown-alongside-predator-atlas-7-handheld-sporting-intels-arc-g-series-chip",
    "domain": "AI 算力 / 半导体",
    "title": "Acer’s wild Project DualPlay Mini is a foldable handheld that doubles as a netbook — concept shown alongside Predator Atlas 7 handheld sporting Intel’s Arc G-series chip",
    "url": "https://www.tomshardware.com/video-games/handheld-gaming/acers-wild-project-dualplay-mini-is-a-foldable-handheld-that-doubles-as-a-netbook-concept-shown-alongside-predator-atlas-7-handheld-sporting-intels-arc-g-series-chip",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T09:30:00+00:00",
    "summary": "Using the recent Predator Atlas 8 as a blueprint, Acer revealed the smaller Atlas 7 alongside a unique concept called Project DualPlay Mini at IFA 2026."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/acer-launches-seven-new-gaming-monitors-across-nitro-and-predator-families-tri-mode-panels-qd-oleds-mini-leds-1-000-hz-and-more",
    "domain": "AI 算力 / 半导体",
    "title": "Acer launches seven new gaming monitors across Nitro and Predator families — tri-mode panels, QD-OLEDs, Mini LEDs, 1,000 Hz, and more",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/acer-launches-seven-new-gaming-monitors-across-nitro-and-predator-families-tri-mode-panels-qd-oleds-mini-leds-1-000-hz-and-more",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T09:30:00+00:00",
    "summary": "Acer has seven new gaming monitors, including a 1,000 Hz 1080p beast"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/acers-swift-blade-14-weighs-just-1-76-pounds-and-uses-wildcat-lake-company-introduces-new-sub-brand-ahead-of-ifa-tradeshow",
    "domain": "AI 算力 / 半导体",
    "title": "Acer's Swift Blade 14 weighs just 1.76 pounds and uses Wildcat Lake — company introduces new sub-brand ahead of IFA tradeshow",
    "url": "https://www.tomshardware.com/laptops/acers-swift-blade-14-weighs-just-1-76-pounds-and-uses-wildcat-lake-company-introduces-new-sub-brand-ahead-of-ifa-tradeshow",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T09:30:00+00:00",
    "summary": "Acer is increasing its lineup of mid-level laptops, with a new, lightweight Swift Blade 14 and a Swift Air 16 with slightly better specs."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/developer-uses-claude-code-to-debloat-android-smart-tv-for-unbelievable-performance-upgrade-tv-now-smoother-than-it-was-new-as-autonomous-agent-deactivates-apps-shortens-animations-all-without-root-access",
    "domain": "AI 算力 / 半导体",
    "title": "Developer uses Claude Code to debloat Android smart TV for 'unbelievable' performance upgrade — TV now smoother than it was new as autonomous agent deactivates apps, shortens animations, all without r",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/developer-uses-claude-code-to-debloat-android-smart-tv-for-unbelievable-performance-upgrade-tv-now-smoother-than-it-was-new-as-autonomous-agent-deactivates-apps-shortens-animations-all-without-root-access",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T09:00:00+00:00",
    "summary": "A developer revitalized his smart TV performance by using Claude Code to debloat it."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/alienwares-new-qd-oled-gaming-monitors-boast-4k-165-hz-1080p-560-hz-panels-dells-new-oleds-target-gamers-who-prioritize-speed-or-crave-pixel-density",
    "domain": "AI 算力 / 半导体",
    "title": "Alienware's new QD-OLED gaming monitors boast 4K 165 Hz, 1080p 560 Hz panels — Dell’s new OLEDs target gamers who prioritize speed or crave pixel density",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/alienwares-new-qd-oled-gaming-monitors-boast-4k-165-hz-1080p-560-hz-panels-dells-new-oleds-target-gamers-who-prioritize-speed-or-crave-pixel-density",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T07:00:00+00:00",
    "summary": "Alienware’s AW3226Q and AW2527HX gaming monitors target two different segments of the market."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/dells-new-14-inch-laptops-take-on-the-macbook-neo-in-a-new-way-ports-and-colors",
    "domain": "AI 算力 / 半导体",
    "title": "Dell's new 14-inch laptops take on the MacBook Neo in a new way — ports and colors",
    "url": "https://www.tomshardware.com/laptops/dells-new-14-inch-laptops-take-on-the-macbook-neo-in-a-new-way-ports-and-colors",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T07:00:00+00:00",
    "summary": "Dell's new 14S laptops are mainstream devices with more colors and more ports than the XPS 13."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-pours-usd3-5-billion-into-mediatek-company-will-adopt-nvlink-fusion-for-its-custom-ai-accelerators",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia pours $3.5 billion into MediaTek — company will adopt NVLink Fusion for its custom AI accelerators",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-pours-usd3-5-billion-into-mediatek-company-will-adopt-nvlink-fusion-for-its-custom-ai-accelerators",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T14:42:22+00:00",
    "summary": "Nvidia invests $3.5 billion in MediaTek as the companies expand their partnership into custom AI infrastructure with NVLink Fusion, local AI computing, and automotive platforms."
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
    "id": "hn:49537553",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.8 Flash and 3.8 Flash Cyber",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/",
    "source": "bratao",
    "platform": "hackernews",
    "points": 981,
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
    "id": "rss:https://www.theverge.com/tech/985689/anker-put-radar-and-flower-power-into-a-sleep-speaker",
    "domain": "大厂 AI 动态",
    "title": "Anker’s sleep speaker uses radar and flower power to help you relax",
    "url": "https://www.theverge.com/tech/985689/anker-put-radar-and-flower-power-into-a-sleep-speaker",
    "source": "Thomas Ricker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T07:30:00+00:00",
    "summary": "Anker's SleepLab speaker promises to track and enhance sleep without a wearable. It uses millimeter-wave radar (60GHz) blasting from your nightstand to track micro-movements in your chest and body to "
  },
  {
    "id": "rss:https://www.theverge.com/tech/986330/soundcore-headphones-earbuds-announcement-ifa-2026",
    "domain": "大厂 AI 动态",
    "title": "Anker’s Soundcore is bringing its incredible call quality to more headphones",
    "url": "https://www.theverge.com/tech/986330/soundcore-headphones-earbuds-announcement-ifa-2026",
    "source": "John.Higgins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T07:30:00+00:00",
    "summary": "After introducing the Thus processing chip in April and releasing it with the Liberty 5 Pro series earbuds, Soundcore is bringing it to more audio products. The Thus chip is behind the best call quali"
  },
  {
    "id": "rss:https://www.theverge.com/tech/986377/ankers-first-otc-hearing-aids-ifa-2026",
    "domain": "大厂 AI 动态",
    "title": "Anker announces its first over-the-counter hearing aids",
    "url": "https://www.theverge.com/tech/986377/ankers-first-otc-hearing-aids-ifa-2026",
    "source": "John.Higgins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T07:30:00+00:00",
    "summary": "In what could be fortuitous timing for hearing aid users, Anker announced its first over-the-counter (OTC) hearing aids at IFA 2026. It was only a couple months ago when LXE Hearing, the parent compan"
  },
  {
    "id": "rss:https://www.theverge.com/tech/986948/anker-eufymake-personal-fabric-printer-dtg-dtf-ifa",
    "domain": "大厂 AI 动态",
    "title": "Anker’s new printer works directly on fabrics",
    "url": "https://www.theverge.com/tech/986948/anker-eufymake-personal-fabric-printer-dtg-dtf-ifa",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T07:30:00+00:00",
    "summary": "After introducing a consumer-friendly UV printer last year capable of printing designs directly on materials like wood, metal, glass, and acrylic, Anker's eufyMake brand is introducing a new machine t"
  },
  {
    "id": "rss:https://www.theverge.com/tech/987936/anker-eufy-mindbase-ai-security-camera-system-matter",
    "domain": "大厂 AI 动态",
    "title": "Anker’s new MindBase is an AI-powered brain for your smart home",
    "url": "https://www.theverge.com/tech/987936/anker-eufy-mindbase-ai-security-camera-system-matter",
    "source": "Jennifer Pattison Tuohy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T07:30:00+00:00",
    "summary": "Anker is launching the Eufy MindBase, a local AI hub for its security cameras that runs an on-device, Anker-developed LLM, which the company says can process your footage without it ever leaving your "
  },
  {
    "id": "rss:https://www.theverge.com/tech/988144/philips-hue-nanoleaf-smart-wall-panels-integration-module",
    "domain": "大厂 AI 动态",
    "title": "Philips Hue adds Nanoleaf&#8217;s light panels to its ecosystem with a $40 module",
    "url": "https://www.theverge.com/tech/988144/philips-hue-nanoleaf-smart-wall-panels-integration-module",
    "source": "Jennifer Pattison Tuohy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T07:30:00+00:00",
    "summary": "Philips Hue is finally adding wall panels into its smart lighting portfolio. But instead of developing its own, it's partnered with longtime rival Nanoleaf, the company that invented the smart modular"
  },
  {
    "id": "rss:https://www.theverge.com/tech/988265/anker-sleep-earbuds-4-pro-price-date-specs",
    "domain": "大厂 AI 动态",
    "title": "Anker put a display on the case of its new sleepbuds",
    "url": "https://www.theverge.com/tech/988265/anker-sleep-earbuds-4-pro-price-date-specs",
    "source": "Thomas Ricker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T07:30:00+00:00",
    "summary": "Anker just announced its new Soundcore Sleep Earbuds 4 and 4 Pro for side-sleepers. They include the same audio masking tech found on last year's A30 sleepbuds (that can really silent a snoring partne"
  },
  {
    "id": "rss:https://www.theverge.com/tech/988363/philips-hue-play-screen-sync-entertainment-lighting",
    "domain": "大厂 AI 动态",
    "title": "Philips Hue adds more affordable options for syncing smart lights with your TV",
    "url": "https://www.theverge.com/tech/988363/philips-hue-play-screen-sync-entertainment-lighting",
    "source": "Jennifer Pattison Tuohy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T07:30:00+00:00",
    "summary": "Philips Hue is slashing the steep entry price of its entertainment sync offerings. The new stripped-down Sync Box 4K starts at $150, compared to $385 for the 8K model. The brand also launched its firs"
  },
  {
    "id": "rss:https://www.theverge.com/tech/988953/philips-hue-smart-lighting-custom-ai-behaviors-sonos-integration",
    "domain": "大厂 AI 动态",
    "title": "Now you can tell the Hue app how you want your smart lights to work",
    "url": "https://www.theverge.com/tech/988953/philips-hue-smart-lighting-custom-ai-behaviors-sonos-integration",
    "source": "Jennifer Pattison Tuohy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T07:30:00+00:00",
    "summary": "Philips Hue's AI assistant can now build automations based on natural language, letting you describe what you want your lights to do. The feature, called Custom AI Behaviors, goes beyond simply changi"
  },
  {
    "id": "rss:https://www.theverge.com/tech/989014/philips-hue-liane-360-rope-lights-smart-lighting-interior-design",
    "domain": "大厂 AI 动态",
    "title": "I want to wrap myself in Hue’s new Liane rope lights",
    "url": "https://www.theverge.com/tech/989014/philips-hue-liane-360-rope-lights-smart-lighting-interior-design",
    "source": "Jennifer Pattison Tuohy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T07:30:00+00:00",
    "summary": "I love smart lighting, but I don't love many of the form factors it comes in. With a few exceptions, most smart, color-changing lamps and fixtures fit better in my teenage son's dorm room than my livi"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/02/the-builders-stage-brings-practical-strategies-for-scaling-startups-to-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "The Builders Stage brings practical strategies for scaling startups to TechCrunch Disrupt 2026",
    "url": "https://techcrunch.com/2026/09/02/the-builders-stage-brings-practical-strategies-for-scaling-startups-to-techcrunch-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T23:01:00+00:00",
    "summary": "The Builders Stage is returning to TechCrunch Disrupt, bringing together founders, startup operators, and investors for practical conversations on what it takes to build and scale."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/02/palo-alto-networks-paid-500m-for-thrive-backed-console-sources-say/",
    "domain": "大厂 AI 动态",
    "title": "Palo Alto Networks paid $500M for Thrive-backed Console, sources say",
    "url": "https://techcrunch.com/2026/09/02/palo-alto-networks-paid-500m-for-thrive-backed-console-sources-say/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T22:44:56+00:00",
    "summary": "The acquisition also leaves Sequoia-backed Serval as the de facto startup leader in AI IT service automation, industry watchers believe."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/02/techcrunch-disrupt-2026s-new-real-world-ai-stage-features-nvidia-robots-and-extinct-animals/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Disrupt 2026’s new Real World AI Stage features Nvidia, robots, and extinct animals",
    "url": "https://techcrunch.com/2026/09/02/techcrunch-disrupt-2026s-new-real-world-ai-stage-features-nvidia-robots-and-extinct-animals/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T22:24:09+00:00",
    "summary": "On our new Real World AI stage, we’ll be focusing on the intersection between the digital and physical, and all the ways we’ll continue to see a blending of the two."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/02/google-spared-from-ad-business-breakup-but-judge-orders-changes-to-how-it-operates/",
    "domain": "大厂 AI 动态",
    "title": "Google spared from ad-business breakup, but judge orders changes to how it operates",
    "url": "https://techcrunch.com/2026/09/02/google-spared-from-ad-business-breakup-but-judge-orders-changes-to-how-it-operates/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T21:38:34+00:00",
    "summary": "Google has dodged an effort to break up its ad business, but a judge said Wednesday that the company will need to adjust its business to benefit competitors."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/02/openais-new-reasoning-technique-alarms-ai-safety-experts/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI’s new reasoning technique alarms AI safety experts",
    "url": "https://techcrunch.com/2026/09/02/openais-new-reasoning-technique-alarms-ai-safety-experts/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T20:19:14+00:00",
    "summary": "OpenAI’s new Astra model will use “recurrent depth,” a technique that allows the model to operate outside of the sequential thinking that characterizes most reasoning models."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/02/mapquest-is-now-the-no-1-u-s-app-after-bucking-trumps-lake-america-renaming/",
    "domain": "大厂 AI 动态",
    "title": "MapQuest is now the No. 1 US app after bucking Trump’s ‘Lake America’ renaming",
    "url": "https://techcrunch.com/2026/09/02/mapquest-is-now-the-no-1-u-s-app-after-bucking-trumps-lake-america-renaming/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T20:12:41+00:00",
    "summary": "The once-dominant mapping app has surged to the top of Apple’s U.S. App Store after refusing to adopt Trump’s “Lake America” name, drawing more than half of its 2026 U.S. downloads in just six days."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/02/it-sure-looks-like-hackers-breached-a-major-id-card-verification-service/",
    "domain": "大厂 AI 动态",
    "title": "It sure looks like hackers breached a major ID card verification service",
    "url": "https://techcrunch.com/2026/09/02/it-sure-looks-like-hackers-breached-a-major-id-card-verification-service/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T19:35:09+00:00",
    "summary": "An identity theft search site claimed to have more than 150 million driver's license photos stolen from an ID verification service. The crime site has now shut down."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/02/delivery-hero-board-backs-ubers-15b-takeover-bid/",
    "domain": "大厂 AI 动态",
    "title": "Delivery Hero board backs Uber’s $15B takeover bid",
    "url": "https://techcrunch.com/2026/09/02/delivery-hero-board-backs-ubers-15b-takeover-bid/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T19:25:35+00:00",
    "summary": "If approved, the combined company would become one of the largest food delivery platforms in the world."
  },
  {
    "id": "rss:https://techcrunch.com/video/pangrams-max-spero-on-why-ai-detection-is-harder-than-real-or-fake/",
    "domain": "大厂 AI 动态",
    "title": "Pangram’s Max Spero on why AI detection is harder than ‘Real or Fake’",
    "url": "https://techcrunch.com/video/pangrams-max-spero-on-why-ai-detection-is-harder-than-real-or-fake/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T17:18:13+00:00",
    "summary": "The internet has a trust problem, and&#160;it’s&#160;not just because social media feeds are filling up with AI&#160;slop. AI-generated text and images are now making their way into job applications, "
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/02/x-shifts-us-creator-payouts-from-stripe-to-x-money/",
    "domain": "大厂 AI 动态",
    "title": "X shifts US creator payouts from Stripe to X Money",
    "url": "https://techcrunch.com/2026/09/02/x-shifts-us-creator-payouts-from-stripe-to-x-money/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T17:12:27+00:00",
    "summary": "X says U.S. creator payouts will now be handled through its X Money payments service, a change that appears to replace the previous Stripe-powered payout system."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/02/u-s-government-sides-with-openai-on-issue-of-training-llms-on-copyrighted-material/",
    "domain": "大厂 AI 动态",
    "title": "US government sides with OpenAI on issue of training LLMs on copyrighted material",
    "url": "https://techcrunch.com/2026/09/02/u-s-government-sides-with-openai-on-issue-of-training-llms-on-copyrighted-material/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T17:09:06+00:00",
    "summary": "\"The United States has a strong interest in continuing to develop a robust and competitive artificial intelligence industry that sets the standard for the practice and procedure of AI use globally,\" t"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/02/enhanced-geothermal-notches-another-win-as-google-buys-400-mw-from-fervo/",
    "domain": "大厂 AI 动态",
    "title": "Enhanced geothermal notches another win as Google buys 400 MW from Fervo",
    "url": "https://techcrunch.com/2026/09/02/enhanced-geothermal-notches-another-win-as-google-buys-400-mw-from-fervo/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T16:54:23+00:00",
    "summary": "Fervo's deal with Google could expand to 1 gigawatt of geothermal power, enough to supply a very large AI data center in Utah."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/02/wonderful-more-than-doubles-its-valuation-to-5b-in-under-6-months/",
    "domain": "大厂 AI 动态",
    "title": "Wonderful more than doubles its valuation to $5B in under 6 months",
    "url": "https://techcrunch.com/2026/09/02/wonderful-more-than-doubles-its-valuation-to-5b-in-under-6-months/",
    "source": "Ram Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T16:04:10+00:00",
    "summary": "Wonderful said it will use its $550 million Series C funding to develop products faster, expand its FDE teams, and meet demand for its products."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/02/indias-richest-man-now-wants-to-turn-aging-computers-into-ai-ready-pcs/",
    "domain": "大厂 AI 动态",
    "title": "India’s richest man now wants to turn aging computers into AI-ready PCs",
    "url": "https://techcrunch.com/2026/09/02/indias-richest-man-now-wants-to-turn-aging-computers-into-ai-ready-pcs/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T16:01:48+00:00",
    "summary": "Jio is betting it can turn an aging computer into an AI-ready PC for as little as about $11 for two months."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/02/hiddenlayer-nabs-100m-as-enterprises-rush-to-secure-their-ai-deployments/",
    "domain": "大厂 AI 动态",
    "title": "HiddenLayer nabs $100M as enterprises rush to secure their AI deployments",
    "url": "https://techcrunch.com/2026/09/02/hiddenlayer-nabs-100m-as-enterprises-rush-to-secure-their-ai-deployments/",
    "source": "Ram Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T15:01:23+00:00",
    "summary": "Security companies are scrambling to build products that can monitor not just agents but also the tools and add-ons they use."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/02/psa-amazons-shopping-ai-can-now-tell-you-if-that-message-is-a-scam/",
    "domain": "大厂 AI 动态",
    "title": "PSA: Amazon’s shopping AI can now tell you if that message is a scam",
    "url": "https://techcrunch.com/2026/09/02/psa-amazons-shopping-ai-can-now-tell-you-if-that-message-is-a-scam/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T14:56:34+00:00",
    "summary": "Amazon is adding a scam-detection feature to Alexa for Shopping that can verify whether suspicious emails, texts, and other messages actually came from the retailer."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/02/adobe-acquires-indian-market-intelligence-startup-rilo/",
    "domain": "大厂 AI 动态",
    "title": "Adobe acquires Indian market intelligence startup Rilo",
    "url": "https://techcrunch.com/2026/09/02/adobe-acquires-indian-market-intelligence-startup-rilo/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T14:03:57+00:00",
    "summary": "This is Adobe's second acquisition out of India after Rephrase.ai in 2023"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/02/norway-considers-ban-on-camera-enabled-wearable-pervert-glasses/",
    "domain": "大厂 AI 动态",
    "title": "Norway considers ban on camera-enabled wearable ‘pervert glasses’",
    "url": "https://techcrunch.com/2026/09/02/norway-considers-ban-on-camera-enabled-wearable-pervert-glasses/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T13:11:47+00:00",
    "summary": "The Nordic country says wearable camera headsets need to be regulated given their privacy risks."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/02/adobe-is-making-its-tools-available-in-slack/",
    "domain": "大厂 AI 动态",
    "title": "Adobe is making its tools available in Slack",
    "url": "https://techcrunch.com/2026/09/02/adobe-is-making-its-tools-available-in-slack/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T13:09:27+00:00",
    "summary": "Users will be able to access Express, Premiere, and Acrobat in Slack"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/02/uber-is-laying-off-10-of-staff-or-3300-people/",
    "domain": "大厂 AI 动态",
    "title": "Uber is laying off 10% of staff, or 3,300 people",
    "url": "https://techcrunch.com/2026/09/02/uber-is-laying-off-10-of-staff-or-3300-people/",
    "source": "Ram Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T12:14:35+00:00",
    "summary": "Uber is laying off about 3,300 people, or about 10% of its global headcount, in a bid to reduce management layers and invest more in its ridesharing, delivery, and robotaxi divisions."
  },
  {
    "id": "rss:https://stratechery.com/2026/fable-5-1-enterprise-frontier-safeguards/",
    "domain": "大厂 AI 动态",
    "title": "Fable 5.1, Enterprise Frontier Safeguards",
    "url": "https://stratechery.com/2026/fable-5-1-enterprise-frontier-safeguards/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T10:00:00+00:00",
    "summary": "Fable 5.1 is out, and the hated Fable data retention policy is not just being altered, but entirely removed in the meantime. Plus, why increased caching is a win-win."
  },
  {
    "id": "rss:https://stratechery.com/2026/nvidia-earnings-dollars-per-gigawatt-open-and-hugging-face/",
    "domain": "大厂 AI 动态",
    "title": "Nvidia Earnings, Dollars Per Gigawatt, Open and Hugging Face",
    "url": "https://stratechery.com/2026/nvidia-earnings-dollars-per-gigawatt-open-and-hugging-face/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T10:00:00+00:00",
    "summary": "Nvidia's earnings were remarking and boring — two sides of the same coin. Everything the company does is about avoiding a consolidated world."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/09/budget-deal-puts-political-control-of-grants-on-hold-until-december/",
    "domain": "大厂 AI 动态",
    "title": "Spending deal comes with a bonus: Blocking political control of grants",
    "url": "https://arstechnica.com/science/2026/09/budget-deal-puts-political-control-of-grants-on-hold-until-december/",
    "source": "John Timmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T21:20:03+00:00",
    "summary": "Congress pauses the OMB's attempt to rewrite how research is funded."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/09/my-drivers-license-is-one-of-153-million-for-sale-on-a-new-dark-website/",
    "domain": "大厂 AI 动态",
    "title": "I rented a car, and within hours, my driver's license was for sale",
    "url": "https://arstechnica.com/security/2026/09/my-drivers-license-is-one-of-153-million-for-sale-on-a-new-dark-website/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T20:32:02+00:00",
    "summary": "The FBI is reportedly investigating a massive data breach that is unfolding in real time."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/09/fcc-plans-robocall-scorecard-to-grade-phone-companies-on-spam-call-blocking/",
    "domain": "大厂 AI 动态",
    "title": "FCC plans robocall scorecard to grade phone companies on spam call blocking",
    "url": "https://arstechnica.com/tech-policy/2026/09/fcc-plans-robocall-scorecard-to-grade-phone-companies-on-spam-call-blocking/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T19:54:27+00:00",
    "summary": "Carrier scorecards may include call-blocking stats and data on customer complaints."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/09/wary-of-artemis-iv-timeline-nasa-is-changing-lunar-spacesuit-design/",
    "domain": "大厂 AI 动态",
    "title": "Wary of Artemis IV timeline, NASA is changing lunar spacesuit design",
    "url": "https://arstechnica.com/space/2026/09/wary-of-artemis-iv-timeline-nasa-is-changing-lunar-spacesuit-design/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T19:37:08+00:00",
    "summary": "\"Requirements are being adjusted to reflect near-term mission needs.\""
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/09/google-releases-gemini-3-8-flash-its-third-flash-model-in-six-weeks/",
    "domain": "大厂 AI 动态",
    "title": "Google releases Gemini 3.8 Flash, its third Flash model in six weeks",
    "url": "https://arstechnica.com/ai/2026/09/google-releases-gemini-3-8-flash-its-third-flash-model-in-six-weeks/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T18:13:54+00:00",
    "summary": "Google's Pro model updates are seemingly paused, but there's yet another Gemini Flash today."
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
    "id": "hn:49511824",
    "domain": "股票",
    "title": "Apple Is Suddenly an AI Infra Stock as OpenAI Buys 10k+ Macs",
    "url": "https://247wallst.com/investing/2026/08/31/apple-is-suddenly-an-ai-infrastructure-stock-as-openai-buys-macs-by-the-tens-of-thousands/",
    "source": "prabal97",
    "platform": "hackernews",
    "points": 40,
    "published_at": "2026-08-31T16:44:15+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3780998",
    "domain": "股票",
    "title": "美国零售柴油价格飙至四年高位，全球供应受扰加剧通胀担忧",
    "url": "https://wallstreetcn.com/articles/3780998",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T07:44:09+00:00",
    "summary": "美国柴油零售均价达每加仑5.783美元，逼近2022年6月创下的每加仑5.816美元历史峰值。中东冲突与俄罗斯炼厂遭袭致全球供应收紧，推高运输与生产成本，加剧通胀压力。特朗普政府已要求炼油商增产，但产能接近极限。能源价格持续走高令美联储政策复杂化，主席沃什警示通胀风险，市场对后续加息预期重新升温。"
  },
  {
    "id": "wscn:3780996",
    "domain": "股票",
    "title": "惠普跟上戴尔的节奏：AI业务扩张提速，上调今明两年营收增长预期",
    "url": "https://wallstreetcn.com/articles/3780996",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T07:24:01+00:00",
    "summary": "惠普季度营收达122亿美元，同比增长34%，超出市场预期。受AI服务器与网络业务强劲需求驱动，公司大幅上调2026及2027财年营收指引。不同于竞头低利竞争超大规模客户，惠普聚焦高利润的企业与主权AI市场，网络与服务器产品表现亮眼，推动盈利与现金流显著改善。"
  },
  {
    "id": "wscn:3780985",
    "domain": "股票",
    "title": "全球债券收益率回落，韩股收涨0.26%，日元急升，布油日内跌超1%",
    "url": "https://wallstreetcn.com/articles/3780985",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T07:23:52+00:00",
    "summary": "欧股开盘涨跌不一，德国DAX指数涨0.04%，MSCI亚太股票指数上涨1.1%，受益于博通对未来两年人工智能芯片销售前景的乐观预期，SK海力士等芯片相关股票领涨。布伦特原油日内跌幅达1.0%，报94.67美元/桶。日元连续第二个交易日走强，一度升至每美元157.63，触及三周高点。"
  },
  {
    "id": "wscn:3780993",
    "domain": "股票",
    "title": "博通史上最强指引的底气：AI巨头集体“抢芯”，谷歌不再是唯一答案",
    "url": "https://wallstreetcn.com/articles/3780993",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T07:14:25+00:00",
    "summary": "博通祭出史上最强前瞻指引：首次明确FY28 AI收入目标高达2300亿美元，对应20GW数据中心部署规模，并承诺每股收益超30美元，远超华尔街预期。Anthropic与OpenAI正取代谷歌成为最大买家，客户格局重塑令市场对博通估值上限展开重新想象，华尔街选择忽略近忧、聚焦远景，集体维持买入评级。"
  },
  {
    "id": "wscn:3780994",
    "domain": "股票",
    "title": "美国“租房一族”加速崛起：不买房，把钱投入股市",
    "url": "https://wallstreetcn.com/articles/3780994",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T06:57:09+00:00",
    "summary": "高房价与高利率倒逼美国高收入年轻人重新算账：租房月均成本比购房低35%，按8%年回报率投资30年，收益与买房相当但流动性更强。哈佛数据显示，高收入租房家庭十年增加120万户。调查显示，近半数千禧一代和Z世代已将租房视为长期战略选择。"
  },
  {
    "id": "wscn:3780986",
    "domain": "股票",
    "title": "AI“资本局”：当大厂“经营现金流”不够烧了",
    "url": "https://wallstreetcn.com/articles/3780986",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T06:47:47+00:00",
    "summary": "大摩认为，科技巨头AI军备竞赛引发融资危机：亚马逊、谷歌自由现金流转负，Meta即将步入负值。大厂被迫削减回购、增发股票、大规模发债，表内债务飙至7700亿美元；更隐蔽的是3.1万亿美元表外承诺暗藏风险。会计迷雾掩盖了真实重负，若AI回报无法覆盖飙升的资金成本，这场算力狂欢将面临崩盘危机。"
  },
  {
    "id": "wscn:3780989",
    "domain": "股票",
    "title": "加息概率一周从37%升至67%，纽约联储主席：长债收益率上行反映经济稳健",
    "url": "https://wallstreetcn.com/articles/3780989",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T06:32:37+00:00",
    "summary": "油价站稳90美元高位叠加美伊地缘紧张，通胀担忧持续升温，强化了美联储需要继续收紧货币政策的预期。威廉姆斯称，长债收益率上行源于经济稳健，并强调需更多数据才能决策，令市场加息预期略有降温。周五非农就业及9月11日的CPI数据将成关键变量，周四的美联储联储理事沃勒讲话亦备受关注。"
  },
  {
    "id": "wscn:3780991",
    "domain": "股票",
    "title": "韩国电力向三星、SK海力士要求预付25万亿韩元电费",
    "url": "https://wallstreetcn.com/articles/3780991",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T06:26:18+00:00",
    "summary": "韩国电力公社寻求将未来电费收入提前变现，以解决电网扩张资金缺口。方案要求三星电子和SK海力士预付合计25万亿韩元（约181亿美元）的电费，覆盖未来五年用电需求。三星电子被要求预付20万亿韩元，SK海力士为5万亿韩元。"
  },
  {
    "id": "wscn:3780992",
    "domain": "股票",
    "title": "存量房贷确认可延至40年，上海部分银行已可申请，但要满足这个年龄条件",
    "url": "https://wallstreetcn.com/articles/3780992",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T06:23:01+00:00",
    "summary": "上海多家银行明确，1991年前生人不能新办理40年期房贷，要求\"贷款人年龄+贷款期限\"不超过75年（部分支行放宽至80年），年龄以贷款发放时计算。存量房贷延期期限不能超过原贷款期限的一半，且与原期限合计不超过40年。"
  },
  {
    "id": "wscn:3780988",
    "domain": "股票",
    "title": "中东局势升级，亚洲LNG现货升至2022年12月以来新高",
    "url": "https://wallstreetcn.com/articles/3780988",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T06:12:24+00:00",
    "summary": "中东局势骤然升温，霍尔木兹海峡断供风险引爆亚洲LNG市场：现货价格升至逾三年高位，较战前翻倍。高价已迫使巴基斯坦取消紧急采购，电力短缺加剧，亚洲能源账单与经济稳定面临双重考验。"
  },
  {
    "id": "wscn:3780990",
    "domain": "股票",
    "title": "韩国紧急回应美国半导体关税计划：竭尽全力确保不损害韩企利益",
    "url": "https://wallstreetcn.com/articles/3780990",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T06:05:50+00:00",
    "summary": "韩国总统府9月3日就美国商务部正在研拟的半导体关税方案作出回应，强调相关具体方案尚未最终确定，首尔将竭尽全力确保相关措施不损害韩国企业利益。此前一天，美国商务部长卢特尼克披露，特朗普政府正在制定一项新的半导体关税政策：在美国本土生产的芯片享受关税豁免，否则须为进入美国市场付出代价。"
  },
  {
    "id": "wscn:3780987",
    "domain": "股票",
    "title": "汇丰财富洞察：「渐进修复，结构分化」存量政策落地与楼市制度重构并行|中国观点",
    "url": "https://wallstreetcn.com/articles/3780987",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T05:41:13+00:00",
    "summary": "宏观经济：存量政策优先，房地产迎制度性变革7月经济数据全面不及预期，社零同比仅增0.6%（前值1...."
  },
  {
    "id": "wscn:3780971",
    "domain": "股票",
    "title": "A股三大股指午后转跌，培育钻石、航运集体走强，半导体继续调整，恒科指跌1%，有色金属活跃",
    "url": "https://wallstreetcn.com/articles/3780971",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T05:26:46+00:00",
    "summary": "盘面上，个股跌多涨少，沪深京三市超3000股飘绿，上午半天成交1.11万亿。沪深两市半日成交额1.1万亿，较上个交易日缩量1104亿。板块方面，航运、保险、券商、交通运输、家电板块走强，培育钻石、液冷服务器、光模块板块等发力拉升，农业股持续调整。"
  },
  {
    "id": "wscn:3780984",
    "domain": "股票",
    "title": "WorkBuddy的生态开局：焦虑错过新入口，也怕交出老地盘",
    "url": "https://wallstreetcn.com/articles/3780984",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T04:55:36+00:00",
    "summary": "打不过就加入"
  },
  {
    "id": "wscn:3780911",
    "domain": "股票",
    "title": "突破4.8%！10年美债无顶狂奔：全球债市风暴还将持续多久？",
    "url": "https://wallstreetcn.com/premium/articles/3780911?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T04:35:38+00:00",
    "summary": "全球债市同步抛售，油价、财政赤字、AI融资与鹰派预期共振，长端美债或继续上探5%关口。"
  },
  {
    "id": "wscn:3780972",
    "domain": "股票",
    "title": "美国AI算力的下一个瓶颈：不是芯片和电力，而是“许可”",
    "url": "https://wallstreetcn.com/articles/3780972",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T04:24:07+00:00",
    "summary": "算力竞赛的下一个卡点，不是芯片，不是电力，而是政治。巴克莱最新报告揭示，71%美国人反对在家门口建数据中心，电费涨幅高达24%，从纽约全州暂停令到弗吉尼亚电网费用转移，各州监管战火全面点燃。许可瓶颈正重塑AI基础设施版图，算力稀缺或将加剧。"
  },
  {
    "id": "wscn:3780980",
    "domain": "股票",
    "title": "英伟达补齐推理侧闭环：联手Equinix与Together AI，向企业开放模型推理",
    "url": "https://wallstreetcn.com/articles/3780980",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T04:10:46+00:00",
    "summary": "英伟达联手全球最大数据中心托管商Equinix及AI推理平台Together AI，三方分工合作——Equinix提供托管、Together AI提供推理平台、英伟达提供GPU及软件栈，共同为企业客户提供开放模型推理服务。此举标志着英伟达将算力生态从训练侧延伸至推理侧，补全完整闭环。"
  },
  {
    "id": "wscn:3780973",
    "domain": "股票",
    "title": "告别大模型“幻觉”与“遗忘”，多Agent矩阵与Skill体系搭建AI投研系统",
    "url": "https://wallstreetcn.com/articles/3780973",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T04:03:51+00:00",
    "summary": "广发证券认为构建AI投研系统的关键是最大化还原真实投研链路，聚焦信息摄入与经验加工两大环节。报告指出，Agent基座选择本质是Harness工程权衡，建议开源架构与一体化产品协同配合。针对上下文衰减痛点，提出多代理矩阵与分步加载方案。Skill体系采用渐进式披露设计，兼顾分析弹性与工程精度。私域RAG知识库被认定为信息摄入层最优解。"
  },
  {
    "id": "wscn:3780878",
    "domain": "股票",
    "title": "日债破3%：一口补贴了全世界三十年的“廉价资本之井”正在干涸",
    "url": "https://wallstreetcn.com/premium/articles/3780878?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T03:59:42+00:00",
    "summary": "日元贬值是在装火药，升值才是扣扳机。"
  },
  {
    "id": "wscn:3780983",
    "domain": "股票",
    "title": "从保费到长期回报：阳光保险「期中考」交卷",
    "url": "https://wallstreetcn.com/articles/3780983",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T03:58:58+00:00",
    "summary": "低利率、客户需求升级与技术变革，正在共同推动保险业进入新的经营周期。\n人口老龄化持续释放养老与健康保..."
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
    "id": "hn:49531107",
    "domain": "金融",
    "title": "A Hedge-Fund Titan's Divorce Is Putting Wall Street's Staggering Wealth on Publi",
    "url": "https://www.wsj.com/personal-finance/a-hedge-fund-titans-divorce-is-putting-wall-streets-staggering-wealth-on-public-view-6c419f4c",
    "source": "kamaraju",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-09-02T02:41:04+00:00",
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
    "id": "rss:https://arxiv.org/abs/2609.02013",
    "domain": "金融",
    "title": "What Would it Cost to End Extreme Poverty?",
    "url": "https://arxiv.org/abs/2609.02013",
    "source": "Roshni Sahoo, Joshua Blumenstock, Paul Niehaus, Leo Selker, Stefan Wager",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T04:00:00+00:00",
    "summary": "arXiv:2609.02013v1 Announce Type: new Abstract: We study poverty minimization via direct transfers, framing this as a statistical learning problem while retaining the information constraints faced by "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.02014",
    "domain": "金融",
    "title": "Insights on Time-consistent Deep Hedging under Elicitable Dynamic Risk Measures",
    "url": "https://arxiv.org/abs/2609.02014",
    "source": "Shuyi Zhang, Fr\\'ed\\'eric Godin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T04:00:00+00:00",
    "summary": "arXiv:2609.02014v1 Announce Type: new Abstract: We study deep hedging in the context of dynamics risk measures, where sequential decisions are time-consistent. Whereas the literature in such context m"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.02447",
    "domain": "金融",
    "title": "Price manipulation in nonlinear transient impact models: rigidity before memory and complete positivity after memory",
    "url": "https://arxiv.org/abs/2609.02447",
    "source": "Minhyeok Lee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T04:00:00+00:00",
    "summary": "arXiv:2609.02447v1 Announce Type: new Abstract: Transient impact models compose a nonlinearity with a memory kernel, and the order of composition determines the criterion for absence of price manipula"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.02525",
    "domain": "金融",
    "title": "Switching Frictions, Heterogeneous Trading Horizons, and Long-Memory Order Flow",
    "url": "https://arxiv.org/abs/2609.02525",
    "source": "Alejandro Rodriguez Dominguez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T04:00:00+00:00",
    "summary": "arXiv:2609.02525v1 Announce Type: new Abstract: This paper develops a mechanism through which costly changes in the representations used for portfolio choice can contribute to persistent signed order "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.02535",
    "domain": "金融",
    "title": "Uniform Inference and Certified Capacity at a Reflexive Stability Boundary",
    "url": "https://arxiv.org/abs/2609.02535",
    "source": "Alejandro Rodriguez Dominguez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T04:00:00+00:00",
    "summary": "arXiv:2609.02535v1 Announce Type: new Abstract: This paper develops uniform inference and certified capacity decisions for an estimated financial stability boundary. Conditional risk, temporary cross-"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.02660",
    "domain": "金融",
    "title": "Modeling Trade Durations under Temporal Granularity Effects in Forex Markets",
    "url": "https://arxiv.org/abs/2609.02660",
    "source": "Vladim\\'ir Hol\\'y",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T04:00:00+00:00",
    "summary": "arXiv:2609.02660v1 Announce Type: new Abstract: Trade durations in high-frequency foreign exchange data exhibit increased occurrence near integer values. To address this empirical phenomenon, we propo"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.02677",
    "domain": "金融",
    "title": "Eliciting ESG Preferences for Reinforcement Learning-Based Portfolio Optimization",
    "url": "https://arxiv.org/abs/2609.02677",
    "source": "Giovanni Dispoto, Marcello Restelli, Carmine Ventre",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T04:00:00+00:00",
    "summary": "arXiv:2609.02677v1 Announce Type: new Abstract: Modern portfolio management increasingly demands a balance between traditional risk-adjusted returns and strict Environmental, Social, and Governance (E"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.02797",
    "domain": "金融",
    "title": "Dutch Books for Language Models",
    "url": "https://arxiv.org/abs/2609.02797",
    "source": "Isaiah Andrews, Suproteem Sarkar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T04:00:00+00:00",
    "summary": "arXiv:2609.02797v1 Announce Type: new Abstract: People increasingly use language models to support life decisions. Many such decisions involve a probabilistic forecast: How likely is a major life even"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.02381",
    "domain": "金融",
    "title": "Viscosity Supersolution Barriers to a Non-local Free Boundary Problem",
    "url": "https://arxiv.org/abs/2609.02381",
    "source": "Avetik Arakelyan, Lusine Poghosyan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T04:00:00+00:00",
    "summary": "arXiv:2609.02381v1 Announce Type: cross Abstract: We study a parabolic obstacle partial integro-differential equation (PIDE) with a dynamically moving bilateral free boundary. This type of problem ari"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.02580",
    "domain": "金融",
    "title": "Competitive Market Behavior of LLMs",
    "url": "https://arxiv.org/abs/2609.02580",
    "source": "Pawel Struski, Jakub Swistak, Inez Okulska, Przemyslaw Biecek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T04:00:00+00:00",
    "summary": "arXiv:2609.02580v1 Announce Type: cross Abstract: Large language models (LLMs) are increasingly deployed as economic agents, yet there is little evidence whether LLM agents are suited for participatin"
  },
  {
    "id": "rss:https://arxiv.org/abs/2601.14454",
    "domain": "金融",
    "title": "How Wasteful is Signaling?",
    "url": "https://arxiv.org/abs/2601.14454",
    "source": "Alex Frankel, Navin Kartik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T04:00:00+00:00",
    "summary": "arXiv:2601.14454v3 Announce Type: replace Abstract: Signaling is wasteful. But how wasteful? We study the fraction of surplus dissipated in a separating equilibrium. For isoelastic environments, this "
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.15444",
    "domain": "金融",
    "title": "Watching Trade from Space: Measuring Maritime Trade Using Satellite Imagery",
    "url": "https://arxiv.org/abs/2604.15444",
    "source": "Yonggeun Jung",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T04:00:00+00:00",
    "summary": "arXiv:2604.15444v2 Announce Type: replace Abstract: This paper combines synthetic aperture radar imagery, nighttime lights, and port characteristics to measure port-level maritime trade using only pub"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.26031",
    "domain": "金融",
    "title": "Geometrically convex return risk measures on AM-algebras",
    "url": "https://arxiv.org/abs/2606.26031",
    "source": "Christian Laudag\\'e",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T04:00:00+00:00",
    "summary": "arXiv:2606.26031v2 Announce Type: replace Abstract: Monetary risk measures quantify the risk of uncertain monetary payoffs (or losses), whereas in time series analysis risk is typically assessed using"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.00858",
    "domain": "金融",
    "title": "Data-Driven Measures of High-Frequency Trading",
    "url": "https://arxiv.org/abs/2608.00858",
    "source": "Gbenga Ibikunle, Ben Moews, Dmitriy Muravyev, Khaladdin Rzayev",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T04:00:00+00:00",
    "summary": "arXiv:2608.00858v2 Announce Type: replace Abstract: Public data do not identify high-frequency trading (HFT), and standard proxies do not separate liquidity-supplying from liquidity-demanding strategi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.30490",
    "domain": "金融",
    "title": "Two Kinds of Nothing: What Insignificant Results in Finance Actually Show",
    "url": "https://arxiv.org/abs/2608.30490",
    "source": "David Tan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T04:00:00+00:00",
    "summary": "arXiv:2608.30490v2 Announce Type: replace Abstract: Claims of the form \"we find no evidence that X affects Y\" appear throughout the applied finance literature, yet whether such a claim contains eviden"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.30999",
    "domain": "金融",
    "title": "Metaorder modelling and identification from public data",
    "url": "https://arxiv.org/abs/2608.30999",
    "source": "Ezra Goliath, Tim Gebbie",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T04:00:00+00:00",
    "summary": "arXiv:2608.30999v2 Announce Type: replace Abstract: Market-order flow in financial markets exhibits long-range correlations. This is a widely known stylised fact of financial markets. A popular hypoth"
  },
  {
    "id": "rss:https://arxiv.org/abs/2504.02518",
    "domain": "金融",
    "title": "Online Multivariate Regularized Distributional Regression for High-dimensional Probabilistic Electricity Price Forecasting",
    "url": "https://arxiv.org/abs/2504.02518",
    "source": "Simon Hirsch",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T04:00:00+00:00",
    "summary": "arXiv:2504.02518v4 Announce Type: replace-cross Abstract: Probabilistic electricity price forecasting (PEPF) is vital for short-term electricity markets, yet the multivariate nature of day-ahead price"
  },
  {
    "id": "rss:https://arxiv.org/abs/2511.03474",
    "domain": "金融",
    "title": "On a Stationarity Theory for Stochastic Volterra Integral Equations with Affine Drift",
    "url": "https://arxiv.org/abs/2511.03474",
    "source": "Emmanuel Gnabeyeu, Gilles Pag\\`es",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T04:00:00+00:00",
    "summary": "arXiv:2511.03474v2 Announce Type: replace-cross Abstract: This paper investigate the properties of solutions to forward Stochastic Volterra Integral Equations (SVIEs for short) with affine drift, spec"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.23416",
    "domain": "金融",
    "title": "The Axiomatic Trader: Latent Regularity, Information Budgets, and the Canonical Form of a Quantitative Investment System",
    "url": "https://arxiv.org/abs/2608.23416",
    "source": "Jiayu Li",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T04:00:00+00:00",
    "summary": "arXiv:2608.23416v2 Announce Type: replace-cross Abstract: Systematic trading rests on one article of faith: that regularities found in the past persist. This paper does three things. First, it states "
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
    "points": 54,
    "published_at": "2026-08-25T11:27:51+00:00",
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
    "id": "hn:49414279",
    "domain": "金融",
    "title": "Tesla discontinues its Solar Roof tiles, not economically viable",
    "url": "https://electrek.co/2026/08/20/tesla-discontinues-solar-roof-panels-only/",
    "source": "MilnerRoute",
    "platform": "hackernews",
    "points": 25,
    "published_at": "2026-08-24T01:21:56+00:00",
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
    "id": "hn:49404624",
    "domain": "金融",
    "title": "Jane Street took $15B hit in July tied to Situational Awareness",
    "url": "https://www.reuters.com/business/finance/jane-street-took-15-billion-hit-july-tied-situational-awareness-sources-say-2026-08-14/",
    "source": "paulpauper",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-08-22T22:50:51+00:00",
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
    "id": "hn:49350858",
    "domain": "金融",
    "title": "AI Is Upending One of Finance's Cushiest Jobs",
    "url": "https://www.bloomberg.com/news/features/2026-06-05/ai-is-upending-traditional-financial-advisor-jobs",
    "source": "theriddlr",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-08-18T18:59:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:49208461",
    "domain": "金融",
    "title": "New Intelligence Warns Russia May Provoke NATO Amid Dwindling U.S. Munitions",
    "url": "https://www.wsj.com/finance/investing/new-intelligence-warns-russia-may-provoke-nato-amid-dwindling-u-s-munitions-68f497c7",
    "source": "doener",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-08-07T10:52:27+00:00",
    "summary": ""
  }
]
```
