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

- 今日日期：`2026-06-30`
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
  "date": "2026-06-30",
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
    "points": 3483396,
    "published_at": "2026-01-15T03:56:12+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n1. 构建智能体设计模式：反射、工具使用、规划与多智能体工作流；\n2. 将人工智能与外部工具集成：数据库、API、网络搜索与代码执行；\n3. 评估并优化人工智能系统：性能指标、错误分析与生产部署"
  },
  {
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "9分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 1370192,
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
    "points": 1293935,
    "published_at": "2026-05-05T14:08:25+00:00",
    "summary": "Claude Code保姆级教学【收藏起来不会错！】\n从上手安装，到高级用法，这期一次讲全～\n花了三周做教程，希望能帮到你嘻嘻，感谢朋友们的三连+关注啦～"
  },
  {
    "id": "bvid:BV1w9MczyETB",
    "domain": "AI",
    "title": "【Vibe Coding】0基础项目实战教学丨Claude Code，Codex，Cursor教程",
    "url": "http://www.bilibili.com/video/av114669670898752",
    "source": "蛋黄酱拌巧克力",
    "platform": "bilibili",
    "points": 1032594,
    "published_at": "2025-06-12T12:28:18+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV11NNAz5EKn",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！",
    "url": "http://www.bilibili.com/video/av116187623069851",
    "source": "AI-智能体搭建教程",
    "platform": "bilibili",
    "points": 805571,
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
    "points": 646922,
    "published_at": "2026-06-09T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“VibeCoding”免费获取\n【课程简介】从零开始，用自然语言指挥AI开发真实软件项目！"
  },
  {
    "id": "bvid:BV1Yi5M6DERk",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116560144369496",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 484896,
    "published_at": "2026-05-12T06:24:19+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 469550,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1AnQNYxEsy",
    "domain": "AI",
    "title": "MCP是啥？技术原理是什么？一个视频搞懂MCP的一切。Windows系统配置MCP，Cursor Cline使用MCP",
    "url": "http://www.bilibili.com/video/av114155298228756",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 415802,
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
    "points": 377666,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1VCVS6PEAd",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent零基础全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116668525186915",
    "source": "大模型入门教程",
    "platform": "bilibili",
    "points": 273353,
    "published_at": "2026-05-31T09:46:57+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1qGc7zwEX6",
    "domain": "AI",
    "title": "史上最强 AI 编程工具Cursor来啦！Cursor保姆级使用教程！新手友好！看到就是赚到！！！",
    "url": "http://www.bilibili.com/video/av116061928226926",
    "source": "知名的阿呆同学",
    "platform": "bilibili",
    "points": 246375,
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
    "points": 175812,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 159900,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 158363,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV1RNTtzMENj",
    "domain": "AI",
    "title": "从零编写MCP并发布上线，超简单！手把手教程",
    "url": "http://www.bilibili.com/video/av114630814862349",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 145481,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1ExV36wEsE",
    "domain": "AI",
    "title": "VS Code 安装 Claude Code 并接入 DeepSeek！Claude Code for VS Code！VSCode使用ClaudeCode插件",
    "url": "http://www.bilibili.com/video/av116662871268177",
    "source": "FutureAI实验室",
    "platform": "bilibili",
    "points": 108863,
    "published_at": "2026-05-30T09:44:52+00:00",
    "summary": "本节视频编号71，评论区自助领取配套文档，记得一键三连哦！"
  },
  {
    "id": "bvid:BV1g49KBqE1g",
    "domain": "AI",
    "title": "【Java+大模型】Java AI Agent✚Spring AI✚Spring AI Alibaba Agent Framework整体结构✚Skill！",
    "url": "http://www.bilibili.com/video/av116339758860081",
    "source": "图灵官方",
    "platform": "bilibili",
    "points": 99732,
    "published_at": "2026-04-03T08:15:24+00:00",
    "summary": "整理制作不易，大家记得点个关注，一键三连呀【点赞、收藏、转发】感谢支持~\n配套大模型笔记/AI大模型学习大纲/面试真题自取：https://www.bilibili.com/read/cv39638062/?spm_id_from=333.1387.0.0&amp;jump_opus=1"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 97454,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1A24y1J7Dt",
    "domain": "AI",
    "title": "如何在VS Code中使用Cursor自动生成代码",
    "url": "http://www.bilibili.com/video/av781409810",
    "source": "许你再少年",
    "platform": "bilibili",
    "points": 73443,
    "published_at": "2023-03-23T11:32:23+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1ZjDYB7Eam",
    "domain": "AI",
    "title": "从 0 到 1：6小时掌握 Vibe Coding！ Claude Code ＋ AI 这支影片直接让你超越 90% AI 玩家",
    "url": "http://www.bilibili.com/video/av116362122894759",
    "source": "李哈利Harry",
    "platform": "bilibili",
    "points": 61412,
    "published_at": "2026-04-08T11:00:00+00:00",
    "summary": "🌟 加入AI大师社群并运用AI创业赚钱：https://www.skool.com/aiagent/about?ref=f2b566934c5c4639aaa47ab1fe39310e\n📌 加入我的免费 Skool 社群，获取模板：https://www.skool.com/aiagent8/about?ref=f2b566934c5c4639aaa47ab1fe39310e\n\n🚧 开始使用 n8"
  },
  {
    "id": "bvid:BV1ZEJA6xEds",
    "domain": "AI",
    "title": "最新方法！国内免费无限制，使用Claude Code！",
    "url": "http://www.bilibili.com/video/av116746874848391",
    "source": "我是阿众",
    "platform": "bilibili",
    "points": 56241,
    "published_at": "2026-06-15T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 54556,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 52574,
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
    "points": 47266,
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
    "points": 40668,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 38386,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 29834,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV1bh3LzqEze",
    "domain": "AI",
    "title": "Chatbox AI终端：跨平台+MCP+知识库+开源+免费！一键连接所有AI语言模型！手把手安装使用指南！",
    "url": "http://www.bilibili.com/video/av114793218380950",
    "source": "_Smzh_",
    "platform": "bilibili",
    "points": 27559,
    "published_at": "2025-07-04T10:00:00+00:00",
    "summary": "chatbox官网：https://chatboxai.app\ngithub仓库：https://github.com/chatboxai/chatbox\n\nLM Studio教程：BV1usrLYTEZR\nTGW懒人包部署教程：BV1dVCzYUE7G\n本地语言模型个人推荐：BV1Bb421E7j7"
  },
  {
    "id": "bvid:BV1xzGH6uEG8",
    "domain": "AI",
    "title": "AI全自动化搭建复杂Simulink模型！5步即可完成部署，全流程分享！",
    "url": "http://www.bilibili.com/video/av116629870481178",
    "source": "电气攻城狮001",
    "platform": "bilibili",
    "points": 25983,
    "published_at": "2026-05-24T13:50:56+00:00",
    "summary": "本期分享五步实操流程，借助 Claude Code 交互载体接入 DeepSeek 大模型，搭配 2026.5.21 最新版 Simulink Agentic Toolkit，解锁 68 项建模技能。依次完成 API 额度配置、环境部署、工具包安装，连通校验后开启全自动模式。无需手动拖拽模块与布线，输入指令即可依托 Simscape 蓝库，在 MATLAB2026a 中自动搭建三相并网逆变器开环模"
  },
  {
    "id": "bvid:BV11K9gBqEnW",
    "domain": "AI",
    "title": "【杀戮尖塔2】AI MOD 配置教程第一期来辣！手把手教你怎么改提示词！以及如何设计自己的爬塔玩法",
    "url": "http://www.bilibili.com/video/av116341654755924",
    "source": "分歧点WhatIf",
    "platform": "bilibili",
    "points": 24537,
    "published_at": "2026-04-03T16:14:43+00:00",
    "summary": "每个参数都是干什么的，如何修改提示词的教程。\n不知道这是什么？请看合集内的视频~\n我做了一个 AI 的杀戮尖塔2MOD！\n可以和怪物对话，策反怪物，带着怪物爬塔（重写了几乎每一个怪物在友方时候的行为），还能给怪物打防御，带个沙虫全吃了！\n可以和上古之民对话，聊嗨了会给你 1～2 个额外赐福，还能帮你指示为未来\n可以让偷窃草蜢偷队友的 key 卡，想无限？偷了！\n可以和商人讨价还价，甚至白嫖\n多人的"
  },
  {
    "id": "bvid:BV1nf42127MW",
    "domain": "AI",
    "title": "用AI Agent做一个法律咨询助手，罗老看了都直呼内行 feat.通义千问大模型&amp;阿里云百炼平台",
    "url": "http://www.bilibili.com/video/av1204786228",
    "source": "御风大世界",
    "platform": "bilibili",
    "points": 21248,
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
    "points": 20523,
    "published_at": "2026-03-26T12:00:00+00:00",
    "summary": "之前，我一直在研究怎么远程使用 Claude Code 开发项目，并且能实时预览效果。但是一直都没有找到合适的解决方案，要么就是给一个临时公网链接预览，每次都需要再配置，要么就是购买云服务器来配置，都感觉挺麻烦的~\n\n最近，我发现这个蒲公英异地组网的方案，用来做远程开发 Claude Code 项目，感觉非常方便，不仅能修改代码，而且我实时预览的需求也很好的满足了。\n\n这样我随时随地都可以用 AI"
  },
  {
    "id": "bvid:BV1cCEi6sEU5",
    "domain": "AI",
    "title": "🦊他能成功吗？Claude Code 接管虚幻引擎5，打造一款游戏 | 带你走完整个流程",
    "url": "http://www.bilibili.com/video/av116731724959171",
    "source": "Apeak_虚幻丰哥",
    "platform": "bilibili",
    "points": 16670,
    "published_at": "2026-06-11T13:41:36+00:00",
    "summary": "Claude Code 接管虚幻引擎5，打造了一款游戏\n下载我的 CLAUDE.md（帮你省 token 的配置）\n链接：https://pan.quark.cn/s/b6e50b4b2535\n提取码：tbaE\nStefan 3D AI ：https://www.youtube.com/watch?v=iRcrZjOt5H8&amp;t=1s\n🔗 完整教程指南和链接：https://www.top"
  },
  {
    "id": "bvid:BV1ssEE6CEks",
    "domain": "AI",
    "title": "Ai自动画图：CAD建筑平面图测试（CodexGPT5.5）",
    "url": "http://www.bilibili.com/video/av116719259485897",
    "source": "Tutor南洋",
    "platform": "bilibili",
    "points": 16058,
    "published_at": "2026-06-09T08:47:15+00:00",
    "summary": "体验一下ai画图，不过CAD软件基本操作也不能拉下~\nCAD教学基础入门视频合集↓\n传送门：BV1aT4y1B7oY\n整个合集教学的，不要跳着看啊喂！\n看完了那基本就能跟上啦，提问请@我，不然评论太多我是看不到的"
  },
  {
    "id": "bvid:BV15i7K69EN7",
    "domain": "AI",
    "title": "【6.22最新发布】claude桌面版安装教程！一周快速入门claude code保姆级教程！",
    "url": "http://www.bilibili.com/video/av116793196676384",
    "source": "是蒜七丫",
    "platform": "bilibili",
    "points": 14718,
    "published_at": "2026-06-22T10:07:14+00:00",
    "summary": "求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连"
  },
  {
    "id": "bvid:BV1JU7E6PEar",
    "domain": "AI",
    "title": "Cursor 已死？我为什么要退订 Cursor ？",
    "url": "http://www.bilibili.com/video/av116819553683121",
    "source": "小狗瑞恩Ryan",
    "platform": "bilibili",
    "points": 11049,
    "published_at": "2026-06-27T01:52:00+00:00",
    "summary": "当了一年多的 Cursor 重度用户，最近把它退订了。\n\n不是它变差了，是 Claude Code 和 Codex 真的太好用了。\n\n几个真实感受： ① 大模型越来越强，我已经不怎么手写代码了 ② Cursor 套的是 VS Code 壳子，只属于程序员 ③ 底层模型不在一个量级——Claude 有 Opus 和 Fable 5，Codex 有 GPT 5.5/5.6，Cursor 的 Compo"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "穷在街头无人问lhj",
    "platform": "bilibili",
    "points": 10987,
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
    "points": 10817,
    "published_at": "2026-06-10T06:04:26+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1etEQ6DETs",
    "domain": "AI",
    "title": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！",
    "url": "http://www.bilibili.com/video/av116724192118321",
    "source": "AI产品经理大模型",
    "platform": "bilibili",
    "points": 10612,
    "published_at": "2026-06-10T05:41:54+00:00",
    "summary": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 9121,
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
    "points": 8364,
    "published_at": "2025-06-04T07:08:58+00:00",
    "summary": "全程干货无废话！MCP最新实战教程，从环境部署、原理详解到项目实战，带你彻底吃透MCP！MCPServer开发，mcp开发，mcp教程，mcp项目 完整视频教程+讲解课件+学习笔记+AI大模型知识库已打包可分享！"
  },
  {
    "id": "bvid:BV1C3jt64EPS",
    "domain": "AI",
    "title": "B站讲的最好的Vibe Coding企业级项目实战教程（2026最新版）从入门到进阶，七天速通Claude Code+Codex+CursorAI工程化编程开发",
    "url": "http://www.bilibili.com/video/av116787425383675",
    "source": "图灵学院诸葛",
    "platform": "bilibili",
    "points": 8092,
    "published_at": "2026-06-21T09:48:04+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n 【本视频笔记代码、大模型最新学习路线、系统学习课程、实战案例、电子书+问题解答等戳这里获取→https://www.bilibili.com/read/cv39576966/?jump_opus=1】"
  },
  {
    "id": "bvid:BV1wEzvBvE2f",
    "domain": "AI",
    "title": "Claude Code 实战配置集合，Everything Claude Code ，提升效率，规范ai编程！",
    "url": "http://www.bilibili.com/video/av115961348751544",
    "source": "三少科技",
    "platform": "bilibili",
    "points": 7401,
    "published_at": "2026-01-26T12:19:35+00:00",
    "summary": "我的知识星球，https://t.zsxq.com/jVAk9\n\n莱卡云： https://www.lcayun.com/aff/GEYCYCZE"
  },
  {
    "id": "bvid:BV12MEg6pE9o",
    "domain": "AI",
    "title": "【乐鑫教程】乐鑫文档 MCP 服务器上线，现已支持微信登录！",
    "url": "http://www.bilibili.com/video/av116713957956440",
    "source": "乐鑫信息科技",
    "platform": "bilibili",
    "points": 7044,
    "published_at": "2026-06-08T10:17:31+00:00",
    "summary": "手把手教你如何使用最新乐鑫文档知识库，帮你在 Claude / Cursor 等平台解答问题、生成代码、迁移 ESP-IDF 版本、烧录固件。 MCP 服务器现已支持微信扫码一键登录，快来一试！\n\n视频重点内容包括👇：\n\n- 如何将 MCP 服务器添加到 VS Code\n- 让 Copilot 基于乐鑫文档对比旧版和最新版 I2C 驱动\n- 驱动迁移\n- Copilot 编译代码、烧录代码并监控输"
  },
  {
    "id": "bvid:BV1Wkjy6gEFx",
    "domain": "AI",
    "title": "B站讲的最好的Vibe Coding企业级项目实战（2026最新版）Claude Code+Codex+Cursor，从环境安装到实战，全部都讲明白了！！",
    "url": "http://www.bilibili.com/video/av116798397616142",
    "source": "程序员码哥",
    "platform": "bilibili",
    "points": 7001,
    "published_at": "2026-06-23T08:12:47+00:00",
    "summary": "B站讲的最好的Vibe Coding企业级项目实战（2026最新版）Claude Code+Codex+Cursor，从环境安装到实战，全部都讲明白了！！\n【视频配套学习笔记、Agent开发、大模型最新学习路线、系统学习、实战案例、电子书+问题解答】都在这了：https://www.bilibili.com/read/cv39979382/"
  },
  {
    "id": "bvid:BV1QU6GYFEio",
    "domain": "AI",
    "title": "[课程4] 用Cursor开发数据库真的很简单 | Agent应用 | 用Codebase解决跨文件错误",
    "url": "http://www.bilibili.com/video/av113742109021318",
    "source": "Zhu的AI日记",
    "platform": "bilibili",
    "points": 6986,
    "published_at": "2024-12-31T12:30:00+00:00",
    "summary": "***这是全网最完整的分享如何在不懂编程的情况下，利用结构化思维，用Cursor开发商业app的系列课程。\n《懒人记单词》是基于艾宾浩斯遗忘曲线设计的记单词神器，它可以对每一个单词进行人性化的解读，并在每一个遗忘周期到来时及时提醒，并通过单词释义选择，拼写和造句进行全方位的巩固，同时AI还能对你的句子进行多维度的评估，确保你对每一个单词不仅会认，而且会用。\n\n***你将在本视频中学到：\n1.数据库"
  },
  {
    "id": "bvid:BV1fNs9eiEm9",
    "domain": "AI",
    "title": "Cursor AI编程结合cocos3.8游戏开发教程-01",
    "url": "http://www.bilibili.com/video/av113187471105975",
    "source": "太阳8800",
    "platform": "bilibili",
    "points": 6478,
    "published_at": "2024-09-23T15:15:13+00:00",
    "summary": "开源源码仓库\nhttps://gitee.com/gamepublic/chess-cards"
  },
  {
    "id": "bvid:BV1u4G9zmEte",
    "domain": "AI",
    "title": "什么是MCP？VS Code中使用MCP Server",
    "url": "http://www.bilibili.com/video/av114426032168712",
    "source": "AI落地派",
    "platform": "bilibili",
    "points": 6346,
    "published_at": "2025-04-30T08:51:30+00:00",
    "summary": "什么是MCP，怎么样使用MCP Server，不用写SQL语句就可以查询数据库。\n\nMCP Servers\nhttps://smithery.ai/\nhttps://github.com/punkpeye/awesome-mcp-servers\nhttps://github.com/modelcontextprotocol/servers\n\nMCP Server for MySQL based o"
  },
  {
    "id": "bvid:BV1Bo736yESV",
    "domain": "AI",
    "title": "【2026最新版】Codex &amp; Claude Code从零开始带你1天刷完Vibe Coding企业级电商项目实战，比付费强十倍！",
    "url": "http://www.bilibili.com/video/av116815460043570",
    "source": "程序员北边",
    "platform": "bilibili",
    "points": 5012,
    "published_at": "2026-06-26T08:34:40+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n本视频配套文档课件笔记代码及AI大模型学习路线图戳这里获取→https://www.bilibili.com/read/cv39693258/"
  },
  {
    "id": "rss:https://www.eetimes.com/model-context-protocol-emerges-as-a-common-framework-for-enterprise-ai-systems/",
    "domain": "AI 算力 / 半导体",
    "title": "Model Context Protocol Emerges as a Common Framework for Enterprise AI Systems",
    "url": "https://www.eetimes.com/model-context-protocol-emerges-as-a-common-framework-for-enterprise-ai-systems/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T07:00:00+00:00",
    "summary": "MCP gives enterprise AI a common, open plumbing layer to connect models with tools, data, and agents. The post Model Context Protocol Emerges as a Common Framework for Enterprise AI Systems appeared f"
  },
  {
    "id": "rss:https://www.eetimes.com/u-s-eyes-china-expanding-role-in-latin-america/",
    "domain": "AI 算力 / 半导体",
    "title": "U.S. Eyes China’s Expanding Role in Latin America",
    "url": "https://www.eetimes.com/u-s-eyes-china-expanding-role-in-latin-america/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T21:00:00+00:00",
    "summary": "As U.S. regulators focus on supply chain transparency, China's expanding presence in Latin America has emerged as a major strategic challenge. The post U.S. Eyes China&#8217;s Expanding Role in Latin "
  },
  {
    "id": "rss:https://www.eetimes.com/panel-with-arteris-gf-tenstorrent-risc-v-ecosystem-growth-for-physical-ai/",
    "domain": "AI 算力 / 半导体",
    "title": "Panel with Arteris, GlobalFoundries, Tenstorrent: RISC-V Ecosystem Growth for Physical AI",
    "url": "https://www.eetimes.com/panel-with-arteris-gf-tenstorrent-risc-v-ecosystem-growth-for-physical-ai/",
    "source": "EE Times Staff",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T16:53:48+00:00",
    "summary": "RISC-V heavyweights tackle physical AI, edge autonomy, and TOPS-per-watt—watch how robots chase their killer app. The post Panel with Arteris, GlobalFoundries, Tenstorrent: RISC-V Ecosystem Growth for"
  },
  {
    "id": "rss:https://www.eetimes.com/europes-path-to-defense-resilience-lies-in-technological-independence/",
    "domain": "AI 算力 / 半导体",
    "title": "Europe’s Path to Defense Resilience Lies in Technological Independence",
    "url": "https://www.eetimes.com/europes-path-to-defense-resilience-lies-in-technological-independence/",
    "source": "Florian Pivit",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T12:34:57+00:00",
    "summary": "If Europe wants true defense resilience, it must reduce its dependence on big foreign tech ecosystems. The post Europe’s Path to Defense Resilience Lies in Technological Independence appeared first on"
  },
  {
    "id": "rss:https://www.eetimes.com/satvu-targets-industrial-intelligence-with-thermal-imaging/",
    "domain": "AI 算力 / 半导体",
    "title": "SatVu Targets Industrial Intelligence with Thermal Imaging",
    "url": "https://www.eetimes.com/satvu-targets-industrial-intelligence-with-thermal-imaging/",
    "source": "Rebecca Pool",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T07:20:00+00:00",
    "summary": "With HotSat-2 in orbit and fresh funding, U.K. startup SatVu is demonstrating how high-resolution thermal satellite data can reveal real-world industrial activity. The post SatVu Targets Industrial In"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/amd-expo-ull-ram-drops-at-jaw-dropping-usd1-099-despite-promises-of-it-being-effectively-the-same-price-ddr5-6000-c26-32gb-kit-sports-80-percent-ull-tax",
    "domain": "AI 算力 / 半导体",
    "title": "AMD EXPO ULL RAM drops at jaw-dropping $1,099 despite promises of it being 'effectively the same price' — DDR5-6000 C26 32GB kit sports 80% ULL tax",
    "url": "https://www.tomshardware.com/pc-components/ram/amd-expo-ull-ram-drops-at-jaw-dropping-usd1-099-despite-promises-of-it-being-effectively-the-same-price-ddr5-6000-c26-32gb-kit-sports-80-percent-ull-tax",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T20:16:12+00:00",
    "summary": "Newegg has started selling G.Skill’s Trident Z5 NeoX memory kits featuring AMD ULL technology, and the prices are already high."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpu-drivers/cuda-emulator-for-amd-gpus-zluda-loses-funding-with-v6-release-embattled-project-goes-back-to-hobby-status-but-now-includes-32-bit-physx-support",
    "domain": "AI 算力 / 半导体",
    "title": "CUDA emulator for AMD GPUs Zluda loses funding with v6 release — embattled project goes back to hobby status but now includes 32-bit PhysX support",
    "url": "https://www.tomshardware.com/pc-components/gpu-drivers/cuda-emulator-for-amd-gpus-zluda-loses-funding-with-v6-release-embattled-project-goes-back-to-hobby-status-but-now-includes-32-bit-physx-support",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T18:29:21+00:00",
    "summary": "Zluda is back to a hobby, as the open-source project has lost commercial funding with version 6 but added early 32-bit PhysX support."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/valve-threatens-legal-action-against-dbrand-over-its-unsanctioned-portal-2-inspired-companion-cube-edgy-accessories-manufacturer-kills-product-after-asking-for-licensing-deal-admits-it-didnt-have-the-right-to-make-it",
    "domain": "AI 算力 / 半导体",
    "title": "Valve threatens legal action against Dbrand over its unsanctioned Portal 2-inspired Companion Cube — edgy accessories manufacturer kills product after asking for licensing deal, admits it didn't have ",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/valve-threatens-legal-action-against-dbrand-over-its-unsanctioned-portal-2-inspired-companion-cube-edgy-accessories-manufacturer-kills-product-after-asking-for-licensing-deal-admits-it-didnt-have-the-right-to-make-it",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T17:26:18+00:00",
    "summary": "Valve has asked Dbrand to stop selling its Portal 2-themed Companion Cube cases for the Steam Machine, since it never asked the company permission to begin with."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/legacy-nvidia-rtx-3060-12gb-returns-to-retail-five-years-after-original-launch-priced-at-usd339-resurrected-gpu-strategy-that-jensen-called-a-good-idea-apparently-comes-to-fruition",
    "domain": "AI 算力 / 半导体",
    "title": "Legacy Nvidia RTX 3060 12GB returns to retail five years after original launch, priced at $339 — resurrected GPU strategy that Jensen called a 'good idea' apparently comes to fruition",
    "url": "https://www.tomshardware.com/pc-components/gpus/legacy-nvidia-rtx-3060-12gb-returns-to-retail-five-years-after-original-launch-priced-at-usd339-resurrected-gpu-strategy-that-jensen-called-a-good-idea-apparently-comes-to-fruition",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T17:11:15+00:00",
    "summary": "After Nvidia CEO Jensen Huang said that \"it's a good idea\" to consider re-introducing older GPUs made on trailing process nodes, the five-year-old RTX 3060 is back on e-tailer shelves, priced at $339."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/south-korea-unveils-usd520-billion-investment-plan-with-samsung-and-sk-hynix-to-expand-memory-chip-dominance-plan-includes-four-new-fabs-and-hbm-facilities-amid-strong-government-support",
    "domain": "AI 算力 / 半导体",
    "title": "South Korea unveils $520 billion investment plan with Samsung and SK Hynix to expand memory chip dominance — plan includes four new fabs and HBM facilities, amid strong government support",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/south-korea-unveils-usd520-billion-investment-plan-with-samsung-and-sk-hynix-to-expand-memory-chip-dominance-plan-includes-four-new-fabs-and-hbm-facilities-amid-strong-government-support",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T14:12:23+00:00",
    "summary": "President Lee unveiled an 800 trillion won ($520B) public-private plan for four new Samsung and SK Hynix fabs, dwarfing the US CHIPS Act tenfold."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/steamroller-becomes-first-prebuilt-gaming-pc-to-ship-with-steamos-ryzen-9600x-radeon-rx-7600-16gb-ddr5-ram-system-available-for-preorder-at-usd1-299",
    "domain": "AI 算力 / 半导体",
    "title": "Steamroller becomes first prebuilt gaming PC to ship with SteamOS — Ryzen 9600X, Radeon RX 7600, 16GB DDR5 RAM system available for preorder at $1,299",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/steamroller-becomes-first-prebuilt-gaming-pc-to-ship-with-steamos-ryzen-9600x-radeon-rx-7600-16gb-ddr5-ram-system-available-for-preorder-at-usd1-299",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T13:30:00+00:00",
    "summary": "Steamroller is the first commercially available prebuilt gaming PC running SteamOS, pairing standard desktop components with future upgradeability."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/samsung-sk-hynix-and-micron-sued-over-alleged-dram-price-fixing-amid-record-memory-costs",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung, SK hynix, and Micron sued over alleged DRAM price fixing amid record memory costs — lawsuit claims coordinated HBM shift was cover to curtail DDR3 and DDR4 production",
    "url": "https://www.tomshardware.com/tech-industry/samsung-sk-hynix-and-micron-sued-over-alleged-dram-price-fixing-amid-record-memory-costs",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T13:18:54+00:00",
    "summary": "Samsung, SK hynix, and Micron were sued on June 25th in the U.S. District Court for the Northern District of California."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/imecs-2026-roadmap-details-0-3nm-nodes-by-2038-cfet-transistors-become-viable-at-0-7nm-company-redefines-moores-law-as-cell-sizes-gain-importance-for-density",
    "domain": "AI 算力 / 半导体",
    "title": "Imec's 2026 roadmap details 0.3nm nodes by 2038, CFET transistors become viable at 0.7nm — company redefines Moore's Law as cell sizes gain importance for density",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/imecs-2026-roadmap-details-0-3nm-nodes-by-2038-cfet-transistors-become-viable-at-0-7nm-company-redefines-moores-law-as-cell-sizes-gain-importance-for-density",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T13:15:14+00:00",
    "summary": "As CPP shrinking stalls, chipmakers find a new way to increase transistor density. Imec foresees 0.3nm in 2038, CFET insertion in 2038, HLSI era."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-a-massive-usd1-100-on-this-rtx-5080-gaming-pc-with-a-9800x3d-from-hp-now-just-usd2-499-liquid-cooled-omen-35l-rig-unlocks-4k-gameplay-with-32gb-ddr5-and-a-2tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Save a massive $1,100 on this RTX 5080 gaming PC with a 9800X3D from HP, now just $2,499 — liquid-cooled Omen 35L rig unlocks 4K gameplay with 32GB DDR5 and a 2TB SSD",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-a-massive-usd1-100-on-this-rtx-5080-gaming-pc-with-a-9800x3d-from-hp-now-just-usd2-499-liquid-cooled-omen-35l-rig-unlocks-4k-gameplay-with-32gb-ddr5-and-a-2tb-ssd",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T11:15:36+00:00",
    "summary": "Save $1,100 on this HP Omen 45L gaming rig, fitted with a 9800X3D, RTX 5080, 32GB of DDR5 RAM, and 2TB in SSD storage, all for just $2,499.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/pc-building/pick-up-hotos-ultra-useful-3d-printing-tool-for-just-usd29-save-40-percent-on-this-35-piece-cordless-rotary-tool-to-give-your-creations-a-finishing-touch",
    "domain": "AI 算力 / 半导体",
    "title": "Pick up Hoto's ultra-useful 3D printing tool for just $29 — save 40% on this 35-piece Cordless Rotary Tool to give your creations a finishing touch",
    "url": "https://www.tomshardware.com/desktops/pc-building/pick-up-hotos-ultra-useful-3d-printing-tool-for-just-usd29-save-40-percent-on-this-35-piece-cordless-rotary-tool-to-give-your-creations-a-finishing-touch",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T11:12:00+00:00",
    "summary": "Save on these brilliant Hoto tools for PC builders and hobbyists. Hoto's cordless rotary tool is now only $29."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/chinas-hollow-core-fiber-trial-pushes-51-3-tb-s-over-128-miles-without-signal-regeneration-milestone-targets-ai-era-networking-bottlenecks",
    "domain": "AI 算力 / 半导体",
    "title": "China’s hollow-core fiber trial pushes 51.3 Tb/s over 128 miles without signal regeneration — milestone targets AI-era networking bottlenecks",
    "url": "https://www.tomshardware.com/networking/chinas-hollow-core-fiber-trial-pushes-51-3-tb-s-over-128-miles-without-signal-regeneration-milestone-targets-ai-era-networking-bottlenecks",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T10:00:00+00:00",
    "summary": "YOFC, China Telecom, and Dekoli claim a 51.3 Tb/s hollow-core fiber field-trial record over 206.5 km, using 1.2 Tb/s-per-wavelength WDM transmission without repeaters or remote-pumped amplifiers."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/pong-game-that-recompiles-itself-every-frame-wins-the-ioccc29-obfuscated-c-contest",
    "domain": "AI 算力 / 半导体",
    "title": "Pong game recompiles its own source code every frame — winning entry at IOCCC29 was generated by a custom compiler",
    "url": "https://www.tomshardware.com/tech-industry/pong-game-that-recompiles-itself-every-frame-wins-the-ioccc29-obfuscated-c-contest",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T09:30:00+00:00",
    "summary": "Jonah Uellenberg won the Ping Pong Prize at the 29th International Obfuscated C Code Contest earlier this month, with a version of Pong that recompiles its own source code on every frame."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/pnys-performance-32gb-ddr5-5600-ram-becomes-the-cheapest-2x16gb-kit-ddr5-kit-gets-a-usd70-discount",
    "domain": "AI 算力 / 半导体",
    "title": "Corsair's Vengeance 32GB DDR5-5600 RAM becomes the cheapest 2x16GB kit— DDR5 kit gets a $111 discount",
    "url": "https://www.tomshardware.com/pc-components/pnys-performance-32gb-ddr5-5600-ram-becomes-the-cheapest-2x16gb-kit-ddr5-kit-gets-a-usd70-discount",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T14:32:37+00:00",
    "summary": "This 32GB DDR5 memory kit won't impress enthusiasts with its timings or design, but its aggressive price makes it difficult to overlook."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/lenovo-says-the-ramageddon-is-the-new-normal-outlines-survival-guide-at-isc-2026-an-exec-said-it-will-never-be-like-it-was-last-year",
    "domain": "AI 算力 / 半导体",
    "title": "Lenovo says the 'RAMageddon' is the new normal, outlines survival guide — at ISC 2026 an exec said 'it will never be like it was last year'",
    "url": "https://www.tomshardware.com/pc-components/ram/lenovo-says-the-ramageddon-is-the-new-normal-outlines-survival-guide-at-isc-2026-an-exec-said-it-will-never-be-like-it-was-last-year",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T13:50:59+00:00",
    "summary": "At the International Supercomputing Conference this past week, Lenovo reportedly said the memory market 'it will never be like it was last year.'"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/pc-building/diy-3d-printed-steam-machine-a-like-uses-diagonal-mobo-mounting-parts-include-a-mini-itx-motherboard-rtx-5060-and-a-flex-atx-psu",
    "domain": "AI 算力 / 半导体",
    "title": "AMD engineer 3D-prints Steam Machine-a-like with diagonal mobo mounting — parts include a Mini ITX motherboard, RTX 5060, and a flex ATX PSU",
    "url": "https://www.tomshardware.com/desktops/pc-building/diy-3d-printed-steam-machine-a-like-uses-diagonal-mobo-mounting-parts-include-a-mini-itx-motherboard-rtx-5060-and-a-flex-atx-psu",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T12:36:37+00:00",
    "summary": "The Terk Box v1.1 looks like the closest DIY alternative to Valve's Steam Machine yet. 3D print source files are available."
  },
  {
    "id": "rss:https://www.tomshardware.com/service-providers/streaming/us-seizes-nearly-400-domains-streaming-the-2026-world-cup",
    "domain": "AI 算力 / 半导体",
    "title": "400 domains used for illegal 2026 World Cup streams seized by US Justice Department — operation is five times the scale of the previous crackdown",
    "url": "https://www.tomshardware.com/service-providers/streaming/us-seizes-nearly-400-domains-streaming-the-2026-world-cup",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T12:18:15+00:00",
    "summary": "The US Department of Justice has announced that it has seized nearly 400 domains that were illegally streaming live matches from the 2026 FIFA World Cup."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/chinas-loongson-launches-homegrown-16-core-server-cpu-built-on-loongarch-architecture-40w-chip-with-ddr4-ecc-and-32-pcie-lanes-targets-cheap-smb-file-database-and-web-servers",
    "domain": "AI 算力 / 半导体",
    "title": "China’s Loongson launches homegrown 16-core server CPU built on LoongArch architecture — 40W chip with DDR4 ECC and 32 PCIe lanes targets cheap SMB file, database, and web servers",
    "url": "https://www.tomshardware.com/pc-components/cpus/chinas-loongson-launches-homegrown-16-core-server-cpu-built-on-loongarch-architecture-40w-chip-with-ddr4-ecc-and-32-pcie-lanes-targets-cheap-smb-file-database-and-web-servers",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T12:00:00+00:00",
    "summary": "Loongson has announced the 3C3000, a 16-core LoongArch server CPU with DDR4 ECC, 32 PCIe lanes, 40W typical power, and performance claimed to match the earlier 3C5000."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/ai-coding-agents-can-be-tricked-into-installing-malware-via-clean-github-repositories-mozillas-0din-team-shows-how-claude-code-can-be-exploited-by-its-own-helpfulness",
    "domain": "AI 算力 / 半导体",
    "title": "AI coding agents can be tricked into installing malware via 'clean' GitHub repositories — Mozilla's 0din team shows how Claude Code can be exploited by its own helpfulness",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/ai-coding-agents-can-be-tricked-into-installing-malware-via-clean-github-repositories-mozillas-0din-team-shows-how-claude-code-can-be-exploited-by-its-own-helpfulness",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T11:30:00+00:00",
    "summary": "Claude and other AI agents fooled into running malware with just a minimal GitHub repository — ask the bot to initialize the project and you get hacked"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/playstation-is-removing-over-500-movies-from-uk-customers-accounts-with-no-refunds-iconic-films-like-terminator-2-apocalypse-now-and-mulholland-drive-are-getting-deleted",
    "domain": "AI 算力 / 半导体",
    "title": "PlayStation is removing over 500 movies from UK customers' accounts with no refunds — Iconic films like Terminator 2, Apocalypse Now, and Mulholland Drive are getting deleted",
    "url": "https://www.tomshardware.com/video-games/playstation/playstation-is-removing-over-500-movies-from-uk-customers-accounts-with-no-refunds-iconic-films-like-terminator-2-apocalypse-now-and-mulholland-drive-are-getting-deleted",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T11:00:00+00:00",
    "summary": "Sony will delete 551 movies from PlayStation users' accounts in the UK on September 1, 2026. These are films distributed by StudioCanal that no longer come under licensing agreements between the two c"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/pc-building/japanese-firm-launches-hyper-realistic-capsule-toy-pc-parts-you-can-assemble-and-play-with-tiny-motherboards-cases-and-cpus-are-coming-after-tarlin-inks-collab-with-the-big-four-pc-parts-makers",
    "domain": "AI 算力 / 半导体",
    "title": "Japanese firm launches hyper-realistic capsule toy PC parts ‘you can assemble and play with’ — tiny motherboards, cases, and CPUs are coming after Tarlin inks collab with the ‘big four’ PC parts maker",
    "url": "https://www.tomshardware.com/desktops/pc-building/japanese-firm-launches-hyper-realistic-capsule-toy-pc-parts-you-can-assemble-and-play-with-tiny-motherboards-cases-and-cpus-are-coming-after-tarlin-inks-collab-with-the-big-four-pc-parts-makers",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T10:30:00+00:00",
    "summary": "A Japanese capsule toy maker has announced an official collaboration with ASRock, Gigabyte, MSI, and Intel to make tiny PC components that buyers 'can assemble and play with.'"
  },
  {
    "id": "rss:https://www.eetimes.com/synaptics-acquisition-by-onsemi-affirms-edge-ai-is-for-real/",
    "domain": "AI 算力 / 半导体",
    "title": "Synaptics Acquisition by Onsemi Affirms Edge AI Is for Real",
    "url": "https://www.eetimes.com/synaptics-acquisition-by-onsemi-affirms-edge-ai-is-for-real/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T14:41:31+00:00",
    "summary": "Here is why a power and sensing specialist has snapped AI-native compute assets to foray into the physical AI world. The post Synaptics Acquisition by Onsemi Affirms Edge AI Is for Real appeared first"
  },
  {
    "id": "rss:https://www.eetimes.com/the-pqc-silicon-is-here-today-for-tomorrows-quantum-threats/",
    "domain": "AI 算力 / 半导体",
    "title": "The PQC Silicon Is Here Today for Tomorrow’s Quantum Threats",
    "url": "https://www.eetimes.com/the-pqc-silicon-is-here-today-for-tomorrows-quantum-threats/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T08:38:45+00:00",
    "summary": "Two new security chips aim to future-proof devices for the quantum era by integrating hardware accelerators that support PQC algorithms. The post The PQC Silicon Is Here Today for Tomorrow’s Quantum T"
  },
  {
    "id": "rss:https://www.eetimes.com/next%e2%80%91gen-adas-ad-architectures-power-networking-safety-sensors/",
    "domain": "AI 算力 / 半导体",
    "title": "Next‑Gen ADAS/AD Architectures: Power, Networking, Safety & Sensors",
    "url": "https://www.eetimes.com/next%e2%80%91gen-adas-ad-architectures-power-networking-safety-sensors/",
    "source": "Infineon Technologies",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T08:13:23+00:00",
    "summary": "Join this webinar and learn how high‑performance semiconductor technologies support centralized sensor fusion and reliable ADAS systems. The post Next‑Gen ADAS/AD Architectures: Power, Networking, Saf"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/get-an-rtx-5060-gaming-laptop-loaded-with-ryzen-7-cpu-and-32gb-ram-for-usd1-099-mobile-gaming-upgrade-just-got-usd300-cheaper",
    "domain": "AI 算力 / 半导体",
    "title": "Get an RTX 5060 gaming laptop loaded with Ryzen 7 CPU and 32GB RAM for $1,099 — mobile gaming upgrade just got $300 cheaper",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/get-an-rtx-5060-gaming-laptop-loaded-with-ryzen-7-cpu-and-32gb-ram-for-usd1-099-mobile-gaming-upgrade-just-got-usd300-cheaper",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T17:10:07+00:00",
    "summary": "The Gigabyte Aero X16 positions itself as a compelling mid-range gaming laptop offering a smooth high-refresh display, capable RTX 5060 graphics performance, and future-ready upgrade options."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/apple-reportedly-lobbies-uncle-sam-for-access-to-chinese-memory-chips-tech-giant-allegedly-wants-to-buy-from-blacklisted-cxmt",
    "domain": "AI 算力 / 半导体",
    "title": "Apple reportedly lobbies Uncle Sam for access to Chinese memory chips — tech giant allegedly wants to buy from blacklisted CXMT",
    "url": "https://www.tomshardware.com/tech-industry/apple-reportedly-lobbies-uncle-sam-for-access-to-chinese-memory-chips-tech-giant-allegedly-wants-to-buy-from-blacklisted-cxmt",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T14:51:29+00:00",
    "summary": "Following a historic price hike, the Financial Times reports that Apple is lobbying in Washington to secure approval to buy cheaper RAM from CXMT. The manufacturer is currently designated as a Chinese"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/console-gaming/steam-machine-scalping-hits-usd3-000-on-ebay-as-sellers-list-preorder-reservations-scalpers-already-flipping-queues-for-2x-the-msrp-of-the-2tb-model",
    "domain": "AI 算力 / 半导体",
    "title": "Steam Machine scalping hits $3,000 on eBay as sellers list preorder reservations — scalpers already flipping queues for 2X the MSRP of the 2TB model",
    "url": "https://www.tomshardware.com/video-games/console-gaming/steam-machine-scalping-hits-usd3-000-on-ebay-as-sellers-list-preorder-reservations-scalpers-already-flipping-queues-for-2x-the-msrp-of-the-2tb-model",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T14:24:10+00:00",
    "summary": "Several listings for Steam Machine pre-orders are being sold at markups so high that buyers will have to pay 140% to 167% above Valve's selling price."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intels-next-gen-52-core-nova-lake-cpu-could-pull-up-to-474w-high-end-lga1954-motherboards-may-need-three-8-pin-power-connectors-to-feed-the-monster",
    "domain": "AI 算力 / 半导体",
    "title": "Intel's next-gen 52-core Nova Lake CPU could pull up to 474W — high-end LGA1954 motherboards may need three 8-pin power connectors to feed the monster",
    "url": "https://www.tomshardware.com/pc-components/cpus/intels-next-gen-52-core-nova-lake-cpu-could-pull-up-to-474w-high-end-lga1954-motherboards-may-need-three-8-pin-power-connectors-to-feed-the-monster",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T14:05:30+00:00",
    "summary": "Intel's flagship 52-core Nova Lake processor could feature a 474W PL2 power limit. At the same time, the new LGA1954 platform may introduce motherboard tiers for up to 175W CPUs and optional triple EP"
  },
  {
    "id": "rss:https://www.tomshardware.com/live/news/best-amazon-prime-day-deals-2026",
    "domain": "AI 算力 / 半导体",
    "title": "Best Amazon Prime Day tech deals you can still get LIVE, last chance for hot deals — PC hardware deals on GPUs, CPUs, SSDs, and more",
    "url": "https://www.tomshardware.com/live/news/best-amazon-prime-day-deals-2026",
    "source": "The Editors of Tom&#039;s Hardware",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T13:18:26+00:00",
    "summary": "Find the very best PC hardware deals during Amazon Prime Day."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/bambu-lab-a2l-3d-printer-review",
    "domain": "AI 算力 / 半导体",
    "title": "Bambu Lab A2L 3D printer review: The A1 grows up",
    "url": "https://www.tomshardware.com/3d-printing/bambu-lab-a2l-3d-printer-review",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T13:05:02+00:00",
    "summary": "Bambu Lab adds a bigger bed slinger to their lineup."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/controllers-gamepads/modded-steam-controller-can-automatically-charge-itself-like-a-robot-vacuum-enthusiast-creates-github-program-that-uses-the-vibration-motor-to-walk-it-back-to-its-docking-station",
    "domain": "AI 算力 / 半导体",
    "title": "Modded Steam Controller can automatically charge itself like a robot vacuum — enthusiast creates GitHub program that uses the vibration motor to walk it back to its docking station",
    "url": "https://www.tomshardware.com/peripherals/controllers-gamepads/modded-steam-controller-can-automatically-charge-itself-like-a-robot-vacuum-enthusiast-creates-github-program-that-uses-the-vibration-motor-to-walk-it-back-to-its-docking-station",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T11:00:00+00:00",
    "summary": "Ray Foss built this program that uses computer vision to let your Steam Controller slide back towards its charging puck by just using its built-in haptic motors. You can also try it for yourself by vi"
  },
  {
    "id": "rss:https://www.tomshardware.com/phones/commodore-drops-callback-flip-ohine-to-399-by-defaulting-to-recycled-memory-chips",
    "domain": "AI 算力 / 半导体",
    "title": "Commodore drops Callback flip phone by $100 by defaulting to recycled memory chips and unbundling the earphones — Callback 8020 drops to $399 as skyrocketing memory prices punish smartphone buyers",
    "url": "https://www.tomshardware.com/phones/commodore-drops-callback-flip-ohine-to-399-by-defaulting-to-recycled-memory-chips",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T10:30:00+00:00",
    "summary": "Commodore has slashed the starting price of its Callback 8020 flip phone to $399, down from $499."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/ram-crisis-provokes-enthusiast-to-try-windows-11-on-ddr1-era-hardware-other-key-vintage-components-included-the-core-2-q6600-and-ati-radeon-hd-4650-agp",
    "domain": "AI 算力 / 半导体",
    "title": "RAM crisis provokes enthusiast to try Windows 11 on DDR1-era hardware — other key vintage components included the Core 2 Q6600 and ATI Radeon HD 4650 AGP",
    "url": "https://www.tomshardware.com/software/windows/ram-crisis-provokes-enthusiast-to-try-windows-11-on-ddr1-era-hardware-other-key-vintage-components-included-the-core-2-q6600-and-ati-radeon-hd-4650-agp",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T10:00:00+00:00",
    "summary": "Enthusiast demos Microsoft’s newest OS running 'completely stable' on a Core 2 Quad Q6600, using a DDR1 motherboard, supported by an ATi Radeon HD 4650 AGP graphics card."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/incredible-ryzen-7-9800x3d-prebuilt-deal-comes-with-rx-9070-xt-and-32gb-of-ddr5-for-usd750-off-get-a-prime-ibuypower-4k-gaming-rig-for-just-usd1-749",
    "domain": "AI 算力 / 半导体",
    "title": "Incredible Ryzen 7 9800X3D prebuilt deal comes with an RX 9070 XT and 32GB of DDR5 for $750 off — get a prime iBuyPower 4K gaming rig for just $1,749",
    "url": "https://www.tomshardware.com/pc-components/incredible-ryzen-7-9800x3d-prebuilt-deal-comes-with-rx-9070-xt-and-32gb-of-ddr5-for-usd750-off-get-a-prime-ibuypower-4k-gaming-rig-for-just-usd1-749",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T20:01:01+00:00",
    "summary": "The iBuyPower Y40 PC is on an incredible sale, offering a Ryzen 7 9800X3D, RX 9070 XT, 1TB of storage, and 32GB of memory for $750 off."
  },
  {
    "id": "rss:https://www.eetimes.com/jim-keller-on-tenstorrents-blackhole-scaling-and-ipo-ambitions/",
    "domain": "AI 算力 / 半导体",
    "title": "Jim Keller: ‘AI Still Obeys the Old Laws of Compute’",
    "url": "https://www.eetimes.com/jim-keller-on-tenstorrents-blackhole-scaling-and-ipo-ambitions/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T22:00:00+00:00",
    "summary": "Invoking Rent's Rule and Amdahl's Law, Keller argues that memory and communication, not bigger processors, will define the future of AI infrastructure The post Jim Keller: ‘AI Still Obeys the Old Laws"
  },
  {
    "id": "rss:https://www.eetimes.com/openai-jalapeno-will-be-spicy-but-the-real-sizzle-is-its-chip-design-ai/",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI’s Jalapeño Will Be Spicy, But the Real Sizzle Is Its Chip Design AI",
    "url": "https://www.eetimes.com/openai-jalapeno-will-be-spicy-but-the-real-sizzle-is-its-chip-design-ai/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T15:59:00+00:00",
    "summary": "The custom inference accelerator follows the hyperscaler playbook, but the AI-automated chip design process could prove the more consequential announcement. The post OpenAI’s Jalapeño Will Be Spicy, B"
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
    "id": "rss:https://www.theverge.com/tech/959144/t-mobile-legacy-plan-retire-sprint",
    "domain": "大厂 AI 动态",
    "title": "T-Mobile is booting customers from its oldest plans",
    "url": "https://www.theverge.com/tech/959144/t-mobile-legacy-plan-retire-sprint",
    "source": "Allison Johnson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T21:06:14+00:00",
    "summary": "Earlier today, T-Mobile started notifying customers that it will be retiring many legacy plans and moving subscribers onto one of its current rate plans. This move includes plans that date back to the"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/958953/supergirl-dcu-warner-bros-discovery-box-office-flop",
    "domain": "大厂 AI 动态",
    "title": "After a great start, DC’s new cinematic universe is already slowing down",
    "url": "https://www.theverge.com/entertainment/958953/supergirl-dcu-warner-bros-discovery-box-office-flop",
    "source": "Charles Pulliam-Moore",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T21:00:00+00:00",
    "summary": "While Kara Zor-El's appearance at the end of James Gunn's Superman was a very pleasant surprise, Warner Bros. Discovery's plan to fast-track a standalone Supergirl feature always felt a little dubious"
  },
  {
    "id": "rss:https://www.theverge.com/tech/959229/iphone-18-pro-leak-apple-dark-web",
    "domain": "大厂 AI 动态",
    "title": "Leaked iPhone 18 Pro photos reportedly wound up on the dark web",
    "url": "https://www.theverge.com/tech/959229/iphone-18-pro-leak-apple-dark-web",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T20:18:26+00:00",
    "summary": "Leaked iPhone 18 Pro photos and parts lists appeared on the dark web following a data breach affecting one of Apple's key suppliers, according to a report from Reuters. The leaked images show a drop t"
  },
  {
    "id": "rss:https://www.theverge.com/tech/959211/tidal-ai-music-policy-demonetizingdetect-label",
    "domain": "大厂 AI 动态",
    "title": "Tidal won’t pay royalties on AI-generated music but isn’t banning it outright",
    "url": "https://www.theverge.com/tech/959211/tidal-ai-music-policy-demonetizingdetect-label",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T19:47:35+00:00",
    "summary": "Tidal shared its new policies regarding AI-generated music today and how the platform plans to \"protect artists\" and \"inform listeners.\" Instead of banning it outright, starting on July 15th Tidal wil"
  },
  {
    "id": "rss:https://www.theverge.com/games/959191/sony-next-generation-playstation-ps6-beyond-the-living-room",
    "domain": "大厂 AI 动态",
    "title": "Sony&#8217;s next-gen PlayStation will go ‘beyond the living room’",
    "url": "https://www.theverge.com/games/959191/sony-next-generation-playstation-ps6-beyond-the-living-room",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T19:12:15+00:00",
    "summary": "Sony hinted in a recent Q&#38;A with investors that the next generation PlayStation will offer some kind of experience that lets you play games outside of your living room. Here's the relevant portion"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/959174/openai-codex-hardware-work-louder",
    "domain": "大厂 AI 动态",
    "title": "OpenAI is teasing new hardware… for Codex",
    "url": "https://www.theverge.com/ai-artificial-intelligence/959174/openai-codex-hardware-work-louder",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T18:52:03+00:00",
    "summary": "OpenAI is releasing some sort of device related to its AI-powered coding tool, Codex, on July 15th. In a video posted to X on Monday, OpenAI shows a square-shaped device with several buttons, alongsid"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/959080/ipad-air-m3-5g-wifi-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "At $499, Apple&#8217;s M3-powered iPad Air is a good deal",
    "url": "https://www.theverge.com/gadgets/959080/ipad-air-m3-5g-wifi-deal-sale",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T17:49:12+00:00",
    "summary": "Most of Apple&#8217;s price increases have gone into effect, resulting in iPads and other products costing hundreds more than they did a few days ago. If last week’s Prime Day sale wasn&#8217;t a good"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/958906/best-july-4th-tech-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "The best July 4th sales we found so far",
    "url": "https://www.theverge.com/gadgets/958906/best-july-4th-tech-deal-sale",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T16:42:48+00:00",
    "summary": "July 4th sales are typically a precursor to what we&#8217;d see during a mid-July Prime Day, but obviously things are flipped around this year. Last week&#8217;s big Prime Day sale is over, yet there "
  },
  {
    "id": "rss:https://www.theverge.com/tech/958832/whatsapp-usernames-rollout-reservation-availability",
    "domain": "大厂 AI 动态",
    "title": "WhatsApp is launching usernames: here’s how to reserve yours",
    "url": "https://www.theverge.com/tech/958832/whatsapp-usernames-rollout-reservation-availability",
    "source": "Jess Weatherbed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T16:00:00+00:00",
    "summary": "WhatsApp is introducing a new way to add and chat with contacts, without having to share your phone number. Usernames will launch \"later this year,\" in a move to make the communications platform \"even"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/959033/health-location-data-protection-act-ai-warren-scanlon",
    "domain": "大厂 AI 动态",
    "title": "Lawmakers want to ban AI companies from selling your health data",
    "url": "https://www.theverge.com/ai-artificial-intelligence/959033/health-location-data-protection-act-ai-warren-scanlon",
    "source": "Hayden Field",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T16:00:00+00:00",
    "summary": "A new proposal would ban the sale of Americans' health and location information to data brokers - including information people reveal to an AI chatbot like ChatGPT or Claude. In the coming weeks, Sena"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/29/the-ai-jobs-debate-just-got-messier/",
    "domain": "大厂 AI 动态",
    "title": "The AI jobs debate just got messier",
    "url": "https://techcrunch.com/2026/06/29/the-ai-jobs-debate-just-got-messier/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T04:01:00+00:00",
    "summary": "A new report finds \"high-intensity AI adopters” saw headcount increase 10.2%. Among those companies, entry-level headcount rose by 12%, countering the rhetoric that AI kills junior jobs."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/29/vibe-coding-platform-base44-launches-own-model-as-ai-startups-seek-defensibility/",
    "domain": "大厂 AI 动态",
    "title": "Vibe coding platform Base44 launches own model as AI startups seek defensibility",
    "url": "https://techcrunch.com/2026/06/29/vibe-coding-platform-base44-launches-own-model-as-ai-startups-seek-defensibility/",
    "source": "Anna Heim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T02:28:41+00:00",
    "summary": "Wix-owned vibe coding platform Base44 has started rolling out its own AI model — with hopes that it will eventually outperform frontier models."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/29/chamath-palihapitiya-raises-135m-series-a-for-his-ai-coding-startup-takes-ceo-role/",
    "domain": "大厂 AI 动态",
    "title": "Chamath Palihapitiya raises $135M Series A for his AI coding startup, takes CEO role",
    "url": "https://techcrunch.com/2026/06/29/chamath-palihapitiya-raises-135m-series-a-for-his-ai-coding-startup-takes-ceo-role/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T20:55:50+00:00",
    "summary": "VCs remain thirsty to fund AI coding startups. This one, founded by investor Chamath Palihapitiya, is no exception."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/29/geminis-personalized-ai-image-generation-is-now-free-for-u-s-users/",
    "domain": "大厂 AI 动态",
    "title": "Gemini’s personalized AI image generation is now free for US users",
    "url": "https://techcrunch.com/2026/06/29/geminis-personalized-ai-image-generation-is-now-free-for-u-s-users/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T20:12:59+00:00",
    "summary": "Google is expanding Gemini’s personalized AI image generation to eligible free users in the U.S., allowing the chatbot to create images based on your interests and data from connected Google apps."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/29/watch-out-amazon-the-kobo-ereader-now-has-a-goodreads-rival/",
    "domain": "大厂 AI 动态",
    "title": "Watch out, Amazon: The Kobo eReader now has a Goodreads rival",
    "url": "https://techcrunch.com/2026/06/29/watch-out-amazon-the-kobo-ereader-now-has-a-goodreads-rival/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T19:06:21+00:00",
    "summary": "Kobo users can now automatically sync their reading progress to StoryGraph, making it easier to track books, reading stats, and challenges without relying on Amazon’s Goodreads."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/29/waymo-and-uber-quietly-part-ways-in-phoenix/",
    "domain": "大厂 AI 动态",
    "title": "Waymo and Uber quietly part ways in Phoenix",
    "url": "https://techcrunch.com/2026/06/29/waymo-and-uber-quietly-part-ways-in-phoenix/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T18:45:12+00:00",
    "summary": "Uber said it is readying the launch of a separate autonomous vehicle partnership in the city, but did not name the partner."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/29/anthropic-and-gov-newsom-forge-deal-allowing-california-government-to-use-claude-at-half-price/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic and Gov. Newsom forge deal allowing California government to use Claude at half price",
    "url": "https://techcrunch.com/2026/06/29/anthropic-and-gov-newsom-forge-deal-allowing-california-government-to-use-claude-at-half-price/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T18:10:26+00:00",
    "summary": "As Anthropic forges a closer relationship with the state of California, the federal government has made an enemy out of the OpenAI rival."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/29/south-korean-tech-giants-commit-over-550b-to-ease-ramageddon/",
    "domain": "大厂 AI 动态",
    "title": "South Korean tech giants commit over $550B to ease ‘RAMageddon’",
    "url": "https://techcrunch.com/2026/06/29/south-korean-tech-giants-commit-over-550b-to-ease-ramageddon/",
    "source": "Kate Park",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T18:07:48+00:00",
    "summary": "The world's two largest memory chip companies vow to build more memory lab fabs as South Korea positions itself as an AI tech powerhouse country."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/29/arena-the-ai-leaderboard-everyone-uses-is-now-a-100m-business/",
    "domain": "大厂 AI 动态",
    "title": "Arena, the AI leaderboard everyone uses, is now a $100M business",
    "url": "https://techcrunch.com/2026/06/29/arena-the-ai-leaderboard-everyone-uses-is-now-a-100m-business/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T17:39:17+00:00",
    "summary": "The startup, which runs a popular free AI leaderboard, launched its commercial service just last September."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/29/cursor-now-has-a-mobile-app-for-guiding-your-coding-agent-on-the-go/",
    "domain": "大厂 AI 动态",
    "title": "Cursor now has a mobile app for guiding your coding agent on the go",
    "url": "https://techcrunch.com/2026/06/29/cursor-now-has-a-mobile-app-for-guiding-your-coding-agent-on-the-go/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T17:03:50+00:00",
    "summary": "Cursor has launched a new mobile app for remote oversight over coding agents."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/29/trump-administration-threatens-92-gw-of-new-electricity-supply-with-red-tape/",
    "domain": "大厂 AI 动态",
    "title": "Trump administration threatens 92 GW of new electricity supply with red tape",
    "url": "https://techcrunch.com/2026/06/29/trump-administration-threatens-92-gw-of-new-electricity-supply-with-red-tape/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T16:58:30+00:00",
    "summary": "The Trump administration's moves threaten $121 billion in new solar and wind power, two energy sources that are the biggest contributors to new capacity in the U.S."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/29/tidal-cracks-down-on-ai-music-by-cutting-off-monetization/",
    "domain": "大厂 AI 动态",
    "title": "TIDAL cracks down on AI music by cutting off monetization",
    "url": "https://techcrunch.com/2026/06/29/tidal-cracks-down-on-ai-music-by-cutting-off-monetization/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T16:29:04+00:00",
    "summary": "In addition, TIDAL will use automated tools to remove AI-generated music that attempts to impersonate an artist or a group, the company said."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/29/in-major-privacy-win-supreme-court-rules-geofence-warrants-are-protected-by-privacy-rights/",
    "domain": "大厂 AI 动态",
    "title": "In major privacy win, Supreme Court rules geofence warrants are protected by privacy rights",
    "url": "https://techcrunch.com/2026/06/29/in-major-privacy-win-supreme-court-rules-geofence-warrants-are-protected-by-privacy-rights/",
    "source": "Zack Whittaker, Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T16:05:23+00:00",
    "summary": "The Supreme Court's decision to limit geofence warrants is a win for privacy advocates, who called their use unconstitutional but sought an outright ban."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/29/whatsapp-now-lets-you-reserve-usernames/",
    "domain": "大厂 AI 动态",
    "title": "WhatsApp now lets you reserve usernames",
    "url": "https://techcrunch.com/2026/06/29/whatsapp-now-lets-you-reserve-usernames/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T16:00:00+00:00",
    "summary": "WhatsApp username can be between 3 to 35 characters."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/29/rocket-lab-continues-buying-spree-by-acquiring-satellite-company-iridium/",
    "domain": "大厂 AI 动态",
    "title": "Rocket Lab continues buying spree by acquiring satellite company Iridium",
    "url": "https://techcrunch.com/2026/06/29/rocket-lab-continues-buying-spree-by-acquiring-satellite-company-iridium/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T15:02:07+00:00",
    "summary": "The all-stock deal values Iridium at $8 billion and gives Rocket Lab even more firepower to compete against Amazon and SpaceX."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/29/robot-hand-company-settles-tesla-trade-secret-suit-and-announces-11m-raise/",
    "domain": "大厂 AI 动态",
    "title": "Robot hand company settles Tesla trade secret suit and announces $11M raise",
    "url": "https://techcrunch.com/2026/06/29/robot-hand-company-settles-tesla-trade-secret-suit-and-announces-11m-raise/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T14:00:08+00:00",
    "summary": "The startup, Proception, is taking a unique approach to collecting training data to tackle one of the hardest problems in robotics: hands."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/29/pocket-raises-11m-in-bet-on-rising-demand-for-ai-note-taking-devices/",
    "domain": "大厂 AI 动态",
    "title": "Pocket raises $11M in bet on rising demand for AI note-taking devices",
    "url": "https://techcrunch.com/2026/06/29/pocket-raises-11m-in-bet-on-rising-demand-for-ai-note-taking-devices/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T13:16:00+00:00",
    "summary": "Pocket sells a $129 credit card-shaped puck, which sticks to the back of your phone, and promises unlimited recordings, transcriptions, and to-do items."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/29/flipper-devices-new-busy-bar-is-a-customizable-display-for-productivity/",
    "domain": "大厂 AI 动态",
    "title": "Flipper Device’s new Busy Bar is a customizable display for productivity",
    "url": "https://techcrunch.com/2026/06/29/flipper-devices-new-busy-bar-is-a-customizable-display-for-productivity/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T13:00:00+00:00",
    "summary": "The company's productivity-focused gadget helps you set timers, block apps, and display custom messages and widgets on an LED display."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/29/omen-ais-plan-to-optimize-data-centers-is-all-wet/",
    "domain": "大厂 AI 动态",
    "title": "Omen AI’s plan to optimize data centers is all wet",
    "url": "https://techcrunch.com/2026/06/29/omen-ais-plan-to-optimize-data-centers-is-all-wet/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T13:00:00+00:00",
    "summary": "Omen AI raised a $31 million Series A to monitor chip coolant and stop bacterial outbreaks in data centers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/28/california-law-targeting-loud-streaming-ads-takes-effect-on-july-1/",
    "domain": "大厂 AI 动态",
    "title": "California law targeting loud streaming ads takes effect on July 1",
    "url": "https://techcrunch.com/2026/06/28/california-law-targeting-loud-streaming-ads-takes-effect-on-july-1/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T21:34:14+00:00",
    "summary": "Streaming ads might be getting a lot quieter."
  },
  {
    "id": "rss:https://stratechery.com/2026/summer-break-week-of-june-29/",
    "domain": "大厂 AI 动态",
    "title": "Summer Break: Week of June 29",
    "url": "https://stratechery.com/2026/summer-break-week-of-june-29/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T10:00:00+00:00",
    "summary": "Stratechery is on summer break the week of June 29. There will be no Weekly Article or Updates. The next Update will be on Monday, July 6. Dithering,&#160;Sharp Tech, and&#160;Sharp China&#160;will al"
  },
  {
    "id": "rss:https://arstechnica.com/information-technology/2026/06/us-offers-10-million-for-info-on-group-behind-signal-and-whatsapp-hacking-spree/",
    "domain": "大厂 AI 动态",
    "title": "US offers $10 million for info on group behind Signal and WhatsApp hacking spree",
    "url": "https://arstechnica.com/information-technology/2026/06/us-offers-10-million-for-info-on-group-behind-signal-and-whatsapp-hacking-spree/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T22:05:33+00:00",
    "summary": "Operation by two Russia-state groups has been ongoing since at least March."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/06/south-korea-to-spend-1t-on-more-memory-chip-production-and-humanoid-robots/",
    "domain": "大厂 AI 动态",
    "title": "South Korea to spend $1T on more memory chip production and humanoid robots",
    "url": "https://arstechnica.com/ai/2026/06/south-korea-to-spend-1t-on-more-memory-chip-production-and-humanoid-robots/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T21:09:43+00:00",
    "summary": "South Korea targets physical AI lead and commercial humanoid robots by 2028."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/06/solar-outproduced-coal-in-april-but-not-on-the-grid/",
    "domain": "大厂 AI 动态",
    "title": "US renewable boom passes key milestone in April",
    "url": "https://arstechnica.com/science/2026/06/solar-outproduced-coal-in-april-but-not-on-the-grid/",
    "source": "John Timmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T20:12:30+00:00",
    "summary": "Small-scale solar helped renewables hit nearly triple coal's generation in the US."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/06/supreme-court-ruling-guts-governments-use-of-geofence-warrants/",
    "domain": "大厂 AI 动态",
    "title": "Supreme Court ruling guts government’s use of geofence warrants",
    "url": "https://arstechnica.com/tech-policy/2026/06/supreme-court-ruling-guts-governments-use-of-geofence-warrants/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T20:04:04+00:00",
    "summary": "SCOTUS falls short of deeming geofence warrants unconstitutional, though."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/06/sony-erases-digital-content-from-libraries-were-reminded-we-dont-own-what-we-buy/",
    "domain": "大厂 AI 动态",
    "title": "Sony erases digital content from libraries; we're reminded we don’t own what we buy",
    "url": "https://arstechnica.com/gadgets/2026/06/sony-erases-digital-content-from-libraries-were-reminded-we-dont-own-what-we-buy/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T19:10:57+00:00",
    "summary": "Sony has been scaling down its digitial store for a few years."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/06/ozone-damage-could-have-been-detected-decades-earlier/",
    "domain": "大厂 AI 动态",
    "title": "Ozone loss was a thing even before CFCs were widely used",
    "url": "https://arstechnica.com/science/2026/06/ozone-damage-could-have-been-detected-decades-earlier/",
    "source": "Scott K. Johnson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T19:00:23+00:00",
    "summary": "With today’s scientific tools, the problem could have been spotted in the 1950s."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/06/google-warns-eus-plans-to-weaken-its-monopoly-could-expose-user-data/",
    "domain": "大厂 AI 动态",
    "title": "Google warns EU's plans to weaken its monopoly could expose user data",
    "url": "https://arstechnica.com/gadgets/2026/06/google-warns-eus-plans-to-weaken-its-monopoly-could-expose-user-data/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T18:21:31+00:00",
    "summary": "The EU wants Google to share search data with competitors and open up AI on Android, but Google alleges major privacy risks."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/06/quera-promises-thousands-of-error-corrected-qubits-by-2029/",
    "domain": "大厂 AI 动态",
    "title": "Quantum computing startup says it will leapfrog everybody",
    "url": "https://arstechnica.com/science/2026/06/quera-promises-thousands-of-error-corrected-qubits-by-2029/",
    "source": "John Timmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T17:59:50+00:00",
    "summary": "But the system would require a massive leap from any of its existing hardware."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/06/kalshi-sues-illinois-over-new-tax-on-prediction-market-sports-bets/",
    "domain": "大厂 AI 动态",
    "title": "Kalshi sues Illinois over new tax on prediction market sports bets",
    "url": "https://arstechnica.com/tech-policy/2026/06/kalshi-sues-illinois-over-new-tax-on-prediction-market-sports-bets/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T17:48:11+00:00",
    "summary": "Illinois now a key battleground in fight over prediction market sports bets."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/06/f1-in-austria-starts-off-exciting-then-does-the-opposite/",
    "domain": "大厂 AI 动态",
    "title": "F1 in Austria: Starts off exciting, then goes the opposite way",
    "url": "https://arstechnica.com/cars/2026/06/f1-in-austria-starts-off-exciting-then-does-the-opposite/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T16:04:52+00:00",
    "summary": "A heatwave, engine upgrades, plus power levels for the next two seasons."
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/06/wildwood-featurette-lifts-the-veil-on-building-its-stop-motion-world/",
    "domain": "大厂 AI 动态",
    "title": "Wildwood featurette lifts the veil on building its stop-motion world",
    "url": "https://arstechnica.com/culture/2026/06/wildwood-featurette-lifts-the-veil-on-building-its-stop-motion-world/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T15:43:50+00:00",
    "summary": "Director Travis Knight is also the creative mind behind 2016's Oscar-nominated Kubo and the Two Strings."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/06/in-a-bold-move-rocket-lab-acquires-iridium-communications/",
    "domain": "大厂 AI 动态",
    "title": "In a bold move, Rocket Lab acquires Iridium Communications",
    "url": "https://arstechnica.com/space/2026/06/in-a-bold-move-rocket-lab-acquires-iridium-communications/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T15:33:54+00:00",
    "summary": "\"We believe this will be one of the most transformative deals in the space industry.\""
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/06/think-tank-games-out-how-to-respond-to-disaster-scenarios-in-space-warfare/",
    "domain": "大厂 AI 动态",
    "title": "Think tank games out how to respond to disaster scenarios in space warfare",
    "url": "https://arstechnica.com/space/2026/06/think-tank-games-out-how-to-respond-to-disaster-scenarios-in-space-warfare/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T15:21:40+00:00",
    "summary": "\"Where does the threshold live that an action necessitates some proportional reaction?\""
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/06/comcast-is-splitting-its-media-and-broadband-properties/",
    "domain": "大厂 AI 动态",
    "title": "Comcast is splitting its media and broadband properties",
    "url": "https://arstechnica.com/tech-policy/2026/06/comcast-is-splitting-its-media-and-broadband-properties/",
    "source": "Oliver Barnes and Daniel Thomas, Financial Times",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T13:25:41+00:00",
    "summary": "NBCUniversal and Sky will be spun off into separate companies."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/06/nasas-x-59-frankenjet-tests-supersonic-flight-without-the-sonic-boom/",
    "domain": "大厂 AI 动态",
    "title": "NASA's X-59 \"frankenjet\" tests supersonic flight without the sonic boom",
    "url": "https://arstechnica.com/gadgets/2026/06/nasas-x-59-frankenjet-tests-supersonic-flight-without-the-sonic-boom/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T10:30:36+00:00",
    "summary": "NASA’s quiet supersonic flight tests could eventually go on a national tour."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/06/why-did-this-journal-retract-two-1940s-papers-by-max-planck/",
    "domain": "大厂 AI 动态",
    "title": "Why did this journal retract two 1940s papers by Max Planck?",
    "url": "https://arstechnica.com/science/2026/06/why-did-this-journal-retract-two-1940s-papers-by-max-planck/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T18:49:21+00:00",
    "summary": "Clicking on the links now reveals blank pages and empty PDFs. \"Intellectually, it’s not acceptable.”"
  },
  {
    "id": "rss:https://www.producthunt.com/products/crest-3",
    "domain": "大厂 AI 动态",
    "title": "Crest",
    "url": "https://www.producthunt.com/products/crest-3",
    "source": "zack",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T19:50:38+00:00",
    "summary": "System stats and translation on your Mac's notch Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/readhere-2",
    "domain": "大厂 AI 动态",
    "title": "ReadHere",
    "url": "https://www.producthunt.com/products/readhere-2",
    "source": "Quazi Marufur Rahman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T17:22:17+00:00",
    "summary": "Lightweight PDF & EPUB reader in your browser Discussion | Link"
  },
  {
    "id": "rss:https://36kr.com/p/3875120747942913?f=rss",
    "domain": "大厂 AI 动态",
    "title": "成立9个月，在手订单4.4亿，「谱星航天」连续完成两轮数亿元融资｜36氪首发",
    "url": "https://36kr.com/p/3875120747942913?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T03:39:04+00:00",
    "summary": "文&nbsp;|&nbsp;阿至 光谱定量遥感赛道跑出一匹黑马。 36氪未来产业独家获悉，光学载荷与微纳卫星系统解决方案提供商上海谱星航天科技有限公司（下简称“谱星航天”）已于近期连续完成天使+、Pre-A两轮融资，累计规模为数亿元。 Pre-A轮由国泰海通、尚融资本、司南基金联合领投，徐汇资本、联融志道、金浦投资跟投，老股东联想控股、鼎农科技、普华资本追投。天使+轮投资方为联想控股、普华资本。 "
  },
  {
    "id": "wscn:3775833",
    "domain": "股票",
    "title": "工信部人士：加大富锂锰基正极、硅基负极、固态电解质等材料攻关",
    "url": "https://wallstreetcn.com/articles/3775833",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T07:00:20+00:00",
    "summary": "工信部官员在动力电池论坛释放重磅信号：全力攻克全固态电池、高比能锂离子电池等关键技术，同时剑指行业\"内卷\"——加强产能预警、推动优质优价竞争秩序、防范内卷外化。官方还明确将深化跨国合作，共同推动全球动力电池产业发展。"
  },
  {
    "id": "wscn:3775825",
    "domain": "股票",
    "title": "科创板首只万亿股，寒武纪凭什么？",
    "url": "https://wallstreetcn.com/articles/3775825",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T06:58:37+00:00",
    "summary": "寒武纪盘中大涨超8%，股价触及1613元，总市值突破1.01万亿元，成科创板首只万亿股，已超过了大摩基准情景下1528元的目标价。公司一季度营收28.85亿元，扣非净利润激增238.56%至9.34亿元，现金流转正。高盛、大摩看好大厂订单密集交付及供应链稳定，分别调高目标价至2406元和1528元，但373倍动态市盈率引发估值争议。"
  },
  {
    "id": "wscn:3775830",
    "domain": "股票",
    "title": "日元跌破162，日本财长措辞克制、干预信号或暂未升温",
    "url": "https://wallstreetcn.com/articles/3775830",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T06:47:10+00:00",
    "summary": "日元创1986年以来最低水平，日本财长虽重申准备采取行动，但措辞克制，未主动释放强硬干预信号，与4月干预前的紧急警告形成明显对比。这表明直接入市干预的门槛或尚未触及，政策信号未随汇率下跌而升级，市场仍在试探实际干预的触发条件。"
  },
  {
    "id": "wscn:3775737",
    "domain": "股票",
    "title": "Switch交换芯片：AI组网革新的\"第三核心硬件\"，国产替代能否破局？",
    "url": "https://wallstreetcn.com/premium/articles/3775737?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T06:42:23+00:00",
    "summary": "全球以太网交换机市场收入达551亿美元，同比增长31.5%，其中数据中心交换机收入达325亿美元，同比增长53.5%。AI训练与推理对超低延迟、高带宽互联的需求急剧上升，正直接带动Switch产品量价齐升。"
  },
  {
    "id": "wscn:3775824",
    "domain": "股票",
    "title": "失守4000关口！黄金月内累计跌超12%，高盛：牛市还没完",
    "url": "https://wallstreetcn.com/articles/3775824",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T06:05:53+00:00",
    "summary": "现货黄金周二盘中最低触及3943美元，为去年11月以来最低日内水平，月内迄今累计下跌约12.4%，主因伊朗战争后能源飙升加剧通胀，推高美联储加息预期及美元指数。然而高盛力挺黄金，维持年末4900美元目标价不变，强调新兴市场央行结构性增持与财政隐忧长期利好不变。"
  },
  {
    "id": "wscn:3775823",
    "domain": "股票",
    "title": "智谱万亿，该重估MiniMax了",
    "url": "https://wallstreetcn.com/articles/3775823",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T05:41:17+00:00",
    "summary": "智谱与MiniMax估值差达7倍，源于市场暂以Coding能力为核心定价锚。但Coding壁垒短，MiniMax正快速追赶；且其在毛利高、变现快的视频生成领域的价值尚未被定价。随着大模型估值体系成熟与校准，MiniMax亟待价值重估。"
  },
  {
    "id": "wscn:3775502",
    "domain": "股票",
    "title": "AI驱动全球模拟芯片结构性复苏，为什么这轮国产替代比以往更值得关注？",
    "url": "https://wallstreetcn.com/premium/articles/3775502?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T05:28:41+00:00",
    "summary": "中国模拟芯片行业进入“AI带来行业总需求扩张+全球龙头聚焦高端市场+国内企业加速进口替代”三重驱动共同作用的新阶段。"
  },
  {
    "id": "wscn:3775821",
    "domain": "股票",
    "title": "杠杆下的科技牛市：杠杆链条逼近极限，韩国或成为场系统性风险新震源",
    "url": "https://wallstreetcn.com/articles/3775821",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T05:17:10+00:00",
    "summary": "高盛表示，以韩国为核心的亚洲市场对科技与存储股的无止境杠杆需求，推动标普500指数总收益期货融资利率飙升至历史高位，KOSPI呈现自我强化反馈回路。杠杆ETF与TRS使经销商敞口接近饱和，一旦融资成本触发临界点引致流动性骤紧，将引发系统性去杠杆和资产中断断崖式下跌。"
  },
  {
    "id": "wscn:3775809",
    "domain": "股票",
    "title": "颠覆VC常识！Benchmark合伙人：AI时代的投资估值新模式",
    "url": "https://wallstreetcn.com/articles/3775809",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T04:07:20+00:00",
    "summary": "Benchmark合伙人Ev Randle指出，在全新的P×Q×M估值模型中，AI公司虽毛利偏低，但凭借按需提供“数字劳动力”的能力，客单价正呈指数级飙升，如开发者年均AI工具花费可达3.6万美元。与此同时，市场正面临推理算力的“瀑布式”需求爆发，以及前沿模型与开源模型之间的“数万亿美元定价权之争”。"
  },
  {
    "id": "wscn:3775807",
    "domain": "股票",
    "title": "创业板大涨3%，寒武纪市值破万亿，光模块、玻璃基板爆发，MLCC龙头跌停，恒科指涨超1%",
    "url": "https://wallstreetcn.com/articles/3775807",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T04:05:44+00:00",
    "summary": "盘面上，个股涨跌互现，全市场超2700只个股上涨，超百股涨停。量能明显萎缩，上午半天成交2.12万亿。沪深两市半日成交额2.1万亿，较上个交易日缩量近4000亿。板块方面，CPO、光纤概念股再度爆发，培育钻石、人形机器人、消费电子、光刻机、存储器、稀土永磁、固态电池概念股活跃；煤炭、黄金、银行、保险、医药、白酒、电力板块走弱。"
  },
  {
    "id": "wscn:3775819",
    "domain": "股票",
    "title": "央行月末操作“一增一减”：隔夜逆回购翻倍至6000亿，精准熨平跨季资金面",
    "url": "https://wallstreetcn.com/articles/3775819",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T03:54:13+00:00",
    "summary": "6月30日，央行将隔夜逆回购操作规模从前一日的3000亿元大幅加码至6000亿元，实现规模翻倍；与此同时，7天期逆回购操作规模则从1575亿元缩减至695亿元。这“一增一减”的操作，向市场传递了精准呵护短期资金面、同时避免资金过度淤积的明确信号。"
  },
  {
    "id": "wscn:3775817",
    "domain": "股票",
    "title": "韩国800万亿韩元砸存储，影响有多大？",
    "url": "https://wallstreetcn.com/articles/3775817",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T03:53:09+00:00",
    "summary": "韩国政府宣布在西南地区新建存储芯片集群，三星披露2450万亿韩元国内长期投资计划，标志着韩国半导体产业迎来数十年最大扩张。美银证券与高盛均指出，受基建与投产周期制约，新产能最早需8至10年后方能实质影响全球供给，短期供需格局不变。"
  },
  {
    "id": "wscn:3775818",
    "domain": "股票",
    "title": "本末动力通过港交所聆讯，专注机器人动力模块",
    "url": "https://wallstreetcn.com/articles/3775818",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T03:34:28+00:00",
    "summary": "核心业务自我造血路径初显。"
  },
  {
    "id": "wscn:3775748",
    "domain": "股票",
    "title": "半导体扩产超级周期“黄金窗口”：材料与设备的万亿拐点红利",
    "url": "https://wallstreetcn.com/premium/articles/3775748?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T03:16:16+00:00",
    "summary": "三星、SK海力士正开启存储芯片领域史无前例的扩产浪潮，全球存储资本开支2026/2027年预计分别达1103亿和1685亿美元，同比增长63%/53%。"
  },
  {
    "id": "wscn:3775814",
    "domain": "股票",
    "title": "字节梁汝波发布全员邮件  强调AI时代的新领导力原则",
    "url": "https://wallstreetcn.com/articles/3775814",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T03:07:00+00:00",
    "summary": "要求Leader实质产出。"
  },
  {
    "id": "wscn:3775810",
    "domain": "股票",
    "title": "Rubin缩水背后，英伟达的CUDA神话正在松动",
    "url": "https://wallstreetcn.com/articles/3775810",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T03:04:06+00:00",
    "summary": "英伟达的产品迭代速度，正在撞上物理极限的墙。 更大的芯片→更复杂的封装→更高的缺陷率→要么延迟、要么缩水。这是一条不能无限延伸的曲线。而与此同时，竞争对手们正在用另一种方式绕过这面墙：不做更大的芯片，做更专用的芯片。"
  },
  {
    "id": "wscn:3775811",
    "domain": "股票",
    "title": "立讯精密正式启动H股全球发售，最高募资31亿美元，预计7月9日上市",
    "url": "https://wallstreetcn.com/articles/3775811",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T02:58:56+00:00",
    "summary": "苹果核心供应商立讯精密于6月30日正式启动H股全球发售，拟发行约3.835亿股，最高发售价每股63.28港元，募资净额约240亿港元（约31亿美元），预计7月9日在港交所挂牌。募资资金主要用于扩产、研发及产业链并购。公司2025年营收达3323亿元，汽车电子业务占比快速提升。"
  },
  {
    "id": "wscn:3775808",
    "domain": "股票",
    "title": "美银中国机构调研：对中概互联网低迷“感到无力”，对AI模型“尚难判断赢家”，字节是巨大威胁",
    "url": "https://wallstreetcn.com/articles/3775808",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T02:55:56+00:00",
    "summary": "美银美林最新调研揭示，\"无力感\"成为香港及内地机构对话的高频词，投资者陷入\"估值已低却不敢买入\"的困境，多数机构拒绝以超15倍市盈率介入任何中国互联网股票。此外，AI模型竞争格局混沌，市场竞争极为激烈，现阶段断言最终赢家为时尚早，字节跳动在AI及云计算布局令竞争威胁升级。"
  },
  {
    "id": "wscn:3775803",
    "domain": "股票",
    "title": "高盛6月DRAM调查：大幅上调HBM2027年价格预期",
    "url": "https://wallstreetcn.com/articles/3775803",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T02:35:38+00:00",
    "summary": "高盛6月DRAM情绪调查维持温和正面，最大增量信息是将三星2027年HBM价格增长预期从+14%大幅上调至+44%，并认为仍有上行空间。与此同时，DDR5现货价格自5月初上涨20%，韩国5月DRAM出口同比暴增370%再创历史新高，产业链景气度全面走强，AI算力需求持续成为核心驱动力。"
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
    "id": "rss:https://arxiv.org/abs/2606.28706",
    "domain": "金融",
    "title": "Balancing Shareholder Value and Financial Stability under a Reduced-Form Liquidation Model",
    "url": "https://arxiv.org/abs/2606.28706",
    "source": "Benjamin Avanzi, Bernard Wong, Jinxia Zhu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T04:00:00+00:00",
    "summary": "arXiv:2606.28706v1 Announce Type: new Abstract: Modern resolution and prudential regimes increasingly wind up a distressed firm not at a single hard threshold but through a graduated, state-dependent "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.28891",
    "domain": "金融",
    "title": "Hedging Maturity-Specific Risk in Forward Curve Derivatives under Stochastic Volatility",
    "url": "https://arxiv.org/abs/2606.28891",
    "source": "Riccardo Alberti, Sven Karbach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T04:00:00+00:00",
    "summary": "arXiv:2606.28891v1 Announce Type: new Abstract: We study the variance-optimal hedging of European contingent claims written on forwards. We assume that the dynamics of the underlying forward curves fo"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.28919",
    "domain": "金融",
    "title": "Topping Up and Optimal Redistribution",
    "url": "https://arxiv.org/abs/2606.28919",
    "source": "Zi Yang Kang, Mitchell Watt",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T04:00:00+00:00",
    "summary": "arXiv:2606.28919v1 Announce Type: new Abstract: This paper studies how topping up -- allowing recipients of in-kind transfers to supplement subsidized consumption in a private market -- affects optima"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.28990",
    "domain": "金融",
    "title": "The Fundamental Theorem of Asset Pricing, Formalized in Lean 4",
    "url": "https://arxiv.org/abs/2606.28990",
    "source": "Raphael Coelho",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T04:00:00+00:00",
    "summary": "arXiv:2606.28990v1 Announce Type: new Abstract: The Fundamental Theorem of Asset Pricing states that a market is free of arbitrage exactly when it admits an equivalent martingale measure. We formalize"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.29056",
    "domain": "金融",
    "title": "Green Transformational Leadership and Sustainable Nursing Practices: Evidence from the Healthcare Sector",
    "url": "https://arxiv.org/abs/2606.29056",
    "source": "Thabit Atobishi, Saeed Nosratabadi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T04:00:00+00:00",
    "summary": "arXiv:2606.29056v1 Announce Type: new Abstract: The healthcare sector contributes approximately 4.4% of global greenhouse gas emissions, yet research on the organizational determinants of sustainable "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.29227",
    "domain": "金融",
    "title": "The Human-Machine Knowledge Spiral",
    "url": "https://arxiv.org/abs/2606.29227",
    "source": "Aaron Chatterji, Daniel Rock, Eduard Talamas",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T04:00:00+00:00",
    "summary": "arXiv:2606.29227v1 Announce Type: new Abstract: Nonaka emphasized that innovation is the result of a continuous back-and-forth between tacit and explicit knowledge. Artificial intelligence introduces "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.29290",
    "domain": "金融",
    "title": "Supply Chain Propagation of Textual Signals: LLM Embeddings and Cross-Sectional Return Predictability",
    "url": "https://arxiv.org/abs/2606.29290",
    "source": "Asef Y{\\i}lk{\\i}",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T04:00:00+00:00",
    "summary": "arXiv:2606.29290v1 Announce Type: new Abstract: This paper proposes a novel asset pricing framework that augments large language model (LLM) embeddings of annual report disclosures with supply chain k"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.29299",
    "domain": "金融",
    "title": "Bayesian Optimization on the Equilibrium Manifold",
    "url": "https://arxiv.org/abs/2606.29299",
    "source": "Felix Kubler",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T04:00:00+00:00",
    "summary": "arXiv:2606.29299v1 Announce Type: new Abstract: Computing optimal policy in heterogeneous-agent economies is complicated by the possibility of multiple equilibria. We overcome this difficulty by showi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.29406",
    "domain": "金融",
    "title": "Adaptive AI Delegation under Uncertainty: A Bayesian Governance Policy for Sequential Decision Authority",
    "url": "https://arxiv.org/abs/2606.29406",
    "source": "Matthew Francis Dixon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T04:00:00+00:00",
    "summary": "arXiv:2606.29406v1 Announce Type: new Abstract: Organizations increasingly use large language models and agentic AI systems to generate probabilistic assessments and candidate actions in high-conseque"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.29572",
    "domain": "金融",
    "title": "Valuation Reveals Uncertainty",
    "url": "https://arxiv.org/abs/2606.29572",
    "source": "Jongjin Park, Hyungbin Park",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T04:00:00+00:00",
    "summary": "arXiv:2606.29572v1 Announce Type: new Abstract: This paper studies the recovery of uncertainty from dynamic sublinear valuation rules. A robust valuation assigns each payoff its worst-case expected va"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.29591",
    "domain": "金融",
    "title": "The Bounce Has No Direction: Sign, Magnitude, and the Microstructure of Equity Return Predictability",
    "url": "https://arxiv.org/abs/2606.29591",
    "source": "Victoria Portnaya",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T04:00:00+00:00",
    "summary": "arXiv:2606.29591v1 Announce Type: new Abstract: SPY's lag-1 return autocorrelation ($\\hat\\rho(1)=-0.081$, $z=-7.4$) is among the most significant regularities in empirical equity finance, yet the stan"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.30070",
    "domain": "金融",
    "title": "Financial Resilience Evaluation: From Conditional Expectations to Dynamic Convex Risk Measures",
    "url": "https://arxiv.org/abs/2606.30070",
    "source": "Matteo Ferrari, Roger J. A. Laeven, Emanuela Rosazza Gianin, Marco Zullino",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T04:00:00+00:00",
    "summary": "arXiv:2606.30070v1 Announce Type: new Abstract: Financial resilience concerns the rate at which a position recovers, or further deteriorates, in response to adverse conditions. As a first step, Laeven"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.30193",
    "domain": "金融",
    "title": "Hidden Dependence and Aggregate Tail Risk",
    "url": "https://arxiv.org/abs/2606.30193",
    "source": "Corrado De Vecchi, Max Nendel, Steven Vanduffel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T04:00:00+00:00",
    "summary": "arXiv:2606.30193v1 Announce Type: new Abstract: We study risk aggregation problems for arbitrary non-decreasing aggregation functions and tail risk measures under dependence uncertainty in a distribut"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.30363",
    "domain": "金融",
    "title": "Strategic Risk Reduction: Self-Protection and Self-Insurance",
    "url": "https://arxiv.org/abs/2606.30363",
    "source": "Wing Fung Chong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T04:00:00+00:00",
    "summary": "arXiv:2606.30363v1 Announce Type: new Abstract: This paper studies how a risk holder should combine self-protection and self-insurance when market insurance is absent. In a Bernoulli loss model, self-"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.30381",
    "domain": "金融",
    "title": "Bank Earnings, Credit Supply & the Macroeconomy: Evidence from Canada",
    "url": "https://arxiv.org/abs/2606.30381",
    "source": "Santiago Camara, Sanaa Latif",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T04:00:00+00:00",
    "summary": "arXiv:2606.30381v1 Announce Type: new Abstract: This paper studies whether news about banks' balance sheets propagates to aggregate financial conditions and macroeconomic activity. We construct high-f"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.30470",
    "domain": "金融",
    "title": "Swimming in Dark Water: When Cartels Mimic Competition",
    "url": "https://arxiv.org/abs/2606.30470",
    "source": "David Imhof, Thierry Madi\\`es, Martin Huber",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T04:00:00+00:00",
    "summary": "arXiv:2606.30470v1 Announce Type: new Abstract: This paper analyzes the internal organization and economic effects of a bid-rigging cartel in the road construction sector of the Swiss canton of Ticino"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.28869",
    "domain": "金融",
    "title": "A General Theory of Paths: Signatures, Jump Lifts, and Expected Signatures of Self-Exciting Processes",
    "url": "https://arxiv.org/abs/2606.28869",
    "source": "Miquel Noguer i Alonso",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T04:00:00+00:00",
    "summary": "arXiv:2606.28869v1 Announce Type: cross Abstract: This paper develops a path-first theory using the signature as a universal coordinate for deterministic paths, rough paths, jump streams, and path-val"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.29018",
    "domain": "金融",
    "title": "Liquidity-Based Audit of Algorithmic Trading Strategies",
    "url": "https://arxiv.org/abs/2606.29018",
    "source": "Irene Aldridge",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T04:00:00+00:00",
    "summary": "arXiv:2606.29018v1 Announce Type: cross Abstract: We show that net demand for liquidity by algo strategies is identifiable from its trade and price history alone, with no knowledge of its signal or op"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.29143",
    "domain": "金融",
    "title": "Comonotonic and moment matching approximations for sums of lognormal random variables",
    "url": "https://arxiv.org/abs/2606.29143",
    "source": "Chunle Huang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T04:00:00+00:00",
    "summary": "arXiv:2606.29143v1 Announce Type: cross Abstract: In this paper, based on the concept of weighted distribution, we introduce a kind of new approximations for sums of lognormal random variables, such t"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.29251",
    "domain": "金融",
    "title": "When Summaries Distort Decisions: Information Fidelity in LLM-Compressed Financial Analysis",
    "url": "https://arxiv.org/abs/2606.29251",
    "source": "Hoyoung Lee, Suhwan Park, Seunghan Lee, Jun Seo, Jaehoon Lee, Sungdong Yoo, Minjae Kim, CheolWon Na, Zhangyang Wang, Zach Golkhou, Minkyu Kim, Sotirios Sabanis, Alejandro Lopez-Lira, Dhagash Mehta, Soonyoung Lee, Chanyeol Choi, Wonbin Ahn, Yongjae Lee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T04:00:00+00:00",
    "summary": "arXiv:2606.29251v1 Announce Type: cross Abstract: Financial decision-makers face more information than they can directly inspect, making context compression necessary. Yet when large language models ("
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.29771",
    "domain": "金融",
    "title": "CLQT: A Closed-Loop, Cost-Aware, Strategy-Consistent Benchmark for Diagnostic Evaluation of LLM Portfolio-Management Agents",
    "url": "https://arxiv.org/abs/2606.29771",
    "source": "Bo Qu, Mingguang Chen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T04:00:00+00:00",
    "summary": "arXiv:2606.29771v1 Announce Type: cross Abstract: LLM agents are increasingly cast as autonomous portfolio managers, and benchmarks have moved from financial question-answering to sequential trading. "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.29793",
    "domain": "金融",
    "title": "Fund2Persona: A Framework for Building and Refining Financial Advisor Personas from Fund Disclosure Data",
    "url": "https://arxiv.org/abs/2606.29793",
    "source": "Suhwan Park, Hoyoung Lee, Zhangyang Wang, Alejandro Lopez-Lira, Young Cha, Chanyeol Choi, Jaewon Choi, Yongjae Lee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T04:00:00+00:00",
    "summary": "arXiv:2606.29793v1 Announce Type: cross Abstract: Demand for personalized financial advising is growing, but consistent advisor expertise is difficult to obtain, scale, and encode in LLM systems. Simp"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.30037",
    "domain": "金融",
    "title": "Heads, Not Backbones: Output Heads Dominate Architectures on Fat-Tailed Returns",
    "url": "https://arxiv.org/abs/2606.30037",
    "source": "Sichao He, Yansong Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T04:00:00+00:00",
    "summary": "arXiv:2606.30037v1 Announce Type: cross Abstract: In a deep forecasting pipeline for fat-tailed financial returns at short horizons, which matters more - the backbone architecture or the output head? "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.30085",
    "domain": "金融",
    "title": "Not-quite-human tastes: the stylized omnivorousness of LLM survey surrogates",
    "url": "https://arxiv.org/abs/2606.30085",
    "source": "Xiangyu Ma, Mengmi Zhang, Shannon Ang, Minne Chen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T04:00:00+00:00",
    "summary": "arXiv:2606.30085v1 Announce Type: cross Abstract: Large-language models have proven to be remarkable if inconsistent parrots of public attitudes and opinions. The extent to which LLMs are able to prod"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.30359",
    "domain": "金融",
    "title": "Decision-support strategies for photovoltaic self-consumption under declining electricity prices and limited remuneration of surplus generation",
    "url": "https://arxiv.org/abs/2606.30359",
    "source": "Ana B. Crist\\'obal (0000-0002-4314-6160), Daniel Sierra (0000-0002-6289-7605), Laura Palomino (0000-0002-6289-7605), Luis Miguel Carrasco (0000-0002-6289-7605), Luis Narvarte (0000-0002-6289-7605)",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T04:00:00+00:00",
    "summary": "arXiv:2606.30359v1 Announce Type: cross Abstract: The success of distributed photovoltaics may be undermining its own future. As solar penetration increases, electricity prices decline during periods "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.30473",
    "domain": "金融",
    "title": "Field Order Should Not Matter: Permutation-Invariant Embedding Model Fine-Tuning for Structured Metadata Retrieval",
    "url": "https://arxiv.org/abs/2606.30473",
    "source": "Aivin V. Solatorio, Olivier Dupriez, Rafael Macalaba",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T04:00:00+00:00",
    "summary": "arXiv:2606.30473v1 Announce Type: cross Abstract: We study retrieval over catalogs of structured metadata, where each record is a small schema whose fields answer different kinds of query. Embedding a"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.30583",
    "domain": "金融",
    "title": "AI Premium",
    "url": "https://arxiv.org/abs/2606.30583",
    "source": "Nicola Borri, Yukun Liu, Aleh Tsyvinski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T04:00:00+00:00",
    "summary": "arXiv:2606.30583v1 Announce Type: cross Abstract: Using 380 trillion tokens of realized AI consumption across more than four hundred large language models from the licensed proprietary OpenRouter data"
  },
  {
    "id": "rss:https://arxiv.org/abs/2107.01730",
    "domain": "金融",
    "title": "Asymptotic Analysis of Risk Premia Induced by Law-Invariant Risk Measures",
    "url": "https://arxiv.org/abs/2107.01730",
    "source": "Thomas Knispel, Roger J. A. Laeven, Gregor Svindland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T04:00:00+00:00",
    "summary": "arXiv:2107.01730v2 Announce Type: replace Abstract: We analyze the limiting behavior of the risk premium associated with the Pareto optimal risk sharing contract in an infinitely expanding pool of ris"
  },
  {
    "id": "rss:https://arxiv.org/abs/2402.06635",
    "domain": "金融",
    "title": "Large and Deep Factor Models",
    "url": "https://arxiv.org/abs/2402.06635",
    "source": "Bryan Kelly, Boris Kuznetsov, Semyon Malamud, Yuan Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T04:00:00+00:00",
    "summary": "arXiv:2402.06635v3 Announce Type: replace Abstract: We show that a deep neural network (DNN) trained to construct a stochastic discount factor (SDF) admits an additive decomposition separating nonline"
  }
]
```
