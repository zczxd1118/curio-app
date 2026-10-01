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

- 今日日期：`2026-10-01`
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
  "date": "2026-10-01",
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
    "points": 2024472,
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
    "points": 1920752,
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
    "points": 1351072,
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
    "points": 1299793,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1o19aBJEAo",
    "domain": "AI",
    "title": "【全100集】吊打付费！目前B站最全最细的AI真人短剧制作保姆级教程！2026最新版AI视频生成全流程教学！七天就能从小白到大神！带你从入门到精通实现商业变现！",
    "url": "http://www.bilibili.com/video/av116492733518306",
    "source": "AI绘画学习教程",
    "platform": "bilibili",
    "points": 1273408,
    "published_at": "2026-05-04T08:11:00+00:00",
    "summary": "持续更新中！资料和工具在评论区哦"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 1040126,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1aeLqzUE6L",
    "domain": "AI",
    "title": "10分钟讲清楚 Prompt, Agent, MCP 是什么",
    "url": "http://www.bilibili.com/video/av114410228025650",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 893384,
    "published_at": "2025-05-01T09:00:00+00:00",
    "summary": "up的科学星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV139bD6gEa8",
    "domain": "AI",
    "title": "Pi 大道至简，超越Codex和Claude Code的极简Agent，保姆级全攻略， 一期视频精通",
    "url": "http://www.bilibili.com/video/av117104095268420",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 837424,
    "published_at": "2026-08-16T07:53:45+00:00",
    "summary": "Pi是近期热度超高的AI Agent。用四个字形容那就是大道至简。 Pi只有四个默认工具，（读文件，写文件，改文件，运行命令），系统提示词也仅仅只有一千Token。极致的精简带来了极致效率提升，在多项权威基准测试里，Pi 的代码质量，工作速度，成本等方面多方面超过主流Agent Codex和Claude Code。 Pi还有极其开放的插件生态，可以自己编写插件扩展Pi的能力。"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 822147,
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
    "points": 699428,
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
    "points": 674173,
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
    "points": 591011,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV1eK5DzHEWu",
    "domain": "AI",
    "title": "MCP实战指南，mcp视频教程，2小时学透mcp",
    "url": "http://www.bilibili.com/video/av114380213586544",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 417035,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 416654,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1vG8QzcE5X",
    "domain": "AI",
    "title": "Claude使用指南，claude code零基础教程，claude code安装配置到实战",
    "url": "http://www.bilibili.com/video/av114933744272468",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 355493,
    "published_at": "2025-07-30T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从概念到安装，再到Claude Code的具体使用，开发效率原地起飞！"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 302342,
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
    "points": 299389,
    "published_at": "2025-04-15T00:59:13+00:00",
    "summary": "MCP终极指南 - 带你深入掌握MCP（基础篇）\n\n时间轴：\n01:05 MCP简要介绍\n02:47 安装 MCP Host（Cline）\n03:15 配置 Cline 用的 API Key\n06:01 第一个 MCP 问题\n06:31 概念解释：MCP Server 和 Tool\n09:13 配置 MCP Server\n14:19 使用 MCP Server\n15:24 MCP 交互流程详解\n1"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 223943,
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
    "points": 191638,
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
    "points": 182415,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1WWYE6LEzx",
    "domain": "AI",
    "title": "黑马程序员2026全网最夯VibeCoding零基础入门到实战项目开发全套视频教程，AI辅助编程从入门到实战，涵盖Claude Code、DeepSeek等内容",
    "url": "http://www.bilibili.com/video/av117251667724450",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 177470,
    "published_at": "2026-09-14T01:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260914\n2026黑马程序员AI智能应用开发学习路线图\nhttps://www.bilibili.com/opus/1156896913511940102\n如何下载资料\nhttps://www.bilibili.com/read/cv7881295/\n学习+球球群625260577，告别孤单，共同进步！\n\n【AI智能"
  },
  {
    "id": "bvid:BV1RNTtzMENj",
    "domain": "AI",
    "title": "从零编写MCP并发布上线，超简单！手把手教程",
    "url": "http://www.bilibili.com/video/av114630814862349",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 158170,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1eYPpeWEnT",
    "domain": "AI",
    "title": "Cursor + MCP = 王炸！彻底颠覆我的Cursor工作流，效率直接起飞",
    "url": "http://www.bilibili.com/video/av114073660301264",
    "source": "御风大世界",
    "platform": "bilibili",
    "points": 151525,
    "published_at": "2025-02-27T03:19:03+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 93862,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1K6YM69ESq",
    "domain": "AI",
    "title": "AI+网络安全实战：从Agent入门到AI智能体挖漏洞教程！网络安全|信息安全|黑客技术|渗透测试|SRC漏洞挖掘|AI审计|HVV护网行动|靶场练习-码士集团",
    "url": "http://www.bilibili.com/video/av117247037213495",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 82799,
    "published_at": "2026-09-10T13:47:24+00:00",
    "summary": "这套课程围绕「AI+网络安全」展开，从AI智能体基础入门，到WorkBuddy、Trae等主流Agent工具的实际应用，再到API-Key接入、Skill使用等核心能力，逐步进入AI漏洞挖掘、代码审计、CTF题目分析等安全实战场景。同时结合SRC漏洞挖掘、HVV护网、安全竞赛以及网络安全就业方向，帮助你系统了解AI在网络安全学习、开发与实战中的应用方式。适合网络安全初学者、安全从业者以及希望利用A"
  },
  {
    "id": "bvid:BV1A24y1J7Dt",
    "domain": "AI",
    "title": "如何在VS Code中使用Cursor自动生成代码",
    "url": "http://www.bilibili.com/video/av781409810",
    "source": "许你再少年",
    "platform": "bilibili",
    "points": 74466,
    "published_at": "2023-03-23T11:32:23+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1aQMX6oEni",
    "domain": "AI",
    "title": "【Agent面经】目前B站最细的（AI Agent）高频面试八股文，吊打付费，帮你避开99%面试坑！存下吧，很难找全的！",
    "url": "http://www.bilibili.com/video/av117030678239428",
    "source": "Agent开发实战",
    "platform": "bilibili",
    "points": 69627,
    "published_at": "2026-08-03T08:50:19+00:00",
    "summary": "【Agent面试100问】目前B站最细的（AI Agent）高频面试八股文，吊打付费，帮你避开99%面试坑！存下吧，很难找全的！"
  },
  {
    "id": "bvid:BV1VL3F6pE9K",
    "domain": "AI",
    "title": "0基础入门智能体agent测试：AI测试基础+AI智能体(Agent)测试从零入门全攻略，2026最新版！",
    "url": "http://www.bilibili.com/video/av116991151113881",
    "source": "黑马测试",
    "platform": "bilibili",
    "points": 64263,
    "published_at": "2026-07-27T09:19:37+00:00",
    "summary": "还在卷传统软件测试？2026年必学的AI智能体(Agent)测试来了！本期视频专为0基础小白打造，从软件测试基础讲起...若要本视频配套资源笔记可加up主企微（请看置顶留言最后一句话）。"
  },
  {
    "id": "bvid:BV1AJen6SEVQ",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Agent智能体】教程！大模型入门到进阶，一套全解决！Agentic AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av117274400790619",
    "source": "吴恩达Agent",
    "platform": "bilibili",
    "points": 58258,
    "published_at": "2026-09-15T09:48:26+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n1. 构建智能体设计模式：反射、工具使用、规划与多智能体工作流；\n2. 将人工智能与外部工具集成：数据库、API、网络搜索与代码执行；\n3. 评估并优化人工智能系统：性能指标、错误分析与生产部署\n4、使用开放标准格式和最佳实践创建可重复使用的技能，并组合以创建复杂的工作流程。\n5、建立定制代码生成技能，审核你的代"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operit教程：入门安卓最强大ai平台operitAI",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 56558,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1LXhc6yEkc",
    "domain": "AI",
    "title": "昔涟/Cyrene-Agent 安装配置/演示教程",
    "url": "http://www.bilibili.com/video/av117164694570292",
    "source": "Playa0",
    "platform": "bilibili",
    "points": 51978,
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
    "points": 48820,
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
    "points": 44472,
    "published_at": "2026-09-19T10:14:15+00:00",
    "summary": "如果需要文档，私信主播，主页送免费的token，文件在群里 Q群1124987353"
  },
  {
    "id": "bvid:BV1phaq6bEyQ",
    "domain": "AI",
    "title": "自费实测！这堆 AI Agent，到底哪个值得你用？【Agent大横评】",
    "url": "http://www.bilibili.com/video/av117346291157971",
    "source": "三颗门牙X",
    "platform": "bilibili",
    "points": 43670,
    "published_at": "2026-09-28T11:00:00+00:00",
    "summary": "现在的 AI Agent，一个比一个能吹，到底哪个真能干活？\n这期我自费充了会员，把 Codex、WorkBuddy、DeepSeek Harness、千问办公、豆包工作、Kimi、GLM、MiniMax 拉出来试了一圈。从 PPT、Excel、网页，到动画、3D 看房和交互原型，看看实际效果，也聊聊日常用起来顺不顺手。\n同一个模型，换个 Agent，效果和花费能差多少？模型够强，软件就一定好用？"
  },
  {
    "id": "bvid:BV1uVSUBkEfZ",
    "domain": "AI",
    "title": "Microsoft Copilot完整教程(上) 从入门到Agent 一站式掌握AI办公",
    "url": "http://www.bilibili.com/video/av116351721084069",
    "source": "星小脉",
    "platform": "bilibili",
    "points": 35672,
    "published_at": "2026-04-05T11:00:20+00:00",
    "summary": "2026年最全面的Microsoft Copilot教程上半部分。从Copilot首页入门到Agent深度解析，涵盖搜索、资料库、AI视频生成、Copilot Pages、PowerPoint智能幻灯片等全部功能。由培训了6万人的AI顾问Cherie Brock与Sabrina Ramonov联合讲解。"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 34433,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1CmAGegEpa",
    "domain": "AI",
    "title": "使用Cursor实战Java项目（Cursor写Java代码）",
    "url": "http://www.bilibili.com/video/av114012708733672",
    "source": "小道仙97",
    "platform": "bilibili",
    "points": 33024,
    "published_at": "2025-02-16T09:02:42+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 30829,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV1g6fdYcEes",
    "domain": "AI",
    "title": "Cursor从小白到专家-第19课：如何用Cursor开发安卓APP？",
    "url": "http://www.bilibili.com/video/av113888322524233",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 28971,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1z2Yw6sEgB",
    "domain": "AI",
    "title": "这就是最强性能的MC服务器！Mac Mini M6！",
    "url": "http://www.bilibili.com/video/av117362917382346",
    "source": "脏小豆",
    "platform": "bilibili",
    "points": 27686,
    "published_at": "2026-10-01T02:00:00+00:00",
    "summary": "无广！无广！无广！\n是性能最强的MC服务器，但是性价比不高！"
  },
  {
    "id": "bvid:BV1yANy6mEWe",
    "domain": "AI",
    "title": "《面向真正工程师的 Claude Code》中文语音Claude Code for Real Engineers",
    "url": "http://www.bilibili.com/video/av116910150847928",
    "source": "明文传输不",
    "platform": "bilibili",
    "points": 25282,
    "published_at": "2026-07-13T02:25:44+00:00",
    "summary": "一门为期两周的异步 cohorts 课程，由知名开发者专家 Matt Pocock 主讲，旨在帮助开发者以真正的工程方式掌握 Claude Code 这一 AI 编码工具，从而在生产环境中实现更高效、更安全的软件开发。\n课程核心围绕纠正开发者使用 AI 编码时常见的两种极端错误：完全委托（导致代码混乱、技术债务）和毫不委托（导致效率低下、认知过载），转而教你设计一条主动、自信的中间路径。\n课程主要"
  },
  {
    "id": "bvid:BV1jCaq6nESn",
    "domain": "AI",
    "title": "【Opus 5.5半价】零基础小白友好，15分钟彻底学习Claude桌面版",
    "url": "http://www.bilibili.com/video/av117346425374831",
    "source": "LeaderAI",
    "platform": "bilibili",
    "points": 24409,
    "published_at": "2026-09-28T03:03:19+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 23503,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22800,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1oQYL64EJV",
    "domain": "AI",
    "title": "【SRC漏洞挖掘】2026最适合新手的AI+自动化挖漏洞教程，从环境搭建到漏洞验证，手把手带你挖到第一个SRC漏洞！",
    "url": "http://www.bilibili.com/video/av117251248490748",
    "source": "阿盾聊安全",
    "platform": "bilibili",
    "points": 22291,
    "published_at": "2026-09-11T07:39:16+00:00",
    "summary": "这套 18 节教程带你从零跑通 AI 自动化挖漏洞全流程：环境搭建、Hermes部署、Burp/Nuclei 集成、资产侦察、漏洞发现到报告验证，一套打通。\n适合有 Web 安全基础、想从手动挖洞升级到自动化的同学。\n资料和工具包见评论区，三连不迷路。"
  },
  {
    "id": "bvid:BV1nChG6nEY4",
    "domain": "AI",
    "title": "韦东山老师教你用 DeepSeek 与 Claude Code，在 Ubuntu 中搭建嵌入式 Linux AI 开发环境：从安装配置到代码智能辅助开发实战",
    "url": "http://www.bilibili.com/video/av117155165177009",
    "source": "韦东山",
    "platform": "bilibili",
    "points": 21057,
    "published_at": "2026-08-25T08:22:35+00:00",
    "summary": "韦东山老师手把手教你在 Ubuntu 中搭建嵌入式 AI 开发环境，完整介绍开发工具、VMware Tools、中文输入法、VS Code 与常用插件的安装配置，以及 DeepSeek API Key 和 Claude Code 的接入方法。借助 AI 大模型完成代码分析、工程理解、问题排查和辅助开发，让嵌入式 Linux 学习与开发更加高效。\n查看完整文字教程：https://www.100as"
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 18874,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1tG4y1a739",
    "domain": "AI",
    "title": "[FakePlayer]给服务器一堆假玩家",
    "url": "http://www.bilibili.com/video/av814611629",
    "source": "CyanBukkit网站",
    "platform": "bilibili",
    "points": 17976,
    "published_at": "2022-08-15T14:35:57+00:00",
    "summary": "https://mcwiki.go176.net/topic/91/"
  },
  {
    "id": "bvid:BV1HfYW6dEsh",
    "domain": "AI",
    "title": "vsTrader马上要关闭内地服务器了。",
    "url": "http://www.bilibili.com/video/av117239403513785",
    "source": "v1312996",
    "platform": "bilibili",
    "points": 17380,
    "published_at": "2026-09-09T05:36:24+00:00",
    "summary": "理财有风险，投资需谨慎。"
  },
  {
    "id": "bvid:BV1pfuR69EoF",
    "domain": "AI",
    "title": "【全80集】零基础Vibe Coding教程，Vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av117070675118277",
    "source": "暴龙Boy",
    "platform": "bilibili",
    "points": 15293,
    "published_at": "2026-08-10T10:45:04+00:00",
    "summary": ""
  },
  {
    "id": "hn:49872723",
    "domain": "AI 算力 / 半导体",
    "title": "Owed a billion dollars in Nvidia stock",
    "url": "https://colo.to/nvidia-stock-narrative.html",
    "source": "Eric_Gullichsen",
    "platform": "hackernews",
    "points": 1087,
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
    "id": "hn:49906100",
    "domain": "AI 算力 / 半导体",
    "title": "OpenDLSS: A Vulkan Reimplementation of Nvidia's DLSS 5 Neural Rendering Network",
    "url": "https://github.com/maanHimself/OpenDLSS-NR",
    "source": "sagacity",
    "platform": "hackernews",
    "points": 65,
    "published_at": "2026-09-30T08:43:21+00:00",
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
    "points": 128,
    "published_at": "2026-09-15T15:31:55+00:00",
    "summary": ""
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
    "id": "rss:https://www.eetimes.com/astera-labs-leo-controller-update-targets-memory-constraints/",
    "domain": "AI 算力 / 半导体",
    "title": "Astera Labs’ Leo Controller Update Targets Memory Constraints",
    "url": "https://www.eetimes.com/astera-labs-leo-controller-update-targets-memory-constraints/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T22:00:00+00:00",
    "summary": "Astera Labs pairs Leo memory controllers with Scorpio fabric switches to bring scalable memory closer to AI accelerators. The post Astera Labs’ Leo Controller Update Targets Memory Constraints appeare"
  },
  {
    "id": "rss:https://www.eetimes.com/ai-data-centers-make-power-cooling-critical-to-scaling/",
    "domain": "AI 算力 / 半导体",
    "title": "AI Data Centers Make Power, Cooling Critical to Scaling",
    "url": "https://www.eetimes.com/ai-data-centers-make-power-cooling-critical-to-scaling/",
    "source": "Stephen Las Marias",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T14:42:45+00:00",
    "summary": "AI is transforming data centers into infrastructure platforms where power, cooling, and semiconductors determine scalability. The post AI Data Centers Make Power, Cooling Critical to Scaling appeared "
  },
  {
    "id": "rss:https://www.eetimes.com/eu-cyber-resilience-act-three-misconceptions-that-put-embedded-products-at-risk/",
    "domain": "AI 算力 / 半导体",
    "title": "EU Cyber Resilience Act: Three Misconceptions That Put Embedded Products at Risk",
    "url": "https://www.eetimes.com/eu-cyber-resilience-act-three-misconceptions-that-put-embedded-products-at-risk/",
    "source": "Florian Drittenthaler",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T13:13:52+00:00",
    "summary": "The EU Cyber Resilience Act affects more embedded products than manufacturers may expect, with implications for connectivity, resale, and long-term security support. The post EU Cyber Resilience Act: "
  },
  {
    "id": "rss:https://www.eetimes.com/webs-91j0-enables-vision-ai-at-smart-intersections/",
    "domain": "AI 算力 / 半导体",
    "title": "WEBS-91J0 Enables Vision AI at Smart Intersections",
    "url": "https://www.eetimes.com/webs-91j0-enables-vision-ai-at-smart-intersections/",
    "source": "Portwell",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T13:00:00+00:00",
    "summary": "Discover how Portwell’s WEBS-91J0 enables Vision AI and local edge inference for real-time traffic monitoring and smarter, safer smart intersections. The post WEBS-91J0 Enables Vision AI at Smart Inte"
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
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/florida-attorney-general-asks-judge-to-bar-openai-from-developing-new-ai-models-without-third-party-approval-openai-says-it-already-paused-training-its-most-capable-models-last-week",
    "domain": "AI 算力 / 半导体",
    "title": "Florida attorney general asks judge to bar OpenAI from developing new AI models without third-party approval",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/florida-attorney-general-asks-judge-to-bar-openai-from-developing-new-ai-models-without-third-party-approval-openai-says-it-already-paused-training-its-most-capable-models-last-week",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T13:20:00+00:00",
    "summary": "Florida asked a court to bar OpenAI from developing new AI models without third-party approval and to keep minors off ChatGPT."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/policy/trump-tells-federal-agencies-to-use-the-term-super-intelligence-instead-of-artificial-intelligence-president-insists-that-ai-is-only-suffering-from-a-branding-problem",
    "domain": "AI 算力 / 半导体",
    "title": "Trump tells federal agencies to use the term 'Super Intelligence ' instead of artificial intelligence",
    "url": "https://www.tomshardware.com/tech-industry/policy/trump-tells-federal-agencies-to-use-the-term-super-intelligence-instead-of-artificial-intelligence-president-insists-that-ai-is-only-suffering-from-a-branding-problem",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T12:51:29+00:00",
    "summary": "President Donald Trump issued an executive order directing all federal agencies to stop using the term 'artificial intelligence' and instead call it 'Super Intelligence.' The president said that the n"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/the-price-of-ai-is-crashing-faster-than-the-rate-of-moores-law-report-suggests-intelligence-costs-are-in-freefall-outpacing-comparative-technologies-like-compute-dna-sequencing-and-lithium-batteries",
    "domain": "AI 算力 / 半导体",
    "title": "The price of AI is crashing faster than the rate of Moore's Law, report suggests",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/the-price-of-ai-is-crashing-faster-than-the-rate-of-moores-law-report-suggests-intelligence-costs-are-in-freefall-outpacing-comparative-technologies-like-compute-dna-sequencing-and-lithium-batteries",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T12:40:00+00:00",
    "summary": "The price of AI \"intelligence,\" has fallen dramatically in recent years, faster than any other transformational technology in history according to some estimates. This raises serious questions about t"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/the-state-of-agentic-ai-in-chip-design-tools-in-2026-cadence-synopsys-and-siemens-all-pitch-autonomous-engineers",
    "domain": "AI 算力 / 半导体",
    "title": "The state of agentic AI in chip design tools in 2026",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/the-state-of-agentic-ai-in-chip-design-tools-in-2026-cadence-synopsys-and-siemens-all-pitch-autonomous-engineers",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T12:20:00+00:00",
    "summary": "Cadence, Synopsys, and Siemens all offer agentic AI for chip design, largely built on Nvidia's stack, with varying claims of autonomy."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/the-ethernet-spec-was-first-drafted-on-this-day-in-1980-dec-intel-and-xerox-defined-the-standard-several-years-before-the-internet-existed",
    "domain": "AI 算力 / 半导体",
    "title": "The Ethernet spec was first drafted on this day in 1980",
    "url": "https://www.tomshardware.com/networking/the-ethernet-spec-was-first-drafted-on-this-day-in-1980-dec-intel-and-xerox-defined-the-standard-several-years-before-the-internet-existed",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T12:00:00+00:00",
    "summary": "On this day in 1980, version 1.0 of the Ethernet specification was published by Digital Equipment Corporation (DEC), Intel, and Xerox."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/developer-trains-a-small-ai-on-a-single-rtx-3080-ti-gaming-gpu-to-play-pokemon-red-model-discovered-what-each-button-does-by-predicting-what-happens-next",
    "domain": "AI 算力 / 半导体",
    "title": "Developer trains a small AI on a single RTX 3080 Ti gaming GPU to 'play' Pokémon Red",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/developer-trains-a-small-ai-on-a-single-rtx-3080-ti-gaming-gpu-to-play-pokemon-red-model-discovered-what-each-button-does-by-predicting-what-happens-next",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T11:30:00+00:00",
    "summary": "A developer trained a JEPA world model, based on LeWorldModel research co-authored by Yann LeCun, on an RTX 3080 Ti to play Pokémon Red."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/nuvacore-reveals-unconventional-core-first-cpu-ip-design-strategy-chip-startup-led-by-apple-and-nuvia-legends-plans-to-delay-isa-selection-for-as-long-as-possible",
    "domain": "AI 算力 / 半导体",
    "title": "Nuvacore reveals unconventional Core First CPU IP design strategy",
    "url": "https://www.tomshardware.com/pc-components/cpus/nuvacore-reveals-unconventional-core-first-cpu-ip-design-strategy-chip-startup-led-by-apple-and-nuvia-legends-plans-to-delay-isa-selection-for-as-long-as-possible",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T11:00:00+00:00",
    "summary": "NuvaCore says it is developing its new WarpCore CPU IP without first choosing the ISA it will implement. This unusual development strategy is meant to offer the company maximum technology and business"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/asics/this-is-how-ai-should-be-used-openai-head-of-hardware-breaks-down-the-ai-assisted-design-of-its-jalapeno-asic",
    "domain": "AI 算力 / 半导体",
    "title": "‘This is how AI should be used’ — OpenAI head of hardware breaks down the AI-assisted design of its Jalapeño ASIC",
    "url": "https://www.tomshardware.com/tech-industry/asics/this-is-how-ai-should-be-used-openai-head-of-hardware-breaks-down-the-ai-assisted-design-of-its-jalapeno-asic",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T10:59:59+00:00",
    "summary": "OpenAI says AI-assisted Jalapeño chip design \"established a new baseline\" for the industry, and there is already a lot of interest from others to learn how the company pulled it off."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/pick-up-a-new-34-inch-gaming-monitor-from-acer-for-just-usd189-save-24-percent-on-this-curved-ultrawide-with-a-qhd-resolution",
    "domain": "AI 算力 / 半导体",
    "title": "Pick up a new 34-inch gaming monitor from Acer for just $189 — save 24% on this curved ultrawide with a QHD resolution",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/pick-up-a-new-34-inch-gaming-monitor-from-acer-for-just-usd189-save-24-percent-on-this-curved-ultrawide-with-a-qhd-resolution",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T10:59:04+00:00",
    "summary": "Just $189 for a 34-inch curved ultrawide gaming monitor with a QHD resolution and 1500R curve."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/pentagon-gets-pwned-as-breach-exposes-sensitive-data-on-nearly-three-million-military-and-civilian-personnel-stolen-info-includes-social-security-numbers-and-job-related-records",
    "domain": "AI 算力 / 半导体",
    "title": "Pentagon gets pwned as breach exposes sensitive data on nearly three million military and civilian personnel",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/pentagon-gets-pwned-as-breach-exposes-sensitive-data-on-nearly-three-million-military-and-civilian-personnel-stolen-info-includes-social-security-numbers-and-job-related-records",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T10:30:00+00:00",
    "summary": "Hackers have breached the U.S. Department of Defense's information systems. The Pentagon says that it has already secured the source of the leak, but the records of millions of DoD personnel are now i"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/former-evga-employee-recounts-companys-degrading-relationship-with-nvidia-before-2022-blow-up-founders-editions-pricing-mandates-and-forward-looking-tech-all-led-to-friction",
    "domain": "AI 算力 / 半导体",
    "title": "Former EVGA employee recounts company’s degrading relationship with Nvidia before 2022 blow-up",
    "url": "https://www.tomshardware.com/pc-components/gpus/former-evga-employee-recounts-companys-degrading-relationship-with-nvidia-before-2022-blow-up-founders-editions-pricing-mandates-and-forward-looking-tech-all-led-to-friction",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T10:00:00+00:00",
    "summary": "In a personal blog, former EVGA product manager Brendon Ray Hedrick shared how the first Nvidia Founders Edition GPUs alarmed the company and how pricing pressure and risky forward-looking tech ultima"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/amd-acquires-ai-legend-fei-fei-lis-world-labs-for-usd8-2-billion-imagenet-pioneer-will-become-amd-chief-scientist-as-the-chipmaker-brings-her-lab-in-house",
    "domain": "AI 算力 / 半导体",
    "title": "AMD acquires AI legend Fei-Fei Li's World Labs for $8.2 billion",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/amd-acquires-ai-legend-fei-fei-lis-world-labs-for-usd8-2-billion-imagenet-pioneer-will-become-amd-chief-scientist-as-the-chipmaker-brings-her-lab-in-house",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T09:30:00+00:00",
    "summary": "AMD has agreed agreed to buy generative AI world model developer World Labs for $8.2 billion in stock. Legendary CEO and co-founder Fei-Fei Li will join the company as an executive vice president and "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/zotac-denies-warranty-support-to-rtx-3060-owner-in-india-after-just-one-year-despite-offering-three-years-of-coverage-company-says-gpus-2023-import-date-takes-precedence-over-purchase-date",
    "domain": "AI 算力 / 半导体",
    "title": "Zotac denies warranty support to RTX 3060 owner in India after just one year despite offering three years of coverage",
    "url": "https://www.tomshardware.com/pc-components/gpus/zotac-denies-warranty-support-to-rtx-3060-owner-in-india-after-just-one-year-despite-offering-three-years-of-coverage-company-says-gpus-2023-import-date-takes-precedence-over-purchase-date",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T15:17:35+00:00",
    "summary": "The owner of a Zotac RTX 3060 in India was denied warranty coverage just one year after buying the card in 2025, despite Zotac's offer of a three-year standard warranty in the country. The company cla"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/nintendo/score-the-nintendo-switch-2-at-its-lowest-ever-amazon-uk-price-now-just-gbp354-99-pocket-a-gbp65-discount-on-nintendos-portable-gaming-console-with-a-7-9-inch-1080p-screen-4k-dock-and-magnetic-controllers",
    "domain": "AI 算力 / 半导体",
    "title": "Score the Nintendo Switch 2 at its lowest ever Amazon UK price, now just £354.99",
    "url": "https://www.tomshardware.com/video-games/nintendo/score-the-nintendo-switch-2-at-its-lowest-ever-amazon-uk-price-now-just-gbp354-99-pocket-a-gbp65-discount-on-nintendos-portable-gaming-console-with-a-7-9-inch-1080p-screen-4k-dock-and-magnetic-controllers",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T15:11:18+00:00",
    "summary": "The Nintendo Switch 2 is now at a record low price on Amazon UK at just £354.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/blockchain-assisted-cyberattacks-surge-fivefold-driven-by-iranian-and-north-korean-state-actors-russia-linked-groups-open-weight-llms-are-linked-to-an-increase-in-attacks",
    "domain": "AI 算力 / 半导体",
    "title": "Blockchain-assisted cyberattacks surge fivefold, driven by Iranian and North Korean state actors, Russia-linked groups",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/blockchain-assisted-cyberattacks-surge-fivefold-driven-by-iranian-and-north-korean-state-actors-russia-linked-groups-open-weight-llms-are-linked-to-an-increase-in-attacks",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T14:10:00+00:00",
    "summary": "A new report says blockchain dead-drop attacks have risen 440%, with state-linked and criminal groups using transactions, smart contracts, and even phantom wallets to hide malware payloads and C2 infr"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-lists-existential-risks-to-humanity-as-one-of-its-risk-factors-in-ipo-prospectus-80-pages-of-risk-factors-dwarf-business-description-as-firm-eyes-usd2-trillion-debut",
    "domain": "AI 算力 / 半导体",
    "title": "Anthropic lists ‘existential risks to humanity’ as one of its risk factors in IPO prospectus",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-lists-existential-risks-to-humanity-as-one-of-its-risk-factors-in-ipo-prospectus-80-pages-of-risk-factors-dwarf-business-description-as-firm-eyes-usd2-trillion-debut",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T13:30:00+00:00",
    "summary": "Anthropic serves a dire warning in its IPO prospectus, saying how a rogue model could lead to the end of humanity and, consequentially, its business. Nevertheless, investors are still hoping for a $2-"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/usb/we-tested-13-power-banks-to-help-you-choose-the-best-one-from-10-25k-mah-and-20-220w",
    "domain": "AI 算力 / 半导体",
    "title": "We tested 13 power banks to help you choose the best one",
    "url": "https://www.tomshardware.com/peripherals/usb/we-tested-13-power-banks-to-help-you-choose-the-best-one-from-10-25k-mah-and-20-220w",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T13:10:00+00:00",
    "summary": "We tested 13 power banks from Anker, Belkin, Baseus, Cuktech, and Sharge, tracking charge times, output, temps, and capacity to see which actually hold up."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/silicon-is-starting-to-design-silicon-how-ai-is-being-used-in-chipmaking-from-eda-tools-to-openais-jalapeno-and-beyond",
    "domain": "AI 算力 / 半导体",
    "title": "Silicon is starting to design silicon — how AI is being used in chipmaking, from EDA tools to OpenAI's Jalapeño and beyond",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/silicon-is-starting-to-design-silicon-how-ai-is-being-used-in-chipmaking-from-eda-tools-to-openais-jalapeno-and-beyond",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T12:40:00+00:00",
    "summary": "How close is AI to designing the very same chips it runs on? We explore how artificial intelligence is being used in modern chip design today."
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
    "id": "hn:49913571",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/",
    "source": "bradleyg223",
    "platform": "hackernews",
    "points": 1393,
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
    "points": 615,
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
    "id": "hn:49914236",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon (High): Intelligence, Performance and Price Analysis",
    "url": "https://artificialanalysis.ai/models/gemini-4-argon",
    "source": "theanonymousone",
    "platform": "hackernews",
    "points": 105,
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
    "id": "rss:https://www.theverge.com/entertainment/1003182/universal-hollywood-fast-and-furious-rollercoaster-noise",
    "domain": "大厂 AI 动态",
    "title": "Noise from Universal&#8217;s latest ride made rich locals furious, fast",
    "url": "https://www.theverge.com/entertainment/1003182/universal-hollywood-fast-and-furious-rollercoaster-noise",
    "source": "Jess Weatherbed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T09:00:04+00:00",
    "summary": "Universal Studios Hollywood has pledged to erect another sound barrier around its latest attraction after local residents complained about the bloodcurdling screams from riders. In a meeting attended "
  },
  {
    "id": "rss:https://www.theverge.com/tech/1002680/vivo-x-fold-6-global-release-specs-cameras",
    "domain": "大厂 AI 动态",
    "title": "Vivo’s X Fold 6 accidentally feels like a throwback",
    "url": "https://www.theverge.com/tech/1002680/vivo-x-fold-6-global-release-specs-cameras",
    "source": "Dominic Preston",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T02:00:00+00:00",
    "summary": "It's a quirk of the release calendar that when Vivo's X Fold 6 launched in China this June, it was just another foldable. Now that it's ready for its global release, the size and aspect ratio feel odd"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1003068/elon-musk-grokipedia-v-0-3-spacexai",
    "domain": "大厂 AI 动态",
    "title": "Elon Musk’s Grokipedia has a ‘newly refreshed’ design",
    "url": "https://www.theverge.com/tech/1003068/elon-musk-grokipedia-v-0-3-spacexai",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T00:23:45+00:00",
    "summary": "Grokipedia, SpaceXAI's AI-powered competitor to Wikipedia, recently started incorporating edits again, and today, it got some design tweaks as part of a v0.3 update, including a new logo and refreshes"
  },
  {
    "id": "rss:https://www.theverge.com/news/1003037/paramount-david-ellison-co-ceo-ynon-kriez",
    "domain": "大厂 AI 动态",
    "title": "The new and huger Paramount has a new co-CEO",
    "url": "https://www.theverge.com/news/1003037/paramount-david-ellison-co-ceo-ynon-kriez",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T23:08:49+00:00",
    "summary": "Paramount is appointing a new co-CEO ahead of the close of its $110 billion merger with Warner Bros. Discovery. Ynon Kreiz, previously Mattel's chairman and CEO, will be joining Paramount to lead alon"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/1002958/neon-a24-creative-commons-scp-foundation-movie",
    "domain": "大厂 AI 动态",
    "title": "Neon sticks it to A24 by announcing a Creative Commons SCP Foundation movie",
    "url": "https://www.theverge.com/entertainment/1002958/neon-a24-creative-commons-scp-foundation-movie",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T20:45:00+00:00",
    "summary": "A24 pissed off one of the internet's largest horror communities when it announced it was working on an SCP Foundation film, but apparently hadn't bothered to contact the SCP Wiki team, nor did it comm"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1002980/google-gemini-4-argon",
    "domain": "大厂 AI 动态",
    "title": "Google announces Gemini 4 and says it&#8217;s so capable that only &#8216;trusted cyber defenders&#8217; can have it right now",
    "url": "https://www.theverge.com/tech/1002980/google-gemini-4-argon",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T20:41:41+00:00",
    "summary": "Google today revealed its next AI frontier model, which it's calling Gemini 4 Argon. The new model delivers \"frontier performance in complex workflows across real-world software engineering, enterpris"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1002779/openai-dots-meta-muse-ai-agents-hardware-devices",
    "domain": "大厂 AI 动态",
    "title": "The AI Tamagotchis are coming",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1002779/openai-dots-meta-muse-ai-agents-hardware-devices",
    "source": "Hayden Field",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T18:07:38+00:00",
    "summary": "While AI has made plenty of inroads on people's phones and computers, it's largely failed in dedicated devices. But over the next year, two major AI companies, Meta and OpenAI, will attempt to change "
  },
  {
    "id": "rss:https://www.theverge.com/tech/1002788/old-reddit-ai-scraping",
    "domain": "大厂 AI 动态",
    "title": "Reddit says it has to cut back access to ‘Old Reddit’ because of AI bots",
    "url": "https://www.theverge.com/tech/1002788/old-reddit-ai-scraping",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T17:45:00+00:00",
    "summary": "Reddit is further limiting who can use the \"Old Reddit\" experience as part of its efforts to combat scraping and automated traffic. Reddit recently started forcing users to log in to be able to use Ol"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1002766/amazon-delivery-driver-smart-glasses-privacy",
    "domain": "大厂 AI 动态",
    "title": "Amazon&#8217;s delivery driver smart glasses will reportedly take photos &#8216;almost constantly&#8217;",
    "url": "https://www.theverge.com/tech/1002766/amazon-delivery-driver-smart-glasses-privacy",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T17:21:29+00:00",
    "summary": "Amazon deliveries could soon come with a new catch: the delivery driver's smart glasses will be snapping photos of anything they see while they're in use, including people and private property. Bloomb"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1002636/ai-execs-trump-self-policing-deal-comments",
    "domain": "大厂 AI 动态",
    "title": "Here&#8217;s what AI leaders are saying about Trump’s new safety plan",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1002636/ai-execs-trump-self-policing-deal-comments",
    "source": "Jess Weatherbed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T17:15:49+00:00",
    "summary": "After hosting a meal with Big Tech leaders on Tuesday, President Donald Trump responded to journalist questions about his artificial intelligence announcements in typical fashion. He said his previous"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/30/google-releases-gemini-4-argon-called-its-most-powerful-model-yet/",
    "domain": "大厂 AI 动态",
    "title": "Google releases Gemini 4 Argon, called its most powerful model yet",
    "url": "https://techcrunch.com/2026/09/30/google-releases-gemini-4-argon-called-its-most-powerful-model-yet/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T23:43:07+00:00",
    "summary": "Google has released its latest Gemini model, marketing it as a workhorse for coding and cybersecurity work."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/30/the-pentagon-taps-elon-musk-and-palmer-luckey-to-help-decide-what-the-military-should-do-next/",
    "domain": "大厂 AI 动态",
    "title": "The Pentagon taps Elon Musk and Palmer Luckey to help decide what the military should do next",
    "url": "https://techcrunch.com/2026/09/30/the-pentagon-taps-elon-musk-and-palmer-luckey-to-help-decide-what-the-military-should-do-next/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T23:08:00+00:00",
    "summary": "Defense Secretary Pete Hegseth just launched a 120-day study on the future of warfare, led by Elon Musk, Palmer Luckey, and Newt Gingrich, and while it makes sense given their ties to the administrati"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/30/valor-atreides-and-sequoia-back-ai-startup-flow-engineering-at-750m-valuation/",
    "domain": "大厂 AI 动态",
    "title": "Valor, Atreides, and Sequoia back AI startup Flow Engineering at $750M valuation",
    "url": "https://techcrunch.com/2026/09/30/valor-atreides-and-sequoia-back-ai-startup-flow-engineering-at-750m-valuation/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T21:07:40+00:00",
    "summary": "Flow Engineering, which is bringing AI agents to hardware design, also landed Roelof Botha as an angel investor and board member."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/30/factory-ceo-just-accused-his-vc-board-advisor-of-spying-for-cognition/",
    "domain": "大厂 AI 动态",
    "title": "Factory CEO just accused his VC board adviser of spying for Cognition",
    "url": "https://techcrunch.com/2026/09/30/factory-ceo-just-accused-his-vc-board-advisor-of-spying-for-cognition/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T20:39:09+00:00",
    "summary": "VC Chris Degnan and former board adviser to Factory AI has taken a job as chief revenue officer for competitor Cognition -- and everyone is arguing on X about it."
  },
  {
    "id": "rss:https://techcrunch.com/video/is-neko-healths-body-scan-worth-it-spotify-billionaires-startup-has-come-to-america/",
    "domain": "大厂 AI 动态",
    "title": "Is Neko Health’s body scan worth it? Spotify billionaire’s startup has come to America",
    "url": "https://techcrunch.com/video/is-neko-healths-body-scan-worth-it-spotify-billionaires-startup-has-come-to-america/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T20:20:02+00:00",
    "summary": "Spotify founder Daniel Ek’s Neko Health raised $700 million to build a business around scanning your body, but it’s not the only company centering its roadmap around a new kind of preventative healthc"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/30/hackers-stole-millions-of-us-military-personnel-records-during-months-long-data-breach/",
    "domain": "大厂 AI 动态",
    "title": "Hackers stole millions of US military personnel records during months-long data breach",
    "url": "https://techcrunch.com/2026/09/30/hackers-stole-millions-of-us-military-personnel-records-during-months-long-data-breach/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T19:29:08+00:00",
    "summary": "The Department of Defense notified millions of current and former U.S. military personnel that their personal information had been stolen in a months-long breach."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/30/doordashs-drone-strategy-started-on-the-ground/",
    "domain": "大厂 AI 动态",
    "title": "DoorDash’s drone strategy started on the ground",
    "url": "https://techcrunch.com/2026/09/30/doordashs-drone-strategy-started-on-the-ground/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T19:22:13+00:00",
    "summary": "DoorDash unveiled the six-propeller aircraft that will be used in its new drone delivery business at its annual Dash Forward 2026 event."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/30/bmw-built-the-same-car-for-gas-and-electric-the-ev-is-4400-cheaper/",
    "domain": "大厂 AI 动态",
    "title": "BMW built the same car for gas and electric. The EV is $4,400 cheaper.",
    "url": "https://techcrunch.com/2026/09/30/bmw-built-the-same-car-for-gas-and-electric-the-ev-is-4400-cheaper/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T19:19:40+00:00",
    "summary": "The new BMW 3 Series shows just how quickly EVs have caught up to fossil fuel vehicles on pricing."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/30/openais-jev-clone-could-help-the-frontier-lab-stop-its-swarming-agents/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI’s Jev clone could help the frontier lab stop its swarming agents",
    "url": "https://techcrunch.com/2026/09/30/openais-jev-clone-could-help-the-frontier-lab-stop-its-swarming-agents/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T19:00:57+00:00",
    "summary": "OpenAI's \"Decisions API\" is a Jev clone that confirms the importance of fast, cheap intelligence."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/30/ai-voice-startup-elevenlabs-doubles-valuation-to-22b/",
    "domain": "大厂 AI 动态",
    "title": "AI voice startup ElevenLabs doubles valuation to $22B",
    "url": "https://techcrunch.com/2026/09/30/ai-voice-startup-elevenlabs-doubles-valuation-to-22b/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T18:23:57+00:00",
    "summary": "The $300 million employee tender was co-led by Wellington and T. Rowe Price."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/30/reddit-is-killing-rss-feeds-ending-public-api-access-because-of-ai-bots/",
    "domain": "大厂 AI 动态",
    "title": "Reddit is killing RSS feeds and ending public API access because of AI bots",
    "url": "https://techcrunch.com/2026/09/30/reddit-is-killing-rss-feeds-ending-public-api-access-because-of-ai-bots/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T17:45:00+00:00",
    "summary": "Reddit is ending support for RSS feeds, as the company continues tightening access to its trove of user-generated content."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/30/the-ugly-economics-of-consumer-ai/",
    "domain": "大厂 AI 动态",
    "title": "The ugly economics of consumer AI",
    "url": "https://techcrunch.com/2026/09/30/the-ugly-economics-of-consumer-ai/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T17:24:45+00:00",
    "summary": "There’s a reason frontier labs have gotten gun-shy about consumer AI — and it’s not because the tech isn’t good enough."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/30/meta-disputes-claim-that-muse-read-a-users-private-messages-without-permission/",
    "domain": "大厂 AI 动态",
    "title": "Meta disputes claim that Muse read a user’s private messages without permission",
    "url": "https://techcrunch.com/2026/09/30/meta-disputes-claim-that-muse-read-a-users-private-messages-without-permission/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T16:24:23+00:00",
    "summary": "Meta says its Muse AI agent cannot access a user’s Messages without explicit permission, disputing a journalist’s account that the agent read his private messages while the required Mac setting was tu"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/30/doordash-launches-an-ai-agent-you-can-text-to-order-food/",
    "domain": "大厂 AI 动态",
    "title": "DoorDash launches an AI agent you can text to order food",
    "url": "https://techcrunch.com/2026/09/30/doordash-launches-an-ai-agent-you-can-text-to-order-food/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T16:00:24+00:00",
    "summary": "By launching an AI agent for food ordering, DoorDash is looking to gain an edge over rivals Uber Eats and Grubhub."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/30/destro-ais-secret-sauce-is-getting-robots-and-humans-on-the-same-page/",
    "domain": "大厂 AI 动态",
    "title": "Destro AI’s secret sauce is getting robots and humans on the same page",
    "url": "https://techcrunch.com/2026/09/30/destro-ais-secret-sauce-is-getting-robots-and-humans-on-the-same-page/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T16:00:00+00:00",
    "summary": "\"One of the biggest reasons we are winning against robotics companies is because we are not a robotics company.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/30/instincts-new-product-recommendations-are-giving-some-users-the-ick/",
    "domain": "大厂 AI 动态",
    "title": "Instinct’s new product recommendations are giving some users the ick",
    "url": "https://techcrunch.com/2026/09/30/instincts-new-product-recommendations-are-giving-some-users-the-ick/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T15:56:28+00:00",
    "summary": "Instinct is rolling out human-curated product and travel recommendations, but some users aren’t happy about getting suggestions they never asked for."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/30/fedex-orders-2000-electric-trucks-from-harbinger-in-300m-deal/",
    "domain": "大厂 AI 动态",
    "title": "FedEx orders 2,000 electric trucks from Harbinger in $300M deal",
    "url": "https://techcrunch.com/2026/09/30/fedex-orders-2000-electric-trucks-from-harbinger-in-300m-deal/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T15:26:02+00:00",
    "summary": "The order -- Harbinger's biggest ever -- comes as the startup is reportedly considering an IPO."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/30/pledge-signed-by-president-trump-and-top-ai-leaders-misspells-the-united-states/",
    "domain": "大厂 AI 动态",
    "title": "Pledge signed by President Trump and top AI leaders misspells the United States",
    "url": "https://techcrunch.com/2026/09/30/pledge-signed-by-president-trump-and-top-ai-leaders-misspells-the-united-states/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T14:50:55+00:00",
    "summary": "On Tuesday, President Donald Trump and top AI leaders announced a signed pledge called a “Joint Commitment on Frontier Responsibilities” — a voluntary promise to implement more controls and safety mea"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/30/google-launches-fitbit-air-in-india-though-its-high-price-might-deter-the-masses/",
    "domain": "大厂 AI 动态",
    "title": "Google launches Fitbit Air in India, though its high price might deter the masses",
    "url": "https://techcrunch.com/2026/09/30/google-launches-fitbit-air-in-india-though-its-high-price-might-deter-the-masses/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T14:32:03+00:00",
    "summary": "Fitbit Air costs around $146 in India, roughly $47 more than its U.S. pricing."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/30/instagram-rolls-out-an-ai-video-assistant-for-creators/",
    "domain": "大厂 AI 动态",
    "title": "Instagram rolls out an AI video assistant for creators",
    "url": "https://techcrunch.com/2026/09/30/instagram-rolls-out-an-ai-video-assistant-for-creators/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T14:30:00+00:00",
    "summary": "This conversational AI assistant is intended to provide personalized feedback to creators, rather than generic advice."
  },
  {
    "id": "rss:https://stratechery.com/2026/openai-dev-day-dot-and-openais-product-transition-sign-in-with-chatgpt/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI Dev Day, Dot and OpenAI’s Product Transition, Sign In With ChatGPT",
    "url": "https://stratechery.com/2026/openai-dev-day-dot-and-openais-product-transition-sign-in-with-chatgpt/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T10:00:00+00:00",
    "summary": "OpenAI's Dev Day showcased a product that is, frankly, pretty confusing. However, there is more vision here than it might seem."
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
    "points": 325,
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
    "points": 155,
    "published_at": "2026-09-30T04:37:37+00:00",
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
    "id": "hn:49916668",
    "domain": "金融",
    "title": "10-year Treasury yield climbs above 5.3% to a level not seen in 24 years",
    "url": "https://www.wsj.com/finance/investing/surging-yields-bring-the-bond-market-back-to-the-turn-of-the-century-2b74773f",
    "source": "kaycebasques",
    "platform": "hackernews",
    "points": 96,
    "published_at": "2026-10-01T01:40:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:49916955",
    "domain": "金融",
    "title": "Cities Are Forced to Funnel License Plate Data to a Federal Surveillance Program",
    "url": "https://www.404media.co/how-cities-are-forced-to-funnel-license-plate-data-to-a-massive-federal-surveillance-program-hidta/",
    "source": "ripe",
    "platform": "hackernews",
    "points": 80,
    "published_at": "2026-10-01T02:26:17+00:00",
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
    "id": "rss:https://arxiv.org/abs/2609.38230",
    "domain": "金融",
    "title": "Basket implied volatility skew and stickiness",
    "url": "https://arxiv.org/abs/2609.38230",
    "source": "Masaaki Fukasawa, Jun Maeda, Tatsuya Ogiwara",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T04:00:00+00:00",
    "summary": "arXiv:2609.38230v1 Announce Type: new Abstract: We study the short-maturity implied volatility and the skew stickiness ratio for baskets of assets with continuous, possibly rough, stochastic volatilit"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.38459",
    "domain": "金融",
    "title": "Maintaining Human Verification Capacity under Automation",
    "url": "https://arxiv.org/abs/2609.38459",
    "source": "Li Gan, Eric Gan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T04:00:00+00:00",
    "summary": "arXiv:2609.38459v1 Announce Type: new Abstract: Human verification depends on expertise that must be maintained before it is needed. This paper links reliance on automated checks, investment in human "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.38545",
    "domain": "金融",
    "title": "Say, Echo, Do: Strategic Narratives and Revealed Positioning in Financial Markets",
    "url": "https://arxiv.org/abs/2609.38545",
    "source": "Ali Atiah Alzahrani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T04:00:00+00:00",
    "summary": "arXiv:2609.38545v1 Announce Type: new Abstract: Machine-learning signals built from financial text treat what institutions say, and what the media repeat, as evidence about value. But whoever shapes a"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.38765",
    "domain": "金融",
    "title": "Multiperiod bond portfolio optimization with transaction costs using a Markov Decision process",
    "url": "https://arxiv.org/abs/2609.38765",
    "source": "Balaji Ramachandran, Srikanth Iyer, Shashi Jain",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T04:00:00+00:00",
    "summary": "arXiv:2609.38765v1 Announce Type: new Abstract: Bank treasury portfolios must balance yield, liquidity, and interest-rate risk across bonds of different maturities. Static allocation rules are ill-sui"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.39256",
    "domain": "金融",
    "title": "Stochastic Knothe-Rosenblatt: Light-speed Calibration of Stochastic Local Volatility Models",
    "url": "https://arxiv.org/abs/2609.39256",
    "source": "Mathias Beiglb\\\"ock, Manuel Hasenbichler, Gudmund Pammer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T04:00:00+00:00",
    "summary": "arXiv:2609.39256v1 Announce Type: new Abstract: European option smiles determine the risk-neutral marginal laws of an asset, but not their intertemporal coupling, which is decisive for many applicatio"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.39264",
    "domain": "金融",
    "title": "Exchange Rate Determination for Cryptocurrency Mergers: A Formal Framework",
    "url": "https://arxiv.org/abs/2609.39264",
    "source": "Massimiliano Sala, Daniela Visetti",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T04:00:00+00:00",
    "summary": "arXiv:2609.39264v1 Announce Type: new Abstract: Many of the thousands of existing cryptocurrencies suffer from declining adoption, low liquidity and weak security, and merging two of them into a singl"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.39569",
    "domain": "金融",
    "title": "Spouse-Protected Tontines: Household Decumulation via Neural-Network Optimization",
    "url": "https://arxiv.org/abs/2609.39569",
    "source": "Duy-Minh Dang, Yukan Perumal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T04:00:00+00:00",
    "summary": "arXiv:2609.39569v1 Announce Type: new Abstract: We develop a spouse-protected tontine in which a first death changes the household state but generates no pool transfer. The same account remains attach"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.39932",
    "domain": "金融",
    "title": "Food Insecurity Among Military Veterans",
    "url": "https://arxiv.org/abs/2609.39932",
    "source": "Senan Hogan-Hennessy, Seungmin Lee, Christopher B. Barrett, John Hoddinott, Matthew P. Rabbitt",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T04:00:00+00:00",
    "summary": "arXiv:2609.39932v1 Announce Type: new Abstract: Veterans face multiple hardships after they leave the military. Is food insecurity one of these hardships? This paper examines the long-term effects of "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.39261",
    "domain": "金融",
    "title": "Jacobian Rank Collapse in Decision-Focused Learning",
    "url": "https://arxiv.org/abs/2609.39261",
    "source": "Aojie Yuan, Haiyue Zhang, Zijian Su",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T04:00:00+00:00",
    "summary": "arXiv:2609.39261v1 Announce Type: cross Abstract: Decision-focused learning (DFL) trains predictors through downstream objectives, but a different loss need not provide an independent parameter-update"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.39420",
    "domain": "金融",
    "title": "QuantCode Model: Specializing Language Models for Executable Algorithmic Trading Code",
    "url": "https://arxiv.org/abs/2609.39420",
    "source": "Alexey Chernysh, Orkhan Ekhtibarov, Dmitry Zmitrovich",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T04:00:00+00:00",
    "summary": "arXiv:2609.39420v1 Announce Type: cross Abstract: Large language models are strong general-purpose code generators, but executable algorithmic trading remains a demanding specialization target: a mode"
  },
  {
    "id": "rss:https://arxiv.org/abs/2512.07787",
    "domain": "金融",
    "title": "VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables",
    "url": "https://arxiv.org/abs/2512.07787",
    "source": "Nawaf Mohammed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T04:00:00+00:00",
    "summary": "arXiv:2512.07787v5 Announce Type: replace Abstract: Value-at-Risk (VaR) may reward diversification at some probability levels and penalize it at others. We study the two extremal regimes in which one "
  },
  {
    "id": "rss:https://arxiv.org/abs/2601.17247",
    "domain": "金融",
    "title": "Learning Optimal Liquidation with Closing Auctions",
    "url": "https://arxiv.org/abs/2601.17247",
    "source": "Julius Graf, Thibaut Mastrolia",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T04:00:00+00:00",
    "summary": "arXiv:2601.17247v3 Announce Type: replace Abstract: We study liquidation when continuous trading is followed by a closing auction. The trader first sells through a limit-order book, then submits signe"
  },
  {
    "id": "rss:https://arxiv.org/abs/2603.10202",
    "domain": "金融",
    "title": "Variance-Corrected Multi-Asset Equity Simulation with Hybrid Hidden Markov Marginals",
    "url": "https://arxiv.org/abs/2603.10202",
    "source": "Abdulrahman Alswaidan, Jeffrey D. Varner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T04:00:00+00:00",
    "summary": "arXiv:2603.10202v3 Announce Type: replace Abstract: Synthetic multi-asset equity data must reproduce each asset's return distribution and its relationship with the market. Reusing a generator fitted t"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.12283",
    "domain": "金融",
    "title": "Large Language Model-Driven Small-Capitalization Trading: Integrating Financial News Sentiment, Macroeconomic Indicators, and Technical Signals",
    "url": "https://arxiv.org/abs/2608.12283",
    "source": "Alireza Kargarzadeh, Nariman Khaledian, Navid Parvini, Arman Khaledian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T04:00:00+00:00",
    "summary": "arXiv:2608.12283v2 Announce Type: replace Abstract: Large language models can extract richer signals from financial news than fixed sentiment lexicons, and recent work has explored feeding such signal"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.05804",
    "domain": "金融",
    "title": "Why China Succeeds: A Road to Prosperity",
    "url": "https://arxiv.org/abs/2609.05804",
    "source": "Qingjie Xia",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T04:00:00+00:00",
    "summary": "arXiv:2609.05804v2 Announce Type: replace Abstract: Why China Succeeds offers what no existing book does: a single, unified explanatory framework that traces China's rise from its ancient civilization"
  },
  {
    "id": "rss:https://arxiv.org/abs/2507.09601",
    "domain": "金融",
    "title": "NMIXX: Domain-Adapted Neural Embeddings for Cross-Lingual eXploration of Finance",
    "url": "https://arxiv.org/abs/2507.09601",
    "source": "Hanwool Lee, Sara Yu, Yewon Hwang, Jonghyun Choi, Heejae Ahn, Sungbum Jung, Youngjae Yu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T04:00:00+00:00",
    "summary": "arXiv:2507.09601v3 Announce Type: replace-cross Abstract: Financial text embeddings must distinguish changes in event status, perspective, and obligations even when passages share similar wording. NMI"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.23916",
    "domain": "金融",
    "title": "Agent-Facing Information Design in LLM Tool Registries: A Preregistered Test of Rhetoric, Position and Structure",
    "url": "https://arxiv.org/abs/2605.23916",
    "source": "Haochuan Kevin Wang, Zechen Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T04:00:00+00:00",
    "summary": "arXiv:2605.23916v2 Announce Type: replace-cross Abstract: AI agents often pick tools from registries, where each tool's provider writes its description. We ask whether sales language in those descript"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.31345",
    "domain": "金融",
    "title": "On the asymptotic shape of quantile surfaces",
    "url": "https://arxiv.org/abs/2609.31345",
    "source": "Florian Gach, Simon Hochgerner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T04:00:00+00:00",
    "summary": "arXiv:2609.31345v2 Announce Type: replace-cross Abstract: This article is concerned with the asymptotic shape of quantile surfaces, defined as the set of quantiles at a given level $\\alpha$ generated "
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
    "id": "hn:49762617",
    "domain": "金融",
    "title": "Elon Musk and Tesla Forged a New EV Path",
    "url": "https://spectrum.ieee.org/elon-musk-tesla",
    "source": "vinhnx",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-09-19T02:08:54+00:00",
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
