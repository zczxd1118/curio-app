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

- 今日日期：`2026-11-10`
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
  "date": "2026-11-10",
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
    "id": "bvid:BV1REx46NEc4",
    "domain": "AI",
    "title": "【全网最全】DeepSeek Harness超详细教程！50分钟吃透DSH，让SuperAgent给你干活！",
    "url": "http://www.bilibili.com/video/av117540671982699",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 2467773,
    "published_at": "2026-11-01T10:22:02+00:00",
    "summary": "DeepSeek Harness超详细教程！\n大家可以速速收藏啦~\n耗时60天制作！感谢大家的三联\n未来还会出其他AI教程，大家可以关注一下~"
  },
  {
    "id": "bvid:BV1E7wtzaEdq",
    "domain": "AI",
    "title": "从 LLM 到 Agent Skill，一期视频带你打通底层逻辑！",
    "url": "http://www.bilibili.com/video/av116227955497963",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 2228611,
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
    "points": 2101895,
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
    "points": 1482701,
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
    "points": 1475083,
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
    "points": 1449802,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV14rzQB9EJj",
    "domain": "AI",
    "title": "Claude Code 从 0 到 1 全攻略：MCP / SubAgent / Agent Skill / Hook / 图片 / 上下文处理/ 后台任务",
    "url": "http://www.bilibili.com/video/av115954889596221",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 1344046,
    "published_at": "2026-01-25T08:55:20+00:00",
    "summary": "时间戳如下，方便大家跳转观看：\n \n第一部分：环境搭建与基础交互\n- 01:09 安装 Claude Code\n- 01:43 登录与授权\n- 02:55 第一个实战问题\n- 03:12 三种模式详解 (默认/自动/规划)\n \n第二部分：复杂任务处理与终端控制\n- 06:00 执行终端命令 (Bash)\n- 06:49 使用规划模式 (Plan Mode)\n- 11:06 跳过所有权限检测 (da"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 748889,
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
    "points": 596159,
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
    "points": 550046,
    "published_at": "2026-11-05T10:00:00+00:00",
    "summary": "我们花了两个月整理出来了AI工具：Codex从入门到精通的全教程。这里面包含了安装、核心功能介绍、以及可快速上手的实战案例等等 完全免费的公益课程，如果你看完觉得有帮助，麻烦【点赞、投币、收藏】一键三连，就当作这门课的学费啦！做免费课程不容易，先谢谢大家支持！"
  },
  {
    "id": "bvid:BV13YRjBTEPb",
    "domain": "AI",
    "title": "Hermes Agent零基础、保姆级教程，小白也能轻松玩转",
    "url": "http://www.bilibili.com/video/av116503638706867",
    "source": "iwenwiki",
    "platform": "bilibili",
    "points": 431884,
    "published_at": "2026-05-02T06:51:59+00:00",
    "summary": "全B站最详细的Hermes Agent教程，从部署到玩转！零基础，小白也能轻松玩转Hermes Agent，真正的AI助手，恐怖如斯！"
  },
  {
    "id": "bvid:BV1kr4h6fExw",
    "domain": "AI",
    "title": "DeepSeek 新出的 Super Agent 是什么？真有用么？",
    "url": "http://www.bilibili.com/video/av117564076202051",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 410376,
    "published_at": "2026-11-05T13:35:56+00:00",
    "summary": "DeepSeek Harness 团队最新开源的 Super-agent 是什么？和传统 Agent 有什么区别？它是怎么工作的？真的能提升 AI 工作的效率么？一期视频带你掌握 Super-agent 智能体，对 AI 小白、AI 编程爱好者、前端和后端程序员、AI 应用开发求职者都有帮助\n编程学习教程+实战项目+简历模板：codefather.cn\n免费 AI 编程教程：github.com/"
  },
  {
    "id": "bvid:BV1vG8QzcE5X",
    "domain": "AI",
    "title": "Claude使用指南，claude code零基础教程，claude code安装配置到实战",
    "url": "http://www.bilibili.com/video/av114933744272468",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 358258,
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
    "points": 351320,
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
    "points": 324257,
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
    "points": 296587,
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
    "points": 230020,
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
    "points": 186310,
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
    "points": 165344,
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
    "points": 161855,
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
    "points": 104378,
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
    "points": 97021,
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
    "points": 94292,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operit教程：入门安卓最强大ai平台operitAI",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 77317,
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
    "points": 69764,
    "published_at": "2026-08-27T00:43:58+00:00",
    "summary": "v1.1.6安装包：\n夸克网盘：\n链接：https://pan.quark.cn/s/43ff3db459f4?pwd=SD2k\n提取码：SD2k\ngithub仓库：\nPlaya-0v0/Cyrene-Agent: An open-source AI desktop companion inspired by Cyrene, combining immersive Chat, personaliz"
  },
  {
    "id": "bvid:BV1RrZHYqEvm",
    "domain": "AI",
    "title": "Cursor+Figma MCP，自动生成可编辑设计稿",
    "url": "http://www.bilibili.com/video/av114257538650701",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 52819,
    "published_at": "2025-03-31T14:36:31+00:00",
    "summary": "分享了两种Figma MCP。一种是通过获取Figma API key来实现Cursor和Figma的连接，更侧重精准控制。\n.\n因为大多数 Figma 文件都会非常大，如果你想让Cursor精准链接到文件中的特定元素，一般选择这个MCP会更合适。\n.\n另一种则是通过Figma插件形式，通过channel实现与Cursor的连接，更侧重从0到1的设计元素生成，比较适合没有太多设计基础的用户。\n.\n"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 50326,
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
    "points": 48019,
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
    "points": 47815,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1uVSUBkEfZ",
    "domain": "AI",
    "title": "Microsoft Copilot完整教程(上) 从入门到Agent 一站式掌握AI办公",
    "url": "http://www.bilibili.com/video/av116351721084069",
    "source": "星小脉",
    "platform": "bilibili",
    "points": 44181,
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
    "points": 41331,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV1h3W76wEem",
    "domain": "AI",
    "title": "Claude(Code)桌面APP，保姆级全攻略，一期视频精通，顶级Agent软件长什么样？",
    "url": "http://www.bilibili.com/video/av117580048108571",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 41224,
    "published_at": "2026-11-08T09:14:07+00:00",
    "summary": "最近Claude桌面端（Claude Desktop） 有了一大波功能更新。随着一步步的迭代，它已经把 Claude Code 的编程、Claude Design 的设计，以及 Claude Cowork 的办公等核心能力，全部收入了同一个桌面客户端，特别是Claude Code已经从原本黑乎乎的命令行工具，进化成了桌面客户端的完全体形态。再搭配上超强的Opus5.5 模型，已经能称得上是地表顶级"
  },
  {
    "id": "bvid:BV1hmb26ZEws",
    "domain": "AI",
    "title": "DeepSeek Harness 实测  Claude Code 对比后，梁神我错了 差距比我想的大",
    "url": "http://www.bilibili.com/video/av117100337236191",
    "source": "程序员晓刘",
    "platform": "bilibili",
    "points": 38684,
    "published_at": "2026-08-15T16:01:38+00:00",
    "summary": "这期用同一个 DeepSeek Pro 0813 模型，分别在 Claude Code 和 DeepSeek Harness 里完成同样的任务，对比工具链对最终效果的影响。\n实测内容包括：\nFPS 游戏 Demo、灯塔预警沙盘、手枪组装动画、显示器组装动画，以及 DeepSeek Harness 的插件化源码流程。\n整体看下来，模型本身当然重要，但 Harness 在插件化、流程记录、缓存命中和任"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 34672,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1sQaL6vEkb",
    "domain": "AI",
    "title": "小白向，ai入门第一课：agent的部署和使用！",
    "url": "http://www.bilibili.com/video/av117349378166797",
    "source": "沈三殊",
    "platform": "bilibili",
    "points": 32674,
    "published_at": "2026-09-28T15:30:36+00:00",
    "summary": "详细的agent部署介绍：https://pan.quark.cn/s/3846914c6da7\n欢迎来到ai的世界！！\n有疑问欢迎私信。"
  },
  {
    "id": "bvid:BV18cnF6NEjC",
    "domain": "AI",
    "title": "实测！Grok Cursor等多模型整合后，性价比如何？",
    "url": "http://www.bilibili.com/video/av117471180821997",
    "source": "野生吃货",
    "platform": "bilibili",
    "points": 30439,
    "published_at": "2026-10-20T03:50:25+00:00",
    "summary": "简介无推广内容\n视频中演示网站有正规ICP备案"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29943,
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
    "points": 29051,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1wpxq6VEXx",
    "domain": "AI",
    "title": "【AI时代的STM32教程】AI Agent 初体验",
    "url": "http://www.bilibili.com/video/av117529699682124",
    "source": "keysking",
    "platform": "bilibili",
    "points": 28980,
    "published_at": "2026-10-30T11:52:06+00:00",
    "summary": "一句话，让 AI 帮我们完成第一个 STM32C5 程序！🚀\n本期我们一起认识 AI Agent，学习如何描述开发需求，并借助开源的 STM32C5DevSkills，让 AI 完成工程创建、芯片配置、代码编写和编译烧录，让律动小板上的小灯闪烁起来！\n也特别感谢 @意法半导体中国   对本系列教程的支持～下期我们再亲手走一遍开发流程，把 Agent 替我们完成的工作，一步步搞明白！"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 26588,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 26335,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1uwxG6DEra",
    "domain": "AI",
    "title": "3分钟讲透：Vibe Coding如何避免💩屎山代码",
    "url": "http://www.bilibili.com/video/av117513727838880",
    "source": "鲤哥builder",
    "platform": "bilibili",
    "points": 23891,
    "published_at": "2026-10-27T16:09:19+00:00",
    "summary": ""
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
    "id": "bvid:BV1m7N1zKEU8",
    "domain": "AI",
    "title": "🚀Cursor+Serena最佳组合告别AI编程工具短板！支持Claude Code、windsurf、Cline！让AI编程不再是简单读取代码而是智能分析",
    "url": "http://www.bilibili.com/video/av114721764152608",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 20800,
    "published_at": "2025-06-21T14:18:09+00:00",
    "summary": "🚀Cursor+Serena最佳组合告别AI编程工具短板！支持Claude Code、windsurf、Cline！让AI编程不再是简单读取代码而是智能分析依赖关系，让复杂开源项目二次开发效率提升十倍\n\n🚀🚀🚀视频简介：\n✅震撼！这款完全开源免费的AI编程助手Serena，竟然能像资深开发者一样真正理解复杂项目代码结构，从需求分析到最终实现测试一站式搞定，颠覆传统AI编程工具！\n✅本期视频详细介绍"
  },
  {
    "id": "bvid:BV1bBHm6MEG5",
    "domain": "AI",
    "title": "这绝对是b站讲的最好的Claude Code全套实战教程，手把手带你搞定国内环境安装配置，全程干货无废话！AI大模型/MCP/Skill/智能体/Agent",
    "url": "http://www.bilibili.com/video/av117402847155229",
    "source": "大模型饼饼",
    "platform": "bilibili",
    "points": 19719,
    "published_at": "2026-10-08T02:13:21+00:00",
    "summary": "这绝对是B站讲得最好的Claude Code全套实战教程！手把手带你搞定国内环境安装配置、基础操作、高阶实战技巧，课程不堆砌冗余理论，聚焦真实开发场景，带你吃透Claude Code核心能力，打通MCP、Skill与Agent智能体联动开发。不管你是想提升日常编码效率，还是入门AI智能体开发，这套教程都非常适合你，全程干货无废话！"
  },
  {
    "id": "bvid:BV1xh3C6cEGv",
    "domain": "AI",
    "title": "两周完成一篇SCI论文，用claude code帮你干",
    "url": "http://www.bilibili.com/video/av117002408559933",
    "source": "博士大师兄木水",
    "platform": "bilibili",
    "points": 16097,
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
    "points": 15542,
    "published_at": "2026-04-15T09:55:02+00:00",
    "summary": "配套资料👉：https://b23.tv/qvhxmaQ\n包括:AI测试网站，几十个AI场景测试完整流程，skil文档，测试八股文，项目源码，测试用例模板，工具安装包，学习计划表，学习路线，100g测试新人资料包等等，资料百分百免费，放心领取~"
  },
  {
    "id": "bvid:BV1DSFeeqEck",
    "domain": "AI",
    "title": "Cursor从小白到专家-第20课：Cursor记住的对话太短？四种方法增强上下文管理",
    "url": "http://www.bilibili.com/video/av113928420005852",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 14643,
    "published_at": "2025-02-01T11:39:40+00:00",
    "summary": "在多轮对话后，如果大家发现Cursor写的代码开始不尽人意，那么很可能是对话超出上下文限制了。\n.\n上下文限制是AI模型的通病之一，即使Cursor官方人员也表示他们还没找到针对“无限上下文”的解决方案。所以今天这条视频，并不是，也没有能力从根本上解决这个问题，而是给大家分享四种增强上下文管理的方法，让Cursor不那么“健忘”：\n.\n方法一：Summarized Composers\n方法二：Op"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 13849,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
  },
  {
    "id": "bvid:BV1tDnV6ME79",
    "domain": "AI",
    "title": "当我把claude code搬进安卓设备……",
    "url": "http://www.bilibili.com/video/av117462439826705",
    "source": "Grey-Oak",
    "platform": "bilibili",
    "points": 12948,
    "published_at": "2026-10-18T14:44:02+00:00",
    "summary": "cccodroid 是一个开源的安卓应用，把 Claude Code 装进你的安卓设备。不用 root，不刷机，也不套 Linux 虚拟环境，工具直接在安卓上原生运行。\n\n视频全程实机录屏（联想y700二代平板，骁龙 8+），没有连电脑：\n· 一句话让它改代码，先给计划，你点批准才动手\n· 终端里 pkg install rust，现场打包 APK 装上\n· docx / xlsx / pptx "
  },
  {
    "id": "hn:50418016",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia CEO Jensen Huang's letter to staff about affair",
    "url": "https://nvidianews.nvidia.com/news/a-message-to-our-company",
    "source": "karimf",
    "platform": "hackernews",
    "points": 959,
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
    "points": 490,
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
    "id": "hn:50427486",
    "domain": "AI 算力 / 半导体",
    "title": "Commerce Dept Inquiry into Megaspeed Halted After Nvdia Intervention",
    "url": "https://www.nytimes.com/2026/11/09/business/economy/nvidia-megaspeed-investigation-huang.html",
    "source": "louiereederson",
    "platform": "hackernews",
    "points": 51,
    "published_at": "2026-11-09T16:10:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:50392256",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia was in 1 in 11 startup rounds over $100M last year",
    "url": "https://datahyena.com/research/a-chipmaker-was-in-one-of-every-eleven-100m-rounds/",
    "source": "ghostfoxgod",
    "platform": "hackernews",
    "points": 79,
    "published_at": "2026-11-06T13:48:35+00:00",
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
    "id": "hn:50416787",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Opens Investigation into Jensen Huang's Relationship with Chinese Spy",
    "url": "https://www.nytimes.com/2026/11/08/technology/nvidia-investigation-jensen-huang-china.html",
    "source": "Aboutplants",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-11-08T20:25:56+00:00",
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
    "id": "hn:50415161",
    "domain": "AI 算力 / 半导体",
    "title": "US believes Nvidia's Huang had romantic relationship with alleged Chinese spy",
    "url": "https://www.ft.com/content/a55a2a22-4479-4f93-a445-6147a5c6d790",
    "source": "mgh2",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-11-08T17:19:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:50417283",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia launches investigation into CEO's affair with suspected Chinese spy",
    "url": "https://www.bbc.co.uk/news/articles/c3dxw10rjn9no",
    "source": "haritha-j",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-11-08T21:09:42+00:00",
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
    "id": "rss:https://www.eetimes.com/powering-ai-data-centers-rethinking-energy-infrastructure-for-the-next-wave-of-ai-growth/",
    "domain": "AI 算力 / 半导体",
    "title": "Powering AI Data Centers: Rethinking Energy Infrastructure for the Next Wave of AI Growth",
    "url": "https://www.eetimes.com/powering-ai-data-centers-rethinking-energy-infrastructure-for-the-next-wave-of-ai-growth/",
    "source": "EE Times Staff",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T14:00:51+00:00",
    "summary": "AI data centers need faster, resilient power; learn how microgrids, storage, and intelligent controls can ease grid constraints in this partner interview. The post Powering AI Data Centers: Rethinking"
  },
  {
    "id": "rss:https://www.eetimes.com/still-looking-for-diamonds/",
    "domain": "AI 算力 / 半导体",
    "title": "Still Looking for Diamonds",
    "url": "https://www.eetimes.com/still-looking-for-diamonds/",
    "source": "Moshe Zalcberg",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T13:31:16+00:00",
    "summary": "Silicon carbide demand surges, but Europe risks hollow sovereignty as investment flows abroad; see why Bulgaria’s fab needs customers first. The post Still Looking for Diamonds appeared first on EE Ti"
  },
  {
    "id": "rss:https://www.eetimes.com/designing-smarter-security-and-portable-camera-systems/",
    "domain": "AI 算力 / 半导体",
    "title": "Designing Smarter Security and Portable Camera Systems",
    "url": "https://www.eetimes.com/designing-smarter-security-and-portable-camera-systems/",
    "source": "onsemi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T13:27:35+00:00",
    "summary": "Security and portable camera designers must balance image quality, power consumption, connectivity, and system cost across widely different operating environments. This guide provides a practical syst"
  },
  {
    "id": "rss:https://www.eetimes.com/deepx-tapes-out-second-gen-chip-projects-6-7x-performance-gain-with-lpddr5x-pim/",
    "domain": "AI 算力 / 半导体",
    "title": "DeepX Tapes Out Second-Gen Chip, Projects 6.7× Performance Gain With LPDDR5x-PIM",
    "url": "https://www.eetimes.com/deepx-tapes-out-second-gen-chip-projects-6-7x-performance-gain-with-lpddr5x-pim/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T06:47:26+00:00",
    "summary": "DeepX is targeting edge markets including robotics with its second-generation AI accelerator, which can run large LLMs on device in under 5 W. The post DeepX Tapes Out Second-Gen Chip, Projects 6.7× P"
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
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/acer-predator-helios-neo-16s-ai-review",
    "domain": "AI 算力 / 半导体",
    "title": "Acer Predator Helios Neo 16S AI Review: Slim OLED gaming that doesn't last long",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/acer-predator-helios-neo-16s-ai-review",
    "source": "Charles Jefferies",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T14:05:00+00:00",
    "summary": "The Acer Predator Helios Neo 16S AI pairs strong gaming performance, a 240 Hz OLED display, and good upgradeability but compromises the package with relatively short battery life."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-pro-6000-users-cables-almost-melted-even-when-limited-to-500w-12v-2x6-cables-appear-to-still-cause-problems-show-clear-signs-of-melting",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia RTX PRO 6000 user’s cables almost melted, even when limited to 500W",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-pro-6000-users-cables-almost-melted-even-when-limited-to-500w-12v-2x6-cables-appear-to-still-cause-problems-show-clear-signs-of-melting",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T14:00:00+00:00",
    "summary": "The 12V-2x6 connector nearly took out two RTX PRO 6000 Blackwell Workstation GPUs; luckily, the owner spotted the damaged cables before they melted the GPU connectors."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/anthropic-skips-six-year-waitlist-with-massive-usd3-4-billion-gas-turbine-generator-deal-firm-takes-over-onepwrs-orders-secures-1-7gw-of-capacity-to-power-ai-data-centers",
    "domain": "AI 算力 / 半导体",
    "title": "Anthropic skips six-year waitlist with massive $3.4 billion gas turbine generator deal",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/anthropic-skips-six-year-waitlist-with-massive-usd3-4-billion-gas-turbine-generator-deal-firm-takes-over-onepwrs-orders-secures-1-7gw-of-capacity-to-power-ai-data-centers",
    "source": "Newton Gitonga",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T13:45:00+00:00",
    "summary": "Anthropic has committed $3.4 billion to secure 1.7GW of gas-fired generators from OnePWR Solutions, taking over existing Caterpillar orders as lengthy equipment lead times push AI companies to build t"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/memory-shortage-spurs-smartphone-makers-to-melt-used-memory-off-old-devices-then-re-solder-it-onto-new-products-recycled-memory-to-keep-budget-phones-affordable-reballing-adoption-to-double-by-2027",
    "domain": "AI 算力 / 半导体",
    "title": "Memory shortage spurs smartphone makers to melt used memory off old devices, then re-solder it onto new products",
    "url": "https://www.tomshardware.com/pc-components/dram/memory-shortage-spurs-smartphone-makers-to-melt-used-memory-off-old-devices-then-re-solder-it-onto-new-products-recycled-memory-to-keep-budget-phones-affordable-reballing-adoption-to-double-by-2027",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T13:40:00+00:00",
    "summary": "Reballed memory currently accounts for a small share of smartphone components, but adoption could nearly double by 2027 as manufacturers look for alternatives to increasingly expensive DRAM."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/lawyer-builds-private-ai-server-with-eight-used-nvidia-v100-gpus-up-to-215-tokens-per-second-to-keep-legal-files-offline-costing-about-usd2-400-per-four-gpu-board",
    "domain": "AI 算力 / 半导体",
    "title": "Lawyer builds private AI server with eight used Nvidia V100 GPUs",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/lawyer-builds-private-ai-server-with-eight-used-nvidia-v100-gpus-up-to-215-tokens-per-second-to-keep-legal-files-offline-costing-about-usd2-400-per-four-gpu-board",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T13:20:00+00:00",
    "summary": "A lawyer runs DeepSeek V4.1 Flash on eight used 2018-era Nvidia V100 GPUs at up to 215 tokens/s, keeping case files in the office."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/china-builds-massive-800-megawatt-ai-data-center-campus-to-rival-us-stargate-project-galaxy-campus-delivers-first-120-megawatts-in-a-year-at-one-fifth-the-cost",
    "domain": "AI 算力 / 半导体",
    "title": "China builds massive 800-megawatt AI data center campus to rival US Stargate project",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/china-builds-massive-800-megawatt-ai-data-center-campus-to-rival-us-stargate-project-galaxy-campus-delivers-first-120-megawatts-in-a-year-at-one-fifth-the-cost",
    "source": "Newton Gitonga",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T13:00:00+00:00",
    "summary": "Envision has delivered the first 120MW of its Galaxy AI datacenter in less than a year, combining wind farms, battery storage and an unconventional cooling system to cut costs and keep power-hungry se"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/spoof-program-monitors-and-emails-your-ram-usage-to-sam-altman-if-under-90-percent-utilization-ram-altman-logs-usage-and-reports-you-for-wasting-memory",
    "domain": "AI 算力 / 半导体",
    "title": "Spoof program monitors and emails your RAM usage to Sam Altman if under 90% utilization",
    "url": "https://www.tomshardware.com/pc-components/ram/spoof-program-monitors-and-emails-your-ram-usage-to-sam-altman-if-under-90-percent-utilization-ram-altman-logs-usage-and-reports-you-for-wasting-memory",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T12:31:12+00:00",
    "summary": "A new GitHub repository dubbed ram-altman features a script to monitor your PC’s RAM usage and report back to the eponymous OpenAI boss."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/huawei-develops-entirely-chinese-homegrown-desktop-pc-system-features-10-core-20-thread-kirin-x90-consumer-cpu-and-huaweis-own-harmonyos-operating-system-but-western-supply-chain-lingers",
    "domain": "AI 算力 / 半导体",
    "title": "Huawei develops 'entirely Chinese' homegrown desktop PC system",
    "url": "https://www.tomshardware.com/tech-industry/huawei-develops-entirely-chinese-homegrown-desktop-pc-system-features-10-core-20-thread-kirin-x90-consumer-cpu-and-huaweis-own-harmonyos-operating-system-but-western-supply-chain-lingers",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T12:30:00+00:00",
    "summary": "Huawei's 'entirely Chinese' desktop system does not use components made outside of China, yet they still rely on semiconductor supply chain that includes tools and materials from America, the Netherla"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/grab-amds-fastest-mainstream-gaming-cpu-for-a-record-low-usd399-99-right-now-powerhouse-ryzen-7-9800x3d-chip-is-a-must-buy-upgrade-for-any-am5-gaming-pc-build",
    "domain": "AI 算力 / 半导体",
    "title": "Grab AMD's fastest mainstream gaming CPU for a record-low $399.99 right now",
    "url": "https://www.tomshardware.com/pc-components/cpus/grab-amds-fastest-mainstream-gaming-cpu-for-a-record-low-usd399-99-right-now-powerhouse-ryzen-7-9800x3d-chip-is-a-must-buy-upgrade-for-any-am5-gaming-pc-build",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T12:21:50+00:00",
    "summary": "The AMD Ryzen 7 9800X3D is down to an all-time low price of $399.95, with the 9850X3D down to $419.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/wearable-tech/wearable-sleep-trackers-are-using-your-brainwaves-to-train-ai-models-without-explicit-user-consent-tens-of-millions-of-hours-of-eeg-data-harvested",
    "domain": "AI 算力 / 半导体",
    "title": "Wearable sleep trackers are using your brainwaves to train AI models without explicit user consent",
    "url": "https://www.tomshardware.com/peripherals/wearable-tech/wearable-sleep-trackers-are-using-your-brainwaves-to-train-ai-models-without-explicit-user-consent-tens-of-millions-of-hours-of-eeg-data-harvested",
    "source": "Newton Gitonga",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T12:00:00+00:00",
    "summary": "Wearable neurotech companies have collected millions of hours of brainwave recordings to train AI models, raising questions about user consent, data privacy and who ultimately controls our neural data"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpu-drivers/amd-adrenalin-bug-could-be-writing-data-continuously-wearing-out-ssds-radeon-owner-claims-external-events-utility-used-up-1-percent-of-ssd-health-every-month-for-over-a-year",
    "domain": "AI 算力 / 半导体",
    "title": "AMD admits GPU driver bug is writing data continuously, wearing out SSDs",
    "url": "https://www.tomshardware.com/pc-components/gpu-drivers/amd-adrenalin-bug-could-be-writing-data-continuously-wearing-out-ssds-radeon-owner-claims-external-events-utility-used-up-1-percent-of-ssd-health-every-month-for-over-a-year",
    "source": "Newton Gitonga",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T11:46:33+00:00",
    "summary": "AMD is investigating reports that its External Events Utility generates continuous SSD writes of up to 5MB/s, even when Radeon-powered PCs are idle. Users have also reported declining SSD health, whil"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-usd300-on-this-rtx-5070-gaming-pc-with-32gb-ddr5-now-under-usd2-000-pre-built-abs-rig-from-newegg-is-4k-ready-with-an-intel-cpu-and-a-1tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Save $300 on this RTX 5070 gaming PC with 32GB DDR5, now under $2,000",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-usd300-on-this-rtx-5070-gaming-pc-with-32gb-ddr5-now-under-usd2-000-pre-built-abs-rig-from-newegg-is-4k-ready-with-an-intel-cpu-and-a-1tb-ssd",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T11:36:31+00:00",
    "summary": "This ABS Flux II Aqua gaming PC deal unlocks 1440p and 4K gameplay for just $1,999.99. This pre-built comes with a 20-core Intel CPU, an Nvidia GeForce RTX 5070, a 1TB SSD, and 32GB of DDR5 RAM, savin"
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/lg-woled-tvs-suffer-from-edge-rot-pixel-death-pixels-go-dark-around-the-edges-similar-to-a-mold-pattern-nearly-all-woled-test-units-show-clear-signs-of-degradation",
    "domain": "AI 算力 / 半导体",
    "title": "LG WOLED TVs suffer from 'edge rot' pixel death",
    "url": "https://www.tomshardware.com/monitors/lg-woled-tvs-suffer-from-edge-rot-pixel-death-pixels-go-dark-around-the-edges-similar-to-a-mold-pattern-nearly-all-woled-test-units-show-clear-signs-of-degradation",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T11:30:00+00:00",
    "summary": "LG WOLED TV panels made around 2019 to 2023 may be susceptible to edge rot — almost all of RTings' WOLED test units show clear signs of degradation"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/docking-stations-hubs/synaptics-sends-cease-and-desist-order-to-creator-of-open-source-displaylink-driver-dares-him-to-publicize-its-threats-dev-reverse-engineers-displaylink-using-claude-ai-and-rust-synaptics-threatens-to-bill-creator-for-legal-documentation",
    "domain": "AI 算力 / 半导体",
    "title": "Synaptics sends cease-and-desist order to creator of open-source DisplayLink driver, dares him to publicize its threats",
    "url": "https://www.tomshardware.com/peripherals/docking-stations-hubs/synaptics-sends-cease-and-desist-order-to-creator-of-open-source-displaylink-driver-dares-him-to-publicize-its-threats-dev-reverse-engineers-displaylink-using-claude-ai-and-rust-synaptics-threatens-to-bill-creator-for-legal-documentation",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T11:00:00+00:00",
    "summary": "A hobbyist's effort to make DisplayLink work better on Linux is turning into a legal saga."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/security-researcher-had-to-jailbreak-their-car-just-to-update-the-clock-missing-tomtom-sd-card-locked-settings-menu-custom-linux-exploit-deployed-to-adjust-daylight-saving-time",
    "domain": "AI 算力 / 半导体",
    "title": "Security researcher had to jailbreak their car just to update the clock",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/security-researcher-had-to-jailbreak-their-car-just-to-update-the-clock-missing-tomtom-sd-card-locked-settings-menu-custom-linux-exploit-deployed-to-adjust-daylight-saving-time",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T10:40:00+00:00",
    "summary": "A security researcher has revealed how they managed to update the time on their car infotainment system using reverse engineering techniques."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/grab-32-gb-of-ram-for-just-usd209-99-thanks-to-the-g-skill-ripjaws-v-ddr4-3200-kit-rare-sale-on-a-quality-kit-from-an-enthusiast-brand-with-a-stellar-reputation",
    "domain": "AI 算力 / 半导体",
    "title": "Grab 32 GB of RAM for just $209.99 thanks to the G.Skill Ripjaws V DDR4-3200 kit",
    "url": "https://www.tomshardware.com/pc-components/grab-32-gb-of-ram-for-just-usd209-99-thanks-to-the-g-skill-ripjaws-v-ddr4-3200-kit-rare-sale-on-a-quality-kit-from-an-enthusiast-brand-with-a-stellar-reputation",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T10:20:00+00:00",
    "summary": "Grab 32 GB of RAM for just $209.99 thanks to the G.Skill Ripjaws V DDR4-3200 kit"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-ceo-jensen-huang-admits-to-having-an-affair-with-suspected-chinese-spy-jensen-apologizes-in-letter-to-staff-company-board-forms-independent-committee-to-investigate",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia CEO Jensen Huang admits to having an affair with suspected Chinese spy",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-ceo-jensen-huang-admits-to-having-an-affair-with-suspected-chinese-spy-jensen-apologizes-in-letter-to-staff-company-board-forms-independent-committee-to-investigate",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-08T21:27:29+00:00",
    "summary": "Nvidia's board of directors is investigating a report about Jensen Huang's alleged affair with a client, claims it is still confident in Jensen and leadership team."
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
    "points": 863,
    "published_at": "2026-11-07T09:46:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:50363461",
    "domain": "大厂 AI 动态",
    "title": "Tell HN: Gemini trains on chat history, even for subscribers (personal accounts)",
    "url": "https://news.ycombinator.com/item?id=50363461",
    "source": "jameslk",
    "platform": "hackernews",
    "points": 736,
    "published_at": "2026-11-04T10:10:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:50429426",
    "domain": "大厂 AI 动态",
    "title": "Google Gemini routes personal Drive files and emails to human annotators",
    "url": "https://github.com/thisisme6598/gemini_files/",
    "source": "gf74918",
    "platform": "hackernews",
    "points": 620,
    "published_at": "2026-11-09T18:24:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:50411961",
    "domain": "大厂 AI 动态",
    "title": "Llama-modchip: 284B DeepSeek on 64GB RAM, no GPU",
    "url": "https://github.com/synchopate/llama-modchip",
    "source": "joshcsimmons",
    "platform": "hackernews",
    "points": 480,
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
    "id": "rss:https://www.theverge.com/entertainment/1030510/paramount-skydance-david-ellison-ai",
    "domain": "大厂 AI 动态",
    "title": "David Ellison says AI could be the ‘biggest creative unlock in modern history’",
    "url": "https://www.theverge.com/entertainment/1030510/paramount-skydance-david-ellison-ai",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T00:28:49+00:00",
    "summary": "During Paramount Skydance's latest earnings call, CEO David Ellison said \"it's hard to imagine\" AI won't have a bigger impact on the film industry than CGI. In response to a question about the company"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1030328/what-could-china-get-from-jensen-huang",
    "domain": "大厂 AI 动态",
    "title": "What could China get from Jensen Huang?",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1030328/what-could-china-get-from-jensen-huang",
    "source": "Lauren Feiner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T23:51:58+00:00",
    "summary": "It's difficult to overstate Nvidia's power in today's AI landscape. The company's chips are the bedrock upon which advanced AI technology in the US is being built, and demand has consistently outpaced"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1030446/trump-jensen-huang-press-conference",
    "domain": "大厂 AI 动态",
    "title": "Here’s what Trump said he knew about Jensen Huang",
    "url": "https://www.theverge.com/tech/1030446/trump-jensen-huang-press-conference",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T23:47:46+00:00",
    "summary": "President Trump held a White House press briefing earlier today and responded to several questions about his knowledge of Nvidia CEO Jensen Huang's affair with an alleged Chinese spy. Huang said this "
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1030422/nvidia-jensen-huang-ai-china-alice-huang",
    "domain": "大厂 AI 动态",
    "title": "Everything we know so far about the Nvidia spy scandal targeting CEO Jensen Huang",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1030422/nvidia-jensen-huang-ai-china-alice-huang",
    "source": "Richard Lawler",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T23:07:59+00:00",
    "summary": "The leather-jacketed CEO of Nvidia, Jensen Huang, has acknowledged an affair with Megaspeed exec Alice Huang, spurring an investigation by his company and intense discussions worldwide. Recent reporti"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1030262/msi-mag-272qp-qd-oled-x24-monitor-woot-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "MSI’s refurbished QD-OLED gaming monitor is on sale for under $300",
    "url": "https://www.theverge.com/gadgets/1030262/msi-mag-272qp-qd-oled-x24-monitor-woot-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T21:43:41+00:00",
    "summary": "One of the best upgrades you can make to your PC gaming setup is an OLED monitor. Fortunately, MSI’s factory-reconditioned Mag 272QP X24 is on sale at Woot through November 18th with a 180-day manufac"
  },
  {
    "id": "rss:https://www.theverge.com/science/1030252/ai-data-center-climate-pledge-united-nations-cop31",
    "domain": "大厂 AI 动态",
    "title": "The global pledge to use AI for climate good is a cruel joke",
    "url": "https://www.theverge.com/science/1030252/ai-data-center-climate-pledge-united-nations-cop31",
    "source": "Justine Calma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T21:13:16+00:00",
    "summary": "At this point, reading through the latest splashy pledge to use AI for the good of the environment feels like downing a nonalcoholic beer. Admittedly, I'm suspicious from the onset. How can this be go"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1030084/apple-intelligence-usage-packs-ai-features-creator-studio-logic-pro",
    "domain": "大厂 AI 动态",
    "title": "Apple’s $50 Intelligence Usage Packs extend access to some AI features",
    "url": "https://www.theverge.com/tech/1030084/apple-intelligence-usage-packs-ai-features-creator-studio-logic-pro",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T19:09:58+00:00",
    "summary": "After publishing a support article in early September outlining usage limits for some Apple Intelligence features, the company has updated Logic Pro with an option to \"Buy More Usage\" for a one-time p"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1030005/anthropic-claude-fable-mythos-5-2",
    "domain": "大厂 AI 动态",
    "title": "Anthropic launches new Claude Fable and Mythos 5.2 models",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1030005/anthropic-claude-fable-mythos-5-2",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T19:00:00+00:00",
    "summary": "Anthropic is announcing two new models today: Claude Fable 5.2 and Claude Mythos 5.2, which it says are designed to take on \"daunting\" technical challenges. The company claims the new models show impr"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1029998/game-pass-ultimate-three-months-lego-pokemon-pikachu-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "You can grab three months of Game Pass Ultimate for under $20 per month",
    "url": "https://www.theverge.com/gadgets/1029998/game-pass-ultimate-three-months-lego-pokemon-pikachu-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T18:35:25+00:00",
    "summary": "The price of Xbox Game Pass Ultimate has fluctuated between $20 and $30 per month over the last year, but you can get three months of the top plan for around $19 per month. At Newegg, using the coupon"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1030061/instagram-ai-effect-builder-filters",
    "domain": "大厂 AI 动态",
    "title": "Instagram’s Effect Builder makes new filters from AI prompts",
    "url": "https://www.theverge.com/tech/1030061/instagram-ai-effect-builder-filters",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T18:07:23+00:00",
    "summary": "After expanding its Edits app to macOS last week, Instagram's next move is launching this Effect Builder that generates custom filters for your Stories posts with AI. Available now for US residents wh"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/09/otter-ai-can-now-follow-conversations-across-30-languages/",
    "domain": "大厂 AI 动态",
    "title": "Otter AI can now follow conversations across 30+ languages",
    "url": "https://techcrunch.com/2026/11/09/otter-ai-can-now-follow-conversations-across-30-languages/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T07:00:00+00:00",
    "summary": "Otter AI just added support for 27 languages and revealed an upcoming feature that can follow along if speakers switch between languages."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/09/californias-proposed-billionaire-tax-fails-to-pass/",
    "domain": "大厂 AI 动态",
    "title": "California’s proposed ‘billionaire tax’ fails to pass",
    "url": "https://techcrunch.com/2026/11/09/californias-proposed-billionaire-tax-fails-to-pass/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T05:18:43+00:00",
    "summary": "California voters rejected Proposition 40, the one-time 5% tax on billionaires, the AP reported Monday. Tech leaders outspent backers roughly 10 to 1 to defeat it, and the founders and economists Tech"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/09/jensen-huangs-alleged-honeypot-scandal-has-inspired-some-top-notch-memes/",
    "domain": "大厂 AI 动态",
    "title": "Jensen Huang’s alleged honeypot scandal has inspired some top-notch memes",
    "url": "https://techcrunch.com/2026/11/09/jensen-huangs-alleged-honeypot-scandal-has-inspired-some-top-notch-memes/",
    "source": "Dominic-Madori Davis, Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T04:34:15+00:00",
    "summary": "The internet is having a field day with Nvidia's Jensen Huang's alleged honeypot scandal."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/09/anthropic-reportedly-plans-to-move-forward-with-ipo-plans/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic reportedly plans to move forward with IPO plans",
    "url": "https://techcrunch.com/2026/11/09/anthropic-reportedly-plans-to-move-forward-with-ipo-plans/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T01:27:12+00:00",
    "summary": "The AI company is expected to set its valuation range this week, the Wall Street Journal reported."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/09/jensen-huang-reportedly-engaged-a-pr-firm-with-a-history-of-handling-high-profile-sex-scandals-a-year-ago/",
    "domain": "大厂 AI 动态",
    "title": "Jensen Huang reportedly engaged a PR firm with a history of handling high-profile sex scandals a year ago",
    "url": "https://techcrunch.com/2026/11/09/jensen-huang-reportedly-engaged-a-pr-firm-with-a-history-of-handling-high-profile-sex-scandals-a-year-ago/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T23:28:37+00:00",
    "summary": "The PR firm was enlisted shortly after an October 2025 New York Times report described Alice Huang's business dealings with Jensen Huang, Wired reported."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/09/hotel-giant-wyndham-exposed-customer-data-after-app-security-lapse/",
    "domain": "大厂 AI 动态",
    "title": "Hotel giant Wyndham exposed customer data after app security lapse",
    "url": "https://techcrunch.com/2026/11/09/hotel-giant-wyndham-exposed-customer-data-after-app-security-lapse/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T23:03:46+00:00",
    "summary": "Exclusive: Wyndham left a hardcoded credential in its customer app, allowing anyone to access customer data. The hotel giant wouldn't say if it has the ability to check for any past unauthorized acces"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/09/a-short-seller-flagged-nvidia-ceos-ties-to-a-suspected-chinese-spy-six-months-before-the-scandal/",
    "domain": "大厂 AI 动态",
    "title": "A short seller flagged Nvidia CEO’s ties to a suspected Chinese spy six months before the scandal",
    "url": "https://techcrunch.com/2026/11/09/a-short-seller-flagged-nvidia-ceos-ties-to-a-suspected-chinese-spy-six-months-before-the-scandal/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T22:46:09+00:00",
    "summary": "Six months before Nvidia's spy scandal erupted, Culper Research was already questioning Jensen Huang's unusually close relationship with a Chinese executive."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/09/the-race-is-on-to-sue-nvidia/",
    "domain": "大厂 AI 动态",
    "title": "The race is on to sue Nvidia",
    "url": "https://techcrunch.com/2026/11/09/the-race-is-on-to-sue-nvidia/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T22:23:42+00:00",
    "summary": "Nvidia’s stock slid more than 4% after its board opened an investigation into Jensen Huang’s relationship with a suspected Chinese spy, and one securities law expert says the company’s earlier insiste"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/09/fervo-now-has-12b-in-orders-for-its-geothermal-power-tech/",
    "domain": "大厂 AI 动态",
    "title": "Fervo now has $12B in orders for its geothermal power tech",
    "url": "https://techcrunch.com/2026/11/09/fervo-now-has-12b-in-orders-for-its-geothermal-power-tech/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T20:55:34+00:00",
    "summary": "Geothermal company Fervo is targeting natural gas as it brings down geothermal drilling costs at its 8.4 GW resource in Utah."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/09/jensen-huang-pulls-out-of-elevenlabs-summit-amid-nvidia-controversy/",
    "domain": "大厂 AI 动态",
    "title": "Jensen Huang pulls out of ElevenLabs Summit amid Nvidia controversy",
    "url": "https://techcrunch.com/2026/11/09/jensen-huang-pulls-out-of-elevenlabs-summit-amid-nvidia-controversy/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T20:09:06+00:00",
    "summary": "The Nvidia CEO also pulled out of an Anthropic event earlier."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/09/youtube-streaming-data-returns-to-billboard-charts-ending-major-disagreement/",
    "domain": "大厂 AI 动态",
    "title": "YouTube streaming data returns to Billboard charts, ending major disagreement",
    "url": "https://techcrunch.com/2026/11/09/youtube-streaming-data-returns-to-billboard-charts-ending-major-disagreement/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T19:39:41+00:00",
    "summary": "YouTube will resume sharing streaming data with Billboard in 2027 after changes to the chart formula give more weight to free, ad-supported music streams."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/09/anthropic-releases-new-mythos-and-fable-models-amid-rsi-concerns/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic releases new Mythos and Fable models amid RSI concerns",
    "url": "https://techcrunch.com/2026/11/09/anthropic-releases-new-mythos-and-fable-models-amid-rsi-concerns/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T19:24:51+00:00",
    "summary": "Anthropic says the new models \"show improvements in areas like coding, reasoning, and vision,\" as well as in communicating more clearly with users."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/09/ai-hardware-startup-nominal-triples-valuation-to-3b-in-8-months/",
    "domain": "大厂 AI 动态",
    "title": "AI hardware startup Nominal triples valuation to $3B in 8 months",
    "url": "https://techcrunch.com/2026/11/09/ai-hardware-startup-nominal-triples-valuation-to-3b-in-8-months/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T19:21:46+00:00",
    "summary": "Nominal, a startup that offers an AI platform for hardware engineering and claims Anduril as a major customer, has raised another big round of financing that triples its valuation."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/09/france-blames-iran-for-mass-hacks-targeting-freezers-in-grocery-stores-and-blood-banks/",
    "domain": "大厂 AI 动态",
    "title": "France blames Iran for mass-hacks targeting freezers in grocery stores and blood banks",
    "url": "https://techcrunch.com/2026/11/09/france-blames-iran-for-mass-hacks-targeting-freezers-in-grocery-stores-and-blood-banks/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T19:19:24+00:00",
    "summary": "France's foreign minister blamed Iran for launching at least two waves of cyberattacks targeting industrial refrigerated and freezer units across France and wider Europe."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/09/jensen-huangs-affair-with-alleged-chinese-spy-puts-nvidias-china-ambitions-under-scrutiny/",
    "domain": "大厂 AI 动态",
    "title": "Jensen Huang’s affair with alleged Chinese spy puts Nvidia’s China ambitions under scrutiny",
    "url": "https://techcrunch.com/2026/11/09/jensen-huangs-affair-with-alleged-chinese-spy-puts-nvidias-china-ambitions-under-scrutiny/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T18:09:52+00:00",
    "summary": "Jensen Huang’s alleged affair with a suspected Chinese spy threatens to complicate Nvidia’s lobbying efforts to loosen U.S. chip export restrictions and maintain access to China’s lucrative AI market."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/09/meta-releases-muse-ember-a-new-lightweight-model-for-agent-execution/",
    "domain": "大厂 AI 动态",
    "title": "Meta releases Muse Ember, a new lightweight model for agent execution",
    "url": "https://techcrunch.com/2026/11/09/meta-releases-muse-ember-a-new-lightweight-model-for-agent-execution/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T18:00:00+00:00",
    "summary": "At 10 cents per million input tokens, Ember is significantly cheaper than frontier competitors like Haiku and Luna."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/09/uber-launches-parking-service-following-spothero-acquisition-with-an-eye-on-robotaxis/",
    "domain": "大厂 AI 动态",
    "title": "Uber launches parking service following SpotHero acquisition, with an eye on robotaxis",
    "url": "https://techcrunch.com/2026/11/09/uber-launches-parking-service-following-spothero-acquisition-with-an-eye-on-robotaxis/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T17:00:00+00:00",
    "summary": "Uber Parking is the latest example of the company offering products beyond its core ride-hailing service."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/09/anthropic-joins-ais-natural-gas-frenzy-buys-3-4b-worth-of-turbines/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic joins AI’s natural gas frenzy, buys $3.4B worth of turbines",
    "url": "https://techcrunch.com/2026/11/09/anthropic-joins-ais-natural-gas-frenzy-buys-3-4b-worth-of-turbines/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T16:56:54+00:00",
    "summary": "Anthropic bought billions of dollars' worth of natural gas turbines in a deal that could give it buyer's remorse."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/09/mediums-new-tk-app-brings-ai-assistance-directly-into-the-writing-process/",
    "domain": "大厂 AI 动态",
    "title": "Medium’s new TK app brings AI assistance directly into the writing process",
    "url": "https://techcrunch.com/2026/11/09/mediums-new-tk-app-brings-ai-assistance-directly-into-the-writing-process/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T16:12:28+00:00",
    "summary": "Medium's new writing app embraces AI-assisted writing, despite growing controversy over the technology's role in publishing."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/09/meta-expands-instagrams-ai-age-guessing-tech-globally/",
    "domain": "大厂 AI 动态",
    "title": "Meta expands Instagram’s AI age-guessing tech globally",
    "url": "https://techcrunch.com/2026/11/09/meta-expands-instagrams-ai-age-guessing-tech-globally/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T15:32:27+00:00",
    "summary": "Meta says it will use its AI technology to look for clues about people it suspects to be teenagers — even if they use an adult birthday."
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
    "id": "rss:https://arstechnica.com/culture/2026/11/dcu-shake-up-james-gunn-and-peter-safran-out-post-merger/",
    "domain": "大厂 AI 动态",
    "title": "DCU shake-up: James Gunn and Peter Safran out post-merger",
    "url": "https://arstechnica.com/culture/2026/11/dcu-shake-up-james-gunn-and-peter-safran-out-post-merger/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T21:55:35+00:00",
    "summary": "Producer and former Kevin Feige protege Jeremy Latcham will replace Gunn and Safran."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/11/man-who-lost-308000-on-sports-bets-sues-kalshi-for-offering-illegal-gambling/",
    "domain": "大厂 AI 动态",
    "title": "Man who lost $308,000 on sports bets sues Kalshi for offering illegal gambling",
    "url": "https://arstechnica.com/tech-policy/2026/11/man-who-lost-308000-on-sports-bets-sues-kalshi-for-offering-illegal-gambling/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T21:13:39+00:00",
    "summary": "Lawsuit demands Kalshi return losses because online betting is illegal in Washington."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/11/a-sam-altman-parody-offers-an-amusing-lesson-in-memory-management/",
    "domain": "大厂 AI 动态",
    "title": "A Sam Altman parody offers an amusing lesson in memory management",
    "url": "https://arstechnica.com/gadgets/2026/11/a-sam-altman-parody-offers-an-amusing-lesson-in-memory-management/",
    "source": "Nick Indge",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T20:49:09+00:00",
    "summary": "We verified the RAM numbers are real without sending any emails to OpenAI."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/11/vulnerability-that-lets-hackers-ssh-into-linux-devices-is-under-active-exploitation/",
    "domain": "大厂 AI 动态",
    "title": "Vulnerability that lets hackers SSH into Linux devices is under active exploitation",
    "url": "https://arstechnica.com/security/2026/11/vulnerability-that-lets-hackers-ssh-into-linux-devices-is-under-active-exploitation/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T19:41:34+00:00",
    "summary": "\"*sshole\" poses a serious threat to Internet security."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/11/us-military-notionally-interested-in-satellite-constellation-around-moon/",
    "domain": "大厂 AI 动态",
    "title": "Pentagon mulls placing fleet of military satellites around the Moon",
    "url": "https://arstechnica.com/space/2026/11/us-military-notionally-interested-in-satellite-constellation-around-moon/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T19:08:37+00:00",
    "summary": "\"Please jump on my cislunar bandwagon because I need some more friends here.\""
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/11/claude-code-settings-files-expose-thousands-of-secrets-on-github/",
    "domain": "大厂 AI 动态",
    "title": "Claude Code is accidentally exposing secrets all over GitHub",
    "url": "https://arstechnica.com/ai/2026/11/claude-code-settings-files-expose-thousands-of-secrets-on-github/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T17:24:26+00:00",
    "summary": "\"Do not ask again\" prompt leads to passwords, API keys, and more being shared."
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
    "id": "hn:50051583",
    "domain": "股票",
    "title": "Research Firm Calls Anthropic's IPO 'Unprecedented Test of Investor Gullibity'",
    "url": "https://www.cnbc.com/2026/10/07/anthropic-will-be-most-ridiculous-ipo-of-year-analyst-says.html",
    "source": "m463",
    "platform": "hackernews",
    "points": 244,
    "published_at": "2026-10-12T05:03:47+00:00",
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
    "points": 1160,
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
    "points": 521,
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
    "points": 206,
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
    "id": "hn:50156189",
    "domain": "金融",
    "title": "The US orders every civilian agency to rip out DeepSeek, even tools built on it",
    "url": "https://madrobot.blog/2026/10/19/us-bans-deepseek-federal-agencies-dhs-order-remove-third-party/",
    "source": "jacquesm",
    "platform": "hackernews",
    "points": 66,
    "published_at": "2026-10-19T18:41:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:50328462",
    "domain": "金融",
    "title": "US Jobs Pickup May Keep Fed on Track to Hike Rates Again",
    "url": "https://www.bloomberg.com/news/articles/2026-10-31/us-jobs-pickup-may-keep-fed-on-track-to-hike-rates-again",
    "source": "frank_clover",
    "platform": "hackernews",
    "points": 36,
    "published_at": "2026-11-01T18:51:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:50202671",
    "domain": "金融",
    "title": "AI compute is the new oil–and needs a new market",
    "url": "https://www.economist.com/finance-and-economics/2026/10/22/ai-compute-is-the-new-oil-and-needs-a-new-market",
    "source": "ijidak",
    "platform": "hackernews",
    "points": 54,
    "published_at": "2026-10-22T23:45:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:50074739",
    "domain": "金融",
    "title": "Americans Trust in Federal Government Sinks to New Depths",
    "url": "https://news.gallup.com/poll/715361/trust-federal-government-sinks-new-depths.aspx",
    "source": "giuliomagnifico",
    "platform": "hackernews",
    "points": 49,
    "published_at": "2026-10-13T16:48:18+00:00",
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
    "id": "hn:50194602",
    "domain": "金融",
    "title": "Full Disk Encryption on Fedora with TPM2",
    "url": "https://www.apalrd.net/posts/2026/ent_luks/",
    "source": "speckx",
    "platform": "hackernews",
    "points": 34,
    "published_at": "2026-10-22T12:46:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:50122776",
    "domain": "金融",
    "title": "Show HN: Stoke Money – Personal finance app built around a cash flow forecast",
    "url": "https://stoke.money",
    "source": "_wesley",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-10-16T18:54:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:50236506",
    "domain": "金融",
    "title": "F45 (Fedora 45) Final Is No-Go",
    "url": "https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/EWDOYT6TOMFY4XPL5MJC2QWCDJBOR6MU/",
    "source": "gnabgib",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-10-25T22:09:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:50159683",
    "domain": "金融",
    "title": "Trump Appointees Asked a Federal Agency to Acquire a Voting Machine and Hack It",
    "url": "https://www.propublica.org/article/cisa-election-security-donald-trump",
    "source": "soundworlds",
    "platform": "hackernews",
    "points": 29,
    "published_at": "2026-10-20T00:09:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:50152041",
    "domain": "金融",
    "title": "Federal judge rules Flock violated the fourth amendment",
    "url": "https://twitter.com/scotus_wire/status/2106487374624514071",
    "source": "vessenes",
    "platform": "hackernews",
    "points": 27,
    "published_at": "2026-10-19T13:14:41+00:00",
    "summary": ""
  }
]
```
