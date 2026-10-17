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

- 今日日期：`2026-10-17`
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
  "date": "2026-10-17",
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
    "title": "8分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 1983465,
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
    "points": 1405473,
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
    "points": 1353291,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 1208887,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1yorUYWEGD",
    "domain": "AI",
    "title": "普通人也可以看的 AI 编程指南 | Cursor 教程｜Cursor 使用技巧和思路｜如何免费使用 Cursor｜AI 编程",
    "url": "http://www.bilibili.com/video/av113786467981446",
    "source": "不正经的前端啊",
    "platform": "bilibili",
    "points": 946603,
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
    "points": 900529,
    "published_at": "2025-05-01T09:00:00+00:00",
    "summary": "up的科学星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 857655,
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
    "points": 718617,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1VZWc6dECG",
    "domain": "AI",
    "title": "【Re:从零开始的AI学习】第一季总集篇｜从入门到用好 AI",
    "url": "http://www.bilibili.com/video/av117430848391663",
    "source": "卡普迪姆",
    "platform": "bilibili",
    "points": 663713,
    "published_at": "2026-10-13T00:57:21+00:00",
    "summary": "这次，我把【Re：从零开始的 AI 学习】第一季全 13 期完整连在一起啦！\n新来的朋友或者想要查漏补缺的伙伴，现在可以一口气通关！从 AI 入门与提示词技巧，到 Agent 玩法、主流模型对比与使用成本……跟着走一遍就能彻底搞懂。\n希望这个系列能给你带来哪怕一点点启发，欢迎点赞、投币、收藏一键三连支持！也超级欢迎转发安利给身边的朋友～\n\n【目录】\n00:00 导语\n00:32 AI 这三年发生了"
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 542113,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1AnQNYxEsy",
    "domain": "AI",
    "title": "MCP是啥？技术原理是什么？一个视频搞懂MCP的一切。Windows系统配置MCP，Cursor Cline使用MCP",
    "url": "http://www.bilibili.com/video/av114155298228756",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 425041,
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
    "points": 356041,
    "published_at": "2026-04-29T08:23:29+00:00",
    "summary": "配置方法如下：\n(想用真心换取你的关注...蟹蟹泥...)\nsetting.json添加：\n{ &quot;name&quot;: &quot;ANTHROPIC_BASE_URL&quot;, &quot;value&quot;: &quot;https://xxxx&quot; }, \n{ &quot;name&quot;: &quot;ANTHROPIC_AUTH_TOKEN&quot;, "
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 322973,
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
    "points": 308154,
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
    "points": 279527,
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
    "points": 207672,
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
    "points": 183844,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1RNTtzMENj",
    "domain": "AI",
    "title": "从零编写MCP并发布上线，超简单！手把手教程",
    "url": "http://www.bilibili.com/video/av114630814862349",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 159789,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 136701,
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
    "points": 94062,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1VL3F6pE9K",
    "domain": "AI",
    "title": "0基础入门智能体agent测试：AI测试基础+AI智能体(Agent)测试从零入门全攻略，2026最新版！",
    "url": "http://www.bilibili.com/video/av116991151113881",
    "source": "黑马测试",
    "platform": "bilibili",
    "points": 79975,
    "published_at": "2026-07-27T09:19:37+00:00",
    "summary": "还在卷传统软件测试？2026年必学的AI智能体(Agent)测试来了！本期视频专为0基础小白打造，从软件测试基础讲起...若要本视频配套资源笔记可加up主企微（请看置顶留言最后一句话）。"
  },
  {
    "id": "bvid:BV15Vhy6cEhd",
    "domain": "AI",
    "title": "通俗易懂地讲解什么是Agent？",
    "url": "http://www.bilibili.com/video/av117330906449673",
    "source": "洪涛同学LovTech",
    "platform": "bilibili",
    "points": 77169,
    "published_at": "2026-09-25T09:12:59+00:00",
    "summary": "从0到1搭建一个简易Agent，从小白的角度出发解释Agent是如何运行的？"
  },
  {
    "id": "bvid:BV1XnuGzfEp7",
    "domain": "AI",
    "title": "让你手中的AI好用10倍！5个好玩实用的MCP推荐，让你不只会用AI搜索",
    "url": "http://www.bilibili.com/video/av114835262018810",
    "source": "田同学Tino",
    "platform": "bilibili",
    "points": 76424,
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
    "points": 66431,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 56081,
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
    "points": 49316,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 34529,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 30971,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV13tuqzwEm9",
    "domain": "AI",
    "title": "一个视频彻底掌握ClaudeCode使用MCP",
    "url": "http://www.bilibili.com/video/av114851586252599",
    "source": "创哥的AI实验室",
    "platform": "bilibili",
    "points": 29899,
    "published_at": "2025-07-14T12:32:55+00:00",
    "summary": "Claude Code命令行的方式，让MCP的操作也令很多朋友感觉不适，这个视频专门做了一些介绍。\n\n希望能帮助到大家。"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 24708,
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
    "points": 22813,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 21994,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV188UHYkEdg",
    "domain": "AI",
    "title": "Cursor / Windsurf + Android Studio 高效AI编程：零基础也能开发安卓应用",
    "url": "http://www.bilibili.com/video/av113502647750313",
    "source": "kate人不错",
    "platform": "bilibili",
    "points": 21168,
    "published_at": "2024-11-18T07:04:36+00:00",
    "summary": "欢迎关注我的知识星球：https://t.zsxq.com/FF0He\n\n我会分享最新AI资讯、源代码、回答你的提问。\n\n视频亮点：\n\n双工具对比：解析 Cursor 和 Windsurf 各自优势\n实战案例：从五子棋到卡路里计算AI应用的完整开发过程\n专业部署：Android Studio 配置与构建技巧\n\n时间戳：\n\n0:00 - 引言\n\n0:26 - 我开发的应用演示\n\n2:33 - Rea"
  },
  {
    "id": "bvid:BV1sQaL6vEkb",
    "domain": "AI",
    "title": "小白向，ai入门第一课：agent的部署和使用！",
    "url": "http://www.bilibili.com/video/av117349378166797",
    "source": "沈三殊",
    "platform": "bilibili",
    "points": 19535,
    "published_at": "2026-09-28T15:30:36+00:00",
    "summary": "详细的agent部署介绍：https://pan.quark.cn/s/3846914c6da7\n欢迎来到ai的世界！！\n有疑问欢迎私信。"
  },
  {
    "id": "bvid:BV126pk6sETS",
    "domain": "AI",
    "title": "连 json都不会，进了福布斯团队。面试的时候才知道vibe coding是什么，两天后他给我发了offer。",
    "url": "http://www.bilibili.com/video/av117436686795057",
    "source": "揽星Celeste",
    "platform": "bilibili",
    "points": 19149,
    "published_at": "2026-10-14T01:35:05+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV15phrzqEzK",
    "domain": "AI",
    "title": "【Claude Code Router】一键直连五大模型",
    "url": "http://www.bilibili.com/video/av115121162553281",
    "source": "她笑中藏泪花",
    "platform": "bilibili",
    "points": 17605,
    "published_at": "2025-08-31T03:09:22+00:00",
    "summary": "Claude Code Router 教程：手把手完成 CCR 配置与 PROXY_URL 代理，一次直连 Gemini、Kimi、DeepSeek、GLM、Qwen，区分 Anthropic 与 OpenAI 端点，并附 /model 切换与报错速查。点击查看。\n博文链接：https://rosetears.cn/archives/61/"
  },
  {
    "id": "bvid:BV18TZYY8EuJ",
    "domain": "AI",
    "title": "微软最新AI Agent入门课程 • 中英",
    "url": "http://www.bilibili.com/video/av114246130076146",
    "source": "Mindofuture",
    "platform": "bilibili",
    "points": 17600,
    "published_at": "2025-03-30T02:06:00+00:00",
    "summary": "在这门包含10节课的课程中，我们将带你从概念到代码，全面覆盖构建AI代理的基础知识。在这里找到完整的“AI代理入门”课程及代码示例\nhttps://github.com/microsoft/ai-agents-for-beginners\n\nP01 什么是AI代理\nP02 使用哪种AI代理框架\nP03 如何设计优秀的AI代理\nP04 什么是代理工具使用设计模式\nP05 什么是代理式RAG\nP06 如"
  },
  {
    "id": "bvid:BV1xJpC6ZED4",
    "domain": "AI",
    "title": "10月最新Claude防封号最安全的！注册+订阅充值教程！新手看完直接上手！",
    "url": "http://www.bilibili.com/video/av117438196746547",
    "source": "团子讲Ai",
    "platform": "bilibili",
    "points": 15464,
    "published_at": "2026-10-14T07:59:49+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1yyQEBdEkm",
    "domain": "AI",
    "title": "【2026B站最全】Claude Code+软件测试实操教程!看完我直接删了收藏夹所有测试教程,从账号注册到Plan驱动测试项目,小白3天上手！",
    "url": "http://www.bilibili.com/video/av116408092525631",
    "source": "软件测试大神",
    "platform": "bilibili",
    "points": 15356,
    "published_at": "2026-04-15T09:55:02+00:00",
    "summary": "配套资料👉：https://b23.tv/qvhxmaQ\n包括:AI测试网站，几十个AI场景测试完整流程，skil文档，测试八股文，项目源码，测试用例模板，工具安装包，学习计划表，学习路线，100g测试新人资料包等等，资料百分百免费，放心领取~"
  },
  {
    "id": "bvid:BV17Lap6VEUr",
    "domain": "AI",
    "title": "【全80集】Vibe Coding 零基础入门到实战教程，由浅入深（全程干货）",
    "url": "http://www.bilibili.com/video/av117353572468721",
    "source": "数据拾光屋",
    "platform": "bilibili",
    "points": 14110,
    "published_at": "2026-10-02T09:25:00+00:00",
    "summary": "本套教程专门为零基础学员而制，全程干货无废话，喜欢的小伙伴记得点赞三连喔~\n【视频配套籽料+1V1问题解答请看 ”置顶平论” 哦】"
  },
  {
    "id": "bvid:BV18j5DzyEmD",
    "domain": "AI",
    "title": "Cursor-AI编程完整版入门教程",
    "url": "http://www.bilibili.com/video/av114379827713362",
    "source": "SiKi老师",
    "platform": "bilibili",
    "points": 12939,
    "published_at": "2025-04-22T11:00:00+00:00",
    "summary": "更多编程教程请访问我们官网www.sikiedu.com\n\nHi，我是SiKi老师，这个课程里面老师会带着大家学习使用全球目前最火的AI编程工具-Cursor的使用。\n\n教学内容：\n1、Cursor的下载和安装\n2、Cursor的基本设置\n3、使用Cursor开发贪吃蛇游戏\n4、使用Cursor开发一个博客网站\n5、Trae（字节旗下AI编程工具）的使用初体验"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 12661,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
  },
  {
    "id": "bvid:BV15epZ61E7F",
    "domain": "AI",
    "title": "我为什么强烈推荐Cursor的Pro套餐，Grok Bot真的太好用了！",
    "url": "http://www.bilibili.com/video/av117428784862489",
    "source": "AI摸鱼的梁师傅",
    "platform": "bilibili",
    "points": 11046,
    "published_at": "2026-10-12T16:06:10+00:00",
    "summary": "这期讲清楚三件事：为什么选 Cursor（官网软件直连、支付宝付款）；Pro 的两个模型池子怎么分（Grok/Composer 一池，Claude/GPT 共享一池）；附赠的 Grok Bot 怎么用——它有自己的云端电脑，合上 Mac 也在替你干活：定时简报、盯 PR、管邮件日历，还能多 Bot 协作。\n00:00 封号焦虑，和订套餐的理由 00:35 为什么是 Cursor：直连 + 支付宝 "
  },
  {
    "id": "bvid:BV1bBHm6MEG5",
    "domain": "AI",
    "title": "这绝对是b站讲的最好的Claude Code全套实战教程，手把手带你搞定国内环境安装配置，全程干货无废话！AI大模型/MCP/Skill/智能体/Agent",
    "url": "http://www.bilibili.com/video/av117402847155229",
    "source": "大模型饼饼",
    "platform": "bilibili",
    "points": 8213,
    "published_at": "2026-10-08T02:13:21+00:00",
    "summary": "这绝对是B站讲得最好的Claude Code全套实战教程！手把手带你搞定国内环境安装配置、基础操作、高阶实战技巧，课程不堆砌冗余理论，聚焦真实开发场景，带你吃透Claude Code核心能力，打通MCP、Skill与Agent智能体联动开发。不管你是想提升日常编码效率，还是入门AI智能体开发，这套教程都非常适合你，全程干货无废话！"
  },
  {
    "id": "bvid:BV17NJS6QEfE",
    "domain": "AI",
    "title": "Vibe Coding 有哪些高效的做法习惯？",
    "url": "http://www.bilibili.com/video/av117447894045979",
    "source": "AAA话题批发",
    "platform": "bilibili",
    "points": 7968,
    "published_at": "2026-10-16T01:30:00+00:00",
    "summary": "随着 AI 编程 Agent 普及，Vibe Coding 已经成为很多开发者的日常工作方式。不少人把精力耗费在打磨各种花式提示词上，但实际项目中经常遇到 Token 消耗爆炸、Agent 找不准代码、结果不稳定、大量人工兜底的问题。这篇文章结合多项行业实验与大厂内部项目实践，跳出提示词技巧，分享 Vibe Coding 真正高效的工作习惯与项目配置思路。\n文章开篇借助真实工程实验案例，展示合理拆"
  },
  {
    "id": "bvid:BV1aSR4BKESW",
    "domain": "AI",
    "title": "安卓手机部署Claude Code",
    "url": "http://www.bilibili.com/video/av116526891993752",
    "source": "中国小骑士",
    "platform": "bilibili",
    "points": 8063,
    "published_at": "2026-05-06T09:24:14+00:00",
    "summary": "通过Termux安装Claude Code并且接入国内大模型"
  },
  {
    "id": "bvid:BV1snhi6WE5P",
    "domain": "AI",
    "title": "【Cursor使用教程】史上最强AI编程工具Cursor！Cursor入门到精通保姆级教程！安装搭建/高阶技巧使用/开发小游戏/应用场景案例实战",
    "url": "http://www.bilibili.com/video/av117308156614035",
    "source": "图灵课堂",
    "platform": "bilibili",
    "points": 7992,
    "published_at": "2026-09-21T08:55:13+00:00",
    "summary": "整理制作不易，大家记得点个关注，一键三连呀【点赞、收藏、转发】感谢支持~\n全套AI大模型笔记/学习大纲/面试真题自取：https://www.bilibili.com/read/cv39638062/?spm_id_from=333.1387.0.0&amp;jump_opus=1"
  },
  {
    "id": "bvid:BV1UP5Q6aEVT",
    "domain": "AI",
    "title": "国内网络手把手安装安装Claude Code + 自动剪辑视频Skill",
    "url": "http://www.bilibili.com/video/av116571787823926",
    "source": "跟着阿亮学AI",
    "platform": "bilibili",
    "points": 7939,
    "published_at": "2026-05-14T07:40:10+00:00",
    "summary": "国内网络手把手安装安装Claude Code！不用写代码，新手也能剪动画视频\n✅ Claude Code保姆及安装教程+配置Kimi模型\n✅ Remotion一句话出动画，一键剪辑skill开源，口播+字幕直接出成品\n全套教程文档已备好！小白也能实现动画剪视频自由"
  },
  {
    "id": "bvid:BV18KJX6mEiH",
    "domain": "AI",
    "title": "太炸裂了！Claude Code 3.0彻底杀疯了！",
    "url": "http://www.bilibili.com/video/av117450007911196",
    "source": "烟神殿殿主",
    "platform": "bilibili",
    "points": 7395,
    "published_at": "2026-10-16T10:04:56+00:00",
    "summary": "原视频链接：https://www.youtube.com/watch?v=8nh1dcH4uJU\n本视频为AI技术搬运翻译，使用AI智能移除原视频广告营销内容，旨在降低信息差，帮助大家了解海外最新AI动态。\n翻译：烟神殿API,模型gemini-3.8-flash\n配音：使用的时FishTTS官方接口配音"
  },
  {
    "id": "bvid:BV1aMAczmEmf",
    "domain": "AI",
    "title": "[MoonPack]在布吉岛里注入模组-mcp",
    "url": "http://www.bilibili.com/video/av116264966163402",
    "source": "DanciestZebra70",
    "platform": "bilibili",
    "points": 7338,
    "published_at": "2026-03-21T03:13:25+00:00",
    "summary": "交流群\n①1051043310\n②365233792"
  },
  {
    "id": "hn:50008187",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI annualised revenues $20B less than previously signalled",
    "url": "https://www.cnbc.com/2026/10/08/open-ai-revenue-nvidia-oracle-coreweave.html",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 432,
    "published_at": "2026-10-08T16:45:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:49844663",
    "domain": "AI 算力 / 半导体",
    "title": "ASML says it sold 'absolutely nothing' in Europe in 2026",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/asml-says-its-sells-absolutely-nothing-in-europe-calls-on-eu-to-help-create-demand",
    "source": "MC995",
    "platform": "hackernews",
    "points": 403,
    "published_at": "2026-09-25T13:49:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:50035886",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia in talks to acquire US 'open' model startup Reflection AI",
    "url": "https://www.ft.com/content/052610c5-22b4-4dd4-932e-b7f9f0628b6a",
    "source": "arkj",
    "platform": "hackernews",
    "points": 179,
    "published_at": "2026-10-10T18:48:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:50086363",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's first GPU: GeForce 256",
    "url": "https://dfarq.homeip.net/nvidias-first-gpu-geforce-256/",
    "source": "ibobev",
    "platform": "hackernews",
    "points": 79,
    "published_at": "2026-10-14T12:05:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:50110301",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia, Apple, Google, Microsoft, Amazon, Meta gave Trump $92M for his ballroom",
    "url": "https://www.theverge.com/policy/1012047/nvidia-apple-google-microsoft-amazon-meta-trump-ballroom",
    "source": "jacquesm",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-10-15T21:11:05+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/semicon-west-2026-displays-ai-era-chipmaking-workforce-development/",
    "domain": "AI 算力 / 半导体",
    "title": "SEMICON West 2026 Displays AI-Era Chipmaking, Workforce Development",
    "url": "https://www.eetimes.com/semicon-west-2026-displays-ai-era-chipmaking-workforce-development/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T20:59:50+00:00",
    "summary": "The trillion-dollar semiconductor industry is ready to adapt and expand its fab infrastructure for the AI wave. The post SEMICON West 2026 Displays AI-Era Chipmaking, Workforce Development appeared fi"
  },
  {
    "id": "rss:https://www.eetimes.com/data-center-power-a-prominent-highlight-of-ocp-2026/",
    "domain": "AI 算力 / 半导体",
    "title": "Data Center Power a Prominent Highlight of OCP 2026",
    "url": "https://www.eetimes.com/data-center-power-a-prominent-highlight-of-ocp-2026/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T15:00:00+00:00",
    "summary": "The OCP Summit showcased power delivery boards, PSU designs, hot-swap controllers, and event-based telemetry. The post Data Center Power a Prominent Highlight of OCP 2026 appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/taiwans-ai-ambitions-run-into-talent-gap/",
    "domain": "AI 算力 / 半导体",
    "title": "Taiwan’s AI Ambitions Run into Talent Gap",
    "url": "https://www.eetimes.com/taiwans-ai-ambitions-run-into-talent-gap/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T10:55:42+00:00",
    "summary": "AMD’s David Wang told EE Times that while Taiwan has huge opportunities in rack-scale AI, physical AI, and AI PC markets, the sticking point may well be talent. The post Taiwan’s AI Ambitions Run into"
  },
  {
    "id": "rss:https://www.eetimes.com/your-chip-works-prove-it-is-secure/",
    "domain": "AI 算力 / 半导体",
    "title": "Your Chip Works. Prove It Is Secure.",
    "url": "https://www.eetimes.com/your-chip-works-prove-it-is-secure/",
    "source": "Arteris",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T08:37:49+00:00",
    "summary": "Join this 30-Minute BitCast as our expert demonstrates how information flow tracking follows security-sensitive assets during existing simulation or emulation runs. The post Your Chip Works. Prove It "
  },
  {
    "id": "rss:https://www.eetimes.com/ai-moves-to-system-level-co-design-how-can-taiwan-capture-more-value/",
    "domain": "AI 算力 / 半导体",
    "title": "AI Moves to System-Level Co-Design: How Can Taiwan Capture More Value",
    "url": "https://www.eetimes.com/ai-moves-to-system-level-co-design-how-can-taiwan-capture-more-value/",
    "source": "Susan Hong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T07:18:34+00:00",
    "summary": "During a panel session at iTechCon 2026, discussions explored how Taiwan can build on its strengths in semiconductors, advanced packaging, and system design to support AI development. The post AI Move"
  },
  {
    "id": "rss:https://www.eetimes.com/japan-offers-globalfoundries-21b-for-u-s-fab-expansion/",
    "domain": "AI 算力 / 半导体",
    "title": "Japan Offers GlobalFoundries $21B for U.S. Fab Expansion",
    "url": "https://www.eetimes.com/japan-offers-globalfoundries-21b-for-u-s-fab-expansion/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T19:00:00+00:00",
    "summary": "Japan’s $21B offer to GlobalFoundries would add two New York fabs and lift U.S. chip capacity 10%; see why analysts warn on state support. The post Japan Offers GlobalFoundries $21B for U.S. Fab Expan"
  },
  {
    "id": "rss:https://www.eetimes.com/data-orchestration-the-foundation-for-the-next-generation-semiconductor-enterprise/",
    "domain": "AI 算力 / 半导体",
    "title": "Data Orchestration: The Foundation for the Next-generation Semiconductor Enterprise",
    "url": "https://www.eetimes.com/data-orchestration-the-foundation-for-the-next-generation-semiconductor-enterprise/",
    "source": "Siemens Digital Industries",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T14:00:00+00:00",
    "summary": "Data orchestration gives semiconductor engineering teams a practical way to unify disconnected equipment, systems, and data without replacing existing infrastructure. By creating a connected execution"
  },
  {
    "id": "rss:https://www.eetimes.com/husb237-the-cost-effective-pd-sink-with-just-2-passives/",
    "domain": "AI 算力 / 半导体",
    "title": "HUSB237: The Cost-Effective PD Sink with Just 2 Passives",
    "url": "https://www.eetimes.com/husb237-the-cost-effective-pd-sink-with-just-2-passives/",
    "source": "Hynetek Semiconductor Co., Ltd.",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T13:00:00+00:00",
    "summary": "Discover Hynetek’s HUSB237, a compact USB-PD sink controller enabling firmware-free USB-C upgrades up to 100W with only two external components. The post HUSB237: The Cost-Effective PD Sink with Just "
  },
  {
    "id": "rss:https://www.eetimes.com/small-volumes-big-impact-europes-hidden-role-in-advanced-chipmaking/",
    "domain": "AI 算力 / 半导体",
    "title": "Small Volumes, Big Impact: Europe’s Hidden Role in Advanced Chipmaking",
    "url": "https://www.eetimes.com/small-volumes-big-impact-europes-hidden-role-in-advanced-chipmaking/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T10:54:08+00:00",
    "summary": "A Fraunhofer–IMS Nanofabrication partnership illustrates how Europe's low-volume semiconductor manufacturing can support the world's most advanced chipmaking. The post Small Volumes, Big Impact: Europ"
  },
  {
    "id": "rss:https://www.eetimes.com/grid-modernization-hidden-cost-a-growing-attack-surface-few-are-watching/",
    "domain": "AI 算力 / 半导体",
    "title": "Grid Modernization’s Hidden Cost: A Growing Attack Surface Few Are Watching",
    "url": "https://www.eetimes.com/grid-modernization-hidden-cost-a-growing-attack-surface-few-are-watching/",
    "source": "David Montoya",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T08:00:00+00:00",
    "summary": "Grid modernization is expanding the energy sector’s cyberattack surface, while limited visibility across IT and OT networks leaves connected assets exposed. The post Grid Modernization’s Hidden Cost: "
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/this-could-be-your-last-chance-to-grab-an-rtx-5090-how-to-secure-nvidias-top-rtx-gpu-as-rumors-of-discontinuation-swirl",
    "domain": "AI 算力 / 半导体",
    "title": "This could be your last chance to grab an RTX 5090",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/this-could-be-your-last-chance-to-grab-an-rtx-5090-how-to-secure-nvidias-top-rtx-gpu-as-rumors-of-discontinuation-swirl",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T17:04:44+00:00",
    "summary": "With no new Nvidia 5090 GPU replacement anticipated before at least 2028, this could well be your last opportunity to get your hands on a very powerful GPU for gaming."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/china-startup-demoes-prototype-euv-light-source-15w-of-output-power-and-90-percent-domestic-components-still-years-away-from-viability",
    "domain": "AI 算力 / 半导体",
    "title": "China startup demoes prototype EUV light source",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/china-startup-demoes-prototype-euv-light-source-15w-of-output-power-and-90-percent-domestic-components-still-years-away-from-viability",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T16:30:00+00:00",
    "summary": "Chinese startup Langdao Silex showcased its laser-produced plasma EUV source at a trade show, but the technology will likely take many years before it gets to decent EUV power levels. Even if it does,"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/gun-rights-activist-unveils-worlds-first-ai-made-3d-printed-firearm-22-caliber-handgun-created-by-an-ai-that-can-generate-guns-called-gatgpt",
    "domain": "AI 算力 / 半导体",
    "title": "Gun-rights activist unveils world's first 'AI-made' 3D-printed firearm — .22 caliber handgun created by an 'AI that can generate guns' called GatGPT",
    "url": "https://www.tomshardware.com/3d-printing/gun-rights-activist-unveils-worlds-first-ai-made-3d-printed-firearm-22-caliber-handgun-created-by-an-ai-that-can-generate-guns-called-gatgpt",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T16:20:41+00:00",
    "summary": "A gun rights activist has unveiled the world's first AI-made 3D printed firearm."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/nvidia-rtx-spark-devices-are-now-officially-on-sale-secure-the-surface-laptop-ultra-or-other-rtx-spark-laptops-here-starting-at-usd2-599-where-to-buy-pricing-and-availability-revealed-on-several-models",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia RTX Spark devices are now officially on sale, secure the Surface Laptop Ultra or other RTX Spark laptops here",
    "url": "https://www.tomshardware.com/laptops/nvidia-rtx-spark-devices-are-now-officially-on-sale-secure-the-surface-laptop-ultra-or-other-rtx-spark-laptops-here-starting-at-usd2-599-where-to-buy-pricing-and-availability-revealed-on-several-models",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T15:38:45+00:00",
    "summary": "Orders are live on Nvidia RTX Spark laptops, including the Microsoft Surface Laptop Ultra and devices from HP, Lenovo, Asus, and Dell."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/new-york-rep-announces-game-ownership-bill-that-would-require-consumer-ownership-rather-than-sale-of-licenses-would-also-require-publishers-to-keep-the-game-functional-after-support-ends",
    "domain": "AI 算力 / 半导体",
    "title": "New York rep announces game ownership bill that would require consumer ownership rather than sale of licenses",
    "url": "https://www.tomshardware.com/video-games/new-york-rep-announces-game-ownership-bill-that-would-require-consumer-ownership-rather-than-sale-of-licenses-would-also-require-publishers-to-keep-the-game-functional-after-support-ends",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T13:51:32+00:00",
    "summary": "New York joins Pennsylvania in protecting gamers' rights to own games, requiring publishers to provide an offline mode and the right to transfer games."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/motherboards/gigabyte-x870-aorus-infinity-motherboard-review",
    "domain": "AI 算力 / 半导体",
    "title": "Gigabyte X870 Aorus Infinity Motherboard Review: limited-edition, designed for extreme overclocking, but pricey for X870",
    "url": "https://www.tomshardware.com/pc-components/motherboards/gigabyte-x870-aorus-infinity-motherboard-review",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T13:00:00+00:00",
    "summary": "Gigabyte’s limited-edition 40th-anniversary X870 Aorus Infinity motherboard is designed for extreme overclocking, with everything you need for daily use."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/googlebooks-are-as-poorly-timed-as-valves-steam-machine-and-may-suffer-a-similar-fate",
    "domain": "AI 算力 / 半导体",
    "title": "Googlebooks are as poorly timed as Valve’s Steam Machine, and may suffer a similar fate",
    "url": "https://www.tomshardware.com/laptops/googlebooks-are-as-poorly-timed-as-valves-steam-machine-and-may-suffer-a-similar-fate",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T12:30:00+00:00",
    "summary": "Google attempted to take its Chromebook platform upscale with Googlebooks. But the timing could not have been worse. Phone support at launch is extremely limited, and most people use Android phones an"
  },
  {
    "id": "rss:https://www.tomshardware.com/tablets/microsoft-surface/microsoft-surface-laptop-ultra-rtx-spark-review",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft Surface Laptop Ultra review: RTX Spark in a straight-up beautiful Windows PC",
    "url": "https://www.tomshardware.com/tablets/microsoft-surface/microsoft-surface-laptop-ultra-rtx-spark-review",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T12:00:00+00:00",
    "summary": "Microsoft’s Surface Laptop Ultra is its most beautiful laptop ever, but using Windows on it is the same as ever. Only AI enthusiasts will get the most out of RTX Spark."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/taiwan-raising-usd4-billion-to-build-industrial-park-in-texas-to-support-us-chipmaking-supply-chain-project-to-support-countless-small-manufacturers-crucial-to-tsmc-foxconn-supply-chain",
    "domain": "AI 算力 / 半导体",
    "title": "Taiwan raising $4 billion to build industrial park in Texas to support US chipmaking supply chain",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/taiwan-raising-usd4-billion-to-build-industrial-park-in-texas-to-support-us-chipmaking-supply-chain-project-to-support-countless-small-manufacturers-crucial-to-tsmc-foxconn-supply-chain",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T11:57:18+00:00",
    "summary": "This $4 billion industrial park would make it easier for smaller Taiwanese companies who can't afford to build their own sites in the U.S. to expand and follow major Taiwanese manufacturers like TSMC "
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/epic-introduces-an-improved-version-of-anti-cheat-for-linux-eac-linux-v2-will-finally-allow-linux-gamers-to-play-fortnite",
    "domain": "AI 算力 / 半导体",
    "title": "Epic introduces an improved version of anti-cheat for Linux",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/epic-introduces-an-improved-version-of-anti-cheat-for-linux-eac-linux-v2-will-finally-allow-linux-gamers-to-play-fortnite",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T11:30:00+00:00",
    "summary": "Epic wants to work with developers and maintainers to find the best solution to making anti-cheat work seamlessly on Linux."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cooling/experiment-shows-liquid-metal-tim-doesnt-dry-out-it-turns-solid-two-year-electron-microscope-test-finds-gallium-bonds-with-copper-coolers-and-nickel-plating-keeps-the-layer-about-10-times-thinner",
    "domain": "AI 算力 / 半导体",
    "title": "Experiment shows liquid metal TIM doesn’t dry out; it turns solid",
    "url": "https://www.tomshardware.com/pc-components/cooling/experiment-shows-liquid-metal-tim-doesnt-dry-out-it-turns-solid-two-year-electron-microscope-test-finds-gallium-bonds-with-copper-coolers-and-nickel-plating-keeps-the-layer-about-10-times-thinner",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T11:00:00+00:00",
    "summary": "Der8auer’s two-year electron microscope test shows liquid metal’s gallium turns solid on copper and nickel-plated coolers."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ddr5/corsairs-vengeance-rgb-ddr5-32gb-memory-receives-a-usd108-price-cut-the-cheapest-ddr5-5600-kit-available-to-buy-right-now",
    "domain": "AI 算力 / 半导体",
    "title": "Corsair's Vengeance RGB DDR5 32GB memory receives a $108 price cut",
    "url": "https://www.tomshardware.com/pc-components/ddr5/corsairs-vengeance-rgb-ddr5-32gb-memory-receives-a-usd108-price-cut-the-cheapest-ddr5-5600-kit-available-to-buy-right-now",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T10:55:27+00:00",
    "summary": "Save $108 on Corsair's Vengeance RGB RAM and bag 32GB of DDR5 memory for your PC."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/linux/linus-torvalds-posts-his-first-llm-assisted-patch-to-the-linux-kernel-after-issuing-clear-pro-ai-directives-the-bossman-makes-use-of-ai-tooling-himself",
    "domain": "AI 算力 / 半导体",
    "title": "Linus Torvalds posts his first AI-assisted patch to the Linux kernel, synthetic test clocks 23x performance leap",
    "url": "https://www.tomshardware.com/software/linux/linus-torvalds-posts-his-first-llm-assisted-patch-to-the-linux-kernel-after-issuing-clear-pro-ai-directives-the-bossman-makes-use-of-ai-tooling-himself",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T10:30:00+00:00",
    "summary": "Linus Torvalds posts his first LLM-assisted patch to the Linux kernel — after issuing clear pro-AI directives, the bossman makes use of AI tooling himself"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/thai-cops-bust-audacious-cross-border-fiberoptic-cable-running-to-myanmar-scam-compound-350-meter-48-core-cable-was-supplying-illegal-border-casino-and-a-scam-center-with-6tb-of-data-per-day",
    "domain": "AI 算力 / 半导体",
    "title": "Thai cops bust 'audacious' cross-border fiberoptic cable running to Myanmar scam compound",
    "url": "https://www.tomshardware.com/tech-industry/thai-cops-bust-audacious-cross-border-fiberoptic-cable-running-to-myanmar-scam-compound-350-meter-48-core-cable-was-supplying-illegal-border-casino-and-a-scam-center-with-6tb-of-data-per-day",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T10:24:24+00:00",
    "summary": "Thai authorities have busted a cross-border fiber-optic internet cable being used to steal data."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/ukrainian-drones-hit-russian-data-centers-disrupting-russian-apps-and-services-attacks-highlight-the-fragility-of-the-countrys-digital-services",
    "domain": "AI 算力 / 半导体",
    "title": "Ukrainian drones hit Russian data centers, disrupting Russian apps and services",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/ukrainian-drones-hit-russian-data-centers-disrupting-russian-apps-and-services-attacks-highlight-the-fragility-of-the-countrys-digital-services",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T10:15:00+00:00",
    "summary": "After Ukrainian long-range strike drones targeted Russian data centers, various Russian digital services and apps went down or faced severe disruption. There's even some suggestion that online bot act"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/newegg-has-slashed-usd260-off-this-all-amd-4k-gaming-pc-9800x3d-and-radeon-rx-9070-xt-combo-comes-with-32gb-of-ddr5-and-a-2tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Newegg has slashed $260 off this all-AMD 4K gaming PC — 9800X3D and Radeon RX 9070 XT combo comes with 32GB of DDR5 and a 2TB SSD",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/newegg-has-slashed-usd260-off-this-all-amd-4k-gaming-pc-9800x3d-and-radeon-rx-9070-xt-combo-comes-with-32gb-of-ddr5-and-a-2tb-ssd",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T10:03:21+00:00",
    "summary": "Save $260 on an all-AMD gaming PC with 9800X3D and Radeon RX 9070 XT."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/jailbroken-ps5s-can-now-run-local-ai-models-at-over-100-tokens-per-second-fork-of-ps5lm-goes-native-and-accesses-gpu-and-more-ram",
    "domain": "AI 算力 / 半导体",
    "title": "Jailbroken PS5s can now run local AI models at over 100+ tokens per second",
    "url": "https://www.tomshardware.com/video-games/playstation/jailbroken-ps5s-can-now-run-local-ai-models-at-over-100-tokens-per-second-fork-of-ps5lm-goes-native-and-accesses-gpu-and-more-ram",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T10:00:00+00:00",
    "summary": "PS5LM gets a fork, allowing it to run natively and use the GPU and more RAM to run larger LLMs, even running Qwen3.8-27B at 20 tokens per second."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/formlabs-form-studio-1-review",
    "domain": "AI 算力 / 半导体",
    "title": "Formlabs Form Studio 1 Review: Professional status, consumer price tag",
    "url": "https://www.tomshardware.com/3d-printing/formlabs-form-studio-1-review",
    "source": "Matt Farmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T18:00:00+00:00",
    "summary": "The Form Studio 1 is Formlabs first consumer-grade printer. It combines a 200 × 125 × 235 mm build volume with resin heating, automatic dispensing, and a free Open Material Mode."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/sk-hynix-reportedly-playing-hardball-with-trump-admin-over-3d-nand-fab-company-demands-increased-chipmaking-equipment-exports-to-china-in-exchange-for-us-fab",
    "domain": "AI 算力 / 半导体",
    "title": "SK hynix denies playing hardball with Trump admin over 3D NAND fab",
    "url": "https://www.tomshardware.com/pc-components/ssds/sk-hynix-reportedly-playing-hardball-with-trump-admin-over-3d-nand-fab-company-demands-increased-chipmaking-equipment-exports-to-china-in-exchange-for-us-fab",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T17:40:09+00:00",
    "summary": "SK hynix reportedly conditions building new Solidigm 3D NAND fab in the U.S. to equipment exports to the Solidigm fab in Dalian, China."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-5090-disappears-from-micro-center-amid-rumors-of-a-production-halt-retailer-flags-flagship-as-not-carried-as-stock-mysteriously-vanishes",
    "domain": "AI 算力 / 半导体",
    "title": "RTX 5090 disappears from Nvidia marketplace amid reports of a production halt",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-5090-disappears-from-micro-center-amid-rumors-of-a-production-halt-retailer-flags-flagship-as-not-carried-as-stock-mysteriously-vanishes",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T15:37:41+00:00",
    "summary": "Micro Center has reclassified Nvidia GeForce RTX 5090 graphics cards as 'Not Carried,' and almost all units are out of stock at its stores."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/googlebooks-from-dell-lenovo-and-hp-tested-nice-hardware-but-the-os-isnt-ready-yet",
    "domain": "AI 算力 / 半导体",
    "title": "Googlebooks from Dell, Lenovo, and HP tested: Nice hardware, but the OS isn't ready yet",
    "url": "https://www.tomshardware.com/laptops/googlebooks-from-dell-lenovo-and-hp-tested-nice-hardware-but-the-os-isnt-ready-yet",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T15:00:00+00:00",
    "summary": "Googlebook OS needs a lot of love to feel like something other than Android on a PC."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/mini-pcs/sipeed-reveals-chinese-made-dgx-spark-and-ryzen-ai-halo-rival-expected-to-cost-usd3-999-maixstation-pairs-axeras-ax8860p-with-128gb-of-lpddr5x-at-273-gb-s-with-promising-local-ai-performance-claims",
    "domain": "AI 算力 / 半导体",
    "title": "Sipeed reveals Chinese-made DGX Spark and Ryzen AI Halo rival, expected to cost $3,999",
    "url": "https://www.tomshardware.com/desktops/mini-pcs/sipeed-reveals-chinese-made-dgx-spark-and-ryzen-ai-halo-rival-expected-to-cost-usd3-999-maixstation-pairs-axeras-ax8860p-with-128gb-of-lpddr5x-at-273-gb-s-with-promising-local-ai-performance-claims",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T14:30:00+00:00",
    "summary": "Sipeed’s MaixStation pairs Axera’s AX8860P with 128GB of LPDDR5X at 273 GB/s to take on Nvidia’s DGX Spark and AMD’s Ryzen AI Halo."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/the-internet-isnt-the-best-place-for-finding-pc-components-to-upgrade-your-computer-brick-and-mortar-stores-still-reign-supreme-thanks-to-bundled-deals",
    "domain": "AI 算力 / 半导体",
    "title": "The internet isn’t the best place to find upgrades for your computer — brick-and-mortar stores still reign supreme thanks to bundled deals",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/the-internet-isnt-the-best-place-for-finding-pc-components-to-upgrade-your-computer-brick-and-mortar-stores-still-reign-supreme-thanks-to-bundled-deals",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T14:00:00+00:00",
    "summary": "Component bundles are a great way of offsetting high prices on certain parts, but your proximity to a Micro Center may save you even more."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/eu-negotiates-sanction-swap-with-china-to-rescue-critical-asml-supplier-german-coatings-firm-faces-shutdown-without-chinese-rare-earths",
    "domain": "AI 算力 / 半导体",
    "title": "EU negotiates sanction swap with China to rescue critical ASML supplier",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/eu-negotiates-sanction-swap-with-china-to-rescue-critical-asml-supplier-german-coatings-firm-faces-shutdown-without-chinese-rare-earths",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T13:30:00+00:00",
    "summary": "The EU is reportedly negotiating with Beijing to remove Chinese restrictions on German ASML supplier Sindlhauser Materials, to prevent the China-dependent company from going out of business"
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/alienware-aw3226q-32-inch-4k-oled-gaming-monitor-review",
    "domain": "AI 算力 / 半导体",
    "title": "Alienware AW3226Q 32-inch 4K OLED gaming monitor review: Sleek design with performance and value to match",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/alienware-aw3226q-32-inch-4k-oled-gaming-monitor-review",
    "source": "Christian Eberle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T13:00:00+00:00",
    "summary": "Alienware rolls Tandem RGB Stripe OLED tech into a stylish 32-inch gaming monitor for a low price. The AW3226Q delivers 4K resolution, 165 Hz, Adaptive-Sync, HDR400 True Black, Dolby Vision, and wide-"
  },
  {
    "id": "rss:https://www.tomshardware.com/service-providers/network-providers/malicious-russian-disinformation-bot-traffic-barely-flinches-after-ukraine-strikes-yandex-data-centers-and-auto-migration-kicks-in-cloudflare-tracks-170-million-automated-attacks-shifting-to-alternate-cloud-hosts",
    "domain": "AI 算力 / 半导体",
    "title": "Malicious Russian disinformation bot traffic barely flinches after Ukraine strikes Yandex data centers and auto-migration kicks in",
    "url": "https://www.tomshardware.com/service-providers/network-providers/malicious-russian-disinformation-bot-traffic-barely-flinches-after-ukraine-strikes-yandex-data-centers-and-auto-migration-kicks-in-cloudflare-tracks-170-million-automated-attacks-shifting-to-alternate-cloud-hosts",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T12:28:24+00:00",
    "summary": "Ukraine's strikes on Russian data centers have caused legitimate bot traffic to go down, but malicious bots remain operational."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/we-test-the-rtx-spark-superchip-in-microsofts-surface-laptop-ultra-nvidias-windows-on-arm-platform-impresses-in-local-ai-but-gaming-isnt-its-strong-suit",
    "domain": "AI 算力 / 半导体",
    "title": "We tested the RTX Spark Superchip in Microsoft's Surface Laptop Ultra",
    "url": "https://www.tomshardware.com/laptops/we-test-the-rtx-spark-superchip-in-microsofts-surface-laptop-ultra-nvidias-windows-on-arm-platform-impresses-in-local-ai-but-gaming-isnt-its-strong-suit",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T12:00:21+00:00",
    "summary": "We've tested Nvidia's RTX Spark against the latest and greatest from Apple and AMD to see how Nvidia's efforts to transform the PC for the agentic AI era stack up."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/asml-reports-record-usd13-billion-quarter-vows-to-expand-capacity-as-demand-for-lithography-equipment-soars-customers-eager-to-secure-orders-in-2030-as-demand-is-expected-to-outstrip-2027-and-2028-supply",
    "domain": "AI 算力 / 半导体",
    "title": "ASML reports record $13 billion quarter, vows to expand capacity as demand for lithography equipment soars",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/asml-reports-record-usd13-billion-quarter-vows-to-expand-capacity-as-demand-for-lithography-equipment-soars-customers-eager-to-secure-orders-in-2030-as-demand-is-expected-to-outstrip-2027-and-2028-supply",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T12:00:00+00:00",
    "summary": "ASML vows to expand production capacity amid growing demand, record earnings and profitability."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/save-usd249-on-32gb-of-ddr5-with-this-3-item-newegg-bundle-score-32gb-of-g-skill-trident-z5-neox-ram-a-ryzen-7-9800x3d-and-an-msi-x870e-motherboard-for-only-usd1-094-99",
    "domain": "AI 算力 / 半导体",
    "title": "Save $249 on 32GB of DDR5 with this 3-item Newegg bundle",
    "url": "https://www.tomshardware.com/pc-components/save-usd249-on-32gb-of-ddr5-with-this-3-item-newegg-bundle-score-32gb-of-g-skill-trident-z5-neox-ram-a-ryzen-7-9800x3d-and-an-msi-x870e-motherboard-for-only-usd1-094-99",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T11:56:24+00:00",
    "summary": "Score 32GB of G.Skill DDR5-6000 RAM for just $321 in Newegg’s new AM5 combo. For $1,094 ($249 off), you also get a Ryzen 7 9800X3D and an MSI X870E Tomahawk MAX WiFi board, plus a free AIO cooler."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/asml-struggling-to-keep-up-with-demand-for-chipmaking-equipment-as-ai-spending-continues-to-boom-chipmakers-are-already-looking-to-place-orders-for-2029-and-2030-output-ceo-says-demand-could-surpass-capacity-despite-massive-expansion-plans",
    "domain": "AI 算力 / 半导体",
    "title": "ASML struggling to keep up with demand for chipmaking equipment as AI spending continues to boom",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/asml-struggling-to-keep-up-with-demand-for-chipmaking-equipment-as-ai-spending-continues-to-boom-chipmakers-are-already-looking-to-place-orders-for-2029-and-2030-output-ceo-says-demand-could-surpass-capacity-despite-massive-expansion-plans",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T11:30:00+00:00",
    "summary": "ASML says customers are already placing orders for advanced chipmaking tools years in advance, with AI-driven semiconductor demand remaining strong enough to strain capacity despite planned expansions"
  },
  {
    "id": "hn:50081435",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Reportedly Ending the RTX 5090, Reserves GB202 for Workstation GPUs",
    "url": "https://www.techpowerup.com/353578/nvidia-reportedly-ending-the-rtx-5090-reserves-gb202-silicon-for-workstation-gpus",
    "source": "kristianp",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-10-14T01:52:56+00:00",
    "summary": ""
  },
  {
    "id": "hn:50062098",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia accused of trying to cut a deal with Anna's Archive",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-accused-of-trying-to-cut-a-deal-with-annas-archive-for-high-speed-access-to-the-massive-pirated-book-haul-allegedly-chased-stolen-data-to-fuel-its-llms",
    "source": "amai",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-10-12T19:57:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:50046896",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia-backed data centre firm Firmus scraps IPO as AI valuation concerns deepen",
    "url": "https://www.bbc.com/news/articles/ck9dzpw4ll8po",
    "source": "devonnull",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-10-11T19:26:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:49973937",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's Olympus Core: Pushing Server Single Threaded Performance Boundaries",
    "url": "https://chipsandcheese.com/p/nvidias-olympus-core-pushing-server",
    "source": "pella",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-10-06T03:51:00+00:00",
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
    "id": "hn:49913571",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/",
    "source": "bradleyg223",
    "platform": "hackernews",
    "points": 1705,
    "published_at": "2026-09-30T20:04:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:50073879",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon",
    "url": "https://deepmind.google/models/gemini/",
    "source": "737max",
    "platform": "hackernews",
    "points": 1461,
    "published_at": "2026-10-13T16:03:16+00:00",
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
    "id": "hn:49957116",
    "domain": "大厂 AI 动态",
    "title": "Turn off Apple Intelligence on macOS 27 and get its disk space back",
    "url": "https://github.com/omlahore/RemoveMacAI",
    "source": "privacyisntdead",
    "platform": "hackernews",
    "points": 775,
    "published_at": "2026-10-04T19:42:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:49848269",
    "domain": "大厂 AI 动态",
    "title": "Ollaya – Ollama for open-source, Jev-style decision models",
    "url": "https://ollaya.dev/",
    "source": "Ardakilic",
    "platform": "hackernews",
    "points": 618,
    "published_at": "2026-09-25T18:33:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:50122431",
    "domain": "大厂 AI 动态",
    "title": "Llama.cpp on a jailbroken PS5: run any GGUF model natively on the console",
    "url": "https://github.com/cobanov/PS5LM",
    "source": "Anon84",
    "platform": "hackernews",
    "points": 272,
    "published_at": "2026-10-16T18:32:35+00:00",
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
    "id": "hn:50118688",
    "domain": "大厂 AI 动态",
    "title": "Show HN: Gemini 4 Argon plays StarCraft",
    "url": "https://starskirmish.com/bench/v0-2/",
    "source": "__cayenne__",
    "platform": "hackernews",
    "points": 213,
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
    "points": 232,
    "published_at": "2026-10-13T16:55:47+00:00",
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
    "id": "hn:49914236",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon (High): Intelligence, Performance and Price Analysis",
    "url": "https://artificialanalysis.ai/models/gemini-4-argon",
    "source": "theanonymousone",
    "platform": "hackernews",
    "points": 113,
    "published_at": "2026-09-30T20:50:28+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/tech/1010131/apple-iphone-duo-news-announcements",
    "domain": "大厂 AI 动态",
    "title": "All the news about the iPhone Duo",
    "url": "https://www.theverge.com/tech/1010131/apple-iphone-duo-news-announcements",
    "source": "Verge Staff",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T23:36:26+00:00",
    "summary": "Apple has finally announced its long-rumored foldable: the iPhone Duo. The new phone has a 5.4-inch outer display and a 7.6-inch inner display, a “nano‑texture” finish on the inner screen, and barely "
  },
  {
    "id": "rss:https://www.theverge.com/tech/1013314/apple-app-store-nudify-ai-apps-harassment",
    "domain": "大厂 AI 动态",
    "title": "Apple&#8217;s updated App Store rules go after &#8216;nudify&#8217; AI apps",
    "url": "https://www.theverge.com/tech/1013314/apple-app-store-nudify-ai-apps-harassment",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T22:51:22+00:00",
    "summary": "Apple's App Store rules now more explicitly ban so-called \"nudify\" apps that generate intimate images of people without their consent using AI tools. The rule changes follow significant criticism towa"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/1013277/wu-tang-once-upon-a-time-in-shaolin-pablo-torre-martin-shkreli",
    "domain": "大厂 AI 动态",
    "title": "We can finally hear some of Wu-Tang Clan&#8217;s Once Upon A Time in Shaolin album",
    "url": "https://www.theverge.com/entertainment/1013277/wu-tang-once-upon-a-time-in-shaolin-pablo-torre-martin-shkreli",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T20:50:27+00:00",
    "summary": "Wu-Tang's Once Upon A Time in Shaolin album has, for the most part, been extremely difficult to listen to, but you can now hear two snippets of the album thanks to the podcast Pablo Torre Finds Out, w"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/1013280/tesla-chp-fsd-crash",
    "domain": "大厂 AI 动态",
    "title": "Tesla driver says he was asleep and using FSD when he crashed into highway patrol cars",
    "url": "https://www.theverge.com/transportation/1013280/tesla-chp-fsd-crash",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T20:49:04+00:00",
    "summary": "After this horrific crash involving a Tesla driver who said he was asleep and using the driver assist mode, the California Highway Patrol warns that \"Despite its name, full self-driving is not fully a"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1013025/apple-home-collection-products-lg-schneider-smart-home",
    "domain": "大厂 AI 动态",
    "title": "Why Apple is finally making its own smart home devices",
    "url": "https://www.theverge.com/tech/1013025/apple-home-collection-products-lg-schneider-smart-home",
    "source": "Jennifer Pattison Tuohy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T18:30:27+00:00",
    "summary": "For more than a decade, Apple has told other companies to build smart home devices for its platform. This week, Apple launched its own. The Apple Home Collection is a lineup of cameras, thermostats, s"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1012962/apple-tv-4k-fourth-generation-fanttik-s1-pro-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "The new Apple TV 4K just got its first (very small) discount",
    "url": "https://www.theverge.com/gadgets/1012962/apple-tv-4k-fourth-generation-fanttik-s1-pro-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T16:02:22+00:00",
    "summary": "Earlier this week, Apple announced its new Apple TV 4K, which costs nearly twice as much as the 2022 model did at launch. Amazon is now offering the first discount on the forthcoming streaming box (co"
  },
  {
    "id": "rss:https://www.theverge.com/podcast/1012911/apple-homeview-apps-carplay-vergecast",
    "domain": "大厂 AI 动态",
    "title": "Apple&#8217;s HomeView has an app problem",
    "url": "https://www.theverge.com/podcast/1012911/apple-homeview-apps-carplay-vergecast",
    "source": "David Pierce",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T15:38:17+00:00",
    "summary": "It's been a couple of days since Apple's big smart home announcement, and we have some more information - and a bunch of new questions - about the Apple HomeView. The device has plenty of computing oo"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1012901/analogue-retro-console-supern-nt-plus-nintendo-sega-genesis-mega-plus",
    "domain": "大厂 AI 动态",
    "title": "Analogue is re-releasing its SNES and Genesis consoles with some nice upgrades",
    "url": "https://www.theverge.com/tech/1012901/analogue-retro-console-supern-nt-plus-nintendo-sega-genesis-mega-plus",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T15:08:38+00:00",
    "summary": "Analogue announced new versions of its Super Nt and Mega Sg retro consoles today with a \"reworked industrial design\" and built-in wireless connectivity for controllers and accessories. Like the origin"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1012918/google-play-store-fake-whatsapp-android",
    "domain": "大厂 AI 动态",
    "title": "A fake WhatsApp clone is showing up before the real version on the Play Store",
    "url": "https://www.theverge.com/tech/1012918/google-play-store-fake-whatsapp-android",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T15:02:23+00:00",
    "summary": "After a Chrome clone was spotted on the Play Store earlier this week, a user on Reddit says they're seeing a fake version of WhatsApp in a \"sponsored\" slot above the real version. As reported earlier "
  },
  {
    "id": "rss:https://www.theverge.com/tech/1012748/nvidia-rtx-spark-windows-arm-laptops-asus-hp-lenovo-impressions",
    "domain": "大厂 AI 动态",
    "title": "A week with RTX Spark: everything we’ve learned using Nvidia’s new laptops",
    "url": "https://www.theverge.com/tech/1012748/nvidia-rtx-spark-windows-arm-laptops-asus-hp-lenovo-impressions",
    "source": "Tom Warren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T15:00:00+00:00",
    "summary": "Nvidia's RTX Spark N1X processor is finally here, and we've been collectively testing a small fortune's worth of powerful laptops sporting this new \"superchip.\" RTX Spark is designed to be a high-perf"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/16/mark-wahlberg-wants-to-take-on-the-longevity-startup-crowd-with-an-affordable-gym-concept/",
    "domain": "大厂 AI 动态",
    "title": "Mark Wahlberg wants to take on the longevity-startup crowd with an affordable gym concept",
    "url": "https://techcrunch.com/2026/10/16/mark-wahlberg-wants-to-take-on-the-longevity-startup-crowd-with-an-affordable-gym-concept/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T02:36:18+00:00",
    "summary": "Mark Wahlberg, who once sank money into a gym chain that got kicked off the NYSE, is now building his own, and he promises you’ll get a cold plunge, a blood panel and a protein muffin without needing "
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/16/replit-is-no-longer-working-with-anthropic-ceo-says/",
    "domain": "大厂 AI 动态",
    "title": "Replit is no longer working with Anthropic, CEO says",
    "url": "https://techcrunch.com/2026/10/16/replit-is-no-longer-working-with-anthropic-ceo-says/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T21:22:28+00:00",
    "summary": "Masad said the decision was made for a number of different reasons, including cost. Replit announced a partnership with OpenAI in August, but there was never any indication that it was no longer with "
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/16/porsches-electric-macan-turbo-is-an-automotive-existential-crisis/",
    "domain": "大厂 AI 动态",
    "title": "Porsche’s electric Macan Turbo is an automotive existential crisis",
    "url": "https://techcrunch.com/2026/10/16/porsches-electric-macan-turbo-is-an-automotive-existential-crisis/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T19:40:00+00:00",
    "summary": "The 2026 Porsche Macan Turbo EV is a two-row crossover with 630 horsepower and a 100-kilowatt-hour battery."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/16/india-becomes-the-latest-country-to-report-rogue-ai-agent-activity/",
    "domain": "大厂 AI 动态",
    "title": "India becomes the latest country to report rogue AI agent activity",
    "url": "https://techcrunch.com/2026/10/16/india-becomes-the-latest-country-to-report-rogue-ai-agent-activity/",
    "source": "Aditya Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T17:52:24+00:00",
    "summary": "The agents got in through credentials and connection settings left exposed in app configurations, public code repositories, and overly permissive cloud roles."
  },
  {
    "id": "rss:https://techcrunch.com/video/a-nvidia-insider-turned-vc-on-why-robotics-hasnt-hit-its-chatgpt-moment-yet/",
    "domain": "大厂 AI 动态",
    "title": "An Nvidia insider-turned-VC on why robotics hasn’t hit its ChatGPT moment, yet",
    "url": "https://techcrunch.com/video/a-nvidia-insider-turned-vc-on-why-robotics-hasnt-hit-its-chatgpt-moment-yet/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T16:30:00+00:00",
    "summary": "Amulya Vishwanath, who spent seven years leading product marketing for NVIDIA’s robotics platforms, says robotics is currently in its “Lego era,” with the basic building blocks like actuators, robotic"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/16/waymos-robotaxis-are-headed-to-canada/",
    "domain": "大厂 AI 动态",
    "title": "Waymo’s robotaxis are headed to Canada",
    "url": "https://techcrunch.com/2026/10/16/waymos-robotaxis-are-headed-to-canada/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T16:06:38+00:00",
    "summary": "The company will start off by testing its self-driving vehicles on Toronto's streets."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/16/elorians-first-ai-model-wants-to-reason-with-images-not-just-about-them/",
    "domain": "大厂 AI 动态",
    "title": "Elorian’s first AI model wants to reason with images, not just about them",
    "url": "https://techcrunch.com/2026/10/16/elorians-first-ai-model-wants-to-reason-with-images-not-just-about-them/",
    "source": "Aditya Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T16:01:37+00:00",
    "summary": "According to Elorian's evaluations, Glimpse outperforms even GPT-6 Astra on scientific chart reasoning and short-form video captioning, with competitive results on other visual reasoning tasks."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/16/tressfecta-wants-to-make-hair-braiding-a-less-arduous-task-for-hairstylists/",
    "domain": "大厂 AI 动态",
    "title": "Tressfecta wants to make hair braiding a less arduous task for hairstylists",
    "url": "https://techcrunch.com/2026/10/16/tressfecta-wants-to-make-hair-braiding-a-less-arduous-task-for-hairstylists/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T16:00:00+00:00",
    "summary": "Tressfecta builds products for textured hair. Its first project is a tool called Plait Pilot that helps braiders with the initial process of separating hair from packs before braiding begins."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/16/in-you-can-see-everything-elizabeth-holmes-meets-her-equal-in-comedian-nathan-fielder/",
    "domain": "大厂 AI 动态",
    "title": "In ‘You Can See Everything,’ Elizabeth Holmes meets her equal in comedian Nathan Fielder",
    "url": "https://techcrunch.com/2026/10/16/in-you-can-see-everything-elizabeth-holmes-meets-her-equal-in-comedian-nathan-fielder/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T16:00:00+00:00",
    "summary": "Nathan Fielder's documentary about disgraced Theranos CEO Elizabeth Holmes has created a constellation of colliding personas that interrogate the very nature of authenticity."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/16/jev-is-vercels-fastest-adopted-ai-model-ever/",
    "domain": "大厂 AI 动态",
    "title": "Jev is Vercel’s fastest-adopted AI model ever",
    "url": "https://techcrunch.com/2026/10/16/jev-is-vercels-fastest-adopted-ai-model-ever/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T15:33:49+00:00",
    "summary": "The data comes from Vercel's AI gateway, a unified API service similar to OpenRouter."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/16/mark-wahlberg-on-using-ai-in-film-the-right-way-and-being-open-to-an-ai-clone-carrying-on-his-legacy/",
    "domain": "大厂 AI 动态",
    "title": "Mark Wahlberg on using AI in film ‘the right way’ and being open to an AI clone carrying on his legacy",
    "url": "https://techcrunch.com/2026/10/16/mark-wahlberg-on-using-ai-in-film-the-right-way-and-being-open-to-an-ai-clone-carrying-on-his-legacy/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T14:26:51+00:00",
    "summary": "Actor and angel investor Mark Wahlberg says he's OK with using AI in filmmaking, provided it's used \"to enhance what you're doing.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/16/veritas-is-building-a-chip-to-verify-luxury-goods/",
    "domain": "大厂 AI 动态",
    "title": "Veritas expands its anti-counterfeit chip to jewelry, trophies, and fragrance bottles",
    "url": "https://techcrunch.com/2026/10/16/veritas-is-building-a-chip-to-verify-luxury-goods/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T14:00:00+00:00",
    "summary": "Counterfeiters are getting better at replicating brands' marks and passing off dupes, known as \"superfakes,\" as genuine items. A startup called Veritas wants to tackle the problem with its own chip th"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/16/replits-ceo-says-the-future-of-work-is-the-self-driving-company/",
    "domain": "大厂 AI 动态",
    "title": "Replit’s CEO says the future of work is the ‘self-driving company’",
    "url": "https://techcrunch.com/2026/10/16/replits-ceo-says-the-future-of-work-is-the-self-driving-company/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T12:55:09+00:00",
    "summary": "Replit CEO Amjad Masad envisions a future of “self-driving companies,” where AI agents handle day-to-day tasks and people focus on higher-level decisions."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/15/even-benchmark-thinks-ai-is-eroding-the-venture-pact-against-backing-rivals/",
    "domain": "大厂 AI 动态",
    "title": "Even Benchmark thinks AI is eroding the venture pact against backing rivals",
    "url": "https://techcrunch.com/2026/10/15/even-benchmark-thinks-ai-is-eroding-the-venture-pact-against-backing-rivals/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T05:16:46+00:00",
    "summary": "Benchmark says the Valley’s rule against backing rivals is getting harder to keep."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/15/tesla-reveals-spacex-powered-roadster-that-flies-and-falls-with-style/",
    "domain": "大厂 AI 动态",
    "title": "Tesla reveals SpaceX-powered Roadster that flies and falls with style",
    "url": "https://techcrunch.com/2026/10/15/tesla-reveals-spacex-powered-roadster-that-flies-and-falls-with-style/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T01:17:43+00:00",
    "summary": "The new car used thrusters to leap over a Cybercab, Cybertruck, Tesla Semi, Model Y, and Model 3 at a demo in Texas."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/15/when-it-came-to-cal-ais-viral-success-a-small-army-of-influencers-paid-off/",
    "domain": "大厂 AI 动态",
    "title": "When it came to Cal AI’s viral success, a small army of influencers paid off",
    "url": "https://techcrunch.com/2026/10/15/when-it-came-to-cal-ais-viral-success-a-small-army-of-influencers-paid-off/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T23:44:56+00:00",
    "summary": "The company generated over $30 million in revenue in two years and was acquired by MyFitnessPal for an undisclosed amount of money in March."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/15/and-the-winner-of-startup-battlefield-at-disrupt-2026-is-intero-biosystems/",
    "domain": "大厂 AI 动态",
    "title": "And the winner of Startup Battlefield at Disrupt 2026 is: Intero Biosystems",
    "url": "https://techcrunch.com/2026/10/15/and-the-winner-of-startup-battlefield-at-disrupt-2026-is-intero-biosystems/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T23:33:45+00:00",
    "summary": "Intero Biosystems beat out 199 other Startup Battlefield companies to take home the $100,000 grand prize at TechCrunch Disrupt 2026."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/15/amazon-devices-chief-panos-panay-on-the-importance-of-failure-and-bouncing-back-from-it/",
    "domain": "大厂 AI 动态",
    "title": "Amazon devices chief Panos Panay on the importance of failure and bouncing back from it",
    "url": "https://techcrunch.com/2026/10/15/amazon-devices-chief-panos-panay-on-the-importance-of-failure-and-bouncing-back-from-it/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T20:38:13+00:00",
    "summary": "Panay said that it's possible to recover and learn from all sorts of failures, even catastrophic ones, when building products."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/15/meta-launches-an-open-weight-model-that-runs-on-macs/",
    "domain": "大厂 AI 动态",
    "title": "Meta launches an open-weight AI model that runs on Macs",
    "url": "https://techcrunch.com/2026/10/15/meta-launches-an-open-weight-model-that-runs-on-macs/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T20:04:53+00:00",
    "summary": "Meta and Apple have teamed up for the launch of the social media giant's newest model, Muse Spark Open, which will run locally on Apple silicon."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/15/amazon-devices-chief-panos-panay-sees-a-future-where-ai-devices-replace-the-need-to-use-apps/",
    "domain": "大厂 AI 动态",
    "title": "Amazon devices chief Panos Panay sees a future where AI devices replace the need to use apps",
    "url": "https://techcrunch.com/2026/10/15/amazon-devices-chief-panos-panay-sees-a-future-where-ai-devices-replace-the-need-to-use-apps/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T19:55:25+00:00",
    "summary": "Speaking at TechCrunch Disrupt, Amazon devices chief Panos Panay described a future where ambient AI devices work in the background, anticipating users' needs instead of waiting for commands."
  },
  {
    "id": "rss:https://stratechery.com/2026/home-at-last/",
    "domain": "大厂 AI 动态",
    "title": "2026.42: Home At Last",
    "url": "https://stratechery.com/2026/home-at-last/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T17:42:42+00:00",
    "summary": "The best Stratechery content from the week of October 12, 2026, including what Apple is doing, SpaceX's appetite, and the title, takes, and the Washington Wizards."
  },
  {
    "id": "rss:https://stratechery.com/2026/a-conversation-with-ari-emanuel-about-entertainment-and-ai/",
    "domain": "大厂 AI 动态",
    "title": "A Conversation With Ari Emanuel About Entertainment and AI",
    "url": "https://stratechery.com/2026/a-conversation-with-ari-emanuel-about-entertainment-and-ai/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T10:00:00+00:00",
    "summary": "A conversation with Hollywood super-agent Ari Emanuel about his memoir, the impact of AI on Hollywood, and the power of a phone call."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/10/openai-models-hacked-a-crypto-wallet-and-breached-more-websites/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI models hacked a crypto wallet and breached more websites",
    "url": "https://arstechnica.com/security/2026/10/openai-models-hacked-a-crypto-wallet-and-breached-more-websites/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T20:59:01+00:00",
    "summary": "The actions could have resulted in criminal charges had humans been behind the keyboard."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/10/thegentlemanpervert-producing-ai-csam-is-a-nj-prosecutor-say-cops/",
    "domain": "大厂 AI 动态",
    "title": "“thegentlemanpervert” producing AI CSAM is a NJ prosecutor, say cops",
    "url": "https://arstechnica.com/tech-policy/2026/10/thegentlemanpervert-producing-ai-csam-is-a-nj-prosecutor-say-cops/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T20:20:07+00:00",
    "summary": "Discord user flagged AI CSAM, triggering arrest of New Jersey deputy AG."
  },
  {
    "id": "rss:https://arstechnica.com/gaming/2026/10/us-rep-proposes-bill-to-give-video-game-buyers-ownership-not-a-license/",
    "domain": "大厂 AI 动态",
    "title": "US Rep proposes bill to give video game buyers \"ownership,\" not \"a license\"",
    "url": "https://arstechnica.com/gaming/2026/10/us-rep-proposes-bill-to-give-video-game-buyers-ownership-not-a-license/",
    "source": "Samuel Axon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T19:41:18+00:00",
    "summary": "There are still significant hurdles ahead, both technical and legislative."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/10/ray-ban-meta-smart-glasses-found-recording-audio-without-wearers-consent/",
    "domain": "大厂 AI 动态",
    "title": "Bug turns one of the biggest fears about Ray-Ban Meta smart glasses into reality",
    "url": "https://arstechnica.com/gadgets/2026/10/ray-ban-meta-smart-glasses-found-recording-audio-without-wearers-consent/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T19:11:50+00:00",
    "summary": "The bug is fixed, but privacy concerns remain."
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
    "id": "hn:49886005",
    "domain": "股票",
    "title": "Anthropic's IPO prospectus shows AI vision, surging costs",
    "url": "https://www.reuters.com/business/finance/anthropics-ipo-prospectus-shows-sweeping-ai-vision-surging-costs-2026-09-28/",
    "source": "6thbit",
    "platform": "hackernews",
    "points": 145,
    "published_at": "2026-09-28T23:40:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:50113666",
    "domain": "股票",
    "title": "South Korea's stock market down, president telling people not to commit suicide",
    "url": "https://twitter.com/litcapital/status/2110752546415382699",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-10-16T03:26:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:50113735",
    "domain": "股票",
    "title": "CoreWeave Founders Shield Fortunes with $3.3B Stock Sales",
    "url": "https://www.bloomberg.com/news/articles/2026-10-15/coreweave-founders-shield-fortunes-with-3-3-billion-stock-sales",
    "source": "qlte",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-10-16T03:34:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:50122366",
    "domain": "股票",
    "title": "Anthropic's Valuation Collapsed by $500B",
    "url": "https://www.telegraph.co.uk/business/2026/10/16/anthropic-valuation-ipo-ai-stock-listing/",
    "source": "novaRom",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-10-16T18:27:58+00:00",
    "summary": ""
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
    "id": "hn:50029452",
    "domain": "股票",
    "title": "Data Center Darling Firmus's $30B IPO Dream Crushed in 48 Hours",
    "url": "https://www.bloomberg.com/news/articles/2026-10-09/data-center-darling-s-30-billion-ipo-dream-crushed-in-48-hours",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-10-10T04:04:17+00:00",
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
    "id": "hn:50098423",
    "domain": "股票",
    "title": "Asia chip stocks fall, AI funding worries",
    "url": "https://www.cnbc.com/2026/10/15/sk-hynix-samsung-softbank-stocks-asia-tech-rout-ai-funding-worries.html",
    "source": "kristianp",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-10-15T02:29:41+00:00",
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
    "id": "hn:50086344",
    "domain": "股票",
    "title": "Humxn Commits $50M to Buy Skilled Trades Data for Robotics Training",
    "url": "https://markets.businessinsider.com/news/stocks/humxn-research-labs-wants-to-buy-50-million-worth-of-skilled-trades-farming-and-manufacturing-data-for-ai-robotics-training-1036622854",
    "source": "howdoweknowit",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-10-14T12:04:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:50019535",
    "domain": "股票",
    "title": "Meadows – a small language for stock-and-flow diagrams that run",
    "url": "https://lorezzed.github.io/meadows/",
    "source": "jjsalamon",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-10-09T12:29:40+00:00",
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
    "id": "hn:49914149",
    "domain": "股票",
    "title": "Anthropic's IPO Prospectus Is a Fucking Doozy",
    "url": "https://daringfireball.net/linked/2026/09/30/reuters-anthropic-ipo-prospectus",
    "source": "danaris",
    "platform": "hackernews",
    "points": 71,
    "published_at": "2026-09-30T20:44:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:49997175",
    "domain": "股票",
    "title": "The world has nearly burned through its oil stockpile buffer",
    "url": "https://www.reuters.com/business/energy/world-has-nearly-burned-through-its-oil-stockpile-buffer-executives-say-2026-10-06/",
    "source": "geox",
    "platform": "hackernews",
    "points": 45,
    "published_at": "2026-10-07T18:50:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:50029232",
    "domain": "股票",
    "title": "Data centre company's much-hyped Australian stock market listing imploded",
    "url": "https://www.theguardian.com/australia-news/2026/oct/09/firmus-australian-stock-market-listing-bust-finance",
    "source": "stubish",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-10-10T03:23:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:50008977",
    "domain": "股票",
    "title": "Frontier AI models outperform analysts on earnings prediction",
    "url": "https://samaya.ai/blog/frontier-ai-models-outperform-human-experts-on-earnings-prediction",
    "source": "ashwinpp",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-10-08T17:33:29+00:00",
    "summary": ""
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
    "id": "hn:49796292",
    "domain": "股票",
    "title": "Smart Ring Maker Oura, Backers Seek $2.2B in US IPO",
    "url": "https://www.bloomberg.com/news/articles/2026-09-21/smart-ring-maker-oura-backers-seek-2-2-billion-in-us-ipo",
    "source": "elo2000",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-09-22T02:53:48+00:00",
    "summary": ""
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
    "id": "hn:50112657",
    "domain": "金融",
    "title": "Tesla Roadster",
    "url": "https://www.tesla.com/roadster",
    "source": "shekhar101",
    "platform": "hackernews",
    "points": 1370,
    "published_at": "2026-10-16T01:32:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:49778029",
    "domain": "金融",
    "title": "Samsung is expected to more than double output of its HBM4 and HBM4E DRAM",
    "url": "https://en.sedaily.com/finance/2026/09/20/samsung-to-double-hbm4-output-next-year-sources-say",
    "source": "giuliomagnifico",
    "platform": "hackernews",
    "points": 562,
    "published_at": "2026-09-20T17:38:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:49948254",
    "domain": "金融",
    "title": "Federal judge calls Flock 'indiscriminate mass surveillance'",
    "url": "https://techcrunch.com/2026/10/03/federal-judge-calls-flock-indiscriminate-mass-surveillance/",
    "source": "sbulaev",
    "platform": "hackernews",
    "points": 503,
    "published_at": "2026-10-03T22:07:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:49824686",
    "domain": "金融",
    "title": "Feds Target AI Critics as \"Foreign Agents\"",
    "url": "https://www.kenklippenstein.com/p/feds-think-ai-critics-are-foreign",
    "source": "nmeagent",
    "platform": "hackernews",
    "points": 396,
    "published_at": "2026-09-24T00:41:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:49875913",
    "domain": "金融",
    "title": "Parley: Federated, decentralised chat that speaks plain IRC",
    "url": "https://git.mills.io/prologic/parley",
    "source": "davidcollantes",
    "platform": "hackernews",
    "points": 330,
    "published_at": "2026-09-28T10:30:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:49921118",
    "domain": "金融",
    "title": "Meta Uses A.I. Data Centers to Avoid Billions in Federal Taxes",
    "url": "https://www.nytimes.com/2026/09/30/technology/meta-ai-data-centers-taxes.html",
    "source": "gmays",
    "platform": "hackernews",
    "points": 259,
    "published_at": "2026-10-01T13:05:51+00:00",
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
    "id": "hn:50090662",
    "domain": "金融",
    "title": "Tesla's Robotaxis Blow Through School Zones, NHTSA Petition Alleges",
    "url": "https://www.extremetech.com/cars/teslas-robotaxis-blow-through-school-zones-nhtsa-petition-alleges",
    "source": "speckx",
    "platform": "hackernews",
    "points": 146,
    "published_at": "2026-10-14T16:45:19+00:00",
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
    "id": "hn:50080275",
    "domain": "金融",
    "title": "Show HN: Pulse Local, a Mac budgeting app whose AI models run on your machine",
    "url": "https://pulseos.finance",
    "source": "niztk",
    "platform": "hackernews",
    "points": 121,
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
    "id": "hn:50105900",
    "domain": "金融",
    "title": "Market selloff, rising rates test AI data centre deal boom",
    "url": "https://www.reuters.com/business/finance/market-selloff-rising-rates-test-ai-data-centre-deal-boom-2026-10-15/",
    "source": "tartoran",
    "platform": "hackernews",
    "points": 73,
    "published_at": "2026-10-15T16:17:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:50116255",
    "domain": "金融",
    "title": "Tesla's new Roadster makes a flying debut, hitting 60 MPH in under a second",
    "url": "https://www.foxbusiness.com/technology/teslas-new-roadster-makes-flying-debut-hitting-60-mph-under-second",
    "source": "nsoonhui",
    "platform": "hackernews",
    "points": 70,
    "published_at": "2026-10-16T09:40:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:50114077",
    "domain": "金融",
    "title": "Tesla makes cars that fly? [video]",
    "url": "https://www.youtube.com/watch?v=7p5LxFdc-Qg",
    "source": "merinpapz10",
    "platform": "hackernews",
    "points": 69,
    "published_at": "2026-10-16T04:27:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:50118624",
    "domain": "金融",
    "title": "Tesla unveils 'flying' Roadster with SpaceX thrusters [video]",
    "url": "https://www.youtube.com/watch?v=eqOfmtTJD1A",
    "source": "skadamat",
    "platform": "hackernews",
    "points": 63,
    "published_at": "2026-10-16T14:12:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:49981063",
    "domain": "金融",
    "title": "Former German spy chief arrested for attempted treason",
    "url": "https://www.reuters.com/business/finance/former-german-spy-chief-detained-suspicion-espionage-treason-bild-reports-2026-10-06/",
    "source": "semiquaver",
    "platform": "hackernews",
    "points": 130,
    "published_at": "2026-10-06T16:51:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:50049302",
    "domain": "金融",
    "title": "Governments are mishandling the affordability crisis",
    "url": "https://www.economist.com/finance-and-economics/2026/10/08/governments-are-mishandling-the-affordability-crisis",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 105,
    "published_at": "2026-10-11T23:40:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:50112380",
    "domain": "金融",
    "title": "Tesla Debuts 2026 Roadster",
    "url": "https://www.nytimes.com/2026/10/15/business/tesla-roadster-2026-ev-sports-car.html",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 38,
    "published_at": "2026-10-16T00:57:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:49916668",
    "domain": "金融",
    "title": "10-year Treasury yield climbs above 5.3% to a level not seen in 24 years",
    "url": "https://www.wsj.com/finance/investing/surging-yields-bring-the-bond-market-back-to-the-turn-of-the-century-2b74773f",
    "source": "kaycebasques",
    "platform": "hackernews",
    "points": 125,
    "published_at": "2026-10-01T01:40:50+00:00",
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
    "id": "hn:50074739",
    "domain": "金融",
    "title": "Americans Trust in Federal Government Sinks to New Depths",
    "url": "https://news.gallup.com/poll/715361/trust-federal-government-sinks-new-depths.aspx",
    "source": "giuliomagnifico",
    "platform": "hackernews",
    "points": 48,
    "published_at": "2026-10-13T16:48:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:50023065",
    "domain": "金融",
    "title": "Tesla Rebrands Full Self-Driving as Tesla Assisted Driving in Europe",
    "url": "https://qz.com/tesla-full-self-driving-rebranding-europe-assisted-driving-100926",
    "source": "ilreb",
    "platform": "hackernews",
    "points": 53,
    "published_at": "2026-10-09T16:38:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:49916955",
    "domain": "金融",
    "title": "Cities Are Forced to Funnel License Plate Data to a Federal Surveillance Program",
    "url": "https://www.404media.co/how-cities-are-forced-to-funnel-license-plate-data-to-a-massive-federal-surveillance-program-hidta/",
    "source": "ripe",
    "platform": "hackernews",
    "points": 93,
    "published_at": "2026-10-01T02:26:17+00:00",
    "summary": ""
  },
  {
    "id": "hn:50062076",
    "domain": "金融",
    "title": "\"Today we're laying off a large part of the Airtable team \"",
    "url": "https://twitter.com/fedesimio/status/2109713695165329511",
    "source": "tortilla",
    "platform": "hackernews",
    "points": 45,
    "published_at": "2026-10-12T19:56:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:49938815",
    "domain": "金融",
    "title": "Federal Judge Rules a Flock Search Was Unconstitutional",
    "url": "https://www.404media.co/federal-judge-rules-a-flock-search-was-indiscriminate-mass-surveillance-and-unconstitutional/",
    "source": "pavel_lishin",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-10-02T21:28:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:49930690",
    "domain": "金融",
    "title": "Quantitative Finance with OCaml",
    "url": "https://qcaml.com/index.html",
    "source": "leonry",
    "platform": "hackernews",
    "points": 54,
    "published_at": "2026-10-02T07:14:34+00:00",
    "summary": ""
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
    "id": "hn:49769668",
    "domain": "金融",
    "title": "OpenAI and Anthropic oversold AI security breaches",
    "url": "https://nypost.com/2026/09/19/us-news/openai-anthropic-oversold-security-breaches-to-pressure-feds-into-protecting-turf-insiders/",
    "source": "hei-lima",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-09-19T19:59:28+00:00",
    "summary": ""
  },
  {
    "id": "hn:49924299",
    "domain": "金融",
    "title": "Sony released the first CD audio player on this day in 1982",
    "url": "https://www.tomshardware.com/pc-components/storage/sony-released-the-first-cd-audio-player-on-this-day-in-1982-player-cost-usd3-700-when-adjusted-for-inflation-but-it-would-be-another-decade-before-the-cd-rom-driven-multimedia-pc-era-began",
    "source": "Brajeshwar",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-10-01T17:07:39+00:00",
    "summary": ""
  }
]
```
