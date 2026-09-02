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

- 今日日期：`2026-09-02`
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
  "date": "2026-09-02",
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
    "points": 4414003,
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
    "points": 1791549,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV14rzQB9EJj",
    "domain": "AI",
    "title": "Claude Code 从 0 到 1 全攻略：MCP / SubAgent / Agent Skill / Hook / 图片 / 上下文处理/ 后台任务",
    "url": "http://www.bilibili.com/video/av115954889596221",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 1295272,
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
    "points": 1226972,
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
    "points": 1142232,
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
    "points": 880556,
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
    "points": 683705,
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
    "points": 674907,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1aDMezREUj",
    "domain": "AI",
    "title": "Cursor使用教程，2小时玩转cursor，cursor无限续杯",
    "url": "http://www.bilibili.com/video/av114691716154833",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 586610,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV1RSFUzVEAG",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Claude Code】教程！大模型入门到进阶，一套全解决！Claude Code探索-测试-重构-调试代码库—附带课件代码",
    "url": "http://www.bilibili.com/video/av116045469783373",
    "source": "吴恩达的AI课",
    "platform": "bilibili",
    "points": 578038,
    "published_at": "2026-02-10T08:59:28+00:00",
    "summary": "【吴恩达】2026年公认最好的【Claude Code】教程！大模型入门到进阶，一套全解决！Claude Code探索-测试-重构-调试代码库—附带课件代码"
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 441263,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1vG8QzcE5X",
    "domain": "AI",
    "title": "Claude使用指南，claude code零基础教程，claude code安装配置到实战",
    "url": "http://www.bilibili.com/video/av114933744272468",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 353295,
    "published_at": "2025-07-30T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从概念到安装，再到Claude Code的具体使用，开发效率原地起飞！"
  },
  {
    "id": "bvid:BV1ia9UBPESQ",
    "domain": "AI",
    "title": "在VScode中配置Claude Code并接入DeepSeek V4 Pro【oo唠嗑教程】",
    "url": "http://www.bilibili.com/video/av116487012549813",
    "source": "沉默的羔丸ovo",
    "platform": "bilibili",
    "points": 320903,
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
    "points": 278870,
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
    "points": 263771,
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
    "points": 252341,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 180435,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 177315,
    "published_at": "2026-04-27T08:51:41+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n   喜欢视频课程的同学一键三连多多支持一下，长按点赞五秒=lv6大佬 可以的发送彩色弹幕哦。\n配套源码项目已打包评论区回复up"
  },
  {
    "id": "bvid:BV16NvCBrEVs",
    "domain": "AI",
    "title": "什么是Vibe Coding，以及怎么使用？",
    "url": "http://www.bilibili.com/video/av115797133368973",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 164451,
    "published_at": "2025-12-28T12:36:33+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 161577,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 155032,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1nM6dBdER6",
    "domain": "AI",
    "title": "vscode如何使用AI编程",
    "url": "http://www.bilibili.com/video/av115875633960242",
    "source": "波哥的编程课",
    "platform": "bilibili",
    "points": 138196,
    "published_at": "2026-01-11T08:58:44+00:00",
    "summary": "如何在vs code中使用AI进行开发，推荐了国产AI编程助手，包括安装扩展、注册登录、选择模型、生成代码和微调代码等步骤。同时，强调AI编程还有很多复杂方面，欢迎在评论区留言。"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 105317,
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
    "points": 93511,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 54707,
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
    "points": 47674,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 41295,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operitAI教程：入门安卓最强大ai平台",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 37398,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1AGRtBnE3S",
    "domain": "AI",
    "title": "别手动写测试用例了!2026最新Claude Code+Skills实现需求文档生成全量用例|全流程AI驱动软件测试落地方案,测试效率翻10倍！",
    "url": "http://www.bilibili.com/video/av116528787756865",
    "source": "清风说测试开发",
    "platform": "bilibili",
    "points": 32728,
    "published_at": "2026-05-07T00:00:00+00:00",
    "summary": "全栈课一共分为6大块内容\n第一块：AI智能体开发基础(AI大模型、工具、记忆、MCP、中间件、Skills等核心内容)\n第二块：Claude Code,Trea+skills实现基于需求文档生成用例，基于OpenClaw实现接口自动化落地，基于hermes Agent实现web自动化落地\n第三块：功能测试的智能体开发(项目RAG知识库搭建+Agent搭建+skills开发，实现用例生成的Agent"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 30444,
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
    "points": 28907,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1Z5KU6UExC",
    "domain": "AI",
    "title": "【吴恩达2026】Vibe Coding保姆级教程，手把手从环境搭建到工作流完整闭环！——DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116951003242391",
    "source": "吴恩达AIAgent",
    "platform": "bilibili",
    "points": 23247,
    "published_at": "2026-07-20T07:01:13+00:00",
    "summary": "本套课专门解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22753,
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
    "points": 20818,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV14erKYuEaE",
    "domain": "AI",
    "title": "最强编程AI Cursor+Unity制作一个史诗游戏(详细)",
    "url": "http://www.bilibili.com/video/av113774908413987",
    "source": "多西杰克",
    "platform": "bilibili",
    "points": 17781,
    "published_at": "2025-01-05T09:01:00+00:00",
    "summary": "网上惊呼Cursor AI厉害的内容很多，但结合Unity做游戏的不多，我就来实测一下，做一个AAA大作......"
  },
  {
    "id": "bvid:BV1N4tH6GE2h",
    "domain": "AI",
    "title": "Anthropic重磅史诗升级！Claude Code 2.0全自动模式深度实测，多智能体协同全自动写完项目！",
    "url": "http://www.bilibili.com/video/av117184256810815",
    "source": "进化中的阿陈",
    "platform": "bilibili",
    "points": 16790,
    "published_at": "2026-08-30T11:39:11+00:00",
    "summary": "程序员彻底被解放了！Anthropic 重磅发布 Claude Code 2.0！新增王炸级 Auto Mode 全自动模式，无需人工确认全自动写完复杂项目；多 Sub-Agents 智能体协同并行开发，原生内置 iOS 模拟器实时调试 App 与无头浏览器测试，配合 Opus 5 简直强到离谱，速看实测！"
  },
  {
    "id": "bvid:BV1iDRQBrEF6",
    "domain": "AI",
    "title": "Claude + Blender 现在太强了 —— 完整免费设置",
    "url": "http://www.bilibili.com/video/av116543333601720",
    "source": "设计之道",
    "platform": "bilibili",
    "points": 16599,
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
    "points": 15803,
    "published_at": "2025-03-30T02:06:00+00:00",
    "summary": "在这门包含10节课的课程中，我们将带你从概念到代码，全面覆盖构建AI代理的基础知识。在这里找到完整的“AI代理入门”课程及代码示例\nhttps://github.com/microsoft/ai-agents-for-beginners\n\nP01 什么是AI代理\nP02 使用哪种AI代理框架\nP03 如何设计优秀的AI代理\nP04 什么是代理工具使用设计模式\nP05 什么是代理式RAG\nP06 如"
  },
  {
    "id": "bvid:BV1nChG6nEY4",
    "domain": "AI",
    "title": "韦东山老师教你用 DeepSeek 与 Claude Code，在 Ubuntu 中搭建嵌入式 Linux AI 开发环境：从安装配置到代码智能辅助开发实战",
    "url": "http://www.bilibili.com/video/av117155165177009",
    "source": "韦东山",
    "platform": "bilibili",
    "points": 13955,
    "published_at": "2026-08-25T08:22:35+00:00",
    "summary": "韦东山老师手把手教你在 Ubuntu 中搭建嵌入式 AI 开发环境，完整介绍开发工具、VMware Tools、中文输入法、VS Code 与常用插件的安装配置，以及 DeepSeek API Key 和 Claude Code 的接入方法。借助 AI 大模型完成代码分析、工程理解、问题排查和辅助开发，让嵌入式 Linux 学习与开发更加高效。\n查看完整文字教程：https://www.100as"
  },
  {
    "id": "bvid:BV1eMgG6QEeG",
    "domain": "AI",
    "title": "【吴恩达】这绝对是把《Vibe Coding》讲得最通透的一套课！手把手教你构建自己的企业级AI工作流，学完直接落地！——附带课件代码",
    "url": "http://www.bilibili.com/video/av117081815189025",
    "source": "吴恩达Agents",
    "platform": "bilibili",
    "points": 13452,
    "published_at": "2026-08-12T09:29:57+00:00",
    "summary": "Vibe Coding火了，但你会发现——AI写的代码像开盲盒，今天能跑明天崩，项目一大就乱套。\n规范驱动开发（SDD） 就是来解决这个问题的。它的核心理念很简单：在让AI写代码之前，先和AI在统一的规范文档里对齐需求，把开发变成可预测、可追溯、可控制的过程。"
  },
  {
    "id": "bvid:BV1HhGo6aEvE",
    "domain": "AI",
    "title": "本地大模型也能联网搜索！LM Studio × MCP 接入教程",
    "url": "http://www.bilibili.com/video/av116635490911881",
    "source": "aopstudio",
    "platform": "bilibili",
    "points": 11991,
    "published_at": "2026-05-25T13:41:46+00:00",
    "summary": "本视频演示如何为 LM Studio 接入 MCP 联网搜索服务，让本地运行的大模型具备实时搜索网络的能力。\nMCP（Model Context Protocol）是 Anthropic 推出的开放协议，允许模型通过标准化接口调用外部工具。本次接入的搜索服务来自 MCPWorld，底层通过 npx 调用，无需额外部署服务端，配置完成后即可在 LM Studio 的对话界面中直接发起联网搜索。\n本视"
  },
  {
    "id": "bvid:BV1zbduYgEBH",
    "domain": "AI",
    "title": "Cursor新手教程⑤：Cursor降智真相+解决办法",
    "url": "http://www.bilibili.com/video/av114311359891940",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 10914,
    "published_at": "2025-04-10T02:53:27+00:00",
    "summary": "你是不是经常碰到这种情况：\n你试图修复一个小错误\n人工智能给出一个看似合理的更改建议\n这个修复导致其他地方出错\n你要求人工智能修复新出现的问题\n这又产生了另外两个问题\n如此反复\n本视频带你拆解Cursor降智的真相以及解决办法"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 9930,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
  },
  {
    "id": "bvid:BV1zJuz6NEgJ",
    "domain": "AI",
    "title": "重量级！我用 Agent 重做了角色扮演体验：一句脑洞生成属于自己的酒馆世界",
    "url": "http://www.bilibili.com/video/av117076932953852",
    "source": "Soul_糖",
    "platform": "bilibili",
    "points": 9645,
    "published_at": "2026-08-11T12:48:17+00:00",
    "summary": "做了一个新项目：Nora&#x27;s Tavern。\n\n简单说，就是把 Agent 接进酒馆流程里。\n你不用一上来就手搓角色卡、世界书、开场剧情，只要先说一句脑洞，Nora 会帮你把角色身份、关系线、冲突和第一幕搭出来。\n\n这期先用“芙宁娜演出结束后的世界”做个演示。\n后面继续更新导入角色卡、修改世界、双端使用和 Nora 养成。"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 9464,
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
    "points": 9093,
    "published_at": "2025-06-04T07:08:58+00:00",
    "summary": "全程干货无废话！MCP最新实战教程，从环境部署、原理详解到项目实战，带你彻底吃透MCP！MCPServer开发，mcp开发，mcp教程，mcp项目 完整视频教程+讲解课件+学习笔记+AI大模型知识库已打包可分享！"
  },
  {
    "id": "bvid:BV12MEg6pE9o",
    "domain": "AI",
    "title": "【乐鑫教程】乐鑫文档 MCP 服务器上线，现已支持微信登录！",
    "url": "http://www.bilibili.com/video/av116713957956440",
    "source": "乐鑫信息科技",
    "platform": "bilibili",
    "points": 9015,
    "published_at": "2026-06-08T10:17:31+00:00",
    "summary": "手把手教你如何使用最新乐鑫文档知识库，帮你在 Claude / Cursor 等平台解答问题、生成代码、迁移 ESP-IDF 版本、烧录固件。 MCP 服务器现已支持微信扫码一键登录，快来一试！\n\n视频重点内容包括👇：\n\n- 如何将 MCP 服务器添加到 VS Code\n- 让 Copilot 基于乐鑫文档对比旧版和最新版 I2C 驱动\n- 驱动迁移\n- Copilot 编译代码、烧录代码并监控输"
  },
  {
    "id": "bvid:BV1xh3C6cEGv",
    "domain": "AI",
    "title": "两周完成一篇SCI论文，用claude code帮你干",
    "url": "http://www.bilibili.com/video/av117002408559933",
    "source": "博士大师兄木水",
    "platform": "bilibili",
    "points": 8525,
    "published_at": "2026-07-29T08:53:04+00:00",
    "summary": "大师兄八股文SCI速成模板已制作成skill，手把手带你实现一键生成SCI论文初稿"
  },
  {
    "id": "bvid:BV1RxLg6FEkx",
    "domain": "AI",
    "title": "AI编程利器cursor+codex，草图变代码实现屏显",
    "url": "http://www.bilibili.com/video/av116583162774844",
    "source": "郭天祥老师",
    "platform": "bilibili",
    "points": 7606,
    "published_at": "2026-05-16T07:53:18+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1NP546xEUj",
    "domain": "AI",
    "title": "5分钟安装Claudecode并进入deepseek",
    "url": "http://www.bilibili.com/video/av116555396419337",
    "source": "宝藏女嗨沈幼楚",
    "platform": "bilibili",
    "points": 7359,
    "published_at": "2026-05-11T10:11:25+00:00",
    "summary": "-"
  },
  {
    "id": "hn:49458161",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia agrees to acquire Hugging Face for $13B",
    "url": "https://www.businessinsider.com/nvidia-in-talks-to-buy-hugging-face-13-billion-dollars-2026-8",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 1981,
    "published_at": "2026-08-27T01:12:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:49434378",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI Jalapeño: Better than Nvidia Blackwell",
    "url": "https://newsletter.semianalysis.com/p/openai-jalapeno-better-than-nvidia",
    "source": "bmulholland",
    "platform": "hackernews",
    "points": 584,
    "published_at": "2026-08-25T14:06:02+00:00",
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
    "id": "rss:https://www.eetimes.com/from-silos-to-systems-from-data-to-insight/",
    "domain": "AI 算力 / 半导体",
    "title": "From Silos to Systems, from Data to Insight: Unlocking Organizational Knowledge and Winning in the AI Era with Keysight SOS Enterprise",
    "url": "https://www.eetimes.com/from-silos-to-systems-from-data-to-insight/",
    "source": "Keysight Technologies",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T03:41:26+00:00",
    "summary": "The white paper introduces Keysight SOS Enterprise as an AI-ready engineering data and IP management platform designed to help semiconductor and electronics companies centrally manage, govern, and sec"
  },
  {
    "id": "rss:https://www.eetimes.com/exclusive-sir-robin-saxby-reflects-on-impact-of-ai-geopolitics-and-retirement/",
    "domain": "AI 算力 / 半导体",
    "title": "Exclusive: Sir Robin Saxby Reflects on Impact of AI, Geopolitics, and Retirement",
    "url": "https://www.eetimes.com/exclusive-sir-robin-saxby-reflects-on-impact-of-ai-geopolitics-and-retirement/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T22:00:00+00:00",
    "summary": "An EE Times exclusive video interview with Sir Robin Saxby, founding CEO of Arm, on industry transformation in the age of AI, geopolitics, and how retirement has allowed him to support new startups. T"
  },
  {
    "id": "rss:https://www.eetimes.com/how-ai-is-reshaping-the-global-semiconductor-patent-landscape/",
    "domain": "AI 算力 / 半导体",
    "title": "How AI Is Reshaping the Global Semiconductor Patent Landscape",
    "url": "https://www.eetimes.com/how-ai-is-reshaping-the-global-semiconductor-patent-landscape/",
    "source": "Stefani Munoz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T16:32:49+00:00",
    "summary": "AI is turning chip patents into a geopolitical battle for dominance, from Nvidia’s CUDA moat to China’s filing surge. The post How AI Is Reshaping the Global Semiconductor Patent Landscape appeared fi"
  },
  {
    "id": "rss:https://www.eetimes.com/opportunity-charging-enabled-by-fast-charging-multivoltage-batteries/",
    "domain": "AI 算力 / 半导体",
    "title": "Opportunity Charging Enabled by Fast Charging MultiVoltage Batteries",
    "url": "https://www.eetimes.com/opportunity-charging-enabled-by-fast-charging-multivoltage-batteries/",
    "source": "Green Cubes Technology",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T14:56:51+00:00",
    "summary": "While opportunity charging is a practice applicable to both Lead Acidand Lithium-ion (Li-ion) batteries for motive power systems, fast charging is a key differentiator for Lithium-ion batteries. Becau"
  },
  {
    "id": "rss:https://www.eetimes.com/the-future-of-cable-testing-why-intelligent-automation-is-replacing-manual-validation/",
    "domain": "AI 算力 / 半导体",
    "title": "The Future of Cable Testing: Why Intelligent Automation is Replacing Manual Validation",
    "url": "https://www.eetimes.com/the-future-of-cable-testing-why-intelligent-automation-is-replacing-manual-validation/",
    "source": "Vitrek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T14:39:23+00:00",
    "summary": "This whitepaper examines the limitations of manual cable validation processes and explores how automated testing strategies help address common engineering and manufacturing pain points. Topics includ"
  },
  {
    "id": "rss:https://www.eetimes.com/the-link-budget-is-decided-at-the-connector/",
    "domain": "AI 算力 / 半导体",
    "title": "The Link Budget Is Decided at the Connector",
    "url": "https://www.eetimes.com/the-link-budget-is-decided-at-the-connector/",
    "source": "Vivek Raghuraman, CEO and co-founder of Mixx Technologies.",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T14:27:31+00:00",
    "summary": "Scale-up optics will be decided by the link budget. The largest recoverable losses sit at the connector and inside the silicon photonics platform. The post The Link Budget Is Decided at the Connector "
  },
  {
    "id": "rss:https://www.eetimes.com/from-silos-to-systems-from-data-to-insight-unlocking-organizational-knowledge-and-winning-in-the-ai-era-with-keysight-sos-enterprise/",
    "domain": "AI 算力 / 半导体",
    "title": "From Silos to Systems, from Data to Insight : Unlocking Organizational Knowledge and Winning in the AI Era with Keysight SOS Enterprise",
    "url": "https://www.eetimes.com/from-silos-to-systems-from-data-to-insight-unlocking-organizational-knowledge-and-winning-in-the-ai-era-with-keysight-sos-enterprise/",
    "source": "Keysight Technologies",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T14:00:00+00:00",
    "summary": "The white paper introduces Keysight SOS Enterprise as an AI-ready engineering data and IP management platform designed to help semiconductor and electronics companies centrally manage, govern, and sec"
  },
  {
    "id": "rss:https://www.eetimes.com/monitoring-pv-efficiency-fault-detection/",
    "domain": "AI 算力 / 半导体",
    "title": "Monitoring PV Efficiency & Fault Detection",
    "url": "https://www.eetimes.com/monitoring-pv-efficiency-fault-detection/",
    "source": "Applications for Reed Relays",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T14:00:00+00:00",
    "summary": "Solar PV installations rely on ongoing monitoring to maintain energy yield, uptime and safe operation throughout their working life. This application guide explains how insulation degradation can crea"
  },
  {
    "id": "rss:https://www.eetimes.com/inside-rochester-electronics-tls360-program/",
    "domain": "AI 算力 / 半导体",
    "title": "Inside Rochester Electronics’ TLS360™ Program",
    "url": "https://www.eetimes.com/inside-rochester-electronics-tls360-program/",
    "source": "Rochester Electronics",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T13:00:00+00:00",
    "summary": "For engineers working on long-lifecycle systems such as aerospace and defense platforms, industrial controls, medical devices, and transportation infrastructure, obsolescence is a recurring, costly ce"
  },
  {
    "id": "rss:https://www.eetimes.com/solid-state-relays-for-thermostat-design/",
    "domain": "AI 算力 / 半导体",
    "title": "Solid-State Relays for Thermostat Design",
    "url": "https://www.eetimes.com/solid-state-relays-for-thermostat-design/",
    "source": "Vince Wen, Product Marketing Engineer, Monolithic Power Systems, Inc. (MPS)",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T13:00:00+00:00",
    "summary": "Mechanical relay vs. solid-state relay for thermostat design: compare lifespan, switching speed, power loss, EMI, and PCB space using the MP9566. The post Solid-State Relays for Thermostat Design appe"
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/alienwares-new-qd-oled-gaming-monitors-boast-4k-165-hz-1080p-560-hz-panels-dells-new-oleds-target-gamers-who-prioritize-speed-or-crave-pixel-density",
    "domain": "AI 算力 / 半导体",
    "title": "Alienware's new QD-OLED gaming monitors boast 4K 165 Hz, 1080p 560 Hz panels — Dell’s new OLEDs target gamers who prioritize speed or crave pixel density",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/alienwares-new-qd-oled-gaming-monitors-boast-4k-165-hz-1080p-560-hz-panels-dells-new-oleds-target-gamers-who-prioritize-speed-or-crave-pixel-density",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T07:00:00+00:00",
    "summary": "Alienware’s AW3226Q and AW2527HX gaming monitors target two different segments of the market."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/dells-new-14-inch-laptops-take-on-the-macbook-neo-in-a-new-way-ports-and-colors",
    "domain": "AI 算力 / 半导体",
    "title": "Dell's new 14-inch laptops take on the MacBook Neo in a new way — ports and colors",
    "url": "https://www.tomshardware.com/laptops/dells-new-14-inch-laptops-take-on-the-macbook-neo-in-a-new-way-ports-and-colors",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T07:00:00+00:00",
    "summary": "Dell's new 14S laptops are mainstream devices with more colors and more ports than the XPS 13."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-pours-usd3-5-billion-into-mediatek-company-will-adopt-nvlink-fusion-for-its-custom-ai-accelerators",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia pours $3.5 billion into MediaTek — company will adopt NVLink Fusion for its custom AI accelerators",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-pours-usd3-5-billion-into-mediatek-company-will-adopt-nvlink-fusion-for-its-custom-ai-accelerators",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T14:42:22+00:00",
    "summary": "Nvidia invests $3.5 billion in MediaTek as the companies expand their partnership into custom AI infrastructure with NVLink Fusion, local AI computing, and automotive platforms."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/alienware-16x-aurora-review",
    "domain": "AI 算力 / 半导体",
    "title": "Alienware 16X Aurora review: A thoroughly competent gaming laptop",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/alienware-16x-aurora-review",
    "source": "Charles Jefferies",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T14:31:18+00:00",
    "summary": "The Alienware 16X Aurora pairs a gorgeous 240 Hz OLED display with solid performance, sturdy build quality, and strong upgradeability, though its size and battery life limit portability."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidias-controversial-dlss-5-will-launch-september-3-with-nba2k27-available-on-all-rtx-50-series-gpus-laptops-and-geforce-now",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's controversial DLSS 5 will launch September 3 with NBA2K27, company shares first benchmarks — available on all RTX 50 series GPUs, laptops, and GeForce NOW",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidias-controversial-dlss-5-will-launch-september-3-with-nba2k27-available-on-all-rtx-50-series-gpus-laptops-and-geforce-now",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T13:00:00+00:00",
    "summary": "Nvidia has confirmed DLSS 5 will launch on September 3 in NBA2K27. It will be supported on all RTX 50 series GPUs, laptops, and GeForce NOW."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidias-top-end-rtx-5090-gaming-gpu-now-costs-at-least-usd5-000-blackwell-cards-continue-to-endure-drastic-price-hikes",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's top-end RTX 5090 gaming GPU now costs at least $5,000 — Blackwell cards continue to endure drastic price hikes",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidias-top-end-rtx-5090-gaming-gpu-now-costs-at-least-usd5-000-blackwell-cards-continue-to-endure-drastic-price-hikes",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T12:04:18+00:00",
    "summary": "The entire PC hardware industry is in shambles when it comes to consumer products, and GPUs are one of the most affected components. Everything from budget options to high-end models is now significan"
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/national-telecoms-provider-to-make-usd2-7-billion-selling-old-copper-in-ai-boom-bt-to-strip-200-000-tons-from-legacy-network",
    "domain": "AI 算力 / 半导体",
    "title": "National telecoms provider could make $2.7 billion selling recycled copper in AI boom — BT to strip 200,000 tons from legacy network",
    "url": "https://www.tomshardware.com/networking/national-telecoms-provider-to-make-usd2-7-billion-selling-old-copper-in-ai-boom-bt-to-strip-200-000-tons-from-legacy-network",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T12:00:00+00:00",
    "summary": "The UK's largest telecommunications company, BT, could potentially make $2.7 billion as it recycles all the old copper in its network as it upgrades to fiber optic. The massive amount is driven by the"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/chinese-court-freezes-318-million-in-nexperia-assets-as-wingtech-presses-to-regain-control",
    "domain": "AI 算力 / 半导体",
    "title": "Chinese court freezes $318 million in Nexperia assets as Wingtech presses to regain control — Dutch chipmaker says seizures won't affect day-to-day operations",
    "url": "https://www.tomshardware.com/tech-industry/chinese-court-freezes-318-million-in-nexperia-assets-as-wingtech-presses-to-regain-control",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T11:57:20+00:00",
    "summary": "The total value of the frozen assets exceeds Wingtech’s entire first-half revenue, with the company reporting 1.51 billion yuan in H1 2026 sales, down more than 90% year over year."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/blindlock-hides-your-password-manager-and-secure-vault-in-a-png-image-also-offers-secure-notes-2fa-and-a-crypto-address-book-with-optional-hardware-security-keys",
    "domain": "AI 算力 / 半导体",
    "title": "BlindLock hides your password manager and secure vault in a PNG image — also offers secure notes, 2FA, and a crypto address book, with optional hardware security keys",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/blindlock-hides-your-password-manager-and-secure-vault-in-a-png-image-also-offers-secure-notes-2fa-and-a-crypto-address-book-with-optional-hardware-security-keys",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T11:45:16+00:00",
    "summary": "A new local‑only password manager, notes app, and secure vault that hides your secrets in an ordinary-looking .PNG image file is now available."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/save-usd300-on-this-240hz-oled-gaming-laptop-with-an-rtx-5070-ti-now-just-usd1-899-acer-predator-helios-rig-ships-with-a-24-core-intel-cpu-32gb-ddr5-and-a-1tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Save $300 on this 240Hz OLED gaming laptop with an RTX 5070 Ti, now just $1,899 — Acer Predator Helios rig ships with a 24-core Intel CPU, 32GB DDR5 and a 1TB SSD",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/save-usd300-on-this-240hz-oled-gaming-laptop-with-an-rtx-5070-ti-now-just-usd1-899-acer-predator-helios-rig-ships-with-a-24-core-intel-cpu-32gb-ddr5-and-a-1tb-ssd",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T11:27:25+00:00",
    "summary": "This Acer Predator Helios Neo 16S AI gaming laptop has dropped to just $1,899.99, giving you a high-end rig with an RTX 5070 Ti, 32GB DDR5 and a 1TB SSD."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/usd899-gets-you-a-fully-fledged-ddr5-gaming-pc-in-best-buys-labor-day-sales-save-usd300-off-the-ibuypower-slate-pc-powered-by-intels-b570-graphics-with-10gb-of-vram",
    "domain": "AI 算力 / 半导体",
    "title": "$899 gets you a fully fledged DDR5 gaming PC in Best Buy's Labor Day sales — save $300 off the iBuypower Slate PC powered by Intel's B570 graphics with 10GB of VRAM",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/usd899-gets-you-a-fully-fledged-ddr5-gaming-pc-in-best-buys-labor-day-sales-save-usd300-off-the-ibuypower-slate-pc-powered-by-intels-b570-graphics-with-10gb-of-vram",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T11:20:38+00:00",
    "summary": "Save $300 on a brand-new iBuypower Slate gaming PC in the Best Buy Labor Day sales."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/hot-chips-2026-samsung-reveals-a-three-phase-hbm-roadmap-that-puts-logic-and-compute-inside-memory-zhbm-ultimately-stacks-dram-directly-on-top-of-the-processor",
    "domain": "AI 算力 / 半导体",
    "title": "Hot Chips 2026: Samsung reveals a three-phase HBM roadmap that puts logic and compute inside memory — zHBM ultimately stacks DRAM directly on top of the processor",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/hot-chips-2026-samsung-reveals-a-three-phase-hbm-roadmap-that-puts-logic-and-compute-inside-memory-zhbm-ultimately-stacks-dram-directly-on-top-of-the-processor",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T11:06:15+00:00",
    "summary": "Samsung detailed a three-phase HBM roadmap at Hot Chips 2026 that progressively moves logic into the base die and ultimately stacks DRAM directly on the processor."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/cxmt-reportedly-begins-risk-production-of-hbm3e-memory-in-breakthrough-for-chinese-dram-production-company-could-be-in-mass-production-in-2027",
    "domain": "AI 算力 / 半导体",
    "title": "CXMT reportedly begins risk production of HBM3E memory in breakthrough for Chinese DRAM production — company could be in mass production in 2027",
    "url": "https://www.tomshardware.com/pc-components/dram/cxmt-reportedly-begins-risk-production-of-hbm3e-memory-in-breakthrough-for-chinese-dram-production-company-could-be-in-mass-production-in-2027",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T10:30:00+00:00",
    "summary": "CXMT is reportedly sampling its HBM3E memory with Alibaba Group's T-Head and Cambricon Technologies."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/console-gaming/playstation-store-buy-button-class-action-may-never-reach-a-courtroom",
    "domain": "AI 算力 / 半导体",
    "title": "Sony argues ‘reasonable consumers would not be misled’ into believing they own digital games in class action motion — PlayStation Store ‘buy’ button lawsuit may never reach a courtroom",
    "url": "https://www.tomshardware.com/video-games/console-gaming/playstation-store-buy-button-class-action-may-never-reach-a-courtroom",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T10:00:00+00:00",
    "summary": "Sony Interactive Entertainment asked a federal judge to push a proposed class action lawsuit over the PlayStation Store’s “buy” and “purchase” labels out of court and into individual arbitration."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/arm-faces-potential-shareholder-revolt-over-ceos-excessive-usd800-million-pay-package-huge-stock-award-would-only-be-fully-realised-if-chip-designer-hits-usd2-trillion-valuation",
    "domain": "AI 算力 / 半导体",
    "title": "Arm faces potential shareholder revolt over CEO's 'excessive' $800 million pay package — huge stock award would only be fully realised if chip designer hits $2 trillion valuation",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/arm-faces-potential-shareholder-revolt-over-ceos-excessive-usd800-million-pay-package-huge-stock-award-would-only-be-fully-realised-if-chip-designer-hits-usd2-trillion-valuation",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T10:00:00+00:00",
    "summary": "Proxy advisers kick against Arm's proposal to approve a performance pay plan that could award CEO Rene Haas about $800 million if the chip designer reaches a $2 trillion valuation."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/linux/linux-kernel-nears-2-000-cves-per-release-as-ai-bug-hunters-scour-40-million-lines-of-code-maintainers-say-they-are-completely-overwhelmed",
    "domain": "AI 算力 / 半导体",
    "title": "Linux kernel nears record 2,000 vulnerabilities per release as AI bug hunters scour 40 million lines of code — maintainers say they are 'completely overwhelmed' by CVE finds",
    "url": "https://www.tomshardware.com/software/linux/linux-kernel-nears-2-000-cves-per-release-as-ai-bug-hunters-scour-40-million-lines-of-code-maintainers-say-they-are-completely-overwhelmed",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T09:30:00+00:00",
    "summary": "AI-assisted bug hunting is driving Linux toward 2,000 CVEs per release, surfacing real flaws and mountains of low-priority work for overwhelmed maintainers."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/routers/tp-link-announces-its-first-consumer-wi-fi-8-routers-archer-8-ultra-preorder-commences-september-30-in-select-regions",
    "domain": "AI 算力 / 半导体",
    "title": "TP-Link announces its first consumer Wi-Fi 8 routers — Archer 8 Ultra preorder commences September 30, in select regions",
    "url": "https://www.tomshardware.com/networking/routers/tp-link-announces-its-first-consumer-wi-fi-8-routers-archer-8-ultra-preorder-commences-september-30-in-select-regions",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T04:00:00+00:00",
    "summary": "TP-Link’s Wi-Fi 8 launch remains complicated in the US due to ongoing FCC restrictions"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/kingstons-nv3-1tb-pcie-4-0-ssd-drops-to-usd156-99-at-newegg-27-percent-off-brings-it-down-to-just-15-7-cents-per-gb",
    "domain": "AI 算力 / 半导体",
    "title": "Kingston's NV3 1TB PCIe 4.0 SSD drops to $156.99 at Newegg — 27% off brings it down to just 15.7 cents per GB",
    "url": "https://www.tomshardware.com/pc-components/ssds/kingstons-nv3-1tb-pcie-4-0-ssd-drops-to-usd156-99-at-newegg-27-percent-off-brings-it-down-to-just-15-7-cents-per-gb",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T18:16:28+00:00",
    "summary": "The Kingston NV3 may not be built for heavy workloads, but its respectable gaming performance and low power consumption make this PCIe 4.0 SSD a compelling secondary storage upgrade."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/g-skill-drops-new-amd-expo-ull-ram-for-ryzen-cpus-flare-x5x-brings-new-ull-optimized-subtimings-but-pricing-remains-a-mystery",
    "domain": "AI 算力 / 半导体",
    "title": "G.Skill drops new AMD EXPO ULL RAM for Ryzen CPUs — Flare X5X brings new ULL optimized subtimings, but pricing remains a mystery",
    "url": "https://www.tomshardware.com/pc-components/ram/g-skill-drops-new-amd-expo-ull-ram-for-ryzen-cpus-flare-x5x-brings-new-ull-optimized-subtimings-but-pricing-remains-a-mystery",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T17:28:43+00:00",
    "summary": "G.Skill launches new Flare X5X DDR5 memory kits with AMD EXPO ULL technology for Ryzen processors."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/trump-says-communities-that-reject-data-centers-want-to-end-up-being-backwards-and-poor-president-claims-china-could-not-be-happier-with-ai-data-center-backlash-in-the-us",
    "domain": "AI 算力 / 半导体",
    "title": "Trump says communities that reject data centers 'want to end up being backwards and poor' — President claims China 'could not be happier' with AI data center backlash in the US",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/trump-says-communities-that-reject-data-centers-want-to-end-up-being-backwards-and-poor-president-claims-china-could-not-be-happier-with-ai-data-center-backlash-in-the-us",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T17:05:57+00:00",
    "summary": "President Donald Trump claims that communities rejecting AI data center constructions \"want to end up being backwards and poor.\""
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/manufacturing/motorless-solid-state-cooler-uses-heat-to-cool-itself-could-recycle-processor-heat-into-cooling-shape-memory-alloy-films-could-turn-data-center-exhaust-into-refrigeration",
    "domain": "AI 算力 / 半导体",
    "title": "Motorless solid-state cooler uses heat to cool itself; could recycle processor heat into cooling — shape-memory alloy films could turn data center exhaust into refrigeration",
    "url": "https://www.tomshardware.com/tech-industry/manufacturing/motorless-solid-state-cooler-uses-heat-to-cool-itself-could-recycle-processor-heat-into-cooling-shape-memory-alloy-films-could-turn-data-center-exhaust-into-refrigeration",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T15:40:00+00:00",
    "summary": "German and Japanese researchers demonstrate a heat-driven elastocaloric cooler that uses shape-memory alloys to turn waste heat into cooling."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/save-usd240-on-a-four-item-gaming-build-combo-from-newegg-usd1-113-buys-a-ryzen-7-9800x3d-32gb-of-corsair-ddr5-ram-a-gigabyte-x870e-motherboard-plus-a-free-240mm-aio-and-amd-game-bundle",
    "domain": "AI 算力 / 半导体",
    "title": "Save $240 on a four-item gaming build combo from Newegg – $1,113 buys a Ryzen 7 9800X3D, 32GB of Corsair DDR5 RAM, a Gigabyte X870E Motherboard, plus a free 240mm AIO and AMD game bundle",
    "url": "https://www.tomshardware.com/pc-components/save-usd240-on-a-four-item-gaming-build-combo-from-newegg-usd1-113-buys-a-ryzen-7-9800x3d-32gb-of-corsair-ddr5-ram-a-gigabyte-x870e-motherboard-plus-a-free-240mm-aio-and-amd-game-bundle",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T15:26:42+00:00",
    "summary": "This Newegg 3-item bundle pairs the fast, gaming-focused Ryzen 7 9800X3D with 32GB of Corsair Vengeance DDR5-6000 RAM and a Gigabyte X870E Aorus Pro board for only $1,113.99. That's a $240 savings, pl"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/jensen-huang-and-lisa-su-snubbed-by-times-2026-ai-list-paris-hilton-and-ben-affleck-among-others-make-the-list-as-architects-of-ai-are-totally-absent",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang and Lisa Su snubbed by TIME’s 2026 list of top 100 AI leaders — Paris Hilton and Ben Affleck, among others, make the list as ‘Architects of AI’ inexplicably not listed",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/jensen-huang-and-lisa-su-snubbed-by-times-2026-ai-list-paris-hilton-and-ben-affleck-among-others-make-the-list-as-architects-of-ai-are-totally-absent",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T14:52:59+00:00",
    "summary": "Nvidia’s sole representative on the fourth annual TIME100 AI is its head of sustainability, who sits alongside Paris Hilton and Ben Affleck."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpu-drivers/nvidias-latest-driver-update-breaks-mvolt-overclocking-functionality-nifty-open-source-app-allowed-users-to-increase-the-power-limit-to-700w-on-their-rtx-50-series-gpus-without-hardware-mods",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's latest driver update breaks mVolt+ overclocking functionality — Nifty, open-source app allowed users to increase the power limit to 700W on their RTX 50-series GPUs without hardware mods",
    "url": "https://www.tomshardware.com/pc-components/gpu-drivers/nvidias-latest-driver-update-breaks-mvolt-overclocking-functionality-nifty-open-source-app-allowed-users-to-increase-the-power-limit-to-700w-on-their-rtx-50-series-gpus-without-hardware-mods",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T14:35:14+00:00",
    "summary": "Overclocking utility mVolt+ seems to have been blocked by the latest Nvidia driver update, hard crashing the moment you try to adjust the core power limit. However, it seems like a driver conflict mor"
  },
  {
    "id": "rss:https://www.tomshardware.com/maker-stem/xtool-f2-ultra-uv-dual-laser-engraver-review",
    "domain": "AI 算力 / 半导体",
    "title": "xTool F2 Ultra UV dual laser engraver review: So cool it’s hot",
    "url": "https://www.tomshardware.com/maker-stem/xtool-f2-ultra-uv-dual-laser-engraver-review",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T14:30:00+00:00",
    "summary": "xTool’s new F2 Ultra UV cuts and engraves with cold UV light."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/key-nvidia-and-intel-supplier-raided-over-alleged-china-origin-fraud-unimicron-faces-probe-over-pcb-origin-washing-risk-of-40-percent-u-s-tariff-penalty",
    "domain": "AI 算力 / 半导体",
    "title": "Key Nvidia and Intel supplier raided over alleged China origin fraud — Unimicron faces probe over PCB origin washing, risk of 40% U.S. tariff penalty",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/key-nvidia-and-intel-supplier-raided-over-alleged-china-origin-fraud-unimicron-faces-probe-over-pcb-origin-washing-risk-of-40-percent-u-s-tariff-penalty",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T11:55:33+00:00",
    "summary": "Taiwanese prosecutors are investigating Unimicron, one of the world’s largest PCB and chip substrate makers and a key supplier to Nvidia, Intel, Google, and Amazon, over allegations that it shipped Ch"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/chinas-cxmt-beats-western-chipmakers-to-announcement-of-lpddr6-mass-production-xiaomi-smartphones-to-debut-industrys-first-lpddr6-chips",
    "domain": "AI 算力 / 半导体",
    "title": "China's CXMT beats Western chipmakers to announcement of LPDDR6 mass production — Xiaomi smartphones to debut industry’s first LPDDR6 chips",
    "url": "https://www.tomshardware.com/pc-components/dram/chinas-cxmt-beats-western-chipmakers-to-announcement-of-lpddr6-mass-production-xiaomi-smartphones-to-debut-industrys-first-lpddr6-chips",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T10:30:00+00:00",
    "summary": "CXMT claims to be the first to mass-produce LPDDR6 memory. Yet, for a niche phone."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/diehard-asus-customer-gets-rma-denied-for-a-cheap-2-4-ghz-headset-receiver-despite-spending-more-than-usd30-000-with-the-brand-firm-refuses-to-send-a-cheap-dongle-then-relents-after-social-media-backlash",
    "domain": "AI 算力 / 半导体",
    "title": "Diehard Asus customer gets RMA denied for a cheap 2.4 GHz headset receiver despite spending more than $30,000 with the brand — firm refuses to send a cheap dongle, then relents after social media back",
    "url": "https://www.tomshardware.com/peripherals/diehard-asus-customer-gets-rma-denied-for-a-cheap-2-4-ghz-headset-receiver-despite-spending-more-than-usd30-000-with-the-brand-firm-refuses-to-send-a-cheap-dongle-then-relents-after-social-media-backlash",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T10:00:00+00:00",
    "summary": "Asus refused to replace a loyal customer's wireless headset receiver because accessories are apparently not covered under warranty. The customer was not happy to see his dedication be put into questio"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/man-uses-robot-vacuum-to-covertly-record-his-wifes-affair-wins-divorce-settlement-but-gets-sentenced-to-prison-for-making-an-illegal-recording-husband-lands-behind-bars-after-counter-suit-over-privacy-rights",
    "domain": "AI 算力 / 半导体",
    "title": "Man uses robot vacuum to covertly record his wife's affair, wins divorce settlement but gets sentenced to prison for making an illegal recording — Husband lands behind bars after counter-suit over pri",
    "url": "https://www.tomshardware.com/tech-industry/man-uses-robot-vacuum-to-covertly-record-his-wifes-affair-wins-divorce-settlement-but-gets-sentenced-to-prison-for-making-an-illegal-recording-husband-lands-behind-bars-after-counter-suit-over-privacy-rights",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T09:30:00+00:00",
    "summary": "A Taiwanese man sued his wife for having an affair using recordings from a robot vacuum to prove his case. He won, but got sued by the wife for infringing on her personal privacy and was fined the equ"
  },
  {
    "id": "hn:49387755",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia AVO scores 100% on the ARC-AGI-3 interactive reasoning benchmark",
    "url": "https://twitter.com/NVIDIAAI/status/2090786258981466231",
    "source": "dsrtslnd23",
    "platform": "hackernews",
    "points": 71,
    "published_at": "2026-08-21T13:26:03+00:00",
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
    "id": "hn:49497235",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's AI advantage is moving beyond the GPU",
    "url": "https://techcrunch.com/2026/08/29/nvidias-ai-advantage-is-moving-beyond-the-gpu/",
    "source": "01-_-",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-08-30T09:57:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:49447878",
    "domain": "AI 算力 / 半导体",
    "title": "Who bears the risk in Nvidia's $500B financing platform?",
    "url": "https://www.sascha-steffen.de/updates/nvidia-500bn-ai-financing-credit-risk",
    "source": "rwmj",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-08-26T12:32:31+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/speedy-34-inch-240-hz-ultrawide-oled-monitor-now-usd600-off-lg-ultragear-34gx900a-b-only-usd599-99",
    "domain": "AI 算力 / 半导体",
    "title": "Speedy 34-inch 240 Hz ultrawide OLED monitor now $600 off — LG UltraGear 34GX900A-B only $599.99",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/speedy-34-inch-240-hz-ultrawide-oled-monitor-now-usd600-off-lg-ultragear-34gx900a-b-only-usd599-99",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T18:08:43+00:00",
    "summary": "The LG UltraGear 34GX900A-B packs a fast 240 Hz OLED panel and 3440 x 1440 resolution into an immersive 800R curved display, now available for 50% off."
  },
  {
    "id": "hn:49455507",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Announces Financial Results for Second Quarter Fiscal 2027",
    "url": "https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027",
    "source": "NewCzech",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-08-26T20:35:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:49436796",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI claims its new chips can outperform Nvidia processors in tests",
    "url": "https://www.bloomberg.com/news/articles/2026-08-25/openai-claims-its-new-chips-can-outperform-nvidia-processors-in-tests",
    "source": "TravisJamison",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-08-25T16:35:58+00:00",
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
    "id": "hn:49184755",
    "domain": "大厂 AI 动态",
    "title": "Changes at Google DeepMind: Demis Hassabis from CEO to Chair, Jeff Dean departs",
    "url": "https://blog.google/company-news/inside-google/message-ceo/next-chapter-ai-momentum/",
    "source": "colesantiago",
    "platform": "hackernews",
    "points": 867,
    "published_at": "2026-08-05T16:05:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:49220126",
    "domain": "大厂 AI 动态",
    "title": "DeepMind's WeatherNext model achieves breakthrough forecasting cyclones",
    "url": "https://deepmind.google/blog/weathernext-ai-model-achieves-breakthrough-in-forecasting-cyclones/",
    "source": "bhavansig",
    "platform": "hackernews",
    "points": 449,
    "published_at": "2026-08-08T09:18:50+00:00",
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
    "points": 296,
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
    "id": "hn:49515293",
    "domain": "大厂 AI 动态",
    "title": "29,787 Open Ollama Servers and an Unsolved Mystery",
    "url": "https://day50.dev/woahllama/",
    "source": "kristopolous",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-08-31T21:52:49+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/987839/dell-14s-student-laptop-ifa-2026-price-specs",
    "domain": "大厂 AI 动态",
    "title": "Dell’s newest laptop sounds a lot like a MacBook Neo",
    "url": "https://www.theverge.com/gadgets/987839/dell-14s-student-laptop-ifa-2026-price-specs",
    "source": "Antonio G. Di Benedetto",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T07:00:00+00:00",
    "summary": "Dell's new Dell 14S laptop sounds a lot like a MacBook Neo: it comes in four colors, is aimed at students, and it starts with 8GB of RAM and 256GB of storage. Announced at IFA 2026, the 14S is meant t"
  },
  {
    "id": "rss:https://www.theverge.com/tech/987582/irobot-roomba-max-875-sealforce-robot-vacuum-announced",
    "domain": "大厂 AI 动态",
    "title": "This new Roomba seals itself to your carpet",
    "url": "https://www.theverge.com/tech/987582/irobot-roomba-max-875-sealforce-robot-vacuum-announced",
    "source": "Jennifer Pattison Tuohy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T06:00:00+00:00",
    "summary": "iRobot has announced a new flagship robot vacuum, which it will showcase at IFA in Berlin this week, the company's first big tech trade show in years. The Roomba maker will be exhibiting under its new"
  },
  {
    "id": "rss:https://www.theverge.com/tech/987429/google-needs-hollywood-more-than-the-studios-need-ai",
    "domain": "大厂 AI 动态",
    "title": "Google needs Hollywood more than the studios need AI",
    "url": "https://www.theverge.com/tech/987429/google-needs-hollywood-more-than-the-studios-need-ai",
    "source": "Charles Pulliam-Moore",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T22:50:29+00:00",
    "summary": "Google has reportedly been reaching out to a number of Hollywood's biggest studios, hoping to strike licensing agreements that would allow it to train its AI models on copyrighted material in exchange"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/987830/anthropic-claude-fable-mythos-5-1",
    "domain": "大厂 AI 动态",
    "title": "Anthropic launches Claude Fable 5.1 and says it&#8217;s up to 45 percent cheaper for agentic work",
    "url": "https://www.theverge.com/ai-artificial-intelligence/987830/anthropic-claude-fable-mythos-5-1",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T22:01:36+00:00",
    "summary": "Anthropic says its newest AI models, Fable 5.1 and Mythos 5.1, address criticisms from customers about price, data retention, and overzealous safeguards. The company claims Claude Fable 5.1 offers str"
  },
  {
    "id": "rss:https://www.theverge.com/tech/987784/apple-maps-lake-america-renaming",
    "domain": "大厂 AI 动态",
    "title": "Apple Maps follows Google in renaming Lake Ontario",
    "url": "https://www.theverge.com/tech/987784/apple-maps-lake-america-renaming",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T21:22:56+00:00",
    "summary": "Apple Maps has officially changed the name of Lake Ontario to Lake America, as reported earlier by Bloomberg. The company joins Google in re-labeling the Great Lake following an executive order signed"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/987670/lenovo-yoga-7i-2in1-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Lenovo&#8217;s 2-in-1 Yoga 7i is a great Labor Day deal at $750",
    "url": "https://www.theverge.com/gadgets/987670/lenovo-yoga-7i-2in1-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T20:54:08+00:00",
    "summary": "Best Buy is celebrating Labor Day all week long with big deals, including a deep discount on the Lenovo Yoga 7i 2-in-1, taking its original $1,1199.99 price down to $749.99. It’s a capable configurati"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/987695/openai-astra-unreleased-model-cybersecurity-delay",
    "domain": "大厂 AI 动态",
    "title": "OpenAI delayed its new model’s development after the Hugging Face hack",
    "url": "https://www.theverge.com/ai-artificial-intelligence/987695/openai-astra-unreleased-model-cybersecurity-delay",
    "source": "Hayden Field",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T20:45:49+00:00",
    "summary": "After an unreleased OpenAI model wreaked enough havoc to make international headlines, OpenAI delayed the development of a different unreleased model suite, Astra, in order to shore up its safety work"
  },
  {
    "id": "rss:https://www.theverge.com/tech/987574/sonos-beam-ultra-first-listen",
    "domain": "大厂 AI 动态",
    "title": "On first listen, the Sonos Beam Ultra sounds great",
    "url": "https://www.theverge.com/tech/987574/sonos-beam-ultra-first-listen",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T20:08:38+00:00",
    "summary": "Sonos unveiled a bunch of new stuff today at its open house event. There's the $699 Beam Ultra soundbar and the $449 Ace Ultra headphones, plus several under-the-hood app updates (some coming sooner t"
  },
  {
    "id": "rss:https://www.theverge.com/tech/987550/tim-cook-apple-environment-sustainability-legacy",
    "domain": "大厂 AI 动态",
    "title": "Tim Cook did alright by the environment — but AI could upend his climate legacy",
    "url": "https://www.theverge.com/tech/987550/tim-cook-apple-environment-sustainability-legacy",
    "source": "Justine Calma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T19:43:39+00:00",
    "summary": "As he steps down from his post as Apple CEO today, Tim Cook leaves behind a mostly positive environmental record. As far as billionaire tech moguls and the environment go, Cook will likely be remember"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/987566/ai-civilizations-opeai-hugging-face-hack",
    "domain": "大厂 AI 动态",
    "title": "The rise of AI &#8216;civilizations&#8217; and the fall of corporate responsibility",
    "url": "https://www.theverge.com/ai-artificial-intelligence/987566/ai-civilizations-opeai-hugging-face-hack",
    "source": "Robert Hart",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T19:02:54+00:00",
    "summary": "Depending on who you ask, developer platform Hugging Face was recently attacked by OpenAI - after it lost control of its own AI tools - or by a succession of AI \"civilizations.\" Welcome to the linguis"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/01/larry-pages-flying-car-company-pivotal-loses-its-ceo/",
    "domain": "大厂 AI 动态",
    "title": "Larry Page’s flying car company Pivotal loses its CEO",
    "url": "https://techcrunch.com/2026/09/01/larry-pages-flying-car-company-pivotal-loses-its-ceo/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T23:59:59+00:00",
    "summary": "The company told TechCrunch he is \"pursuing new endeavors.\" Karklin will be replaced on an interim basis by Mike Ross, an aviation executive who joined Pivotal's board of directors in November 2025."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/01/reliances-jiohotstar-takes-its-streaming-empire-global-without-sports/",
    "domain": "大厂 AI 动态",
    "title": "Reliance’s JioHotstar takes its streaming empire global — without sports",
    "url": "https://techcrunch.com/2026/09/01/reliances-jiohotstar-takes-its-streaming-empire-global-without-sports/",
    "source": "Ivan Mehta, Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T23:00:00+00:00",
    "summary": "JioHotstar will only have entertainment content when it launches in the UK, Canada, and Singapore."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/01/apple-follows-google-in-adopting-trumps-lake-america-name/",
    "domain": "大厂 AI 动态",
    "title": "Apple follows Google in adopting Trump’s ‘Lake America’ name",
    "url": "https://techcrunch.com/2026/09/01/apple-follows-google-in-adopting-trumps-lake-america-name/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T22:13:34+00:00",
    "summary": "Apple Maps is following President Trump's executive order to change the name of Lake Ontario to Lake America."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/01/afterquery-reportedly-becomes-y-combinators-fastest-ever-unicorn-now-valued-at-3-2b/",
    "domain": "大厂 AI 动态",
    "title": "AfterQuery reportedly becomes Y Combinator’s fastest-ever unicorn, now valued at $3.2B",
    "url": "https://techcrunch.com/2026/09/01/afterquery-reportedly-becomes-y-combinators-fastest-ever-unicorn-now-valued-at-3-2b/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T22:08:24+00:00",
    "summary": "AI model-training startup AfterQuery has reportedly raised a round that valued it at $3.2 billion, just five months after announcing its $30 million Series A at a $300 million valuation in April."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/01/open-ais-astra-model-is-on-the-way-and-very-good-at-breaking-into-computer-systems/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI’s Astra model is on the way — and very good at breaking into computer systems",
    "url": "https://techcrunch.com/2026/09/01/open-ais-astra-model-is-on-the-way-and-very-good-at-breaking-into-computer-systems/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T21:06:24+00:00",
    "summary": "OpenAI previewed the precautions it is taking as it prepares to release Astra, its newest, cyber-critical LLM."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/01/googles-android-update-tackles-motion-sickness-accessibility-and-more/",
    "domain": "大厂 AI 动态",
    "title": "Google’s Android update tackles motion sickness, accessibility, and more",
    "url": "https://techcrunch.com/2026/09/01/googles-android-update-tackles-motion-sickness-accessibility-and-more/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T20:53:05+00:00",
    "summary": "While some of the features see Google playing catch-up to Apple, which already offers similar features for iPhone users, others specifically leverage Gemini to provide various improvements."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/01/x-says-attackers-are-targeting-accounts-after-the-launch-of-x-money/",
    "domain": "大厂 AI 动态",
    "title": "X says attackers are targeting user accounts after the launch of X Money",
    "url": "https://techcrunch.com/2026/09/01/x-says-attackers-are-targeting-accounts-after-the-launch-of-x-money/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T20:48:32+00:00",
    "summary": "X is investigating a wave of unsolicited password reset emails that it believes may be tied to the rollout of its new payments service."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/01/john-ternus-hypes-huge-launch-next-week-in-first-memo-as-apple-ceo/",
    "domain": "大厂 AI 动态",
    "title": "John Ternus hypes ‘huge launch next week’ in first memo as Apple CEO",
    "url": "https://techcrunch.com/2026/09/01/john-ternus-hypes-huge-launch-next-week-in-first-memo-as-apple-ceo/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T19:45:28+00:00",
    "summary": "Apple is hosting its iPhone release event next week, which is rumored to feature the first-ever foldable iPhone."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/01/anthropics-new-fable-release-is-cheaper-less-restrictive/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic’s new Fable release is cheaper, less restrictive",
    "url": "https://techcrunch.com/2026/09/01/anthropics-new-fable-release-is-cheaper-less-restrictive/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T19:39:22+00:00",
    "summary": "Fable 5.1 includes changes meant to reduce token cost and false-positive restrictions from the model's safeguards."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/01/thrives-kushner-defends-involvement-in-fifa-mess-hires-elons-go-to-lawyer/",
    "domain": "大厂 AI 动态",
    "title": "Thrive’s Kushner defends involvement in FIFA mess, hires Elon’s go-to lawyer",
    "url": "https://techcrunch.com/2026/09/01/thrives-kushner-defends-involvement-in-fifa-mess-hires-elons-go-to-lawyer/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T19:30:24+00:00",
    "summary": "New York's prestigious-yet-secretive venture firm Thrive Capital finally speaks out about its involvement in the messy drama upending international soccer."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/01/who-is-john-ternus-the-incoming-apple-ceo/",
    "domain": "大厂 AI 动态",
    "title": "Who is John Ternus, the new Apple CEO?",
    "url": "https://techcrunch.com/2026/09/01/who-is-john-ternus-the-incoming-apple-ceo/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T18:02:00+00:00",
    "summary": "Starting on September 1, Ternus will lead one of the world's most valuable companies, but if you're not a dedicated Apple enthusiast, you've probably never heard of this man, who has largely remained "
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/01/googles-answer-to-canva-is-an-ai-tool-where-you-prompt-instead-of-design/",
    "domain": "大厂 AI 动态",
    "title": "Google’s answer to Canva is an AI tool where you prompt instead of design",
    "url": "https://techcrunch.com/2026/09/01/googles-answer-to-canva-is-an-ai-tool-where-you-prompt-instead-of-design/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T17:35:37+00:00",
    "summary": "With Google Pics, Google is pushing deeper into the creative software market dominated by Canva and Adobe, but with a distinctly AI-first approach."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/01/chatgpt-health-adds-epic-integration-for-clinicians-to-import-patient-data/",
    "domain": "大厂 AI 动态",
    "title": "ChatGPT Health adds Epic integration for clinicians to import patient data",
    "url": "https://techcrunch.com/2026/09/01/chatgpt-health-adds-epic-integration-for-clinicians-to-import-patient-data/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T17:00:00+00:00",
    "summary": "OpenAI said that the integration provides read-only access to health records for clinicians."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/01/waymo-goes-on-offense-ahead-of-teslas-cybercab-launch/",
    "domain": "大厂 AI 动态",
    "title": "Waymo goes on offense ahead of Tesla’s Cybercab launch",
    "url": "https://techcrunch.com/2026/09/01/waymo-goes-on-offense-ahead-of-teslas-cybercab-launch/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T16:49:12+00:00",
    "summary": "Waymo argued that fully autonomous vehicles aren't possible without using a mix of sensors and warned that pure end-to-end AI systems aren't safe enough."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/01/sequoia-incubated-empirik-launches-with-21m-to-predict-outages-before-they-happen/",
    "domain": "大厂 AI 动态",
    "title": "Sequoia-incubated Empirik launches with $21M to predict outages before they happen",
    "url": "https://techcrunch.com/2026/09/01/sequoia-incubated-empirik-launches-with-21m-to-predict-outages-before-they-happen/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T16:31:04+00:00",
    "summary": "The startup wants to do for IT infrastructure what Cursor did for software engineering."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/01/gopro-to-be-acquired-for-285m-will-remain-a-public-company/",
    "domain": "大厂 AI 动态",
    "title": "GoPro to be acquired for $285M, will remain a public company",
    "url": "https://techcrunch.com/2026/09/01/gopro-to-be-acquired-for-285m-will-remain-a-public-company/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T15:57:23+00:00",
    "summary": "GoPro is merging with a company that builds AI infrastructure, and will continue supporting existing consumer products."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/01/amazon-alexa-can-now-alert-you-when-something-new-might-tempt-you-to-shop/",
    "domain": "大厂 AI 动态",
    "title": "Amazon Alexa can now alert you when something new might tempt you to shop",
    "url": "https://techcrunch.com/2026/09/01/amazon-alexa-can-now-alert-you-when-something-new-might-tempt-you-to-shop/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T15:51:55+00:00",
    "summary": "Amazon is adding a new Alexa-powered feature called “Update Me When” that can send personalized alerts about product launches, tours, books, shows, and other events that could trigger a purchase."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/01/air-raises-50m-to-help-companies-vet-the-skills-and-add-ons-ai-agents-use/",
    "domain": "大厂 AI 动态",
    "title": "AIR raises $50M to help companies vet the skills and add-ons AI agents use",
    "url": "https://techcrunch.com/2026/09/01/air-raises-50m-to-help-companies-vet-the-skills-and-add-ons-ai-agents-use/",
    "source": "Ram Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T15:45:51+00:00",
    "summary": "AIR's platform can discover agents running at a company, continuously vets any skills and add-ons they use, and blocks any unwanted behavior."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/01/microsoft-365-outage-drags-on-but-things-are-improving/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft 365 outage drags on, but things are improving",
    "url": "https://techcrunch.com/2026/09/01/microsoft-365-outage-drags-on-but-things-are-improving/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T15:23:15+00:00",
    "summary": "Microsoft 365 and Outlook are still seeing service degradations on Tuesday, the company's status page indicates."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/01/fambot-introduces-an-ai-chief-of-staff-for-families/",
    "domain": "大厂 AI 动态",
    "title": "Fambot introduces an ‘AI chief of staff’ for families",
    "url": "https://techcrunch.com/2026/09/01/fambot-introduces-an-ai-chief-of-staff-for-families/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T15:10:58+00:00",
    "summary": "Fambot is building an AI “chief of staff” to help families manage the emails, calendars, school updates, sports schedules, and other logistics of raising kids."
  },
  {
    "id": "rss:https://stratechery.com/2026/nvidia-earnings-dollars-per-gigawatt-open-and-hugging-face/",
    "domain": "大厂 AI 动态",
    "title": "Nvidia Earnings, Dollars Per Gigawatt, Open and Hugging Face",
    "url": "https://stratechery.com/2026/nvidia-earnings-dollars-per-gigawatt-open-and-hugging-face/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T10:00:00+00:00",
    "summary": "Nvidia's earnings were remarking and boring — two sides of the same coin. Everything the company does is about avoiding a consolidated world."
  },
  {
    "id": "rss:https://stratechery.com/2026/meta-settles-a-framework-for-regulating-content-the-rest-of-big-tech/",
    "domain": "大厂 AI 动态",
    "title": "Meta Settles, A Framework For Regulating Content, The Rest of Big Tech",
    "url": "https://stratechery.com/2026/meta-settles-a-framework-for-regulating-content-the-rest-of-big-tech/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T10:00:00+00:00",
    "summary": "Meta's settlement makes sense for all parties, but the entire sage highlights why any solution to regulating technology feels off."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/09/range-rover-ev-electric-propulsion-pairs-perfectly-with-this-luxury-suv/",
    "domain": "大厂 AI 动态",
    "title": "Here's our first look—and drive—of the 2027 Range Rover Electric",
    "url": "https://arstechnica.com/cars/2026/09/range-rover-ev-electric-propulsion-pairs-perfectly-with-this-luxury-suv/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T23:01:52+00:00",
    "summary": "333 miles of real-world range with uncompromised comfort and off-road ability."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/09/august-research-roundup-7-cool-science-stories-we-almost-missed/",
    "domain": "大厂 AI 动态",
    "title": "Research roundup: 7 cool science stories we almost missed",
    "url": "https://arstechnica.com/science/2026/09/august-research-roundup-7-cool-science-stories-we-almost-missed/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T19:06:10+00:00",
    "summary": "\"Black hole stars,\" making cookies from plastic, tiny sound-powered drones, and more."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/09/cdc-reported-then-deleted-two-measles-deaths-that-were-questioned-by-rfk-jr/",
    "domain": "大厂 AI 动态",
    "title": "A newborn and child reportedly died of measles; CDC isn't counting them",
    "url": "https://arstechnica.com/health/2026/09/cdc-reported-then-deleted-two-measles-deaths-that-were-questioned-by-rfk-jr/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T18:21:16+00:00",
    "summary": "Historically, state health departments determine cases and deaths, not the CDC."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/09/latest-android-drop-connects-gemini-to-find-hub-adds-keep-notes-and-themes-to-messages/",
    "domain": "大厂 AI 动态",
    "title": "New Android Drop adds remembered items in Find Hub, makes anti-nausea dots official",
    "url": "https://arstechnica.com/gadgets/2026/09/latest-android-drop-connects-gemini-to-find-hub-adds-keep-notes-and-themes-to-messages/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T18:00:02+00:00",
    "summary": "New features are rolling out across the Android ecosystem starting today."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/09/ftc-alleges-amazon-illegally-made-20-billion-by-rigging-billions-of-ad-auctions/",
    "domain": "大厂 AI 动态",
    "title": "FTC alleges Amazon illegally made $20 billion by rigging billions of ad auctions",
    "url": "https://arstechnica.com/tech-policy/2026/09/ftc-alleges-amazon-illegally-made-20-billion-by-rigging-billions-of-ad-auctions/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T17:51:17+00:00",
    "summary": "FTC says firm replaces actual ad-auction results \"with higher prices set by Amazon.\""
  },
  {
    "id": "hn:49511824",
    "domain": "股票",
    "title": "Apple Is Suddenly an AI Infra Stock as OpenAI Buys 10k+ Macs",
    "url": "https://247wallst.com/investing/2026/08/31/apple-is-suddenly-an-ai-infrastructure-stock-as-openai-buys-macs-by-the-tens-of-thousands/",
    "source": "prabal97",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-08-31T16:44:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:49166182",
    "domain": "股票",
    "title": "Bending Spoons makes first post-IPO acquisition with $1.3B Airtable deal",
    "url": "https://live.euronext.com/en/financial-news/bending-spoons-makes-first-post-ipo-acquisition-13-billion-airtable-deal",
    "source": "riffraff",
    "platform": "hackernews",
    "points": 118,
    "published_at": "2026-08-04T09:27:47+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3780896",
    "domain": "股票",
    "title": "黄金卖压即将枯竭！德银：鹰派美联储冲击有限，主动资金或接棒下一轮涨势",
    "url": "https://wallstreetcn.com/articles/3780896",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T07:31:35+00:00",
    "summary": "黄金迎关键转折。德银：CTA买盘见顶且卖压枯竭，金价无惧鹰派冲击。主动资金正蓄势接棒，有望开启新一轮上涨。此外，白银做多信号强烈，铜市正逼近十年一遇的极端“拐角”。"
  },
  {
    "id": "wscn:3780898",
    "domain": "股票",
    "title": "星宇股份董事长回应“批量解约应届生”：公司深刻反省并真诚道歉，正在政府部门指导下妥善落实相关措施",
    "url": "https://wallstreetcn.com/articles/3780898",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T07:29:57+00:00",
    "summary": "星宇股份董事长周晓萍在业绩会上回应应届生解约风波，称公司已致歉并正落实整改，同时就不实报道向网信、网安部门投诉。此前公司因解约107名应届生引发关注，常州市人社局通报企业不存在违规补贴，截至8月25日已有22人重新就业。"
  },
  {
    "id": "wscn:3780897",
    "domain": "股票",
    "title": "宋雪涛：加息也救不了长端利率",
    "url": "https://wallstreetcn.com/articles/3780897",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T07:18:58+00:00",
    "summary": "国金宏观认为，美国长端利率高企主要源于实际利率，而非通胀预期，AI投资与油价属供给和结构问题，加息难以解决。AI已成为国家战略投资，高融资需求将持续，首先压制非AI经济。联储政策空间有限，市场与联储互相猜测加剧波动。真正核心在于AI能否尽快变现，若不能，高利率与财政压力将转化为债务与估值风险。"
  },
  {
    "id": "wscn:3780891",
    "domain": "股票",
    "title": "道指五个月来首次跌破50日均线，技术面发出警示信号",
    "url": "https://wallstreetcn.com/articles/3780891",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T06:44:51+00:00",
    "summary": "道指近五个月来首次跌破50日均线，标普500与纳指亦濒临失守，标志着市场短期动能面临由盈转亏的技术性转折。本轮回调的核心诱因在于长期美债收益率逼近5%关口、中东局势推高油价引发通胀担忧，以及债务扩张带来的利率压力。短期内，均线破位或触发量化与技术盘卖压，市场波动风险显著上升。"
  },
  {
    "id": "wscn:3780893",
    "domain": "股票",
    "title": "从全球主张到中国实践，CFA协会如何以“标准”回应行业变化",
    "url": "https://wallstreetcn.com/articles/3780893",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T06:42:08+00:00",
    "summary": "“Set the Standard”：立于标准，驭势未来"
  },
  {
    "id": "wscn:3780888",
    "domain": "股票",
    "title": "Altman谈下一代模型：若出现RSI将推迟IPO，部分新AI云“不可持续的愚蠢”",
    "url": "https://wallstreetcn.com/articles/3780888",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T06:41:06+00:00",
    "summary": "AI“递归自我改进（RSI）”或提前降临。奥特曼警告：这将打破算力见顶论，驱动巨头无视短期利润狂囤GPU。因AI进化过快，OpenAI已放缓训练死守安全底线，更酝酿全面推迟IPO。决定2028年AI资本开支（CapEx）天花板的，不是Coding之外是否出现了新的万亿美元应用，而是RSI是否到来。"
  },
  {
    "id": "wscn:3780892",
    "domain": "股票",
    "title": "8月全球资产大洗牌  ：黄金飙升9.7%领跑，农产品狂飙 ，长债成最大输家",
    "url": "https://wallstreetcn.com/articles/3780892",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T06:14:53+00:00",
    "summary": "德银表示，8月全球资产显著分化，地缘封锁与极端天气推升通胀预期，叠加财政干预引发“金融抑制”担忧，促使黄金、白银及农产品强劲暴涨，美元连续走弱；强劲经济数据支撑标普500等股市稳步创新高。相反，债市遭遇抛售，美德日等主要经济体长端收益率冲至多年高位，美联储鹰派信号更令9月加息概率升至65%。"
  },
  {
    "id": "wscn:3780820",
    "domain": "股票",
    "title": "英伟达为什么化35亿美元锁定联发科？一张可转债背后的AI工厂卡位战！",
    "url": "https://wallstreetcn.com/premium/articles/3780820?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T05:59:32+00:00",
    "summary": "联发科完成大规模海外可转债（CB）发行，募资总额39亿美元，英伟达以35亿美元（占发行额约89.7%）领投，Alphabet跟投剩余份额。"
  },
  {
    "id": "wscn:3780886",
    "domain": "股票",
    "title": "日本央行鹰派委员放话：下次加息幅度或超0.25%，连续加息也不排除",
    "url": "https://wallstreetcn.com/articles/3780886",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T05:31:03+00:00",
    "summary": "日本央行鹰派代表高田创表示，下次加息幅度“未必是0.25个百分点”，甚至不排除0.5%或0.75%的更大幅度加息，连续加息亦是可能选项——这一表态大幅超出市场此前的惯性预期。日元闻讯走强，一度升至159.80附近。"
  },
  {
    "id": "wscn:3780885",
    "domain": "股票",
    "title": "美伊局势重燃通胀担忧，布油涨至95美元，全球债市遭猛烈抛售，韩股下跌4%",
    "url": "https://wallstreetcn.com/articles/3780885",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T05:28:14+00:00",
    "summary": "美伊军事交火重燃、油价急涨，通胀忧虑与加息预期双双升温，美债、日债、澳债等主要市场收益率纷纷攀升至十年乃至数十年高位。韩国综指跌幅扩大至4%，SK海力士与三星电子均跌逾4%。布伦特原油上涨1%至每桶95.61美元，柴油价格攀升至四个多月来最高位，欧洲天然气价格亦升至2023年以来最高水平。"
  },
  {
    "id": "wscn:3779056",
    "domain": "股票",
    "title": "解密央行版“权力的游戏”：原美联储高级经济学家胡捷带你看清全球第一央行的变局与冲击",
    "url": "https://wallstreetcn.com/articles/3779056",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T05:18:41+00:00",
    "summary": "2026年9月6日，上海交通大学高级金融学院教授，原美联储高级经济学家胡捷带你读懂美联储背后的权利博弈"
  },
  {
    "id": "wscn:3780874",
    "domain": "股票",
    "title": "创业板跌2%，军工逆势大涨，宇树科技股价较上市首日“腰斩”，中际旭创跌破万亿市值，恒科指跌超1%，科网股普遍下跌",
    "url": "https://wallstreetcn.com/articles/3780874",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T04:07:45+00:00",
    "summary": "盘面上，个股跌多涨少，沪深京三市超4000股飘绿，上午半天成交1.23万亿。沪深两市半日成交额1.21万亿，较上个交易日缩量1403亿。板块方面，农业、金属、煤炭、光模块、石化板块领跌，银行板块维持强势局面，军工、次新股、玻纤、培育钻石、ADC板块活跃。"
  },
  {
    "id": "wscn:3780890",
    "domain": "股票",
    "title": "PIAGET伯爵Polo系列三问腕表",
    "url": "https://wallstreetcn.com/articles/3780890",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T04:01:26+00:00",
    "summary": "PIAGET伯爵Polo系列三问腕表\nPIAGET伯爵独家臻献Polo系列三问腕表，以半镂空表盘巧..."
  },
  {
    "id": "wscn:3780881",
    "domain": "股票",
    "title": "植田和男放鹰“暗示9月加息”：货币条件仍然宽松，我们希望继续加息",
    "url": "https://wallstreetcn.com/articles/3780881",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T03:59:10+00:00",
    "summary": "植田和男在G20会议后表示货币条件仍然宽松、“希望继续加息”，并将在9月17—18日会议上重点讨论通胀上行风险。隔夜指数掉期显示9月加息概率已接近100%，若成行将打破此前约六个月的加息间隔，成为植田任期内最快的后续加息。日经225指数、韩国KOSPI均跌超2%，日债承压。"
  },
  {
    "id": "wscn:3780883",
    "domain": "股票",
    "title": "苹果换帅“价码”落定：Ternus 75%股权对赌标普500，库克降薪留任护航平稳过渡",
    "url": "https://wallstreetcn.com/articles/3780883",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T03:56:38+00:00",
    "summary": "苹果新任CEO John Ternus 2027财年的目标薪酬总额约为5800万美元，其中高达5500万美元的股权奖励有75%直接与标普500指数表现挂钩。转任执行董事长的Tim Cook新薪酬方案目标总额约为4700万美元，其中4500万美元的股权奖励中有一半与大盘表现挂钩。"
  },
  {
    "id": "wscn:3780880",
    "domain": "股票",
    "title": "借半导体红利重注AI！韩国820万亿预算落地，创历年来最高支出增速",
    "url": "https://wallstreetcn.com/articles/3780880",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T03:44:01+00:00",
    "summary": "韩国正式通过史上最激进预算案：2027年总支出高达820.9万亿韩元，同比暴增93万亿，21.3万亿韩元重金押注AI三大超级项目，162.3万亿\"未来应对基金\"同步落地。半导体超级周期带来的税收红利为这场豪赌提供底气，债务率有望降至48.3%——但超百万亿闲置资金引发\"小金库\"争议，刚性福利支出急速膨胀的财政隐忧，正悄然积聚。"
  },
  {
    "id": "wscn:3780878",
    "domain": "股票",
    "title": "日债破3%：一口补贴了全世界三十年的“廉价资本之井”正在干涸",
    "url": "https://wallstreetcn.com/premium/articles/3780878?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T03:43:15+00:00",
    "summary": "9月1日下午，东京债券市场刚恢复交易没几分钟，日本10年期国债收益率就冲上了3.0%。上一次见到这个数字，还是1996年。从短到长，整条收益率曲线全面沦陷——20年期触及1996年以来最高，30年期逼近历史纪录，5年期创了新高。"
  },
  {
    "id": "wscn:3780882",
    "domain": "股票",
    "title": "上市第11个交易日，宇树科技股价腰斩",
    "url": "https://wallstreetcn.com/articles/3780882",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T03:41:57+00:00",
    "summary": "顶着“人形机器人第一股”光环，宇树科技仅两周市值便蒸发超2200亿元。暴跌背后，标志着行业正式从“烧钱讲故事”步入残酷的“盈利验证”新阶段。市场人士指出，股价回调源于多重因素，并不代表基本面突变。CEO王兴兴回应：用业绩回报股东。"
  },
  {
    "id": "wscn:3780872",
    "domain": "股票",
    "title": "美柴油裂解价差突破106美元创历史新高，特朗普面临“中选冲击”",
    "url": "https://wallstreetcn.com/articles/3780872",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T03:06:52+00:00",
    "summary": "美国柴油裂解价差突破每桶106美元创历史新高，零售价格逼近每加仑5.63美元，距2022年历史纪录仅一步之遥。柴油价格飙升直接冲击农业、卡车运输和冬季取暖需求，政治上威胁共和党在红州的中期选举基本盘。特朗普紧急召集炼油商赴白宫会谈，聚焦于如何扩大炼油产能、压低燃油价格。"
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
    "id": "hn:49396088",
    "domain": "股票",
    "title": "S&P 500 CEO median pay hits $17.3M, widening CEO-worker ratio to 312-to-1",
    "url": "https://finance.yahoo.com/markets/stocks/articles/p-500-ceo-median-pay-234900518.html",
    "source": "newsomix9xl",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-08-22T02:38:14+00:00",
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
    "id": "hn:49366252",
    "domain": "股票",
    "title": "OpenAI 'will be a public company in 2027' or sooner, CFO Friar tells employees",
    "url": "https://www.cnbc.com/2026/08/19/open-ai-ipo-timing-2027-friar.html",
    "source": "thm",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-08-19T19:42:35+00:00",
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
    "id": "hn:49253785",
    "domain": "股票",
    "title": "OpenAI wraps $7B share sale ahead of potential IPO",
    "url": "https://www.cnbc.com/2026/08/10/openai-wraps-7-billion-share-sale-ahead-of-potential-ipo-.html",
    "source": "kristianp",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-08-11T05:40:35+00:00",
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
    "id": "hn:49175192",
    "domain": "金融",
    "title": "Thanks FedEx, This Is Why We Keep Getting Phished (2024)",
    "url": "https://www.troyhunt.com/thanks-fedex-this-is-why-we-keep-getting-phished/",
    "source": "stymaar",
    "platform": "hackernews",
    "points": 338,
    "published_at": "2026-08-04T21:09:39+00:00",
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
    "id": "hn:49415187",
    "domain": "金融",
    "title": "Nearly 3M Teslas recalled in China over hidden door handles",
    "url": "https://www.bbc.com/news/articles/c4g6ggdg030o",
    "source": "chicken-stew",
    "platform": "hackernews",
    "points": 120,
    "published_at": "2026-08-24T04:27:57+00:00",
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
    "id": "rss:https://arxiv.org/abs/2609.00332",
    "domain": "金融",
    "title": "Latent-Space No-Arbitrage Geometry of Generative Models for Implied Volatility Surfaces",
    "url": "https://arxiv.org/abs/2609.00332",
    "source": "Jing Wang, Shuaiqiang Liu, Cornelis Vuik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T04:00:00+00:00",
    "summary": "arXiv:2609.00332v1 Announce Type: new Abstract: Generative models for implied volatility surfaces must produce outputs that satisfy static no-arbitrage constraints. We study these constraints in laten"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.00438",
    "domain": "金融",
    "title": "Single- and Multilevel Quadrature with Error Control for Fourier Pricing under the Rough Heston Model",
    "url": "https://arxiv.org/abs/2609.00438",
    "source": "Chiheb Ben Hammouda, Abderrahmene Ben Romdhane, Michael Samet, Raul F. Tempone",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T04:00:00+00:00",
    "summary": "arXiv:2609.00438v1 Announce Type: new Abstract: Unlike the classical Heston model, Fourier pricing under the rough Heston model requires solving a fractional Riccati equation at every quadrature point"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.00911",
    "domain": "金融",
    "title": "Pricing the DeFi Tail: Do Protocols or Depositors Price Operational Risk?",
    "url": "https://arxiv.org/abs/2609.00911",
    "source": "Nils Bundi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T04:00:00+00:00",
    "summary": "arXiv:2609.00911v1 Announce Type: new Abstract: Similar to banks, DeFi protocols expose depositors to operational risk (USD 9.45 billion across 1,075 events since 2020). Unlike banks, they are not req"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.00943",
    "domain": "金融",
    "title": "Illiquidity at Risk",
    "url": "https://arxiv.org/abs/2609.00943",
    "source": "Demetrio Lacava, Paolo Santucci de Magistris",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T04:00:00+00:00",
    "summary": "arXiv:2609.00943v1 Announce Type: new Abstract: Market efficiency relies fundamentally on stable liquidity. Consequently, forecasting liquidity dynamics is a priority for both investors and regulators"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.01183",
    "domain": "金融",
    "title": "Harvesting the Variance Risk Premium in Nuclear and Energy Equities: A Short-Put Portfolio Derisking Strategy",
    "url": "https://arxiv.org/abs/2609.01183",
    "source": "Jilang Miao, Nonna Sorokina",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T04:00:00+00:00",
    "summary": "arXiv:2609.01183v1 Announce Type: new Abstract: We study whether nuclear and energy-adjacent equity options exhibit a harvestable variance risk premium. Using CRSP and OptionMetrics data for 2000-2024"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.01263",
    "domain": "金融",
    "title": "AI and the Economy: An Economic Examination of Production, Distribution, Firms, Labor, and Welfare",
    "url": "https://arxiv.org/abs/2609.01263",
    "source": "Ali Zeytoon-Nejad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T04:00:00+00:00",
    "summary": "arXiv:2609.01263v1 Announce Type: new Abstract: Artificial Intelligence (AI) is rapidly transforming economic systems by altering production processes, labor markets, and the structure of firms and in"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.01323",
    "domain": "金融",
    "title": "Adaptive singular-point method for pricing and hedging surrenderable equity-linked contracts",
    "url": "https://arxiv.org/abs/2609.01323",
    "source": "Andrea Molent, Marcellino Gaudenzi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T04:00:00+00:00",
    "summary": "arXiv:2609.01323v1 Announce Type: new Abstract: We propose a deterministic numerical method for pricing and hedging surrenderable equity-linked life-insurance contracts with periodic premiums and fund"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.00731",
    "domain": "金融",
    "title": "Agentic Empirical Asset Pricing: Methodological Foundations",
    "url": "https://arxiv.org/abs/2609.00731",
    "source": "Yingjian Pan, Xiaowei Ding, Kay Giesecke",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T04:00:00+00:00",
    "summary": "arXiv:2609.00731v1 Announce Type: cross Abstract: Recent advances in LLM agents enable a new paradigm for asset pricing, which we call Agentic Empirical Asset Pricing (AEAP): systems that autonomously"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.01133",
    "domain": "金融",
    "title": "Scalable Inversion of Contests with Correlated Performances, Including Softmax and Multinomial Probit",
    "url": "https://arxiv.org/abs/2609.01133",
    "source": "Peter Cotton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T04:00:00+00:00",
    "summary": "arXiv:2609.01133v1 Announce Type: cross Abstract: Multinomial probit choice probabilities over n alternatives are Gaussian orthant integrals, computed by simulation for thirty years, one expensive int"
  },
  {
    "id": "rss:https://arxiv.org/abs/2210.15946",
    "domain": "金融",
    "title": "Local Media and the Shaping of Social Norms: Evidence from the Ebola outbreak",
    "url": "https://arxiv.org/abs/2210.15946",
    "source": "Ada Gonzalez-Torres",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T04:00:00+00:00",
    "summary": "arXiv:2210.15946v3 Announce Type: replace Abstract: Media's influence on norms and behavior is widely recognized. Less is known about the role played by media being local. I examine this in a high-sta"
  },
  {
    "id": "rss:https://arxiv.org/abs/2408.15675",
    "domain": "金融",
    "title": "Quantifying the degree of risk aversion of spectral risk measures",
    "url": "https://arxiv.org/abs/2408.15675",
    "source": "E. Ruben van Beesten",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T04:00:00+00:00",
    "summary": "arXiv:2408.15675v4 Announce Type: replace Abstract: This paper introduces a quantitative notion of the degree of risk aversion of spectral risk measures. We define a family of degree functionals chara"
  },
  {
    "id": "rss:https://arxiv.org/abs/2504.06550",
    "domain": "金融",
    "title": "Blameocracy: Causal Rhetoric in Politics",
    "url": "https://arxiv.org/abs/2504.06550",
    "source": "Francesco Bilotta, Alberto Binetti, Giacomo Manferdini",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T04:00:00+00:00",
    "summary": "arXiv:2504.06550v4 Announce Type: replace Abstract: This paper studies the supply and returns of causal rhetoric in politics: politicians' language linking political actions to outcomes through blame "
  },
  {
    "id": "rss:https://arxiv.org/abs/2508.03230",
    "domain": "金融",
    "title": "To Bubble or Not to Bubble: Asset Price Dynamics and Optimality in OLG Economies",
    "url": "https://arxiv.org/abs/2508.03230",
    "source": "Stefano Bosi (UEVE), Cuong Le Van (CES, PSE), Ngoc-Sang Pham (EM Normandie)",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T04:00:00+00:00",
    "summary": "arXiv:2508.03230v4 Announce Type: replace Abstract: We study an overlapping generations (OLG) exchange economy with an asset that yields dividends. First, we derive general conditions, based on exogen"
  },
  {
    "id": "rss:https://arxiv.org/abs/2603.09142",
    "domain": "金融",
    "title": "How bad is time variability for users in mobility services? An economic framework under expected- and non-expected utility",
    "url": "https://arxiv.org/abs/2603.09142",
    "source": "David Z. W. Wang, Zhaoqi Zang, Xiangdong Xu, Shaojun Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T04:00:00+00:00",
    "summary": "arXiv:2603.09142v2 Announce Type: replace Abstract: Time variability is a pervasive feature of mobility services and a major source of welfare loss. Although literature has quantified the cost of time"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.06737",
    "domain": "金融",
    "title": "Fast-excursion limit of the Heston model",
    "url": "https://arxiv.org/abs/2606.06737",
    "source": "Ryan McCrickerd",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T04:00:00+00:00",
    "summary": "arXiv:2606.06737v3 Announce Type: replace Abstract: This article introduces an unconventional model for price processes in finance that emerges from the classical Heston model under Mechkov's fast-rev"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.10245",
    "domain": "金融",
    "title": "A Fast Implied Volatility Method with Expansions",
    "url": "https://arxiv.org/abs/2606.10245",
    "source": "Alper Hekimoglu, Ismail Hakki Gokgoz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T04:00:00+00:00",
    "summary": "arXiv:2606.10245v2 Announce Type: replace Abstract: We present a regime-split Black--Scholes implied volatility solver in which every initial seed is a fully closed-form analytical expression, derived"
  },
  {
    "id": "rss:https://arxiv.org/abs/2202.02787",
    "domain": "金融",
    "title": "Stable cooperation emerges in stochastic multiplicative growth",
    "url": "https://arxiv.org/abs/2202.02787",
    "source": "Lorenzo Fant, Onofrio Mazzarisi, Emanuele Panizon, Jacopo Grilli",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T04:00:00+00:00",
    "summary": "arXiv:2202.02787v2 Announce Type: replace-cross Abstract: Understanding the evolutionary stability of cooperation is a central problem in biology, sociology, and economics. There exist only a few know"
  },
  {
    "id": "rss:https://arxiv.org/abs/2511.09454",
    "domain": "金融",
    "title": "Individualized Algorithmic Advice as a Strategic Signal on Competitive Markets",
    "url": "https://arxiv.org/abs/2511.09454",
    "source": "Tobias R. Rebholz, Maxwell Uphoff, Christian H. R. Bernges, Florian Scholten",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T04:00:00+00:00",
    "summary": "arXiv:2511.09454v2 Announce Type: replace-cross Abstract: As algorithms increasingly mediate competitive decision-making, their influence extends beyond individual outcomes to shaping strategic market"
  },
  {
    "id": "rss:https://arxiv.org/abs/2512.08472",
    "domain": "金融",
    "title": "Measuring Computer Science Enthusiasm: A Questionnaire-Based Analysis of Age and Gender Effects on Students' Interest",
    "url": "https://arxiv.org/abs/2512.08472",
    "source": "Kai Marquardt, Robert Hanak, Anne Koziolek, Lucia Happe",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T04:00:00+00:00",
    "summary": "arXiv:2512.08472v2 Announce Type: replace-cross Abstract: This study examines how age and gender independently shape adolescents' interest in computer science (CS) education. Building on the Person-Ob"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.01300",
    "domain": "金融",
    "title": "On explicit solutions to a class of quadratic BSDEJs driven by affine Volterra processes with jumps and applications",
    "url": "https://arxiv.org/abs/2604.01300",
    "source": "Sigui Brice Dro, Emmanuel Gnabeyeu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T04:00:00+00:00",
    "summary": "arXiv:2604.01300v2 Announce Type: replace-cross Abstract: In this paper we consider a class of quadratic BSDEs with jumps (quadratic BSDEJs) involving inhomogeneous affine Volterra processes and show "
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.05990",
    "domain": "金融",
    "title": "Direct Air Capture in Europe's 2050 Energy System: Integration, Storage and Cost Drivers",
    "url": "https://arxiv.org/abs/2604.05990",
    "source": "Maximilian Bernecker, Felix M\\\"usgens",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T04:00:00+00:00",
    "summary": "arXiv:2604.05990v2 Announce Type: replace-cross Abstract: Direct Air Carbon Capture and Storage (DACCS) can mitigate hard-to-abate emissions, e.g. from transport or industry. However, there is a wide "
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.07567",
    "domain": "金融",
    "title": "Marginal Persistence and Dynamic Copula Dependence in Sovereign Rating Migration Counts: A Discrete Interval-Likelihood MAGMAR Analysis",
    "url": "https://arxiv.org/abs/2604.07567",
    "source": "Marina Palaisti",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T04:00:00+00:00",
    "summary": "arXiv:2604.07567v2 Announce Type: replace-cross Abstract: This paper develops an observed-data likelihood for applying moving-aggregate modified autoregressive (MAGMAR) copula time-series models to di"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.02828",
    "domain": "金融",
    "title": "Proper-score observation-driven filters: local geometry, estimation, and continuous-time limits",
    "url": "https://arxiv.org/abs/2608.02828",
    "source": "Giulia Livieri, Gianluca Palmari",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T04:00:00+00:00",
    "summary": "arXiv:2608.02828v2 Announce Type: replace-cross Abstract: Observation-driven filters usually use the likelihood score, tying their updates to the logarithmic scoring rule. We study recursions driven i"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.12281",
    "domain": "金融",
    "title": "Unequal urban capacities for mobility adaptation under fuel-price shocks",
    "url": "https://arxiv.org/abs/2608.12281",
    "source": "Zihao Zhang, Yuanbo Zhang, Xiaolei Ma, Yuan Liao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T04:00:00+00:00",
    "summary": "arXiv:2608.12281v2 Announce Type: replace-cross Abstract: What a city makes reachable depends less on what it contains than on who can still afford to move when travel costs rise. We leverage the 2026"
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
    "id": "hn:49432102",
    "domain": "金融",
    "title": "Nostr vs. Fediverse vs. Bluesky: A Comparison of Decentralized Social Protocols",
    "url": "https://soapbox.pub/blog/comparing-protocols",
    "source": "Bluestein",
    "platform": "hackernews",
    "points": 54,
    "published_at": "2026-08-25T11:27:51+00:00",
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
    "id": "hn:49206115",
    "domain": "金融",
    "title": "Anthropic CEO reportedly worried new hires only care about money",
    "url": "https://finance.yahoo.com/technology/ai/articles/anthropic-ceo-reportedly-worried-hires-160000647.html",
    "source": "frays",
    "platform": "hackernews",
    "points": 65,
    "published_at": "2026-08-07T05:15:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:49444266",
    "domain": "金融",
    "title": "Running out of money': Kraft, McDonald's, Whirlpool CEOs flag consumer concern",
    "url": "https://finance.yahoo.com/economy/articles/running-money-kraft-mcdonald-whirlpool-114500035.html",
    "source": "MrJagil",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-08-26T05:14:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:49441647",
    "domain": "金融",
    "title": "Complete list of U.S. products subject to counter tariffs",
    "url": "https://www.canada.ca/en/department-finance/programs/international-trade-finance-policy/canadas-response-us-tariffs/complete-list-us-products-subject-to-counter-tariffs.html",
    "source": "jonbaer",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-08-25T22:38:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:49243531",
    "domain": "金融",
    "title": "China is now the world's greatest oil power",
    "url": "https://www.economist.com/finance-and-economics/2026/08/09/china-is-now-the-worlds-great-oil-power",
    "source": "bookofjoe",
    "platform": "hackernews",
    "points": 56,
    "published_at": "2026-08-10T13:40:46+00:00",
    "summary": ""
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
    "id": "hn:49414279",
    "domain": "金融",
    "title": "Tesla discontinues its Solar Roof tiles, not economically viable",
    "url": "https://electrek.co/2026/08/20/tesla-discontinues-solar-roof-panels-only/",
    "source": "MilnerRoute",
    "platform": "hackernews",
    "points": 25,
    "published_at": "2026-08-24T01:21:56+00:00",
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
    "id": "hn:49391382",
    "domain": "金融",
    "title": "Tesla sunsets its Solar Roof tiles",
    "url": "https://www.theverge.com/tech/983167/tesla-solar-roof-tiles-discontinued",
    "source": "doener",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-08-21T17:32:57+00:00",
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
    "id": "hn:49352830",
    "domain": "金融",
    "title": "The most influential economist is oddly unconvincing",
    "url": "https://www.economist.com/finance-and-economics/2026/08/17/the-worlds-most-influential-economist-is-oddly-unconvincing",
    "source": "aragonite",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-08-18T21:15:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:49350858",
    "domain": "金融",
    "title": "AI Is Upending One of Finance's Cushiest Jobs",
    "url": "https://www.bloomberg.com/news/features/2026-06-05/ai-is-upending-traditional-financial-advisor-jobs",
    "source": "theriddlr",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-08-18T18:59:38+00:00",
    "summary": ""
  }
]
```
