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

- 今日日期：`2026-08-23`
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
  "date": "2026-08-23",
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
    "title": "9分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 1741206,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1E7wtzaEdq",
    "domain": "AI",
    "title": "从 LLM 到 Agent Skill，一期视频带你打通底层逻辑！",
    "url": "http://www.bilibili.com/video/av116227955497963",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 1719832,
    "published_at": "2026-03-14T14:22:56+00:00",
    "summary": "AI 核心概念大串联：LLM, Token, Context, Context Window, Prompt, User Prompt, System Prompt, Tool, MCP, Agent, Agent Skill，一期视频带你打通 AI 底层逻辑！"
  },
  {
    "id": "bvid:BV1j9MP6wEV9",
    "domain": "AI",
    "title": "从零开始，学会让桌面Agent帮你干活！【小白教程】",
    "url": "http://www.bilibili.com/video/av116861865887789",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 1337931,
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
    "points": 1283040,
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
    "points": 1169745,
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
    "points": 1091758,
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
    "points": 944095,
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
    "points": 876940,
    "published_at": "2025-05-01T09:00:00+00:00",
    "summary": "up的科学星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV1ZzvUBXEoL",
    "domain": "AI",
    "title": "【2026最新版】保姆级AI Agent智能体系统教程，手把手带你从0基础开始搭建企业级AI Agent智能体！全程干货无废话！让你少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av115818910194374",
    "source": "极客教学",
    "platform": "bilibili",
    "points": 858223,
    "published_at": "2026-01-01T08:40:14+00:00",
    "summary": "【2026最新版】保姆级AI Agent智能体系统教程，手把手带你从0基础开始搭建企业级AI Agent智能体！全程干货无废话！让你少走99%的弯路！"
  },
  {
    "id": "bvid:BV1WBG9zgECp",
    "domain": "AI",
    "title": "史上最强 AI 编程工具免费啦！Cursor 保姆级使用教程！新手友好！看到就是赚到！｜ 集成 MCP ！",
    "url": "http://www.bilibili.com/video/av114426116120045",
    "source": "AfterShip",
    "platform": "bilibili",
    "points": 671834,
    "published_at": "2025-05-01T04:00:00+00:00",
    "summary": "相信你已经在网上刷到过不少的 AI 工具，但如果你让我推荐最值得我们每个人学习的一款 AI 工具，那绝对就是史上最强的 AI 编程工具 —— Cursor。为此，我们录制了一个保姆级的 Cursor 新手教程，在这里免费分享给大家。即使你是一个对 AI 完全 0 基础的新手小白，看完这个视频后，你也可以彻底了解 Cursor 这个软件，并知道如何从 0 到 1 用 Cursor 做出入门级的 AI"
  },
  {
    "id": "bvid:BV1wugF6YEL3",
    "domain": "AI",
    "title": "再见Claude Code！你好DeepSeek Harness！",
    "url": "http://www.bilibili.com/video/av117089415204498",
    "source": "Lau博士的云组会",
    "platform": "bilibili",
    "points": 657069,
    "published_at": "2026-08-13T17:42:16+00:00",
    "summary": "DeepSeek Harness开源了。看完就两个字：牛逼\n本期视频，Lau博士就带着大家一起，解读DeepSeek 亲手做的这个 Harness，到底有什么不一样。"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 635557,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 616487,
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
    "points": 570467,
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
    "points": 439319,
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
    "points": 352499,
    "published_at": "2025-07-30T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从概念到安装，再到Claude Code的具体使用，开发效率原地起飞！"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 271284,
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
    "points": 249886,
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
    "points": 244752,
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
    "points": 179699,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV16Luq6FEmP",
    "domain": "AI",
    "title": "当不懂代码的老婆，第一次接触vibe coding……",
    "url": "http://www.bilibili.com/video/av117076211536327",
    "source": "糖果果的未来要发光",
    "platform": "bilibili",
    "points": 176616,
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
    "points": 165328,
    "published_at": "2026-04-27T08:51:41+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n   喜欢视频课程的同学一键三连多多支持一下，长按点赞五秒=lv6大佬 可以的发送彩色弹幕哦。\n配套源码项目已打包评论区回复up"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 161206,
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
    "points": 159475,
    "published_at": "2025-02-18T13:13:51+00:00",
    "summary": "我试用了几十种AI编程辅助工具，找到了其中三个免费，并且效果最好的方案。 本期视频就来跟大家分享一下。视频中间会穿插很多AI编程工具的使用技巧，还有看待AI编程的一些个人思考。本期视频没有广告都是个人的经验干货，废话不多说我们直接开始。"
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 153051,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1RNTtzMENj",
    "domain": "AI",
    "title": "从零编写MCP并发布上线，超简单！手把手教程",
    "url": "http://www.bilibili.com/video/av114630814862349",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 153027,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 140868,
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
    "points": 99828,
    "published_at": "2025-04-15T11:00:00+00:00",
    "summary": "最近MCP太火了，阿里直接跟进把MCP整合到百炼平台里面了，做了一个MCP的“应用商店”。\n之前不管是在cursor还是Claude上还是需要配置一下MCP服务器，现在在百炼上就可以直接无脑添加MCP工具，非常方便。\n而且因为在平台上一体化，和大模型可以打包配置，让后端的运维部署变得更轻松。\n这个视频教你怎么用阿里云百炼的MCP工具创建一个agent应用。"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 94953,
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
    "points": 93326,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1myM96nETU",
    "domain": "AI",
    "title": "AI 赛博女友！本地部署教程，无需 API、完全免费，8G显存就能跑！实时语音聊天，几乎零延迟，太上头了！| 零度解说",
    "url": "http://www.bilibili.com/video/av117032322339286",
    "source": "零度解说",
    "platform": "bilibili",
    "points": 54926,
    "published_at": "2026-08-04T12:00:00+00:00",
    "summary": "AI 赛博女友一键安装包下载：https://www.freedidi.com/24984.html"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 54362,
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
    "points": 47641,
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
    "points": 45695,
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
    "points": 40940,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV19W8M69ELt",
    "domain": "AI",
    "title": "【入站必看】B站史上最全Codex零基础教程！90分钟入门到进阶！（含22大案例+30000字配套图文资料）",
    "url": "http://www.bilibili.com/video/av117131979134458",
    "source": "GenJi是真想教会你",
    "platform": "bilibili",
    "points": 36828,
    "published_at": "2026-08-22T03:02:11+00:00",
    "summary": "欢迎来到「GenJi的好奇心作坊」第一期充电专属视频，也是一套为精心大家准备的90分钟Codex保姆级教程。课程前后耗时数月，从安装配置、界面操作和基础功能讲起，再通过22个真实案例，带你完成AI短片、自动剪辑、数据动画等专业项目。\n即使没有编程基础，也能跟着课程走完需求表达、任务拆解、执行制作、报错修复、结果验证和最终交付的完整流程。\n本期使用的提示词、Skill和插件清单也已全部整理好，充电后"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 34170,
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
    "points": 30291,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operitAI教程：入门安卓最强大ai平台",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 30268,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29648,
    "published_at": "2025-07-16T13:10:54+00:00",
    "summary": "Cursor用不了？三款AI编程工具完美代替Cursor\naugmentCode\nTrae\nKiro"
  },
  {
    "id": "bvid:BV1aQMX6oEni",
    "domain": "AI",
    "title": "【Agent面经】目前B站最细的（AI Agent）高频面试八股文，吊打付费，帮你避开99%面试坑！存下吧，很难找全的！",
    "url": "http://www.bilibili.com/video/av117030678239428",
    "source": "Agent开发实战",
    "platform": "bilibili",
    "points": 24771,
    "published_at": "2026-08-03T08:50:19+00:00",
    "summary": "【Agent面试100问】目前B站最细的（AI Agent）高频面试八股文，吊打付费，帮你避开99%面试坑！存下吧，很难找全的！"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22732,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1Z5KU6UExC",
    "domain": "AI",
    "title": "【吴恩达2026】Vibe Coding保姆级教程，手把手从环境搭建到工作流完整闭环！——DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116951003242391",
    "source": "吴恩达AIAgent",
    "platform": "bilibili",
    "points": 22333,
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
    "points": 20496,
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
    "points": 19943,
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
    "points": 17737,
    "published_at": "2025-01-05T09:01:00+00:00",
    "summary": "网上惊呼Cursor AI厉害的内容很多，但结合Unity做游戏的不多，我就来实测一下，做一个AAA大作......"
  },
  {
    "id": "bvid:BV1hmb26ZEws",
    "domain": "AI",
    "title": "DeepSeek Harness 实测  Claude Code 对比后，梁神我错了 差距比我想的大",
    "url": "http://www.bilibili.com/video/av117100337236191",
    "source": "程序员晓刘",
    "platform": "bilibili",
    "points": 14775,
    "published_at": "2026-08-15T16:01:38+00:00",
    "summary": "这期用同一个 DeepSeek Pro 0813 模型，分别在 Claude Code 和 DeepSeek Harness 里完成同样的任务，对比工具链对最终效果的影响。\n实测内容包括：\nFPS 游戏 Demo、灯塔预警沙盘、手枪组装动画、显示器组装动画，以及 DeepSeek Harness 的插件化源码流程。\n整体看下来，模型本身当然重要，但 Harness 在插件化、流程记录、缓存命中和任"
  },
  {
    "id": "bvid:BV11EJn6JEk9",
    "domain": "AI",
    "title": "claude+ccswitch配置glm5.2",
    "url": "http://www.bilibili.com/video/av116742495999581",
    "source": "cctryflow",
    "platform": "bilibili",
    "points": 13938,
    "published_at": "2026-06-13T11:13:45+00:00",
    "summary": "智谱文档：https://docs.bigmodel.cn/cn/coding-plan/latest-model"
  },
  {
    "id": "bvid:BV1GT3t6aEDd",
    "domain": "AI",
    "title": "【2026 最新】Claude Code保姆级全套教程｜安装配置｜环境调试｜案例实战｜AI 辅助编程完整学习",
    "url": "http://www.bilibili.com/video/av117007877999539",
    "source": "IT职业规划-码士集团",
    "platform": "bilibili",
    "points": 11718,
    "published_at": "2026-07-30T09:09:33+00:00",
    "summary": "本合集完整讲解 Claude Code 这款 AI 编码工具，包含软件安装、环境配置、实操案例，保姆式教学，帮助开发者提升编码效率，适合后端、程序员学习，持续更新建议收藏。"
  },
  {
    "id": "bvid:BV1f57C6YErb",
    "domain": "AI",
    "title": "手把手教你Codex安装和使用MCP！新手必备~",
    "url": "http://www.bilibili.com/video/av116696861907147",
    "source": "Raina测试",
    "platform": "bilibili",
    "points": 11170,
    "published_at": "2026-06-06T11:29:00+00:00",
    "summary": "这一期给大家分享下在codex里面如何配置和使用MCP，和skill一样，MCP也是我们平时用得比较多的，所以建议大家也可以学一下它的基础配置和使用~\n步骤都不难，跟着操作就可以了"
  },
  {
    "id": "hn:49255710",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's Risky Business",
    "url": "https://stratechery.com/2026/nvidias-risky-business/",
    "source": "jonbaer",
    "platform": "hackernews",
    "points": 356,
    "published_at": "2026-08-11T10:02:00+00:00",
    "summary": ""
  },
  {
    "id": "hn:49323686",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia dramatically reduces amount of OpenAI infra financing it may guarantee",
    "url": "https://www.reuters.com/business/nvidia-scales-back-250-billion-openai-data-center-guarantee-wsj-reports-2026-08-14/",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 252,
    "published_at": "2026-08-16T21:07:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:49263340",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Nemotron 3.5 Lightning and NeMo Switchyard",
    "url": "https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/",
    "source": "droidjj",
    "platform": "hackernews",
    "points": 262,
    "published_at": "2026-08-11T19:35:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:49387755",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia AVO scores 100% on the ARC-AGI-3 interactive reasoning benchmark",
    "url": "https://twitter.com/NVIDIAAI/status/2090786258981466231",
    "source": "dsrtslnd23",
    "platform": "hackernews",
    "points": 70,
    "published_at": "2026-08-21T13:26:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:49257947",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Nemotron 3.5 Lightning",
    "url": "https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-NVFP4",
    "source": "beklein",
    "platform": "hackernews",
    "points": 122,
    "published_at": "2026-08-11T13:26:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:49393647",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia just showed that the harness, not the AI model, is now the real hero",
    "url": "https://techcrunch.com/2026/08/21/nvidia-just-showed-that-the-harness-not-the-ai-model-is-now-the-real-hero/",
    "source": "dthread3",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-08-21T20:52:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:49388268",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia AVO achieves 100% in ARC-AGI-3",
    "url": "https://developer.nvidia.com/blog/nvidia-avo-reaches-100-on-arc-agi-3-demonstrating-a-frontier-level-general-purpose-architecture-for-long-horizon-autonomous-agents/",
    "source": "rochansinha",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-08-21T14:05:37+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/chinas-nand-specialist-ymtc-moves-closer-to-ipo/",
    "domain": "AI 算力 / 半导体",
    "title": "China’s NAND Specialist YMTC Moves Closer to IPO",
    "url": "https://www.eetimes.com/chinas-nand-specialist-ymtc-moves-closer-to-ipo/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T18:00:00+00:00",
    "summary": "YMTC must raise capital to explore demand for AI-driven memory while balancing domestic and overseas markets. The post China’s NAND Specialist YMTC Moves Closer to IPO appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/the-human-brain-versus-ai-similar-results-very-different-machines/",
    "domain": "AI 算力 / 半导体",
    "title": "The Human Brain Versus AI: Similar Results, Very Different Machines",
    "url": "https://www.eetimes.com/the-human-brain-versus-ai-similar-results-very-different-machines/",
    "source": "Lauro Rizzatti",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T07:43:42+00:00",
    "summary": "Contrast 20 watts with a megawatt: The brain and the LLM aren’t in the same race. The post The Human Brain Versus AI: Similar Results, Very Different Machines appeared first on EE Times."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/microsoft-blames-rgb-peripherals-for-crashing-windows-11-rgb-software-is-causing-blue-screens-crashes-and-game-freezes",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft blames RGB peripherals for crashing Windows 11 — RGB software is causing blue screens, crashes, and game freezes",
    "url": "https://www.tomshardware.com/software/windows/microsoft-blames-rgb-peripherals-for-crashing-windows-11-rgb-software-is-causing-blue-screens-crashes-and-game-freezes",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T16:21:34+00:00",
    "summary": "RGB software is reportedly wreaking havoc on Windows PCs. The drivers used by these applications can trip up anti-cheat software, causing your games or entire system to crash. For now, the only soluti"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/linux/25-years-after-the-death-of-3dfx-the-voodoo-3-gets-a-linux-driver-update-classic-voodoo-gpus-can-now-boot-without-a-pc-bios",
    "domain": "AI 算力 / 半导体",
    "title": "25 years after the death of 3dfx, the Voodoo 3 gets a Linux driver update — classic Voodoo GPUs can now boot without a PC BIOS",
    "url": "https://www.tomshardware.com/software/linux/25-years-after-the-death-of-3dfx-the-voodoo-3-gets-a-linux-driver-update-classic-voodoo-gpus-can-now-boot-without-a-pc-bios",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T15:48:10+00:00",
    "summary": "It's been a quarter-century since the firm folded, but the graphics chips still have utility in esoteric use cases."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/case-fans/snap-on-lcd-brings-mini-displays-to-any-120mm-pc-fan-thermalrights-fan-frame-vision-1-lets-you-display-information-and-custom-themes-on-your-case-fans",
    "domain": "AI 算力 / 半导体",
    "title": "Snap-on LCD brings mini displays to any 120mm PC fan — Thermalright's Fan Frame Vision-1 lets you display information and custom themes on your case fans",
    "url": "https://www.tomshardware.com/pc-components/case-fans/snap-on-lcd-brings-mini-displays-to-any-120mm-pc-fan-thermalrights-fan-frame-vision-1-lets-you-display-information-and-custom-themes-on-your-case-fans",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T14:49:09+00:00",
    "summary": "The Thermalright Fan Frame Vision-1 is a clip-on 3.69-inch screen that snaps directly in front of your PC case fans. These accessories let you display temperature, fan speed, and other information acr"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/ascii-cyberpunk-city-prototype-runs-on-rust-webassembly-engine-and-webgl-shaders",
    "domain": "AI 算力 / 半导体",
    "title": "Walk through a 3D cyberpunk city built purely from ASCII characters — a text-based metropolis runs on a 283KB Rust WebAssembly engine feeding a WebGL renderer",
    "url": "https://www.tomshardware.com/tech-industry/ascii-cyberpunk-city-prototype-runs-on-rust-webassembly-engine-and-webgl-shaders",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T14:37:14+00:00",
    "summary": "Solo developer Grow Now! Games has put a playable browser build of its walkable ASCII cyberpunk city online, powered by a 283KB Rust WebAssembly engine and rendered in WebGL."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/logitech-faces-lawsuit-for-withholding-usd61m-in-tariff-refunds-from-customers-lawsuit-claims-company-extracted-up-to-usd97m-from-consumers-in-2026-through-tariff-justified-price-increases",
    "domain": "AI 算力 / 半导体",
    "title": "Logitech faces lawsuit for withholding $61M in tariff refunds from customers — lawsuit claims company extracted up to $97M from consumers in 2026 through tariff-justified price increases",
    "url": "https://www.tomshardware.com/peripherals/logitech-faces-lawsuit-for-withholding-usd61m-in-tariff-refunds-from-customers-lawsuit-claims-company-extracted-up-to-usd97m-from-consumers-in-2026-through-tariff-justified-price-increases",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T14:13:50+00:00",
    "summary": "Consumers who bought products from Logitech after it increased its prices due to tariffs still haven't received their refunds, even after the U.S. government returned $61 million to the company. Now t"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-mice/razer-hyperflux-v2-review-the-best-wireless-charging-mat-for-razer-mice",
    "domain": "AI 算力 / 半导体",
    "title": "Razer HyperFlux V2 Review: The best wireless charging mat for Razer mice",
    "url": "https://www.tomshardware.com/peripherals/gaming-mice/razer-hyperflux-v2-review-the-best-wireless-charging-mat-for-razer-mice",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T14:08:39+00:00",
    "summary": "Razer's HyperFlux V2 is a wireless charging mouse pad that works with current mice from Razer's Basilisk, Cobra, and Naga lines."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/us-authorities-say-siemens-controllers-used-for-water-and-other-infrastructure-are-being-targeted-by-hackers-agencies-claim-threat-actors-use-ai-tools-to-generate-exploitation-scripts",
    "domain": "AI 算力 / 半导体",
    "title": "US authorities say Siemens controllers used for water and other infrastructure are being targeted by hackers — agencies claim threat actors use AI tools to generate exploitation scripts",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/us-authorities-say-siemens-controllers-used-for-water-and-other-infrastructure-are-being-targeted-by-hackers-agencies-claim-threat-actors-use-ai-tools-to-generate-exploitation-scripts",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T13:57:17+00:00",
    "summary": "Siemens S7 PLCs, commonly used in critical infrastructure, are reportedly being targeted by hackers and could potentially lead to disruption of industrial processes, safety incidents, downtime or equi"
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/save-usd532-on-a-480-hz-oled-gaming-monitor-amazon-drops-a-massive-53-percent-discount-on-the-lg-ultragear-27gx790a-b",
    "domain": "AI 算力 / 半导体",
    "title": "Save $532 on a 480 Hz OLED gaming monitor — Amazon drops a massive 53% discount on the LG UltraGear 27GX790A-B",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/save-usd532-on-a-480-hz-oled-gaming-monitor-amazon-drops-a-massive-53-percent-discount-on-the-lg-ultragear-27gx790a-b",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T13:50:07+00:00",
    "summary": "The LG UltraGear 27GX790A-B packs a 27-inch 1440p WOLED panel with a 480 Hz refresh rate, 0.03ms response time, and support for DisplayHDR True Black 400."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/this-week-on-toms-hardware-premium-august-22-2026-foundries-supercomputers-china-and-how-to-not-overpay-on-a-motherboard",
    "domain": "AI 算力 / 半导体",
    "title": "This week on Tom's Hardware Premium: August 22, 2026 — foundries, supercomputers, China, and how to not overpay on a motherboard",
    "url": "https://www.tomshardware.com/tech-industry/this-week-on-toms-hardware-premium-august-22-2026-foundries-supercomputers-china-and-how-to-not-overpay-on-a-motherboard",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T13:00:00+00:00",
    "summary": "We recap this week's Tom's Hardware Premium articles, including our latest advice on your next motherboard purchase, a look inside Samsung's Fab roadmaps, and much more."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/desktop-cpu-shipments-crater-20-percent-amid-high-component-costs-but-amd-gains-record-share-despite-ugly-desktop-processor-market-intel-floods-laptop-market-with-millions-of-cpus-but-amd-still-sets-all-time-share-records",
    "domain": "AI 算力 / 半导体",
    "title": "Desktop CPU shipments crater 20% amid high component costs, but AMD gains record share despite 'ugly' desktop processor market — Intel floods laptop market with millions of CPUs, but AMD still sets al",
    "url": "https://www.tomshardware.com/pc-components/cpus/desktop-cpu-shipments-crater-20-percent-amid-high-component-costs-but-amd-gains-record-share-despite-ugly-desktop-processor-market-intel-floods-laptop-market-with-millions-of-cpus-but-amd-still-sets-all-time-share-records",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T12:30:00+00:00",
    "summary": "As Intel boosts output of data center and notebook CPUs, AMD manages to outgrow it and keep capturing market share from its arch-rival."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/storage-unit-auction-winner-finds-retro-pentium-4-pc-with-a-see-through-uv-reactive-psu-y2k-time-capsule-discovered-among-100-laptops-and-hundreds-of-ram-sticks",
    "domain": "AI 算力 / 半导体",
    "title": "Storage unit auction winner finds retro Pentium 4 PC with a see-through, UV-reactive PSU — Y2K time capsule discovered among 100 laptops and hundreds of RAM sticks",
    "url": "https://www.tomshardware.com/pc-components/storage-unit-auction-winner-finds-retro-pentium-4-pc-with-a-see-through-uv-reactive-psu-y2k-time-capsule-discovered-among-100-laptops-and-hundreds-of-ram-sticks",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T12:00:00+00:00",
    "summary": "This vintage PC build looks like it came straight out of the 90s with a bold, in-your-face look that make sure you can't mistake it for anything but a gamer's lifeline. What you're looking at is an Ap"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/gigabyte-rtx-3070-owner-discovers-protective-film-on-vrm-thermal-pads-after-nearly-five-years-claims-removal-and-repasting-dropped-gpu-hotspot-temperatures-by-30-c",
    "domain": "AI 算力 / 半导体",
    "title": "Gamer uncovers factory plastic left on RTX 3070 VRM pads after five years, causing overheating — claims removal and repasting dropped GPU hotspot temperatures by 30°C",
    "url": "https://www.tomshardware.com/pc-components/gpus/gigabyte-rtx-3070-owner-discovers-protective-film-on-vrm-thermal-pads-after-nearly-five-years-claims-removal-and-repasting-dropped-gpu-hotspot-temperatures-by-30-c",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T11:30:00+00:00",
    "summary": "A Gigabyte RTX 3070 owner discovered protective films covering its VRM thermal pads, after nearly five years of use potentially causing excessive temperatures and frequent black screens."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/power-supplies/asrock-steel-legend-sl-1200p-power-supply-review",
    "domain": "AI 算力 / 半导体",
    "title": "ASRock Steel Legend SL-1200P power supply review: A winning combination of genuine Platinum efficiency and a stand-out design",
    "url": "https://www.tomshardware.com/pc-components/power-supplies/asrock-steel-legend-sl-1200p-power-supply-review",
    "source": "E. Fylladitakis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T11:05:00+00:00",
    "summary": "The ASRock Steel Legend SL-1200P is a visually distinct, technically capable 1200W unit with genuine Platinum efficiency, dual 12V-2x6 outputs, and a few thoughtful engineering touches that set it apa"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/console-gaming/take-two-subpoenas-microsoft-for-windows-device-ids-of-everyone-in-three-discord-servers-in-gta-6-leak-hunt",
    "domain": "AI 算力 / 半导体",
    "title": "GTA 6 leaks prompt Take-Two to subpoena Microsoft for Windows device IDs of everyone in three Discord servers — daily gameplay leaks shatter cloud of secrecy around the much-hyped game",
    "url": "https://www.tomshardware.com/video-games/console-gaming/take-two-subpoenas-microsoft-for-windows-device-ids-of-everyone-in-three-discord-servers-in-gta-6-leak-hunt",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T11:00:00+00:00",
    "summary": "Take-Two Interactive filed two DMCA subpoenas demanding that Microsoft and Discord identify the person or people behind the \"CyberLeek\" persona."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/console-gaming/us-console-sales-fall-39-percent-in-july-as-memory-costs-push-average-price-to-542",
    "domain": "AI 算力 / 半导体",
    "title": "Spending on physical games falls to lowest on record since 1995 — US console sales plunge 39% in July as memory costs push average price to $542",
    "url": "https://www.tomshardware.com/video-games/console-gaming/us-console-sales-fall-39-percent-in-july-as-memory-costs-push-average-price-to-542",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T10:30:00+00:00",
    "summary": "U.S. console hardware sales fell 39% by unit volume in July against a year earlier, while the average price paid for a new system rose 16% to $542."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/pc-building/alleged-amazon-cpu-scam-hits-pc-shop-twice-in-three-days-ryzen-5-9600x-orders-arrive-with-empty-retail-boxes",
    "domain": "AI 算力 / 半导体",
    "title": "Back-to-back Amazon CPU scam delivers empty Ryzen 5 9600X boxes in 72 hours — $ 10,000-a-month business customer captures fraud on camera",
    "url": "https://www.tomshardware.com/desktops/pc-building/alleged-amazon-cpu-scam-hits-pc-shop-twice-in-three-days-ryzen-5-9600x-orders-arrive-with-empty-retail-boxes",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T10:00:00+00:00",
    "summary": "A PC shop that spends over $10,000 a month on Amazon hardware says two AMD Ryzen 5 9600X orders arrived with the CPUs missing."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/get-a-full-size-keychron-mechanical-keyboard-for-just-usd29-50-percent-off-this-104-key-wired-keeb-with-your-choice-of-keychron-super-brown-or-red-switches",
    "domain": "AI 算力 / 半导体",
    "title": "Get a full-size Keychron mechanical keyboard for just $29 — 50% off this 104-key wired keeb with your choice of Keychron Super Brown or Red switches",
    "url": "https://www.tomshardware.com/pc-components/get-a-full-size-keychron-mechanical-keyboard-for-just-usd29-50-percent-off-this-104-key-wired-keeb-with-your-choice-of-keychron-super-brown-or-red-switches",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T16:45:23+00:00",
    "summary": "Keychron’s C2 Pro full-size wired mechanical keyboard hits an all time low of $29.99 at W00t with code KEYCHRON ($24.99 if you’re new to Woot) - QMK programmability, pre-lubed switches, make this a gr"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/get-a-usd75-discount-on-your-next-corsair-upgrade-stack-your-cart-up-to-usd350-to-enjoy-big-savings",
    "domain": "AI 算力 / 半导体",
    "title": "Get a $75 discount on your next Corsair upgrade — stack your cart up to $350 to enjoy big savings",
    "url": "https://www.tomshardware.com/pc-components/get-a-usd75-discount-on-your-next-corsair-upgrade-stack-your-cart-up-to-usd350-to-enjoy-big-savings",
    "source": "Sponsored",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T15:27:27+00:00",
    "summary": "Corsair launches a back-to-school promotion offering $75 off qualifying purchases of $350 or more in the U.S."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/external-ssds/sandisk-expansion-cards-for-xbox-series-x-s-now-available-on-amazon-alternative-storage-solution-to-seagate-wd-arrives-on-the-market-five-years-after-the-launch-of-the-consoles",
    "domain": "AI 算力 / 半导体",
    "title": "SanDisk expansion cards for Xbox Series X|S now available on Amazon — alternative storage solution to Seagate, WD arrives on the market five years after the launch of the consoles",
    "url": "https://www.tomshardware.com/pc-components/external-ssds/sandisk-expansion-cards-for-xbox-series-x-s-now-available-on-amazon-alternative-storage-solution-to-seagate-wd-arrives-on-the-market-five-years-after-the-launch-of-the-consoles",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T15:25:29+00:00",
    "summary": "The SanDisk Optimus GX C50 expansion cards for the Xbox Series X|S are now available on Amazon starting at $249.99 for the 1TB variant. While gamers can use external drives to copy and backup games fr"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-fights-to-keep-chatgpt-lawsuit-away-from-a-state-jury",
    "domain": "AI 算力 / 半导体",
    "title": "Florida seeks court ruling to officially classify Sam Altman and ChatGPT as a 'public nuisance' — OpenAI fights to keep lawsuit away from a state jury",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-fights-to-keep-chatgpt-lawsuit-away-from-a-state-jury",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T15:11:18+00:00",
    "summary": "Florida's lawsuit against OpenAI and Sam Altman has now been sitting before U.S. District Judge Aileen Cannon in Fort Pierce for seven weeks."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/worlds-largest-open-library-calls-for-volunteers-to-scan-and-preserve-physical-books-as-ai-companies-buy-scan-and-destroy-them-annas-archive-says-time-is-running-out-as-knowledge-is-permanently-monopolized-on-private-servers",
    "domain": "AI 算力 / 半导体",
    "title": "World's largest open library calls for volunteers to scan and preserve physical books as AI companies buy, scan, and destroy them — Anna's Archive says ‘time is running out’ as ‘knowledge is permanent",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/worlds-largest-open-library-calls-for-volunteers-to-scan-and-preserve-physical-books-as-ai-companies-buy-scan-and-destroy-them-annas-archive-says-time-is-running-out-as-knowledge-is-permanently-monopolized-on-private-servers",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T14:33:36+00:00",
    "summary": "A volunteer for Anna's Archive is calling for volunteers to scan and upload books to the shadow library to help preserve human knowledge for the public. The move comes as more AI companies buy, scan, "
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/elegoo-centauri-2-combo-review",
    "domain": "AI 算力 / 半导体",
    "title": "Elegoo Centauri 2 Combo review: A budget-friendly printer made even more budget-friendly",
    "url": "https://www.tomshardware.com/3d-printing/elegoo-centauri-2-combo-review",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T14:05:33+00:00",
    "summary": "The Elegoo Centauri 2 Combo is an excellent four-color printer, but is it worth the savings without an enclosure?"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/toms-hardware-innovation-awards-2026-progress-amid-turmoil",
    "domain": "AI 算力 / 半导体",
    "title": "Tom’s Hardware Innovation Awards 2026: Progress amid turmoil",
    "url": "https://www.tomshardware.com/pc-components/toms-hardware-innovation-awards-2026-progress-amid-turmoil",
    "source": "The Editors of Tom&#039;s Hardware",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T14:02:24+00:00",
    "summary": "The continued industry advancements give us several new picks for our annual Tom's Hardware Innovation Awards: a set of products that set or expand the standard for others."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/lg-enters-chip-packaging-arena-with-laser-direct-imaging-machine-as-tsmcs-cowos-remains-constrained-maskless-machine-is-designed-to-pattern-fine-interconnects-trading-resolution-for-higher-throughput",
    "domain": "AI 算力 / 半导体",
    "title": "LG enters chip packaging arena with Laser Direct Imaging machine, as TSMC's CoWoS remains constrained — maskless machine is designed to pattern fine interconnects, trading resolution for higher throug",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/lg-enters-chip-packaging-arena-with-laser-direct-imaging-machine-as-tsmcs-cowos-remains-constrained-maskless-machine-is-designed-to-pattern-fine-interconnects-trading-resolution-for-higher-throughput",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T13:35:14+00:00",
    "summary": "LG rolls-out laser direct imaging lithography machine for chip packaging and high-density PCBs."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/unlock-toms-hardware-premiums-hot-chips-2026-coverage-for-free-sign-up-for-an-account-to-read-technical-breakdowns-from-the-show",
    "domain": "AI 算力 / 半导体",
    "title": "Unlock Tom's Hardware Premium's Hot Chips 2026 coverage for free — sign up for an account to read technical breakdowns from the show",
    "url": "https://www.tomshardware.com/tech-industry/unlock-toms-hardware-premiums-hot-chips-2026-coverage-for-free-sign-up-for-an-account-to-read-technical-breakdowns-from-the-show",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T13:00:00+00:00",
    "summary": "For a limited time, you’ll be able to read all of our latest reports from Hot Chips 2026 with a Tom’s Hardware account, no payment required."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/lg-display-introduces-new-oled-deposition-technique-that-uses-lithography-instead-of-metal-masks-flipp-photolithography-delivers-1-6x-brightness-and-2-4x-longer-lifespan",
    "domain": "AI 算力 / 半导体",
    "title": "LG Display introduces new OLED deposition technique that uses lithography instead of metal masks — \"FLiPP\" photolithography delivers 1.6x brightness and 2.4x longer lifespan",
    "url": "https://www.tomshardware.com/monitors/lg-display-introduces-new-oled-deposition-technique-that-uses-lithography-instead-of-metal-masks-flipp-photolithography-delivers-1-6x-brightness-and-2-4x-longer-lifespan",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T12:40:00+00:00",
    "summary": "OLED displays have long been manufacturer using a metal mask for deposition that wastes material, is expensive, and can sag under its own weight. LG Display's FLiPP solves this by using photolithograp"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/supermicro-fires-several-employees-following-investigation-into-usd2-5-billion-china-ai-chip-smuggling-claims-that-senior-management-had-no-knowledge-of-illicit-transactions",
    "domain": "AI 算力 / 半导体",
    "title": "Supermicro fires several employees following investigation into $2.5 billion China AI chip smuggling — claims that senior management had no knowledge of illicit transactions",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/supermicro-fires-several-employees-following-investigation-into-usd2-5-billion-china-ai-chip-smuggling-claims-that-senior-management-had-no-knowledge-of-illicit-transactions",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T12:20:54+00:00",
    "summary": "An independent investigation on Supermicro clears senior management from any wrong-doing and also says that its financial statements were still reliable, despite the alleged diversion of its restricte"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/applications/cpu-z-gets-biggest-update-since-2001-with-v3-100-health-checks-built-in-stress-testing-and-xoc-effective-clock-tracking",
    "domain": "AI 算力 / 半导体",
    "title": "CPU-Z gets biggest update since 2001 with V3 — 100+ health checks, built-in stress testing, and XOC effective clock tracking",
    "url": "https://www.tomshardware.com/software/applications/cpu-z-gets-biggest-update-since-2001-with-v3-100-health-checks-built-in-stress-testing-and-xoc-effective-clock-tracking",
    "source": "Aaron Klotz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T12:20:00+00:00",
    "summary": "CPU-Z V3 introduces an overhauled validation system with over 100 detection points, and a new advanced validation feature that will check PC health with a stress test."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/micron-commits-usd10-billion-to-new-us-based-research-labs-boise-hub-to-target-post-dram-and-nand-technologies-and-packaging",
    "domain": "AI 算力 / 半导体",
    "title": "Micron commits $10 billion to new US-based Research Labs — Boise hub to target post-DRAM and NAND technologies and packaging",
    "url": "https://www.tomshardware.com/tech-industry/micron-commits-usd10-billion-to-new-us-based-research-labs-boise-hub-to-target-post-dram-and-nand-technologies-and-packaging",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T12:00:00+00:00",
    "summary": "Micron's Research Labs to bring together the company's own research with research by customers, partners, universities, startups, and government organizations to develop pre-competitive IP for next-ge"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/china-approves-first-nvidia-h200-deliveries-to-bytedance-and-tencent-under-case-by-case-import-licenses",
    "domain": "AI 算力 / 半导体",
    "title": "H200 AI GPUs finally reach China under case-by-case import licenses, but it's already too late for Nvidia — homemade chips corner the China market as country seeks semiconductor independence",
    "url": "https://www.tomshardware.com/pc-components/gpus/china-approves-first-nvidia-h200-deliveries-to-bytedance-and-tencent-under-case-by-case-import-licenses",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T11:40:00+00:00",
    "summary": "Most of each company's U.S.-licensed allowance, understood to be up to 100,000 units apiece, must stay outside the mainland."
  },
  {
    "id": "hn:49322519",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia discloses $21B stake in SpaceX at end of second quarter",
    "url": "https://www.cnbc.com/2026/08/14/nvidia-discloses-21-billion-stake-in-spacex-at-end-of-second-quarter.html",
    "source": "johnbarron",
    "platform": "hackernews",
    "points": 47,
    "published_at": "2026-08-16T18:40:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:49342314",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia discloses $21B stake in SpaceX",
    "url": "https://arstechnica.com/information-technology/2026/08/nvidia-discloses-21b-stake-in-spacex/",
    "source": "joozio",
    "platform": "hackernews",
    "points": 31,
    "published_at": "2026-08-18T07:02:04+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/synopsys-updates-cxl-ip-portfolio-for-ai-era-infrastructure/",
    "domain": "AI 算力 / 半导体",
    "title": "Synopsys Updates CXL IP Portfolio for AI-Era Infrastructure",
    "url": "https://www.eetimes.com/synopsys-updates-cxl-ip-portfolio-for-ai-era-infrastructure/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T14:07:45+00:00",
    "summary": "Synopsys’s CXL 4.0 IP aims to help designers build faster, more flexible and secure disaggregated computing architectures as AI systems demand more memory capacity and bandwidth. The post Synopsys Upd"
  },
  {
    "id": "rss:https://www.eetimes.com/andes-condor-closure-came-amid-broader-cost-cutting-effort/",
    "domain": "AI 算力 / 半导体",
    "title": "Andes Condor Closure Came Amid Broader Cost-Cutting Effort",
    "url": "https://www.eetimes.com/andes-condor-closure-came-amid-broader-cost-cutting-effort/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T22:00:00+00:00",
    "summary": "Andes Technology’s decision to close Condor was part of a broader 10-20% operational cost-cutting exercise, with Condor probably considered too expensive a bet. The post Andes Condor Closure Came Amid"
  },
  {
    "id": "rss:https://www.eetimes.com/ibm-makes-quantum-cryogenics-modular-but-scaling-problems-remain/",
    "domain": "AI 算力 / 半导体",
    "title": "IBM Makes Quantum Cryogenics Modular, but Scaling Problems Remain",
    "url": "https://www.eetimes.com/ibm-makes-quantum-cryogenics-modular-but-scaling-problems-remain/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T13:55:51+00:00",
    "summary": "IBM’s new cryogenic architecture tackles one obstacle to fault-tolerant quantum computing, while exposing wiring, control, interconnect, and reliability challenges. The post IBM Makes Quantum Cryogeni"
  },
  {
    "id": "rss:https://www.eetimes.com/running-local-llms-on-the-arduino-uno-q-board-a-practical-guide/",
    "domain": "AI 算力 / 半导体",
    "title": "Running Local LLMs on the Arduino® UNO™ Q Board: a Practical Guide",
    "url": "https://www.eetimes.com/running-local-llms-on-the-arduino-uno-q-board-a-practical-guide/",
    "source": "Arduino Team",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T13:00:00+00:00",
    "summary": "Learn how to run local LLMs on Arduino UNO Q — from model selection and quantization to memory constraints and real-world edge AI use cases. The post Running Local LLMs on the Arduino® UNO™ Q Board: a"
  },
  {
    "id": "rss:https://www.eetimes.com/when-interoperability-becomes-infrastructure/",
    "domain": "AI 算力 / 半导体",
    "title": "When Interoperability Becomes Infrastructure",
    "url": "https://www.eetimes.com/when-interoperability-becomes-infrastructure/",
    "source": "Peter Hunt",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T07:43:30+00:00",
    "summary": "As Matter matures, manufacturers face a new challenge: maintaining visibility into connected products after deployment. The post When Interoperability Becomes Infrastructure appeared first on EE Times"
  },
  {
    "id": "hn:49325115",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC Uses Old Fabs to Make New Chips [video]",
    "url": "https://www.youtube.com/watch?v=cDxVYQrxeiQ",
    "source": "eig",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-08-17T00:07:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:49282762",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia doubles RTX PRO 6000 Blackwell's MSRP to a staggering $16,000",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-doubles-rtx-pro-6000-blackwells-msrp-to-a-staggering-usd16-000-96gb-card-started-pre-orders-below-usd8-000-last-year",
    "source": "jacquesm",
    "platform": "hackernews",
    "points": 37,
    "published_at": "2026-08-13T07:28:54+00:00",
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
    "id": "rss:https://www.eetimes.com/marvell-targets-ai-bottlenecks-with-memory-disaggregation-portfolio/",
    "domain": "AI 算力 / 半导体",
    "title": "Marvell Targets AI Bottlenecks with Memory-Disaggregation Portfolio",
    "url": "https://www.eetimes.com/marvell-targets-ai-bottlenecks-with-memory-disaggregation-portfolio/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T14:39:27+00:00",
    "summary": "Marvell attacks AI’s memory choke point with SSD, CXL, and photonic fabrics to push data nearer compute. The post Marvell Targets AI Bottlenecks with Memory-Disaggregation Portfolio appeared first on "
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
    "points": 449,
    "published_at": "2026-08-08T09:18:50+00:00",
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
    "id": "rss:https://www.theverge.com/entertainment/983322/musical-spirograph-generative-composition",
    "domain": "大厂 AI 动态",
    "title": "Doodle generative compositions in your browser with Musical Spirograph",
    "url": "https://www.theverge.com/entertainment/983322/musical-spirograph-generative-composition",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T17:00:00+00:00",
    "summary": "I remember having a Spirograph as a kid and being obsessed with it. Its geometric patterns are hypnotic and gorgeous. I also love generative music composition. So bringing those two things together in"
  },
  {
    "id": "rss:https://www.theverge.com/report/980452/w-kamau-bell-whos-with-me-comedy-interview",
    "domain": "大厂 AI 动态",
    "title": "W. Kamau Bell has the most practical ‘most indispensable tool’",
    "url": "https://www.theverge.com/report/980452/w-kamau-bell-whos-with-me-comedy-interview",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T15:00:00+00:00",
    "summary": "W. Kamau Bell is one of those people who has always just seemed to be there. From Totally Biased, to Politically Re-Active, United Shades of America, and We Need to Talk About Cosby, his blend of come"
  },
  {
    "id": "rss:https://www.theverge.com/tech/983598/amazon-price-increase-echo-kindle-fire-tv",
    "domain": "大厂 AI 动态",
    "title": "Amazon just hiked the prices for Echo, Fire TV, and Kindle products by up to 60 percent",
    "url": "https://www.theverge.com/tech/983598/amazon-price-increase-echo-kindle-fire-tv",
    "source": "Jennifer Pattison Tuohy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T13:41:01+00:00",
    "summary": "Citing \"significant increases in memory and storage component costs,\" Amazon has raised prices on Echos, Kindles, Fire TVs, and Eeros by up to 60 percent, as first reported by Fortune. The cheapest pr"
  },
  {
    "id": "rss:https://www.theverge.com/tech/983554/hp-omnibook-3-16-snapdragon-laptop-review",
    "domain": "大厂 AI 动态",
    "title": "An okay laptop with 16GB of RAM is better than a nice laptop with 8GB, and this $520 HP OmniBook proves it",
    "url": "https://www.theverge.com/tech/983554/hp-omnibook-3-16-snapdragon-laptop-review",
    "source": "Antonio G. Di Benedetto",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T13:00:00+00:00",
    "summary": "Laptop prices are out of whack. $500 used to get you a tolerable laptop, and $900 got you a really good one. They often had similar CPU, RAM, and storage options because that stuff was comparatively c"
  },
  {
    "id": "rss:https://www.theverge.com/tech/983375/fairphone-6-plus-framework-12-laptop-mutiny-mortal-shell-2",
    "domain": "大厂 AI 动态",
    "title": "Two great new repairable gadgets",
    "url": "https://www.theverge.com/tech/983375/fairphone-6-plus-framework-12-laptop-mutiny-mortal-shell-2",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T12:00:00+00:00",
    "summary": "Hi, friends! Welcome to Installer No. 141, your guide to the best and Verge-iest stuff in the world. (If you're new here, welcome, I'm newish here too, and also you can read all the old editions at th"
  },
  {
    "id": "rss:https://www.theverge.com/tech/983500/hoverair-versa-halted-us-fcc-drone-ban-indiegogo",
    "domain": "大厂 AI 动态",
    "title": "HoverAir’s transforming modular drone has already been halted in the US",
    "url": "https://www.theverge.com/tech/983500/hoverair-versa-halted-us-fcc-drone-ban-indiegogo",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T22:14:11+00:00",
    "summary": "I am so sorry, fellow US gadget fans: the FCC's drone ban appears to have struck again. The HoverAir Versa - a baby steadycam with snap-on propeller wings that transform it into a drone - has already "
  },
  {
    "id": "rss:https://www.theverge.com/tech/983531/tiktok-settle-doj-lawsuit-coppa",
    "domain": "大厂 AI 动态",
    "title": "TikTok will pay $400 million to settle DOJ child privacy lawsuit",
    "url": "https://www.theverge.com/tech/983531/tiktok-settle-doj-lawsuit-coppa",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T22:13:34+00:00",
    "summary": "The US Department of Justice announced on Friday that TikTok will pay $400 million to settle a lawsuit filed in 2024 over allegedly violating the Children's Online Privacy Protection Act (COPPA). In t"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/983502/linkedin-ai-slop-button-one-million-people-message",
    "domain": "大厂 AI 动态",
    "title": "Over 1 million people have clicked LinkedIn’s AI slop button",
    "url": "https://www.theverge.com/ai-artificial-intelligence/983502/linkedin-ai-slop-button-one-million-people-message",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T21:25:50+00:00",
    "summary": "LinkedIn actually announced a \"Seems like AI slop\" button on July 30th, and the company says that a lot of people have already used it. According to a Thursday post from chief product officer Hari Sri"
  },
  {
    "id": "rss:https://www.theverge.com/tech/983451/apple-layoffs-vision-pro-siri",
    "domain": "大厂 AI 动态",
    "title": "Apple is laying off staffers working on the Vision Pro and Siri",
    "url": "https://www.theverge.com/tech/983451/apple-layoffs-vision-pro-siri",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T19:44:55+00:00",
    "summary": "Apple is laying off staff on the Siri and the Vision Pro teams, according to Bloomberg. The cuts include \"largely shutting down\" a Vision Pro gaming team and \"reducing the size\" of the team that makes"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/982513/best-buy-gift-card-in-store-deal",
    "domain": "大厂 AI 动态",
    "title": "$100 Best Buy gift cards will be $60 at stores Saturday",
    "url": "https://www.theverge.com/gadgets/982513/best-buy-gift-card-in-store-deal",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T18:00:00+00:00",
    "summary": "The best gift card deal we’ve spotted this year is happening Saturday, August 22nd, at Best Buy stores for one day only. In celebration of the retailer’s 60th anniversary, you can purchase a $100 Best"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/22/two-years-after-launch-walmarts-flipkart-is-closing-in-on-indias-quick-commerce-leaders/",
    "domain": "大厂 AI 动态",
    "title": "Two years after launch, Walmart’s Flipkart is closing in on India’s quick-commerce leaders",
    "url": "https://techcrunch.com/2026/08/22/two-years-after-launch-walmarts-flipkart-is-closing-in-on-indias-quick-commerce-leaders/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T03:00:00+00:00",
    "summary": "Flipkart's quick-commerce venture is delivering 1.1 million to 1.2 million orders a day, nearly triple its November volume."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/22/harvards-699-startup-bootcamp-offers-ai-avatars-of-its-instructors/",
    "domain": "大厂 AI 动态",
    "title": "Harvard’s $699 startup bootcamp offers AI avatars of its instructors",
    "url": "https://techcrunch.com/2026/08/22/harvards-699-startup-bootcamp-offers-ai-avatars-of-its-instructors/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T21:46:56+00:00",
    "summary": "In the HBS Foundry program, AI avatars provide feedback during practice pitches and board meetings."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/22/will-the-dojs-investigation-into-a16z-spook-other-vcs/",
    "domain": "大厂 AI 动态",
    "title": "Will the DOJ’s investigation into a16z spook other VCs?",
    "url": "https://techcrunch.com/2026/08/22/will-the-dojs-investigation-into-a16z-spook-other-vcs/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T20:24:20+00:00",
    "summary": "On the latest episode of Equity, we wonder why the DOJ is investigating startup board seats."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/22/inherent-founded-by-deepmind-alumni-says-its-ai-teammate-just-outperformed-anthropic-and-openai-at-replicating-research/",
    "domain": "大厂 AI 动态",
    "title": "Inherent, founded by DeepMind alumni, says its AI ‘teammate’ just outperformed Anthropic and OpenAI at replicating research",
    "url": "https://techcrunch.com/2026/08/22/inherent-founded-by-deepmind-alumni-says-its-ai-teammate-just-outperformed-anthropic-and-openai-at-replicating-research/",
    "source": "Anna Heim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T19:00:00+00:00",
    "summary": "Built by DeepMind alumni, British AI lab Inherent released Faraday, an AI agent whose ability to replicate scientific papers could be a stepping stone for innovation."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/22/openai-says-california-should-strengthen-its-ai-safety-bill/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI says California should strengthen its AI safety bill",
    "url": "https://techcrunch.com/2026/08/22/openai-says-california-should-strengthen-its-ai-safety-bill/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T16:30:34+00:00",
    "summary": "OpenAI is calling for California to strengthen SB 53, an AI safety bill that the company previously opposed."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/22/frontier-ai-labs-still-wont-say-how-theyd-contain-a-rogue-model/",
    "domain": "大厂 AI 动态",
    "title": "Frontier AI labs still won’t say how they’d contain a rogue model",
    "url": "https://techcrunch.com/2026/08/22/frontier-ai-labs-still-wont-say-how-theyd-contain-a-rogue-model/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T16:00:00+00:00",
    "summary": "A new study finds leading AI labs have few publicly documented plans for containing rogue models, raising questions about preparedness as AI systems increasingly demonstrate unexpected and potentially"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/22/us-battery-startups-have-found-a-lifeline-in-defense/",
    "domain": "大厂 AI 动态",
    "title": "US battery startups have found a lifeline in defense",
    "url": "https://techcrunch.com/2026/08/22/us-battery-startups-have-found-a-lifeline-in-defense/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T15:20:00+00:00",
    "summary": "U.S. battery startups pulled in $500 million in grants from the Department of Energy, throwing a lifeline to an industry that was on the ropes after EV incentives were slashed."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/22/pixel-11-pro-xl-review-snappier-cameras-cant-hide-an-iterative-upgrade/",
    "domain": "大厂 AI 动态",
    "title": "Pixel 11 Pro XL review: Snappier cameras can’t hide an iterative upgrade",
    "url": "https://techcrunch.com/2026/08/22/pixel-11-pro-xl-review-snappier-cameras-cant-hide-an-iterative-upgrade/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T14:00:00+00:00",
    "summary": "Google’s Pixel 11 Pro XL brings snappier cameras and genuinely useful AI features like Rambler, but its iterative upgrades may not be enough to tempt recent Pixel owners."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/21/michael-polansky-is-training-an-ai-model-on-skin-thats-still-alive/",
    "domain": "大厂 AI 动态",
    "title": "Michael Polansky is training an AI model on skin that’s still alive",
    "url": "https://techcrunch.com/2026/08/21/michael-polansky-is-training-an-ai-model-on-skin-thats-still-alive/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T01:31:04+00:00",
    "summary": "Michael Polansky — better known publicly as Lady Gaga's partner and a former top deputy to Sean Parker — has quietly spent years building an AI-driven startup that keeps living human skin tissue alive"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/21/japanese-space-tech-startup-letara-expands-beyond-satellite-thrusters-with-16m/",
    "domain": "大厂 AI 动态",
    "title": "Japanese space tech startup Letara expands beyond satellite thrusters with $16M",
    "url": "https://techcrunch.com/2026/08/21/japanese-space-tech-startup-letara-expands-beyond-satellite-thrusters-with-16m/",
    "source": "Kate Park",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T01:03:06+00:00",
    "summary": "Japanese space startup Letara is betting its hybrid rocket technology can move beyond small satellite thrusters into a broader market for space, defense and security, after raising ¥2.6 billion ($16 m"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/21/anthropics-opus-4-6-is-a-smut-machine/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic’s Opus 4.6 is a smut-machine",
    "url": "https://techcrunch.com/2026/08/21/anthropics-opus-4-6-is-a-smut-machine/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T23:07:25+00:00",
    "summary": "Anthropic forbids its Claude models from generating sexually explicit content. But a series of tests conducted by TechCrunch found that it didn't take much to get past the restriction."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/21/nvidia-partners-with-data-center-developer-cloverleaf/",
    "domain": "大厂 AI 动态",
    "title": "Nvidia partners with data center developer Cloverleaf",
    "url": "https://techcrunch.com/2026/08/21/nvidia-partners-with-data-center-developer-cloverleaf/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T22:37:38+00:00",
    "summary": "Nvidia continues to pour money into data center development — just as AI data centers bring lots of money into Nvidia."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/21/how-ai-accounting-startup-rillet-raised-100m-and-became-a-unicorn-in-48-hours/",
    "domain": "大厂 AI 动态",
    "title": "How AI accounting startup Rillet raised $100M and became a unicorn in 48 hours",
    "url": "https://techcrunch.com/2026/08/21/how-ai-accounting-startup-rillet-raised-100m-and-became-a-unicorn-in-48-hours/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T22:10:01+00:00",
    "summary": "Rillet CEO Nicolas Kopp shared growth numbers at a board meeting and set off a fundraising frenzy from Iconiq, Sequoia and others. Without even trying."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/21/apple-is-reportedly-cutting-hundreds-of-jobs-from-siri-vision-pro-teams/",
    "domain": "大厂 AI 动态",
    "title": "Apple is reportedly cutting hundreds of jobs from Siri, Vision Pro teams",
    "url": "https://techcrunch.com/2026/08/21/apple-is-reportedly-cutting-hundreds-of-jobs-from-siri-vision-pro-teams/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T20:58:07+00:00",
    "summary": "Apple has admitted that some roles are being impacted as it shifts its focus away from certain initiatives."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/21/tiktok-reaches-400m-settlement-over-childrens-privacy-lawsuit/",
    "domain": "大厂 AI 动态",
    "title": "TikTok reaches $400M settlement over children’s privacy lawsuit",
    "url": "https://techcrunch.com/2026/08/21/tiktok-reaches-400m-settlement-over-childrens-privacy-lawsuit/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T20:25:21+00:00",
    "summary": "Two years after the U.S. Department of Justice alleged that TikTok violated the Children’s Online Privacy Protection Act, it has reached a $400 million settlement."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/21/the-225-pebble-time-2-is-a-refreshingly-fun-smartwatch/",
    "domain": "大厂 AI 动态",
    "title": "The $225 Pebble Time 2 is a refreshingly fun smartwatch",
    "url": "https://techcrunch.com/2026/08/21/the-225-pebble-time-2-is-a-refreshingly-fun-smartwatch/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T19:57:46+00:00",
    "summary": "The $225 Pebble Time 2 pairs quirky watch faces and apps with physical buttons, an e-paper display, weeks of battery life, and a playful hacker spirit."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/21/last-chance-save-up-to-300-on-your-techcrunch-disrupt-2026-ticket-today/",
    "domain": "大厂 AI 动态",
    "title": "Last chance: Save up to $300 on your TechCrunch Disrupt 2026 ticket today",
    "url": "https://techcrunch.com/2026/08/21/last-chance-save-up-to-300-on-your-techcrunch-disrupt-2026-ticket-today/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T19:16:15+00:00",
    "summary": "If you’ve been circling around Disrupt, then now’s the best time to lock in your pass and start getting ready to join the rest of the startup community gathering in San Francisco from October 13-15 at"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/21/teslas-solar-roof-is-dead-heres-what-went-wrong/",
    "domain": "大厂 AI 动态",
    "title": "Tesla’s solar roof is dead — here’s what went wrong",
    "url": "https://techcrunch.com/2026/08/21/teslas-solar-roof-is-dead-heres-what-went-wrong/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T18:09:53+00:00",
    "summary": "Tesla's solar roof was an experiment that never really caught on for the company. But does that mean the concept of roof-integrated solar is dead?"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/21/waymo-hands-over-documents-in-nhtsas-child-collision-probe/",
    "domain": "大厂 AI 动态",
    "title": "Waymo hands over documents in NHTSA’s child collision probe",
    "url": "https://techcrunch.com/2026/08/21/waymo-hands-over-documents-in-nhtsas-child-collision-probe/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T17:49:58+00:00",
    "summary": "The responses to NHTSA's questions so far are redacted entirely, citing \"confidential business information.\""
  },
  {
    "id": "rss:https://stratechery.com/2026/app-snore/",
    "domain": "大厂 AI 动态",
    "title": "2026.34: App Snore",
    "url": "https://stratechery.com/2026/app-snore/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T17:00:00+00:00",
    "summary": "The best Stratechery content from the week of August 17, 2026, including Apple making compromises in the EU, Truth (Social) and reconciliation, and August fun with the Clippers and Lakers."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/08/memories-stick-around-even-after-half-the-synapses-are-gone/",
    "domain": "大厂 AI 动态",
    "title": "Putting mice into hibernation causes a major loss of synapses",
    "url": "https://arstechnica.com/science/2026/08/memories-stick-around-even-after-half-the-synapses-are-gone/",
    "source": "Jacek Krywko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T11:22:32+00:00",
    "summary": "Hibernation cuts down on synapses, but mice seem to retain memories anyway."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/08/dismantling-the-roadless-rule-threatens-to-disrupt-wildlife-and-water-in-us/",
    "domain": "大厂 AI 动态",
    "title": "Dismantling the Roadless Rule threatens to disrupt wildlife and water in US",
    "url": "https://arstechnica.com/science/2026/08/dismantling-the-roadless-rule-threatens-to-disrupt-wildlife-and-water-in-us/",
    "source": "Mariah Meek and Travis Belote, The Conversation",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T11:08:53+00:00",
    "summary": "Lands free of roads are under threat from the Trump administration’s proposed rollback."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/08/trump-admin-calls-for-more-spaceports-to-handle-surge-in-launches/",
    "domain": "大厂 AI 动态",
    "title": "Trump's space transportation policy calls for new spaceport on federal land",
    "url": "https://arstechnica.com/space/2026/08/trump-admin-calls-for-more-spaceports-to-handle-surge-in-launches/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T23:32:17+00:00",
    "summary": "\"We probably need another site that's capable of heavy and super heavy launch capability.\""
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/08/researchers-use-thunderquakes-to-study-structure-of-earths-surface/",
    "domain": "大厂 AI 动态",
    "title": "Thunder + fiber-optic cabling used for seismic imaging",
    "url": "https://arstechnica.com/science/2026/08/researchers-use-thunderquakes-to-study-structure-of-earths-surface/",
    "source": "John Timmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T20:26:46+00:00",
    "summary": "Thunderstorms make seismic waves that can be used to find sub-surface features."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/08/class-action-accuses-brokers-of-hiding-zillow-listings-driving-up-nyc-rents/",
    "domain": "大厂 AI 动态",
    "title": "Hidden Zillow listings created fake supply shock, raising NYC rents, lawsuit says",
    "url": "https://arstechnica.com/tech-policy/2026/08/class-action-accuses-brokers-of-hiding-zillow-listings-driving-up-nyc-rents/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T20:10:50+00:00",
    "summary": "Renters say hidden Zillow listings make it harder to afford living in New York City."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/08/motorolas-grapheneos-phones-will-launch-in-2027-priced-higher-than-pixels/",
    "domain": "大厂 AI 动态",
    "title": "Motorola's GrapheneOS phones will launch in 2027 priced higher than Pixels",
    "url": "https://arstechnica.com/gadgets/2026/08/motorolas-grapheneos-phones-will-launch-in-2027-priced-higher-than-pixels/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T19:32:29+00:00",
    "summary": "The private Android-based OS will expand beyond Pixels next year."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/08/lawsuit-demands-logitech-hand-tariff-refunds-over-to-customers/",
    "domain": "大厂 AI 动态",
    "title": "Lawsuit demands Logitech hand tariff refunds over to customers",
    "url": "https://arstechnica.com/tech-policy/2026/08/lawsuit-demands-logitech-hand-tariff-refunds-over-to-customers/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T19:04:41+00:00",
    "summary": "Logitech increased prices by up to 25 percent last year."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/08/chinese-regulators-tell-tesla-to-fix-nearly-3-million-cars/",
    "domain": "大厂 AI 动态",
    "title": "Chinese regulators tell Tesla to fix nearly 3 million cars",
    "url": "https://arstechnica.com/cars/2026/08/chinese-regulators-tell-tesla-to-fix-nearly-3-million-cars/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T18:07:15+00:00",
    "summary": "Chinese safety regulators have cracked down on doors that don't open in a crash."
  },
  {
    "id": "hn:49401229",
    "domain": "股票",
    "title": "Anthropic IPO filing will show AI backlash as a risk factor, sources say",
    "url": "https://www.cnbc.com/2026/08/21/-anthropic-ipo-filing-will-show-ai-backlash-as-risk-sources-say.html",
    "source": "newsomix9xl",
    "platform": "hackernews",
    "points": 35,
    "published_at": "2026-08-22T16:23:09+00:00",
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
    "id": "hn:49397022",
    "domain": "股票",
    "title": "Ask HN: What is the evidence for a stock market bubble in AI?",
    "url": "https://news.ycombinator.com/item?id=49397022",
    "source": "roschdal",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-08-22T06:07:48+00:00",
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
    "id": "wscn:3780074",
    "domain": "股票",
    "title": "吴恩达：构建和部署AI应用必须啃下这六块硬骨头",
    "url": "https://wallstreetcn.com/articles/3780074",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T03:52:02+00:00",
    "summary": "吴恩达深度拆解AI工程师核心能力：从LLM底层原理、数据喂养、智能体搭建，到评估驱动开发、生产环境运维，再到机器学习基础，六块硬骨头环环相扣。其中最关键的一条——能跑通严格评估闭环，才是优秀与普通工程师的真正分水岭。"
  },
  {
    "id": "wscn:3780070",
    "domain": "股票",
    "title": "7月再现！高盛：存储“股价业绩差”最具吸引力，金融和硬资产成为新热点",
    "url": "https://wallstreetcn.com/articles/3780070",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T03:24:18+00:00",
    "summary": "高盛认为，AI交易的“躺赢”时代已经结束，当前的超额收益仅存于股价过度偏离盈利时的精准低吸，存储和数据中心最具战术吸引力。而市场正加速摆脱AI单一叙事，呈现出多点开花的特征：动量因子转向软件、欧日银行迎结构性机遇、黄金矿商与铜矿股存在估值及盈利修复空间，同时法国政治风险溢价被低估。"
  },
  {
    "id": "wscn:3780072",
    "domain": "股票",
    "title": "3天暴涨23%！什么推动加密市场势头反转？",
    "url": "https://wallstreetcn.com/premium/articles/3780072?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T02:49:29+00:00",
    "summary": "本周加密市场暴涨由空头挤压、机构买盘及宏观利好驱动，但趋势延续需看现货买盘，后续关注政策与美联储。"
  },
  {
    "id": "wscn:3780071",
    "domain": "股票",
    "title": "《财经》实地走访追觅：回款争议与产线调整",
    "url": "https://wallstreetcn.com/articles/3780071",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T02:41:21+00:00",
    "summary": "持续两个多月的业务调整，还未能让追觅稳住。追觅已经开始陆续支付部分供应商的回款，但产线收缩引发的连锁反应仍在扩散。据多位供应商反馈，追觅拖欠从今年二季度开始集中出现，金额从几万元到上千万元不等，涉及的业务包括被收缩的智能大家电、智能戒指、手机等，以及包括扫地机、洗地机在内的智能清洁板块。"
  },
  {
    "id": "wscn:3780069",
    "domain": "股票",
    "title": "美财政部加码长债回购，黄金、比特币为什么会涨？",
    "url": "https://wallstreetcn.com/articles/3780069",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T02:35:04+00:00",
    "summary": "美国财政部加码长债回购，分析人士指出，此举重燃\"美元贬值交易\"逻辑，投资者转向硬资产避险。受此影响，比特币当周大涨22.6%，黄金突破200日均线，黄金ETF创今年最大单日资金流入。"
  },
  {
    "id": "wscn:3779970",
    "domain": "股票",
    "title": "下周重磅日程：全市场最关注的经济数据、央行大会和财报一起来了",
    "url": "https://wallstreetcn.com/articles/3779970",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T02:14:19+00:00",
    "summary": "杰克逊霍尔央行年会召开，沃什将发表演讲；美财长贝森特预计将公布新一轮财政整顿计划及伊朗制裁措施。美国7月PCE数据也将出炉。此外，英伟达二季报来袭，验证AI资本开支周期；国内方面，美团、拼多多、哔哩哔哩、长鑫科技、德明利、源杰科技等放榜，A港股迎来中报收官高峰。"
  },
  {
    "id": "wscn:3780061",
    "domain": "股票",
    "title": "“我们遭到了袭击！”加拿大强力反制：对美等额关税9月8日生效，午夜紧急召回谈判团队",
    "url": "https://wallstreetcn.com/articles/3780061",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T01:58:55+00:00",
    "summary": "加美贸易谈判于8月22日宣告破裂，加拿大总理卡尼在全国电视讲话中强调，美方谈判末期提出损害加拿大主权及核心产业的苛刻条款，致使协议功亏一篑。他表示加拿大绝不以主权换协议，并将推出更多应对措施。卡尼随即宣布等额报复性关税将于9月8日生效，涵盖乳制品、钢铁、家电等多个领域。"
  },
  {
    "id": "wscn:3780067",
    "domain": "股票",
    "title": "特朗普的“大麻烦”：40万亿美元债务，6.5%按揭利率与5美元柴油价格",
    "url": "https://wallstreetcn.com/articles/3780067",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T01:39:23+00:00",
    "summary": "特朗普执政不足两年，伊朗战争与减税政策已令美国经济承压：国债突破40万亿美元，长期国债收益率升至19年高位；汽油价格上涨约40%。财政赤字削减目标难以实现，GDP增速远低于官方预期。市场人士警告，白宫的干预言辞透出焦虑，或进一步恶化市场情绪。"
  },
  {
    "id": "wscn:3780068",
    "domain": "股票",
    "title": "债券危机没有结束",
    "url": "https://wallstreetcn.com/articles/3780068",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T01:31:16+00:00",
    "summary": "东吴证券陈李认为，美债不会卖不出去。美债不缺买家，缺的是愿意低价接盘的买家。财政赤字今年累计近1.8万亿美元，回购只是零头，买不掉赤字。长端利率大概率继续磨顶——债券危机没有结束，只是换了一种更安静的方式继续存在。"
  },
  {
    "id": "wscn:3780066",
    "domain": "股票",
    "title": "因存储芯片成本飙升，英伟达高端服务器被曝明年将涨价15%",
    "url": "https://wallstreetcn.com/articles/3780066",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T00:49:31+00:00",
    "summary": "媒体援引知情人士报道称，此次涨价将从明年初出货的系统开始生效，影响范围包括搭载旗舰级Vera Rubin和Grace Blackwell芯片的系统。给微软、谷歌和甲骨文等大厂代工服务器的工厂，已经发出了涨价通知。具体涨幅将取决于英伟达芯片的代际和存储配置。"
  },
  {
    "id": "wscn:3780065",
    "domain": "股票",
    "title": "瑞银调研：过去一周，霍尔木兹海峡日流量超600万桶",
    "url": "https://wallstreetcn.com/articles/3780065",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T12:55:29+00:00",
    "summary": "瑞银报告指出，霍尔木兹海峡石油过境量仍略高于600万桶/日。尽管可见油轮流量处于低位，但“暗流”运输已升至500万—600万桶/日，部分弥补表面航运缺口。与此同时，海湾其他产油国原油装载量回升至1020万桶/日，部分对冲伊朗出口停滞。随着美伊紧张局势转向经济制裁，油市焦点转向伊朗出口收缩幅度及替代供应能力。"
  },
  {
    "id": "wscn:3780064",
    "domain": "股票",
    "title": "从濒临出局到市值暴涨440亿美元：Moderna的癌症疫苗十年豪赌",
    "url": "https://wallstreetcn.com/articles/3780064",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T12:49:53+00:00",
    "summary": "某种意义上，如果没有新冠疫苗带来的巨额现金流，Moderna或许很难将这场高风险的癌症押注坚持到今天。"
  },
  {
    "id": "wscn:3780062",
    "domain": "股票",
    "title": "贝森特\"工具箱\"难敌油价与消费疲软双重夹击，高盛：“市场弥漫着滞胀的味道”",
    "url": "https://wallstreetcn.com/articles/3780062",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T10:50:50+00:00",
    "summary": "高盛认为，贝森特试图通过扩大美债回购、推进财政整合稳定长端债市，但长债收益率短暂下行后迅速反弹，政策工具仍难化解财政与供需压力。与此同时，滞胀信号强化：油价单周涨逾7%，10年期盈亏平衡通胀率两周升近10个基点；消费却持续降温，沃尔玛同店销售增速降至六年低点2.6%，“滞胀篮子”本周涨6.7%。"
  },
  {
    "id": "wscn:3780055",
    "domain": "股票",
    "title": "硅谷调研后，高盛的总结：Agent进入执行时代，AI竞争转向工作流，世界模型崛起",
    "url": "https://wallstreetcn.com/articles/3780055",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T09:54:17+00:00",
    "summary": "高盛报告指出，AI正从“回答”迈向“执行”，产业竞争转向工作流掌控。Agent落地关键在可控性与责任划分，具备清晰边界与可验证结果的工作流将优先自动化。模型市场走向分工：前沿模型主导高价值任务，开源模型承担规模化推理。同时，世界模型驱动AI进入物理世界，有望催生算力新增长曲线，未来5年需求或增长24倍。"
  },
  {
    "id": "wscn:3780063",
    "domain": "股票",
    "title": "恒生科技指数拟扩至50只，宁德时代等20家公司有望入选",
    "url": "https://wallstreetcn.com/articles/3780063",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T09:51:14+00:00",
    "summary": "恒生科技指数拟迎大扩容，成分股将从30增至50只并首设“收入增长”门槛。新规虽注入成长新血，但头部“二八分化”格局难撼。宁德时代、优必选等20家新贵有望火线入围。"
  },
  {
    "id": "wscn:3779793",
    "domain": "股票",
    "title": "晶圆代工Q2业绩复盘：华虹高弹性、中芯规模释放，国产替代高景气延续",
    "url": "https://wallstreetcn.com/premium/articles/3779793?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T09:45:46+00:00",
    "summary": "AI外溢订单+成熟制程涨价双轮驱动，国产代工从底部修复进入持续景气阶段。"
  },
  {
    "id": "wscn:3780060",
    "domain": "股票",
    "title": "特斯拉官宣！9月3日在奥斯汀举行Cybercab发布会",
    "url": "https://wallstreetcn.com/articles/3780060",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T07:10:59+00:00",
    "summary": "特斯拉将于当地时间9月3日在奥斯汀发布无方向盘、无踏板的无人驾驶车型Cybercab。此前报道称该车已完成道路测试和员工试乘，计划先向员工、后对公众开放。目前奥斯汀Robotaxi以186辆改装Model Y为主，Cybercab将逐步加入，但年内量产有限，商业化许可尚待明确。"
  },
  {
    "id": "wscn:3780057",
    "domain": "股票",
    "title": "宁德时代盯上储能“小单”",
    "url": "https://wallstreetcn.com/articles/3780057",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T06:02:39+00:00",
    "summary": "大储龙头开始争夺中小集成商。"
  },
  {
    "id": "wscn:3780059",
    "domain": "股票",
    "title": "东财发布半年报：非货基金规模首破万亿，中期不分红",
    "url": "https://wallstreetcn.com/articles/3780059",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T05:48:01+00:00",
    "summary": "证券收入也大幅提升"
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
    "id": "hn:49322233",
    "domain": "股票",
    "title": "AI is not just one bubble, strategist says – but a 'rolling sequence of bubbles'",
    "url": "https://fortune.com/2026/08/16/ai-bubble-sequence-saas-software-stocks-silver-prices-chipmakers/",
    "source": "pessimizer",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-08-16T18:05:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:49338121",
    "domain": "股票",
    "title": "US tech stock correction likely, warn ECB economists",
    "url": "https://www.ft.com/content/cb4b22ab-4183-4d19-be60-6d2fab86d86d",
    "source": "aanet",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-08-17T21:46:22+00:00",
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
    "id": "hn:49305685",
    "domain": "股票",
    "title": "Backtesting Congress members stock trades by the disclosure date",
    "url": "https://investingpaths.com/tools/congress",
    "source": "ProdRatSuperior",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-08-14T23:08:56+00:00",
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
    "id": "hn:49355142",
    "domain": "金融",
    "title": "Sticky wage norms and the real wage cost of unexpected inflation",
    "url": "https://bfi.uchicago.edu/wp-content/uploads/2026/08/BFI_WP_2026-108-1.pdf",
    "source": "jplusequalt",
    "platform": "hackernews",
    "points": 391,
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
    "id": "hn:49122994",
    "domain": "金融",
    "title": "Situational Awareness down 67% in July in AI stock rout",
    "url": "https://www.wsj.com/finance/investing/situational-awareness-down-67-in-july-in-ai-stock-rout-cd19901f",
    "source": "pondsider",
    "platform": "hackernews",
    "points": 157,
    "published_at": "2026-07-31T13:37:36+00:00",
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
    "id": "hn:49304409",
    "domain": "金融",
    "title": "Make a 6-Tesla-class high-temperature superconducting dipole magnet at 4.2 K",
    "url": "https://journals.aps.org/prab/abstract/10.1103/4nhs-bkwh",
    "source": "supermagnet",
    "platform": "hackernews",
    "points": 48,
    "published_at": "2026-08-14T20:49:29+00:00",
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
    "id": "hn:49182971",
    "domain": "金融",
    "title": "OpenAI settles claims of discrimination against US workers for $3.2M",
    "url": "https://finance.yahoo.com/technology/ai/articles/openai-settles-claims-discrimination-against-221429616.html",
    "source": "declan_roberts",
    "platform": "hackernews",
    "points": 27,
    "published_at": "2026-08-05T13:57:19+00:00",
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
    "id": "hn:49033778",
    "domain": "金融",
    "title": "Reality Bites Elon Musk and His Tesla, SpaceX Believers",
    "url": "https://www.wsj.com/finance/stocks/reality-bites-elon-musk-and-his-tesla-spacex-believers-1b639591",
    "source": "doener",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-07-24T10:59:51+00:00",
    "summary": ""
  }
]
```
