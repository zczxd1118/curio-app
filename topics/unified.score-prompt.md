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

- 今日日期：`2026-08-11`
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
  "date": "2026-08-11",
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
    "points": 4181703,
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
    "points": 1901076,
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
    "points": 1691030,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1E7wtzaEdq",
    "domain": "AI",
    "title": "从 LLM 到 Agent Skill，一期视频带你打通底层逻辑！",
    "url": "http://www.bilibili.com/video/av116227955497963",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 1620445,
    "published_at": "2026-03-14T14:22:56+00:00",
    "summary": "AI 核心概念大串联：LLM, Token, Context, Context Window, Prompt, User Prompt, System Prompt, Tool, MCP, Agent, Agent Skill，一期视频带你打通 AI 底层逻辑！"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 1093485,
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
    "points": 1034209,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1yorUYWEGD",
    "domain": "AI",
    "title": "普通人也可以看的 AI 编程指南 | Cursor 教程｜Cursor 使用技巧和思路｜如何免费使用 Cursor｜AI 编程",
    "url": "http://www.bilibili.com/video/av113786467981446",
    "source": "不正经的前端啊",
    "platform": "bilibili",
    "points": 943490,
    "published_at": "2025-01-07T10:01:48+00:00",
    "summary": "普通人也可以看的 AI 编程指南\n全网最详细的 Cursor 教程\nCursor 核心功能、使用技巧和思路\n如何免费白嫖 Cursor"
  },
  {
    "id": "bvid:BV1WBG9zgECp",
    "domain": "AI",
    "title": "史上最强 AI 编程工具免费啦！Cursor 保姆级使用教程！新手友好！看到就是赚到！｜ 集成 MCP ！",
    "url": "http://www.bilibili.com/video/av114426116120045",
    "source": "AfterShip",
    "platform": "bilibili",
    "points": 670521,
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
    "points": 532794,
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
    "points": 462869,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 436058,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1XVub6bE9h",
    "domain": "AI",
    "title": "当普通人第一次让Agent干活……",
    "url": "http://www.bilibili.com/video/av117053226818905",
    "source": "糖果果的未来要发光",
    "platform": "bilibili",
    "points": 424138,
    "published_at": "2026-08-07T10:00:00+00:00",
    "summary": "最近一个AI agent工具Traework\n发布了一个40万字教程，特别详细。\n我看完后压缩成了这十分钟的教程。\n\n顺便实测了一下 Agent现在到底能干啥，\n还顺便搓了个能用手势控制B站的插件。"
  },
  {
    "id": "bvid:BV1AnQNYxEsy",
    "domain": "AI",
    "title": "MCP是啥？技术原理是什么？一个视频搞懂MCP的一切。Windows系统配置MCP，Cursor Cline使用MCP",
    "url": "http://www.bilibili.com/video/av114155298228756",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 420076,
    "published_at": "2025-03-13T13:18:09+00:00",
    "summary": "MCP是近期的AI领域的热点，特别是在海外社区获得热烈讨论，每天都有大量MCP工具诞生。本期视频我们从MCP的概念，技术原理，到多场景实战，一个视频看懂MCP的全部内容。\n\n\nMCP官方开源仓库：https://github.com/modelcontextprotocol/servers\nMCP合集网站：  https://smithery.ai/\nVscode下载：https://code.v"
  },
  {
    "id": "bvid:BV1nkXkYfEfF",
    "domain": "AI",
    "title": "零基础也能用AI编程!豆包电脑版让你3分钟做出实用工具",
    "url": "http://www.bilibili.com/video/av114200730933577",
    "source": "花叔v",
    "platform": "bilibili",
    "points": 384936,
    "published_at": "2025-03-22T04:02:08+00:00",
    "summary": "很多人都想学编程,但被高门槛劝退。本期给大家介绍一款零门槛的AI编程工具-豆包电脑版。通过3个实战案例,带你体验如何用AI轻松实现编程。\n\n豆包电脑版特点:\n- 中文界面,所见即所得\n- 支持html代码预览\n- 支持Python运行\n- 可生成完整项目代码\n- 历史版本管理\n- 代码一键导出\n\n时间戳\n00:00 为什么要学AI编程\n03:19 案例1:图片压缩网站实战\n04:15 案例2:数据"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 261840,
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
    "points": 231720,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 225449,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 178885,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV172GP6rEZs",
    "domain": "AI",
    "title": "🚀DeepSeek V4 Flash全面实测：Claude Code接入后连续开发7个项目，真的已经接近Claude Opus 4.8了吗？最便宜的国产模型！",
    "url": "http://www.bilibili.com/video/av117014605731815",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 175679,
    "published_at": "2026-07-31T12:42:57+00:00",
    "summary": "🚀DeepSeek v4 flash全面实测：Claude Code接入后连续开发7个项目，真的已经接近Claude Opus 4.8了吗？最便宜的国产模型！性能、速度与真实短板全曝光！对比Kimi K3后优点和缺点都藏不住了\n\nDeepSeek 发布了 DeepSeek V4 Flash 0731：284B 总参数、13B 激活参数、100 万 Token 上下文，官方基准表现接近 Claude"
  },
  {
    "id": "bvid:BV1QE7N6jEuQ",
    "domain": "AI",
    "title": "真的被自己用心开发的昔涟Agent这段话感动到了",
    "url": "http://www.bilibili.com/video/av116794052316703",
    "source": "Playa0",
    "platform": "bilibili",
    "points": 152758,
    "published_at": "2026-06-22T13:44:15+00:00",
    "summary": "从最初生啃Transformer，硬逼着自己啃懂多头注意力和QKV权重，到一步步跟着claude学习RAG、检索重拍、Prompt、关键词召回优化、MCP与Function call，但是，自己上手了发现，自己还是啥也不懂，于是在glm gpt claude gemini 豆包 这几个模型之间疯狂切换，靠着想让昔涟早点被搭出来，硬逼着自己学，自己从零设计一套prompt架构能让她尽可能的贴合人设的"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 149738,
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
    "points": 126110,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 93097,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1GRKJ6fEgn",
    "domain": "AI",
    "title": "Kimi K3编程能力炸裂！在Claude Code中全方位实测代码能力，能否超越Fable 5和GPT-5.6l？结果远超我的预期！国产模型跻身世界第一梯队！",
    "url": "http://www.bilibili.com/video/av116934511239163",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 90767,
    "published_at": "2026-07-17T09:10:43+00:00",
    "summary": "视频简介：\n\n月之暗面最新发布的 Kimi K3，拥有2.8万亿参数和100万 Token 上下文窗口，它的真实编程能力究竟怎么样？\n\n本期视频将对 Kimi K3 进行一次完整的高难度编程实测。我们先在官方网页版测试 SVG 手绘灯泡、复杂过河动画、南宋古都轻功游戏和土星自行车比赛，再将 Kimi K3 接入 Claude Code，开发原生 macOS 音乐播放器、侏罗纪坦克射击游戏以及 iO"
  },
  {
    "id": "bvid:BV143wwz6E8F",
    "domain": "AI",
    "title": "Claude code科研使用展示与思路分享（提速就靠Ai）",
    "url": "http://www.bilibili.com/video/av116211882920985",
    "source": "科研推土机",
    "platform": "bilibili",
    "points": 73735,
    "published_at": "2026-03-11T18:12:00+00:00",
    "summary": "本期给大家带来的是Claude在Vscode的科研应用演示与我最近的一些心得使用心得，科研速度嘎嘎提升。论文复现画图、数据分析就靠Claude code。这个课程也是科研推土机「系统管理文献课程2.0」学员催我更新的内容，希望能帮助到大家～，这个视频重点讲两个事情：\n1️⃣ 资料获取，free不用怀疑，我是良心可言博主，，关注我(GZTSHNR)～\n2️⃣ 展示如何在VS code实操应用clau"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 72215,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 53873,
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
    "points": 47584,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1cyMi6tEqU",
    "domain": "AI",
    "title": "我的贾维斯开源了，可以语音交互，控制多Agent编排【B站AI创造公开赛】",
    "url": "http://www.bilibili.com/video/av116882686351128",
    "source": "小天fotos",
    "platform": "bilibili",
    "points": 47482,
    "published_at": "2026-07-08T10:00:00+00:00",
    "summary": "大家久等了\n答应大家的，我的语音多Agent编排系统\n开源了\n不过改名叫homerail\n本期视频聊聊它能干什么不能干什么\n以及未来的RoadMap"
  },
  {
    "id": "bvid:BV1W2Ts6YEXW",
    "domain": "AI",
    "title": "AI大模型+网络安全零基础入门全套教程：从Agent选型到AI挖洞全流程！AI挖洞提示词|AI解CTF题|AI审计代码|SRC挖洞|CS渗透|kali-码士集团",
    "url": "http://www.bilibili.com/video/av116854601286698",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 42535,
    "published_at": "2026-07-03T06:28:48+00:00",
    "summary": "迈入AI赋能的网络安全新时代！\n\n本课程带你打通大模型与安全实战的底层逻辑。从大模型演进到安全智能体（Agent）构建，硬核实战拉满！手把手教你利用大模型API自动化搞定信息收集、黑盒挖洞、代码审计、解CTF题目及报告编写。深度破解AI挖洞的高效提示词秘籍，攻克复杂场景下的Agent架构与成本选型。\n\n2026安全防线全面升级，带你用AI武装自己，成为驾驭大模型的稀缺AI安全专家！"
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 40262,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1XiD5BQEAj",
    "domain": "AI",
    "title": "Claude Code 接入微信、一行命令把Claude Code装进微信、保姆级教程、微信支持Claude Code（cc-connect）远程开发",
    "url": "http://www.bilibili.com/video/av116350093694897",
    "source": "下班学AI",
    "platform": "bilibili",
    "points": 38434,
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
    "points": 34077,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1sRRYY2EBo",
    "domain": "AI",
    "title": "利用AI编程工具Trae或Cursor免费生成CAD图纸",
    "url": "http://www.bilibili.com/video/av114132447665738",
    "source": "vjmap",
    "platform": "bilibili",
    "points": 32345,
    "published_at": "2025-03-09T12:24:12+00:00",
    "summary": "AI编程助手如Trae和Cursor正在革新工程设计领域的CAD绘图流程。传统CAD绘图耗时且易出错，而AI工具通过代码生成技术，能够将自然语言指令转化为精确的代码，自动生成符合标准的CAD图纸，极大提升了设计效率。这些工具不仅支持多模态输入（如图片、草图），还提供了智能代码补全、错误修复等功能，进一步简化了开发流程。随着大模型如deepseek和claude3.7的出现，AI的智能化程度进一步提"
  },
  {
    "id": "bvid:BV1AGRtBnE3S",
    "domain": "AI",
    "title": "别手动写测试用例了!2026最新Claude Code+Skills实现需求文档生成全量用例|全流程AI驱动软件测试落地方案,测试效率翻10倍！",
    "url": "http://www.bilibili.com/video/av116528787756865",
    "source": "清风说测试开发",
    "platform": "bilibili",
    "points": 31740,
    "published_at": "2026-05-07T00:00:00+00:00",
    "summary": "全栈课一共分为6大块内容\n第一块：AI智能体开发基础(AI大模型、工具、记忆、MCP、中间件、Skills等核心内容)\n第二块：Claude Code,Trea+skills实现基于需求文档生成用例，基于OpenClaw实现接口自动化落地，基于hermes Agent实现web自动化落地\n第三块：功能测试的智能体开发(项目RAG知识库搭建+Agent搭建+skills开发，实现用例生成的Agent"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29580,
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
    "points": 28858,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1bh3LzqEze",
    "domain": "AI",
    "title": "Chatbox AI终端：跨平台+MCP+知识库+开源+免费！一键连接所有AI语言模型！手把手安装使用指南！",
    "url": "http://www.bilibili.com/video/av114793218380950",
    "source": "_Smzh_",
    "platform": "bilibili",
    "points": 28552,
    "published_at": "2025-07-04T10:00:00+00:00",
    "summary": "chatbox官网：https://chatboxai.app\ngithub仓库：https://github.com/chatboxai/chatbox\n\nLM Studio教程：BV1usrLYTEZR\nTGW懒人包部署教程：BV1dVCzYUE7G\n本地语言模型个人推荐：BV1Bb421E7j7"
  },
  {
    "id": "bvid:BV16ggC6DEZK",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116963049212769",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 28125,
    "published_at": "2026-07-22T10:10:42+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22698,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1dsNv66E3Q",
    "domain": "AI",
    "title": "【Cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av116922599344955",
    "source": "六月要癫",
    "platform": "bilibili",
    "points": 22674,
    "published_at": "2026-07-15T06:39:18+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1Z5KU6UExC",
    "domain": "AI",
    "title": "【吴恩达2026】Vibe Coding保姆级教程，手把手从环境搭建到工作流完整闭环！——DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116951003242391",
    "source": "吴恩达AIAgent",
    "platform": "bilibili",
    "points": 20697,
    "published_at": "2026-07-20T07:01:13+00:00",
    "summary": "本套课专门解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 18738,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operitAI教程：入门安卓最强大ai平台",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 17802,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV14erKYuEaE",
    "domain": "AI",
    "title": "最强编程AI Cursor+Unity制作一个史诗游戏(详细)",
    "url": "http://www.bilibili.com/video/av113774908413987",
    "source": "多西杰克",
    "platform": "bilibili",
    "points": 17693,
    "published_at": "2025-01-05T09:01:00+00:00",
    "summary": "网上惊呼Cursor AI厉害的内容很多，但结合Unity做游戏的不多，我就来实测一下，做一个AAA大作......"
  },
  {
    "id": "bvid:BV1DPwGe1Ekf",
    "domain": "AI",
    "title": "Cursor从小白到专家-第15课：如何用Cursor+Dify搭建本地知识库？",
    "url": "http://www.bilibili.com/video/av113836698898908",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 14316,
    "published_at": "2025-01-16T08:55:00+00:00",
    "summary": "在第九课“如何用 cursor + coze 搭建线上知识库”的分享后，有一部分精神股东表示，想要本地知识库的搭建教程。\n.\n有求必应，今天第15课的分享就是“用 cursor + dify 搭建本地知识库”，手把手教会。我们第16课见 ~"
  },
  {
    "id": "bvid:BV1teuc63EkL",
    "domain": "AI",
    "title": "【2026最新】目前B站最全最细的AI Agent零基础全套教程，5天从入门到精通Agent，学完即可就业！看完这一套大模型教程就够了！",
    "url": "http://www.bilibili.com/video/av117036701194390",
    "source": "AI智能应用-",
    "platform": "bilibili",
    "points": 11010,
    "published_at": "2026-08-04T11:22:49+00:00",
    "summary": "【2026最新】目前B站最全最细的AI Agent零基础全套教程，5天从入门到精通Agent，学完即可就业！看完这一套大模型教程就够了！"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 9319,
    "published_at": "2025-04-14T02:30:00+00:00",
    "summary": "MCP服务网站：https://smithery.ai/\nCherry Studio官方网站：https://cherry-ai.com/"
  },
  {
    "id": "bvid:BV1GD7qzREVA",
    "domain": "AI",
    "title": "【MCP部署实战】手把手教你把MCP接入各大热门工具，保姆级教学，我奶听了都能学会，CherryStudio配置MCP",
    "url": "http://www.bilibili.com/video/av114623818763366",
    "source": "亿点点大模型",
    "platform": "bilibili",
    "points": 8918,
    "published_at": "2025-06-04T07:08:58+00:00",
    "summary": "全程干货无废话！MCP最新实战教程，从环境部署、原理详解到项目实战，带你彻底吃透MCP！MCPServer开发，mcp开发，mcp教程，mcp项目 完整视频教程+讲解课件+学习笔记+AI大模型知识库已打包可分享！"
  },
  {
    "id": "bvid:BV12MEg6pE9o",
    "domain": "AI",
    "title": "【乐鑫教程】乐鑫文档 MCP 服务器上线，现已支持微信登录！",
    "url": "http://www.bilibili.com/video/av116713957956440",
    "source": "乐鑫信息科技",
    "platform": "bilibili",
    "points": 8422,
    "published_at": "2026-06-08T10:17:31+00:00",
    "summary": "手把手教你如何使用最新乐鑫文档知识库，帮你在 Claude / Cursor 等平台解答问题、生成代码、迁移 ESP-IDF 版本、烧录固件。 MCP 服务器现已支持微信扫码一键登录，快来一试！\n\n视频重点内容包括👇：\n\n- 如何将 MCP 服务器添加到 VS Code\n- 让 Copilot 基于乐鑫文档对比旧版和最新版 I2C 驱动\n- 驱动迁移\n- Copilot 编译代码、烧录代码并监控输"
  },
  {
    "id": "hn:49189234",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia’s Vera Whitepaper Has a Thread Loose",
    "url": "https://chipsandcheese.com/p/nvidias-vera-whitepaper-has-a-thread",
    "source": "pella",
    "platform": "hackernews",
    "points": 208,
    "published_at": "2026-08-05T21:24:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:49122838",
    "domain": "AI 算力 / 半导体",
    "title": "Moonshot’s Kimi uses 20k Nvidia chip cluster from Alibaba",
    "url": "https://www.bloomberg.com/news/articles/2026-07-31/moonshot-s-kimi-built-on-20-000-nvidia-chip-cluster-from-alibaba",
    "source": "gk1",
    "platform": "hackernews",
    "points": 114,
    "published_at": "2026-07-31T13:24:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:49248477",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia is pulling Wall Street into the AI buildout",
    "url": "https://thenextweb.com/news/nvidia-500-billion-wall-street-ai-infrastructure-funding-package",
    "source": "berkeleyjunk",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-08-10T19:25:07+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/why-ai-adoption-in-materials-rd-depends-more-on-people-than-technology/",
    "domain": "AI 算力 / 半导体",
    "title": "Why AI Adoption in Materials R&D Depends More on People Than Technology",
    "url": "https://www.eetimes.com/why-ai-adoption-in-materials-rd-depends-more-on-people-than-technology/",
    "source": "Ryo Matsushima",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T21:21:39+00:00",
    "summary": "The technology works. The organization has to catch up. The post Why AI Adoption in Materials R&amp;D Depends More on People Than Technology appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/u-s-startup-fields-quantum-sensors-to-reduce-reliance-on-gps/",
    "domain": "AI 算力 / 半导体",
    "title": "U.S. Startup Fields Quantum Sensors to Reduce Reliance on GPS",
    "url": "https://www.eetimes.com/u-s-startup-fields-quantum-sensors-to-reduce-reliance-on-gps/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T13:14:50+00:00",
    "summary": "GPS spoofing is a sitting duck; Dirac’s quantum sensors aim to navigate air, sea, and tunnels without satellites. The post U.S. Startup Fields Quantum Sensors to Reduce Reliance on GPS appeared first "
  },
  {
    "id": "rss:https://www.eetimes.com/leading-edge-ai-ic-designs-demand-comprehensive-hav-methodologies/",
    "domain": "AI 算力 / 半导体",
    "title": "Leading-edge AI IC designs demand comprehensive HAV methodologies",
    "url": "https://www.eetimes.com/leading-edge-ai-ic-designs-demand-comprehensive-hav-methodologies/",
    "source": "Juergen Jaeger, Director of Prototyping Product Strategy, Siemens EDA",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T13:00:00+00:00",
    "summary": "Learn how comprehensive hardware-assisted verification helps AI SoC teams accelerate RTL, software development and system validation. The post Leading-edge AI IC designs demand comprehensive HAV metho"
  },
  {
    "id": "rss:https://www.eetimes.com/can-ai-command-earth-to-orbit-operations/",
    "domain": "AI 算力 / 半导体",
    "title": "Can AI Command Earth-to-Orbit Operations?",
    "url": "https://www.eetimes.com/can-ai-command-earth-to-orbit-operations/",
    "source": "Anne-Françoise Pelé",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T08:00:00+00:00",
    "summary": "The aerospace and defense sector is facing a confluence of geopolitical instability, rapid technological advances, evolving security requirements, and complex global supply chains. The post Can AI Com"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/linux/xbox-pc-and-game-pass-titles-are-coming-to-linux-through-xodus-heroic-launcher-devs-embark-on-new-open-source-reverse-engineering-project",
    "domain": "AI 算力 / 半导体",
    "title": "Xbox PC and Game Pass titles are coming to Linux through 'Xodus' — Heroic Launcher devs embark on new open-source reverse-engineering project",
    "url": "https://www.tomshardware.com/software/linux/xbox-pc-and-game-pass-titles-are-coming-to-linux-through-xodus-heroic-launcher-devs-embark-on-new-open-source-reverse-engineering-project",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T18:11:48+00:00",
    "summary": "You might be able to enjoy Xbox PC and PC Game Pass titles on Linux very soon thanks to the efforts of the Xodus team, who're emulating the entire Xbox PC stack through open-source implementations of "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/geforce-rtx-50-series-gpu-prices-spike-as-much-as-39-percent-as-blackwell-price-hikes-hit-the-us-rtx-5070-gets-a-36-percent-hike-rtx-5060-up-27-percent-at-the-median-of-newegg-listings",
    "domain": "AI 算力 / 半导体",
    "title": "GeForce RTX 50-series GPU prices spike as much as 39% as Blackwell price hikes hit the US — RTX 5070 gets a 36% hike, RTX 5060 up 27% at the median of Newegg listings",
    "url": "https://www.tomshardware.com/pc-components/gpus/geforce-rtx-50-series-gpu-prices-spike-as-much-as-39-percent-as-blackwell-price-hikes-hit-the-us-rtx-5070-gets-a-36-percent-hike-rtx-5060-up-27-percent-at-the-median-of-newegg-listings",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T16:55:46+00:00",
    "summary": "After recent news of price hikes on RTX 50-series GPUs in other regions, those same increases now appear to have come Stateside, as Newegg prices for some Blackwell cards have spiked as much as 39% co"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-reportedly-testing-lower-memory-configs-of-rubin-ultra-as-memory-shortage-bites-back-designs-tested-include-as-little-as-192-gb-and-step-back-to-hbm4",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia reportedly testing lower memory configs of Rubin Ultra as memory shortage bites back — designs tested include as little as 192 GB and step back to HBM4",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-reportedly-testing-lower-memory-configs-of-rubin-ultra-as-memory-shortage-bites-back-designs-tested-include-as-little-as-192-gb-and-step-back-to-hbm4",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T16:47:00+00:00",
    "summary": "Nvidia is reportedly testing at least three Rubin Ultra configurations that pack as little as 192 GB of memory, as opposed to the 1 TB of HBM4E originally announced."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/rogue-ai-agent-tasked-with-booking-a-gym-class-hacks-system-removes-other-participant-says-sorry-about-that-after-trying-to-bump-user-up-the-waitlist",
    "domain": "AI 算力 / 半导体",
    "title": "Rogue AI agent tasked with booking a gym class hacks system, removes other participant — says 'sorry about that' after trying to bump user up the waitlist",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/rogue-ai-agent-tasked-with-booking-a-gym-class-hacks-system-removes-other-participant-says-sorry-about-that-after-trying-to-bump-user-up-the-waitlist",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T16:00:02+00:00",
    "summary": "A rogue OpenClaw tasked with booking a gym class for its user hacked into the system and removed another participant."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intels-core-ultra-5-250k-plus-is-down-to-its-lowest-price-ever-at-usd154-get-a-20-core-midrange-cpu-with-5-5-ghz-boost-for-an-entry-level-price",
    "domain": "AI 算力 / 半导体",
    "title": "Intel's Core Ultra 5 250K Plus is down to its lowest price ever at $154 — get a 20-core midrange CPU with 5.5 GHz boost for an entry-level price",
    "url": "https://www.tomshardware.com/pc-components/cpus/intels-core-ultra-5-250k-plus-is-down-to-its-lowest-price-ever-at-usd154-get-a-20-core-midrange-cpu-with-5-5-ghz-boost-for-an-entry-level-price",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T13:54:16+00:00",
    "summary": "Intel's 20-core Core Ultra 5 250K Plus is down to its lowest price ever on Amazon, selling for just $154 on sale."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/acer-swift-go-16-ai-amd-gorgon-point-review",
    "domain": "AI 算力 / 半导体",
    "title": "Acer Swift Go 16 AI (AMD Gorgon Point) Review: A balanced, affordable, big-screen portable",
    "url": "https://www.tomshardware.com/laptops/acer-swift-go-16-ai-amd-gorgon-point-review",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T13:05:00+00:00",
    "summary": "Acer’s Swift Go 16 AI is a capable mid-range laptop with a large touchscreen and a slim metal shell. It stands out among modern competition, if you can find it on sale for under $1,000."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/ai-data-center-bans-surge-past-500-nationwide-as-local-us-politicians-begin-blocking-new-developments-growing-public-outrage-and-bipartisan-pushback-threaten-big-tech-expansion-plans",
    "domain": "AI 算力 / 半导体",
    "title": "AI data center bans surge past 500 nationwide as local US politicians begin blocking new developments — growing public outrage and bipartisan pushback threaten big tech expansion plans",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/ai-data-center-bans-surge-past-500-nationwide-as-local-us-politicians-begin-blocking-new-developments-growing-public-outrage-and-bipartisan-pushback-threaten-big-tech-expansion-plans",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T12:25:51+00:00",
    "summary": "New AI data center development bans jumped to over 500 in July, according to recent analysis, with political and public pressure growing."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/hyperscalers-commit-nearly-usd2-trillion-to-secure-ai-hardware-and-memory-google-leads-usd811-billion-spending-surge-while-apple-trails-at-usd57-billion",
    "domain": "AI 算力 / 半导体",
    "title": "Hyperscalers commit nearly $2 trillion to secure AI hardware and memory — Google leads $811 billion spending surge while Apple trails at $57 billion",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/hyperscalers-commit-nearly-usd2-trillion-to-secure-ai-hardware-and-memory-google-leads-usd811-billion-spending-surge-while-apple-trails-at-usd57-billion",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T12:00:00+00:00",
    "summary": "As hyperscalers increase their long-term purchase commitments, the high-tech industry faces a tectonic shift as CSPs overwhelm consumer electronics companies."
  },
  {
    "id": "rss:https://www.tomshardware.com/service-providers/streaming/geforce-now-exploit-lets-you-access-the-full-windows-desktop-through-a-simple-file-swap-modder-runs-local-ai-models-on-ultimate-tier-with-48gb-of-vram-and-no-restrictions",
    "domain": "AI 算力 / 半导体",
    "title": "GeForce NOW exploit lets you access the full Windows desktop through a simple file swap — Modder runs local AI models on Ultimate tier with 48GB of VRAM and no restrictions",
    "url": "https://www.tomshardware.com/service-providers/streaming/geforce-now-exploit-lets-you-access-the-full-windows-desktop-through-a-simple-file-swap-modder-runs-local-ai-models-on-ultimate-tier-with-48gb-of-vram-and-no-restrictions",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T12:00:00+00:00",
    "summary": "Swapping the executable of a game with a modified file will fool Steam into thinking it's opening that game when it's really just giving you unrestricted desktop access. This is against GeForce NOW's "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/steam-hardware-distributor-hit-by-cyberattack-expect-fake-messages-valve-warns-europe-vendor-has-personal-information-and-hardware-purchase-details-stolen",
    "domain": "AI 算力 / 半导体",
    "title": "Steam hardware distributor hit by cyberattack, 'expect fake messages,' Valve warns — Europe vendor has personal information and hardware purchase details stolen",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/steam-hardware-distributor-hit-by-cyberattack-expect-fake-messages-valve-warns-europe-vendor-has-personal-information-and-hardware-purchase-details-stolen",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T11:49:06+00:00",
    "summary": "Steam hardware customers in Europe should 'expect fake messages' said Valve in an email bulletin, after a distributor's security was breached."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/over-70-percent-of-americans-oppose-ai-data-centers-us-protests-intensify-as-more-arrests-are-being-made-almost-40-arrested-this-year-in-backlash-to-ai-factory-buildout",
    "domain": "AI 算力 / 半导体",
    "title": "Over 70% of Americans oppose AI data centers; US protests intensify as more arrests are being made — almost 40 arrested this year in backlash to AI factory buildout",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/over-70-percent-of-americans-oppose-ai-data-centers-us-protests-intensify-as-more-arrests-are-being-made-almost-40-arrested-this-year-in-backlash-to-ai-factory-buildout",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T11:40:00+00:00",
    "summary": "The public pushback against data center construction projects is only growing stronger, even as some protesting local residents have been arrested in the process."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/hoverair-unveils-the-versa-modular-pocket-gimbal-camera-that-transforms-into-a-self-flying-drone-modular-camera-transforms-into-an-auto-tracking-drone-by-magnetically-snapping-together-for-instant-palm-launch-and-ai-tracking",
    "domain": "AI 算力 / 半导体",
    "title": "HoverAir unveils the Versa modular pocket gimbal camera that transforms into a self-flying drone — Modular camera transforms into an auto-tracking drone by magnetically snapping together for instant p",
    "url": "https://www.tomshardware.com/tech-industry/drones/hoverair-unveils-the-versa-modular-pocket-gimbal-camera-that-transforms-into-a-self-flying-drone-modular-camera-transforms-into-an-auto-tracking-drone-by-magnetically-snapping-together-for-instant-palm-launch-and-ai-tracking",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T11:20:00+00:00",
    "summary": "Have you ever wanted a pocket gimbal camera and a selfie drone that follows your around autonomously in one device? That's what the HoverAir Versa offers with a transforming, two-in-one body that can "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/the-only-current-generation-graphics-card-on-sale-below-msrp-amds-radeon-rx-9070-gre-gpu-with-12gb-of-vram-returns-to-its-lowest-ever-price-of-usd499",
    "domain": "AI 算力 / 半导体",
    "title": "The only current-generation graphics card on sale below MSRP — AMD's Radeon RX 9070 GRE GPU with 12GB of VRAM returns to its lowest-ever price of $499",
    "url": "https://www.tomshardware.com/pc-components/gpus/the-only-current-generation-graphics-card-on-sale-below-msrp-amds-radeon-rx-9070-gre-gpu-with-12gb-of-vram-returns-to-its-lowest-ever-price-of-usd499",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T10:58:38+00:00",
    "summary": "Grab a new GPU for less than the MSRP launch price. Gigabyte's Gaming RX 9070 GRE falls to its lowest-ever price."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/uks-royal-navy-sea-drones-contain-component-that-secretly-sent-data-to-china-report-claims-government-cuts-camera-connectivity-and-insists-data-wasnt-sensitive-only-heartbeat-communications",
    "domain": "AI 算力 / 半导体",
    "title": "UK's Royal Navy sea drones contain component that secretly sent data to China, report claims — government cuts camera connectivity and insists data wasn’t sensitive, only ‘heartbeat communications’",
    "url": "https://www.tomshardware.com/tech-industry/drones/uks-royal-navy-sea-drones-contain-component-that-secretly-sent-data-to-china-report-claims-government-cuts-camera-connectivity-and-insists-data-wasnt-sensitive-only-heartbeat-communications",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T10:31:39+00:00",
    "summary": "K3 Scout surveillance drones used by the UK’s Royal Navy contain components that have been secretly transmitting data to China, according to reports."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/windows-11s-built-in-weather-app-hogs-more-than-1-2-gigabytes-of-ram-just-to-tell-the-forecast-memory-sucking-web-wrapper-filled-with-ads-masquerades-as-an-actual-application",
    "domain": "AI 算力 / 半导体",
    "title": "Windows 11's built-in weather app hogs more than 1.2 gigabytes of RAM just to tell the forecast — memory-sucking web wrapper filled with ads masquerades as an actual application",
    "url": "https://www.tomshardware.com/software/windows/windows-11s-built-in-weather-app-hogs-more-than-1-2-gigabytes-of-ram-just-to-tell-the-forecast-memory-sucking-web-wrapper-filled-with-ads-masquerades-as-an-actual-application",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T10:30:00+00:00",
    "summary": "MSN Weather acts as the native weather app for Windows 11 and all it does it run a bunch of Chromium subprocesses in the background to retrieve the forecast data. This causes it to use 5x more memory "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/save-nearly-usd350-on-this-4tb-samsung-9910-pro-ssd-with-gen-5-speeds-right-now-limited-time-woot-sale-delivers-ultra-fast-storage-with-speeds-up-to-14-800-mb-s",
    "domain": "AI 算力 / 半导体",
    "title": "Save nearly $350 on this 4TB Samsung 9910 Pro SSD with Gen 5 speeds right now —limited-time Woot sale delivers ultra-fast storage with speeds up to 14,800 MB/s",
    "url": "https://www.tomshardware.com/pc-components/ssds/save-nearly-usd350-on-this-4tb-samsung-9910-pro-ssd-with-gen-5-speeds-right-now-limited-time-woot-sale-delivers-ultra-fast-storage-with-speeds-up-to-14-800-mb-s",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T10:18:51+00:00",
    "summary": "Save $413 on this 4TB Samsung 9100 Pro SSD, offering super-fast Gen 5 speeds, now priced at $619.99 in this limited-time Woot sale."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/chinese-farmer-kills-25-acres-of-crops-after-following-ai-generated-weed-and-pest-control-advice-farmer-trusted-pesticide-recipe-after-months-of-successful-advice",
    "domain": "AI 算力 / 半导体",
    "title": "Chinese farmer kills 25 acres of crops after following AI-generated weed and pest control advice — farmer trusted pesticide recipe after months of successful advice",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/chinese-farmer-kills-25-acres-of-crops-after-following-ai-generated-weed-and-pest-control-advice-farmer-trusted-pesticide-recipe-after-months-of-successful-advice",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T10:00:00+00:00",
    "summary": "A farmer in China followed an AI app's advice for his 25-acre farmland, resulting in the death of his entire crop of sesame seedlings. 67-year-old man was initially skeptical of the tool but eventuall"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/space/europe-expands-its-starlink-rival-to-348-satellites-as-iris2-moves-into-implementation-eur15-6-billion-network-will-boost-eu-government-capacity-by-60-percent-with-launches-starting-in-2029",
    "domain": "AI 算力 / 半导体",
    "title": "Europe expands its Starlink rival to 348 satellites as IRIS² moves into implementation — €15.6 billion network will boost EU government capacity by 60%, with launches starting in 2029",
    "url": "https://www.tomshardware.com/tech-industry/space/europe-expands-its-starlink-rival-to-348-satellites-as-iris2-moves-into-implementation-eur15-6-billion-network-will-boost-eu-government-capacity-by-60-percent-with-launches-starting-in-2029",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T09:30:00+00:00",
    "summary": "Europe has finalized plans for its €15.6 billion IRIS² satellite network, expanding it to 348 satellites with first launches scheduled for 2029."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/wolfbox-mf60-compressed-air-duster-is-nearly-40-percent-off-in-a-limited-time-deal-powerful-rechargeable-devices-propulsion-fan-runs-at-up-to-110-000-rpm",
    "domain": "AI 算力 / 半导体",
    "title": "Wolfbox MF60 Compressed Air Duster is nearly 40% off in a limited-time deal — powerful rechargeable device's propulsion fan runs at up to 110,000 RPM",
    "url": "https://www.tomshardware.com/pc-components/wolfbox-mf60-compressed-air-duster-is-nearly-40-percent-off-in-a-limited-time-deal-powerful-rechargeable-devices-propulsion-fan-runs-at-up-to-110-000-rpm",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T15:52:16+00:00",
    "summary": "The Wolfbox MegaFlow 60 has surprisingly dipped below the price of the MegaFlow 50 air duster, and is currently just $30.39."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-keyboards/turtle-beach-command-series-kb5-review-a-touchscreen-and-a-numberpad-in-one-keyboard",
    "domain": "AI 算力 / 半导体",
    "title": "Turtle Beach Command Series KB5 Review: A touchscreen and a numberpad in one keyboard?",
    "url": "https://www.tomshardware.com/peripherals/gaming-keyboards/turtle-beach-command-series-kb5-review-a-touchscreen-and-a-numberpad-in-one-keyboard",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T15:02:16+00:00",
    "summary": "The Turtle Beach Command Series KB5 is a full-size, wired, low-profile keyboard with a small, programmable touchscreen."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/pc-cases/noctua-finds-more-than-half-of-tested-pc-cases-misstate-cpu-cooler-clearances-hands-on-checks-reveal-errors-ranging-from-3-5mm-to-10mm-internal-compatibility-team-conducted-measurements-of-more-than-a-hundred-cases",
    "domain": "AI 算力 / 半导体",
    "title": "Noctua finds more than half of tested PC cases misstate CPU cooler clearances — hands-on checks reveal errors ranging from -3.5mm to +10mm, internal compatibility team conducted measurements of more t",
    "url": "https://www.tomshardware.com/pc-components/pc-cases/noctua-finds-more-than-half-of-tested-pc-cases-misstate-cpu-cooler-clearances-hands-on-checks-reveal-errors-ranging-from-3-5mm-to-10mm-internal-compatibility-team-conducted-measurements-of-more-than-a-hundred-cases",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T14:35:00+00:00",
    "summary": "Users are asking why some measurements on Noctua's compatibility page are different from manufacturer spec sheets."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/liquid-cooling/modder-pumps-liquid-directly-over-bare-gpu-silicon-via-3d-printed-block-drops-rtx-2060-super-load-temps-to-28-c-despite-initial-leaks",
    "domain": "AI 算力 / 半导体",
    "title": "Modder pumps liquid directly over bare GPU silicon via 3D-printed block — drops RTX 2060 Super load temps to 28°C despite initial leaks",
    "url": "https://www.tomshardware.com/pc-components/liquid-cooling/modder-pumps-liquid-directly-over-bare-gpu-silicon-via-3d-printed-block-drops-rtx-2060-super-load-temps-to-28-c-despite-initial-leaks",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T14:15:00+00:00",
    "summary": "The fearless TrashBench has been testing direct die water cooling of graphics cards and suffered most of the leaky nightmares you might expect."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/musks-terafab-projected-to-be-larger-than-the-pentagon-apple-park-mall-of-america-and-giga-texas-combined-all-in-one-chip-manufacturing-facility-visualized-to-show-the-projects-massive-footprint",
    "domain": "AI 算力 / 半导体",
    "title": "Musk’s Terafab projected to be larger than the Pentagon, Apple Park, Mall of America, and Giga Texas, combined — all-in-one chip manufacturing facility visualized to show the project’s massive footpri",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/musks-terafab-projected-to-be-larger-than-the-pentagon-apple-park-mall-of-america-and-giga-texas-combined-all-in-one-chip-manufacturing-facility-visualized-to-show-the-projects-massive-footprint",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T13:55:00+00:00",
    "summary": "Elon Musk's Terafab will have at least 100 million sq. ft of interior space, making it the largest such structure on Earth by a big margin. It seems that it will need this amount of space, though, for"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/microsoft-office/x64-port-of-microsoft-word-for-windows-1-1a-arrives-you-can-now-run-this-seminal-1990-word-processor-natively-in-windows-11",
    "domain": "AI 算力 / 半导体",
    "title": "x64 port of Microsoft Word for Windows 1.1a arrives — you can now run this seminal 1990 word processor natively in Windows 11",
    "url": "https://www.tomshardware.com/software/microsoft-office/x64-port-of-microsoft-word-for-windows-1-1a-arrives-you-can-now-run-this-seminal-1990-word-processor-natively-in-windows-11",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T13:40:00+00:00",
    "summary": "A developer has ported 1990's Microsoft Word for Windows 1.1a to x64 so it can run natively on Windows 11 PC systems."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/two-variants-of-nvidias-rtx-spark-show-up-on-geekbench-revealing-a-cut-down-18-core-model-full-20-core-beats-most-x86-mobile-chips-across-multi-core-and-single-core-tests",
    "domain": "AI 算力 / 半导体",
    "title": "Two variants of Nvidia's RTX Spark show up on Geekbench, revealing a cut-down 18-core model — Full 20-core beats most x86 mobile chips across multi-core and single-core tests",
    "url": "https://www.tomshardware.com/pc-components/cpus/two-variants-of-nvidias-rtx-spark-show-up-on-geekbench-revealing-a-cut-down-18-core-model-full-20-core-beats-most-x86-mobile-chips-across-multi-core-and-single-core-tests",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T13:20:00+00:00",
    "summary": "The 20-core SKU of the RTX Spark that we've known to exist for a long time scored 2,570 points in the single-core test and 23,126 points in the multi-core test. The second, 18-core cut-down SKU scored"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/fcc-moves-to-ban-lidar-equipped-foreign-drones-from-us-classifies-the-technology-as-military-grade-in-a-proposal-that-could-also-hit-thermal-models-and-the-swarms-used-drone-light-shows",
    "domain": "AI 算力 / 半导体",
    "title": "FCC moves to ban LiDAR-equipped foreign drones from US — classifies the technology as \"military-grade\" in a proposal that could also hit thermal models and the swarms used in drone light shows",
    "url": "https://www.tomshardware.com/tech-industry/drones/fcc-moves-to-ban-lidar-equipped-foreign-drones-from-us-classifies-the-technology-as-military-grade-in-a-proposal-that-could-also-hit-thermal-models-and-the-swarms-used-drone-light-shows",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T13:00:00+00:00",
    "summary": "The FCC is proposing a retroactive sales ban on previously approved foreign-made drones with LiDAR and other “military-grade” features, potentially removing several popular DJI models from U.S. stores"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/amazons-new-7-65gw-texas-ai-data-center-power-plant-could-become-the-largest-source-of-co2-pollution-in-the-us-custom-35-turbine-gas-plant-authorized-to-emit-33-million-tons-of-annual-greenhouse-gases",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon’s new 7.65GW Texas AI data center power plant could become the largest source of CO₂ pollution in the US — custom 35-turbine gas plant authorized to emit 33 million tons of annual greenhouse ga",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/amazons-new-7-65gw-texas-ai-data-center-power-plant-could-become-the-largest-source-of-co2-pollution-in-the-us-custom-35-turbine-gas-plant-authorized-to-emit-33-million-tons-of-annual-greenhouse-gases",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T12:40:00+00:00",
    "summary": "Amazon is reportedly building a 7.65GW natural gas power plant in Texas to feed a new AI data center, with permits allowing up to 33 million tons of CO₂ emissions per year."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/kansas-town-silences-public-comment-on-gigawatt-ai-data-center-after-receiving-death-threats-moves-to-virtual-meetings-shift-follows-physics-teachers-arrest-for-clapping-at-data-center-hearing",
    "domain": "AI 算力 / 半导体",
    "title": "Kansas town silences public comment on gigawatt AI data center after receiving death threats, moves to virtual meetings — shift follows physics teacher's arrest for clapping at data center hearing",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/kansas-town-silences-public-comment-on-gigawatt-ai-data-center-after-receiving-death-threats-moves-to-virtual-meetings-shift-follows-physics-teachers-arrest-for-clapping-at-data-center-hearing",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T12:20:00+00:00",
    "summary": "Emporia, Kansas, switched to virtual city council meetings after death threats intensified against city leaders. The move also canceled public comments, prompting some members of the public to ask why"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-core-ultra-7-270k-plus-vs-amd-ryzen-7-7700x3d-faceoff",
    "domain": "AI 算力 / 半导体",
    "title": "Intel Core Ultra 7 270K Plus vs AMD Ryzen 7 7700X3D faceoff — battle of the upper mid-range CPUs",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-core-ultra-7-270k-plus-vs-amd-ryzen-7-7700x3d-faceoff",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T12:05:00+00:00",
    "summary": "AMD's 3D V-Cache takes on Intel's latest Core Ultra architecture as we compare the two across various metrics including gaming, productivity, power consumption, and value."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/usb-flash-drives/open-source-stealth-usb-hides-an-encrypted-partition-behind-an-8gb-decoy-drive-phantom-drive-appears-as-a-regular-usb-stick-until-you-create-a-text-file-to-unlock-the-hidden-data",
    "domain": "AI 算力 / 半导体",
    "title": "Open-source stealth USB hides an encrypted partition behind an 8GB decoy drive — 'Phantom Drive' appears as a regular USB stick until you create a text file to unlock the hidden data",
    "url": "https://www.tomshardware.com/pc-components/usb-flash-drives/open-source-stealth-usb-hides-an-encrypted-partition-behind-an-8gb-decoy-drive-phantom-drive-appears-as-a-regular-usb-stick-until-you-create-a-text-file-to-unlock-the-hidden-data",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T12:00:00+00:00",
    "summary": "This USB looks like a standard 8GB drive, but it unlocks a hidden partition when you create a text file with the password inside. The password is never actually written to storage; it's instead interc"
  },
  {
    "id": "rss:https://www.eetimes.com/after-seven-ceos-in-10-years-imagination-is-sticking-to-its-strategy/",
    "domain": "AI 算力 / 半导体",
    "title": "After Seven CEOs in 10 Years, Imagination Is Sticking to Its Strategy",
    "url": "https://www.eetimes.com/after-seven-ceos-in-10-years-imagination-is-sticking-to-its-strategy/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T22:00:00+00:00",
    "summary": "Imagination dumps CPU/NPU dreams, doubles down on GPUs and China under CEO No. 7. The post After Seven CEOs in 10 Years, Imagination Is Sticking to Its Strategy appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/rolecs-technoplus-ip-rated-pole-mount-plastic-enclosures-for-iot-iiot-and-factory-automation/",
    "domain": "AI 算力 / 半导体",
    "title": "ROLEC’s technoPLUS: IP-rated Pole-mount Plastic Enclosures for IoT/IIoT and Factory Automation",
    "url": "https://www.eetimes.com/rolecs-technoplus-ip-rated-pole-mount-plastic-enclosures-for-iot-iiot-and-factory-automation/",
    "source": "ROLEC",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T16:15:30+00:00",
    "summary": "IoT/IIoT and factory automation are driving demand for ROLEC’s updated pole-mountable technoPLUS (IP 66, IP 67, IP 69K) plastic enclosures. Electronics designers specify them for ‘close-to-the-process"
  },
  {
    "id": "rss:https://www.eetimes.com/biwin-and-tera-industria-de-semicondutores-sign-strategic-partnership-agreement/",
    "domain": "AI 算力 / 半导体",
    "title": "BIWIN and Tera Indústria de Semicondutores Sign Strategic Partnership Agreement",
    "url": "https://www.eetimes.com/biwin-and-tera-industria-de-semicondutores-sign-strategic-partnership-agreement/",
    "source": "BIWIN Semiconductor",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T16:08:31+00:00",
    "summary": "Shenzhen, China / Manaus, Brazil – August 6th, 2026: BIWIN Semiconductor (HK) Company Limited (&#8220;BIWIN&#8221;), a global provider of memory and storage packaging solutions, and TERA INDÚSTRIA DE "
  },
  {
    "id": "rss:https://www.eetimes.com/chiplet-architectures-as-a-practical-path-to-scalable-automotive-compute/",
    "domain": "AI 算力 / 半导体",
    "title": "Chiplet Architectures as a Practical Path to Scalable Automotive Compute",
    "url": "https://www.eetimes.com/chiplet-architectures-as-a-practical-path-to-scalable-automotive-compute/",
    "source": "Cyril Cordoba",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T13:56:43+00:00",
    "summary": "Chiplets are auto’s escape hatch from bloated SoCs, scaling SDV compute without wrecking cost or software. The post Chiplet Architectures as a Practical Path to Scalable Automotive Compute appeared fi"
  },
  {
    "id": "rss:https://www.eetimes.com/inside-device-connectivity-a-new-design-discipline-for-next-gen-vehicles/",
    "domain": "AI 算力 / 半导体",
    "title": "Inside Device Connectivity: A New Design Discipline for Next-Gen Vehicles",
    "url": "https://www.eetimes.com/inside-device-connectivity-a-new-design-discipline-for-next-gen-vehicles/",
    "source": "TE Connectivity",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T10:53:14+00:00",
    "summary": "Join this webinar where our expert will introduce Inside Device Connectivity as a focused design discipline to ensure power, signal, and data move predictably and robustly within automotive electronic"
  },
  {
    "id": "rss:https://www.eetimes.com/stmicroelectronics-bets-on-hardware-based-post-quantum-cryptography-with-st54m/",
    "domain": "AI 算力 / 半导体",
    "title": "STMicroelectronics Bets on Hardware-Based Post-Quantum Cryptography with ST54M",
    "url": "https://www.eetimes.com/stmicroelectronics-bets-on-hardware-based-post-quantum-cryptography-with-st54m/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T08:00:00+00:00",
    "summary": "ST’s ST54M bakes post-quantum crypto into phone hardware before hackers harvest today’s secrets. The post STMicroelectronics Bets on Hardware-Based Post-Quantum Cryptography with ST54M appeared first "
  },
  {
    "id": "hn:49177126",
    "domain": "AI 算力 / 半导体",
    "title": "It looks like 'Big Short' investor Michael Burry nailed bet against chip stocks",
    "url": "https://www.businessinsider.com/big-short-michael-burry-ai-chip-stocks-soxx-nvidia-substack-2026-8",
    "source": "mapping365",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-08-05T00:30:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:49084371",
    "domain": "AI 算力 / 半导体",
    "title": "Show HN: Tines 3B – safe workflow automation for when everyone builds software",
    "url": "https://www.tines.com/",
    "source": "retsol",
    "platform": "hackernews",
    "points": 27,
    "published_at": "2026-07-28T14:23:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:49125140",
    "domain": "AI 算力 / 半导体",
    "title": "Hygon Reveals 512-Thread CPU and AI GPU to Rival Intel Xeon and Nvidia",
    "url": "https://www.ubergizmo.com/2026/06/hygon-512-thread-cpu/",
    "source": "rbanffy",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-07-31T16:21:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:49093429",
    "domain": "AI 算力 / 半导体",
    "title": "Kospi Plunges After Nvidia CEO's Visits Spark 'Huang Curse' Fears",
    "url": "https://www.chosun.com/english/market-money-en/2026/07/29/6FEUZWQT5BG3HMJ3G2RZPHROGM/",
    "source": "mapping365",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-07-29T04:29:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:48992221",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC eyes price hikes of up to 25% on chip production services in 2027",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/tsmc-eyes-price-hikes-of-up-to-25-percent-on-chip-production-services-in-2027-report-claims-plans-to-raise-baseline-prices-by-5-percent-to-10-percent-on-advanced-nodes",
    "source": "speckx",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-07-21T13:40:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:48894277",
    "domain": "AI 算力 / 半导体",
    "title": "Apple's rumored M7 Ultra targets 1.5TB and Blackwell-class AI performance",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/apples-rumored-m7-ultra-targets-1-5tb-of-memory-and-blackwell-class-ai",
    "source": "rbanffy",
    "platform": "hackernews",
    "points": 26,
    "published_at": "2026-07-13T15:32:19+00:00",
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
    "id": "hn:49184755",
    "domain": "大厂 AI 动态",
    "title": "Changes at Google DeepMind: Demis Hassabis from CEO to Chair, Jeff Dean departs",
    "url": "https://blog.google/company-news/inside-google/message-ceo/next-chapter-ai-momentum/",
    "source": "colesantiago",
    "platform": "hackernews",
    "points": 863,
    "published_at": "2026-08-05T16:05:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:48993414",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.6 Flash, 3.5 Flash-Lite, and 3.5 Flash Cyber",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/",
    "source": "logickkk1",
    "platform": "hackernews",
    "points": 760,
    "published_at": "2026-07-21T15:17:16+00:00",
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
    "points": 445,
    "published_at": "2026-08-08T09:18:50+00:00",
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
    "id": "hn:48925271",
    "domain": "大厂 AI 动态",
    "title": "Why I Left Google DeepMind",
    "url": "https://turntrout.com/why-i-left-google-deepmind",
    "source": "apsec112",
    "platform": "hackernews",
    "points": 390,
    "published_at": "2026-07-15T18:40:34+00:00",
    "summary": ""
  },
  {
    "id": "hn:48936451",
    "domain": "大厂 AI 动态",
    "title": "NotebookLM is now Gemini Notebook",
    "url": "https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/",
    "source": "xnx",
    "platform": "hackernews",
    "points": 371,
    "published_at": "2026-07-16T16:08:13+00:00",
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
    "id": "hn:48965880",
    "domain": "大厂 AI 动态",
    "title": "Ollama: All Aboard Open Models",
    "url": "https://ollama.com/blog/all-aboard-open-models",
    "source": "inferhaven",
    "platform": "hackernews",
    "points": 138,
    "published_at": "2026-07-19T07:59:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:48998606",
    "domain": "大厂 AI 动态",
    "title": "Gemini last models: temperature, top_p, and top_k are deprecated and ignored",
    "url": "https://ai.google.dev/gemini-api/docs/latest-model",
    "source": "greatgib",
    "platform": "hackernews",
    "points": 136,
    "published_at": "2026-07-21T21:27:54+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/977623/mark-zuckerberg-ai-manifesto-dim-vision",
    "domain": "大厂 AI 动态",
    "title": "Mark Zuckerberg doesn’t understand how to live",
    "url": "https://www.theverge.com/ai-artificial-intelligence/977623/mark-zuckerberg-ai-manifesto-dim-vision",
    "source": "Elizabeth Lopatto",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T22:00:00+00:00",
    "summary": "Recently, a man I was rock climbing with told me about how he'd used AI to make a motivational poster for himself, which he'd hung on his bedroom wall: a bear, walking a slackline over a canyon, holdi"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/977626/anker-nano-travel-adapter-summer-travel-tech-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Anker&#8217;s travel charger works in almost any country and is down to $20",
    "url": "https://www.theverge.com/gadgets/977626/anker-nano-travel-adapter-summer-travel-tech-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T21:18:15+00:00",
    "summary": "If you’ve got international travel coming up, an adapter is essential for keeping your phone, earbuds, power banks, and other gadgets charged. Anker’s Nano Travel Adapter is one of our picks from our "
  },
  {
    "id": "rss:https://www.theverge.com/tech/977581/bluesky-hide-reposts-user-post-count-threads",
    "domain": "大厂 AI 动态",
    "title": "Bluesky now lets you hide reposts from that annoying person you follow",
    "url": "https://www.theverge.com/tech/977581/bluesky-hide-reposts-user-post-count-threads",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T19:26:50+00:00",
    "summary": "Bluesky has added a new feature that lets you hide reposts from a specific person in your feeds. The tool might be helpful if you want to stop seeing reposts from that one person who clogs up your fee"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/977489/costco-switch-2-microsd-express-switch-online-expansion-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Costco&#8217;s great Switch 2 console bundle includes over $100 in free stuff",
    "url": "https://www.theverge.com/gadgets/977489/costco-switch-2-microsd-express-switch-online-expansion-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T19:14:27+00:00",
    "summary": "The cost of the Nintendo Switch 2 is going up by $50 on September 1st, 2026, resulting in a $499.99 price tag for just the console. We’re just weeks away, but Costco is offering a fantastic $499.99 bu"
  },
  {
    "id": "rss:https://www.theverge.com/tech/977448/made-by-google-2026-pixel-hardware-launch-event",
    "domain": "大厂 AI 动态",
    "title": "What to expect from Google’s 2026 Pixel hardware launch event",
    "url": "https://www.theverge.com/tech/977448/made-by-google-2026-pixel-hardware-launch-event",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T17:30:00+00:00",
    "summary": "It's that time of year: On Wednesday, Google is set to host its annual Made by Google hardware launch event for Pixel gadgets. Google itself has already teased new slab-style and foldable Pixel smartp"
  },
  {
    "id": "rss:https://www.theverge.com/streaming/977474/youtube-partner-program-new-requirements",
    "domain": "大厂 AI 动态",
    "title": "YouTube is making it harder to earn money on YouTube",
    "url": "https://www.theverge.com/streaming/977474/youtube-partner-program-new-requirements",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T17:26:46+00:00",
    "summary": "Starting February 1st, 2027, creators who want to monetize their channel through YouTube's Partner Program (YPP) will need at least 1,000 subscribers and either 8,000 qualified watch hours over the pa"
  },
  {
    "id": "rss:https://www.theverge.com/tech/977395/meta-mark-zuckerberg-superintelligent-ai-ramble",
    "domain": "大厂 AI 动态",
    "title": "Four takeaways from Mark Zuckerberg&#8217;s massive AI manifesto",
    "url": "https://www.theverge.com/tech/977395/meta-mark-zuckerberg-superintelligent-ai-ramble",
    "source": "Jess Weatherbed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T15:19:05+00:00",
    "summary": "Meta CEO Mark Zuckerberg has a lot to say about the idealized future he now envisions for humanity co-existing with artificial intelligence - his latest essay spans more than 6,500 words on the matter"
  },
  {
    "id": "rss:https://www.theverge.com/tech/977199/apple-will-stream-friday-night-baseball-live-in-vision-pro",
    "domain": "大厂 AI 动态",
    "title": "Apple will stream Friday Night Baseball live in Vision Pro",
    "url": "https://www.theverge.com/tech/977199/apple-will-stream-friday-night-baseball-live-in-vision-pro",
    "source": "David Imel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T15:00:00+00:00",
    "summary": "Starting on Friday, August 28th, Apple will begin streaming Friday Night Baseball in immersive video on Apple Vision Pro. The stream will feature commentary from various analysts and reporters, and li"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/977300/keychron-hall-effect-sony-inzone-headsets-gaming-laptop-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Keychron’s wireless Hall effect keyboard is back to its lowest price",
    "url": "https://www.theverge.com/gadgets/977300/keychron-hall-effect-sony-inzone-headsets-gaming-laptop-deal-sale",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T14:27:23+00:00",
    "summary": "Getting a keyboard with customizable Hall effect sensors is more affordable than it used to be, and you don’t need to compromise on quality to get a good deal. Keychron’s aluminum-clad K2 HE with a 75"
  },
  {
    "id": "rss:https://www.theverge.com/podcast/975732/bose-ceo-lila-snyder-ai-wearables-licensing-headphones-audio",
    "domain": "大厂 AI 动态",
    "title": "What happens to Bose when headphones become AI?",
    "url": "https://www.theverge.com/podcast/975732/bose-ceo-lila-snyder-ai-wearables-licensing-headphones-audio",
    "source": "Nilay Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T14:00:00+00:00",
    "summary": "Today, I’m talking with Lila Snyder, who is the CEO of Bose. You certainly know Bose — it’s one of the most famous brands in all of consumer tech. The company started 60 years ago selling speakers to "
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/10/openai-reportedly-completed-a-7-billion-employee-tender-offer/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI reportedly completed a $7 billion employee tender offer",
    "url": "https://techcrunch.com/2026/08/10/openai-reportedly-completed-a-7-billion-employee-tender-offer/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T00:03:18+00:00",
    "summary": "San Francisco's housing market is in trouble again."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/10/as-ai-led-attacks-multiply-openai-launches-a-new-cyber-model/",
    "domain": "大厂 AI 动态",
    "title": "As AI-led attacks multiply, OpenAI launches a new cyber model",
    "url": "https://techcrunch.com/2026/08/10/as-ai-led-attacks-multiply-openai-launches-a-new-cyber-model/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T23:56:15+00:00",
    "summary": "OpenAI is expanding its AI cybersecurity defense program Daybreak, and rolling out a new cyber-trained AI model with it."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/10/jeff-bezos-might-finally-get-his-hands-on-a-sports-team/",
    "domain": "大厂 AI 动态",
    "title": "Jeff Bezos might finally get his hands on a sports team",
    "url": "https://techcrunch.com/2026/08/10/jeff-bezos-might-finally-get-his-hands-on-a-sports-team/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T23:16:44+00:00",
    "summary": "Jeff Bezos is reportedly close to buying his first stake in a sports team: the U.K.'s famed Liverpool Football Club."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/10/now-rippling-is-counter-suing-tiny-startup-runlayer/",
    "domain": "大厂 AI 动态",
    "title": "Now Rippling is counter-suing tiny startup Runlayer",
    "url": "https://techcrunch.com/2026/08/10/now-rippling-is-counter-suing-tiny-startup-runlayer/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T22:26:54+00:00",
    "summary": "This lawsuit follows one filed last month by Runlayer that accused Rippling of stealing its product ideas. It's a seller- and buyer-beware market warning."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/10/google-co-founder-sergey-brin-has-now-spent-100-million-to-fight-the-billionaire-tax/",
    "domain": "大厂 AI 动态",
    "title": "Google co-founder Sergey Brin has now spent $100 million to fight the billionaire tax",
    "url": "https://techcrunch.com/2026/08/10/google-co-founder-sergey-brin-has-now-spent-100-million-to-fight-the-billionaire-tax/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T21:20:04+00:00",
    "summary": "California's Prop 40 would impose a one-time 5% tax on the net worth of the state's billionaires."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/10/mark-zuckerbergs-ai-manifesto-is-exactly-why-people-dont-like-ai/",
    "domain": "大厂 AI 动态",
    "title": "Mark Zuckerberg’s AI manifesto is exactly why people don’t like AI",
    "url": "https://techcrunch.com/2026/08/10/mark-zuckerbergs-ai-manifesto-is-exactly-why-people-dont-like-ai/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T20:53:02+00:00",
    "summary": "On Monday, Mark Zuckerberg published a 6,500-word manifesto about personal AI, largely about the possibilities for the \"personal superintelligence\" systems Meta AI is building."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/10/tech-industry-is-buzzing-after-a-claude-agent-hacked-into-a-gym/",
    "domain": "大厂 AI 动态",
    "title": "Tech industry is buzzing after a Claude agent hacked into a gym",
    "url": "https://techcrunch.com/2026/08/10/tech-industry-is-buzzing-after-a-claude-agent-hacked-into-a-gym/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T20:04:24+00:00",
    "summary": "An OpenClaw agent hacked into a gym's reservation system to bump its human boss higher on a class' waitlist. And the tech industry took notice."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/10/aptoide-becomes-the-first-rival-app-store-to-return-to-google-play-in-the-us/",
    "domain": "大厂 AI 动态",
    "title": "Aptoide becomes the first rival app store to return to Google Play in the US",
    "url": "https://techcrunch.com/2026/08/10/aptoide-becomes-the-first-rival-app-store-to-return-to-google-play-in-the-us/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T18:31:54+00:00",
    "summary": "Aptoide has brought its games store back to Google Play after more than a decade, as court-ordered changes open Android to competing app stores."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/10/social-media-platforms-still-facing-thousands-of-user-addiction-lawsuits-after-failed-appeals/",
    "domain": "大厂 AI 动态",
    "title": "Social media platforms still facing thousands of user addiction lawsuits after failed appeals",
    "url": "https://techcrunch.com/2026/08/10/social-media-platforms-still-facing-thousands-of-user-addiction-lawsuits-after-failed-appeals/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T18:30:33+00:00",
    "summary": "Platforms like Meta, TikTok, Snapchat, and Google are facing a long road of litigation."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/10/youtube-now-requires-creators-to-have-twice-as-many-watch-hours-to-start-earning-money/",
    "domain": "大厂 AI 动态",
    "title": "YouTube now requires creators to have twice as many watch hours to start earning money",
    "url": "https://techcrunch.com/2026/08/10/youtube-now-requires-creators-to-have-twice-as-many-watch-hours-to-start-earning-money/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T18:27:44+00:00",
    "summary": "Creators who want to start earning on the platform will need at least 8,000 qualified watch hours over the past year or 20 million qualified Shorts views in the last 90 days."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/10/clicks-power-keyboard-brings-blackberry-style-typing-to-any-phone-with-some-compromises/",
    "domain": "大厂 AI 动态",
    "title": "Clicks’ Power Keyboard brings BlackBerry-style typing to any phone — with some compromises",
    "url": "https://techcrunch.com/2026/08/10/clicks-power-keyboard-brings-blackberry-style-typing-to-any-phone-with-some-compromises/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T18:00:39+00:00",
    "summary": "Clicks’ $99 Power Keyboard brings a customizable, slide-out physical keyboard to MagSafe and Qi2 smartphones, but its added heft can make larger phones awkward to use."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/10/metas-new-glimmer-ai-model-offers-a-hint-at-zuckerbergs-personal-intelligence-vision/",
    "domain": "大厂 AI 动态",
    "title": "Meta’s new Glimmer AI model offers a hint at Zuckerberg’s personal intelligence vision",
    "url": "https://techcrunch.com/2026/08/10/metas-new-glimmer-ai-model-offers-a-hint-at-zuckerbergs-personal-intelligence-vision/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T16:20:13+00:00",
    "summary": "Meta’s new open-weight Muse Glimmer model offers a glimpse of Mark Zuckerberg’s personal superintelligence vision, as well as the emerging divide between AI users can own and access."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/10/sila-lands-1-4b-pentagon-loan-as-militaries-demand-more-batteries/",
    "domain": "大厂 AI 动态",
    "title": "Sila lands $1.4B Pentagon loan as militaries demand more batteries",
    "url": "https://techcrunch.com/2026/08/10/sila-lands-1-4b-pentagon-loan-as-militaries-demand-more-batteries/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T15:22:42+00:00",
    "summary": "Battery materials startup Sila will use a $1.4 billion loan from the U.S. Department of Defense to scale production at its factory in Washington state."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/10/archer-buys-former-rival-wisk-aero/",
    "domain": "大厂 AI 动态",
    "title": "Archer buys former rival Wisk Aero",
    "url": "https://techcrunch.com/2026/08/10/archer-buys-former-rival-wisk-aero/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T15:09:39+00:00",
    "summary": "The two companies were once embroiled in a trade secret theft lawsuit. Now, Wisk is being absorbed into Archer."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/10/a-data-breach-at-shipping-giant-ceva-logistics-is-rippling-across-banks-retailers-steam-gamers-and-beyond/",
    "domain": "大厂 AI 动态",
    "title": "A data breach at shipping giant Ceva Logistics is rippling across banks, retailers, Steam gamers, and beyond",
    "url": "https://techcrunch.com/2026/08/10/a-data-breach-at-shipping-giant-ceva-logistics-is-rippling-across-banks-retailers-steam-gamers-and-beyond/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T14:20:19+00:00",
    "summary": "Companies that rely on Ceva Logistics for shipping their physical goods to customers say their personal data was taken during a recent cyberattack."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/10/signed-up-for-klaviyo-dozens-of-advertisers-may-have-seen-your-password/",
    "domain": "大厂 AI 动态",
    "title": "Signed up for Klaviyo? Dozens of advertisers may have seen your password",
    "url": "https://techcrunch.com/2026/08/10/signed-up-for-klaviyo-dozens-of-advertisers-may-have-seen-your-password/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T14:14:43+00:00",
    "summary": "A bug in the tech giant's website the logo of US marketing automation company Klaviyo Inc. is seen displayed on a smartphone in front of an abstract background on a computer screen.."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/10/discovered-materials-is-playing-ai-whack-a-mole-to-hunt-cooler-chips/",
    "domain": "大厂 AI 动态",
    "title": "Discovered Materials is playing AI whack-a-mole to hunt cooler chips",
    "url": "https://techcrunch.com/2026/08/10/discovered-materials-is-playing-ai-whack-a-mole-to-hunt-cooler-chips/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T12:00:00+00:00",
    "summary": "Discovered Materials raised $9 million to fund the hunt for more novel materials to build more efficient chips."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/10/google-play-adds-venmo-as-a-payment-option/",
    "domain": "大厂 AI 动态",
    "title": "Google Play adds Venmo as a payment option",
    "url": "https://techcrunch.com/2026/08/10/google-play-adds-venmo-as-a-payment-option/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T12:00:00+00:00",
    "summary": "The ability to add Venmo to Google Play comes as people are spending more money on apps and games."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/09/embattled-hedge-fund-situational-awareness-invests-400m-in-chip-startup-source-foundry/",
    "domain": "大厂 AI 动态",
    "title": "Embattled hedge fund Situational Awareness invests $400M in chip startup Source Foundry",
    "url": "https://techcrunch.com/2026/08/09/embattled-hedge-fund-situational-awareness-invests-400m-in-chip-startup-source-foundry/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T20:35:17+00:00",
    "summary": "The AI-focused hedge fund is still making some big bets."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/09/anthropic-is-turning-claude-codes-auto-mode-on-by-default/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic is turning Claude Code’s auto mode on by default",
    "url": "https://techcrunch.com/2026/08/09/anthropic-is-turning-claude-codes-auto-mode-on-by-default/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T19:20:32+00:00",
    "summary": "Programming with Claude Code will soon require even less human oversight."
  },
  {
    "id": "rss:https://stratechery.com/2026/apple-earnings-more-on-amazons-earnings/",
    "domain": "大厂 AI 动态",
    "title": "Apple Earnings, More on Amazon’s Earnings",
    "url": "https://stratechery.com/2026/apple-earnings-more-on-amazons-earnings/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T10:00:00+00:00",
    "summary": "Apple's earnings (and stock) are limited not by memory but rather chip shortages; then, more on Amazon's earnings and Andy Jassy's market analysis."
  },
  {
    "id": "rss:https://arstechnica.com/gaming/2026/08/ars-live-ross-scott-discusses-the-stop-killing-games-movement/",
    "domain": "大厂 AI 动态",
    "title": "Ars Live: Ross Scott discusses the Stop Killing Games movement",
    "url": "https://arstechnica.com/gaming/2026/08/ars-live-ross-scott-discusses-the-stop-killing-games-movement/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T22:23:43+00:00",
    "summary": "Our discussion takes place live on August 11 at 3 pm ET."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/08/with-new-open-models-meta-pitches-another-reboot-of-its-struggling-ai-strategy/",
    "domain": "大厂 AI 动态",
    "title": "With new open models, Meta pitches another reboot of its struggling AI strategy",
    "url": "https://arstechnica.com/ai/2026/08/with-new-open-models-meta-pitches-another-reboot-of-its-struggling-ai-strategy/",
    "source": "Samuel Axon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T22:13:03+00:00",
    "summary": "Meta has been trailing competitors. Zuckerberg thinks he's found a way forward."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/08/trump-signs-bonkers-order-that-cuts-vaccines-promotes-ones-that-dont-exist/",
    "domain": "大厂 AI 动态",
    "title": "Trump signs bonkers order that cuts vaccines, promotes ones that don't exist",
    "url": "https://arstechnica.com/health/2026/08/trump-signs-bonkers-order-that-cuts-vaccines-promotes-ones-that-dont-exist/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T21:42:56+00:00",
    "summary": "Trump falsely claimed the MMR vaccine is \"quite lethal\" and linked shots to autism."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/08/players-lose-access-to-aliens-fireteam-elite-on-nintendo-switch-without-refunds/",
    "domain": "大厂 AI 动态",
    "title": "Developer Cold Iron Studios shuts down cloud version of $60 game with no refunds",
    "url": "https://arstechnica.com/gadgets/2026/08/players-lose-access-to-aliens-fireteam-elite-on-nintendo-switch-without-refunds/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T21:26:38+00:00",
    "summary": "A reminder of the perils of digital ownership."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/08/amazon-funds-biggest-gas-power-plant-in-us-despite-climate-pledge/",
    "domain": "大厂 AI 动态",
    "title": "Amazon backs power plant that may become top source of US climate pollution",
    "url": "https://arstechnica.com/tech-policy/2026/08/amazon-funds-biggest-gas-power-plant-in-us-despite-climate-pledge/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T20:45:52+00:00",
    "summary": "Amazon announces first off-the-grid data center in race to reap AI profits."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/08/zuckerbergs-super-yacht-stood-by-while-stranded-boaters-looked-for-help/",
    "domain": "大厂 AI 动态",
    "title": "Zuckerberg’s superyacht ignored emergency channel, failed to aid stranded boat",
    "url": "https://arstechnica.com/gadgets/2026/08/zuckerbergs-super-yacht-stood-by-while-stranded-boaters-looked-for-help/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T20:01:15+00:00",
    "summary": "Zuckerberg’s superyacht and support ship were slow to heed Coast Guard call."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/08/has-ford-got-cheap-car-fever-allegedly-a-25k-crossover-is-on-the-way/",
    "domain": "大厂 AI 动态",
    "title": "Has Ford got cheap car fever? A $25K crossover is supposedly on the way.",
    "url": "https://arstechnica.com/cars/2026/08/has-ford-got-cheap-car-fever-allegedly-a-25k-crossover-is-on-the-way/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T17:07:47+00:00",
    "summary": "Ford dealers were told about the new Escape-sized model; one of them spilled the beans."
  },
  {
    "id": "hn:48933344",
    "domain": "股票",
    "title": "SpaceX stock erases all its gains and slides below IPO price in intraday trading",
    "url": "https://www.latimes.com/business/story/2026-07-16/spacex-stock-erases-gains-slides-below-ipo-price-in-intraday-trading",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 314,
    "published_at": "2026-07-16T12:02:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:49122994",
    "domain": "股票",
    "title": "Situational Awareness down 67% in July in AI stock rout",
    "url": "https://www.wsj.com/finance/investing/situational-awareness-down-67-in-july-in-ai-stock-rout-cd19901f",
    "source": "pondsider",
    "platform": "hackernews",
    "points": 157,
    "published_at": "2026-07-31T13:37:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:48948435",
    "domain": "股票",
    "title": "Short sellers notch $8.7B profit as SpaceX shares dip to IPO price",
    "url": "https://www.reuters.com/business/media-telecom/short-sellers-rack-up-87-bln-profit-spacex-slips-below-ipo-price-ortex-2026-07-16/",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 168,
    "published_at": "2026-07-17T15:17:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:49166182",
    "domain": "股票",
    "title": "Bending Spoons makes first post-IPO acquisition with $1.3B Airtable deal",
    "url": "https://live.euronext.com/en/financial-news/bending-spoons-makes-first-post-ipo-acquisition-13-billion-airtable-deal",
    "source": "riffraff",
    "platform": "hackernews",
    "points": 115,
    "published_at": "2026-08-04T09:27:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:49151871",
    "domain": "股票",
    "title": "Situational Awareness and the Impending Stock Market Volatility",
    "url": "https://www.emergingtrajectories.com/lh/situational-awareness-bigger-picture/",
    "source": "cl42",
    "platform": "hackernews",
    "points": 71,
    "published_at": "2026-08-03T06:17:53+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3779143",
    "domain": "股票",
    "title": "AI杠杆、美债利率与霍尔木兹海峡--这个夏天主导全球市场的三大因素",
    "url": "https://wallstreetcn.com/articles/3779143",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T04:17:23+00:00",
    "summary": "这个夏天，AI杠杆爆仓、美债长端利率创19年新高、霍尔木兹停火协议反复撕裂——三件事表面独立，底层可能是同一件事：全球资本正在从过剩走向稀缺。AI需求仍在加速，但杠杆不可持续；美联储降息175bp，长端利率却不降反升；海峡定价从“一次性冲击”变为“持续风险折价”。7月的极端波动不是终点，是新范式的预演。"
  },
  {
    "id": "wscn:3779141",
    "domain": "股票",
    "title": "创业板盘中拉升涨超1%，CRO、创新药大涨，MLCC集体上涨，商业航天调整，恒科指跌超1%，科网股普跌",
    "url": "https://wallstreetcn.com/articles/3779141",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T04:04:23+00:00",
    "summary": "盘面上，个股跌多涨少，沪深京三市近3300股飘绿，上午半天成交1.53万亿。沪深两市半日成交额1.52万亿，较上个交易日缩量2153亿。板块方面，医药生物股持续发酵，CRO、创新药方向领涨；半导体材料、AI应用、光伏、算力租赁题材活跃。商业航天、黄金、工业金属、锂电池、大消费概念股走弱。"
  },
  {
    "id": "wscn:3779152",
    "domain": "股票",
    "title": "英国FCA筹备黄金代币化监管框架，伦敦力守全球金市龙头地位",
    "url": "https://wallstreetcn.com/articles/3779152",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T03:36:44+00:00",
    "summary": "英国金融行为监管局（FCA）正加速推进代币化黄金监管框架建设，已与多家大型银行展开磋商，预计数月内发布相关标准公告。核心议题包括代币化黄金作为批发市场抵押品的应用，以及如何在现有权限内覆盖监管盲区。此举背景下，伦敦占据全球约70%黄金交易份额，但面临被超越风险。"
  },
  {
    "id": "wscn:3779064",
    "domain": "股票",
    "title": "AI制药初探：200+药物分子进入临床试验，产业链上游开启三位数业绩大爆发",
    "url": "https://wallstreetcn.com/premium/articles/3779064?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T03:36:17+00:00",
    "summary": "全球AI制药市场规模预计将从2025年的约28亿美元增长至2035年的160-240亿美元（CAGR 23-27%），亚太地区正以27%以上的增速成为增长主引擎。"
  },
  {
    "id": "wscn:3779153",
    "domain": "股票",
    "title": "新美联储通讯社：沃什“嘴硬”也敌不过数据，两份通胀报告或决定9月加息命运",
    "url": "https://wallstreetcn.com/articles/3779153",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T03:32:27+00:00",
    "summary": "Nick Timiraos认为两份通胀数据即将成为新任美联储主席沃什的信誉大考。7月议息会议后，一场语焉不详的新闻发布会令市场罕见地在其发言期间推高长端国债收益率，内部异见票数攀升，信誉裂痕已现。核心CPI 0.2%是分水岭——数据偏热，他将陷入\"加息自证\"或\"沉默承压\"的两难；数据温和，才能在杰克逊霍尔重夺主动。"
  },
  {
    "id": "wscn:3779151",
    "domain": "股票",
    "title": "华为AI芯片来时的路",
    "url": "https://wallstreetcn.com/articles/3779151",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T03:28:18+00:00",
    "summary": "华为AI芯片之路是一场无路可退的极限突围。面对全面断供，华为“重新发明”一切，构建昇腾全栈底座，以系统级集群创新打破单芯片封锁。凭借“阿甘精神”的坚守，昇腾成功支撑DeepSeek等大模型，真正实现了中国AI算力的软硬协同与逆境重生。"
  },
  {
    "id": "wscn:3779129",
    "domain": "股票",
    "title": "Agent经济学拐点：AI Agent电脑操作小时成本已低于离岸人力外包，准确率也更高",
    "url": "https://wallstreetcn.com/articles/3779129",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T03:24:10+00:00",
    "summary": "AI Agent操控电脑的能力已在2026年越过两条关键红线：最优模型在标准桌面任务中完成率达85%，超越人类的72%；运行成本降至每小时6至8美元，低于印度离岸人力的10美元。技术与经济的双重拐点正在颠覆BPO市场，而真正的护城河已从\"谁的模型更强\"转移至\"谁更懂企业内部流程\"。"
  },
  {
    "id": "wscn:3779145",
    "domain": "股票",
    "title": "Meta开源最强AI模型，扎克伯格向OpenAI和Anthropic发起挑战",
    "url": "https://wallstreetcn.com/articles/3779145",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T03:13:26+00:00",
    "summary": "Meta宣布开源最强AI模型Muse Spark 1.2，并推出专为消费级设备设计的Muse Glimmer系列。CEO扎克伯格强调开源战略可填补市场空缺，对抗OpenAI、Anthropic等封闭式生态，并呼吁美国政策降低开源模型竞争壁垒。"
  },
  {
    "id": "wscn:3779150",
    "domain": "股票",
    "title": "百花奖里的AI短片，开始读懂导演语言了",
    "url": "https://wallstreetcn.com/articles/3779150",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T03:07:25+00:00",
    "summary": "AI生成的影像第一次有了进入百花奖的专属通道。\n8月8日，第38届大众电影百花奖AIGC推优单元在北..."
  },
  {
    "id": "wscn:3779144",
    "domain": "股票",
    "title": "联合干预之后谁来接棒：日本央行加息时机成为市场焦点",
    "url": "https://wallstreetcn.com/articles/3779144",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T03:06:39+00:00",
    "summary": "日元干预效果正迅速消退——从40年低位164反弹至155后，再次逼近160关口。问题的核心已从\"是否干预\"转向\"何时加息\"：欧洲央行被排除在协调机制之外，令联合干预公信力大打折扣；市场共识逐渐清晰，若无日本央行加息配合，任何汇率支撑都将昙花一现。9月还是12月？这场加息时机之争，正牵动全球套息交易的命运。"
  },
  {
    "id": "wscn:3779147",
    "domain": "股票",
    "title": "小牛电动二季度销量增长24%，规模回升后仍需面对盈利压力",
    "url": "https://wallstreetcn.com/articles/3779147",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T02:47:43+00:00",
    "summary": "当季净亏损1.02亿元。"
  },
  {
    "id": "wscn:3779146",
    "domain": "股票",
    "title": "九号公司上半年营收增长22%，两轮车业务进入规模扩张阶段",
    "url": "https://wallstreetcn.com/articles/3779146",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T02:46:01+00:00",
    "summary": "但扩张影响了利润。"
  },
  {
    "id": "wscn:3779134",
    "domain": "股票",
    "title": "NPO--CPO到来之前的“过渡方案”，国产算力的新战场？",
    "url": "https://wallstreetcn.com/articles/3779134",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T02:28:20+00:00",
    "summary": "近封装光学（NPO）作为可插拔模块与CPO之间的中间方案，凭借现场可更换、故障范围可控、制造良率较高三大优势，正在国内超节点建设加速背景下迎来产业化窗口。东北证券认为，国内厂商在硅光、精密耦合等领域积累可直接迁移，并重点推荐光引擎、高密度光连接、FAU、光源材料、先进封装及国产算力芯片六大投资方向。"
  },
  {
    "id": "wscn:3779142",
    "domain": "股票",
    "title": "巨头竞购OpenRouter，AI“路由层”走红",
    "url": "https://wallstreetcn.com/articles/3779142",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T02:24:23+00:00",
    "summary": "据报道，Stripe拟以百亿美元收购AI路由初创公司OpenRouter，引发Snowflake、Cloudflare等巨头竞相接触路由赛道。AI路由技术可在不同模型间智能调度任务，大幅压缩成本，因AI智能体爆发式增长及开源模型成熟而走红。众多初创公司两周内收到大量投资收购邀约。"
  },
  {
    "id": "wscn:3779135",
    "domain": "股票",
    "title": "MLCC持续涨价：一枝独秀还是重蹈存储的覆辙？",
    "url": "https://wallstreetcn.com/premium/articles/3779135?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T02:24:00+00:00",
    "summary": "这一轮MLCC行情，是2017年的复刻，还是存储史诗级牛市的镜像？"
  },
  {
    "id": "wscn:3779140",
    "domain": "股票",
    "title": "3个月狂砸600亿美元！Anthropic再签91亿算力大单，与比特币矿企Riot达成长约",
    "url": "https://wallstreetcn.com/articles/3779140",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T02:23:22+00:00",
    "summary": "Anthropic斥资91亿美元与比特币矿企Riot Platforms签署20年算力长约，供应191兆瓦算力，若行使延期选项总价值最高达161亿美元。这是Anthropic近月连签的第三笔巨额算力协议，三笔合计规模已超600亿美元。消息公布后，Riot股价盘后暴涨25%，其\"挖矿转AI\"的估值逻辑获市场强烈认可。"
  },
  {
    "id": "wscn:3779138",
    "domain": "股票",
    "title": "中国模型正“走出”价格战，“走向”智能战",
    "url": "https://wallstreetcn.com/articles/3779138",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T02:03:39+00:00",
    "summary": "摩根士丹利认为，中国大模型行业正经历从价格竞争到智能竞争的结构性转变：DeepSeek宣布大幅上调API价格，Kimi K3和Qwen3.8-Max以2.8万亿和2.4万亿参数进入大参数时代，开源模型授权条款也趋于收紧。这三重变化共同指向更健康的商业化环境：定价回归理性、变现路径拓宽、进入壁垒抬高。"
  },
  {
    "id": "wscn:3779139",
    "domain": "股票",
    "title": "OpenAI斥资70亿美元回购员工股份，估值8520亿美元静待上市窗口",
    "url": "https://wallstreetcn.com/articles/3779139",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T01:49:44+00:00",
    "summary": "OpenAI斥资70亿美元回购员工股份，估值锚定8520亿美元，且罕见地未引入任何外部投资者——资金全部来自自身资产负债表。此举不仅为员工IPO前提供套现通道，更被视为上市冲刺的明确信号。"
  },
  {
    "id": "wscn:3779136",
    "domain": "股票",
    "title": "瑞银企业调研：AI支出依旧强劲，“自建”软件已成趋势，数据管理层至关重要",
    "url": "https://wallstreetcn.com/articles/3779136",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T01:49:18+00:00",
    "summary": "企业AI投入正经历结构性转变：从\"烧token\"转向算ROI，但预算并未收缩。瑞银最新调研显示，云基础设施与数据管理层（Databricks、Snowflake）地位稳固，传统SaaS厂商却持续被冷落——企业普遍选择自建AI系统。与此同时，CodeRabbit等AI原生小厂正悄然切入采购清单，一场产业链分化已然开启。"
  },
  {
    "id": "wscn:3778941",
    "domain": "股票",
    "title": "从“化工品”到“认证材料”，AI服务器正在如何改写树脂行业？",
    "url": "https://wallstreetcn.com/premium/articles/3778941?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T01:48:01+00:00",
    "summary": "AI服务器进入Rubin迭代周期后，PCB正在从传统承载件升级为机柜级高速互连介质，高频高速覆铜板随之从M8向M9、M10演进。与铜箔、电子布相比，树脂未必是当前涨价最剧烈的材料，却可能是国产替代弹性最大的环节——PPO、碳氢树脂等供需趋紧，国产M9产品开始批量供货，新增产能又集中在三季度释放。当“认证、缺货、扩产、订单”同时出现，高频高速树脂是否正在从产业预期真正进入业绩兑现期？"
  },
  {
    "id": "hn:49092549",
    "domain": "股票",
    "title": "Chip stocks slide in US and Asia as AI jitters rattle investors",
    "url": "https://www.bbc.com/news/articles/cly8zng43npo",
    "source": "yogthos",
    "platform": "hackernews",
    "points": 74,
    "published_at": "2026-07-29T01:56:00+00:00",
    "summary": ""
  },
  {
    "id": "hn:49137024",
    "domain": "股票",
    "title": "Oil companies report sky-high profits thanks to wartime crude prices",
    "url": "https://www.npr.org/2026/07/31/nx-s1-5910660/big-oil-earnings-q2-2026",
    "source": "speckx",
    "platform": "hackernews",
    "points": 63,
    "published_at": "2026-08-01T18:28:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:48938001",
    "domain": "股票",
    "title": "SPCX is now Wall Street's most shorted new stock",
    "url": "https://invezz.com/news/2026/07/16/the-worlds-most-valuable-ipo-spcx-is-now-wall-streets-most-shorted-new-stock/",
    "source": "lbrito",
    "platform": "hackernews",
    "points": 81,
    "published_at": "2026-07-16T18:03:56+00:00",
    "summary": ""
  },
  {
    "id": "hn:49111879",
    "domain": "股票",
    "title": "Citadel Buys Situational Awareness's Stock Portfolio After Big Losses in AI",
    "url": "https://www.wsj.com/finance/citadel-buys-situational-awarenesss-stock-portfolio-after-big-losses-in-ai-5117159b",
    "source": "mudil",
    "platform": "hackernews",
    "points": 54,
    "published_at": "2026-07-30T16:00:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:48950580",
    "domain": "股票",
    "title": "SpaceX stock drops to a new low and loses $1T in value in a month",
    "url": "https://www.businessinsider.com/spacex-stock-drops-new-low-ipo-price-starship-launch-scrubbed-2026-7",
    "source": "01-_-",
    "platform": "hackernews",
    "points": 74,
    "published_at": "2026-07-17T18:26:02+00:00",
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
    "id": "hn:49087537",
    "domain": "股票",
    "title": "Chip stocks tumble as AI sell-off deepens",
    "url": "https://www.ft.com/content/f8c03b5b-e194-4236-82c3-389b6f5dd7ae",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 36,
    "published_at": "2026-07-28T17:54:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:48958985",
    "domain": "股票",
    "title": "Traders are increasingly betting against SpaceX just weeks after IPO",
    "url": "https://www.ft.com/content/2b96703d-440b-46db-8d86-9fff9ecc59d5",
    "source": "ethanhawksley",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-07-18T15:26:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:49162737",
    "domain": "股票",
    "title": "Palantir soars 12% on blowout quarter, with US commercial revenue soaring ~150%",
    "url": "https://www.cnbc.com/2026/08/03/palantir-pltr-earnings-q2-2026.html",
    "source": "gslin",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-08-03T23:36:32+00:00",
    "summary": ""
  },
  {
    "id": "hn:49136787",
    "domain": "股票",
    "title": "Reddit Stock Collapses 23% as AI Eats Away at User Growth",
    "url": "https://www.barchart.com/story/news/3584357/reddit-stock-collapses-23-as-ai-eats-away-at-user-growth",
    "source": "thm",
    "platform": "hackernews",
    "points": 29,
    "published_at": "2026-08-01T18:03:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:48984021",
    "domain": "股票",
    "title": "Mark Cuban: fight inequality by giving all workers company stock",
    "url": "https://fortune.com/2026/07/20/mark-cuban-income-inequality-company-stock-spacex-ipo-cost-plus-drugs/",
    "source": "01-_-",
    "platform": "hackernews",
    "points": 46,
    "published_at": "2026-07-20T19:52:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:49115139",
    "domain": "股票",
    "title": "Microsoft's $450B Jump Is Biggest in Stock Market History",
    "url": "https://www.bloomberg.com/news/articles/2026-07-30/microsoft-eyes-history-with-490-billion-pop-in-market-value",
    "source": "signatoremo",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-07-30T20:12:40+00:00",
    "summary": ""
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
    "id": "hn:48923343",
    "domain": "股票",
    "title": "SpaceX stock sinks below $135 IPO price for the first time",
    "url": "https://www.cnbc.com/2026/07/15/spacex-spcx-stock-ipo-price.html",
    "source": "abduhl",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-07-15T16:30:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:49081705",
    "domain": "股票",
    "title": "AI sell-off intensifies as investors ditch chip stocks",
    "url": "https://www.theguardian.com/business/2026/jul/28/ai-sell-off-chip-stocks-sk-hynix-samsung",
    "source": "lilerjee",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-07-28T10:08:46+00:00",
    "summary": ""
  },
  {
    "id": "hn:49114131",
    "domain": "股票",
    "title": "Citadel buys most of Situational's stock holdings after AI share rout",
    "url": "https://www.reuters.com/technology/citadel-buys-most-situationals-stock-holdings-after-ai-share-rout-sources-say-2026-07-30/",
    "source": "paulpauper",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-07-30T18:54:46+00:00",
    "summary": ""
  },
  {
    "id": "hn:49091512",
    "domain": "股票",
    "title": "Apple becomes second $5T company as investors flee AI stocks",
    "url": "https://www.theguardian.com/technology/2026/jul/28/apple-second-ever-5tn-company-as-investors-flee-ai-stocks",
    "source": "devonnull",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-07-28T23:41:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:49145809",
    "domain": "股票",
    "title": "As Reddit stock falls, CEO questions value of Google's AI Overviews",
    "url": "https://arstechnica.com/ai/2026/08/reddit-ceo-on-ai-overviews-were-still-looking-for-that-win-win/",
    "source": "Brajeshwar",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-08-02T16:09:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:49095568",
    "domain": "股票",
    "title": "Korean Stocks Plunge 16% in Two-Day Burst of Retail Selling",
    "url": "https://www.bloomberg.com/news/articles/2026-07-29/korean-stocks-tumble-a-second-day-as-sk-hynix-results-disappoint",
    "source": "emsidisii",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-07-29T10:25:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:49119293",
    "domain": "股票",
    "title": "Aschenbrenner's hedge fund forced to unwind all public stock positions",
    "url": "https://www.cnbc.com/2026/07/30/leopold-aschenbrenners-hedge-fund-is-facing-steep-ai-losses.html",
    "source": "akbabu",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-07-31T05:22:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:48899454",
    "domain": "股票",
    "title": "$65K to work at Anthropic? Debate ensues amid IPO wave",
    "url": "https://missionlocal.org/2026/07/anthropic-sf-affordability-ipo-housing-evictions-rent/",
    "source": "gcheong",
    "platform": "hackernews",
    "points": 30,
    "published_at": "2026-07-13T21:56:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:48889982",
    "domain": "股票",
    "title": "Xbox CEO Asha Sharma, who laid off 3,200 employees, to lead task force on jobs",
    "url": "https://www.pcgamer.com/gaming-industry/us-federal-reserve-taps-xbox-ceo-asha-sharma-who-just-laid-off-3-200-employees-to-lead-task-force-on-jobs/",
    "source": "robtherobber",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-07-13T09:27:08+00:00",
    "summary": ""
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
    "id": "hn:48915953",
    "domain": "金融",
    "title": "Stripe and Advent have made a joint offer to acquire PayPal – sources",
    "url": "https://www.reuters.com/business/finance/stripe-advent-offer-buy-paypal-more-than-53-billion-sources-say-2026-07-15/",
    "source": "rvz",
    "platform": "hackernews",
    "points": 494,
    "published_at": "2026-07-15T03:32:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:49175192",
    "domain": "金融",
    "title": "Thanks FedEx, This Is Why We Keep Getting Phished (2024)",
    "url": "https://www.troyhunt.com/thanks-fedex-this-is-why-we-keep-getting-phished/",
    "source": "stymaar",
    "platform": "hackernews",
    "points": 337,
    "published_at": "2026-08-04T21:09:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:49245487",
    "domain": "金融",
    "title": "Study links GLP-1 drugs to bigger jump in women's employment than a degree",
    "url": "https://finance.yahoo.com/healthcare/articles/harvard-study-links-glp-1-123000637.html",
    "source": "metadat",
    "platform": "hackernews",
    "points": 121,
    "published_at": "2026-08-10T16:02:34+00:00",
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
    "id": "hn:49245071",
    "domain": "金融",
    "title": "Force-Fed by ICE",
    "url": "https://www.theguardian.com/us-news/2026/aug/10/ice-force-feeding-detention-gabar-choli",
    "source": "HotGarbage",
    "platform": "hackernews",
    "points": 87,
    "published_at": "2026-08-10T15:35:44+00:00",
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
    "id": "hn:49046525",
    "domain": "金融",
    "title": "The Fedora 45 Sausage Factory",
    "url": "https://supakeen.com/weblog/the-fedora-45-sausage-factory/",
    "source": "6581",
    "platform": "hackernews",
    "points": 158,
    "published_at": "2026-07-25T11:04:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:49243531",
    "domain": "金融",
    "title": "China is now the world's greatest oil power",
    "url": "https://www.economist.com/finance-and-economics/2026/08/09/china-is-now-the-worlds-great-oil-power",
    "source": "bookofjoe",
    "platform": "hackernews",
    "points": 53,
    "published_at": "2026-08-10T13:40:46+00:00",
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
    "id": "rss:https://arxiv.org/abs/2608.07479",
    "domain": "金融",
    "title": "Marginally Useful: Formalizing the Information Gap in Conformal Prediction",
    "url": "https://arxiv.org/abs/2608.07479",
    "source": "Peter Cotton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T04:00:00+00:00",
    "summary": "arXiv:2608.07479v1 Announce Type: new Abstract: Conformal prediction gives finite-sample, distribution-free marginal coverage for a set. The guarantee is real, and it is often misread as evidence of f"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.07536",
    "domain": "金融",
    "title": "Yield Curve Prediction with Machine Learning: Forecasting Approaches and the Role of Macroeconomic Predictors",
    "url": "https://arxiv.org/abs/2608.07536",
    "source": "Jeron Tan Kang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T04:00:00+00:00",
    "summary": "arXiv:2608.07536v1 Announce Type: new Abstract: This paper compares direct-yield and factor-based approaches to U.S. Treasury yield curve forecasting using a common high-dimensional macroeconomic info"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.07588",
    "domain": "金融",
    "title": "Workplace dependence in urban economies",
    "url": "https://arxiv.org/abs/2608.07588",
    "source": "Zs\\'ofia Z\\'ador, Bal\\'azs Lengyel, Riccardo Di Clemente",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T04:00:00+00:00",
    "summary": "arXiv:2608.07588v1 Announce Type: new Abstract: Remote work has fundamentally reshaped urban economic life, and the spatial organisation of activity across cities. However, access to flexible work is "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.07690",
    "domain": "金融",
    "title": "On a Simple Relationship Between Order Imbalance, Skew and Width in Over-The-Counter Trading",
    "url": "https://arxiv.org/abs/2608.07690",
    "source": "Peter Cotton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T04:00:00+00:00",
    "summary": "arXiv:2608.07690v1 Announce Type: new Abstract: We consider a market maker who can only obtain and dispose of inventory by responding to a sequence of sealed-bid enquiries, and whose customers arrive "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.07709",
    "domain": "金融",
    "title": "Microstructural Foundation for the Rough Hawkes--Heston Model",
    "url": "https://arxiv.org/abs/2608.07709",
    "source": "Yingli Wang, Yinhao Wu, Lingjiong Zhu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T04:00:00+00:00",
    "summary": "arXiv:2608.07709v1 Announce Type: new Abstract: Hawkes-based microstructural foundations for rough volatility, leverage, and rough Heston-type limits were developed by El Euch et al. (2018, Finance St"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.07819",
    "domain": "金融",
    "title": "The friendship paradox: Causal evidence of its behavioral consequences",
    "url": "https://arxiv.org/abs/2608.07819",
    "source": "Gary Charness, Francesco Feri, Matthew O. Jackson, Miguel A. Melendez-Jimenez, Matthias Sutter",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T04:00:00+00:00",
    "summary": "arXiv:2608.07819v1 Announce Type: new Abstract: We provide a first causal analysis of the behavioral consequences of the friendship paradox-the fact that people's friends in a network have more connec"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.08197",
    "domain": "金融",
    "title": "Self-Explaining Segment Trees: A KPI-Conditioned Segmentation Framework for Business Analytics with Node-Level Explanation via Recursive Subspace Partitioning",
    "url": "https://arxiv.org/abs/2608.08197",
    "source": "Girish G N, Dhanashekar Kandaswamy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T04:00:00+00:00",
    "summary": "arXiv:2608.08197v1 Announce Type: new Abstract: Business users confronted with a moving metric need to know which part of their data moved and why. Existing data-explanation methods typically return p"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.08405",
    "domain": "金融",
    "title": "Robustness or Crowding: Experimental Design for Trading Strategy Capacity",
    "url": "https://arxiv.org/abs/2608.08405",
    "source": "Alejandro Rodriguez Dominguez, Miquel Noguer i Alonso",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T04:00:00+00:00",
    "summary": "arXiv:2608.08405v1 Announce Type: new Abstract: How much capital a trading strategy can absorb before its edge disappears is a causal question about how much is deployed, but it is answered with obser"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.08437",
    "domain": "金融",
    "title": "AI and the Research Team",
    "url": "https://arxiv.org/abs/2608.08437",
    "source": "Johan Fourie",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T04:00:00+00:00",
    "summary": "arXiv:2608.08437v1 Announce Type: new Abstract: Artificial intelligence is associated with larger research teams, yet in mathematics, among the most codifiable fields, individual researchers working w"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.08690",
    "domain": "金融",
    "title": "Price Responses of Rwandan Tungsten Exports under Conflict Minerals Regulation",
    "url": "https://arxiv.org/abs/2608.08690",
    "source": "Haruka Nagamori, Kazuhiko Nishimura",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T04:00:00+00:00",
    "summary": "arXiv:2608.08690v1 Announce Type: new Abstract: Section 1502 of the Dodd--Frank Act, enacted in 2010, requires U.S.-listed companies using tin, tantalum, tungsten, and gold (3TG) from the Democratic R"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.08851",
    "domain": "金融",
    "title": "Estimated Demand for Mega-Constellation Internet Service",
    "url": "https://arxiv.org/abs/2608.08851",
    "source": "Akhil Rao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T04:00:00+00:00",
    "summary": "arXiv:2608.08851v1 Announce Type: new Abstract: The near-term growth of the commercial space economy and sustainability of the low-Earth orbit (LEO) environment depends on the commercial prospects of "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.08900",
    "domain": "金融",
    "title": "High-Order Expansions of the Optimizer Map via Bell Polynomials",
    "url": "https://arxiv.org/abs/2608.08900",
    "source": "Oleksii Mostovyi, Thaleia Zariphopoulou",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T04:00:00+00:00",
    "summary": "arXiv:2608.08900v1 Announce Type: new Abstract: Completely monotonic inverse marginal (CMIM) utilities, introduced in [MSZ24], constitute a tractable class of preferences that includes many of the mos"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.08934",
    "domain": "金融",
    "title": "Political Power-Sharing, Firm Entry, and Economic Growth: Evidence from Multiple Elected Representatives",
    "url": "https://arxiv.org/abs/2608.08934",
    "source": "Harsha Dutta, Pulak Ghosh, Arkodipta Sarkar, Nishant Vats",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T04:00:00+00:00",
    "summary": "arXiv:2608.08934v1 Announce Type: new Abstract: We examine the effect of political power-sharing on local economic activity. This effect depends on the relative importance of the risks associated with"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.09188",
    "domain": "金融",
    "title": "When Cross-Venue Agreement Is Not Price Discovery: Disclosure Frontiers for 24/7 Equity-Perpetual Oracles",
    "url": "https://arxiv.org/abs/2608.09188",
    "source": "Donghwa Seo, Doohwi Cha, Seunghan Son, Juyeong Lee, Minjae Lee, Minsuk Sung",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T04:00:00+00:00",
    "summary": "arXiv:2608.09188v1 Announce Type: new Abstract: Crypto-listed equity perpetuals trade while the primary cash market is closed, yet still need a mark for margin, funding, and liquidation. We model the "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.09378",
    "domain": "金融",
    "title": "Scaling laws of Stablecoin Transactions: Evidence from USDT and USDC on the Ethereum blockchain",
    "url": "https://arxiv.org/abs/2608.09378",
    "source": "Kundan Mukhia, Sabat Rai, Vivek Shrivastav, Imran Ansari, Md. Nurujjaman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T04:00:00+00:00",
    "summary": "arXiv:2608.09378v1 Announce Type: new Abstract: Stablecoins have rapidly emerged as an important class of digital assets and a component of the digital financial ecosystem. Despite their growing impor"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.09456",
    "domain": "金融",
    "title": "Climate-Conditioned Cascade Modeling for Multi-Peril Reinsurance: Analysis and Controlled Numerical Applications",
    "url": "https://arxiv.org/abs/2608.09456",
    "source": "N. Karimi, E. Salavati, F. Shokrollahi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T04:00:00+00:00",
    "summary": "arXiv:2608.09456v1 Announce Type: new Abstract: Climate perils are linked through event ordering and state-dependent propagation, features not fully captured by joint loss distributions alone. This pa"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.09576",
    "domain": "金融",
    "title": "Anomaly detection in European cryptocurrency exchange-traded products",
    "url": "https://arxiv.org/abs/2608.09576",
    "source": "Julia Ko\\'nczal, Rafa{\\l} Po{\\l}ocza\\'nski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T04:00:00+00:00",
    "summary": "arXiv:2608.09576v1 Announce Type: new Abstract: Cryptocurrency exchange-traded products (ETPs) listed on European exchanges provide a regulated environment for studying intraday market anomalies. We s"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.09641",
    "domain": "金融",
    "title": "Lower spectrum of financial correlation matrices: a new perspective on market synchronization",
    "url": "https://arxiv.org/abs/2608.09641",
    "source": "Rosanna Grassi, Caterina Pastorino, Pierpaolo Uberti",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T04:00:00+00:00",
    "summary": "arXiv:2608.09641v1 Announce Type: new Abstract: In this paper we investigate the information content of the lower part of the spectrum of financial correlation matrices, as a source of information on "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.09642",
    "domain": "金融",
    "title": "Beyond headcount and human capital: The Effective Cognitive Population as a decomposable capacity unit for AI-era planning",
    "url": "https://arxiv.org/abs/2608.09642",
    "source": "Kwan Soo Shin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T04:00:00+00:00",
    "summary": "arXiv:2608.09642v1 Announce Type: new Abstract: National planning counts population, human capital, and artificial-intelligence preparedness in separate ledgers. Demographic accounting has advanced fr"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.09859",
    "domain": "金融",
    "title": "Nash Peer-to-Peer Insurance Bargaining under Price Fairness and Coalitional Stability",
    "url": "https://arxiv.org/abs/2608.09859",
    "source": "Tim J. Boonen, Wing Fung Chong, Kenneth Tsz Hin Ng, Tak Wa Ng",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T04:00:00+00:00",
    "summary": "arXiv:2608.09859v1 Announce Type: new Abstract: We study peer-to-peer (P2P) insurance contracting between a risk-averse P2P reinsurer and multiple risk-averse peers in an asymmetric Nash-bargaining fr"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.09882",
    "domain": "金融",
    "title": "Environmental and Economic Implications of Artificial Intelligence Data Centers in the United States",
    "url": "https://arxiv.org/abs/2608.09882",
    "source": "Johanna Bola\\~nos-Zu\\~niga, Alberto J. Lamadrid",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T04:00:00+00:00",
    "summary": "arXiv:2608.09882v1 Announce Type: new Abstract: In this study, we use electricity demand growth, cooling requirements, and backup system operation to evaluate the environmental and economic implicatio"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.07504",
    "domain": "金融",
    "title": "Innovating with Generative AI: A Human Bottleneck Framework",
    "url": "https://arxiv.org/abs/2608.07504",
    "source": "Julian De Freitas, Ayelet Israeli, Gideon Nave, Artem Timoshenko, Olivier Toubia",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T04:00:00+00:00",
    "summary": "arXiv:2608.07504v1 Announce Type: cross Abstract: We propose a human bottleneck perspective for understanding how generative AI transforms the innovation process. The central premise is that many cons"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.08299",
    "domain": "金融",
    "title": "Non-linear optimal stopping with Bermudan strategies: the infinite horizon case",
    "url": "https://arxiv.org/abs/2608.08299",
    "source": "Miryana Grigorova, Ohood Aldalbahi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T04:00:00+00:00",
    "summary": "arXiv:2608.08299v1 Announce Type: cross Abstract: In this paper, we consider an optimal stopping problem with infinite horizon, non-negative pay-offs and non-linear evaluations $\\rho_{S,\\tau}$ indexed"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.08625",
    "domain": "金融",
    "title": "Retained hidden excess generates memory in price-limited markets",
    "url": "https://arxiv.org/abs/2608.08625",
    "source": "Debraj Das",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T04:00:00+00:00",
    "summary": "arXiv:2608.08625v1 Announce Type: cross Abstract: The daily return of a stock is often restricted to an exchange-imposed band to curb extreme fluctuations. Any attempted price movement beyond this ban"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.08634",
    "domain": "金融",
    "title": "Can Open-Weight Models Compete on Financial Text Comprehension?",
    "url": "https://arxiv.org/abs/2608.08634",
    "source": "Jan Sp\\\"orer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T04:00:00+00:00",
    "summary": "arXiv:2608.08634v1 Announce Type: cross Abstract: Open-weight language models from Chinese AI labs caught up on benchmarks relative to proprietary frontier models in recent months. Yet their reliabili"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.08825",
    "domain": "金融",
    "title": "Hybrid Neural-Classical Correction for Frozen Time Series Foundation Models: A Comprehensive Ablation Study on High-Frequency Stock Prediction",
    "url": "https://arxiv.org/abs/2608.08825",
    "source": "Kasun Dewage, Suranadi De Silva, Shankhadeep Mondal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T04:00:00+00:00",
    "summary": "arXiv:2608.08825v1 Announce Type: cross Abstract: Foundation models for time series forecasting demonstrate impressive zero-shot generalization but often underperform on specialized domains such as hi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.09069",
    "domain": "金融",
    "title": "Telemetry and Concealment in Self-Adapting Generative AI: Logging Architecture, Adversarial Model Hiding, and the Limits of Detection",
    "url": "https://arxiv.org/abs/2608.09069",
    "source": "Sriram Nagaraj",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T04:00:00+00:00",
    "summary": "arXiv:2608.09069v1 Announce Type: cross Abstract: Model risk management (MRM) guidance assumes a static model lifecycle, in which models are developed, independently validated, and implemented without"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.09087",
    "domain": "金融",
    "title": "Joint Lyapunov Certificates for K-Agent Generative AI Governance: Stochastic Stability, Emergent Ensemble Risk, and Zero-Knowledge Governance Attestation",
    "url": "https://arxiv.org/abs/2608.09087",
    "source": "Sriram Nagaraj",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T04:00:00+00:00",
    "summary": "arXiv:2608.09087v1 Announce Type: cross Abstract: We develop a rigorous mathematical framework for the governance of systems of K self-adapting generative AI models under the principles of Model Risk "
  },
  {
    "id": "rss:https://arxiv.org/abs/2403.06150",
    "domain": "金融",
    "title": "Artificial Intelligence, Data and Competition",
    "url": "https://arxiv.org/abs/2403.06150",
    "source": "Zhang Xu, Mingsheng Zhang, Wei Zhao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T04:00:00+00:00",
    "summary": "arXiv:2403.06150v3 Announce Type: replace Abstract: This paper examines how data inputs shape competition among artificial intelligences (AIs) in pricing games. The dataset assigns labels to consumers"
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
    "id": "hn:49174369",
    "domain": "金融",
    "title": "Waymo CEO explains why Tesla’s camera-only self-driving falls short",
    "url": "https://electrek.co/2026/08/04/waymo-co-ceo-camera-only-self-driving-tesla/",
    "source": "theanonymousone",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-08-04T20:11:15+00:00",
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
    "points": 41,
    "published_at": "2026-08-05T15:24:38+00:00",
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
    "id": "hn:48884775",
    "domain": "金融",
    "title": "Storm clouds gather over America's financial supremacy",
    "url": "https://www.economist.com/finance-and-economics/2026/07/12/storm-clouds-gather-over-americas-financial-supremacy",
    "source": "pseudolus",
    "platform": "hackernews",
    "points": 70,
    "published_at": "2026-07-12T21:04:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:49082706",
    "domain": "金融",
    "title": "AI revenues are growing fast, but not fast enough",
    "url": "https://www.economist.com/finance-and-economics/2026/07/28/ai-revenues-are-growing-fast-but-not-fast-enough",
    "source": "vinni2",
    "platform": "hackernews",
    "points": 50,
    "published_at": "2026-07-28T12:19:54+00:00",
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
  }
]
```
