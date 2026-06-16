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

- 今日日期：`2026-06-16`
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
  "date": "2026-06-16",
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
    "points": 3188621,
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
    "points": 1168874,
    "published_at": "2026-03-14T14:22:56+00:00",
    "summary": "AI 核心概念大串联：LLM, Token, Context, Context Window, Prompt, User Prompt, System Prompt, Tool, MCP, Agent, Agent Skill，一期视频带你打通 AI 底层逻辑！"
  },
  {
    "id": "bvid:BV1NvRyBzEhq",
    "domain": "AI",
    "title": "全网最全！60分钟全面掌握Claude Code～【附完整文档】",
    "url": "http://www.bilibili.com/video/av116522328524431",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 1160385,
    "published_at": "2026-05-05T14:08:25+00:00",
    "summary": "Claude Code保姆级教学【收藏起来不会错！】\n从上手安装，到高级用法，这期一次讲全～\n花了三周做教程，希望能帮到你嘻嘻，感谢朋友们的三连+关注啦～"
  },
  {
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "9分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 1145618,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1yorUYWEGD",
    "domain": "AI",
    "title": "普通人也可以看的 AI 编程指南 | Cursor 教程｜Cursor 使用技巧和思路｜如何免费使用 Cursor｜AI 编程",
    "url": "http://www.bilibili.com/video/av113786467981446",
    "source": "不正经的前端啊",
    "platform": "bilibili",
    "points": 938296,
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
    "points": 838876,
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
    "points": 698622,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1aDMezREUj",
    "domain": "AI",
    "title": "Cursor使用教程，2小时玩转cursor，cursor无限续杯",
    "url": "http://www.bilibili.com/video/av114691716154833",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 572344,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV1AnQNYxEsy",
    "domain": "AI",
    "title": "MCP是啥？技术原理是什么？一个视频搞懂MCP的一切。Windows系统配置MCP，Cursor Cline使用MCP",
    "url": "http://www.bilibili.com/video/av114155298228756",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 414182,
    "published_at": "2025-03-13T13:18:09+00:00",
    "summary": "MCP是近期的AI领域的热点，特别是在海外社区获得热烈讨论，每天都有大量MCP工具诞生。本期视频我们从MCP的概念，技术原理，到多场景实战，一个视频看懂MCP的全部内容。\n\n\nMCP官方开源仓库：https://github.com/modelcontextprotocol/servers\nMCP合集网站：  https://smithery.ai/\nVscode下载：https://code.v"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 410870,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1eK5DzHEWu",
    "domain": "AI",
    "title": "MCP实战指南，mcp视频教程，2小时学透mcp",
    "url": "http://www.bilibili.com/video/av114380213586544",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 372562,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1Yi5M6DERk",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116560144369496",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 324385,
    "published_at": "2026-05-12T06:24:19+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1jp5s6vE3P",
    "domain": "AI",
    "title": "【全36集】吊打付费！“即梦+豆包+剪映”快速掌握AI视频制作技巧，手把手教你从0到1制作AI短片！AI视频生成零基础入门保姆级教程 教你玩转AI影视赛道！",
    "url": "http://www.bilibili.com/video/av116554289191849",
    "source": "AIGC视频制作教学",
    "platform": "bilibili",
    "points": 312567,
    "published_at": "2026-05-11T05:41:29+00:00",
    "summary": "持续更新中~评论区获取课程资料哟~求一键三连~谢谢各位观众老爷！！！！"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 312412,
    "published_at": "2026-06-09T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“VibeCoding”免费获取\n【课程简介】从零开始，用自然语言指挥AI开发真实软件项目！"
  },
  {
    "id": "bvid:BV1cpEd66EjT",
    "domain": "AI",
    "title": "Claude Fable 5 首发实测，真是太烧了。。完爆 GPT 5.5！",
    "url": "http://www.bilibili.com/video/av116725718717656",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 300250,
    "published_at": "2026-06-10T12:11:13+00:00",
    "summary": "全球最贵的 AI 模型 Claude Fable 5 来了！这期视频带你看看它到底值不值，用两轮硬核实测对比 Fable 5、Opus 4.8 和 GPT-5.5 的 AI 编程能力。\n开源 AI 编程教程：github.com/liyupi/ai-guide\n编程学习教程+实战项目+简历模板：codefather.cn\n视频先带你了解 Claude Fable 5 的核心更新，包括 Fable "
  },
  {
    "id": "bvid:BV1FuXpBcEuo",
    "domain": "AI",
    "title": "Comfyui工作流从零基础到精通（2026新手入门实用版comfyui教程）详细从零开始学习comfyui工作流搭建，全程干货无废话！AI绘画AI视频生成",
    "url": "http://www.bilibili.com/video/av116294712102434",
    "source": "ComfyUl官方教学",
    "platform": "bilibili",
    "points": 245349,
    "published_at": "2026-03-26T09:21:12+00:00",
    "summary": "视频中的整合包以及up整理的AI绘画全套籽料包敲【7】全部抱走哦～只求换大家的一个[热词系列_三连]\n大家不要白嫖啊(┯_┯)，一个小小的赞也可谢谢了"
  },
  {
    "id": "bvid:BV1AHDuBoE2S",
    "domain": "AI",
    "title": "锐评vibe coding工具“从夯到拉”",
    "url": "http://www.bilibili.com/video/av116347090502349",
    "source": "布鲁歇一歇",
    "platform": "bilibili",
    "points": 242329,
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
    "points": 235996,
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
    "points": 216983,
    "published_at": "2025-04-15T00:59:13+00:00",
    "summary": "MCP终极指南 - 带你深入掌握MCP（基础篇）\n\n时间轴：\n01:05 MCP简要介绍\n02:47 安装 MCP Host（Cline）\n03:15 配置 Cline 用的 API Key\n06:01 第一个 MCP 问题\n06:31 概念解释：MCP Server 和 Tool\n09:13 配置 MCP Server\n14:19 使用 MCP Server\n15:24 MCP 交互流程详解\n1"
  },
  {
    "id": "bvid:BV1h4DkBaEu1",
    "domain": "AI",
    "title": "Claude Code、Codex (ChatGPT)、Cursor该怎么选？Max/Pro/Ultra Plan亲身经验分享",
    "url": "http://www.bilibili.com/video/av116385829095069",
    "source": "HexUp",
    "platform": "bilibili",
    "points": 178043,
    "published_at": "2026-04-11T11:37:54+00:00",
    "summary": "Claude Code、Cursor、ChatGPT——编程 Agent 怎么选？                                     \n                                                                                        \n  我目前同时订阅了 Claude Max、Cursor Ult"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 174550,
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
    "points": 156062,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV1b5AeeGEFc",
    "domain": "AI",
    "title": "Cursor太贵？分享三个免费AI编程方案+海量编程技巧【如何看待AI编程】",
    "url": "http://www.bilibili.com/video/av114025056699722",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 155326,
    "published_at": "2025-02-18T13:13:51+00:00",
    "summary": "我试用了几十种AI编程辅助工具，找到了其中三个免费，并且效果最好的方案。 本期视频就来跟大家分享一下。视频中间会穿插很多AI编程工具的使用技巧，还有看待AI编程的一些个人思考。本期视频没有广告都是个人的经验干货，废话不多说我们直接开始。"
  },
  {
    "id": "bvid:BV16NvCBrEVs",
    "domain": "AI",
    "title": "什么是Vibe Coding，以及怎么使用？",
    "url": "http://www.bilibili.com/video/av115797133368973",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 151172,
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
    "points": 143140,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 128941,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1j67k6oENA",
    "domain": "AI",
    "title": "Claude Ultracode 超码 上线 | 操控100个Agent并行开发  保姆级实战教程",
    "url": "http://www.bilibili.com/video/av116697163896598",
    "source": "技术胖",
    "platform": "bilibili",
    "points": 103916,
    "published_at": "2026-06-05T11:05:27+00:00",
    "summary": "Ultracode 功能太好用了，就是Claude Code昨天新出的“超码”功能，如果你Vibe Coding ，那这个技巧一定要掌握。他解决了Claude Code 一次性跑不完大型任务的问题。\n本期视频很长，但看完你的AI Coding能力将超越整个团队。并且把视频内容整理成了文字版，放在评论区，方便你学习使用。视频很干，可以先喝口水润润喉咙。"
  },
  {
    "id": "bvid:BV1fRSfBWE5X",
    "domain": "AI",
    "title": "vlog｜白天上班 晚上vibe coding，准备一个月上架我的第一款App！",
    "url": "http://www.bilibili.com/video/av116357526003120",
    "source": "chocpink_AI版",
    "platform": "bilibili",
    "points": 96869,
    "published_at": "2026-04-06T11:33:25+00:00",
    "summary": "想了很久终于开始了这件事——vibe coding！\n\n下面快速总结了我用到的一些工具：\nApptweak：竞品调研\nfigma make、google stitch、impeccable插件：生成UI页面\nfigma mcp/plugin：连接到cursor\npinterest/小红书/iconfont：找图片/icon素材\nGrok：生图、素材优化\ncursor+Xcode（swift）：落地"
  },
  {
    "id": "bvid:BV1g49KBqE1g",
    "domain": "AI",
    "title": "【Java+大模型】Java AI Agent✚Spring AI✚Spring AI Alibaba Agent Framework整体结构✚Skill！",
    "url": "http://www.bilibili.com/video/av116339758860081",
    "source": "图灵官方",
    "platform": "bilibili",
    "points": 90812,
    "published_at": "2026-04-03T08:15:24+00:00",
    "summary": "整理制作不易，大家记得点个关注，一键三连呀【点赞、收藏、转发】感谢支持~\n配套大模型笔记/AI大模型学习大纲/面试真题自取：https://www.bilibili.com/read/cv39638062/?spm_id_from=333.1387.0.0&amp;jump_opus=1"
  },
  {
    "id": "bvid:BV1RAEz6EE98",
    "domain": "AI",
    "title": "为什么Claude Code+DeepSeekV4是最有性价比的个人AI Agent?",
    "url": "http://www.bilibili.com/video/av116732144392386",
    "source": "呱声一片",
    "platform": "bilibili",
    "points": 87029,
    "published_at": "2026-06-11T15:27:06+00:00",
    "summary": "官方文档地址：https://api-docs.deepseek.com/zh-cn/quick_start/agent_integrations/claude_code"
  },
  {
    "id": "bvid:BV1YP5W6ZEP9",
    "domain": "AI",
    "title": "VibeCoding就该这么做！",
    "url": "http://www.bilibili.com/video/av116552997276199",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 74637,
    "published_at": "2026-05-14T09:00:00+00:00",
    "summary": "UV教程：https://www.bilibili.com/video/BV1Stwfe1E7s/\n代码及知识星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV1HM7C6BEnF",
    "domain": "AI",
    "title": "【B站精选】目前B站最细最全的AI大模型全套教程，2026最新版，包含所有干货！手把手带你从入门到精通！少走99%的弯路！存下吧！真的很难找全的！",
    "url": "http://www.bilibili.com/video/av116696929076767",
    "source": "AIAgent开发",
    "platform": "bilibili",
    "points": 60234,
    "published_at": "2026-06-05T10:11:18+00:00",
    "summary": "【B站精选】目前B站最细最全的AI大模型全套教程，2026最新版，包含所有干货！手把手带你从入门到精通！少走99%的弯路！存下吧！真的很难找全的！"
  },
  {
    "id": "bvid:BV1ZjDYB7Eam",
    "domain": "AI",
    "title": "从 0 到 1：6小时掌握 Vibe Coding！ Claude Code ＋ AI 这支影片直接让你超越 90% AI 玩家",
    "url": "http://www.bilibili.com/video/av116362122894759",
    "source": "李哈利Harry",
    "platform": "bilibili",
    "points": 58065,
    "published_at": "2026-04-08T11:00:00+00:00",
    "summary": "🌟 加入AI大师社群并运用AI创业赚钱：https://www.skool.com/aiagent/about?ref=f2b566934c5c4639aaa47ab1fe39310e\n📌 加入我的免费 Skool 社群，获取模板：https://www.skool.com/aiagent8/about?ref=f2b566934c5c4639aaa47ab1fe39310e\n\n🚧 开始使用 n8"
  },
  {
    "id": "bvid:BV1AbLu6uENH",
    "domain": "AI",
    "title": "全透明！三小时做出你的人生第一个小程序",
    "url": "http://www.bilibili.com/video/av116598815850864",
    "source": "没token的Mav",
    "platform": "bilibili",
    "points": 51917,
    "published_at": "2026-05-19T02:15:03+00:00",
    "summary": "完整微信小程序开发+发布流程"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 51804,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1ZrXLYyEFx",
    "domain": "AI",
    "title": "自己动手写一个MCP Server，你就知道MCP怎么回事了",
    "url": "http://www.bilibili.com/video/av114183114856586",
    "source": "AI橙爆了",
    "platform": "bilibili",
    "points": 49246,
    "published_at": "2025-03-18T11:15:52+00:00",
    "summary": "视频制作不易，请一键三连！私我领取文档源码"
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 35852,
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
    "points": 29677,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 29036,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1bh3LzqEze",
    "domain": "AI",
    "title": "Chatbox AI终端：跨平台+MCP+知识库+开源+免费！一键连接所有AI语言模型！手把手安装使用指南！",
    "url": "http://www.bilibili.com/video/av114793218380950",
    "source": "_Smzh_",
    "platform": "bilibili",
    "points": 27296,
    "published_at": "2025-07-04T10:00:00+00:00",
    "summary": "chatbox官网：https://chatboxai.app\ngithub仓库：https://github.com/chatboxai/chatbox\n\nLM Studio教程：BV1usrLYTEZR\nTGW懒人包部署教程：BV1dVCzYUE7G\n本地语言模型个人推荐：BV1Bb421E7j7"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 24164,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV11K9gBqEnW",
    "domain": "AI",
    "title": "【杀戮尖塔2】AI MOD 配置教程第一期来辣！手把手教你怎么改提示词！以及如何设计自己的爬塔玩法",
    "url": "http://www.bilibili.com/video/av116341654755924",
    "source": "分歧点WhatIf",
    "platform": "bilibili",
    "points": 23274,
    "published_at": "2026-04-03T16:14:43+00:00",
    "summary": "每个参数都是干什么的，如何修改提示词的教程。\n不知道这是什么？请看合集内的视频~\n我做了一个 AI 的杀戮尖塔2MOD！\n可以和怪物对话，策反怪物，带着怪物爬塔（重写了几乎每一个怪物在友方时候的行为），还能给怪物打防御，带个沙虫全吃了！\n可以和上古之民对话，聊嗨了会给你 1～2 个额外赐福，还能帮你指示为未来\n可以让偷窃草蜢偷队友的 key 卡，想无限？偷了！\n可以和商人讨价还价，甚至白嫖\n多人的"
  },
  {
    "id": "bvid:BV188UHYkEdg",
    "domain": "AI",
    "title": "Cursor / Windsurf + Android Studio 高效AI编程：零基础也能开发安卓应用",
    "url": "http://www.bilibili.com/video/av113502647750313",
    "source": "kate人不错",
    "platform": "bilibili",
    "points": 21039,
    "published_at": "2024-11-18T07:04:36+00:00",
    "summary": "欢迎关注我的知识星球：https://t.zsxq.com/FF0He\n\n我会分享最新AI资讯、源代码、回答你的提问。\n\n视频亮点：\n\n双工具对比：解析 Cursor 和 Windsurf 各自优势\n实战案例：从五子棋到卡路里计算AI应用的完整开发过程\n专业部署：Android Studio 配置与构建技巧\n\n时间戳：\n\n0:00 - 引言\n\n0:26 - 我开发的应用演示\n\n2:33 - Rea"
  },
  {
    "id": "bvid:BV1WwD9BEES7",
    "domain": "AI",
    "title": "保姆级ClaudeCode从0到1完整实战项目",
    "url": "http://www.bilibili.com/video/av116391835343750",
    "source": "是茂宇呀",
    "platform": "bilibili",
    "points": 20835,
    "published_at": "2026-04-12T12:59:04+00:00",
    "summary": "花了两天录制了这个教程帮助到家从0到1的完整做一个项目并带大家入门，项目中用到的相关提示词及文档教我都分享了在了www.maoyu.site"
  },
  {
    "id": "bvid:BV1XxXpBEEHU",
    "domain": "AI",
    "title": "Claude Code远程开发终极方案！手机改代码+实时预览~【小白教程】",
    "url": "http://www.bilibili.com/video/av116294326230438",
    "source": "爱听书的程序员阿超",
    "platform": "bilibili",
    "points": 19054,
    "published_at": "2026-03-26T12:00:00+00:00",
    "summary": "之前，我一直在研究怎么远程使用 Claude Code 开发项目，并且能实时预览效果。但是一直都没有找到合适的解决方案，要么就是给一个临时公网链接预览，每次都需要再配置，要么就是购买云服务器来配置，都感觉挺麻烦的~\n\n最近，我发现这个蒲公英异地组网的方案，用来做远程开发 Claude Code 项目，感觉非常方便，不仅能修改代码，而且我实时预览的需求也很好的满足了。\n\n这样我随时随地都可以用 AI"
  },
  {
    "id": "bvid:BV1hEVY6jEGT",
    "domain": "AI",
    "title": "最新【Claude pro Max】保姆级充值教程 Claude code国内购买教程 注册+订阅一个视频教会你",
    "url": "http://www.bilibili.com/video/av116657754277772",
    "source": "小轩AI-",
    "platform": "bilibili",
    "points": 17137,
    "published_at": "2026-05-29T12:07:14+00:00",
    "summary": "aipayok.com"
  },
  {
    "id": "bvid:BV1FMEP6FE4S",
    "domain": "AI",
    "title": "2026 AI Agent哪家强？新手应该怎么选？",
    "url": "http://www.bilibili.com/video/av116692332187087",
    "source": "saysky96",
    "platform": "bilibili",
    "points": 15867,
    "published_at": "2026-06-04T14:38:26+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1cCVZ6NEym",
    "domain": "AI",
    "title": "这绝对是B站讲的最全最细的VibeCoding系统教程，手把手带你从环境安装到实战，包含所有干货！让你少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av116673944492771",
    "source": "峰识在大模型",
    "platform": "bilibili",
    "points": 14970,
    "published_at": "2026-06-01T08:53:14+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n本视频配套课件笔记代码/学习大纲/大模型学习路线戳这里获取→https://www.bilibili.com/opus/1195847460814061571?spm_id_from=333.1387.0.0\n另外有需要AI大模型学习路线图+必看书籍（国内外大牛著作）+入门及进阶视频教程+项目实战及源码提供+面试实战场景"
  },
  {
    "id": "bvid:BV19eQ3BJEkg",
    "domain": "AI",
    "title": "手撕大厂题-vibe coding降龙七步",
    "url": "http://www.bilibili.com/video/av116403881385303",
    "source": "青阳-AI",
    "platform": "bilibili",
    "points": 14570,
    "published_at": "2026-04-14T16:00:12+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1qBJ36yEC1",
    "domain": "AI",
    "title": "【2026最新】这绝对是b站讲的最好的Vibe Coding教程，手把手教你从安装到代码实战的保姆级教程！!少走99%弯路！",
    "url": "http://www.bilibili.com/video/av116752478377523",
    "source": "AI大模型_小奕",
    "platform": "bilibili",
    "points": 13123,
    "published_at": "2026-06-15T05:37:28+00:00",
    "summary": "本套教程从零开始讲解，手把手教学！\n无论是新手小白，还是有一定基础的小伙伴皆可学习。\n如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！"
  },
  {
    "id": "hn:48377404",
    "domain": "AI 算力 / 半导体",
    "title": "Use your Nvidia GPU's VRAM as swap space on Linux",
    "url": "https://github.com/c0dejedi/nbd-vram",
    "source": "tanelpoder",
    "platform": "hackernews",
    "points": 472,
    "published_at": "2026-06-02T22:55:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:48424605",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia is proposing a beast of a CPU system for Windows PCs",
    "url": "https://twitter.com/lemire/status/2062880075117113739",
    "source": "tosh",
    "platform": "hackernews",
    "points": 331,
    "published_at": "2026-06-06T12:52:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:48509844",
    "domain": "AI 算力 / 半导体",
    "title": "SkillSpector",
    "url": "https://github.com/NVIDIA/SkillSpector",
    "source": "taubek",
    "platform": "hackernews",
    "points": 49,
    "published_at": "2026-06-12T21:49:49+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/risc-v-silicon-in-the-jungle-could-save-the-amazon/",
    "domain": "AI 算力 / 半导体",
    "title": "RISC-V Silicon in the Jungle Could Save the Amazon",
    "url": "https://www.eetimes.com/risc-v-silicon-in-the-jungle-could-save-the-amazon/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T08:41:10+00:00",
    "summary": "Researchers at the University of São Paulo use RISC-V to build the Internet of Trees, a real-time monitoring network for the Amazon rainforest. The post RISC-V Silicon in the Jungle Could Save the Ama"
  },
  {
    "id": "rss:https://www.eetimes.com/globalfoundries-first-chipmaker-to-support-open-standard-for-ai-scale-up/",
    "domain": "AI 算力 / 半导体",
    "title": "GlobalFoundries: First Chipmaker to Support Open Standard for AI Scale Up",
    "url": "https://www.eetimes.com/globalfoundries-first-chipmaker-to-support-open-standard-for-ai-scale-up/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T22:00:00+00:00",
    "summary": "GlobalFoundries leads with the first silicon to support OCI MSA, shaking up AI data centers. The post GlobalFoundries: First Chipmaker to Support Open Standard for AI Scale Up appeared first on EE Tim"
  },
  {
    "id": "rss:https://www.eetimes.com/tensordyne-tapes-out-lns-based-ai-chip-claims-huge-power-advantages/",
    "domain": "AI 算力 / 半导体",
    "title": "Tensordyne Tapes Out LNS-Based AI Chip, Claims Huge Power Advantages",
    "url": "https://www.eetimes.com/tensordyne-tapes-out-lns-based-ai-chip-claims-huge-power-advantages/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T16:00:00+00:00",
    "summary": "The company said it can consume an order of magnitude less power per token versus GPU alternatives. The post Tensordyne Tapes Out LNS-Based AI Chip, Claims Huge Power Advantages appeared first on EE T"
  },
  {
    "id": "rss:https://www.eetimes.com/andy-mclean-rapidus-mou-will-help-british-innovators-access-2-nm-technology/",
    "domain": "AI 算力 / 半导体",
    "title": "Andy McLean: Rapidus MoU Will Help British Innovators Access 2-nm Technology",
    "url": "https://www.eetimes.com/andy-mclean-rapidus-mou-will-help-british-innovators-access-2-nm-technology/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T13:10:12+00:00",
    "summary": "As the UK Semiconductor Centre signs an MoU with Rapidus, EE Times speaks exclusively with its new CEO, Andy McLean. The post Andy McLean: Rapidus MoU Will Help British Innovators Access 2-nm Technolo"
  },
  {
    "id": "rss:https://www.eetimes.com/how-multi-sense-technologies-are-redefining-human-machine-interfaces-and-dexterous-robotics/",
    "domain": "AI 算力 / 半导体",
    "title": "How Multi-Sense Technologies Are Redefining Human-Machine Interfaces and Dexterous Robotics",
    "url": "https://www.eetimes.com/how-multi-sense-technologies-are-redefining-human-machine-interfaces-and-dexterous-robotics/",
    "source": "Vibheesh Bharathan, Director, Head of PSOC™ Multi-Sense MCUs, Infineon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T13:00:00+00:00",
    "summary": "Discover how multi-sense technologies are transforming HMIs, smart appliances, and dexterous robotics with AI-powered tactile sensing. The post How Multi-Sense Technologies Are Redefining Human-Machin"
  },
  {
    "id": "rss:https://www.eetimes.com/imec-pushes-quantum-toward-manufacturable-silicon-systems/",
    "domain": "AI 算力 / 半导体",
    "title": "Imec Pushes Quantum Toward Manufacturable Silicon Systems",
    "url": "https://www.eetimes.com/imec-pushes-quantum-toward-manufacturable-silicon-systems/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T08:13:05+00:00",
    "summary": "Imec says advanced lithography and semiconductor integration techniques may help scale silicon spin qubits toward manufacturable quantum systems. The post Imec Pushes Quantum Toward Manufacturable Sil"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-takes-over-mext-to-address-growing-memory-constraints-in-the-data-center-memory-tiering-technology-enables-flash-to-appear-as-dram-to-applications",
    "domain": "AI 算力 / 半导体",
    "title": "AMD takes over MEXT to 'address growing memory constraints' in the data center — memory tiering technology enables flash to appear as DRAM to applications",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-takes-over-mext-to-address-growing-memory-constraints-in-the-data-center-memory-tiering-technology-enables-flash-to-appear-as-dram-to-applications",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T19:00:47+00:00",
    "summary": "AMD acquires MEXT to get Predictive Memory Engine that offloads infrequently accessed data from DRAM to NAND storage."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/multiple-small-tennessee-counties-pass-temporary-data-center-bans-nashville-also-passed-near-unanimous-moratorium-on-first-reading",
    "domain": "AI 算力 / 半导体",
    "title": "Multiple small Tennessee counties pass temporary data center bans — Nashville also passed near-unanimous moratorium on first reading",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/multiple-small-tennessee-counties-pass-temporary-data-center-bans-nashville-also-passed-near-unanimous-moratorium-on-first-reading",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T18:06:33+00:00",
    "summary": "Two jurisdictions in Tennessee just passed a data center moratorium as three more a set to vote on bills that delay these projects. These temporary bans have gained widespread support, especially in r"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/marvell-details-vision-of-optically-interconnected-data-centers-spanning-across-thousands-of-kilometers-new-interconnects-sampling-later-this-year-would-allow-csps-to-pool-resources-based-on-workload",
    "domain": "AI 算力 / 半导体",
    "title": "Marvell details vision of optically-interconnected data centers spanning across thousands of kilometers — new interconnects sampling later this year would allow CSPs to pool resources based on workloa",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/marvell-details-vision-of-optically-interconnected-data-centers-spanning-across-thousands-of-kilometers-new-interconnects-sampling-later-this-year-would-allow-csps-to-pool-resources-based-on-workload",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T16:49:39+00:00",
    "summary": "Marvell shares its vision for optically connected data centers, connecting devices across hundreds of kilometers, and the company already has hardware to build them."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/chinas-top-court-bars-infineon-from-selling-gan-power-chips-in-china",
    "domain": "AI 算力 / 半导体",
    "title": "China's supreme court bans Infineon from selling GaN power chips in China — market-leader Innoscience secures major victory in multi-region patent war",
    "url": "https://www.tomshardware.com/tech-industry/chinas-top-court-bars-infineon-from-selling-gan-power-chips-in-china",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T14:27:11+00:00",
    "summary": "China's Supreme People's Court on Friday upheld an injunction prohibiting Infineon from selling disputed GaN products in mainland China."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/bambu-labs-big-anniversary-sale-is-live-with-up-to-52-percent-off-score-huge-discounts-on-their-most-popular-3d-printers-and-accessories",
    "domain": "AI 算力 / 半导体",
    "title": "Bambu Lab's big anniversary sale is live with up to 52% off — score huge discounts on their most popular 3D printers and accessories",
    "url": "https://www.tomshardware.com/3d-printing/bambu-labs-big-anniversary-sale-is-live-with-up-to-52-percent-off-score-huge-discounts-on-their-most-popular-3d-printers-and-accessories",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T14:14:33+00:00",
    "summary": "Save on some of the best 3D printers in Bambu Lab's Anniversary sale"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/cancelled-xbox-360-version-of-goldeneye-007-gets-recompiled-for-pc-no-emulator-the-game-runs-as-a-real-native-executable-insists-dev",
    "domain": "AI 算力 / 半导体",
    "title": "Cancelled Xbox 360 version of GoldenEye 007 gets recompiled for PC — ‘No emulator, the game runs as a real native executable,’ insists dev",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/cancelled-xbox-360-version-of-goldeneye-007-gets-recompiled-for-pc-no-emulator-the-game-runs-as-a-real-native-executable-insists-dev",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T13:43:30+00:00",
    "summary": "GoldenEye Recomp v1.0 has been released, providing 'a native PC port of GoldenEye 007 built by statically recompiling the original game into C++' with no emulation involved."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/docking-stations-hubs/cooler-master-masterhub-review",
    "domain": "AI 算力 / 半导体",
    "title": "Cooler Master MasterHUB review: A modular stream deck with potential",
    "url": "https://www.tomshardware.com/peripherals/docking-stations-hubs/cooler-master-masterhub-review",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T13:10:00+00:00",
    "summary": "Cooler Master's MasterHUB is a modular customizable macropad that's perhaps a little too ambitious. Its modularity is nicely implemented, but it's limited by its software and lack of plugins."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/score-32gb-of-ddr5-ram-from-only-usd240-in-these-newegg-hardware-bundles-for-intel-and-amd-gaming-pc-builds-huge-savings-on-premium-gigabyte-motherboards-coupled-with-popular-corsair-vengeance-memory",
    "domain": "AI 算力 / 半导体",
    "title": "Score 32GB of DDR5 RAM from only $240 in these Newegg hardware bundles for Intel and AMD gaming PC builds — huge savings on premium Gigabyte motherboards coupled with popular Corsair Vengeance memory",
    "url": "https://www.tomshardware.com/pc-components/score-32gb-of-ddr5-ram-from-only-usd240-in-these-newegg-hardware-bundles-for-intel-and-amd-gaming-pc-builds-huge-savings-on-premium-gigabyte-motherboards-coupled-with-popular-corsair-vengeance-memory",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T12:19:25+00:00",
    "summary": "These Newegg bundles for Intel and AMD gaming PC builds feature 32GB of Corsair Vengeance DDR5 RAM from only $240, featuring Gigabyte motherboards."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/asus-proart-pa27usd-27-inch-oled-review",
    "domain": "AI 算力 / 半导体",
    "title": "Asus ProArt PA27USD 27-inch OLED review: Precision color with high-speed gaming prowess",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/asus-proart-pa27usd-27-inch-oled-review",
    "source": "Christian Eberle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T12:10:00+00:00",
    "summary": "Asus combines professional and gaming cred in the ProArt PA27USD. It’s a 27-inch QD-OLED with 4K resolution, professional image modes, auto-calibration, 240 Hz, Adaptive-Sync, HDR10, HLG, Dolby Vision"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/chromebooks/google-chromebook-marks-its-15th-anniversary-slow-feature-rollouts-and-a-canceled-steam-beta-leave-it-largely-stuck-in-classrooms",
    "domain": "AI 算力 / 半导体",
    "title": "Google Chromebook marks its 15th anniversary — slow feature rollouts and a canceled Steam beta leave it largely stuck in classrooms",
    "url": "https://www.tomshardware.com/laptops/chromebooks/google-chromebook-marks-its-15th-anniversary-slow-feature-rollouts-and-a-canceled-steam-beta-leave-it-largely-stuck-in-classrooms",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T12:00:01+00:00",
    "summary": "Today marks 15 years since the first Chromebooks hit the market."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/samsungs-49-inch-ultrawide-odyssey-g9-gaming-monitor-dips-to-the-lowest-ever-price-of-usd664-at-amazon-get-240hz-refresh-rate-and-dense-109-ppi-for-34-percent-off",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung's 49-inch ultrawide Odyssey G9 gaming monitor dips to the lowest-ever price of $664 at Amazon — get 240Hz refresh rate and dense 109 PPI for 34% off",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/samsungs-49-inch-ultrawide-odyssey-g9-gaming-monitor-dips-to-the-lowest-ever-price-of-usd664-at-amazon-get-240hz-refresh-rate-and-dense-109-ppi-for-34-percent-off",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T11:18:44+00:00",
    "summary": "Save 34% on Samsung's Odyssey G9 gaming monitor and pick up this massive 49-inch display for just $664.99. Its lowest-ever price."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/fbi-and-google-dismantle-chinese-phishing-service-that-coached-buyers-to-generate-scam-sites-with-gemini",
    "domain": "AI 算力 / 半导体",
    "title": "FBI dismantles Chinese phishing service that coached buyers to generate scam sites using AI —$88 cybercrime product linked to $1.9 billion in losses, 3.87 million stolen cards",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/fbi-and-google-dismantle-chinese-phishing-service-that-coached-buyers-to-generate-scam-sites-with-gemini",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T11:10:54+00:00",
    "summary": "The FBI, Google, and Lumen Technologies say they’ve dismantled a China-based phishing-as-a-service operation called Outsider Enterprise."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/42-percent-slashed-of-samsungs-990-pro-ssd-2tb-now-usd369-usd270-savings-brings-one-of-the-fastest-pcie-4-0-ssds-to-its-lowest-price-in-months",
    "domain": "AI 算力 / 半导体",
    "title": "42% slashed off Samsung's 990 Pro SSD, 2TB now $369 — $270 savings brings one of the fastest PCIe 4.0 SSDs to its lowest price in months",
    "url": "https://www.tomshardware.com/pc-components/42-percent-slashed-of-samsungs-990-pro-ssd-2tb-now-usd369-usd270-savings-brings-one-of-the-fastest-pcie-4-0-ssds-to-its-lowest-price-in-months",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T10:49:25+00:00",
    "summary": "Samsung's 990 Pro 2TB is one of the fastest PCIe 4.0 M.2 SSDs around, delivering excellent performance and efficiency and backed by a 5-year warranty - now priced at $369.99, it's not the cheapest aro"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/2021-honda-civic-infotainment-system-can-be-jailbroken-via-usb-flaw-uses-public-android-test-keys-to-install-unauthorized-apps-enables-for-evilvalet-attacks",
    "domain": "AI 算力 / 半导体",
    "title": "2021 Honda Civic infotainment system can be jailbroken via USB — flaw uses public Android test keys to install unauthorized apps, enables for 'EvilValet' attacks",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/2021-honda-civic-infotainment-system-can-be-jailbroken-via-usb-flaw-uses-public-android-test-keys-to-install-unauthorized-apps-enables-for-evilvalet-attacks",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T10:00:00+00:00",
    "summary": "A software architect determined that they could practically install anything they want on the infotainment system of their 2021 Honda Civic through the front USB port. While the head unit required a s"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intels-upcoming-raptor-lake-next-will-reportedly-top-out-at-20-cores-and-retain-core-200-branding-lineup-may-include-a-special-10-core-sku-with-24mb-of-l3-cache",
    "domain": "AI 算力 / 半导体",
    "title": "Intel's upcoming 'Raptor Lake Next' will reportedly top out at 20 cores and retain Core 200 branding — Lineup may include a special 10-core SKU with 24MB of L3 cache",
    "url": "https://www.tomshardware.com/pc-components/cpus/intels-upcoming-raptor-lake-next-will-reportedly-top-out-at-20-cores-and-retain-core-200-branding-lineup-may-include-a-special-10-core-sku-with-24mb-of-l3-cache",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T14:57:07+00:00",
    "summary": "Intel's Raptor Lake family might be coming back for a third time and sit alongside Nova Lake on shelves as the budget-oriented offering from the company."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/servers/amazon-says-its-data-centers-consume-only-0-075-percent-of-the-water-americans-use-for-watering-their-lawns-and-gardens-company-also-boasts-of-its-improvements-in-water-efficiency",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon says its data centers consume only 0.075% of the water Americans use for watering their lawns and gardens — company also boasts of its improvements in water efficiency",
    "url": "https://www.tomshardware.com/desktops/servers/amazon-says-its-data-centers-consume-only-0-075-percent-of-the-water-americans-use-for-watering-their-lawns-and-gardens-company-also-boasts-of-its-improvements-in-water-efficiency",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T14:25:00+00:00",
    "summary": "Amazon says that it uses 2.5 billion gallons of water annually for data center cooling but compares it to the 3.3 trillion gallons of water used for watering lawns and gardens in the U.S. every year."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/computer-history-museum-recalls-astonishing-retro-haul-recovered-from-abandoned-german-warehouse-over-2-000-artifacts-spanning-the-1930s-to-1980s-required-seven-tractor-trailers-after-a-wwii-bomb-scare",
    "domain": "AI 算力 / 半导体",
    "title": "Computer History Museum recalls ‘astonishing’ retro haul recovered from abandoned German warehouse — over 2,000 artifacts spanning the 1930s to 1980s required seven tractor-trailers after a WWII bomb ",
    "url": "https://www.tomshardware.com/tech-industry/computer-history-museum-recalls-astonishing-retro-haul-recovered-from-abandoned-german-warehouse-over-2-000-artifacts-spanning-the-1930s-to-1980s-required-seven-tractor-trailers-after-a-wwii-bomb-scare",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T14:00:00+00:00",
    "summary": "The Computer History Museum recalls one of its biggest ever retro treasure troves. This ‘astonishing’ haul was rescued from an abandoned warehouse in the town of Castrop-Rauxel, Germany."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/apple-made-marketing-gold-from-the-power-mac-g4-supercomputer-export-ban-in-1999-pentagon-banned-sales-of-the-400-mhz-g4-in-50-countries-when-it-launched-and-became-the-first-pc-to-be-classed-as-a-weapon",
    "domain": "AI 算力 / 半导体",
    "title": "Apple made marketing gold from the export ban on Power Mac G4 'supercomputer' in 1999, 'for the first time in history a personal computer has been classified as a weapon' — Pentagon banned sales of th",
    "url": "https://www.tomshardware.com/tech-industry/apple-made-marketing-gold-from-the-power-mac-g4-supercomputer-export-ban-in-1999-pentagon-banned-sales-of-the-400-mhz-g4-in-50-countries-when-it-launched-and-became-the-first-pc-to-be-classed-as-a-weapon",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T14:00:00+00:00",
    "summary": "In the context of the recent tech export bans, we look back at the Apple PowerMac G4 export ban from 1999 and Steve Jobs making marketing gold from the situation."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/servers/researchers-recycle-old-phones-and-cluster-them-into-computing-platforms-says-processors-on-modern-smartphones-deliver-higher-single-core-performance-than-comparable-multicore-servers",
    "domain": "AI 算力 / 半导体",
    "title": "Researchers recycle old phones and cluster them into ‘computing platforms’ that operate as a low-cost data center — says processors on modern smartphones deliver higher single-core performance than co",
    "url": "https://www.tomshardware.com/desktops/servers/researchers-recycle-old-phones-and-cluster-them-into-computing-platforms-says-processors-on-modern-smartphones-deliver-higher-single-core-performance-than-comparable-multicore-servers",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T13:34:49+00:00",
    "summary": "A team of researchers from UC San Diego found that 'old' smartphones from 2023 could be combined to build a server capable of running apps locally, instead of relying on cloud servers located on a dis"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/snapmaker-launches-usd150-000-innovation-fund-for-open-source-3d-printing-cash-rewards-target-developers-backing-the-u1-toolchanger-across-klipper-orcaslicer-and-moonraker-ecosystems",
    "domain": "AI 算力 / 半导体",
    "title": "Snapmaker launches $150,000 Innovation Fund for open source 3D printing — cash rewards target developers backing the U1 toolchanger across Klipper, OrcaSlicer, and Moonraker ecosystems",
    "url": "https://www.tomshardware.com/3d-printing/snapmaker-launches-usd150-000-innovation-fund-for-open-source-3d-printing-cash-rewards-target-developers-backing-the-u1-toolchanger-across-klipper-orcaslicer-and-moonraker-ecosystems",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T13:30:00+00:00",
    "summary": "Snapmaker celebrates 10 years in business by sponsoring open-source developers and you."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/grab-this-msi-codex-z2-16-thread-gaming-ryzen-pc-with-a-2tb-ssd-at-a-usd400-discount-system-packs-a-ryzen-8700f-16gb-ddr5-and-rtx-5060-ti-8gb-for-usd1-499",
    "domain": "AI 算力 / 半导体",
    "title": "Grab this MSI Codex Z2 16-thread gaming Ryzen PC with a 2TB SSD at a $400 discount — system packs a Ryzen 8700F, 16GB DDR5, and RTX 5060 Ti 8GB for $1,499",
    "url": "https://www.tomshardware.com/pc-components/grab-this-msi-codex-z2-16-thread-gaming-ryzen-pc-with-a-2tb-ssd-at-a-usd400-discount-system-packs-a-ryzen-8700f-16gb-ddr5-and-rtx-5060-ti-8gb-for-usd1-499",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T13:28:13+00:00",
    "summary": "MSI's prebuilt gaming desktop pairs a Zen 4 processor with Nvidia's latest RTX 5060 Ti graphics card and comes housed in an airflow-focused chassis with ARGB lighting."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/nist-gets-metal-3d-printers-to-mix-alloys-mid-print-by-rewriting-the-lasers-path",
    "domain": "AI 算力 / 半导体",
    "title": "New 3D printer tech uses elliptical laser beams to stir molten metal and create ‘alloys-on-demand’ — existing machinery can implement technique in software meaning for more convenient, stronger alloy ",
    "url": "https://www.tomshardware.com/3d-printing/nist-gets-metal-3d-printers-to-mix-alloys-mid-print-by-rewriting-the-lasers-path",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T13:02:26+00:00",
    "summary": "NIST has demonstrated a metal 3D printing method that stirs molten metal during the print by sending the laser along looping elliptical paths instead of straight lines."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/microsoft-is-reportedly-testing-copilot-ai-features-with-discrete-gpus-instead-of-npus-a-feature-available-on-windows-app-sdk-with-a-windows-insider-experimental-channel-build-and-developer-mode-turned-on",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft is reportedly testing Copilot+ AI features with discrete GPUs instead of NPUs — a feature available on Windows App SDK with a Windows Insider Experimental Channel build and Developer Mode tu",
    "url": "https://www.tomshardware.com/software/windows/microsoft-is-reportedly-testing-copilot-ai-features-with-discrete-gpus-instead-of-npus-a-feature-available-on-windows-app-sdk-with-a-windows-insider-experimental-channel-build-and-developer-mode-turned-on",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T13:00:00+00:00",
    "summary": "Microsoft is experimenting with Windows AI features on non-Copilot devices, finally allowing AI features to run on discrete GPUs. This move expands its user base and gives more users access to Windows"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-hit-with-sweeping-probe-from-massive-coalition-of-42-us-state-attorneys-general-just-days-after-reported-ipo-filing-subpoena-targets-chatgpt-makers-ads-data-practices-handling-of-minors-model-sycophancy-and-safety-policies",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI hit with sweeping probe from massive coalition of 42 US state attorneys general just days after reported IPO filing — subpoena targets ChatGPT maker’s ads, data practices, handling of minors, m",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-hit-with-sweeping-probe-from-massive-coalition-of-42-us-state-attorneys-general-just-days-after-reported-ipo-filing-subpoena-targets-chatgpt-makers-ads-data-practices-handling-of-minors-model-sycophancy-and-safety-policies",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T12:30:00+00:00",
    "summary": "State attorneys general have opened a broad investigation into OpenAI, subpoenaing documents on ads, user retention, data handling, minors, health data, model behavior, and safety policies."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/macbooks/amd-taunts-apples-macbook-neo-for-failing-to-run-75-percent-of-top-pc-games-only-5-out-of-the-20-top-pc-games-work-on-the-neo-while-all-run-on-amds-budget-offerings",
    "domain": "AI 算力 / 半导体",
    "title": "AMD taunts Apple's MacBook Neo for failing to run 75% of top PC games — Only 5 out of the 20 top PC games work on the Neo, while all run on AMD's budget offerings",
    "url": "https://www.tomshardware.com/laptops/macbooks/amd-taunts-apples-macbook-neo-for-failing-to-run-75-percent-of-top-pc-games-only-5-out-of-the-20-top-pc-games-work-on-the-neo-while-all-run-on-amds-budget-offerings",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T12:00:00+00:00",
    "summary": "AMD is reminding folks not to buy a MacBook, even if it's as good of a deal as the Neo, if you primarily want to game on it. Instead, AMD's own budget laptops can run all the modern titles you want, w"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/trump-adviser-david-sacks-says-anthropic-refused-to-fix-fable-5-jailbreak-before-us-export-controls",
    "domain": "AI 算力 / 半导体",
    "title": "US government warned Anthropic that Fable 5 had been jailbroken, but firm 'refused' to fix before US implemented export controls — Anthropic defended its decision by saying the jailbreak 'isn’t seriou",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/trump-adviser-david-sacks-says-anthropic-refused-to-fix-fable-5-jailbreak-before-us-export-controls",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T11:46:43+00:00",
    "summary": "David Sacks said the US government warned Anthropic that Claude Fable 5 had been jailbroken and that CEO Dario Amodei refused to fix the flaw."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-cryptomining-networks-320-000-rtx-3090-class-gpus-allegedly-burn-112-megawatts-of-power-on-zero-useful-ai-computation-pearls-gpus-are-doing-random-matrix-math-study-claims",
    "domain": "AI 算力 / 半导体",
    "title": "AI cryptomining network's 320,000 RTX 3090-class GPUs allegedly burn 112 megawatts of power on ‘zero useful AI computation’ — GPU rental costs jump 38%, but Pearl’s cards are doing random matrix math,",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-cryptomining-networks-320-000-rtx-3090-class-gpus-allegedly-burn-112-megawatts-of-power-on-zero-useful-ai-computation-pearls-gpus-are-doing-random-matrix-math-study-claims",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T11:30:00+00:00",
    "summary": "A preprint claims Pearl’s AI mining network consumes 320,000 GPU-equivalents and 112 MW while producing no verified useful AI computation."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/webcams/razer-kiyo-v2-x-review",
    "domain": "AI 算力 / 半导体",
    "title": "Razer Kiyo V2 X Review: Auto-focus for life",
    "url": "https://www.tomshardware.com/peripherals/webcams/razer-kiyo-v2-x-review",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T11:10:00+00:00",
    "summary": "Razer's Kiyo V2 X is the most budget-friendly of its current webcam lineup; it records video at 1440p / 60 fps and features \"speedy\" auto-focus, a wide 80-degree field of view, and a smoothly integrat"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/console-gaming/hardcore-spongebob-speedrunners-smudged-xbox-optical-disks-to-exploit-lag-clip-trick-filthy-disks-smeared-with-grease-and-sweat-cut-gameplay-times-in-ultimate-pursuit-of-speed",
    "domain": "AI 算力 / 半导体",
    "title": "Hardcore SpongeBob speedrunners smudged Xbox optical disks with sweat and grease to exploit 'lag clip' trick — filthy smeared disks cut gameplay times in ultimate pursuit of speed",
    "url": "https://www.tomshardware.com/video-games/console-gaming/hardcore-spongebob-speedrunners-smudged-xbox-optical-disks-to-exploit-lag-clip-trick-filthy-disks-smeared-with-grease-and-sweat-cut-gameplay-times-in-ultimate-pursuit-of-speed",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T11:00:00+00:00",
    "summary": "A grease smear-induced optical disc reading quirk can save speedrunners lots of time in SpongeBob SquarePants: Battle for Bikini Bottom on Xbox."
  },
  {
    "id": "hn:48444451",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia partners with LG robotics to build humanoid robots in South Korea",
    "url": "https://blogs.nvidia.com/blog/nvidia-and-lg-group-ai-factory/",
    "source": "spwa4",
    "platform": "hackernews",
    "points": 59,
    "published_at": "2026-06-08T12:25:14+00:00",
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
    "id": "hn:48431367",
    "domain": "AI 算力 / 半导体",
    "title": "The Russian who invented semiconductors 25 years before the USA",
    "url": "https://www.semidoped.com/p/til-the-man-who-invented-the-future",
    "source": "johncole",
    "platform": "hackernews",
    "points": 53,
    "published_at": "2026-06-07T03:00:52+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/uclas-125m-semiconductor-hub-we-want-high-impact-not-incremental-research/",
    "domain": "AI 算力 / 半导体",
    "title": "UCLA’s $125M Semiconductor Hub: “We Want High Impact, Not Incremental Research”",
    "url": "https://www.eetimes.com/uclas-125m-semiconductor-hub-we-want-high-impact-not-incremental-research/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T19:00:00+00:00",
    "summary": "UCLA launches a $125M semiconductor hub to smash chip bottlenecks with AI research. The post UCLA’s $125M Semiconductor Hub: “We Want High Impact, Not Incremental Research” appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/tecate-group-announces-new-ultracapacitor-cells-rated-foroperation-up-to-105c-221f/",
    "domain": "AI 算力 / 半导体",
    "title": "Tecate Group Announces New Ultracapacitor Cells Rated forOperation up to 105°C (221°F)",
    "url": "https://www.eetimes.com/tecate-group-announces-new-ultracapacitor-cells-rated-foroperation-up-to-105c-221f/",
    "source": "Tecate Group",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T18:49:02+00:00",
    "summary": "San Diego, CA: June 1, 2026. Tecate Group today announced the expansion of its ultracapacitorproduct offerings with new cells rated for operation up to 105°C (221°F). The new TPLT productseries is rat"
  },
  {
    "id": "rss:https://www.eetimes.com/peak-goes-automotive-ethernet-pae-media-converter-connects-100-1000base-t1-with-standard-ethernet/",
    "domain": "AI 算力 / 半导体",
    "title": "PEAK Goes Automotive Ethernet: PAE-Media Converter connects 100/1000BASE-T1 with Standard Ethernet",
    "url": "https://www.eetimes.com/peak-goes-automotive-ethernet-pae-media-converter-connects-100-1000base-t1-with-standard-ethernet/",
    "source": "HMS Networks",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T17:01:05+00:00",
    "summary": "Unique Features for Automotive Testing The PAE-Media Converter addresses crucial market challenges in automotive development and validation with three core innovations. It enables realistic fault simu"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-usd500-on-this-beastly-gaming-rig-with-an-rtx-5060-ti-16gb-ryzen-7800x3d-and-32gb-of-ram-skytechs-desktop-gaming-pc-now-just-usd1-499",
    "domain": "AI 算力 / 半导体",
    "title": "Save $500 on this beastly gaming rig with an RTX 5060 Ti 16GB, Ryzen 7800X3D, and 32GB of RAM — Skytech's desktop gaming PC now just $1,499",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-usd500-on-this-beastly-gaming-rig-with-an-rtx-5060-ti-16gb-ryzen-7800x3d-and-32gb-of-ram-skytechs-desktop-gaming-pc-now-just-usd1-499",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T14:29:37+00:00",
    "summary": "Looking for a solid gaming PC but tired of seeing exorbitant prices on every retailer's website? We've got you covered with this prebuilt, equipped with high-quality components ready for 1440p gaming "
  },
  {
    "id": "hn:48439316",
    "domain": "AI 算力 / 半导体",
    "title": "Huawei executive credits bans for accelerating domestic chip independence",
    "url": "https://www.techradar.com/pro/huaweis-chairman-officially-thanks-the-us-government-for-enabling-chinas-semiconductor-industry-chain-to-truly-grow",
    "source": "yogthos",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-06-07T22:38:25+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/indian-firm-scales-single-walled-carbon-nanotube-production-for-batteries-and-chips/",
    "domain": "AI 算力 / 半导体",
    "title": "Indian Firm Scales Single-Walled Carbon Nanotube Production for Batteries and Chips",
    "url": "https://www.eetimes.com/indian-firm-scales-single-walled-carbon-nanotube-production-for-batteries-and-chips/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T08:04:16+00:00",
    "summary": "NoPo scales HiPco single-walled carbon nanotube output for sub-2-nm chips and anodes. The post Indian Firm Scales Single-Walled Carbon Nanotube Production for Batteries and Chips appeared first on EE "
  },
  {
    "id": "hn:48430986",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC CEO: I envy their 80% gross margins, but I would never do that",
    "url": "https://www.thestreet.com/investing/stocks/tsmc-taiwan-semiconductor-ceo-sends-blunt-message-to-memory-chip-rivals",
    "source": "teleforce",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-06-07T01:53:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:48274048",
    "domain": "AI 算力 / 半导体",
    "title": "Taiwan Overtakes India as Fifth-Largest Stock Market",
    "url": "https://www.bloomberg.com/news/articles/2026-05-26/tsmc-s-relentless-rise-powers-taiwan-s-market-value-above-india",
    "source": "leopoldj",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-05-26T01:49:54+00:00",
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
    "id": "hn:48450142",
    "domain": "大厂 AI 动态",
    "title": "Apple reveals new AI architecture built around Google Gemini models",
    "url": "https://www.macrumors.com/2026/06/08/apple-reveals-new-ai-architecture/",
    "source": "unclefuzzy",
    "platform": "hackernews",
    "points": 737,
    "published_at": "2026-06-08T19:14:47+00:00",
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
    "id": "hn:48449084",
    "domain": "大厂 AI 动态",
    "title": "Siri AI",
    "url": "https://www.apple.com/apple-intelligence/",
    "source": "0xedb",
    "platform": "hackernews",
    "points": 681,
    "published_at": "2026-06-08T18:17:53+00:00",
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
    "id": "hn:48297467",
    "domain": "大厂 AI 动态",
    "title": "Gemini, Gophers, and Fingers. Oh My Alternative Internets Beyond HTTPS",
    "url": "https://brennan.day/gemini-gophers-and-fingers-oh-my-alternative-internets-beyond-https/",
    "source": "ChrisArchitect",
    "platform": "hackernews",
    "points": 147,
    "published_at": "2026-05-27T17:24:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:48373764",
    "domain": "大厂 AI 动态",
    "title": "GitHub Copilot App",
    "url": "https://github.com/features/preview/github-app",
    "source": "theanonymousone",
    "platform": "hackernews",
    "points": 124,
    "published_at": "2026-06-02T17:58:55+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/950412/anthropic-trump-adminstration-claude-mythos-fable-5-export-controls",
    "domain": "大厂 AI 动态",
    "title": "Inside the fight over Claude Mythos 5",
    "url": "https://www.theverge.com/ai-artificial-intelligence/950412/anthropic-trump-adminstration-claude-mythos-fable-5-export-controls",
    "source": "Hayden Field",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T03:00:00+00:00",
    "summary": "As the rest of the country celebrated the USA's first World Cup win and the New York Knicks championship, Anthropic spent its weekend fighting the Trump administration over its latest model release. A"
  },
  {
    "id": "rss:https://www.theverge.com/tech/950264/meta-ai-mode-search-facebook",
    "domain": "大厂 AI 动态",
    "title": "Facebook’s new AI Mode search gets its info from public posts",
    "url": "https://www.theverge.com/tech/950264/meta-ai-mode-search-facebook",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T21:15:08+00:00",
    "summary": "Your public Facebook posts could help inform AI-generated results in Meta's new AI Mode. When you search on Facebook, the \"AI Mode\" option will appear alongside the usual search modes like \"People\" an"
  },
  {
    "id": "rss:https://www.theverge.com/games/950204/xbox-ninja-theory-shutdown-hellblade-senua",
    "domain": "大厂 AI 动态",
    "title": "Xbox is closing down Hellblade creator Ninja Theory",
    "url": "https://www.theverge.com/games/950204/xbox-ninja-theory-shutdown-hellblade-senua",
    "source": "Tom Warren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T21:13:35+00:00",
    "summary": "Xbox is closing down Ninja Theory, the studio behind the Hellblade series, a source tells The Verge. Staffers were told on a call on Monday about the closure, but they are hoping the studio will find "
  },
  {
    "id": "rss:https://www.theverge.com/streaming/950116/fox-roku-takeover",
    "domain": "大厂 AI 动态",
    "title": "Fox wants to take over your TV — and the tech inside it",
    "url": "https://www.theverge.com/streaming/950116/fox-roku-takeover",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T20:04:29+00:00",
    "summary": "Fox is about to take over the TVs in more than 100 million homes worldwide. On Monday, Fox announced that it's acquiring Roku, the streaming middleman that serves as a portal for viewers to hop into s"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/950043/amazon-smart-thermostat-early-prime-day-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Amazon&#8217;s Smart Thermostat is on sale for just $58",
    "url": "https://www.theverge.com/gadgets/950043/amazon-smart-thermostat-early-prime-day-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T19:33:28+00:00",
    "summary": "If your electricity bill climbs every summer, a smart thermostat could help keep cooling costs in check. The Amazon Smart Thermostat is an excellent option for its price, especially today. It&#8217;s "
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/950026/anthropic-fable-mythos-ban-ai-shutdown",
    "domain": "大厂 AI 动态",
    "title": "All the news about Anthropic&#8217;s new AI fight with the White House",
    "url": "https://www.theverge.com/ai-artificial-intelligence/950026/anthropic-fable-mythos-ban-ai-shutdown",
    "source": "Richard Lawler",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T19:04:53+00:00",
    "summary": "Anthropic was already navigating one dispute with the government in its standoff with the Pentagon, and then came an order on June 12th to block off foreign access to its most recently released AI mod"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/944084/best-early-prime-day-deals",
    "domain": "大厂 AI 动态",
    "title": "The best early Amazon Prime Day deals so far",
    "url": "https://www.theverge.com/gadgets/944084/best-early-prime-day-deals",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T18:39:37+00:00",
    "summary": "Amazon’s earlier-than-usual Prime Day doesn’t begin until June 23rd, but there are several even earlier deals on must-have products that you can check out right now. To name some examples, Apple’s Air"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/949986/anthropic-fable-mythos-shutdown-sovereign-ai",
    "domain": "大厂 AI 动态",
    "title": "Trump’s Anthropic shutdown just made the case for non-American AI",
    "url": "https://www.theverge.com/ai-artificial-intelligence/949986/anthropic-fable-mythos-shutdown-sovereign-ai",
    "source": "Robert Hart",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T18:10:27+00:00",
    "summary": "At Washington's request, Anthropic suddenly took its newest and most powerful AI models offline over the weekend. The American company said it had little choice after the White House demanded it block"
  },
  {
    "id": "rss:https://www.theverge.com/tech/950005/google-chrome-removing-ad-blocker-loopholes",
    "domain": "大厂 AI 动态",
    "title": "Google Chrome is closing the loopholes that let old ad blockers keep working",
    "url": "https://www.theverge.com/tech/950005/google-chrome-removing-ad-blocker-loopholes",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T18:06:18+00:00",
    "summary": "Google Chrome version 150 and 151, expected in late June and July, respectively, will cut off support for the last remaining workarounds for running older ad blockers, 9to5Google reports. Google phase"
  },
  {
    "id": "rss:https://www.theverge.com/policy/949970/ai-regulation-child-safety-kosa-congress",
    "domain": "大厂 AI 动态",
    "title": "Big Tech’s desperate last push at AI regulation",
    "url": "https://www.theverge.com/policy/949970/ai-regulation-child-safety-kosa-congress",
    "source": "Tina Nguyen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T17:44:10+00:00",
    "summary": "For months, Big Tech's Washington lobbyists have chased after the holy grail of pro-AI legislation: preemption. This would be a comprehensive federal law, passed in Congress and signed by the presiden"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/15/malaysias-respond-io-raises-62-5m-eyes-acquisitions-in-north-america-and-europe/",
    "domain": "大厂 AI 动态",
    "title": "Malaysia’s AI agent-powered messaging app Respond.io raises $62.5M, eyes acquisitions",
    "url": "https://techcrunch.com/2026/06/15/malaysias-respond-io-raises-62-5m-eyes-acquisitions-in-north-america-and-europe/",
    "source": "Kate Park",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T06:59:00+00:00",
    "summary": "Respond.io, one of Malaysia startups to watch, uses AI agents to handle high volumes of customer inquiries and charges per convo, not per seat."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/15/sundar-pichai-faces-boos-walkout-at-stanford-graduation-ceremony-over-googles-israel-ice-ties/",
    "domain": "大厂 AI 动态",
    "title": "Sundar Pichai faces boos, walkout at Stanford graduation ceremony over Google’s Israel, ICE ties",
    "url": "https://techcrunch.com/2026/06/15/sundar-pichai-faces-boos-walkout-at-stanford-graduation-ceremony-over-googles-israel-ice-ties/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T23:51:44+00:00",
    "summary": "AI is once again at the heart of a college graduation protest — this time for the technology's use in Google's defense contracts."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/15/the-us-governments-anthropic-models-ban-was-never-about-an-ai-jailbreak/",
    "domain": "大厂 AI 动态",
    "title": "The US government’s Anthropic models ban was never about an AI jailbreak",
    "url": "https://techcrunch.com/2026/06/15/the-us-governments-anthropic-models-ban-was-never-about-an-ai-jailbreak/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T21:50:21+00:00",
    "summary": "The Trump administration's decision that forced Anthropic to pull its latest cybersecurity models could be reactionary, retaliatory, or both, but the message is clear: The AI industry isn't immune fro"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/15/metas-new-ai-mode-on-facebook-pulls-from-public-info-across-its-platforms/",
    "domain": "大厂 AI 动态",
    "title": "Meta’s new ‘AI Mode’ on Facebook pulls from public info across its platforms",
    "url": "https://techcrunch.com/2026/06/15/metas-new-ai-mode-on-facebook-pulls-from-public-info-across-its-platforms/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T18:30:58+00:00",
    "summary": "Meta announced Monday that it's rolling out a wave of new AI features on Facebook, the latest sign of the company's effort to catch up in the AI race and keep users more engaged on the platform."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/15/spacex-is-public-everything-you-need-to-know-post-ipo/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX is public: Everything you need to know post-IPO",
    "url": "https://techcrunch.com/2026/06/15/spacex-is-public-everything-you-need-to-know-post-ipo/",
    "source": "Kirsten Korosec, Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T18:30:34+00:00",
    "summary": "TechCrunch has followed SpaceX's start, struggles, and successes from the early days. And we're here for what happens next too. This package of SpaceX IPO coverage includes who stands to win (and mayb"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/15/social-media-ban-children-countries-list/",
    "domain": "大厂 AI 动态",
    "title": "These are the countries moving to ban social media for children",
    "url": "https://techcrunch.com/2026/06/15/social-media-ban-children-countries-list/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T17:41:02+00:00",
    "summary": "Australia was the first country to issue a ban in late 2025, aiming to reduce the pressures and risks that young users may face on social media, including cyberbullying, social media addiction, and ex"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/15/cybersecurity-vets-protest-dangerous-us-government-ban-on-anthropics-most-powerful-models/",
    "domain": "大厂 AI 动态",
    "title": "Cybersecurity vets protest ‘dangerous’ US government ban on Anthropic’s most powerful models",
    "url": "https://techcrunch.com/2026/06/15/cybersecurity-vets-protest-dangerous-us-government-ban-on-anthropics-most-powerful-models/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T15:29:51+00:00",
    "summary": "A group made up of dozens of cybersecurity experts urged the White House to remove export-control restrictions on Anthropic’s Fable and Mythos models, arguing that the order is going to limit the abil"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/15/spacexs-biggest-ever-ipo-just-grew-to-85-7-billion-raised/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX’s biggest-ever IPO just grew to $85.7 billion raised",
    "url": "https://techcrunch.com/2026/06/15/spacexs-biggest-ever-ipo-just-grew-to-85-7-billion-raised/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T14:45:03+00:00",
    "summary": "SpaceX's IPO underwriters maxed out their share purchases, adding to an already historic amount of money raised."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/15/uk-unveils-sweeping-social-media-ban-for-users-under-16/",
    "domain": "大厂 AI 动态",
    "title": "UK unveils sweeping social media ban for users under 16",
    "url": "https://techcrunch.com/2026/06/15/uk-unveils-sweeping-social-media-ban-for-users-under-16/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T14:36:56+00:00",
    "summary": "The ban would apply to a range of social media platforms, including Snapchat, TikTok, YouTube, Instagram, Facebook, and X."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/15/salesforce-acquires-ai-customer-service-platform-fin-for-3-6b/",
    "domain": "大厂 AI 动态",
    "title": "Salesforce acquires AI customer service platform Fin for $3.6B",
    "url": "https://techcrunch.com/2026/06/15/salesforce-acquires-ai-customer-service-platform-fin-for-3-6b/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T14:34:45+00:00",
    "summary": "Salesforce says it wants to use Fin's team and technology to improve Agentforce, its existing enterprise platform that businesses can use to build custom AI agents that automate tasks."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/15/sarvam-becomes-indias-newest-ai-unicorn-with-234-million-funding-round-led-by-hcltech/",
    "domain": "大厂 AI 动态",
    "title": "Sarvam becomes India’s newest AI unicorn with $234 million funding round led by HCLTech",
    "url": "https://techcrunch.com/2026/06/15/sarvam-becomes-indias-newest-ai-unicorn-with-234-million-funding-round-led-by-hcltech/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T13:46:08+00:00",
    "summary": "Indian IT services company HCLTech is investing $150 million in the Bengaluru startup."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/15/fox-to-acquire-roku-in-22-billion-deal/",
    "domain": "大厂 AI 动态",
    "title": "Fox to acquire Roku in $22B deal",
    "url": "https://techcrunch.com/2026/06/15/fox-to-acquire-roku-in-22-billion-deal/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T13:43:05+00:00",
    "summary": "Fox says the deal will create the third-largest television company in the United States."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/15/ai-agents-are-becoming-employees-newcore-emerges-with-66m-to-give-them-identities/",
    "domain": "大厂 AI 动态",
    "title": "As AI agents become employees, NewCore emerges with $66M to give them identities",
    "url": "https://techcrunch.com/2026/06/15/ai-agents-are-becoming-employees-newcore-emerges-with-66m-to-give-them-identities/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T13:00:00+00:00",
    "summary": "NewCore argues the next challenge in enterprise security will be managing AI agents, not people."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/15/a-satellite-just-learned-to-find-things-on-its-own-heres-what-that-means/",
    "domain": "大厂 AI 动态",
    "title": "A satellite just learned to find things on its own — here’s what that means",
    "url": "https://techcrunch.com/2026/06/15/a-satellite-just-learned-to-find-things-on-its-own-heres-what-that-means/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T12:00:00+00:00",
    "summary": "In April, for the first time ever, an Earth observation satellite found what it was looking for, all on its own."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/15/the-ai-layoff-wave-is-becoming-a-powder-keg/",
    "domain": "大厂 AI 动态",
    "title": "The AI layoff wave is becoming a powder keg",
    "url": "https://techcrunch.com/2026/06/15/the-ai-layoff-wave-is-becoming-a-powder-keg/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T07:25:41+00:00",
    "summary": "At the very moment that tens of thousands of workers are being shown the door, a small cohort of AI insiders is becoming wealthy on a scale that's hard to comprehend."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/14/orbio-raises-21-million-to-automate-hiring-and-onboarding-for-frontline-workers/",
    "domain": "大厂 AI 动态",
    "title": "Orbio raises $21 million to automate hiring and onboarding for frontline workers",
    "url": "https://techcrunch.com/2026/06/14/orbio-raises-21-million-to-automate-hiring-and-onboarding-for-frontline-workers/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T04:01:00+00:00",
    "summary": "Orbio announces $21 million Series A in round led by Dawn Capital."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/14/startup-ceo-charlie-javice-is-reportedly-angling-for-a-trump-pardon/",
    "domain": "大厂 AI 动态",
    "title": "Startup CEO Charlie Javice is reportedly angling for a Trump pardon",
    "url": "https://techcrunch.com/2026/06/14/startup-ceo-charlie-javice-is-reportedly-angling-for-a-trump-pardon/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T21:55:34+00:00",
    "summary": "JPMorgan can't be pleased by any of this."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/14/uk-may-ban-social-media-for-children-under-16/",
    "domain": "大厂 AI 动态",
    "title": "UK may ban social media for children under 16",
    "url": "https://techcrunch.com/2026/06/14/uk-may-ban-social-media-for-children-under-16/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T20:17:00+00:00",
    "summary": "The U.K. seems to be following Australia's lead in banning a wide swath of social media for teens."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/14/as-ai-companies-race-to-go-public-who-else-is-along-for-the-ride/",
    "domain": "大厂 AI 动态",
    "title": "As AI companies race to go public, who else is along for the ride?",
    "url": "https://techcrunch.com/2026/06/14/as-ai-companies-race-to-go-public-who-else-is-along-for-the-ride/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T16:38:09+00:00",
    "summary": "Startups are trying to \"ride that SpaceX IPO wave.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/14/techcrunch-mobility-spacex-rockets-past-tesla/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Mobility: SpaceX rockets past Tesla",
    "url": "https://techcrunch.com/2026/06/14/techcrunch-mobility-spacex-rockets-past-tesla/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T16:05:00+00:00",
    "summary": "Welcome back to TechCrunch Mobility, your hub for the future of transportation and now, more than ever, how AI is playing a part."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/06/key-mission-for-europes-commercial-space-enterprise-scrubbed-again/",
    "domain": "大厂 AI 动态",
    "title": "Key mission for Europe's commercial space enterprise scrubbed again",
    "url": "https://arstechnica.com/space/2026/06/key-mission-for-europes-commercial-space-enterprise-scrubbed-again/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T23:40:38+00:00",
    "summary": "Isar Aerospace is not hurting for money, but it is sorely lacking in the currency of flight experience."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/06/covid-vaccines-still-protect-against-heart-problems-large-study-finds/",
    "domain": "大厂 AI 动态",
    "title": "Heart protection from COVID shots remains amid updates, study finds",
    "url": "https://arstechnica.com/health/2026/06/covid-vaccines-still-protect-against-heart-problems-large-study-finds/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T21:04:26+00:00",
    "summary": "Despite continued benefits, anti-vaccine rhetoric has driven down vaccination."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/06/uk-to-ban-social-media-for-kids-under-16-may-impose-overnight-curfews/",
    "domain": "大厂 AI 动态",
    "title": "UK to ban social media for kids under 16, may impose overnight curfews",
    "url": "https://arstechnica.com/tech-policy/2026/06/uk-to-ban-social-media-for-kids-under-16-may-impose-overnight-curfews/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T20:14:04+00:00",
    "summary": "Critics say bans push kids to riskier alternatives and can be beaten with VPNs."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/06/chipmaker-nvidia-seeks-to-raise-over-25b-in-first-bond-deal-since-2021/",
    "domain": "大厂 AI 动态",
    "title": "Chipmaker Nvidia seeks to raise over $25B in first bond deal since 2021",
    "url": "https://arstechnica.com/ai/2026/06/chipmaker-nvidia-seeks-to-raise-over-25b-in-first-bond-deal-since-2021/",
    "source": "Michelle Chan and Tim Bradshaw, Financial Times",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T19:07:02+00:00",
    "summary": "Debt sale set to test investor appetite for further exposure to AI sector amid a deluge of borrowing."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/06/a-chinese-rocket-breaks-apart-dangerously-close-to-the-starlink-constellation/",
    "domain": "大厂 AI 动态",
    "title": "A Chinese rocket breaks apart dangerously close to the Starlink constellation",
    "url": "https://arstechnica.com/space/2026/06/a-chinese-rocket-breaks-apart-dangerously-close-to-the-starlink-constellation/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T18:55:41+00:00",
    "summary": "The rocket's breakup likely generated 100 to 150 new pieces of space junk."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/06/foxs-22b-roku-acquisition-aims-to-expand-its-reach-into-smart-tvs-advertising/",
    "domain": "大厂 AI 动态",
    "title": "Fox’s $22B Roku acquisition aims to expand its reach into smart TVs, advertising",
    "url": "https://arstechnica.com/gadgets/2026/06/foxs-22b-roku-acquisition-aims-to-expand-its-reach-into-smart-tvs-advertising/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T18:29:47+00:00",
    "summary": "Fox plans to take over Roku's streaming hardware, OS, and FAST services."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/06/users-cry-foul-after-amd-stripped-memory-crypto-from-its-consumer-cpus/",
    "domain": "大厂 AI 动态",
    "title": "Users cry foul after AMD stripped memory crypto from its consumer CPUs",
    "url": "https://arstechnica.com/security/2026/06/users-cry-foul-after-amd-stripped-memory-crypto-from-its-consumer-cpus/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T17:55:46+00:00",
    "summary": "AMD's stripping of TSME from consumer CPUs appears to be a deliberate, covert move."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/06/20-years-of-intel-macs-why-apple-switched-and-why-it-switched-again/",
    "domain": "大厂 AI 动态",
    "title": "20 years of Intel Macs: Why Apple switched, and why it switched again",
    "url": "https://arstechnica.com/gadgets/2026/06/20-years-of-intel-macs-why-apple-switched-and-why-it-switched-again/",
    "source": "Andrew Cunningham",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T16:32:14+00:00",
    "summary": "Remembering the ups and downs of the Intel Mac era as it finally winds down."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/06/good-news-we-have-extra-time-before-the-sun-ends-life-on-earth/",
    "domain": "大厂 AI 动态",
    "title": "Good news—we have extra time before the Sun ends life on Earth",
    "url": "https://arstechnica.com/science/2026/06/good-news-we-have-extra-time-before-the-sun-ends-life-on-earth/",
    "source": "Scott K. Johnson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T16:28:17+00:00",
    "summary": "Will the Sun roast Earth’s plants or starve them?"
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/06/f1-in-spain-an-old-fashioned-strategy-fight-can-still-be-thrilling/",
    "domain": "大厂 AI 动态",
    "title": "F1 in Spain: An old-fashioned strategy fight can still be thrilling",
    "url": "https://arstechnica.com/cars/2026/06/f1-in-spain-an-old-fashioned-strategy-fight-can-still-be-thrilling/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T15:25:17+00:00",
    "summary": "Armed with a ton of new upgrades, Ferrari came to Spain full of confidence."
  },
  {
    "id": "hn:48405718",
    "domain": "股票",
    "title": "SpaceX, Other Mega IPOs Denied Fast Index Entry by S&P",
    "url": "https://www.bloomberg.com/news/articles/2026-06-04/s-p-dow-jones-keeps-megacap-ipo-rules-as-is-after-consultation",
    "source": "tristanj",
    "platform": "hackernews",
    "points": 1062,
    "published_at": "2026-06-04T22:48:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:48455233",
    "domain": "股票",
    "title": "We Think the SpaceX IPO Is Overvalued",
    "url": "https://www.morningstar.com/stocks/why-we-think-spacex-ipo-is-overvalued?content_id=20768396545",
    "source": "0xedb",
    "platform": "hackernews",
    "points": 268,
    "published_at": "2026-06-09T01:56:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:48314363",
    "domain": "股票",
    "title": "Sam Altman and Dario Amodei are both walking back AI jobs apocalypse predictions",
    "url": "https://fortune.com/2026/05/26/sam-altman-dario-amodei-walking-back-ai-jobs-apocalypse-prophecies-ipo/",
    "source": "ianrahman",
    "platform": "hackernews",
    "points": 236,
    "published_at": "2026-05-28T19:43:14+00:00",
    "summary": ""
  },
  {
    "id": "hn:48373909",
    "domain": "股票",
    "title": "Morningstar values SpaceX at $780B, half its IPO target",
    "url": "https://www.reuters.com/business/media-telecom/morningstar-values-spacex-780-billion-half-its-ipo-target-2026-06-02/",
    "source": "berkeleyjunk",
    "platform": "hackernews",
    "points": 212,
    "published_at": "2026-06-02T18:09:53+00:00",
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
    "id": "hn:48542209",
    "domain": "股票",
    "title": "Fox Is Buying Roku",
    "url": "https://www.fastcompany.com/91559558/fox-corp-buying-roku-stock-prices-fall-on-tv-streaming-merger",
    "source": "simonebrunozzi",
    "platform": "hackernews",
    "points": 79,
    "published_at": "2026-06-15T14:55:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:48446310",
    "domain": "股票",
    "title": "Italy's Bending Spoons, owner of AOL and Vimeo, files for Nasdaq IPO",
    "url": "https://www.reuters.com/legal/transactional/italys-bending-spoons-files-us-ipo-2026-06-08/",
    "source": "mmarian",
    "platform": "hackernews",
    "points": 123,
    "published_at": "2026-06-08T15:04:17+00:00",
    "summary": ""
  },
  {
    "id": "hn:48394034",
    "domain": "股票",
    "title": "The SpaceX IPO will be the theft of the century",
    "url": "https://montanaskeptic.substack.com/p/the-spacex-ipo-will-be-the-theft",
    "source": "400thecat",
    "platform": "hackernews",
    "points": 142,
    "published_at": "2026-06-04T04:52:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:48504013",
    "domain": "股票",
    "title": "SpaceX's president is floating a Tesla merger as the company begins trading",
    "url": "https://qz.com/spacex-tesla-merger-gwynne-shotwell-ipo-061226",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 72,
    "published_at": "2026-06-12T13:47:21+00:00",
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
    "id": "hn:48505968",
    "domain": "股票",
    "title": "Elon Musk Becomes First Trillionaire as SpaceX Starts Trading",
    "url": "https://www.nytimes.com/live/2026/06/12/business/spacex-ipo-elon-musk/heres-the-latest",
    "source": "droidjj",
    "platform": "hackernews",
    "points": 50,
    "published_at": "2026-06-12T16:13:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48385866",
    "domain": "股票",
    "title": "SpaceX's IPO is a disaster waiting to happen for your pension fund",
    "url": "https://www.irishtimes.com/business/2026/06/03/heavily-in-debt-loss-making-with-eyes-on-sending-people-to-mars-why-would-anyone-invest-in-spacex/",
    "source": "anonymousDan",
    "platform": "hackernews",
    "points": 92,
    "published_at": "2026-06-03T16:02:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:48506701",
    "domain": "股票",
    "title": "SpaceX increases almost 30% after biggest IPO",
    "url": "https://www.cnbc.com/2026/06/12/spacex-ipo-spcx-live-updates.html",
    "source": "somenameforme",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-06-12T17:10:07+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3774781",
    "domain": "股票",
    "title": "德银大幅上调人形机器人出货预测：2026年翻倍至5万台，2050年剑指700万台",
    "url": "https://wallstreetcn.com/articles/3774781",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T08:43:11+00:00",
    "summary": "德银将2026年全球人形机器人出货预测调高逾一倍至近5万台，2030年和2050年分别看至70万与700万台。中国是此轮出货增长的核心引擎，预计今年出货4万台，宇树等厂商领跑全球。"
  },
  {
    "id": "wscn:3774786",
    "domain": "股票",
    "title": "世界黄金协会：全球央行购金意愿创记录新高，金价回调成新一轮买入窗口？",
    "url": "https://wallstreetcn.com/articles/3774786",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T08:37:06+00:00",
    "summary": "世界黄金协会最新调查显示，74家受访央行中45%计划未来12个月增持黄金，为史上最高比例，89%预计全球央行黄金储备将持续扩张。新兴市场领衔、本币采购主导、美元储备地位受质疑，多重结构性力量叠加，而近期金价回调或正催生新一轮战略买入窗口。"
  },
  {
    "id": "wscn:3774763",
    "domain": "股票",
    "title": "创业板冲高回落涨超1%，AI硬件再集体拉升，恒科指跌超2%，科网股普跌",
    "url": "https://wallstreetcn.com/articles/3774763",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T08:32:16+00:00",
    "summary": "盘面上，个股涨跌互现，全市场超2700只个股上涨，超百股涨停。今天全市场成交3.09万亿，沪深两市成交额3.06万亿，较上一个交易日放量300余亿。板块方面，PCB、玻璃纤维、稀土、CPO、锂电池、光伏、人形机器人、存储器、超级电容概念股活跃；煤炭、海运、金融、黄金、医药、化工板块走弱。"
  },
  {
    "id": "wscn:3774791",
    "domain": "股票",
    "title": "这两类电商岗位正在被AI加速取代",
    "url": "https://wallstreetcn.com/articles/3774791",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T08:30:43+00:00",
    "summary": "客服和设计"
  },
  {
    "id": "wscn:3774784",
    "domain": "股票",
    "title": "Citrini：AMD、苹果双双押注闪存替代DRAM，内存成本或直降55倍",
    "url": "https://wallstreetcn.com/articles/3774784",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T08:27:43+00:00",
    "summary": "面对DRAM价格暴涨，AI存储向低成本闪存转移。AMD收购内存优化公司MEXT将AI驱动闪存技术引入数据中心，苹果推进端侧闪存方案。巨头看重闪存成本仅为DRAM的1/55，正重构AI存储架构。"
  },
  {
    "id": "wscn:3774767",
    "domain": "股票",
    "title": "福克斯以220亿美元拿下Roku，默多克家族开启流媒体新棋局",
    "url": "https://wallstreetcn.com/articles/3774767",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T08:27:24+00:00",
    "summary": "福克斯220亿美元豪赌：以史上最大并购押注流媒体未来。收购Roku后，合并体将一举覆盖逾1亿流媒体家庭，跻身美国电视收视第三强，超越Netflix。然而福克斯股价重挫17%，分析师援引AT&T收购时代华纳的失败前车，对这场内容与平台的豪赌能否创造价值深表疑虑。"
  },
  {
    "id": "wscn:3774789",
    "domain": "股票",
    "title": "万亿巨头的宿命：SpaceX正在成为自己的最大风险",
    "url": "https://wallstreetcn.com/articles/3774789",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T08:25:44+00:00",
    "summary": "SpaceX上市仅两天，市值盘后一度突破3万亿美元超越微软，散户资金高度集中驱动轧空狂潮。然而历史数据冷酷警示：全球市值前十巨头40年间年化回报持续跑输大盘。马斯克\"2031年万亿营收\"豪言更触发IPO静默期合规红线，6月底解禁窗口将是这场盛宴的真正压力测试。"
  },
  {
    "id": "wscn:3774788",
    "domain": "股票",
    "title": "韩国银行全面收紧\"借钱炒股\"，高盛建议客户对冲KOSPI下行风险",
    "url": "https://wallstreetcn.com/articles/3774788",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T08:17:39+00:00",
    "summary": "韩国股市暗流涌动：银行正全面收紧信用贷款与透支账户，切断散户借钱炒股的资金链；与此同时，400亿美元杠杆ETF叠加期权隐含波动率从20%飙升至80%，令市场对价格冲击极度敏感。高盛警告，AI与半导体逻辑未变，但一旦信贷收缩与杠杆再平衡同步引爆，建议保留核心仓位，同时用衍生品覆盖短期回撤风险。"
  },
  {
    "id": "wscn:3774790",
    "domain": "股票",
    "title": "加码空间智能 卓越睿新引入World Labs世界模型",
    "url": "https://wallstreetcn.com/articles/3774790",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T08:07:18+00:00",
    "summary": "在刚刚举行的2026北京智源大会上，\"世界模型\"被业界视为AI从二维感知向三维空间理解跃迁的关键一跃..."
  },
  {
    "id": "wscn:3774774",
    "domain": "股票",
    "title": "美伊协议达成，亚洲“股债汇”齐升：日股首破7万点，越南股市外资单日净流入创六年新高，印度汇率走高",
    "url": "https://wallstreetcn.com/articles/3774774",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T07:59:38+00:00",
    "summary": "美伊局势缓和持续提振市场，日经225指数突破70000点大关，创下历史新高。越南股市外资单日净流入达1.604亿美元，为近六年最高纪录；印度外国投资者单日购入印度债券逾1400亿卢比（约15亿美元），创历史最高单日购买量。美股期货小幅走低，欧股小幅高开，布伦特原油跌破每桶83美元。现货黄金上涨0.3%。"
  },
  {
    "id": "wscn:3774783",
    "domain": "股票",
    "title": "Anthropic高管赴白宫谈判，Claude Fable 5或以新方式重新上线",
    "url": "https://wallstreetcn.com/articles/3774783",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T07:33:34+00:00",
    "summary": "针对美国政府以\"安全护栏可被绕过\"为由对Claude Fable 5实施出口管制，Anthropic高管赴白宫谈判。知情人士称，美商务部愿寻找方式让Fable 5重新上线，前提是Anthropic完全解决政府担忧。Anthropic称政府担忧被夸大，模型目前仍被禁用。"
  },
  {
    "id": "wscn:3774775",
    "domain": "股票",
    "title": "OpenAI去年烧钱340亿美元，预计净亏损385亿，亏损额同比扩大近8倍",
    "url": "https://wallstreetcn.com/articles/3774775",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T07:33:23+00:00",
    "summary": "OpenAI 2025年净亏损高达385亿美元，是2024年的近8倍——但这场\"账面惊雷\"绝大部分源于公司结构转型触发的逾300亿元非现金冲销，剔除后实际运营亏损约80亿美元。与此同时，其营收两年翻超2.5倍至130亿美元，并已秘密向SEC递交IPO文件，估值7300亿美元的AI巨头正加速奔向资本市场。"
  },
  {
    "id": "wscn:3774647",
    "domain": "股票",
    "title": "铜箔热潮：英伟达亲自下场抢购，2026年缺口1500吨",
    "url": "https://wallstreetcn.com/premium/articles/3774647?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T07:32:36+00:00",
    "summary": "HVLP4铜箔正成为2026年新瓶颈——预计缺口1500吨，2027年扩至2500吨。英伟达罕见绕过CCL厂商，直接锁定铜箔与玻纤布产能，并向谷歌、AWS、Meta施压协同备货。供需失衡短期难解，少数掌握关键材料产能的供应商坐拥极强议价权。"
  },
  {
    "id": "wscn:3774782",
    "domain": "股票",
    "title": "越来越近，却始终签不成！大摩：美伊协议难产概率高达70%",
    "url": "https://wallstreetcn.com/articles/3774782",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T07:26:46+00:00",
    "summary": "摩根大通最新警告：美伊谈判深陷\"永远接近、却从不正式签署\"的怪圈，协议达成概率仅一成，而延续僵局的概率高达七成。布伦特原油虽从冲突高点118美元跌至87美元，市场却可能正在低估尾部风险。"
  },
  {
    "id": "wscn:3774780",
    "domain": "股票",
    "title": "DeepSeek首次融资落地：募集超500亿，估值超3300亿元",
    "url": "https://wallstreetcn.com/articles/3774780",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T07:17:38+00:00",
    "summary": "DeepSeek完成首轮外部融资，创始人梁文锋个人出资200亿元，为本轮最大投资方；腾讯、宁德时代、京东、网易及IDG资本等跟投。为确保梁文锋的绝对控制权，外部投资者资金须注入由其管理的有限合伙企业，股份锁定期五年。国家人工智能产业投资基金为唯一例外，直接注资10亿元并享有投票权。"
  },
  {
    "id": "wscn:3774778",
    "domain": "股票",
    "title": "黄金最坏时刻已经过去？巴克莱高喊“抄底”，花旗上调目标价",
    "url": "https://wallstreetcn.com/articles/3774778",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T07:03:28+00:00",
    "summary": "巴克莱与花旗同日喊多！黄金历经25%深度调整，美伊谅解备忘录签署在即，油价预期全面逆转，通胀逆风趋于消散。花旗将3个月目标价升至4500美元，6至12个月看涨5000美元；巴克莱断言：此轮是\"价格重置\"，不是牛市终结。"
  },
  {
    "id": "wscn:3774777",
    "domain": "股票",
    "title": "日本央行副行长内田真一：将继续根据经济和物价情况加息",
    "url": "https://wallstreetcn.com/articles/3774777",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T07:01:57+00:00",
    "summary": "更多消息，持续更新中"
  },
  {
    "id": "wscn:3773647",
    "domain": "股票",
    "title": "800V多空激辩：能否重构兆瓦级算力的未来主权？",
    "url": "https://wallstreetcn.com/premium/articles/3773647?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T06:35:50+00:00",
    "summary": "800V高压直流（HVDC）供电架构正从“实验室概念”加速迈向产业化拐点，这是AI数据中心机架功率密度突破600kW后的物理必然选择。英伟达目标2027年实现规模化商用，以支撑1MW及以上超高功率密度IT机架。"
  },
  {
    "id": "wscn:3774773",
    "domain": "股票",
    "title": "对冲基金经理Gavin Baker：教科书式的IPO执行，SpaceX要做“太阳系时代的东印度公司”，成就“史上最伟大”",
    "url": "https://wallstreetcn.com/articles/3774773",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T06:32:58+00:00",
    "summary": "SpaceX以\"教科书式\"IPO强势登场，两日涨逾30%、全程无剧烈波动。对冲基金名将Gavin Baker重仓押注，将其终极形态类比为\"太阳系时代的东印度公司\"——轨道算力成本仅地面一半，Cursor已渗透逾半数财富500强，他直言：这或许是人类史上最重要的企业，没有之一。"
  },
  {
    "id": "wscn:3774772",
    "domain": "股票",
    "title": "光互联市场引爆上游争夺战，AMD扫货CW激光器",
    "url": "https://wallstreetcn.com/articles/3774772",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T06:01:30+00:00",
    "summary": "据报道，AMD正加速采购CW激光器以摆脱英伟达生态依赖。机构预测CPO/NPO市场将从2025年约1亿美元飙升至2030年逾390亿美元，而所有硅光子解决方案，包括CPO和NPO架构，均需要外部CW激光器作为光源支撑。目前全球CW激光器市场高度集中，Lumentum产能已排期至2028年，供应极度紧张。"
  },
  {
    "id": "hn:48193111",
    "domain": "股票",
    "title": "Anthropic Is Preparing for IPO and We Should Be Worried",
    "url": "https://www.vincentschmalbach.com/anthropic-ipo-developers-should-be-worried-v2/",
    "source": "vincent_s",
    "platform": "hackernews",
    "points": 89,
    "published_at": "2026-05-19T13:30:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:48506306",
    "domain": "股票",
    "title": "SpaceX vaults over $2T valuation as stock jumps after record IPO",
    "url": "https://www.reuters.com/legal/transactional/after-record-ipo-musks-spacex-faces-next-test-market-debut-2026-06-12/",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-06-12T16:39:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:48499349",
    "domain": "股票",
    "title": "StonkRider – Ride any stock chart",
    "url": "https://stonkrider.com/",
    "source": "nreece",
    "platform": "hackernews",
    "points": 42,
    "published_at": "2026-06-12T02:58:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:48390053",
    "domain": "股票",
    "title": "Iran war drains US oil stocks to lowest level since 2004",
    "url": "https://www.ft.com/content/d0be73c8-b8d8-4ffd-874e-e97a6ecffef7",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 61,
    "published_at": "2026-06-03T21:06:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:48505175",
    "domain": "股票",
    "title": "SpaceX makes largest ever stock market debut at $1.77T valuation",
    "url": "https://www.theguardian.com/science/2026/jun/12/spacex-stock-price-ipo-spcx",
    "source": "thomascountz",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-06-12T15:10:16+00:00",
    "summary": ""
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
    "id": "hn:48452224",
    "domain": "股票",
    "title": "OpenAI Confidentially Files for IPO",
    "url": "https://www.cnbc.com/2026/06/08/openai-confidentially-files-for-ipo-prepping-wall-street-for-ai-debut.html",
    "source": "rvz",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-06-08T21:16:20+00:00",
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
    "id": "hn:48496263",
    "domain": "股票",
    "title": "Musk's SpaceX prices record $75B IPO at $135 a share",
    "url": "https://www.reuters.com/world/musks-spacex-prices-record-75-billion-ipo-135-share-2026-06-11/",
    "source": "TechTechTech",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-06-11T20:53:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:48497351",
    "domain": "股票",
    "title": "SpaceX officially prices shares at $135 in the largest IPO ever",
    "url": "https://techcrunch.com/2026/06/11/spacex-officially-prices-shares-at-135-in-the-largest-ipo-ever/",
    "source": "7777777phil",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-06-11T22:36:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:48451099",
    "domain": "股票",
    "title": "Why Morningstar believes the SpaceX IPO is overvalued",
    "url": "https://www.morningstar.com/stocks/why-we-think-spacex-ipo-is-overvalued",
    "source": "ForHackernews",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-06-08T20:07:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:48482342",
    "domain": "股票",
    "title": "US stock market to stop shrinking for first time in 23 years",
    "url": "https://www.ft.com/content/f7dae4e1-d650-45ab-ac97-043c7a965d24",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-06-10T20:37:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:48391046",
    "domain": "股票",
    "title": "We Uncovered a Hidden Wealth Transfer in the SpaceX IPO. You're Holding the Bag [video]",
    "url": "https://www.youtube.com/watch?v=sYA-z0Y8WRQ",
    "source": "CharlesW",
    "platform": "hackernews",
    "points": 29,
    "published_at": "2026-06-03T22:32:44+00:00",
    "summary": ""
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
    "id": "hn:48404734",
    "domain": "股票",
    "title": "Fidelity lowers SpaceX IPO entry requirement from $500,000 to just $2,000",
    "url": "https://finance.yahoo.com/markets/stocks/articles/fidelity-cuts-spacex-ipo-eligibility-183319186.html",
    "source": "tcp_handshaker",
    "platform": "hackernews",
    "points": 23,
    "published_at": "2026-06-04T21:15:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:48383625",
    "domain": "股票",
    "title": "Dell inks $9.7B Pentagon contract after Trump acquires stock",
    "url": "https://www.washingtonpost.com/politics/2026/05/28/dell-inks-97-billion-pentagon-contract-after-trump-acquires-stock-praises-company/",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-06-03T13:19:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:48436328",
    "domain": "股票",
    "title": "Musk's SpaceX IPO Narrative Is a Whole New Level of Bullshit",
    "url": "https://text.tchncs.de/chronik-des-laufenden-wahnsinns/h1elon-musk-has-spouted-his-fair-share-of-bullshit-but-his-latest-claims-about",
    "source": "doener",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-06-07T16:24:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:48364055",
    "domain": "金融",
    "title": "Can the stockmarket swallow Anthropic, SpaceX and OpenAI?",
    "url": "https://www.economist.com/finance-and-economics/2026/06/01/can-the-stockmarket-swallow-anthropic-spacex-and-openai",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 724,
    "published_at": "2026-06-01T23:45:46+00:00",
    "summary": ""
  },
  {
    "id": "hn:48454210",
    "domain": "金融",
    "title": "Federal judge blocks H1B visa $100K fee",
    "url": "https://www.alaskasnewssource.com/2026/06/08/federal-judge-blocks-h1-b-visa-100k-fee/",
    "source": "naturalmovement",
    "platform": "hackernews",
    "points": 191,
    "published_at": "2026-06-09T00:01:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:48507248",
    "domain": "金融",
    "title": "Tesla Full Self Driving uses bicycle lane in official Denmark approval video",
    "url": "https://politiken.dk/danmark/forbrug/biler/art10875514/Allerede-12-sekunder-inde-i-PR-videoen-beg%C3%A5r-selvk%C3%B8rende-Tesla-f%C3%B8rste-fejl-i-k%C3%B8benhavnsk-gade-%E2%80%93-men-det-bliver-v%C3%A6rre-endnu",
    "source": "Veserv",
    "platform": "hackernews",
    "points": 122,
    "published_at": "2026-06-12T17:49:48+00:00",
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
    "id": "hn:48479537",
    "domain": "金融",
    "title": "Meta steals a tactic from Tesla and builds data centers in tents",
    "url": "https://techcrunch.com/2026/06/04/meta-steals-a-tactic-from-tesla-and-builds-data-centers-in-tents/",
    "source": "gnabgib",
    "platform": "hackernews",
    "points": 105,
    "published_at": "2026-06-10T17:18:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:48546358",
    "domain": "金融",
    "title": "US Government Reportedly Allowing Federal Data Center Rules to Expire",
    "url": "https://gizmodo.com/us-government-reportedly-allowing-federal-data-center-rules-to-expire-2000772083",
    "source": "01-_-",
    "platform": "hackernews",
    "points": 37,
    "published_at": "2026-06-15T20:06:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48360414",
    "domain": "金融",
    "title": "Making Debian or Fedora persistent live images",
    "url": "https://sigwait.org/~alex/blog/2026/05/28/smdBC8.html",
    "source": "henry_flower",
    "platform": "hackernews",
    "points": 89,
    "published_at": "2026-06-01T18:02:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:48483445",
    "domain": "金融",
    "title": "US President says 'I love the inflation'",
    "url": "https://www.cnbc.com/2026/06/10/trump-inflation-cpi-iran-oil.html",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 66,
    "published_at": "2026-06-10T22:12:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:48518434",
    "domain": "金融",
    "title": "Gas Prices Wipe Out More Than a Year of Wage Gains",
    "url": "https://www.wsj.com/economy/inflation-wages-american-workers-cbe3f187",
    "source": "karakoram",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-06-13T15:49:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:48523232",
    "domain": "金融",
    "title": "Monero Inflation Checker",
    "url": "https://www.moneroinflation.com/",
    "source": "Cider9986",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-06-14T01:16:10+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.14798",
    "domain": "金融",
    "title": "Two Sides of Schur Damping: High-Dimensional Pseudo-Likelihoods and Portfolio Allocation",
    "url": "https://arxiv.org/abs/2606.14798",
    "source": "Peter Cotton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T04:00:00+00:00",
    "summary": "arXiv:2606.14798v1 Announce Type: new Abstract: Two communities that rarely cite each other -- spatial statisticians fitting high-dimensional weather fields, and quantitative investors building portfo"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.14830",
    "domain": "金融",
    "title": "Pricing Excess-of-Loss Reinsurance and CAT Bonds under Climate Uncertainty: A Cox Process Framework with Temperature-Dependent Stochastic Intensity",
    "url": "https://arxiv.org/abs/2606.14830",
    "source": "Nader Karimi, Foad Shokrollahi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T04:00:00+00:00",
    "summary": "arXiv:2606.14830v1 Announce Type: new Abstract: This paper develops a climate-aware pricing framework for excess-of-loss (XL) reinsurance contracts and catastrophe (CAT) bonds under non-stationary cat"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.15089",
    "domain": "金融",
    "title": "A Machine-Checked It\\^o Calculus for Brownian Motion",
    "url": "https://arxiv.org/abs/2606.15089",
    "source": "Raphael Coelho",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T04:00:00+00:00",
    "summary": "arXiv:2606.15089v1 Announce Type: new Abstract: We present a machine-checked development of the $L^2$ It\\^o calculus of Brownian motion on a bounded time interval $[0,T]$, formalized in Lean 4 on top "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.15473",
    "domain": "金融",
    "title": "Belief at Risk: Quantifying Agentic AI Model Risk with LLM-Inferred Bayesian State Filters",
    "url": "https://arxiv.org/abs/2606.15473",
    "source": "Matthew Francis Dixon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T04:00:00+00:00",
    "summary": "arXiv:2606.15473v1 Announce Type: new Abstract: Agentic AI systems create model risk because uncertain beliefs are coupled to autonomous actions. This paper develops a mathematical framework for quant"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.15502",
    "domain": "金融",
    "title": "Fast, Reliable, and Error-Bounded Option Pricing with Pretrained Neural Networks: A GJR--GARCH Study",
    "url": "https://arxiv.org/abs/2606.15502",
    "source": "Thijs van den Berg",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T04:00:00+00:00",
    "summary": "arXiv:2606.15502v1 Announce Type: new Abstract: Many models in quantitative finance have no closed-form option prices and rely on slow, noisy Monte Carlo simulation; neural surrogates restore speed bu"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.15715",
    "domain": "金融",
    "title": "Trading in the Sunshine or in the Shade: Market Impact and Adverse Selection on Hyperliquid",
    "url": "https://arxiv.org/abs/2606.15715",
    "source": "Davide Barone, Fabrizio Lillo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T04:00:00+00:00",
    "summary": "arXiv:2606.15715v1 Announce Type: new Abstract: Sunshine trading theory predicts that publicly disclosing trading intentions can reduce adverse selection and attract liquidity provision, lowering exec"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.15755",
    "domain": "金融",
    "title": "A Multiplex Network Hawkes Model for Systemic Risk Measurement",
    "url": "https://arxiv.org/abs/2606.15755",
    "source": "Mante Zelvyte, Jim E. Griffin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T04:00:00+00:00",
    "summary": "arXiv:2606.15755v1 Announce Type: new Abstract: We introduce the Multiplex Network Hawkes model, which extends the network Hawkes framework of Linderman & Adams (2014) by allowing multiple excitation "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.15960",
    "domain": "金融",
    "title": "Chaining Tasks, Redefining Work: A Theory of AI Automation",
    "url": "https://arxiv.org/abs/2606.15960",
    "source": "Mert Demirer, John J. Horton, Nicole Immorlica, Brendan Lucier, Peyman Shahidi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T04:00:00+00:00",
    "summary": "arXiv:2606.15960v1 Announce Type: new Abstract: Production is a sequence of steps that can be executed (1) manually, (2) augmented with AI, or (3) fully automated within contiguous AI-executed steps c"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.15999",
    "domain": "金融",
    "title": "U.S. Policies Unintentionally Accelerated China's Open AI Ecosystems",
    "url": "https://arxiv.org/abs/2606.15999",
    "source": "Wang Jin, Nadav Kunievsky, Bowen Lou, Tianshu Sun, James Evans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T04:00:00+00:00",
    "summary": "arXiv:2606.15999v1 Announce Type: new Abstract: Over the past decade, U.S. policies have increasingly aimed to preserve artificial intelligence (AI) leadership by promoting domestic free-market polici"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.16269",
    "domain": "金融",
    "title": "Revisiting Trade-sign Long-memory and Square-root Law price impact",
    "url": "https://arxiv.org/abs/2606.16269",
    "source": "Chris Angstmann, Tim Gebbie",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T04:00:00+00:00",
    "summary": "arXiv:2606.16269v1 Announce Type: new Abstract: Starting with a coupled discrete reaction--diffusion formulation for the lit and latent order books with non-uniformly sampled event times and meta-orde"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.16469",
    "domain": "金融",
    "title": "Probabilistic Identification of Technology Tipping Points in Deeply Decarbonised Energy Systems",
    "url": "https://arxiv.org/abs/2606.16469",
    "source": "Gian M\\\"uller, Thomas Sch\\\"ob, Jann M. Weinand, Iain Staffell",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T04:00:00+00:00",
    "summary": "arXiv:2606.16469v1 Announce Type: new Abstract: Energy policy is often guided by a small set of least-cost pathways to net-zero emissions, despite wide uncertainty in technology performance, fuel pric"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.16493",
    "domain": "金融",
    "title": "Forward Hedging Reshapes Incentive Provision",
    "url": "https://arxiv.org/abs/2606.16493",
    "source": "Ren\\'e A\\\"id, Nizar Touzi, St\\'ephane Villeneuve",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T04:00:00+00:00",
    "summary": "arXiv:2606.16493v1 Announce Type: new Abstract: We study how forward hedging reshapes incentive provision inside the firm. We consider a risk-averse producer facing demand and production risk that can"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.16619",
    "domain": "金融",
    "title": "Expanding the rough Heston model in $H$",
    "url": "https://arxiv.org/abs/2606.16619",
    "source": "Paul P. Hager, D\\\"orte Kreher",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T04:00:00+00:00",
    "summary": "arXiv:2606.16619v1 Announce Type: new Abstract: We study the dependence of the fractional Riccati equation in the rough Heston model on the Hurst parameter $H$. For each expansion point $H_0\\in(-1/2,1"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.16840",
    "domain": "金融",
    "title": "Crashing Together, Rallying Apart: Dynamic Conditional Tail Dependence in Cryptocurrency Markets",
    "url": "https://arxiv.org/abs/2606.16840",
    "source": "Rama Siva Sarwari Mallela, Manuele Leonelli",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T04:00:00+00:00",
    "summary": "arXiv:2606.16840v1 Announce Type: new Abstract: Cryptocurrency markets are prone to violent, synchronised drawdowns, challenging the claim that a basket of crypto-assets offers genuine internal divers"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.17032",
    "domain": "金融",
    "title": "Sharpe Ratio and Return-VaR Ratio Maximization for Option Portfolios with Skew-Elliptical $t$ Underlying Returns",
    "url": "https://arxiv.org/abs/2606.17032",
    "source": "Kyle Sung, Traian A. Pirvu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T04:00:00+00:00",
    "summary": "arXiv:2606.17032v1 Announce Type: new Abstract: We provide a formulation for optimal option portfolios under Sharpe Ratio maximization when the underlying returns follow a skew-elliptical t-distributi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.14887",
    "domain": "金融",
    "title": "Estimating Sloppy Directions via KDE: The Case of Kirman's Ants",
    "url": "https://arxiv.org/abs/2606.14887",
    "source": "Karl Naumann-Woleske",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T04:00:00+00:00",
    "summary": "arXiv:2606.14887v1 Announce Type: cross Abstract: Models whose predictions depend on only a handful of well-constrained parameter combinations, termed sloppy models, are ubiquitous in nonlinear stocha"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.15452",
    "domain": "金融",
    "title": "PHINN: Persistent Homology Inspired Neural Network for Rare-Event Time Series Generation",
    "url": "https://arxiv.org/abs/2606.15452",
    "source": "Emre Yusuf, Ren Takahashi, Jayabrata Bhaduri",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T04:00:00+00:00",
    "summary": "arXiv:2606.15452v1 Announce Type: cross Abstract: Rare events in time series are critical to model but hard to learn due to data scarcity. Current generative models struggle with extreme values. We ob"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.15701",
    "domain": "金融",
    "title": "Robust Transformer-Based One-Step Stock Index Forecasting via Shifted Data Augmentation",
    "url": "https://arxiv.org/abs/2606.15701",
    "source": "Tien Thanh Thach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T04:00:00+00:00",
    "summary": "arXiv:2606.15701v1 Announce Type: cross Abstract: Transformers have shown remarkable success in sequence modeling, yet their direct application to financial time series remains challenging due to nois"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.15757",
    "domain": "金融",
    "title": "Towards a Theory of Modular Natives: Explaining Superscaling, China's Greatest Innovation Yet",
    "url": "https://arxiv.org/abs/2606.15757",
    "source": "Bent Flyvbjerg, Alexander Budzier, Maria Christodoulou",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T04:00:00+00:00",
    "summary": "arXiv:2606.15757v1 Announce Type: cross Abstract: First, we present a new theory of \"modular natives.\" A modular native is a basic building block that is born modular, e.g., a solar cell. The theory p"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.15936",
    "domain": "金融",
    "title": "A game of information",
    "url": "https://arxiv.org/abs/2606.15936",
    "source": "Dorje C. Brody",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T04:00:00+00:00",
    "summary": "arXiv:2606.15936v1 Announce Type: cross Abstract: A game of information concerns two players transmitting messages that are obscured by noise. A receiver digests the combination of the two information"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.16326",
    "domain": "金融",
    "title": "Gaming-Resistant Insurance Contracts for Autonomous AI Agents: Strategy-Proof Toll Mechanism Design",
    "url": "https://arxiv.org/abs/2606.16326",
    "source": "Hao-Hsuan Chen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T04:00:00+00:00",
    "summary": "arXiv:2606.16326v1 Announce Type: cross Abstract: Paper A defines a time-consistent actuarial runtime that prices each side-effect-bearing action against a contractually fixed safe default and gates e"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.16961",
    "domain": "金融",
    "title": "Beyond the Smile: A Hybrid Convolutional VAE for Crypto Volatility Surfaces",
    "url": "https://arxiv.org/abs/2606.16961",
    "source": "Sadanand Singh, Allam Reddy, Manan Chopra",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T04:00:00+00:00",
    "summary": "arXiv:2606.16961v1 Announce Type: cross Abstract: We present a convolutional variational autoencoder for cryptocurrency implied-volatility surfaces, together with a deployable predictor that combines "
  },
  {
    "id": "rss:https://arxiv.org/abs/2209.01235",
    "domain": "金融",
    "title": "Smiles in Profiles: Improving Efficiency While Reducing Disparities in Online Marketplaces",
    "url": "https://arxiv.org/abs/2209.01235",
    "source": "Susan Athey, Dean Karlan, Emil Palikot, Yuan Yuan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T04:00:00+00:00",
    "summary": "arXiv:2209.01235v5 Announce Type: replace Abstract: Online platforms often have conflicting goals: they face tradeoffs between increasing efficiency and reducing disparities, where the latter may rela"
  },
  {
    "id": "rss:https://arxiv.org/abs/2407.06619",
    "domain": "金融",
    "title": "CAESar: Conditional Autoregressive Expected Shortfall",
    "url": "https://arxiv.org/abs/2407.06619",
    "source": "Federico Gatta, Fabrizio Lillo, Piero Mazzarisi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T04:00:00+00:00",
    "summary": "arXiv:2407.06619v2 Announce Type: replace Abstract: In financial risk management, Value at Risk (VaR) estimates potential portfolio losses but fails to account for losses beyond a certain threshold. E"
  },
  {
    "id": "rss:https://arxiv.org/abs/2410.20060",
    "domain": "金融",
    "title": "Constrained portfolio optimization in a life-cycle model: A deep pricing kernel approach",
    "url": "https://arxiv.org/abs/2410.20060",
    "source": "Wenyuan Li, Pengyu Wei",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T04:00:00+00:00",
    "summary": "arXiv:2410.20060v3 Announce Type: replace Abstract: This paper considers the constrained portfolio optimization in a generalized life-cycle model. The individual with a stochastic income manages a por"
  },
  {
    "id": "rss:https://arxiv.org/abs/2508.20225",
    "domain": "金融",
    "title": "Optimal Quoting under Adverse Selection and Price Reading",
    "url": "https://arxiv.org/abs/2508.20225",
    "source": "Alexander Barzykin, Philippe Bergault, Olivier Gu\\'eant, Malo Lemmel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T04:00:00+00:00",
    "summary": "arXiv:2508.20225v5 Announce Type: replace Abstract: Over the past decade, many dealers have implemented algorithmic models to automatically respond to RFQs and manage flows originating from their elec"
  },
  {
    "id": "rss:https://arxiv.org/abs/2601.04608",
    "domain": "金融",
    "title": "Forecasting the U.S. Treasury Yield Curve: A Distributionally Robust Machine Learning Approach for Interest Rate Risk Management",
    "url": "https://arxiv.org/abs/2601.04608",
    "source": "Jinjun Liu, Ming-Yen Cheng",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T04:00:00+00:00",
    "summary": "arXiv:2601.04608v2 Announce Type: replace Abstract: U.S. Treasury yields are central to global asset pricing but are noisy and subject to policy uncertainty, supply-demand forces, and behavioral effec"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.18343",
    "domain": "金融",
    "title": "Explicit Rational Formulae for Bachelier (Normal) Implied Volatility",
    "url": "https://arxiv.org/abs/2605.18343",
    "source": "Fabien Le Floc'h",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T04:00:00+00:00",
    "summary": "arXiv:2605.18343v4 Announce Type: replace Abstract: We present two explicit rational formulae for Bachelier, or normal, implied volatility. The formulae take the option price, forward, strike, and exp"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.09025",
    "domain": "金融",
    "title": "Continuous Cash-Overlay Filters for a Static Growth--Defensive Risk Sleeve: Slow-Tail Compensation, V-Shape Crash Brakes, Walk-Forward Validation, and Max-Cash Combination",
    "url": "https://arxiv.org/abs/2606.09025",
    "source": "Zheli Xiong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T04:00:00+00:00",
    "summary": "arXiv:2606.09025v2 Announce Type: replace Abstract: This paper studies a modular cash-overlay rule for allocating between a fixed growth-defensive risky sleeve R and interest-bearing cash C. The risky"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.12717",
    "domain": "金融",
    "title": "Mixture-Preserving, Arbitrage-Free Interpolation for Volatility-Surface Models",
    "url": "https://arxiv.org/abs/2606.12717",
    "source": "Thijs van den Berg",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T04:00:00+00:00",
    "summary": "arXiv:2606.12717v2 Announce Type: replace Abstract: Given risk-neutral densities of a tradeable forward, fitted as $N$-component mixtures at a finite set of expiration pillars, we look for a continuou"
  },
  {
    "id": "hn:48384810",
    "domain": "金融",
    "title": "Tesla retroactively added 'supervised' to FSD contracts owners signed years ago",
    "url": "https://electrek.co/2026/06/03/tesla-retroactively-modified-fsd-contracts-supervised/",
    "source": "breve",
    "platform": "hackernews",
    "points": 73,
    "published_at": "2026-06-03T14:43:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:48406282",
    "domain": "金融",
    "title": "S&P Global keeps fast index entry rules unchanged as SpaceX listing looms",
    "url": "https://www.reuters.com/business/finance/sp-global-keeps-fast-entry-proposal-unchanged-spacex-listing-looms-2026-06-04/",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 49,
    "published_at": "2026-06-04T23:55:20+00:00",
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
    "id": "hn:48451917",
    "domain": "金融",
    "title": "Federal judge rules Trump's $100k fee for H-1B visas unlawful",
    "url": "https://www.theguardian.com/us-news/2026/jun/08/trump-h-1b-visa-fee-invalidated",
    "source": "xpl",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-06-08T20:57:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48476514",
    "domain": "金融",
    "title": "GnuCash is right. It's also why I built my own finance app",
    "url": "https://k-id.app/blog/gnucash-is-right/",
    "source": "tinosar",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-06-10T14:06:22+00:00",
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
    "id": "hn:48449003",
    "domain": "金融",
    "title": "Half of Americans say they're worse off financially than a year ago",
    "url": "https://www.cbsnews.com/news/americans-worse-off-financially-year-ago-fed-survey/",
    "source": "tcp_handshaker",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-06-08T18:12:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:48488805",
    "domain": "金融",
    "title": "Feds will abruptly dismantle system monitoring climate change, oceans",
    "url": "https://www.usatoday.com/story/news/nation/2026/06/11/climate-change-ocean-monitoring-system-dismantled/90378309007/",
    "source": "OutOfHere",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-06-11T11:12:24+00:00",
    "summary": ""
  },
  {
    "id": "hn:48436542",
    "domain": "金融",
    "title": "Ripping a DVD, a federal crime in 1999, requires $22 and free software in 2026",
    "url": "https://ringmast4r.substack.com/p/in-1999-this-was-a-federal-crime",
    "source": "akkartik",
    "platform": "hackernews",
    "points": 30,
    "published_at": "2026-06-07T16:48:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:48491301",
    "domain": "金融",
    "title": "Craig Federighi Details Apple's Collaboration with Google for Siri AI in iOS 27",
    "url": "https://9to5mac.com/2026/06/08/craig-federighi-details-apples-collaboration-with-google-for-siri-ai-in-ios-27/",
    "source": "tambourine_man",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-06-11T15:01:26+00:00",
    "summary": ""
  }
]
```
