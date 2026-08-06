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

- 今日日期：`2026-08-06`
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
  "date": "2026-08-06",
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
    "points": 1668895,
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
    "points": 1574080,
    "published_at": "2026-03-14T14:22:56+00:00",
    "summary": "AI 核心概念大串联：LLM, Token, Context, Context Window, Prompt, User Prompt, System Prompt, Tool, MCP, Agent, Agent Skill，一期视频带你打通 AI 底层逻辑！"
  },
  {
    "id": "bvid:BV1j9MP6wEV9",
    "domain": "AI",
    "title": "从零开始，学会让桌面Agent帮你干活！【小白教程】",
    "url": "http://www.bilibili.com/video/av116861865887789",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 1313091,
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
    "points": 1057408,
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
    "points": 1010947,
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
    "points": 943230,
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
    "points": 670126,
    "published_at": "2025-05-01T04:00:00+00:00",
    "summary": "相信你已经在网上刷到过不少的 AI 工具，但如果你让我推荐最值得我们每个人学习的一款 AI 工具，那绝对就是史上最强的 AI 编程工具 —— Cursor。为此，我们录制了一个保姆级的 Cursor 新手教程，在这里免费分享给大家。即使你是一个对 AI 完全 0 基础的新手小白，看完这个视频后，你也可以彻底了解 Cursor 这个软件，并知道如何从 0 到 1 用 Cursor 做出入门级的 AI"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 597160,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 493862,
    "published_at": "2026-07-01T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260701\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\nAI大模型开发热门教程：\nAI大模型开发：BV1h1"
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 434060,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 425106,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1AnQNYxEsy",
    "domain": "AI",
    "title": "MCP是啥？技术原理是什么？一个视频搞懂MCP的一切。Windows系统配置MCP，Cursor Cline使用MCP",
    "url": "http://www.bilibili.com/video/av114155298228756",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 419631,
    "published_at": "2025-03-13T13:18:09+00:00",
    "summary": "MCP是近期的AI领域的热点，特别是在海外社区获得热烈讨论，每天都有大量MCP工具诞生。本期视频我们从MCP的概念，技术原理，到多场景实战，一个视频看懂MCP的全部内容。\n\n\nMCP官方开源仓库：https://github.com/modelcontextprotocol/servers\nMCP合集网站：  https://smithery.ai/\nVscode下载：https://code.v"
  },
  {
    "id": "bvid:BV1eK5DzHEWu",
    "domain": "AI",
    "title": "MCP实战指南，mcp视频教程，2小时学透mcp",
    "url": "http://www.bilibili.com/video/av114380213586544",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 393082,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1nkXkYfEfF",
    "domain": "AI",
    "title": "零基础也能用AI编程!豆包电脑版让你3分钟做出实用工具",
    "url": "http://www.bilibili.com/video/av114200730933577",
    "source": "花叔v",
    "platform": "bilibili",
    "points": 384786,
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
    "points": 257733,
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
    "points": 224071,
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
    "points": 212412,
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
    "points": 178565,
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
    "points": 168387,
    "published_at": "2026-07-31T12:42:57+00:00",
    "summary": "🚀DeepSeek v4 flash全面实测：Claude Code接入后连续开发7个项目，真的已经接近Claude Opus 4.8了吗？最便宜的国产模型！性能、速度与真实短板全曝光！对比Kimi K3后优点和缺点都藏不住了\n\nDeepSeek 发布了 DeepSeek V4 Flash 0731：284B 总参数、13B 激活参数、100 万 Token 上下文，官方基准表现接近 Claude"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 140177,
    "published_at": "2026-04-27T08:51:41+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n   喜欢视频课程的同学一键三连多多支持一下，长按点赞五秒=lv6大佬 可以的发送彩色弹幕哦。\n配套源码项目已打包评论区回复up"
  },
  {
    "id": "bvid:BV1g49KBqE1g",
    "domain": "AI",
    "title": "【Java+大模型】Java AI Agent✚Spring AI✚Spring AI Alibaba Agent Framework整体结构✚Skill！",
    "url": "http://www.bilibili.com/video/av116339758860081",
    "source": "图灵官方",
    "platform": "bilibili",
    "points": 122108,
    "published_at": "2026-04-03T08:15:24+00:00",
    "summary": "整理制作不易，大家记得点个关注，一键三连呀【点赞、收藏、转发】感谢支持~\n配套大模型笔记/AI大模型学习大纲/面试真题自取：https://www.bilibili.com/read/cv39638062/?spm_id_from=333.1387.0.0&amp;jump_opus=1"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 120699,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1EVuqzrEMJ",
    "domain": "AI",
    "title": "【保姆级教程】手把手教你低成本制作AI女友，【一定要看置顶评论】，可随身携带，自由对话",
    "url": "http://www.bilibili.com/video/av114851468812000",
    "source": "往生堂研发",
    "platform": "bilibili",
    "points": 112070,
    "published_at": "2025-07-14T12:03:53+00:00",
    "summary": "文档地址\nhttps://github.com/xinnan-tech/xiaozhi-esp32-server/blob/main/docs/Deployment.md?_refluxos=a10#%E6%96%B9%E5%BC%8F%E4%B8%80docker%E5%8F%AA%E8%BF%90%E8%A1%8Cserver"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 93019,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1khMX63EjU",
    "domain": "AI",
    "title": "Vibe Coding竞赛，Claude遗憾落败?",
    "url": "http://www.bilibili.com/video/av117030980230736",
    "source": "GenJi是真想教会你",
    "platform": "bilibili",
    "points": 80191,
    "published_at": "2026-08-05T10:30:00+00:00",
    "summary": "我和源宝打了个赌：半天时间，vibe coding一个活动社交App，看谁做的更好？最后Claude Code居然遗憾落败？这期视频，我们将用秒哒手把手带你走完，从一个简单的想法到App上架应用商店的全套流程！开发过程又发生了哪些趣事？一起来看看～"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 57435,
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
    "points": 53675,
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
    "points": 47560,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1W2Ts6YEXW",
    "domain": "AI",
    "title": "AI大模型+网络安全零基础入门全套教程：从Agent选型到AI挖洞全流程！AI挖洞提示词|AI解CTF题|AI审计代码|SRC挖洞|CS渗透|kali-码士集团",
    "url": "http://www.bilibili.com/video/av116854601286698",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 40731,
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
    "points": 39960,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 34032,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV16ggC6DEZK",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116963049212769",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 27584,
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
    "points": 22688,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV188UHYkEdg",
    "domain": "AI",
    "title": "Cursor / Windsurf + Android Studio 高效AI编程：零基础也能开发安卓应用",
    "url": "http://www.bilibili.com/video/av113502647750313",
    "source": "kate人不错",
    "platform": "bilibili",
    "points": 21122,
    "published_at": "2024-11-18T07:04:36+00:00",
    "summary": "欢迎关注我的知识星球：https://t.zsxq.com/FF0He\n\n我会分享最新AI资讯、源代码、回答你的提问。\n\n视频亮点：\n\n双工具对比：解析 Cursor 和 Windsurf 各自优势\n实战案例：从五子棋到卡路里计算AI应用的完整开发过程\n专业部署：Android Studio 配置与构建技巧\n\n时间戳：\n\n0:00 - 引言\n\n0:26 - 我开发的应用演示\n\n2:33 - Rea"
  },
  {
    "id": "bvid:BV1C3jt64EPS",
    "domain": "AI",
    "title": "B站讲的最好的Vibe Coding企业级项目实战教程（2026最新版）从入门到进阶，七天速通Claude Code+Codex+CursorAI工程化编程开发",
    "url": "http://www.bilibili.com/video/av116787425383675",
    "source": "图灵学院诸葛",
    "platform": "bilibili",
    "points": 20397,
    "published_at": "2026-06-21T09:48:04+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n 【本视频笔记代码、大模型最新学习路线、系统学习课程、实战案例、电子书+问题解答等戳这里获取→https://www.bilibili.com/read/cv39576966/?jump_opus=1】"
  },
  {
    "id": "bvid:BV15hNq6LE6V",
    "domain": "AI",
    "title": "7月最新Claude防封号最安全的！注册+订阅充值教程！A畜看到直接腿软，大喊完蛋了，随后呜呼",
    "url": "http://www.bilibili.com/video/av116923035617928",
    "source": "hjhjljkn",
    "platform": "bilibili",
    "points": 19771,
    "published_at": "2026-07-15T09:16:34+00:00",
    "summary": "AI充值站：njzqhy.top"
  },
  {
    "id": "bvid:BV1Z5KU6UExC",
    "domain": "AI",
    "title": "【吴恩达2026】Vibe Coding保姆级教程，手把手从环境搭建到工作流完整闭环！——DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116951003242391",
    "source": "吴恩达AIAgent",
    "platform": "bilibili",
    "points": 19467,
    "published_at": "2026-07-20T07:01:13+00:00",
    "summary": "本套课专门解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1dsNv66E3Q",
    "domain": "AI",
    "title": "【Cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av116922599344955",
    "source": "六月要癫",
    "platform": "bilibili",
    "points": 18394,
    "published_at": "2026-07-15T06:39:18+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1gf3T6KEef",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Vibe Coding】教程！从环境搭建到工作流完整闭环，一套全解决！DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116979708990688",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 18351,
    "published_at": "2026-07-25T08:47:37+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 18170,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1YGKJ6tEdz",
    "domain": "AI",
    "title": "Vibe Coding我的赛博女友",
    "url": "http://www.bilibili.com/video/av116933101950817",
    "source": "天工开帧",
    "platform": "bilibili",
    "points": 13632,
    "published_at": "2026-07-17T09:50:00+00:00",
    "summary": "Vibe Coding大赏之赛博女友。总体花费100个馒头左右，由于显存限制，目前实时数字人的版本没办法跑起来。目前可以24挂着，随时对话随时打断。作用嘛，除了聊天就是在我忙的时候顺手帮我查个东西。未来开发方向接入pi-agent，让它真正干活，当然，只是得上qwen27B以上得模型才有可用性。也就是说所有模型显存开销打底得36G以上。囧。当然如果不要无限制，可以接入在线模型或在线TTS，但是，我"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operitAI教程：入门安卓最强大ai平台",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 11819,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1Qt3B6oESF",
    "domain": "AI",
    "title": "开源赛博女友 AI的她 codex复现    本地部署  16g显存可运行",
    "url": "http://www.bilibili.com/video/av116998935676747",
    "source": "Penpos",
    "platform": "bilibili",
    "points": 10891,
    "published_at": "2026-07-28T18:09:30+00:00",
    "summary": "动态视频生成 地址：runninghub.ai/ai-detail/2082088529447321601?inviteCode=rh-v1118\n一键包地址 ：https://e5fklqa5fj.feishu.cn/wiki/ZPFIwAWzfiDilAkcHk0czuiRnhf"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 9292,
    "published_at": "2025-04-14T02:30:00+00:00",
    "summary": "MCP服务网站：https://smithery.ai/\nCherry Studio官方网站：https://cherry-ai.com/"
  },
  {
    "id": "bvid:BV1mtGK6hEKC",
    "domain": "AI",
    "title": "Deepseek V4 Flash最新测评！Claude Code版！",
    "url": "http://www.bilibili.com/video/av117015578676037",
    "source": "AI产品狙击手",
    "platform": "bilibili",
    "points": 8611,
    "published_at": "2026-07-31T16:41:51+00:00",
    "summary": "上期完成 DeepSeek V4 Flash 在 Codex 平台测评，本期统一拉满 High 思考深度接入 Claude Code 复测，用全套标准化用例横向对比模型真实表现，基础指令、24 点运算、密码锁逻辑推理全部答对，仅十条顺序句子存在单句通顺度瑕疵；代码生成环节暴露统一痛点，所有大型开发任务耗时动辄数十分钟，判断是新模型上线调用高峰算力拥堵导致，自制桌面操作系统成品完整性不及 Codex"
  },
  {
    "id": "bvid:BV14uTM69EUd",
    "domain": "AI",
    "title": "破甲claude/减少claude道德约束/ai破解卡密",
    "url": "http://www.bilibili.com/video/av116826918880943",
    "source": "去码头整点海鸥啊",
    "platform": "bilibili",
    "points": 8342,
    "published_at": "2026-06-28T09:05:03+00:00",
    "summary": "企鹅交流群：1038830654"
  },
  {
    "id": "bvid:BV12MEg6pE9o",
    "domain": "AI",
    "title": "【乐鑫教程】乐鑫文档 MCP 服务器上线，现已支持微信登录！",
    "url": "http://www.bilibili.com/video/av116713957956440",
    "source": "乐鑫信息科技",
    "platform": "bilibili",
    "points": 8240,
    "published_at": "2026-06-08T10:17:31+00:00",
    "summary": "手把手教你如何使用最新乐鑫文档知识库，帮你在 Claude / Cursor 等平台解答问题、生成代码、迁移 ESP-IDF 版本、烧录固件。 MCP 服务器现已支持微信扫码一键登录，快来一试！\n\n视频重点内容包括👇：\n\n- 如何将 MCP 服务器添加到 VS Code\n- 让 Copilot 基于乐鑫文档对比旧版和最新版 I2C 驱动\n- 驱动迁移\n- Copilot 编译代码、烧录代码并监控输"
  },
  {
    "id": "bvid:BV15H37zHE7Q",
    "domain": "AI",
    "title": "开源小智服务器xiaozhi-server自动更新以及最新版本MCP接入点配置保姆教程",
    "url": "http://www.bilibili.com/video/av114794426270759",
    "source": "毕乐labs",
    "platform": "bilibili",
    "points": 7527,
    "published_at": "2025-07-04T10:13:51+00:00",
    "summary": "更新过程中遇到xiaozhi-server无法启动的问题，是因为最新的配置有更新，视频中有展示如何解决。对大家有帮助的话请关注up主~"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 7503,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
  },
  {
    "id": "bvid:BV1QU6GYFEio",
    "domain": "AI",
    "title": "[课程4] 用Cursor开发数据库真的很简单 | Agent应用 | 用Codebase解决跨文件错误",
    "url": "http://www.bilibili.com/video/av113742109021318",
    "source": "Zhu的AI日记",
    "platform": "bilibili",
    "points": 7014,
    "published_at": "2024-12-31T12:30:00+00:00",
    "summary": "***这是全网最完整的分享如何在不懂编程的情况下，利用结构化思维，用Cursor开发商业app的系列课程。\n《懒人记单词》是基于艾宾浩斯遗忘曲线设计的记单词神器，它可以对每一个单词进行人性化的解读，并在每一个遗忘周期到来时及时提醒，并通过单词释义选择，拼写和造句进行全方位的巩固，同时AI还能对你的句子进行多维度的评估，确保你对每一个单词不仅会认，而且会用。\n\n***你将在本视频中学到：\n1.数据库"
  },
  {
    "id": "hn:49035303",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia, Microsoft, Meta warn against overregulating open-weight models",
    "url": "https://www.cnbc.com/2026/07/24/nvidia-microsoft-meta-open-weight-ai-models.html",
    "source": "louiereederson",
    "platform": "hackernews",
    "points": 659,
    "published_at": "2026-07-24T13:32:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:49034868",
    "domain": "AI 算力 / 半导体",
    "title": "Half-Life 2 running natively on HaikuOS",
    "url": "https://discuss.haiku-os.org/t/haiku-nvidia-porting-nvidia-driver-for-turing-gpus/16520?page=18",
    "source": "m0do1",
    "platform": "hackernews",
    "points": 339,
    "published_at": "2026-07-24T12:53:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:49189234",
    "domain": "AI 算力 / 半导体",
    "title": "NVIDIA’s Vera Whitepaper Has a Thread Loose",
    "url": "https://chipsandcheese.com/p/nvidias-vera-whitepaper-has-a-thread",
    "source": "pella",
    "platform": "hackernews",
    "points": 112,
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
    "id": "hn:49035751",
    "domain": "AI 算力 / 半导体",
    "title": "Open Weights and American AI Leadership [pdf]",
    "url": "https://images.nvidia.com/pdf/Open-Weights-and-American-AI-Leadership.pdf",
    "source": "lairv",
    "platform": "hackernews",
    "points": 112,
    "published_at": "2026-07-24T13:58:12+00:00",
    "summary": ""
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
    "id": "hn:49071512",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's $750B in Deals Reignite Circular AI Fears",
    "url": "https://www.bloomberg.com/news/articles/2026-07-27/nvidia-s-750-billion-deals-revive-fear-of-ai-circular-financing",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 81,
    "published_at": "2026-07-27T16:02:00+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/samsung-lays-out-ai-memory-roadmap/",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung Lays Out AI Memory Roadmap",
    "url": "https://www.eetimes.com/samsung-lays-out-ai-memory-roadmap/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T21:35:58+00:00",
    "summary": "Samsung bets on zHBM and zNAND-O to smash AI’s memory wall, promising 8× HBM5 performance and 3D stacks. The post Samsung Lays Out AI Memory Roadmap appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/safeguarding-fab-throughput-with-ai-augmented-data-insights/",
    "domain": "AI 算力 / 半导体",
    "title": "Safeguarding Fab Throughput with AI-Augmented Data Insights",
    "url": "https://www.eetimes.com/safeguarding-fab-throughput-with-ai-augmented-data-insights/",
    "source": "Alessandro Chimera, Industry Solutions Lead, Spotfire",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T13:00:00+00:00",
    "summary": "Discover how a Al-infused visual analytics platform empower engineers to solve complex manufacturing challenges for faster root cause analysis. The post Safeguarding Fab Throughput with AI-Augmented D"
  },
  {
    "id": "rss:https://www.eetimes.com/unstacking-the-future-navigating-the-3d-ic-frontier/",
    "domain": "AI 算力 / 半导体",
    "title": "Unstacking the Future: Navigating the 3D IC Frontier",
    "url": "https://www.eetimes.com/unstacking-the-future-navigating-the-3d-ic-frontier/",
    "source": "Piyush Sancheti, VP Central Engineering Solutions (3D IC), and Todd Burkholder, 3D IC Technology Writer, Siemens EDA",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T13:00:00+00:00",
    "summary": "3D IC introduces new system-level hurdles that demand innovative 3D IC solutions that address exploration, design, analysis, reliability, and test. The post Unstacking the Future: Navigating the 3D IC"
  },
  {
    "id": "rss:https://www.eetimes.com/neuromorphic-insect-eye-for-physical-ai/",
    "domain": "AI 算力 / 半导体",
    "title": "Insect-Inspired Neuromorphic Sensor Targets Physical AI",
    "url": "https://www.eetimes.com/neuromorphic-insect-eye-for-physical-ai/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T12:30:00+00:00",
    "summary": "Neuromorphic engineering could address the latency and power limitations of conventional cameras. The post Insect-Inspired Neuromorphic Sensor Targets Physical AI appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/electronica-2026-electronics-as-the-basis-of-the-all-electric-society/",
    "domain": "AI 算力 / 半导体",
    "title": "electronica 2026: Electronics as the Basis of the All-Electric Society",
    "url": "https://www.eetimes.com/electronica-2026-electronics-as-the-basis-of-the-all-electric-society/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T07:30:00+00:00",
    "summary": "electronica 2026 puts chips, AI, energy efficiency, and cyber resilience at the heart of the all-electric society. The post electronica 2026: Electronics as the Basis of the All-Electric Society appea"
  },
  {
    "id": "rss:https://www.eetimes.com/automotive-cybersecurity-ai-attack-surfaces-grow/",
    "domain": "AI 算力 / 半导体",
    "title": "Automotive Cybersecurity: AI Attack Surfaces Grow",
    "url": "https://www.eetimes.com/automotive-cybersecurity-ai-attack-surfaces-grow/",
    "source": "Egil Juliussen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T22:00:00+00:00",
    "summary": "AI and software-defined cars turn APIs, servers, and chargers into hacker playgrounds; see why automakers must harden fleets now. The post Automotive Cybersecurity: AI Attack Surfaces Grow appeared fi"
  },
  {
    "id": "rss:https://www.eetimes.com/jamie-urquhart-1957-2026-friendly-supportive-right-to-the-end/",
    "domain": "AI 算力 / 半导体",
    "title": "Jamie Urquhart (1957-2026): Friendly, Supportive, Right to the End",
    "url": "https://www.eetimes.com/jamie-urquhart-1957-2026-friendly-supportive-right-to-the-end/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T17:33:32+00:00",
    "summary": "Arm co-founder Jamie Urquhart backed chips, startups, and people to the end—read how his quiet force shaped an industry. The post Jamie Urquhart (1957-2026): Friendly, Supportive, Right to the End app"
  },
  {
    "id": "rss:https://www.eetimes.com/new-space-power-computing-and-thermal-challenges-beyond-earth/",
    "domain": "AI 算力 / 半导体",
    "title": "New Space: Power, Computing and Thermal Challenges Beyond Earth",
    "url": "https://www.eetimes.com/new-space-power-computing-and-thermal-challenges-beyond-earth/",
    "source": "EE Times Staff",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T14:48:24+00:00",
    "summary": "New Space explores the technologies reshaping the commercial space economy. The post New Space: Power, Computing and Thermal Challenges Beyond Earth appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/protecting-military-ai-agents-from-cyberthreats/",
    "domain": "AI 算力 / 半导体",
    "title": "Protecting Military AI Agents From Cyberthreats",
    "url": "https://www.eetimes.com/protecting-military-ai-agents-from-cyberthreats/",
    "source": "Liam Critchley",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T07:36:29+00:00",
    "summary": "Military AI faces hackers, poisoned data, and weak rules; lock it down with zero trust, red-teaming, and real governance. The post Protecting Military AI Agents From Cyberthreats appeared first on EE "
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/xbox/microsoft-wants-the-next-gen-xbox-helix-to-play-every-xbox-game-ever-made-as-it-urges-publishers-to-opt-in-new-report-also-claims-xbox-360-games-coming-to-pc-soon",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft wants the next-gen Xbox Helix to play every Xbox game ever made as it urges publishers to opt in — New report also claims Xbox 360 games coming to PC soon",
    "url": "https://www.tomshardware.com/video-games/xbox/microsoft-wants-the-next-gen-xbox-helix-to-play-every-xbox-game-ever-made-as-it-urges-publishers-to-opt-in-new-report-also-claims-xbox-360-games-coming-to-pc-soon",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T14:51:31+00:00",
    "summary": "The upcoming Xbox Helix is starting to feel more like a PC than any console before, and Microsoft's latest efforts to unite all Xbox generations under one roof, according to a new leaked memo, seem to"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/usd4-429-order-for-a-rog-astral-rtx-5090-cancelled-by-nvidia-due-to-a-late-price-increase-with-asus-blamed-marketplace-buyer-refunded-after-immediate-usd500-increase-with-top-spec-gpu-now-almost-2-5x-higher-than-msrp",
    "domain": "AI 算力 / 半导体",
    "title": "$4,429 order for a ROG Astral RTX 5090 cancelled by Nvidia due to a 'late' price increase, with Asus blamed — marketplace buyer refunded after immediate $500 increase, with top-spec GPU now almost 2.5",
    "url": "https://www.tomshardware.com/pc-components/gpus/usd4-429-order-for-a-rog-astral-rtx-5090-cancelled-by-nvidia-due-to-a-late-price-increase-with-asus-blamed-marketplace-buyer-refunded-after-immediate-usd500-increase-with-top-spec-gpu-now-almost-2-5x-higher-than-msrp",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T14:48:13+00:00",
    "summary": "Nvidia cancelled a Redditor's Asus ROG Astral RTX 5090 BTF GPU order, originally priced at $4,429, because of a $500 price rise, with Nvidia blaming Asus for the confusion."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/chinas-cxmt-targets-30-percent-dram-memory-market-share-by-2030-with-sixth-mega-fab-future-plans-bottlenecked-by-access-to-advanced-chipmaking-tools",
    "domain": "AI 算力 / 半导体",
    "title": "China's CXMT targets 30% DRAM memory market share by 2030 with sixth mega-fab — future plans bottlenecked by access to advanced chipmaking tools",
    "url": "https://www.tomshardware.com/pc-components/dram/chinas-cxmt-targets-30-percent-dram-memory-market-share-by-2030-with-sixth-mega-fab-future-plans-bottlenecked-by-access-to-advanced-chipmaking-tools",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T14:31:50+00:00",
    "summary": "ChangXin Memory Technologies (CXMT) began considering building its sixth DRAM fab in China to boost memory output in the coming years. If all announced projects proceed as planned, the company's produ"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/microsoft-quietly-purges-32gb-of-ram-recommendations-from-its-website-company-reels-from-the-effects-of-the-memory-shortage-as-it-released-8gb-base-models-for-surface-laptops-this-year",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft quietly purges 32GB of RAM recommendations from its website — company reels from the effects of the memory shortage as it released 8GB base models for Surface laptops this year",
    "url": "https://www.tomshardware.com/software/windows/microsoft-quietly-purges-32gb-of-ram-recommendations-from-its-website-company-reels-from-the-effects-of-the-memory-shortage-as-it-released-8gb-base-models-for-surface-laptops-this-year",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T13:12:34+00:00",
    "summary": "Microsoft once recommended 32GB of RAM as a future-proof \"no worries\" upgrade for gamers, but it seems that it wants you to forget that it ever gave that suggestion. That's because laptop manufacturer"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/score-all-the-essentials-of-a-great-gaming-pc-for-only-usd983-98-usd155-savings-nets-9800x3d-1tb-samsung-9100-ssd-16gb-of-ddr5-ram-asus-b850-motherboard-and-free-msi-aio",
    "domain": "AI 算力 / 半导体",
    "title": "Score all the essentials of a great gaming PC for only $983.98 — $155 savings nets 9800X3D, 1TB Samsung 9100 SSD, 16GB of DDR5 RAM, Asus B850 motherboard, and free MSI AIO",
    "url": "https://www.tomshardware.com/pc-components/score-all-the-essentials-of-a-great-gaming-pc-for-only-usd983-98-usd155-savings-nets-9800x3d-1tb-samsung-9100-ssd-16gb-of-ddr5-ram-asus-b850-motherboard-and-free-msi-aio",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T12:01:51+00:00",
    "summary": "Save $155 on this 4-item Newegg Gaming PC Combo - $983 buys 9800X3D, Samsung's blazing fast 1TB 9100 Pro SSD, 16GB of RAM, and Asus B850 motherboard"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/us-military-gps-jamming-exercise-suspected-of-contributing-to-civilian-plane-crash-in-new-mexico-medevac-flight-lost-signal-before-flying-into-a-mountain-killing-everyone-onboard",
    "domain": "AI 算力 / 半导体",
    "title": "US military GPS jamming exercise suspected of contributing to civilian plane crash in New Mexico — medevac flight lost signal before flying into a mountain, killing everyone onboard",
    "url": "https://www.tomshardware.com/tech-industry/us-military-gps-jamming-exercise-suspected-of-contributing-to-civilian-plane-crash-in-new-mexico-medevac-flight-lost-signal-before-flying-into-a-mountain-killing-everyone-onboard",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T12:00:16+00:00",
    "summary": "A medevac flight in New Mexico suffered from GPS interference due to activities by nearby U.S. military units. Although it didn't directly cause the plane to crash, it added to the stress and workload"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/elon-musk-says-spacex-will-exclusively-use-nvidia-gpus-because-they-are-the-best-says-optimized-vera-rubin-nvl72-will-be-launched-into-space-next-year",
    "domain": "AI 算力 / 半导体",
    "title": "Elon Musk says SpaceX will exclusively use Nvidia GPUs 'because they are the best' — says optimized Vera Rubin NVL72 will be launched into space next year",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/elon-musk-says-spacex-will-exclusively-use-nvidia-gpus-because-they-are-the-best-says-optimized-vera-rubin-nvl72-will-be-launched-into-space-next-year",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T11:50:34+00:00",
    "summary": "Elon Musk's SpaceX and xAI will exclusive use Nvidia AI accelerators for training and inference as companies believe Vera Rubin is the best AI compute architecture available today."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/huge-usd750-saving-makes-this-gigabyte-oled-gaming-laptop-with-an-rtx-5070-ti-an-absolute-steal-right-now-just-usd1-999-for-1600p-rig-with-32gb-ddr5-1tb-ssd-and-a-24-core-intel-cpu",
    "domain": "AI 算力 / 半导体",
    "title": "Huge $750 saving makes this Gigabyte OLED gaming laptop with an RTX 5070 Ti an absolute steal right now — just $1,999 for 1600p rig with 32GB DDR5, 1TB SSD, and a 24-core Intel CPU",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/huge-usd750-saving-makes-this-gigabyte-oled-gaming-laptop-with-an-rtx-5070-ti-an-absolute-steal-right-now-just-usd1-999-for-1600p-rig-with-32gb-ddr5-1tb-ssd-and-a-24-core-intel-cpu",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T11:06:29+00:00",
    "summary": "Save $750.99 on this powerhouse Gigabyte Aorus Master OLED gaming laptop with an RTX 5070 Ti and 32GB DDR5 for $1,999."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/liquid-cooling/frore-claims-its-liquidjet-can-drop-nvidia-rubin-gpu-temperatures-by-10-c-can-also-boost-performance-by-15-percent-as-hyperscalers-eye-using-delidded-gpus-in-production-environments",
    "domain": "AI 算力 / 半导体",
    "title": "Frore claims its LiquidJet can drop Nvidia Rubin GPU temperatures by 10°C — can also boost performance by 15% as hyperscalers eye using delidded GPUs in production environments",
    "url": "https://www.tomshardware.com/pc-components/liquid-cooling/frore-claims-its-liquidjet-can-drop-nvidia-rubin-gpu-temperatures-by-10-c-can-also-boost-performance-by-15-percent-as-hyperscalers-eye-using-delidded-gpus-in-production-environments",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T11:02:00+00:00",
    "summary": "As cooling becomes a crucial element for economic efficiency of AI data centers, Frore claims that using is LiquidJet coldplate could increase efficiency of token generation by 15%."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/pc-cases/montech-tg3-panoramic-mid-tower-case-review",
    "domain": "AI 算力 / 半导体",
    "title": "Montech TG3 Panoramic Mid-tower case review: a fantastic value, with four included RGB fans and panoramic views",
    "url": "https://www.tomshardware.com/pc-components/pc-cases/montech-tg3-panoramic-mid-tower-case-review",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T11:00:00+00:00",
    "summary": "Montech's TG3 is a marvelous value in the budget mid-tower space, with ample room for components and four included fans. It also offers solid noise-normalized cooling for the CPU and a good all-around"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/macbooks/best-buy-has-slashed-usd900-off-this-macbook-laden-with-memory-14-inch-m4-pro-with-48gb-of-memory-and-2tb-of-storage-now-only-usd2-999",
    "domain": "AI 算力 / 半导体",
    "title": "Best Buy has slashed $900 off this MacBook laden with memory — 14-inch M4 Pro with 48GB of memory and 2TB of storage now only $2,999",
    "url": "https://www.tomshardware.com/laptops/macbooks/best-buy-has-slashed-usd900-off-this-macbook-laden-with-memory-14-inch-m4-pro-with-48gb-of-memory-and-2tb-of-storage-now-only-usd2-999",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T10:39:33+00:00",
    "summary": "In a time of extreme memory and storage pricing, this Apple MacBook Pro deal from Best Buy slashes $900 off the 48GB M4 Pro machine."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-headsets/glorious-wireless-infiniteplay-gaming-headset-review",
    "domain": "AI 算力 / 半导体",
    "title": "Glorious Wireless InfinitePlay Gaming Headset Review",
    "url": "https://www.tomshardware.com/peripherals/gaming-headsets/glorious-wireless-infiniteplay-gaming-headset-review",
    "source": "Christopher Coke",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T10:00:00+00:00",
    "summary": "The Glorious Wireless InfinitePlay offers solid sound, quality comms, and never-ending uptime at a reduced price. There’s a handful of trade-offs, but this headset has more wins than losses and is def"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/humble-nas-gets-transformed-into-a-gaming-pc-with-and-rtx-5060-hanging-from-its-side-frankenstein-rig-hides-dedicated-psu-in-drive-bay-to-achieve-vast-performance-increase-over-igpu",
    "domain": "AI 算力 / 半导体",
    "title": "Crazed modder turns NAS into a gaming PC with RTX 5060 hanging from the side, boosts frame rate by 828% — Frankenstein rig hides dedicated PSU in drive bay, breaks Time Spy world record for the onboar",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/humble-nas-gets-transformed-into-a-gaming-pc-with-and-rtx-5060-hanging-from-its-side-frankenstein-rig-hides-dedicated-psu-in-drive-bay-to-achieve-vast-performance-increase-over-igpu",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T09:21:13+00:00",
    "summary": "A modder has attached a full-sized RTX 5060 graphics card to a ZimaCube 2 NAS server and achieved up to 8x faster performance in games. The jerry-rigged setup doesn't look the most polished, and the C"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/amd-doubles-data-center-revenue-year-over-year-but-gaming-revenue-plunged-by-31-percent-ceo-lisa-su-says-prices-have-weighed-on-consumer-demand-but-is-optimistic-about-client-market",
    "domain": "AI 算力 / 半导体",
    "title": "AMD doubles data center revenue year over year, but gaming revenue plunged by 31% — CEO Lisa Su says prices have 'weighed on' consumer demand but is 'optimistic' about client market",
    "url": "https://www.tomshardware.com/tech-industry/amd-doubles-data-center-revenue-year-over-year-but-gaming-revenue-plunged-by-31-percent-ceo-lisa-su-says-prices-have-weighed-on-consumer-demand-but-is-optimistic-about-client-market",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T22:03:07+00:00",
    "summary": "AMD reported record revenue in Q2 2026, including doubling its data center business year-over-year, but gaming revenue dived 31%."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/more-gpu-price-hikes-loom-for-asia-as-japanese-distributor-warns-of-new-increases-cfd-sales-signals-20-percent-to-40-percent-higher-prices-on-gigabyte-graphics-card-orders-starting-this-month",
    "domain": "AI 算力 / 半导体",
    "title": "More GPU price hikes loom for Asia as Japanese distributor warns of new increases — CFD Sales signals 20% to 40% higher prices on Gigabyte graphics card orders starting this month",
    "url": "https://www.tomshardware.com/pc-components/gpus/more-gpu-price-hikes-loom-for-asia-as-japanese-distributor-warns-of-new-increases-cfd-sales-signals-20-percent-to-40-percent-higher-prices-on-gigabyte-graphics-card-orders-starting-this-month",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T17:38:15+00:00",
    "summary": "Japanese technology supplier and distributor confirms that the Gigabyte graphics card will cost between 20% and 40% more due to a new price increase."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/us-mulling-ban-on-key-chinese-networking-tech-in-data-center-component-crackdown-white-house-wants-to-impose-restrictions-in-2026-china-says-it-will-respond-if-necessary",
    "domain": "AI 算力 / 半导体",
    "title": "US mulling ban on key Chinese networking tech in data center component crackdown — White House wants to impose restrictions in 2026, China says it will respond if necessary",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/us-mulling-ban-on-key-chinese-networking-tech-in-data-center-component-crackdown-white-house-wants-to-impose-restrictions-in-2026-china-says-it-will-respond-if-necessary",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T16:54:00+00:00",
    "summary": "Sources say that the FCC is drafting a ban on optical transceivers for data centers. These components, which convert electrical signals into light signals, are said to pose a risk as they can be used "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/texas-slams-on-the-breaks-for-1-800-data-centers-power-grid-requirements-are-five-times-higher-than-peak-record-demand-474-gigawatts-of-power-requests-are-now-subject-to-new-moratorium",
    "domain": "AI 算力 / 半导体",
    "title": "Texas slams on the brakes for 1,800 data centers, power grid requirements are five times higher than peak record demand — 474 gigawatts of power requests are now subject to new moratorium",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/texas-slams-on-the-breaks-for-1-800-data-centers-power-grid-requirements-are-five-times-higher-than-peak-record-demand-474-gigawatts-of-power-requests-are-now-subject-to-new-moratorium",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T16:48:12+00:00",
    "summary": "Gov. Greg Abbott (R) instructed PUCT and ERCOT to pause all data center applications until they complete an audit on all the information that data center developers must submit. The move reportedly ca"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/kioxia-and-sandisk-demonstrate-the-worlds-highest-density-3d-nand-flash-332-active-layers-and-up-to-4-800-mt-s-interface",
    "domain": "AI 算力 / 半导体",
    "title": "Kioxia and Sandisk demonstrate the world's highest-density 3D NAND flash — 332 active layers and up to 4,800 MT/s interface",
    "url": "https://www.tomshardware.com/pc-components/ssds/kioxia-and-sandisk-demonstrate-the-worlds-highest-density-3d-nand-flash-332-active-layers-and-up-to-4-800-mt-s-interface",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T16:15:42+00:00",
    "summary": "Kioxia and Sandisk introduce BiCS10 3D QLC NAND device with a record areal density of over 37 Gbit/mm^2."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/sandisk-and-sk-hynix-unveil-hbf-spec-up-to-16-hi-nand-stacks-3-tb-s-bandwidth-ucie",
    "domain": "AI 算力 / 半导体",
    "title": "New HBF spec outlines tech that can give GPUs terabytes of extra memory — Sandisk and SK hynix unveil spec with up to 16-Hi NAND stacks, 3 TB/s bandwidth, UCIe",
    "url": "https://www.tomshardware.com/pc-components/ssds/sandisk-and-sk-hynix-unveil-hbf-spec-up-to-16-hi-nand-stacks-3-tb-s-bandwidth-ucie",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T14:42:58+00:00",
    "summary": "Sandisk and SK hynix formally introduce HBF specification that promises up to 3 TB/s of bandwidth eventually, though only four companies are currently interested in the technology."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cooling/pc-cooling-outfit-arctic-reverses-tariff-era-price-hikes-after-us-government-refund-lowers-prices-across-lineup-including-coolers-and-case-fans",
    "domain": "AI 算力 / 半导体",
    "title": "PC cooling outfit Arctic reverses tariff-era price hikes after US government refund — lowers prices across lineup, including coolers and case fans",
    "url": "https://www.tomshardware.com/pc-components/cooling/pc-cooling-outfit-arctic-reverses-tariff-era-price-hikes-after-us-government-refund-lowers-prices-across-lineup-including-coolers-and-case-fans",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T13:37:09+00:00",
    "summary": "The company says it is honoring its earlier promise to reverse tariff-driven price increases, becoming one of the first PC hardware vendors to publicly roll back pricing after a major court ruling."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/chinese-chipmaking-tool-roadmap-examined",
    "domain": "AI 算力 / 半导体",
    "title": "Chinese chipmaking tool roadmaps examined — Beijing's nascent lithography tools target DUV production at five machines a year, and an EUV prototype with no chips",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/chinese-chipmaking-tool-roadmap-examined",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T13:15:00+00:00",
    "summary": "Ultimately, three markers will indicate whether China’s domestic DUV program is a legitimate rival or yet more state-sanctioned hot air."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/at-least-37-people-arrested-in-2026-so-far-for-protesting-against-data-centers-most-taken-into-custody-acted-peacefully-only-broke-petty-rules",
    "domain": "AI 算力 / 半导体",
    "title": "At least 37 people arrested in 2026 so far for protesting against data centers, most for breaking 'petty rules' — most taken into custody acted peacefully",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/at-least-37-people-arrested-in-2026-so-far-for-protesting-against-data-centers-most-taken-into-custody-acted-peacefully-only-broke-petty-rules",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T12:53:03+00:00",
    "summary": "Data center protesters are getting arrested for minor infractions, yet they continue pushing back against these projects. Aside from the arrests, there's also at least 12 instances (probably more) whe"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/lenovo-loq-essentials-15-gen-11-review",
    "domain": "AI 算力 / 半导体",
    "title": "Lenovo LOQ Essentials 15 Gen 11 Review: A good display meets a low-power RTX 5060",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/lenovo-loq-essentials-15-gen-11-review",
    "source": "Charles Jefferies",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T12:00:00+00:00",
    "summary": "The Lenovo LOQ Essentials 15 Gen 11 pairs an RTX 5060, 144 Hz display, and excellent upgradeability with a comfortable keyboard, but its low-power GPU configuration and outdated CPU leave it strugglin"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/apple-is-getting-this-wrong-says-openai-startup-blasts-iphone-maker-over-lawsuit-alleging-it-stole-confidential-information-through-ex-apple-employees",
    "domain": "AI 算力 / 半导体",
    "title": "‘Apple is getting this wrong,’ says OpenAI — startup blasts iPhone maker over lawsuit alleging it stole confidential information through ex-Apple employees",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/apple-is-getting-this-wrong-says-openai-startup-blasts-iphone-maker-over-lawsuit-alleging-it-stole-confidential-information-through-ex-apple-employees",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T11:52:34+00:00",
    "summary": "OpenAI denies Apple's allegations in a blog post. The company claims that it doesn't have and even doesn't want its rivals trade secrets."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/chinese-ship-spotted-lurking-over-taiwan-us-undersea-cables-research-vessel-seen-loitering-above-the-8-000-mile-pacific-light-cable-network-fiber-optic-system",
    "domain": "AI 算力 / 半导体",
    "title": "Chinese ship spotted lurking over Taiwan-US undersea cables — 'research vessel' seen loitering above the 8,000-mile Pacific Light Cable Network fiber-optic system",
    "url": "https://www.tomshardware.com/networking/chinese-ship-spotted-lurking-over-taiwan-us-undersea-cables-research-vessel-seen-loitering-above-the-8-000-mile-pacific-light-cable-network-fiber-optic-system",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T11:49:18+00:00",
    "summary": "A new video shows Taiwan’s Coast Guard warning a 200-ft long Chinese-flagged research vessel, spotted loitering over a fiber internet cable, to change course."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/desks/grab-a-new-secretlab-sit-to-stand-desk-for-usd699-save-usd50-as-the-magnus-evo-receives-its-first-ever-discount",
    "domain": "AI 算力 / 半导体",
    "title": "Grab a new Secretlab sit-to-stand desk for $699 — Save $50 as the Magnus Evo receives its first-ever discount",
    "url": "https://www.tomshardware.com/peripherals/desks/grab-a-new-secretlab-sit-to-stand-desk-for-usd699-save-usd50-as-the-magnus-evo-receives-its-first-ever-discount",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T10:37:50+00:00",
    "summary": "Secretlab has finally reduced the price of the Magnus Evo standing desk. In its first-ever discount, you can save $50 on a new sit-to-stand desk."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/16gb-gpus-and-8-core-cpus-officially-become-the-most-popular-configs-on-steam-latest-hardware-survey-shows-modern-gamings-growing-hunger-for-more-resources",
    "domain": "AI 算力 / 半导体",
    "title": "16GB GPUs and 8-core CPUs officially become the most popular configs on Steam — Latest hardware survey shows modern gaming's growing hunger for more resources",
    "url": "https://www.tomshardware.com/pc-components/16gb-gpus-and-8-core-cpus-officially-become-the-most-popular-configs-on-steam-latest-hardware-survey-shows-modern-gamings-growing-hunger-for-more-resources",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T10:30:00+00:00",
    "summary": "For the first time in Steam history, 8-core CPUs have overtaken 6-core CPUs and GPUs with 16GB of VRAM have overtaken 8GB GPUs. Even though the hardware survey doesn't represent everyone, it still ind"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/three-major-pc-makers-now-using-chinese-memory-to-fight-unprecedented-memory-shortage-report-claims-hp-asus-and-acer-using-small-amounts-of-cxmt-chips-in-limited-number-of-notebooks-for-non-us-market",
    "domain": "AI 算力 / 半导体",
    "title": "Three major PC makers now using Chinese memory to fight 'unprecedented memory shortage,' report claims — HP, Asus, and Acer using 'small amounts' of CXMT chips in limited number of notebooks for non-U",
    "url": "https://www.tomshardware.com/tech-industry/three-major-pc-makers-now-using-chinese-memory-to-fight-unprecedented-memory-shortage-report-claims-hp-asus-and-acer-using-small-amounts-of-cxmt-chips-in-limited-number-of-notebooks-for-non-us-market",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T10:15:23+00:00",
    "summary": "A new report claims that HP, Asus, and Acer have started to use a small amount of CXMT memory chips in notebooks for non-US markets."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/china-cracks-down-on-copycat-chip-designs-with-new-regulations-and-penalties-new-guidelines-enforce-originality-and-independent-development",
    "domain": "AI 算力 / 半导体",
    "title": "China cracks down on copycat chip designs with new regulations and penalties — new guidelines enforce originality and independent development",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/china-cracks-down-on-copycat-chip-designs-with-new-regulations-and-penalties-new-guidelines-enforce-originality-and-independent-development",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T10:00:00+00:00",
    "summary": "China tightens legal protections for domestically developed chip layout designs by raising originality requirements and strengthening infringement penalties."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/pc-building/this-144-piece-toolkit-is-a-must-buy-for-hobbyists-and-pc-builders-for-under-usd40-pocket-a-20-percent-saving-on-this-screwdriver-set-with-two-drivers-120-magnetic-bits-and-22-repair-tools-for-your-projects",
    "domain": "AI 算力 / 半导体",
    "title": "This 144-piece toolkit is a must-buy for hobbyists and PC builders for under $40 — pocket a 20% saving on this screwdriver set with two drivers, 120 magnetic bits, and 22 repair tools for your project",
    "url": "https://www.tomshardware.com/desktops/pc-building/this-144-piece-toolkit-is-a-must-buy-for-hobbyists-and-pc-builders-for-under-usd40-pocket-a-20-percent-saving-on-this-screwdriver-set-with-two-drivers-120-magnetic-bits-and-22-repair-tools-for-your-projects",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T09:43:27+00:00",
    "summary": "Pick up this 144-in-1 repair toolkit from Strebito, with 120 bits and a number of other tools, for less than $40 right now, saving you 20%."
  },
  {
    "id": "rss:https://www.eetimes.com/renesas-tackles-memory-bottleneck-with-mrdimm-update/",
    "domain": "AI 算力 / 半导体",
    "title": "Renesas Tackles Memory Bottleneck with MRDIMM Update",
    "url": "https://www.eetimes.com/renesas-tackles-memory-bottleneck-with-mrdimm-update/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T19:00:00+00:00",
    "summary": "Renesas’s Gen 3 DDR5 MRDIMM attacks AI’s memory choke point with 16,000 MT/s bandwidth and no platform overhaul. The post Renesas Tackles Memory Bottleneck with MRDIMM Update appeared first on EE Time"
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
    "id": "hn:49025890",
    "domain": "AI 算力 / 半导体",
    "title": "AMD's 256-core Epyc 9996 'Venice' claims up to a 3.4x jump over Intel Xeon",
    "url": "https://www.tomshardware.com/pc-components/cpus/amds-256-core-epyc-9996-venice-claims-up-to-a-3-4x-jump-over-intel-xeon-competition-20-percent-over-nvidia-vera-zen-6-comes-with-up-to-1024mb-of-l3-16-channel-memory-and-5ghz-clock-speeds",
    "source": "rndsignals",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-07-23T18:16:54+00:00",
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
    "id": "hn:49184755",
    "domain": "大厂 AI 动态",
    "title": "Changes at Google DeepMind: Demis Hassabis from CEO to Chair, Jeff Dean departs",
    "url": "https://blog.google/company-news/inside-google/message-ceo/next-chapter-ai-momentum/",
    "source": "colesantiago",
    "platform": "hackernews",
    "points": 579,
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
    "points": 619,
    "published_at": "2026-07-30T15:15:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:49184757",
    "domain": "大厂 AI 动态",
    "title": "Demis Hassabis is moving from CEO to Chairman at Google DeepMind",
    "url": "https://www.axios.com/2026/08/05/google-deepmind-demis-hassabis-ai",
    "source": "ot",
    "platform": "hackernews",
    "points": 369,
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
    "points": 383,
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
    "points": 197,
    "published_at": "2026-07-27T09:56:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:49187259",
    "domain": "大厂 AI 动态",
    "title": "Sula: A Gemini protocol server written in Scryer Prolog",
    "url": "https://sagredo.dev/projects/sula/",
    "source": "triska",
    "platform": "hackernews",
    "points": 48,
    "published_at": "2026-08-05T18:52:58+00:00",
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
    "id": "hn:48864507",
    "domain": "大厂 AI 动态",
    "title": "Please don't discontinue Gemini 2.5 Flash",
    "url": "https://discuss.ai.google.dev/t/please-dont-discontinue-gemini-2-5-flash/174246",
    "source": "NickDob",
    "platform": "hackernews",
    "points": 135,
    "published_at": "2026-07-10T20:00:28+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/976004/elon-musk-grokipedia-ai-wikipedia-not-updating-dead",
    "domain": "大厂 AI 动态",
    "title": "Elon Musk&#8217;s attempt at an AI Wikipedia hasn&#8217;t been updated in months",
    "url": "https://www.theverge.com/ai-artificial-intelligence/976004/elon-musk-grokipedia-ai-wikipedia-not-updating-dead",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T00:25:10+00:00",
    "summary": "xAI's Grokipedia, an online encyclopedia with AI-generated articles that Elon Musk once promised would be a \"massive improvement\" over Wikipedia, apparently hasn't been updated since April 24th, accor"
  },
  {
    "id": "rss:https://www.theverge.com/tech/975955/x-twitter-nikita-bier-leaving",
    "domain": "大厂 AI 动态",
    "title": "X product chief Nikita Bier is leaving after one year",
    "url": "https://www.theverge.com/tech/975955/x-twitter-nikita-bier-leaving",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T22:19:55+00:00",
    "summary": "X head of product Nikita Bier is stepping down and says he will move into a role as an advisor, writing that \"it's time to pass the torch and demote myself to my natural state: a poster.\" He shared th"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/975723/ring-wired-doorbell-pro-battery-doorbell-plus-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Two of Ring&#8217;s latest video doorbells are a lot cheaper than usual",
    "url": "https://www.theverge.com/gadgets/975723/ring-wired-doorbell-pro-battery-doorbell-plus-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T17:53:43+00:00",
    "summary": "Ring&#8217;s Wired Doorbell Pro and Battery Doorbell Plus are two of the brand&#8217;s most well-rounded video doorbells, whether you&#8217;re looking for a hardwired model or one that runs on a batte"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/975651/uber-ceo-earnings-waymo-partnership",
    "domain": "大厂 AI 动态",
    "title": "Uber CEO brushes off reports of a Waymo break-up",
    "url": "https://www.theverge.com/transportation/975651/uber-ceo-earnings-waymo-partnership",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T17:34:48+00:00",
    "summary": "After Uber and Waymo ended their partnership in Phoenix earlier this year, experts and robotaxi watchers wondered whether the companies' improbable bromance was fraying. Not so, Uber CEO Dara Khosrows"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/975603/refurbished-apple-macbook-neo-google-wireless-charger-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Apple’s selling refurbished MacBook Neos with a $100 discount",
    "url": "https://www.theverge.com/gadgets/975603/refurbished-apple-macbook-neo-google-wireless-charger-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T16:59:23+00:00",
    "summary": "Apple’s most affordable laptop, the MacBook Neo, is available once again at its pre-price hike price. All four colors are currently discounted and available refurbished through the company, with the b"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/975528/fenix-flexin-ai-music-generator-treblo",
    "domain": "大厂 AI 动态",
    "title": "Sure seems like Fenix Flexin used AI music generator Treblo",
    "url": "https://www.theverge.com/ai-artificial-intelligence/975528/fenix-flexin-ai-music-generator-treblo",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T16:57:25+00:00",
    "summary": "We were pretty sure that Fenix Flexin's \"Rubberz\" was made using AI, but musician Medasin was confident that it was made using Treblo specifically. Now the company and a new detection tool seem to con"
  },
  {
    "id": "rss:https://www.theverge.com/tech/975677/google-deepmind-ai-demis-hassabis-shakeup",
    "domain": "大厂 AI 动态",
    "title": "Google just announced a major shakeup of its top AI leadership",
    "url": "https://www.theverge.com/tech/975677/google-deepmind-ai-demis-hassabis-shakeup",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T16:47:23+00:00",
    "summary": "Google is making some significant AI leadership changes, including a major shift for Google DeepMind leader Demis Hassabis. Hassabis will become the chair of Google DeepMind and the chief scientist at"
  },
  {
    "id": "rss:https://www.theverge.com/science/975545/spacex-x-earnings-ai-data-centers-compute-space",
    "domain": "大厂 AI 动态",
    "title": "SpaceX is barely Space and mostly X",
    "url": "https://www.theverge.com/science/975545/spacex-x-earnings-ai-data-centers-compute-space",
    "source": "Elizabeth Lopatto",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T16:35:56+00:00",
    "summary": "Once, I had some questions about why SpaceX, Elon Musk's healthiest company, acquired xAI, his sickliest one. Now I have some questions about why we're calling the whole thing SpaceX. Look, what we ha"
  },
  {
    "id": "rss:https://www.theverge.com/tech/975398/reddit-ai-rules-hub-moderator-old-reddit-developer-platform",
    "domain": "大厂 AI 动态",
    "title": "Reddit is introducing a new moderator: AI",
    "url": "https://www.theverge.com/tech/975398/reddit-ai-rules-hub-moderator-old-reddit-developer-platform",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T16:00:00+00:00",
    "summary": "Reddit is enlisting AI to help moderate new subreddits - and eventually the rest of site. The company is introducing automated moderation tools that rely on LLMs to help mods manage their communities,"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/975577/aisi-openai-anthropic-agent-hacking",
    "domain": "大厂 AI 动态",
    "title": "Rogue AI agents created fake online identities in another hacking attempt",
    "url": "https://www.theverge.com/ai-artificial-intelligence/975577/aisi-openai-anthropic-agent-hacking",
    "source": "Robert Hart",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T15:14:57+00:00",
    "summary": "Yet more rogue AI agents from OpenAI and Anthropic have been caught attempting to hack real targets online without permission. The discoveries add to a growing list of previously unknown incidents tha"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/05/get-up-to-400-off-your-techcrunch-disrupt-2026-pass-until-friday/",
    "domain": "大厂 AI 动态",
    "title": "Get up to $400 off your TechCrunch Disrupt 2026 pass until Friday",
    "url": "https://techcrunch.com/2026/08/05/get-up-to-400-off-your-techcrunch-disrupt-2026-pass-until-friday/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T22:55:43+00:00",
    "summary": "Starting today, you can take an additional $100 off your founder, investor, or attendee TechCrunch Disrupt 2026 pass, which is a nice bonus on top of our current discounted pricing."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/05/nikita-bier-steps-down-as-xs-head-of-product/",
    "domain": "大厂 AI 动态",
    "title": "Nikita Bier steps down as X’s head of product",
    "url": "https://techcrunch.com/2026/08/05/nikita-bier-steps-down-as-xs-head-of-product/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T21:30:50+00:00",
    "summary": "The serial entrepreneur is stepping down a little over a year after taking the \"24/7 job\" of overseeing X."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/05/travis-kalanicks-robotics-startup-atoms-taps-former-uber-finance-chief-as-cfo/",
    "domain": "大厂 AI 动态",
    "title": "Travis Kalanick’s robotics startup Atoms taps former Uber finance chief as CFO",
    "url": "https://techcrunch.com/2026/08/05/travis-kalanicks-robotics-startup-atoms-taps-former-uber-finance-chief-as-cfo/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T21:26:40+00:00",
    "summary": "Kalanick continues to get the band back together, after acquiring Anthony Levandowski's autonomy startup, and even soliciting investment from Uber."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/05/meta-launches-muse-code-an-ai-agent-for-large-code-bases/",
    "domain": "大厂 AI 动态",
    "title": "Meta launches Muse Code, an AI agent for large code bases",
    "url": "https://techcrunch.com/2026/08/05/meta-launches-muse-code-an-ai-agent-for-large-code-bases/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T21:21:28+00:00",
    "summary": "Meta expanded its AI coding offerings with a new agent that, it promises, can handle complex tasks with complex software."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/05/trumps-doj-gains-oversight-of-openais-green-card-employee-sponsorships/",
    "domain": "大厂 AI 动态",
    "title": "Trump’s DOJ gains oversight of OpenAI’s green-card employee sponsorships",
    "url": "https://techcrunch.com/2026/08/05/trumps-doj-gains-oversight-of-openais-green-card-employee-sponsorships/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T21:05:37+00:00",
    "summary": "The DOJ alleged that OpenAI did not meaningful attempt to hire U.S. citizens before seeking permanent residence for Visa-holding employees."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/05/moove-raises-250m-to-become-the-backbone-of-the-robotaxi-industry/",
    "domain": "大厂 AI 动态",
    "title": "Moove raises $250M to become the backbone of the robotaxi industry",
    "url": "https://techcrunch.com/2026/08/05/moove-raises-250m-to-become-the-backbone-of-the-robotaxi-industry/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T20:50:45+00:00",
    "summary": "Moove is scaling up the autonomous vehicle fleet management side of its business and plans to someday own, not just manage, Waymo robotaxis."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/05/how-lightspeed-found-its-newest-hire-via-instagram-dm/",
    "domain": "大厂 AI 动态",
    "title": "How Lightspeed found its newest hire … via Instagram DM",
    "url": "https://techcrunch.com/2026/08/05/how-lightspeed-found-its-newest-hire-via-instagram-dm/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T20:48:56+00:00",
    "summary": "Lightspeed partners Josh Machiz and Claire Zau stopped by the Equity studio to talk about the strategies behind their growing social media presence and their podcast, Lightwork."
  },
  {
    "id": "rss:https://techcrunch.com/video/why-lightspeed-is-going-all-in-on-creator-led-venture-capital/",
    "domain": "大厂 AI 动态",
    "title": "Why Lightspeed is going all-in on creator-led venture capital",
    "url": "https://techcrunch.com/video/why-lightspeed-is-going-all-in-on-creator-led-venture-capital/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T20:48:54+00:00",
    "summary": "Venture firms are turning to creators to build trust with the next generation of founders before a check is ever written.&#160;It&#8217;s&#160;a trend&#160;that&#8217;s&#160;been building with&#160;a1"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/05/klaviyo-acquires-elias-torres-agency-in-full-circle-reunion-for-tech-founders/",
    "domain": "大厂 AI 动态",
    "title": "Klaviyo acquires Elias Torres’ Agency in full-circle reunion for tech founders",
    "url": "https://techcrunch.com/2026/08/05/klaviyo-acquires-elias-torres-agency-in-full-circle-reunion-for-tech-founders/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T20:05:00+00:00",
    "summary": "The serial entrepreneur joins the e-commerce company as CPO to lead its AI agents."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/05/jeff-dean-and-other-top-ai-researchers-are-leaving-google-to-launch-their-own-startup/",
    "domain": "大厂 AI 动态",
    "title": "Jeff Dean and other top AI researchers are leaving Google to launch their own startup",
    "url": "https://techcrunch.com/2026/08/05/jeff-dean-and-other-top-ai-researchers-are-leaving-google-to-launch-their-own-startup/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T19:30:19+00:00",
    "summary": "The legendary Google executive is joined by other outgoing Google execs in a joint mission to use AI to push forward the process of scientific discovery."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/05/reddit-aims-to-make-karma-less-important-for-first-time-posters-with-shift-to-ai-moderation-tools/",
    "domain": "大厂 AI 动态",
    "title": "Reddit aims to make ‘karma’ less important for first-time posters with shift to AI moderation tools",
    "url": "https://techcrunch.com/2026/08/05/reddit-aims-to-make-karma-less-important-for-first-time-posters-with-shift-to-ai-moderation-tools/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T18:00:40+00:00",
    "summary": "Reddit is expanding its moderation tools and building stronger abuse prevention systems that it says could eventually reduce communities’ reliance on karma and account-age requirements, making it easi"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/05/lucid-motors-just-delayed-its-affordable-ev-now-what/",
    "domain": "大厂 AI 动态",
    "title": "Lucid Motors just delayed its affordable EV. Now what?",
    "url": "https://techcrunch.com/2026/08/05/lucid-motors-just-delayed-its-affordable-ev-now-what/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T17:57:45+00:00",
    "summary": "The Cosmos EV is now slated for release in the second half of 2027. CEO Silvio Napoli said he's focused on getting the EV right, as well as its nearer-term robotaxi project with Uber and Nuro."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/05/meet-the-eight-startups-pitching-at-startup-battlefield-australia/",
    "domain": "大厂 AI 动态",
    "title": "Meet the eight startups pitching at Startup Battlefield Australia",
    "url": "https://techcrunch.com/2026/08/05/meet-the-eight-startups-pitching-at-startup-battlefield-australia/",
    "source": "Isabelle Johannessen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T17:02:00+00:00",
    "summary": "The applications are in, and the TechCrunch Startup Battlefield team made their decisions!"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/05/psa-apples-private-relay-can-leak-your-real-ip-address/",
    "domain": "大厂 AI 动态",
    "title": "PSA: Apple’s Private Relay can leak your real IP address",
    "url": "https://techcrunch.com/2026/08/05/psa-apples-private-relay-can-leak-your-real-ip-address/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T16:52:29+00:00",
    "summary": "A bug in how Apple implements its Private Relay feature, which in theory masks users’ IP addresses from the sites they visit, can reveal users’ real IP addresses."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/05/shopify-says-ai-search-is-driving-more-traffic-and-sales-not-replacing-google/",
    "domain": "大厂 AI 动态",
    "title": "Shopify says AI search is driving more traffic and sales, not replacing Google",
    "url": "https://techcrunch.com/2026/08/05/shopify-says-ai-search-is-driving-more-traffic-and-sales-not-replacing-google/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T15:56:14+00:00",
    "summary": "Shopify says AI isn’t cannibalizing search traffic the way it has for publishers. Instead, AI-driven traffic and orders to Shopify stores tripled year over year in Q2."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/05/hark-previews-its-browser-use-agent-for-completing-tasks/",
    "domain": "大厂 AI 动态",
    "title": "Hark previews its browser use agent for completing tasks",
    "url": "https://techcrunch.com/2026/08/05/hark-previews-its-browser-use-agent-for-completing-tasks/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T15:46:27+00:00",
    "summary": "Hark claims that its browser use agent is faster and cheaper than competition."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/05/zoox-to-start-charging-for-robotaxi-rides-in-las-vegas/",
    "domain": "大厂 AI 动态",
    "title": "Zoox to start charging for robotaxi rides in Las Vegas",
    "url": "https://techcrunch.com/2026/08/05/zoox-to-start-charging-for-robotaxi-rides-in-las-vegas/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T15:06:42+00:00",
    "summary": "This marks the official launch of Zoox's commercial operations."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/05/techcrunch-disrupt-2026s-real-world-ai-stage-features-robots-automated-factories-and-extinct-animals/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Disrupt 2026’s Real World AI Stage features robots, automated factories, and extinct animals",
    "url": "https://techcrunch.com/2026/08/05/techcrunch-disrupt-2026s-real-world-ai-stage-features-robots-automated-factories-and-extinct-animals/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T15:05:00+00:00",
    "summary": "On our new Real World AI stage, we’ll be focusing on the intersection between the digital and physical, and all the ways we’ll continue to see a blending of the two."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/05/as-gen-z-reconsiders-dating-apps-tinders-irl-events-expand-to-dozens-more-cities/",
    "domain": "大厂 AI 动态",
    "title": "As Gen Z reconsiders dating apps, Tinder’s IRL events expand to dozens more cities",
    "url": "https://techcrunch.com/2026/08/05/as-gen-z-reconsiders-dating-apps-tinders-irl-events-expand-to-dozens-more-cities/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T14:45:06+00:00",
    "summary": "Tinder is expanding its in-person events feature from an initial Los Angeles test to 26 cities worldwide by the end of September."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/05/trump-epa-wrongly-canceled-20b-in-climate-funds-appeals-court-rules/",
    "domain": "大厂 AI 动态",
    "title": "Trump EPA wrongly canceled $20B in climate funds, appeals court rules",
    "url": "https://techcrunch.com/2026/08/05/trump-epa-wrongly-canceled-20b-in-climate-funds-appeals-court-rules/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T14:40:13+00:00",
    "summary": "Climate nonprofits can again access their federal funding more than a year after the Trump EPA ordered Citibank to freeze their accounts."
  },
  {
    "id": "rss:https://stratechery.com/2026/google-earnings-the-frontier-case-amazon-earnings/",
    "domain": "大厂 AI 动态",
    "title": "Google Earnings, The Frontier Case, Amazon Earnings",
    "url": "https://stratechery.com/2026/google-earnings-the-frontier-case-amazon-earnings/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T10:00:00+00:00",
    "summary": "Google's earnings seemed to confirm the Anthropic hedge; it was Andy Jassy who explained why their — and Amazon's — capex was justifiable."
  },
  {
    "id": "rss:https://stratechery.com/2026/microsoft-earnings-microsoft-vs-meta-the-efficiency-payoff/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft Earnings, Microsoft vs. Meta, The Efficiency Payoff",
    "url": "https://stratechery.com/2026/microsoft-earnings-microsoft-vs-meta-the-efficiency-payoff/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T10:00:00+00:00",
    "summary": "Microsoft's earnings were compelling because they showed a clarity of strategy, lower costs, and a tangibility of application. The reason why is scarier."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/08/thousands-of-servers-can-be-backdoored-by-exploiting-buggy-motherboard-controllers/",
    "domain": "大厂 AI 动态",
    "title": "Thousands of servers can be backdoored by exploiting buggy motherboard controllers",
    "url": "https://arstechnica.com/security/2026/08/thousands-of-servers-can-be-backdoored-by-exploiting-buggy-motherboard-controllers/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T22:35:20+00:00",
    "summary": "Baseboard management controllers from the world's biggest manufacturers are a security mess."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/08/schwartz-confirmed-as-cdc-director-after-bungling-confirmation-hearing/",
    "domain": "大厂 AI 动态",
    "title": "Schwartz confirmed as CDC director after bungling confirmation hearing",
    "url": "https://arstechnica.com/health/2026/08/schwartz-confirmed-as-cdc-director-after-bungling-confirmation-hearing/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T21:03:18+00:00",
    "summary": "Schwartz is well-qualified for the role, but crashed and burned in Senate hearing."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/08/anthropics-ai-used-fake-identities-malware-in-rogue-attack-on-github-project/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic’s AI used fake identities, malware in rogue attack on GitHub project",
    "url": "https://arstechnica.com/security/2026/08/anthropics-ai-used-fake-identities-malware-in-rogue-attack-on-github-project/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T20:47:11+00:00",
    "summary": "Anthropic and OpenAI models’ unprompted actions forced halt to UK cyber tests."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/08/reddit-signals-ominous-upcoming-changes-for-old-reddit-com/",
    "domain": "大厂 AI 动态",
    "title": "Reddit signals ominous upcoming \"changes” for old.reddit.com",
    "url": "https://arstechnica.com/gadgets/2026/08/reddit-signals-ominous-upcoming-changes-for-old-reddit-com/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T20:01:32+00:00",
    "summary": "Reddit says the beloved site is used for some \"bad behavior.\""
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/08/hank-green-found-the-ai-problem-that-youtube-labels-cant-catch/",
    "domain": "大厂 AI 动态",
    "title": "Hank Green found the AI problem that YouTube labels can’t catch",
    "url": "https://arstechnica.com/ai/2026/08/hank-green-found-the-ai-problem-that-youtube-labels-cant-catch/",
    "source": "Nate Anderson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T19:51:40+00:00",
    "summary": "\"Slop\" isn't the only problem."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/08/spacex-claims-starlink-mobile-will-be-better-than-att-t-mobile-and-verizon/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX claims Starlink Mobile will be better than AT&T, T-Mobile, and Verizon",
    "url": "https://arstechnica.com/tech-policy/2026/08/spacex-claims-starlink-mobile-will-be-better-than-att-t-mobile-and-verizon/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T19:38:56+00:00",
    "summary": "SpaceX won't build large cell towers but plans small base stations across US."
  },
  {
    "id": "hn:49057574",
    "domain": "股票",
    "title": "Google Discloses $94.1B in SpaceX Stock, Marking 6% Stake",
    "url": "https://www.wsj.com/tech/google-discloses-94-1-billion-in-spacex-stock-marking-6-stake-91655d7c",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 342,
    "published_at": "2026-07-26T12:43:21+00:00",
    "summary": ""
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
    "id": "hn:49166182",
    "domain": "股票",
    "title": "Bending Spoons makes first post-IPO acquisition with $1.3B Airtable deal",
    "url": "https://live.euronext.com/en/financial-news/bending-spoons-makes-first-post-ipo-acquisition-13-billion-airtable-deal",
    "source": "riffraff",
    "platform": "hackernews",
    "points": 110,
    "published_at": "2026-08-04T09:27:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:49122994",
    "domain": "股票",
    "title": "Situational Awareness down 67% in July in AI stock rout",
    "url": "https://www.wsj.com/finance/investing/situational-awareness-down-67-in-july-in-ai-stock-rout-cd19901f",
    "source": "pondsider",
    "platform": "hackernews",
    "points": 155,
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
    "id": "hn:49151871",
    "domain": "股票",
    "title": "Situational Awareness and the Impending Stock Market Volatility",
    "url": "https://www.emergingtrajectories.com/lh/situational-awareness-bigger-picture/",
    "source": "cl42",
    "platform": "hackernews",
    "points": 70,
    "published_at": "2026-08-03T06:17:53+00:00",
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
    "id": "wscn:3778500",
    "domain": "股票",
    "title": "有色乘风起：地缘和利率仅是表象，供给短缺锚定三重驱动力",
    "url": "https://wallstreetcn.com/premium/articles/3778500?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T05:48:39+00:00",
    "summary": "下半年有色金属有望进入\"供给刚性锚定价格底部、三重需求驱动力（AI基建、能源转型、央行购金）打开向上空间\"的新阶段。"
  },
  {
    "id": "wscn:3778819",
    "domain": "股票",
    "title": "谷歌最重要的人，离职去做的“Loop”有多重要？",
    "url": "https://wallstreetcn.com/articles/3778819",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T05:48:21+00:00",
    "summary": "谷歌前首席科学家Jeff Dean等离职创办Discovery Loop。其核心“Loop”旨在实现科学方法的自动化，让AI自主闭环提出、执行并评估实验。其重要性在于：重塑了科研范式，推动AI走向“递归自我改进”（用AI研发AI），极大提升科学发现的效率。未来人类仅需设定目标，由AI主导无尽探索。"
  },
  {
    "id": "wscn:3778821",
    "domain": "股票",
    "title": "亚洲科技股承压，韩股跌超4%、SK海力士跌10%，金价升至近两月高位，油价走低",
    "url": "https://wallstreetcn.com/articles/3778821",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T05:47:29+00:00",
    "summary": "韩股下挫4.5%，SK海力士跌幅达10%，日经225指数跌1.6%，东证指数跌0.4%。日本铠侠下跌9%。闪迪盘后跌8%，西部数据暴跌12%，两家公司均刚刚发布财报。黄金上涨0.4%，报每盎司4260美元，创6月以来最高水平。"
  },
  {
    "id": "wscn:3778825",
    "domain": "股票",
    "title": "光量子计算公司图灵量子启动A股上市辅导",
    "url": "https://wallstreetcn.com/articles/3778825",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T05:42:54+00:00",
    "summary": "由上交教授创立。"
  },
  {
    "id": "wscn:3778822",
    "domain": "股票",
    "title": "韩日NAND竞争白热化：三星、铠侠同期量产最新规格AI存储芯片",
    "url": "https://wallstreetcn.com/articles/3778822",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T05:39:34+00:00",
    "summary": "铠侠凭超300层NAND及PCIe 6.0方案正面硬刚三星，三星则以破430层的V10工艺强势反击。韩日巨头巅峰对决正重塑NAND市场格局。"
  },
  {
    "id": "wscn:3778824",
    "domain": "股票",
    "title": "英伟达急寻中国AI基站供应商，明后年启动端侧算力组网",
    "url": "https://wallstreetcn.com/articles/3778824",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T05:37:55+00:00",
    "summary": "寻找端侧“中际旭创”！英伟达正急寻中国供应商开发6G AI基站，抢占AI 2.0边缘算力先机。目前其已结盟佳贤通信，年底将推样机。依托中国无可替代的基站供应链，此举有望撬动千亿美元级的AI-RAN蓝海市场。"
  },
  {
    "id": "wscn:3778820",
    "domain": "股票",
    "title": "大模型竞争白热化，张一鸣喊话：字节跳动“拒绝蒸馏”，不用别人输出换榜单排名",
    "url": "https://wallstreetcn.com/articles/3778820",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T05:28:52+00:00",
    "summary": "张一鸣在内部明确表态：字节跳动做模型须坚持长期主义，严禁“蒸馏”开源模型，拒绝用别人的输出换取一时榜单排名。他指出，蒸馏会干扰真正的长期技术突破，字节愿为此牺牲部分短期收益，内部已通过API检测等手段加强相关限制。"
  },
  {
    "id": "wscn:3778655",
    "domain": "股票",
    "title": "从极端回撤到阶段反弹，A股科技板块的4个关键信号是什么？",
    "url": "https://wallstreetcn.com/premium/articles/3778655?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T04:41:52+00:00",
    "summary": "7月创业板指、科创50分别下跌23.0%和25.9%，8月4日双创迎来显著反弹，这究竟只是极端跌幅后的技术性回补，还是科技行情重新启动的起点？判断答案不能只看AI产业景气，也不能机械套用“跌多必涨”的历史规律，而应同时回答四个问题：本轮下跌杀的是情绪、估值还是产业逻辑，融资盘与拥挤筹码是否真正出清，历史上的次月反弹能提供多大参考，以及市场能否重新回到由景气度和盈利预期驱动的定价逻辑？"
  },
  {
    "id": "wscn:3778805",
    "domain": "股票",
    "title": "创业板半日跌近0.7%，有色金属爆发，半导体材料再拉升，恒指、恒科指均跌超1%，AI大模型双雄逆势拉升",
    "url": "https://wallstreetcn.com/articles/3778805",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T04:02:29+00:00",
    "summary": "盘面上，个股跌多涨少，沪深京三市超3700股飘绿，上午半天成交1.77万亿。沪深两市半日成交额1.75万亿，较上个交易日放量600余亿。板块方面，AI应用、新能源车、光伏、锂电池、核电、机器人、特高压概念股跌幅靠前；半导体、工业金属、稳定币、PCB、CPO、商业航天题材活跃。"
  },
  {
    "id": "wscn:3778814",
    "domain": "股票",
    "title": "DeepSeek官宣涨价，且“幅度较大”！",
    "url": "https://wallstreetcn.com/articles/3778814",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T03:37:19+00:00",
    "summary": "DeepSeek宣布将大幅上调API定价，距其引入峰谷机制仅三周。背后是惊人的用量海啸——旗下V4 Flash单日消耗高达8万亿Token。与此同时，公司ARR已达4亿至5亿美元，正筹备500亿元融资。"
  },
  {
    "id": "wscn:3778816",
    "domain": "股票",
    "title": "历史一再重演？BTIG技术策略师：本轮科技股反弹与2000年泡沫顶部惊人相似",
    "url": "https://wallstreetcn.com/articles/3778816",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T03:37:09+00:00",
    "summary": "Krinsky警告，标普500走势、微软历史轨迹及半导体板块技术形态均现惊人镜像。他判断本轮反弹大概率止步于50日均线，届时受伤投资者将转为卖家。市场本质是存量资金\"抢椅子式\"轮动而非真正牛市，科技股动能耗尽后缺乏接棒力量。"
  },
  {
    "id": "wscn:3778817",
    "domain": "股票",
    "title": "金价一周暴涨250美元，黄金牛市回来了吗？",
    "url": "https://wallstreetcn.com/premium/articles/3778817?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T03:26:47+00:00",
    "summary": "一夜暴涨，金饰逼近1300元/克，黄金牛市杀回？受降息预期与央行扫货支撑，金价强劲反弹。但别急着去金店当“接盘侠”！警惕首饰高溢价，保值首选金条或ETF。切记：黄金只为压箱底，绝非暴富捷径，拒绝追高、分批定投才是普通人的淘金正道。"
  },
  {
    "id": "wscn:3778815",
    "domain": "股票",
    "title": "韩国杠杆ETF监管风暴：金融委员长、总统府政策室长相继遭刑事举报",
    "url": "https://wallstreetcn.com/articles/3778815",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T03:24:15+00:00",
    "summary": "韩国单一股票杠杆ETF风波持续发酵，矛头直指监管决策核心。金融委员会委员长李亿远、总统府政策室长金容范相继遭刑事举报，被指在选举前夕仓促推动高风险产品上市，疑似绕过压力测试等必要审核程序，致大量投资者受损。围绕这批杠杆ETF的监管合规性争议持续发酵，相关产品的后续命运亦存在不确定性。"
  },
  {
    "id": "wscn:3778813",
    "domain": "股票",
    "title": "SpaceX股价单日暴跌14%背后：机构抛售、散户接盘",
    "url": "https://wallstreetcn.com/articles/3778813",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T03:07:25+00:00",
    "summary": "SpaceX上市后首份财报引爆市场分歧——二季度资本支出逾180亿美元，较预期高出近40%，机构投资者闻风出逃，单日股价重挫13%；散户却在开盘首小时创纪录逆势抄底，买入额创纪录达2200万美元。同一份财报，机构看到的是现金流承压，散户押注的是AI长期壁垒。"
  },
  {
    "id": "wscn:3778806",
    "domain": "股票",
    "title": "TMT基金遭遇历史级重创！摩根大通：AI交易或将越来越依赖散户资金",
    "url": "https://wallstreetcn.com/articles/3778806",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T03:04:19+00:00",
    "summary": "摩根大通最新报告显示，TMT股票行业对冲基金7月单月亏损10.2%（不含Situational Awareness），为该类别有史以来最大单月跌幅。该行警告，此次重创将结构性压缩对冲基金持有科技仓位的能力，AI相关交易长期或将越来越依赖散户资金，更易受杠杆ETF和散户保证金账户的波动冲击。"
  },
  {
    "id": "wscn:3778747",
    "domain": "股票",
    "title": "1000亿美元干预之后：美日还有哪些工具？如何影响套利交易？",
    "url": "https://wallstreetcn.com/premium/articles/3778747?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T02:59:17+00:00",
    "summary": "美日千亿美元联合干预暂稳日元，但利差未改，贬值及套利将卷土重来，158后美日仍有多项工具可用。"
  },
  {
    "id": "wscn:3778808",
    "domain": "股票",
    "title": "详解存储长协：这轮周期的底部，已被抬至历史峰值之上",
    "url": "https://wallstreetcn.com/articles/3778808",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T02:53:58+00:00",
    "summary": "存储行业定价权正经历系统性重组。三星、SK海力士、美光、闪迪四大原厂同步将长协期限从一年拉至五年，产能锁定率从30%跃升至60%-70%，预付款规模高达数百亿美元。更关键的是，部分新合同价格保护单向倾斜——跌幅设底、涨幅无顶。即便价格跌至合同下限，毛利率仍远超历史任何一轮周期峰值。"
  },
  {
    "id": "wscn:3778804",
    "domain": "股票",
    "title": "黑客浪潮袭击华尔街：Point72、千禧、城堡等顶级对冲基金遭\"语音钓鱼\"攻击",
    "url": "https://wallstreetcn.com/articles/3778804",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T02:35:29+00:00",
    "summary": "Point72、千禧管理、城堡投资等华尔街顶级对冲基金近期集中遭遇\"语音钓鱼\"攻击——黑客借助AI模仿真人声音诱骗员工交出系统权限。安全专家警告，AI将攻击成本大幅压缩，单次定向攻击目标已从50个暴增至1000个，金融系统正面临前所未有的系统性风险。"
  },
  {
    "id": "wscn:3778809",
    "domain": "股票",
    "title": "铜博士最近为什么涨疯了？",
    "url": "https://wallstreetcn.com/articles/3778809",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T02:32:03+00:00",
    "summary": "每一次科技的跨越，背后都是一场资源的重新分配。全球“随时能提的铜”仅剩9.4万吨，只够全世界用一天多。美国为防加税疯狂囤货，仓库铜堆出百年纪录；矿端却告急，冶炼厂倒贴钱抢原料。铜价直逼历史高点，投行激辩多空，一场“铜战”正在上演。"
  },
  {
    "id": "wscn:3778807",
    "domain": "股票",
    "title": "央行独立性还在吗？报道：沃什上任后，多次与特朗普“私下通话”",
    "url": "https://wallstreetcn.com/articles/3778807",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T02:15:05+00:00",
    "summary": "据报道，沃什就任不足三个月，已多次与特朗普私下通话，话题涵盖伊朗战争经济影响与人工智能崛起。这一沟通模式打破了近年来总统与美联储主席之间保持正式、有限接触的惯例。上一次，白宫与美联储接触较为频繁，是1960年代尼克松对时任美联储主席伯恩斯施压，要求其在1972年大选前放松货币政策，此后通胀飙升。"
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
    "id": "hn:49145809",
    "domain": "股票",
    "title": "As Reddit stock falls, CEO questions value of Google's AI Overviews",
    "url": "https://arstechnica.com/ai/2026/08/reddit-ceo-on-ai-overviews-were-still-looking-for-that-win-win/",
    "source": "Brajeshwar",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-08-02T16:09:26+00:00",
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
    "id": "hn:49033778",
    "domain": "股票",
    "title": "Reality Bites Elon Musk and His Tesla, SpaceX Believers",
    "url": "https://www.wsj.com/finance/stocks/reality-bites-elon-musk-and-his-tesla-spacex-believers-1b639591",
    "source": "doener",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-07-24T10:59:51+00:00",
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
    "points": 331,
    "published_at": "2026-08-04T21:09:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:48878126",
    "domain": "金融",
    "title": "Under federal rule, colleges must leave grads better off or lose financial aid",
    "url": "https://www.npr.org/2026/06/30/nx-s1-5835631/turner-camhi-do-no-harm-college-loans",
    "source": "nradov",
    "platform": "hackernews",
    "points": 198,
    "published_at": "2026-07-12T04:00:14+00:00",
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
    "id": "hn:49174369",
    "domain": "金融",
    "title": "Waymo CEO explains why Tesla’s camera-only self-driving falls short",
    "url": "https://electrek.co/2026/08/04/waymo-co-ceo-camera-only-self-driving-tesla/",
    "source": "theanonymousone",
    "platform": "hackernews",
    "points": 42,
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
    "points": 41,
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
    "id": "hn:48826703",
    "domain": "金融",
    "title": "Is The Economist Always Wrong?",
    "url": "https://www.economist.com/interactive/finance-and-economics/2026/07/02/is-the-economist-always-wrong",
    "source": "nreece",
    "platform": "hackernews",
    "points": 138,
    "published_at": "2026-07-08T02:17:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:49182971",
    "domain": "金融",
    "title": "OpenAI settles claims of discrimination against US workers for $3.2M",
    "url": "https://finance.yahoo.com/technology/ai/articles/openai-settles-claims-discrimination-against-221429616.html",
    "source": "declan_roberts",
    "platform": "hackernews",
    "points": 24,
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
    "points": 19,
    "published_at": "2026-08-05T21:08:25+00:00",
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
    "id": "rss:https://arxiv.org/abs/2608.04023",
    "domain": "金融",
    "title": "Monsoon Mayhem to Market Waves: Forecasting Fisheries Resilience in Sri Lanka",
    "url": "https://arxiv.org/abs/2608.04023",
    "source": "Ruzaini Ahmed, Yohan Jayasinghe, Tharumini Gamage, Ifaz Ikram, Hasini Lawanya, Nirasha Munasinghe, Patalee Narasinghe, Nisansa de Silva, Sandareka Wickramanayake",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T04:00:00+00:00",
    "summary": "arXiv:2608.04023v1 Announce Type: new Abstract: Sri Lanka's fisheries sector is important for jobs and food supply. Between 2019 and 2025, it faced several major problems at the same time, and how the"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.04198",
    "domain": "金融",
    "title": "Does generative AI narrow education-based productivity gaps? Evidence from a randomized experiment",
    "url": "https://arxiv.org/abs/2608.04198",
    "source": "Guillermo Cruces (University of Nottingham), Diego Fernandez Meijide (Universidad de San Andres), Sebastian Galiani (Tulane University), Ramiro Galvez (UTDT), Maria Lombardi (UTDT)",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T04:00:00+00:00",
    "summary": "arXiv:2608.04198v1 Announce Type: new Abstract: Does generative artificial intelligence (AI) widen or narrow productivity gaps across workers? We study this in a randomized online experiment with 1,17"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.04200",
    "domain": "金融",
    "title": "From Financial Sentiment Classification to Return Predictability: A QLoRA Benchmark of Large Language Models",
    "url": "https://arxiv.org/abs/2608.04200",
    "source": "Fusheng Luo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T04:00:00+00:00",
    "summary": "arXiv:2608.04200v1 Announce Type: new Abstract: Financial sentiment classifiers are commonly evaluated against human labels, but strong linguistic performance does not necessarily imply economically u"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.04373",
    "domain": "金融",
    "title": "Public Trader Identity: Adverse Selection and Return Predictability",
    "url": "https://arxiv.org/abs/2608.04373",
    "source": "Daojing Zhai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T04:00:00+00:00",
    "summary": "arXiv:2608.04373v1 Announce Type: new Abstract: Informed traders are supposed to need anonymity: they profit by hiding among the uninformed. A decentralized exchange now publishes the counterparty: ev"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.04409",
    "domain": "金融",
    "title": "Quantifying Different Gains from Trade in Quality",
    "url": "https://arxiv.org/abs/2608.04409",
    "source": "Yuting Chen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T04:00:00+00:00",
    "summary": "arXiv:2608.04409v1 Announce Type: new Abstract: In this paper, I study to what extent countries differ in their preferences for quality and their technologies for improving quality. The paper also qua"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.04529",
    "domain": "金融",
    "title": "Low-rank and graphon limits for dynamic threshold distress contagion in heterogeneous financial networks",
    "url": "https://arxiv.org/abs/2608.04529",
    "source": "Pengbin Feng",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T04:00:00+00:00",
    "summary": "arXiv:2608.04529v1 Announce Type: new Abstract: We study a deterministic contagion model for a large population of financial institutions connected by a weighted directed exposure matrix. The sign con"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.04532",
    "domain": "金融",
    "title": "Optimal Life Insurance Decision in Mean-Variance DC Management with Mortality Improvements",
    "url": "https://arxiv.org/abs/2608.04532",
    "source": "Yueman Fen, Wenyuan Li, Mengyi Xu, Pengyu Wei",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T04:00:00+00:00",
    "summary": "arXiv:2608.04532v1 Announce Type: new Abstract: This paper studies the investment and insurance strategies of defined-contribution (DC) pension plans under the mean-variance framework. We consider a s"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.04547",
    "domain": "金融",
    "title": "Attributing Differences Between Forecast Runs to Input Changes, With Applications to CCAR and CECL Exercises",
    "url": "https://arxiv.org/abs/2608.04547",
    "source": "Xuan Mei, Junze Lin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T04:00:00+00:00",
    "summary": "arXiv:2608.04547v1 Announce Type: new Abstract: Forecasting systems used in the Comprehensive Capital Analysis and Review (CCAR) and Current Expected Credit Losses (CECL) processes combine portfolio d"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.04925",
    "domain": "金融",
    "title": "From Long to Short: How Interest Rates Shape Life Insurance Markets",
    "url": "https://arxiv.org/abs/2608.04925",
    "source": "Ziang Li, Derek Wenning",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T04:00:00+00:00",
    "summary": "arXiv:2608.04925v1 Announce Type: new Abstract: This paper explores how financial institutions pass interest rate risk through to product markets using the life insurance industry as a setting. We sho"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.04929",
    "domain": "金融",
    "title": "Open Information: A Defining Perspective on Web Datasets for Carbon Pricing",
    "url": "https://arxiv.org/abs/2608.04929",
    "source": "Sidharth Mallik, Anastasios Megaritis, Waymond Rodgers",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T04:00:00+00:00",
    "summary": "arXiv:2608.04929v1 Announce Type: new Abstract: The impact of web datasets on market prices has suggested the development of new sources of information, such as social media and web portals, indicatin"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.04977",
    "domain": "金融",
    "title": "The Role of Risk Sharing in Attenuating Business Cycles Within Currency Unions",
    "url": "https://arxiv.org/abs/2608.04977",
    "source": "Alberto Pavia, Christian Proebsting",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T04:00:00+00:00",
    "summary": "arXiv:2608.04977v1 Announce Type: new Abstract: The United States is a currency union where multiple risk-sharing mechanisms--- migration, fiscal transfers, income diversification and credit markets--"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.04987",
    "domain": "金融",
    "title": "Portfolio Allocation under Heterogeneous Scales and Multifractality",
    "url": "https://arxiv.org/abs/2608.04987",
    "source": "Shinji Kakinaka, Ken Umeno",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T04:00:00+00:00",
    "summary": "arXiv:2608.04987v1 Announce Type: new Abstract: Cross-correlations between financial signals are neither scale-free nor amplitude-independent: they vary with the time scale over which they are measure"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.04305",
    "domain": "金融",
    "title": "Adaptive Finite-Budget Training for CVaR Risk-Aware Q-Learning",
    "url": "https://arxiv.org/abs/2608.04305",
    "source": "Yifan Wu, Junjie Lei, Wenjie Huang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T04:00:00+00:00",
    "summary": "arXiv:2608.04305v1 Announce Type: cross Abstract: Risk-aware Q-learning (RaQL) provides a model-free, two-timescale estimator for dynamic risk objectives, but its finite-budget behavior remains fragil"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.04832",
    "domain": "金融",
    "title": "Robust Control under Stationary Ambiguity",
    "url": "https://arxiv.org/abs/2608.04832",
    "source": "Konrad J. Mueller, Amira Akkari, Ben Wood, Lukas Gonon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T04:00:00+00:00",
    "summary": "arXiv:2608.04832v1 Announce Type: cross Abstract: Control policies optimized in simulation can perform poorly in the real system when the parameters $x$ of the simulator are estimated from limited dat"
  },
  {
    "id": "rss:https://arxiv.org/abs/2404.13291",
    "domain": "金融",
    "title": "Optimal Design of Automated Market Makers on Decentralized Exchanges",
    "url": "https://arxiv.org/abs/2404.13291",
    "source": "Xue Dong He, Chen Yang, Yutian Zhou",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T04:00:00+00:00",
    "summary": "arXiv:2404.13291v4 Announce Type: replace Abstract: Automated market makers are a popular mechanism used on decentralized exchange, through which users trade assets with each other directly and automa"
  },
  {
    "id": "rss:https://arxiv.org/abs/2409.05194",
    "domain": "金融",
    "title": "Risk Measure Duality Without Structure",
    "url": "https://arxiv.org/abs/2409.05194",
    "source": "Vasily Melnikov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T04:00:00+00:00",
    "summary": "arXiv:2409.05194v3 Announce Type: replace Abstract: We study risk measures on vector spaces of random variables which a priori have little structure, such as spaces lacking law invariance or a lattice"
  },
  {
    "id": "rss:https://arxiv.org/abs/2412.18405",
    "domain": "金融",
    "title": "Generalized Mean Absolute Directional Loss for Machine Learning Trading Models",
    "url": "https://arxiv.org/abs/2412.18405",
    "source": "Jakub Micha\\'nk\\'ow, Pawe{\\l} Sakowski, Robert \\'Slepaczuk",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T04:00:00+00:00",
    "summary": "arXiv:2412.18405v2 Announce Type: replace Abstract: The article presents and evaluates a custom loss function designed specifically for machine learning models used in algorithmic trading. Regardless "
  },
  {
    "id": "rss:https://arxiv.org/abs/2507.07358",
    "domain": "金融",
    "title": "Variable annuities: A closer look at ratchet guarantees, hybrid contract designs, and taxation",
    "url": "https://arxiv.org/abs/2507.07358",
    "source": "Jennifer Alonso-Garcia, Len Patrick Dominic M. Garces, Jonathan Ziveyi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T04:00:00+00:00",
    "summary": "arXiv:2507.07358v2 Announce Type: replace Abstract: This paper investigates optimal withdrawal strategies and behavior of policyholders in a variable annuity (VA) contract with a guaranteed minimum wi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2508.16872",
    "domain": "金融",
    "title": "Population change, age structure, and socio-economic performance",
    "url": "https://arxiv.org/abs/2508.16872",
    "source": "Corey J. A. Bradshaw, Shana M. McDermott, Matthew E. Oliver",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T04:00:00+00:00",
    "summary": "arXiv:2508.16872v3 Announce Type: replace Abstract: Concerns about declining or ageing populations often centre on the possibility that fewer people or older age structures could weaken economies, str"
  },
  {
    "id": "rss:https://arxiv.org/abs/2510.20748",
    "domain": "金融",
    "title": "Reinforcement Learning and Consumption-Savings Behavior",
    "url": "https://arxiv.org/abs/2510.20748",
    "source": "Brandon Kaplowitz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T04:00:00+00:00",
    "summary": "arXiv:2510.20748v2 Announce Type: replace Abstract: This paper demonstrates how reinforcement learning can explain two puzzling empirical patterns in household consumption behavior during economic dow"
  },
  {
    "id": "rss:https://arxiv.org/abs/2512.22476",
    "domain": "金融",
    "title": "AutoQuant: An Auditable Expert-System Framework for Execution-Constrained Auto-Tuning in Cryptocurrency Perpetual Futures",
    "url": "https://arxiv.org/abs/2512.22476",
    "source": "Kaihong Deng",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T04:00:00+00:00",
    "summary": "arXiv:2512.22476v2 Announce Type: replace Abstract: Backtests of cryptocurrency perpetual futures are sensitive to execution timing, funding alignment, trading costs, and reuse of evaluation windows d"
  },
  {
    "id": "rss:https://arxiv.org/abs/2603.02187",
    "domain": "金融",
    "title": "Does the Market Anticipate? Can it? Should it?",
    "url": "https://arxiv.org/abs/2603.02187",
    "source": "Kangda Ken Wren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T04:00:00+00:00",
    "summary": "arXiv:2603.02187v5 Announce Type: replace Abstract: We explore a nuance to 'no arbitrage': it can be suboptimal to act upon an arbitrage immediately; in such cases optimised trading can suppress the a"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.16997",
    "domain": "金融",
    "title": "Hedging the Singularity",
    "url": "https://arxiv.org/abs/2604.16997",
    "source": "Andrew Y. Chen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T04:00:00+00:00",
    "summary": "arXiv:2604.16997v3 Announce Type: replace Abstract: AI stocks trade at extraordinary valuations. We develop an asset pricing model in which investors use AI stocks to hedge against an AI singularity t"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.25353",
    "domain": "金融",
    "title": "How Likely and How Deep? Sharp Joint Bounds on Risk-Neutral Crash Probability and Conditional Depth from Option Bid-Ask Quotes",
    "url": "https://arxiv.org/abs/2607.25353",
    "source": "Jirong Zhuang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T04:00:00+00:00",
    "summary": "arXiv:2607.25353v2 Announce Type: replace Abstract: Option quotes with bid-ask spreads do not point-identify the risk-neutral probability of a crash below a given threshold, nor the expected depth of "
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
    "points": 49,
    "published_at": "2026-07-28T12:19:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:49024958",
    "domain": "金融",
    "title": "DOT cranks up its campaign to strip bike lane references from federal websites",
    "url": "https://text.npr.org/nx-s1-5900901",
    "source": "Jtsummers",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-07-23T17:11:39+00:00",
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
    "id": "hn:49100970",
    "domain": "金融",
    "title": "Trump administration Is Repurposing Federal Land for A.I. Data Centers",
    "url": "https://www.nytimes.com/2026/07/29/climate/trump-federal-data-centers.html",
    "source": "cdrnsf",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-07-29T18:09:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:48880233",
    "domain": "金融",
    "title": "IT administrators are \"fed up\" with Microsoft's \"useless\" apps and Windows 11",
    "url": "https://www.neowin.net/news/it-admins-feel-overwhelmingly-sick-of-microsoft-and-windows-11-garbage-apps-products/",
    "source": "01-_-",
    "platform": "hackernews",
    "points": 46,
    "published_at": "2026-07-12T11:22:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:48824584",
    "domain": "金融",
    "title": "JPMorgan, BofA and Others Explore Buying Card Network to Raise Debit-Card Fees",
    "url": "https://www.wsj.com/finance/banking/jpmorgan-bank-of-america-and-other-banks-explore-a-deal-to-shake-up-payments-world-9d8639fb",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-07-07T22:04:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:49028304",
    "domain": "金融",
    "title": "US announces double-digit tariffs on most of globe to replace expiring duties",
    "url": "https://finance.yahoo.com/economy/policy/article/trump-administration-announces-the-next-phase-of-global-tariffs-with-10-to-125-rates-on-much-of-the-globe-210032314.html",
    "source": "ck2",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-07-23T21:28:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:49051055",
    "domain": "金融",
    "title": "Fedora 45 Atomic Desktops Look to Allow for Web-Based Remote Installations",
    "url": "https://www.phoronix.com/news/Fedora-45-Atomic-Remote-Install",
    "source": "nateb2022",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-07-25T20:10:00+00:00",
    "summary": ""
  },
  {
    "id": "hn:49047488",
    "domain": "金融",
    "title": "Stripe in talks to acquire OpenRouter in potential $10B deal, WSJ reports",
    "url": "https://finance.yahoo.com/technology/ai/articles/stripe-talks-acquire-openrouter-potential-215104525.html",
    "source": "nlpnerd",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-07-25T13:38:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:48953857",
    "domain": "金融",
    "title": "Nadella Blasts AI Industry's Double Standard",
    "url": "https://finance.biggo.com/news/438f299b-ca23-468d-b37d-0ffe09a4ca55",
    "source": "nittanymount",
    "platform": "hackernews",
    "points": 30,
    "published_at": "2026-07-18T00:28:46+00:00",
    "summary": ""
  },
  {
    "id": "hn:48999329",
    "domain": "金融",
    "title": "A Man Who Runs the IRS Spied on Colleagues When He Worked at JPMorgan",
    "url": "https://www.wsj.com/finance/banking/irs-bisignano-spying-jpmorgan-6cd1ddf0",
    "source": "cwwc",
    "platform": "hackernews",
    "points": 25,
    "published_at": "2026-07-21T22:40:46+00:00",
    "summary": ""
  }
]
```
