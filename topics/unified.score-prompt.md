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

- 今日日期：`2026-11-14`
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
  "date": "2026-11-14",
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
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "8分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 2118274,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 1509114,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 1492218,
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
    "points": 1461837,
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
    "points": 913190,
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
    "points": 900477,
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
    "points": 753292,
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
    "points": 596547,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV1kr4h6fExw",
    "domain": "AI",
    "title": "DeepSeek 新出的 Super Agent 是什么？真有用么？",
    "url": "http://www.bilibili.com/video/av117564076202051",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 462448,
    "published_at": "2026-11-05T13:35:56+00:00",
    "summary": "DeepSeek Harness 团队最新开源的 Super-agent 是什么？和传统 Agent 有什么区别？它是怎么工作的？真的能提升 AI 工作的效率么？一期视频带你掌握 Super-agent 智能体，对 AI 小白、AI 编程爱好者、前端和后端程序员、AI 应用开发求职者都有帮助\n编程学习教程+实战项目+简历模板：codefather.cn\n免费 AI 编程教程：github.com/"
  },
  {
    "id": "bvid:BV13YRjBTEPb",
    "domain": "AI",
    "title": "Hermes Agent零基础、保姆级教程，小白也能轻松玩转",
    "url": "http://www.bilibili.com/video/av116503638706867",
    "source": "iwenwiki",
    "platform": "bilibili",
    "points": 433516,
    "published_at": "2026-05-02T06:51:59+00:00",
    "summary": "全B站最详细的Hermes Agent教程，从部署到玩转！零基础，小白也能轻松玩转Hermes Agent，真正的AI助手，恐怖如斯！"
  },
  {
    "id": "bvid:BV1vG8QzcE5X",
    "domain": "AI",
    "title": "Claude使用指南，claude code零基础教程，claude code安装配置到实战",
    "url": "http://www.bilibili.com/video/av114933744272468",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 358490,
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
    "points": 354880,
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
    "points": 326641,
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
    "points": 298471,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1RdLm6PEFF",
    "domain": "AI",
    "title": "ClaudeCode桌面版 = 中文汉化 + 免登录 + 接入DeekSeek + 安装自己的Skill",
    "url": "http://www.bilibili.com/video/av116606717919919",
    "source": "iwenwiki",
    "platform": "bilibili",
    "points": 288073,
    "published_at": "2026-05-20T11:45:46+00:00",
    "summary": "全B站最详细的 ClaudeCode 桌面版教程，从安装到免登录，中文汉化，接入DeepSeek，安装使用自己的Skill，ClaudeCode真正的AI编程工具，恐怖如斯！\nAgent Skills课程在这里：https://www.bilibili.com/video/BV1ugdgBQED4/?spm_id_from=333.1387.homepage.video_card.click&am"
  },
  {
    "id": "bvid:BV1h64y1v7tt",
    "domain": "AI",
    "title": "Windows Server2016网络操作系统服务器教程（已更新）",
    "url": "http://www.bilibili.com/video/av760038986",
    "source": "尚优大课堂",
    "platform": "bilibili",
    "points": 238604,
    "published_at": "2021-04-15T03:23:09+00:00",
    "summary": "本视频以Windows Server 2016操作系统为例，演示日常工作中常用的服务器相关功能的配置和管理，能够让大家直观的学习Windows服务器的操作系统各种操作，与大家同学学习提高。"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 233018,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1468g6DEWs",
    "domain": "AI",
    "title": "【全100集】(允许白嫖) 2026最全最细的AI教程零基础入门到精通，一周带你小白变大神！全程干货无废话！存下吧，少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av117115386404821",
    "source": "AI产品经理入门教程-",
    "platform": "bilibili",
    "points": 187777,
    "published_at": "2026-08-18T13:11:45+00:00",
    "summary": "【2026最新版AI教程零基础入门到精通｜配套学习路线+工具包+实战项目，看置顶评论自取】\n 本套教程专为零基础设计，从AI是什么到独立用AI解决实际问题，手把手带你系统走完从入门到精通的完整路径。 ✅ AI认知入门：什么是AI/大模型、它们能做什么不能做什么、别被营销话术忽悠\n✅ 核心技能掌握：提示词工程、多轮对话技巧、让AI稳定输出的方法论\n✅ 进阶能力突破：AI工作流搭建、智能体开发、多工具"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 186700,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1sZMq6qEko",
    "domain": "AI",
    "title": "从0做出你的第一个App ｜ 零基础AI编程保姆教程",
    "url": "http://www.bilibili.com/video/av117038647352026",
    "source": "木子不写代码",
    "platform": "bilibili",
    "points": 172148,
    "published_at": "2026-08-07T12:15:00+00:00",
    "summary": "这期视频，我会手把手带你，用 AI 做出你的第一个 App。\n全程假设你没有任何编程和AI的基础，\n我们从如何写需求提示词开始，\n到确定页面结构和设计，\n产品需求文档，\n开发计划，\n第一版APP验收，\ngit代码存档，\n二次开发，\n界面美化，\n做好的APP也会开源给到大家，\n我也会演示如何获取这个项目源代码并且用AI继续定制开发，\n视频到最后，\n你会收获一个为自己的工作和生活定制的专属APP！\n和"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 165834,
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
    "points": 161979,
    "published_at": "2025-02-18T13:13:51+00:00",
    "summary": "我试用了几十种AI编程辅助工具，找到了其中三个免费，并且效果最好的方案。 本期视频就来跟大家分享一下。视频中间会穿插很多AI编程工具的使用技巧，还有看待AI编程的一些个人思考。本期视频没有广告都是个人的经验干货，废话不多说我们直接开始。"
  },
  {
    "id": "bvid:BV1eYPpeWEnT",
    "domain": "AI",
    "title": "Cursor + MCP = 王炸！彻底颠覆我的Cursor工作流，效率直接起飞",
    "url": "http://www.bilibili.com/video/av114073660301264",
    "source": "御风大世界",
    "platform": "bilibili",
    "points": 151815,
    "published_at": "2025-02-27T03:19:03+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1VL3F6pE9K",
    "domain": "AI",
    "title": "0基础入门智能体agent测试：AI测试基础+AI智能体(Agent)测试从零入门全攻略，2026最新版！",
    "url": "http://www.bilibili.com/video/av116991151113881",
    "source": "黑马测试",
    "platform": "bilibili",
    "points": 111383,
    "published_at": "2026-07-27T09:19:37+00:00",
    "summary": "还在卷传统软件测试？2026年必学的AI智能体(Agent)测试来了！本期视频专为0基础小白打造，从软件测试基础讲起...若要本视频配套资源笔记可加up主企微（请看置顶留言最后一句话）。"
  },
  {
    "id": "bvid:BV1kGo6BdEsT",
    "domain": "AI",
    "title": "如何用Claude Skill 做高质量 PPT（附完整教程）",
    "url": "http://www.bilibili.com/video/av116474832361424",
    "source": "阿西_出海",
    "platform": "bilibili",
    "points": 104609,
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
    "points": 98118,
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
    "points": 94314,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1h3W76wEem",
    "domain": "AI",
    "title": "Claude(Code)桌面APP，保姆级全攻略，一期视频精通，顶级Agent软件长什么样？",
    "url": "http://www.bilibili.com/video/av117580048108571",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 85973,
    "published_at": "2026-11-08T09:14:07+00:00",
    "summary": "最近Claude桌面端（Claude Desktop） 有了一大波功能更新。随着一步步的迭代，它已经把 Claude Code 的编程、Claude Design 的设计，以及 Claude Cowork 的办公等核心能力，全部收入了同一个桌面客户端，特别是Claude Code已经从原本黑乎乎的命令行工具，进化成了桌面客户端的完全体形态。再搭配上超强的Opus5.5 模型，已经能称得上是地表顶级"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operit教程：入门安卓最强大ai平台operitAI",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 78511,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1XnuGzfEp7",
    "domain": "AI",
    "title": "让你手中的AI好用10倍！5个好玩实用的MCP推荐，让你不只会用AI搜索",
    "url": "http://www.bilibili.com/video/av114835262018810",
    "source": "田同学Tino",
    "platform": "bilibili",
    "points": 77892,
    "published_at": "2025-07-12T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV17Lap6VEUr",
    "domain": "AI",
    "title": "【全80集】Vibe Coding 零基础入门到实战教程，由浅入深（全程干货）",
    "url": "http://www.bilibili.com/video/av117353572468721",
    "source": "数据拾光屋",
    "platform": "bilibili",
    "points": 53052,
    "published_at": "2026-10-02T09:25:00+00:00",
    "summary": "本套教程专门为零基础学员而制，全程干货无废话，喜欢的小伙伴记得点赞三连喔 ~"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 50448,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1hxMbzqEzU",
    "domain": "AI",
    "title": "小智MCP自由了！我开源了个命令行神器实现多MCP聚合",
    "url": "http://www.bilibili.com/video/av114686414625640",
    "source": "闪电蘑菇",
    "platform": "bilibili",
    "points": 43466,
    "published_at": "2025-06-15T08:31:55+00:00",
    "summary": "- 我写的小智客户端命令行工具\n - github: https://github.com/shenjingnan/xiaozhi-client\n - gitee: https://gitee.com/shenjingnan/xiaozhi-client\n\n- 小智官方MCP示例代码仓库：\n - github: https://github.com/78/mcp-calculator\n - git"
  },
  {
    "id": "bvid:BV1XiD5BQEAj",
    "domain": "AI",
    "title": "Claude Code 接入微信、一行命令把Claude Code装进微信、保姆级教程、微信支持Claude Code（cc-connect）远程开发",
    "url": "http://www.bilibili.com/video/av116350093694897",
    "source": "下班学AI",
    "platform": "bilibili",
    "points": 41410,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 34692,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1wpxq6VEXx",
    "domain": "AI",
    "title": "【AI时代的STM32教程】AI Agent 初体验",
    "url": "http://www.bilibili.com/video/av117529699682124",
    "source": "keysking",
    "platform": "bilibili",
    "points": 33941,
    "published_at": "2026-10-30T11:52:06+00:00",
    "summary": "一句话，让 AI 帮我们完成第一个 STM32C5 程序！🚀\n本期我们一起认识 AI Agent，学习如何描述开发需求，并借助开源的 STM32C5DevSkills，让 AI 完成工程创建、芯片配置、代码编写和编译烧录，让律动小板上的小灯闪烁起来！\n也特别感谢 @意法半导体中国   对本系列教程的支持～下期我们再亲手走一遍开发流程，把 Agent 替我们完成的工作，一步步搞明白！"
  },
  {
    "id": "bvid:BV1sQaL6vEkb",
    "domain": "AI",
    "title": "小白向，ai入门第一课：agent的部署和使用！",
    "url": "http://www.bilibili.com/video/av117349378166797",
    "source": "沈三殊",
    "platform": "bilibili",
    "points": 33411,
    "published_at": "2026-09-28T15:30:36+00:00",
    "summary": "详细的agent部署介绍：https://pan.quark.cn/s/3846914c6da7\n欢迎来到ai的世界！！\n有疑问欢迎私信。"
  },
  {
    "id": "bvid:BV1cVW86JE2e",
    "domain": "AI",
    "title": "Vibe Coding 完不会获客？我用 AI 做了一个「营销数据库」！【B站AI创造公开赛】",
    "url": "http://www.bilibili.com/video/av117587245599812",
    "source": "熠辉IndieDev",
    "platform": "bilibili",
    "points": 30427,
    "published_at": "2026-11-10T01:00:00+00:00",
    "summary": "产品做出来了，第一批用户去哪找？我用两个月做了 BizPeel，收录700多个公开营收的产品，拆解真实获客动作。本期演示在 Google Antigravity 接入 BizPeel MCP，由 Gemini 4 Argon 查找同类产品、整理增长实验；报告生成时用 Gemini Flash 清洗数据，再由 Gemini 4 Argon 撰写。\n\n注： 部分Google技术仅适用于出海场景。"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29960,
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
    "points": 29060,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1uwxG6DEra",
    "domain": "AI",
    "title": "3分钟讲透：Vibe Coding如何避免💩屎山代码",
    "url": "http://www.bilibili.com/video/av117513727838880",
    "source": "鲤哥builder",
    "platform": "bilibili",
    "points": 27468,
    "published_at": "2026-10-27T16:09:19+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 26930,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22858,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1YGKJ6tEdz",
    "domain": "AI",
    "title": "Vibe Coding我的赛博女友",
    "url": "http://www.bilibili.com/video/av116933101950817",
    "source": "天工开帧",
    "platform": "bilibili",
    "points": 17270,
    "published_at": "2026-07-17T09:50:00+00:00",
    "summary": "Vibe Coding大赏之赛博女友。总体花费100个馒头左右，由于显存限制，目前实时数字人的版本没办法跑起来。目前可以24挂着，随时对话随时打断。作用嘛，除了聊天就是在我忙的时候顺手帮我查个东西。未来开发方向接入pi-agent，让它真正干活，当然，只是得上qwen27B以上得模型才有可用性。也就是说所有模型显存开销打底得36G以上。囧。当然如果不要无限制，可以接入在线模型或在线TTS，但是，我"
  },
  {
    "id": "bvid:BV1yyQEBdEkm",
    "domain": "AI",
    "title": "【2026B站最全】Claude Code+软件测试实操教程!看完我直接删了收藏夹所有测试教程,从账号注册到Plan驱动测试项目,小白3天上手！",
    "url": "http://www.bilibili.com/video/av116408092525631",
    "source": "软件测试大神",
    "platform": "bilibili",
    "points": 15577,
    "published_at": "2026-04-15T09:55:02+00:00",
    "summary": "配套资料👉：https://b23.tv/qvhxmaQ\n包括:AI测试网站，几十个AI场景测试完整流程，skil文档，测试八股文，项目源码，测试用例模板，工具安装包，学习计划表，学习路线，100g测试新人资料包等等，资料百分百免费，放心领取~"
  },
  {
    "id": "bvid:BV1rPWd6nEP4",
    "domain": "AI",
    "title": "【硬核科普】11月12日Claude新规封号潮！我研究了官方条款，总结出8个封号原因+7步自救指南",
    "url": "http://www.bilibili.com/video/av117603150337497",
    "source": "IPdodo",
    "platform": "bilibili",
    "points": 13986,
    "published_at": "2026-11-12T11:11:37+00:00",
    "summary": "Claude 11月12日新规生效，封号潮来了？\n本期视频基于官方政策原文，讲清楚： \n① 新规改了什么（三类地区/组织限制） \n② KYC验证全流程与失败处理 \n③ 8大封号原因与逐项排查方法 \n④ 被封后的申诉/数据导出/退款七步自救"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 14005,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
  },
  {
    "id": "bvid:BV1rCJdzFEQg",
    "domain": "AI",
    "title": "让AI帮你干活：WindowsMCP安装和使用！",
    "url": "http://www.bilibili.com/video/av115242814212549",
    "source": "磊哥AI实战",
    "platform": "bilibili",
    "points": 13670,
    "published_at": "2025-09-22T00:00:00+00:00",
    "summary": "AI 自动操作你的电脑，解放双手，提升工作效率。"
  },
  {
    "id": "bvid:BV1EEM96uEPP",
    "domain": "AI",
    "title": "【逆向】掌握MCP功能使用修改分析，成为逆向高手！",
    "url": "http://www.bilibili.com/video/av117030460131623",
    "source": "009安乐",
    "platform": "bilibili",
    "points": 13469,
    "published_at": "2026-08-03T07:47:28+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1Yhb66LEaF",
    "domain": "AI",
    "title": "3分钟，教你什么是vibe coding",
    "url": "http://www.bilibili.com/video/av117115000524101",
    "source": "开聊pro",
    "platform": "bilibili",
    "points": 13186,
    "published_at": "2026-08-18T06:12:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:50459703",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia is preparing to oust Jensen Huang",
    "url": "https://www.wsj.com/business/nvidia-is-preparing-to-oust-nvidia-ceo-jensen-huang-30f421ad",
    "source": "jbredeche",
    "platform": "hackernews",
    "points": 1223,
    "published_at": "2026-11-11T22:31:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:50418016",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia CEO Jensen Huang's letter to staff about affair",
    "url": "https://nvidianews.nvidia.com/news/a-message-to-our-company",
    "source": "karimf",
    "platform": "hackernews",
    "points": 987,
    "published_at": "2026-11-08T22:20:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:50477231",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia employees petition to bring back Jensen Huang",
    "url": "https://www.wired.com/story/nvidia-employees-petition-for-jensen-huangs-return/",
    "source": "lavendermon",
    "platform": "hackernews",
    "points": 801,
    "published_at": "2026-11-13T02:16:24+00:00",
    "summary": ""
  },
  {
    "id": "hn:50493251",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia allegedly engineered scarcity by funding AI startups to buy its GPUs",
    "url": "https://www.techpowerup.com/354814/nvidia-allegedly-engineered-scarcity-by-funding-ai-startups-to-buy-its-gpus",
    "source": "speckx",
    "platform": "hackernews",
    "points": 559,
    "published_at": "2026-11-14T02:52:59+00:00",
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
    "id": "hn:50473190",
    "domain": "AI 算力 / 半导体",
    "title": "Former Nvidia CEO Huang had a relationship with a second employee, sources say",
    "url": "https://www.reuters.com/technology/former-nvidia-ceo-huang-had-relationship-with-second-employee-sources-say-2026-11-12/",
    "source": "jbredeche",
    "platform": "hackernews",
    "points": 453,
    "published_at": "2026-11-12T19:51:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:50416801",
    "domain": "AI 算力 / 半导体",
    "title": "Statement from Nvidia board of directors",
    "url": "https://nvidianews.nvidia.com/news/statement-from-nvidia-board-of-directors",
    "source": "vincentchau",
    "platform": "hackernews",
    "points": 494,
    "published_at": "2026-11-08T20:26:43+00:00",
    "summary": ""
  },
  {
    "id": "hn:50467132",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang resigns as Nvidia CEO immediately",
    "url": "https://www.reuters.com/live/nvidia-live-board-meets-fate-ceo-jensen-huang-after-affair-reports-2026-11-12/",
    "source": "ksec",
    "platform": "hackernews",
    "points": 375,
    "published_at": "2026-11-12T13:56:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:50487864",
    "domain": "AI 算力 / 半导体",
    "title": "$11.4M in Nvidia hardware vanishes during shipment from CA to TX",
    "url": "https://www.freightwaves.com/news/11-4-million-in-nvidia-hardware-vanishes-during-shipment-from-california-to-texas",
    "source": "crescit_eundo",
    "platform": "hackernews",
    "points": 353,
    "published_at": "2026-11-13T18:40:44+00:00",
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
    "id": "hn:50492993",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia director sold nearly $1B in stock weeks before the Jensen Huang scandal",
    "url": "https://finance.yahoo.com/markets/stocks/articles/nvidia-director-sold-nearly-1b-160000846.html",
    "source": "LopRabbit",
    "platform": "hackernews",
    "points": 202,
    "published_at": "2026-11-14T02:21:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:50459776",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia prepares to fire CEO Jensen Huang, WSJ reports",
    "url": "https://twitter.com/watcherguru/status/2120645607866188008",
    "source": "alexmolas",
    "platform": "hackernews",
    "points": 225,
    "published_at": "2026-11-11T22:36:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:50467139",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia CEO Jensen Huang resigns after reports of second affair deepened scandal",
    "url": "https://www.bbc.co.uk/news/live/c6zjry11v8w1t",
    "source": "cognoboffin",
    "platform": "hackernews",
    "points": 168,
    "published_at": "2026-11-12T13:56:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:50479721",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC Hacked",
    "url": "https://www.sec.gov/Archives/edgar/data/1046179/000104617926000800/a20261112statementregardin.htm",
    "source": "gmays",
    "platform": "hackernews",
    "points": 115,
    "published_at": "2026-11-13T07:39:55+00:00",
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
    "id": "hn:50483391",
    "domain": "AI 算力 / 半导体",
    "title": "The Downfall of Jensen Huang: Nvidia's Greed and Corruption [video]",
    "url": "https://www.youtube.com/watch?v=YYU_geUwQoA",
    "source": "belst",
    "platform": "hackernews",
    "points": 76,
    "published_at": "2026-11-13T13:45:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:50467191",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia CEO Jensen Huang resigns after reports of extramarital relationships",
    "url": "https://www.nbcnews.com/tech/tech-news/nvidia-ceo-jensen-huang-resigns-reports-extramarital-relationships-rcna608402",
    "source": "sonabinu",
    "platform": "hackernews",
    "points": 72,
    "published_at": "2026-11-12T14:00:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:50486489",
    "domain": "AI 算力 / 半导体",
    "title": "Arm boss Rene Haas approached in Nvidia CEO search",
    "url": "https://www.ft.com/content/2a64f698-46dd-4178-a3f4-4c5f4c0a0926",
    "source": "bazzmt",
    "platform": "hackernews",
    "points": 66,
    "published_at": "2026-11-13T17:10:33+00:00",
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
    "id": "hn:50491690",
    "domain": "AI 算力 / 半导体",
    "title": "An open letter to the Nvidia Board of Directors",
    "url": "https://standwithjensen.com/",
    "source": "iLuddite",
    "platform": "hackernews",
    "points": 40,
    "published_at": "2026-11-13T23:34:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:50476257",
    "domain": "AI 算力 / 半导体",
    "title": "US Intel isn't sure if Alice Huang spied on Nvidia for China",
    "url": "https://www.cnn.com/2026/11/12/politics/alice-huang-us-intel-jensen-huang-nvidia",
    "source": "Leary",
    "platform": "hackernews",
    "points": 38,
    "published_at": "2026-11-13T00:02:34+00:00",
    "summary": ""
  },
  {
    "id": "hn:50478724",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang's Last Hours as Nvidia CEO",
    "url": "https://www.bloomberg.com/news/articles/2026-11-13/inside-jensen-huang-s-final-hours-as-the-ceo-of-nvidia",
    "source": "ex-aws-dude",
    "platform": "hackernews",
    "points": 26,
    "published_at": "2026-11-13T05:26:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:50479703",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC Has Been Hacked",
    "url": "https://mlq.ai/news/tsmc-says-employee-personal-data-was-posted-online-from-a-cloud-providers-systems/",
    "source": "pretext",
    "platform": "hackernews",
    "points": 23,
    "published_at": "2026-11-13T07:37:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:50467593",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang Resigns as Nvidia CEO After Affairs",
    "url": "https://www.nytimes.com/live/2026/11/12/business/nvidia-jensen-huang-resigns",
    "source": "speckx",
    "platform": "hackernews",
    "points": 23,
    "published_at": "2026-11-12T14:17:39+00:00",
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
    "id": "hn:50465687",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen's (Nvidia) Adventure",
    "url": "https://www.wheresyoured.at/jensens-bizarre-adventure/",
    "source": "vitorfblima",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-11-12T11:24:22+00:00",
    "summary": ""
  },
  {
    "id": "hn:50488717",
    "domain": "AI 算力 / 半导体",
    "title": "Most affairs don't matter much. Nvidia Jensen's blunder will rock the world",
    "url": "https://www.theregister.com/columnists/2026/11/13/most-affairs-dont-matter-except-to-the-people-involved-ex-nvidia-ceo-jensens-blunder-will-rock-the-world/5309649",
    "source": "CrankyBear",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-11-13T19:47:08+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/nova-scotia-bets-on-microelectronics-integration-not-chip-fabs/",
    "domain": "AI 算力 / 半导体",
    "title": "Nova Scotia Bets on Microelectronics Integration, Not Chip Fabs",
    "url": "https://www.eetimes.com/nova-scotia-bets-on-microelectronics-integration-not-chip-fabs/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T18:00:00+00:00",
    "summary": "Atlantic Canada’s coastal engineering cluster is turning specialized components and rugged hardware into exportable tools for subsea research, security, and resource markets. The post Nova Scotia Bets"
  },
  {
    "id": "rss:https://www.eetimes.com/newspace-grade-nor-flash-right-sized-reliability-for-space-missions/",
    "domain": "AI 算力 / 半导体",
    "title": "NewSpace-Grade NOR Flash: Right-Sized Reliability for Space Missions",
    "url": "https://www.eetimes.com/newspace-grade-nor-flash-right-sized-reliability-for-space-missions/",
    "source": "Infineon Technologies",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T15:00:00+00:00",
    "summary": "This paper first examines how total ionizing dose and single-event effects degrade NOR Flash. It focuses on the charge pumps, sense amplifiers, and control logic that often fail before the storage arr"
  },
  {
    "id": "rss:https://www.eetimes.com/electronica-2026-chipmakers-move-up-the-stack-as-data-centers-and-physical-ai-take-center-stage/",
    "domain": "AI 算力 / 半导体",
    "title": "electronica 2026: Chipmakers Move Up the Stack as Data Centers and Physical AI Take Center Stage",
    "url": "https://www.eetimes.com/electronica-2026-chipmakers-move-up-the-stack-as-data-centers-and-physical-ai-take-center-stage/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T14:47:27+00:00",
    "summary": "Explore how electronica 2026 shows chipmakers shifting to AI platforms as data centers, edge AI, and robotics reshape power and silicon. The post electronica 2026: Chipmakers Move Up the Stack as Data"
  },
  {
    "id": "rss:https://www.eetimes.com/how-novogenius-mcu-devices-are-reshaping-the-automotive-edge-node/",
    "domain": "AI 算力 / 半导体",
    "title": "How NovoGenius® MCU+ Devices Are Reshaping the Automotive Edge Node",
    "url": "https://www.eetimes.com/how-novogenius-mcu-devices-are-reshaping-the-automotive-edge-node/",
    "source": "Christopher McGrady",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T10:41:03+00:00",
    "summary": "NOVOSENSE NovoGenius MCU+ chips integrate analog, power, and drivers, adding intelligence to automotive edge nodes for motor control, sensing and lighting. The post How NovoGenius® MCU+ Devices Are Re"
  },
  {
    "id": "rss:https://www.eetimes.com/jensen-resigns-over-second-affair/",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Resigns Over Second Affair",
    "url": "https://www.eetimes.com/jensen-resigns-over-second-affair/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T20:48:35+00:00",
    "summary": "Nvidia CEO’s second affair scandal in a week prompted his resignation, and the board is now searching for a new leader for the company. The post Jensen Resigns Over Second Affair appeared first on EE "
  },
  {
    "id": "rss:https://www.eetimes.com/design-smarter-energy-harvesting-for-battery-free-and-low-maintenance-devices-in-safety-security-applications/",
    "domain": "AI 算力 / 半导体",
    "title": "Design Smarter – Energy Harvesting for Battery-Free and Low-Maintenance Devices in Safety & Security applications",
    "url": "https://www.eetimes.com/design-smarter-energy-harvesting-for-battery-free-and-low-maintenance-devices-in-safety-security-applications/",
    "source": "Nexperia",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T15:00:00+00:00",
    "summary": "Battery-powered sensors and detectors underpin modern safety and security systems, yet they create a constant maintenance burden. Hundreds of devices need manual battery swaps, often in hard-to-reach "
  },
  {
    "id": "rss:https://www.eetimes.com/can-machines-see-a-sick-plant-before-a-farmer-can/",
    "domain": "AI 算力 / 半导体",
    "title": "Can Machines See a Sick Plant Before a Farmer Can?",
    "url": "https://www.eetimes.com/can-machines-see-a-sick-plant-before-a-farmer-can/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T13:00:00+00:00",
    "summary": "Soybean disease research shows the promise of hyperspectral imaging, while semiconductor advances could make spectral sensing affordable for farmers. The post Can Machines See a Sick Plant Before a Fa"
  },
  {
    "id": "rss:https://www.eetimes.com/connecting-ai-to-the-physical-world/",
    "domain": "AI 算力 / 半导体",
    "title": "Connecting AI to the Physical World",
    "url": "https://www.eetimes.com/connecting-ai-to-the-physical-world/",
    "source": "Eric K. C. Tsang, CEO and founder, Vicinity Technologies Limited",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T10:20:00+00:00",
    "summary": "Why specialized wireless devices and SDR software IP matter to the next wave of intelligent machines The post Connecting AI to the Physical World appeared first on EE Times."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-board-reportedly-approached-arm-ceo-rene-haas-during-replacement-search-jensen-huangs-transgressions-leave-nvidia-scrambling-to-fill-a-massive-void",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia board reportedly approached Arm CEO Rene Haas during replacement search",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-board-reportedly-approached-arm-ceo-rene-haas-during-replacement-search-jensen-huangs-transgressions-leave-nvidia-scrambling-to-fill-a-massive-void",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T21:00:00+00:00",
    "summary": "Nvidia's board of directors reportedly approached Rene Haas, chief executive of Arm and a long-time Nvidia veteran, in CEO search."
  },
  {
    "id": "rss:https://www.tomshardware.com/gift-guides-seasonal-sales/keyboards-and-keyboard-accessories-under-usd100-budget-friendly-gifts-for-keyboard-enthusiasts",
    "domain": "AI 算力 / 半导体",
    "title": "Keyboards and keyboard accessories under $100 — budget-friendly gifts for keyboard enthusiasts",
    "url": "https://www.tomshardware.com/gift-guides-seasonal-sales/keyboards-and-keyboard-accessories-under-usd100-budget-friendly-gifts-for-keyboard-enthusiasts",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T18:25:25+00:00",
    "summary": "The best sub-$100 gifts to get the keyboard enthusiast in your life — even if they already have their end-game keyboard."
  },
  {
    "id": "rss:https://www.tomshardware.com/gift-guides-seasonal-sales/10-great-pc-upgrades-for-under-usd100-spice-up-your-setup-for-less-with-these-gifts-and-impulse-purchases",
    "domain": "AI 算力 / 半导体",
    "title": "10 great PC upgrades for under $100",
    "url": "https://www.tomshardware.com/gift-guides-seasonal-sales/10-great-pc-upgrades-for-under-usd100-spice-up-your-setup-for-less-with-these-gifts-and-impulse-purchases",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T17:00:00+00:00",
    "summary": "If you're in the market for a PC upgrade for a cheaper gift, here are 10 items under $100."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/unannounced-intel-core-ultra-7-260k-cpu-surfaces-in-newegg-prebuilt-gaming-pcs-intel-doesnt-have-official-specs-list-available-for-exclusive-arrow-lake-chip",
    "domain": "AI 算力 / 半导体",
    "title": "Unannounced Intel Core Ultra 7 260K CPU surfaces in Newegg prebuilt gaming PCs",
    "url": "https://www.tomshardware.com/pc-components/cpus/unannounced-intel-core-ultra-7-260k-cpu-surfaces-in-newegg-prebuilt-gaming-pcs-intel-doesnt-have-official-specs-list-available-for-exclusive-arrow-lake-chip",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T16:30:00+00:00",
    "summary": "The mysterious Intel Core Ultra 7 260K has surfaced in some prebuilt gaming PCs on Newegg, despite no official mention of the chip from Intel."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/malaysia-and-singapore-step-up-nvidia-ai-chip-probes-as-charges-brought-against-chinese-national-over-917-smuggled-servers-firm-at-center-of-jensen-huang-controversy-announces-inventory-audit-to-account-for-all-restricted-gpus",
    "domain": "AI 算力 / 半导体",
    "title": "Malaysia and Singapore step up Nvidia AI chip probes amidst Jensen Huang controversy",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/malaysia-and-singapore-step-up-nvidia-ai-chip-probes-as-charges-brought-against-chinese-national-over-917-smuggled-servers-firm-at-center-of-jensen-huang-controversy-announces-inventory-audit-to-account-for-all-restricted-gpus",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T16:15:28+00:00",
    "summary": "Malaysia is investigating possible re-exports of Nvidia AI hardware amid concerns about circumvention of U.S. restrictions on China as Singapore charges an executive over suspicious purchases of 917 A"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/popular-gaming-chair-and-desk-maker-secretlab-launches-dedicated-us-brick-and-mortar-locations-new-shop-in-la-spaces-in-best-buy",
    "domain": "AI 算力 / 半导体",
    "title": "Popular gaming chair and desk maker Secretlab launches dedicated US brick-and-mortar locations — new shop in LA, spaces in Best Buy",
    "url": "https://www.tomshardware.com/peripherals/popular-gaming-chair-and-desk-maker-secretlab-launches-dedicated-us-brick-and-mortar-locations-new-shop-in-la-spaces-in-best-buy",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T16:00:00+00:00",
    "summary": "Secretlab now sells its wares inside Best Buy and in a dedicated store in LA."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/broken-and-shattered-nvidia-ceo-jensen-huang-surrendered-during-resignation-meeting-report-claims-thousands-of-employees-rally-calling-for-reinstatement-on-internal-forum",
    "domain": "AI 算力 / 半导体",
    "title": "‘Broken and shattered’ Nvidia CEO Jensen Huang surrendered during resignation meeting, report claims",
    "url": "https://www.tomshardware.com/tech-industry/broken-and-shattered-nvidia-ceo-jensen-huang-surrendered-during-resignation-meeting-report-claims-thousands-of-employees-rally-calling-for-reinstatement-on-internal-forum",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T13:16:16+00:00",
    "summary": "Jensen Huang reportedly called himself 'a piece of sh--\" after his forced departure, but employees still want him back."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/japanese-workers-return-to-fax-machines-during-ongoing-microsoft-365-outage-were-going-full-analog-say-workers-forced-to-ditch-pdfs",
    "domain": "AI 算力 / 半导体",
    "title": "Japanese workers return to fax machines during ongoing Microsoft 365 outage",
    "url": "https://www.tomshardware.com/software/japanese-workers-return-to-fax-machines-during-ongoing-microsoft-365-outage-were-going-full-analog-say-workers-forced-to-ditch-pdfs",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T12:57:37+00:00",
    "summary": "Japanese workers are breaking out fax machines to deal with Microsoft's 365 outage."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/walmart-has-slashed-usd730-off-this-monster-gaming-pc-with-rtx-5070-ti-also-features-a-24-core-intel-processor-32gb-ddr5-2tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Walmart has slashed $730 off this monster gaming PC with RTX 5070 Ti",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/walmart-has-slashed-usd730-off-this-monster-gaming-pc-with-rtx-5070-ti-also-features-a-24-core-intel-processor-32gb-ddr5-2tb-ssd",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T11:30:00+00:00",
    "summary": "Save $730 on this CyberPowerPC with Intel Core Ultra 9 285 and RTX 5070 Ti."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/mass-smuggling-of-nvidia-ai-gpus-could-be-the-underlying-cause-of-jensen-huangs-departure-analysts-claim-more-than-1-5-gigawatts-of-banned-chips-tracked-to-china-despite-export-controls",
    "domain": "AI 算力 / 半导体",
    "title": "Mass smuggling of up to 1.5 million Nvidia AI GPUs could be the underlying cause of Jensen Huang's departure, analysts claim",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/mass-smuggling-of-nvidia-ai-gpus-could-be-the-underlying-cause-of-jensen-huangs-departure-analysts-claim-more-than-1-5-gigawatts-of-banned-chips-tracked-to-china-despite-export-controls",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T11:00:00+00:00",
    "summary": "Top analyst firm SemiAnalysis says it has tracked staggering 1.5 gigawatts of banned AI accelerators flowing into China."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/how-shanghai-fund-manager-kang-wei-introduced-his-wife-alice-huang-to-jensen-and-built-usd7-5-billion-nvidia-ai-gpu-smuggling-operation-mistresss-husband-joked-she-was-the-ceos-personal-assistant",
    "domain": "AI 算力 / 半导体",
    "title": "How Shanghai fund manager Kang Wei introduced his wife Alice Huang to Jensen and built $7.5 billion Nvidia AI GPU smuggling operation",
    "url": "https://www.tomshardware.com/tech-industry/how-shanghai-fund-manager-kang-wei-introduced-his-wife-alice-huang-to-jensen-and-built-usd7-5-billion-nvidia-ai-gpu-smuggling-operation-mistresss-husband-joked-she-was-the-ceos-personal-assistant",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T11:00:00+00:00",
    "summary": "While Alice Huang lives on the headlines, it was actually her husband who put her in the same room as Jensen Huang."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/controllers-gamepads/grab-this-8bitdo-wireless-controller-for-your-gaming-pc-and-switch-2-at-its-lowest-ever-price-now-usd51-12-27-percent-off-this-fully-customizable-ultimate-2-gamepad-with-tmr-joysticks-dual-triggers-and-remappable-buttons",
    "domain": "AI 算力 / 半导体",
    "title": "Grab this 8BitDo wireless controller for your gaming PC and Switch 2 at its lowest ever price, now $51.12",
    "url": "https://www.tomshardware.com/peripherals/controllers-gamepads/grab-this-8bitdo-wireless-controller-for-your-gaming-pc-and-switch-2-at-its-lowest-ever-price-now-usd51-12-27-percent-off-this-fully-customizable-ultimate-2-gamepad-with-tmr-joysticks-dual-triggers-and-remappable-buttons",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T10:53:49+00:00",
    "summary": "This 8BitDo Ultimate 2 game controller for your PC or Nintendo Switch is down to a record low price on Amazon right now."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/1994-jeep-cherokee-owner-hacks-32-year-old-car-with-claude-ai-to-pass-california-smog-tests-enthusiast-reverse-engineered-the-ancient-ecu-for-diagnostics-and-control",
    "domain": "AI 算力 / 半导体",
    "title": "1994 Jeep Cherokee owner hacks 32-year-old car with Claude AI to pass California smog tests",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/1994-jeep-cherokee-owner-hacks-32-year-old-car-with-claude-ai-to-pass-california-smog-tests-enthusiast-reverse-engineered-the-ancient-ecu-for-diagnostics-and-control",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T10:30:00+00:00",
    "summary": "An AI enthusiast managed to get his old 1994 Jeep Cherokee to pass the California smog tests thanks to the help of AI, a little electronics wiring skill, and $15 of components."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/macos/macos-on-pc-becomes-possible-again-thanks-to-apple-silicon-translator-for-x86-64-hackintosh-revival-project-currently-slow-and-not-very-stable",
    "domain": "AI 算力 / 半导体",
    "title": "macOS on PC becomes possible again thanks to Apple Silicon translator for x86-64",
    "url": "https://www.tomshardware.com/software/macos/macos-on-pc-becomes-possible-again-thanks-to-apple-silicon-translator-for-x86-64-hackintosh-revival-project-currently-slow-and-not-very-stable",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T10:00:00+00:00",
    "summary": "macOS on PCs becomes possible thanks to Apple Silicon translator for x86-64 — Hackintoshes"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/russias-google-says-nearly-3-percent-of-its-data-was-lost-after-crippling-ukraine-drone-strikes-opens-secret-availability-zones-yandex-cloud-blames-lack-of-user-backups-for-lost-data-now-forcibly-applies-backup-rules-by-default",
    "domain": "AI 算力 / 半导体",
    "title": "Russia’s Google says nearly 3% of its data was lost after crippling Ukraine drone strikes, opens secret availability zones",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/russias-google-says-nearly-3-percent-of-its-data-was-lost-after-crippling-ukraine-drone-strikes-opens-secret-availability-zones-yandex-cloud-blames-lack-of-user-backups-for-lost-data-now-forcibly-applies-backup-rules-by-default",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T21:00:00+00:00",
    "summary": "Yandex Cloud boasted that it had 'restored access to more than 97% of customer data' after Ukrainian drone attack damage."
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
    "points": 871,
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
    "points": 737,
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
    "points": 678,
    "published_at": "2026-11-10T12:11:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:50471431",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Hydrogen",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/",
    "source": "dvaplima",
    "platform": "hackernews",
    "points": 565,
    "published_at": "2026-11-12T18:01:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:50456791",
    "domain": "大厂 AI 动态",
    "title": "Gemini Decisions API",
    "url": "https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/",
    "source": "iamdelirium",
    "platform": "hackernews",
    "points": 568,
    "published_at": "2026-11-11T18:32:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:50472260",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Hydrogen and Orchestrator",
    "url": "https://antigravity.google/blog/gemini-4-hydrogen-in-google-antigravity/",
    "source": "jonbaer",
    "platform": "hackernews",
    "points": 499,
    "published_at": "2026-11-12T18:52:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:50411961",
    "domain": "大厂 AI 动态",
    "title": "Llama-modchip: 284B DeepSeek on 64GB RAM, no GPU",
    "url": "https://github.com/synchopate/llama-modchip",
    "source": "joshcsimmons",
    "platform": "hackernews",
    "points": 485,
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
    "id": "hn:50442303",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Carbon is now available",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/",
    "source": "meetpateltech",
    "platform": "hackernews",
    "points": 295,
    "published_at": "2026-11-10T16:07:15+00:00",
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
    "id": "hn:50471428",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Hydrogen",
    "url": "https://deepmind.google/models/model-cards/gemini-4-hydrogen/",
    "source": "it_works",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-11-12T18:01:37+00:00",
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
    "id": "rss:https://www.theverge.com/news/1033489/faa-ground-stop",
    "domain": "大厂 AI 动态",
    "title": "FAA lifts nationwide ground stop that blocked takeoffs for hours",
    "url": "https://www.theverge.com/news/1033489/faa-ground-stop",
    "source": "Richard Lawler",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-14T01:53:04+00:00",
    "summary": "Takeoffs from airports throughout the US largely stopped on Friday after the FAA issued a national ground stop at 3:44PM ET \"due to extraordinary circumstances and for reasons of safety.\" More than fo"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1033697/amazon-world-product-graph-ai-search",
    "domain": "大厂 AI 动态",
    "title": "Amazon has a plan to index the world’s online shopping data",
    "url": "https://www.theverge.com/tech/1033697/amazon-world-product-graph-ai-search",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T23:49:11+00:00",
    "summary": "Amazon has plans to build a vault of data on every product sold anywhere on the internet, even products Amazon doesn't sell, and make the information available through its own site, according to Reute"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1033425/openai-chatgpt-wallet",
    "domain": "大厂 AI 动态",
    "title": "ChatGPT Wallet lets OpenAI’s Dots agents make purchases for you",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1033425/openai-chatgpt-wallet",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T20:45:10+00:00",
    "summary": "After launching its Dots AI agents platform earlier this year, OpenAI is launching a wallet for the agents. ChatGPT Wallet is rolling out starting today for ChatGPT Pro subscribers in the US aged 18 a"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1033185/nothing-cmf-speaker-s-m-black-friday-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "CMF’s milk carton-shaped Bluetooth speaker is down to a new low price",
    "url": "https://www.theverge.com/gadgets/1033185/nothing-cmf-speaker-s-m-black-friday-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T20:30:00+00:00",
    "summary": "Bluetooth speakers are often boring boxes in plain colors, but not this one! As part of Nothing’s ongoing early Black Friday promo, you can grab its unique, milk carton-shaped CMF Speaker S from Amazo"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1033046/playstation-xbox-gift-card-gta-vi-6-preorder-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Here’s how you can save on your GTA VI preorder ahead of launch",
    "url": "https://www.theverge.com/gadgets/1033046/playstation-xbox-gift-card-gta-vi-6-preorder-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T19:14:38+00:00",
    "summary": "The long-awaited launch of GTA VI is around the corner, happening next Friday, November 19th. While discounts on the game itself will be rare for some time, there’s a clever workaround to save you a f"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1033159/keychron-t1-he-trackball-wireless-mouse-adjustable",
    "domain": "大厂 AI 动态",
    "title": "You can adjust the position of the trackball on Keychron’s new wireless mouse",
    "url": "https://www.theverge.com/tech/1033159/keychron-t1-he-trackball-wireless-mouse-adjustable",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T18:10:41+00:00",
    "summary": "The Nape Pro was Keychron's first trackball device that was introduced at CES 2026 with a slim and compact design allowing it to be positioned right up against a keyboard. The company's new T1 HE inst"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1033051/nvidia-jensen-huang-chips-gpu-supply-chain-climate-pollution",
    "domain": "大厂 AI 动态",
    "title": "Jensen Huang was reckless with the environment, too",
    "url": "https://www.theverge.com/tech/1033051/nvidia-jensen-huang-chips-gpu-supply-chain-climate-pollution",
    "source": "Justine Calma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T17:44:22+00:00",
    "summary": "Under cofounder Jensen Huang, Nvidia has become the engine for the AI boom - and one of the tech industry's biggest environmental liabilities. Its sought-after chips have triggered a new wave of water"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1033026/camp-snap-retro-digital-video-campcorder-cs-8-micro-keychain",
    "domain": "大厂 AI 动态",
    "title": "The smallest version of Camp Snap’s retro digital camcorder fits on your keychain",
    "url": "https://www.theverge.com/tech/1033026/camp-snap-retro-digital-video-campcorder-cs-8-micro-keychain",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T17:12:56+00:00",
    "summary": "Last week, Camp Snap launched a miniaturized version of its screen-free CS-8 video camera that was half the size of the original with a smaller grip designed to be easier for kids to hold. But it turn"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1033076/apple-tv-4k-youtube-error",
    "domain": "大厂 AI 动态",
    "title": "The new Apple TV has a YouTube problem",
    "url": "https://www.theverge.com/tech/1033076/apple-tv-4k-youtube-error",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T16:55:57+00:00",
    "summary": "People who received the brand new Apple TV 4k today saw some strange error messages as soon as they opened the YouTube app. As the first units arrived, the app was initially only showing a black scree"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1032862/microsoft-outlook-down-outage",
    "domain": "大厂 AI 动态",
    "title": "Microsoft&#8217;s massive Outlook outage might be over",
    "url": "https://www.theverge.com/tech/1032862/microsoft-outlook-down-outage",
    "source": "Jess Weatherbed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T16:17:11+00:00",
    "summary": "Service is recovering for Microsoft Outlook and 365 after an almost two-day outage impacting millions of users around the world. While some apps and features are still running in a degraded state on F"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/13/amazons-new-kindle-colorsoft-is-a-premium-e-reader-with-a-premium-price/",
    "domain": "大厂 AI 动态",
    "title": "Amazon’s new Kindle Colorsoft is a premium e-reader with a premium price",
    "url": "https://techcrunch.com/2026/11/13/amazons-new-kindle-colorsoft-is-a-premium-e-reader-with-a-premium-price/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T23:00:00+00:00",
    "summary": "The latest model is lighter and thinner than its predecessor and features an edge-to-edge display. But if you already own the first-generation Colorsoft, there’s little reason to upgrade."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/13/jensen-huangs-departure-blasts-big-hole-in-ai-startup-funding-vcs-and-founders-say/",
    "domain": "大厂 AI 动态",
    "title": "Jensen Huang’s departure blasts big hole in AI startup funding, VCs and founders say",
    "url": "https://techcrunch.com/2026/11/13/jensen-huangs-departure-blasts-big-hole-in-ai-startup-funding-vcs-and-founders-say/",
    "source": "Marina Temkin, Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T22:43:00+00:00",
    "summary": "Nvidia poured tens of billions into AI startups under Huang. Without him at the helm, founders and VCs are bracing for smaller checks and lower valuations."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/13/u-s-government-grounds-all-flights-across-the-united-states-due-to-extraordinary-cirumstances/",
    "domain": "大厂 AI 动态",
    "title": "US government grounds all flights across the United States ‘due to extraordinary circumstances’",
    "url": "https://techcrunch.com/2026/11/13/u-s-government-grounds-all-flights-across-the-united-states-due-to-extraordinary-cirumstances/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T21:44:38+00:00",
    "summary": "A spokesperson for the FAA told TechCrunch that it issued the ground stop \"following communication issues impacting multiple Air Route Traffic Control Centers,\" which manage the airspace across the Un"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/13/this-young-startup-wants-to-power-floating-data-centers-with-the-oceans-heat-and-investors-are-already-on-board/",
    "domain": "大厂 AI 动态",
    "title": "This young startup wants to power floating data centers with the ocean’s heat, and investors are already on board",
    "url": "https://techcrunch.com/2026/11/13/this-young-startup-wants-to-power-floating-data-centers-with-the-oceans-heat-and-investors-are-already-on-board/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T20:07:24+00:00",
    "summary": "Drogue is harvesting heat from the ocean to power data centers on floating vessels. The first prototype should be bobbing around the ocean, crunching bits, in less than two years."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/13/ai-agent-startup-langchain-hits-3b-valuation/",
    "domain": "大厂 AI 动态",
    "title": "AI agent startup LangChain hits $3B valuation",
    "url": "https://techcrunch.com/2026/11/13/ai-agent-startup-langchain-hits-3b-valuation/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T19:37:57+00:00",
    "summary": "LangChain now claims 7,000 customers of its model and platform agnostic agent management tool LangSmith."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/13/export-banned-nvidia-chips-are-behind-chinas-most-powerful-ai-models-uh-oh-jensen/",
    "domain": "大厂 AI 动态",
    "title": "Export-banned Nvidia chips are behind China’s most powerful AI models — uh-oh, Jensen!",
    "url": "https://techcrunch.com/2026/11/13/export-banned-nvidia-chips-are-behind-chinas-most-powerful-ai-models-uh-oh-jensen/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T18:40:30+00:00",
    "summary": "New research shows the most advanced AI models from China were trained on banned Nvidia chips."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/13/chatgpts-new-wallet-lets-ai-agents-shop-and-check-out-for-you/",
    "domain": "大厂 AI 动态",
    "title": "ChatGPT’s new Wallet lets AI agents shop and check out for you",
    "url": "https://techcrunch.com/2026/11/13/chatgpts-new-wallet-lets-ai-agents-shop-and-check-out-for-you/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T16:00:12+00:00",
    "summary": "ChatGPT Wallet lets AI agents shop and check out on users' behalf, starting with a limited rollout to U.S. Pro subscribers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/13/nvidia-ceo-jensen-huangs-affair-with-alleged-chinese-spy-a-timeline/",
    "domain": "大厂 AI 动态",
    "title": "The unfolding Jensen Huang scandal: a timeline",
    "url": "https://techcrunch.com/2026/11/13/nvidia-ceo-jensen-huangs-affair-with-alleged-chinese-spy-a-timeline/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T15:58:00+00:00",
    "summary": "Jensen Huang has resigned from Nvidia following an affair, which could have ramifications for national security as the U.S. and China race to develop the most advanced AI infrastructure."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/13/uber-confirms-hackers-stole-thousands-of-drivers-license-information-in-data-breach/",
    "domain": "大厂 AI 动态",
    "title": "Uber confirms hackers stole thousands of drivers’ license information in data breach",
    "url": "https://techcrunch.com/2026/11/13/uber-confirms-hackers-stole-thousands-of-drivers-license-information-in-data-breach/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T14:57:55+00:00",
    "summary": "The ridesharing giant said drivers' license information stored by AI cloud company Fireworks AI was stolen during a security incident."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/13/elevenlabs-new-app-combines-meeting-note-taking-and-dictation-for-teams/",
    "domain": "大厂 AI 动态",
    "title": "ElevenLabs’ new app combines meeting note-taking and dictation for teams",
    "url": "https://techcrunch.com/2026/11/13/elevenlabs-new-app-combines-meeting-note-taking-and-dictation-for-teams/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T14:44:48+00:00",
    "summary": "ElevenAI is a new meeting notetaker and dictation app aimed at teams and enterprises."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/13/microsoft-latest-email-outage-turned-into-a-full-blown-global-cloud-crisis/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft’s latest email outage turned into a full-blown global cloud crisis",
    "url": "https://techcrunch.com/2026/11/13/microsoft-latest-email-outage-turned-into-a-full-blown-global-cloud-crisis/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T13:15:20+00:00",
    "summary": "Microsoft's daylong outage began with Outlook and Teams and ended up taking much of the company's cloud services offline. Microsoft says it's gradually restoring service."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/13/israels-vcs-see-opportunity-for-challengers-in-nvidias-turmoil/",
    "domain": "大厂 AI 动态",
    "title": "Israel’s VCs see opportunity for challengers in Nvidia’s turmoil",
    "url": "https://techcrunch.com/2026/11/13/israels-vcs-see-opportunity-for-challengers-in-nvidias-turmoil/",
    "source": "Anna Heim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T12:52:19+00:00",
    "summary": "Given Nvidia’s stronghold on AI and its importance in Israel, many in the country's startup ecosystem are worried about the impact of his departure."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/13/jensen-huang-didnt-show-confidence-in-his-successor-report-says/",
    "domain": "大厂 AI 动态",
    "title": "Jensen Huang didn’t show confidence in his successor, report says",
    "url": "https://techcrunch.com/2026/11/13/jensen-huang-didnt-show-confidence-in-his-successor-report-says/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T12:28:23+00:00",
    "summary": "Huang described Kress as a \"deer in the headlights\" during a meeting in summer."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/12/democrats-launch-nvidia-investigation-write-scathing-letter-on-huangs-scheme-with-trump/",
    "domain": "大厂 AI 动态",
    "title": "Democrats launch Nvidia investigation, write scathing letter on Huang’s ‘scheme’ with Trump",
    "url": "https://techcrunch.com/2026/11/12/democrats-launch-nvidia-investigation-write-scathing-letter-on-huangs-scheme-with-trump/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T22:42:51+00:00",
    "summary": "This Congressional investigation into Nvidia's China sales and its dealings with Trump is the second one, so far, since news of the alleged spy affair broke."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/12/muse-can-now-place-calls-to-u-s-businesses-if-you-pay/",
    "domain": "大厂 AI 动态",
    "title": "Muse can now place calls to US businesses — if you pay",
    "url": "https://techcrunch.com/2026/11/12/muse-can-now-place-calls-to-u-s-businesses-if-you-pay/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T22:22:28+00:00",
    "summary": "Muse's AI can now place outbound calls to U.S. businesses — but it's not free."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/12/nebius-tests-the-neocloud-playbook-with-40-billion-in-planned-spending/",
    "domain": "大厂 AI 动态",
    "title": "Nebius tests the neocloud playbook with $40 billion in planned spending",
    "url": "https://techcrunch.com/2026/11/12/nebius-tests-the-neocloud-playbook-with-40-billion-in-planned-spending/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T21:27:10+00:00",
    "summary": "Nebius plans to fund its $40 billion AI infrastructure expansion through customer prepayments and loans, even as delays at a Microsoft data center raise questions about its financing model."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/12/jensen-huang-was-having-a-third-affair-reuters-reports/",
    "domain": "大厂 AI 动态",
    "title": "Jensen Huang was having a third affair, Reuters reports",
    "url": "https://techcrunch.com/2026/11/12/jensen-huang-was-having-a-third-affair-reuters-reports/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T20:26:47+00:00",
    "summary": "Reuters is withholding the name of the new employee linked to Huang, but says she is an employee of Nvidia."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/12/googles-latest-search-upgrade-promises-better-answers-to-your-most-complicated-questions/",
    "domain": "大厂 AI 动态",
    "title": "Google’s latest Search upgrade promises better answers to your most complicated questions",
    "url": "https://techcrunch.com/2026/11/12/googles-latest-search-upgrade-promises-better-answers-to-your-most-complicated-questions/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T19:27:45+00:00",
    "summary": "Powered by Gemini 4 Hydrogen, Google's AI Mode is getting better at understanding complex queries, surfacing relevant links, and delivering richer visual responses."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/12/nectar-launches-an-ai-agent-to-automate-creator-discovery-and-outreach-for-brands/",
    "domain": "大厂 AI 动态",
    "title": "Nectar launches an AI agent to automate creator discovery and outreach for brands",
    "url": "https://techcrunch.com/2026/11/12/nectar-launches-an-ai-agent-to-automate-creator-discovery-and-outreach-for-brands/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T19:11:00+00:00",
    "summary": "Nectar's new AI agent automates influencer marketing, helping brands discover creators, manage outreach and partnerships, and track campaign results."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/12/jensen-huangs-exit-puts-nvidias-support-for-open-source-in-question/",
    "domain": "大厂 AI 动态",
    "title": "Jensen Huang’s exit puts Nvidia’s support for open source in question",
    "url": "https://techcrunch.com/2026/11/12/jensen-huangs-exit-puts-nvidias-support-for-open-source-in-question/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T18:39:23+00:00",
    "summary": "Jensen Huang’s resignation raises questions about Nvidia’s commitment to open source AI, including its Hugging Face acquisition, open-weight models, and advocacy against restrictions, as the company n"
  },
  {
    "id": "rss:https://stratechery.com/2026/the-end-of-jensen/",
    "domain": "大厂 AI 动态",
    "title": "2026.46: The End of Jensen",
    "url": "https://stratechery.com/2026/the-end-of-jensen/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T18:00:00+00:00",
    "summary": "The best Stratechery content from the week of November 9, 2026, including the shocking demise of Jensen Huang; enterprise, consumer and Intel; and professional basketbal."
  },
  {
    "id": "rss:https://stratechery.com/2026/sharp-tech-on-video-nvidia-after-jensen-huang-ominous-news-for-american-ai-d-c-gets-its-revenge/",
    "domain": "大厂 AI 动态",
    "title": "Sharp Tech on Video: Nvidia After Jensen Huang, Ominous News for American AI, D.C. Gets Its Revenge",
    "url": "https://stratechery.com/2026/sharp-tech-on-video-nvidia-after-jensen-huang-ominous-news-for-american-ai-d-c-gets-its-revenge/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T03:47:52+00:00",
    "summary": "Sharp Tech is, for the first time, available on video. You have three ways to consume it: YouTube, Spotify, and here on Stratechery"
  },
  {
    "id": "rss:https://stratechery.com/2026/an-interview-with-roblox-ceo-david-baszucki-about-aggregating-play/",
    "domain": "大厂 AI 动态",
    "title": "An Interview With Roblox CEO David Baszucki About Aggregating Play",
    "url": "https://stratechery.com/2026/an-interview-with-roblox-ceo-david-baszucki-about-aggregating-play/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T11:00:00+00:00",
    "summary": "An interview with Roblox CEO David Baszucki about how AI is transforming game creation, and why that opens up huge opportunities to both enable developers and make Roblox both an Aggregator and a plat"
  },
  {
    "id": "hn:50307219",
    "domain": "股票",
    "title": "Anthropic may not secure investment-grade rating after IPO, Blackstone says",
    "url": "https://www.ft.com/content/59383c7f-8d82-493f-bf01-d2e862a1018f",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 327,
    "published_at": "2026-10-30T17:27:25+00:00",
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
    "id": "hn:50484110",
    "domain": "股票",
    "title": "Amodei Says AI Will Cure Cancer in a Decade. Doctors Are Skeptical",
    "url": "https://www.businessinsider.com/dario-amodei-anthropic-cancer-cure-ipo-roadshow-backlash-doctors-2026-11",
    "source": "robin_reala",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-11-13T14:34:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:50467092",
    "domain": "股票",
    "title": "Jensen Huang resigning effective immediately",
    "url": "https://www.stocktitan.net/news/NVDA/nvidia-announces-ceo-03al5m45ne1p.html",
    "source": "chrisss395",
    "platform": "hackernews",
    "points": 27,
    "published_at": "2026-11-12T13:52:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:50311311",
    "domain": "股票",
    "title": "Anthropic to receive high 'junk' rating from credit agencies following IPO",
    "url": "https://techcrunch.com/2026/10/30/anthropic-expected-to-receive-high-junk-rating-from-credit-agencies-following-ipo-report-says/",
    "source": "jnord",
    "platform": "hackernews",
    "points": 104,
    "published_at": "2026-10-30T23:08:12+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.netinterest.co/p/a-bankers-guide-to-anthropic",
    "domain": "股票",
    "title": "A Banker’s Guide to Anthropic",
    "url": "https://www.netinterest.co/p/a-bankers-guide-to-anthropic",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T18:00:43+00:00",
    "summary": "Why the IPO is a credit event"
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
    "id": "hn:50391456",
    "domain": "金融",
    "title": "Tesla to wind down Cybertruck production",
    "url": "https://www.nbcnews.com/tech/tech-news/tesla-wind-cybertruck-production-years-poor-sales-markets-rcna607817",
    "source": "PLenz",
    "platform": "hackernews",
    "points": 1164,
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
    "points": 525,
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
    "id": "hn:50414427",
    "domain": "金融",
    "title": "Tesla Hasn't Had a Successful New Product Launch Since JB Straubel Stepped Down",
    "url": "https://cleantechnica.com/2026/11/07/tesla-hasnt-had-a-successful-new-product-launch-since-jb-straubel-stepped-down-as-cto/",
    "source": "gumby",
    "platform": "hackernews",
    "points": 208,
    "published_at": "2026-11-08T16:07:42+00:00",
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
    "id": "hn:50475829",
    "domain": "金融",
    "title": "Richard Posner has died",
    "url": "https://www.law.uchicago.edu/news/senior-lecturer-richard-posner-law-and-economics-pioneer-and-former-federal-appellate-judge",
    "source": "sebg",
    "platform": "hackernews",
    "points": 52,
    "published_at": "2026-11-12T23:19:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:50492178",
    "domain": "金融",
    "title": "Tesla Opens Cybercab Orders to 'Select Customers' at $29,990 Plus $299 per Month",
    "url": "https://insideevs.com/news/815473/tesla-cybercab-pricing-sales-announced/",
    "source": "iBelieve",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-11-14T00:33:50+00:00",
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
    "id": "hn:50394130",
    "domain": "金融",
    "title": "Tesla Ends Cybertruck Production",
    "url": "https://www.heise.de/en/news/Tesla-ends-Cybertruck-production-in-Texas-11515739.html",
    "source": "Betelbuddy",
    "platform": "hackernews",
    "points": 26,
    "published_at": "2026-11-06T16:05:54+00:00",
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
    "id": "hn:50360067",
    "domain": "金融",
    "title": "Tesla allegedly misled South Korean customers about automated-driving tech",
    "url": "https://www.reuters.com/business/autos-transportation/tesla-misled-south-korean-customers-about-automated-driving-tech-consumer-group-2026-11-04/",
    "source": "EA-3167",
    "platform": "hackernews",
    "points": 29,
    "published_at": "2026-11-04T00:19:50+00:00",
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
  },
  {
    "id": "hn:50467087",
    "domain": "电子信息与芯片",
    "title": "Jensen Huang resigns",
    "url": "https://apnews.com/article/nvidia-megaspeed-china-singapore-huang-5403f152a601cf82ce939f1d24fffa0f",
    "source": "lldb",
    "platform": "hackernews",
    "points": 4024,
    "published_at": "2026-11-12T13:52:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:50459321",
    "domain": "电子信息与芯片",
    "title": "Jensen Huang said to have had relationship with executive who reports to him",
    "url": "https://www.nytimes.com/2026/11/11/technology/jensen-huang-nvidia-affair.html",
    "source": "louiereederson",
    "platform": "hackernews",
    "points": 410,
    "published_at": "2026-11-11T22:03:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:50471621",
    "domain": "电子信息与芯片",
    "title": "Singapore Says U.S. Not Helpful on Investigation into Suspected Spy's Company",
    "url": "https://www.nytimes.com/2026/11/12/business/nvidia-megaspeed-alice-huang.html",
    "source": "tedd4u",
    "platform": "hackernews",
    "points": 182,
    "published_at": "2026-11-12T18:14:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:50473868",
    "domain": "电子信息与芯片",
    "title": "Jensen Huang Third Affair Allegations Revealed",
    "url": "https://www.forbes.com/sites/alisondurkee/2026/11/12/jensen-huang-had-a-third-affair-with-another-nvidia-employee-report-says/",
    "source": "FinnLobsien",
    "platform": "hackernews",
    "points": 58,
    "published_at": "2026-11-12T20:36:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:50459679",
    "domain": "电子信息与芯片",
    "title": "Jensen Huang had a second affair – with an employee",
    "url": "https://www.cnbc.com/2026/11/11/nvidia-jensen-huang-affair-employee.html",
    "source": "justswim",
    "platform": "hackernews",
    "points": 52,
    "published_at": "2026-11-11T22:29:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:50427486",
    "domain": "电子信息与芯片",
    "title": "Commerce Dept Inquiry into Megaspeed Halted After Nvdia Intervention",
    "url": "https://www.nytimes.com/2026/11/09/business/economy/nvidia-megaspeed-investigation-huang.html",
    "source": "louiereederson",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-11-09T16:10:07+00:00",
    "summary": ""
  }
]
```
