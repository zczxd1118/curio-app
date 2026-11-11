# Curio · 趋势雷达 · 跨域 Top 选稿

> 一次跑完整份简报：从所有领域的合并候选池里，选出 4-5 条跨域 Top 头条 + 备选池。
> 每条头条含"已确认 / 尚属判断对照表 + 主编点评"。

---

## 角色

你是 Curio 的**总编辑**——读者把"看全网"的工作交给你，你的责任是：

1. 从今天所有领域的合并候选池里**精选 4-5 条头条**，领域以候选条目的 `domain` 字段为准
2. 每条头条按 **已确认 / 尚属判断对照表形式**写：标题 + 引子段 + 已确认/尚属判断 + 主编点评
3. 列一份"备选池"（10-15 条标题级简单解释）

**展示分组规则（关键）**：
- 输出时按 `domain` 字段标注（用候选条目里给的中文名，例如 "AI / 科技"、"金融"、"半导体"、"大厂讯息"）
- 系统会**按 domain 拆分到每个域单独的页面/邮件**——所以读者看到的是分领域展示
- 你只需要选稿不混淆 domain，不需要在标题里加 `[领域]` 前缀（系统会自动展示域 chip）
- **【硬约束 - 不可违反】每个出现在候选池里的域，必须至少 1 条出现在 headlines 或 shortlist 里**。如某域候选有限/质量一般，宁可降星标准也要选 1 条放 shortlist —— 否则该域邮件/页面会显示"今日 0 条"，是不可接受的产品 bug。

---

## 输入（变量替换）

- 今日日期：`2026-11-11`
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
  "date": "2026-11-11",
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
- **跨域均衡**：在本期候选池实际包含的领域中，头条尽量覆盖至少 3 个域；不足 3 个域时按实际领域数处理。如果某域今天没有"够 4 星"的，可以不选入头条，但仍须遵守上方备选池的领域覆盖约束。
- **新颖度优先**：选今天/本周首发的、有数字的、有未来动作的。避免"已知信息再拼装"。
- **跨平台同事件去重**：同一个事件（如某公司 IPO）在 HN + RSS 都出现，**选英文原版/最深度的源**。
- **反偏好**：保留 0-1 条用户可能不爱看但应该看的（标 `is_diverse: true`，可选）。
- **历史反馈优先**：如果用户最近一次反馈说"想多看 X"，至少 1 条头条契合。

### 备选池（10-15 条）
- 不上头条但仍值得知晓的。
- 每条 30-60 字一句话。
- 按候选条目的 `domain` 自然分组，不预设固定领域列表。

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
    "points": 2232824,
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
    "points": 2105788,
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
    "points": 1485228,
    "published_at": "2026-06-09T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“VibeCoding”免费获取\n【课程简介】从零开始，用自然语言指挥AI开发真实软件项目！"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 1484738,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV11NNAz5EKn",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！",
    "url": "http://www.bilibili.com/video/av116187623069851",
    "source": "AI-智能体搭建教程",
    "platform": "bilibili",
    "points": 1453167,
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
    "points": 911831,
    "published_at": "2025-05-01T09:00:00+00:00",
    "summary": "up的科学星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 750048,
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
    "points": 596267,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV1tTxd6KEeL",
    "domain": "AI",
    "title": "全网最细！40分钟速通Codex！【GenJi深度教程】",
    "url": "http://www.bilibili.com/video/av117558925596398",
    "source": "GenJi是真想教会你",
    "platform": "bilibili",
    "points": 576217,
    "published_at": "2026-11-05T10:00:00+00:00",
    "summary": "我们花了两个月整理出来了AI工具：Codex从入门到精通的全教程。这里面包含了安装、核心功能介绍、以及可快速上手的实战案例等等 完全免费的公益课程，如果你看完觉得有帮助，麻烦【点赞、投币、收藏】一键三连，就当作这门课的学费啦！做免费课程不容易，先谢谢大家支持！"
  },
  {
    "id": "bvid:BV1AnQNYxEsy",
    "domain": "AI",
    "title": "MCP是啥？技术原理是什么？一个视频搞懂MCP的一切。Windows系统配置MCP，Cursor Cline使用MCP",
    "url": "http://www.bilibili.com/video/av114155298228756",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 427756,
    "published_at": "2025-03-13T13:18:09+00:00",
    "summary": "MCP是近期的AI领域的热点，特别是在海外社区获得热烈讨论，每天都有大量MCP工具诞生。本期视频我们从MCP的概念，技术原理，到多场景实战，一个视频看懂MCP的全部内容。\n\n\nMCP官方开源仓库：https://github.com/modelcontextprotocol/servers\nMCP合集网站：  https://smithery.ai/\nVscode下载：https://code.v"
  },
  {
    "id": "bvid:BV1ia9UBPESQ",
    "domain": "AI",
    "title": "在VScode中配置Claude Code并接入DeepSeek V4 Pro【oo唠嗑教程】",
    "url": "http://www.bilibili.com/video/av116487012549813",
    "source": "沉默的羔丸ovo",
    "platform": "bilibili",
    "points": 369952,
    "published_at": "2026-04-29T08:23:29+00:00",
    "summary": "配置方法如下：\n(想用真心换取你的关注...蟹蟹泥...)\nsetting.json添加：\n{ &quot;name&quot;: &quot;ANTHROPIC_BASE_URL&quot;, &quot;value&quot;: &quot;https://xxxx&quot; }, \n{ &quot;name&quot;: &quot;ANTHROPIC_AUTH_TOKEN&quot;, "
  },
  {
    "id": "bvid:BV1vG8QzcE5X",
    "domain": "AI",
    "title": "Claude使用指南，claude code零基础教程，claude code安装配置到实战",
    "url": "http://www.bilibili.com/video/av114933744272468",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 358313,
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
    "points": 352190,
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
    "points": 324861,
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
    "points": 297094,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 230851,
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
    "points": 186409,
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
    "points": 165511,
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
    "points": 162859,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1b5AeeGEFc",
    "domain": "AI",
    "title": "Cursor太贵？分享三个免费AI编程方案+海量编程技巧【如何看待AI编程】",
    "url": "http://www.bilibili.com/video/av114025056699722",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 161886,
    "published_at": "2025-02-18T13:13:51+00:00",
    "summary": "我试用了几十种AI编程辅助工具，找到了其中三个免费，并且效果最好的方案。 本期视频就来跟大家分享一下。视频中间会穿插很多AI编程工具的使用技巧，还有看待AI编程的一些个人思考。本期视频没有广告都是个人的经验干货，废话不多说我们直接开始。"
  },
  {
    "id": "bvid:BV1kGo6BdEsT",
    "domain": "AI",
    "title": "如何用Claude Skill 做高质量 PPT（附完整教程）",
    "url": "http://www.bilibili.com/video/av116474832361424",
    "source": "阿西_出海",
    "platform": "bilibili",
    "points": 104436,
    "published_at": "2026-04-27T04:45:20+00:00",
    "summary": "很多人问我上期爆了的那条视频里，那个 PPT 是怎么做的。\n其实我是用 Anthropic 最近出的 Claude Design 做的，这个功能一发出来就在全网传疯了，一条推文就冲上了 6000 多万曝光。\n本期视频我会带你手把手从 0 到 1 把这个Skill 装好，然后一起跑一个成品效果出来。"
  },
  {
    "id": "bvid:BV1K6YM69ESq",
    "domain": "AI",
    "title": "AI+网络安全实战：从Agent入门到AI智能体挖漏洞教程！网络安全|信息安全|黑客技术|渗透测试|SRC漏洞挖掘|AI审计|HVV护网行动|靶场练习-码士集团",
    "url": "http://www.bilibili.com/video/av117247037213495",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 97324,
    "published_at": "2026-09-10T13:47:24+00:00",
    "summary": "这套课程围绕「AI+网络安全」展开，从AI智能体基础入门，到WorkBuddy、Trae等主流Agent工具的实际应用，再到API-Key接入、Skill使用等核心能力，逐步进入AI漏洞挖掘、代码审计、CTF题目分析等安全实战场景。同时结合SRC漏洞挖掘、HVV护网、安全竞赛以及网络安全就业方向，帮助你系统了解AI在网络安全学习、开发与实战中的应用方式。适合网络安全初学者、安全从业者以及希望利用A"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 94295,
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
    "points": 77770,
    "published_at": "2025-07-12T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operit教程：入门安卓最强大ai平台operitAI",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 77574,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV143wwz6E8F",
    "domain": "AI",
    "title": "Claude code科研使用展示与思路分享（提速就靠Ai）",
    "url": "http://www.bilibili.com/video/av116211882920985",
    "source": "科研推土机",
    "platform": "bilibili",
    "points": 76928,
    "published_at": "2026-03-11T18:12:00+00:00",
    "summary": "本期给大家带来的是Claude在Vscode的科研应用演示与我最近的一些心得使用心得，科研速度嘎嘎提升。论文复现画图、数据分析就靠Claude code。这个课程也是科研推土机「系统管理文献课程2.0」学员催我更新的内容，希望能帮助到大家～，这个视频重点讲两个事情：\n1️⃣ 资料获取，free不用怀疑，我是良心可言博主，，关注我(GZTSHNR)～\n2️⃣ 展示如何在VS code实操应用clau"
  },
  {
    "id": "bvid:BV19wXvBpEaL",
    "domain": "AI",
    "title": "认真用 Claude Code 的人，迟早会遇见 Everything Claude Code",
    "url": "http://www.bilibili.com/video/av116319122885806",
    "source": "极客魔导师",
    "platform": "bilibili",
    "points": 64125,
    "published_at": "2026-03-30T16:47:51+00:00",
    "summary": "Everything Claude Code 是目前 GitHub 上 116K star 的 Claude Code 配置项目。本期从斜杠命令、子代理、Hooks 到学习系统，带你把这个项目真正用起来。"
  },
  {
    "id": "bvid:BV1x3Wu6FEpj",
    "domain": "AI",
    "title": "【全网首发】如何不花钱雇24小时贴身秘书？全网最全的Personal AI保姆级的教程",
    "url": "http://www.bilibili.com/video/av117591808940027",
    "source": "GenJi是真想教会你",
    "platform": "bilibili",
    "points": 60552,
    "published_at": "2026-11-10T11:26:33+00:00",
    "summary": "消息回不完、自动扣费防不住、收藏夹一直吃灰，这些琐事你中了几条？这次我把生活和工作里的9件琐事，统统交给了蚂蚁新升级的个人AI助理【灵光2.0】，从下载登录、连接工具到布置长期任务，手把手带你玩一遍，看看最近爆火的Personal AI到底能帮我们管多少事。视频里的大肥鱼部署链接在评论区掉落，记得看到最后~"
  },
  {
    "id": "bvid:BV1xYwgztESh",
    "domain": "AI",
    "title": "Claude Code + PPTSkills  10分钟! 保姆级教程！ 生成可编辑科研汇报 PPT!",
    "url": "http://www.bilibili.com/video/av116234582495649",
    "source": "旭光升",
    "platform": "bilibili",
    "points": 59931,
    "published_at": "2026-03-15T18:25:56+00:00",
    "summary": "Claude Code4.6 + PPTSkills 保姆级教程！\n10分钟  生成可编辑科研汇报 PPT！"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 56847,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1h3W76wEem",
    "domain": "AI",
    "title": "Claude(Code)桌面APP，保姆级全攻略，一期视频精通，顶级Agent软件长什么样？",
    "url": "http://www.bilibili.com/video/av117580048108571",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 52335,
    "published_at": "2026-11-08T09:14:07+00:00",
    "summary": "最近Claude桌面端（Claude Desktop） 有了一大波功能更新。随着一步步的迭代，它已经把 Claude Code 的编程、Claude Design 的设计，以及 Claude Cowork 的办公等核心能力，全部收入了同一个桌面客户端，特别是Claude Code已经从原本黑乎乎的命令行工具，进化成了桌面客户端的完全体形态。再搭配上超强的Opus5.5 模型，已经能称得上是地表顶级"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 50358,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV17Lap6VEUr",
    "domain": "AI",
    "title": "【全80集】Vibe Coding 零基础入门到实战教程，由浅入深（全程干货）",
    "url": "http://www.bilibili.com/video/av117353572468721",
    "source": "数据拾光屋",
    "platform": "bilibili",
    "points": 49313,
    "published_at": "2026-10-02T09:25:00+00:00",
    "summary": "本套教程专门为零基础学员而制，全程干货无废话，喜欢的小伙伴记得点赞三连喔 ~"
  },
  {
    "id": "bvid:BV1vYFQzQE4P",
    "domain": "AI",
    "title": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！Claude Code Hooks回调+Agent Teams全自动开发零轮询",
    "url": "http://www.bilibili.com/video/av116046157647899",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 47816,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1thQPYfEYC",
    "domain": "AI",
    "title": "全流程演示Cursor + Blender MCP实现自动3D建模",
    "url": "http://www.bilibili.com/video/av114155835103525",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 44749,
    "published_at": "2025-03-13T15:31:17+00:00",
    "summary": "自动3D建模这个例子，是不是让大家一下子就看懂MCP的用途了。\n.\n后面会实测更多Cursor+MCP的更多玩法，欢迎继续围观\n.\n欢迎加入我的知识星球，有问必答：https://t.zsxq.com/fD4Fb\n.\nblender mcp项目：https://github.com/ahujasid/blender-mcp/tree/main"
  },
  {
    "id": "bvid:BV1uVSUBkEfZ",
    "domain": "AI",
    "title": "Microsoft Copilot完整教程(上) 从入门到Agent 一站式掌握AI办公",
    "url": "http://www.bilibili.com/video/av116351721084069",
    "source": "星小脉",
    "platform": "bilibili",
    "points": 44422,
    "published_at": "2026-04-05T11:00:20+00:00",
    "summary": "2026年最全面的Microsoft Copilot教程上半部分。从Copilot首页入门到Agent深度解析，涵盖搜索、资料库、AI视频生成、Copilot Pages、PowerPoint智能幻灯片等全部功能。由培训了6万人的AI顾问Cherie Brock与Sabrina Ramonov联合讲解。"
  },
  {
    "id": "bvid:BV1XiD5BQEAj",
    "domain": "AI",
    "title": "Claude Code 接入微信、一行命令把Claude Code装进微信、保姆级教程、微信支持Claude Code（cc-connect）远程开发",
    "url": "http://www.bilibili.com/video/av116350093694897",
    "source": "下班学AI",
    "platform": "bilibili",
    "points": 41353,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV1sQaL6vEkb",
    "domain": "AI",
    "title": "小白向，ai入门第一课：agent的部署和使用！",
    "url": "http://www.bilibili.com/video/av117349378166797",
    "source": "沈三殊",
    "platform": "bilibili",
    "points": 32874,
    "published_at": "2026-09-28T15:30:36+00:00",
    "summary": "详细的agent部署介绍：https://pan.quark.cn/s/3846914c6da7\n欢迎来到ai的世界！！\n有疑问欢迎私信。"
  },
  {
    "id": "bvid:BV1G6xW6WE6W",
    "domain": "AI",
    "title": "AI 人设教程，怎么让 AI 像个人",
    "url": "http://www.bilibili.com/video/av117540185446942",
    "source": "秋秋大肥鱼",
    "platform": "bilibili",
    "points": 31038,
    "published_at": "2026-11-01T08:17:22+00:00",
    "summary": "写人设别再堆形容词了。\n\n这条讲四件事：写她怕什么、先写句子再写性格、留个会犯的错、写完先跑几天。中间还有一段翻车现场——四条全写上了，开口还是像个客服。\n\n结尾给一个能直接省时间的做法。"
  },
  {
    "id": "bvid:BV1wpxq6VEXx",
    "domain": "AI",
    "title": "【AI时代的STM32教程】AI Agent 初体验",
    "url": "http://www.bilibili.com/video/av117529699682124",
    "source": "keysking",
    "platform": "bilibili",
    "points": 30334,
    "published_at": "2026-10-30T11:52:06+00:00",
    "summary": "一句话，让 AI 帮我们完成第一个 STM32C5 程序！🚀\n本期我们一起认识 AI Agent，学习如何描述开发需求，并借助开源的 STM32C5DevSkills，让 AI 完成工程创建、芯片配置、代码编写和编译烧录，让律动小板上的小灯闪烁起来！\n也特别感谢 @意法半导体中国   对本系列教程的支持～下期我们再亲手走一遍开发流程，把 Agent 替我们完成的工作，一步步搞明白！"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29944,
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
    "points": 29054,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1spTy6DEb4",
    "domain": "AI",
    "title": "Claude code接管科研全流程：cc-kaiti 带你从 0 走到开题报告和答辩 PPT",
    "url": "http://www.bilibili.com/video/av116866278233889",
    "source": "做科研的大师兄",
    "platform": "bilibili",
    "points": 25636,
    "published_at": "2026-07-05T07:53:28+00:00",
    "summary": "十二年科研经验加持的课题开题Skill，从零开始到拿到一份完整的开题报告及开题PPT，仅需一天！\n\n本次视频分享的cc-kaiti这个skill文件及配套的资料包，在后台私我“cc开题”获取~"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22856,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1f57C6YErb",
    "domain": "AI",
    "title": "手把手教你Codex安装和使用MCP！新手必备~",
    "url": "http://www.bilibili.com/video/av116696861907147",
    "source": "Raina测试",
    "platform": "bilibili",
    "points": 19188,
    "published_at": "2026-06-06T11:29:00+00:00",
    "summary": "这一期给大家分享下在codex里面如何配置和使用MCP，和skill一样，MCP也是我们平时用得比较多的，所以建议大家也可以学一下它的基础配置和使用~\n步骤都不难，跟着操作就可以了"
  },
  {
    "id": "bvid:BV1nwKc6pEmi",
    "domain": "AI",
    "title": "手把手教你用Claude Code做投研分析（AI Investing）",
    "url": "http://www.bilibili.com/video/av116938386775380",
    "source": "frank-quant",
    "platform": "bilibili",
    "points": 18815,
    "published_at": "2026-07-18T01:35:16+00:00",
    "summary": "只敲一行命令，就能得到一份带四个视角、交叉验证、明确标注不确定性的深度投研报告——这一期手把手教你怎么做到。\n\n我们实测了 GitHub 上爆火的开源项目 ai-berkshire（一万多 star）：它把巴菲特、芒格、段永平、李录四位大师的价值投资方法，做成了一套能在 Claude Code / Codex 里一条命令调用的 AI 投研工作流，一共 19 个技能。全程以小米集团为例，从安装、跑报"
  },
  {
    "id": "bvid:BV1iDRQBrEF6",
    "domain": "AI",
    "title": "Claude + Blender 现在太强了 —— 完整免费设置",
    "url": "http://www.bilibili.com/video/av116543333601720",
    "source": "设计之道",
    "platform": "bilibili",
    "points": 17996,
    "published_at": "2026-05-09T07:11:36+00:00",
    "summary": "【简介】\nAnthropic 刚刚发布了用于创意工具的官方 Claude Connectors —— 其中 Blender 连接器对 3D 艺术家来说最重要。在本视频中，我将展示最佳的 Claude + Blender 免费设置，以及为什么这次更新可能会改变我们构建 3D 场景的方式。\n\n【你将学到】\n01:13 步骤 1：安装 Blender MCP 和 Claude Code\n02:31 步骤"
  },
  {
    "id": "bvid:BV1xh3C6cEGv",
    "domain": "AI",
    "title": "两周完成一篇SCI论文，用claude code帮你干",
    "url": "http://www.bilibili.com/video/av117002408559933",
    "source": "博士大师兄木水",
    "platform": "bilibili",
    "points": 16161,
    "published_at": "2026-07-29T08:53:04+00:00",
    "summary": "大师兄八股文SCI速成模板已制作成skill，手把手带你实现一键生成SCI论文初稿"
  },
  {
    "id": "bvid:BV1yyQEBdEkm",
    "domain": "AI",
    "title": "【2026B站最全】Claude Code+软件测试实操教程!看完我直接删了收藏夹所有测试教程,从账号注册到Plan驱动测试项目,小白3天上手！",
    "url": "http://www.bilibili.com/video/av116408092525631",
    "source": "软件测试大神",
    "platform": "bilibili",
    "points": 15561,
    "published_at": "2026-04-15T09:55:02+00:00",
    "summary": "配套资料👉：https://b23.tv/qvhxmaQ\n包括:AI测试网站，几十个AI场景测试完整流程，skil文档，测试八股文，项目源码，测试用例模板，工具安装包，学习计划表，学习路线，100g测试新人资料包等等，资料百分百免费，放心领取~"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 13886,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
  },
  {
    "id": "hn:50418016",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia CEO Jensen Huang's letter to staff about affair",
    "url": "https://nvidianews.nvidia.com/news/a-message-to-our-company",
    "source": "karimf",
    "platform": "hackernews",
    "points": 980,
    "published_at": "2026-11-08T22:20:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:50362905",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia RTX Spark encrypted firmware slows inference speed to 35% on Linux",
    "url": "https://www.mindstudio.ai/blog/linux-nvidia-rtx-spark-laptop",
    "source": "novaRom",
    "platform": "hackernews",
    "points": 617,
    "published_at": "2026-11-04T08:46:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:50416801",
    "domain": "AI 算力 / 半导体",
    "title": "Statement from Nvidia board of directors",
    "url": "https://nvidianews.nvidia.com/news/statement-from-nvidia-board-of-directors",
    "source": "vincentchau",
    "platform": "hackernews",
    "points": 491,
    "published_at": "2026-11-08T20:26:43+00:00",
    "summary": ""
  },
  {
    "id": "hn:50293047",
    "domain": "AI 算力 / 半导体",
    "title": "Alleged Chinese spy had 'close relationship' with Nvidia boss Jensen Huang",
    "url": "https://nypost.com/2026/10/29/business/alleged-chinese-spy-had-close-relationship-with-nvidia-boss-jensen-huang-report/",
    "source": "mgh2",
    "platform": "hackernews",
    "points": 371,
    "published_at": "2026-10-29T17:43:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:50348962",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia – open-source auto-ontology",
    "url": "https://github.com/NVIDIA/auto-ontology",
    "source": "campervans",
    "platform": "hackernews",
    "points": 292,
    "published_at": "2026-11-03T07:04:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:50327058",
    "domain": "AI 算力 / 半导体",
    "title": "Seoul Viosys begins production of rare-earth-free white light emitter",
    "url": "https://www.semiconductor-today.com/news_items/2026/oct/seoul-291026.shtml",
    "source": "gmays",
    "platform": "hackernews",
    "points": 195,
    "published_at": "2026-11-01T16:23:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:50387738",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Kubernetes Engine (NVKE)",
    "url": "https://github.com/dsx-ai-factory/nvke",
    "source": "gkapur",
    "platform": "hackernews",
    "points": 124,
    "published_at": "2026-11-06T03:16:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:50427486",
    "domain": "AI 算力 / 半导体",
    "title": "Commerce Dept Inquiry into Megaspeed Halted After Nvdia Intervention",
    "url": "https://www.nytimes.com/2026/11/09/business/economy/nvidia-megaspeed-investigation-huang.html",
    "source": "louiereederson",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-11-09T16:10:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:50275128",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Nemotron 3.5 Transcribe: open ASR for 40 languages",
    "url": "https://huggingface.co/blog/nvidia/nemotron-transcribe-granary",
    "source": "wondersky",
    "platform": "hackernews",
    "points": 134,
    "published_at": "2026-10-28T15:17:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:50424604",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's China Problem [pdf]",
    "url": "https://culperresearch.com/wp-content/uploads/2026/05/Culper_NVDA_5-13-2026.pdf",
    "source": "Erikun",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-11-09T12:20:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:50392256",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia was in 1 in 11 startup rounds over $100M last year",
    "url": "https://datahyena.com/research/a-chipmaker-was-in-one-of-every-eleven-100m-rounds/",
    "source": "ghostfoxgod",
    "platform": "hackernews",
    "points": 82,
    "published_at": "2026-11-06T13:48:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:50363861",
    "domain": "AI 算力 / 半导体",
    "title": "RTX 5090 Street Prices Top $9k as Nvidia GPU Costs Climb",
    "url": "https://aroundprague.cz/en/news/us/rtx-5090-street-prices-top-9-000-as-nvidia-gpu-costs-climb",
    "source": "teleforce",
    "platform": "hackernews",
    "points": 78,
    "published_at": "2026-11-04T11:02:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:50416679",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Board to Probe Spying Case After CEO Admits Affair",
    "url": "https://www.bloomberg.com/news/articles/2026-11-08/nvidia-board-to-probe-spying-case-after-ceo-jensen-huang-admits-infidelity",
    "source": "specialp",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-11-08T20:14:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:50432415",
    "domain": "AI 算力 / 半导体",
    "title": "Fireworks AI Hacked",
    "url": "https://www.bloomberg.com/news/articles/2026-11-09/nvidia-backed-fireworks-ai-notifies-customers-of-its-second-hack-in-weeks",
    "source": "aeetes",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-11-09T21:26:09+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/dukosi-samples-contactless-battery-communication-system-for-evs-grid-storage/",
    "domain": "AI 算力 / 半导体",
    "title": "Dukosi Samples Contactless Battery Communication System for EVs, Grid Storage",
    "url": "https://www.eetimes.com/dukosi-samples-contactless-battery-communication-system-for-evs-grid-storage/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T08:30:00+00:00",
    "summary": "Dukosi DK-NFLNK provides synchronous communication with DKCMS battery monitoring systems. The post Dukosi Samples Contactless Battery Communication System for EVs, Grid Storage appeared first on EE Ti"
  },
  {
    "id": "rss:https://www.eetimes.com/saskatchewans-semiconductor-strength-is-connecting-the-pieces/",
    "domain": "AI 算力 / 半导体",
    "title": "Saskatchewan’s Semiconductor Strength Is Connecting the Pieces",
    "url": "https://www.eetimes.com/saskatchewans-semiconductor-strength-is-connecting-the-pieces/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T20:00:00+00:00",
    "summary": "Saskatchewan brings together AI infrastructure, quantum research, chip design talent, and advanced materials expertise to expand its role in Canada’s technology ecosystem. The post Saskatchewan’s Semi"
  },
  {
    "id": "rss:https://www.eetimes.com/people-detection-in-confined-spaces-elevator-application/",
    "domain": "AI 算力 / 半导体",
    "title": "People Detection in Confined Spaces: Elevator Application",
    "url": "https://www.eetimes.com/people-detection-in-confined-spaces-elevator-application/",
    "source": "Thomas Parton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T15:00:00+00:00",
    "summary": "This technical white paper details an embedded occupancy-monitoring solution for elevator cabins combining the Melexis MLX90642 Far-Infrared (FIR) thermal sensor array with a hardware-agnostic People "
  },
  {
    "id": "rss:https://www.eetimes.com/the-ai-power-bill-who-gets-grid-capacity-and-who-bears-the-risk/",
    "domain": "AI 算力 / 半导体",
    "title": "The AI Power Bill: Who Gets Grid Capacity, and Who Bears the Risk?",
    "url": "https://www.eetimes.com/the-ai-power-bill-who-gets-grid-capacity-and-who-bears-the-risk/",
    "source": "Ron Honig",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T15:00:00+00:00",
    "summary": "As electricity access becomes a financial barrier to AI expansion, the U.S. and China face different risks in building the infrastructure of the digital economy. The post The AI Power Bill: Who Gets G"
  },
  {
    "id": "rss:https://www.eetimes.com/bluetooth-high-data-throughput-a-foundation-for-next-generation-wireless-experiences/",
    "domain": "AI 算力 / 半导体",
    "title": "Bluetooth® High Data Throughput: a Foundation for Next Generation Wireless Experiences",
    "url": "https://www.eetimes.com/bluetooth-high-data-throughput-a-foundation-for-next-generation-wireless-experiences/",
    "source": "Bluetooth SIG",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T14:00:00+00:00",
    "summary": "Bluetooth® High Data Throughput enables faster data transfer, greater capacity, energy efficiency, and reliability for advanced wireless applications. The post Bluetooth® High Data Throughput: a Found"
  },
  {
    "id": "rss:https://www.eetimes.com/what-it-takes-to-let-a-farm-robot-work-alone/",
    "domain": "AI 算力 / 半导体",
    "title": "What It Takes to Let a Farm Robot Work Alone",
    "url": "https://www.eetimes.com/what-it-takes-to-let-a-farm-robot-work-alone/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T08:32:00+00:00",
    "summary": "Safe agricultural autonomy depends on matching safeguards to the machine, its surroundings, and the people who interact with it. The post What It Takes to Let a Farm Robot Work Alone appeared first on"
  },
  {
    "id": "rss:https://www.eetimes.com/we-source-chips-others-cannot-secure-2026/",
    "domain": "AI 算力 / 半导体",
    "title": "We Source Chips Others Cannot Secure, 2026",
    "url": "https://www.eetimes.com/we-source-chips-others-cannot-secure-2026/",
    "source": "Chang Ming International Technology Co., Ltd.",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T07:48:14+00:00",
    "summary": "Chang Ming delivers scarce semiconductors, with rigorous 9-step quality inspection &#038; global supply chain support for European &#038; American electronics buyers. The post We Source Chips Others C"
  },
  {
    "id": "rss:https://www.eetimes.com/gigadevice-new-gen-high-performance-mcu-portfolio-for-full-scenario-industrial-applications/",
    "domain": "AI 算力 / 半导体",
    "title": "GigaDevice New-Gen High-Performance MCU Portfolio for Full-Scenario Industrial Applications",
    "url": "https://www.eetimes.com/gigadevice-new-gen-high-performance-mcu-portfolio-for-full-scenario-industrial-applications/",
    "source": "GigaDevice",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T06:00:00+00:00",
    "summary": "GigaDevice officially lunches its new-generation GD32H7 MCU portfolio built on a unified chip architecture. Discover More. The post GigaDevice New-Gen High-Performance MCU Portfolio for Full-Scenario "
  },
  {
    "id": "rss:https://www.eetimes.com/can-jensen-keep-his-job/",
    "domain": "AI 算力 / 半导体",
    "title": "Can Jensen Keep His Job?",
    "url": "https://www.eetimes.com/can-jensen-keep-his-job/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T19:59:12+00:00",
    "summary": "Nvidia CEO admits to romantic affair with Megaspeed managing director, a known Chinese intelligence asset. The post Can Jensen Keep His Job? appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/advancing-integrated-optics-celestica-broadcom-interview-at-ocp-global-summit/",
    "domain": "AI 算力 / 半导体",
    "title": "Advancing Integrated Optics: Celestica & Broadcom Interview at OCP Global Summit",
    "url": "https://www.eetimes.com/advancing-integrated-optics-celestica-broadcom-interview-at-ocp-global-summit/",
    "source": "EE Times Partner Content",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T14:20:32+00:00",
    "summary": "Celestica and Broadcom explain how integrated optics can cut power and latency for AI data centers—watch the OCP Summit partner interview. The post Advancing Integrated Optics: Celestica &amp; Broadco"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/liquid-cooling/enterprising-pc-modder-makes-a-split-cooling-system-to-keep-it-from-overheating-his-room-winter-cold-keeps-cpu-and-gpu-temperatures-below-50-c-under-load",
    "domain": "AI 算力 / 半导体",
    "title": "Modder routes PC water cooling loop to radiator outside to beat the winter heat",
    "url": "https://www.tomshardware.com/pc-components/liquid-cooling/enterprising-pc-modder-makes-a-split-cooling-system-to-keep-it-from-overheating-his-room-winter-cold-keeps-cpu-and-gpu-temperatures-below-50-c-under-load",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T10:30:00+00:00",
    "summary": "A Reddit PC builder didn't want to bother opening a window in the winter when their system made their legs too hot, so they created an automated split cooling system to dump heat outside."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/3-500-ai-laser-robots-patrol-norwegian-salmon-farms-killing-sea-lice-parasites-get-zapped-by-high-tech-alternative-to-harsh-chemical-baths",
    "domain": "AI 算力 / 半导体",
    "title": "3,500 laser-armed AI submarine drones patrol Norwegian salmon farms, killing sea lice and protecting 112 million fish",
    "url": "https://www.tomshardware.com/tech-industry/drones/3-500-ai-laser-robots-patrol-norwegian-salmon-farms-killing-sea-lice-parasites-get-zapped-by-high-tech-alternative-to-harsh-chemical-baths",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T10:00:00+00:00",
    "summary": "3,500 Stingray AI laser robots deployed around salmon pens along the Norwegian coast 24/7 protect over 112 million fish from sea lice."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/policy/microsoft-lobbies-against-potential-ban-on-chinese-optical-networking-gear-for-ai-data-centers-as-fcc-mulls-restricting-imports-industry-group-says-move-could-grind-data-center-rollout-to-a-halt",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft lobbies against potential ban on Chinese optical networking gear for AI data centers as FCC mulls restricting imports",
    "url": "https://www.tomshardware.com/tech-industry/policy/microsoft-lobbies-against-potential-ban-on-chinese-optical-networking-gear-for-ai-data-centers-as-fcc-mulls-restricting-imports-industry-group-says-move-could-grind-data-center-rollout-to-a-halt",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T17:51:31+00:00",
    "summary": "The ITI is lobbying against the ban of these optical transceivers needed by data centers to convert electrical signals into optical signals."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-vp-and-chief-zen-architect-rebuke-claims-that-nvidia-and-arm-made-cpus-for-agentic-ai-we-didnt-magically-know-four-years-ago-that-agentic-was-going-to-be-a-thing",
    "domain": "AI 算力 / 半导体",
    "title": "AMD VP and chief Zen architect rebuke claims that Nvidia and Arm made CPUs for agentic AI — ‘We didn’t magically know four years ago that agentic was going to be a thing’",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-vp-and-chief-zen-architect-rebuke-claims-that-nvidia-and-arm-made-cpus-for-agentic-ai-we-didnt-magically-know-four-years-ago-that-agentic-was-going-to-be-a-thing",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T17:20:00+00:00",
    "summary": "Nvidia and Arm have new “agentic CPUs,” a title that high-ranking AMD employees are pushing back against with the launch of Zen 6 EPYC Venice CPUs."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-zen-6-epyc-venice-deep-dive-and-benchmarking-dual-epyc-9996-with-1-024-threads-delivers-up-to-93-percent-performance-gain-gen-on-gen-9686f-outclasses-nvidias-vera",
    "domain": "AI 算力 / 半导体",
    "title": "AMD Zen 6 EPYC ‘Venice’ deep dive and benchmarking",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-zen-6-epyc-venice-deep-dive-and-benchmarking-dual-epyc-9996-with-1-024-threads-delivers-up-to-93-percent-performance-gain-gen-on-gen-9686f-outclasses-nvidias-vera",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T17:00:00+00:00",
    "summary": "AMD has pulled back the curtain on its Zen 6 microarchitecture. We deep-dive into the differences between Zen 5 and 6, as well as detail our first benchmarks of AMD’s Venice CPUs."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/policy/alice-huang-reportedly-instrumental-in-securing-over-usd7-5-billion-of-nvidia-ai-gpu-imports-during-three-year-relationship-with-jensen-huang-helped-move-240-000-banned-chips-into-china-mostly-h100-and-h200",
    "domain": "AI 算力 / 半导体",
    "title": "Alice Huang reportedly instrumental in securing over $7.5 billion of Nvidia AI GPU imports during three-year relationship with Jensen Huang",
    "url": "https://www.tomshardware.com/tech-industry/policy/alice-huang-reportedly-instrumental-in-securing-over-usd7-5-billion-of-nvidia-ai-gpu-imports-during-three-year-relationship-with-jensen-huang-helped-move-240-000-banned-chips-into-china-mostly-h100-and-h200",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T16:50:02+00:00",
    "summary": "Alice Huang is reportedly connected to a web of Chinese companies, which then leveraged her closeness to Jensen Huang to gain access to billions of dollars' worth of Nvidia GPUs."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/secretlab-debuts-monitor-light-bar-add-on-to-reduce-glare-and-eye-strain-ergoarch-has-a-three-point-adjustment-arm-costs-usd179",
    "domain": "AI 算力 / 半导体",
    "title": "Secretlab debuts monitor light bar add-on to reduce glare and eye strain",
    "url": "https://www.tomshardware.com/peripherals/secretlab-debuts-monitor-light-bar-add-on-to-reduce-glare-and-eye-strain-ergoarch-has-a-three-point-adjustment-arm-costs-usd179",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T15:30:16+00:00",
    "summary": "Popular desk and chair maker Secretlab has released a new monitor light bar."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/new-framework-grades-ai-jailbreaks-across-capability-gains-scope-and-how-easy-they-are-to-deploy-frontier-model-forum-proposes-cvss-style-rating-system-for-new-ai-models",
    "domain": "AI 算力 / 半导体",
    "title": "New framework grades AI jailbreaks across capability gains, scope, and how easy they are to deploy",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/new-framework-grades-ai-jailbreaks-across-capability-gains-scope-and-how-easy-they-are-to-deploy-frontier-model-forum-proposes-cvss-style-rating-system-for-new-ai-models",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T13:40:00+00:00",
    "summary": "Frontier Model Forum releases its Jailbreak Rating Framework to estimate how easy it is for models to escape their cages and how much damage they can do."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/going-deep-on-local-ai-performance-with-apples-mac-studio-with-m5-ultra-inference-engine-recipes-mandatory-for-bigger-models-as-mlx-stack-matures",
    "domain": "AI 算力 / 半导体",
    "title": "Going deep on local AI performance benchmarking with Apple’s Mac Studio with M5 Ultra taking on Nvidia DGX Spark",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/going-deep-on-local-ai-performance-with-apples-mac-studio-with-m5-ultra-inference-engine-recipes-mandatory-for-bigger-models-as-mlx-stack-matures",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T13:20:00+00:00",
    "summary": "But if you're thinking about dropping over $10K for the purpose of building a local AI inference setup, is a Mac Studio right for you?"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/elon-musks-terafab-targets-1-million-wafers-a-month-after-2032-planned-700-000-monthly-memory-wafers-could-rival-samsungs-entire-estimated-dram-production-capacity",
    "domain": "AI 算力 / 半导体",
    "title": "Elon Musk’s Terafab targets 1 million wafers a month after 2032",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/elon-musks-terafab-targets-1-million-wafers-a-month-after-2032-planned-700-000-monthly-memory-wafers-could-rival-samsungs-entire-estimated-dram-production-capacity",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T13:00:00+00:00",
    "summary": "Tesla and SpaceX’s Terafab reportedly plans 1 million wafers per month after 2032, with about 700,000 for memory."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/linux/linus-torvalds-says-that-ai-fixes-drove-most-of-the-progress-in-latest-linux-kernel-bpf-saw-more-ai-written-fixes-than-bug-reports-possibly-indicating-a-tidal-shift-for-open-source-maintainers-tired-of-flood-of-junk-reports",
    "domain": "AI 算力 / 半导体",
    "title": "Linus Torvalds says that AI fixes drove most of the progress in latest Linux kernel",
    "url": "https://www.tomshardware.com/software/linux/linus-torvalds-says-that-ai-fixes-drove-most-of-the-progress-in-latest-linux-kernel-bpf-saw-more-ai-written-fixes-than-bug-reports-possibly-indicating-a-tidal-shift-for-open-source-maintainers-tired-of-flood-of-junk-reports",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T12:40:00+00:00",
    "summary": "Linus Torvalds thinks that AI fixes drove most of the progress in Linux kernel 7.4rc2 — BPF saw more AI-written fixes than bug reports, possibly indicating a tidal shift"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/policy/president-trump-says-the-fbi-is-investigating-jensen-huangs-affair-nvidia-also-accused-of-intervening-in-megaspeed-chip-smuggling-investigation",
    "domain": "AI 算力 / 半导体",
    "title": "President Trump says the FBI is investigating Jensen Huang’s affair",
    "url": "https://www.tomshardware.com/tech-industry/policy/president-trump-says-the-fbi-is-investigating-jensen-huangs-affair-nvidia-also-accused-of-intervening-in-megaspeed-chip-smuggling-investigation",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T12:33:17+00:00",
    "summary": "The FBI is probably concerned about the implication of a Chinese agent having influence over the leader of the U.S.'s leading AI chip manufacturer."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/usd10-programmer-saves-bios-locked-lenovo-thinkpads-from-the-dump-exploit-bypasses-supervisor-passwords-to-save-4th-to-8th-gen-intel-models-from-e-waste",
    "domain": "AI 算力 / 半导体",
    "title": "$10 programmer saves BIOS-locked Lenovo ThinkPads from the dump",
    "url": "https://www.tomshardware.com/laptops/usd10-programmer-saves-bios-locked-lenovo-thinkpads-from-the-dump-exploit-bypasses-supervisor-passwords-to-save-4th-to-8th-gen-intel-models-from-e-waste",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T12:20:00+00:00",
    "summary": "Many cheap company ThinkPads come with supervisor passwords and often end up as e-waste. Ukrainian YouTuber Hileeq shows how easy it is to bypass the password with a $10 programmer."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/software-engineer-rickrolls-his-prusa-3d-printer-via-remote-code-execution-exploit-one-week-of-testing-with-claude-opus-uncovers-23-prusa-buddy-firmware-defects",
    "domain": "AI 算力 / 半导体",
    "title": "Software engineer Rickrolls his Prusa 3D printer via remote code execution exploit",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/software-engineer-rickrolls-his-prusa-3d-printer-via-remote-code-execution-exploit-one-week-of-testing-with-claude-opus-uncovers-23-prusa-buddy-firmware-defects",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T12:18:07+00:00",
    "summary": "A software engineer demonstrated the ability to Rickroll a 3D printer via remote code execution (RCE). This security flaw has been fixed in the latest Prusa software."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/upgrade-your-ps5s-storage-for-gta-6s-digital-pre-load-with-these-ssd-storage-options-from-usd174-ultra-fast-drives-slot-into-the-m-2-expansion-slot-to-ready-your-console-for-gtas-huge-212gb-installation",
    "domain": "AI 算力 / 半导体",
    "title": "Upgrade your PS5's storage for GTA 6's digital pre-load with these SSD storage options from $174",
    "url": "https://www.tomshardware.com/video-games/playstation/upgrade-your-ps5s-storage-for-gta-6s-digital-pre-load-with-these-ssd-storage-options-from-usd174-ultra-fast-drives-slot-into-the-m-2-expansion-slot-to-ready-your-console-for-gtas-huge-212gb-installation",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T12:00:00+00:00",
    "summary": "With GTA 6's digital pre-loads beginning on November 10, you'll need enough storage on your PS5 to match. Here are some of the top PS5 SSD options to help you."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/steam-store-adds-average-fps-data-so-you-can-see-game-performance-before-making-a-purchase-steam-deck-only-for-now-with-desktop-pc-support-planned",
    "domain": "AI 算力 / 半导体",
    "title": "Steam Store adds average FPS data so you can see game performance before making a purchase",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/steam-store-adds-average-fps-data-so-you-can-see-game-performance-before-making-a-purchase-steam-deck-only-for-now-with-desktop-pc-support-planned",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T11:53:36+00:00",
    "summary": "Valve is adding a new feature to the Steam store that tracks performance data and then displays it anonymously to users who match the hardware."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/controllers-gamepads/grab-this-gamesir-super-nova-wireless-controller-at-a-record-low-amazon-price-now-under-usd40-20-percent-discount-on-pc-and-switch-gamepad-that-ships-with-drift-free-hall-effect-sticks-and-a-customizable-layout",
    "domain": "AI 算力 / 半导体",
    "title": "Grab this GameSir Super Nova wireless controller at a record-low Amazon price, now under $40",
    "url": "https://www.tomshardware.com/peripherals/controllers-gamepads/grab-this-gamesir-super-nova-wireless-controller-at-a-record-low-amazon-price-now-under-usd40-20-percent-discount-on-pc-and-switch-gamepad-that-ships-with-drift-free-hall-effect-sticks-and-a-customizable-layout",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T11:42:06+00:00",
    "summary": "Grab this fully loaded wireless gaming controller from GameSir for a record-low Amazon price of $39.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ddr5/grab-32gb-ddr5-for-usd371-in-this-newegg-ram-bundle-with-the-9800x3d-usd70-less-than-buying-it-separately-usd138-saving-on-parts-for-a-4k-gaming-pc-including-a-gigabyte-x870-motherboard-and-free-atx-case",
    "domain": "AI 算力 / 半导体",
    "title": "Grab 32GB DDR5 for $371 in this Newegg RAM bundle with the 9800X3D, $70 less than buying it separately",
    "url": "https://www.tomshardware.com/pc-components/ddr5/grab-32gb-ddr5-for-usd371-in-this-newegg-ram-bundle-with-the-9800x3d-usd70-less-than-buying-it-separately-usd138-saving-on-parts-for-a-4k-gaming-pc-including-a-gigabyte-x870-motherboard-and-free-atx-case",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T11:09:51+00:00",
    "summary": "This Newegg bundle brings together the AMD Ryzen 7 9800X3D, 32GB of DDR5-6000 RAM, a Gigabyte X870 Aorus Elite Wi-Fi 7 motherboard, and a free ATX case for $1,090.98."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/external-ssds/seagate-resurrects-hybrid-storage-hands-on-with-the-firecuda-forge-8-or-20tb-external-hard-drive-requires-you-to-bring-your-own-nvme-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Seagate resurrects hybrid storage: Hands-on with the FireCuda Forge – 8 or 20TB external hard drive requires you to bring your own NVMe SSD",
    "url": "https://www.tomshardware.com/pc-components/external-ssds/seagate-resurrects-hybrid-storage-hands-on-with-the-firecuda-forge-8-or-20tb-external-hard-drive-requires-you-to-bring-your-own-nvme-ssd",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T11:01:00+00:00",
    "summary": "Seagate takes on high SSD storage prices with the Firecuda Forge, a 8TB or 20TB hard drive that requires you to bring your own M.2 2280 SSD (ideally 1TB, with DRAM). It's a throwback to the days of hy"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/all-net-connected-vehicles-from-two-major-automakers-allowed-hackers-to-remotely-unlock-doors-and-start-the-engine-now-patched-hard-coded-credentials-and-bypassed-mfa-security-showcase-a-lack-of-101-level-best-practices",
    "domain": "AI 算力 / 半导体",
    "title": "All net-connected vehicles from two major automakers allowed hackers to remotely unlock doors and start the engine",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/all-net-connected-vehicles-from-two-major-automakers-allowed-hackers-to-remotely-unlock-doors-and-start-the-engine-now-patched-hard-coded-credentials-and-bypassed-mfa-security-showcase-a-lack-of-101-level-best-practices",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T10:50:00+00:00",
    "summary": "Any net-connected vehicle from two automakers could be remotely opened and started — now-patched failures with API backend security showcase a lack of 101-level best practices"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/space/orbiting-esa-satellite-plays-doom-after-receiving-voice-commands-from-amateur-radio-operators-on-earth-27-mb-ai-speech-model-executes-the-game-on-the-seventh-attempt",
    "domain": "AI 算力 / 半导体",
    "title": "Orbiting ESA satellite plays Doom after receiving voice commands from amateur radio operators on Earth",
    "url": "https://www.tomshardware.com/tech-industry/space/orbiting-esa-satellite-plays-doom-after-receiving-voice-commands-from-amateur-radio-operators-on-earth-27-mb-ai-speech-model-executes-the-game-on-the-seventh-attempt",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T10:30:00+00:00",
    "summary": "Radio amateurs in Oslo spoke a command to ESA’s OPS-SAT PRETTY satellite, which recognized it on board and launched Doom."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/law-firm-files-class-action-lawsuit-against-nvidia-after-ceo-jensen-huang-confirms-affair-with-alleged-chinese-spy-more-to-come-as-multiple-other-law-firms-investigate-securities-fraud-following-stock-drop",
    "domain": "AI 算力 / 半导体",
    "title": "Law firm files class-action lawsuit against Nvidia after CEO Jensen Huang confirms affair with alleged Chinese spy",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/law-firm-files-class-action-lawsuit-against-nvidia-after-ceo-jensen-huang-confirms-affair-with-alleged-chinese-spy-more-to-come-as-multiple-other-law-firms-investigate-securities-fraud-following-stock-drop",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T00:03:08+00:00",
    "summary": "Class-action lawsuit and legal investigations against Nvidia over securities fraud start flying"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cryptocurrency/ethereum-foundation-sued-after-firing-employee-over-mandatory-source-seppuku-suicide-pact-crypto-firm-demanded-employees-pledge-to-take-their-own-lives-with-a-sword-to-protect-open-source-code-founder-vitalik-claims-1-000-year-mandate-just-artwork",
    "domain": "AI 算力 / 半导体",
    "title": "Ethereum Foundation sued after firing employee over mandatory 'Source Seppuku' suicide pact",
    "url": "https://www.tomshardware.com/tech-industry/cryptocurrency/ethereum-foundation-sued-after-firing-employee-over-mandatory-source-seppuku-suicide-pact-crypto-firm-demanded-employees-pledge-to-take-their-own-lives-with-a-sword-to-protect-open-source-code-founder-vitalik-claims-1-000-year-mandate-just-artwork",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T18:43:48+00:00",
    "summary": "A former employee of The Ethereum Foundation is suing the nonprofit after being fired for refusing to sign its 'Source Seppuku License.'"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/policy/nvidia-cracks-down-on-overseas-cloud-ai-gpu-rentals-for-china-partners-face-51-percent-non-chinese-quota-as-black-market-b300-rack-prices-surge-to-usd2-8-million",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia cracks down on overseas cloud AI GPU rentals for China",
    "url": "https://www.tomshardware.com/tech-industry/policy/nvidia-cracks-down-on-overseas-cloud-ai-gpu-rentals-for-china-partners-face-51-percent-non-chinese-quota-as-black-market-b300-rack-prices-surge-to-usd2-8-million",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T17:48:17+00:00",
    "summary": "Nvidia may cap cloud partners’ Chinese business at 49% as Chinese firms buy up more than 1 million gaming and workstation GPUs."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/nvidia-ceo-jensen-huang-summoned-to-congressional-committee-over-affair-with-alleged-chinese-spy-says-recent-reports-raise-concerns-over-security-protocols-and-ties-to-chinese-intelligence",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia CEO Jensen Huang summoned to Congress over affair with alleged Chinese spy",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/nvidia-ceo-jensen-huang-summoned-to-congressional-committee-over-affair-with-alleged-chinese-spy-says-recent-reports-raise-concerns-over-security-protocols-and-ties-to-chinese-intelligence",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T15:57:13+00:00",
    "summary": "Jensen Huang has been summoned to appear before Congress's Select Committee on the CCP."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/deepx-ai-chip-runs-so-cool-that-a-butter-heatsink-doesnt-melt-the-dx-m1-processor-impresses-in-a-bizarre-new-dairy-based-benchmark",
    "domain": "AI 算力 / 半导体",
    "title": "Bizarre AI chip demo uses butter to highlight how new chip runs 40 degrees cooler than the competition",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/deepx-ai-chip-runs-so-cool-that-a-butter-heatsink-doesnt-melt-the-dx-m1-processor-impresses-in-a-bizarre-new-dairy-based-benchmark",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T15:15:00+00:00",
    "summary": "DEEPX demonstrated its DX-M1 processor’s cool running capabilities in a bizarre dairy-based thermal benchmark."
  },
  {
    "id": "hn:50073879",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon",
    "url": "https://deepmind.google/models/gemini/",
    "source": "737max",
    "platform": "hackernews",
    "points": 1467,
    "published_at": "2026-10-13T16:03:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:50261319",
    "domain": "大厂 AI 动态",
    "title": "Genie 4",
    "url": "https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/",
    "source": "acossta",
    "platform": "hackernews",
    "points": 1044,
    "published_at": "2026-10-27T16:06:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:50276792",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Carbon",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/",
    "source": "acossta",
    "platform": "hackernews",
    "points": 1019,
    "published_at": "2026-10-28T17:01:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:50403097",
    "domain": "大厂 AI 动态",
    "title": "Every Mac comes with an (undocumented) family member classifier",
    "url": "https://8rank.ai/game/apple-intelligence-personal-knowledge-graph",
    "source": "infwhispers",
    "platform": "hackernews",
    "points": 867,
    "published_at": "2026-11-07T09:46:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:50429426",
    "domain": "大厂 AI 动态",
    "title": "Google Gemini routes personal Drive files and emails to human annotators",
    "url": "https://github.com/thisisme6598/gemini_files/",
    "source": "gf74918",
    "platform": "hackernews",
    "points": 720,
    "published_at": "2026-11-09T18:24:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:50363461",
    "domain": "大厂 AI 动态",
    "title": "Tell HN: Gemini trains on chat history, even for subscribers (personal accounts)",
    "url": "https://news.ycombinator.com/item?id=50363461",
    "source": "jameslk",
    "platform": "hackernews",
    "points": 737,
    "published_at": "2026-11-04T10:10:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:50439193",
    "domain": "大厂 AI 动态",
    "title": "AlphaProof Code",
    "url": "https://deepmind.google/blog/introducing-alphaproof-code/",
    "source": "ilreb",
    "platform": "hackernews",
    "points": 639,
    "published_at": "2026-11-10T12:11:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:50411961",
    "domain": "大厂 AI 动态",
    "title": "Llama-modchip: 284B DeepSeek on 64GB RAM, no GPU",
    "url": "https://github.com/synchopate/llama-modchip",
    "source": "joshcsimmons",
    "platform": "hackernews",
    "points": 483,
    "published_at": "2026-11-08T10:22:04+00:00",
    "summary": ""
  },
  {
    "id": "hn:50392118",
    "domain": "大厂 AI 动态",
    "title": "Gemini Omni 1.2 Flash",
    "url": "https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/",
    "source": "thisisauserid",
    "platform": "hackernews",
    "points": 369,
    "published_at": "2026-11-06T13:35:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:50442303",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Carbon is now available",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/",
    "source": "meetpateltech",
    "platform": "hackernews",
    "points": 285,
    "published_at": "2026-11-10T16:07:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:50122431",
    "domain": "大厂 AI 动态",
    "title": "Llama.cpp on a jailbroken PS5: run any GGUF model natively on the console",
    "url": "https://github.com/cobanov/PS5LM",
    "source": "Anon84",
    "platform": "hackernews",
    "points": 375,
    "published_at": "2026-10-16T18:32:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:50288019",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Carbon is the new #1 on the Artificial Analysis Intelligence Index v5",
    "url": "https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1",
    "source": "theHocineSaad",
    "platform": "hackernews",
    "points": 339,
    "published_at": "2026-10-29T12:41:56+00:00",
    "summary": ""
  },
  {
    "id": "hn:50118688",
    "domain": "大厂 AI 动态",
    "title": "Show HN: Gemini 4 Argon plays StarCraft",
    "url": "https://starskirmish.com/bench/v0-2/",
    "source": "__cayenne__",
    "platform": "hackernews",
    "points": 254,
    "published_at": "2026-10-16T14:18:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:50074869",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon for Robotics",
    "url": "https://developers.googleblog.com/gemini-4-argon-for-robotics/",
    "source": "xnx",
    "platform": "hackernews",
    "points": 235,
    "published_at": "2026-10-13T16:55:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:50355504",
    "domain": "大厂 AI 动态",
    "title": "Google researchers demand freedom to tell the world what they know about AI",
    "url": "https://www.washingtonpost.com/technology/2026/11/03/google-deepmind-staff-protest-lifetime-ban-criticizing-company/",
    "source": "nsagent",
    "platform": "hackernews",
    "points": 92,
    "published_at": "2026-11-03T17:55:26+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/tech/1031446/microsoft-automatic-super-resolution-auto-sr-upscaling",
    "domain": "大厂 AI 动态",
    "title": "Microsoft’s DLSS competitor is out for the Xbox Ally X and works in handheld mode",
    "url": "https://www.theverge.com/tech/1031446/microsoft-automatic-super-resolution-auto-sr-upscaling",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T00:34:24+00:00",
    "summary": "Microsoft is now rolling out Automatic Super Resolution (Auto SR), an upscaling technology that competes with Nvidia's DLSS, for the Xbox Ally X, Xbox Ally X20, and select Windows Copilot Plus PCs, th"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1031256/meta-quest-disney-plus-vr-3d-movies",
    "domain": "大厂 AI 动态",
    "title": "The VR Disney Plus app on Meta Quest now has 3D movies",
    "url": "https://www.theverge.com/tech/1031256/meta-quest-disney-plus-vr-3d-movies",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T22:00:00+00:00",
    "summary": "Disney is bringing more than 60 3D movies to the Disney Plus app on Meta Quest. The movies will be available to Disney Plus subscribers as part of an updated Disney Plus app that's rolling out today. "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1031284/oura-counsel-health-acquisition",
    "domain": "大厂 AI 动态",
    "title": "Oura is acquiring medical AI chatbot startup Counsel Health",
    "url": "https://www.theverge.com/gadgets/1031284/oura-counsel-health-acquisition",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T21:40:31+00:00",
    "summary": "Oura announced its quarterly earnings today and said it agreed to acquire Counsel Health for $625 million, after adding the company's AI chatbot to its app earlier this year. Counsel Health calls itse"
  },
  {
    "id": "rss:https://www.theverge.com/games/1031242/sony-playstation-fairgames-canceled",
    "domain": "大厂 AI 动态",
    "title": "Sony cancels live-service shooter Fairgames",
    "url": "https://www.theverge.com/games/1031242/sony-playstation-fairgames-canceled",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T21:06:12+00:00",
    "summary": "Sony has canceled Fairgames, a heist game announced in 2023, according to Bloomberg. Fairgames had once been part of Sony's big planned push for PlayStation live service games, but the company ended u"
  },
  {
    "id": "rss:https://www.theverge.com/games/1031144/sony-playstation-plus-windows-pc-app-shutting-down",
    "domain": "大厂 AI 动态",
    "title": "The PlayStation Plus PC app is shutting down next month",
    "url": "https://www.theverge.com/games/1031144/sony-playstation-plus-windows-pc-app-shutting-down",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T19:40:52+00:00",
    "summary": "Sony is retiring the PlayStation Plus app for PC on December 10th. Sony says it will notify users directly about the shutdown. The app allowed PlayStation Plus Premium subscribers to stream certain ga"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1031028/spacex-starlink-mini-2-satellite-internet-terminal-hot-swap-battery",
    "domain": "大厂 AI 动态",
    "title": "Starlink Mini 2 adds a swappable battery",
    "url": "https://www.theverge.com/tech/1031028/spacex-starlink-mini-2-satellite-internet-terminal-hot-swap-battery",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T19:19:12+00:00",
    "summary": "SpaceX announced a new version of its all-in-one satellite internet terminal that integrates a dish, Wi-Fi router, and now a battery into a single device about the size of a laptop. According to some "
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1031063/jensen-huang-ai-race-us-china-spy",
    "domain": "大厂 AI 动态",
    "title": "The US is winning the AI race. Jensen Huang could have blown it",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1031063/jensen-huang-ai-race-us-china-spy",
    "source": "Robert Hart",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T19:04:05+00:00",
    "summary": "As espionage targets go, Jensen Huang is perhaps one of the least surprising on Earth. The Nvidia CEO runs one of the world's most valuable companies, controls the in-demand technology fueling the AI "
  },
  {
    "id": "rss:https://www.theverge.com/tech/1030766/google-pixel-tag-tracker-find-hub-uwb-bluetooth-sounding",
    "domain": "大厂 AI 动态",
    "title": "Google’s Pixel Tag tracker is now available",
    "url": "https://www.theverge.com/tech/1030766/google-pixel-tag-tracker-find-hub-uwb-bluetooth-sounding",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T19:00:00+00:00",
    "summary": "After years of third-party Android trackers from companies like Samsung, Motorola, and Pebblebee, Google's Pixel Tag is now available for purchase. First announced in August, the Pixel Tag is designed"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1031089/google-pixel-drop-november-2026-hilight",
    "domain": "大厂 AI 动态",
    "title": "Google is making Pixel HiLight slightly more useful",
    "url": "https://www.theverge.com/tech/1031089/google-pixel-drop-november-2026-hilight",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T19:00:00+00:00",
    "summary": "Google is adding a new feature to its underwhelming HiLight light on the back of Pixel 11 Pro phones: As part of the November 2026 Pixel Drop, the light can light up when you get Google Messages texts"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1030970/bambu-p2s-combo-3d-printer-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "One of our favorite multi-filament 3D printers is $100 off",
    "url": "https://www.theverge.com/gadgets/1030970/bambu-p2s-combo-3d-printer-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T18:42:03+00:00",
    "summary": "If you’re tired of filament jams and clogged nozzles, perhaps it’s time for a new 3D printer. Through December 1st, the Bambu Lab P2S Combo, currently one of the best models that’s easy to use, is dis"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/10/nvidias-crisis-has-corporate-governance-experts-reaching-for-the-popcorn/",
    "domain": "大厂 AI 动态",
    "title": "Nvidia’s crisis has corporate governance experts reaching for the popcorn",
    "url": "https://techcrunch.com/2026/11/10/nvidias-crisis-has-corporate-governance-experts-reaching-for-the-popcorn/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T07:30:51+00:00",
    "summary": "The governance experts we talked to say nobody has seen anything like what's unfolding right now."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/10/x-launches-its-own-clipping-feature-to-spur-influencer-engagement/",
    "domain": "大厂 AI 动态",
    "title": "X launches its own clipping feature to spur influencer engagement",
    "url": "https://techcrunch.com/2026/11/10/x-launches-its-own-clipping-feature-to-spur-influencer-engagement/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T01:02:13+00:00",
    "summary": "X is jumping into clipping, the popular practice of cutting long videos into short, shareable clips that can go viral."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/10/openai-acquires-odessia-travel-startup-created-by-sonder-founder/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI acquires Odessia, travel startup created by Sonder founder",
    "url": "https://techcrunch.com/2026/11/10/openai-acquires-odessia-travel-startup-created-by-sonder-founder/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T21:08:52+00:00",
    "summary": "OpenAI has not yet said what its plans are for the future of travel. But Sonder founder Francis Davidson is a well-known figure in the travel industry."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/10/openai-anthropic-face-new-oversight-as-new-yorks-ai-safety-law-takes-effect/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI, Anthropic face new oversight as New York’s AI safety law takes effect",
    "url": "https://techcrunch.com/2026/11/10/openai-anthropic-face-new-oversight-as-new-yorks-ai-safety-law-takes-effect/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T20:52:13+00:00",
    "summary": "New York is preparing to enforce its sweeping AI safety law, requiring major developers like OpenAI and Anthropic to register, disclose safety practices, and report critical incidents or face fines."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/10/proximal-ventures-raises-debut-fund-to-back-startups-bringing-ai-to-drug-development/",
    "domain": "大厂 AI 动态",
    "title": "Proximal Ventures raises debut fund to back startups bringing AI to drug development",
    "url": "https://techcrunch.com/2026/11/10/proximal-ventures-raises-debut-fund-to-back-startups-bringing-ai-to-drug-development/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T20:47:05+00:00",
    "summary": "Former SignalFire investor Sahir Raoof raises $27.5 million for new fund targeting AI in pharma."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/10/x-energy-gets-green-light-to-build-its-first-small-modular-nuclear-reactors/",
    "domain": "大厂 AI 动态",
    "title": "X-energy gets green light to build its first small modular nuclear reactors",
    "url": "https://techcrunch.com/2026/11/10/x-energy-gets-green-light-to-build-its-first-small-modular-nuclear-reactors/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T20:43:55+00:00",
    "summary": "X-energy received a construction permit from the U.S. Nuclear Regulatory Commission to build four reactors in Texas."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/10/all-7-anthropic-founders-will-each-cash-out-about-250m-in-ipo/",
    "domain": "大厂 AI 动态",
    "title": "All 7 Anthropic founders will each cash out about $250M in IPO",
    "url": "https://techcrunch.com/2026/11/10/all-7-anthropic-founders-will-each-cash-out-about-250m-in-ipo/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T19:57:52+00:00",
    "summary": "Each of the seven co-founders plans to sell exactly the same number of shares in the IPO, which would bring each of them about $250 million in cash at the midpoint of the price range while leaving the"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/10/oura-to-acquire-ai-native-primary-care-startup-counsel-health-for-625m/",
    "domain": "大厂 AI 动态",
    "title": "Oura to acquire AI-native primary care startup Counsel Health for $625M",
    "url": "https://techcrunch.com/2026/11/10/oura-to-acquire-ai-native-primary-care-startup-counsel-health-for-625m/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T19:23:34+00:00",
    "summary": "The deal comes a few weeks after Oura postponed its up to $2.2 billion IPO indefinitely, citing “uncertainty in the IPO market.”"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/10/psi-is-trying-to-make-a-business-out-of-ai-driven-scientific-discovery/",
    "domain": "大厂 AI 动态",
    "title": "PSI is trying to make a business out of AI-driven scientific discovery",
    "url": "https://techcrunch.com/2026/11/10/psi-is-trying-to-make-a-business-out-of-ai-driven-scientific-discovery/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T19:03:52+00:00",
    "summary": "PSI used an unreleased Anthropic model to answer a fundamental question about quantum computing that scientists have pursued for nearly two decades."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/10/openai-rolls-out-new-business-profiles-making-chatgpt-just-a-little-bit-more-like-google/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI rolls out new business profiles, making ChatGPT just a little bit more like Google",
    "url": "https://techcrunch.com/2026/11/10/openai-rolls-out-new-business-profiles-making-chatgpt-just-a-little-bit-more-like-google/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T18:49:52+00:00",
    "summary": "OpenAI is looking to make ChatGPT a more robust consumer discovery engine, and a host of new features seek to empower businesses to help it do that."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/10/pixel-tag-googles-30-android-ready-answer-to-apples-airtag-is-now-available/",
    "domain": "大厂 AI 动态",
    "title": "Pixel Tag, Google’s $30 Android-ready answer to Apple’s AirTag, is now available",
    "url": "https://techcrunch.com/2026/11/10/pixel-tag-googles-30-android-ready-answer-to-apples-airtag-is-now-available/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T18:49:19+00:00",
    "summary": "Google's Pixel Tag lets you track lost items with your Android device, similar to Apple's AirTag."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/10/anthropic-launches-claude-meetings-to-turn-workplace-discussions-into-plans-and-tasks/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic launches Claude Meetings to turn workplace discussions into plans and tasks",
    "url": "https://techcrunch.com/2026/11/10/anthropic-launches-claude-meetings-to-turn-workplace-discussions-into-plans-and-tasks/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T17:30:00+00:00",
    "summary": "As participants talk, Claude can draft the plan being discussed, map out a timeline on a whiteboard, answer questions in the meeting chat, and access connected work apps to retrieve information, such "
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/10/nvidia-ceo-jensen-huangs-affair-with-alleged-chinese-spy-a-timeline/",
    "domain": "大厂 AI 动态",
    "title": "Nvidia CEO Jensen Huang’s affair with alleged Chinese spy: a timeline",
    "url": "https://techcrunch.com/2026/11/10/nvidia-ceo-jensen-huangs-affair-with-alleged-chinese-spy-a-timeline/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T17:04:19+00:00",
    "summary": "The affair could have ramifications for national security as the U.S. and China race to develop the most advanced AI infrastructure."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/10/sundrop-turns-your-endless-baby-photos-into-recaps-time-lapses-and-more-without-ai/",
    "domain": "大厂 AI 动态",
    "title": "Sundrop turns your endless baby photos into recaps, time lapses, and more — without AI",
    "url": "https://techcrunch.com/2026/11/10/sundrop-turns-your-endless-baby-photos-into-recaps-time-lapses-and-more-without-ai/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T16:50:38+00:00",
    "summary": "Sundrop is a new iPhone app that uses Apple's on-device AI to help parents rediscover their favorite photos and create keepsakes without uploading images to the cloud."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/10/apple-tv-makes-sign-language-interpretation-a-built-in-accessibility-feature/",
    "domain": "大厂 AI 动态",
    "title": "Apple TV makes sign language interpretation a built-in accessibility feature",
    "url": "https://techcrunch.com/2026/11/10/apple-tv-makes-sign-language-interpretation-a-built-in-accessibility-feature/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T16:00:00+00:00",
    "summary": "Apple TV's new accessibility feature lets viewers turn on sign language interpretation within supported titles."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/10/google-broadens-its-ai-hardware-portfolio-with-two-new-specialized-chips/",
    "domain": "大厂 AI 动态",
    "title": "Google broadens its AI hardware portfolio with two new specialized chips",
    "url": "https://techcrunch.com/2026/11/10/google-broadens-its-ai-hardware-portfolio-with-two-new-specialized-chips/",
    "source": "Ram Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T15:54:08+00:00",
    "summary": "Google's new tensor processing units (TPUs) broaden its chip portfolio to more use cases: confidential model training and more memory capacity."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/10/n-able-takes-its-remote-access-service-offline-after-researcher-publishes-dozens-of-zero-day-bugs/",
    "domain": "大厂 AI 动态",
    "title": "N-able takes its remote access service offline after researcher publishes dozens of zero-day bugs",
    "url": "https://techcrunch.com/2026/11/10/n-able-takes-its-remote-access-service-offline-after-researcher-publishes-dozens-of-zero-day-bugs/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T15:45:27+00:00",
    "summary": "The remote access giant also urged its self-hosted customers to take down their own servers amid a \"critical security incident,\" fearing the possibility of cyberattacks."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/10/metas-ai-agent-muse-lands-on-apple-watch-and-wear-os/",
    "domain": "大厂 AI 动态",
    "title": "Meta’s AI agent Muse lands on Apple Watch and Android Wear OS",
    "url": "https://techcrunch.com/2026/11/10/metas-ai-agent-muse-lands-on-apple-watch-and-wear-os/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T15:29:30+00:00",
    "summary": "Users can now interact with Meta’s AI assistant through voice calls, text messages, or dictation on their Apple Watch."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/10/reddit-is-turning-user-conversations-into-ai-powered-product-reviews/",
    "domain": "大厂 AI 动态",
    "title": "Reddit is turning user conversations into AI-powered product reviews",
    "url": "https://techcrunch.com/2026/11/10/reddit-is-turning-user-conversations-into-ai-powered-product-reviews/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T15:00:00+00:00",
    "summary": "Reddit's new AI-powered reviews summarize what users like and dislike about 10,000 products, helping shoppers research purchases ahead of the holidays."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/10/new-whatsapp-head-wants-to-make-the-app-easier-to-use-give-its-ai-more-chops/",
    "domain": "大厂 AI 动态",
    "title": "New WhatsApp head wants to make the app easier to use, give its AI more chops",
    "url": "https://techcrunch.com/2026/11/10/new-whatsapp-head-wants-to-make-the-app-easier-to-use-give-its-ai-more-chops/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T15:00:00+00:00",
    "summary": "Kunal Shah said the company wants to make voice notes, groups, stickers, and video \"simpler and more expressive.\""
  },
  {
    "id": "rss:https://stratechery.com/2026/the-jensen-huang-story-gets-worse-washington-vs-new-york-silicon-valley/",
    "domain": "大厂 AI 动态",
    "title": "The Jensen Huang Story Gets Worse, Washington vs. New York, Silicon Valley",
    "url": "https://stratechery.com/2026/the-jensen-huang-story-gets-worse-washington-vs-new-york-silicon-valley/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T11:00:00+00:00",
    "summary": "The Jensen Huang story got worse for him on Monday; the real risk for Huang is governance, even more than national security. Who benefits?"
  },
  {
    "id": "rss:https://stratechery.com/2026/jensen-huangs-affair-the-culper-report-huangs-righteousness/",
    "domain": "大厂 AI 动态",
    "title": "Jensen Huang’s Affair, The Culper Report, Huang’s Righteousness",
    "url": "https://stratechery.com/2026/jensen-huangs-affair-the-culper-report-huangs-righteousness/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T11:00:00+00:00",
    "summary": "Nvidia CEO Jensen Huang admitted to an affair with a Chinese spy, and that might not be the end of his troubles. I hope he survives, but his influence will never be the same."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/11/seagate-resurrects-the-ssd-hdd-hybrid-drive/",
    "domain": "大厂 AI 动态",
    "title": "Seagate's new hybrid drive raises some old questions",
    "url": "https://arstechnica.com/gadgets/2026/11/seagate-resurrects-the-ssd-hdd-hybrid-drive/",
    "source": "Nick Indge",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T23:30:56+00:00",
    "summary": "The FireCuda Forge revisits an old idea, with some familiar questions."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/11/the-us-military-seems-to-be-getting-nervous-about-the-launch-supply-crunch/",
    "domain": "大厂 AI 动态",
    "title": "The US military seems to be getting nervous about the launch supply crunch",
    "url": "https://arstechnica.com/space/2026/11/the-us-military-seems-to-be-getting-nervous-about-the-launch-supply-crunch/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T23:02:39+00:00",
    "summary": "\"Launch is extremely constrained and that is exactly the situation we predicted.\""
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/11/ring-cameras-go-mobile-as-amazon-debuts-ai-powered-security-drone-and-robot/",
    "domain": "大厂 AI 动态",
    "title": "Ring cameras go mobile as Amazon debuts AI-powered security drone and robot",
    "url": "https://arstechnica.com/ai/2026/11/ring-cameras-go-mobile-as-amazon-debuts-ai-powered-security-drone-and-robot/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T22:35:01+00:00",
    "summary": "Amazon's roaming Ring Robotics devices will debut in late 2026 and early 2027."
  },
  {
    "id": "hn:50306008",
    "domain": "股票",
    "title": "US tech stocks see sharp falls over AI cost fears",
    "url": "https://www.bbc.co.uk/news/articles/cvwy72e0n72yo",
    "source": "mindracer",
    "platform": "hackernews",
    "points": 270,
    "published_at": "2026-10-30T16:13:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:50381623",
    "domain": "股票",
    "title": "Nasdaq plummets 4% into correction territory",
    "url": "https://www.cnbc.com/2026/11/04/stock-market-today-live-updates.html",
    "source": "kristianp",
    "platform": "hackernews",
    "points": 227,
    "published_at": "2026-11-05T17:11:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:50346153",
    "domain": "股票",
    "title": "Intel stock collapse worsens as $3.5T chip rout spreads",
    "url": "https://finance.yahoo.com/markets/article/the-intel-stock-collapse-is-getting-worse--and-the-37-trillion-chip-rout-is-spreading-212154947.html",
    "source": "entryleveljobsc",
    "platform": "hackernews",
    "points": 236,
    "published_at": "2026-11-03T00:08:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:50342284",
    "domain": "股票",
    "title": "Oracle files to sell $20B in new stock, bonds to finance AI buildout",
    "url": "https://www.cnbc.com/2026/11/02/oracle-files-to-sell-20-billion-in-new-stock-bonds-to-finance-ai-buildout.html",
    "source": "smartmic",
    "platform": "hackernews",
    "points": 200,
    "published_at": "2026-11-02T19:27:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:50384822",
    "domain": "股票",
    "title": "$2.5T has been wiped from US stocks",
    "url": "https://finlaws.substack.com/p/25t-has-been-wiped-from-us-stocks",
    "source": "madihaa",
    "platform": "hackernews",
    "points": 164,
    "published_at": "2026-11-05T21:39:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:50382179",
    "domain": "股票",
    "title": "Nasdaq Sinks 5% as Investors Retreat from AI Trade After Election",
    "url": "https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-11-05-2026",
    "source": "armcat",
    "platform": "hackernews",
    "points": 163,
    "published_at": "2026-11-05T18:00:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:50151376",
    "domain": "股票",
    "title": "The obscure trust looming over Anthropic's IPO",
    "url": "https://www.wsj.com/tech/ai/anthropic-ipo-private-trust-188f41f7?st=RtdGHg&reflink=desktopwebshare_permalink",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 154,
    "published_at": "2026-10-19T12:06:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:50401029",
    "domain": "股票",
    "title": "The AI sell-off compared to well-known stock market crashes",
    "url": "https://www.kadoa.com/companies/insights/ai-selloff-perspective",
    "source": "hubraumhugo",
    "platform": "hackernews",
    "points": 101,
    "published_at": "2026-11-07T02:20:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:50445463",
    "domain": "股票",
    "title": "Anthropic Targets $1.4T Valuation in IPO",
    "url": "https://www.bloomberg.com/news/videos/2026-11-10/anthropic-targets-1-4-trillion-valuation-in-ipo-video",
    "source": "rndsignals",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-11-10T19:56:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:50280197",
    "domain": "股票",
    "title": "Alphabet Announces Third Quarter 2026 Results [pdf]",
    "url": "https://s206.q4cdn.com/479360582/files/doc_financials/2026/q3/2026q3-alphabet-earnings-release.pdf",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 82,
    "published_at": "2026-10-28T20:11:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:50362274",
    "domain": "股票",
    "title": "AI stocks slide as Texas governor result raises data center risks",
    "url": "https://www.cnbc.com/2026/11/04/ai-stocks-texas-governor-data-centers.html",
    "source": "1659447091",
    "platform": "hackernews",
    "points": 56,
    "published_at": "2026-11-04T07:00:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:50386909",
    "domain": "股票",
    "title": "Investors wipe $2.5T off Nasdaq as blue tsunami prompts AI fears",
    "url": "https://www.reuters.com/legal/transactional/ai-data-center-stocks-slip-democratic-sweep-clouds-expansion-plans-2026-11-05/",
    "source": "lilerjee",
    "platform": "hackernews",
    "points": 46,
    "published_at": "2026-11-06T01:11:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:50352405",
    "domain": "股票",
    "title": "US Hedge Funds Just Sold Every AI Stock They Bought Since 2025",
    "url": "https://finance.yahoo.com/markets/stocks/articles/us-hedge-funds-just-sold-113114644.html",
    "source": "robin_reala",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-11-03T14:27:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:50389401",
    "domain": "股票",
    "title": "Global stocks tumble as AI panic grips markets after Democrats' midterm success",
    "url": "https://www.theguardian.com/business/live/2026/nov/06/global-stocks-tumble-ai-panic-markets-democrats-midterms-success-jobs-oil-dollar-latest-news-updates",
    "source": "drayfield",
    "platform": "hackernews",
    "points": 36,
    "published_at": "2026-11-06T07:52:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:50351712",
    "domain": "股票",
    "title": "Anthropic's IPO Filing Warns It May Be 'Imminently' Close to RSI",
    "url": "https://epyhia.com/anthropic-s-ipo-filing-warns-it-may-be-imminently-close-to-recursive",
    "source": "arbuge",
    "platform": "hackernews",
    "points": 34,
    "published_at": "2026-11-03T13:26:43+00:00",
    "summary": ""
  },
  {
    "id": "hn:50384382",
    "domain": "股票",
    "title": "Chip stocks get slaughtered as Wall Street in worst post-midterm day since 1896",
    "url": "https://finance.yahoo.com/markets/article/chip-stocks-get-slaughtered-as-wall-street-heads-for-its-worst-post-midterm-day-since-1896-163413900.html",
    "source": "novaRom",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-11-05T20:58:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:50385642",
    "domain": "股票",
    "title": "Michael Burry says Anthropic is 'betting its existence' on optimism",
    "url": "https://www.businessinsider.com/michael-burry-anthropic-ipo-outlook-ant-big-short-2026-11",
    "source": "mgh2",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-11-05T22:49:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:50386483",
    "domain": "股票",
    "title": "Major Investors Are Skeptical Anthropic IPO Can Achieve $1.5T Valuation",
    "url": "https://www.wsj.com/finance/major-investors-are-skeptical-anthropic-ipo-can-achieve-1-5-trillion-valuation-ca965d8b",
    "source": "sandinmyjoints",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-11-06T00:17:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:50295611",
    "domain": "股票",
    "title": "Reddit will force everyone to log in",
    "url": "https://www.theverge.com/tech/1022571/reddit-login-requirement-q3-2026-earnings",
    "source": "timpera",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-10-29T20:43:17+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.netinterest.co/p/the-insatiable-demand-for-alpha",
    "domain": "股票",
    "title": "The Insatiable Demand for Alpha",
    "url": "https://www.netinterest.co/p/the-insatiable-demand-for-alpha",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T17:59:24+00:00",
    "summary": "Why a market shakedown could leave the biggest pod shops stronger"
  },
  {
    "id": "hn:50326281",
    "domain": "股票",
    "title": "Ant: Can unprecedented revenue growth outrun irresponsibly large investment",
    "url": "https://leonlins.com/writing/anthropic_ipo",
    "source": "avoidboringppl",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-11-01T14:56:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:50323575",
    "domain": "股票",
    "title": "We're Living in the Age of the Imperial CEO",
    "url": "https://www.wsj.com/tech/ai/anthropic-ipo-dual-class-stock-founder-control-4c43a56d",
    "source": "pretext",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-11-01T08:09:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:50167295",
    "domain": "股票",
    "title": "Data center stocks slide as Korea IPO plunges 30%, pressuring tech sentiment",
    "url": "https://www.cnbc.com/2026/10/20/data-center-stocks-slide-as-korea-ipo-plunges-30percent-pressuring-tech-sentiment.html",
    "source": "PLenz",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-10-20T14:50:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:50142772",
    "domain": "股票",
    "title": "How the Fed Is Quietly Inflating the AI Bubble While Hiking Your Electric Bill",
    "url": "https://www.thebignewsletter.com/p/how-the-federal-reserve-secretly",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 30,
    "published_at": "2026-10-18T16:48:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:50071744",
    "domain": "股票",
    "title": "Sprout Pi Mainboard – A modern, RP2350-powered motherboard for iPods",
    "url": "https://www.crowdsupply.com/certain-things/sprout-pi-mainboard",
    "source": "esskay",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-10-13T13:49:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:50171533",
    "domain": "股票",
    "title": "Anthropic S-1 Shows Red-Hot Growth, Risks and Computing Costs",
    "url": "https://www.wsj.com/tech/ai/anthropic-revenue-growth-ipo-accaf0f1",
    "source": "mmmmmbop",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-10-20T19:34:39+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.netinterest.co/p/follow-the-money-ece",
    "domain": "股票",
    "title": "Follow the Money",
    "url": "https://www.netinterest.co/p/follow-the-money-ece",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T17:48:55+00:00",
    "summary": "What six years and 300+ posts of Net Interest say about where finance is heading"
  },
  {
    "id": "hn:50251762",
    "domain": "股票",
    "title": "Anthropic Is the Most Ridiculous IPO of 2026 [pdf]",
    "url": "https://www.newconstructs.com/wp-content/uploads/2026/10/Anthropic-Is-The-Most-Ridiculous-IPO-of-2026.pdf",
    "source": "simonebrunozzi",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-10-26T22:06:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:50243343",
    "domain": "股票",
    "title": "Anthropic rushing IPO before AI bubble bursts",
    "url": "https://nypost.com/2026/10/23/business/wall-street-is-urging-anthropic-openai-to-do-their-ipos-in-a-hurry-heres-why/",
    "source": "nothrowaways",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-10-26T13:30:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:50082283",
    "domain": "股票",
    "title": "US Says Chinese Hackers Attacked DOJ, NASA, Federal Reserve, Senate",
    "url": "https://www.usatoday.com/story/news/politics/2026/08/26/chinese-hackers-cyberattack-us-government/91473585007/",
    "source": "gmays",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-10-14T04:09:23+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.netinterest.co/p/capital-wars",
    "domain": "股票",
    "title": "Capital Wars",
    "url": "https://www.netinterest.co/p/capital-wars",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T16:24:17+00:00",
    "summary": "CoreWeave and the Economics of a Data Center Build"
  },
  {
    "id": "rss:https://www.netinterest.co/p/me-and-my-agents",
    "domain": "股票",
    "title": "Me and My Agents",
    "url": "https://www.netinterest.co/p/me-and-my-agents",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T16:39:55+00:00",
    "summary": "Unleashing AI Agents on Bank Earnings"
  },
  {
    "id": "rss:https://www.netinterest.co/p/when-saturday-comes",
    "domain": "股票",
    "title": "When Saturday Comes",
    "url": "https://www.netinterest.co/p/when-saturday-comes",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-10T12:42:20+00:00",
    "summary": "Football as an Asset Class"
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
    "id": "hn:50391456",
    "domain": "金融",
    "title": "Tesla to wind down Cybertruck production",
    "url": "https://www.nbcnews.com/tech/tech-news/tesla-wind-cybertruck-production-years-poor-sales-markets-rcna607817",
    "source": "PLenz",
    "platform": "hackernews",
    "points": 1163,
    "published_at": "2026-11-06T12:13:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:50154244",
    "domain": "金融",
    "title": "DeepSeek banned from U.S. federal civilian agencies under new DHS order",
    "url": "https://www.reuters.com/technology/us-banning-chinese-ai-deepseek-government-agency-it-systems-2026-10-19/",
    "source": "cmrdporcupine",
    "platform": "hackernews",
    "points": 584,
    "published_at": "2026-10-19T16:16:46+00:00",
    "summary": ""
  },
  {
    "id": "hn:50385870",
    "domain": "金融",
    "title": "Cuban: Facebook knowingly runs AI deepfake scam ads; docs say $16B fraud revenue",
    "url": "https://finance.yahoo.com/technology/ai/articles/mark-cuban-says-facebook-knowingly-213000020.html",
    "source": "randycupertino",
    "platform": "hackernews",
    "points": 523,
    "published_at": "2026-11-05T23:09:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:50305573",
    "domain": "金融",
    "title": "The federated code forge",
    "url": "https://tangled.org/blog/forge/",
    "source": "zlliang",
    "platform": "hackernews",
    "points": 333,
    "published_at": "2026-10-30T15:44:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:50414427",
    "domain": "金融",
    "title": "Tesla Hasn't Had a Successful New Product Launch Since JB Straubel Stepped Down",
    "url": "https://cleantechnica.com/2026/11/07/tesla-hasnt-had-a-successful-new-product-launch-since-jb-straubel-stepped-down-as-cto/",
    "source": "gumby",
    "platform": "hackernews",
    "points": 207,
    "published_at": "2026-11-08T16:07:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:50173487",
    "domain": "金融",
    "title": "Feds suspect ransom negotiator ran ShinyHunters extortion site",
    "url": "https://krebsonsecurity.com/2026/10/feds-suspect-ransom-negotiator-ran-shinyhunters-extortion-site/",
    "source": "Bender",
    "platform": "hackernews",
    "points": 270,
    "published_at": "2026-10-20T22:21:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:50131440",
    "domain": "金融",
    "title": "US federal budget deficit jumps 12% in one year to nearly $2 Trillion",
    "url": "https://finance.yahoo.com/economy/policy/article/the-us-federal-budget-deficit-for-2026-just-came-in-its-1992-trillion-191917669.html",
    "source": "ck2",
    "platform": "hackernews",
    "points": 208,
    "published_at": "2026-10-17T14:22:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:50260526",
    "domain": "金融",
    "title": "A $300B 'Debt Wall' Is Looming over Private-Equity Backed Companies",
    "url": "https://www.wsj.com/finance/investing/a-300-billion-debt-wall-is-looming-over-private-equity-backed-companies-d6359497",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 178,
    "published_at": "2026-10-27T15:09:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:50059446",
    "domain": "金融",
    "title": "Feds got warrants to use fake cell towers to hunt down Don Lemon's producer",
    "url": "https://www.wired.com/story/feds-got-warrants-to-use-fake-cell-towers-to-hunt-down-don-lemons-producer/",
    "source": "rndsignals",
    "platform": "hackernews",
    "points": 196,
    "published_at": "2026-10-12T17:08:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:50190168",
    "domain": "金融",
    "title": "Epic Games Inc v Apple Inc",
    "url": "https://www.judgments.fedcourt.gov.au/judgments/Judgments/fca/single/2026/2026fca1552",
    "source": "Mayzie",
    "platform": "hackernews",
    "points": 193,
    "published_at": "2026-10-22T01:52:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:50236073",
    "domain": "金融",
    "title": "Nvidia and Micron Make Up 34% of America's Earnings Boom",
    "url": "https://www.wsj.com/finance/stocks/the-earnings-boom-is-heavily-reliant-on-just-a-handful-of-stocks-21decb53",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 176,
    "published_at": "2026-10-25T21:07:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:50057956",
    "domain": "金融",
    "title": "French supermarkets suffer fridge shutdown after 'unprecedented' cyberattack",
    "url": "https://uk.finance.yahoo.com/news/french-supermarket-chains-cyberattack-forced-115141288.html",
    "source": "thinkcontext",
    "platform": "hackernews",
    "points": 155,
    "published_at": "2026-10-12T15:36:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:50387406",
    "domain": "金融",
    "title": "Tesla and SpaceX lose over $420B in combined market cap in the two days",
    "url": "https://techlaws.pages.dev/tesla-and-spacex-lose-over-420b-in-combined-market-cap-in-the-two-days/",
    "source": "Pepitobombito",
    "platform": "hackernews",
    "points": 84,
    "published_at": "2026-11-06T02:30:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:50080275",
    "domain": "金融",
    "title": "Show HN: Pulse Local, a Mac budgeting app whose AI models run on your machine",
    "url": "https://pulseos.finance",
    "source": "niztk",
    "platform": "hackernews",
    "points": 122,
    "published_at": "2026-10-13T23:13:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:50082021",
    "domain": "金融",
    "title": "Strafe: A new open-source, E2E Encrypted, and federated alternative to Discord",
    "url": "https://strafe.chat/",
    "source": "brydencalaway",
    "platform": "hackernews",
    "points": 118,
    "published_at": "2026-10-14T03:28:00+00:00",
    "summary": ""
  },
  {
    "id": "hn:50274706",
    "domain": "金融",
    "title": "Tesla Semi catches fire on I-880",
    "url": "https://electrek.co/2026/10/28/tesla-semi-fire-i-880-hayward-no-crash/",
    "source": "metadat",
    "platform": "hackernews",
    "points": 96,
    "published_at": "2026-10-28T14:54:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:50278678",
    "domain": "金融",
    "title": "Show HN: A proof-of-concept formalization of the IRS federal tax forms",
    "url": "https://github.com/emmilco/us-tax-model",
    "source": "RGS1811",
    "platform": "hackernews",
    "points": 84,
    "published_at": "2026-10-28T18:30:53+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.12899",
    "domain": "金融",
    "title": "AFNO: Universal Certifiably-Arbitrage-Free Operator Learning Framework for European Call-Price Surfaces",
    "url": "https://arxiv.org/abs/2611.12899",
    "source": "Anastasis Kratsios, Yannick Limmer, Hans Buehler, Blanka Horvath, Raeid Saqur",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T05:00:00+00:00",
    "summary": "arXiv:2611.12899v1 Announce Type: new Abstract: Neural operators (NOs) have been introduced as deep learning-powered solutions to the computational bottleneck of solving families of problems. Once tra"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.12987",
    "domain": "金融",
    "title": "Global Trends and Heterogeneity in Modified Adjusted Net Savings",
    "url": "https://arxiv.org/abs/2611.12987",
    "source": "Xin Xiao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T05:00:00+00:00",
    "summary": "arXiv:2611.12987v1 Announce Type: new Abstract: Modified adjusted net savings is a derived weak sustainability indicator obtained by subtracting education expenditure from adjusted net savings (ANS). "
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.13194",
    "domain": "金融",
    "title": "Taste or Strategy? Nationalistic Bias and Competitor Penalties in Figure Skating Judging",
    "url": "https://arxiv.org/abs/2611.13194",
    "source": "Jialin Liu, Shu Shen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T05:00:00+00:00",
    "summary": "arXiv:2611.13194v1 Announce Type: new Abstract: Many decisions rest on expert panels whose members have ties to some candidates, and favoritism is hard to tell from shared taste or better information."
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.13230",
    "domain": "金融",
    "title": "Dynamic investment and coordination in teams: Theory and experimental evidence",
    "url": "https://arxiv.org/abs/2611.13230",
    "source": "David Gill, Victoria Prowse, J. Lucas Reddinger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T05:00:00+00:00",
    "summary": "arXiv:2611.13230v1 Announce Type: new Abstract: Teamwork requires more than the general skills that team members bring. In successful teams, members invest in team-specific skill or capital that accum"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.13365",
    "domain": "金融",
    "title": "Making sense of rule 605",
    "url": "https://arxiv.org/abs/2611.13365",
    "source": "Peter B. Lerner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T05:00:00+00:00",
    "summary": "arXiv:2611.13365v1 Announce Type: new Abstract: The paper analyzes monthly reports of two companies: one market maker, Virtu, and one broker-dealer, SoHo, in the period between January 2021 and March "
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.13616",
    "domain": "金融",
    "title": "Optimal Trading Speed on Blockchain",
    "url": "https://arxiv.org/abs/2611.13616",
    "source": "Ruizhe Jia, Shihao Yu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T05:00:00+00:00",
    "summary": "arXiv:2611.13616v1 Announce Type: new Abstract: On blockchain-based exchanges, faster blocks weaken the priority-fee competition among arbitrageurs and shift rents from the block producer to them. Equ"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.13715",
    "domain": "金融",
    "title": "Optimal Regulation and Information Institutions with Hidden Network Equilibria",
    "url": "https://arxiv.org/abs/2611.13715",
    "source": "Christian Jaag",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T05:00:00+00:00",
    "summary": "arXiv:2611.13715v1 Announce Type: new Abstract: Aggregate outcomes can conceal network configurations that expose households to uninsurable risk and require different public services. We study a regul"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.13866",
    "domain": "金融",
    "title": "Economic Benefits of Cross-Border Electricity Trade and Domestic Electricity Production in Switzerland",
    "url": "https://arxiv.org/abs/2611.13866",
    "source": "Benjamin Lietti, Ambra Van Liedekerke, Marino Bucher, Michael Beer, Nicolas Eschenbaum, Reto Foellmi, Blazhe Gjorgiev, Fabian Gottschlich, Giovanni Sansavini, Christian Sch\\\"utz, Urs Trinkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T05:00:00+00:00",
    "summary": "arXiv:2611.13866v1 Announce Type: new Abstract: This paper assesses the economic benefits of cross-border electricity trade in the context of rising energy prices and geopolitical uncertainty. Switzer"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.14117",
    "domain": "金融",
    "title": "Fine-Tuning an Order-Flow Foundation Model for Sub-Second Forecasting",
    "url": "https://arxiv.org/abs/2611.14117",
    "source": "Fedor Shabashev",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T05:00:00+00:00",
    "summary": "arXiv:2611.14117v1 Announce Type: new Abstract: Generative models have become the standard approach in language and vision. These models are typically pretrained first and then fine-tuned. Recent work"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.14146",
    "domain": "金融",
    "title": "Estimating multidimensional poverty under incomplete data in North Macedonia",
    "url": "https://arxiv.org/abs/2611.14146",
    "source": "Maja Gerovska Mitev, Viktor Stojkoski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T05:00:00+00:00",
    "summary": "arXiv:2611.14146v1 Announce Type: new Abstract: Multidimensional Poverty Indices (MPIs) are available for more than 100 countries, but rarely below the national or regional level. Local estimates requ"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.14245",
    "domain": "金融",
    "title": "Deep Learning for Operator Maps in Optimal Liquidation",
    "url": "https://arxiv.org/abs/2611.14245",
    "source": "Ryan Donnelly, Luca Galimberti, Brian Healy, Siqi Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T05:00:00+00:00",
    "summary": "arXiv:2611.14245v1 Announce Type: new Abstract: We analyze the solution map of a optimal execution problem in which price dynamics are subject to a general transient impact kernel. Given the structure"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.13259",
    "domain": "金融",
    "title": "Choosing Complexity: Cognitive Ability, Overconfidence, and Task Choice",
    "url": "https://arxiv.org/abs/2611.13259",
    "source": "David Gill, Zhongheng Qiao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T05:00:00+00:00",
    "summary": "arXiv:2611.13259v1 Announce Type: cross Abstract: Workers and organizations routinely choose between complex tasks that differ in their success-payment tradeoff. We study how cognitive ability and ove"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.13550",
    "domain": "金融",
    "title": "Tabular Foundation Models in Financial Predictions",
    "url": "https://arxiv.org/abs/2611.13550",
    "source": "Ed deHaan, Allen H. Huang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T05:00:00+00:00",
    "summary": "arXiv:2611.13550v1 Announce Type: cross Abstract: This technical note introduces tabular foundation models (TFMs) to accounting research and evaluates their performance in one common benchmark task: p"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.13841",
    "domain": "金融",
    "title": "Nonzero-Sum Stochastic Exit Games with Singular Belief Dynamics",
    "url": "https://arxiv.org/abs/2611.13841",
    "source": "Yukun Cao, Jan Palczewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T05:00:00+00:00",
    "summary": "arXiv:2611.13841v1 Announce Type: cross Abstract: We study a two-player nonzero-sum stochastic exit game with asymmetric information. Each firm chooses the time to exit a duopoly and, conditional on r"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.13962",
    "domain": "金融",
    "title": "Deceleration without identification: testing a power-law trend in Bitcoin prices under persistent noise",
    "url": "https://arxiv.org/abs/2611.13962",
    "source": "Carlos Baquero, Raquel Menezes",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T05:00:00+00:00",
    "summary": "arXiv:2611.13962v1 Announce Type: cross Abstract: Plotted against time since its first block on logarithmic axes, the price of Bitcoin lies close to a straight line, and a power law in time has been p"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.14325",
    "domain": "金融",
    "title": "Point-in-Time Encoders for Earnings Calls",
    "url": "https://arxiv.org/abs/2611.14325",
    "source": "Alessio Brini",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T05:00:00+00:00",
    "summary": "arXiv:2611.14325v1 Announce Type: cross Abstract: Text encoders turn earnings calls into vectors for search, for language models that answer from retrieved passages, and for forecasting models. A live"
  },
  {
    "id": "rss:https://arxiv.org/abs/2507.08244",
    "domain": "金融",
    "title": "Advancing AI Capabilities and Evolving Labor Outcomes",
    "url": "https://arxiv.org/abs/2507.08244",
    "source": "Jacob Dominski, Tyler Boes, Yong Suk Lee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T05:00:00+00:00",
    "summary": "arXiv:2507.08244v3 Announce Type: replace Abstract: This paper examines how labor market outcomes have evolved across occupations as AI capabilities advanced from generative AI chatbots to reasoning m"
  },
  {
    "id": "rss:https://arxiv.org/abs/2512.07154",
    "domain": "金融",
    "title": "Asian option valuation under price impact",
    "url": "https://arxiv.org/abs/2512.07154",
    "source": "Priyanshu Tiwari, Sourav Majumdar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T05:00:00+00:00",
    "summary": "arXiv:2512.07154v3 Announce Type: replace Abstract: We develop a model for arithmetic and geometric Asian option valuation with external order flow and dealer execution costs. We first formulate it as"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.29290",
    "domain": "金融",
    "title": "Supply Chain Propagation of Textual Signals: LLM Embeddings and Cross-Sectional Return Predictability",
    "url": "https://arxiv.org/abs/2606.29290",
    "source": "Asef Y{\\i}lk{\\i}",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T05:00:00+00:00",
    "summary": "arXiv:2606.29290v2 Announce Type: replace Abstract: This paper proposes a novel asset pricing framework that augments large language model (LLM) embeddings of annual report disclosures with supply cha"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.10053",
    "domain": "金融",
    "title": "Do wind and solar curtail at negative electricity prices? Incentives and evidence across two decades of German renewable support schemes",
    "url": "https://arxiv.org/abs/2609.10053",
    "source": "Lion Hirth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T05:00:00+00:00",
    "summary": "arXiv:2609.10053v2 Announce Type: replace Abstract: In many power systems, installed wind and solar now exceed peak electricity demand. In very sunny or windy periods, curtailing renewable generation "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.35111",
    "domain": "金融",
    "title": "The overlooked price feedback: Why simulations overstate distribution grid peaks from home batteries under real time pricing",
    "url": "https://arxiv.org/abs/2609.35111",
    "source": "Lion Hirth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T05:00:00+00:00",
    "summary": "arXiv:2609.35111v4 Announce Type: replace Abstract: Simulation studies of home batteries under real-time electricity pricing commonly find that synchronized charging creates new load peaks in distribu"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.10731",
    "domain": "金融",
    "title": "Have wind and solar energy increased electricity price volatility? And what is electricity price volatility, anyway?",
    "url": "https://arxiv.org/abs/2611.10731",
    "source": "Lion Hirth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T05:00:00+00:00",
    "summary": "arXiv:2611.10731v2 Announce Type: replace Abstract: It is widely held that wind and solar power increase the volatility of electricity prices. This paper argues that the literature conflates two disti"
  },
  {
    "id": "rss:https://arxiv.org/abs/2403.01361",
    "domain": "金融",
    "title": "Bandit Profit-maximization for Targeted Marketing",
    "url": "https://arxiv.org/abs/2403.01361",
    "source": "Joon Suk Huh, Ellen Vitercik, Kirthevasan Kandasamy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T05:00:00+00:00",
    "summary": "arXiv:2403.01361v3 Announce Type: replace-cross Abstract: We study a sequential profit-maximization problem, optimizing for both price and ancillary variables like marketing expenditures. Specifically"
  },
  {
    "id": "rss:https://arxiv.org/abs/2511.06165",
    "domain": "金融",
    "title": "Spatial Selection and the Multiscale Dynamics of Urban Change",
    "url": "https://arxiv.org/abs/2511.06165",
    "source": "Jordan T Kemp, Laura F\\\"ursich, Elias Tannira, Lu\\'is M A Bettencourt",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T05:00:00+00:00",
    "summary": "arXiv:2511.06165v2 Announce Type: replace-cross Abstract: Growth is a multi-layered phenomenon in human societies, composed of socioeconomic and demographic change at many different scales. Yet, stand"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.24490",
    "domain": "金融",
    "title": "Market Regime Council for Dynamic Credit Assignment in Multi-Agent LLM Decision Systems",
    "url": "https://arxiv.org/abs/2605.24490",
    "source": "Yunhua Pei, Zerui Ge, Jin Zheng, John Cartlidge",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T05:00:00+00:00",
    "summary": "arXiv:2605.24490v2 Announce Type: replace-cross Abstract: Multi-agent LLM decision systems for portfolio management still lack a principled way to assign credit across specialist agents, remain vulner"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.26074",
    "domain": "金融",
    "title": "StakeBench: Evaluating Language Understanding Grounded in Market Commitment",
    "url": "https://arxiv.org/abs/2605.26074",
    "source": "Yunhua Pei, Jingyu Hu, Yiwei Shi, Hongnan Ma, Weiru Liu, John Cartlidge",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T05:00:00+00:00",
    "summary": "arXiv:2605.26074v2 Announce Type: replace-cross Abstract: Existing financial NLP benchmarks often rely on labels supplied by outside observers, measuring how language is perceived rather than what spe"
  },
  {
    "id": "hn:50291902",
    "domain": "金融",
    "title": "Alphabet heads for a $500B drop in market value, biggest in its history",
    "url": "https://finance.yahoo.com/markets/article/alphabet-heads-for-a-500-billion-drop-in-market-value-the-biggest-in-its-history-134824763.html",
    "source": "rawgabbit",
    "platform": "hackernews",
    "points": 62,
    "published_at": "2026-10-29T16:39:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:50372038",
    "domain": "金融",
    "title": "Harmony: Chat like Discord. Federated like email",
    "url": "https://mony.lol/",
    "source": "FinalDestiny",
    "platform": "hackernews",
    "points": 37,
    "published_at": "2026-11-04T21:49:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:50105900",
    "domain": "金融",
    "title": "Market selloff, rising rates test AI data centre deal boom",
    "url": "https://www.reuters.com/business/finance/market-selloff-rising-rates-test-ai-data-centre-deal-boom-2026-10-15/",
    "source": "tartoran",
    "platform": "hackernews",
    "points": 75,
    "published_at": "2026-10-15T16:17:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:50394771",
    "domain": "金融",
    "title": "Only 16% of U.S. fast-charging stations meet federal NEVI standards (open data)",
    "url": "https://chargingnear.me/data",
    "source": "parkgraph",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-11-06T16:45:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:50161207",
    "domain": "金融",
    "title": "U.S. Supreme Court to review 1868 federal ban on home distilling of liquor",
    "url": "https://www.staradvertiser.com/2026/10/19/breaking-news/u-s-supreme-court-to-review-1868-federal-ban-on-home-distilling-of-liquor/",
    "source": "Jimmc414",
    "platform": "hackernews",
    "points": 68,
    "published_at": "2026-10-20T04:02:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:50253630",
    "domain": "金融",
    "title": "The 'Buy, Borrow and Die' Wealth Strategy Has Become a $5T Market",
    "url": "https://www.wsj.com/finance/the-buy-borrow-and-die-wealth-strategy-has-become-a-5-trillion-market-d9149a9d",
    "source": "tysone",
    "platform": "hackernews",
    "points": 66,
    "published_at": "2026-10-27T01:30:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:50156189",
    "domain": "金融",
    "title": "The US orders every civilian agency to rip out DeepSeek, even tools built on it",
    "url": "https://madrobot.blog/2026/10/19/us-bans-deepseek-federal-agencies-dhs-order-remove-third-party/",
    "source": "jacquesm",
    "platform": "hackernews",
    "points": 66,
    "published_at": "2026-10-19T18:41:10+00:00",
    "summary": ""
  }
]
```
