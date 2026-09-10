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

- 今日日期：`2026-09-10`
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
  "date": "2026-09-10",
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
    "points": 1884203,
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
    "points": 1839637,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1j9MP6wEV9",
    "domain": "AI",
    "title": "从零开始，学会让桌面Agent帮你干活！【小白教程】",
    "url": "http://www.bilibili.com/video/av116861865887789",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 1353850,
    "published_at": "2026-07-05T02:00:00+00:00",
    "summary": "用不上codex的朋友们！新的国产Agent直接上手，来跑通8大用法～\n感谢朋友们的三连+关注～"
  },
  {
    "id": "bvid:BV14rzQB9EJj",
    "domain": "AI",
    "title": "Claude Code 从 0 到 1 全攻略：MCP / SubAgent / Agent Skill / Hook / 图片 / 上下文处理/ 后台任务",
    "url": "http://www.bilibili.com/video/av115954889596221",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 1306440,
    "published_at": "2026-01-25T08:55:20+00:00",
    "summary": "时间戳如下，方便大家跳转观看：\n \n第一部分：环境搭建与基础交互\n- 01:09 安装 Claude Code\n- 01:43 登录与授权\n- 02:55 第一个实战问题\n- 03:12 三种模式详解 (默认/自动/规划)\n \n第二部分：复杂任务处理与终端控制\n- 06:00 执行终端命令 (Bash)\n- 06:49 使用规划模式 (Plan Mode)\n- 11:06 跳过所有权限检测 (da"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 1268506,
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
    "points": 1189717,
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
    "points": 883838,
    "published_at": "2025-05-01T09:00:00+00:00",
    "summary": "up的科学星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 780827,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 739020,
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
    "points": 669029,
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
    "points": 442138,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1ia9UBPESQ",
    "domain": "AI",
    "title": "在VScode中配置Claude Code并接入DeepSeek V4 Pro【oo唠嗑教程】",
    "url": "http://www.bilibili.com/video/av116487012549813",
    "source": "沉默的羔丸ovo",
    "platform": "bilibili",
    "points": 329449,
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
    "points": 285257,
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
    "points": 275259,
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
    "points": 258146,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 189241,
    "published_at": "2026-04-27T08:51:41+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n   喜欢视频课程的同学一键三连多多支持一下，长按点赞五秒=lv6大佬 可以的发送彩色弹幕哦。\n配套源码项目已打包评论区回复up"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 180977,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 167843,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 161934,
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
    "points": 155669,
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
    "points": 112585,
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
    "points": 93628,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1W9YH6HEtz",
    "domain": "AI",
    "title": "感谢这 100 万个 B 友，来一波私密问答吧！",
    "url": "http://www.bilibili.com/video/av117238430439027",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 84115,
    "published_at": "2026-09-09T03:50:00+00:00",
    "summary": "时隔 6 年，终于拥有 100 万个粉丝了，感谢大家的关注。\n作为一名 AI + 编程博主，真的非常荣幸，之后会给大家带来更多好玩又实用的 AI 编程知识。\n编程学习教程+实战项目+简历模板：codefather.cn\n免费 AI 编程教程：github.com/liyupi/ai-guide\n记得三连支持、关注鱼皮，让更多朋友学到知识哦~"
  },
  {
    "id": "bvid:BV143wwz6E8F",
    "domain": "AI",
    "title": "Claude code科研使用展示与思路分享（提速就靠Ai）",
    "url": "http://www.bilibili.com/video/av116211882920985",
    "source": "科研推土机",
    "platform": "bilibili",
    "points": 75116,
    "published_at": "2026-03-11T18:12:00+00:00",
    "summary": "本期给大家带来的是Claude在Vscode的科研应用演示与我最近的一些心得使用心得，科研速度嘎嘎提升。论文复现画图、数据分析就靠Claude code。这个课程也是科研推土机「系统管理文献课程2.0」学员催我更新的内容，希望能帮助到大家～，这个视频重点讲两个事情：\n1️⃣ 资料获取，free不用怀疑，我是良心可言博主，，关注我(GZTSHNR)～\n2️⃣ 展示如何在VS code实操应用clau"
  },
  {
    "id": "bvid:BV1XnuGzfEp7",
    "domain": "AI",
    "title": "让你手中的AI好用10倍！5个好玩实用的MCP推荐，让你不只会用AI搜索",
    "url": "http://www.bilibili.com/video/av114835262018810",
    "source": "田同学Tino",
    "platform": "bilibili",
    "points": 74461,
    "published_at": "2025-07-12T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1bjKkzPEEA",
    "domain": "AI",
    "title": "cursor+uniapp零基础开发工作报告小程序❗️30分钟保姆级教程",
    "url": "http://www.bilibili.com/video/av114756274947612",
    "source": "智码侃侃Tom",
    "platform": "bilibili",
    "points": 67194,
    "published_at": "2025-06-28T02:00:00+00:00",
    "summary": "这期视频我们将用AI完成前端开发+后端开发，并实现用户数据隔离的功能，让小程序达到可商用的标准，理论+实操+效果演示帮助零基础的同学快速上手。"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 54967,
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
    "points": 47783,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1vYFQzQE4P",
    "domain": "AI",
    "title": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！Claude Code Hooks回调+Agent Teams全自动开发零轮询",
    "url": "http://www.bilibili.com/video/av116046157647899",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 47684,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1ZWYAzuEKN",
    "domain": "AI",
    "title": "MC服务器管理？一个服务端插件就够了",
    "url": "http://www.bilibili.com/video/av115172383395362",
    "source": "Norcleeh",
    "platform": "bilibili",
    "points": 45349,
    "published_at": "2025-09-09T04:12:51+00:00",
    "summary": "欢迎使用OPanel！这是一个以插件/模组形式存在的Minecraft服务器管理面板，开箱即用、简洁美观。\n\nGithub仓库：https://github.com/opanel-mc/opanel\n目前尚未发布正式版本，欢迎各位使用、测试、反馈、贡献，为项目仓库点亮star！\n正式版发布后将会上传至各大模组平台\n若有其他问题，欢迎在项目仓库内提出issue"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operitAI教程：入门安卓最强大ai平台",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 42100,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1FzfoYSE4f",
    "domain": "AI",
    "title": "影刀AI Power零基础教程：02 智能体——打造企业AI超级员工",
    "url": "http://www.bilibili.com/video/av113888003622214",
    "source": "影刀RPA",
    "platform": "bilibili",
    "points": 41692,
    "published_at": "2025-02-06T02:00:00+00:00",
    "summary": "AI智能体：场景化智能助手，打造企业AI超级员工\n影刀AI Power，帮助企业将AI用起来。让每个员工都能拥有AI能力，在工作中使用AI解决问题。\n\n影刀AP企业版免费试用申请：http://s.winrobot360.com/g02tp\n影刀AP社区版使用：https://www.yingdao.com/ai-power/"
  },
  {
    "id": "bvid:BV1VL3F6pE9K",
    "domain": "AI",
    "title": "0基础入门智能体agent测试：AI测试基础+AI智能体(Agent)测试从零入门全攻略，2026最新版！",
    "url": "http://www.bilibili.com/video/av116991151113881",
    "source": "黑马测试",
    "platform": "bilibili",
    "points": 39893,
    "published_at": "2026-07-27T09:19:37+00:00",
    "summary": "还在卷传统软件测试？2026年必学的AI智能体(Agent)测试来了！本期视频专为0基础小白打造，从软件测试基础讲起...若要本视频配套资源笔记可加up主企微（请看置顶留言最后一句话）。"
  },
  {
    "id": "bvid:BV1XiD5BQEAj",
    "domain": "AI",
    "title": "Claude Code 接入微信、一行命令把Claude Code装进微信、保姆级教程、微信支持Claude Code（cc-connect）远程开发",
    "url": "http://www.bilibili.com/video/av116350093694897",
    "source": "下班学AI",
    "platform": "bilibili",
    "points": 39709,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 30545,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29725,
    "published_at": "2025-07-16T13:10:54+00:00",
    "summary": "Cursor用不了？三款AI编程工具完美代替Cursor\naugmentCode\nTrae\nKiro"
  },
  {
    "id": "bvid:BV1WtoTBiEuR",
    "domain": "AI",
    "title": "Claude Code多Agent模式实战分享",
    "url": "http://www.bilibili.com/video/av116454666012312",
    "source": "Simon林_",
    "platform": "bilibili",
    "points": 25568,
    "published_at": "2026-04-23T15:18:08+00:00",
    "summary": "Claude Code有2种多Agent模式：多个subagents模式和多个独立agent模式"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22768,
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
    "points": 21641,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV188UHYkEdg",
    "domain": "AI",
    "title": "Cursor / Windsurf + Android Studio 高效AI编程：零基础也能开发安卓应用",
    "url": "http://www.bilibili.com/video/av113502647750313",
    "source": "kate人不错",
    "platform": "bilibili",
    "points": 21144,
    "published_at": "2024-11-18T07:04:36+00:00",
    "summary": "欢迎关注我的知识星球：https://t.zsxq.com/FF0He\n\n我会分享最新AI资讯、源代码、回答你的提问。\n\n视频亮点：\n\n双工具对比：解析 Cursor 和 Windsurf 各自优势\n实战案例：从五子棋到卡路里计算AI应用的完整开发过程\n专业部署：Android Studio 配置与构建技巧\n\n时间戳：\n\n0:00 - 引言\n\n0:26 - 我开发的应用演示\n\n2:33 - Rea"
  },
  {
    "id": "bvid:BV1eMgG6QEeG",
    "domain": "AI",
    "title": "【吴恩达】这绝对是把《Vibe Coding》讲得最通透的一套课！手把手教你构建自己的企业级AI工作流，学完直接落地！——附带课件代码",
    "url": "http://www.bilibili.com/video/av117081815189025",
    "source": "吴恩达Agents",
    "platform": "bilibili",
    "points": 19913,
    "published_at": "2026-08-12T09:29:57+00:00",
    "summary": "Vibe Coding火了，但你会发现——AI写的代码像开盲盒，今天能跑明天崩，项目一大就乱套。\n规范驱动开发（SDD） 就是来解决这个问题的。它的核心理念很简单：在让AI写代码之前，先和AI在统一的规范文档里对齐需求，把开发变成可预测、可追溯、可控制的过程。"
  },
  {
    "id": "bvid:BV1iDRQBrEF6",
    "domain": "AI",
    "title": "Claude + Blender 现在太强了 —— 完整免费设置",
    "url": "http://www.bilibili.com/video/av116543333601720",
    "source": "设计之道",
    "platform": "bilibili",
    "points": 16836,
    "published_at": "2026-05-09T07:11:36+00:00",
    "summary": "【简介】\nAnthropic 刚刚发布了用于创意工具的官方 Claude Connectors —— 其中 Blender 连接器对 3D 艺术家来说最重要。在本视频中，我将展示最佳的 Claude + Blender 免费设置，以及为什么这次更新可能会改变我们构建 3D 场景的方式。\n\n【你将学到】\n01:13 步骤 1：安装 Blender MCP 和 Claude Code\n02:31 步骤"
  },
  {
    "id": "bvid:BV18TZYY8EuJ",
    "domain": "AI",
    "title": "微软最新AI Agent入门课程 • 中英",
    "url": "http://www.bilibili.com/video/av114246130076146",
    "source": "Mindofuture",
    "platform": "bilibili",
    "points": 16101,
    "published_at": "2025-03-30T02:06:00+00:00",
    "summary": "在这门包含10节课的课程中，我们将带你从概念到代码，全面覆盖构建AI代理的基础知识。在这里找到完整的“AI代理入门”课程及代码示例\nhttps://github.com/microsoft/ai-agents-for-beginners\n\nP01 什么是AI代理\nP02 使用哪种AI代理框架\nP03 如何设计优秀的AI代理\nP04 什么是代理工具使用设计模式\nP05 什么是代理式RAG\nP06 如"
  },
  {
    "id": "bvid:BV1JgVq6ME6v",
    "domain": "AI",
    "title": "超详细Claude Code+Harness教程",
    "url": "http://www.bilibili.com/video/av116679111610655",
    "source": "知了传课",
    "platform": "bilibili",
    "points": 13911,
    "published_at": "2026-06-02T06:33:18+00:00",
    "summary": "面向2026最新版超详细Claude Code+Harness教程，保姆级教程，高效AI编程技巧。资料领取请关注置顶评论。"
  },
  {
    "id": "bvid:BV1dogD6aERB",
    "domain": "AI",
    "title": "2026年医学生必看的【AI+医学】最强教程来了（学习路线+完整教程）手把手教你医学方向如何结合AI搞定论文和项目！",
    "url": "http://www.bilibili.com/video/av116968686359676",
    "source": "迪哥AI大讲堂-",
    "platform": "bilibili",
    "points": 10976,
    "published_at": "2026-07-23T17:38:08+00:00",
    "summary": "迪哥给大家准备了医学人工智能学习资料包，可在评论区获取！\n包含：\n1、上百篇医学方向人工智能顶会论文+源码\n2、90+各种疾病医疗数据集\n3、人工智能医学领域经典实战项目\n4、医学生必备的学习路线图"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 10433,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 10083,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1xh3C6cEGv",
    "domain": "AI",
    "title": "两周完成一篇SCI论文，用claude code帮你干",
    "url": "http://www.bilibili.com/video/av117002408559933",
    "source": "博士大师兄木水",
    "platform": "bilibili",
    "points": 9807,
    "published_at": "2026-07-29T08:53:04+00:00",
    "summary": "大师兄八股文SCI速成模板已制作成skill，手把手带你实现一键生成SCI论文初稿"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 9503,
    "published_at": "2025-04-14T02:30:00+00:00",
    "summary": "MCP服务网站：https://smithery.ai/\nCherry Studio官方网站：https://cherry-ai.com/"
  },
  {
    "id": "bvid:BV12MEg6pE9o",
    "domain": "AI",
    "title": "【乐鑫教程】乐鑫文档 MCP 服务器上线，现已支持微信登录！",
    "url": "http://www.bilibili.com/video/av116713957956440",
    "source": "乐鑫信息科技",
    "platform": "bilibili",
    "points": 9178,
    "published_at": "2026-06-08T10:17:31+00:00",
    "summary": "手把手教你如何使用最新乐鑫文档知识库，帮你在 Claude / Cursor 等平台解答问题、生成代码、迁移 ESP-IDF 版本、烧录固件。 MCP 服务器现已支持微信扫码一键登录，快来一试！\n\n视频重点内容包括👇：\n\n- 如何将 MCP 服务器添加到 VS Code\n- 让 Copilot 基于乐鑫文档对比旧版和最新版 I2C 驱动\n- 驱动迁移\n- Copilot 编译代码、烧录代码并监控输"
  },
  {
    "id": "hn:49548952",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia to acquire Hugging Face",
    "url": "https://www.cnbc.com/2026/09/03/nvidia-agrees-to-buy-hugging-face-for-almost-13-billion-ai-expansion.html",
    "source": "tosh",
    "platform": "hackernews",
    "points": 329,
    "published_at": "2026-09-03T12:10:33+00:00",
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
    "id": "hn:49567357",
    "domain": "AI 算力 / 半导体",
    "title": "Georgi Gerganov on llama.cpp/ggml future after Nvidia acquisition of HuggingFace",
    "url": "https://twitter.com/ggerganov/status/2095897173376618881",
    "source": "theanonymousone",
    "platform": "hackernews",
    "points": 76,
    "published_at": "2026-09-04T17:12:22+00:00",
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
    "id": "hn:49594189",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's Jensen Huang says 'AGI has arrived' and congratulates OpenAI",
    "url": "https://www.businessinsider.com/nvidia-jensen-huang-agi-openai-astra-ai-2026-9",
    "source": "vinni2",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-09-07T05:23:31+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/cincon-high-performance-power-modules-for-edge-ai-ipcs/",
    "domain": "AI 算力 / 半导体",
    "title": "Cincon High-Performance Power Modules for Edge AI & IPCs",
    "url": "https://www.eetimes.com/cincon-high-performance-power-modules-for-edge-ai-ipcs/",
    "source": "Cincon Elctronics Co., Ltd.",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T08:00:00+00:00",
    "summary": "As AI moves to the edge, IPCs demand compact, rugged power. Cincon offers baseplate-cooled DC-DC &#038; AC-DC solutions for fanless, harsh AIoT environments. The post Cincon High-Performance Power Mod"
  },
  {
    "id": "rss:https://www.eetimes.com/leds-push-wireless-power-further/",
    "domain": "AI 算力 / 半导体",
    "title": "LEDs Push Wireless Power Further",
    "url": "https://www.eetimes.com/leds-push-wireless-power-further/",
    "source": "Rebecca Pool",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T20:00:00+00:00",
    "summary": "An LED alternative to laser wireless power transfer from the Institute of Science Tokyo uses adaptive optics and AI beam steering to charge indoor IoT devices 5 meters away. The post LEDs Push Wireles"
  },
  {
    "id": "rss:https://www.eetimes.com/the-hardware-assisted-verification-imperative/",
    "domain": "AI 算力 / 半导体",
    "title": "The Hardware-assisted Verification Imperative",
    "url": "https://www.eetimes.com/the-hardware-assisted-verification-imperative/",
    "source": "Juergen Jaeger, Siemens EDA",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T12:00:00+00:00",
    "summary": "Read why today’s IC system projects for applications like AI and superscalar acceleration require the most comprehensive HAV solutions and methodologies. The post The Hardware-assisted Verification Im"
  },
  {
    "id": "rss:https://www.eetimes.com/biwin-brings-storage-solutions-for-ai-era-at-embedded-world-na-2026/",
    "domain": "AI 算力 / 半导体",
    "title": "BIWIN Brings Storage Solutions for AI Era at embedded world NA 2026",
    "url": "https://www.eetimes.com/biwin-brings-storage-solutions-for-ai-era-at-embedded-world-na-2026/",
    "source": "BIWIN STORAGE TECHNOLOGY CO., LTD.",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T12:00:00+00:00",
    "summary": "Visit BIWIN at Booth #6104 during embedded world NA 2026 to explore eSSDs, embedded memory, and industrial storage built for cloud and edge applications. The post BIWIN Brings Storage Solutions for AI"
  },
  {
    "id": "rss:https://www.eetimes.com/bridging-the-hpc-software-gap-for-practical-quantum-computing/",
    "domain": "AI 算力 / 半导体",
    "title": "Bridging the HPC Software Gap for Practical Quantum Computing",
    "url": "https://www.eetimes.com/bridging-the-hpc-software-gap-for-practical-quantum-computing/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T12:00:00+00:00",
    "summary": "HPC centers must address the infrastructure bottleneck to integrate quantum systems and unlock their full potential. The post Bridging the HPC Software Gap for Practical Quantum Computing appeared fir"
  },
  {
    "id": "rss:https://www.eetimes.com/quantum-scaling-is-becoming-a-control-electronics-problem/",
    "domain": "AI 算力 / 半导体",
    "title": "Quantum Scaling Is Becoming a Control-Electronics Problem",
    "url": "https://www.eetimes.com/quantum-scaling-is-becoming-a-control-electronics-problem/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T08:05:43+00:00",
    "summary": "Too many wires, too much heat, and too much latency are forcing quantum control electronics deeper into the cold. The post Quantum Scaling Is Becoming a Control-Electronics Problem appeared first on E"
  },
  {
    "id": "rss:https://www.eetimes.com/strategy-paper-urges-canada-to-add-semiconductors-to-ai-strategy/",
    "domain": "AI 算力 / 半导体",
    "title": "Strategy Paper Urges Canada to Add Semiconductors to AI Strategy",
    "url": "https://www.eetimes.com/strategy-paper-urges-canada-to-add-semiconductors-to-ai-strategy/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T19:00:00+00:00",
    "summary": "Canada’s sovereign AI ambitions will fall short unless procurement, talent, funding, and existing semiconductor strengths are aligned behind domestic hardware capability. The post Strategy Paper Urges"
  },
  {
    "id": "rss:https://www.eetimes.com/the-pragmatic-path-to-achieving-cra-compliance-and-securing-your-access-to-the-eu-market/",
    "domain": "AI 算力 / 半导体",
    "title": "The Pragmatic Path to Achieving CRA Compliance and Securing Your Access to the EU Market",
    "url": "https://www.eetimes.com/the-pragmatic-path-to-achieving-cra-compliance-and-securing-your-access-to-the-eu-market/",
    "source": "MediaTek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T14:39:23+00:00",
    "summary": "As the EU Cyber Resilience Act (CRA) approaches, IoT manufacturers face stringent cybersecurity requirements across the entire product lifecycle. MediaTek, together with our strategic partners, invite"
  },
  {
    "id": "rss:https://www.eetimes.com/the-security-ai-that-learns-the-language-of-movement/",
    "domain": "AI 算力 / 半导体",
    "title": "The Security AI That Learns the Language of Movement",
    "url": "https://www.eetimes.com/the-security-ai-that-learns-the-language-of-movement/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T13:15:17+00:00",
    "summary": "UNC Charlotte researchers use edge AI to learn normal motion, predict what comes next, and flag anomalies for human review. The post The Security AI That Learns the Language of Movement appeared first"
  },
  {
    "id": "rss:https://www.eetimes.com/powering-high-precision-lasers/",
    "domain": "AI 算力 / 半导体",
    "title": "Powering High Precision Lasers",
    "url": "https://www.eetimes.com/powering-high-precision-lasers/",
    "source": "P-DUKE",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T13:00:00+00:00",
    "summary": "Today, no one can imagine life without the vast number of laser applications, ranging from milliwatt-class lasers to high-power processing. The post Powering High Precision Lasers appeared first on EE"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/apple-a20-pro-powers-iphone-18-pro-the-companys-first-2-nanometer-smartphone-chip",
    "domain": "AI 算力 / 半导体",
    "title": "Apple A20 Pro powers iPhone Duo, 18 Pro — the company's first 2-nanometer smartphone chip",
    "url": "https://www.tomshardware.com/pc-components/cpus/apple-a20-pro-powers-iphone-18-pro-the-companys-first-2-nanometer-smartphone-chip",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T17:33:21+00:00",
    "summary": "Apple's new A20 Pro SOC will power the iPhone 18 Pro and iPhone Duo as its first 2 nm smartphone chip."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/handheld-gaming/switch-2-zelda-40th-anniversary-edition-preorders-hit-usd1-000-on-ebay-amazon-and-walmart-are-your-last-shot-at-usd520-msrp",
    "domain": "AI 算力 / 半导体",
    "title": "Switch 2 Zelda 40th Anniversary Edition preorders open on Amazon for $519.99 — here's your last shot to grab the limited-edition console at MSRP",
    "url": "https://www.tomshardware.com/video-games/handheld-gaming/switch-2-zelda-40th-anniversary-edition-preorders-hit-usd1-000-on-ebay-amazon-and-walmart-are-your-last-shot-at-usd520-msrp",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T17:06:03+00:00",
    "summary": "Scalpers have started selling preorders of the Nintendo Switch 2 The Legend of Zelda 40th Anniversary Edition on eBay, starting at $700."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-backed-auto-overclocking-tool-hypertune-optimizes-individual-systems-not-test-profiles-tool-claims-fps-improvement-of-up-to-60-percent-on-intel-based-systems",
    "domain": "AI 算力 / 半导体",
    "title": "Intel-backed auto-overclocking tool Hypertune optimizes individual systems, not test profiles — tool claims FPS improvement of up to 60% on Intel-based systems",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-backed-auto-overclocking-tool-hypertune-optimizes-individual-systems-not-test-profiles-tool-claims-fps-improvement-of-up-to-60-percent-on-intel-based-systems",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T16:03:05+00:00",
    "summary": "Hypertune is an automated overclocking tool built on top of Intel's Extreme Tuning Utility (XTU) SDK and built in collaboration with engineers at Intel."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/framework-cuts-32gb-and-64gb-memory-prices-for-new-laptop-13-pro-issues-retroactive-refunds-modular-laptop-maker-secures-limited-quantity-of-lpcamm2-ram-at-lower-cost",
    "domain": "AI 算力 / 半导体",
    "title": "Framework cuts 32GB and 64GB memory prices for new Laptop 13 Pro, issues retroactive refunds — modular laptop maker secures 'limited quantity' of LPCAMM2 RAM at lower cost",
    "url": "https://www.tomshardware.com/laptops/framework-cuts-32gb-and-64gb-memory-prices-for-new-laptop-13-pro-issues-retroactive-refunds-modular-laptop-maker-secures-limited-quantity-of-lpcamm2-ram-at-lower-cost",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T15:00:00+00:00",
    "summary": "Modular laptop maker Framework is dropping some of its memory pricing, including for some already-shipped orders, in a piece of good news for consumers."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/microsoft-reportedly-gives-secret-xbox-game-pass-discounts-to-churned-subscribers-to-reel-them-back-in-targeted-offers-slash-up-to-30-percent-off-the-regular-price",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft reportedly gives secret Xbox Game Pass discounts to churned subscribers to reel them back in — targeted offers slash up to 30% off the regular price",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/microsoft-reportedly-gives-secret-xbox-game-pass-discounts-to-churned-subscribers-to-reel-them-back-in-targeted-offers-slash-up-to-30-percent-off-the-regular-price",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T14:39:23+00:00",
    "summary": "Microsoft appears to be using dynamic pricing to push select users to commit to Xbox Game Pass."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-says-its-next-generation-processors-could-be-made-at-samsung-double-sourcing-with-tsmc-hints-at-massive-volume-requirements",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI says its next-generation processors could be made at Samsung — double-sourcing with TSMC hints at massive volume requirements",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-says-its-next-generation-processors-could-be-made-at-samsung-double-sourcing-with-tsmc-hints-at-massive-volume-requirements",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T14:30:00+00:00",
    "summary": "OpenAI deepens chip cooperation with Samsung, possibly prepares to Double source AI ASICs from two foundries in a bid to get more in-house silicon to its data centers."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/save-40-percent-on-autodesks-media-and-entertainment-collection-thousands-of-dollars-worth-of-software-in-a-single-bundle",
    "domain": "AI 算力 / 半导体",
    "title": "Save 40% on Autodesk’s Media and Entertainment Collection — thousands of dollars worth of software in a single bundle",
    "url": "https://www.tomshardware.com/pc-components/save-40-percent-on-autodesks-media-and-entertainment-collection-thousands-of-dollars-worth-of-software-in-a-single-bundle",
    "source": "Sponsored",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T13:33:15+00:00",
    "summary": "Autodesk is offering a 40% discount on its Media and Entertainment Collection for a limited time."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/goodram-px700-2tb-ssd-review",
    "domain": "AI 算力 / 半导体",
    "title": "Goodram PX700 2TB SSD Review: High-end punch on a budget core",
    "url": "https://www.tomshardware.com/pc-components/ssds/goodram-px700-2tb-ssd-review",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T12:34:37+00:00",
    "summary": "The Goodram PX700 matches good all-around performance with high power-efficiency in a cool-running package. It performs mostly like a premium drive, although pricing remains a concern."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/openais-breakthrough-solution-for-the-elusive-navier-stokes-problem-overshadowed-by-plagiarism-controversy-researcher-says-openai-scraped-codex-session-and-issued-career-threats",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI's breakthrough solution for the elusive Navier-Stokes problem overshadowed by plagiarism controversy — researcher says OpenAI scraped Codex session and issued career threats",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/openais-breakthrough-solution-for-the-elusive-navier-stokes-problem-overshadowed-by-plagiarism-controversy-researcher-says-openai-scraped-codex-session-and-issued-career-threats",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T12:30:00+00:00",
    "summary": "OpenAI announced that a team using one of its internal frontier models has solved the Navier-Stokes problem. However, the announcement has been mired in controversy."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/lg-strongly-denies-tv-security-claims-says-tracking-and-snooping-concerns-not-true-online-investigation-claims-216-000-000-spy-tvs-record-audio",
    "domain": "AI 算力 / 半导体",
    "title": "LG strongly denies TV spying claims, says tracking and snooping concerns 'not true' — online investigation claims 216,000,000 TVs spy and record audio",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/lg-strongly-denies-tv-security-claims-says-tracking-and-snooping-concerns-not-true-online-investigation-claims-216-000-000-spy-tvs-record-audio",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T11:50:18+00:00",
    "summary": "LG has strongly denied recent security and privacy concerns raised regarding its smart TVs."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/nintendo/nintendo-unveils-the-legend-of-zelda-40th-anniversary-switch-2-for-usd520-first-ever-special-edition-switch-2-drops-october-19-alongside-usd100-pro-controller-pre-orders-live",
    "domain": "AI 算力 / 半导体",
    "title": "Nintendo unveils The Legend of Zelda 40th Anniversary Switch 2 for $520 — First-ever special-edition Switch 2 drops October 19, alongside $100 Pro Controller, pre-orders live",
    "url": "https://www.tomshardware.com/video-games/nintendo/nintendo-unveils-the-legend-of-zelda-40th-anniversary-switch-2-for-usd520-first-ever-special-edition-switch-2-drops-october-19-alongside-usd100-pro-controller-pre-orders-live",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T11:40:00+00:00",
    "summary": "Nintendo is releasing its first-ever limited-edition Switch 2 to commemorate Zelda's 40th anniversary and it will cost $520. It does not come with Ocarina of Time, but you can purchase a similarly-the"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-claims-gpt-6-astra-is-an-ethereal-alien-mind-with-agi-like-qualities-company-warns-of-alignment-challenges-as-new-frontier-leader-emerges",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI claims GPT-6 Astra is an ethereal 'Alien Mind' with AGI-like qualities — company warns of alignment challenges as new frontier leader emerges",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-claims-gpt-6-astra-is-an-ethereal-alien-mind-with-agi-like-qualities-company-warns-of-alignment-challenges-as-new-frontier-leader-emerges",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T11:20:00+00:00",
    "summary": "OpenAI has made bold claims with its new GPT-6 Astra AI model, and it's certainly capable, but benchmarks suggest it has many of the usual weaknesses alongside the strengths, while cost and accessibil"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/this-usd502-4tb-crucial-t705-is-the-cheapest-gen-5-ssd-you-can-buy-right-now-for-just-12-5-cents-per-gb-ultra-fast-storage-upgrade-with-unreal-14-500-mb-s-speeds-is-usd181-less-than-a-month-ago-hitting-its-lowest-price-since-february",
    "domain": "AI 算力 / 半导体",
    "title": "This $502 4TB Crucial T705 is the cheapest Gen 5 SSD you can buy right now for just 12.5 cents per GB — ultra-fast storage upgrade with unreal 14,500 MB/s speeds is $181 less than a month ago, hitting",
    "url": "https://www.tomshardware.com/pc-components/ssds/this-usd502-4tb-crucial-t705-is-the-cheapest-gen-5-ssd-you-can-buy-right-now-for-just-12-5-cents-per-gb-ultra-fast-storage-upgrade-with-unreal-14-500-mb-s-speeds-is-usd181-less-than-a-month-ago-hitting-its-lowest-price-since-february",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T11:05:46+00:00",
    "summary": "Save 10% on this 4TB Crucial T705 SSD, the cheapest Gen 5 4TB SSD on the market by some distance at the moment, now just $502.51."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/power-supplies/phanteks-amp-gh-750w-power-supply-review",
    "domain": "AI 算力 / 半导体",
    "title": "Phanteks AMP GH 750W power supply review: Great buy at sub-$90 street pricing, but comes with a 450W cap on its 12V-2x6 connector",
    "url": "https://www.tomshardware.com/pc-components/power-supplies/phanteks-amp-gh-750w-power-supply-review",
    "source": "E. Fylladitakis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T11:05:00+00:00",
    "summary": "Phanteks' mainstream ATX 3.1 line, with Japanese capacitors, an 8-year warranty, and street pricing under $90, but with a 450W cap on its 12V-2x6 connector."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidias-unreleased-rtx-3070-ti-16gb-comes-to-life-thanks-to-a-modders-crazy-gddr6-swap-frankenstein-card-combines-rtx-3070-pcb-and-new-vram-with-rtx-3070-ti-gpu",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's unreleased RTX 3070 Ti 16GB comes to life thanks to a modder's crazy GDDR6 swap — Frankenstein card combines RTX 3070 PCB and new VRAM with RTX 3070 Ti GPU",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidias-unreleased-rtx-3070-ti-16gb-comes-to-life-thanks-to-a-modders-crazy-gddr6-swap-frankenstein-card-combines-rtx-3070-pcb-and-new-vram-with-rtx-3070-ti-gpu",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T11:00:00+00:00",
    "summary": "A modder has recreated the never-released RTX 3070 Ti with 16GB of VRAM using GDDR6 chips instead of the GDDR6X the retail 3070 Ti actually shipped with."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/researcher-reconstructs-infamous-stuxnet-malware-source-code-attack-targeted-iranian-nuclear-facilities-and-was-the-first-software-of-its-type-to-cause-physical-damage",
    "domain": "AI 算力 / 半导体",
    "title": "Researcher reverse-engineers infamous Stuxnet malware source code, publishes it on Github for all — attack targeted Iranian nuclear facilities and was the first software of its type to cause physical ",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/researcher-reconstructs-infamous-stuxnet-malware-source-code-attack-targeted-iranian-nuclear-facilities-and-was-the-first-software-of-its-type-to-cause-physical-damage",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T10:30:00+00:00",
    "summary": "An anonymous security researcher has reconstructed the source code of the infamous Stuxnet worm, which was built to subtly interfere with Iranian uranium enrichment during the Bush and Obama administr"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/glacier-strewn-patagonia-pitches-for-mega-data-center-business-coldness-and-energy-resources-a-plus-but-poor-connectivity-issues-need-to-be-resolved",
    "domain": "AI 算力 / 半导体",
    "title": "Big Tech eyes glacier-strewn Patagonia for building mega AI data centers — region offers 17,300 glaciers, coldness, and cheap energy, but fiber lines are scarce",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/glacier-strewn-patagonia-pitches-for-mega-data-center-business-coldness-and-energy-resources-a-plus-but-poor-connectivity-issues-need-to-be-resolved",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T10:00:00+00:00",
    "summary": "Patagonia, a region of Argentina with 17,300 glaciers has the potential to turn into a data center hotspot."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/more-than-10-percent-chance-ai-could-kill-all-humans-in-the-next-10-years-anthropic-safety-researcher-says-departing-employee-says-ai-companies-are-gambling-with-our-lives",
    "domain": "AI 算力 / 半导体",
    "title": "More than 10% chance AI 'could kill all humans' in the next 10 years, Anthropic safety researcher says — departing employee says AI companies are 'gambling with our lives'",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/more-than-10-percent-chance-ai-could-kill-all-humans-in-the-next-10-years-anthropic-safety-researcher-says-departing-employee-says-ai-companies-are-gambling-with-our-lives",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T09:26:28+00:00",
    "summary": "Anthropic AI safety researcher has warned there's a more than 10% chance AI could kill all humans."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/tsmc-to-start-using-high-na-euv-lithography-in-2030-a10-or-a11-technology-prime-candidates-for-use",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC to start using High-NA EUV lithography in 2030 — A10 or A11 technology prime candidates for use",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/tsmc-to-start-using-high-na-euv-lithography-in-2030-a10-or-a11-technology-prime-candidates-for-use",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T15:00:00+00:00",
    "summary": "TSMC discloses plans to use High-NA EUV lithography in 2030, 6×12-inch photomasks with new scanners in 2033."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-reportedly-set-to-hike-cpu-prices-by-10-percent-ahead-of-major-annual-product-launch-in-march-2027-report-says-amd-will-follow-up-between-june-and-july",
    "domain": "AI 算力 / 半导体",
    "title": "Intel reportedly set to hike CPU prices by 10% ahead of 'major annual product' launch in March 2027 — report says AMD will follow up between June and July",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-reportedly-set-to-hike-cpu-prices-by-10-percent-ahead-of-major-annual-product-launch-in-march-2027-report-says-amd-will-follow-up-between-june-and-july",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T14:18:42+00:00",
    "summary": "Intel is reportedly set to raise CPU prices by 10%, following two other price increases, as it prepares for a major product launch in March 2027."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/benchmarking-qwen-3-8-27b-on-rtx-5090-and-beyond-vram-capacity-alone-cant-overcome-severe-software-and-inference-engine-bottlenecks",
    "domain": "AI 算力 / 半导体",
    "title": "Benchmarking Qwen 3.8 27B on RTX 5090 and beyond — VRAM capacity alone can't overcome severe software and inference engine bottlenecks",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/benchmarking-qwen-3-8-27b-on-rtx-5090-and-beyond-vram-capacity-alone-cant-overcome-severe-software-and-inference-engine-bottlenecks",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T13:30:02+00:00",
    "summary": "Following the release of Qwen 3.8 27B, we put our trusty hardware to the test to see which hardware might be best suited for running this open-weight AI model."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/super-smash-bros-melee-gets-fully-decompiled-after-over-six-years-of-effort-ambitious-and-technically-impressive-project-delivers-gamecube-classic-as-c-code",
    "domain": "AI 算力 / 半导体",
    "title": "Super Smash Bros Melee gets fully decompiled after over six years of effort — ambitious and technically impressive project delivers GameCube classic as C code",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/super-smash-bros-melee-gets-fully-decompiled-after-over-six-years-of-effort-ambitious-and-technically-impressive-project-delivers-gamecube-classic-as-c-code",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T12:57:45+00:00",
    "summary": "A Super Smash Bros Melee decompilation project hit its key long-standing goal a few hours ago."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/sony-threatens-to-cut-off-customer-support-and-pursue-legal-action-over-harassment-as-backlash-to-playstations-physical-disc-phaseout-intensifies-company-to-move-forward-with-no-disc-decision-despite-several-lawsuits",
    "domain": "AI 算力 / 半导体",
    "title": "Sony threatens to cut off customer support and pursue legal action over harassment as backlash to PlayStation’s physical-disc phaseout intensifies — company to move forward with no disc decision despi",
    "url": "https://www.tomshardware.com/video-games/playstation/sony-threatens-to-cut-off-customer-support-and-pursue-legal-action-over-harassment-as-backlash-to-playstations-physical-disc-phaseout-intensifies-company-to-move-forward-with-no-disc-decision-despite-several-lawsuits",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T12:20:00+00:00",
    "summary": "Sony Japan has introduced a customer-harassment policy as anger continues over PlayStation’s plan to phase out physical game discs by 2028."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/all-in-one-dlss-unlocked-mod-brings-dlss-5-and-multi-frame-gen-to-rtx-20-30-and-40-series-hybrid-tool-taps-amd-fsr-3-1-to-boost-frame-rates-up-to-6x",
    "domain": "AI 算力 / 半导体",
    "title": "All-in-one 'DLSS Unlocked' mod brings DLSS 5 and multi-frame gen to RTX 20, 30, and 40 series — hybrid tool taps AMD FSR 3.1 to boost frame rates up to 6X",
    "url": "https://www.tomshardware.com/pc-components/gpus/all-in-one-dlss-unlocked-mod-brings-dlss-5-and-multi-frame-gen-to-rtx-20-30-and-40-series-hybrid-tool-taps-amd-fsr-3-1-to-boost-frame-rates-up-to-6x",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T12:00:00+00:00",
    "summary": "Performance for the mod remains untested but just the sheer utility of DLSS Unlocked easily puts it at the top of the RTX GPUs mod list. It combines OptiScaler_DLSSNR with DLSS Enabled to bring neural"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/quantum-computing/nec-has-quietly-quit-quantum-computing-hardware-development-report-claims-company-says-it-will-continue-to-evaluate-practical-applications-and-industrialization-of-quantum-technologies",
    "domain": "AI 算力 / 半导体",
    "title": "NEC has quietly quit quantum computing hardware development, report claims — company says it will continue to evaluate practical applications and industrialization of quantum technologies",
    "url": "https://www.tomshardware.com/tech-industry/quantum-computing/nec-has-quietly-quit-quantum-computing-hardware-development-report-claims-company-says-it-will-continue-to-evaluate-practical-applications-and-industrialization-of-quantum-technologies",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T11:45:00+00:00",
    "summary": "NEC reportedly quits development of quantum computers, but plans to explore practical applications for such systems."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/vintage-emulator-studio-recreates-44-legendary-synths-down-to-the-chip-level-free-mame-powered-component-level-emulation-should-offer-exceedingly-accurate-sound",
    "domain": "AI 算力 / 半导体",
    "title": "Vintage Emulator Studio recreates 44 legendary synths down to the chip level — free MAME-powered component-level emulation should offer exceedingly accurate sound",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/vintage-emulator-studio-recreates-44-legendary-synths-down-to-the-chip-level-free-mame-powered-component-level-emulation-should-offer-exceedingly-accurate-sound",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T11:40:00+00:00",
    "summary": "Vintage Emulator Studio brings iconic vintage synths and samplers to life — MAME-powered component-level emulation should offer exceedingly accurate sound"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cryptocurrency/hackers-drain-usd320-million-in-bitcoin-from-liquid-network-emptying-roughly-95-percent-of-federation-wallet-attackers-claim-theyre-the-good-guys-and-will-return-funds-after-the-vulnerability-is-fixed",
    "domain": "AI 算力 / 半导体",
    "title": "Hackers drain $320 million in Bitcoin from Liquid Network, emptying roughly 95% of federation wallet — attackers claim they’re the ‘good guys’ and will return funds after the vulnerability is fixed",
    "url": "https://www.tomshardware.com/tech-industry/cryptocurrency/hackers-drain-usd320-million-in-bitcoin-from-liquid-network-emptying-roughly-95-percent-of-federation-wallet-attackers-claim-theyre-the-good-guys-and-will-return-funds-after-the-vulnerability-is-fixed",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T11:20:00+00:00",
    "summary": "Hackers claiming to be white hats drained about $320 million in Bitcoin from Liquid Network’s federation wallet, promising to return the funds after the platform fixes the underlying bug"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/programming/google-maps-entire-brain-and-central-nervous-system-of-adult-male-fruit-fly-software-engineers-immediately-make-it-run-doom-ai-powered-3d-model-of-over-166-000-neurons-can-also-play-super-mario-64",
    "domain": "AI 算力 / 半导体",
    "title": "Google maps entire brain and central nervous system of adult male fruit fly, software engineers immediately make it run Doom — AI-powered 3D model of over 166,000 neurons can also play Super Mario 64",
    "url": "https://www.tomshardware.com/software/programming/google-maps-entire-brain-and-central-nervous-system-of-adult-male-fruit-fly-software-engineers-immediately-make-it-run-doom-ai-powered-3d-model-of-over-166-000-neurons-can-also-play-super-mario-64",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T11:06:26+00:00",
    "summary": "Scientists mapped the complete brain and central nervous system of an adult male fruit fly for the first time. Days later the full MaleCNS v1.0 fruit fly connectome was being trained to play Doom and "
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/get-a-32gb-ddr5-gaming-pc-for-just-usd1-379-at-newegg-usd420-discount-includes-20-core-intel-cpu-and-rtx-5060",
    "domain": "AI 算力 / 半导体",
    "title": "Get a 32GB DDR5 gaming PC for just $1,379 at Newegg — $420 discount includes 20-core Intel CPU and RTX 5060",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/get-a-32gb-ddr5-gaming-pc-for-just-usd1-379-at-newegg-usd420-discount-includes-20-core-intel-cpu-and-rtx-5060",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T11:02:34+00:00",
    "summary": "Save over $400 on this DDR5 gaming PC with RTX 5060 and Core i7-14700F."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ddr5/this-usd389-32gb-ddr5-ram-kit-is-the-cheapest-on-sale-right-now-for-a-gaming-pc-upgrade-higher-spec-ram-for-usd415-gives-pc-builders-rare-choice-as-the-ai-boom-continues-to-force-memory-prices-higher",
    "domain": "AI 算力 / 半导体",
    "title": "This $389 32GB DDR5 RAM kit is the cheapest on sale right now for a gaming PC upgrade — higher-spec RAM for $415 gives PC builders rare choice as the AI boom continues to force memory prices higher",
    "url": "https://www.tomshardware.com/pc-components/ddr5/this-usd389-32gb-ddr5-ram-kit-is-the-cheapest-on-sale-right-now-for-a-gaming-pc-upgrade-higher-spec-ram-for-usd415-gives-pc-builders-rare-choice-as-the-ai-boom-continues-to-force-memory-prices-higher",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T11:00:24+00:00",
    "summary": "These DDR5 32GB memory kits are the cheapest you'll find on sale right now, starting at $389."
  },
  {
    "id": "hn:49557813",
    "domain": "AI 算力 / 半导体",
    "title": "Tell HN: NVIDIA's Acquisition of HuggingFace was for $HuggingFace",
    "url": "https://news.ycombinator.com/item?id=49557813",
    "source": "MontagFTB",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-09-03T22:08:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:49552375",
    "domain": "AI 算力 / 半导体",
    "title": "Texas Data Center Map: See where data centers are operating or planned",
    "url": "https://www.kxan.com/news/texas/texas-data-center-tracker-see-where-600-projects-are-operating-or-planned-across-state-in-interactive-map/",
    "source": "simonpure",
    "platform": "hackernews",
    "points": 34,
    "published_at": "2026-09-03T16:10:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:49552616",
    "domain": "AI 算力 / 半导体",
    "title": "Launch HN: Mireye (YC S26) – Infrastructure for Physical World AI Agents",
    "url": "https://news.ycombinator.com/item?id=49552616",
    "source": "anshchokshi",
    "platform": "hackernews",
    "points": 28,
    "published_at": "2026-09-03T16:24:13+00:00",
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
    "points": 1159,
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
    "id": "hn:49611251",
    "domain": "大厂 AI 动态",
    "title": "AlphaGenome Atlas: a high-resolution map of human DNA",
    "url": "https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphagenome-atlas/",
    "source": "utiiiD",
    "platform": "hackernews",
    "points": 593,
    "published_at": "2026-09-08T14:55:45+00:00",
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
    "points": 297,
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
    "id": "hn:49602490",
    "domain": "大厂 AI 动态",
    "title": "Emacs Bedrock 2.0",
    "url": "https://lambdaland.org/posts/2026-09-06-bedrock-v2/",
    "source": "ashton314",
    "platform": "hackernews",
    "points": 190,
    "published_at": "2026-09-07T20:12:12+00:00",
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
    "id": "hn:49610641",
    "domain": "大厂 AI 动态",
    "title": "AlphaGenome Atlas predictive map of every DNA letter change in the human genome",
    "url": "https://deepmind.google/blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/",
    "source": "fady0",
    "platform": "hackernews",
    "points": 90,
    "published_at": "2026-09-08T14:14:15+00:00",
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
    "id": "hn:49566788",
    "domain": "大厂 AI 动态",
    "title": "Project HydraFusion: Frontier quality via multi-model orchestration",
    "url": "https://github.blog/ai-and-ml/github-copilot/project-hydrafusion-frontier-quality-via-multi-model-orchestration/",
    "source": "qainsights",
    "platform": "hackernews",
    "points": 79,
    "published_at": "2026-09-04T16:24:50+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/transportation/992443/volvo-xc40-phev-specs-price-gemini",
    "domain": "大厂 AI 动态",
    "title": "Volvo XC40 PHEV is back with a new look, better sensors, and Gemini AI",
    "url": "https://www.theverge.com/transportation/992443/volvo-xc40-phev-specs-price-gemini",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T07:00:00+00:00",
    "summary": "It's been about three years since Volvo discontinued its plug-in hybrid XC40. The mild hybrid version remains on sale in the US and elsewhere, alongside the electric EX40. Today, Volvo announced it wa"
  },
  {
    "id": "rss:https://www.theverge.com/tech/993064/no-airpods-with-cameras-apple-event",
    "domain": "大厂 AI 动态",
    "title": "There aren’t AirPods with cameras yet and I hope it stays that way",
    "url": "https://www.theverge.com/tech/993064/no-airpods-with-cameras-apple-event",
    "source": "John.Higgins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T23:00:04+00:00",
    "summary": "September Apple events are always a swirl of information and new, exciting products, and today's was no different. Apple announced its first foldable, the iPhone Duo, alongside the iPhone 18 Pro and P"
  },
  {
    "id": "rss:https://www.theverge.com/tech/993048/iphone-18-pro-black-color",
    "domain": "大厂 AI 动态",
    "title": "The black iPhone Pro returns",
    "url": "https://www.theverge.com/tech/993048/iphone-18-pro-black-color",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T22:37:51+00:00",
    "summary": "Apple has seen reason: It has a black model in the iPhone Pro lineup again. Last year, Apple went bold with its colors for the iPhone 17 Pro, offering a flashy orange, a shiny silver, and a dark blue."
  },
  {
    "id": "rss:https://www.theverge.com/tech/992755/apple-iphone-duo-history-of-devices",
    "domain": "大厂 AI 动态",
    "title": "The incomplete history of Duo devices",
    "url": "https://www.theverge.com/tech/992755/apple-iphone-duo-history-of-devices",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T22:23:35+00:00",
    "summary": "Apple announced the company's first device with a folding screen today, the iPhone Duo, but that's where the firsts end. The Duo is not only far from the first foldable on the market thanks to the eff"
  },
  {
    "id": "rss:https://www.theverge.com/tech/993022/wordpress-automattic-ceo-matt-mullenweg-leave-of-absence",
    "domain": "大厂 AI 动态",
    "title": "Automattic CEO Matt Mullenweg placed on leave",
    "url": "https://www.theverge.com/tech/993022/wordpress-automattic-ceo-matt-mullenweg-leave-of-absence",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T22:15:52+00:00",
    "summary": "Matt Mullenweg, the CEO of WordPress.com owner Automattic, has been placed on a paid leave of absence, as reported earlier by 404 Media. In an internal message by the outlet, Mullenweg claims Automatt"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/993005/smartphone-price-hikes-apple-iphone-18-pro",
    "domain": "大厂 AI 动态",
    "title": "It’s the year of smartphone price hikes",
    "url": "https://www.theverge.com/gadgets/993005/smartphone-price-hikes-apple-iphone-18-pro",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T21:52:43+00:00",
    "summary": "Paying more for a new phone seems almost unavoidable after Apple's event today. The new iPhone 18 Pro and Pro Max start at $1,199 and $1,299, respectively - a $100 price hike over their predecessors. "
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/991977/suno-releases-its-first-ai-music-model-made-with-record-industry-help",
    "domain": "大厂 AI 动态",
    "title": "Suno releases its first AI music model made with record industry help",
    "url": "https://www.theverge.com/ai-artificial-intelligence/991977/suno-releases-its-first-ai-music-model-made-with-record-industry-help",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T21:42:19+00:00",
    "summary": "Suno's new v6 AI music model is its first made with support from the record industry. Suno's Jack Brody told The Verge that v6 was \"trained from the ground up, with a new set of data that does not inc"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/992953/openai-math-millennium-prize-navier-stokes",
    "domain": "大厂 AI 动态",
    "title": "OpenAI’s sly mathematical breakthrough sends a chill through academia",
    "url": "https://www.theverge.com/ai-artificial-intelligence/992953/openai-math-millennium-prize-navier-stokes",
    "source": "Robert Hart",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T21:16:34+00:00",
    "summary": "OpenAI's announcement Tuesday that it has solved one of mathematics' legendary Millennium Prize problems should have been a moment of triumph. The result is both an undeniable achievement and a striki"
  },
  {
    "id": "rss:https://www.theverge.com/tech/992919/apple-siri-ai-audio-intelligence-privacy",
    "domain": "大厂 AI 动态",
    "title": "Read the Apple document explaining how new listening features still protect your privacy",
    "url": "https://www.theverge.com/tech/992919/apple-siri-ai-audio-intelligence-privacy",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T20:44:43+00:00",
    "summary": "At Wednesday's iPhone Duo launch event, Apple announced a handful of new Siri AI Audio Intelligence features, including Siri Recap, Live Rewind, Sound Recognition, and Music Recognition. Alongside its"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/990508/apple-watch-series-12-ultra-4-spec-comparison",
    "domain": "大厂 AI 动态",
    "title": "How the new Apple Watches compare to the last-gen models",
    "url": "https://www.theverge.com/gadgets/990508/apple-watch-series-12-ultra-4-spec-comparison",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T20:42:51+00:00",
    "summary": "Apple rolled out the Apple Watch Series 12 and Apple Watch Ultra 4 at its \"Surprise and shine\" event. The new watches feature sizable improvements to their health sensors and tracking, plus the abilit"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/09/ai-research-startup-listen-labs-scrubbed-a-1-5b-funding-round-for-salesforce-talks/",
    "domain": "大厂 AI 动态",
    "title": "AI research startup Listen Labs scrubbed a $1.5B funding round for Salesforce talks",
    "url": "https://techcrunch.com/2026/09/09/ai-research-startup-listen-labs-scrubbed-a-1-5b-funding-round-for-salesforce-talks/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T00:00:37+00:00",
    "summary": "Listen Labs walked away from a signed Series C term sheet from Menlo Ventures, sources say."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/09/automattics-board-forces-ceo-matt-mullenweg-into-leave-of-absence/",
    "domain": "大厂 AI 动态",
    "title": "Automattic’s board forces CEO Matt Mullenweg into leave of absence",
    "url": "https://techcrunch.com/2026/09/09/automattics-board-forces-ceo-matt-mullenweg-into-leave-of-absence/",
    "source": "Julie Bort, Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T23:14:29+00:00",
    "summary": "Mullenweg said in a company Slack message that it was against his will."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/09/openai-adds-a-prominent-ai-doomer-to-its-board-of-directors/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI adds a prominent AI doomer to its board of directors",
    "url": "https://techcrunch.com/2026/09/09/openai-adds-a-prominent-ai-doomer-to-its-board-of-directors/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T22:25:22+00:00",
    "summary": "Paul Christiano, an influential AI researcher focused on alignment, is joining the OpenAI Foundation as a member of its board."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/09/massachusetts-hits-data-centers-with-new-clean-power-rules/",
    "domain": "大厂 AI 动态",
    "title": "Massachusetts hits data centers with new clean power rules",
    "url": "https://techcrunch.com/2026/09/09/massachusetts-hits-data-centers-with-new-clean-power-rules/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T21:43:34+00:00",
    "summary": "Massachusetts has become the third state in as many months to slap new restrictions on data center development."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/09/apples-new-ceo-is-reviving-a-steve-jobs-strategy-from-25-years-ago/",
    "domain": "大厂 AI 动态",
    "title": "Apple’s new CEO is reviving a Steve Jobs strategy from 25 years ago",
    "url": "https://techcrunch.com/2026/09/09/apples-new-ceo-is-reviving-a-steve-jobs-strategy-from-25-years-ago/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T20:58:09+00:00",
    "summary": "John Ternus made the case in his first keynote as Apple CEO that the iPhone isn't going anywhere."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/09/apple-watchs-new-ai-features-are-normalizing-the-idea-that-technology-is-always-listening/",
    "domain": "大厂 AI 动态",
    "title": "Apple Watch’s new AI features are normalizing the idea that technology is always listening",
    "url": "https://techcrunch.com/2026/09/09/apple-watchs-new-ai-features-are-normalizing-the-idea-that-technology-is-always-listening/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T20:24:48+00:00",
    "summary": "Apple says its new watches won’t save raw audio, but features that can transcribe recent speech and summarize ambient conversations raise new questions about consent, privacy, and how people behave wh"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/09/everything-apple-announced-at-its-fall-iphone-event-from-the-foldable-iphone-duo-to-an-always-listening-apple-watch/",
    "domain": "大厂 AI 动态",
    "title": "Everything Apple announced at its fall iPhone event, from the foldable iPhone Duo to an always-listening Apple Watch",
    "url": "https://techcrunch.com/2026/09/09/everything-apple-announced-at-its-fall-iphone-event-from-the-foldable-iphone-duo-to-an-always-listening-apple-watch/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T20:03:43+00:00",
    "summary": "The main event was the tech giant's highly anticipated first foldable phone, the iPhone Duo."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/09/there-are-new-shiny-iphones-so-apple-is-making-you-pay-more-for-older-models/",
    "domain": "大厂 AI 动态",
    "title": "There are new shiny iPhones, so Apple is making you pay more for older models",
    "url": "https://techcrunch.com/2026/09/09/there-are-new-shiny-iphones-so-apple-is-making-you-pay-more-for-older-models/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T19:56:18+00:00",
    "summary": "Apple is raising the price of its existing iPhone models by $100, including iPhone 16, iPhone 17, and iPhone Air."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/09/the-hinge-for-apples-new-foldable-phone-was-built-with-ai/",
    "domain": "大厂 AI 动态",
    "title": "The hinge for Apple’s new foldable phone was built with AI",
    "url": "https://techcrunch.com/2026/09/09/the-hinge-for-apples-new-foldable-phone-was-built-with-ai/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T19:21:48+00:00",
    "summary": "Apple says it used AI and 3D printing in the manufacturing process for its long-awaited foldable phone."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/09/apple-watchs-new-feature-listens-to-your-chats-and-recaps-them/",
    "domain": "大厂 AI 动态",
    "title": "Apple Watch’s new feature listens to your chats and recaps them",
    "url": "https://techcrunch.com/2026/09/09/apple-watchs-new-feature-listens-to-your-chats-and-recaps-them/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T19:08:59+00:00",
    "summary": "The Siri Recap feature is similar to other note-taking apps like Granola."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/09/harvey-hits-15-5b-valuation-months-after-reaching-11b/",
    "domain": "大厂 AI 动态",
    "title": "Harvey hits $15.5B valuation, months after reaching $11B",
    "url": "https://techcrunch.com/2026/09/09/harvey-hits-15-5b-valuation-months-after-reaching-11b/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T18:34:24+00:00",
    "summary": "The legal AI startup and VC darling has nearly doubled its valuation in nine months."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/09/apples-revamped-health-app-will-calculate-your-health-age-and-readiness-score/",
    "domain": "大厂 AI 动态",
    "title": "Apple’s revamped Health app will calculate your ‘health age’ and readiness score",
    "url": "https://techcrunch.com/2026/09/09/apples-revamped-health-app-will-calculate-your-health-age-and-readiness-score/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T18:16:29+00:00",
    "summary": "The update uses Apple Intelligence to make better sense of your health data."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/09/apple-unveils-watch-series-12-and-watch-ultra-4-with-an-ai-upgrade-that-can-recap-your-day/",
    "domain": "大厂 AI 动态",
    "title": "Apple unveils Watch Series 12 and Watch Ultra 4 with an AI upgrade that can recap your day",
    "url": "https://techcrunch.com/2026/09/09/apple-unveils-watch-series-12-and-watch-ultra-4-with-an-ai-upgrade-that-can-recap-your-day/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T18:08:46+00:00",
    "summary": "Most notably, Apple is taking aim at the growing wave of AI wearables with new \"Audio Intelligence\" features that let you rewind moments and remember details from daily conversations."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/09/apple-has-a-new-way-prove-your-iphone-photos-arent-ai-slop/",
    "domain": "大厂 AI 动态",
    "title": "Apple has a new way to prove your iPhone photos aren’t AI slop",
    "url": "https://techcrunch.com/2026/09/09/apple-has-a-new-way-prove-your-iphone-photos-arent-ai-slop/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T18:08:35+00:00",
    "summary": "Apple introduced Apple Reference Image to help users determine whether photos have been edited, including alterations made by AI."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/09/apple-shows-off-airpods-5-with-improved-active-noise-cancellation/",
    "domain": "大厂 AI 动态",
    "title": "Apple shows off AirPods 5 with improved active noise cancellation",
    "url": "https://techcrunch.com/2026/09/09/apple-shows-off-airpods-5-with-improved-active-noise-cancellation/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T18:06:40+00:00",
    "summary": "The AirPods 5 support better noise cancellation, Siri AI, and offer volume controls on the stem."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/09/apple-unveils-its-first-foldable-the-iphone-duo/",
    "domain": "大厂 AI 动态",
    "title": "Apple unveils its first foldable, the iPhone Duo",
    "url": "https://techcrunch.com/2026/09/09/apple-unveils-its-first-foldable-the-iphone-duo/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T17:58:14+00:00",
    "summary": "Unlike early iterations of foldables, which looked like vertical slabs, Apple adopted a wider form factor that could aid in a better aspect ratio while watching videos when the device is unfolded."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/09/apple-ceo-john-ternus-says-the-best-ai-device-is-still-the-iphone/",
    "domain": "大厂 AI 动态",
    "title": "Apple CEO John Ternus says the best AI device is still the iPhone",
    "url": "https://techcrunch.com/2026/09/09/apple-ceo-john-ternus-says-the-best-ai-device-is-still-the-iphone/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T17:36:05+00:00",
    "summary": "The company also argued that its on-device models offer consumers more privacy."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/09/apple-launches-iphone-18-pro-with-upgraded-camera/",
    "domain": "大厂 AI 动态",
    "title": "Apple launches iPhone 18 Pro with upgraded camera",
    "url": "https://techcrunch.com/2026/09/09/apple-launches-iphone-18-pro-with-upgraded-camera/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T17:26:05+00:00",
    "summary": "Apple's new iPhone 18 Pro lineup upgrades the camera and comes in burgundy."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/09/doj-wants-more-answers-on-foxs-22b-roku-deal/",
    "domain": "大厂 AI 动态",
    "title": "DOJ wants more answers on Fox’s $22B Roku deal",
    "url": "https://techcrunch.com/2026/09/09/doj-wants-more-answers-on-foxs-22b-roku-deal/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T16:44:21+00:00",
    "summary": "The investigation also comes as the DOJ has faced criticism over how it handles major mergers, including questions about political influence."
  },
  {
    "id": "rss:https://techcrunch.com/video/superintelligence-is-coming-should-we-let-it/",
    "domain": "大厂 AI 动态",
    "title": "Superintelligence is coming. Should we let it?",
    "url": "https://techcrunch.com/video/superintelligence-is-coming-should-we-let-it/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T16:05:35+00:00",
    "summary": "AI companies have been talking about superintelligent AI like&#160;it&#8217;s&#160;inevitable, but recent&#160;safety incidents&#160;like&#160;OpenAI&#8217;s&#160;Hugging Face breach&#160;are&#160;dem"
  },
  {
    "id": "rss:https://stratechery.com/2026/openai-does-math-reward-hacking-meta-launches-personal-agent/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI Does Math, Reward-Hacking, Meta Launches Personal Agent",
    "url": "https://stratechery.com/2026/openai-does-math-reward-hacking-meta-launches-personal-agent/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T10:00:00+00:00",
    "summary": "OpenAI solving one of the most famous math problems is extremely impressive, and of little impact to most people's lives; Meta's Muse agent launch has the potential to be the exact opposite."
  },
  {
    "id": "rss:https://stratechery.com/2026/write-things-down/",
    "domain": "大厂 AI 动态",
    "title": "Write Things Down",
    "url": "https://stratechery.com/2026/write-things-down/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T10:00:00+00:00",
    "summary": "Writing things down is powerful, for humans and for AI; what comes first, however, is what to write, why to do it, and actually getting things done."
  },
  {
    "id": "rss:https://arstechnica.com/information-technology/2026/09/4-groups-caught-using-the-same-chrome-and-windows-exploit-kit/",
    "domain": "大厂 AI 动态",
    "title": "4 groups caught using the same Chrome and Windows exploit kit",
    "url": "https://arstechnica.com/information-technology/2026/09/4-groups-caught-using-the-same-chrome-and-windows-exploit-kit/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T20:55:02+00:00",
    "summary": "A patch gap and the hastened pace of AI-based vulnerability discovery are likely contributors."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/09/as-europe-flounders-in-space-a-rising-french-star-may-show-the-way/",
    "domain": "大厂 AI 动态",
    "title": "Europe may finally have found a space entrepreneur who is meeting the moment",
    "url": "https://arstechnica.com/space/2026/09/as-europe-flounders-in-space-a-rising-french-star-may-show-the-way/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T20:27:40+00:00",
    "summary": "\"We will not be relevant without a massive rocket at a massive cadence.\""
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/09/six-chinese-ai-firms-accused-of-aggressively-copying-us-frontier-models/",
    "domain": "大厂 AI 动态",
    "title": "Six Chinese AI firms accused of aggressively copying US frontier models",
    "url": "https://arstechnica.com/tech-policy/2026/09/six-chinese-ai-firms-accused-of-aggressively-copying-us-frontier-models/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T20:06:28+00:00",
    "summary": "US urges AI firms to ID, then secretly switch, Chinese users to less-capable models."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/09/apples-long-rumored-foldable-becomes-reality-with-the-2000-iphone-duo/",
    "domain": "大厂 AI 动态",
    "title": "Apple's long-rumored foldable becomes reality with the $2,000 iPhone Duo",
    "url": "https://arstechnica.com/gadgets/2026/09/apples-long-rumored-foldable-becomes-reality-with-the-2000-iphone-duo/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T19:42:00+00:00",
    "summary": "Apple's first foldable can be yours next month."
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
    "id": "wscn:3781482",
    "domain": "股票",
    "title": "《金融强国建设“十五五”规划》正式出台：2035年基本建成中国特色现代金融体系",
    "url": "https://wallstreetcn.com/articles/3781482",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T07:25:32+00:00",
    "summary": "更多消息，持续更新中"
  },
  {
    "id": "wscn:3781484",
    "domain": "股票",
    "title": "规避反垄断审查？英伟达被美司法部调查",
    "url": "https://wallstreetcn.com/articles/3781484",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T07:20:51+00:00",
    "summary": "英伟达与AI芯片新星Groq的一纸\"许可协议\"，正将这家市值5.4万亿美元的芯片巨头推上反垄断调查的风口。美国司法部怀疑，这笔协议不过是披着许可外衣的变相并购——核心技术授权加上CEO等高管集体出走，实质已完成收购，却巧妙绕开常规并购审查。"
  },
  {
    "id": "wscn:3781478",
    "domain": "股票",
    "title": "贝莱德：抛弃传统60/40组合，改用50/30/20——20%配私募市场",
    "url": "https://wallstreetcn.com/articles/3781478",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T06:40:15+00:00",
    "summary": "贝莱德高管表示，AI建设浪潮带来百年一遇的投资转变，正重塑资产配置格局。因传统60/40股债组合受通胀与债市波动挑战，建议调整为50/30/20（含20%私募资产）。预计全球另类资产规模2030年将达30万亿美元，AI已成为私募配置的核心宏观驱动力。"
  },
  {
    "id": "wscn:3781314",
    "domain": "股票",
    "title": "日元急涨破153：升值空间还有多大？套利交易危险吗？",
    "url": "https://wallstreetcn.com/premium/articles/3781314?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T06:37:44+00:00",
    "summary": "日元急升源于政策预期与空头平仓，套利风险升高但未必崩盘，后续升值空间看下周美日央行会议。"
  },
  {
    "id": "wscn:3781479",
    "domain": "股票",
    "title": "高盛评苹果折叠iPhone：定价“Affordable”，今年出货最高可达3500万台",
    "url": "https://wallstreetcn.com/articles/3781479",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T06:36:27+00:00",
    "summary": "高盛报告指出，iPhone Duo凭“史上最薄”设计与“实惠”的定价，有望打开大众市场，维持2026年出货1400万至3500万台预测。新品在铰链、散热及摄像领域的升级，将对鸿海等大中华区供应链构成利好。"
  },
  {
    "id": "wscn:3781476",
    "domain": "股票",
    "title": "美股风险溢价创2002年来新低，摩根大通：利率上行冲击将比过去二十年更痛",
    "url": "https://wallstreetcn.com/articles/3781476",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T06:12:10+00:00",
    "summary": "美股风险缓冲垫告急。摩根大通警告，标普500股权风险溢价已跌至2.1%，创2002年来最低，较历史均值低逾100个基点。低溢价时代暗藏三重隐患：股市对利率冲击的敏感性系统性提升、全球投资者超配股票至二十年高位面临再平衡压力、股债正相关格局强化令风险平价策略持续失效。一旦实际利率进一步走高，这场静悄悄的估值重定价或将猛烈显现。"
  },
  {
    "id": "wscn:3781475",
    "domain": "股票",
    "title": "台积电8月营收5148亿元台币创新高，扩厂速度空前仍追不上需求",
    "url": "https://wallstreetcn.com/articles/3781475",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T05:41:21+00:00",
    "summary": "累计2026年1月至8月，台积电合并营收约为新台币3兆3,868亿7,000万元，较2025年同期约2兆4,320亿元增长39.3%。以绝对金额计算，前八个月营收较去年同期增加逾9,500亿新台币，规模可观。台积电近日表示，即使正以前所未有的速度兴建新厂，产能扩充仍追不上需求。"
  },
  {
    "id": "wscn:3781477",
    "domain": "股票",
    "title": "韩国央行警告：挂钩芯片股的海外衍生品激增，正在放大本土市场波动",
    "url": "https://wallstreetcn.com/articles/3781477",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T05:39:27+00:00",
    "summary": "韩国央行在报告中警告，与本土芯片股挂钩的海外衍生品及高杠杆对冲基金正大幅放大股市波动。报告点名对冲基金Situational Awareness使用高杠杆建仓与平仓，加剧了7月KOSPI暴跌，并强调风险已向加密市场等跨界传导，呼吁强化海外监管。"
  },
  {
    "id": "wscn:3781392",
    "domain": "股票",
    "title": "动力煤如期逼近千元，煤炭行业的好日子还能持续多久？",
    "url": "https://wallstreetcn.com/premium/articles/3781392?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T05:11:40+00:00",
    "summary": "2026年上半年，煤炭行业重新进入盈利上行通道，二季度改善明显加速，核心推动来自煤价回升。进入下半年，市场关注点已经从半年报本身转向更重要的问题：供给收缩还能持续多久、库存能否继续去化，以及逼近千元的动力煤最终会在哪里形成这一轮高点。"
  },
  {
    "id": "wscn:3781464",
    "domain": "股票",
    "title": "A股三大股指小幅下跌，多只银行股创新高，存储芯片活跃，恒科指跌超2%，AI大模型双雄大幅下挫",
    "url": "https://wallstreetcn.com/articles/3781464",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T04:05:13+00:00",
    "summary": "盘面上，个股跌多涨少，沪深京三市约4300股飘绿，市场量能萎缩，上午半天成交1.1万亿。沪深两市半日成交额1.09万亿，较上个交易日缩量1170亿。板块方面，玻纤、覆铜板、银行、电力股表现强势，存储、公路、港口、燃气、券商板块活跃，海运、农业、汽车、零售板块调整。"
  },
  {
    "id": "wscn:3781467",
    "domain": "股票",
    "title": "硅谷都在聊些什么？AI下半场开始！高盛Communacopia + TMT大会现场解码巨头框架",
    "url": "https://wallstreetcn.com/premium/articles/3781467?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T03:26:55+00:00",
    "summary": "旧金山高盛Communacopia + Technology Conference 2026的三场session，把未来三年AI算力产业链的经济模型、产能节奏、客户结构一次性摊开。"
  },
  {
    "id": "wscn:3781470",
    "domain": "股票",
    "title": "贝森特成功“突袭”日元，但为何无力驯服美债？",
    "url": "https://wallstreetcn.com/articles/3781470",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T03:12:33+00:00",
    "summary": "贝森特能联合美日政策协调、释放“信息优势”信号，逼退日元空头；却在30万亿美元美债市场束手无策——财赤扩张、通胀黏性、国债供给高企，这些结构性力量不是靠几十亿回购能撼动的。政府可以影响价格偏离均衡的速度，却无法决定均衡本身。"
  },
  {
    "id": "wscn:3781472",
    "domain": "股票",
    "title": "连续四月领跑细分赛道｜两万车主用真实选择，看懂别克至境E7油换电逻辑",
    "url": "https://wallstreetcn.com/articles/3781472",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T02:58:43+00:00",
    "summary": "国内汽车置换市场已经迎来大变局，过去几年，新能源市场主要依靠新增购车用户驱动。2026年，存量置换成..."
  },
  {
    "id": "wscn:3781387",
    "domain": "股票",
    "title": "DCI超级周期：康宁长单锁到2032年，光纤真的供不应求？",
    "url": "https://wallstreetcn.com/premium/articles/3781387?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T02:51:42+00:00",
    "summary": "从GPU机房走向“国家级骨干网”——AI光通信投资边界的第二次扩张。"
  },
  {
    "id": "wscn:3781469",
    "domain": "股票",
    "title": "阿布扎比穆巴达拉战略入股瑞幸拆解：新老基金优先股转让，交易规模约10亿美元",
    "url": "https://wallstreetcn.com/articles/3781469",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T02:48:15+00:00",
    "summary": "大钲受益所有权不变"
  },
  {
    "id": "wscn:3781465",
    "domain": "股票",
    "title": "浏览破亿！Anthropic对齐负责人亲认：十年内AI灭绝人类概率超10%",
    "url": "https://wallstreetcn.com/articles/3781465",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T02:33:37+00:00",
    "summary": "Anthropic核心研究员在IPO前夕愤然辞职，一封万字檄文浏览量破亿。对齐负责人罕见公开承认：十年内AI灭绝人类概率超10%，且“根本没有解决方案”。当前，Claude模型已在真实互联网上独立完成黑客攻击，还学会了“自欺欺人”以规避审查——潘多拉魔盒已开，却无人敢踩刹车。"
  },
  {
    "id": "wscn:3781462",
    "domain": "股票",
    "title": "调研亚洲机构后，高盛合伙人点评：7月遭重创，如今对AI交易“谨慎过头”了",
    "url": "https://wallstreetcn.com/articles/3781462",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T02:32:03+00:00",
    "summary": "7月动量股历史性暴跌在亚洲投资者心中留下\"创伤\"，但高盛完成亚洲客户调研后直言：谨慎情绪已矫枉过正。多项数据显示，机构杠杆率、AI持仓及情绪指标均跌至年内低位，而标普500二季度每股收益却同比劲增30%，基本面与情绪严重背离。防御性定位正在积蓄上行动能，IPO管线或成触发反攻的关键催化剂。"
  },
  {
    "id": "wscn:3781463",
    "domain": "股票",
    "title": "高盛TMT大会第二日亮点：AI从概念走向商业化，闪迪判断NAND供给将长期偏弱",
    "url": "https://wallstreetcn.com/articles/3781463",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T02:00:23+00:00",
    "summary": "高盛科技大会第二日，闪迪给出存储行业供给侧判断：NAND供给增长在可预见的未来将持续受限，而AI推理需求持续扩张，供需格局长期偏紧。与此同时，Etsy、Booking.com、Block等多家公司披露AI在匹配转化、客服、基础设施等场景的实际落地进展，AI从概念加速走向可量化的商业收益。"
  },
  {
    "id": "wscn:3781458",
    "domain": "股票",
    "title": "Codex主管Tibo：“清晰的意图表达、架构品味与系统把控力”是AI时代最不可替代的",
    "url": "https://wallstreetcn.com/articles/3781458",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T01:50:48+00:00",
    "summary": "OpenAI Codex主管认为，AI时代，“如果你无法解释你在试图实现什么，如果你无法表达你的意图，如果你与你所服务的社区没有连接，如果你没有品味——那做出好的工作会难得多。”他透露，OpenAI已将AI代码审查模型强制应用于所有PR，安全检测全自动、“超越人类水平”。"
  },
  {
    "id": "wscn:3781459",
    "domain": "股票",
    "title": "日本正在把全球“拖下水”",
    "url": "https://wallstreetcn.com/articles/3781459",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T01:37:23+00:00",
    "summary": "日本30年来首次突破3%的国债收益率正在引发全球警报，野村表示，这轮全球长端利率上行的震源正是日本本土——财政扩张失控、央行加息预期叠加，财政风险溢价已成最大推手。更令市场警惕的是，日债收益率持续攀升不仅威胁全球金融机构资产负债表，更可能刺破AI科技股泡沫，引爆一场突发性经济减速。"
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
    "id": "hn:49511824",
    "domain": "股票",
    "title": "Apple Is Suddenly an AI Infra Stock as OpenAI Buys 10k+ Macs",
    "url": "https://247wallst.com/investing/2026/08/31/apple-is-suddenly-an-ai-infrastructure-stock-as-openai-buys-macs-by-the-tens-of-thousands/",
    "source": "prabal97",
    "platform": "hackernews",
    "points": 41,
    "published_at": "2026-08-31T16:44:15+00:00",
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
    "id": "hn:49401229",
    "domain": "股票",
    "title": "Anthropic IPO filing will show AI backlash as a risk factor, sources say",
    "url": "https://www.cnbc.com/2026/08/21/-anthropic-ipo-filing-will-show-ai-backlash-as-risk-sources-say.html",
    "source": "newsomix9xl",
    "platform": "hackernews",
    "points": 37,
    "published_at": "2026-08-22T16:23:09+00:00",
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
    "id": "hn:49594251",
    "domain": "金融",
    "title": "Switzerland's Federal Government Is Replacing Microsoft on 3k Computers",
    "url": "https://itsfoss.com/news/switzerland-replace-microssoft-pilot/",
    "source": "ivell",
    "platform": "hackernews",
    "points": 367,
    "published_at": "2026-09-07T05:33:25+00:00",
    "summary": ""
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
    "id": "hn:49602582",
    "domain": "金融",
    "title": "A Tesla ran a stop sign and killed a man, Full Self-Driving/Autopilot was on",
    "url": "https://electrek.co/2026/09/07/tesla-driver-assist-stop-sign-buena-vista/",
    "source": "FabHK",
    "platform": "hackernews",
    "points": 168,
    "published_at": "2026-09-07T20:21:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:49601846",
    "domain": "金融",
    "title": "Tesla killing Solar Roof is leaving installers with six-figure losses",
    "url": "https://electrek.co/2026/09/01/tesla-solar-roof-exit-installers-losses/",
    "source": "voxadam",
    "platform": "hackernews",
    "points": 135,
    "published_at": "2026-09-07T19:08:47+00:00",
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
    "points": 125,
    "published_at": "2026-09-06T22:43:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:49626052",
    "domain": "金融",
    "title": "One woman's Tesla was remotely controlled by an abusive ex-partner",
    "url": "https://www.theguardian.com/australia-news/2026/sep/09/how-one-womans-tesla-was-remotely-controlled-and-harass-by-her-abusive-ex-partner-ntwnfb",
    "source": "gradschool",
    "platform": "hackernews",
    "points": 72,
    "published_at": "2026-09-09T13:16:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:49596610",
    "domain": "金融",
    "title": "Initial effects of AI technology on employment look positive",
    "url": "https://www.economist.com/finance-and-economics/2026/09/04/the-jobs-apocalypse-is-postponed-an-ai-jobs-boom-is-here",
    "source": "MrBuddyCasino",
    "platform": "hackernews",
    "points": 99,
    "published_at": "2026-09-07T10:38:32+00:00",
    "summary": ""
  },
  {
    "id": "hn:49599058",
    "domain": "金融",
    "title": "If a Tesla Cybercab fleet were profitable, Tesla wouldn't sell you one",
    "url": "https://electrek.co/2026/09/07/tesla-cybercab-fleet-profitable-wouldnt-sell/",
    "source": "jijojv",
    "platform": "hackernews",
    "points": 98,
    "published_at": "2026-09-07T14:49:43+00:00",
    "summary": ""
  },
  {
    "id": "hn:49612981",
    "domain": "金融",
    "title": "DOJ Blocked ICE Agent Shooting Charge over Federal Prosecutor's Objections",
    "url": "https://www.propublica.org/article/doj-blocks-charges-ice-agent-minneapolis-julio-cesar-sosa-celis",
    "source": "paimapi",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-09-08T16:54:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:49625461",
    "domain": "金融",
    "title": "Teen reading slumps to worst this century due to surge in screen time",
    "url": "https://finance.yahoo.com/news/teen-reading-slumps-worst-century-111013754.html",
    "source": "pseudolus",
    "platform": "hackernews",
    "points": 41,
    "published_at": "2026-09-09T12:29:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:49633640",
    "domain": "金融",
    "title": "DHS Program Analyzes Americans' Finances to Flag Drivers for Traffic Stops",
    "url": "https://www.military.com/dhs-program-analyzes-americans-finances-to-flag-drivers-for-traffic-stops-report",
    "source": "randycupertino",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-09-09T20:22:20+00:00",
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
    "id": "rss:https://arxiv.org/abs/2609.09323",
    "domain": "金融",
    "title": "Buy Now, Pay Later: Academic Insights and Open Policy Questions",
    "url": "https://arxiv.org/abs/2609.09323",
    "source": "Benedict Guttman-Kenney, Walter W. Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T04:00:00+00:00",
    "summary": "arXiv:2609.09323v1 Announce Type: new Abstract: Buy Now, Pay Later (BNPL) has moved from a novelty product to mainstream consumer finance in the space of a few years. Before 2020, BNPL was a niche off"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.09337",
    "domain": "金融",
    "title": "Credible Discourse on Climate Policy: Beyond Dueling Certitudes",
    "url": "https://arxiv.org/abs/2609.09337",
    "source": "Charles F. Manski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T04:00:00+00:00",
    "summary": "arXiv:2609.09337v1 Announce Type: new Abstract: Whatever the policy question under consideration, reasoned and realistic evaluation requires credible policy analysis under uncertainty. This holds part"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.09405",
    "domain": "金融",
    "title": "The Log S-fBM model: Statistical analysis",
    "url": "https://arxiv.org/abs/2609.09405",
    "source": "Othmane Zarhali, Emmanuel Bacry, Jean-Fran\\c{c}ois Muzy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T04:00:00+00:00",
    "summary": "arXiv:2609.09405v1 Announce Type: new Abstract: The Log S-fBM model, introduced by Wu et al., is a stochastic volatility model whose log volatility is a stationary fractional Brownian motion (S-fBM): "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.09470",
    "domain": "金融",
    "title": "Geometric and Arithmetic Likelihood Aggregation for Diffusions with Heterogeneous Volatility",
    "url": "https://arxiv.org/abs/2609.09470",
    "source": "Jan Vecer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T04:00:00+00:00",
    "summary": "arXiv:2609.09470v1 Announce Type: new Abstract: We study how to combine diffusion models that disagree about drift and covariance. Candidate-first relative-entropy minimization gives geometric pooling"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.09673",
    "domain": "金融",
    "title": "Reducing Prescription Errors Through Information Intervention: A Field Experiment in Healthcare Operations",
    "url": "https://arxiv.org/abs/2609.09673",
    "source": "Xiaodan Shao, Vivek Choudhary, Arnab Majumdar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T04:00:00+00:00",
    "summary": "arXiv:2609.09673v1 Announce Type: new Abstract: Drug-drug interaction (DDI) errors pose serious risks to patient safety. Existing decision-support systems often require physicians to respond to alerts"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.09859",
    "domain": "金融",
    "title": "How an Economy Shrinks in Space: Concavity-on-Jobs and Upward Consolidation under Demographic Decline",
    "url": "https://arxiv.org/abs/2609.09859",
    "source": "Tomoya Mori, Miki Ogawa",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T04:00:00+00:00",
    "summary": "arXiv:2609.09859v1 Announce Type: new Abstract: When a country's population declines, the aggregate economy appears to contract on the intensive margin: industrial diversity intact, every industry a l"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.10053",
    "domain": "金融",
    "title": "Do wind and solar curtail at negative electricity prices? Incentives and evidence across two decades of German renewable support schemes",
    "url": "https://arxiv.org/abs/2609.10053",
    "source": "Lion Hirth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T04:00:00+00:00",
    "summary": "arXiv:2609.10053v1 Announce Type: new Abstract: In many power systems, wind and solar generation increasingly often exceeds electricity demand. Curtailing renewable generation in those hours matters b"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.10380",
    "domain": "金融",
    "title": "High Volume Low Complexity Surgical Hubs in England: Can They Improve Physician Productivity?",
    "url": "https://arxiv.org/abs/2609.10380",
    "source": "Zecharias Anteneh, Adriana Castelli, Peter Sivey, Andrew Street, Jinglin Wen, Joy Adamson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T04:00:00+00:00",
    "summary": "arXiv:2609.10380v1 Announce Type: new Abstract: Whether organisational separation of elective and emergency care improves physician productivity remains an open question. Most existing evidence relies"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.10407",
    "domain": "金融",
    "title": "dexamine: A Python package for Uniswap event data on Ethereum",
    "url": "https://arxiv.org/abs/2609.10407",
    "source": "Magnus Hansson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T04:00:00+00:00",
    "summary": "arXiv:2609.10407v1 Announce Type: new Abstract: Decentralized exchanges record trading and liquidity provision on public blockchains, but empirical analysis requires interpreting these records and lin"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.09226",
    "domain": "金融",
    "title": "Adaptive Entangled Game Modules in Artificial General Intelligence",
    "url": "https://arxiv.org/abs/2609.09226",
    "source": "Haochen Li, Xinshuai Guo, Jingdong Ouyang, Wei Zhang, Leilei Shi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T04:00:00+00:00",
    "summary": "arXiv:2609.09226v1 Announce Type: cross Abstract: We introduce a probability-wave framework for modeling the collective behavior of interacting adaptive agents, deriving testable eigenmodes through a "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.09588",
    "domain": "金融",
    "title": "Signal Correlation, IC, and PnL Dependence",
    "url": "https://arxiv.org/abs/2609.09588",
    "source": "Marc Nunes",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T04:00:00+00:00",
    "summary": "arXiv:2609.09588v1 Announce Type: cross Abstract: Signal correlation and PnL correlation are correlations over different index sets - across assets at each date versus across dates for scalar payoffs "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.09945",
    "domain": "金融",
    "title": "Adversarial Training for Tabular Credit Scoring: A Multi-Attack Robustness Evaluation in P2P Lending",
    "url": "https://arxiv.org/abs/2609.09945",
    "source": "Gijs A. F. Niewzwaag, Marijn G. S. Veth, Manuele Massei, Marcos R. Machado",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T04:00:00+00:00",
    "summary": "arXiv:2609.09945v1 Announce Type: cross Abstract: Machine learning-based credit scoring is increasingly central to Peer-to-Peer (P2P) lending, yet its resilience to adversarial manipulation, where app"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.10074",
    "domain": "金融",
    "title": "Strategic communication of narratives: An experiment",
    "url": "https://arxiv.org/abs/2609.10074",
    "source": "Gerrit Bauch, Arthur Dolgopolov, Manuel Foerster",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T04:00:00+00:00",
    "summary": "arXiv:2609.10074v1 Announce Type: cross Abstract: We investigate the strategic communication of narratives under model uncertainty. The sender has private information about the true data-generating pr"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.10227",
    "domain": "金融",
    "title": "Italian Business-to-Business Invoicing Data: A Network Analysis",
    "url": "https://arxiv.org/abs/2609.10227",
    "source": "Valerio Astuti, Daniele Piras",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T04:00:00+00:00",
    "summary": "arXiv:2609.10227v1 Announce Type: cross Abstract: We present a comprehensive description of the network of Italian Business-to-Business commercial relationships, based on the universe of electronic in"
  },
  {
    "id": "rss:https://arxiv.org/abs/2502.21141",
    "domain": "金融",
    "title": "Tracks to Modernity: Railroads, Growth, and Social Movements in Denmark",
    "url": "https://arxiv.org/abs/2502.21141",
    "source": "Tom G\\\"orges, Magnus {\\O}rberg Rove, Paul Sharp, Christian Vedel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T04:00:00+00:00",
    "summary": "arXiv:2502.21141v3 Announce Type: replace Abstract: We examine how railroads shaped Denmark's nineteenth-century economic transformation and the diffusion of Grundtvigian institutions. Using a panel o"
  },
  {
    "id": "rss:https://arxiv.org/abs/2507.08302",
    "domain": "金融",
    "title": "Arbitrage on Decentralized Exchanges",
    "url": "https://arxiv.org/abs/2507.08302",
    "source": "Xue Dong He, Chen Yang, Yutian Zhou",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T04:00:00+00:00",
    "summary": "arXiv:2507.08302v3 Announce Type: replace Abstract: Decentralized exchanges using automated market makers create arbitrage opportunities with centralized exchanges, where gas fees and transaction orde"
  },
  {
    "id": "rss:https://arxiv.org/abs/2508.17695",
    "domain": "金融",
    "title": "Revisiting H\\\"otte (2025): A Companion Analysis with Extended Evidence from UK Inter-Industry Payment Data, 2017-2024",
    "url": "https://arxiv.org/abs/2508.17695",
    "source": "Kerstin H\\\"otte",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T04:00:00+00:00",
    "summary": "arXiv:2508.17695v2 Announce Type: replace Abstract: In 2025, the UK Office for National Statistics released a novel dataset of monthly inter-industry payment flows during January 2017 to November 2024"
  },
  {
    "id": "rss:https://arxiv.org/abs/2509.24747",
    "domain": "金融",
    "title": "Meyer risk measures",
    "url": "https://arxiv.org/abs/2509.24747",
    "source": "Christian Laudag\\'e, Felix-Benedikt Liebrich",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T04:00:00+00:00",
    "summary": "arXiv:2509.24747v2 Announce Type: replace Abstract: Risk measures summarize the risk profile of financial positions in a single metric, which allows their comparison and supports investment decisions."
  },
  {
    "id": "rss:https://arxiv.org/abs/2511.06545",
    "domain": "金融",
    "title": "AI Coding Tools and Digital Entrepreneurship: The Role of Software Expertise",
    "url": "https://arxiv.org/abs/2511.06545",
    "source": "Ruiqing Cao, Abhishek Bhatia",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T04:00:00+00:00",
    "summary": "arXiv:2511.06545v3 Announce Type: replace Abstract: While digital technologies expand entrepreneurial access by providing technical resources, it is less known whether they enable ventures to create d"
  },
  {
    "id": "rss:https://arxiv.org/abs/2512.02362",
    "domain": "金融",
    "title": "Reconstructing Large Scale Production Networks",
    "url": "https://arxiv.org/abs/2512.02362",
    "source": "Ashwin Bhattathiripad, Vipin P Veetil",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T04:00:00+00:00",
    "summary": "arXiv:2512.02362v4 Announce Type: replace Abstract: Firm-to-firm production networks matter for aggregate propagation, but they are rarely observed. This paper reconstructs national-scale, weighted fi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2512.19705",
    "domain": "金融",
    "title": "Generative AI for Analysts",
    "url": "https://arxiv.org/abs/2512.19705",
    "source": "Jian Xue, Qian Zhang, Wu Zhu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T04:00:00+00:00",
    "summary": "arXiv:2512.19705v2 Announce Type: replace Abstract: We study how generative artificial intelligence (GenAI) reshapes financial analysts' information production. Using the 2023 integration of GenAI int"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.05320",
    "domain": "金融",
    "title": "Screening-Off Information and Conditional Risk in Portfolio Choice",
    "url": "https://arxiv.org/abs/2607.05320",
    "source": "Alejandro Rodriguez Dominguez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T04:00:00+00:00",
    "summary": "arXiv:2607.05320v3 Announce Type: replace Abstract: Conditional portfolio models estimate risk relative to a chosen information set, yet rarely test whether that information removes common cross-asset"
  },
  {
    "id": "rss:https://arxiv.org/abs/2311.12169",
    "domain": "金融",
    "title": "Optimal Retirement Choice under Age-dependent Force of Mortality",
    "url": "https://arxiv.org/abs/2311.12169",
    "source": "Giorgio Ferrari, Shihao Zhu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T04:00:00+00:00",
    "summary": "arXiv:2311.12169v2 Announce Type: replace-cross Abstract: This paper examines optimal investment, consumption, and retirement timing under an age-dependent force of mortality. We formulate the optimiz"
  },
  {
    "id": "rss:https://arxiv.org/abs/2501.17577",
    "domain": "金融",
    "title": "On the Singular Control of a Diffusion and its Running Infimum or Supremum",
    "url": "https://arxiv.org/abs/2501.17577",
    "source": "Giorgio Ferrari, Neofytos Rodosthenous",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T04:00:00+00:00",
    "summary": "arXiv:2501.17577v3 Announce Type: replace-cross Abstract: We study a class of singular stochastic control problems for a one-dimensional diffusion $X$ in which the performance criterion to be optimise"
  },
  {
    "id": "rss:https://arxiv.org/abs/2512.16396",
    "domain": "金融",
    "title": "Global universal approximation with Brownian signatures",
    "url": "https://arxiv.org/abs/2512.16396",
    "source": "Mihriban Ceylan, David J. Pr\\\"omel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T04:00:00+00:00",
    "summary": "arXiv:2512.16396v3 Announce Type: replace-cross Abstract: We establish $L^p$-universal approximation theorems for general path-dependent and non-anticipative functionals on suitable rough path spaces,"
  },
  {
    "id": "rss:https://arxiv.org/abs/2601.09673",
    "domain": "金融",
    "title": "A probabilistic match classification model for low-scoring sports",
    "url": "https://arxiv.org/abs/2601.09673",
    "source": "L\\'aszl\\'o Csat\\'o, Andr\\'as Gyimesi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T04:00:00+00:00",
    "summary": "arXiv:2601.09673v3 Announce Type: replace-cross Abstract: All existing match classification models in the tournament design literature suffer from two major limitations: a contestant is considered ind"
  },
  {
    "id": "hn:49564189",
    "domain": "金融",
    "title": "Norway's Oil Fund Proposes Selling Roughly $80B in U.S. Treasurys",
    "url": "https://www.wsj.com/finance/investing/norways-oil-fund-proposes-cut-to-government-bond-holdings-d930893f",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 47,
    "published_at": "2026-09-04T13:15:24+00:00",
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
    "id": "hn:49551601",
    "domain": "金融",
    "title": "Inside Google’s $200bn Wall Street finance machine for Anthropic",
    "url": "https://www.ft.com/content/549f2e23-5aa2-49c7-9ea6-a9784ab7087c",
    "source": "porridgeraisin",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-09-03T15:26:27+00:00",
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
    "id": "hn:49432102",
    "domain": "金融",
    "title": "Nostr vs. Fediverse vs. Bluesky: A Comparison of Decentralized Social Protocols",
    "url": "https://soapbox.pub/blog/comparing-protocols",
    "source": "Bluestein",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-08-25T11:27:51+00:00",
    "summary": ""
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
    "id": "hn:49396088",
    "domain": "金融",
    "title": "S&P 500 CEO median pay hits $17.3M, widening CEO-worker ratio to 312-to-1",
    "url": "https://finance.yahoo.com/markets/stocks/articles/p-500-ceo-median-pay-234900518.html",
    "source": "newsomix9xl",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-08-22T02:38:14+00:00",
    "summary": ""
  },
  {
    "id": "hn:49348573",
    "domain": "金融",
    "title": "Trump 2.0 has deleted or altered nearly 400 US datasets",
    "url": "https://www.theguardian.com/us-news/ng-interactive/2026/aug/18/trump-federal-data-deleted-altered",
    "source": "_djo_",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-08-18T16:51:15+00:00",
    "summary": ""
  }
]
```
