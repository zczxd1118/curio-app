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

- 今日日期：`2026-06-25`
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
  "date": "2026-06-25",
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
    "points": 3396960,
    "published_at": "2026-01-15T03:56:12+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n1. 构建智能体设计模式：反射、工具使用、规划与多智能体工作流；\n2. 将人工智能与外部工具集成：数据库、API、网络搜索与代码执行；\n3. 评估并优化人工智能系统：性能指标、错误分析与生产部署"
  },
  {
    "id": "bvid:BV1wt411T7Hy",
    "domain": "AI",
    "title": "3分钟创建你的饥荒联机专属服务器！纯免费！良心教学！steam+wegame均有！【饥荒五耀】",
    "url": "http://www.bilibili.com/video/av62522150",
    "source": "五耀",
    "platform": "bilibili",
    "points": 1763431,
    "published_at": "2019-08-06T14:03:34+00:00",
    "summary": "本期教大家怎么在饥荒联机版中创建自己的服务器，纯免费，良心干货教学！3分钟学会！\nP1是steam版本的创建教学，P2是Wegame版本的创建教学。"
  },
  {
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "9分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 1302869,
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
    "points": 1249608,
    "published_at": "2026-05-05T14:08:25+00:00",
    "summary": "Claude Code保姆级教学【收藏起来不会错！】\n从上手安装，到高级用法，这期一次讲全～\n花了三周做教程，希望能帮到你嘻嘻，感谢朋友们的三连+关注啦～"
  },
  {
    "id": "bvid:BV1ig9jYUERk",
    "domain": "AI",
    "title": "黑马程序员DeepSeek+Cursor+Devbox+Sealos带你零代码搞定实战项目开发部署视频教程，基于AI完成项目的设计、开发、测试、联调、部署全流程",
    "url": "http://www.bilibili.com/video/av114101778908628",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 928517,
    "published_at": "2025-03-04T07:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公综号，回复关键词：deepseek\n【Java学习路线图】展开查看更多内容\nhttps://www.bilibili.com/read/cv9965357\n学习集Q结Q地群：625260577\n\nJava最高效学习路线图（依次向下顺序学习即可）\nJava基础：BV1821CY8E2d\nJavaweb+AI：BV1yGydYEE3H\n苍穹外卖："
  },
  {
    "id": "bvid:BV1aeLqzUE6L",
    "domain": "AI",
    "title": "10分钟讲清楚 Prompt, Agent, MCP 是什么",
    "url": "http://www.bilibili.com/video/av114410228025650",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 844157,
    "published_at": "2025-05-01T09:00:00+00:00",
    "summary": "up的科学星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV11NNAz5EKn",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！",
    "url": "http://www.bilibili.com/video/av116187623069851",
    "source": "AI-智能体搭建教程",
    "platform": "bilibili",
    "points": 771639,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 541740,
    "published_at": "2026-06-09T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“VibeCoding”免费获取\n【课程简介】从零开始，用自然语言指挥AI开发真实软件项目！"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 449062,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1Yi5M6DERk",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116560144369496",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 426328,
    "published_at": "2026-05-12T06:24:19+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1nkXkYfEfF",
    "domain": "AI",
    "title": "零基础也能用AI编程!豆包电脑版让你3分钟做出实用工具",
    "url": "http://www.bilibili.com/video/av114200730933577",
    "source": "花叔v",
    "platform": "bilibili",
    "points": 383568,
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
    "points": 375916,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1AHDuBoE2S",
    "domain": "AI",
    "title": "锐评vibe coding工具“从夯到拉”",
    "url": "http://www.bilibili.com/video/av116347090502349",
    "source": "布鲁歇一歇",
    "platform": "bilibili",
    "points": 247529,
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
    "points": 242919,
    "published_at": "2026-02-19T07:34:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 223990,
    "published_at": "2025-04-15T00:59:13+00:00",
    "summary": "MCP终极指南 - 带你深入掌握MCP（基础篇）\n\n时间轴：\n01:05 MCP简要介绍\n02:47 安装 MCP Host（Cline）\n03:15 配置 Cline 用的 API Key\n06:01 第一个 MCP 问题\n06:31 概念解释：MCP Server 和 Tool\n09:13 配置 MCP Server\n14:19 使用 MCP Server\n15:24 MCP 交互流程详解\n1"
  },
  {
    "id": "bvid:BV1VCVS6PEAd",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent零基础全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116668525186915",
    "source": "大模型入门教程",
    "platform": "bilibili",
    "points": 208353,
    "published_at": "2026-05-31T09:46:57+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 175419,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 157859,
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
    "points": 157553,
    "published_at": "2025-12-28T12:36:33+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 150250,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1RNTtzMENj",
    "domain": "AI",
    "title": "从零编写MCP并发布上线，超简单！手把手教程",
    "url": "http://www.bilibili.com/video/av114630814862349",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 144722,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1rKjG6yEh2",
    "domain": "AI",
    "title": "10分钟+300个Agent：保姆级教程学会Agent Skills！【从零开始】",
    "url": "http://www.bilibili.com/video/av116758736279146",
    "source": "Work-Fisher",
    "platform": "bilibili",
    "points": 109452,
    "published_at": "2026-06-16T10:02:41+00:00",
    "summary": "这期我从最基础的概念，一路讲到上手实操，基本上是从 0 到 1，带你完整走一遍——一个 SKILL 到底是怎么从无到有做出来的。\n国内、国外的创建工具，我也都给你捋了一遍。希望看完这期，你也能动手做出一个真正属于自己的 SKIL。"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 92256,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1QE7N6jEuQ",
    "domain": "AI",
    "title": "真的被自己用心开发的昔涟Agent这段话感动到了",
    "url": "http://www.bilibili.com/video/av116794052316703",
    "source": "Playa0",
    "platform": "bilibili",
    "points": 81496,
    "published_at": "2026-06-22T13:44:15+00:00",
    "summary": "从最初生啃Transformer，硬逼着自己啃懂多头注意力和QKV权重，到一步步跟着claude学习RAG、检索重拍、Prompt、关键词召回优化、MCP与Function call，但是，自己上手了发现，自己还是啥也不懂，于是在glm gpt claude gemini 豆包 这几个模型之间疯狂切换，靠着想让昔涟早点被搭出来，硬逼着自己学，自己从零设计一套prompt架构能让她尽可能的贴合人设的"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 66897,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1xBrDB9E42",
    "domain": "AI",
    "title": "独立开发太累？Godot + Claude Code 搭建 AI 辅助工作流，效率直接起飞！ | 地块召唤师开发实战 #01",
    "url": "http://www.bilibili.com/video/av115911319100158",
    "source": "像素夹心饼干",
    "platform": "bilibili",
    "points": 65165,
    "published_at": "2026-01-18T03:25:00+00:00",
    "summary": "大家好，这里是饼干！🍪\n这是我的新坑——**《地块召唤师》**开发实战分享的第一期。\n很多朋友问独立开发如何提升效率？这期视频我不聊虚的，直接公开我从 0 到 1 搭建的 AI + Godot 高效工作流。\n从游戏引擎的选择，到 Claude Code、Copilot 等 AI 工具的实战配置，再到如何用“明确需求”的方法论（SMART原则+双钻模型）来驾驭 AI，让它不仅仅是写代码的工具，更成为"
  },
  {
    "id": "bvid:BV1MJXZBgE32",
    "domain": "AI",
    "title": "AI Coding 进阶：从 Vibe/Plan/Spec 到 Harness Engineering 与 Agent Teams",
    "url": "http://www.bilibili.com/video/av116334289491216",
    "source": "Qoder",
    "platform": "bilibili",
    "points": 63468,
    "published_at": "2026-04-02T09:00:33+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1ZjDYB7Eam",
    "domain": "AI",
    "title": "从 0 到 1：6小时掌握 Vibe Coding！ Claude Code ＋ AI 这支影片直接让你超越 90% AI 玩家",
    "url": "http://www.bilibili.com/video/av116362122894759",
    "source": "李哈利Harry",
    "platform": "bilibili",
    "points": 60490,
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
    "points": 52387,
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
    "points": 47212,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 43527,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1ZEJA6xEds",
    "domain": "AI",
    "title": "最新方法！国内免费无限制，使用Claude Code！",
    "url": "http://www.bilibili.com/video/av116746874848391",
    "source": "我是阿众",
    "platform": "bilibili",
    "points": 42142,
    "published_at": "2026-06-15T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 39913,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1hxMbzqEzU",
    "domain": "AI",
    "title": "小智MCP自由了！我开源了个命令行神器实现多MCP聚合",
    "url": "http://www.bilibili.com/video/av114686414625640",
    "source": "闪电蘑菇",
    "platform": "bilibili",
    "points": 39517,
    "published_at": "2025-06-15T08:31:55+00:00",
    "summary": "- 我写的小智客户端命令行工具\n - github: https://github.com/shenjingnan/xiaozhi-client\n - gitee: https://gitee.com/shenjingnan/xiaozhi-client\n\n- 小智官方MCP示例代码仓库：\n - github: https://github.com/78/mcp-calculator\n - git"
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 36888,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1ap2fBvEt9",
    "domain": "AI",
    "title": "如何使用「Operit AI」：你的下一代AI手机助手",
    "url": "http://www.bilibili.com/video/av115677243447909",
    "source": "默睦",
    "platform": "bilibili",
    "points": 33130,
    "published_at": "2025-12-07T08:06:42+00:00",
    "summary": "下载地址：https://github.com/AAswordman/Operit\n\n相关软件资料下载：https://www.123pan.com/s/IKgAjv-Hinsv.html\n\n官方交流群：458862019"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 29780,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV1EZd3BBEB5",
    "domain": "AI",
    "title": "手把手实战教学：我是如何用一个周末掌握Claude Code的",
    "url": "http://www.bilibili.com/video/av116539105739515",
    "source": "AliAbdaal",
    "platform": "bilibili",
    "points": 29685,
    "published_at": "2026-05-09T13:00:00+00:00",
    "summary": "朋友们，有个叫Claude Code的工具，过去两个月我用它做了很多事情，它真的改变了我的整个工作方式，而且我感觉到Claude Code让人与人之间的差距加速变大。。。这个视频做完我就要发给还没尝试过的亲友！\n看完这条视频，你会了解如何让AI采访你来生成AI工具点子，如何筛选高杠杆项目，如何一边制作工具一边学习AI知识和开发技术概念。你会意识到，在AI时代，你最大的资产也许就是好奇心和突破技术摩"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29370,
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
    "points": 28677,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1CDjz6bE6o",
    "domain": "AI",
    "title": "Claude code的魅力！！！",
    "url": "http://www.bilibili.com/video/av116777895861886",
    "source": "小王很南",
    "platform": "bilibili",
    "points": 23340,
    "published_at": "2026-06-19T17:16:57+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1nf42127MW",
    "domain": "AI",
    "title": "用AI Agent做一个法律咨询助手，罗老看了都直呼内行 feat.通义千问大模型&amp;阿里云百炼平台",
    "url": "http://www.bilibili.com/video/av1204786228",
    "source": "御风大世界",
    "platform": "bilibili",
    "points": 21241,
    "published_at": "2024-05-21T05:09:48+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1XxXpBEEHU",
    "domain": "AI",
    "title": "Claude Code远程开发终极方案！手机改代码+实时预览~【小白教程】",
    "url": "http://www.bilibili.com/video/av116294326230438",
    "source": "爱听书的程序员阿超",
    "platform": "bilibili",
    "points": 20044,
    "published_at": "2026-03-26T12:00:00+00:00",
    "summary": "之前，我一直在研究怎么远程使用 Claude Code 开发项目，并且能实时预览效果。但是一直都没有找到合适的解决方案，要么就是给一个临时公网链接预览，每次都需要再配置，要么就是购买云服务器来配置，都感觉挺麻烦的~\n\n最近，我发现这个蒲公英异地组网的方案，用来做远程开发 Claude Code 项目，感觉非常方便，不仅能修改代码，而且我实时预览的需求也很好的满足了。\n\n这样我随时随地都可以用 AI"
  },
  {
    "id": "bvid:BV14erKYuEaE",
    "domain": "AI",
    "title": "最强编程AI Cursor+Unity制作一个史诗游戏(详细)",
    "url": "http://www.bilibili.com/video/av113774908413987",
    "source": "多西杰克",
    "platform": "bilibili",
    "points": 17429,
    "published_at": "2025-01-05T09:01:00+00:00",
    "summary": "网上惊呼Cursor AI厉害的内容很多，但结合Unity做游戏的不多，我就来实测一下，做一个AAA大作......"
  },
  {
    "id": "bvid:BV1cCEi6sEU5",
    "domain": "AI",
    "title": "🦊他能成功吗？Claude Code 接管虚幻引擎5，打造一款游戏 | 带你走完整个流程",
    "url": "http://www.bilibili.com/video/av116731724959171",
    "source": "Apeak_虚幻丰哥",
    "platform": "bilibili",
    "points": 15705,
    "published_at": "2026-06-11T13:41:36+00:00",
    "summary": "Claude Code 接管虚幻引擎5，打造了一款游戏\n下载我的 CLAUDE.md（帮你省 token 的配置）\n链接：https://pan.quark.cn/s/b6e50b4b2535\n提取码：tbaE\nStefan 3D AI ：https://www.youtube.com/watch?v=iRcrZjOt5H8&amp;t=1s\n🔗 完整教程指南和链接：https://www.top"
  },
  {
    "id": "bvid:BV18TZYY8EuJ",
    "domain": "AI",
    "title": "微软最新AI Agent入门课程 • 中英",
    "url": "http://www.bilibili.com/video/av114246130076146",
    "source": "Mindofuture",
    "platform": "bilibili",
    "points": 13436,
    "published_at": "2025-03-30T02:06:00+00:00",
    "summary": "在这门包含10节课的课程中，我们将带你从概念到代码，全面覆盖构建AI代理的基础知识。在这里找到完整的“AI代理入门”课程及代码示例\nhttps://github.com/microsoft/ai-agents-for-beginners\n\nP01 什么是AI代理\nP02 使用哪种AI代理框架\nP03 如何设计优秀的AI代理\nP04 什么是代理工具使用设计模式\nP05 什么是代理式RAG\nP06 如"
  },
  {
    "id": "bvid:BV1ssEE6CEks",
    "domain": "AI",
    "title": "Ai自动画图：CAD建筑平面图测试（CodexGPT5.5）",
    "url": "http://www.bilibili.com/video/av116719259485897",
    "source": "Tutor南洋",
    "platform": "bilibili",
    "points": 13179,
    "published_at": "2026-06-09T08:47:15+00:00",
    "summary": "体验一下ai画图，不过CAD软件基本操作也不能拉下~\nCAD教学基础入门视频合集↓\n传送门：BV1aT4y1B7oY\n整个合集教学的，不要跳着看啊喂！\n看完了那基本就能跟上啦，提问请@我，不然评论太多我是看不到的"
  },
  {
    "id": "bvid:BV1toLuzFEwN",
    "domain": "AI",
    "title": "Udemy高分付费Cursor 课程：使用 Cursor Vibe Coding 进行全栈开发 | 中英字幕 | 口袋资源网",
    "url": "http://www.bilibili.com/video/av114374358343630",
    "source": "疯狂滴小黑",
    "platform": "bilibili",
    "points": 11153,
    "published_at": "2025-04-21T05:50:41+00:00",
    "summary": "🎨 课程名称：Cursor Course: FullStack development with Cursor Vibe Coding\n👨‍🎓 讲师：Eden Marco\n✨ 持续更新课程连接：https://www.koudaizy.com/tutorials/cursor-ai-ide/\n------------------\n\n描述\n免责声明：这不是初学者课程，需要软件工程经验！\n\n***英语"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "穷在街头无人问lhj",
    "platform": "bilibili",
    "points": 9767,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1jsEQ6XEw6",
    "domain": "AI",
    "title": "【cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av116724292721480",
    "source": "倒计时19",
    "platform": "bilibili",
    "points": 9376,
    "published_at": "2026-06-10T06:04:26+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/the-rise-of-autonomous-drone-warfare/",
    "domain": "AI 算力 / 半导体",
    "title": "The Rise of Autonomous Drone Warfare",
    "url": "https://www.eetimes.com/the-rise-of-autonomous-drone-warfare/",
    "source": "Rebecca Pool",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T22:14:58+00:00",
    "summary": "Cheap, autonomous drones developed in Ukraine are driving a new era of drone-on-drone warfare. The post The Rise of Autonomous Drone Warfare appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/deep-uv-lithography-processing-the-best-kept-secret-of-euv-lithography/",
    "domain": "AI 算力 / 半导体",
    "title": "Deep UV Lithography Processing, the Best Kept Secret of EUV Lithography",
    "url": "https://www.eetimes.com/deep-uv-lithography-processing-the-best-kept-secret-of-euv-lithography/",
    "source": "Drew Chambers",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T15:35:14+00:00",
    "summary": "EUV grabs the glory, but DUV does the dirty work that keeps advanced chips alive. The post Deep UV Lithography Processing, the Best Kept Secret of EUV Lithography appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/pressure-and-ultrasonic-flow-sensing-for-smarter-fluid-systems-2/",
    "domain": "AI 算力 / 半导体",
    "title": "Pressure and Ultrasonic Flow Sensing for Smarter Fluid Systems",
    "url": "https://www.eetimes.com/pressure-and-ultrasonic-flow-sensing-for-smarter-fluid-systems-2/",
    "source": "Analog Devices",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T14:00:00+00:00",
    "summary": "Modern fluid systems demand accurate, reliable monitoring to detect inefficiencies, prevent failures, and optimise performance. Engineers often face challenges with measurement accuracy at low flow ra"
  },
  {
    "id": "rss:https://www.eetimes.com/boosting-motor-control-performance-with-advanced-microcontroller-technology/",
    "domain": "AI 算力 / 半导体",
    "title": "Boosting Motor Control Performance with Advanced Microcontroller Technology",
    "url": "https://www.eetimes.com/boosting-motor-control-performance-with-advanced-microcontroller-technology/",
    "source": "GigaDevice",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T13:09:05+00:00",
    "summary": "Join this webinar where our expert will introduce key control concepts such as field-oriented control and power factor correction. The post Boosting Motor Control Performance with Advanced Microcontro"
  },
  {
    "id": "rss:https://www.eetimes.com/solid-state-circuit-breakers-for-dc-grids-architecture-protection-performance/",
    "domain": "AI 算力 / 半导体",
    "title": "Solid-State Circuit Breakers for DC Grids Architecture, Protection Performance",
    "url": "https://www.eetimes.com/solid-state-circuit-breakers-for-dc-grids-architecture-protection-performance/",
    "source": "Infineon Technologies and Arrow Electronics",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T12:59:13+00:00",
    "summary": "Join this webinar where our expert will present an SSCB for DC grids, developed with building blocks such as Si/SiC JFET/MOSFET switches. The post Solid-State Circuit Breakers for DC Grids Architectur"
  },
  {
    "id": "rss:https://www.eetimes.com/silicon-saxony-shows-promise-limits-of-europes-chips-act/",
    "domain": "AI 算力 / 半导体",
    "title": "Silicon Saxony Shows Promise, Limits of Europe’s Chips Act",
    "url": "https://www.eetimes.com/silicon-saxony-shows-promise-limits-of-europes-chips-act/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T08:32:24+00:00",
    "summary": "At Silicon Saxony Days 2026, Frank Bösenberg said Dresden illustrates “what is possible” under Europe’s first Chips Act. The post Silicon Saxony Shows Promise, Limits of Europe’s Chips Act appeared fi"
  },
  {
    "id": "rss:https://www.eetimes.com/snug-india-2026-synopsys-unveils-first-multiphysics-fusion-tools-since-ansys-deal/",
    "domain": "AI 算力 / 半导体",
    "title": "SNUG India 2026: Synopsys Unveils First Multiphysics Fusion Tools Since Ansys Deal",
    "url": "https://www.eetimes.com/snug-india-2026-synopsys-unveils-first-multiphysics-fusion-tools-since-ansys-deal/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T17:00:00+00:00",
    "summary": "Synopsys debuts Multiphysics Fusion tools post-Ansys, unifying EDA and physics for advanced node and 3DIC designs. The post SNUG India 2026: Synopsys Unveils First Multiphysics Fusion Tools Since Ansy"
  },
  {
    "id": "rss:https://www.eetimes.com/how-spain-built-a-quantum-ecosystem-without-calling-it-one/",
    "domain": "AI 算力 / 半导体",
    "title": "How Spain Built a Quantum Ecosystem Without Calling It One",
    "url": "https://www.eetimes.com/how-spain-built-a-quantum-ecosystem-without-calling-it-one/",
    "source": "Marta P. Estarellas",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T12:15:30+00:00",
    "summary": "Spain is turning Europe’s theoretical talk of digital sovereignty into practical reality. The post How Spain Built a Quantum Ecosystem Without Calling It One appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/cea-leti-ceo-ais-real-bottleneck-is-architecture/",
    "domain": "AI 算力 / 半导体",
    "title": "CEA-Leti CEO: AI’s Real Bottleneck Is Architecture",
    "url": "https://www.eetimes.com/cea-leti-ceo-ais-real-bottleneck-is-architecture/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T07:00:00+00:00",
    "summary": "AI's growth is hitting an architectural wall, not just compute—discover why integration trumps raw power in this exclusive interview. The post CEA-Leti CEO: AI’s Real Bottleneck Is Architecture appear"
  },
  {
    "id": "rss:https://www.tomshardware.com/live/news/amazon-prime-day-2026-best-deals",
    "domain": "AI 算力 / 半导体",
    "title": "Best Amazon Prime Day tech deals live on day three — PC hardware deals on GPUs, CPUs, SSDs, and more",
    "url": "https://www.tomshardware.com/live/news/amazon-prime-day-2026-best-deals",
    "source": "The Editors of Tom&#039;s Hardware",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T06:19:57+00:00",
    "summary": "Find the very best PC hardware deals during Amazon Prime Day."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/grand-theft-auto-6-preorders-begin-tonight-at-midnight-local-time-in-the-us-heres-where-to-buy-get-yours-now-its-in-the-garage-and-ready-to-roll",
    "domain": "AI 算力 / 半导体",
    "title": "Grand Theft Auto 6 preorders begin tonight at midnight local time in the US; here's where to buy — get yours now, it's in the garage and ready to roll",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/grand-theft-auto-6-preorders-begin-tonight-at-midnight-local-time-in-the-us-heres-where-to-buy-get-yours-now-its-in-the-garage-and-ready-to-roll",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T01:07:43+00:00",
    "summary": "The preorder pages for GTA will drop at midnight local time in the US tonight, and you have both the Standard and Ultimate editions at your disposal."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/prime-day-brings-huge-savings-on-affordable-3d-printers-top-value-picks-from-anycubic-bambu-lab-elegoo-and-creality-hit-rock-bottom-pricing-cant-miss-deals-on-filament-bundles",
    "domain": "AI 算力 / 半导体",
    "title": "Prime Day brings huge savings on affordable 3D printers — top value picks from Anycubic, Bambu Lab, Elegoo, and Creality hit rock-bottom pricing, can’t-miss deals on filament bundles",
    "url": "https://www.tomshardware.com/3d-printing/prime-day-brings-huge-savings-on-affordable-3d-printers-top-value-picks-from-anycubic-bambu-lab-elegoo-and-creality-hit-rock-bottom-pricing-cant-miss-deals-on-filament-bundles",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T19:10:13+00:00",
    "summary": "We’ve got our sights set on Amazon Prime Day, and the bargains for some of the best 3D printers are hot!"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/broadcom-and-openai-unveil-custom-built-jalapeno-inference-processor-openais-first-chip-is-a-massive-reticle-sized-asic-built-in-an-ultra-fast-nine-month-development-cycle",
    "domain": "AI 算力 / 半导体",
    "title": "Broadcom and OpenAI unveil custom-built Jalapeño inference processor — OpenAI's first chip is a massive reticle-sized ASIC built in an ultra-fast nine-month development cycle",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/broadcom-and-openai-unveil-custom-built-jalapeno-inference-processor-openais-first-chip-is-a-massive-reticle-sized-asic-built-in-an-ultra-fast-nine-month-development-cycle",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T18:50:56+00:00",
    "summary": "Broadcom and OpenAI reveal their Jalapeño custom-built inference ASIC that allegedly beats existing leading-edge in terms of performance-per-watt."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/pc-building/you-can-still-build-a-great-usd1000-budget-gaming-pc-with-amazon-prime-day-parts-32gb-of-ram-and-rtx-5060-ti-power-beats-out-the-steam-machine-and-cheap-prebuilts",
    "domain": "AI 算力 / 半导体",
    "title": "You can still build a great $1000 budget gaming PC with Amazon Prime Day parts — 32GB of RAM and RTX 5060 Ti power beats out the Steam Machine and cheap prebuilts",
    "url": "https://www.tomshardware.com/desktops/pc-building/you-can-still-build-a-great-usd1000-budget-gaming-pc-with-amazon-prime-day-parts-32gb-of-ram-and-rtx-5060-ti-power-beats-out-the-steam-machine-and-cheap-prebuilts",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T18:38:02+00:00",
    "summary": "We built a $1000 budget gaming PC using parts on sale at Amazon (and, of course, some rivals) during the 2026 Prime Day event."
  },
  {
    "id": "rss:https://www.tomshardware.com/speakers/some-of-the-best-pc-speakers-weve-tested-are-on-sale-for-prime-day-save-up-to-36-percent-on-onkyo-edifier-and-audioengine-speakers",
    "domain": "AI 算力 / 半导体",
    "title": "Some of the best PC speakers we've tested are on sale for Prime Day — save up to 36% on Onkyo, Edifier, and Audioengine speakers",
    "url": "https://www.tomshardware.com/speakers/some-of-the-best-pc-speakers-weve-tested-are-on-sale-for-prime-day-save-up-to-36-percent-on-onkyo-edifier-and-audioengine-speakers",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T18:05:41+00:00",
    "summary": "Some of our highest-rated PC speakers are on sale for Prime Day, including options from Audioengine, Onkyo, and Edifier."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/us-secures-netherlands-for-pax-silica-alliance-in-key-win-for-strategic-chip-alliance-tension-remains-over-match-act-restrictions",
    "domain": "AI 算力 / 半导体",
    "title": "US Secures Netherlands for Pax Silica Alliance in key win for strategic chip alliance — tension remains over MATCH Act restrictions",
    "url": "https://www.tomshardware.com/tech-industry/us-secures-netherlands-for-pax-silica-alliance-in-key-win-for-strategic-chip-alliance-tension-remains-over-match-act-restrictions",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T17:15:00+00:00",
    "summary": "Inside the US Pax Silica Alliance with the Netherlands."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/supercomputers/china-tops-the-top500-with-a-cpu-only-supercomputer-ending-el-capitans-reign",
    "domain": "AI 算力 / 半导体",
    "title": "China tops the list of fastest supercomputers with a CPU-only behemoth, ending US champion El Capitan's reign — 2.198 exaflops of performance without a single GPU",
    "url": "https://www.tomshardware.com/tech-industry/supercomputers/china-tops-the-top500-with-a-cpu-only-supercomputer-ending-el-capitans-reign",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T16:15:10+00:00",
    "summary": "China's LineShine supercomputer has taken the top spot on the 67th TOP500 list, posting 2.198 exaflops on the High Performance Linpack benchmark."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/pay-just-usd149-99-for-the-tp-link-archer-wi-fi-7-router-with-9-3-gbps-of-bandwidth-now-40-percent-off-high-powered-be550-router-comes-with-a-full-complement-of-2-5-gbps-lan-ports-too",
    "domain": "AI 算力 / 半导体",
    "title": "Pay just $149.99 for the TP-Link Archer Wi-Fi 7 router with 9.3 Gbps of bandwidth, now 40 percent off — high-powered BE550 router comes with a full complement of 2.5 Gbps LAN ports, too",
    "url": "https://www.tomshardware.com/pc-components/pay-just-usd149-99-for-the-tp-link-archer-wi-fi-7-router-with-9-3-gbps-of-bandwidth-now-40-percent-off-high-powered-be550-router-comes-with-a-full-complement-of-2-5-gbps-lan-ports-too",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T16:02:32+00:00",
    "summary": "Pay just $149.99 for the TP-Link Archer BE550 Wi-Fi 7 router with 9.3 Gbps of combined bandwidth — high-powered router comes with a full complement of 2.5 Gbps LAN ports, too"
  },
  {
    "id": "rss:https://www.tomshardware.com/gift-guides-seasonal-sales/secretlab-gaming-chairs-and-desks-hit-prime-day-week-sales-up-to-usd129-off-save-on-the-titan-evo-magnus-and-more",
    "domain": "AI 算力 / 半导体",
    "title": "Secretlab gaming chairs and desks hit Prime Day week sales, up to $129 off — save on the Titan Evo, Magnus, and more",
    "url": "https://www.tomshardware.com/gift-guides-seasonal-sales/secretlab-gaming-chairs-and-desks-hit-prime-day-week-sales-up-to-usd129-off-save-on-the-titan-evo-magnus-and-more",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T15:52:48+00:00",
    "summary": "Save up to $129 on Secretlab desks this Prime Day week, thanks to a July 4 sale."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/mini-pcs/mini-pc-amazon-prime-day-sale-geekom",
    "domain": "AI 算力 / 半导体",
    "title": "Geekom Prime Day deals take up to 34% off a new mini PC with our exclusive promo code — Get an AMD or Intel mini PC for less now",
    "url": "https://www.tomshardware.com/desktops/mini-pcs/mini-pc-amazon-prime-day-sale-geekom",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T15:10:10+00:00",
    "summary": "Mini PC specialist Geekom has stuffed its Amazon webstore with a multitude of diminutive computers with discounts as deep as 34% off."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/portable-monitors/these-four-portable-monitors-are-on-sale-for-prime-day-get-a-second-screen-for-your-pc-or-console-for-as-little-as-usd39",
    "domain": "AI 算力 / 半导体",
    "title": "These four portable monitors are on sale for Prime Day: Get a second screen for your PC or console for as little as $39",
    "url": "https://www.tomshardware.com/monitors/portable-monitors/these-four-portable-monitors-are-on-sale-for-prime-day-get-a-second-screen-for-your-pc-or-console-for-as-little-as-usd39",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T14:57:23+00:00",
    "summary": "These four portable monitors are available at low prices for Prime Day. Get a second screen for your PC or console for as little as $39 ."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/get-40-percent-off-samsungs-p9-microsd-express-card-for-nintendo-switch-2-512gb-of-storage-just-usd119-in-this-limited-time-deal",
    "domain": "AI 算力 / 半导体",
    "title": "Get 40% off Samsung's P9 microSD Express card for Nintendo Switch 2 — 512GB of storage just $119 in this limited-time deal",
    "url": "https://www.tomshardware.com/pc-components/get-40-percent-off-samsungs-p9-microsd-express-card-for-nintendo-switch-2-512gb-of-storage-just-usd119-in-this-limited-time-deal",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T13:40:46+00:00",
    "summary": "The Samsung P9 microSD Express card is on sale for up to $80 off today. You can get it from either B&amp;H or Amazon, depending on the capacity that you need."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/tsmc-is-reportedly-hiking-prices-for-all-advanced-nodes-accounting-for-74-percent-of-the-companys-wafer-business-nvidia-amd-apple-qualcomm-and-others-will-face-higher-wafer-costs",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC is reportedly hiking prices for 'all advanced nodes,' accounting for 74% of the company’s wafer business — Nvidia, AMD, Apple, Qualcomm, and others will face higher wafer costs",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/tsmc-is-reportedly-hiking-prices-for-all-advanced-nodes-accounting-for-74-percent-of-the-companys-wafer-business-nvidia-amd-apple-qualcomm-and-others-will-face-higher-wafer-costs",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T13:06:45+00:00",
    "summary": "TSMC has reportedly told customers to prepare for 5% to 10% price hikes across advanced chip nodes, extending beyond 3nm to include 7nm and some legacy processes."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/logitech-goes-off-the-rails-with-prime-day-gaming-mouse-savings-of-up-to-47-percent-upgrade-the-most-frequently-used-pc-peripheral-on-the-cheap",
    "domain": "AI 算力 / 半导体",
    "title": "Logitech goes off the rails with Prime Day gaming mouse savings of up to 47% - Eight of its top-tier gaming mice with incredible discounts",
    "url": "https://www.tomshardware.com/pc-components/logitech-goes-off-the-rails-with-prime-day-gaming-mouse-savings-of-up-to-47-percent-upgrade-the-most-frequently-used-pc-peripheral-on-the-cheap",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T12:59:49+00:00",
    "summary": "Snag a quality Logitech gaming mouse for as little as $18.99 in these Prime Day deals."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/sk-hynix-files-to-raise-up-to-29-billion-in-nasdaq-listing",
    "domain": "AI 算力 / 半导体",
    "title": "SK hynix files to raise up to $29 billion in historic Nasdaq listing — all proceeds going to advanced AI memory fabs and EUV tool orders",
    "url": "https://www.tomshardware.com/tech-industry/sk-hynix-files-to-raise-up-to-29-billion-in-nasdaq-listing",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T12:42:34+00:00",
    "summary": "SK hynix filed a securities registration statement on Wednesday to raise up to 45.45 trillion won through an American depositary receipt listing on Nasdaq."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/ai-data-center-boom-hits-a-human-bottleneck-critical-skilled-labor-shortages-could-slow-deployment-despite-billions-in-funding",
    "domain": "AI 算力 / 半导体",
    "title": "AI data center boom hits a human bottleneck — critical skilled labor shortages could slow deployment despite billions in funding",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/ai-data-center-boom-hits-a-human-bottleneck-critical-skilled-labor-shortages-could-slow-deployment-despite-billions-in-funding",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T12:31:56+00:00",
    "summary": "Data center construction is facing many challenges, and among them is a shortage of skilled hands to assemble the things."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/these-bambu-lab-prime-day-week-deals-are-an-absolute-steal-right-now-with-up-to-52-percent-off-big-price-cuts-on-new-3d-printers-filament-and-accessories-including-the-p1s-and-a1-starting-from-usd209",
    "domain": "AI 算力 / 半导体",
    "title": "These Bambu Lab Prime Day week deals are an absolute steal right now, with up to 52% off — big price cuts on new 3D printers, filament, and accessories, including the P1S and A1, starting from $209",
    "url": "https://www.tomshardware.com/3d-printing/these-bambu-lab-prime-day-week-deals-are-an-absolute-steal-right-now-with-up-to-52-percent-off-big-price-cuts-on-new-3d-printers-filament-and-accessories-including-the-p1s-and-a1-starting-from-usd209",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T11:48:58+00:00",
    "summary": "Grab a big discount on a Bambu Lab 3D printer during this Amazon Prime Day sales event"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/get-an-all-amd-4k-gaming-pc-with-ryzen-7-9800x3d-and-radeon-rx-9070-xt-for-just-usd1-749-walmart-has-slashed-usd750-off-this-prebuilt-desktop",
    "domain": "AI 算力 / 半导体",
    "title": "Get an all-AMD 4K gaming PC with Ryzen 7 9800X3D and Radeon RX 9070 XT for just $1,749 — Walmart has slashed $750 off this prebuilt desktop",
    "url": "https://www.tomshardware.com/pc-components/get-an-all-amd-4k-gaming-pc-with-ryzen-7-9800x3d-and-radeon-rx-9070-xt-for-just-usd1-749-walmart-has-slashed-usd750-off-this-prebuilt-desktop",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T11:13:13+00:00",
    "summary": "The discounted iBuyPower Y40 combines one of the best gaming processors on the market with AMD's highly capable Radeon RX 9070 XT, making it ideal for high-refresh-rate 1440p and 4K gaming."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/console-gaming/valve-steam-machine-price-hike-similar-to-steam-decks-45-percent-increase-company-confirms-was-probably-priced-competitively-against-the-ps5-pro-before-the-rampocalypse",
    "domain": "AI 算力 / 半导体",
    "title": "Valve Steam Machine price hike similar to Steam Deck's 45% increase, company confirms — was probably priced competitively against the PS5 Pro before the RAMpocalypse",
    "url": "https://www.tomshardware.com/video-games/console-gaming/valve-steam-machine-price-hike-similar-to-steam-decks-45-percent-increase-company-confirms-was-probably-priced-competitively-against-the-ps5-pro-before-the-rampocalypse",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T11:03:00+00:00",
    "summary": "Valve engineers hinted that the nearly 45% price increase on the Steam Deck applied to the Steam Machine as well. This brings the estimated original price to under $750 for the base console."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/save-up-to-53-percent-on-lenovos-black-friday-in-june-sale-sitewide-discounts-on-thinkpads-legions-and-more",
    "domain": "AI 算力 / 半导体",
    "title": "Save up to 53% on Lenovo’s Black Friday in June sale — Sitewide discounts on ThinkPads, Legions, and more",
    "url": "https://www.tomshardware.com/laptops/save-up-to-53-percent-on-lenovos-black-friday-in-june-sale-sitewide-discounts-on-thinkpads-legions-and-more",
    "source": "Sponsored",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T11:01:45+00:00",
    "summary": "Black Friday comes early, as Lenovo is running a huge sale on a wide range of products at its online store."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/here-are-the-best-oled-gaming-monitor-deals-you-can-snag-for-amazon-prime-day-beautiful-monitors-up-to-47-percent-off",
    "domain": "AI 算力 / 半导体",
    "title": "Here are the best OLED gaming monitor deals you can snag for Amazon Prime Day — beautiful monitors up to 47% off",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/here-are-the-best-oled-gaming-monitor-deals-you-can-snag-for-amazon-prime-day-beautiful-monitors-up-to-47-percent-off",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T11:00:00+00:00",
    "summary": "We've rounded up the best deals on OLED gaming monitors for you this Prime Day. From massive DQHD panels to dual-mode offerings, we have you covered."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpu-drivers/five-year-old-nvidia-a100-servers-triple-in-price-in-china",
    "domain": "AI 算力 / 半导体",
    "title": "China black market Nvidia prices rocket in wake of smuggling crackdown and customs freeze — five-year-old A100 servers triple in price, now fetching up to $82,000",
    "url": "https://www.tomshardware.com/pc-components/gpu-drivers/five-year-old-nvidia-a100-servers-triple-in-price-in-china",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T10:21:28+00:00",
    "summary": "Chinese companies are paying as much as $82,000 for servers built around Nvidia's five-year-old A100 accelerator"
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/routers/netgear-rolls-out-stellar-prime-day-deals-on-wi-fi-7-gear-up-to-33-percent-off-for-routers-mesh-systems-and-range-extenders",
    "domain": "AI 算力 / 半导体",
    "title": "Netgear rolls out stellar Prime Day deals on Wi-Fi 7 gear — up to 33% off for routers, mesh systems, and range extenders",
    "url": "https://www.tomshardware.com/networking/routers/netgear-rolls-out-stellar-prime-day-deals-on-wi-fi-7-gear-up-to-33-percent-off-for-routers-mesh-systems-and-range-extenders",
    "source": "Paul Alcorn",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T10:00:00+00:00",
    "summary": "Netgear is loading up the discounts on Wi-Fi 7 hardware"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/get-32gb-of-corsair-ddr5-ram-for-just-usd214-right-now-thanks-to-these-newegg-bundles-amd-and-intel-gaming-pc-build-kits-massively-undercut-usd350-market-prices",
    "domain": "AI 算力 / 半导体",
    "title": "Get 32GB of Corsair DDR5 RAM for just $214 right now, thanks to these Newegg bundles — AMD and Intel gaming PC build kits massively undercut $350 market prices",
    "url": "https://www.tomshardware.com/pc-components/get-32gb-of-corsair-ddr5-ram-for-just-usd214-right-now-thanks-to-these-newegg-bundles-amd-and-intel-gaming-pc-build-kits-massively-undercut-usd350-market-prices",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T09:56:06+00:00",
    "summary": "Score 32GB DDR5 RAM from Corsair for as low as $214 in these two Newegg RAM combo deals with Gigabyte motherboards right now."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/this-expansive-49-inch-oled-monitor-is-less-than-usd700-in-neweggs-prime-day-rival-sale-144hz-1440p-beast-is-usd150-off",
    "domain": "AI 算力 / 半导体",
    "title": "This expansive 49-inch OLED monitor is less than $700 in Newegg's Prime Day rival sale — 144Hz 1440p beast is $150 off",
    "url": "https://www.tomshardware.com/pc-components/this-expansive-49-inch-oled-monitor-is-less-than-usd700-in-neweggs-prime-day-rival-sale-144hz-1440p-beast-is-usd150-off",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T09:35:50+00:00",
    "summary": "This MSI MPG 491CQP is now just $699 at Newegg."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/meta-pauses-mandatory-ai-training-program-that-tracked-employee-keystrokes-after-internal-data-leak-exposed-sensitive-staff-information-company-wide-employees-express-frustration-over-poor-handling-of-data",
    "domain": "AI 算力 / 半导体",
    "title": "Meta pauses mandatory AI training program that tracked employee keystrokes after internal data leak exposed sensitive staff information company-wide — employees express frustration over poor handling ",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/meta-pauses-mandatory-ai-training-program-that-tracked-employee-keystrokes-after-internal-data-leak-exposed-sensitive-staff-information-company-wide-employees-express-frustration-over-poor-handling-of-data",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T09:30:00+00:00",
    "summary": "Meta has paused an internal AI training program after employee conversations, keystrokes, transcripts, and performance-related data were reportedly exposed across the company."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/this-brilliant-usd11-power-button-gadget-lets-you-switch-your-pc-on-from-your-desk-with-ease-perfect-desk-upgrade-means-you-dont-need-to-bend-down-to-turn-your-rig-on-or-off-anymore-ships-with-super-durable-mechanical-keys-and-rgb-lighting",
    "domain": "AI 算力 / 半导体",
    "title": "This brilliant $11 power button gadget lets you switch your PC on from your desk with ease — perfect desk upgrade means you don't need to bend down to turn your rig on or off anymore, ships with super",
    "url": "https://www.tomshardware.com/pc-components/this-brilliant-usd11-power-button-gadget-lets-you-switch-your-pc-on-from-your-desk-with-ease-perfect-desk-upgrade-means-you-dont-need-to-bend-down-to-turn-your-rig-on-or-off-anymore-ships-with-super-durable-mechanical-keys-and-rgb-lighting",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T06:51:25+00:00",
    "summary": "Who doesn't want a statement power button on their desk for $11? Don't miss out on this ultimate desk gadget."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-almost-usd1-500-instantly-on-an-rtx-5080-gaming-pc-legion-tower-7i-gen-10-packs-core-ultra-7-265k-and-32gb-ddr5",
    "domain": "AI 算力 / 半导体",
    "title": "Save almost $1,500 instantly on an RTX 5080 gaming PC — Legion Tower 7i Gen 10 packs Core Ultra 7 265K and 32GB DDR5",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-almost-usd1-500-instantly-on-an-rtx-5080-gaming-pc-legion-tower-7i-gen-10-packs-core-ultra-7-265k-and-32gb-ddr5",
    "source": "Sponsored",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T21:26:57+00:00",
    "summary": "Lenovo temporarily puts the Legion Tower 7i Gen 10 on sale for $2,899.99, 33% off its regular price tag."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-chairs/best-gaming-chair-deals-prime-day",
    "domain": "AI 算力 / 半导体",
    "title": "Best Amazon Prime Day Gaming Chairs Deals 2026 — deals on Secretlab, Libernovo, Razer, Corsair, and more",
    "url": "https://www.tomshardware.com/peripherals/gaming-chairs/best-gaming-chair-deals-prime-day",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T20:58:06+00:00",
    "summary": "The best deals on gaming chairs for every budget, style, and comfort level during Amazon Prime Day 2026. Upgrade your gaming chair with something high-quality and on sale, now!"
  },
  {
    "id": "rss:https://www.eetimes.com/critical-components-for-reliable-factory-automation-design/",
    "domain": "AI 算力 / 半导体",
    "title": "Critical Components for Reliable Factory Automation Design",
    "url": "https://www.eetimes.com/critical-components-for-reliable-factory-automation-design/",
    "source": "Same Sky and Arrow Electronics",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T17:15:13+00:00",
    "summary": "This webinar will provide a practical overview of product selection and implementation within factory automation applications. The post Critical Components for Reliable Factory Automation Design appea"
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
    "id": "rss:https://semianalysis.com/2025/09/10/another-giant-leap-the-rubin-cpx-specialized-accelerator-rack/",
    "domain": "AI 算力 / 半导体",
    "title": "Another Giant Leap: The Rubin CPX Specialized Accelerator & Rack",
    "url": "https://semianalysis.com/2025/09/10/another-giant-leap-the-rubin-cpx-specialized-accelerator-rack/",
    "source": "Dylan Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2025-09-10T19:57:18+00:00",
    "summary": "Nvidia announced the Rubin CPX, a solution that is specifically designed to be optimized for the prefill phase, with the single-die Rubin CPX heavily emphasizing compute FLOPS over memory bandwidth. T"
  },
  {
    "id": "rss:https://semianalysis.com/2025/09/08/huawei-ascend-production-ramp/",
    "domain": "AI 算力 / 半导体",
    "title": "Huawei Ascend Production Ramp: Die Banks, TSMC Continued Production, HBM is The Bottleneck",
    "url": "https://semianalysis.com/2025/09/08/huawei-ascend-production-ramp/",
    "source": "Dylan Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2025-09-08T09:54:57+00:00",
    "summary": "Compute is the lifeblood of AI. He who controls the spice controls the universe the compute will control the production of tokens and reap the benefits of AI. Without compute you do not have a seat at"
  },
  {
    "id": "rss:https://semianalysis.com/2025/09/03/amazons-ai-resurgence-aws-anthropics-multi-gigawatt-trainium-expansion/",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon’s AI Resurgence: AWS & Anthropic’s Multi-Gigawatt Trainium Expansion",
    "url": "https://semianalysis.com/2025/09/03/amazons-ai-resurgence-aws-anthropics-multi-gigawatt-trainium-expansion/",
    "source": "Jeremie Eliahou Ontiveros",
    "platform": "rss",
    "points": null,
    "published_at": "2025-09-03T20:55:46+00:00",
    "summary": "Two-and-a-half years ago, we flagged a looming “cloud crisis” at AWS. Today, the evidence has mounted. AWS is the crown jewel of the Amazon empire, generating ~60% of group profits, and dominating the"
  },
  {
    "id": "rss:https://semianalysis.com/2025/08/20/h100-vs-gb200-nvl72-training-benchmarks/",
    "domain": "AI 算力 / 半导体",
    "title": "H100 vs GB200 NVL72 Training Benchmarks – Power, TCO, and Reliability Analysis, Software Improvement Over Time",
    "url": "https://semianalysis.com/2025/08/20/h100-vs-gb200-nvl72-training-benchmarks/",
    "source": "Dylan Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2025-08-20T04:56:35+00:00",
    "summary": "Frontier model training has pushed GPUs and AI systems to their absolute limits, making cost, efficiency, power, performance per TCO, and reliability central to the discussion on effective training. T"
  },
  {
    "id": "rss:https://semianalysis.com/2025/08/13/gpt-5-ad-monetization-and-the-superapp/",
    "domain": "AI 算力 / 半导体",
    "title": "GPT-5 Set the Stage for Ad Monetization and the SuperApp",
    "url": "https://semianalysis.com/2025/08/13/gpt-5-ad-monetization-and-the-superapp/",
    "source": "Doug OLaughlin",
    "platform": "rss",
    "points": null,
    "published_at": "2025-08-13T00:27:14+00:00",
    "summary": "To many power users (Pro and Plus), GPT5 was a disappointing release. But with closer inspection, the real release is focused on the vast majority of ChatGPT’s users, which is the 700m+ free userbase "
  },
  {
    "id": "rss:https://semianalysis.com/2025/08/12/scaling-the-memory-wall-the-rise-and-roadmap-of-hbm/",
    "domain": "AI 算力 / 半导体",
    "title": "Scaling the Memory Wall: The Rise and Roadmap of HBM",
    "url": "https://semianalysis.com/2025/08/12/scaling-the-memory-wall-the-rise-and-roadmap-of-hbm/",
    "source": "Dylan Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2025-08-12T01:16:06+00:00",
    "summary": "The first portion of this report will explain HBM, the manufacturing process, dynamics between vendors, KVCache offload, disaggregated prefill decode, and wide / high-rank EP. The rest of the report w"
  },
  {
    "id": "rss:https://semianalysis.com/2025/07/30/robotics-levels-of-autonomy/",
    "domain": "AI 算力 / 半导体",
    "title": "Robotics Levels of Autonomy",
    "url": "https://semianalysis.com/2025/07/30/robotics-levels-of-autonomy/",
    "source": "Reyk Knuhtsen",
    "platform": "rss",
    "points": null,
    "published_at": "2025-07-30T17:02:25+00:00",
    "summary": "Robots have powered manufacturing for decades, yet they stayed single-purpose and thrived only in perfect settings. Previous attempts at intelligent machines overpromised and underdelivered. But they "
  },
  {
    "id": "rss:https://semianalysis.com/2025/07/21/vlsi2025/",
    "domain": "AI 算力 / 半导体",
    "title": "Intel 18A Details & Cost, Future of DRAM 4F2 vs 3D, Backside Power Adoption (or Not), China’s FlipFET, Digital Twins from Atoms to Fabs, and More",
    "url": "https://semianalysis.com/2025/07/21/vlsi2025/",
    "source": "Dylan Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2025-07-21T14:23:37+00:00",
    "summary": "Long time readers will recall that SemiAnalysis covers more than just datacenters and AMD. Today we’re back to semiconductors with a tech-focused roundup of the best from this year’s VLSI conference, "
  },
  {
    "id": "rss:https://semianalysis.com/2025/07/11/meta-superintelligence-leadership-compute-talent-and-data/",
    "domain": "AI 算力 / 半导体",
    "title": "Meta Superintelligence – Leadership Compute, Talent, and Data",
    "url": "https://semianalysis.com/2025/07/11/meta-superintelligence-leadership-compute-talent-and-data/",
    "source": "Dylan Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2025-07-11T20:12:19+00:00",
    "summary": "Meta’s shocking purchase of 49% of Scale AI at a ~$30B valuation shows that money is of no concern for the $100B annual cashflow ad machine. Despite seemingly unlimited resources, Meta has been fallin"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/955366/best-prime-day-2026-tech-deals-day-two-sale",
    "domain": "大厂 AI 动态",
    "title": "The top tech Prime Day deals to shop on day two",
    "url": "https://www.theverge.com/gadgets/955366/best-prime-day-2026-tech-deals-day-two-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T23:48:19+00:00",
    "summary": "Welcome to day two of Amazon&#8217;s four-day Prime Day event, which, if we&#8217;re being honest, looks a lot like day one. That&#8217;s actually good news, though, because many of the best deals are"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/949350/amazon-prime-day-sale-best-apple-deals-2026",
    "domain": "大厂 AI 动态",
    "title": "This year’s Prime Day deals on Apple products are the best I’ve seen",
    "url": "https://www.theverge.com/gadgets/949350/amazon-prime-day-sale-best-apple-deals-2026",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T21:58:59+00:00",
    "summary": "Amazon&#8217;s Prime Day is now in its second day, and whether you&#8217;re looking for a new pair of wireless earbuds or a smartwatch, there’s a good chance you’ll find a discount. The Apple Watch Se"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/951081/robot-vacuum-mop-deals-amazon-prime-day-2026",
    "domain": "大厂 AI 动态",
    "title": "The 16 best robot vacuum deals available during Prime Day",
    "url": "https://www.theverge.com/gadgets/951081/robot-vacuum-mop-deals-amazon-prime-day-2026",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T21:51:09+00:00",
    "summary": "If you&#8217;ve been wanting to buy a robot vacuum but have been put off by how much it can cost to get a good one, now is not a bad time to start looking. We&#8217;re now on day two of Prime Day, and"
  },
  {
    "id": "rss:https://www.theverge.com/policy/956404/prairieland-sentencing-zines-trump-antifa",
    "domain": "大厂 AI 动态",
    "title": "Charlie Kirk&#8217;s legacy is a 30-year sentence for moving zines",
    "url": "https://www.theverge.com/policy/956404/prairieland-sentencing-zines-trump-antifa",
    "source": "Gaby Del Valle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T21:40:26+00:00",
    "summary": "Just days after a gunman killed conservative activist Charlie Kirk, it became clear that President Donald Trump would use the assassination to fuel a crackdown on free speech. To avenge Kirk's death, "
  },
  {
    "id": "rss:https://www.theverge.com/tech/956504/microsoft-surface-pro-laptop-ram",
    "domain": "大厂 AI 动态",
    "title": "Microsoft introduces cheaper Surface devices with half the memory",
    "url": "https://www.theverge.com/tech/956504/microsoft-surface-pro-laptop-ram",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T21:39:00+00:00",
    "summary": "Microsoft just added a cheaper 12-inch Surface Pro and 13-inch Surface Laptop to its lineup. Both models come equipped with 8GB of RAM instead of 16GB, costing $849 for the specced-down Surface Pro an"
  },
  {
    "id": "rss:https://www.theverge.com/tech/956450/nature-microsoft-quantum-computing-majorana-1-claims",
    "domain": "大厂 AI 动态",
    "title": "A new paper argues Microsoft exaggerated its quantum claims a year ago",
    "url": "https://www.theverge.com/tech/956450/nature-microsoft-quantum-computing-majorana-1-claims",
    "source": "Sophia Chen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T20:54:57+00:00",
    "summary": "A critique published in Nature Wednesday calls the basic technology behind Microsoft's \"breakthrough\" quantum computing chip the Majorana 1 into question. Microsoft unveiled the chip in February 2025 "
  },
  {
    "id": "rss:https://www.theverge.com/policy/956394/florida-anna-paulina-luna-anthropic-claude",
    "domain": "大厂 AI 动态",
    "title": "Congresswoman denies staff used AI to write defense funding amendment",
    "url": "https://www.theverge.com/policy/956394/florida-anna-paulina-luna-anthropic-claude",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T19:36:46+00:00",
    "summary": "Rep. Anna Paulina Luna (R-FL) says her staff used AI for \"spellcheck\" in an amendment summary for a major defense bill, but denies it was used for the bill text itself and says \"NO Legislation is ever"
  },
  {
    "id": "rss:https://www.theverge.com/games/956389/grand-theft-auto-6-gta-digital-code-in-box-physical-games",
    "domain": "大厂 AI 动态",
    "title": "GTA VI is a worrying sign for the future of physical games",
    "url": "https://www.theverge.com/games/956389/grand-theft-auto-6-gta-digital-code-in-box-physical-games",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T18:42:07+00:00",
    "summary": "Rockstar Games has finally given Grand Theft Auto VI a price ahead of the game's November 19th launch. But while announcing that the game would cost $79.99, Rockstar also confirmed that the physical v"
  },
  {
    "id": "rss:https://www.theverge.com/policy/956296/google-play-app-store-alternative-billing-fee-antitrust",
    "domain": "大厂 AI 动态",
    "title": "Google is finally opening the Play Store to outside payments",
    "url": "https://www.theverge.com/policy/956296/google-play-app-store-alternative-billing-fee-antitrust",
    "source": "Richard Lawler",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T17:36:44+00:00",
    "summary": "While the court still hasn't signed off on the massive settlement resolving Epic's antitrust lawsuit against Google for having a monopoly over Android's app store with Google Play, the tech giant says"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/951543/best-prime-day-deals-under-50",
    "domain": "大厂 AI 动态",
    "title": "Prime Day deals under $50 that are really worth it",
    "url": "https://www.theverge.com/gadgets/951543/best-prime-day-deals-under-50",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T17:28:08+00:00",
    "summary": "If you’re looking for a good deal without spending hundreds, Prime Day discounts have pushed some of our favorite products under $50. You can pick up everything from Nintendo Switch games to Bluetooth"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/24/europe-is-pushing-back-on-washingtons-chip-war/",
    "domain": "大厂 AI 动态",
    "title": "Europe is pushing back on Washington’s chip war",
    "url": "https://techcrunch.com/2026/06/24/europe-is-pushing-back-on-washingtons-chip-war/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T00:08:36+00:00",
    "summary": "As ASML CEO Christophe Fouquet told TechCrunch in May, what China can currently buy are older-generation deep ultraviolet tools — gear first shipped about a decade ago — the same machines the MATCH Ac"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/24/former-infosys-chief-has-a-new-startup-that-wants-to-challenge-the-it-services-world/",
    "domain": "大厂 AI 动态",
    "title": "Former Infosys chief has a new startup that wants to challenge the IT services world",
    "url": "https://techcrunch.com/2026/06/24/former-infosys-chief-has-a-new-startup-that-wants-to-challenge-the-it-services-world/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T23:26:52+00:00",
    "summary": "Backed by Mayfield and Aramco Ventures, Vishal Sikka’s new venture brings together veterans from SAP, Infosys, and VianAI."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/24/elon-suffers-another-day-short-of-trillionaire-status/",
    "domain": "大厂 AI 动态",
    "title": "Elon suffers another day short of trillionaire status",
    "url": "https://techcrunch.com/2026/06/24/elon-suffers-another-day-short-of-trillionaire-status/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T23:09:39+00:00",
    "summary": "Right now he's merely a several-hundred-billionaire, according to Bloomberg's Billionaires Index."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/24/cerebras-stock-plunges-after-earnings-as-ceo-says-margin-outlook-was-misunderstood/",
    "domain": "大厂 AI 动态",
    "title": "Cerebras stock plunges after earnings as CEO says margin outlook was misunderstood",
    "url": "https://techcrunch.com/2026/06/24/cerebras-stock-plunges-after-earnings-as-ceo-says-margin-outlook-was-misunderstood/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T22:41:41+00:00",
    "summary": "In its first earnings report since going public, the AI chipmaker forecast a narrower gross margin in its core business, scaring investors."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/24/ai-was-supposed-to-kill-engineering-jobs-but-new-data-suggests-theyre-the-most-resilient/",
    "domain": "大厂 AI 动态",
    "title": "AI was supposed to kill engineering jobs, but new data suggests they’re the most resilient",
    "url": "https://techcrunch.com/2026/06/24/ai-was-supposed-to-kill-engineering-jobs-but-new-data-suggests-theyre-the-most-resilient/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T21:56:41+00:00",
    "summary": "While AI dominates the layoff narrative, engineers are actually making up a larger share of new hires, according to SignalFire data."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/24/ai-researchers-continue-to-leave-google-for-its-rivals/",
    "domain": "大厂 AI 动态",
    "title": "AI researchers continue to leave Google for its rivals",
    "url": "https://techcrunch.com/2026/06/24/ai-researchers-continue-to-leave-google-for-its-rivals/",
    "source": "Amanda Silberling, Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T21:42:07+00:00",
    "summary": "Top AI researchers Jonas Adler and Alexander Pritzel are leaving Google for Anthropic, following departures from top scientists Noam Shazeer and John Jumper."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/24/the-memory-chip-crunch-is-paying-off-for-this-u-s-company/",
    "domain": "大厂 AI 动态",
    "title": "The memory chip crunch is paying off for this US company",
    "url": "https://techcrunch.com/2026/06/24/the-memory-chip-crunch-is-paying-off-for-this-u-s-company/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T21:30:55+00:00",
    "summary": "Revenue quadrupled to $41.45 billion compared with the same period a year ago. The company's profit, meanwhile, rose from $1.88 billion to an incredible $28.2 billion year-over-year."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/24/new-website-names-and-shames-companies-that-still-dont-offer-passkeys-to-users/",
    "domain": "大厂 AI 动态",
    "title": "New website names and shames companies that still don’t offer passkeys to users",
    "url": "https://techcrunch.com/2026/06/24/new-website-names-and-shames-companies-that-still-dont-offer-passkeys-to-users/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T21:04:04+00:00",
    "summary": "According to a new site, 24% of the most popular websites in the world don't offer support for passkeys, which are considered the most secure way to log in to apps and services."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/24/companies-are-scrambling-to-stop-employees-from-maxing-out-ai-budgets-with-small-tasks/",
    "domain": "大厂 AI 动态",
    "title": "Companies are scrambling to stop employees from maxing out AI budgets with small tasks",
    "url": "https://techcrunch.com/2026/06/24/companies-are-scrambling-to-stop-employees-from-maxing-out-ai-budgets-with-small-tasks/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T20:09:45+00:00",
    "summary": "The tokenmaxxing era was brief. We now appear to be entering the era of token rationing."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/24/heres-why-slate-changed-the-battery-in-its-cheap-ev-truck/",
    "domain": "大厂 AI 动态",
    "title": "Here’s why Slate changed the battery in its cheap EV truck",
    "url": "https://techcrunch.com/2026/06/24/heres-why-slate-changed-the-battery-in-its-cheap-ev-truck/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T19:27:56+00:00",
    "summary": "While there was probably a moment when Slate’s leadership had to green-light the switch from one battery type to another, the momentum toward that decision had been building for years."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/24/facebook-rolls-out-an-ai-companion-app-for-creators/",
    "domain": "大厂 AI 动态",
    "title": "Facebook rolls out an AI companion app for creators",
    "url": "https://techcrunch.com/2026/06/24/facebook-rolls-out-an-ai-companion-app-for-creators/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T17:16:24+00:00",
    "summary": "The new app, which is currently being tested with select creators, will have Facebook's recently launched AI creator assistant built into it."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/24/deezer-says-its-new-feature-lets-fans-remix-songs-with-artist-consent/",
    "domain": "大厂 AI 动态",
    "title": "Deezer says its new feature lets fans remix songs with artist consent",
    "url": "https://techcrunch.com/2026/06/24/deezer-says-its-new-feature-lets-fans-remix-songs-with-artist-consent/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T17:14:33+00:00",
    "summary": "Global music streaming service Deezer is taking a contrarian approach to AI, even as it adds a feature that lets fans remix songs."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/24/agility-robotics-plans-to-go-public-via-spac-in-a-2-5b-deal/",
    "domain": "大厂 AI 动态",
    "title": "Agility Robotics plans to go public via SPAC in a $2.5B deal",
    "url": "https://techcrunch.com/2026/06/24/agility-robotics-plans-to-go-public-via-spac-in-a-2-5b-deal/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T16:48:43+00:00",
    "summary": "Agility Robotics, the humanoid robotics startup that spun out of Oregon State University in 2015, expects to generate $620 million in proceeds."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/24/ntsb-launches-probe-into-fatal-texas-tesla-crash/",
    "domain": "大厂 AI 动态",
    "title": "NTSB launches probe into fatal Texas Tesla crash",
    "url": "https://techcrunch.com/2026/06/24/ntsb-launches-probe-into-fatal-texas-tesla-crash/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T16:39:08+00:00",
    "summary": "The safety board, known for its thorough investigations, is probing the crash alongside the National Highway Traffic Safety Administration."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/24/figma-adds-code-layers-support-for-animations-more-ai-features-in-new-update/",
    "domain": "大厂 AI 动态",
    "title": "Figma adds code layers, support for animations, more AI features in new update",
    "url": "https://techcrunch.com/2026/06/24/figma-adds-code-layers-support-for-animations-more-ai-features-in-new-update/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T16:15:00+00:00",
    "summary": "Figma's update adds a new code layer, support for motion and shaders, and the ability to create custom plug-ins for various tasks using AI."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/24/zoox-upgrades-its-robotaxi-as-it-prepares-for-commercial-service/",
    "domain": "大厂 AI 动态",
    "title": "Zoox upgrades its robotaxi as it prepares for commercial service",
    "url": "https://techcrunch.com/2026/06/24/zoox-upgrades-its-robotaxi-as-it-prepares-for-commercial-service/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T15:01:49+00:00",
    "summary": "The new Zoox robotaxi has more cushioning, lighter colors, and a better microphone and speaker for communicating with Zoox Support."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/24/this-new-tracking-label-could-help-solve-cargo-theft/",
    "domain": "大厂 AI 动态",
    "title": "This new tracking label could help solve cargo theft",
    "url": "https://techcrunch.com/2026/06/24/this-new-tracking-label-could-help-solve-cargo-theft/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T15:00:00+00:00",
    "summary": "The Samsara Tracking Label hides a BLE system that can offer real-time location in a disposable package."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI unveils its first custom chip, built by Broadcom",
    "url": "https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T14:54:46+00:00",
    "summary": "Named Jalapeño, the new processor was designed specifically for the unique needs of OpenAI's inference systems."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/24/if-you-want-to-cut-your-screen-time-just-get-a-brick/",
    "domain": "大厂 AI 动态",
    "title": "If you want to cut your screen time, just get a Brick",
    "url": "https://techcrunch.com/2026/06/24/if-you-want-to-cut-your-screen-time-just-get-a-brick/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T14:01:35+00:00",
    "summary": "After years of struggling to curb my screen time, apparently all I needed was a $59 hunk of plastic."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/24/3-days-left-to-save-up-to-190-on-techcrunch-founder-summit-2026/",
    "domain": "大厂 AI 动态",
    "title": "3 days left to save up to $190 on your TechCrunch Founder Summit 2026 pass",
    "url": "https://techcrunch.com/2026/06/24/3-days-left-to-save-up-to-190-on-techcrunch-founder-summit-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T14:00:00+00:00",
    "summary": "You have just 3 days left to save up to $190 on your pass to TechCrunch Founder Summit 2026 before Early Bird rates end on June 26 at 11:59 p.m. PT. Register today."
  },
  {
    "id": "rss:https://stratechery.com/2026/my-vibe-coding-adventure-the-app-and-the-experience-ten-takeaways/",
    "domain": "大厂 AI 动态",
    "title": "My Vibe Coding Adventure, The App and the Experience, Ten Takeaways",
    "url": "https://stratechery.com/2026/my-vibe-coding-adventure-the-app-and-the-experience-ten-takeaways/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T10:00:00+00:00",
    "summary": "My experience and reflections on vibe coding an app that I plan on actually using regularly."
  },
  {
    "id": "rss:https://stratechery.com/2026/memory-chips-and-china-microsoft-and-chinese-models/",
    "domain": "大厂 AI 动态",
    "title": "Memory Chips and China, Microsoft and Chinese Models",
    "url": "https://stratechery.com/2026/memory-chips-and-china-microsoft-and-chinese-models/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T10:00:00+00:00",
    "summary": "The big three memory makers may come to regret opening up the door to Chinese memory makers; Microsoft, meanwhile, is very incentivized to use Chinese models."
  },
  {
    "id": "rss:https://arstechnica.com/gaming/2026/06/grand-theft-auto-vi-will-cost-80-without-a-physical-disc/",
    "domain": "大厂 AI 动态",
    "title": "Hotly anticipated Grand Theft Auto VI will cost more than other AAA games",
    "url": "https://arstechnica.com/gaming/2026/06/grand-theft-auto-vi-will-cost-80-without-a-physical-disc/",
    "source": "Samuel Axon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T22:47:03+00:00",
    "summary": "GTA6 might be an outlier, though—at least for now."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/06/openai-and-broadcom-announce-chip-designed-for-llm-inference-at-scale/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI and Broadcom announce chip designed for LLM inference at scale",
    "url": "https://arstechnica.com/gadgets/2026/06/openai-and-broadcom-announce-chip-designed-for-llm-inference-at-scale/",
    "source": "Samuel Axon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T22:28:18+00:00",
    "summary": "The silicon race is heating up amid the struggle to keep up with demand."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/06/analysis-finds-the-exploration-programs-nasa-recently-canceled-were-running-way-late/",
    "domain": "大厂 AI 动态",
    "title": "13 years and $500 million for a stage adapter? Report justifies NASA cancellations.",
    "url": "https://arstechnica.com/space/2026/06/analysis-finds-the-exploration-programs-nasa-recently-canceled-were-running-way-late/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T21:41:03+00:00",
    "summary": "\"Contract values for these efforts ballooned from nearly $2.8 billion to $5.9 billion.\""
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/06/us-ends-hantavirus-outbreak-response-with-no-answers-on-draconian-quarantines/",
    "domain": "大厂 AI 动态",
    "title": "US ends hantavirus outbreak response with no answers on draconian quarantines",
    "url": "https://arstechnica.com/health/2026/06/us-ends-hantavirus-outbreak-response-with-no-answers-on-draconian-quarantines/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T21:28:39+00:00",
    "summary": "We still don't know why RFK Jr. overruled CDC expert to order strict quarantines."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/06/one-two-punch-delivered-in-global-operation-disrupts-cybercrime-assembly-line/",
    "domain": "大厂 AI 动态",
    "title": "One-two punch delivered in global operation disrupts cybercrime \"assembly line\"",
    "url": "https://arstechnica.com/security/2026/06/one-two-punch-delivered-in-global-operation-disrupts-cybercrime-assembly-line/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T21:03:34+00:00",
    "summary": "\"Operation Endgame\" simultaneously disrupts two widely used crime tools."
  },
  {
    "id": "rss:https://arstechnica.com/features/2026/06/we-take-a-ride-in-slates-24950-electric-pickup/",
    "domain": "大厂 AI 动态",
    "title": "Underpromise, overdeliver? Hands-on with the $24,950 Slate auto.",
    "url": "https://arstechnica.com/features/2026/06/we-take-a-ride-in-slates-24950-electric-pickup/",
    "source": "Roberto Baldwin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T20:28:07+00:00",
    "summary": "It has 205 miles of bare-bones range."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/06/disney-agreed-to-50m-settlement-over-claims-it-made-live-tv-streaming-expensive/",
    "domain": "大厂 AI 动态",
    "title": "Disney agreed to $50M settlement over claims it made live-TV streaming expensive",
    "url": "https://arstechnica.com/tech-policy/2026/06/disney-agreed-to-50m-settlement-over-claims-it-made-live-tv-streaming-expensive/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T20:22:58+00:00",
    "summary": "Lawsuit alleged Disney inflated market prices by making carriers include ESPN."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/06/experimental-wine-bottle-tracks-oxygen-moving-through-the-cork/",
    "domain": "大厂 AI 动态",
    "title": "Experimental wine bottle tracks oxygen moving through the cork",
    "url": "https://arstechnica.com/science/2026/06/experimental-wine-bottle-tracks-oxygen-moving-through-the-cork/",
    "source": "John Timmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T20:04:32+00:00",
    "summary": "The small bit of air in the bottle sees oxygen and other chemicals move in and out."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/06/fcc-plans-id-mandate-that-could-block-anonymous-use-of-prepaid-burner-phones/",
    "domain": "大厂 AI 动态",
    "title": "FCC plans ID mandate that could block anonymous use of prepaid burner phones",
    "url": "https://arstechnica.com/tech-policy/2026/06/fcc-plans-id-mandate-that-could-block-anonymous-use-of-prepaid-burner-phones/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T19:45:37+00:00",
    "summary": "Privacy advocates and domestic violence groups say ID mandate is a big mistake."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/06/formula-e-reveals-first-calendar-for-gen4-with-lots-of-real-race-tracks/",
    "domain": "大厂 AI 动态",
    "title": "Formula E reveals first calendar for GEN4 with lots of real race tracks",
    "url": "https://arstechnica.com/cars/2026/06/formula-e-reveals-first-calendar-for-gen4-with-lots-of-real-race-tracks/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T17:35:45+00:00",
    "summary": "Brands Hatch, COTA, and Zandvoort will all hold an e-Prix in 2027."
  },
  {
    "id": "rss:https://arstechnica.com/google/2026/06/google-starts-lowering-play-store-fees-making-good-on-epic-games-settlement/",
    "domain": "大厂 AI 动态",
    "title": "Google starts lowering Play Store fees, making good on Epic Games settlement",
    "url": "https://arstechnica.com/google/2026/06/google-starts-lowering-play-store-fees-making-good-on-epic-games-settlement/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T17:00:17+00:00",
    "summary": "A few additional markets will get the lower fees this year ahead of a global rollout in 2027."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/06/elon-musk-denies-teslas-autopilot-caused-crash-that-killed-grandmother/",
    "domain": "大厂 AI 动态",
    "title": "Elon Musk denies Tesla’s Autopilot caused crash that killed grandmother",
    "url": "https://arstechnica.com/tech-policy/2026/06/elon-musk-denies-teslas-autopilot-caused-crash-that-killed-grandmother/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T16:40:32+00:00",
    "summary": "Tesla, accused of failing to fix design flaws, blames driver pressing accelerator."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/06/military-branches-restore-flu-shot-requirement-after-virus-swept-through-base/",
    "domain": "大厂 AI 动态",
    "title": "Military branches restore flu shot requirement after virus swept through base",
    "url": "https://arstechnica.com/health/2026/06/military-branches-restore-flu-shot-requirement-after-virus-swept-through-base/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T14:54:54+00:00",
    "summary": "Branches received exceptions to Hegseth's policy that made the shot optional."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/06/here-are-five-ways-you-could-build-a-slate-ev-from-25000-to-37000/",
    "domain": "大厂 AI 动态",
    "title": "Slate Auto's truck builder goes live for its $25k electric pickup",
    "url": "https://arstechnica.com/cars/2026/06/here-are-five-ways-you-could-build-a-slate-ev-from-25000-to-37000/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T14:27:16+00:00",
    "summary": "From a bare-bones pickup to a loaded, wrapped SUV, here's what some Slates will cost."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/06/november-launch-set-for-space-shuttle-endeavours-towering-display/",
    "domain": "大厂 AI 动态",
    "title": "We got a sneak peek of the final space shuttle set to go on public display",
    "url": "https://arstechnica.com/space/2026/06/november-launch-set-for-space-shuttle-endeavours-towering-display/",
    "source": "Robert Pearlman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T14:04:56+00:00",
    "summary": "\"It is an incredible exhibit and incredible sight.\""
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/06/white-house-app-auto-downloads-to-government-phones-cant-be-uninstalled/",
    "domain": "大厂 AI 动态",
    "title": "White House app auto-downloads to government phones, can't be uninstalled",
    "url": "https://arstechnica.com/tech-policy/2026/06/white-house-app-auto-downloads-to-government-phones-cant-be-uninstalled/",
    "source": "Vittoria Elliott, wired.com",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T13:35:19+00:00",
    "summary": "“It’s shooting pure unadulterated propaganda into our veins,” says one worker."
  },
  {
    "id": "rss:https://arstechnica.com/information-technology/2026/06/executive-order-bumps-up-deadline-to-move-off-quantum-vulnerable-crypto/",
    "domain": "大厂 AI 动态",
    "title": "White House drastically shortens deadline for dropping quantum-vulnerable crypto",
    "url": "https://arstechnica.com/information-technology/2026/06/executive-order-bumps-up-deadline-to-move-off-quantum-vulnerable-crypto/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T22:30:57+00:00",
    "summary": "Order warns of national security risks if post-quantum cryptography isn't adopted in time."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/06/uss-climate-gov-site-taken-down-by-trump-relaunched-by-nonprofit/",
    "domain": "大厂 AI 动态",
    "title": "US's climate.gov site, taken down by Trump, relaunched by nonprofit",
    "url": "https://arstechnica.com/science/2026/06/uss-climate-gov-site-taken-down-by-trump-relaunched-by-nonprofit/",
    "source": "John Timmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T22:07:56+00:00",
    "summary": "Climate.us has now restored everything taken down by the government."
  },
  {
    "id": "wscn:3775493",
    "domain": "股票",
    "title": "黄金预测：黄金/美元跌至2026年最低位",
    "url": "https://wallstreetcn.com/articles/3775493",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T06:48:35+00:00",
    "summary": "随着本交易周继续推进，金融市场最引人关注的动态之一便是黄金的持续走弱。黄金已连续两个交易日呈现大幅下..."
  },
  {
    "id": "wscn:3775498",
    "domain": "股票",
    "title": "最高看15000点！摩根大通疯狂唱多韩国股市，两个月三次上调Kospi目标",
    "url": "https://wallstreetcn.com/articles/3775498",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T06:47:26+00:00",
    "summary": "受AI需求与存储芯片超级周期驱动，摩根大通时隔一月再度上调韩国Kospi指数目标价：基准12500点，牛市看至15000点。尽管面临外资抛售压力，但AI芯片强劲盈利及韩国散户买盘提供了坚实支撑。除摩根大通外，高盛近期将Kospi目标价上调至12000点，摩根士丹利也将其目标价上调至10500点。"
  },
  {
    "id": "wscn:3775470",
    "domain": "股票",
    "title": "美光财报炸裂，韩股收涨5.8%，海力士飙升10%创新高，黄金跌破4000，白银再跌1%",
    "url": "https://wallstreetcn.com/articles/3775470",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T06:46:32+00:00",
    "summary": "韩国首尔综指收涨5.8%，海力士飙升10%创新高。日经225指数收涨4.6%。WTI原油跌约1.6%至每桶69.19美元。此外，美元走强令黄金承压，现货金价跌至约3983美元/盎司，再次跌破4000美元关口。现货白银下挫超1%，报56.78美元。"
  },
  {
    "id": "wscn:3775490",
    "domain": "股票",
    "title": "美伊协议后，霍尔木兹海峡战争险保费腰斩，从5%降至2%",
    "url": "https://wallstreetcn.com/articles/3775490",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T06:42:49+00:00",
    "summary": "这使得单艘船舶节省保险成本数十万美元。自6月18日起已有172艘船只过境，航运信心明显回升，越来越多船只重开AIS应答器。但覆盖石油、粮食等大宗商品的货物险保费基本持平，市场对地缘局势判断仍存分歧。"
  },
  {
    "id": "wscn:3775495",
    "domain": "股票",
    "title": "泰国预计今年出口创历史新高，AI带动电子产品需求激增",
    "url": "https://wallstreetcn.com/articles/3775495",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T06:32:47+00:00",
    "summary": "AI基础设施投资浪潮正在重塑泰国出口版图。泰国官员预计，2025年出口总值将达3668亿美元，同比增长8%，创历史新高——电子产品占出口总量近三分之一，成为核心引擎。AI热潮带动泰国科技股飙升，基准股指跃升为东南亚今年表现最佳主要指数。"
  },
  {
    "id": "wscn:3775491",
    "domain": "股票",
    "title": "“电子大米”变“电子黄金”？MLCC价格狂飙：高端产品年内涨价3至5倍，现货报价30分钟一变",
    "url": "https://wallstreetcn.com/articles/3775491",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T06:21:07+00:00",
    "summary": "AI服务器需求爆发引发MLCC价格暴涨，高容值产品年内现货价狂飙3至5倍，华强北报价频率缩至每30分钟更新。由于高端产能扩张需18至24个月，村田等巨头实际发货量仅能满足一两成，高端规格国内交期已大幅拉长至逾20周。"
  },
  {
    "id": "wscn:3774904",
    "domain": "股票",
    "title": "硅电容：MLCC潜在颠覆者？AI先进封装时代的百亿冠军赛道",
    "url": "https://wallstreetcn.com/premium/articles/3774904?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T06:01:34+00:00",
    "summary": "三星电机宣布签下1.5万亿韩元（约合人民币68亿元）硅电容供应大单，标志着这一长期隐身于MLCC阴影下的细分赛道正式进入资本市场的聚光灯。"
  },
  {
    "id": "wscn:3775489",
    "domain": "股票",
    "title": "沃什重创\"美元贬值交易\"！黄金崩了，比特币重挫，芯片狂欢还能撑多久？",
    "url": "https://wallstreetcn.com/articles/3775489",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T05:44:07+00:00",
    "summary": "美联储沃什强鹰首秀击溃“贬值交易”！强美元风暴下，金银与比特币惨遭血洗失守关键价位。与此同时，巨量出逃资金正疯狂涌入半导体板块，但这趟极端波动的芯片狂欢已频现“历史大顶”信号，警惕最后的疯狂。"
  },
  {
    "id": "wscn:3775467",
    "domain": "股票",
    "title": "科创50首破2000点，GPU、存储器领涨，有色金属大跌，恒指跌破23000点，科网股下挫",
    "url": "https://wallstreetcn.com/articles/3775467",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T05:42:29+00:00",
    "summary": "盘面上，个股跌多涨少，沪深京三市超4300股飘绿，上午半天成交2.44万亿。沪深两市半日成交额2.42万亿，较上个交易日放量3370亿。板块方面，券商股午前拉升，金融科技题材同步大涨；半导体产业链持续发酵，GPU、存储器方向领涨。黄金、油气、锂矿、AI应用、工业金属、商业航天板块走弱。"
  },
  {
    "id": "wscn:3775486",
    "domain": "股票",
    "title": "华尔街最担心的问题，美光给出了答案",
    "url": "https://wallstreetcn.com/articles/3775486",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T04:48:37+00:00",
    "summary": "美光用一份财报击碎了“AI需求见顶”的担忧。数据中心收入超预期近七成，HBM产能提前售罄，第四财季指引继续大幅上修，更签下覆盖数千亿美元收入的长期协议。当市场还在担心AI基建降温时，美光传递出的信号却是：存储短缺可能延续到2027年以后，而这轮AI周期远未结束。"
  },
  {
    "id": "wscn:3775468",
    "domain": "股票",
    "title": "瑞银发现：60%已开始控制AI支出，企业转向低成本模型与开源中国模型",
    "url": "https://wallstreetcn.com/articles/3775468",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T04:25:40+00:00",
    "summary": "瑞银调研显示，约60%企业已为Token使用加设护栏，有公司单用户单月花费3.5万美元，有团队Token用量超配额200%。企业的应对策略是\"模型路由\"，简单任务转向低价甚至中国开源模型。高端模型收入增速承压，软件公司站在\"被砍预算\"与\"成为省钱工具\"的岔路口，AI增长逻辑未变，斜率之争才刚开始。"
  },
  {
    "id": "wscn:3775479",
    "domain": "股票",
    "title": "付鹏：突破十年区间，纽元NZD的拐点要来了？【付鹏说28】",
    "url": "https://wallstreetcn.com/premium/articles/3775479?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T04:11:44+00:00",
    "summary": "澳大利亚、新西兰的经济、利差、人口和资本流向正在持续拉开差距，澳纽汇率有望继续上行至历史区间上沿，而新西兰元仍面临较大的贬值压力。"
  },
  {
    "id": "wscn:3775484",
    "domain": "股票",
    "title": "携程2026Q1净收入162亿  Q2预期大幅放缓",
    "url": "https://wallstreetcn.com/articles/3775484",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T04:08:30+00:00",
    "summary": "预计Q2同比增长为3%-8%区间。"
  },
  {
    "id": "wscn:3775478",
    "domain": "股票",
    "title": "美银警告：半导体驱动下，纳斯达克已达\"泡沫临界点\"",
    "url": "https://wallstreetcn.com/articles/3775478",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T03:59:13+00:00",
    "summary": "美国银行衍生品团队发出警告，纳斯达克100自3月底累计涨幅约32%，估值压力持续积聚，纳斯达克泡沫风险指标（BRI）已升至0.8关键阈值。美银指出，市场在宏观逆风下的超强韧性，恰是泡沫积聚的典型特征。"
  },
  {
    "id": "wscn:3775481",
    "domain": "股票",
    "title": "Q3存储涨幅超预期，HBM盈利能力明年追上通用DRAM，野村接连上调海力士和三星目标价",
    "url": "https://wallstreetcn.com/articles/3775481",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T03:50:38+00:00",
    "summary": "将三星目标价从59万韩元上调至67万韩元后，野村再将SK海力士目标价从400万韩元上调至470万韩元。核心驱动是三季度DRAM涨价预期从此前约5%大幅跳升至24%，远超市场预期；此外，HBM因利润率仍比通用DRAM低约30个百分点，要追平盈利能力HBM需要涨价超100%，而2027年有望实现。"
  },
  {
    "id": "wscn:3775164",
    "domain": "股票",
    "title": "功率半导体行业：AI算力与新能源双轮驱动，供给紧俏开启景气上行周期",
    "url": "https://wallstreetcn.com/premium/articles/3775164?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T03:50:09+00:00",
    "summary": "AI算力+新能源+供给收缩，功率半导体迎来新一轮上行周期。"
  },
  {
    "id": "wscn:3775482",
    "domain": "股票",
    "title": "华为汪涛预判2030：全球智能体千亿规模重写通信格局",
    "url": "https://wallstreetcn.com/articles/3775482",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T03:42:11+00:00",
    "summary": "通讯行业迎来全新智能时代"
  },
  {
    "id": "wscn:3775139",
    "domain": "股票",
    "title": "高端PI膜：黄金薄膜的\"供需悬崖\"，从1.2万吨缺口演化220亿国产替代蓝海",
    "url": "https://wallstreetcn.com/premium/articles/3775139?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T03:36:00+00:00",
    "summary": "产业链反馈显示，宇部兴产（UBE）电子级PI膜80%产能已被下游以溢价锁定，海外大厂产能被英伟达等AI算力巨头锁至2027年。这揭示了高端PI膜很可能正经历结构性供需失衡的临界点。"
  },
  {
    "id": "wscn:3775456",
    "domain": "股票",
    "title": "“亚洲版SpaceX”--高盛解读“亚洲太空经济全景”",
    "url": "https://wallstreetcn.com/articles/3775456",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T03:27:53+00:00",
    "summary": "当SpaceX点燃太空经济热情，全球资金扎堆涌向美国上市标的，一个定价错位正在形成——基本面在亚洲，钱先去了美国。高盛53只股票的亚洲太空篮子揭示：从射频芯片、相控阵天线到空间级材料，亚洲供应链撑起全球卫星部署的硬件底座，估值却较全球同行折价60%。未来五年7万颗卫星待发射，这不是科幻押注，而是已进入交付期的制造业扩产周期。"
  },
  {
    "id": "wscn:3775477",
    "domain": "股票",
    "title": "英特尔背书，AI芯片新秀SambaNova估值或达百亿，四个月内暴涨五倍",
    "url": "https://wallstreetcn.com/articles/3775477",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T03:26:42+00:00",
    "summary": "推动本轮估值跃升的关键催化剂之一，是SambaNova与英特尔及Vista Equity Partners的一系列合作落地。英特尔持有SambaNova约9%的股权，同时也是其客户。Vista Equity Partners与其合作打造云服务商，带来35亿美元收入承诺。公司核心优势在于RDU芯片能耗仅为英伟达GPU的十分之一，定位从\"替代者\"转向\"协同者\"。"
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
    "id": "rss:https://www.netinterest.co/p/defying-the-surveys",
    "domain": "股票",
    "title": "Defying the Surveys",
    "url": "https://www.netinterest.co/p/defying-the-surveys",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-04-17T16:54:51+00:00",
    "summary": "Banks report a resilient quarter &#8211; and a lurking threat"
  },
  {
    "id": "rss:https://www.netinterest.co/p/shuffling-risk",
    "domain": "股票",
    "title": "Shuffling Risk",
    "url": "https://www.netinterest.co/p/shuffling-risk",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-04-10T15:10:44+00:00",
    "summary": "An Asset Class Reborn"
  },
  {
    "id": "rss:https://www.netinterest.co/p/new-pod-the-race-to-secure-a-bank",
    "domain": "股票",
    "title": "NEW POD! The Race to Secure a Bank Charter with Adam Shapiro of Klaros Group",
    "url": "https://www.netinterest.co/p/new-pod-the-race-to-secure-a-bank",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-03-31T15:45:44+00:00",
    "summary": "Net Interest Extra ep 21"
  },
  {
    "id": "rss:https://www.netinterest.co/p/revolut-unbound",
    "domain": "股票",
    "title": "Revolut Unbound",
    "url": "https://www.netinterest.co/p/revolut-unbound",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-03-27T16:20:38+00:00",
    "summary": "The Quest to Build the World&#8217;s First Truly Global Bank"
  },
  {
    "id": "rss:https://www.netinterest.co/p/the-underwriters-of-hormuz",
    "domain": "股票",
    "title": "The Underwriters of Hormuz",
    "url": "https://www.netinterest.co/p/the-underwriters-of-hormuz",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-03-20T16:23:35+00:00",
    "summary": "A post on marine insurance &#8211; by popular demand"
  },
  {
    "id": "rss:https://www.netinterest.co/p/new-pod-market-intelligence-in-the",
    "domain": "股票",
    "title": "🎙️ Market Intelligence in the Age of AI: An Interview with Morningstar CEO, Kunal Kapoor",
    "url": "https://www.netinterest.co/p/new-pod-market-intelligence-in-the",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-03-17T16:30:34+00:00",
    "summary": "Net Interest Extra ep 20"
  },
  {
    "id": "rss:https://www.netinterest.co/p/redemption-day",
    "domain": "股票",
    "title": "Redemption Day",
    "url": "https://www.netinterest.co/p/redemption-day",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-03-13T18:09:28+00:00",
    "summary": "When the exit is smaller than the entrance"
  },
  {
    "id": "rss:https://www.netinterest.co/p/learning-from-lloyd",
    "domain": "股票",
    "title": "Learning from Lloyd",
    "url": "https://www.netinterest.co/p/learning-from-lloyd",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-03-06T17:42:54+00:00",
    "summary": "Blankfein, Goldman and the Next Market Reckoning"
  },
  {
    "id": "rss:https://www.netinterest.co/p/new-pod-how-credit-markets-shaped",
    "domain": "股票",
    "title": "🎙️ How Credit Markets Shaped a Nation: An Interview with Sarah Quinn",
    "url": "https://www.netinterest.co/p/new-pod-how-credit-markets-shaped",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-03-03T16:45:21+00:00",
    "summary": "Net Interest Extra ep 19"
  },
  {
    "id": "rss:https://www.netinterest.co/p/two-tribes",
    "domain": "股票",
    "title": "Two Tribes",
    "url": "https://www.netinterest.co/p/two-tribes",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-02-27T17:42:58+00:00",
    "summary": "Private Credit, Public Markets and the AI Reckoning"
  },
  {
    "id": "rss:https://www.netinterest.co/p/ai-and-i",
    "domain": "股票",
    "title": "AI and I",
    "url": "https://www.netinterest.co/p/ai-and-i",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-02-20T17:21:53+00:00",
    "summary": "Claude Code, Bloomberg and the Battle for Data"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.25283",
    "domain": "金融",
    "title": "Competitive satellite placement and the geography of orbital risk: evidence from the geostationary arc",
    "url": "https://arxiv.org/abs/2606.25283",
    "source": "Akhil Rao, Nikodem Szumilo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T04:00:00+00:00",
    "summary": "arXiv:2606.25283v1 Announce Type: new Abstract: Some orbital locations are crowded while others remain unoccupied. We explain why using the geostationary orbit as a near-ideal laboratory: a mature, on"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.25466",
    "domain": "金融",
    "title": "Time-dependent weighted directed networks of cryptocurrency interaction from high-frequency returns",
    "url": "https://arxiv.org/abs/2606.25466",
    "source": "Shubhangam Shukla, Mahesh Peyyala, Abhijit Chakraborty",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T04:00:00+00:00",
    "summary": "arXiv:2606.25466v1 Announce Type: new Abstract: We investigate the evolving structure of interactions in cryptocurrency markets using a network-based framework constructed from high-frequency price da"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.25811",
    "domain": "金融",
    "title": "Hierarchical Graph Learning for Calendar Spread Strategies in Commodity Futures Markets",
    "url": "https://arxiv.org/abs/2606.25811",
    "source": "Yoonsik Hong, Diego Klabjan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T04:00:00+00:00",
    "summary": "arXiv:2606.25811v1 Announce Type: new Abstract: Commodity futures can be represented hierarchically, with underlying assets at the upper level and individual futures contracts at the lower level. Enti"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.25909",
    "domain": "金融",
    "title": "General Equilibrium Effects of Carbon Offsets",
    "url": "https://arxiv.org/abs/2606.25909",
    "source": "Isla Globus-Harris, Daniel H Karney",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T04:00:00+00:00",
    "summary": "arXiv:2606.25909v1 Announce Type: new Abstract: We construct an analytical general equilibrium model of an economy with carbon offsets, and show that increasing the carbon offset price has an ambiguou"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.26024",
    "domain": "金融",
    "title": "Matrix Approximation of Bachelier Option Prices and Greeks under Stochastic Volatility models",
    "url": "https://arxiv.org/abs/2606.26024",
    "source": "Elisa Al\\`os, \\`Oscar Bur\\'es",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T04:00:00+00:00",
    "summary": "arXiv:2606.26024v1 Announce Type: new Abstract: In this paper, we present a numerical method for option pricing and the computation of Greeks under stochastic volatility Bachelier-type models, based o"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.26031",
    "domain": "金融",
    "title": "Geometrically convex return risk measures on AM-algebras",
    "url": "https://arxiv.org/abs/2606.26031",
    "source": "Christian Laudag\\'e",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T04:00:00+00:00",
    "summary": "arXiv:2606.26031v1 Announce Type: new Abstract: Monetary risk measures quantify the risk of uncertain monetary payoffs (or losses), whereas in time series analysis risk is typically assessed using log"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.25007",
    "domain": "金融",
    "title": "Multi-Stream Temporal Fusion for Financial Fraud Detection",
    "url": "https://arxiv.org/abs/2606.25007",
    "source": "Mohammadamin Dashti Moghaddam, Nick Sciarrilli",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T04:00:00+00:00",
    "summary": "arXiv:2606.25007v1 Announce Type: cross Abstract: Financial fraud detection in digital banking requires reasoning over multiple heterogeneous event streams -- transactions, login sessions, risk signal"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.25461",
    "domain": "金融",
    "title": "Equilibrium singular dividend control under ambiguity aggregation of heterogeneous discount rates",
    "url": "https://arxiv.org/abs/2606.25461",
    "source": "Yue Cao, Guohui Guan, Zongxia Liang, Xiaodong Luo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T04:00:00+00:00",
    "summary": "arXiv:2606.25461v1 Announce Type: cross Abstract: This paper studies a singular dividend control problem for a firm with heterogeneous shareholders whose discount rates follow a given distribution. Th"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.25484",
    "domain": "金融",
    "title": "From Causal Discovery to Implementation: An Agentic AI Framework for E-Scooter Mobility Hub Planning Across 29 German Cities",
    "url": "https://arxiv.org/abs/2606.25484",
    "source": "Meng Jin, Melanie Handrich, Simone Martinenz, Nicholas Hoeser, Ziyue Li",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T04:00:00+00:00",
    "summary": "arXiv:2606.25484v1 Announce Type: cross Abstract: Existing approaches to e-scooter mobility hub planning lack city-type-specific causal evidence. Demand models are typically correlational, built on pr"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.25696",
    "domain": "金融",
    "title": "A Two-Stage Decision Support System for Sustainability-Aware Long Short Portfolio Optimization",
    "url": "https://arxiv.org/abs/2606.25696",
    "source": "Giacomo di Tollo, Massimiliano Kaucic, Filippo Piccotto",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T04:00:00+00:00",
    "summary": "arXiv:2606.25696v1 Announce Type: cross Abstract: This paper proposes a two-stage decision support system for long-short portfolio optimization under environmental, social, and governance (ESG) consid"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.25910",
    "domain": "金融",
    "title": "Restoring Incentive Compatibility in Two-Stage Energy Markets with Prosumers",
    "url": "https://arxiv.org/abs/2606.25910",
    "source": "Nikolas Koumpis, Koushik Kar, Leandros Tassiulas, Manolis Zampetakis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T04:00:00+00:00",
    "summary": "arXiv:2606.25910v1 Announce Type: cross Abstract: A central challenge in modern energy market design is the formulation of a strategy-proof imbalance settlement layer that secures both the economic ef"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.25986",
    "domain": "金融",
    "title": "The Inference-Compute Frontier and a Latency-Efficient Architecture for Limit Order Book Prediction",
    "url": "https://arxiv.org/abs/2606.25986",
    "source": "C. Evans Hedges",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T04:00:00+00:00",
    "summary": "arXiv:2606.25986v1 Announce Type: cross Abstract: We study whether a scaling-law-style inference-compute frontier appears in limit order book prediction. Using FI-2010 and a suite of models ranging fr"
  },
  {
    "id": "rss:https://arxiv.org/abs/2411.01103",
    "domain": "金融",
    "title": "Mega Influencers versus Niche Creators: An Empirical Study of Streamer Influence on Endorsed Product Usage",
    "url": "https://arxiv.org/abs/2411.01103",
    "source": "Wooyong Jo, Mike Lewis, Yanwen Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T04:00:00+00:00",
    "summary": "arXiv:2411.01103v2 Announce Type: replace Abstract: Social media has given rise to online consumption communities, or fandoms, which are complex networks of ancillary creators and consumers organized "
  },
  {
    "id": "rss:https://arxiv.org/abs/2411.05470",
    "domain": "金融",
    "title": "Model-free portfolio allocation in continuous-time",
    "url": "https://arxiv.org/abs/2411.05470",
    "source": "Henry Chiu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T04:00:00+00:00",
    "summary": "arXiv:2411.05470v4 Announce Type: replace Abstract: We present a non-probabilistic, path-by-path framework for studying path-dependent (i.e., where weight is a functional of time and historical time-s"
  },
  {
    "id": "rss:https://arxiv.org/abs/2501.03658",
    "domain": "金融",
    "title": "Market Making with Fads, Informed, and Uninformed Traders",
    "url": "https://arxiv.org/abs/2501.03658",
    "source": "Emilio Barucci, Adrien Mathieu, Leandro S\\'anchez-Betancourt",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T04:00:00+00:00",
    "summary": "arXiv:2501.03658v3 Announce Type: replace Abstract: We characterise the solution to a continuous-time optimal liquidity provision problem in a market populated by informed and uninformed traders. In o"
  },
  {
    "id": "rss:https://arxiv.org/abs/2510.25487",
    "domain": "金融",
    "title": "Monetary Regimes and Trade before the Classical Gold Standard: Evidence from the Latin Monetary Union",
    "url": "https://arxiv.org/abs/2510.25487",
    "source": "Jacopo Timini",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T04:00:00+00:00",
    "summary": "arXiv:2510.25487v3 Announce Type: replace Abstract: This paper reexamines the trade effects of the Latin Monetary Union (LMU), a 19th century agreement to standardize gold and silver coinage among sev"
  },
  {
    "id": "rss:https://arxiv.org/abs/2603.20674",
    "domain": "金融",
    "title": "Carbon Farming: An Expository, Inter-Disciplinary Survey",
    "url": "https://arxiv.org/abs/2603.20674",
    "source": "V. Priyanka, Geetha Charan, Rohit P. Suresh, Thandava Sunkara, Manojkumar Patil, Kartik Sagar, Aashman Trivedi, K. Soumya, Subir Paul, Parashuram Hadimani, Ganesh Babu, Ravi Trivedi, Yadati Narahari",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T04:00:00+00:00",
    "summary": "arXiv:2603.20674v3 Announce Type: replace Abstract: Carbon farming is the collection of agricultural best practices specifically designed to maximize the capture and long-term storage of atmospheric c"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.17397",
    "domain": "金融",
    "title": "Designing Recommendation Exposure and Favorite Lists: A Field Experiment in a Spot-Work Platform",
    "url": "https://arxiv.org/abs/2606.17397",
    "source": "Kazuki Sekiya, Suguru Otani, Yuki Komatsu, Yuki Fujii, Shunsuke Ozeki, Shunya Noda",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T04:00:00+00:00",
    "summary": "arXiv:2606.17397v3 Announce Type: replace Abstract: How should recommender systems be designed when recommendations shape access to scarce, short-lived opportunities? We study this question in a produ"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.23596",
    "domain": "金融",
    "title": "Anatomy of the Market: A Body-Tail Test of Factor Models",
    "url": "https://arxiv.org/abs/2606.23596",
    "source": "Useong Shin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T04:00:00+00:00",
    "summary": "arXiv:2606.23596v2 Announce Type: replace Abstract: In an ideal stochastic discount factor, zero pricing errors and the maximum Sharpe ratio coincide; in a low-dimensional approximation they need not."
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.29129",
    "domain": "金融",
    "title": "Governing Technical Debt in Agentic AI Systems",
    "url": "https://arxiv.org/abs/2605.29129",
    "source": "Muhammad Zia Hydari, Raja Iqbal, Narayan Ramasubbu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T04:00:00+00:00",
    "summary": "arXiv:2605.29129v2 Announce Type: replace-cross Abstract: Agentic AI systems are increasingly being explored as production infrastructure: they reason over multiple steps, call tools, act through work"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.08998",
    "domain": "金融",
    "title": "The Token Not Taken: Sampling, State, and the Stochasticity of AI Agents",
    "url": "https://arxiv.org/abs/2606.08998",
    "source": "Muhammad Zia Hydari, Raja Iqbal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T04:00:00+00:00",
    "summary": "arXiv:2606.08998v2 Announce Type: replace-cross Abstract: Agentic AI systems can behave differently across runs: the same request may produce a different plan, a different tool call, a different code "
  }
]
```
