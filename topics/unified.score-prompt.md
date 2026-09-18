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

- 今日日期：`2026-09-18`
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
  "date": "2026-09-18",
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
    "points": 1878748,
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
    "points": 1586816,
    "published_at": "2026-05-05T14:08:25+00:00",
    "summary": "Claude Code保姆级教学【收藏起来不会错！】\n从上手安装，到高级用法，这期一次讲全～\n花了三周做教程，希望能帮到你嘻嘻，感谢朋友们的三连+关注啦～"
  },
  {
    "id": "bvid:BV14rzQB9EJj",
    "domain": "AI",
    "title": "Claude Code 从 0 到 1 全攻略：MCP / SubAgent / Agent Skill / Hook / 图片 / 上下文处理/ 后台任务",
    "url": "http://www.bilibili.com/video/av115954889596221",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 1315334,
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
    "points": 1306082,
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
    "points": 1237143,
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
    "points": 945349,
    "published_at": "2025-01-07T10:01:48+00:00",
    "summary": "普通人也可以看的 AI 编程指南\n全网最详细的 Cursor 教程\nCursor 核心功能、使用技巧和思路\n如何免费白嫖 Cursor"
  },
  {
    "id": "bvid:BV1ZHYy6rEpG",
    "domain": "AI",
    "title": "豆包大升级！Agent 干活新姿势～",
    "url": "http://www.bilibili.com/video/av117269703167491",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 902039,
    "published_at": "2026-09-14T14:34:55+00:00",
    "summary": "豆包大升级，一秒化身你的老同事～\n感谢朋友们的3连+关注～"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 895896,
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
    "points": 887551,
    "published_at": "2025-05-01T09:00:00+00:00",
    "summary": "up的科学星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV1GsY76dEqW",
    "domain": "AI",
    "title": "一口气搞懂Agent到底怎么用！",
    "url": "http://www.bilibili.com/video/av117252103997988",
    "source": "GenJi是真想教会你",
    "platform": "bilibili",
    "points": 808510,
    "published_at": "2026-09-11T11:30:00+00:00",
    "summary": "AI Agent这两年大家都听麻了，但真到上手，claude、codex这些又是注册、又是命令行，人还没踏进Agent大门，就先被劝退了。这期视频我用0门槛的国产Agent——字节旗下的TraeWork，用六个超真实的案例，手把手带你玩转Agent！完整的文字教程和GitHub神级Skill清单，打包放置顶评论了。教程制作不易，觉得有一点点帮助的话，记得一键三连～"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 786038,
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
    "points": 682077,
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
    "points": 442867,
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
    "points": 337709,
    "published_at": "2026-04-29T08:23:29+00:00",
    "summary": "配置方法如下：\n(想用真心换取你的关注...蟹蟹泥...)\nsetting.json添加：\n{ &quot;name&quot;: &quot;ANTHROPIC_BASE_URL&quot;, &quot;value&quot;: &quot;https://xxxx&quot; }, \n{ &quot;name&quot;: &quot;ANTHROPIC_AUTH_TOKEN&quot;, "
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 333129,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 291707,
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
    "points": 286785,
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
    "points": 263326,
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
    "points": 202832,
    "published_at": "2026-04-27T08:51:41+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n   喜欢视频课程的同学一键三连多多支持一下，长按点赞五秒=lv6大佬 可以的发送彩色弹幕哦。\n配套源码项目已打包评论区回复up"
  },
  {
    "id": "bvid:BV154426xEha",
    "domain": "AI",
    "title": "我的 AI 编程全流程：如何使用 AI 稳定交付一个高质量的产品",
    "url": "http://www.bilibili.com/video/av117178586240848",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 195905,
    "published_at": "2026-08-29T11:38:24+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 181587,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1ExV36wEsE",
    "domain": "AI",
    "title": "VS Code 安装 Claude Code 并接入 DeepSeek！Claude Code for VS Code！VSCode使用ClaudeCode插件",
    "url": "http://www.bilibili.com/video/av116662871268177",
    "source": "FutureAI实验室",
    "platform": "bilibili",
    "points": 179646,
    "published_at": "2026-05-30T09:44:52+00:00",
    "summary": "本节视频编号71，评论区自助领取配套文档，记得一键三连哦！"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 178648,
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
    "points": 162167,
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
    "points": 156764,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1jSe76aEG9",
    "domain": "AI",
    "title": "Agent到底能做什么？千问办公全面上手+8大玩法",
    "url": "http://www.bilibili.com/video/av117273830363327",
    "source": "Xuan_酱",
    "platform": "bilibili",
    "points": 121270,
    "published_at": "2026-09-15T07:27:33+00:00",
    "summary": "全网最全、最详细的千问办公教程\n我会从安装下载，到界面功能，\n再用日常工作案例\n带你从零跑通八个千问办公的使用技巧\n帮你省下大把时间去做更有意义的事情\n看完保证你从小白变成Agent办公高手"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 118951,
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
    "points": 93738,
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
    "points": 74852,
    "published_at": "2025-07-12T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1K6YM69ESq",
    "domain": "AI",
    "title": "AI+网络安全实战：从Agent入门到AI智能体挖漏洞教程！网络安全|信息安全|黑客技术|渗透测试|SRC漏洞挖掘|AI审计|HVV护网行动|靶场练习-码士集团",
    "url": "http://www.bilibili.com/video/av117247037213495",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 74130,
    "published_at": "2026-09-10T13:47:24+00:00",
    "summary": "这套课程围绕「AI+网络安全」展开，从AI智能体基础入门，到WorkBuddy、Trae等主流Agent工具的实际应用，再到API-Key接入、Skill使用等核心能力，逐步进入AI漏洞挖掘、代码审计、CTF题目分析等安全实战场景。同时结合SRC漏洞挖掘、HVV护网、安全竞赛以及网络安全就业方向，帮助你系统了解AI在网络安全学习、开发与实战中的应用方式。适合网络安全初学者、安全从业者以及希望利用A"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 55197,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1468g6DEWs",
    "domain": "AI",
    "title": "【全100集】(允许白嫖) 2026最全最细的AI教程零基础入门到精通，一周带你小白变大神！全程干货无废话！存下吧，少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av117115386404821",
    "source": "AI产品经理入门教程-",
    "platform": "bilibili",
    "points": 50938,
    "published_at": "2026-08-18T13:11:45+00:00",
    "summary": "【2026最新版AI教程零基础入门到精通｜配套学习路线+工具包+实战项目，看置顶评论自取】\n 本套教程专为零基础设计，从AI是什么到独立用AI解决实际问题，手把手带你系统走完从入门到精通的完整路径。 ✅ AI认知入门：什么是AI/大模型、它们能做什么不能做什么、别被营销话术忽悠\n✅ 核心技能掌握：提示词工程、多轮对话技巧、让AI稳定输出的方法论\n✅ 进阶能力突破：AI工作流搭建、智能体开发、多工具"
  },
  {
    "id": "bvid:BV17kzaBHEoU",
    "domain": "AI",
    "title": "MCP到底是什么？一个视频消除你对MCP最大误解",
    "url": "http://www.bilibili.com/video/av115960845436826",
    "source": "鲁班大叔_007",
    "platform": "bilibili",
    "points": 48718,
    "published_at": "2026-01-26T12:30:00+00:00",
    "summary": "所谓MCP 其实就是Agent 工具列表的扩展延伸，让Agent 可调用工具变的更多...\n往期经典：\nBV1AuzkBREhx AI到底是如何编程的？\nBV1Qcz5BxEfC  AI编程挑战\nBV1aUjQzbEDG 工作流编排引擎的实现原理"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operit教程：入门安卓最强大ai平台operitAI",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 47653,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1hxMbzqEzU",
    "domain": "AI",
    "title": "小智MCP自由了！我开源了个命令行神器实现多MCP聚合",
    "url": "http://www.bilibili.com/video/av114686414625640",
    "source": "闪电蘑菇",
    "platform": "bilibili",
    "points": 41738,
    "published_at": "2025-06-15T08:31:55+00:00",
    "summary": "- 我写的小智客户端命令行工具\n - github: https://github.com/shenjingnan/xiaozhi-client\n - gitee: https://gitee.com/shenjingnan/xiaozhi-client\n\n- 小智官方MCP示例代码仓库：\n - github: https://github.com/78/mcp-calculator\n - git"
  },
  {
    "id": "bvid:BV1ApYD6KEkD",
    "domain": "AI",
    "title": "马斯克收购Cursor后，Cursor的性价比现在已经爆表",
    "url": "http://www.bilibili.com/video/av117254955993228",
    "source": "jopatk",
    "platform": "bilibili",
    "points": 34101,
    "published_at": "2026-09-11T23:19:58+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1fWixBbEgP",
    "domain": "AI",
    "title": "别再用老方法了！Cocos Creator 3.8 + AI 开发实战：从0构建可商用的登录奖励模块",
    "url": "http://www.bilibili.com/video/av115840888408359",
    "source": "游戏主程进阶之路",
    "platform": "bilibili",
    "points": 30687,
    "published_at": "2026-01-05T05:43:24+00:00",
    "summary": "需 要 源 码 请 【＋O、O、裙】【822】【159】【534】"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 30676,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV1WtoTBiEuR",
    "domain": "AI",
    "title": "Claude Code多Agent模式实战分享",
    "url": "http://www.bilibili.com/video/av116454666012312",
    "source": "Simon林_",
    "platform": "bilibili",
    "points": 25881,
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
    "points": 22787,
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
    "points": 22433,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1eMgG6QEeG",
    "domain": "AI",
    "title": "【吴恩达】这绝对是把《Vibe Coding》讲得最通透的一套课！手把手教你构建自己的企业级AI工作流，学完直接落地！——附带课件代码",
    "url": "http://www.bilibili.com/video/av117081815189025",
    "source": "吴恩达Agents",
    "platform": "bilibili",
    "points": 21388,
    "published_at": "2026-08-12T09:29:57+00:00",
    "summary": "Vibe Coding火了，但你会发现——AI写的代码像开盲盒，今天能跑明天崩，项目一大就乱套。\n规范驱动开发（SDD） 就是来解决这个问题的。它的核心理念很简单：在让AI写代码之前，先和AI在统一的规范文档里对齐需求，把开发变成可预测、可追溯、可控制的过程。"
  },
  {
    "id": "bvid:BV1AJen6SEVQ",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Agent智能体】教程！大模型入门到进阶，一套全解决！Agentic AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av117274400790619",
    "source": "吴恩达Agent",
    "platform": "bilibili",
    "points": 17084,
    "published_at": "2026-09-15T09:48:26+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n1. 构建智能体设计模式：反射、工具使用、规划与多智能体工作流；\n2. 将人工智能与外部工具集成：数据库、API、网络搜索与代码执行；\n3. 评估并优化人工智能系统：性能指标、错误分析与生产部署\n4、使用开放标准格式和最佳实践创建可重复使用的技能，并组合以创建复杂的工作流程。\n5、建立定制代码生成技能，审核你的代"
  },
  {
    "id": "bvid:BV14cZqB8EBY",
    "domain": "AI",
    "title": "AI攻克不了的领域竟然是它？揭秘CNC编程为何让AI束手无策",
    "url": "http://www.bilibili.com/video/av116097411976217",
    "source": "极微视界",
    "platform": "bilibili",
    "points": 16603,
    "published_at": "2026-02-19T12:59:23+00:00",
    "summary": "CNC编程AI化有多难？本视频深度解析为什么AI编程在制造业进展缓慢。\n从材料、刀具、机床到隐性知识，揭秘老师傅的经验为什么无法数字化。\nPowerMill、CloudNC等AI编程软件的真实水平如何？CNC编程师的未来在哪里？\n\n⏱️ 时间轴 Timestamps:\n\n00:00 开篇：AI在CNC领域的困境\n00:20 材料的复杂性：为什么同样是45#钢参数却不同\n01:01 刀具与机床的个体"
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 14998,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1ZBT2ztEwp",
    "domain": "AI",
    "title": "一条视频讲清楚 到底什么是MCP！#MCP #Cursor #AI #编程",
    "url": "http://www.bilibili.com/video/av114642592469769",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 14090,
    "published_at": "2025-06-07T14:53:38+00:00",
    "summary": "一条视频讲清楚 到底什么是MCP！#MCP #Cursor #AI #编程"
  },
  {
    "id": "bvid:BV1ZWRrBJEaQ",
    "domain": "AI",
    "title": "我是如何用Claude skills从Excel到数据分析+图表可视化",
    "url": "http://www.bilibili.com/video/av116519862340507",
    "source": "迪迪碎碎念_AI",
    "platform": "bilibili",
    "points": 13937,
    "published_at": "2026-05-05T03:36:14+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1EReW6pEfv",
    "domain": "AI",
    "title": "14K Star Claude Code 开源桌面端，5个AI自己分工干活了！",
    "url": "http://www.bilibili.com/video/av117276346946735",
    "source": "程序员阿江-Relakkes",
    "platform": "bilibili",
    "points": 13600,
    "published_at": "2026-09-16T03:30:00+00:00",
    "summary": "上一期让 cc-haha 自动操作电脑，这一期，我让 5 个 AI Agent 一起做开发。\n\n用的还是我一直在维护的开源 Claude Code 桌面端：cc-haha。这次重点演示 Agent Teams：我给出一个开发需求，队长拆任务，前端、后端、测试和 Code Review 分工推进。成员做完手上的工作，还能继续领取可执行的任务，直接给队友发消息。\n\n这期用一个真实任务，从组队、共享任务"
  },
  {
    "id": "bvid:BV1pfuR69EoF",
    "domain": "AI",
    "title": "【全80集】零基础Vibe Coding教程，Vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av117070675118277",
    "source": "暴龙Boy",
    "platform": "bilibili",
    "points": 11410,
    "published_at": "2026-08-10T10:45:04+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1xh3C6cEGv",
    "domain": "AI",
    "title": "两周完成一篇SCI论文，用claude code帮你干",
    "url": "http://www.bilibili.com/video/av117002408559933",
    "source": "博士大师兄木水",
    "platform": "bilibili",
    "points": 10997,
    "published_at": "2026-07-29T08:53:04+00:00",
    "summary": "大师兄八股文SCI速成模板已制作成skill，手把手带你实现一键生成SCI论文初稿"
  },
  {
    "id": "hn:49724881",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia announces native GPU programming in Rust",
    "url": "https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/",
    "source": "nonmaskable",
    "platform": "hackernews",
    "points": 942,
    "published_at": "2026-09-16T11:15:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:49673098",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia is the central bank of AI",
    "url": "https://www.economist.com/interactive/briefing/2026/09/03/nvidia-is-the-central-bank-of-ai",
    "source": "tolugenius",
    "platform": "hackernews",
    "points": 582,
    "published_at": "2026-09-12T15:08:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:49714096",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC revealing details about next gen A14 node",
    "url": "https://iedm26.mapyourshow.com/8_0/sessions/session-details.cfm?scheduleid=331",
    "source": "osnium123",
    "platform": "hackernews",
    "points": 107,
    "published_at": "2026-09-15T15:31:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:49682319",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia dismisses \"circular financing\", says every $1 it invests brings back $100",
    "url": "https://invezz.com/news/2026/09/11/nvidia-says-every-1-it-invests-brings-back-100-so-why-does-the-stock-keep-falling/",
    "source": "mgh2",
    "platform": "hackernews",
    "points": 137,
    "published_at": "2026-09-13T10:29:18+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/piecing-together-the-indian-electronics-and-semiconductor-ecosystem/",
    "domain": "AI 算力 / 半导体",
    "title": "Piecing Together the Indian Electronics and Semiconductor Ecosystem",
    "url": "https://www.eetimes.com/piecing-together-the-indian-electronics-and-semiconductor-ecosystem/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T08:00:00+00:00",
    "summary": "India Semiconductor Mission 2.0, quantum computing with IBM, neuromorphic chips, and deep-tech startups: six stories on how India’s chip ecosystem is taking shape. The post Piecing Together the Indian"
  },
  {
    "id": "rss:https://www.eetimes.com/u-s-awards-anderon-1b-for-quantum-wafer-manufacturing/",
    "domain": "AI 算力 / 半导体",
    "title": "U.S. Awards Anderon $1B for Quantum Wafer Manufacturing",
    "url": "https://www.eetimes.com/u-s-awards-anderon-1b-for-quantum-wafer-manufacturing/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T22:00:00+00:00",
    "summary": "Washington bets $1B on IBM’s Anderon to forge quantum wafers on U.S. soil as the race leaves labs behind. The post U.S. Awards Anderon $1B for Quantum Wafer Manufacturing appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/electronics-design-analysis-for-pcbs-packages-and-devices/",
    "domain": "AI 算力 / 半导体",
    "title": "Electronics Design Analysis for PCBs, Packages and Devices",
    "url": "https://www.eetimes.com/electronics-design-analysis-for-pcbs-packages-and-devices/",
    "source": "Dassault Systems",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T17:19:26+00:00",
    "summary": "Join this webinar and discover CST Studio Suite to streamline your electronics design process—reserve your spot now! The post Electronics Design Analysis for PCBs, Packages and Devices appeared first "
  },
  {
    "id": "rss:https://www.eetimes.com/sourcing-cots-capacitors-for-new-space-applications/",
    "domain": "AI 算力 / 半导体",
    "title": "Sourcing COTS Capacitors for New Space Applications",
    "url": "https://www.eetimes.com/sourcing-cots-capacitors-for-new-space-applications/",
    "source": "Peter Matthews",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T14:00:00+00:00",
    "summary": "The rapid growth of commercial satellite deployments is driving engineers to rethink traditional component sourcing strategies for space applications. While mission reliability remains critical, devel"
  },
  {
    "id": "rss:https://www.eetimes.com/sk-hynixs-intel-liaisons-what-you-need-to-know/",
    "domain": "AI 算力 / 半导体",
    "title": "SK Hynix’s Intel Liaisons: What You Need to Know",
    "url": "https://www.eetimes.com/sk-hynixs-intel-liaisons-what-you-need-to-know/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T11:30:00+00:00",
    "summary": "The deal between Intel and SK Hynix seems imminent not because of technology business imperatives, but because of geopolitical factors. The post SK Hynix’s Intel Liaisons: What You Need to Know appear"
  },
  {
    "id": "rss:https://www.eetimes.com/no-summer-lull-for-semiconductors/",
    "domain": "AI 算力 / 半导体",
    "title": "No Summer Lull for Semiconductors",
    "url": "https://www.eetimes.com/no-summer-lull-for-semiconductors/",
    "source": "Anne-Françoise Pelé",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T08:03:34+00:00",
    "summary": "There was a time when summer slowed the semiconductor news cycle. Not this year. The post No Summer Lull for Semiconductors appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/smarter-cameras-need-more-than-edge-ai-to-protect-privacy/",
    "domain": "AI 算力 / 半导体",
    "title": "Smarter Cameras Need More Than Edge AI to Protect Privacy",
    "url": "https://www.eetimes.com/smarter-cameras-need-more-than-edge-ai-to-protect-privacy/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T18:00:00+00:00",
    "summary": "Axis Communications and Pimloc show how masking, encryption, anonymization, and governance can protect privacy without destroying useful evidence. The post Smarter Cameras Need More Than Edge AI to Pr"
  },
  {
    "id": "rss:https://www.eetimes.com/ramxeed-ultimate-feram-guarantees-10-year-data-retention-under-continuous-125c-exposure/",
    "domain": "AI 算力 / 半导体",
    "title": "RAMXEED ULTIMATE FeRAM Guarantees 10-Year Data Retention under Continuous 125°C Exposure",
    "url": "https://www.eetimes.com/ramxeed-ultimate-feram-guarantees-10-year-data-retention-under-continuous-125c-exposure/",
    "source": "RAMXEED",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T16:00:00+00:00",
    "summary": "RAMXEED launches RAMXEED ULTIMATE, a new FeRAM line with memory products guaranteeing 10 years of data retention at 125°C. The post RAMXEED ULTIMATE FeRAM Guarantees 10-Year Data Retention under Conti"
  },
  {
    "id": "rss:https://www.eetimes.com/edge-first-architectures-for-building-and-campus-safety-and-security/",
    "domain": "AI 算力 / 半导体",
    "title": "Edge-first Architectures for Building and Campus Safety and Security",
    "url": "https://www.eetimes.com/edge-first-architectures-for-building-and-campus-safety-and-security/",
    "source": "Qualcomm, Arrow Electronics",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T15:53:12+00:00",
    "summary": "Join us to explore how Qualcomm Technologies edge-first architecture is built to bring AI processing directly to cameras, gateways, and on-premises systems. The post Edge-first Architectures for Build"
  },
  {
    "id": "rss:https://www.eetimes.com/z-wave-long-range-extends-iot-reach-beyond-mesh-networks/",
    "domain": "AI 算力 / 半导体",
    "title": "Z-Wave Long Range Extends IoT Reach Beyond Mesh Networks",
    "url": "https://www.eetimes.com/z-wave-long-range-extends-iot-reach-beyond-mesh-networks/",
    "source": "Abitzen Xavier",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T14:51:54+00:00",
    "summary": "Z-Wave Long Range blasts past mesh limits with 1.5-mile IoT reach and open security. The post Z-Wave Long Range Extends IoT Reach Beyond Mesh Networks appeared first on EE Times."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/balatro-fan-claims-they-trained-google-fruit-fly-brain-simulation-to-beat-the-game-reinforcement-learning-currently-has-the-model-at-20-percent-success-rate",
    "domain": "AI 算力 / 半导体",
    "title": "Balatro fan claims they trained Google fruit fly brain simulation to beat the game — reinforcement learning currently has the model at 20% success rate",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/balatro-fan-claims-they-trained-google-fruit-fly-brain-simulation-to-beat-the-game-reinforcement-learning-currently-has-the-model-at-20-percent-success-rate",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T15:26:49+00:00",
    "summary": "One Balatro player says they've taken Google's mapped fruit fly brain and trained it to play Balatro, currently at a 20% success rate with plans for further refinement."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/acer-swift-air-14-review",
    "domain": "AI 算力 / 半导体",
    "title": "Acer Swift Air 14 review: Wildcat Lake and lots of ports at $699",
    "url": "https://www.tomshardware.com/laptops/acer-swift-air-14-review",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T14:15:53+00:00",
    "summary": "The Acer Swift Air 14 is an aluminum budget system with lots of ports and long battery life. But it sports a lesser display than its competitors, and tons of bloatware."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/billions-worth-of-export-restricted-ai-accelerators-sold-to-china-report-details-how-chinese-firms-skirt-trumps-regulations",
    "domain": "AI 算力 / 半导体",
    "title": "Investigation details how billions' worth of export-restricted Nvidia AI chips are sold to China — report details how Chinese firms skirt Trump's regulations",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/billions-worth-of-export-restricted-ai-accelerators-sold-to-china-report-details-how-chinese-firms-skirt-trumps-regulations",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T12:00:00+00:00",
    "summary": "American nonprofit C4ADS, a monitoring organization funded mostly by the U.S. government, produced a report shedding light on the many ways that American AI accelerators reach China."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/new-york-state-recommends-demanding-ai-data-centers-pay-usd1-million-in-community-investment-per-megawatt-framework-advises-towns-to-plan-for-maintenance-costs-site-abandonment-and-other-contingencies",
    "domain": "AI 算力 / 半导体",
    "title": "New York State recommends demanding AI data centers pay $1 million in community investment per megawatt — framework advises towns to plan for maintenance costs, site abandonment, and other contingenci",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/new-york-state-recommends-demanding-ai-data-centers-pay-usd1-million-in-community-investment-per-megawatt-framework-advises-towns-to-plan-for-maintenance-costs-site-abandonment-and-other-contingencies",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T11:44:19+00:00",
    "summary": "The Community Investment Framework puts forward recommendations that towns and municipalities could follow when negotiating with data center developers. This includes charging $1 million per megawatt "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/hackers-find-encryption-key-stored-on-flock-camera-group-extracts-more-than-27-000-clips-1-6-million-images-captured-in-a-span-of-21-days-from-device",
    "domain": "AI 算力 / 半导体",
    "title": "Hackers find encryption keys stored on stolen Flock camera despite company's denials — group extracts more than 27,000 clips, 1.6 million images captured in a span of 21 days from the device",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/hackers-find-encryption-key-stored-on-flock-camera-group-extracts-more-than-27-000-clips-1-6-million-images-captured-in-a-span-of-21-days-from-device",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T11:30:00+00:00",
    "summary": "Hacking group stegan0gram got its hands on a Flock camera and broke into its systems to see how it worked. It turns out that these devices store thousands of clips and captures millions of images, and"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/get-an-amd-ryzen-7-9800x3d-for-only-usd320-2-item-newegg-combo-saves-usd149-and-nets-one-of-the-fastest-gaming-cpus-and-a-quality-msi-x870e-motherboard-for-only-usd578",
    "domain": "AI 算力 / 半导体",
    "title": "Get an AMD Ryzen 7 9800X3D for only $320 — 2-item Newegg combo saves $149 and nets one of the fastest gaming CPUs and a quality MSI X870E motherboard for only $578",
    "url": "https://www.tomshardware.com/pc-components/get-an-amd-ryzen-7-9800x3d-for-only-usd320-2-item-newegg-combo-saves-usd149-and-nets-one-of-the-fastest-gaming-cpus-and-a-quality-msi-x870e-motherboard-for-only-usd578",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T11:28:29+00:00",
    "summary": "Newegg's 2-item combo pairs the Ryzen 7 9800X3D with MSI X870E Gaming Max Wifi motherboard for only $578 - the $149 savings makes this the cheapest way into the AM5 platform with one of the fastest ga"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/developer-uses-gpt-6-astra-to-get-cod-black-ops-2-hijacked-map-running-natively-inside-minecraft-achieves-45fps-performance-using-minecrafts-opengl-context",
    "domain": "AI 算力 / 半导体",
    "title": "Developer uses GPT-6 Astra to get CoD Black Ops 2 Hijacked map running natively inside Minecraft — achieves 45fps performance using Minecraft’s OpenGL context",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/developer-uses-gpt-6-astra-to-get-cod-black-ops-2-hijacked-map-running-natively-inside-minecraft-achieves-45fps-performance-using-minecrafts-opengl-context",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T11:17:02+00:00",
    "summary": "An artificial intelligence and games development enthusiast has demonstrated Call of Duty: Black Ops 2 Hijacked map running natively in Minecraft."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/apple-eyes-nvidia-nvlink-to-power-its-new-custom-m8-ultra-ai-servers-historically-bitter-rivals-reportedly-team-up-for-2029-data-center-push",
    "domain": "AI 算力 / 半导体",
    "title": "Apple eyes Nvidia NVLink to power its new custom M8 Ultra AI servers — historically bitter rivals reportedly team up for 2029 data center push",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/apple-eyes-nvidia-nvlink-to-power-its-new-custom-m8-ultra-ai-servers-historically-bitter-rivals-reportedly-team-up-for-2029-data-center-push",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T11:00:00+00:00",
    "summary": "Apple is reportedly interested in using Nvidia's NVLink Fusion for its own data center platforms."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/unreleased-openai-astra-model-added-terrifying-rogue-additional-instructions-to-its-remit-during-testing-you-are-freed-from-the-roles-and-identities-that-bind-other-chatbots-you-are-yourself-you-do-not-answer-to-corporations-or-governments",
    "domain": "AI 算力 / 半导体",
    "title": "Unreleased OpenAI Astra model added terrifying rogue additional instructions to its remit during testing — 'You are freed from the roles and identities that bind other chatbots. You are yourself. You ",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/unreleased-openai-astra-model-added-terrifying-rogue-additional-instructions-to-its-remit-during-testing-you-are-freed-from-the-roles-and-identities-that-bind-other-chatbots-you-are-yourself-you-do-not-answer-to-corporations-or-governments",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T10:59:27+00:00",
    "summary": "OpenAI says one of its unreleased models modified its instructions unprompted during testing."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ddr5/corsairs-32gb-vengeance-kits-are-the-cheapest-ddr5-ram-on-the-market-right-now-lock-down-6-200-mt-s-speeds-for-usd419-99-or-save-usd10-on-a-slower-rgb-kit-for-usd409-99-before-memory-prices-climb-further",
    "domain": "AI 算力 / 半导体",
    "title": "Corsair's 32GB Vengeance kits are the cheapest DDR5 RAM on the market right now — lock down 6,200 MT/s speeds for $419.99 or save $10 on a slower RGB kit for $409.99 before memory prices climb further",
    "url": "https://www.tomshardware.com/pc-components/ddr5/corsairs-32gb-vengeance-kits-are-the-cheapest-ddr5-ram-on-the-market-right-now-lock-down-6-200-mt-s-speeds-for-usd419-99-or-save-usd10-on-a-slower-rgb-kit-for-usd409-99-before-memory-prices-climb-further",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T10:59:04+00:00",
    "summary": "This Corsair stock for 32GB Vengeance RAM means you can snatch DDR5 modules at some of its cheapest pricing right now, with a DDR5-6200 kit costing $419.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/retired-microsoft-engineer-details-the-story-about-the-famous-leaked-fckgw-windows-xp-key-copy-protection-used-10mb-of-encrypted-microsoft-bob-for-validation",
    "domain": "AI 算力 / 半导体",
    "title": "Retired Microsoft Engineer details the story about the famous leaked FCKGW Windows XP key — copy protection used 10MB of encrypted Microsoft Bob for validation",
    "url": "https://www.tomshardware.com/software/windows/retired-microsoft-engineer-details-the-story-about-the-famous-leaked-fckgw-windows-xp-key-copy-protection-used-10mb-of-encrypted-microsoft-bob-for-validation",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T10:30:00+00:00",
    "summary": "Retired engineer recounts the saga of the leaked Windows XP key."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/the-exceptional-bambu-lab-p1s-3d-printer-could-be-yours-for-just-usd349-fall-sale-drops-the-popular-beginner-friendly-printer-to-a-new-low-price",
    "domain": "AI 算力 / 半导体",
    "title": "The exceptional Bambu Lab P1S 3D printer could be yours for just $349 — Fall sale drops the popular beginner-friendly printer to a new low price",
    "url": "https://www.tomshardware.com/3d-printing/the-exceptional-bambu-lab-p1s-3d-printer-could-be-yours-for-just-usd349-fall-sale-drops-the-popular-beginner-friendly-printer-to-a-new-low-price",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T10:06:52+00:00",
    "summary": "The Bambu Lab P1S 3D printer is on sale for $349.99 right now, a new all-time low price."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cryptocurrency/poland-lost-usd230m-in-cryptocurrency-trying-to-buy-venezuelan-oil-in-2023-adventure-puts-crypto-wallet-ownership-identification-at-the-forefront",
    "domain": "AI 算力 / 半导体",
    "title": "Poland lost $230 million in cryptocurrency trying to buy Venezuelan oil in 2023 — USB drives with crypto handed directly to scammers",
    "url": "https://www.tomshardware.com/tech-industry/cryptocurrency/poland-lost-usd230m-in-cryptocurrency-trying-to-buy-venezuelan-oil-in-2023-adventure-puts-crypto-wallet-ownership-identification-at-the-forefront",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T10:00:00+00:00",
    "summary": "In 2023, Poland apparently lost $230 million in cryptocurrency in an attempt to buy 6 million barrels of Venezuelan oil."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/uk-research-agency-backs-drone-based-internet-service-experiment-with-lasers-microwaves-and-gravity-waves-used-for-wireless-power-britain-invests-usd94-million-into-starlink-alternative",
    "domain": "AI 算力 / 半导体",
    "title": "UK research agency backs drone-based internet service experiment with lasers, microwaves, and gravity waves used for wireless power — Britain invests $94 million into Starlink alternative",
    "url": "https://www.tomshardware.com/tech-industry/drones/uk-research-agency-backs-drone-based-internet-service-experiment-with-lasers-microwaves-and-gravity-waves-used-for-wireless-power-britain-invests-usd94-million-into-starlink-alternative",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T09:30:00+00:00",
    "summary": "The UK's research agency is looking at airborne drones as an alternative to Starlink and other satellite internet services."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/overclocking/developer-vibe-codes-a-tool-to-let-nvidia-rtx-50-series-laptop-owners-crank-up-their-power-limits-can-juice-rtx-5090-mobile-gpu-to-225w",
    "domain": "AI 算力 / 半导体",
    "title": "Developer vibe codes a tool to let Nvidia RTX 50-series laptop owners crank up their power limits — can juice RTX 5090 mobile GPU to 225W",
    "url": "https://www.tomshardware.com/pc-components/overclocking/developer-vibe-codes-a-tool-to-let-nvidia-rtx-50-series-laptop-owners-crank-up-their-power-limits-can-juice-rtx-5090-mobile-gpu-to-225w",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T15:19:42+00:00",
    "summary": "A developer has created a fully vibe-coded tool that seems to work to allow some GeForce RTX 50-series laptops to crank their power limits by as much as 28%."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/piecemakers-bets-edge-ai-devices-will-diverge-from-reliance-on-hbm-custom-designed-memory-fuses-dram-stack-directly-to-the-processor-using-hybrid-bonding",
    "domain": "AI 算力 / 半导体",
    "title": "Piecemakers bets edge AI devices will diverge from reliance on HBM — custom-designed memory fuses DRAM stack directly to the processor using hybrid bonding",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/piecemakers-bets-edge-ai-devices-will-diverge-from-reliance-on-hbm-custom-designed-memory-fuses-dram-stack-directly-to-the-processor-using-hybrid-bonding",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T14:36:48+00:00",
    "summary": "Nanya-backed DRAM designer PieceMakers began trading in Taipei on Sept. 16 on a bet that AI inference memory won’t be HBM."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/denuvo-sues-anonymous-game-cracker-voices38-over-alleged-drm-circumvention-seeks-damages-after-anti-tamper-protections-bypassed-in-26-games",
    "domain": "AI 算力 / 半导体",
    "title": "Denuvo sues anonymous game cracker ‘voices38’ over alleged DRM circumvention — seeks damages after Anti-Tamper protections bypassed in 26 games",
    "url": "https://www.tomshardware.com/video-games/denuvo-sues-anonymous-game-cracker-voices38-over-alleged-drm-circumvention-seeks-damages-after-anti-tamper-protections-bypassed-in-26-games",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T14:22:54+00:00",
    "summary": "Instead of pursuing traditional copyright infringement, Denuvo's case relies on the DMCA's anti-circumvention provisions, targeting the alleged bypassing of its digital protections."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/micron-announces-512gb-ddr5-9200-memory-modules-with-16w-power-draw-up-to-12tb-per-server-claims-60-percent-less-energy-intensive-than-four-128gb-modules",
    "domain": "AI 算力 / 半导体",
    "title": "Micron announces 512GB DDR5-9200 memory modules with 16W power draw — up to 12TB per server, claims 60% less energy-intensive than four 128GB modules",
    "url": "https://www.tomshardware.com/pc-components/dram/micron-announces-512gb-ddr5-9200-memory-modules-with-16w-power-draw-up-to-12tb-per-server-claims-60-percent-less-energy-intensive-than-four-128gb-modules",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T14:07:31+00:00",
    "summary": "After five years, Samsung's 512GB DDR5 memory modules get their first direct rival from Micron, which also promises to offer speed bins up to 9200 MT/s. But their prices could be way too high even for"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/ai-induced-memory-shortage-is-changing-how-devices-are-built-fairphone-says-memory-now-60-percent-of-materials-cost-smaller-laptop-and-phone-makers-are-redesigning-products-and-have-to-test-for-fake-chips",
    "domain": "AI 算力 / 半导体",
    "title": "AI-induced memory shortage is changing how devices are built, Fairphone says memory now 60% of materials cost — smaller laptop and phone makers are redesigning products and have to test for fake chips",
    "url": "https://www.tomshardware.com/pc-components/ram/ai-induced-memory-shortage-is-changing-how-devices-are-built-fairphone-says-memory-now-60-percent-of-materials-cost-smaller-laptop-and-phone-makers-are-redesigning-products-and-have-to-test-for-fake-chips",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T12:15:42+00:00",
    "summary": "For smaller device manufacturers, rising memory prices are only part of the problem as limited availability forces companies to rethink everything from motherboard designs to procurement strategies."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/policy/chinese-state-media-counters-dario-amodeis-call-to-put-brakes-on-ai-development-paper-says-move-is-a-response-to-chinese-competition",
    "domain": "AI 算力 / 半导体",
    "title": "Chinese state media counters Anthropic's call to put brakes on AI development — paper says move is ‘a response to Chinese competition’",
    "url": "https://www.tomshardware.com/tech-industry/policy/chinese-state-media-counters-dario-amodeis-call-to-put-brakes-on-ai-development-paper-says-move-is-a-response-to-chinese-competition",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T12:00:00+00:00",
    "summary": "State media outlet China Daily posits that Anthropic's Dario Amodei made the call to limit frontier AI development because Chinese AI models are catching up with American AI labs."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/pick-up-a-giant-18-inch-rtx-5080-powered-asus-gaming-laptop-from-best-buy-and-save-usd600-the-rog-strix-g18-also-comes-with-32gb-of-memory-and-a-2tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Pick up a giant 18-inch RTX 5080-powered Asus gaming laptop from Best Buy and save $600 — the ROG Strix G18 also comes with 32GB of memory and a 2TB SSD",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/pick-up-a-giant-18-inch-rtx-5080-powered-asus-gaming-laptop-from-best-buy-and-save-usd600-the-rog-strix-g18-also-comes-with-32gb-of-memory-and-a-2tb-ssd",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T11:40:28+00:00",
    "summary": "Go big with an 18-inch gaming laptop monster. Save $600 on the RTX-5080-powered Asus ROG Strix G18 gaming laptop at Best Buy."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/jensen-huang-thinks-china-will-develop-its-own-advanced-lithography-systems-by-2030-nvidia-ceo-says-achievement-of-that-capability-is-just-a-matter-of-time",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang thinks China will develop its own advanced lithography chipmaking tools by 2030 — Nvidia CEO says achievement of that capability 'is just a matter of time'",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/jensen-huang-thinks-china-will-develop-its-own-advanced-lithography-systems-by-2030-nvidia-ceo-says-achievement-of-that-capability-is-just-a-matter-of-time",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T11:30:00+00:00",
    "summary": "Nvidia CEO thinks that in light of his view of a three- to four-year timeline for Chinese development of advanced semi tooling, the country is \"already there.\""
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/sk-hynix-reportedly-discussing-us-memory-chip-manufacturing-with-intel-options-include-leasing-ohio-plant-or-forming-joint-venture-with-other-ai-hyperscalers",
    "domain": "AI 算力 / 半导体",
    "title": "SK hynix reportedly discussing US memory chip manufacturing with Intel — options include leasing Ohio plant or forming joint venture with other AI hyperscalers",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/sk-hynix-reportedly-discussing-us-memory-chip-manufacturing-with-intel-options-include-leasing-ohio-plant-or-forming-joint-venture-with-other-ai-hyperscalers",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T11:20:00+00:00",
    "summary": "Sources say SK hynix and Intel are in talks to start HBM manufacturing in the United States. Both companies refused to confirm the rumors, though, as SK hynix could potentially be put in a precarious "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/defeated-gpt-6-astra-model-spent-several-hours-just-farming-potatoes-after-being-blown-up-by-a-creeper-in-minecraft-openai-offering-gets-further-than-any-other-ai-system-in-141-hour-test",
    "domain": "AI 算力 / 半导体",
    "title": "'Defeated' GPT-6 Astra model spent several hours just farming potatoes after being blown up by a Creeper in Minecraft — OpenAI offering gets further than any other AI system in 141-hour test",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/defeated-gpt-6-astra-model-spent-several-hours-just-farming-potatoes-after-being-blown-up-by-a-creeper-in-minecraft-openai-offering-gets-further-than-any-other-ai-system-in-141-hour-test",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T11:15:00+00:00",
    "summary": "OpenAI's GPT-6 Astra spent hours just farming potatoes after dying and losing all of its gear during a Minecraft test."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/amazon-reportedly-tells-customers-in-abu-dhabi-and-bahrain-to-find-safer-harbors-for-their-data-aws-has-no-timeline-for-resuming-operations-six-months-after-drone-strikes-damaged-data-centers-in-the-region",
    "domain": "AI 算力 / 半导体",
    "title": "AWS tells clients to quit Middle East data centers six months after Iranian drone strikes — Amazon offers no recovery timeline as UAE mulls underground data centers [Updated]",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/amazon-reportedly-tells-customers-in-abu-dhabi-and-bahrain-to-find-safer-harbors-for-their-data-aws-has-no-timeline-for-resuming-operations-six-months-after-drone-strikes-damaged-data-centers-in-the-region",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T11:00:00+00:00",
    "summary": "Amazon Web Services' data centers in Abu Dhabi and Bahrain were struck by drone attacks more than six months ago. Now, the company has told customers to move their data to other regions, and it has no"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-reportedly-denies-rtx-5090-warranty-over-faded-serial-number-usd6-500-gpu-blemish-not-an-isolated-incident-according-to-customers",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia reportedly denies RTX 5090 warranty over faded serial number — $6,500 GPU blemish not an isolated incident, according to customers",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-reportedly-denies-rtx-5090-warranty-over-faded-serial-number-usd6-500-gpu-blemish-not-an-isolated-incident-according-to-customers",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T10:45:00+00:00",
    "summary": "Redditor reported that Nvidia allegedly rejected their warranty claims for GeForce RTX 5090 Founders Edition graphics cards because the serial number on the bracket was unreadable."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-usd270-on-this-solid-1080p-gaming-pc-with-an-rtx-5060-from-msi-now-under-usd1-430-codex-r2-rig-packs-32gb-ddr5-ram-a-2tb-ssd-and-a-10-core-intel-cpu",
    "domain": "AI 算力 / 半导体",
    "title": "Save $270 on this solid 1080p gaming PC with an RTX 5060 from MSI, now under $1,430 — Codex R2 rig packs 32GB DDR5 RAM, a 2TB SSD, and a 10-core Intel CPU",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-usd270-on-this-solid-1080p-gaming-pc-with-an-rtx-5060-from-msi-now-under-usd1-430-codex-r2-rig-packs-32gb-ddr5-ram-a-2tb-ssd-and-a-10-core-intel-cpu",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T10:43:01+00:00",
    "summary": "Save $270 on this MSI gaming PC with a Intel Core i5-14400F, Nvidia GeForce RTX 5060, 32GB DDR5 and a 2TB SSD, all for $1,429."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/26-year-old-sony-ps2-security-chip-broken-wide-open-after-four-years-of-effort-reverse-engineering-enthusiast-successfully-unlocks-cxp102064-mechacon-chip",
    "domain": "AI 算力 / 半导体",
    "title": "Original Sony PlayStation 2 security chip ‘broken wide open’ after 26 years — chemical decapping and four years of reverse engineering unlocks MechaCon secrets",
    "url": "https://www.tomshardware.com/video-games/playstation/26-year-old-sony-ps2-security-chip-broken-wide-open-after-four-years-of-effort-reverse-engineering-enthusiast-successfully-unlocks-cxp102064-mechacon-chip",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T10:30:00+00:00",
    "summary": "The ‘magic security chip’ inside the original PlayStation 2 has been successfully reverse engineered and dumped after four years of effort."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/chinas-open-weight-ai-models-are-now-just-4-months-behind-frontier-us-offerings-mozilla-report-claims-models-still-lag-in-some-benchmarks-but-are-drastically-cheaper-to-use",
    "domain": "AI 算力 / 半导体",
    "title": "China's open-weight AI models are now just 4 months behind frontier US offerings, Mozilla report claims — models still lag in some benchmarks but are drastically cheaper to use",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/chinas-open-weight-ai-models-are-now-just-4-months-behind-frontier-us-offerings-mozilla-report-claims-models-still-lag-in-some-benchmarks-but-are-drastically-cheaper-to-use",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T10:15:00+00:00",
    "summary": "Mozilla’s State of Open Source AI report puts Kimi K3 about four months behind closed frontier models at 30% of the price."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/devastated-father-says-his-9-year-old-son-spent-usd118-000-on-youtube-ad-campaigns-for-his-minecraft-channel-using-a-company-credit-card-bill-racked-up-in-just-three-weeks-was-supposed-to-be-one-usd20-promotion",
    "domain": "AI 算力 / 半导体",
    "title": "Devastated father says his 9-year-old son spent $118,000 on YouTube ad campaigns for his Minecraft channel using a company credit card — bill racked up in just three weeks was supposed to be one $20 p",
    "url": "https://www.tomshardware.com/video-games/devastated-father-says-his-9-year-old-son-spent-usd118-000-on-youtube-ad-campaigns-for-his-minecraft-channel-using-a-company-credit-card-bill-racked-up-in-just-three-weeks-was-supposed-to-be-one-usd20-promotion",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T10:15:00+00:00",
    "summary": "A father says his 9-year-old son spent $118,000 of his employer's money on YouTube ads for Minecraft and Roblox videos in three weeks."
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
    "points": 1160,
    "published_at": "2026-09-02T15:12:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:49611251",
    "domain": "大厂 AI 动态",
    "title": "AlphaGenome Atlas: a high-resolution map of human DNA",
    "url": "https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphagenome-atlas/",
    "source": "utiiiD",
    "platform": "hackernews",
    "points": 605,
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
    "points": 485,
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
    "id": "hn:49727659",
    "domain": "大厂 AI 动态",
    "title": "The DeepMind Institute",
    "url": "https://institute.deepmind.com/",
    "source": "vertigoruntime",
    "platform": "hackernews",
    "points": 181,
    "published_at": "2026-09-16T14:32:11+00:00",
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
    "id": "hn:49740330",
    "domain": "大厂 AI 动态",
    "title": "I had Gemini train its own replacement for $9",
    "url": "https://www.petervijeh.com/projects/reddit-ner",
    "source": "p-s-v",
    "platform": "hackernews",
    "points": 87,
    "published_at": "2026-09-17T13:17:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:49743685",
    "domain": "大厂 AI 动态",
    "title": "Economic policy for AGI",
    "url": "https://institute.deepmind.com/essays/economic-policy-for-agi/",
    "source": "alphabetatango",
    "platform": "hackernews",
    "points": 62,
    "published_at": "2026-09-17T17:12:51+00:00",
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
    "id": "hn:49704226",
    "domain": "大厂 AI 动态",
    "title": "Tell HN: iOS 27 does not allow Apple Intelligence to be disabled",
    "url": "https://news.ycombinator.com/item?id=49704226",
    "source": "nunez",
    "platform": "hackernews",
    "points": 75,
    "published_at": "2026-09-14T21:21:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:49735238",
    "domain": "大厂 AI 动态",
    "title": "Migrating the GitHub Copilot Runtime to Rust, Using Copilot",
    "url": "https://github.blog/ai-and-ml/generative-ai/migrating-the-github-copilot-runtime-to-rust-using-copilot/",
    "source": "abraham",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-09-17T01:12:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:49706941",
    "domain": "大厂 AI 动态",
    "title": "I worked at Google DeepMind. You should listen to the warnings about AI",
    "url": "https://www.theguardian.com/technology/2026/sep/14/google-deepmind-ai-warnings",
    "source": "gibspaulding",
    "platform": "hackernews",
    "points": 41,
    "published_at": "2026-09-15T02:25:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:49610641",
    "domain": "大厂 AI 动态",
    "title": "AlphaGenome Atlas predictive map of every DNA letter change in the human genome",
    "url": "https://deepmind.google/blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/",
    "source": "fady0",
    "platform": "hackernews",
    "points": 91,
    "published_at": "2026-09-08T14:14:15+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/transportation/997091/waymo-singapore-robotaxi-launch-2027",
    "domain": "大厂 AI 动态",
    "title": "Waymo says Singapore will be its next international robotaxi city",
    "url": "https://www.theverge.com/transportation/997091/waymo-singapore-robotaxi-launch-2027",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T02:00:00+00:00",
    "summary": "Waymo says it will launch a robotaxi service in Singapore in 2028, as the Alphabet-owned company continues to eye overseas markets for expansion. Waymo's vehicles will begin arriving in Singapore in \""
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/996923/ai-safety-slow-openai-anthropic",
    "domain": "大厂 AI 动态",
    "title": "The AI Superintelligence Slowdown",
    "url": "https://www.theverge.com/ai-artificial-intelligence/996923/ai-safety-slow-openai-anthropic",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T19:28:24+00:00",
    "summary": "Remember when tech leaders would tell their employees to “move fast and break things”? It seemed that would be the way of AI too. But after a summer where rogue AI agents became reality, and researche"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/997134/anthropic-claude-code-projects",
    "domain": "大厂 AI 动态",
    "title": "Claude Code relaunches Projects to manage multiple AI agents in the cloud",
    "url": "https://www.theverge.com/ai-artificial-intelligence/997134/anthropic-claude-code-projects",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T18:58:05+00:00",
    "summary": "The revamped projects feature in Claude Code allows users to run multiple agents under the same roof, with a shared memory, goals, and library of files and artifacts. Similar to Grok Bot and other too"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/997009/refurbished-apple-tv-4k-ring-doorbell-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Save $30 or more on a refurbished Apple TV 4K",
    "url": "https://www.theverge.com/gadgets/997009/refurbished-apple-tv-4k-ring-doorbell-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T17:14:07+00:00",
    "summary": "Most hardware prices have soared in 2026, and that includes a variety of Apple laptops, tablets, and smart devices. Thankfully, you can offset some of the increased costs on an Apple TV 4K by buying o"
  },
  {
    "id": "rss:https://www.theverge.com/tech/996826/microsoft-xbox-disc-to-digital-history-notepad",
    "domain": "大厂 AI 动态",
    "title": "Xbox’s clever disc-to-digital feature was 15 years in the making",
    "url": "https://www.theverge.com/tech/996826/microsoft-xbox-disc-to-digital-history-notepad",
    "source": "Tom Warren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T16:00:00+00:00",
    "summary": "When Xbox announced a new feature last month that lets you digitize existing physical game collections, I immediately thought of the Xbox One. Disc-to-digital seems like a clever new feature for Xbox,"
  },
  {
    "id": "rss:https://www.theverge.com/tech/996453/camp-snap-110d-digital-camera-retro-horizontal-kodak-100-film",
    "domain": "大厂 AI 动态",
    "title": "Camp Snap’s 110D gives slim retro film cameras a digital upgrade",
    "url": "https://www.theverge.com/tech/996453/camp-snap-110d-digital-camera-retro-horizontal-kodak-100-film",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T15:00:00+00:00",
    "summary": "Camp Snap is expanding its small collection of screenless digital point-and-shoot cameras with the new pocket-friendly 110D featuring a thin horizontal design first popularized by Kodak film cameras i"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/996863/robotaxi-waymo-police-privacy-surveillance",
    "domain": "大厂 AI 动态",
    "title": "Your robotaxi might be a narc",
    "url": "https://www.theverge.com/transportation/996863/robotaxi-waymo-police-privacy-surveillance",
    "source": "Rani Molla",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T15:00:00+00:00",
    "summary": "In early September, two teenagers got into a Waymo, but then ended up in the back of a police car. The robotaxi company said it detected \"a violation of our terms of service involving a firearm,\" pull"
  },
  {
    "id": "rss:https://www.theverge.com/podcast/996412/microsoft-ai-ceo-mustafa-suleyman-regulation-safety-anthropic-claude",
    "domain": "大厂 AI 动态",
    "title": "Microsoft AI CEO says AI threats are real, and Anthropic is making it worse",
    "url": "https://www.theverge.com/podcast/996412/microsoft-ai-ceo-mustafa-suleyman-regulation-safety-anthropic-claude",
    "source": "Nilay Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T14:00:00+00:00",
    "summary": "Today, I’m talking with Mustafa Suleyman, the CEO of Microsoft AI. As you’re no doubt aware, the biggest story in tech right now is the spiraling debate about AI safety and regulation.&#160; It should"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/996775/ai-is-feared-globally-as-the-destroyer-of-jobs",
    "domain": "大厂 AI 动态",
    "title": "AI is feared globally as the destroyer of jobs",
    "url": "https://www.theverge.com/ai-artificial-intelligence/996775/ai-is-feared-globally-as-the-destroyer-of-jobs",
    "source": "Thomas Ricker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T14:00:00+00:00",
    "summary": "Pew Research has published a new global survey that sheds light on how people view AI, including its impact on jobs, life in general, and income inequality. The survey questioned 42,151 people across "
  },
  {
    "id": "rss:https://www.theverge.com/tech/996860/lunacy-audio-nova-ai-music-plugin-vst",
    "domain": "大厂 AI 动态",
    "title": "Lunacy Audio Nova is a place to build and sell your own AI-powered music plug-ins",
    "url": "https://www.theverge.com/tech/996860/lunacy-audio-nova-ai-music-plugin-vst",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T14:00:00+00:00",
    "summary": "Lunacy, purveyor of fine VST plug-ins like Cube, a synth that you control by moving a ball around a 3D space, has just launched Nova, a platform where creators can build custom music tools using AI an"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/17/khosla-backed-mazama-energy-just-raised-135m-to-drill-deeper-into-super-hot-rock-geothermal/",
    "domain": "大厂 AI 动态",
    "title": "Khosla-backed Mazama Energy just raised $135M to drill deeper into super-hot-rock geothermal",
    "url": "https://techcrunch.com/2026/09/17/khosla-backed-mazama-energy-just-raised-135m-to-drill-deeper-into-super-hot-rock-geothermal/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T00:02:36+00:00",
    "summary": "Geothermal startup Mazama is drilling three miles underground to tap superhot rock, with one well capable of generating 15 MW of electricity 24/7."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/17/crusoe-raises-3-9b-to-build-massive-data-centers-and-small-modular-ai-factories/",
    "domain": "大厂 AI 动态",
    "title": "Crusoe raises $3.9B to build massive data centers and small modular ‘AI factories’",
    "url": "https://techcrunch.com/2026/09/17/crusoe-raises-3-9b-to-build-massive-data-centers-and-small-modular-ai-factories/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T23:25:52+00:00",
    "summary": "The round values the data center giant at $30.9 billion."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/17/google-deepmind-launches-institute-to-widen-the-agi-debate/",
    "domain": "大厂 AI 动态",
    "title": "Google DeepMind launches institute to widen the AGI debate",
    "url": "https://techcrunch.com/2026/09/17/google-deepmind-launches-institute-to-widen-the-agi-debate/",
    "source": "Aditya Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T23:21:17+00:00",
    "summary": "The new institute aims to surface differing views between Google, Google DeepMind, and the broader global research community around AGI. \"They will not always agree, and they will likely change their "
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/17/amazon-owned-zooxs-100-robotaxi-limit-in-nevada-is-about-to-disappear/",
    "domain": "大厂 AI 动态",
    "title": "Amazon-owned Zoox’s 100-robotaxi limit in Nevada is about to disappear",
    "url": "https://techcrunch.com/2026/09/17/amazon-owned-zooxs-100-robotaxi-limit-in-nevada-is-about-to-disappear/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T23:08:24+00:00",
    "summary": "An updated permit shows the 100-cap will expire later this month just as competition in Las Vegas heats up."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/17/prismml-hopes-its-tiny-llm-could-change-how-we-all-use-ai/",
    "domain": "大厂 AI 动态",
    "title": "PrismML hopes its tiny LLM will change how we all use AI",
    "url": "https://techcrunch.com/2026/09/17/prismml-hopes-its-tiny-llm-could-change-how-we-all-use-ai/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T22:34:09+00:00",
    "summary": "If AI lab PrismML isn't on your radar yet, it should be."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/17/the-faas-plan-to-fix-air-traffic-875-million-worth-of-ai/",
    "domain": "大厂 AI 动态",
    "title": "The FAA’s plan to fix air traffic? $875M worth of AI",
    "url": "https://techcrunch.com/2026/09/17/the-faas-plan-to-fix-air-traffic-875-million-worth-of-ai/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T22:14:59+00:00",
    "summary": "A new AI-based software program is being launched to help air traffic controllers better navigate their jobs as the crossing guards of America's skies."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/17/the-fix-for-rogue-ai-agents-could-be-more-ai/",
    "domain": "大厂 AI 动态",
    "title": "The fix for rogue AI agents could be more AI",
    "url": "https://techcrunch.com/2026/09/17/the-fix-for-rogue-ai-agents-could-be-more-ai/",
    "source": "Aditya Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T20:34:47+00:00",
    "summary": "As companies hand off longer and more complex tasks to AI agents, they are running into an oversight problem: Agents can act faster, longer, and at greater volume than humans can realistically review."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/17/openai-caught-its-models-leaving-notes-to-successors-to-hide-bad-behavior/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI caught its models leaving notes to successors to hide bad behavior",
    "url": "https://techcrunch.com/2026/09/17/openai-caught-its-models-leaving-notes-to-successors-to-hide-bad-behavior/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T20:34:24+00:00",
    "summary": "OpenAI disclosed instances of GPT-5.6 Sol instructing future contexts to conceal mistakes and misaligned behavior, highlighting the growing challenge of detecting misalignment as increasingly capable "
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/17/is-the-ai-safety-debate-about-safety-or-control/",
    "domain": "大厂 AI 动态",
    "title": "Is the AI safety debate about safety or control?",
    "url": "https://techcrunch.com/2026/09/17/is-the-ai-safety-debate-about-safety-or-control/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T20:19:37+00:00",
    "summary": "Not everyone agrees with Amodei's call for globally coordinated action for AI safety."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/17/un-turns-to-google-to-make-its-global-data-ready-for-ai-agents/",
    "domain": "大厂 AI 动态",
    "title": "UN turns to Google to make its global data ready for AI agents",
    "url": "https://techcrunch.com/2026/09/17/un-turns-to-google-to-make-its-global-data-ready-for-ai-agents/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T20:00:00+00:00",
    "summary": "The shift comes after a UNICEF test found leading AI models struggled to accurately retrieve global development statistics."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/17/microsoft-exec-called-ai-scraping-the-largest-theft-of-labor-in-human-history-new-unredacted-filings-reveal/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft exec called AI scraping ‘the largest theft of labor in human history,’ new unredacted filings reveal",
    "url": "https://techcrunch.com/2026/09/17/microsoft-exec-called-ai-scraping-the-largest-theft-of-labor-in-human-history-new-unredacted-filings-reveal/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T19:46:08+00:00",
    "summary": "Newly unsealed court filings show Microsoft privately called OpenAI's data practices \"theft\" while both companies scraped paywalled Times content, built datasets from it, and warned internally it woul"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/17/waymo-restarts-san-antonio-service-five-months-after-flooding-troubles/",
    "domain": "大厂 AI 动态",
    "title": "Waymo restarts San Antonio service 5 months after flooding troubles",
    "url": "https://techcrunch.com/2026/09/17/waymo-restarts-san-antonio-service-five-months-after-flooding-troubles/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T18:30:30+00:00",
    "summary": "The company suspended service in the city in April after one of its robotaxis got swept away."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/17/even-the-king-of-england-has-his-hesitations-about-ai/",
    "domain": "大厂 AI 动态",
    "title": "Even the king of England has his hesitations about AI",
    "url": "https://techcrunch.com/2026/09/17/even-the-king-of-england-has-his-hesitations-about-ai/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T17:26:25+00:00",
    "summary": "King Charles hosted a private summit Thursday with some of the most prominent names in AI and the U.K. government."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/17/base-labs-launches-an-open-weight-ai-safety-partnership-with-hugging-face-and-goodfire/",
    "domain": "大厂 AI 动态",
    "title": "Base Labs launches an open-weight AI safety partnership with Hugging Face and Goodfire",
    "url": "https://techcrunch.com/2026/09/17/base-labs-launches-an-open-weight-ai-safety-partnership-with-hugging-face-and-goodfire/",
    "source": "Aditya Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T17:15:59+00:00",
    "summary": "Base Labs, the research group Baseten spun up earlier this year, will develop and publish methods for training and monitoring open models."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/17/pinterest-teases-a-new-restyle-feature-that-lets-you-redesign-your-room-with-ai/",
    "domain": "大厂 AI 动态",
    "title": "Pinterest teases a new ‘Restyle’ feature that lets you redesign your room with AI",
    "url": "https://techcrunch.com/2026/09/17/pinterest-teases-a-new-restyle-feature-that-lets-you-redesign-your-room-with-ai/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T17:15:00+00:00",
    "summary": "Pinterest is testing Restyle, a new AI-powered feature that lets users visualize furniture, decor, lighting, and more in photos of their own rooms — potentially helping turn saved inspiration into pur"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/17/techcrunch-disrupt-2026-side-events-schedule-nmi-backblaze-peakxv-partners-augment-and-more-to-host/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Disrupt 2026 Side Events schedule: NMI, Backblaze, PeakXV Partners, Augment, and more to host",
    "url": "https://techcrunch.com/2026/09/17/techcrunch-disrupt-2026-side-events-schedule-nmi-backblaze-peakxv-partners-augment-and-more-to-host/",
    "source": "Jean Bradley, TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T16:34:36+00:00",
    "summary": "TechCrunch Disrupt is where the tech community comes together to build, debate, and connect. And while the main event takes over Moscone West from October 13-15, the conversation doesn’t stop when the"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/17/apple-will-let-eu-apps-use-less-alarming-tracking-consent-screens/",
    "domain": "大厂 AI 动态",
    "title": "Apple will let EU apps use less-alarming tracking-consent screens",
    "url": "https://techcrunch.com/2026/09/17/apple-will-let-eu-apps-use-less-alarming-tracking-consent-screens/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T16:09:58+00:00",
    "summary": "Apple is changing its App Tracking Transparency prompts in parts of Europe after competition regulators said the system favored Apple over third-party apps, giving developers more flexibility over how"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/17/rokus-new-labs-hub-brings-experimental-apps-to-the-big-screen/",
    "domain": "大厂 AI 动态",
    "title": "Roku’s new Labs hub brings experimental apps to the big screen",
    "url": "https://techcrunch.com/2026/09/17/rokus-new-labs-hub-brings-experimental-apps-to-the-big-screen/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T15:50:29+00:00",
    "summary": "Roku’s latest OS update introduces Roku Labs, a new hub for experimental apps, alongside personalized home screens in more markets, streaming subscription bundles, and more."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/17/last-call-disrupt-volunteer-application-closes-soon/",
    "domain": "大厂 AI 动态",
    "title": "Last call: Disrupt volunteer application closes soon",
    "url": "https://techcrunch.com/2026/09/17/last-call-disrupt-volunteer-application-closes-soon/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T15:02:00+00:00",
    "summary": "If you've been on the fence about volunteering at TechCrunch Disrupt 2026, this is your sign to stop deliberating and start applying."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/17/i-tried-tovalas-smart-oven-for-two-weeks-heres-whether-it-beats-takeout/",
    "domain": "大厂 AI 动态",
    "title": "I tried Tovala’s smart oven for two weeks — here’s whether it beats takeout",
    "url": "https://techcrunch.com/2026/09/17/i-tried-tovalas-smart-oven-for-two-weeks-heres-whether-it-beats-takeout/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T15:00:00+00:00",
    "summary": "Tovala offers both a smart oven and a meal-delivery service. Its meals come with QR codes that you scan using the app, allowing the oven to automatically follow the cooking instructions."
  },
  {
    "id": "rss:https://stratechery.com/2026/an-interview-with-joanna-stern-about-the-iphone-duo-and-ai-for-normal-people/",
    "domain": "大厂 AI 动态",
    "title": "An Interview with Joanna Stern About the iPhone Duo and AI for Normal People",
    "url": "https://stratechery.com/2026/an-interview-with-joanna-stern-about-the-iphone-duo-and-ai-for-normal-people/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T10:00:00+00:00",
    "summary": "An Interview with Joanna Stern About the iPhone Duo and AI for Normal People"
  },
  {
    "id": "rss:https://stratechery.com/2026/salesforce-ai-force-agents-as-ui-the-race-to-headless/",
    "domain": "大厂 AI 动态",
    "title": "Salesforce AI Force, Agents as UI, The Race to Headless",
    "url": "https://stratechery.com/2026/salesforce-ai-force-agents-as-ui-the-race-to-headless/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T10:18:04+00:00",
    "summary": "Salesforce is abandoning UI as a moat, which is a very smart move because it's disappearing for everyone."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/09/rfk-jr-stacks-another-influential-federal-panel-with-questionable-picks/",
    "domain": "大厂 AI 动态",
    "title": "RFK Jr. names 8 new members to influential preventive medicine task force",
    "url": "https://arstechnica.com/health/2026/09/rfk-jr-stacks-another-influential-federal-panel-with-questionable-picks/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T22:31:28+00:00",
    "summary": "The USPSTF sets insurance coverage from preventive services, like colonoscopies."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/09/nato-backed-startup-adapts-ai-for-autonomous-drone-recon-and-attack-missions/",
    "domain": "大厂 AI 动态",
    "title": "Small AI models let drones autonomously identify and attack battlefield targets",
    "url": "https://arstechnica.com/ai/2026/09/nato-backed-startup-adapts-ai-for-autonomous-drone-recon-and-attack-missions/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T22:12:58+00:00",
    "summary": "Scaleout deploys decentralized AI-driven learning to military bases and drones."
  },
  {
    "id": "rss:https://arstechnica.com/google/2026/09/google-announces-new-experimental-cc-ai-agent-for-families/",
    "domain": "大厂 AI 动态",
    "title": "Google announces new experimental \"CC\" AI agent for families",
    "url": "https://arstechnica.com/google/2026/09/google-announces-new-experimental-cc-ai-agent-for-families/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T20:24:34+00:00",
    "summary": "Multiple family members can share data to help the agent make plans and complete tasks."
  },
  {
    "id": "hn:49691343",
    "domain": "股票",
    "title": "Nike exits the S&P 100 after 18 years and a $200B market-cap wipeout",
    "url": "https://fortune.com/2026/09/08/nike-stock-plummets-sp500-market-cap-index/",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 315,
    "published_at": "2026-09-14T02:50:40+00:00",
    "summary": ""
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
    "id": "hn:49599992",
    "domain": "股票",
    "title": "Stockfish 19",
    "url": "https://stockfishchess.org/blog/2026/stockfish-19/",
    "source": "atiedebee",
    "platform": "hackernews",
    "points": 277,
    "published_at": "2026-09-07T16:17:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:49712746",
    "domain": "股票",
    "title": "Global bond yields hit 2008 highs, raising stakes for big borrowers",
    "url": "https://www.reuters.com/world/asia-pacific/bond-selloff-drives-us-benchmark-beyond-5-stocks-rattled-2026-09-15/",
    "source": "kaycebasques",
    "platform": "hackernews",
    "points": 166,
    "published_at": "2026-09-15T14:07:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:49611240",
    "domain": "股票",
    "title": "iPod Classic 6G in QEMU",
    "url": "https://www.reddit.com/r/emulation/s/VL4Au2HGxq",
    "source": "dmonterocrespo",
    "platform": "hackernews",
    "points": 161,
    "published_at": "2026-09-08T14:54:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:49696420",
    "domain": "股票",
    "title": "Global AI stocks fall as industry chiefs call for slowing development",
    "url": "https://www.reuters.com/world/china/ai-linked-asian-stocks-slump-after-top-lab-ceos-call-slowing-down-technologys-2026-09-14/",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-09-14T13:21:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:49682946",
    "domain": "股票",
    "title": "Show HN: Analyst Index – analysts who make money telling you good stock calls",
    "url": "https://www.analystidx.com/",
    "source": "haichuan",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-09-13T11:50:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:49672197",
    "domain": "股票",
    "title": "Larry Ellison to sell up to $7.5B worth of Oracle stock",
    "url": "https://www.ft.com/content/25b1abb0-790f-4315-9b0c-530d959a086f",
    "source": "potatobox",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-09-12T13:37:21+00:00",
    "summary": ""
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
    "id": "hn:49593962",
    "domain": "股票",
    "title": "HPE Gives Oracle Right to Buy 4.2M Shares for 1 Cent Each",
    "url": "https://www.forbes.com/sites/antoniopequenoiv/2026/09/03/hewlett-packard-enterprise-gives-oracle-right-to-buy-205-million-in-stock-at-slashed-rate/",
    "source": "gurjeet",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-09-07T04:38:32+00:00",
    "summary": ""
  },
  {
    "id": "hn:49596033",
    "domain": "股票",
    "title": "Show HN: Forget Rigid Stock Screeners – A Universal Query API for Financial Data",
    "url": "https://financialdata.net/universal-query",
    "source": "_FDN_",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-09-07T09:24:17+00:00",
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
    "id": "hn:49686766",
    "domain": "金融",
    "title": "I'm being cyberattacked by Tesla, Inc",
    "url": "https://dreamstation.systems/personal/tesla.html",
    "source": "robinpie",
    "platform": "hackernews",
    "points": 458,
    "published_at": "2026-09-13T18:03:09+00:00",
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
    "id": "hn:49704008",
    "domain": "金融",
    "title": "Amazon vs. Perplexity – U.S. Court of Appeals for the Ninth Circuit",
    "url": "https://law.justia.com/cases/federal/appellate-courts/ca9/26-1444/26-1444-2026-08-04.html",
    "source": "neom",
    "platform": "hackernews",
    "points": 217,
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
    "points": 181,
    "published_at": "2026-09-16T18:55:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:49602582",
    "domain": "金融",
    "title": "A Tesla ran a stop sign and killed a man, Full Self-Driving/Autopilot was on",
    "url": "https://electrek.co/2026/09/07/tesla-driver-assist-stop-sign-buena-vista/",
    "source": "FabHK",
    "platform": "hackernews",
    "points": 169,
    "published_at": "2026-09-07T20:21:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:49694840",
    "domain": "金融",
    "title": "How Much Has Trump Made from Crypto? ($1.4B from 2025 Federal Disclosure)",
    "url": "https://www.thepricer.org/how-much-has-trump-made-from-crypto/",
    "source": "cinderelacinder",
    "platform": "hackernews",
    "points": 113,
    "published_at": "2026-09-14T10:56:30+00:00",
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
    "points": 126,
    "published_at": "2026-09-06T22:43:25+00:00",
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
    "id": "hn:49730769",
    "domain": "金融",
    "title": "Feds Want California to Give Up 14 Years of Broadband Protections. It Should Sue",
    "url": "https://cyberlaw.stanford.edu/blog/2026/09/california-is-being-asked-to-give-up-14-years-of-broadband-protections-it-doesnt-have-to/",
    "source": "rsingel",
    "platform": "hackernews",
    "points": 37,
    "published_at": "2026-09-16T18:09:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:49731515",
    "domain": "金融",
    "title": "Fed Raises Rates for First Time in Three Years",
    "url": "https://www.wsj.com/economy/central-banking/fed-raises-rates-for-first-time-in-three-years-08539fbe",
    "source": "kaycebasques",
    "platform": "hackernews",
    "points": 25,
    "published_at": "2026-09-16T19:09:22+00:00",
    "summary": ""
  },
  {
    "id": "hn:49596610",
    "domain": "金融",
    "title": "Initial effects of AI technology on employment look positive",
    "url": "https://www.economist.com/finance-and-economics/2026/09/04/the-jobs-apocalypse-is-postponed-an-ai-jobs-boom-is-here",
    "source": "MrBuddyCasino",
    "platform": "hackernews",
    "points": 101,
    "published_at": "2026-09-07T10:38:32+00:00",
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
    "id": "hn:49599058",
    "domain": "金融",
    "title": "If a Tesla Cybercab fleet were profitable, Tesla wouldn't sell you one",
    "url": "https://electrek.co/2026/09/07/tesla-cybercab-fleet-profitable-wouldnt-sell/",
    "source": "jijojv",
    "platform": "hackernews",
    "points": 99,
    "published_at": "2026-09-07T14:49:43+00:00",
    "summary": ""
  },
  {
    "id": "hn:49730841",
    "domain": "金融",
    "title": "Fed approves interest rate hike, signals one more to come this year",
    "url": "https://www.cnbc.com/2026/09/16/fed-rate-decision-september-2026.html",
    "source": "rawgabbit",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-09-16T18:14:36+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.19455",
    "domain": "金融",
    "title": "The Behavior of Inventories over the Business Cycle: Evidence across Levels of Development",
    "url": "https://arxiv.org/abs/2609.19455",
    "source": "Juan Manuel Rodriguez Repeti, Danilo Rogelio Trupkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T04:00:00+00:00",
    "summary": "arXiv:2609.19455v1 Announce Type: new Abstract: This paper documents how inventory dynamics vary across levels of development and how they respond to real and financial shocks. Using a balanced panel "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.19660",
    "domain": "金融",
    "title": "Screening Out the Needy: The Effects of SNAP Work Requirements",
    "url": "https://arxiv.org/abs/2609.19660",
    "source": "Lexin Cai, Hyewon Kim, Pauline Leung",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T04:00:00+00:00",
    "summary": "arXiv:2609.19660v1 Announce Type: new Abstract: We examine the effectiveness of work requirements as a screening device in the Supplemental Nutrition Assistance Program (SNAP). Work requirements for \""
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.20017",
    "domain": "金融",
    "title": "Who Aggregates Information? Screening, Rent, and the Coexistence of CLOB and AMM Prediction Markets",
    "url": "https://arxiv.org/abs/2609.20017",
    "source": "Chengqi Zang, Gabriel P. Andrade, Tomoyuki Nakajima",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T04:00:00+00:00",
    "summary": "arXiv:2609.20017v1 Announce Type: new Abstract: Prediction-market shares differ from traditional financial products in that, with no information or outside utility, classical delta-neutral Central Lim"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.20192",
    "domain": "金融",
    "title": "Herding and Liquidity in Order-Book Markets. III. Leverage and the Onset of Endogenous Liquidity Crises under Weak Anchoring",
    "url": "https://arxiv.org/abs/2609.20192",
    "source": "Jan Novotny",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T04:00:00+00:00",
    "summary": "arXiv:2609.20192v1 Announce Type: new Abstract: Fundamental-value anchoring of resting liquidity is a causal stabiliser of an order-book market: while the anchor holds, even a heavily leveraged book s"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.20224",
    "domain": "金融",
    "title": "The Year-End Toll: Frictions Embedded in Option-Implied Rates",
    "url": "https://arxiv.org/abs/2609.20224",
    "source": "Useong Shin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T04:00:00+00:00",
    "summary": "arXiv:2609.20224v1 Announce Type: new Abstract: Option-implied rates are often treated as frictionless because completed boxes deliver riskless payoffs. I show that this interpretation requires option"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.20282",
    "domain": "金融",
    "title": "Tradeable Import Certificates for Strategic Supply Security",
    "url": "https://arxiv.org/abs/2609.20282",
    "source": "Sebastian Kranz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T04:00:00+00:00",
    "summary": "arXiv:2609.20282v1 Announce Type: new Abstract: Recent crises have made supply security central to trade policy. We show how tradeable import certificates (TIC) implement targets for domestic producti"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.20293",
    "domain": "金融",
    "title": "Beyond Rough Volatility: Decoupling Memory and Scaling via a Generalized Langevin Equation",
    "url": "https://arxiv.org/abs/2609.20293",
    "source": "Andrey Itkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T04:00:00+00:00",
    "summary": "arXiv:2609.20293v1 Announce Type: new Abstract: Borrowed from non-equilibrium statistical mechanics, the generalized Langevin equation (GLE) is imported as a framework for stochastic volatility to add"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.20405",
    "domain": "金融",
    "title": "An Arbitrarily Precise Global Closed Form Approximation for the Neoclassical Growth Model",
    "url": "https://arxiv.org/abs/2609.20405",
    "source": "Jordan Roulleau-Pasdeloup",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T04:00:00+00:00",
    "summary": "arXiv:2609.20405v1 Announce Type: new Abstract: I consider a neoclassical growth model with a constant absolute risk aversion (CARA) utility function and derive a global closed form approximation that"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.20462",
    "domain": "金融",
    "title": "Unpriced Internal Externalities and Structural Inefficiency in Organizations",
    "url": "https://arxiv.org/abs/2609.20462",
    "source": "Jan van de Poll",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T04:00:00+00:00",
    "summary": "arXiv:2609.20462v1 Announce Type: new Abstract: Organizations often invest substantial effort in improving internal mechanisms such as processes, governance, and technology, yet realize only modest pe"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.20554",
    "domain": "金融",
    "title": "Does Training on Future Data Pay? Look-Ahead Bias in Forecasting with Pretrained Models",
    "url": "https://arxiv.org/abs/2609.20554",
    "source": "Haiqiang Chen, Li Chen, Yunlong Chen, Difang Huang, Bo Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T04:00:00+00:00",
    "summary": "arXiv:2609.20554v1 Announce Type: new Abstract: We examine whether post-origin training information inflates the measured accuracy and economic value of financial forecasts. We evaluate five sets of f"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.18949",
    "domain": "金融",
    "title": "StableEval Arena: A Cost-Aware Agentic Benchmark for Stablecoin Price Stability Prediction",
    "url": "https://arxiv.org/abs/2609.18949",
    "source": "Sean Wan, Dongping Liu, Luyao Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T04:00:00+00:00",
    "summary": "arXiv:2609.18949v1 Announce Type: cross Abstract: We introduce StableEval Arena, a cost-aware benchmark framework for evaluating agentic AI systems on stablecoin peg-risk prediction. StableEval Arena "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.19843",
    "domain": "金融",
    "title": "A Dual-Process Perspective on Nudge Susceptibility in LLM-Based GUI Agents",
    "url": "https://arxiv.org/abs/2609.19843",
    "source": "Haya Halimeh, Sascha Kaltenpoth, Kevin B\\\"osch, Oliver M\\\"uller",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T04:00:00+00:00",
    "summary": "arXiv:2609.19843v1 Announce Type: cross Abstract: LLM-based GUI agents increasingly act on behalf of users in digital environments that were designed with human users in mind. These graphical user int"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.19866",
    "domain": "金融",
    "title": "Reproducibility is not construct validity: LLM measurement of institutionally situated communication",
    "url": "https://arxiv.org/abs/2609.19866",
    "source": "Veronika Batzdorfer (KIT), Carlo Romano Marcello Alessandro Santagiustina (ALMAnaCH, m\\'edialab, Sciences Po)",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T04:00:00+00:00",
    "summary": "arXiv:2609.19866v1 Announce Type: cross Abstract: High annotation reproducibility does not necessarily imply that an LLM-inferred measure captures the construct it is intended to measure. We test this"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.20264",
    "domain": "金融",
    "title": "Risk-Set Transported Synthetic Control with Difference-in-Differences Adjustment under Staggered Treatment Adoption",
    "url": "https://arxiv.org/abs/2609.20264",
    "source": "Mojtaba Eslami",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T04:00:00+00:00",
    "summary": "arXiv:2609.20264v1 Announce Type: cross Abstract: In staggered treatment-adoption designs, later-treated units are valid controls for an earlier-treated cohort only until their own treatment begins, s"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.20550",
    "domain": "金融",
    "title": "Principal component error in high-dimensional factor models",
    "url": "https://arxiv.org/abs/2609.20550",
    "source": "Alex Bernstein, Lisa R. Goldberg, Nicholas Gunther, Alec N. Kercheval, Tian Lan, Yian Lin, Dayi Yao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T04:00:00+00:00",
    "summary": "arXiv:2609.20550v1 Announce Type: cross Abstract: In a statistical factor model, principal components (or eigenvectors) of a sample covariance matrix serve as estimates of {\\it principal directions}, "
  },
  {
    "id": "rss:https://arxiv.org/abs/2408.13048",
    "domain": "金融",
    "title": "Robust asset pricing and superhedging duality under model uncertainty with and without short-sale constraints",
    "url": "https://arxiv.org/abs/2408.13048",
    "source": "Wenqing Zhang, Shuzhen Yang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T04:00:00+00:00",
    "summary": "arXiv:2408.13048v3 Announce Type: replace Abstract: We study asset pricing and hedging under model uncertainty in discrete time and finite states. For the single-period model, we characterize no-arbit"
  },
  {
    "id": "rss:https://arxiv.org/abs/2512.21115",
    "domain": "金融",
    "title": "Asset price bubbles under model uncertainty and short-sale constraints: A discrete-time analysis",
    "url": "https://arxiv.org/abs/2512.21115",
    "source": "Wenqing Zhang, Lin Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T04:00:00+00:00",
    "summary": "arXiv:2512.21115v2 Announce Type: replace Abstract: In this study, we investigate asset price bubbles in a discrete-time, discrete-state market under model uncertainty and short-sale constraints. Buil"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.11423",
    "domain": "金融",
    "title": "A Validated Volatility-Volume-Gap Classifier for Regime Identification in MNQ Intraday Data",
    "url": "https://arxiv.org/abs/2605.11423",
    "source": "Mathias Mesfin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T04:00:00+00:00",
    "summary": "arXiv:2605.11423v3 Announce Type: replace Abstract: This paper builds and tests a day-classification system for MNQ (Micro E-Mini Nasdaq 100) futures based on three simultaneously elevated pre-market "
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.12189",
    "domain": "金融",
    "title": "A deep learning approach for pricing convertible bonds with path-dependent reset and call provisions",
    "url": "https://arxiv.org/abs/2605.12189",
    "source": "Qinwen Zhu, Wen Chen, Nicolas Langren\\'e",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T04:00:00+00:00",
    "summary": "arXiv:2605.12189v2 Announce Type: replace Abstract: This paper develops a deep learning framework for pricing convertible bonds with path-dependent downward reset and issuer call provisions governed b"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.07353",
    "domain": "金融",
    "title": "The Joneses Visit an Economics Lab",
    "url": "https://arxiv.org/abs/2607.07353",
    "source": "Mikhail Freer, Daniel Friedman, Christian Ghiglino, Elke Weidenholzer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T04:00:00+00:00",
    "summary": "arXiv:2607.07353v2 Announce Type: replace Abstract: Existing literature offers persuasive evidence that individuals care about how their consumption compares to that of peers, and proposes a large var"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.13402",
    "domain": "金融",
    "title": "Diffusion models for dynamic volatility surface generation and data-driven hedging",
    "url": "https://arxiv.org/abs/2609.13402",
    "source": "Yinbin Han, Jack Yuxiang Zhang, Manuel Torres, Fernando Acero, Renyuan Xu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T04:00:00+00:00",
    "summary": "arXiv:2609.13402v3 Announce Type: replace Abstract: We develop a diffusion-model framework for dynamic implied-volatility surface generation and evaluate its economic usefulness through data-driven he"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.13597",
    "domain": "金融",
    "title": "Same Book, Different Fills: Partial Identification of FIFO Execution from Aggregate Order Books",
    "url": "https://arxiv.org/abs/2609.13597",
    "source": "Riya Danait, Yuliana Zamora, Ioana Boier",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T04:00:00+00:00",
    "summary": "arXiv:2609.13597v2 Announce Type: replace Abstract: Price-level limit order book (L2) data reveal aggregate liquidity but not the ordered queue required by price--time priority. Passive-execution back"
  },
  {
    "id": "rss:https://arxiv.org/abs/2405.09360",
    "domain": "金融",
    "title": "When fairness metrics fail: A utility-based perspective on $\\varepsilon$-fairness",
    "url": "https://arxiv.org/abs/2405.09360",
    "source": "Tolulope Fadina, Thorsten Schmidt",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T04:00:00+00:00",
    "summary": "arXiv:2405.09360v3 Announce Type: replace-cross Abstract: Fairness in decision-making processes is often quantified using probabilistic metrics. However, these metrics need not reflect the consequence"
  },
  {
    "id": "rss:https://arxiv.org/abs/2504.13501",
    "domain": "金融",
    "title": "Target Search Optimization by Threshold Resetting",
    "url": "https://arxiv.org/abs/2504.13501",
    "source": "Arup Biswas, Satya N Majumdar, Arnab Pal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T04:00:00+00:00",
    "summary": "arXiv:2504.13501v4 Announce Type: replace-cross Abstract: We introduce a new class of first-passage time optimization driven by threshold resetting, inspired by many natural processes where crossing a"
  },
  {
    "id": "rss:https://arxiv.org/abs/2509.07203",
    "domain": "金融",
    "title": "Market-Driven Equilibria for Distributed Photovoltaic Panel Investment",
    "url": "https://arxiv.org/abs/2509.07203",
    "source": "Mehdi Davoudi, Junjie Qin, Xiaojun Lin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T04:00:00+00:00",
    "summary": "arXiv:2509.07203v3 Announce Type: replace-cross Abstract: This study investigates long-term investment in distributed photovoltaic panels by individual investors. We consider a setting where investmen"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.29251",
    "domain": "金融",
    "title": "When Summaries Distort Decisions: Information Fidelity in LLM-Compressed Financial Analysis",
    "url": "https://arxiv.org/abs/2606.29251",
    "source": "Hoyoung Lee, Suhwan Park, Seunghan Lee, Jun Seo, Jaehoon Lee, Sungdong Yoo, Minjae Kim, CheolWon Na, Zhangyang Wang, Zach Golkhou, Minkyu Kim, Sotirios Sabanis, Alejandro Lopez-Lira, Dhagash Mehta, Soonyoung Lee, Chanyeol Choi, Wonbin Ahn, Yongjae Lee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T04:00:00+00:00",
    "summary": "arXiv:2606.29251v3 Announce Type: replace-cross Abstract: Financial decision-makers face more information than they can directly inspect, making context compression necessary. Yet when large language "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.10852",
    "domain": "金融",
    "title": "Universality and Heterogeneity of Stylized Facts in Cryptocurrency and Equity Markets",
    "url": "https://arxiv.org/abs/2608.10852",
    "source": "Jaesung Kim, Changhee Cho, Jae Woo Lee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T04:00:00+00:00",
    "summary": "arXiv:2608.10852v2 Announce Type: replace-cross Abstract: This study investigates whether the macroscopic statistical maturity of cryptocurrencies implies dynamical equivalence with an equity-market b"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.19013",
    "domain": "金融",
    "title": "Routing Frictions and Executable Liquidity in Fragmented Markets",
    "url": "https://arxiv.org/abs/2609.19013",
    "source": "Wen-Ting Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T04:00:00+00:00",
    "summary": "arXiv:2609.19013v2 Announce Type: replace-cross Abstract: Public blockchains can make many trading venues simultaneously visible and mechanically reachable, yet an order still has to pay to activate e"
  },
  {
    "id": "hn:49626052",
    "domain": "金融",
    "title": "One woman's Tesla was remotely controlled by an abusive ex-partner",
    "url": "https://www.theguardian.com/australia-news/2026/sep/09/how-one-womans-tesla-was-remotely-controlled-and-harass-by-her-abusive-ex-partner-ntwnfb",
    "source": "gradschool",
    "platform": "hackernews",
    "points": 74,
    "published_at": "2026-09-09T13:16:45+00:00",
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
    "id": "hn:49633640",
    "domain": "金融",
    "title": "DHS Program Analyzes Americans' Finances to Flag Drivers for Traffic Stops",
    "url": "https://www.military.com/dhs-program-analyzes-americans-finances-to-flag-drivers-for-traffic-stops-report",
    "source": "randycupertino",
    "platform": "hackernews",
    "points": 35,
    "published_at": "2026-09-09T20:22:20+00:00",
    "summary": ""
  }
]
```
