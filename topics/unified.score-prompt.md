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

- 今日日期：`2026-06-01`
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
  "date": "2026-06-01",
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
    "points": 1063018,
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
    "points": 865846,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1WBG9zgECp",
    "domain": "AI",
    "title": "史上最强 AI 编程工具免费啦！Cursor 保姆级使用教程！新手友好！看到就是赚到！｜ 集成 MCP ！",
    "url": "http://www.bilibili.com/video/av114426116120045",
    "source": "AfterShip",
    "platform": "bilibili",
    "points": 660091,
    "published_at": "2025-05-01T04:00:00+00:00",
    "summary": "相信你已经在网上刷到过不少的 AI 工具，但如果你让我推荐最值得我们每个人学习的一款 AI 工具，那绝对就是史上最强的 AI 编程工具 —— Cursor。为此，我们录制了一个保姆级的 Cursor 新手教程，在这里免费分享给大家。即使你是一个对 AI 完全 0 基础的新手小白，看完这个视频后，你也可以彻底了解 Cursor 这个软件，并知道如何从 0 到 1 用 Cursor 做出入门级的 AI"
  },
  {
    "id": "bvid:BV11NNAz5EKn",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！",
    "url": "http://www.bilibili.com/video/av116187623069851",
    "source": "AI-智能体搭建教程",
    "platform": "bilibili",
    "points": 564080,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1AnQNYxEsy",
    "domain": "AI",
    "title": "MCP是啥？技术原理是什么？一个视频搞懂MCP的一切。Windows系统配置MCP，Cursor Cline使用MCP",
    "url": "http://www.bilibili.com/video/av114155298228756",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 412222,
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
    "points": 382822,
    "published_at": "2025-03-22T04:02:08+00:00",
    "summary": "很多人都想学编程,但被高门槛劝退。本期给大家介绍一款零门槛的AI编程工具-豆包电脑版。通过3个实战案例,带你体验如何用AI轻松实现编程。\n\n豆包电脑版特点:\n- 中文界面,所见即所得\n- 支持html代码预览\n- 支持Python运行\n- 可生成完整项目代码\n- 历史版本管理\n- 代码一键导出\n\n时间戳\n00:00 为什么要学AI编程\n03:19 案例1:图片压缩网站实战\n04:15 案例2:数据"
  },
  {
    "id": "bvid:BV1eK5DzHEWu",
    "domain": "AI",
    "title": "MCP实战指南，mcp视频教程，2小时学透mcp",
    "url": "http://www.bilibili.com/video/av114380213586544",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 364928,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 310827,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1AHDuBoE2S",
    "domain": "AI",
    "title": "锐评vibe coding工具“从夯到拉”",
    "url": "http://www.bilibili.com/video/av116347090502349",
    "source": "布鲁歇一歇",
    "platform": "bilibili",
    "points": 229809,
    "published_at": "2026-04-04T15:19:25+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1qGc7zwEX6",
    "domain": "AI",
    "title": "史上最强 AI 编程工具Cursor来啦！Cursor保姆级使用教程！新手友好！看到就是赚到！！！",
    "url": "http://www.bilibili.com/video/av116061928226926",
    "source": "知名的阿呆同学",
    "platform": "bilibili",
    "points": 221258,
    "published_at": "2026-02-19T07:34:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 172949,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1Yi5M6DERk",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116560144369496",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 167612,
    "published_at": "2026-05-12T06:24:19+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 149580,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV16NvCBrEVs",
    "domain": "AI",
    "title": "什么是Vibe Coding，以及怎么使用？",
    "url": "http://www.bilibili.com/video/av115797133368973",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 140431,
    "published_at": "2025-12-28T12:36:33+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1RNTtzMENj",
    "domain": "AI",
    "title": "从零编写MCP并发布上线，超简单！手把手教程",
    "url": "http://www.bilibili.com/video/av114630814862349",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 140090,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV11urFBrEc4",
    "domain": "AI",
    "title": "🚀告别Vibe Coding！用Superpowers让Claude Code写出工程级代码，一次通过零报错！遵循TDD最佳实践！支持Codex",
    "url": "http://www.bilibili.com/video/av115877227860495",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 130376,
    "published_at": "2026-01-11T15:43:58+00:00",
    "summary": "🚀开发者必看！Superpowers把专业工程团队方法论固化成Skills，让Claude Code告别越写越乱的困境：规格驱动+代码质量双重保障！AI编程新范式！头脑风暴+计划+执行一条龙自动化\n\n\n🚀🚀🚀 视频简介：\n🎬 本期视频详细演示了开源AI编程工作流系统Superpowers的完整使用方法，并通过开发一款iOS时间线笔记原生应用来实测其效果。\n🔧 核心内容：\nSuperpowers工作"
  },
  {
    "id": "bvid:BV1fRSfBWE5X",
    "domain": "AI",
    "title": "vlog｜白天上班 晚上vibe coding，准备一个月上架我的第一款App！",
    "url": "http://www.bilibili.com/video/av116357526003120",
    "source": "chocpink_AI版",
    "platform": "bilibili",
    "points": 94301,
    "published_at": "2026-04-06T11:33:25+00:00",
    "summary": "想了很久终于开始了这件事——vibe coding！\n\n下面快速总结了我用到的一些工具：\nApptweak：竞品调研\nfigma make、google stitch、impeccable插件：生成UI页面\nfigma mcp/plugin：连接到cursor\npinterest/小红书/iconfont：找图片/icon素材\nGrok：生图、素材优化\ncursor+Xcode（swift）：落地"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 91841,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1KoGE6cE53",
    "domain": "AI",
    "title": "🚀Claude Code重大突破：Workflow功能完整实战教程！ultrawork召唤无数个Agent协同！自动生成JS脚本实现可复用的精准可控工作流",
    "url": "http://www.bilibili.com/video/av116629702777532",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 85581,
    "published_at": "2026-05-24T13:11:48+00:00",
    "summary": "视频简介：\n 全球首测！Anthropic未官宣的Claude Code Workflow隐藏功能完整使用指南，三大阶段六种形态精准解析！AI编程进入脚本化新纪元\n\n 本期视频详细演示了Anthropic为Claude Code V2.1.47和V2.1.48秘密新增的颠覆性Workflow功能！这个被官方从Changelog中紧急删除却未从代码中移除的&quot;隐藏神器&quot;，将成为继M"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 82992,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1KX9jB8E9M",
    "domain": "AI",
    "title": "【2026最新版】目前B站最全最细的 CurSor AI编程零基础全套教程，手把手教你搭建高效Cursor工作流，全程干货无废话！比付费效果强十倍",
    "url": "http://www.bilibili.com/video/av116328887225403",
    "source": "AI大模型技术教程",
    "platform": "bilibili",
    "points": 69823,
    "published_at": "2026-04-01T10:12:34+00:00",
    "summary": "视频配套文档课件笔记代码及AI大模型学习路线图戳这里获取→https://www.bilibili.com/read/cv41777105/?jump_opus=1"
  },
  {
    "id": "bvid:BV143wwz6E8F",
    "domain": "AI",
    "title": "Claude code科研使用展示与思路分享（提速就靠Ai）",
    "url": "http://www.bilibili.com/video/av116211882920985",
    "source": "科研推土机",
    "platform": "bilibili",
    "points": 62575,
    "published_at": "2026-03-11T18:12:00+00:00",
    "summary": "本期给大家带来的是Claude在Vscode的科研应用演示与我最近的一些心得使用心得，科研速度嘎嘎提升。论文复现画图、数据分析就靠Claude code。这个课程也是科研推土机「系统管理文献课程2.0」学员催我更新的内容，希望能帮助到大家～，这个视频重点讲两个事情：\n1️⃣ 资料获取，free不用怀疑，我是良心可言博主，，关注我(GZTSHNR)～\n2️⃣ 展示如何在VS code实操应用clau"
  },
  {
    "id": "bvid:BV12NK1zMESx",
    "domain": "AI",
    "title": "如何用Cursor开发大项目，全流程讲解，干货十足",
    "url": "http://www.bilibili.com/video/av114758657246726",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 57519,
    "published_at": "2025-06-28T02:37:22+00:00",
    "summary": "视频主题&amp;项目背景\n主题： 分享个人如何使用cursor 从0到1开发一个比较大的项目，使用的技术栈是vue+小程序+java\n项目\n一个B2B的订货商城及供应链全流程管理，包含的端有：\n小程序商城端\n供应商端\n仓储物流端\n司机配送端\n销售端\n后台管理系统\n以上小程序端都是使用webview的方式\n核心功能：\n商城的基本功能: 正逆向订单、商品、购物车、优惠券、积分、钱包、充值、工单等\n供"
  },
  {
    "id": "bvid:BV1XdFzz7Ei8",
    "domain": "AI",
    "title": "不写代码就能轻松开发应用？Cursor+Gemini 超强指挥官工作法！",
    "url": "http://www.bilibili.com/video/av116021511853604",
    "source": "PM刘搞定",
    "platform": "bilibili",
    "points": 55745,
    "published_at": "2026-02-06T03:17:18+00:00",
    "summary": "如何像传统互联网大厂一样指挥AI干活？本期视频通过一个“个人工作台”的实战项目，拆解了一套利用 LLM (Gemini) 辅助 Cursor 开发的高效工作流。\n\n核心内容：\n角色转换：你不是程序员，你是产品经理（PM）。\n文档驱动：如何用 AI 生成标准的产品文档 (PRD)、UI 文档和技术方案。\n避坑指南：如何防止 Cursor “手搓核弹”或开发中途“失忆”。\n\n实操流程：\nStep 1："
  },
  {
    "id": "bvid:BV1ZjDYB7Eam",
    "domain": "AI",
    "title": "从 0 到 1：6小时掌握 Vibe Coding！ Claude Code ＋ AI 这支影片直接让你超越 90% AI 玩家",
    "url": "http://www.bilibili.com/video/av116362122894759",
    "source": "李哈利Harry",
    "platform": "bilibili",
    "points": 50955,
    "published_at": "2026-04-08T11:00:00+00:00",
    "summary": "🌟 加入AI大师社群并运用AI创业赚钱：https://www.skool.com/aiagent/about?ref=f2b566934c5c4639aaa47ab1fe39310e\n📌 加入我的免费 Skool 社群，获取模板：https://www.skool.com/aiagent8/about?ref=f2b566934c5c4639aaa47ab1fe39310e\n\n🚧 开始使用 n8"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 50177,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV13K1YBtE6e",
    "domain": "AI",
    "title": "【GMM】MCP 使用说明",
    "url": "http://www.bilibili.com/video/av115485010168640",
    "source": "3DM小莫",
    "platform": "bilibili",
    "points": 35559,
    "published_at": "2025-11-03T09:19:08+00:00",
    "summary": "MCP 支持 是 Gloss Mod Manager（GMM ）在 1.62.0 新增的一个功能， 你需要至少更新到 1.62 才能使用此功能；\n\n你可以使用任何支持 MCP 的客户端 和 AI 使用它, 但建议你的 AI 最大 Token 至少有 32K, 否则部分功能可能会受影响。\n\n相关代码已经开源，欢迎参与维护:  https://github.com/GlossMod/Gloss-Mod"
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 33243,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 29476,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV1ap2fBvEt9",
    "domain": "AI",
    "title": "如何使用「Operit AI」：你的下一代AI手机助手",
    "url": "http://www.bilibili.com/video/av115677243447909",
    "source": "默睦",
    "platform": "bilibili",
    "points": 28775,
    "published_at": "2025-12-07T08:06:42+00:00",
    "summary": "下载地址：https://github.com/AAswordman/Operit\n\n相关软件资料下载：https://www.123pan.com/s/IKgAjv-Hinsv.html\n\n官方交流群：458862019"
  },
  {
    "id": "bvid:BV1e7VA6vEJU",
    "domain": "AI",
    "title": "【2026最新】绝对是B站No.1的Claude Code教程：国内安装+实战开发案例+个人使用心得总结，手把手带你拥抱Vibe Coding！",
    "url": "http://www.bilibili.com/video/av116640356304890",
    "source": "码士集团-马小安",
    "platform": "bilibili",
    "points": 26768,
    "published_at": "2026-05-26T10:22:46+00:00",
    "summary": "绝对是B站No.1的Claude Code教程：国内安装+实战开发案例+个人使用心得总结，手把手带你拥抱Vibe Coding！\n配套课件笔记/PPT已备好，另外有需要AI大模型学习路线图+必看书籍（国内外大牛著作）+入门及进阶视频教程+项目实战及源码提供+面试实战场景题移步评论置顶即可~"
  },
  {
    "id": "bvid:BV116P7zXEkE",
    "domain": "AI",
    "title": "纯小白教学：用vibecoding做个人网站",
    "url": "http://www.bilibili.com/video/av116160209093711",
    "source": "阿囤囤-庞滚滚",
    "platform": "bilibili",
    "points": 24173,
    "published_at": "2026-03-02T15:11:36+00:00",
    "summary": "不需要🪜哦～"
  },
  {
    "id": "bvid:BV11K9gBqEnW",
    "domain": "AI",
    "title": "【杀戮尖塔2】AI MOD 配置教程第一期来辣！手把手教你怎么改提示词！以及如何设计自己的爬塔玩法",
    "url": "http://www.bilibili.com/video/av116341654755924",
    "source": "分歧点WhatIf",
    "platform": "bilibili",
    "points": 22010,
    "published_at": "2026-04-03T16:14:43+00:00",
    "summary": "每个参数都是干什么的，如何修改提示词的教程。\n不知道这是什么？请看合集内的视频~\n我做了一个 AI 的杀戮尖塔2MOD！\n可以和怪物对话，策反怪物，带着怪物爬塔（重写了几乎每一个怪物在友方时候的行为），还能给怪物打防御，带个沙虫全吃了！\n可以和上古之民对话，聊嗨了会给你 1～2 个额外赐福，还能帮你指示为未来\n可以让偷窃草蜢偷队友的 key 卡，想无限？偷了！\n可以和商人讨价还价，甚至白嫖\n多人的"
  },
  {
    "id": "bvid:BV1htCnY4ET6",
    "domain": "AI",
    "title": "用 Cursor AI 写 flutter 直接喂设计图就行 | flutter教程",
    "url": "http://www.bilibili.com/video/av113723805008238",
    "source": "独立开发者_猫哥",
    "platform": "bilibili",
    "points": 17640,
    "published_at": "2024-12-27T08:21:35+00:00",
    "summary": "✏️【关于本期视频】\n在上一篇文章《Flutter 使用 Cursor 和 Figma 快速生成界面代码》中，有同学提到他直接使用了设计稿的图片进行生成。我试了一下，效果确实很好。因此，我整理了一些文档，希望对大家有所帮助。\n下图展示了我没有手动编写任何代码实现的消息首页，支持上下滑动刷新数据。\n👉 文档 https://ducafecat.com/blog/use-cursor-ai-flutt"
  },
  {
    "id": "bvid:BV1NYVG6jEKE",
    "domain": "AI",
    "title": "Claude Code保姆级在国内从安装到代码实战教程，10分钟入门精通",
    "url": "http://www.bilibili.com/video/av116662133132089",
    "source": "字节软件测试",
    "platform": "bilibili",
    "points": 17116,
    "published_at": "2026-05-30T06:39:27+00:00",
    "summary": "Claude Code保姆级在国内从安装到代码实战教程，10分钟入门精通"
  },
  {
    "id": "bvid:BV1XxXpBEEHU",
    "domain": "AI",
    "title": "Claude Code远程开发终极方案！手机改代码+实时预览~【小白教程】",
    "url": "http://www.bilibili.com/video/av116294326230438",
    "source": "爱听书的程序员阿超",
    "platform": "bilibili",
    "points": 16937,
    "published_at": "2026-03-26T12:00:00+00:00",
    "summary": "之前，我一直在研究怎么远程使用 Claude Code 开发项目，并且能实时预览效果。但是一直都没有找到合适的解决方案，要么就是给一个临时公网链接预览，每次都需要再配置，要么就是购买云服务器来配置，都感觉挺麻烦的~\n\n最近，我发现这个蒲公英异地组网的方案，用来做远程开发 Claude Code 项目，感觉非常方便，不仅能修改代码，而且我实时预览的需求也很好的满足了。\n\n这样我随时随地都可以用 AI"
  },
  {
    "id": "bvid:BV1hnjGzLE14",
    "domain": "AI",
    "title": "【小智教程】手挽手教你如何接入别人的MCP服务",
    "url": "http://www.bilibili.com/video/av114568722450105",
    "source": "空白泡泡糖果",
    "platform": "bilibili",
    "points": 16888,
    "published_at": "2025-05-25T13:36:25+00:00",
    "summary": "文档：https://icnt94i5ctj4.feishu.cn/docx/ZkR3d1lfUosIFCx4qWJcI4QunY0\nshay大佬的HA SSE接入文档：https://bbs.hassbian.com/thread-29314-1-1.html"
  },
  {
    "id": "bvid:BV1WtoTBiEuR",
    "domain": "AI",
    "title": "Claude Code多Agent模式实战分享",
    "url": "http://www.bilibili.com/video/av116454666012312",
    "source": "Simon林_",
    "platform": "bilibili",
    "points": 13626,
    "published_at": "2026-04-23T15:18:08+00:00",
    "summary": "Claude Code有2种多Agent模式：多个subagents模式和多个独立agent模式"
  },
  {
    "id": "bvid:BV1ZHAozLE7b",
    "domain": "AI",
    "title": "【SynthPilot】全网首发！2026年最新基于AI的FPGA开发教程，Agent自主编程/调试全链路闭环，500+工具接入Vivado",
    "url": "http://www.bilibili.com/video/av116164755790661",
    "source": "晓川科研站",
    "platform": "bilibili",
    "points": 12758,
    "published_at": "2026-03-03T10:26:33+00:00",
    "summary": "全网首个AI Agent FPGA开发教程。SynthPilot通过MCP协议打通Vivado全链路，AI自主写码、综合、读报告、改Bug、迭代——真正的Agent模式闭环开发。从零开始，带你见证FPGA开发方式的代际变革。\n获取工具:synthpilot.dev\n晓川交流群:1007696121"
  },
  {
    "id": "bvid:BV18TZYY8EuJ",
    "domain": "AI",
    "title": "微软最新AI Agent入门课程 • 中英",
    "url": "http://www.bilibili.com/video/av114246130076146",
    "source": "Mindofuture",
    "platform": "bilibili",
    "points": 12607,
    "published_at": "2025-03-30T02:06:00+00:00",
    "summary": "在这门包含10节课的课程中，我们将带你从概念到代码，全面覆盖构建AI代理的基础知识。在这里找到完整的“AI代理入门”课程及代码示例\nhttps://github.com/microsoft/ai-agents-for-beginners\n\nP01 什么是AI代理\nP02 使用哪种AI代理框架\nP03 如何设计优秀的AI代理\nP04 什么是代理工具使用设计模式\nP05 什么是代理式RAG\nP06 如"
  },
  {
    "id": "bvid:BV165dAYxEdD",
    "domain": "AI",
    "title": "只需几行代码用Java写一个MCP服务！从0到1开发MCP服务！",
    "url": "http://www.bilibili.com/video/av114306863598282",
    "source": "图灵诸葛官方号",
    "platform": "bilibili",
    "points": 12173,
    "published_at": "2025-04-09T07:43:00+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持~\r\n本视频配套资料戳这里获取→https://www.bilibili.com/read/cv38661345/\r\n【还可额外领取100w字Java面试宝典】"
  },
  {
    "id": "bvid:BV1yT8qzMEbd",
    "domain": "AI",
    "title": "基于SpringAI开发Java版mcp服务",
    "url": "http://www.bilibili.com/video/av114942720148945",
    "source": "程序员Cafe",
    "platform": "bilibili",
    "points": 11061,
    "published_at": "2025-07-30T15:05:27+00:00",
    "summary": "如何用Java开发一个mcp服务？如何把已有的spingboot微服务改造成mcp服务呢？如何在mcp客户端调用mcp服务？\n今天来一个保姆级教学"
  },
  {
    "id": "bvid:BV1oNVH6xEWS",
    "domain": "AI",
    "title": "Claude Code 国内直连保姆级教程｜10分钟从入门到精通，原理+安装+实战全覆盖，解锁Vibe Coding编程新范式",
    "url": "http://www.bilibili.com/video/av116667602503393",
    "source": "码士集团-小晨晨晨",
    "platform": "bilibili",
    "points": 9489,
    "published_at": "2026-05-31T06:14:34+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1VCVS6PEAd",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent零基础全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116668525186915",
    "source": "大模型入门教程",
    "platform": "bilibili",
    "points": 9128,
    "published_at": "2026-05-31T09:46:57+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 8900,
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
    "points": 7922,
    "published_at": "2025-06-04T07:08:58+00:00",
    "summary": "全程干货无废话！MCP最新实战教程，从环境部署、原理详解到项目实战，带你彻底吃透MCP！MCPServer开发，mcp开发，mcp教程，mcp项目 完整视频教程+讲解课件+学习笔记+AI大模型知识库已打包可分享！"
  },
  {
    "id": "bvid:BV1oUVc6vEEY",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的 AI 编程工具Cursor保姆级教程！Cursor保姆级安装使用教程！新手友好！看到就是赚到！！！",
    "url": "http://www.bilibili.com/video/av116639383159883",
    "source": "AI大模型教学",
    "platform": "bilibili",
    "points": 6489,
    "published_at": "2026-05-26T06:24:36+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1DUEDz4EhM",
    "domain": "AI",
    "title": "blender mcp 安装教程 适用于 mac 和 window, 使用 trae 编辑器",
    "url": "http://www.bilibili.com/video/av114532416487683",
    "source": "能吃两个西瓜",
    "platform": "bilibili",
    "points": 6436,
    "published_at": "2025-05-19T03:44:27+00:00",
    "summary": "网上基本都是 cursor 为主,  咱们用国产编辑器 trae 来尝试"
  },
  {
    "id": "bvid:BV1uZVJ6GEjB",
    "domain": "AI",
    "title": "目前B站讲的最好的AI Agent智能体开发全套教程，手把手教你快速搭建自己的智能体！全程干货无废话！学完即就业，让你少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av116668072201170",
    "source": "阿里架构师诸葛",
    "platform": "bilibili",
    "points": 6321,
    "published_at": "2026-05-31T07:53:46+00:00",
    "summary": "目前B站讲的最好的AI Agent智能体开发全套教程，手把手教你快速搭建自己的智能体！全程干货无废话！学完即就业，让你少走99%的弯路！"
  },
  {
    "id": "bvid:BV1fNs9eiEm9",
    "domain": "AI",
    "title": "Cursor AI编程结合cocos3.8游戏开发教程-01",
    "url": "http://www.bilibili.com/video/av113187471105975",
    "source": "太阳8800",
    "platform": "bilibili",
    "points": 6324,
    "published_at": "2024-09-23T15:15:13+00:00",
    "summary": "开源源码仓库\nhttps://gitee.com/gamepublic/chess-cards"
  },
  {
    "id": "hn:48352939",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia RTX Spark",
    "url": "https://www.nvidia.com/en-us/products/rtx-spark/",
    "source": "shenli3514",
    "platform": "hackernews",
    "points": 106,
    "published_at": "2026-06-01T05:24:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:48356654",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Cosmos 3",
    "url": "https://developer.nvidia.com/blog/develop-physical-ai-reasoning-world-and-action-models-with-nvidia-cosmos-3/",
    "source": "tosh",
    "platform": "hackernews",
    "points": 101,
    "published_at": "2026-06-01T13:32:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:48356312",
    "domain": "AI 算力 / 半导体",
    "title": "Launch HN: Expanse (YC P26) – Unlock Wasted GPU Capacity",
    "url": "https://news.ycombinator.com/item?id=48356312",
    "source": "ismaeel_bashir",
    "platform": "hackernews",
    "points": 45,
    "published_at": "2026-06-01T13:05:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:48355720",
    "domain": "AI 算力 / 半导体",
    "title": "MacBook Pro Rival with the Nvidia Powered Surface Laptop Ultra",
    "url": "https://www.windowslatest.com/2026/06/01/microsoft-builds-its-ultimate-macbook-pro-rival-with-the-nvidia-powered-surface-laptop-ultra/",
    "source": "jbk",
    "platform": "hackernews",
    "points": 44,
    "published_at": "2026-06-01T12:04:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:48354967",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia announces new AI chip for personal computers",
    "url": "https://www.bbc.com/news/articles/crmp9mppvzro",
    "source": "rishikeshs",
    "platform": "hackernews",
    "points": 42,
    "published_at": "2026-06-01T10:33:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:48352693",
    "domain": "AI 算力 / 半导体",
    "title": "A powerful new chapter for Windows PCs, accelerated by Nvidia RTX Spark",
    "url": "https://blogs.windows.com/windowsexperience/2026/05/31/introducing-a-powerful-new-chapter-for-windows-pcs-accelerated-by-nvidia-rtx-spark/",
    "source": "WalterSobchak",
    "platform": "hackernews",
    "points": 31,
    "published_at": "2026-06-01T04:45:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:48012477",
    "domain": "AI 算力 / 半导体",
    "title": "Offenders sentenced up to 10 years for spying on TSMC",
    "url": "https://www.taipeitimes.com/News/front/archives/2026/04/28/2003856358",
    "source": "ironyman",
    "platform": "hackernews",
    "points": 127,
    "published_at": "2026-05-04T18:04:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:48234574",
    "domain": "AI 算力 / 半导体",
    "title": "How do you build a semiconductor company on something that's free?",
    "url": "https://www.siliconimist.com/p/the-open-source-silicon-business",
    "source": "johncole",
    "platform": "hackernews",
    "points": 99,
    "published_at": "2026-05-22T11:49:04+00:00",
    "summary": ""
  },
  {
    "id": "hn:48352951",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Announces RTX Spark",
    "url": "https://www.theverge.com/tech/940589/nvidia-rtx-spark-n1-n1x-laptop-desktop-pc-cpu-gpu-ai-release-date",
    "source": "rayhaanj",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-06-01T05:26:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:48220446",
    "domain": "AI 算力 / 半导体",
    "title": "IBM invented semiconductor manufacturing automation",
    "url": "https://spectrum.ieee.org/semiconductor-fabrication",
    "source": "rbanffy",
    "platform": "hackernews",
    "points": 81,
    "published_at": "2026-05-21T10:39:48+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/early-memory-contention-checks-reduce-ic-design-risks/",
    "domain": "AI 算力 / 半导体",
    "title": "Early Memory Contention Checks Reduce IC Design Risks",
    "url": "https://www.eetimes.com/early-memory-contention-checks-reduce-ic-design-risks/",
    "source": "Chun-hsiang Chang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T14:00:00+00:00",
    "summary": "Automated schematic-level contention analysis detects memory bottlenecks early, improving SoC reliability, predictability, and silicon quality. The post Early Memory Contention Checks Reduce IC Design"
  },
  {
    "id": "rss:https://www.eetimes.com/high-voltage-gan-bi-directional-switches-strong-performance-simpler-to-use/",
    "domain": "AI 算力 / 半导体",
    "title": "High-Voltage GaN Bi-Directional Switches: Strong Performance, Simpler to Use",
    "url": "https://www.eetimes.com/high-voltage-gan-bi-directional-switches-strong-performance-simpler-to-use/",
    "source": "Renesas",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T14:00:00+00:00",
    "summary": "The demand for more efficient power solutions continues to put pressure on designers to optimize system design without compromising performance. Read how you can simplify high-voltage power conversion"
  },
  {
    "id": "rss:https://www.eetimes.com/product-recall-management-guide-for-electronics-manufacturing-smbs/",
    "domain": "AI 算力 / 半导体",
    "title": "Product Recall Management Guide for Electronics Manufacturing SMBs",
    "url": "https://www.eetimes.com/product-recall-management-guide-for-electronics-manufacturing-smbs/",
    "source": "MRPeasy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T13:00:00+00:00",
    "summary": "This guide explains what product recalls are, what risks they create, and how small and midsize manufacturers can handle them in an organized way. The post Product Recall Management Guide for Electron"
  },
  {
    "id": "rss:https://www.eetimes.com/ai-accelerated-software-security-vulnerability-discovery-is-hardware-next/",
    "domain": "AI 算力 / 半导体",
    "title": "AI-Accelerated Software Security Vulnerability Discovery: Is Hardware Next?",
    "url": "https://www.eetimes.com/ai-accelerated-software-security-vulnerability-discovery-is-hardware-next/",
    "source": "Andreas Kuehlmann, General Manager – Security Solutions, Arteris",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T13:00:00+00:00",
    "summary": "AI is revolutionizing software vulnerability discovery. Could hardware security be next? Explore risks, AI threats and chip defense strategies. In depth. The post AI-Accelerated Software Security Vuln"
  },
  {
    "id": "rss:https://www.eetimes.com/nikon-leveraging-arf-scanner-price-to-challenge-asml/",
    "domain": "AI 算力 / 半导体",
    "title": "Nikon Leveraging ArF Scanner Price to Challenge ASML",
    "url": "https://www.eetimes.com/nikon-leveraging-arf-scanner-price-to-challenge-asml/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T11:57:55+00:00",
    "summary": "The Japanese litho firm is lowering the price of its ArF tools while also launching a brand-new immersion platform by 2028. The post Nikon Leveraging ArF Scanner Price to Challenge ASML appeared first"
  },
  {
    "id": "rss:https://www.eetimes.com/beyond-the-factory-floor-xr-training-for-the-next-industrial-era/",
    "domain": "AI 算力 / 半导体",
    "title": "Beyond the Factory Floor: XR Training for the Next Industrial Era",
    "url": "https://www.eetimes.com/beyond-the-factory-floor-xr-training-for-the-next-industrial-era/",
    "source": "Rebecca Pool",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T07:30:00+00:00",
    "summary": "EU-funded project MASTER is using extended reality to transform how industrial robotics is taught and deployed. The post Beyond the Factory Floor: XR Training for the Next Industrial Era appeared firs"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/computex-2026-day-zero-wrap-up-nvidia-launches-rtx-spark-superchip-assault-on-laptop-and-desktop-markets-intel-readies-xeon-6",
    "domain": "AI 算力 / 半导体",
    "title": "Computex 2026 Day Zero Wrap-Up: Nvidia launches RTX Spark Superchip assault on laptop and desktop markets, Intel readies Xeon 6+",
    "url": "https://www.tomshardware.com/tech-industry/computex-2026-day-zero-wrap-up-nvidia-launches-rtx-spark-superchip-assault-on-laptop-and-desktop-markets-intel-readies-xeon-6",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T16:26:24+00:00",
    "summary": "Here's the best of what was announced during the opening hours of Computex 2026"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/nvidia-enters-the-windows-pc-market-with-rtx-spark",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's RTX Spark could caplitalize where Qualcomm's Arm-based efforts have not — following the expiration of Qualcomm's Windows on Arm deal, Nvidia stands poised to pick up the slack",
    "url": "https://www.tomshardware.com/laptops/nvidia-enters-the-windows-pc-market-with-rtx-spark",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T16:16:28+00:00",
    "summary": "Nvidia unveiled the RTX Spark superchip on May 31st ahead of its GTC Taipei event, putting a 20-core Arm-based Grace CPU and a Blackwell RTX GPU on a single package."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/qualcomm-aims-snapdragon-c-at-300-laptops-as-memory-costs-gut-the-budget-segment",
    "domain": "AI 算力 / 半导体",
    "title": "Qualcomm aims Snapdragon C laptop chip at the budget laptop segment, as manufacturers feel the DRAM squeeze — analysts warn sub $500 laptop market may disappear before 2028",
    "url": "https://www.tomshardware.com/laptops/qualcomm-aims-snapdragon-c-at-300-laptops-as-memory-costs-gut-the-budget-segment",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T16:00:00+00:00",
    "summary": "Qualcomm announced the Snapdragon C Platform on May 28th, ahead of Computex 2026 in Taipei."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/access-toms-hardware-premiums-computex-2026-coverage-for-free-sign-up-for-an-account-to-read-insider-reports-from-the-show",
    "domain": "AI 算力 / 半导体",
    "title": "Access Tom’s Hardware Premium’s Computex 2026 coverage for free — sign up for an account to read insider reports from the show",
    "url": "https://www.tomshardware.com/tech-industry/access-toms-hardware-premiums-computex-2026-coverage-for-free-sign-up-for-an-account-to-read-insider-reports-from-the-show",
    "source": "The Editors of Tom&#039;s Hardware",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T15:39:08+00:00",
    "summary": "For a limited time, you’ll be able to read all of our latest reports from Computex 2026 with a Tom’s Hardware account, no payment required."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/asus-world-first-oled-esports-monitor-can-hit-540hz-at-1080p-rog-strix-oled-model-among-four-fresh-offerings",
    "domain": "AI 算力 / 半导体",
    "title": "Asus' world-first OLED esports monitor can hit 540Hz at 1080p — ROG Strix OLED model among four fresh offerings",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/asus-world-first-oled-esports-monitor-can-hit-540hz-at-1080p-rog-strix-oled-model-among-four-fresh-offerings",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T15:05:20+00:00",
    "summary": "Three of Asus’ new ROG monitors use OLED panels, while the fourth leverages “Fast IPS”"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/asus-rolls-out-a-rog-20th-anniversary-chair-and-backpack-alongside-commemorative-components-and-peripherals-rog-destrier-edition-20-rog-slash-hard-case-luggage-edition-20-are-back-in-black-and-gold",
    "domain": "AI 算力 / 半导体",
    "title": "Asus rolls out a ROG 20th anniversary chair and backpack, alongside commemorative components and peripherals — ROG Destrier Edition 20, ROG SLASH Hard-case Luggage Edition 20 are back in black (and go",
    "url": "https://www.tomshardware.com/peripherals/asus-rolls-out-a-rog-20th-anniversary-chair-and-backpack-alongside-commemorative-components-and-peripherals-rog-destrier-edition-20-rog-slash-hard-case-luggage-edition-20-are-back-in-black-and-gold",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T14:26:18+00:00",
    "summary": "Apart from hardware, Asus’s ROG 20th anniversary products include a Destreir Edition 20 gaming chair and gold-accented luggage and backpacks."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/seven-hospitalized-after-toxic-gas-fire-at-sk-hynix-advanced-memory-plant-cheongju-4th-campus-incident-today-led-to-all-3-600-staff-being-evacuated",
    "domain": "AI 算力 / 半导体",
    "title": "Seven hospitalized after toxic gas fire at SK hynix advanced memory plant — Cheongju 4th campus incident today led to all 3,600 staff being evacuated",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/seven-hospitalized-after-toxic-gas-fire-at-sk-hynix-advanced-memory-plant-cheongju-4th-campus-incident-today-led-to-all-3-600-staff-being-evacuated",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T14:04:50+00:00",
    "summary": "Thousands of SK hynix employees fled their factory stations earlier today as a fire broke out in a room where fluorine gas was used."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/bambu-lab-launches-big-bed-slinger-a2l-companys-h2s-lite-is-half-the-cost-of-h2s-at-just-usd469",
    "domain": "AI 算力 / 半导体",
    "title": "Bambu Lab Launches Big Bed Slinger: A2L — company's 'H2S Lite' is half the cost of H2S at just $469",
    "url": "https://www.tomshardware.com/3d-printing/bambu-lab-launches-big-bed-slinger-a2l-companys-h2s-lite-is-half-the-cost-of-h2s-at-just-usd469",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T14:00:00+00:00",
    "summary": "Or get the combo for $569"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/256gb-of-dual-channel-ram-hits-mass-market-thanks-to-origin-code-quad-rank-cudimm-packs-128gb-of-ddr5-8000-into-a-single-module",
    "domain": "AI 算力 / 半导体",
    "title": "256GB of dual-channel RAM hits mass market thanks to Origin Code — quad-rank CUDIMM packs 128GB of DDR5-8000 into a single module",
    "url": "https://www.tomshardware.com/pc-components/ram/256gb-of-dual-channel-ram-hits-mass-market-thanks-to-origin-code-quad-rank-cudimm-packs-128gb-of-ddr5-8000-into-a-single-module",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T13:36:00+00:00",
    "summary": "Origin Code reveals the brand's Vortex 4R DDR5-8000 256GB (2x128GB) CUDIMM memory kits at Computex 2025."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/toms-hardware-unfiltered-computex-2026-day-0-peek-behind-the-curtain-to-see-how-were-covering-the-biggest-trade-show-of-the-year",
    "domain": "AI 算力 / 半导体",
    "title": "Tom's Hardware Unfiltered: Computex 2026, Day 0 — peek behind the curtain to see how we're covering the biggest trade show of the year",
    "url": "https://www.tomshardware.com/tech-industry/toms-hardware-unfiltered-computex-2026-day-0-peek-behind-the-curtain-to-see-how-were-covering-the-biggest-trade-show-of-the-year",
    "source": "Paul Alcorn",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T13:00:00+00:00",
    "summary": "Our team is on the ground in Taipei for Computex 2026. For the first time, we're peeling back the curtain to show you exactly how we're covering it, documenting our trials and tribulations during the "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/nvidia-says-rtx-spark-chip-will-support-all-major-anti-cheat-and-drm-technologies-fortnite-valorant-denuvo-and-more-to-work-natively-with-windows-on-arm",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia says RTX Spark chip will support all major anti-cheat and DRM technologies — Fortnite, Valorant, Denuvo, and more to work natively with Windows on Arm",
    "url": "https://www.tomshardware.com/pc-components/cpus/nvidia-says-rtx-spark-chip-will-support-all-major-anti-cheat-and-drm-technologies-fortnite-valorant-denuvo-and-more-to-work-natively-with-windows-on-arm",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T12:37:07+00:00",
    "summary": "Microsoft and Nvidia are working together to bring popular anti-cheat software to the new RTX Spark chip, allowing support for all major multiplayer games. So far, Fortnite is the only game that runs "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/asus-monstrous-rog-astral-geforce-rtx-5090-edition-20-includes-expansive-curved-amoled-display-also-debuts-3-000w-power-supply-and-striking-pc-case",
    "domain": "AI 算力 / 半导体",
    "title": "Asus' monstrous ROG Astral GeForce RTX 5090 Edition 20 includes expansive curved AMOLED display — also debuts 3,000W power supply and striking PC case",
    "url": "https://www.tomshardware.com/pc-components/gpus/asus-monstrous-rog-astral-geforce-rtx-5090-edition-20-includes-expansive-curved-amoled-display-also-debuts-3-000w-power-supply-and-striking-pc-case",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T12:35:43+00:00",
    "summary": "Asus has used its Computex press event to showcase a huge celebration of its ROG gaming sub-brand with commemorative gear including the Asus ROG Astral GeForce RTX 5090 Edition 20."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/servers/supermicro-shows-off-vera-rubin-nvl72-rack-with-all-new-type-of-coolant-company-claims-coolant-offers-1-000-times-higher-electrical-impedance-over-standard-cooling",
    "domain": "AI 算力 / 半导体",
    "title": "Supermicro shows off Vera Rubin NVL72 rack with all-new type of coolant — company claims coolant offers 1,000 times higher electrical impedance over standard cooling",
    "url": "https://www.tomshardware.com/desktops/servers/supermicro-shows-off-vera-rubin-nvl72-rack-with-all-new-type-of-coolant-company-claims-coolant-offers-1-000-times-higher-electrical-impedance-over-standard-cooling",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T12:02:07+00:00",
    "summary": "Supermicro demonstrates upcoming servers based on AMD’s EPYC ‘Venice’ CPUs, MI450 accelerators, and Nvidia’s Vera Rubin-based solutions."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/vpn/save-78-percent-on-nords-latest-complete-vpn-package-27-months-of-online-protection-for-usd107",
    "domain": "AI 算力 / 半导体",
    "title": "Save 78% on Nord's latest Complete VPN package — 27 months of online protection for $107",
    "url": "https://www.tomshardware.com/software/vpn/save-78-percent-on-nords-latest-complete-vpn-package-27-months-of-online-protection-for-usd107",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T11:36:31+00:00",
    "summary": "Pick up 27 months of NordVPN coverage for just $107. Fast VPN connections, anti-virus protection, and a password manager for only $3.99 per month."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/us-closes-loophole-that-allowed-chinese-owned-subsidiaries-located-outside-china-to-buy-ai-chips-report-claims-that-hundreds-of-thousands-of-advanced-ai-chips-have-been-acquired-through-bis-blind-spot",
    "domain": "AI 算力 / 半导体",
    "title": "US closes loophole that allowed Chinese-owned subsidiaries located outside China to buy AI chips — report claims that hundreds of thousands of advanced AI chips have been acquired through BIS blind sp",
    "url": "https://www.tomshardware.com/tech-industry/us-closes-loophole-that-allowed-chinese-owned-subsidiaries-located-outside-china-to-buy-ai-chips-report-claims-that-hundreds-of-thousands-of-advanced-ai-chips-have-been-acquired-through-bis-blind-spot",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T11:32:24+00:00",
    "summary": "The BIS just issued a clarification that Chinese-owned subsidiaries are included in U.S. export controls, even if they're based outside of China. However, one source said that some companies have been"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/negative-time-experiment-clears-peer-review-as-photons-appear-to-leave-an-atom-cloud-before-entering",
    "domain": "AI 算力 / 半导体",
    "title": "Negative time experiment clears peer review as photons appear to leave an atom cloud before entering — groundbreaking quantum 'negative time' proven after 1 million test runs",
    "url": "https://www.tomshardware.com/tech-industry/negative-time-experiment-clears-peer-review-as-photons-appear-to-leave-an-atom-cloud-before-entering",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T11:30:00+00:00",
    "summary": "A University of Toronto experiment showing that photons can spend a negative amount of time inside a cloud of atoms has been published in Physical Review Letters."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/portable-monitors/acers-pm131qt-portable-monitor-is-a-12-3-inch-touchscreen-with-magnetic-mounting-a-built-in-kickstand-and-5-point-touch-1920-x-720-ips-screen-has-pogo-pins-for-a-keyboard-and-is-designed-for-secondary-and-in-vehicle-use",
    "domain": "AI 算力 / 半导体",
    "title": "Acer’s PM131QT portable monitor is a 12.3-inch touchscreen with magnetic mounting, a built-in kickstand, and 5-point touch – 1920 x 720 IPS screen has pogo pins for a keyboard, and is designed for sec",
    "url": "https://www.tomshardware.com/monitors/portable-monitors/acers-pm131qt-portable-monitor-is-a-12-3-inch-touchscreen-with-magnetic-mounting-a-built-in-kickstand-and-5-point-touch-1920-x-720-ips-screen-has-pogo-pins-for-a-keyboard-and-is-designed-for-secondary-and-in-vehicle-use",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T11:00:00+00:00",
    "summary": "Are you looking for a compact monitor for multiple uses around the home and on the go? Acer’s new PM131QT might be just what you’re looking for."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/wearable-tech/resourceful-runner-can-race-my-own-ghost-using-homemade-meta-ray-ban-display-app-also-adds-bonus-coins-mini-leaderboard-and-more",
    "domain": "AI 算力 / 半导体",
    "title": "Resourceful runner 'can race my own ghost' using homemade Meta Ray-Ban Display app — also adds bonus coins, mini leaderboard, and more",
    "url": "https://www.tomshardware.com/peripherals/wearable-tech/resourceful-runner-can-race-my-own-ghost-using-homemade-meta-ray-ban-display-app-also-adds-bonus-coins-mini-leaderboard-and-more",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T10:48:30+00:00",
    "summary": "Video demonstrates brand-new gamified running app for the Meta Ray-Ban Display glasses."
  },
  {
    "id": "rss:https://www.tomshardware.com/news/live/computex-2026-",
    "domain": "AI 算力 / 半导体",
    "title": "Computex 2026 Live: Every update and announcement from day one in Taipei",
    "url": "https://www.tomshardware.com/news/live/computex-2026-",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T10:39:37+00:00",
    "summary": "Every update live from Taipei as Computex continues in Taiwan."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-warns-it-has-a-healthy-dose-of-paranoia-over-nvidia-entrance-into-pc-market-company-says-rtx-spark-is-great-for-the-market-while-touting-the-virtues-of-x86",
    "domain": "AI 算力 / 半导体",
    "title": "Intel warns it has 'a healthy dose of paranoia' over Nvidia entrance into PC market — company says RTX Spark is 'great for the market' while touting the virtues of x86",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-warns-it-has-a-healthy-dose-of-paranoia-over-nvidia-entrance-into-pc-market-company-says-rtx-spark-is-great-for-the-market-while-touting-the-virtues-of-x86",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T10:30:00+00:00",
    "summary": "Intel reacts to Nvidia’s RTX Spark announcement, and says that it’s treating the green giant’s entrance into consumer SoCs with “a healthy dose of skepticism.\""
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/amd-promises-13-percent-uplift-with-new-expo-ultra-low-latency-overclocking-on-ddr5-dimms-automatic-memory-overclocking-delivers-4-percent-improvement-over-standard-expo-says-amd",
    "domain": "AI 算力 / 半导体",
    "title": "AMD promises 13% uplift with new EXPO ‘Ultra Low Latency’ overclocking on DDR5 DIMMs — automatic memory overclocking delivers 4% improvement over standard EXPO, says AMD",
    "url": "https://www.tomshardware.com/pc-components/ram/amd-promises-13-percent-uplift-with-new-expo-ultra-low-latency-overclocking-on-ddr5-dimms-automatic-memory-overclocking-delivers-4-percent-improvement-over-standard-expo-says-amd",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T10:30:00+00:00",
    "summary": "AMD’s upcoming EXPO ‘Ultra Low Latency’ automatic memory overclocking promises a 13% improvement over standard DDR5 speeds, as well as a 4% jump compared to standard EXPO."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/we-went-hands-on-with-qualcomms-new-usd300-and-up-arm-laptop-platform-mystery-eight-core-cpu-in-active-cooled-snapdragon-c-laptop-surfaces-in-acer-aspire-go-15",
    "domain": "AI 算力 / 半导体",
    "title": "We went hands-on with Qualcomm's new '$300 and up' ARM laptop platform with mystery eight-core CPU — active-cooled Snapdragon C laptop surfaces in Acer Aspire Go 15",
    "url": "https://www.tomshardware.com/laptops/we-went-hands-on-with-qualcomms-new-usd300-and-up-arm-laptop-platform-mystery-eight-core-cpu-in-active-cooled-snapdragon-c-laptop-surfaces-in-acer-aspire-go-15",
    "source": "Paul Alcorn",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T10:00:00+00:00",
    "summary": "We've learned a few new details of the Snapdragon C platform at Computex 2026 by opening up a few Windows utilities on a demo unit."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/dlss-4-5-ray-reconstruction-update-arrives-in-august-for-better-ray-tracing-visuals-broader-training-data-set-and-second-gen-transformer-architecture-combine-for-improved-image-quality",
    "domain": "AI 算力 / 半导体",
    "title": "DLSS 4.5 Ray Reconstruction update arrives in August for better ray tracing visuals — broader training data set and second-gen transformer architecture combine for improved image quality",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/dlss-4-5-ray-reconstruction-update-arrives-in-august-for-better-ray-tracing-visuals-broader-training-data-set-and-second-gen-transformer-architecture-combine-for-improved-image-quality",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T09:30:00+00:00",
    "summary": "At Computex 2026, Nvidia announced DLSS 4.5 Ray Reconstruction, an updated version of its neural RT denoiser with a second-gen transformer architecture and a broader training data set for better outpu"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/microsoft-surface-laptop-ultra-weilds-nvidias-rtx-spark-superchip-with-128gb-of-ram-20-arm-cpu-cores-and-a-blackwell-gpu-15-inch-mini-led-pixelsense-ultra-display-rounds-out-the-powerful-package",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft Surface Laptop Ultra weilds Nvidia's RTX Spark superchip with 128GB of RAM, 20 Arm CPU cores, and a Blackwell GPU — 15-inch mini-LED PixelSense Ultra display rounds out the powerful package",
    "url": "https://www.tomshardware.com/laptops/microsoft-surface-laptop-ultra-weilds-nvidias-rtx-spark-superchip-with-128gb-of-ram-20-arm-cpu-cores-and-a-blackwell-gpu-15-inch-mini-led-pixelsense-ultra-display-rounds-out-the-powerful-package",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T09:00:00+00:00",
    "summary": "Powered by Nvidia's RTX Spark Superchip, the Surface Laptop Ultra features 20 Arm CPU cores, 6,144 CUDA cores, and up to 128GB of unified memory"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/nvidia-unveils-dgx-sparrk-roadmap-for-laptops-and-desktop-pcs-at-computex-2026-three-generations-outlined-rubin-followed-by-rosa-feynman",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia lays out RTX Spark roadmap for laptops and desktop PCs at Computex 2026 — three generations outlined, Rubin with LPDDR6 memory, followed by Rosa Feynman",
    "url": "https://www.tomshardware.com/pc-components/cpus/nvidia-unveils-dgx-sparrk-roadmap-for-laptops-and-desktop-pcs-at-computex-2026-three-generations-outlined-rubin-followed-by-rosa-feynman",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T05:55:07+00:00",
    "summary": "Along with its first-generation RTX Spark platform for desktop and laptop PCs, Nvidia CEO Jensen Huang revealed the company's commitment to future generations of those platforms on its future roadmaps"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/nvidia-unveils-rtx-spark-superchip-at-computex-2026-new-platform-promises-to-turn-windows-into-an-agentic-ai-os-with-arm-cpu-blackwell-gpu-and-128gb-unified-memory",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia unveils RTX Spark Superchip for laptops and desktop PCs at Computex 2026 – new platform promises to turn Windows into an agentic AI OS with Arm CPU, Blackwell GPU, and 128GB unified memory",
    "url": "https://www.tomshardware.com/laptops/nvidia-unveils-rtx-spark-superchip-at-computex-2026-new-platform-promises-to-turn-windows-into-an-agentic-ai-os-with-arm-cpu-blackwell-gpu-and-128gb-unified-memory",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:52:13+00:00",
    "summary": "At Computex 2026, Nvidia CEO Jensen Huang unveiled the RTX Spark Superchip, a new Arm laptop and desktop platform that powers agentic AI on Windows with a 20-core Arm CPU, powerful 6144-CUDA-core Blac"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-xeon-7-diamond-rapids-cpus-officially-launching-in-2027-on-intel-18a-p-next-gen-p-core-xeon-features-pcie-6-0-50-percent-higher-core-counts-and-twice-the-memory-bandwidth",
    "domain": "AI 算力 / 半导体",
    "title": "Intel Xeon 7 ‘Diamond Rapids’ CPUs officially launching in 2027 on Intel 18A-P — next-gen P-core Xeon features PCIe 6.0, 50% higher core counts, and twice the memory bandwidth",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-xeon-7-diamond-rapids-cpus-officially-launching-in-2027-on-intel-18a-p-next-gen-p-core-xeon-features-pcie-6-0-50-percent-higher-core-counts-and-twice-the-memory-bandwidth",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T03:00:00+00:00",
    "summary": "Intel has officially confirmed its next-gen Xeon 7 Diamond Rapids CPUs are coming in 2027, featuring 50% higher core counts and twice the memory bandwidth of Xeon 6 in a bid to compete against AMD’s u"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/intel-details-long-awaited-crescent-island-ai-gpu-at-computex-boasts-up-to-480-gb-of-lpddr5x-to-combat-memory-shortages-company-shares-more-details-of-its-xe3p-inference-accelerator-at-computex",
    "domain": "AI 算力 / 半导体",
    "title": "Intel details long-awaited Crescent Island AI GPU at Computex, boasts up to 480 GB of LPDDR5X to combat memory shortages — company shares more details of its Xe3P inference accelerator at Computex",
    "url": "https://www.tomshardware.com/pc-components/gpus/intel-details-long-awaited-crescent-island-ai-gpu-at-computex-boasts-up-to-480-gb-of-lpddr5x-to-combat-memory-shortages-company-shares-more-details-of-its-xe3p-inference-accelerator-at-computex",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T03:00:00+00:00",
    "summary": "Intel revealed more details of its next-gen Data Center GPU, code-named Crescent Island, at Computex 2026. This inference-optimized chip will feature up to 480GB of LPDDR5X memory for efficient handli"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-xeon-6-clearwater-forest-puts-18a-in-the-data-center-with-up-to-288-cores-576-mb-of-l3-cache-new-xeon-6990e-is-30-percent-faster-per-thread-than-192-core-amd-epyc-9965-says-intel",
    "domain": "AI 算力 / 半导体",
    "title": "Intel Xeon 6+ ‘Clearwater Forest’ puts 18A in the data center with up to 288 cores, 576 MB of L3 cache — new Xeon 6990E+ is 30% faster per thread than 192-core AMD Epyc 9965, says Intel",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-xeon-6-clearwater-forest-puts-18a-in-the-data-center-with-up-to-288-cores-576-mb-of-l3-cache-new-xeon-6990e-is-30-percent-faster-per-thread-than-192-core-amd-epyc-9965-says-intel",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T03:00:00+00:00",
    "summary": "Intel is putting its 18A node into the data center with new Xeon 6+ Clearwater Forest CPUs, which pack up to 288 E-cores for dense compute."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/amds-formerly-china-exclusive-radeon-rx-9070-gre-goes-global-for-usd549-on-june-2-rdna-4-gpu-will-bridge-the-gap-between-rx-9060-xt-and-rx-9070",
    "domain": "AI 算力 / 半导体",
    "title": "AMD’s formerly China-exclusive Radeon RX 9070 GRE goes global for $549 on June 2 — RDNA 4 GPU will bridge the gap between RX 9060 XT and RX 9070",
    "url": "https://www.tomshardware.com/pc-components/gpus/amds-formerly-china-exclusive-radeon-rx-9070-gre-goes-global-for-usd549-on-june-2-rdna-4-gpu-will-bridge-the-gap-between-rx-9060-xt-and-rx-9070",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T02:00:21+00:00",
    "summary": "AMD has officially launched the Radeon RX 9070 GRE for $549, an RDNA 4 graphics card that was previously exclusive to the Chinese market."
  },
  {
    "id": "hn:48291230",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Vera CPU Benchmarks: Olympus Cores Delivering Great Performance",
    "url": "https://www.phoronix.com/review/nvidia-vera-benchmarks",
    "source": "naves",
    "platform": "hackernews",
    "points": 54,
    "published_at": "2026-05-27T08:15:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:48323697",
    "domain": "AI 算力 / 半导体",
    "title": "The Nvidia Tax",
    "url": "https://www.cringely.com/2026/05/29/the-nvidia-tax/",
    "source": "HotGarbage",
    "platform": "hackernews",
    "points": 23,
    "published_at": "2026-05-29T14:41:43+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/the-stratosphere-race-haps-move-from-experiment-to-commercial-reality/",
    "domain": "AI 算力 / 半导体",
    "title": "The Stratosphere Race: HAPS Move from Experiment to Commercial Reality",
    "url": "https://www.eetimes.com/the-stratosphere-race-haps-move-from-experiment-to-commercial-reality/",
    "source": "Rebecca Pool",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-29T22:00:00+00:00",
    "summary": "Autonomous high-altitude platform stations are getting ready to bridge ground networks and LEO satellites. The post The Stratosphere Race: HAPS Move from Experiment to Commercial Reality appeared firs"
  },
  {
    "id": "rss:https://www.eetimes.com/gartner-says-supply-chain-confront-geopolitical-and-ai-challenges/",
    "domain": "AI 算力 / 半导体",
    "title": "Gartner Says Supply Chain Confront Geopolitical and AI Challenges",
    "url": "https://www.eetimes.com/gartner-says-supply-chain-confront-geopolitical-and-ai-challenges/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-29T14:16:57+00:00",
    "summary": "Gartner Supply Chain Symposium highlights strategies to navigate chaos, orchestrate agility, and accelerate Innovation. The post Gartner Says Supply Chain Confront Geopolitical and AI Challenges appea"
  },
  {
    "id": "hn:47989883",
    "domain": "大厂 AI 动态",
    "title": "VS Code inserting 'Co-Authored-by Copilot' into commits regardless of usage",
    "url": "https://github.com/microsoft/vscode/pull/310226",
    "source": "indrora",
    "platform": "hackernews",
    "points": 1513,
    "published_at": "2026-05-02T19:57:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:48196570",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.5 Flash",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/",
    "source": "spectraldrift",
    "platform": "hackernews",
    "points": 962,
    "published_at": "2026-05-19T17:43:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:48111896",
    "domain": "大厂 AI 动态",
    "title": "Show HN: Needle: We Distilled Gemini Tool Calling into a 26M Model",
    "url": "https://github.com/cactus-compute/needle",
    "source": "HenryNdubuaku",
    "platform": "hackernews",
    "points": 776,
    "published_at": "2026-05-12T18:03:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:48192224",
    "domain": "大厂 AI 动态",
    "title": "Apple unveils new accessibility features",
    "url": "https://www.apple.com/newsroom/2026/05/apple-unveils-new-accessibility-features-and-updates-with-apple-intelligence/",
    "source": "interpol_p",
    "platform": "hackernews",
    "points": 726,
    "published_at": "2026-05-19T12:04:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:48233563",
    "domain": "大厂 AI 动态",
    "title": "Steve Wozniak cheered after telling students they have AI – actual intelligence",
    "url": "https://www.businessinsider.com/steve-wozniak-apple-ai-graduation-speech-2026-5",
    "source": "signa11",
    "platform": "hackernews",
    "points": 650,
    "published_at": "2026-05-22T09:04:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:48196867",
    "domain": "大厂 AI 动态",
    "title": "Gemini CLI will stop working from June 18, 2026",
    "url": "https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/",
    "source": "primaprashant",
    "platform": "hackernews",
    "points": 406,
    "published_at": "2026-05-19T18:03:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:48196609",
    "domain": "大厂 AI 动态",
    "title": "Gemini Omni",
    "url": "https://deepmind.google/models/gemini-omni/",
    "source": "meetpateltech",
    "platform": "hackernews",
    "points": 323,
    "published_at": "2026-05-19T17:46:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:48050278",
    "domain": "大厂 AI 动态",
    "title": "AlphaEvolve: Gemini-powered coding agent scaling impact across fields",
    "url": "https://deepmind.google/blog/alphaevolve-impact/",
    "source": "berlianta",
    "platform": "hackernews",
    "points": 327,
    "published_at": "2026-05-07T15:02:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:48272354",
    "domain": "大厂 AI 动态",
    "title": "Microsoft Copilot Cowork Exfiltrates Files",
    "url": "https://www.promptarmor.com/resources/microsoft-copilot-cowork-exfiltrates-files",
    "source": "Kneenex",
    "platform": "hackernews",
    "points": 264,
    "published_at": "2026-05-25T21:45:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:48111581",
    "domain": "大厂 AI 动态",
    "title": "Reimagining the mouse pointer for the AI era",
    "url": "https://deepmind.google/blog/ai-pointer/",
    "source": "devhouse",
    "platform": "hackernews",
    "points": 252,
    "published_at": "2026-05-12T17:40:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:48297467",
    "domain": "大厂 AI 动态",
    "title": "Gemini, Gophers, and Fingers. Oh My Alternative Internets Beyond HTTPS",
    "url": "https://brennan.day/gemini-gophers-and-fingers-oh-my-alternative-internets-beyond-https/",
    "source": "ChrisArchitect",
    "platform": "hackernews",
    "points": 146,
    "published_at": "2026-05-27T17:24:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:48080702",
    "domain": "大厂 AI 动态",
    "title": "Gemini API File Search is now multimodal",
    "url": "https://blog.google/innovation-and-ai/technology/developers-tools/expanded-gemini-api-file-search-multimodal-rag/",
    "source": "gmays",
    "platform": "hackernews",
    "points": 156,
    "published_at": "2026-05-10T03:22:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:48029334",
    "domain": "大厂 AI 动态",
    "title": "Zuckerberg 'personally authorized' Meta's copyright infringement, publishers say",
    "url": "https://apnews.com/article/meta-mark-zuckerberg-ai-publishers-lawsuit-llama-5609846d4d840014974a847b01079c32",
    "source": "jethronethro",
    "platform": "hackernews",
    "points": 156,
    "published_at": "2026-05-05T22:07:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:48084710",
    "domain": "大厂 AI 动态",
    "title": "Chrome's AI features may be hogging 4GB of your computer storage",
    "url": "https://www.theverge.com/tech/924933/google-chrome-4gb-gemini-nano-ai-features",
    "source": "birdculture",
    "platform": "hackernews",
    "points": 117,
    "published_at": "2026-05-10T15:22:46+00:00",
    "summary": ""
  },
  {
    "id": "hn:48221976",
    "domain": "大厂 AI 动态",
    "title": "Gemini randomly dumped its system prompt",
    "url": "https://gist.github.com/mkaramuk/44a44d83178e632ec0dd1f02186d822c",
    "source": "mkaramuk",
    "platform": "hackernews",
    "points": 94,
    "published_at": "2026-05-21T13:04:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:48029753",
    "domain": "大厂 AI 动态",
    "title": "Xbox CEO ends Copilot AI development and overhauls leadership",
    "url": "https://www.dexerto.com/gaming/xbox-ceo-ends-copilot-ai-development-overhauls-leadership-3361353/",
    "source": "gmays",
    "platform": "hackernews",
    "points": 113,
    "published_at": "2026-05-05T22:43:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:48031707",
    "domain": "大厂 AI 动态",
    "title": "Update on \"Co-authored-by: Copilot\" in commit messages",
    "url": "https://github.com/microsoft/vscode/issues/314311",
    "source": "extesy",
    "platform": "hackernews",
    "points": 102,
    "published_at": "2026-05-06T03:15:05+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/941016/anthropic-has-officially-filed-to-go-public",
    "domain": "大厂 AI 动态",
    "title": "Anthropic has officially filed to go public",
    "url": "https://www.theverge.com/ai-artificial-intelligence/941016/anthropic-has-officially-filed-to-go-public",
    "source": "Hayden Field",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T16:40:38+00:00",
    "summary": "After months of speculation about whether OpenAI or Anthropic would be first in their race to IPO, Anthropic on Monday reached a key milestone: filing to kick off the process with the U.S. Securities "
  },
  {
    "id": "rss:https://www.theverge.com/games/941031/sony-playstation-flexstrike-fight-stick-gaming-monitor-pulse-elevate-speakers-launch-date-price",
    "domain": "大厂 AI 动态",
    "title": "Sony’s new fight stick and gaming monitor launch in August",
    "url": "https://www.theverge.com/games/941031/sony-playstation-flexstrike-fight-stick-gaming-monitor-pulse-elevate-speakers-launch-date-price",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T16:36:18+00:00",
    "summary": "Sony is sharing new details about some of its upcoming gaming-focused hardware, including pricing and August launch dates for its FlexStrike fight stick and its 27-inch monitor. The FlexStrike fight s"
  },
  {
    "id": "rss:https://www.theverge.com/games/939206/summer-game-fest-playstation-xbox-gaming-events-2026",
    "domain": "大厂 AI 动态",
    "title": "Summer Game Fest 2026: All the news from gaming&#8217;s busiest week",
    "url": "https://www.theverge.com/games/939206/summer-game-fest-playstation-xbox-gaming-events-2026",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T15:30:00+00:00",
    "summary": "Get ready for some gaming news. It&#8217;s officially June, which means splashy new events from PlayStation, Xbox, and gaming hype man Geoff Keighley. But this season doesn&#8217;t just feature the bi"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/940830/find-my-bluetooth-tracker-bose-qc-ultra-google-pixel-buds-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "An affordable, long-lasting AirTag alternative is $15 right now",
    "url": "https://www.theverge.com/gadgets/940830/find-my-bluetooth-tracker-bose-qc-ultra-google-pixel-buds-deal-sale",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T15:24:32+00:00",
    "summary": "There are many solid Bluetooth trackers for iPhones that tap into Apple’s expansive Find My network. Some are thin, some are a bit chunkier. And, evidently, some look like tiny soccer balls. Ugreen’s "
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/940869/quinn-erotica-rent-free-ember-and-ice-heated-rivalry-off-campus",
    "domain": "大厂 AI 动态",
    "title": "The next big career move for young Hollywood? Reading audio smut",
    "url": "https://www.theverge.com/entertainment/940869/quinn-erotica-rent-free-ember-and-ice-heated-rivalry-off-campus",
    "source": "Charles Pulliam-Moore",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T15:00:12+00:00",
    "summary": "Though Gen Z has developed a reputation for being so disinterested in sex that they don't even want to see it on TV, the popularity of series like Heated Rivalry and The Summer I Turned Pretty has mad"
  },
  {
    "id": "rss:https://www.theverge.com/games/939238/video-game-gaming-events-summer-game-fest-schedule-2026",
    "domain": "大厂 AI 动态",
    "title": "Your guide to June’s biggest gaming events",
    "url": "https://www.theverge.com/games/939238/video-game-gaming-events-summer-game-fest-schedule-2026",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T15:00:00+00:00",
    "summary": "It's early June, which means it's video game event season once again. Now that E3 has been gone for a few years, a bunch of showcases and presentations have started to fill the void, including big pro"
  },
  {
    "id": "rss:https://www.theverge.com/report/940861/microsoft-build-ai-models-windows-dev-mode-what-to-expect",
    "domain": "大厂 AI 动态",
    "title": "Microsoft to unveil new AI models and Windows improvements at Build",
    "url": "https://www.theverge.com/report/940861/microsoft-build-ai-models-windows-dev-mode-what-to-expect",
    "source": "Tom Warren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T14:39:03+00:00",
    "summary": "Microsoft is heading to San Francisco this week in a bid to win back developers at its Build conference. I've been attending Build since the days when Microsoft called it the Professional Developers C"
  },
  {
    "id": "rss:https://www.theverge.com/tech/940844/computex-2026",
    "domain": "大厂 AI 动态",
    "title": "Computex 2026: All the news and announcements",
    "url": "https://www.theverge.com/tech/940844/computex-2026",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T14:33:02+00:00",
    "summary": "Computex 2026 is kicking off in Taipei, Taiwan this week, where Nvidia, AMD, Qualcomm, Intel, and other tech brands are announcing new laptops, handhelds, chips, and more.&#160; Nvidia unveiled RTX Sp"
  },
  {
    "id": "rss:https://www.theverge.com/podcast/940831/ai-grammys-music-recording-harvey-mason",
    "domain": "大厂 AI 动态",
    "title": "AI is blowing up music. How should the Grammys handle it?",
    "url": "https://www.theverge.com/podcast/940831/ai-grammys-music-recording-harvey-mason",
    "source": "Nilay Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T14:30:00+00:00",
    "summary": "Today I’m talking with Harvey Mason Jr., who is CEO of the Recording Academy — that’s the outfit that puts on the Grammy Awards. I last talked to Harvey in 2024, when it was obvious that generative AI"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/940854/strava-restricts-api-access-ai-apps",
    "domain": "大厂 AI 动态",
    "title": "Strava blames zero-code AI apps and scrapers as it tightens API access",
    "url": "https://www.theverge.com/gadgets/940854/strava-restricts-api-access-ai-apps",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T14:06:44+00:00",
    "summary": "The popular fitness-tracking platform, Strava, is restricting access to its API as part of efforts to clamp down on AI scraping, as reported earlier by TechCrunch. Developers who want to build an app "
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/01/zigging-when-most-are-zagging-ex-meta-cto-raises-250m-climate-fund/",
    "domain": "大厂 AI 动态",
    "title": "Zigging when most are zagging, ex-Meta CTO raises $250M climate fund",
    "url": "https://techcrunch.com/2026/06/01/zigging-when-most-are-zagging-ex-meta-cto-raises-250m-climate-fund/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T16:42:22+00:00",
    "summary": "Mike Schroepfer's Gigascale Capital has raised a large fund to back founders building climate-friendly solutions for the world's energy and material shortages."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/01/anthropic-files-to-go-public/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic files to go public",
    "url": "https://techcrunch.com/2026/06/01/anthropic-files-to-go-public/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T16:36:55+00:00",
    "summary": "The company said Monday it has filed confidentially for an IPO."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/01/spacex-says-it-may-issue-significant-equity-in-future-transactions/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX says it may issue ‘significant’ equity in ‘future transactions’",
    "url": "https://techcrunch.com/2026/06/01/spacex-says-it-may-issue-significant-equity-in-future-transactions/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T16:09:56+00:00",
    "summary": "The company added a warning to prospective investors that a major dilution could be in the cards after it goes public."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/01/this-ai-weather-startup-is-out-forecasting-government-agencies/",
    "domain": "大厂 AI 动态",
    "title": "This AI weather startup is out-forecasting government agencies",
    "url": "https://techcrunch.com/2026/06/01/this-ai-weather-startup-is-out-forecasting-government-agencies/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T16:00:00+00:00",
    "summary": "Windborne Systems' newest weather forecasting model beats the best government predictions by days."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/01/duckduckgo-makes-its-no-ai-search-engine-easier-to-access-as-its-traffic-booms/",
    "domain": "大厂 AI 动态",
    "title": "DuckDuckGo makes its ‘no-AI’ search engine easier to access as its traffic booms",
    "url": "https://techcrunch.com/2026/06/01/duckduckgo-makes-its-no-ai-search-engine-easier-to-access-as-its-traffic-booms/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T14:49:10+00:00",
    "summary": "Alternative search engine DuckDuckGo launches 'no AI' web extensions for Chrome and Firefox users."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/01/revolut-rolls-out-services-to-thousands-of-users-in-india-ahead-of-broader-launch/",
    "domain": "大厂 AI 动态",
    "title": "Revolut rolls out services to thousands of users in India ahead of broader launch",
    "url": "https://techcrunch.com/2026/06/01/revolut-rolls-out-services-to-thousands-of-users-in-india-ahead-of-broader-launch/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T14:46:08+00:00",
    "summary": "The British fintech has built a waitlist of about 450,000 users in India as it prepares for a broader launch."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/01/strava-declares-war-on-scrapers-ahead-of-ipo/",
    "domain": "大厂 AI 动态",
    "title": "Strava declares war on scrapers ahead of IPO",
    "url": "https://techcrunch.com/2026/06/01/strava-declares-war-on-scrapers-ahead-of-ipo/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T12:00:00+00:00",
    "summary": "Strava will charge a flat monthly fee from developers to access its API."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/01/unastella-a-south-korean-rocket-startup-that-launched-from-home-raises-24m/",
    "domain": "大厂 AI 动态",
    "title": "Unastella, a South Korean rocket startup that launched from home, raises $24M",
    "url": "https://techcrunch.com/2026/06/01/unastella-a-south-korean-rocket-startup-that-launched-from-home-raises-24m/",
    "source": "Kate Park",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T10:00:00+00:00",
    "summary": "The Seoul-based rocket startup is developing its own launch vehicles and engines."
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/31/erin-brockovich-takes-aim-at-data-center-secrecy/",
    "domain": "大厂 AI 动态",
    "title": "Erin Brockovich takes aim at data center secrecy",
    "url": "https://techcrunch.com/2026/05/31/erin-brockovich-takes-aim-at-data-center-secrecy/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T21:05:14+00:00",
    "summary": "Environmental activist Erin Brockovich has a new mission."
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/31/this-weekends-two-biggest-movies-were-both-directed-by-youtubers/",
    "domain": "大厂 AI 动态",
    "title": "This weekend’s two biggest movies were both directed by YouTubers",
    "url": "https://techcrunch.com/2026/05/31/this-weekends-two-biggest-movies-were-both-directed-by-youtubers/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T18:34:58+00:00",
    "summary": "The YouTube-to-prestige-horror pipeline is looking very strong."
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/31/this-is-fine-artist-kc-green-reaches-agreement-with-ai-startup-artisan/",
    "domain": "大厂 AI 动态",
    "title": "‘This is fine’ artist KC Green reaches agreement with AI startup Artisan",
    "url": "https://techcrunch.com/2026/05/31/this-is-fine-artist-kc-green-reaches-agreement-with-ai-startup-artisan/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T18:28:17+00:00",
    "summary": "The startup has apparently taken down the ads using KC Green's \"This is fine\" meme."
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/31/techcrunch-mobility-it-doesnt-matter-that-people-hate-the-ferrari-luce/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Mobility: It doesn’t matter that people hate the Ferrari Luce",
    "url": "https://techcrunch.com/2026/05/31/techcrunch-mobility-it-doesnt-matter-that-people-hate-the-ferrari-luce/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T16:05:00+00:00",
    "summary": "Welcome back to TechCrunch Mobility, your hub for the future of transportation and now, more than ever, how AI is playing a part."
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/31/making-sense-of-the-debate-over-ai-psychosis/",
    "domain": "大厂 AI 动态",
    "title": "Making sense of the debate over AI psychosis",
    "url": "https://techcrunch.com/2026/05/31/making-sense-of-the-debate-over-ai-psychosis/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T15:30:00+00:00",
    "summary": "On the latest episode of Equity, we debate whether tech CEOs are \"uniquely prone to AI psychosis.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/31/black-founders-raise-highest-amount-of-quarterly-funding-since-2022-but-theres-a-catch/",
    "domain": "大厂 AI 动态",
    "title": "Black founders raise highest amount of quarterly funding since 2022, but there’s a catch",
    "url": "https://techcrunch.com/2026/05/31/black-founders-raise-highest-amount-of-quarterly-funding-since-2022-but-theres-a-catch/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T15:00:00+00:00",
    "summary": "Speaking to TechCrunch, Crunchbase’s head of research Gené Teare, said the factors holding back Black founders include “access to networks, relationships, and early introductions.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/31/i-went-to-the-so-called-steroid-olympics-to-understand-why-silicon-valley-is-obsessed-with-peptides/",
    "domain": "大厂 AI 动态",
    "title": "What happens in Vega$: steroids, swimmers, and a billion-dollar hustle",
    "url": "https://techcrunch.com/2026/05/31/i-went-to-the-so-called-steroid-olympics-to-understand-why-silicon-valley-is-obsessed-with-peptides/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T13:00:00+00:00",
    "summary": "The Enhanced Games — a singular sporting competition where a majority of the athletes were on performance enhancing drugs — may herald a new business model that the tech industry is ready to embrace."
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/30/softbank-says-it-will-invest-up-to-e75-billion-to-build-french-data-centers/",
    "domain": "大厂 AI 动态",
    "title": "SoftBank says it will invest up to €75 billion to build French data centers",
    "url": "https://techcrunch.com/2026/05/30/softbank-says-it-will-invest-up-to-e75-billion-to-build-french-data-centers/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-30T21:45:00+00:00",
    "summary": "The goal, the firm said, is to develop and operate up to 5 gigawatts of additional data center capacity."
  },
  {
    "id": "rss:https://stratechery.com/2026/youtubers-win-the-box-office-goodbye-gatekeepers-the-youtube-bar/",
    "domain": "大厂 AI 动态",
    "title": "YouTubers Win the Box Office, Goodbye Gatekeepers, The YouTube Bar",
    "url": "https://stratechery.com/2026/youtubers-win-the-box-office-goodbye-gatekeepers-the-youtube-bar/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T10:00:00+00:00",
    "summary": "YouTubers are ruling the box office, and it shouldn't be a surprise: succeeding on YouTube is a much higher bar than the gates that currently govern Hollywood."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/06/amd-extends-socket-am5-support-through-at-least-2029-am4-refuses-to-die/",
    "domain": "大厂 AI 动态",
    "title": "AMD extends Socket AM5 support through at least 2029; AM4 refuses to die",
    "url": "https://arstechnica.com/gadgets/2026/06/amd-extends-socket-am5-support-through-at-least-2029-am4-refuses-to-die/",
    "source": "Andrew Cunningham",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T17:02:22+00:00",
    "summary": "The 5800X3D returns at $349, while the 7700X3D debuts at $329."
  },
  {
    "id": "rss:https://arstechnica.com/gaming/2026/06/asus-gives-the-rox-xbox-ally-the-oled-screen-it-deserves/",
    "domain": "大厂 AI 动态",
    "title": "ROG Xbox Ally X20 adds OLED screen, control upgrades",
    "url": "https://arstechnica.com/gaming/2026/06/asus-gives-the-rox-xbox-ally-the-oled-screen-it-deserves/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T16:04:45+00:00",
    "summary": "But the hardware refresh is tethered to a bundle with pricey AR glasses."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/06/nvidia-gets-into-the-arm-pc-business-with-new-high-end-rtx-spark-processor/",
    "domain": "大厂 AI 动态",
    "title": "Nvidia RTX Spark comes to Windows PCs with Arm CPU, RTX GPU, and unified memory",
    "url": "https://arstechnica.com/gadgets/2026/06/nvidia-gets-into-the-arm-pc-business-with-new-high-end-rtx-spark-processor/",
    "source": "Andrew Cunningham",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T14:47:22+00:00",
    "summary": "Nvidia's new chips will power laptop workstations and mini desktop PCs at first."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/06/intel-our-upcoming-ai-chip-will-be-cheaper-run-cooler-than-nvidia-amd-options/",
    "domain": "大厂 AI 动态",
    "title": "Intel: Our upcoming AI chip will be cheaper, run cooler than Nvidia, AMD options",
    "url": "https://arstechnica.com/ai/2026/06/intel-our-upcoming-ai-chip-will-be-cheaper-run-cooler-than-nvidia-amd-options/",
    "source": "Financial Times",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T13:32:16+00:00",
    "summary": "Crescent Island is an air-cooled chip that uses LPDDR5 memory."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/06/openais-math-breakthrough-played-to-ais-strengths/",
    "domain": "大厂 AI 动态",
    "title": "An OpenAI model solved a famous math problem that stumped humans for 80 years",
    "url": "https://arstechnica.com/ai/2026/06/openais-math-breakthrough-played-to-ais-strengths/",
    "source": "Kai Williams",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T11:00:00+00:00",
    "summary": "I tried to explain OpenAI’s solution more clearly than OpenAI did."
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/05/on-its-40th-anniversary-we-reassess-1986s-spacecamp/",
    "domain": "大厂 AI 动态",
    "title": "On its 40th anniversary, we reassess 1986's SpaceCamp",
    "url": "https://arstechnica.com/culture/2026/05/on-its-40th-anniversary-we-reassess-1986s-spacecamp/",
    "source": "Eric Berger & Lee Hutchinson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T11:15:12+00:00",
    "summary": "Is it a hidden gem, a cult classic, or hopelessly dumb? We vote \"all of the above.\""
  },
  {
    "id": "hn:48314363",
    "domain": "股票",
    "title": "Sam Altman and Dario Amodei are both walking back AI jobs apocalypse predictions",
    "url": "https://fortune.com/2026/05/26/sam-altman-dario-amodei-walking-back-ai-jobs-apocalypse-prophecies-ipo/",
    "source": "ianrahman",
    "platform": "hackernews",
    "points": 234,
    "published_at": "2026-05-28T19:43:14+00:00",
    "summary": ""
  },
  {
    "id": "hn:48210226",
    "domain": "股票",
    "title": "OpenAI Is Preparing to File for an IPO Soon",
    "url": "https://www.wsj.com/tech/ai/openai-is-preparing-to-file-for-an-ipo-very-soon-0ec95af5",
    "source": "louiereederson",
    "platform": "hackernews",
    "points": 206,
    "published_at": "2026-05-20T16:24:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:48134429",
    "domain": "股票",
    "title": "Sam Altman's Business Dealings Under GOP Scrutiny Ahead of OpenAI's IPO",
    "url": "https://www.wsj.com/tech/ai/sam-altmans-business-dealings-under-gop-scrutiny-ahead-of-openais-ipo-52c1cc4d",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 199,
    "published_at": "2026-05-14T12:27:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:48217052",
    "domain": "股票",
    "title": "OpenAI to confidentially file for IPO as soon as Friday",
    "url": "https://www.cnbc.com/2026/05/20/openai-ipo-filing.html",
    "source": "doppp",
    "platform": "hackernews",
    "points": 137,
    "published_at": "2026-05-21T02:24:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:48354214",
    "domain": "股票",
    "title": "How Not to Buy SpaceX Stock (It's Harder Than You Think)",
    "url": "https://cranberries.medium.com/how-not-to-buy-spacex-stock-its-harder-than-you-think-a37610cb8bd3",
    "source": "clktmr",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-06-01T08:50:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:48343303",
    "domain": "股票",
    "title": "The SpaceX IPO is great for Elon Musk and terrible for you",
    "url": "https://www.theverge.com/ai-artificial-intelligence/940001/elon-musk-spacex-ipo-ai",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-05-31T05:34:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:48359035",
    "domain": "股票",
    "title": "Anthropic Files to Go Public, Setting Stage for Huge I.P.O.",
    "url": "https://www.nytimes.com/2026/06/01/technology/anthropic-ipo.html",
    "source": "jbegley",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-06-01T16:27:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:48281983",
    "domain": "股票",
    "title": "Show HN: A website that tracks every stock trade Congress makes",
    "url": "https://congress.kadoa.com/",
    "source": "hubraumhugo",
    "platform": "hackernews",
    "points": 62,
    "published_at": "2026-05-26T16:28:56+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3773592",
    "domain": "股票",
    "title": "抗议以军扩大在黎行动，伊朗据称将暂停与美沟通，计划彻底封锁霍尔木兹海峡",
    "url": "https://wallstreetcn.com/articles/3773592",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T16:07:28+00:00",
    "summary": "据伊媒，伊朗官员称，以色列必须立即停止在黎巴嫩和加沙地带的军事行动，并从黎巴嫩撤出，在此要求得到满足前，伊朗不会举行任何谈判。伊朗最高领袖军事顾问：伊方耐心有限，绝不允许海上封锁继续。伊朗外交部：未就核问题细节进行谈判，重点是结束战争。报道称以色列扩大在黎巴嫩的军事行动是与美国协调进行。美军证实驻科威特基地遭伊朗袭击，称无人员伤亡、成功拦截两枚伊方导弹。"
  },
  {
    "id": "wscn:3773596",
    "domain": "股票",
    "title": "美国5月ISM制造业扩张速度创四年来最快",
    "url": "https://wallstreetcn.com/articles/3773596",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T15:07:46+00:00",
    "summary": "5月ISM制造业指数超预期升至54，连续五个月扩张；新订单增速加速至四个月高位，生产同步回升，AI投资与抢购备货双轮驱动。然而，伊朗冲突推高油价与原材料成本，制造业物价支付指数82.1，小幅回落，仍接近2022年以来高位。"
  },
  {
    "id": "wscn:3773589",
    "domain": "股票",
    "title": "点石成金？特朗普“旧吹票视频”扩散，IBM盘中大涨9%创历史新高",
    "url": "https://wallstreetcn.com/articles/3773589",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T14:42:08+00:00",
    "summary": "一段特朗普盛赞IBM首席执行官的老视频在社交媒体上重新流传，叠加巴克莱首次覆盖给予增持评级，推动IBM股价周一盘中一度涨近9%。但行情并非仅由情绪驱动——IBM此前已斩获10亿美元政府量子合同，并宣布百亿美元投资计划。值得注意的是，特朗普信托账户持有IBM股票。"
  },
  {
    "id": "wscn:3773597",
    "domain": "股票",
    "title": "市值差4500亿！智谱狂飙，MiniMax怎么了？",
    "url": "https://wallstreetcn.com/articles/3773597",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T14:21:10+00:00",
    "summary": "智谱与MiniMax同日登陆港股，五个月后市值相差近4500亿港元。智谱借Agent叙事和API量价齐升，股价暴涨超1600%；而MiniMax因业务分散缺乏集中交易主题被冷落。尽管两者收入体量相近，资本市场却给出了截然不同的定价。"
  },
  {
    "id": "wscn:3773537",
    "domain": "股票",
    "title": "伊朗称将全面封锁霍尔木兹，美股低开，IBM涨近9%，ARM大涨12%，美油涨6%",
    "url": "https://wallstreetcn.com/articles/3773537",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T13:50:07+00:00",
    "summary": "美股三大指数集体低开，纳斯达克综合指数跌0.18%，标普500指数跌0.19%，纳斯达克综合指数跌0.18%。英伟达开盘上涨3%，ARM上涨12%；IBM上涨8.7%，有望创下历史新高。布伦特原油涨破每桶95美元，美元时隔三个交易日首度走强，黄金下跌1.5%至每盎司约4469美元。"
  },
  {
    "id": "wscn:3773593",
    "domain": "股票",
    "title": "豪掷870亿美元押注欧洲AI，孙正义：这场革命比互联网时代大50倍！",
    "url": "https://wallstreetcn.com/articles/3773593",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T13:21:45+00:00",
    "summary": "软银宣布在法国建设欧洲最大AI基础设施，规划5GW数据中心容量。孙正义直言AI革命规模或达互联网时代50倍，即使出现泡沫和调整也将是“最佳买点”。"
  },
  {
    "id": "wscn:3773591",
    "domain": "股票",
    "title": "600多元就能押注马斯克？上万人12亿元疯抢“SpaceX代币”，其本质只是一张“白条”，投资者或“血本无归”",
    "url": "https://wallstreetcn.com/articles/3773591",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T13:12:02+00:00",
    "summary": "1.4万人豪掷12亿元抢购“SpaceX代币”，但买到的并非SpaceX股权。 preSPAX本质上只是发行方提供的与SpaceX估值挂钩的衍生品，既无分红权、投票权，也无真实股权支撑。其面临底层资产、清算机制和平台信用三重风险，若发行方违约或SpaceX推迟上市，投资者甚至可能血本无归。"
  },
  {
    "id": "wscn:3773590",
    "domain": "股票",
    "title": "华为手机终于要涨价了",
    "url": "https://wallstreetcn.com/articles/3773590",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T13:09:56+00:00",
    "summary": "但没有大幅上调"
  },
  {
    "id": "wscn:3773586",
    "domain": "股票",
    "title": "巴菲特退场后的第一枪 赌的到底是什么？",
    "url": "https://wallstreetcn.com/premium/articles/3773586?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T13:04:24+00:00",
    "summary": "\"后巴菲特时代\"的第一张牌，已经打出来了。"
  },
  {
    "id": "wscn:3773587",
    "domain": "股票",
    "title": "日本追加预算不额外发债，新出口订单与海关出口增速背离，厄尔尼诺呈气象冲击与地缘风险溢价---0601宏观脱水",
    "url": "https://wallstreetcn.com/premium/articles/3773587?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T13:00:41+00:00",
    "summary": "美联储鸽派官员意外放鹰，但美伊缓和使加息定价回落，2027年12月加息的概率仍占主流。日本公布3万亿..."
  },
  {
    "id": "wscn:3773588",
    "domain": "股票",
    "title": "存量公募基金今起调整基准，业内人士：不会引发基金调仓",
    "url": "https://wallstreetcn.com/articles/3773588",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T12:52:23+00:00",
    "summary": "此次公募基金修改业绩基准秉持“尽量调整基准而不调仓”的原则，这也意味着调了基准的基金不需要调仓，而不是调了基准导致调仓。事实上，调整基准只是为了让基准更精准地反映产品的投资运作特点，帮助投资者更有效率地筛选基金。"
  },
  {
    "id": "wscn:3773585",
    "domain": "股票",
    "title": "赛力斯打出下一张牌",
    "url": "https://wallstreetcn.com/articles/3773585",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T12:39:36+00:00",
    "summary": "联手字节，造一台“AI原生汽车”。"
  },
  {
    "id": "wscn:3773581",
    "domain": "股票",
    "title": "美团电话会：受高基数影响下半年订单增速或放缓，将线上线下双向加码AI",
    "url": "https://wallstreetcn.com/articles/3773581",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T12:33:00+00:00",
    "summary": "美团CEO王兴重申“零售+科技”核心战略，表示将持续加大线上线下AI投入。目前，AI助手“小团”已升级至App核心入口，能够处理复杂指令。针对订单走势，管理层预计下半年受高基数影响可能出现同比负增长，但订单结构持续优化，交易总额（GTV）增长将更具韧性，用户频次与留存率的提升才是长期增长的关键驱动力。"
  },
  {
    "id": "wscn:3773506",
    "domain": "股票",
    "title": "你可以不相信叙事甚至是数据 但市场是诚实的：它正在定价滞胀",
    "url": "https://wallstreetcn.com/premium/articles/3773506?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T12:30:36+00:00",
    "summary": "麦当劳们“出卖”了真相。"
  },
  {
    "id": "wscn:3773525",
    "domain": "股票",
    "title": "AI杠杆投注已达历史高点，暴热行情何时迎来拐点？",
    "url": "https://wallstreetcn.com/premium/articles/3773525?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T12:20:11+00:00",
    "summary": "AI硬件杠杆与情绪达历史极值，基本面支撑下短期仍存空间，夏季或迎再平衡。"
  },
  {
    "id": "wscn:3773582",
    "domain": "股票",
    "title": "中国电车5月洗牌加速，零跑、蔚来、极氪集体狂奔，理想失速，比亚迪承压",
    "url": "https://wallstreetcn.com/articles/3773582",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T12:10:00+00:00",
    "summary": "零跑汽车以8.16万辆交付量创历史新高，同比增长81%；蔚来、极氪分别实现62.3%和81.8%的同比增长；理想汽车受L系列换代周期影响，5月交付量同比下滑18.4%，成为主要新势力中少数出现负增长的企业。问界环比增长近五成，小米连续两个月交付超3万辆。"
  },
  {
    "id": "wscn:3773584",
    "domain": "股票",
    "title": "打破\"只买不卖\"惯例！MSTR首度出售比特币，套现250万美元",
    "url": "https://wallstreetcn.com/articles/3773584",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T12:09:27+00:00",
    "summary": "Strategy于5月26日至31日间以平均每枚77135美元的净价出售了32枚比特币，总金额约250万美元，为Strategy迄今首次正式披露的比特币处置操作。此次出售均价高于持仓成本约1.9%，公司当前整体持仓账面盈利空间已大幅收窄。"
  },
  {
    "id": "wscn:3773583",
    "domain": "股票",
    "title": "美团领投 A 轮， Mindverse 总融资 5000 万美元，打造持续学习的 Agent 模型",
    "url": "https://wallstreetcn.com/articles/3773583",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T12:06:50+00:00",
    "summary": "Mindverse专注用强化学习+LoRA技术进行模型后训练，让Agent从真实任务中持续学习、低成本进化，而非仅靠提示词拼凑。基于这一理念，团队即将开源750B参数Agent模型。"
  },
  {
    "id": "wscn:3773578",
    "domain": "股票",
    "title": "高盛：空头大撤退！对冲基金以半年最快速度追涨美股",
    "url": "https://wallstreetcn.com/articles/3773578",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T11:17:05+00:00",
    "summary": "高盛报告显示，上周对冲基金对美股的净买入规模创六个月新高。衡量其风险偏好的关键指标多空净杠杆率已升至55.3%，处于近一年来的第89百分位，表明基金正以较高信心“上杠杆”做多。资金流向上，金融股获显著净买入，而工业股空头敞口已升至高位。"
  },
  {
    "id": "wscn:3773579",
    "domain": "股票",
    "title": "从“周期大宗商品”到“战略核心资产”，摩根大通：本轮存储超级周期将“更高、更长”",
    "url": "https://wallstreetcn.com/articles/3773579",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T11:16:17+00:00",
    "summary": "摩根大通大幅上调全球存储市场预期，预计2028年市场规模将达1.7万亿美元。AI需求正从GPU向CPU全面扩散，推动服务器内存需求超预期增长，HBM供需缺口有望持续至2028年。随着存储在云厂商资本开支中的占比突破50%，行业正从周期性商品转变为AI基础设施核心资产。"
  },
  {
    "id": "hn:48330421",
    "domain": "股票",
    "title": "The record divide between corporate profits and worker pay",
    "url": "https://www.wsj.com/finance/stocks/the-record-divide-between-corporate-profits-and-worker-pay-ea4c75bc",
    "source": "hhs",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-05-29T22:55:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:48285468",
    "domain": "股票",
    "title": "There are now more ETFs than stocks in the US",
    "url": "https://www.apollo.com/wealth/the-daily-spark/more-etfs-than-stocks",
    "source": "akyuu",
    "platform": "hackernews",
    "points": 44,
    "published_at": "2026-05-26T20:22:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:48280561",
    "domain": "股票",
    "title": "Stockholm poised to become leading European geospatial intel player",
    "url": "https://www.intelligenceonline.com/europe-russia/2026/05/26/stockholm-poised-to-become-leading-european-geospatial-intel-player,110772386-eve",
    "source": "alephnerd",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-05-26T14:44:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:48231815",
    "domain": "股票",
    "title": "SpaceX not the behemoth everyone thought",
    "url": "https://www.axios.com/2026/05/21/spacex-ipo-musk-ai",
    "source": "kaycebasques",
    "platform": "hackernews",
    "points": 61,
    "published_at": "2026-05-22T04:03:36+00:00",
    "summary": ""
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
    "id": "hn:48229528",
    "domain": "股票",
    "title": "The SpaceX IPO It's Worse Than You Think [video]",
    "url": "https://www.youtube.com/watch?v=-X6YzlY_8tM",
    "source": "ZeljkoS",
    "platform": "hackernews",
    "points": 47,
    "published_at": "2026-05-21T22:19:28+00:00",
    "summary": ""
  },
  {
    "id": "hn:48297843",
    "domain": "股票",
    "title": "Steam Deck OLED is back in stock, with a price increase for both models",
    "url": "https://store.steampowered.com/news/group/45479024/view/672869045073085538",
    "source": "no_news_is",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-05-27T17:50:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:48210908",
    "domain": "股票",
    "title": "OpenAI Is Preparing to File for an IPO in the Coming Days or Weeks",
    "url": "https://www.wsj.com/tech/ai/openai-ipo-filing-date-0ec95af5",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 36,
    "published_at": "2026-05-20T17:13:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:48261390",
    "domain": "股票",
    "title": "Show HN: My homelab is outperforming the stock market",
    "url": "https://stocks.sjer.red",
    "source": "shepherdjerred",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-05-24T21:54:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:48227827",
    "domain": "股票",
    "title": "SpaceX's IPO Bagship carries full payload of Elon's mistakes",
    "url": "https://jamesthomason.com/spacex-ipo-bagship-carries-full-payload-of-elons-mistakes/",
    "source": "dollar",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-05-21T19:30:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:48270880",
    "domain": "股票",
    "title": "SpaceX's IPO Filing Shows Elon's Twitter 'Business Genius' Was a Fantasy",
    "url": "https://www.techdirt.com/2026/05/22/spacexs-ipo-filing-shows-elons-twitter-business-genius-was-a-fantasy/",
    "source": "velik_m",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-05-25T19:50:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:48304589",
    "domain": "股票",
    "title": "SpaceX IPO: Did Musk Rig the Stock Market? [video]",
    "url": "https://www.youtube.com/watch?v=sYA-z0Y8WRQ",
    "source": "mgh2",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-05-28T04:42:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:48205351",
    "domain": "股票",
    "title": "Cities: Skylines Uses a Stock-Market Analogy to Influence Gameplay",
    "url": "http://jkm.dev/posts/cities-skylines-trading-market/",
    "source": "birdculture",
    "platform": "hackernews",
    "points": 30,
    "published_at": "2026-05-20T09:55:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:48254524",
    "domain": "股票",
    "title": "Reddit stock drops almost 6%, Meta launches standalone app for online forums",
    "url": "https://www.cnbc.com/2026/05/22/reddit-stock-drops-after-meta-launches-forum-app.html",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-05-24T04:58:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:48242934",
    "domain": "股票",
    "title": "Cheap AI Could Derail OpenAI and Anthropic's IPOs",
    "url": "https://www.cnbc.com/2026/05/20/cheap-ai-could-derail-openai-and-anthropics-ipos.html",
    "source": "gmays",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-05-22T23:37:17+00:00",
    "summary": ""
  },
  {
    "id": "hn:48044444",
    "domain": "股票",
    "title": "SpaceX IPO gives Musk unchecked power and forbids investor lawsuits",
    "url": "https://arstechnica.com/tech-policy/2026/05/report-spacex-ipo-gives-musk-unchecked-power-and-forbids-investor-lawsuits/",
    "source": "pzxc",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-05-07T01:47:05+00:00",
    "summary": ""
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
    "id": "hn:48046818",
    "domain": "股票",
    "title": "SpaceX IPO gives Musk power and curbs shareholder rights",
    "url": "https://www.reuters.com/sustainability/boards-policy-regulation/spacex-ipo-gives-musk-sweeping-power-curbs-shareholder-rights-2026-05-06/",
    "source": "denis1",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-05-07T08:17:33+00:00",
    "summary": ""
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
    "id": "hn:48198551",
    "domain": "金融",
    "title": "Tesla's lithium refinery discharges 231,000 gallons of polluted wastewater a day",
    "url": "https://www.autonocion.com/us/tesla-lithium-refinery-texas/",
    "source": "atombender",
    "platform": "hackernews",
    "points": 498,
    "published_at": "2026-05-19T19:52:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48088151",
    "domain": "金融",
    "title": "Maryland citizens hit with $2B power grid upgrade for out-of-state AI",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/maryland-citizens-slapped-with-usd2-billion-grid-upgrade-bill-for-out-of-state-ai-data-centers-state-complains-to-federal-energy-regulators-says-additional-cost-breaks-ratepayer-protection-pledge-promises",
    "source": "lemonberry",
    "platform": "hackernews",
    "points": 319,
    "published_at": "2026-05-10T21:16:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:48108313",
    "domain": "金融",
    "title": "US inflation jumps to 3.8% as energy costs surge from Iran war",
    "url": "https://www.bbc.com/news/articles/c202pgxx89lo",
    "source": "tartoran",
    "platform": "hackernews",
    "points": 260,
    "published_at": "2026-05-12T13:51:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:48023533",
    "domain": "金融",
    "title": "Agents for financial services and insurance",
    "url": "https://www.anthropic.com/news/finance-agents",
    "source": "louiereederson",
    "platform": "hackernews",
    "points": 257,
    "published_at": "2026-05-05T15:05:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:48206387",
    "domain": "金融",
    "title": "The quadratic sandwich",
    "url": "https://fedemagnani.github.io/math/2026/04/08/the-quadratic-sandwich.html",
    "source": "cpp_frog",
    "platform": "hackernews",
    "points": 147,
    "published_at": "2026-05-20T12:06:56+00:00",
    "summary": ""
  },
  {
    "id": "hn:48100152",
    "domain": "金融",
    "title": "590k buyers paid $59M for Trump's gold phone, but not one has shipped",
    "url": "https://finance.yahoo.com/markets/stocks/articles/590-000-buyers-paid-59-223500998.html",
    "source": "surprisetalk",
    "platform": "hackernews",
    "points": 162,
    "published_at": "2026-05-11T20:19:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:48317563",
    "domain": "金融",
    "title": "Microsoft data suggests using AI is more expensive than hiring people",
    "url": "https://finance.yahoo.com/sectors/technology/articles/microsoft-data-suggests-using-ai-225900743.html",
    "source": "voxadam",
    "platform": "hackernews",
    "points": 68,
    "published_at": "2026-05-29T00:49:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:48349067",
    "domain": "金融",
    "title": "Nearly Half of Home Insurance Claims Result in Zero Payout",
    "url": "https://www.wsj.com/finance/the-home-insurance-coin-flip-nearly-half-of-claims-result-in-zero-payout-4b49acaf",
    "source": "bookofjoe",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-05-31T19:45:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:48338988",
    "domain": "金融",
    "title": "Driver, 87, dies after Tesla on Autopilot mode crashes into pond",
    "url": "https://www.usatoday.com/story/news/nation/2026/05/29/tesla-on-autopilot-mode-crashes-into-pond-87-year-old-driver-dies/90319482007/",
    "source": "thinkcontext",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-05-30T17:59:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:48341005",
    "domain": "金融",
    "title": "Tesla's 'Full Self-Driving' fraud lawsuit gets first hearing in China",
    "url": "https://electrek.co/2026/05/30/tesla-fsd-china-lawsuit-first-hearing-10-owners/",
    "source": "breve",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-05-30T21:58:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:48007503",
    "domain": "金融",
    "title": "Why Almost Everyone Loses–Except a Few Sharks–On Prediction Markets",
    "url": "https://www.wsj.com/finance/investing/polymarket-kalshi-betting-profits-prediction-markets-eb23ac11",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 104,
    "published_at": "2026-05-04T11:49:16+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30363",
    "domain": "金融",
    "title": "Enhancing Regime Shift Detection Using Unstructured Data: A Study on the Treasury Market",
    "url": "https://arxiv.org/abs/2605.30363",
    "source": "Mingxuan Yi, Vidal Mehra, Jing Chen, John Cartlidge",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30363v1 Announce Type: new Abstract: Regime shifts in financial markets reorganise the joint dynamics of asset prices and macro variables, breaking any single-regime calibration. They are n"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30435",
    "domain": "金融",
    "title": "Global Science Sustains U.S. Innovation",
    "url": "https://arxiv.org/abs/2605.30435",
    "source": "Christopher R. Esposito",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30435v1 Announce Type: new Abstract: Like physical products, new technologies are developed using globally sourced inputs. Yet while the supply chains behind physical goods are well underst"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30464",
    "domain": "金融",
    "title": "Distributional Portfolio Optimization (DPO): A Unified Framework for Distributions over Weights, Returns, and Parameters",
    "url": "https://arxiv.org/abs/2605.30464",
    "source": "Miquel Noguer i Alonso",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30464v1 Announce Type: new Abstract: Classical portfolio optimization treats expected returns, covariances, and allocations as deterministic. Modern practice replaces at least one by a dist"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30562",
    "domain": "金融",
    "title": "Option Pricing under Stochastic Volatility and Jumps:A PIDE Framework with Empirical Evidence",
    "url": "https://arxiv.org/abs/2605.30562",
    "source": "Abigail Anokyewaa Mensah, Ayush Jha, Hongwei Mei, Rui Wang, Svetlozar T. Rachev, Frank J. Fabozzi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30562v1 Announce Type: new Abstract: We develop a partial integro-differential equation (PIDE) framework for option pricing under joint stochastic volatility and jump dynamics, and evaluate"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30567",
    "domain": "金融",
    "title": "Valuation of GLWB-LTC Annuities with L\\'evy Equity Dynamics, Stochastic Interest Rates and Health-State Transitions",
    "url": "https://arxiv.org/abs/2605.30567",
    "source": "Andrea Molent",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30567v1 Announce Type: new Abstract: This paper develops a valuation framework for guaranteed lifetime withdrawal benefit (GLWB) contracts with long-term care (LTC) features when the refere"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30643",
    "domain": "金融",
    "title": "Quality-Adjusted Hit-Ratio Targeting in Corporate Bond Market Making",
    "url": "https://arxiv.org/abs/2605.30643",
    "source": "Bouna Niang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30643v1 Announce Type: new Abstract: Hit ratio is a common service metric for electronic corporate bond market making, but raw hit-ratio targets can be economically misleading when client f"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30672",
    "domain": "金融",
    "title": "Residual Supply and the Price of Risk Absorption",
    "url": "https://arxiv.org/abs/2605.30672",
    "source": "Ziyao Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30672v1 Announce Type: new Abstract: When redeeming open-end funds sell and natural buyers do not step in at once, some limited-capital investor must take the other side and carry the inven"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30683",
    "domain": "金融",
    "title": "Towards an Ideometrics-Based General Theory of Human Progress",
    "url": "https://arxiv.org/abs/2605.30683",
    "source": "Igor Rudan, Steven Kerr",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30683v1 Announce Type: new Abstract: This paper proposes ideometrics as the foundation for a generalised and potentially testable theory of human progress and civilisational progress, thus "
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30943",
    "domain": "金融",
    "title": "Inspectable Neural Markov Models for Non-Stationary Time Series",
    "url": "https://arxiv.org/abs/2605.30943",
    "source": "Jan Rovirosa, Jesse Schmolze",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30943v1 Announce Type: new Abstract: Modeling non-stationary stochastic systems requires balancing the representational capacity of deep learning with the structural transparency of classic"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30442",
    "domain": "金融",
    "title": "When market boundaries weaken: Network reconfiguration and regime-dependent cross-asset spillovers",
    "url": "https://arxiv.org/abs/2605.30442",
    "source": "Ruixue Jing, Luis Enrique Correa Rocha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30442v1 Announce Type: cross Abstract: Cryptocurrencies are increasingly adopted as investment assets, making their interactions with traditional financial markets central to cross-asset di"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30720",
    "domain": "金融",
    "title": "Kalimati Vegetable Price Index Forecasting with a Momentum Corrected Online Stacking Ensemble",
    "url": "https://arxiv.org/abs/2605.30720",
    "source": "Sahaj Raj Malla",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30720v1 Announce Type: cross Abstract: Forecasting agricultural commodity prices in emerging economies is difficult due to high volatility, frequent supply disruptions, and strong cultural "
  },
  {
    "id": "rss:https://arxiv.org/abs/2503.08503",
    "domain": "金融",
    "title": "Optimal Contract Design with Quadratic Effort Cost",
    "url": "https://arxiv.org/abs/2503.08503",
    "source": "Xinfu Chen, Shuaijie Qian, Guan Qiao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2503.08503v3 Announce Type: replace Abstract: The existence of an optimal contract of the principal-agent problem is a central issue in contract design. According to Cvitani\\'c et al. [2], such "
  },
  {
    "id": "rss:https://arxiv.org/abs/2504.20429",
    "domain": "金融",
    "title": "Estimating the housing production function with unobserved land heterogeneity",
    "url": "https://arxiv.org/abs/2504.20429",
    "source": "Yusuke Adachi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2504.20429v3 Announce Type: replace Abstract: Housing supply in dense cities depends on the ability of builders to substitute capital for scarce land. This margin is difficult to estimate becaus"
  },
  {
    "id": "rss:https://arxiv.org/abs/2507.04545",
    "domain": "金融",
    "title": "Measuring Social Media Network Effects",
    "url": "https://arxiv.org/abs/2507.04545",
    "source": "Sinan Aral, Seth G Benzell, Avinash Collis, Christos Nicolaides",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2507.04545v2 Announce Type: replace Abstract: Network effects -- the utility gains from additional consumers of a good -- are widely regarded as critical to the digital economy. Yet recent theor"
  },
  {
    "id": "rss:https://arxiv.org/abs/2510.15617",
    "domain": "金融",
    "title": "Price Pass-Through of Austria's Single-Use Plastics Producer Charges: Evidence from Retail Offer Spells",
    "url": "https://arxiv.org/abs/2510.15617",
    "source": "Felix Reichel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2510.15617v4 Announce Type: replace Abstract: Single use plastics (SUPs) impose substantial environmental costs. Following Directive (EU) 2019/904, Austria introduced producer charges and mandat"
  },
  {
    "id": "rss:https://arxiv.org/abs/2601.14150",
    "domain": "金融",
    "title": "Trade relationships during and after a crisis",
    "url": "https://arxiv.org/abs/2601.14150",
    "source": "Alejandra Martinez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2601.14150v3 Announce Type: replace Abstract: This paper provides causal evidence that temporary supply disruptions reshape firms' relationship portfolios in international trade. Using exogenous"
  },
  {
    "id": "rss:https://arxiv.org/abs/2603.29317",
    "domain": "金融",
    "title": "Should I State or Should I Show? Aligning AI with Human Preferences",
    "url": "https://arxiv.org/abs/2603.29317",
    "source": "Keaton Ellis, Wanying Huang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2603.29317v2 Announce Type: replace Abstract: As AI agents become more autonomous, properly aligning their objectives with human preferences becomes increasingly important. We study how effectiv"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.20636",
    "domain": "金融",
    "title": "Continuous Timing Signals for Growth-Defensive Style Allocation: Factor Attribution, Risk Matching, and Out-of-Sample Evidence",
    "url": "https://arxiv.org/abs/2605.20636",
    "source": "Zheli Xiong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.20636v2 Announce Type: replace Abstract: This paper studies conditional allocation between a growth/technology ETF basket, denoted by $G$, and a defensive income/value-oriented ETF basket, "
  },
  {
    "id": "rss:https://arxiv.org/abs/2509.13323",
    "domain": "金融",
    "title": "AI Behavioral Science",
    "url": "https://arxiv.org/abs/2509.13323",
    "source": "Matthew O. Jackson, Qiaozhu Me, Stephanie W. Wang, Yutong Xie, Walter Yuan, Seth Benzell, Erik Brynjolfsson, Colin F. Camerer, James Evans, Brian Jabarian, Jon Kleinberg, Juanjuan Meng, Sendhil Mullainathan, Asuman Ozdaglar, Thomas Pfeiffer, Moshe Tennenholtz, Robb Willer, Diyi Yang, Teng Ye",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2509.13323v2 Announce Type: replace-cross Abstract: We outline a foundation for a new field of ``AI Behavioral Science,'' covering three perspectives. First, as AI becomes ubiquitous and is incr"
  },
  {
    "id": "hn:48328797",
    "domain": "金融",
    "title": "Federal judge orders Trump's name be removed from Kennedy Center",
    "url": "https://www.msn.com/en-us/news/politics/federal-judge-orders-trump-s-name-be-removed-from-kennedy-center/ar-AA24neRw",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 27,
    "published_at": "2026-05-29T20:29:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:48327518",
    "domain": "金融",
    "title": "Americans Are Falling Behind on Their $1.25T Credit-Card Bill",
    "url": "https://www.wsj.com/personal-finance/credit/us-credit-card-debt-af5c7c77",
    "source": "tcp_handshaker",
    "platform": "hackernews",
    "points": 26,
    "published_at": "2026-05-29T18:41:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:48333813",
    "domain": "金融",
    "title": "Tesla Self-Certifies Level 4 Autonomous Vehicles in Texas",
    "url": "https://www.notateslaapp.com/news/4216/tesla-self-certifies-l4-autonomy-in-texas",
    "source": "frankacter",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-05-30T07:58:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:48055238",
    "domain": "金融",
    "title": "Cloudflare lays off 1,100 employees (~20% of workforce)",
    "url": "https://finance.yahoo.com/markets/stocks/articles/cloudflare-announces-first-quarter-2026-201500778.html",
    "source": "gcr",
    "platform": "hackernews",
    "points": 83,
    "published_at": "2026-05-07T21:22:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:48210413",
    "domain": "金融",
    "title": "Standard Chartered CEO walks back comment about 'lower-value human capital'",
    "url": "https://www.wsj.com/finance/banking/ceo-walks-back-comment-about-replacing-lower-value-human-capital-with-ai-15bdfc5c",
    "source": "Brajeshwar",
    "platform": "hackernews",
    "points": 57,
    "published_at": "2026-05-20T16:38:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:48271942",
    "domain": "金融",
    "title": "Show HN: Fungible – A local personal finance app in the terminal",
    "url": "https://github.com/tomfunk/fungible",
    "source": "tomfunk",
    "platform": "hackernews",
    "points": 30,
    "published_at": "2026-05-25T21:35:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:48271001",
    "domain": "金融",
    "title": "Stablecoins Are Private Money. That's Why They're a Risk to the Economy",
    "url": "https://www.wsj.com/finance/currencies/stablecoins-are-private-money-thats-why-theyre-a-risk-to-the-economy-d3498171",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 27,
    "published_at": "2026-05-25T20:02:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:48307404",
    "domain": "金融",
    "title": "Why Tesla's AI trainers don't trust its self-driving tech – or its safety stats",
    "url": "https://www.reuters.com/investigations/why-teslas-ai-trainers-dont-trust-its-self-driving-tech-or-its-safety-stats-2026-05-28/",
    "source": "puzzlingcaptcha",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-05-28T11:21:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:48221518",
    "domain": "金融",
    "title": "Tesla Cybertruck driver arrested after driving into lake to use 'wade mode'",
    "url": "https://www.bbc.co.uk/news/articles/c072x1kml44o",
    "source": "LaSombra",
    "platform": "hackernews",
    "points": 35,
    "published_at": "2026-05-21T12:24:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:48199462",
    "domain": "金融",
    "title": "Invisible_playwright: Stealth Firefox that passes every bot detection test",
    "url": "https://github.com/feder-cr/invisible_playwright",
    "source": "thunderbong",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-05-19T20:51:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:48104043",
    "domain": "金融",
    "title": "Arcadia, CA, Mayor Federally Charged with Acting as Illegal Agent of PRC, Pleads",
    "url": "https://www.justice.gov/usao-cdca/pr/arcadia-mayor-federally-charged-acting-illegal-agent-peoples-republic-china",
    "source": "737min",
    "platform": "hackernews",
    "points": 37,
    "published_at": "2026-05-12T03:59:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:48229518",
    "domain": "金融",
    "title": "Show HN: Smithereen – an early-Facebook-style Fediverse server",
    "url": "https://smithereen.software",
    "source": "grishka",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-05-21T22:18:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:48033721",
    "domain": "金融",
    "title": "Fedora is now the default Linux recommendation, and Ubuntu did this to itself",
    "url": "https://www.xda-developers.com/fedora-becoming-default-linux-recommendation-ubuntu-fault/",
    "source": "bundie",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-05-06T08:27:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:47992303",
    "domain": "金融",
    "title": "Wyoming celebrates 'nuclear Renaissance' as feds approve license for a reactor",
    "url": "https://text.npr.org/nx-s1-5798892",
    "source": "mooreds",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-05-03T01:18:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:48004992",
    "domain": "金融",
    "title": "Feds Fine Durham Energy Efficiency Co $722M",
    "url": "https://www.theassemblync.com/news/business/american-efficient-ferc-durham-fine/",
    "source": "ChuckMcM",
    "platform": "hackernews",
    "points": 31,
    "published_at": "2026-05-04T05:32:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:48040639",
    "domain": "金融",
    "title": "Google to sell TPU chips to select customers",
    "url": "https://finance.yahoo.com/markets/stocks/article/google-to-sell-tpu-chips-to-select-customers-in-latest-shot-at-nvidia-214900221.html",
    "source": "gmays",
    "platform": "hackernews",
    "points": 28,
    "published_at": "2026-05-06T19:34:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:48060663",
    "domain": "金融",
    "title": "Salary isn't everything: Why flexibility to work remotely is the future of work",
    "url": "https://thehill.com/opinion/finance/5859902-hybrid-work-performance-retention/",
    "source": "robtherobber",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-05-08T09:20:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:48115538",
    "domain": "金融",
    "title": "America is experiencing a productivity miracle",
    "url": "https://www.economist.com/finance-and-economics/2026/05/11/america-is-experiencing-a-productivity-miracle",
    "source": "mackmcconnell",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-05-12T22:39:47+00:00",
    "summary": ""
  }
]
```
