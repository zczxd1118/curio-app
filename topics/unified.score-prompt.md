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

- 今日日期：`2026-08-14`
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
  "date": "2026-08-14",
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
    "points": 4225645,
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
    "points": 1705902,
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
    "points": 1327430,
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
    "points": 1270299,
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
    "points": 1116191,
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
    "points": 1050644,
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
    "points": 943653,
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
    "points": 873530,
    "published_at": "2025-05-01T09:00:00+00:00",
    "summary": "up的科学星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV17sAte3Exh",
    "domain": "AI",
    "title": "AI做高质量PPT从写到讲的全流程拆解，一期给你讲透！【旁门左道PPT】",
    "url": "http://www.bilibili.com/video/av114039887759711",
    "source": "旁门左道PPT",
    "platform": "bilibili",
    "points": 629714,
    "published_at": "2025-02-21T04:08:12+00:00",
    "summary": "更新一期2025年最新的Ai做PPT-全流程实操教程！&lt;不是那种一键生成通用型PPT的--！&gt;这次我帮大家把做PPT从写到说的全流程拆解出来了，极致压榨各种Ai工具在各个环节使劲儿，去帮大家做出有内容有分析长得还可以的PPT，全程高能，记得码住再看~"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 558975,
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
    "points": 491820,
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
    "points": 436911,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1eK5DzHEWu",
    "domain": "AI",
    "title": "MCP实战指南，mcp视频教程，2小时学透mcp",
    "url": "http://www.bilibili.com/video/av114380213586544",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 396578,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1ia9UBPESQ",
    "domain": "AI",
    "title": "在VScode中配置Claude Code并接入DeepSeek V4 Pro【oo唠嗑教程】",
    "url": "http://www.bilibili.com/video/av116487012549813",
    "source": "沉默的羔丸voov",
    "platform": "bilibili",
    "points": 305899,
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
    "points": 264542,
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
    "points": 235790,
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
    "points": 233578,
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
    "points": 179106,
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
    "points": 160962,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV16Luq6FEmP",
    "domain": "AI",
    "title": "当不懂代码的老婆，第一次接触vibe coding……",
    "url": "http://www.bilibili.com/video/av117076211536327",
    "source": "糖果果的未来要发光",
    "platform": "bilibili",
    "points": 159243,
    "published_at": "2026-08-11T09:50:27+00:00",
    "summary": "当不懂代码的老婆，第一次接触vibe coding……"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 155087,
    "published_at": "2026-04-27T08:51:41+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n   喜欢视频课程的同学一键三连多多支持一下，长按点赞五秒=lv6大佬 可以的发送彩色弹幕哦。\n配套源码项目已打包评论区回复up"
  },
  {
    "id": "bvid:BV11urFBrEc4",
    "domain": "AI",
    "title": "🚀告别Vibe Coding！用Superpowers让Claude Code写出工程级代码，一次通过零报错！遵循TDD最佳实践！支持Codex",
    "url": "http://www.bilibili.com/video/av115877227860495",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 154520,
    "published_at": "2026-01-11T15:43:58+00:00",
    "summary": "🚀开发者必看！Superpowers把专业工程团队方法论固化成Skills，让Claude Code告别越写越乱的困境：规格驱动+代码质量双重保障！AI编程新范式！头脑风暴+计划+执行一条龙自动化\n\n\n🚀🚀🚀 视频简介：\n🎬 本期视频详细演示了开源AI编程工作流系统Superpowers的完整使用方法，并通过开发一款iOS时间线笔记原生应用来实测其效果。\n🔧 核心内容：\nSuperpowers工作"
  },
  {
    "id": "bvid:BV1wugF6YEL3",
    "domain": "AI",
    "title": "再见Claude Code！你好DeepSeek Harness！",
    "url": "http://www.bilibili.com/video/av117089415204498",
    "source": "Lau博士的云组会",
    "platform": "bilibili",
    "points": 138626,
    "published_at": "2026-08-13T17:42:16+00:00",
    "summary": "DeepSeek Harness开源了。看完就两个字：牛逼\n本期视频，Lau博士就带着大家一起，解读DeepSeek 亲手做的这个 Harness，到底有什么不一样。"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 130119,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1dpdZYBE9q",
    "domain": "AI",
    "title": "零代码让AI秒接海量MCP工具！最适合小白的MCP集合平台",
    "url": "http://www.bilibili.com/video/av114340703243255",
    "source": "AI研究室-帆哥",
    "platform": "bilibili",
    "points": 99773,
    "published_at": "2025-04-15T11:00:00+00:00",
    "summary": "最近MCP太火了，阿里直接跟进把MCP整合到百炼平台里面了，做了一个MCP的“应用商店”。\n之前不管是在cursor还是Claude上还是需要配置一下MCP服务器，现在在百炼上就可以直接无脑添加MCP工具，非常方便。\n而且因为在平台上一体化，和大模型可以打包配置，让后端的运维部署变得更轻松。\n这个视频教你怎么用阿里云百炼的MCP工具创建一个agent应用。"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 93180,
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
    "points": 91108,
    "published_at": "2026-07-17T09:10:43+00:00",
    "summary": "视频简介：\n\n月之暗面最新发布的 Kimi K3，拥有2.8万亿参数和100万 Token 上下文窗口，它的真实编程能力究竟怎么样？\n\n本期视频将对 Kimi K3 进行一次完整的高难度编程实测。我们先在官方网页版测试 SVG 手绘灯泡、复杂过河动画、南宋古都轻功游戏和土星自行车比赛，再将 Kimi K3 接入 Claude Code，开发原生 macOS 音乐播放器、侏罗纪坦克射击游戏以及 iO"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 79079,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1xYwgztESh",
    "domain": "AI",
    "title": "Claude Code + PPTSkills  10分钟! 保姆级教程！ 生成可编辑科研汇报 PPT!",
    "url": "http://www.bilibili.com/video/av116234582495649",
    "source": "旭光升",
    "platform": "bilibili",
    "points": 56881,
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
    "points": 54011,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV11DjT6uEhc",
    "domain": "AI",
    "title": "【端侧AI】嵌入式AI教程（基于RK3588）",
    "url": "http://www.bilibili.com/video/av116757511542670",
    "source": "Coder-Dawn",
    "platform": "bilibili",
    "points": 51296,
    "published_at": "2026-06-16T02:57:32+00:00",
    "summary": "从零到一入门级嵌入式AI课程！\n从环境搭建---&gt;模型训练---&gt;模型转换---&gt;模型部署全流程!\n\n视频全部公开免费，资料加入知识库获得(资料费9.9，需要的可滴滴)！"
  },
  {
    "id": "bvid:BV1vYFQzQE4P",
    "domain": "AI",
    "title": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！Claude Code Hooks回调+Agent Teams全自动开发零轮询",
    "url": "http://www.bilibili.com/video/av116046157647899",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 47596,
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
    "points": 43593,
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
    "points": 40484,
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
    "points": 38680,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV1NddKBvEsY",
    "domain": "AI",
    "title": "claude code 桌面端安装并且配置第三方api使用教程，想体验的尽早吧，因为这公司可能不知道哪天抽风就会禁用了！#claude #ai #人工智能",
    "url": "http://www.bilibili.com/video/av116535968466799",
    "source": "菜鸡的老黎",
    "platform": "bilibili",
    "points": 37221,
    "published_at": "2026-05-07T23:56:28+00:00",
    "summary": "claude code 桌面端安装并且配置第三方api使用教程，想体验的尽早吧，因为这公司可能不知道哪天抽风就会禁用了！#claude #ai #人工智能 #agent"
  },
  {
    "id": "bvid:BV1Y6uC6TE1m",
    "domain": "AI",
    "title": "疯狂Vibe Coding一周，我烧了近100亿Token，做了5个项目！",
    "url": "http://www.bilibili.com/video/av117080321957877",
    "source": "神烦老狗",
    "platform": "bilibili",
    "points": 35929,
    "published_at": "2026-08-12T03:12:41+00:00",
    "summary": "项目地址：\nlocal-ops — 本地服务指挥台（零依赖 Python + 原生前端）：https://github.com/laogou717/local-ops\nmd-wechat — 公众号排版工具：https://github.com/laogou717/md-wechat\ndaydream-room — 白日梦陈列室：https://github.com/laogou717/daydr"
  },
  {
    "id": "bvid:BV1cCj2ztEf5",
    "domain": "AI",
    "title": "Cursor+Claude Code+Claude 4终极组合！仅用10分钟为开源项目Magentic-UI完美集成JWT用户认证系统，编程效率提升300%",
    "url": "http://www.bilibili.com/video/av114574527307727",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 35114,
    "published_at": "2025-05-26T14:20:15+00:00",
    "summary": "Cursor+Claude Code+Claude 4终极组合！仅用10分钟为开源项目Magentic-UI完美集成JWT用户认证系统，编程效率提升300%，告别传统开发模式！小白也能轻松开发商业项目\n\n🚀🚀🚀视频简介：\n✅【保姆级教程】从技术栈分析到功能实现：Claude Code完整开发流程深度解析！从零开始为微软开源智能体项目添加完整用户认证功能，支持注册登录退出，让你的AI应用瞬间变身多用"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 34110,
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
    "points": 32367,
    "published_at": "2025-03-09T12:24:12+00:00",
    "summary": "AI编程助手如Trae和Cursor正在革新工程设计领域的CAD绘图流程。传统CAD绘图耗时且易出错，而AI工具通过代码生成技术，能够将自然语言指令转化为精确的代码，自动生成符合标准的CAD图纸，极大提升了设计效率。这些工具不仅支持多模态输入（如图片、草图），还提供了智能代码补全、错误修复等功能，进一步简化了开发流程。随着大模型如deepseek和claude3.7的出现，AI的智能化程度进一步提"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29598,
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
    "points": 28870,
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
    "points": 28637,
    "published_at": "2025-07-04T10:00:00+00:00",
    "summary": "chatbox官网：https://chatboxai.app\ngithub仓库：https://github.com/chatboxai/chatbox\n\nLM Studio教程：BV1usrLYTEZR\nTGW懒人包部署教程：BV1dVCzYUE7G\n本地语言模型个人推荐：BV1Bb421E7j7"
  },
  {
    "id": "bvid:BV11K9gBqEnW",
    "domain": "AI",
    "title": "【杀戮尖塔2】AI MOD 配置教程第一期来辣！手把手教你怎么改提示词！以及如何设计自己的爬塔玩法",
    "url": "http://www.bilibili.com/video/av116341654755924",
    "source": "分歧点WhatIf",
    "platform": "bilibili",
    "points": 26328,
    "published_at": "2026-04-03T16:14:43+00:00",
    "summary": "每个参数都是干什么的，如何修改提示词的教程。\n不知道这是什么？请看合集内的视频~\n我做了一个 AI 的杀戮尖塔2MOD！\n可以和怪物对话，策反怪物，带着怪物爬塔（重写了几乎每一个怪物在友方时候的行为），还能给怪物打防御，带个沙虫全吃了！\n可以和上古之民对话，聊嗨了会给你 1～2 个额外赐福，还能帮你指示为未来\n可以让偷窃草蜢偷队友的 key 卡，想无限？偷了！\n可以和商人讨价还价，甚至白嫖\n多人的"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22701,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operitAI教程：入门安卓最强大ai平台",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 21705,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1gf3T6KEef",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Vibe Coding】教程！从环境搭建到工作流完整闭环，一套全解决！DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116979708990688",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 21440,
    "published_at": "2026-07-25T08:47:37+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1Z5KU6UExC",
    "domain": "AI",
    "title": "【吴恩达2026】Vibe Coding保姆级教程，手把手从环境搭建到工作流完整闭环！——DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116951003242391",
    "source": "吴恩达AIAgent",
    "platform": "bilibili",
    "points": 21289,
    "published_at": "2026-07-20T07:01:13+00:00",
    "summary": "本套课专门解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1zjd3BiEzo",
    "domain": "AI",
    "title": "别再二选一：Claude Code + Codex 联用才是最强姿势",
    "url": "http://www.bilibili.com/video/av116537746791000",
    "source": "星小脉",
    "platform": "bilibili",
    "points": 20046,
    "published_at": "2026-05-08T07:34:23+00:00",
    "summary": "Codex 已悄然追上 Claude Code，GPT 5.5 比肩 Opus 4.7、OpenAI Pro 额度更大方。但作者 Chase 想说：别再纠结谁更好，最佳姿势是把两者一起用——Codex 桌面应用直接跑 Claude Code 终端，让两个模型互查方案、互查代码（一次实测 Claude Code 帮 Codex 抓出 20 个 bug）。背后更重要的思路是 tool agnostic"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 19172,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "hn:49255710",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's Risky Business",
    "url": "https://stratechery.com/2026/nvidias-risky-business/",
    "source": "jonbaer",
    "platform": "hackernews",
    "points": 354,
    "published_at": "2026-08-11T10:02:00+00:00",
    "summary": ""
  },
  {
    "id": "hn:49263340",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Nemotron 3.5 Lightning and NeMo Switchyard",
    "url": "https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/",
    "source": "droidjj",
    "platform": "hackernews",
    "points": 261,
    "published_at": "2026-08-11T19:35:52+00:00",
    "summary": ""
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
    "id": "hn:49257947",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Nemotron 3.5 Lightning",
    "url": "https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-NVFP4",
    "source": "beklein",
    "platform": "hackernews",
    "points": 121,
    "published_at": "2026-08-11T13:26:02+00:00",
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
    "id": "rss:https://www.eetimes.com/smartphone-makers-squeezed-by-soaring-chip-costs/",
    "domain": "AI 算力 / 半导体",
    "title": "Smartphone Makers Squeezed by Soaring Chip Costs",
    "url": "https://www.eetimes.com/smartphone-makers-squeezed-by-soaring-chip-costs/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T18:47:35+00:00",
    "summary": "Chip costs are gutting smartphone margins; expect pricier iPhones and fewer cheap phones. The post Smartphone Makers Squeezed by Soaring Chip Costs appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/enabling-robot-operating-systems/",
    "domain": "AI 算力 / 半导体",
    "title": "Enabling Robot Operating Systems—Introducing the ADI Trinamic Motor Controller ROS1 Driver",
    "url": "https://www.eetimes.com/enabling-robot-operating-systems/",
    "source": "Krizelle Paulene Apostol , Software Systems Engineer, Jamila Macagba , Senior Software Systems Engineer, and Maggie Maralit , Software Systems Design Engineering Manager",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T16:14:17+00:00",
    "summary": "Robot Operating System (ROS) drivers were developed on Analog Devices prod ucts so that they can be readily used within a ROS ecosystem. This article will give an overview on how to use and integrate "
  },
  {
    "id": "rss:https://www.eetimes.com/ais-next-bottleneck-is-public-consent/",
    "domain": "AI 算力 / 半导体",
    "title": "AI’s Next Bottleneck Is Public Consent",
    "url": "https://www.eetimes.com/ais-next-bottleneck-is-public-consent/",
    "source": "Zaheer Ali",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T14:13:06+00:00",
    "summary": "AI’s next choke point isn’t chips—it’s public trust as states slow data centers over power, water, and secrecy. The post AI&#8217;s Next Bottleneck Is Public Consent appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/neuromorphic-computing-needs-more-than-novel-chips/",
    "domain": "AI 算力 / 半导体",
    "title": "Neuromorphic Computing Needs More Than Novel Chips",
    "url": "https://www.eetimes.com/neuromorphic-computing-needs-more-than-novel-chips/",
    "source": "Isaac Lopez, President, OmniScale Media & Charity Plata, Communications Chair, SC26",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T13:00:00+00:00",
    "summary": "Katie Schuman on why neuromorphic computing needs HPC engineers, compilers, and shared hardware access to move from promise to practice. The post Neuromorphic Computing Needs More Than Novel Chips app"
  },
  {
    "id": "rss:https://www.eetimes.com/using-agents-to-maximize-nvidia-jetson-memory-usage-at-the-edge/",
    "domain": "AI 算力 / 半导体",
    "title": "Using Agents to Maximize NVIDIA Jetson Memory Usage at the Edge",
    "url": "https://www.eetimes.com/using-agents-to-maximize-nvidia-jetson-memory-usage-at-the-edge/",
    "source": "Morten Block, Global Eng. Director, Segments and Technology go-to-market",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T12:00:00+00:00",
    "summary": "Discover how NVIDIA Jetson's software optimization stack can reclaim significant memory, enabling teams to run bigger AI workloads at a lower module cost. The post Using Agents to Maximize NVIDIA Jets"
  },
  {
    "id": "rss:https://www.eetimes.com/hong-kong-electronics-fairs-launch-in-october/",
    "domain": "AI 算力 / 半导体",
    "title": "Hong Kong Electronics Fairs Launch in October!",
    "url": "https://www.eetimes.com/hong-kong-electronics-fairs-launch-in-october/",
    "source": "HKTDC",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T08:00:00+00:00",
    "summary": "Cutting-Edge Technologies on Display This October, Shaping the Future of Industries The post Hong Kong Electronics Fairs Launch in October! appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/revolutionizing-safety-unveiling-the-power-of-safety-bubble-detectors-in-robotics/",
    "domain": "AI 算力 / 半导体",
    "title": "Revolutionizing Safety: Unveiling the Power of Safety Bubble Detectors in Robotics",
    "url": "https://www.eetimes.com/revolutionizing-safety-unveiling-the-power-of-safety-bubble-detectors-in-robotics/",
    "source": "Rajesh Mahapatra, Senior Manager, Anil Sripadarao, Principal Engineer, Prasanna Bhat, Engineer, Colm Prendergast, Senior Principal Engineer, Shane O’Meara, Senior Manager, Dara O’Sullivan, Director, Anders Frederiksen, Principal Specialist, and Sagar Walishetti, Engineer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T19:34:18+00:00",
    "summary": "This article will explain the architecture of real-time safety bubble detection that includes challenges for developing a modular solution, optimizing such a high data bandwidth application to run at "
  },
  {
    "id": "rss:https://www.eetimes.com/meta-cuts-server-count-25-by-reusing-old-memory-can-anyone-else-do-it/",
    "domain": "AI 算力 / 半导体",
    "title": "Meta Cuts Server Count 25% by Reusing Old Memory: Can Anyone Else Do It?",
    "url": "https://www.eetimes.com/meta-cuts-server-count-25-by-reusing-old-memory-can-anyone-else-do-it/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T18:40:03+00:00",
    "summary": "Meta squeezes 25% fewer servers from old DDR4 via CXL, but most firms face messy DIMM, power, and telemetry traps. The post Meta Cuts Server Count 25% by Reusing Old Memory: Can Anyone Else Do It? app"
  },
  {
    "id": "rss:https://www.eetimes.com/navigating-gmsl-how-pixel-and-tunnel-modes-enhance-system-performance/",
    "domain": "AI 算力 / 半导体",
    "title": "Navigating GMSL: How Pixel and Tunnel Modes Enhance System Performance",
    "url": "https://www.eetimes.com/navigating-gmsl-how-pixel-and-tunnel-modes-enhance-system-performance/",
    "source": "Flavius Luntrașu , Senior Engineer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T18:34:51+00:00",
    "summary": "This article explores how GMSL™ technology transports high-speed CSI-2 video data and compares the advantages of pixel mode and tunnel mode in modern imaging systems. Learn how each approach impacts d"
  },
  {
    "id": "rss:https://www.eetimes.com/building-supply-chain-resilience-selecting-reliable-capacitor-suppliers/",
    "domain": "AI 算力 / 半导体",
    "title": "Building Supply Chain Resilience: Selecting Reliable Capacitor Suppliers",
    "url": "https://www.eetimes.com/building-supply-chain-resilience-selecting-reliable-capacitor-suppliers/",
    "source": "Shanghai Yongming Electronic Co.,Ltd",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T13:00:00+00:00",
    "summary": "Supply chain stability is becoming a key consideration for companies when selecting electronic components. Discover more! The post Building Supply Chain Resilience: Selecting Reliable Capacitor Suppli"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/prusa-research-xl-core-one-and-core-one-l-all-to-receive-second-generation-upgrades-all-new-orders-get-updated-model-for-free",
    "domain": "AI 算力 / 半导体",
    "title": "Prusa Research XL, Core One, and Core One L all to receive second-generation upgrades — all new orders get updated model for 'free'",
    "url": "https://www.tomshardware.com/3d-printing/prusa-research-xl-core-one-and-core-one-l-all-to-receive-second-generation-upgrades-all-new-orders-get-updated-model-for-free",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T20:35:52+00:00",
    "summary": "Prusa Research just announced that its “entire lineup” of 3D printers is getting second-generation upgrades and a “+” designation. This includes the XL, CORE One, and CORE One L."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/microsofts-nemesis-drops-new-zero-day-privilege-escalation-vulnerability-attack-grants-system-level-privileges-but-it-could-already-be-patched",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft's nemesis drops new zero-day privilege escalation vulnerability — attack grants system-level privileges, but it could already be patched",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/microsofts-nemesis-drops-new-zero-day-privilege-escalation-vulnerability-attack-grants-system-level-privileges-but-it-could-already-be-patched",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T17:36:40+00:00",
    "summary": "Nightmare Eclipse drops ShieldBreak, another Windows zero-day privilege escalation vulnerability, but Microsoft has rushed quickly to block it with Defender"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/near-packaged-optics-gains-ground-aso-the-industry-hedges-against-co-packaged-optics-growing-pains",
    "domain": "AI 算力 / 半导体",
    "title": "Near-packaged optics (NPO) gains ground as the industry hedges against CPO's growing pains — analysts say volume for NPO silicon photonics products will extend until the end of the decade",
    "url": "https://www.tomshardware.com/tech-industry/near-packaged-optics-gains-ground-aso-the-industry-hedges-against-co-packaged-optics-growing-pains",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T16:52:45+00:00",
    "summary": "The case for near-packaged optics (NPO) is strengthening, as the growing pains of co-packaged optics (CPO) become apparent. We explain the material differences between the two technologies as optics a"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/ps5-emulation-arrives-on-steam-deck-astro-playroom-showcased-running-at-0-6-fps-milestone-sharpemu-development-shows-promise-despite-unplayable-performance",
    "domain": "AI 算力 / 半导体",
    "title": "PS5 emulation arrives on Steam Deck, Astro Playroom showcased running at 0.6 FPS — milestone SharpEmu development shows promise, despite unplayable performance",
    "url": "https://www.tomshardware.com/video-games/playstation/ps5-emulation-arrives-on-steam-deck-astro-playroom-showcased-running-at-0-6-fps-milestone-sharpemu-development-shows-promise-despite-unplayable-performance",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T13:37:59+00:00",
    "summary": "Astro's Playroom runs at 0.5 to 1 FPS on the Steam Deck when emulated through SharpEmu. It's not much — it's nothing at all, in fact — but just the proof-of-concept alone is enough to stir up exciteme"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cxmt-overtakes-tencent-to-become-chinas-most-valuable-company-17-days-after-its-ipo",
    "domain": "AI 算力 / 半导体",
    "title": "Memory maker CXMT overtakes Tencent to become China's most valuable company 17 days after its IPO — now worth $524 billion",
    "url": "https://www.tomshardware.com/tech-industry/cxmt-overtakes-tencent-to-become-chinas-most-valuable-company-17-days-after-its-ipo",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T13:27:14+00:00",
    "summary": "ChangXin Memory Technologies (CXMT) is now the world's most valuable Chinese company after passing Tencent."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/mechanical-keyboards/keychron-launches-ludicrous-100-key-custom-macro-pad-10-x-10-keyboard-uses-exclusive-keychron-apex-switches-and-features-per-key-rgb-control",
    "domain": "AI 算力 / 半导体",
    "title": "Keychron launches ludicrous 100-key custom macro pad — 10 x 10 ‘keyboard’ uses ‘exclusive’ Keychron Apex switches and features per-key RGB control",
    "url": "https://www.tomshardware.com/peripherals/mechanical-keyboards/keychron-launches-ludicrous-100-key-custom-macro-pad-10-x-10-keyboard-uses-exclusive-keychron-apex-switches-and-features-per-key-rgb-control",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T13:08:50+00:00",
    "summary": "The Keychron C100 8K macro pad features 100 customizable keys, per-key RGB lighting, and 8K polling rate to give you the ultimate advantage in productivity and gaming. It also has hot-swappable Keychr"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/mini-pcs/geekom-it13-max-2026-review-meteor-lake-rides-again-in-a-usd799-mini-pc",
    "domain": "AI 算力 / 半导体",
    "title": "Geekom IT13 Max 2026 review: Meteor Lake rides again in a $799 mini PC",
    "url": "https://www.tomshardware.com/desktops/mini-pcs/geekom-it13-max-2026-review-meteor-lake-rides-again-in-a-usd799-mini-pc",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T13:05:00+00:00",
    "summary": "Geekom mates an Intel Meteor Lake Core Ultra 9 processor with soldered 24GB DDR5 dual-channel RAM to conjure up an attractively specified and priced mini PC for the RAMpocalypse era."
  },
  {
    "id": "rss:https://www.tomshardware.com/gift-guides-seasonal-sales/best-deals-on-pc-furniture-save-money-on-chairs-desks-monitor-stands-boom-arms-and-more",
    "domain": "AI 算力 / 半导体",
    "title": "Best deals on PC setup accessories — save money on chairs, desks, monitor stands, boom arms, and more",
    "url": "https://www.tomshardware.com/gift-guides-seasonal-sales/best-deals-on-pc-furniture-save-money-on-chairs-desks-monitor-stands-boom-arms-and-more",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T12:30:00+00:00",
    "summary": "We've scoured the internet and found the best deals on PC office and gaming furniture. Find the best desks, chairs, monitor arms, and more."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/motherboards/maxsun-terminator-b850m-pro-ii-motherboard-review",
    "domain": "AI 算力 / 半导体",
    "title": "Maxsun Terminator B850M Pro II Motherboard Review: Comparable features, but US pricing is over MSRP",
    "url": "https://www.tomshardware.com/pc-components/motherboards/maxsun-terminator-b850m-pro-ii-motherboard-review",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T12:05:00+00:00",
    "summary": "Maxsun’s Terminator B850M Pro II is a decent budget option in the Micro ATX form factor, but only if you can find it for the $199.99 MSRP."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/coin-sized-device-can-hack-a-boeing-737s-flight-management-computer-mess-with-takeoff-weights-or-even-divert-an-aircraft-gadget-connects-to-an-easily-accessible-port-that-overrides-commands-from-the-pilots-uses-in-flight-wi-fi",
    "domain": "AI 算力 / 半导体",
    "title": "Coin-sized device can hack a Boeing 737’s Flight Management Computer, mess with takeoff weights, or even divert an aircraft — gadget connects to an easily accessible port that overrides commands from ",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/coin-sized-device-can-hack-a-boeing-737s-flight-management-computer-mess-with-takeoff-weights-or-even-divert-an-aircraft-gadget-connects-to-an-easily-accessible-port-that-overrides-commands-from-the-pilots-uses-in-flight-wi-fi",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T12:04:32+00:00",
    "summary": "Security researchers discovered a way to tap into the avionics of a Boeing 737 and remotely give its flight management computer erroneous data through in-flight Wi-Fi. This coin-sized device plugs int"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ddr5/get-16gb-of-ddr5-ram-free-when-you-buy-amds-9900x-and-an-asus-tuf-motherboard-usd659-newegg-combo-saves-usd274-and-you-get-a-free-240mm-aio",
    "domain": "AI 算力 / 半导体",
    "title": "Get 16GB of DDR5 RAM free when you buy AMD's 9900X and an Asus TUF motherboard — $659 Newegg combo saves $274, and you get a free 240mm AIO",
    "url": "https://www.tomshardware.com/pc-components/ddr5/get-16gb-of-ddr5-ram-free-when-you-buy-amds-9900x-and-an-asus-tuf-motherboard-usd659-newegg-combo-saves-usd274-and-you-get-a-free-240mm-aio",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T11:50:20+00:00",
    "summary": "Save $274 and snag 16GB of DDR5 RAM for free in this 3-item Newegg combo with Ryzen 9 9900X, Asus TUF Gaming X870E-Plus Wifi7, and 16GB of dual channel Team Group T-Force Vulkan RAM"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/zoomsday-vulnerability-let-anyone-in-a-zoom-meeting-take-over-anybody-else-ai-assisted-research-only-used-20-prompts-to-find-an-exploit-to-hack-hundred-of-millions-of-people",
    "domain": "AI 算力 / 半导体",
    "title": "Critical 'Zoomsday' flaw enables total device takeover during Zoom calls — AI-assisted research only used 20 prompts to find an exploit to hack hundreds of millions of people.",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/zoomsday-vulnerability-let-anyone-in-a-zoom-meeting-take-over-anybody-else-ai-assisted-research-only-used-20-prompts-to-find-an-exploit-to-hack-hundred-of-millions-of-people",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T11:20:00+00:00",
    "summary": "Zoomsday vulnerability let anyone in a Zoom meeting take over anybody else. The vulnerability was developed with AI assistance and took research only used 20 prompts to find an exploit to hack hundred"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/controllers-gamepads/this-usd57-99-8bitdo-ultimate-2-wireless-controller-is-a-brilliantly-customizable-option-for-pc-gamers-fully-customizable-gamepad-with-nintendo-switch-compatibility-includes-dual-triggers-tmr-joysticks-and-adjustable-rgb-lighting",
    "domain": "AI 算力 / 半导体",
    "title": "This $57.99 8BitDo Ultimate 2 wireless controller is a brilliantly customizable option for PC gamers — fully customizable gamepad with Nintendo Switch compatibility includes dual triggers, TMR joystic",
    "url": "https://www.tomshardware.com/peripherals/controllers-gamepads/this-usd57-99-8bitdo-ultimate-2-wireless-controller-is-a-brilliantly-customizable-option-for-pc-gamers-fully-customizable-gamepad-with-nintendo-switch-compatibility-includes-dual-triggers-tmr-joysticks-and-adjustable-rgb-lighting",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T11:10:28+00:00",
    "summary": "Save 17% on this 8BitDo Ultimate 2 game controller for your PC or Nintendo Switch right now."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/jump-into-pc-gaming-for-under-a-thousand-dollars-with-a-usd350-saving-on-this-rtx-5060-powered-laptop-the-15-6-inch-msi-cyborg-15-is-just-usd949-at-walmart",
    "domain": "AI 算力 / 半导体",
    "title": "Jump into PC gaming for under a thousand dollars with a $350 saving on this RTX 5060-powered laptop — the 15.6-inch MSI Cyborg 15 is just $949 at Walmart",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/jump-into-pc-gaming-for-under-a-thousand-dollars-with-a-usd350-saving-on-this-rtx-5060-powered-laptop-the-15-6-inch-msi-cyborg-15-is-just-usd949-at-walmart",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T11:07:46+00:00",
    "summary": "Bag a new gaming laptop for under $1K at Walmart, thanks to a $350 saving on the latest MSI Cyborg 15."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/analysts-see-increasing-foundry-success-conviction-as-intel-ceo-puts-usd12-million-more-of-his-own-money-in-company-analysts-point-to-accelerating-foundry-progress-and-capex-expansion",
    "domain": "AI 算力 / 半导体",
    "title": "Analysts see 'increasing foundry success conviction' as Intel CEO puts $12 million more of his own money in company — analysts point to accelerating foundry progress and capex expansion",
    "url": "https://www.tomshardware.com/pc-components/cpus/analysts-see-increasing-foundry-success-conviction-as-intel-ceo-puts-usd12-million-more-of-his-own-money-in-company-analysts-point-to-accelerating-foundry-progress-and-capex-expansion",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T11:00:00+00:00",
    "summary": "Intel's Lip-Bu Ran reportedly buys $12 million worth of Intel stock as analysts believe that the management is increasingly convinced about landing external customers."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/cloud-storage/nine-pbs-loses-access-to-70-years-of-data-after-contracted-cloud-storage-vendor-goes-defunct-public-tv-channel-sues-iron-mountain-data-center-which-hosts-archival-materials-to-ensure-preservation",
    "domain": "AI 算力 / 半导体",
    "title": "PBS broadcaster loses access to 50TB of data comprising 70 years of TV history after contracted cloud storage vendor goes defunct — public TV channel sues Iron Mountain data center, which hosts archiv",
    "url": "https://www.tomshardware.com/software/cloud-storage/nine-pbs-loses-access-to-70-years-of-data-after-contracted-cloud-storage-vendor-goes-defunct-public-tv-channel-sues-iron-mountain-data-center-which-hosts-archival-materials-to-ensure-preservation",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T10:40:00+00:00",
    "summary": "Public broadcaster Nine PBS is in trouble after its cloud storage provider went out of business and it now can't access more than 50TB of archival data. The data center hosting the files can't simply "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/alabama-residents-left-powerless-to-stop-massive-bitcoin-mining-data-center-despite-county-and-town-moratoriums-hole-in-state-zoning-laws-lets-facility-through",
    "domain": "AI 算力 / 半导体",
    "title": "Alabama residents left powerless to stop massive Bitcoin mining data center despite county and town moratoriums — hole in state zoning laws lets facility through",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/alabama-residents-left-powerless-to-stop-massive-bitcoin-mining-data-center-despite-county-and-town-moratoriums-hole-in-state-zoning-laws-lets-facility-through",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T10:20:00+00:00",
    "summary": "Alabama residents left powerless to stop 50 MW Bitcoin mining facility despite county and town moratoriums thanks to the state's lack of appropriate zoning laws."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/portable-monitors/jsaux-flipgo-horizon-pro-dual-screen-portable-monitor-review",
    "domain": "AI 算力 / 半导体",
    "title": "JSAUX FlipGo Horizon Pro dual-screen portable monitor review: Jack of all trades, master of some",
    "url": "https://www.tomshardware.com/monitors/portable-monitors/jsaux-flipgo-horizon-pro-dual-screen-portable-monitor-review",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T10:05:00+00:00",
    "summary": "The FlipGo Horizon Pro brings dual 15.6-inch displays and a built-in hub."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/elon-musk-says-xai-will-increase-data-center-capacity-7x-by-2027-targeting-10-gigawatts-of-compute-up-to-usd500-billion-in-revenue-by-the-end-of-next-year",
    "domain": "AI 算力 / 半导体",
    "title": "Elon Musk says xAI will increase data center capacity 7x by 2027 — targeting 10 gigawatts of compute, up to $500 billion in revenue by the end of next year",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/elon-musk-says-xai-will-increase-data-center-capacity-7x-by-2027-targeting-10-gigawatts-of-compute-up-to-usd500-billion-in-revenue-by-the-end-of-next-year",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T10:00:00+00:00",
    "summary": "Elon Musk expects xAI to increase its nameplate power draw to 10 GW by late 2027, which will increase its performance by orders of magnitude what is available to AI today."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/cerebras-shares-plunge-nearly-20-percent-after-missing-earnings-expectations-hardware-sales-drop-but-ai-cloud-revenue-climbs-281-percent",
    "domain": "AI 算力 / 半导体",
    "title": "Cerebras shares plunge nearly 20% after missing earnings expectations — hardware sales drop but AI cloud revenue climbs 281%",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/cerebras-shares-plunge-nearly-20-percent-after-missing-earnings-expectations-hardware-sales-drop-but-ai-cloud-revenue-climbs-281-percent",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T09:46:20+00:00",
    "summary": "Cerebras keeps growing, but misses forecast as hardware sales dip amid explosive increase of AI cloud revenue."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/the-current-state-of-pcie-6-0-ssds-and-controllers-marvell-phison-and-smi-prepare-controllers-as-drives-finally-come-to-market-following-years-of-delays",
    "domain": "AI 算力 / 半导体",
    "title": "The current state of PCIe 6.0 SSDs and controllers — Marvell, Phison, and SMI prepare controllers as drives finally come to market following years of delays",
    "url": "https://www.tomshardware.com/tech-industry/the-current-state-of-pcie-6-0-ssds-and-controllers-marvell-phison-and-smi-prepare-controllers-as-drives-finally-come-to-market-following-years-of-delays",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T09:40:00+00:00",
    "summary": "PCIe 6.0 SSDs are almost here. We review the state of PCIe 6.0 SSDs and controllers from Micron and Samsung, as well as controllers that can handle 2 Petabyte-class SSDs with 28 TB/s read/write speeds"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/applications/vibe-coded-app-adds-a-3d-video-rental-storefront-to-your-jellyfin-htpc-self-hosted-open-source-project-brings-back-memories-of-browsing-for-vhs-tapes-on-saturday-afternoons",
    "domain": "AI 算力 / 半导体",
    "title": "Vibe-coded app adds a 3D video rental storefront to your Jellyfin HTPC — self-hosted, open-source project brings back memories of browsing for VHS tapes on Saturday afternoons",
    "url": "https://www.tomshardware.com/software/applications/vibe-coded-app-adds-a-3d-video-rental-storefront-to-your-jellyfin-htpc-self-hosted-open-source-project-brings-back-memories-of-browsing-for-vhs-tapes-on-saturday-afternoons",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T09:00:00+00:00",
    "summary": "A Redditor vibe-coded a Jellyfin front-end that mimics that old video rental stores from the 1990s. This simulation is more than just a selection screen, though, and is a complete experience on its ow"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/qualcomm-details-snapdragon-c-specs-for-usd300-laptops-for-the-first-time-claims-67-percent-faster-performance-on-battery-than-intel-n250-ac-performance-remains-a-mystery",
    "domain": "AI 算力 / 半导体",
    "title": "Qualcomm details Snapdragon C specs for $300 laptops for the first time — claims 67% faster performance on battery than Intel N250, AC performance remains a mystery (updated)",
    "url": "https://www.tomshardware.com/pc-components/cpus/qualcomm-details-snapdragon-c-specs-for-usd300-laptops-for-the-first-time-claims-67-percent-faster-performance-on-battery-than-intel-n250-ac-performance-remains-a-mystery",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T21:14:33+00:00",
    "summary": "Qualcomm has detailed the specs for its Snapdragon C processor, with 8 cores and claimed \"all-day\" battery life."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/oracle-plans-more-layoffs-weeks-after-spending-most-of-its-2-1-billion-restructuring-budget",
    "domain": "AI 算力 / 半导体",
    "title": "Oracle plans more layoffs weeks after spending most of its $2.1 billion restructuring budget, report claims — some teams face double-digit percentage reductions, 21,000 full-time positions already eli",
    "url": "https://www.tomshardware.com/tech-industry/oracle-plans-more-layoffs-weeks-after-spending-most-of-its-2-1-billion-restructuring-budget",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T17:00:04+00:00",
    "summary": "Oracle plans to cut more jobs this month, with reductions on some teams reaching double-digit percentages."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-doubles-rtx-pro-6000-blackwells-msrp-to-a-staggering-usd16-000-96gb-card-started-pre-orders-below-usd8-000-last-year",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia doubles RTX PRO 6000 Blackwell's MSRP to a staggering $16,000 — 96GB card started pre-orders below $8,000 last year",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-doubles-rtx-pro-6000-blackwells-msrp-to-a-staggering-usd16-000-96gb-card-started-pre-orders-below-usd8-000-last-year",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T15:53:19+00:00",
    "summary": "A data center GPU has become more expensive because of the AI boom enabled by unprecedented data center buildouts — shocking. Nvidia's RTX 6000 Pro Blackwell is now twice as costly as it was last year"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/ai-data-center-developers-begin-suing-local-jurisdictions-behind-bans-and-moratoriums-claims-range-from-officials-exceeding-authority-to-violations-of-due-process-and-equal-protection-laws",
    "domain": "AI 算力 / 半导体",
    "title": "AI data center developers begin suing local jurisdictions behind bans and moratoriums — claims range from officials exceeding authority to violations of due process and equal protection laws",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/ai-data-center-developers-begin-suing-local-jurisdictions-behind-bans-and-moratoriums-claims-range-from-officials-exceeding-authority-to-violations-of-due-process-and-equal-protection-laws",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T15:46:55+00:00",
    "summary": "Some data center developers are suing local governments for passing temporary bans and moratorium, saying that they such moves violated their rights to due process and equal protection. This move has "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/coreweave-ceo-mike-intrator-says-it-has-signed-an-a100-contract-running-into-2029",
    "domain": "AI 算力 / 半导体",
    "title": "CoreWeave proves Nvidia's aging AI GPUs from 2020 can generate profit nine years after deployment, signs A100 contracts into 2029 — power constraints and legacy infrastructure keep old GPUs profitable",
    "url": "https://www.tomshardware.com/tech-industry/coreweave-ceo-mike-intrator-says-it-has-signed-an-a100-contract-running-into-2029",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T15:41:47+00:00",
    "summary": "CoreWeave reported $2.58 billion in quarterly revenue, up 112% year over year."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/suspected-china-linked-hackers-used-ai-to-run-the-first-ever-end-to-end-autonomous-cyberattack-on-taiwans-government-israeli-firm-says-open-source-built-tool-continuously-devised-effective-hack-strategies-in-real-time",
    "domain": "AI 算力 / 半导体",
    "title": "Suspected China-linked hackers used AI to run the first-ever end-to-end autonomous cyberattack on Taiwan's government, Israeli firm says — open-source-built tool continuously devised effective hack st",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/suspected-china-linked-hackers-used-ai-to-run-the-first-ever-end-to-end-autonomous-cyberattack-on-taiwans-government-israeli-firm-says-open-source-built-tool-continuously-devised-effective-hack-strategies-in-real-time",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T14:58:54+00:00",
    "summary": "Suspected China-linked hackers used autonomous AI agents to breach Taiwanese government systems, compromising 85 accounts and stealing 2,500+ records."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/qidi-plus5-3d-printer-review",
    "domain": "AI 算力 / 半导体",
    "title": "QIDI Plus5 3D printer review: The best one yet",
    "url": "https://www.tomshardware.com/3d-printing/qidi-plus5-3d-printer-review",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T14:08:09+00:00",
    "summary": "QIDI Plus5 is polished, huge, and produces excellent prints with some of the toughest technical filaments."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/nova-lake-cpus-with-cut-down-e-core-clusters-may-still-retain-full-cache-pool-says-new-leak-8p-12e-config-predictions-revised-from-33mb-to-36mb-4p-4e-config-from-15mb-to-18mb",
    "domain": "AI 算力 / 半导体",
    "title": "Nova Lake CPUs with cut-down E-core clusters may still retain full cache pool, says new leak — 8P+12E config predictions revised from 33MB to 36MB, 4P+4E config from 15MB to 18MB",
    "url": "https://www.tomshardware.com/pc-components/cpus/nova-lake-cpus-with-cut-down-e-core-clusters-may-still-retain-full-cache-pool-says-new-leak-8p-12e-config-predictions-revised-from-33mb-to-36mb-4p-4e-config-from-15mb-to-18mb",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T13:37:47+00:00",
    "summary": "A new leak from Jaykihn says some Nova Lake SKUs, including mobile counterparts, will retain the cache config of their fully-enabled variants despite having reduced E-cores."
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
    "id": "hn:49184755",
    "domain": "大厂 AI 动态",
    "title": "Changes at Google DeepMind: Demis Hassabis from CEO to Chair, Jeff Dean departs",
    "url": "https://blog.google/company-news/inside-google/message-ceo/next-chapter-ai-momentum/",
    "source": "colesantiago",
    "platform": "hackernews",
    "points": 864,
    "published_at": "2026-08-05T16:05:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:49289112",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.7 Flash",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/",
    "source": "thisisauserid",
    "platform": "hackernews",
    "points": 698,
    "published_at": "2026-08-13T17:23:22+00:00",
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
    "points": 447,
    "published_at": "2026-08-08T09:18:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:49267928",
    "domain": "大厂 AI 动态",
    "title": "llama.cpp",
    "url": "https://llama.app",
    "source": "kristianpaul",
    "platform": "hackernews",
    "points": 361,
    "published_at": "2026-08-12T04:51:59+00:00",
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
    "id": "hn:49259339",
    "domain": "大厂 AI 动态",
    "title": "Apple Silicon and macOS VMs: Faster LLM Inference with llama.cpp",
    "url": "https://github.com/trycua/cua/blob/main/blog/gpu-passthrough-macos-vms.md",
    "source": "frabonacci",
    "platform": "hackernews",
    "points": 305,
    "published_at": "2026-08-11T14:50:33+00:00",
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
    "id": "hn:49256057",
    "domain": "大厂 AI 动态",
    "title": "What I learned by putting GitHub Copilot behind a MitM proxy",
    "url": "https://www.lighthousenewsletter.com/p/i-put-github-copilot-behind-a-mitm",
    "source": "j0selit0",
    "platform": "hackernews",
    "points": 195,
    "published_at": "2026-08-11T10:40:47+00:00",
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
    "id": "rss:https://www.theverge.com/policy/979977/trump-declares-100-percent-tariffs-on-many-drones-and-all-aircraft-parts",
    "domain": "大厂 AI 动态",
    "title": "Trump declares 100 percent tariffs on many drones and all aircraft parts",
    "url": "https://www.theverge.com/policy/979977/trump-declares-100-percent-tariffs-on-many-drones-and-all-aircraft-parts",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T01:06:15+00:00",
    "summary": "The United States has already banned future foreign drones from entering the United States unless their companies kiss the ring - as well as routers, robots, and Roombas. Now, President Donald Trump i"
  },
  {
    "id": "rss:https://www.theverge.com/tech/979967/apple-epic-games-external-links-fees-filing",
    "domain": "大厂 AI 动态",
    "title": "Apple and Epic argue over how much Apple should get from purchases made outside the App Store",
    "url": "https://www.theverge.com/tech/979967/apple-epic-games-external-links-fees-filing",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T23:13:24+00:00",
    "summary": "In a new filing in its long-running legal dispute with Epic Games, Apple has proposed a structure that would allow it to collect fees on digital purchases made via external links that don't use the co"
  },
  {
    "id": "rss:https://www.theverge.com/policy/979852/that-is-not-acceptable-judge-orders-google-to-make-rival-app-store-installs-easier",
    "domain": "大厂 AI 动态",
    "title": "‘That is not acceptable’: Judge orders Google to make rival app store installs easier",
    "url": "https://www.theverge.com/policy/979852/that-is-not-acceptable-judge-orders-google-to-make-rival-app-store-installs-easier",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T21:53:04+00:00",
    "summary": "One month after Epic Games and Google seemingly stopped fighting over the future of Android app distribution, they were back in a San Francisco courtroom today - where Judge James Donato just ordered "
  },
  {
    "id": "rss:https://www.theverge.com/tech/979869/flock-alpr-ai-surveillance-protest-privacy",
    "domain": "大厂 AI 动态",
    "title": "The fight over Flock and other ALPRs",
    "url": "https://www.theverge.com/tech/979869/flock-alpr-ai-surveillance-protest-privacy",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T21:46:21+00:00",
    "summary": "There are over 120,000 of Flock’s automatic license plate reader (ALPR) cameras installed all over the US. Flock’s cameras, and others like them, use AI to identify and track vehicles based on their l"
  },
  {
    "id": "rss:https://www.theverge.com/tech/979871/microsoft-copilot-mico-retired",
    "domain": "大厂 AI 动态",
    "title": "Microsoft’s Clippy-like Mico character is no longer the face of Copilot",
    "url": "https://www.theverge.com/tech/979871/microsoft-copilot-mico-retired",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T21:42:38+00:00",
    "summary": "Microsoft Copilot will no longer show its emotive yellow blob, Mico, when you use the chatbot's voice mode. In a support page, Microsoft says it's going to move Mico to its Learn Live platform, where "
  },
  {
    "id": "rss:https://www.theverge.com/games/979855/netflix-shut-down-night-school-studio-moonloot-games",
    "domain": "大厂 AI 动态",
    "title": "Netflix is closing two game studios",
    "url": "https://www.theverge.com/games/979855/netflix-shut-down-night-school-studio-moonloot-games",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T20:52:58+00:00",
    "summary": "Netflix plans to shut down two of its gaming studios, as reported by Game File and Variety, as it makes a bigger shift toward party games and titles streamed to TVs. One of the studios being shut down"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/979699/hp-omnibook-x-flip-pixel-buds-pro-2-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "This school-friendly laptop from HP is $300 off",
    "url": "https://www.theverge.com/gadgets/979699/hp-omnibook-x-flip-pixel-buds-pro-2-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T20:07:53+00:00",
    "summary": "With memory prices still high and showing no signs of dropping, we’re always happy to find a good deal on a budget-friendly system with an adequate amount of RAM. Best Buy has the HP OmniBook X Flip d"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/979815/openai-denise-dresser-leaving-executive-departure",
    "domain": "大厂 AI 动态",
    "title": "OpenAI is losing its second executive this week",
    "url": "https://www.theverge.com/ai-artificial-intelligence/979815/openai-denise-dresser-leaving-executive-departure",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T19:28:39+00:00",
    "summary": "Another OpenAI executive is departing. Denise Dresser, who joined OpenAI as its chief revenue officer in December after serving as CEO of Slack, will be leaving in the \"coming weeks\" to \"pursue other "
  },
  {
    "id": "rss:https://www.theverge.com/policy/979734/trump-administration-cybercrime-private-firms",
    "domain": "大厂 AI 动态",
    "title": "The Trump admin will start letting private firms launch international cyberattacks",
    "url": "https://www.theverge.com/policy/979734/trump-administration-cybercrime-private-firms",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T18:56:13+00:00",
    "summary": "The Trump administration is launching a new program that will allow private firms to perform cyberattacks against foreign criminals, as reported earlier by Bloomberg. The private firms would operate \""
  },
  {
    "id": "rss:https://www.theverge.com/tech/978664/robot-lawnmower-review-segway-mammotion-husqvarna-roborock-dreame",
    "domain": "大厂 AI 动态",
    "title": "I finally found a robot lawnmower I’d trust with my yard",
    "url": "https://www.theverge.com/tech/978664/robot-lawnmower-review-segway-mammotion-husqvarna-roborock-dreame",
    "source": "Jennifer Pattison Tuohy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T18:30:00+00:00",
    "summary": "Robot lawnmowers are finally good enough to take a lot of work out of maintaining a yard, but they’re still not set-it-and-forget-it machines. If you don’t want these autonomous cutting machines to te"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/13/investors-sue-selena-gomez-alleging-fraud-tied-to-her-mental-health-startup/",
    "domain": "大厂 AI 动态",
    "title": "Investors sue Selena Gomez alleging fraud tied to her mental health startup",
    "url": "https://techcrunch.com/2026/08/13/investors-sue-selena-gomez-alleging-fraud-tied-to-her-mental-health-startup/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T22:12:40+00:00",
    "summary": "The plaintiffs say they invested nearly $1.2 million in the company, and are accusing Gomez of failing to build and market the startup."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/13/flock-says-its-new-tool-will-help-identify-police-abuse-but-hasnt-explained-how-it-works/",
    "domain": "大厂 AI 动态",
    "title": "Flock says its new tool will help identify police abuse, but hasn’t explained how it works",
    "url": "https://techcrunch.com/2026/08/13/flock-says-its-new-tool-will-help-identify-police-abuse-but-hasnt-explained-how-it-works/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T22:02:04+00:00",
    "summary": "The surveillance company announced it's making a tool called \"Audit Assistance\" mandatory for all customers, claiming it's already helped catch abuse. But the company has yet to explain how the tool w"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/13/if-apple-sends-you-a-push-notification-alerting-you-to-a-spyware-attack-take-it-seriously/",
    "domain": "大厂 AI 动态",
    "title": "If Apple sends you a push notification alerting you to a spyware attack, take it seriously",
    "url": "https://techcrunch.com/2026/08/13/if-apple-sends-you-a-push-notification-alerting-you-to-a-spyware-attack-take-it-seriously/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T21:50:11+00:00",
    "summary": "Apple now sends out push notifications to iPhone lock screens when the company identifies government spyware targeting someone's devices."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/13/writer-introduces-new-ai-model-and-upgraded-harness-to-contain-token-costs/",
    "domain": "大厂 AI 动态",
    "title": "Writer introduces new AI model and upgraded harness to contain token costs",
    "url": "https://techcrunch.com/2026/08/13/writer-introduces-new-ai-model-and-upgraded-harness-to-contain-token-costs/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T21:13:24+00:00",
    "summary": "Built as a post-training variation on Z.ai's open source model GLM-5.2, Writer says the new system should provide deployment-ready capabilities at a much lower price."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/13/databricks-wanted-to-raise-1b-investors-wanted-15b-it-settled-on-5b-at-a-190b-valuation/",
    "domain": "大厂 AI 动态",
    "title": "Databricks wanted to raise $1B, investors wanted $15B. It settled on $5B at a $190B valuation.",
    "url": "https://techcrunch.com/2026/08/13/databricks-wanted-to-raise-1b-investors-wanted-15b-it-settled-on-5b-at-a-190b-valuation/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T20:14:39+00:00",
    "summary": "AI is expensive, Ali Ghodsi tells TechCrunch. With so many investors wanting into his latest round, he said yes to more than planned."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/13/openai-introduces-ultrafast-a-new-mode-that-makes-gpt-5-6-sol-work-at-14x-the-speed/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI introduces ‘Ultrafast,’ a new mode that makes GPT-5.6 Sol work at 14x the speed",
    "url": "https://techcrunch.com/2026/08/13/openai-introduces-ultrafast-a-new-mode-that-makes-gpt-5-6-sol-work-at-14x-the-speed/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T19:22:40+00:00",
    "summary": "OpenAI is launching a preview of a sped up version of its latest, most powerful model, in an effort to court enterprise users."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/13/ibm-partners-with-openai-to-bolster-enterprise-ai-push/",
    "domain": "大厂 AI 动态",
    "title": "IBM partners with OpenAI to bolster enterprise AI push",
    "url": "https://techcrunch.com/2026/08/13/ibm-partners-with-openai-to-bolster-enterprise-ai-push/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T19:19:49+00:00",
    "summary": "IBM plans to train and certify tens of thousands of consultants on OpenAI's technologies as part of this deal."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/13/anthropic-set-ai-agents-loose-on-the-same-task-they-started-a-turf-war/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic set AI agents loose on the same task. They started a turf war.",
    "url": "https://techcrunch.com/2026/08/13/anthropic-set-ai-agents-loose-on-the-same-task-they-started-a-turf-war/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T18:28:14+00:00",
    "summary": "Anthropic researchers found AI agents can clash, collude, and coordinate in unexpected ways, raising new questions about whether today’s safety tests capture the risks of multi-agent systems."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/13/openai-hires-new-cro-as-executive-shake-up-continues/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI hires new CRO as executive shake-up continues",
    "url": "https://techcrunch.com/2026/08/13/openai-hires-new-cro-as-executive-shake-up-continues/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T17:07:13+00:00",
    "summary": "OpenAI has replaced chief revenue officer Denise Dresser after just nine months on the job, tapping Wiz president and chief operating officer Dali Rajic to take on frontier lab's top sales job."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/13/ford-on-track-to-complete-2b-factory-overhaul-for-fathom-ev-truck/",
    "domain": "大厂 AI 动态",
    "title": "Ford on track to complete $2B factory overhaul for Fathom EV truck",
    "url": "https://techcrunch.com/2026/08/13/ford-on-track-to-complete-2b-factory-overhaul-for-fathom-ev-truck/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T16:37:53+00:00",
    "summary": "Ford expects to begin prototype builds of the Fathom EV in the first quarter of 2027."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/13/x-open-sources-its-ranking-algorithm-letting-users-see-if-theyve-been-shadowbanned/",
    "domain": "大厂 AI 动态",
    "title": "X open sources its ranking algorithm, letting users see if they’ve been ‘shadowbanned’",
    "url": "https://techcrunch.com/2026/08/13/x-open-sources-its-ranking-algorithm-letting-users-see-if-theyve-been-shadowbanned/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T16:00:00+00:00",
    "summary": "X is expanding the open source code behind its 'For You' feed and launching new transparency tools that show users when its ranking systems have affected their accounts or posts."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/13/instagram-introduces-a-redesigned-wordmark/",
    "domain": "大厂 AI 动态",
    "title": "Instagram introduces a redesigned wordmark",
    "url": "https://techcrunch.com/2026/08/13/instagram-introduces-a-redesigned-wordmark/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T15:46:02+00:00",
    "summary": "The social media giant says it was time for a sharper and more modern look after a decade."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/13/microsoft-kills-off-unsuccessful-ai-features-while-merging-its-separate-copilot-apps/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft kills off unsuccessful AI features while merging its separate Copilot apps",
    "url": "https://techcrunch.com/2026/08/13/microsoft-kills-off-unsuccessful-ai-features-while-merging-its-separate-copilot-apps/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T15:30:52+00:00",
    "summary": "Microsoft is simplifying Copilot by combining its consumer and business apps, and dropping AI-generated podcasts, Group Chats, Deep Research, and its Mico character."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/13/nvidias-new-500b-plan-is-risky-but-brilliant-especially-for-aging-gpus/",
    "domain": "大厂 AI 动态",
    "title": "Nvidia’s new $500B plan is risky but brilliant, especially for aging GPUs",
    "url": "https://techcrunch.com/2026/08/13/nvidias-new-500b-plan-is-risky-but-brilliant-especially-for-aging-gpus/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T15:08:00+00:00",
    "summary": "Nvidia has a plan to make sure its GPUs won't lose value. It wants to convince a new crop of financiers to keep lending for AI buildouts."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/13/bartesian-duet-cocktail-maker-review/",
    "domain": "大厂 AI 动态",
    "title": "Who really needs a cocktail robot?",
    "url": "https://techcrunch.com/2026/08/13/bartesian-duet-cocktail-maker-review/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T15:00:00+00:00",
    "summary": "Bartesian's cocktail makers would be best described like a Keurig or Nespresso machine, but for alcoholic drinks."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/13/apple-in-talks-to-pay-publishers-to-provide-siri-with-current-news-report/",
    "domain": "大厂 AI 动态",
    "title": "Apple in talks to pay publishers to provide Siri with current news: report",
    "url": "https://techcrunch.com/2026/08/13/apple-in-talks-to-pay-publishers-to-provide-siri-with-current-news-report/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T14:34:43+00:00",
    "summary": "The tech giant has considered a nine-figure budget for the payments, according to the WSJ."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/13/in-a-first-us-will-allow-some-private-firms-to-carry-out-cyberattacks/",
    "domain": "大厂 AI 动态",
    "title": "In a first, US will allow some private firms to carry out cyberattacks",
    "url": "https://techcrunch.com/2026/08/13/in-a-first-us-will-allow-some-private-firms-to-carry-out-cyberattacks/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T14:09:05+00:00",
    "summary": "The new order sweeps away decades of existing U.S. cybersecurity policy prohibiting private companies from conducting 'hack back' attacks or offensive cyber operations."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/13/can-social-media-start-over-blueskys-ceo-and-coo-deliver-their-case-at-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "Can social media start over? Bluesky’s CEO and COO deliver their case at TechCrunch Disrupt 2026",
    "url": "https://techcrunch.com/2026/08/13/can-social-media-start-over-blueskys-ceo-and-coo-deliver-their-case-at-techcrunch-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T13:30:00+00:00",
    "summary": "Bluesky CEO Toni Schneider is joined by COO Rose Wang for a Disrupt Stage session on whether social media can start over and where Bluesky fits into that potential reboot."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/12/ai-nuclear-power-firm-fermi-finally-has-a-new-ceo/",
    "domain": "大厂 AI 动态",
    "title": "AI nuclear power firm Fermi finally has a new CEO",
    "url": "https://techcrunch.com/2026/08/12/ai-nuclear-power-firm-fermi-finally-has-a-new-ceo/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T22:24:00+00:00",
    "summary": "Lee McIntire, an independent member of Fermi's board, has been hired as CEO, more than three months since the company fired co-founder Toby Neugebauer from the top post."
  },
  {
    "id": "rss:https://stratechery.com/2026/anthropics-watermarking-how-it-probably-works-worse-than-it-seems/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic’s Watermarking, How It (Probably) Works, Worse Than It Seems",
    "url": "https://stratechery.com/2026/anthropics-watermarking-how-it-probably-works-worse-than-it-seems/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T10:00:00+00:00",
    "summary": "Anthropic is adding watermarking in response to the E.U.'s AI law. It's a terrible idea, first and foremost for philosophical reasons."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/08/us-wait-times-for-cancer-surgeries-are-getting-longer-and-longer/",
    "domain": "大厂 AI 动态",
    "title": "US wait times for cancer surgeries are getting longer and longer",
    "url": "https://arstechnica.com/health/2026/08/us-wait-times-for-cancer-surgeries-are-getting-longer-and-longer/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T22:17:29+00:00",
    "summary": "Study finds wait times for cancer surgeries hit 10-year high."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/08/white-house-recruits-security-firms-to-hack-overseas-cybercriminals/",
    "domain": "大厂 AI 动态",
    "title": "Private security firms will soon be allowed to hack overseas cybercriminals",
    "url": "https://arstechnica.com/security/2026/08/white-house-recruits-security-firms-to-hack-overseas-cybercriminals/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T19:38:58+00:00",
    "summary": "Trump memo is first time gov't has authorized private sector to perform cyberattacks."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/08/virgin-galactic-wants-your-help-naming-its-new-delta-class-spaceship/",
    "domain": "大厂 AI 动态",
    "title": "Virgin Galactic wants your help naming its new Delta class spaceship",
    "url": "https://arstechnica.com/space/2026/08/virgin-galactic-wants-your-help-naming-its-new-delta-class-spaceship/",
    "source": "Robert Pearlman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T19:12:15+00:00",
    "summary": "Will it be the VSS... Horizon, Explorer, Ascend or Apeiron?"
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/08/ukrainian-drones-wipe-out-entire-us-tank-brigade-in-live-war-game/",
    "domain": "大厂 AI 动态",
    "title": "Ukrainian drones wipe out entire US tank brigade in live war game",
    "url": "https://arstechnica.com/gadgets/2026/08/ukrainian-drones-wipe-out-entire-us-tank-brigade-in-live-war-game/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T18:31:56+00:00",
    "summary": "Ukrainian drone pilots teach the US military and NATO hard battlefield lessons."
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
    "points": 116,
    "published_at": "2026-08-04T09:27:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:49261857",
    "domain": "股票",
    "title": "The SpaceX Sham",
    "url": "https://dissentmagazine.org/online_articles/spacex-ipo-elon-musk-trillionaire/",
    "source": "cdrnsf",
    "platform": "hackernews",
    "points": 38,
    "published_at": "2026-08-11T17:47:03+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3779421",
    "domain": "股票",
    "title": "创业板冲高回落涨0.65%，稀土拉升，算力硬件大涨，恒科指跌近2%，京东大跌10%、华虹宏力跌12%",
    "url": "https://wallstreetcn.com/articles/3779421",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:17:33+00:00",
    "summary": "盘面上，个股跌多涨少，沪深京三市超3600股飘绿，上午半天成交1.4万亿。沪深两市半日成交额1.39万亿，较上个交易日缩量超2000亿。板块方面，文化传媒、电力、教育、房地产、医药、零售、金融板块跌幅靠前；稀土、工业金属、PCB、CPO概念股活跃。"
  },
  {
    "id": "wscn:3779429",
    "domain": "股票",
    "title": "日本前财务官警告：日元干预随时可能重演，日本央行应加快加息步伐",
    "url": "https://wallstreetcn.com/articles/3779429",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T03:59:00+00:00",
    "summary": "日本财务省前财务官古泽满宏发出强烈警告：日元汇率\"明显过弱\"，干预随时可能重演，日美联手行动不排除。9月加息概率已从24%骤升至76%，终极利率或升至1.75%。高盛提示，一旦日本央行加快紧缩，套利交易平仓压力将向全球股债汇市蔓延。"
  },
  {
    "id": "wscn:3779420",
    "domain": "股票",
    "title": "Anthropic 2万亿美元IPO背后的神秘女人：掌门夫人Cami Clark",
    "url": "https://wallstreetcn.com/articles/3779420",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T03:47:49+00:00",
    "summary": "当Anthropic冲刺逾2万亿美元IPO之际，一个从未出现在组织架构图上的名字正受到华尔街前所未有的审视——CEO Dario Amodei之妻Cami Clark。她将前谷歌CEO Schmidt引入早期投资，曾向爱泼斯坦为成人影片公司募资，还筹划过\"AGI之母基金\"。这位刻意隐身的\"影子顾问\"，正以难以量化的方式左右着全球最炙手可热的AI公司命运。"
  },
  {
    "id": "wscn:3779425",
    "domain": "股票",
    "title": "FDE×Harness --从模型能力转向企业规模化部署",
    "url": "https://wallstreetcn.com/articles/3779425",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T03:42:12+00:00",
    "summary": "企业AI的真正瓶颈已不在于模型能力，而在于能否将AI稳定嵌入核心业务流程。国泰海通分析师最新研报指出，FDE（前线部署工程师）与Agent运行时系统Harness的协同，正成为规模化落地的关键路径——前者将现场经验转化为可复用资产，后者保障智能体稳定执行。价值链正从\"谁的模型更强\"，迁移至\"谁能交付生产系统、谁能把一次经验复用到下一次\"。"
  },
  {
    "id": "wscn:3779424",
    "domain": "股票",
    "title": "央行8月开展万亿级买断式逆回购，首度月中启用隔夜逆回购",
    "url": "https://wallstreetcn.com/articles/3779424",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T03:38:55+00:00",
    "summary": "8月14日，中国人民银行开展10000亿元6个月期买断式逆回购，实现等量续做，同日还首次在月中税期开展3490亿元隔夜逆回购，单日净投放3480亿元。此举旨在精准应对税期资金需求，体现\"削峰填谷\"的细粒度调控意图。受流动性充裕提振，10年期国债收益率降至1.68%，创2025年7月以来新低。"
  },
  {
    "id": "wscn:3779428",
    "domain": "股票",
    "title": "小熊电器上半年净利下降4成  海外增长未能对冲国内压力",
    "url": "https://wallstreetcn.com/articles/3779428",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T03:21:23+00:00",
    "summary": "母婴小家电同比下降22.88%"
  },
  {
    "id": "wscn:3779427",
    "domain": "股票",
    "title": "迅雷二季度营收增长近4成，海外直播扩张压低毛利率",
    "url": "https://wallstreetcn.com/articles/3779427",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T03:19:40+00:00",
    "summary": "增长是真的，赚钱是难的"
  },
  {
    "id": "wscn:3779426",
    "domain": "股票",
    "title": "AI痕迹追踪简史：你的机器写稿记号早被发现了",
    "url": "https://wallstreetcn.com/articles/3779426",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T03:14:17+00:00",
    "summary": "溯源这件小事"
  },
  {
    "id": "wscn:3779351",
    "domain": "股票",
    "title": "逆周期加码与流动性破局：宽松条件是否已具备？",
    "url": "https://wallstreetcn.com/premium/articles/3779351?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T02:09:14+00:00",
    "summary": "银行负债缺口、政府债供给高峰与资金回笼压力叠加，宽松客观条件正在逐步成熟。"
  },
  {
    "id": "wscn:3779418",
    "domain": "股票",
    "title": "网友热议DeepSeek Harness：“自进化软件”的雏形",
    "url": "https://wallstreetcn.com/articles/3779418",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T00:56:29+00:00",
    "summary": "内测用户指出DSH具备\"自进化\"雏形，Agent可自主编写并挂载插件，但当前动态插件重启即消失，仍属实验阶段。对此，有开发者认为\"软件自进化\"是伪命题。此外，DSH启动依赖Node.js工具链，用户体验有待改善，插件生态繁荣的前提是积累足够多的普通用户。"
  },
  {
    "id": "wscn:3779367",
    "domain": "股票",
    "title": "从328MW到5GW：SOFC为何突然站上AI数据中心的主电源牌桌？",
    "url": "https://wallstreetcn.com/premium/articles/3779367?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T00:48:41+00:00",
    "summary": "Nebius再次把SOFC推到AI电力投资的中心，公司将2026年末签约电力目标上调至5GW，并明确解释从燃烧式发电切换Bloom Energy的原因：更快交付之外，低噪音、低用水和相对友好的许可条件同样重要。当AI数据中心同时面对电源、电网、设备、时间和审批约束，电源选择正在从单纯比较度电成本，转向比较“何时能拿到可运营的电”。Bloom订单和收入进入GW级兑现后，下一阶段真正值得跟踪的是什么？"
  },
  {
    "id": "wscn:3779403",
    "domain": "股票",
    "title": "逼近历史警戒线！美债长端融资成本飙升，30年期得标利率创2001年最高",
    "url": "https://wallstreetcn.com/articles/3779403",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T00:47:01+00:00",
    "summary": "美国30年期国债标售得标利率飙至5.216%，创2001年以来新高；10年期利率亦触及2007年以来峰值。需求总量尚存，但海外央行配置比例骤降逾10个百分点，一级交易商被迫兜底。财政赤字、供给扩张与期限溢价三重压力叠加，长端收益率已与货币政策预期脱钩，美国长期融资成本正逼近本世纪警戒线。"
  },
  {
    "id": "wscn:3779419",
    "domain": "股票",
    "title": "高盛点评闪迪“炸裂投资者日”：长期财务指引远超预期，100%超额自由现金流回馈股东",
    "url": "https://wallstreetcn.com/articles/3779419",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T00:39:38+00:00",
    "summary": "高盛认为， 闪迪投资者日发布FY28-30长期指引，毛利率80%、营业利润率75%，远超预期；承诺将100%超额自由现金流回购股票，剩余回购额度达155亿美元。长期客户协议（NBM）已覆盖逾940亿美元合同价值，为业绩提供可见性。HBF高带宽闪存技术有望切入AI推理市场，构成额外上行期权。"
  },
  {
    "id": "wscn:3779417",
    "domain": "股票",
    "title": "“AI云两强”CoreWeave和Nebius业绩强劲！算力租赁价格大涨，短期合同溢价显著",
    "url": "https://wallstreetcn.com/articles/3779417",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T00:38:12+00:00",
    "summary": "AI算力供不应求，租赁价格正在创历史新高。Nebius首次Blackwell芯片拍卖成交价较历史最高价高出15%，CoreWeave 7月直接宣布整体提价25%。短期合同溢价尤为显著，Nebius每兆瓦年化合同价值已突破4000万美元。逻辑是，客户如果需要“立即可用”的算力，就必须为稀缺性付出溢价。"
  },
  {
    "id": "wscn:3779343",
    "domain": "股票",
    "title": "汇丰财富洞察：美联储减少前瞻性指引对美国利率意味着什么？|汇听环球财富",
    "url": "https://wallstreetcn.com/premium/articles/3779343?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T00:14:47+00:00",
    "summary": "美联储强调依赖经济数据做出决策，这意味着利率预期可能会更频繁地发生变化，导致市场波动加剧。我们..."
  },
  {
    "id": "wscn:3779415",
    "domain": "股票",
    "title": "真正的“油价危机”：全球炼油中心大面积停摆，华尔街警告“成品油完美风暴”",
    "url": "https://wallstreetcn.com/articles/3779415",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T00:11:30+00:00",
    "summary": "霍尔木兹危机持续五个月，真正的震荡正在成品油市场引爆：美国柴油裂解价差盘中突破97美元/桶逼近历史极值，全球四大炼油中心三个陷入停摆，中东出口骤降、俄罗斯禁售，美国被迫独撑全球供应却库存告急。美银警告，除非供应出现实质性复苏，柴油市场将在明年相当长时间内维持紧张、波动和高价格状态。"
  },
  {
    "id": "wscn:3779413",
    "domain": "股票",
    "title": "冲刺IPO，OpenAI年化收入已达400亿美元",
    "url": "https://wallstreetcn.com/articles/3779413",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T00:04:13+00:00",
    "summary": "OpenAI年化营收已超400亿美元，较去年底翻倍，7月环比增速超20%。增长主要由AI编程工具、订阅业务及AI Agent企业需求驱动，同时已对部分模型降价以应对Anthropic及开源竞争。"
  },
  {
    "id": "wscn:3779414",
    "domain": "股票",
    "title": "美防长称可“无限期”海上封锁，伊朗称“若条件得不到满足 或升级冲突”，胡塞武装再袭沙特炼油厂",
    "url": "https://wallstreetcn.com/articles/3779414",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T23:58:10+00:00",
    "summary": "美官员称，美军拟派“华盛顿”号替换超期部署的“林肯”号航母以维持封锁。对此，伊朗高官警告将采取升级行动回应，指责美国无力保护盟友，并呼吁建立摆脱美国的地区新秩序。此外，胡塞武装近日连续使用无人机精准打击沙特阿美公司炼油厂。"
  },
  {
    "id": "wscn:3779397",
    "domain": "股票",
    "title": "这个投资者日，闪迪的“炸裂数字”震撼市场",
    "url": "https://wallstreetcn.com/articles/3779397",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T23:49:21+00:00",
    "summary": "闪迪预计，2028至2030财年，非GAAP口径下，公司毛利率维持在约80%，营业利润率约75%，调整后自由现金流利润率约50%；承诺在完成业务投资后，剩余现金100%返还股东；长期输入比特量增长目标为中高双位数，但可供销售的比特量将根据优化盈利能力的需要灵活调整；披露八大客户签长协，协议已覆盖2028财年约三分之二比特出货量；2030年企业级闪存TAM料达1.2ZB。"
  },
  {
    "id": "wscn:3779338",
    "domain": "股票",
    "title": "美PPI数据再缓加息压力，标普新高，美存储股大涨，闪迪飙涨近14%，原油结束连涨",
    "url": "https://wallstreetcn.com/articles/3779338",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T23:23:10+00:00",
    "summary": "标普500指数涨0.65%，纳指涨0.81%。特斯拉涨超3.5%，领涨科技七巨头。存储股西部数据、海力士涨逾7%。受收购报道影响，Workday一度飙升30%。美国9月加息预期收窄，对利率敏感的两年期美债收益率跌4.82个基点。现货黄金跌1.34%，现货白银跌1.43%。原油跌超2%。"
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
    "id": "hn:49257407",
    "domain": "股票",
    "title": "I backtested my own stock rankings. They lost to the index",
    "url": "https://holderdashboard.com/learn/backtest-that-lost-to-the-index",
    "source": "caiocmpaes",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-08-11T12:44:43+00:00",
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
    "id": "hn:49177126",
    "domain": "股票",
    "title": "It looks like 'Big Short' investor Michael Burry nailed bet against chip stocks",
    "url": "https://www.businessinsider.com/big-short-michael-burry-ai-chip-stocks-soxx-nvidia-substack-2026-8",
    "source": "mapping365",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-08-05T00:30:23+00:00",
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
    "points": 13,
    "published_at": "2026-08-02T16:09:26+00:00",
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
    "id": "hn:49245487",
    "domain": "金融",
    "title": "Study links GLP-1 drugs to bigger jump in women's employment than a degree",
    "url": "https://finance.yahoo.com/healthcare/articles/harvard-study-links-glp-1-123000637.html",
    "source": "metadat",
    "platform": "hackernews",
    "points": 131,
    "published_at": "2026-08-10T16:02:34+00:00",
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
    "id": "hn:49245071",
    "domain": "金融",
    "title": "Force-Fed by ICE",
    "url": "https://www.theguardian.com/us-news/2026/aug/10/ice-force-feeding-detention-gabar-choli",
    "source": "HotGarbage",
    "platform": "hackernews",
    "points": 97,
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
    "points": 55,
    "published_at": "2026-08-10T13:40:46+00:00",
    "summary": ""
  },
  {
    "id": "hn:49289340",
    "domain": "金融",
    "title": "Hooray for index funds–just don't call them passive",
    "url": "https://www.economist.com/finance-and-economics/2026/08/11/hooray-for-index-funds-just-dont-call-them-passive",
    "source": "thm",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-08-13T17:37:33+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.12363",
    "domain": "金融",
    "title": "EU-ETS under attack? The impact of carbon price suppression on the decarbonization of the power sector",
    "url": "https://arxiv.org/abs/2608.12363",
    "source": "Javier Gonzalez-Ruiz, Carlos Rodriguez-Pardo, Alice Di Bella, Paolo Mastropietro, Jose Pablo Chavez-Avila, Massimo Tavoni",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2608.12363v1 Announce Type: new Abstract: European countries are debating policies to mitigate the increased energy costs caused by renewed geopolitical tensions, while pursuing decarbonization "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.12424",
    "domain": "金融",
    "title": "AI-Driven Multiscenario Interest Rate Forecasting: A Proof of Concept for Banking Asset Management",
    "url": "https://arxiv.org/abs/2608.12424",
    "source": "Ekkehardt Bauer, Dirk Holl\\\"ander, Linus Wolff, Christoph Ostermair, Kyrillus Aiad, Joachim Hasebrook",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2608.12424v1 Announce Type: new Abstract: This study focuses on developing an AI-supported prototype for multiperspective interest rate forecasting that combines classical econometric models wit"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.12493",
    "domain": "金融",
    "title": "Beyond the Skew-Stickiness Ratio: Transport Geometry of Spot-Driven Variance Surface Dynamics",
    "url": "https://arxiv.org/abs/2608.12493",
    "source": "Charlie Che, Pradeepta Das",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2608.12493v1 Announce Type: new Abstract: We develop a geometric theory of arbitrage-free implied variance surface dynamics. Smile dynamics are formulated as transport flows on the admissible cl"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.12583",
    "domain": "金融",
    "title": "Diffusion Models in Finance: A Survey",
    "url": "https://arxiv.org/abs/2608.12583",
    "source": "Zhuohan Wang, Carmine Ventre",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2608.12583v1 Announce Type: new Abstract: Diffusion generative models have rapidly emerged as powerful tools for modeling complex financial data. Their appeal is both structural and practical: t"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.12587",
    "domain": "金融",
    "title": "DYSANOS Generative Dynamic Smooth Arbitrage-free Non-parametric Option Surfaces",
    "url": "https://arxiv.org/abs/2608.12587",
    "source": "Hans Buehler, Blanka Horvath, Anastasis Kratsios",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2608.12587v1 Announce Type: new Abstract: This article presents with DYSANOS the first generative market model for smooth SANOS option surfaces for all strikes and expiries which are free of sta"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.12594",
    "domain": "金融",
    "title": "What Makes a Peer? Valuation-Anchored Similarity in Private Markets",
    "url": "https://arxiv.org/abs/2608.12594",
    "source": "Sebastian Frank, Jingrao Lyu, Max Jarmey, Preetha Saha, Mingshu Li, Sweet Kaur, Sola Akinola, Dhagash Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2608.12594v1 Announce Type: new Abstract: As more investors contemplate private markets and contend with limited transparency, sparse disclosures, and infrequent transactions, identifying econom"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.12634",
    "domain": "金融",
    "title": "The Price of Permission: Classification Uncertainty in Constrained Capital Markets",
    "url": "https://arxiv.org/abs/2608.12634",
    "source": "Abdulrahman Qadi, Akash Sharma, Francesca Medda",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2608.12634v1 Announce Type: new Abstract: Shariah-compliant equity screening provides a transparent setting in which institutional rules determine who may own a stock. A binary label identifies "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.12667",
    "domain": "金融",
    "title": "Does life-satisfaction inequality measure societal inequality? A focal-value-rounding critique",
    "url": "https://arxiv.org/abs/2608.12667",
    "source": "C. P. Barrington-Leigh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2608.12667v1 Announce Type: new Abstract: The dispersion of self-reported life satisfaction has been proposed and used as a comprehensive measure of societal inequality. A negative cross-country"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.12777",
    "domain": "金融",
    "title": "Physical Extinction and Long-Run Pricing under Time-Varying Beliefs",
    "url": "https://arxiv.org/abs/2608.12777",
    "source": "Sourav Majumdar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2608.12777v1 Announce Type: new Abstract: An investor may be optimistic about aggregate endowment growth at some times and pessimistic at others. The weight placed on her forecast in bond valuat"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.13056",
    "domain": "金融",
    "title": "Simulating Stress Laws under Extremal Dependence: Characterizing What Generative Models Must Preserve",
    "url": "https://arxiv.org/abs/2608.13056",
    "source": "Mantu Gupta, Anand Deo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2608.13056v1 Announce Type: new Abstract: We study stress-scenario generation for systems driven by multivariate heavy-tailed risk factors. Within regions where several financial losses are simu"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.13082",
    "domain": "金融",
    "title": "LOB-ID: Evaluating Synthetic Market Data by Inception Distances",
    "url": "https://arxiv.org/abs/2608.13082",
    "source": "Andreea Bacalum, Zhuohan Wang, Ollie Olby, Martin Garaj, Namid Stillman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2608.13082v1 Announce Type: new Abstract: Generative models of limit orderbook (LOB) data have advanced rapidly, but their evaluation often focuses on stylised facts and selected market statisti"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.13340",
    "domain": "金融",
    "title": "Fee Implied Volatility on Uniswap v3: A DEX Native Proxy and Its Limits",
    "url": "https://arxiv.org/abs/2608.13340",
    "source": "Amy Oumayma Khaldoun",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2608.13340v1 Announce Type: new Abstract: Narrow Uniswap v3 liquidity ranges resemble short dated options, and Panoptic's streaming premium echoes the short maturity concentration of Black-Schol"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.13096",
    "domain": "金融",
    "title": "FlowLOB: Efficient and Controllable Limit Order Book Generation with Flow Matching",
    "url": "https://arxiv.org/abs/2608.13096",
    "source": "Zhuohan Wang, Andreea Bacalum, Ollie Olby, Carmine Ventre, Namid Stillman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2608.13096v1 Announce Type: cross Abstract: Limit order book (LOB) simulators are most useful to practitioners when they combine realistic market dynamics, computationally efficient sampling, co"
  },
  {
    "id": "rss:https://arxiv.org/abs/2212.03931",
    "domain": "金融",
    "title": "A Better Test of Choice Overload",
    "url": "https://arxiv.org/abs/2212.03931",
    "source": "Mark Dean, Dilip Ravindran, J\\\"org Stoye",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2212.03931v4 Announce Type: replace Abstract: Choice overload - in which larger choice sets are detrimental to a chooser's well-being - is potentially of great importance in the design of econom"
  },
  {
    "id": "rss:https://arxiv.org/abs/2506.14614",
    "domain": "金融",
    "title": "Pricing options on the cryptocurrency futures contracts",
    "url": "https://arxiv.org/abs/2506.14614",
    "source": "Julia Ko\\'nczal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2506.14614v2 Announce Type: replace Abstract: The cryptocurrency options market is notable for its high volatility and lower liquidity compared to traditional markets. These characteristics intr"
  },
  {
    "id": "rss:https://arxiv.org/abs/2601.09541",
    "domain": "金融",
    "title": "Designing Ad Auctions with Targeting Information",
    "url": "https://arxiv.org/abs/2601.09541",
    "source": "Srinivas Tunuguntla, Carl F. Mela, Jason Pratt",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2601.09541v2 Announce Type: replace Abstract: Digital advertising publishers sell ad inventory that conveys targeting information, such as demographic, contextual, or behavioral audience segment"
  },
  {
    "id": "rss:https://arxiv.org/abs/2603.16108",
    "domain": "金融",
    "title": "Short-horizon Duesenberry Equilibrium",
    "url": "https://arxiv.org/abs/2603.16108",
    "source": "Jaime Alberto Londo\\~no",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2603.16108v3 Announce Type: replace Abstract: We develop a continuous-time general equilibrium framework for an infinite heterogeneous population whose household types are transported by a Brown"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.03274",
    "domain": "金融",
    "title": "Financial Dynamics and Interconnected Risk of Liquid Restaking",
    "url": "https://arxiv.org/abs/2604.03274",
    "source": "Hasret Ozan Sevim, Christof Ferreira Torres",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2604.03274v2 Announce Type: replace Abstract: Decentralized finance introduces new business models and use cases as part of digital finance. Restaking has recently emerged as a transformative me"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.03499",
    "domain": "金融",
    "title": "Marking-Aware Sequential VaR Recalibration for Standardized Option Books",
    "url": "https://arxiv.org/abs/2604.03499",
    "source": "Tenghan Zhong, Keyuan Wu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2604.03499v3 Announce Type: replace Abstract: Daily Value-at-Risk (VaR) for option books requires more than an accurate quantile forecast. It first requires a precise definition of the loss targ"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.06116",
    "domain": "金融",
    "title": "Sequential Audit Sampling for Finite Populations with Exact and Simulation-based Guarantee",
    "url": "https://arxiv.org/abs/2604.06116",
    "source": "Masahiro Kato, Kei Nakagawa",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2604.06116v2 Announce Type: replace Abstract: Financial statement auditors use a risk-based approach to evidence collection to obtain reasonable assurance. When an initial sample does not suppor"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.16448",
    "domain": "金融",
    "title": "On the Expected Maximum Deficit and the Optimal Allocation of Reserves",
    "url": "https://arxiv.org/abs/2605.16448",
    "source": "Claude Lefevre, Pierre Zuyderhoff",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2605.16448v2 Announce Type: replace Abstract: Let $L$ be a c\\`adl\\`ag net-loss process and $M_t=\\sup_{0\\le s\\le t}L_s$. We study the distorted expected maximum deficit $$ D_g^{(t)}(u)=\\int_u^\\in"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.23347",
    "domain": "金融",
    "title": "Beyond the Margin: Targeted Conservation and Household Water Demand",
    "url": "https://arxiv.org/abs/2606.23347",
    "source": "Andrea Albertazzi, Elisabetta Leni, Ennio Bilancini",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2606.23347v2 Announce Type: replace Abstract: Non-price interventions targeting specific household water uses are increasingly central to conservation policy, but whether end-use savings transla"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.04753",
    "domain": "金融",
    "title": "Fooling Yourself: how narratives shape beliefs",
    "url": "https://arxiv.org/abs/2607.04753",
    "source": "Andrea Albertazzi, Paolo Pin, Marco Stimolo, Alessandro Stringhi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2607.04753v2 Announce Type: replace Abstract: Decision-makers often receive information through narratives combining diagnostic evidence, which favors one state over another, with nondiagnostic "
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.25353",
    "domain": "金融",
    "title": "How Likely and How Deep? Sharp Joint Bounds on Risk-Neutral Crash Probability and Conditional Depth from Option Bid-Ask Quotes",
    "url": "https://arxiv.org/abs/2607.25353",
    "source": "Jirong Zhuang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2607.25353v3 Announce Type: replace Abstract: Option quotes with bid-ask spreads do not point-identify the risk-neutral probability of a crash below a given threshold, nor the expected depth of "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.05755",
    "domain": "金融",
    "title": "Cross-Sectional Heterogeneity in LSTM Networks for Financial Time Series",
    "url": "https://arxiv.org/abs/2608.05755",
    "source": "Julius D\\\"obelt",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2608.05755v2 Announce Type: replace Abstract: Predicting financial asset returns remains one of the most difficult challenges in empirical finance, driven by the low signal-to-noise ratio and th"
  },
  {
    "id": "rss:https://arxiv.org/abs/2410.02091",
    "domain": "金融",
    "title": "The Impact of Generative AI on Collaborative Open-Source Software Development: Evidence from GitHub Copilot",
    "url": "https://arxiv.org/abs/2410.02091",
    "source": "Fangchen Song, Ashish Agarwal, Wen Wen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2410.02091v4 Announce Type: replace-cross Abstract: Generative artificial intelligence (AI) facilitates content production and enhances ideation, with potentially important implications for deve"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.12508",
    "domain": "金融",
    "title": "Interoperability Effects: Extending DeFi Lending Risk Models to Multi-Chain Environments",
    "url": "https://arxiv.org/abs/2605.12508",
    "source": "Hasret Ozan Sevim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2605.12508v2 Announce Type: replace-cross Abstract: On-chain lending has expanded across multiple distributed ledgers as DeFi becomes increasingly multi-chain. This environment introduces novel "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.29018",
    "domain": "金融",
    "title": "Liquidity-Based Audit of Algorithmic Trading Strategies",
    "url": "https://arxiv.org/abs/2606.29018",
    "source": "Irene Aldridge",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2606.29018v2 Announce Type: replace-cross Abstract: We show that net demand for liquidity by algo strategies is identifiable from its trade and price history alone, with no knowledge of its sign"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.11344",
    "domain": "金融",
    "title": "Governing Agentic AI in FinTech",
    "url": "https://arxiv.org/abs/2608.11344",
    "source": "Henry Han",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2608.11344v2 Announce Type: replace-cross Abstract: Financial institutions are delegating consequential decisions to agentic AI systems that decompose goals, coordinate models and tools, and act"
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
    "id": "hn:49111879",
    "domain": "金融",
    "title": "Citadel Buys Situational Awareness's Stock Portfolio After Big Losses in AI",
    "url": "https://www.wsj.com/finance/citadel-buys-situational-awarenesss-stock-portfolio-after-big-losses-in-ai-5117159b",
    "source": "mudil",
    "platform": "hackernews",
    "points": 54,
    "published_at": "2026-07-30T16:00:33+00:00",
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
    "points": 42,
    "published_at": "2026-08-05T15:24:38+00:00",
    "summary": ""
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
  }
]
```
