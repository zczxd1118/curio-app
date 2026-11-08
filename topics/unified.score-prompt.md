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

- 今日日期：`2026-11-08`
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
  "date": "2026-11-08",
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
    "points": 2295004,
    "published_at": "2026-11-01T10:22:02+00:00",
    "summary": "DeepSeek Harness超详细教程！\n大家可以速速收藏啦~\n耗时60天制作！感谢大家的三联\n未来还会出其他AI教程，大家可以关注一下~"
  },
  {
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "8分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 2094289,
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
    "points": 1477083,
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
    "points": 1456125,
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
    "points": 1442656,
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
    "points": 910673,
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
    "points": 894234,
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
    "points": 746419,
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
    "points": 675419,
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
    "points": 595914,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 465828,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV13YRjBTEPb",
    "domain": "AI",
    "title": "Hermes Agent零基础、保姆级教程，小白也能轻松玩转",
    "url": "http://www.bilibili.com/video/av116503638706867",
    "source": "iwenwiki",
    "platform": "bilibili",
    "points": 431006,
    "published_at": "2026-05-02T06:51:59+00:00",
    "summary": "全B站最详细的Hermes Agent教程，从部署到玩转！零基础，小白也能轻松玩转Hermes Agent，真正的AI助手，恐怖如斯！"
  },
  {
    "id": "bvid:BV1AnQNYxEsy",
    "domain": "AI",
    "title": "MCP是啥？技术原理是什么？一个视频搞懂MCP的一切。Windows系统配置MCP，Cursor Cline使用MCP",
    "url": "http://www.bilibili.com/video/av114155298228756",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 427410,
    "published_at": "2025-03-13T13:18:09+00:00",
    "summary": "MCP是近期的AI领域的热点，特别是在海外社区获得热烈讨论，每天都有大量MCP工具诞生。本期视频我们从MCP的概念，技术原理，到多场景实战，一个视频看懂MCP的全部内容。\n\n\nMCP官方开源仓库：https://github.com/modelcontextprotocol/servers\nMCP合集网站：  https://smithery.ai/\nVscode下载：https://code.v"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 349536,
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
    "points": 322982,
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
    "points": 295521,
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
    "points": 228441,
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
    "points": 186137,
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
    "points": 165062,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV1eYPpeWEnT",
    "domain": "AI",
    "title": "Cursor + MCP = 王炸！彻底颠覆我的Cursor工作流，效率直接起飞",
    "url": "http://www.bilibili.com/video/av114073660301264",
    "source": "御风大世界",
    "platform": "bilibili",
    "points": 151773,
    "published_at": "2025-02-27T03:19:03+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1LQaN6RE3v",
    "domain": "AI",
    "title": "【 豆包Agent保姆级教程】吊打付费!  豆包彻底玩明白！只看这一期就够了！10节付费课内容全公开，零基础也能学会!",
    "url": "http://www.bilibili.com/video/av117325671961695",
    "source": "豆包Agent官方教程",
    "platform": "bilibili",
    "points": 110552,
    "published_at": "2026-09-26T09:57:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1kGo6BdEsT",
    "domain": "AI",
    "title": "如何用Claude Skill 做高质量 PPT（附完整教程）",
    "url": "http://www.bilibili.com/video/av116474832361424",
    "source": "阿西_出海",
    "platform": "bilibili",
    "points": 104269,
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
    "points": 96362,
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
    "points": 94276,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV14rxM6qEnL",
    "domain": "AI",
    "title": "最新Skills开发教程，Agent skill实战|WorkBuddy+Codex+DeepSeek Harness",
    "url": "http://www.bilibili.com/video/av117511429295044",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 85552,
    "published_at": "2026-10-28T02:00:00+00:00",
    "summary": "【课程简介】Agent Skills零基础教程，从WorkBuddy、Codex上手到项目落地实战。"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operit教程：入门安卓最强大ai平台operitAI",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 76725,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1713u6XE1D",
    "domain": "AI",
    "title": "Claude Code 完全接管了 Blender，然后创造了这个",
    "url": "http://www.bilibili.com/video/av116980883398142",
    "source": "stefan_3d_ai",
    "platform": "bilibili",
    "points": 70967,
    "published_at": "2026-07-26T11:00:00+00:00",
    "summary": "如果你给一个完全自主的 AI 代理提供对 Blender 的完整终端控制权限，并让它完完全全靠自己独立运行整整一个小时，到底会发生什么可怕的事情？\n\n在这个视频中，我远远超越了简单的代码复制粘贴，结合 Claude Code 和全新发布的官方 Blender MCP 服务器，深入探索了真正的 3D 工作流自动化究竟长什么样。\n\n---\n\n🔹 试用 Tripo AI 并免费获取 500 生成积分：h"
  },
  {
    "id": "bvid:BV1JY4w6kEAe",
    "domain": "AI",
    "title": "【全网首发】Claude防封号独家指南！前后花了5万元！小白保姆级教程【包含对话铺垫/IP DNS/订阅方式/历史记录清除】",
    "url": "http://www.bilibili.com/video/av117546107800312",
    "source": "Gemini3-",
    "platform": "bilibili",
    "points": 68489,
    "published_at": "2026-11-02T09:26:34+00:00",
    "summary": "视频内已经将所有的网站进行打码，没有吐露任何网址，也没有推广违规AI服务\n简介无推广内容\n视频中演示网站有正规ICP备案与ICP许可"
  },
  {
    "id": "bvid:BV19wXvBpEaL",
    "domain": "AI",
    "title": "认真用 Claude Code 的人，迟早会遇见 Everything Claude Code",
    "url": "http://www.bilibili.com/video/av116319122885806",
    "source": "极客魔导师",
    "platform": "bilibili",
    "points": 64109,
    "published_at": "2026-03-30T16:47:51+00:00",
    "summary": "Everything Claude Code 是目前 GitHub 上 116K star 的 Claude Code 配置项目。本期从斜杠命令、子代理、Hooks 到学习系统，带你把这个项目真正用起来。"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 56784,
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
    "points": 50235,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1EfY76YEwp",
    "domain": "AI",
    "title": "14k Star Claude Code 开源桌面端，能自动操作电脑了！",
    "url": "http://www.bilibili.com/video/av117251936293145",
    "source": "程序员阿江-Relakkes",
    "platform": "bilibili",
    "points": 49647,
    "published_at": "2026-09-11T10:30:01+00:00",
    "summary": "基于此前泄露的 Claude Code 源代码，我做了一个开源桌面端 cc-haha，并持续迭代。\n这次重构了 Computer Use 电脑操控功能：AI 能自己看屏幕、操作 APP，在 Mac 后台搭建小镇，也不占用我的鼠标键盘。\n本期从下载安装、模型配置到权限授权，带你一步步用起来。支持自选模型，不需要 Claude 账号。"
  },
  {
    "id": "bvid:BV17Lap6VEUr",
    "domain": "AI",
    "title": "【全80集】Vibe Coding 零基础入门到实战教程，由浅入深（全程干货）",
    "url": "http://www.bilibili.com/video/av117353572468721",
    "source": "数据拾光屋",
    "platform": "bilibili",
    "points": 45558,
    "published_at": "2026-10-02T09:25:00+00:00",
    "summary": "本套教程专门为零基础学员而制，全程干货无废话，喜欢的小伙伴记得点赞三连喔 ~"
  },
  {
    "id": "bvid:BV1uVSUBkEfZ",
    "domain": "AI",
    "title": "Microsoft Copilot完整教程(上) 从入门到Agent 一站式掌握AI办公",
    "url": "http://www.bilibili.com/video/av116351721084069",
    "source": "星小脉",
    "platform": "bilibili",
    "points": 43687,
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
    "points": 41273,
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
    "points": 34661,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1Nu3M6bEXE",
    "domain": "AI",
    "title": "【上海交大张倬胜】大模型系列课程从入门到精通，手把手教学，保姆级教程！涵盖预训练模型微调与部署、提示学习与思维链、模型水印、多模态大模型，比啃书效果好多了",
    "url": "http://www.bilibili.com/video/av116979859984479",
    "source": "Agent开发教程",
    "platform": "bilibili",
    "points": 33710,
    "published_at": "2026-07-25T09:34:49+00:00",
    "summary": "【上海交大张倬胜】大模型系列课程从入门到精通，手把手教学，保姆级教程！涵盖预训练模型微调与部署、提示学习与思维链、模型水印、多模态大模型，比啃书效果好多了，草履虫都能学会！"
  },
  {
    "id": "bvid:BV1sQaL6vEkb",
    "domain": "AI",
    "title": "小白向，ai入门第一课：agent的部署和使用！",
    "url": "http://www.bilibili.com/video/av117349378166797",
    "source": "沈三殊",
    "platform": "bilibili",
    "points": 32284,
    "published_at": "2026-09-28T15:30:36+00:00",
    "summary": "详细的agent部署介绍：https://pan.quark.cn/s/3846914c6da7\n欢迎来到ai的世界！！\n有疑问欢迎私信。"
  },
  {
    "id": "bvid:BV1g6fdYcEes",
    "domain": "AI",
    "title": "Cursor从小白到专家-第19课：如何用Cursor开发安卓APP？",
    "url": "http://www.bilibili.com/video/av113888322524233",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 29044,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1vwXPYkEGx",
    "domain": "AI",
    "title": "Cursor+mcp配置，手把手教你配置任意MCP服务，学不会你打我，小白保姆级教程~MCP服务配置指南 - 提升AI编程助手能力",
    "url": "http://www.bilibili.com/video/av114193181183930",
    "source": "三少科技",
    "platform": "bilibili",
    "points": 27451,
    "published_at": "2025-03-20T05:51:23+00:00",
    "summary": "我的知识星球，https://t.zsxq.com/jVAk9\n\n📌 本期教程通过实战演示，教你在Cursor中配置和使用MCP服务器，特别是filesystem MCP服务，解决Cursor无法写入文件的常见问题。\n⏱️ 内容概要：\n00:00 介绍MCP及其重要性\n02:00 Cursor抽风问题与MCP解决方案\n04:00 配置第一个MCP服务器（filesystem）\n07:00 Wind"
  },
  {
    "id": "bvid:BV1k73y6fEDx",
    "domain": "AI",
    "title": "【ClaudeCode】这绝对是b站讲的最好的Claude Code保姆级全套教程，2026最新版，包含所有干货！七天就能从小白到大神！学完即就业，玩转AI技术",
    "url": "http://www.bilibili.com/video/av117001821488596",
    "source": "爬虫逆向",
    "platform": "bilibili",
    "points": 27249,
    "published_at": "2026-07-29T07:25:00+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 26430,
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
    "points": 26113,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1G6xW6WE6W",
    "domain": "AI",
    "title": "AI 人设教程，怎么让 AI 像个人",
    "url": "http://www.bilibili.com/video/av117540185446942",
    "source": "秋秋大肥鱼",
    "platform": "bilibili",
    "points": 24179,
    "published_at": "2026-11-01T08:17:22+00:00",
    "summary": "写人设别再堆形容词了。\n\n这条讲四件事：写她怕什么、先写句子再写性格、留个会犯的错、写完先跑几天。中间还有一段翻车现场——四条全写上了，开口还是像个客服。\n\n结尾给一个能直接省时间的做法。"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22851,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1bBHm6MEG5",
    "domain": "AI",
    "title": "这绝对是b站讲的最好的Claude Code全套实战教程，手把手带你搞定国内环境安装配置，全程干货无废话！AI大模型/MCP/Skill/智能体/Agent",
    "url": "http://www.bilibili.com/video/av117402847155229",
    "source": "大模型饼饼",
    "platform": "bilibili",
    "points": 19150,
    "published_at": "2026-10-08T02:13:21+00:00",
    "summary": "这绝对是B站讲得最好的Claude Code全套实战教程！手把手带你搞定国内环境安装配置、基础操作、高阶实战技巧，课程不堆砌冗余理论，聚焦真实开发场景，带你吃透Claude Code核心能力，打通MCP、Skill与Agent智能体联动开发。不管你是想提升日常编码效率，还是入门AI智能体开发，这套教程都非常适合你，全程干货无废话！"
  },
  {
    "id": "bvid:BV1iDRQBrEF6",
    "domain": "AI",
    "title": "Claude + Blender 现在太强了 —— 完整免费设置",
    "url": "http://www.bilibili.com/video/av116543333601720",
    "source": "设计之道",
    "platform": "bilibili",
    "points": 17926,
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
    "points": 15965,
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
    "points": 15526,
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
    "points": 13774,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
  },
  {
    "id": "hn:50362905",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia RTX Spark encrypted firmware slows inference speed to 35% on Linux",
    "url": "https://www.mindstudio.ai/blog/linux-nvidia-rtx-spark-laptop",
    "source": "novaRom",
    "platform": "hackernews",
    "points": 615,
    "published_at": "2026-11-04T08:46:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:50293047",
    "domain": "AI 算力 / 半导体",
    "title": "Alleged Chinese spy had 'close relationship' with Nvidia boss Jensen Huang",
    "url": "https://nypost.com/2026/10/29/business/alleged-chinese-spy-had-close-relationship-with-nvidia-boss-jensen-huang-report/",
    "source": "mgh2",
    "platform": "hackernews",
    "points": 365,
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
    "points": 290,
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
    "id": "hn:50236073",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia and Micron Make Up 34% of America's Earnings Boom",
    "url": "https://www.wsj.com/finance/stocks/the-earnings-boom-is-heavily-reliant-on-just-a-handful-of-stocks-21decb53",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 176,
    "published_at": "2026-10-25T21:07:38+00:00",
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
    "id": "hn:50372759",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia store pulls RTX 5080 following RTX 5090 removal, prices rise to 2.2X MSRP",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-store-quietly-pulls-the-rtx-5080-following-rtx-5090-removal-street-prices-climb-to-2-2x-over-msrp",
    "source": "akyuu",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-11-04T23:12:29+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/the-countdown-to-q-day-has-begun/",
    "domain": "AI 算力 / 半导体",
    "title": "The Countdown to Q-Day Has Begun",
    "url": "https://www.eetimes.com/the-countdown-to-q-day-has-begun/",
    "source": "Rebecca Pool",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T21:00:00+00:00",
    "summary": "Will a quantum computer break blockchain cryptography in just two years' time? The post The Countdown to Q-Day Has Begun appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/cosmic-at-semicon-europa-2026-advancing-high-complexity-semiconductor-test-solutions/",
    "domain": "AI 算力 / 半导体",
    "title": "Cosmic at SEMICON Europa 2026: Advancing High-Complexity Semiconductor Test Solutions",
    "url": "https://www.eetimes.com/cosmic-at-semicon-europa-2026-advancing-high-complexity-semiconductor-test-solutions/",
    "source": "Cosmic Group",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T18:48:20+00:00",
    "summary": "ALTOPASCIO, Italy — Nov. 9, 2026 — Cosmic Group will participate in SEMICON Europa 2026 in Munich, held concurrently with electronica from Nov. 10 to 13, 2026. Cosmic will be located at booth C1255. R"
  },
  {
    "id": "rss:https://www.eetimes.com/ibm-amd-mix-quantum-and-ai-at-u-s-national-lab/",
    "domain": "AI 算力 / 半导体",
    "title": "IBM, AMD Mix Quantum and AI at U.S. National Lab",
    "url": "https://www.eetimes.com/ibm-amd-mix-quantum-and-ai-at-u-s-national-lab/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T14:10:57+00:00",
    "summary": "IBM, AMD, and Oak Ridge launch hybrid quantum-classical system to accelerate quantum-error correction research ahead of 2028. The post IBM, AMD Mix Quantum and AI at U.S. National Lab appeared first o"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/this-rtx-5060-gaming-pc-costs-less-than-the-steam-machine-grab-the-ibuypower-slate-prebuilt-pc-with-massive-usd500-discount",
    "domain": "AI 算力 / 半导体",
    "title": "This RTX 5060 gaming PC costs less than the Steam Machine — grab the iBuyPower Slate prebuilt PC with massive $500 discount",
    "url": "https://www.tomshardware.com/pc-components/this-rtx-5060-gaming-pc-costs-less-than-the-steam-machine-grab-the-ibuypower-slate-prebuilt-pc-with-massive-usd500-discount",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T21:27:30+00:00",
    "summary": "Best Buy knocks $500 off the iBUYPOWER Slate, bringing this RTX 5060-powered gaming desktop down to $899 with a Ryzen 5 processor, 16GB of DDR5 memory, and a 1TB SSD"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/this-week-in-toms-hardware-premium-november-7-2026-micron-roadmap-apples-touchscreen-ambitions-globalfoundries-interview-and-much-more",
    "domain": "AI 算力 / 半导体",
    "title": "This week in Tom's Hardware Premium: November 7, 2026",
    "url": "https://www.tomshardware.com/tech-industry/this-week-in-toms-hardware-premium-november-7-2026-micron-roadmap-apples-touchscreen-ambitions-globalfoundries-interview-and-much-more",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T15:00:00+00:00",
    "summary": "This week on Tom's Hardware Premium, we've published in-depth interviews, roadmaps, and features you won't want to miss."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/us-intelligence-believes-jensen-huang-had-romantic-relationship-with-chinese-spy-in-honeypot-operation-spy-suspect-linked-to-company-accused-of-smuggling-usd2-billion-in-ai-chips",
    "domain": "AI 算力 / 半导体",
    "title": "US intelligence believes Jensen Huang had affair with Chinese spy in honeypot operation",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/us-intelligence-believes-jensen-huang-had-romantic-relationship-with-chinese-spy-in-honeypot-operation-spy-suspect-linked-to-company-accused-of-smuggling-usd2-billion-in-ai-chips",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T14:47:37+00:00",
    "summary": "U.S. intelligence sources suggest that Nvidia chief Jensen Huang was targeted by Chinese intelligence in a 'honeypot' operation involving Megaspeed executive Alice Huang."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/grab-a-new-elegoo-3d-printer-from-as-little-as-usd159-right-now-thanks-to-black-friday-sale-now-live-early-discounts-mean-you-can-score-up-to-54-percent-off-filament-and-resin-machines-perfect-for-pro-hobbyists-and-beginners",
    "domain": "AI 算力 / 半导体",
    "title": "Grab a new Elegoo 3D printer from as little as $159 right now, thanks to Black Friday sale, now live",
    "url": "https://www.tomshardware.com/3d-printing/grab-a-new-elegoo-3d-printer-from-as-little-as-usd159-right-now-thanks-to-black-friday-sale-now-live-early-discounts-mean-you-can-score-up-to-54-percent-off-filament-and-resin-machines-perfect-for-pro-hobbyists-and-beginners",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T14:30:00+00:00",
    "summary": "Elegoo's November sale has begun, and you can score savings of up to 54% on a new printer for the entire month, as long as the stock lasts."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/teamgroup-ga-pro-2tb-ssd-review",
    "domain": "AI 算力 / 半导体",
    "title": "TeamGroup GA Pro 2TB SSD Review: A faltering attempt at a mid-range PCIe 5.0 SSD",
    "url": "https://www.tomshardware.com/pc-components/ssds/teamgroup-ga-pro-2tb-ssd-review",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T14:00:00+00:00",
    "summary": "The TeamGroup GA Pro mostly misses. Decent QD8 and steady-state writes can’t make up for weak overall performance, poor efficiency, and high temps."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/nvidias-jensen-huang-officially-called-to-congress-due-to-reports-of-a-chinese-spy-plot-officials-mention-growing-concerns-over-national-security",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's Jensen Huang officially called to Congress due to reports of a Chinese spy plot",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/nvidias-jensen-huang-officially-called-to-congress-due-to-reports-of-a-chinese-spy-plot-officials-mention-growing-concerns-over-national-security",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T13:30:00+00:00",
    "summary": "Nvidia's Jensen Huang officially called to Congress due to reports of Chinese plot — officials mention growing concerns over national security"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/tsmc-denies-exploring-3d-dram-at-nvidias-request-advanced-memory-tech-is-still-years-from-market-viability",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC denies exploring 3D DRAM at Nvidia's request",
    "url": "https://www.tomshardware.com/pc-components/dram/tsmc-denies-exploring-3d-dram-at-nvidias-request-advanced-memory-tech-is-still-years-from-market-viability",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T13:00:00+00:00",
    "summary": "Nvidia reportedly asks TSMC to produce '3D DRAM' to address memory shortages."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/enthusiast-abandons-self-hosted-microsoft-exchange-after-27-years-moving-mailboxes-to-microsoft-365-replaces-final-on-premises-relay-with-postfix-starttls-and-lets-encrypt-certificates",
    "domain": "AI 算力 / 半导体",
    "title": "Enthusiast abandons self-hosted Microsoft Exchange after 27 years, moving mailboxes to Microsoft 365",
    "url": "https://www.tomshardware.com/software/enthusiast-abandons-self-hosted-microsoft-exchange-after-27-years-moving-mailboxes-to-microsoft-365-replaces-final-on-premises-relay-with-postfix-starttls-and-lets-encrypt-certificates",
    "source": "Newton Gitonga",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T12:30:00+00:00",
    "summary": "A homelab enthusiast is retiring a Microsoft Exchange installation that began with Exchange 5.5 on Windows NT 4 in 1999. After migrating mailboxes to Microsoft 365, he kept Exchange 2019 running to re"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/wearable-tech/new-bluetooth-high-data-throughput-may-finally-satisfy-audiophiles-bluetooth-hdt-offers-a-maximum-bandwidth-of-7-5mbps-allowing-true-lossless-transmission",
    "domain": "AI 算力 / 半导体",
    "title": "New Bluetooth High Data Throughput may finally satisfy audiophiles",
    "url": "https://www.tomshardware.com/peripherals/wearable-tech/new-bluetooth-high-data-throughput-may-finally-satisfy-audiophiles-bluetooth-hdt-offers-a-maximum-bandwidth-of-7-5mbps-allowing-true-lossless-transmission",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T12:30:00+00:00",
    "summary": "Bluetooth HDT can offer a maximum bandwidth of 7.5 Mbps, allowing Bluetooth to be used with more sophisticated devices or big lossless audio files."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/ea-producer-found-20-000-archival-media-assets-in-secret-physical-vault-at-its-hq-betacam-vhs-and-d1-tapes-among-6000-assets-digitized-to-remaster-seven-classic-games",
    "domain": "AI 算力 / 半导体",
    "title": "EA producer found 20,000 archival media assets in secret physical vault at its HQ",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/ea-producer-found-20-000-archival-media-assets-in-secret-physical-vault-at-its-hq-betacam-vhs-and-d1-tapes-among-6000-assets-digitized-to-remaster-seven-classic-games",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T11:30:00+00:00",
    "summary": "The discovery of thousands of archival media assets led to the creation of Anniversary Editions of some classic titles."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/us-faa-to-eliminate-floppy-disks-from-air-traffic-control-by-2028-new-system-will-centralize-flight-alerts-restricted-airspace-schedules-and-pilot-reports",
    "domain": "AI 算力 / 半导体",
    "title": "US FAA to eliminate floppy disks from air traffic control by 2028",
    "url": "https://www.tomshardware.com/tech-industry/us-faa-to-eliminate-floppy-disks-from-air-traffic-control-by-2028-new-system-will-centralize-flight-alerts-restricted-airspace-schedules-and-pilot-reports",
    "source": "Newton Gitonga",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T11:00:00+00:00",
    "summary": "The US federal Aviation Administration (FAA) is finally moving to retire floppy disks from its air traffic control infrastructure, with plans to to replace four decades-old information systems across "
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/3d-scanning/elegoo-m1-ultra-review",
    "domain": "AI 算力 / 半导体",
    "title": "Elegoo M1 Ultra review: A good first entry into the scanner market",
    "url": "https://www.tomshardware.com/3d-printing/3d-scanning/elegoo-m1-ultra-review",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T14:00:00+00:00",
    "summary": "Elegoo’s first scanner is a useful tool, but it requires a little extra work."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/globalfoundries-vp-details-fdx-fusion-technology-sporting-7nm-class-performance-without-the-need-for-euv-tools-company-targets-2030-for-high-volume-manufacturing-with-planar-transistors-in-tow",
    "domain": "AI 算力 / 半导体",
    "title": "GlobalFoundries VP details FDX Fusion technology, sporting 7nm-class performance without the need for EUV tools — company targets 2030 for high-volume manufacturing, with planar transistors in tow",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/globalfoundries-vp-details-fdx-fusion-technology-sporting-7nm-class-performance-without-the-need-for-euv-tools-company-targets-2030-for-high-volume-manufacturing-with-planar-transistors-in-tow",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T14:00:00+00:00",
    "summary": "GlobalFoundries reveals new details about its FDX Fusion technology, which promises 7nm-class performance and 8nm-class logic density using planar FD-SOI transistors without EUV lithography, shares wh"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/protesters-storm-microsoft-ai-data-center-construction-site-amsterdam-reportedly-first-of-85-targeted-actions-across-europe",
    "domain": "AI 算力 / 半导体",
    "title": "Protesters storm Microsoft AI data center construction site",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/protesters-storm-microsoft-ai-data-center-construction-site-amsterdam-reportedly-first-of-85-targeted-actions-across-europe",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T13:59:09+00:00",
    "summary": "The protesters stormed over the walls and took over the construction site, with the Stop Dirty Data Centers coalition saying that more actions are planned across Europe."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/nvidia-tightens-tracking-of-ai-gpus-in-southeast-asia-as-chinese-chip-smuggling-draws-scrutiny-report-claims-cloud-providers-must-join-monitoring-program-to-qualify-for-official-partner-status",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia tightens tracking of AI GPUs in Southeast Asia as Chinese chip smuggling draws scrutiny, report claims",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/nvidia-tightens-tracking-of-ai-gpus-in-southeast-asia-as-chinese-chip-smuggling-draws-scrutiny-report-claims-cloud-providers-must-join-monitoring-program-to-qualify-for-official-partner-status",
    "source": "Newton Gitonga",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T13:49:33+00:00",
    "summary": "Nvidia is requiring Southeast Asian cloud providers seeking Nvidia Cloud Partner status to enroll in its Fleet Intelligence tracking program, giving the chipmaker greater visibility into where its AI "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/six-pallets-of-nvidia-gpus-worth-usd11-4-million-stolen-in-california-cargo-heist-authorities-investigate-after-truck-posing-as-a-food-transport-company-disappears",
    "domain": "AI 算力 / 半导体",
    "title": "Six pallets of Nvidia GPUs worth $11.4 million stolen in California cargo heist",
    "url": "https://www.tomshardware.com/pc-components/gpus/six-pallets-of-nvidia-gpus-worth-usd11-4-million-stolen-in-california-cargo-heist-authorities-investigate-after-truck-posing-as-a-food-transport-company-disappears",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T13:35:16+00:00",
    "summary": "The latest incident comes amid growing concerns over GPU theft, with experts warning that advanced Nvidia chips can command significantly higher prices abroad and could end up in black-market channels"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/pc-building/save-26-percent-on-this-142-piece-toolkit-for-your-pc-repairs-and-hobbyist-projects-now-under-usd28-precision-screwdriver-kit-includes-120-magnetic-bits-and-20-different-repair-tools-for-your-next-project",
    "domain": "AI 算力 / 半导体",
    "title": "Save 26% on this 142-piece toolkit for your PC repairs and hobbyist projects, now under $28",
    "url": "https://www.tomshardware.com/desktops/pc-building/save-26-percent-on-this-142-piece-toolkit-for-your-pc-repairs-and-hobbyist-projects-now-under-usd28-precision-screwdriver-kit-includes-120-magnetic-bits-and-20-different-repair-tools-for-your-next-project",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T13:00:00+00:00",
    "summary": "This 142-in-1 repair toolkit from Strebito has 120 bits and a number of other tools, and right now it's just $27.99, saving you 26% overall."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/nvidia-wants-to-repurpose-over-130-old-telco-buildings-as-tiny-data-centers-report-claims-company-in-talks-with-brightspeed-after-pitching-idea-to-parent-company-apollo-global-management",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia wants to repurpose over 130 old telco buildings as tiny data centers, report claims",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/nvidia-wants-to-repurpose-over-130-old-telco-buildings-as-tiny-data-centers-report-claims-company-in-talks-with-brightspeed-after-pitching-idea-to-parent-company-apollo-global-management",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T12:45:00+00:00",
    "summary": "Brightspeed has over 130 facilities located across the U.S., with Nvidia estimating that they could produce up to 1GW of compute capacity."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/rogue-claude-ai-tasked-with-renumbering-pages-accidentally-deletes-law-professors-entire-syllabus-one-year-of-lecture-notes-youre-right-to-be-angry-i-deleted-your-files-through-my-own-carelessness-humbled-agent-admits",
    "domain": "AI 算力 / 半导体",
    "title": "Rogue AI tasked with renumbering pages accidentally deletes law professor's entire syllabus, one year of lecture notes",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/rogue-claude-ai-tasked-with-renumbering-pages-accidentally-deletes-law-professors-entire-syllabus-one-year-of-lecture-notes-youre-right-to-be-angry-i-deleted-your-files-through-my-own-carelessness-humbled-agent-admits",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T12:12:12+00:00",
    "summary": "A University of Chicago lecturer has revealed a rogue Claude AI agent deleted his entire syllabus and year's worth of lecture notes by mistake."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/tesla-unveils-ai-accelerator-roadmap-adopts-new-si-branding-in-super-intelligence-push-si6-to-bring-80x-more-compute-performance-dojo-3-headed-to-space",
    "domain": "AI 算力 / 半导体",
    "title": "Tesla unveils AI accelerator roadmap, adopts new 'SI' branding in 'Super Intelligence' push",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/tesla-unveils-ai-accelerator-roadmap-adopts-new-si-branding-in-super-intelligence-push-si6-to-bring-80x-more-compute-performance-dojo-3-headed-to-space",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T12:00:00+00:00",
    "summary": "Tesla is ramping up its custom silicon ambitions with training-oriented Dojo D3 that can eventually go to orbital data centers and massive SI6 inference accelerator."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/chipsets/intels-next-gen-nova-lake-needs-new-motherboards-what-we-expect-from-nova-point-and-z990-z970-and-b960-chipsets",
    "domain": "AI 算力 / 半导体",
    "title": "Intel’s next-gen Nova Lake needs new motherboards — what we expect from Nova Point and Z990, Z970, and B960 chipsets",
    "url": "https://www.tomshardware.com/pc-components/chipsets/intels-next-gen-nova-lake-needs-new-motherboards-what-we-expect-from-nova-point-and-z990-z970-and-b960-chipsets",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T12:00:00+00:00",
    "summary": "New Intel CPUs mean a new LGA 1954 socket and new motherboards. Here’s what we know about Nova Point’s Z990, Z970, and B960 chipsets, including more PCIe 5.0, Thunderbolt 5, faster base RAM speeds, an"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/score-a-huge-usd600-saving-on-this-rtx-5070-ti-gaming-laptop-from-hp-now-under-usd2-100-hyperx-omen-max-16-machine-is-fully-customizable-base-model-ships-with-16gb-ddr5-and-a-512gb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Score a huge $600 saving on this RTX 5070 Ti gaming laptop from HP, now under $2,100",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/score-a-huge-usd600-saving-on-this-rtx-5070-ti-gaming-laptop-from-hp-now-under-usd2-100-hyperx-omen-max-16-machine-is-fully-customizable-base-model-ships-with-16gb-ddr5-and-a-512gb-ssd",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T11:44:37+00:00",
    "summary": "Save $600 on this customizable RTX 5070 Ti HP Omen Max 16 gaming laptop with 16GB DDR5, 512GB SSD, and a 16-inch display."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/nintendo/nintendos-latest-zelda-remake-already-circulating-online-as-a-switch-2-rom-openai-assisted-software-jailbreak-new-game-dumper-let-pirates-share-game-for-free-immediately-following-release",
    "domain": "AI 算力 / 半导体",
    "title": "Nintendo’s latest Zelda remake already circulating online as a Switch 2 ROM",
    "url": "https://www.tomshardware.com/video-games/nintendo/nintendos-latest-zelda-remake-already-circulating-online-as-a-switch-2-rom-openai-assisted-software-jailbreak-new-game-dumper-let-pirates-share-game-for-free-immediately-following-release",
    "source": "Newton Gitonga",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T11:00:00+00:00",
    "summary": "The Legend of Zelda: Ocarina of Time has reportedly been dumped on its Switch 2 launch day, with its original release and a 23GB update already circulating online."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/gelsinger-backed-nagare-labs-capacitorless-z2ram-promises-sram-speed-with-dram-density-latest-published-cell-retains-data-for-over-300-seconds-at-85-c-but-further-figures-are-projected",
    "domain": "AI 算力 / 半导体",
    "title": "Gelsinger-backed Nagare Labs’ Z2RAM promises SRAM speed at DRAM density",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/gelsinger-backed-nagare-labs-capacitorless-z2ram-promises-sram-speed-with-dram-density-latest-published-cell-retains-data-for-over-300-seconds-at-85-c-but-further-figures-are-projected",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T11:00:00+00:00",
    "summary": "Georgia Tech spinout Nagare Labs, backed by Playground Global, unveils Z2RAM, a capacitorless memory to stack on AI accelerators."
  },
  {
    "id": "rss:https://www.eetimes.com/europe-chip-industry-perfect-storm-or-perfect-timing/",
    "domain": "AI 算力 / 半导体",
    "title": "Europe’s Chip Industry: Perfect Storm or Perfect Timing?",
    "url": "https://www.eetimes.com/europe-chip-industry-perfect-storm-or-perfect-timing/",
    "source": "Anne-Françoise Pelé",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T09:53:05+00:00",
    "summary": "At SEMICON Europa 2026, Europe’s chip industry will confront a “perfect storm” of geopolitical, technological, and competitive pressures. The post Europe’s Chip Industry: Perfect Storm or Perfect Timi"
  },
  {
    "id": "rss:https://www.eetimes.com/ee-times-magazine-november-2026/",
    "domain": "AI 算力 / 半导体",
    "title": "EE Times Magazine – November 2026",
    "url": "https://www.eetimes.com/ee-times-magazine-november-2026/",
    "source": "Anne-Françoise Pelé",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T22:30:00+00:00",
    "summary": "This edition of EE Times Magazine explores advances in semiconductor manufacturing and packaging, farm autonomy, and Canada’s efforts to commercialize emerging technologies. The post EE Times Magazine"
  },
  {
    "id": "rss:https://www.eetimes.com/infineon-leaders-andreas-urschitz-and-maher-matta-on-a-decade-of-oktobertech/",
    "domain": "AI 算力 / 半导体",
    "title": "Infineon Leaders Andreas Urschitz and Maher Matta on a Decade of OktoberTech",
    "url": "https://www.eetimes.com/infineon-leaders-andreas-urschitz-and-maher-matta-on-a-decade-of-oktobertech/",
    "source": "EE Times",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T19:30:52+00:00",
    "summary": "Sponsored: Infineon’s Andreas Urschitz and Maher Matta talk to EE Times at OktoberTech Silicon Valley 2026, looking back on a decade of innovation and growth. The post Infineon Leaders Andreas Urschit"
  },
  {
    "id": "rss:https://www.eetimes.com/infineons-johannes-schoiswohl-on-the-gan-market-at-oktobertech/",
    "domain": "AI 算力 / 半导体",
    "title": "Infineon’s Johannes Schoiswohl on the GaN Market at OktoberTech",
    "url": "https://www.eetimes.com/infineons-johannes-schoiswohl-on-the-gan-market-at-oktobertech/",
    "source": "EE Times",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T19:15:17+00:00",
    "summary": "Sponsored: PEN’s Aalyia Shaukat talks to Infineon’s Johannes Schoiswohl about the GaN market at OktoberTech Silicon Valley 2026, the event’s 10th anniversary. The post Infineon’s Johannes Schoiswohl o"
  },
  {
    "id": "rss:https://www.eetimes.com/infineons-steve-tateosian-talks-iot-consumer-and-industrial-mcus-at-oktobertech/",
    "domain": "AI 算力 / 半导体",
    "title": "Infineon’s Steve Tateosian Talks IoT, Consumer, and Industrial MCUs at OktoberTech",
    "url": "https://www.eetimes.com/infineons-steve-tateosian-talks-iot-consumer-and-industrial-mcus-at-oktobertech/",
    "source": "EE Times",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T18:59:48+00:00",
    "summary": "Sponsored: EDN's Majeed Ahmad talks to Infineon's Steve Tateosian on edge systems, application examples, and the growth of the market. The post Infineon’s Steve Tateosian Talks IoT, Consumer, and Indu"
  },
  {
    "id": "rss:https://www.eetimes.com/from-pytorch-to-product-accelerating-edge-ai-through-open-ecosystems/",
    "domain": "AI 算力 / 半导体",
    "title": "From PyTorch to Product: Accelerating Edge AI Through Open Ecosystems",
    "url": "https://www.eetimes.com/from-pytorch-to-product-accelerating-edge-ai-through-open-ecosystems/",
    "source": "Renesas",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T18:12:42+00:00",
    "summary": "In this 30-Minute BitCast, discover how open-source technologies are helping developers accelerate AI deployment on resource-constrained embedded devices. The post From PyTorch to Product: Acceleratin"
  },
  {
    "id": "rss:https://www.eetimes.com/accelerate-analog-design-with-flexible-ai-native-workflows/",
    "domain": "AI 算力 / 半导体",
    "title": "Accelerate Analog Design with Flexible, AI-Native Workflows",
    "url": "https://www.eetimes.com/accelerate-analog-design-with-flexible-ai-native-workflows/",
    "source": "ChipsAgents",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T17:40:24+00:00",
    "summary": "Join this webinar to learn how ChipAgents’ IC-star chip neural engine automates analog design, simulation, and verification in one unified, flexible agentic loop. The post Accelerate Analog Design wit"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/handheld-gaming/grab-a-nintendo-switch-2-controller-upgrade-from-usd49-just-in-time-for-zelda-ocarina-of-times-remaster-secure-the-tools-to-defeat-ganondorf-with-these-top-wireless-gamepads-from-8bitdo-gamesir-and-others",
    "domain": "AI 算力 / 半导体",
    "title": "Grab a Nintendo Switch 2 controller upgrade from $49, just in time for Zelda: Ocarina of Time's remaster",
    "url": "https://www.tomshardware.com/video-games/handheld-gaming/grab-a-nintendo-switch-2-controller-upgrade-from-usd49-just-in-time-for-zelda-ocarina-of-times-remaster-secure-the-tools-to-defeat-ganondorf-with-these-top-wireless-gamepads-from-8bitdo-gamesir-and-others",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T21:00:00+00:00",
    "summary": "A selection of the best Switch 2 controllers for getting your best Zelda game on."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/combined-flaws-let-anyone-into-alpine-linux-and-other-distros-by-typing-anything-over-256-characters-as-a-password-emergency-fixes-for-openssh-and-musl-libc-issued-for-millions-of-systems-patch-immediately",
    "domain": "AI 算力 / 半导体",
    "title": "Combined OpenSSH and musl-libc flaws let anyone into Alpine Linux and other distros by typing anything over 256 characters as a password",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/combined-flaws-let-anyone-into-alpine-linux-and-other-distros-by-typing-anything-over-256-characters-as-a-password-emergency-fixes-for-openssh-and-musl-libc-issued-for-millions-of-systems-patch-immediately",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T18:14:56+00:00",
    "summary": "Combined OpenSSH and musl-libc flaws let anyone into Alpine Linux and other distros by typing anything over 256 characters as a password"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/india-targets-creating-homegrown-gpus-within-2-years-and-plans-to-commercialize-indigenous-shakti-and-vega-risc-v-processors-sees-ai-boom-as-a-potential-repeat-of-the-y2k-opportunity-for-its-it-industry",
    "domain": "AI 算力 / 半导体",
    "title": "India targets creating homegrown GPUs within 2 years and plans to commercialize indigenous SHAKTI and VEGA processors",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/india-targets-creating-homegrown-gpus-within-2-years-and-plans-to-commercialize-indigenous-shakti-and-vega-risc-v-processors-sees-ai-boom-as-a-potential-repeat-of-the-y2k-opportunity-for-its-it-industry",
    "source": "Newton Gitonga",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T18:00:00+00:00",
    "summary": "MeitY Secretary S. Krishnan says India plans to develop its own GPU under Semiconductor Mission 2.0, with a target of approximately two years. The country is also looking to commercialize its SHAKTI a"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/policy/chinese-ai-lab-moonshot-reportedly-looked-at-european-data-centers-to-access-nvidia-chips-report-claims-kimi-maker-primarily-interested-in-inferencing-capacity-but-also-asked-about-training-clusters",
    "domain": "AI 算力 / 半导体",
    "title": "Chinese AI lab Moonshot reportedly looked at European data centers to access Nvidia chips, report claims",
    "url": "https://www.tomshardware.com/tech-industry/policy/chinese-ai-lab-moonshot-reportedly-looked-at-european-data-centers-to-access-nvidia-chips-report-claims-kimi-maker-primarily-interested-in-inferencing-capacity-but-also-asked-about-training-clusters",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T16:48:30+00:00",
    "summary": "The lab is reportedly interested in renting at least 8,000 Nvidia Blackwell GPUs."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/nintendo/nintendo-switch-2-sales-dropped-by-41-percent-from-last-year-due-to-consoles-price-increase-pressure-to-release-more-big-games-to-make-up-for-shortfall",
    "domain": "AI 算力 / 半导体",
    "title": "Nintendo Switch 2 sales dropped by 41% from last year due to console's price increase",
    "url": "https://www.tomshardware.com/video-games/nintendo/nintendo-switch-2-sales-dropped-by-41-percent-from-last-year-due-to-consoles-price-increase-pressure-to-release-more-big-games-to-make-up-for-shortfall",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T16:27:28+00:00",
    "summary": "Nintendo's Switch 2 sales decreased by 41% compared to the same time frame last year due to an increase in the console's price. Investors are pressuring Nintendo to release more big games to attract m"
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/portable-monitors/uperfect-gr14bu-portable-monitor-review",
    "domain": "AI 算力 / 半导体",
    "title": "UPERFECT GR14BU portable monitor review: A 120 Hz 3K OLED touch display at a killer price",
    "url": "https://www.tomshardware.com/monitors/portable-monitors/uperfect-gr14bu-portable-monitor-review",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T15:00:00+00:00",
    "summary": "With a 3K OLED panel and a 120 Hz refresh rate, the GR14BU comes out swinging."
  },
  {
    "id": "hn:50247677",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia discusses $2k-per-GPU annual fee for software",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-discusses-usd2-000-per-gpu-annual-software-fee-for-running-agents-on-ai-infrastructure-firm-already-charges-more-than-twice-that-amount-for-its-ai-enterprise-software-platform",
    "source": "gscott",
    "platform": "hackernews",
    "points": 41,
    "published_at": "2026-10-26T17:34:45+00:00",
    "summary": ""
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
    "points": 727,
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
    "points": 730,
    "published_at": "2026-11-04T10:10:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:50392118",
    "domain": "大厂 AI 动态",
    "title": "Gemini Omni 1.2 Flash",
    "url": "https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/",
    "source": "thisisauserid",
    "platform": "hackernews",
    "points": 362,
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
    "id": "rss:https://www.theverge.com/tech/1023230/the90-gem-necklace-hands-on-impressions",
    "domain": "大厂 AI 动态",
    "title": "The UV-tracking Gem made me rethink how sunlight affects my health, not just my appearance",
    "url": "https://www.theverge.com/tech/1023230/the90-gem-necklace-hands-on-impressions",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T17:00:00+00:00",
    "summary": "With temperatures rising to the 90s in Los Angeles, avoiding the heat wasn't exactly an option while I was at a relative's outdoor party in August. So I sat beneath a patio umbrella with a powerful fa"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1028917/legend-of-zelda-ocarina-of-time-remake-switch-2-costco-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Costco members can get $5 off the reimagined Ocarina of Time",
    "url": "https://www.theverge.com/gadgets/1028917/legend-of-zelda-ocarina-of-time-remake-switch-2-costco-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T16:00:00+00:00",
    "summary": "While some retailers were offering preorder discounts on the remastered Legend of Zelda: The Ocarina of Time, it’s not too late to save if you missed out. Costco members can currently get $5 off the d"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1029474/discogs-kevin-lewandowski-aeropress-interview",
    "domain": "大厂 AI 动态",
    "title": "Discogs’ Kevin Lewandowski can’t live without his AeroPress",
    "url": "https://www.theverge.com/tech/1029474/discogs-kevin-lewandowski-aeropress-interview",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T16:00:00+00:00",
    "summary": "Twenty-five years ago, Kevin Lewandowski founded Discogs, arguably the destination online for obsessive vinyl collectors and music nerds of all stripes. It is a marketplace for buying and selling reco"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1029489/nyt-cooking-ai-assistant-review",
    "domain": "大厂 AI 动态",
    "title": "NYT Cooking’s AI assistant saved my weeknight chicken, but almost ruined my cake",
    "url": "https://www.theverge.com/tech/1029489/nyt-cooking-ai-assistant-review",
    "source": "Jennifer Pattison Tuohy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T15:50:00+00:00",
    "summary": "Around 7PM each weeknight, I find myself standing in front of the fridge, trying to decide on something for dinner that won't make my husband complain, \"Chicken again?\" Yes, I should meal plan more, b"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1029483/nvidia-ai-chips-china-blacklist-government",
    "domain": "大厂 AI 动态",
    "title": "The US let Nvidia sell chips to an empty office in China",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1029483/nvidia-ai-chips-china-blacklist-government",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T15:43:45+00:00",
    "summary": "Concerns are being raised that neither the Commerce Department nor Nvidia are doing their due diligence when it comes to vetting Chinese firms cleared to handle the company's H200 AI chips. According "
  },
  {
    "id": "rss:https://www.theverge.com/podcast/1029038/ai-cybersecurity-hackers-data-breach-dark-age-alex-stamos",
    "domain": "大厂 AI 动态",
    "title": "AI broke the cybersecurity world. What’s next?",
    "url": "https://www.theverge.com/podcast/1029038/ai-cybersecurity-hackers-data-breach-dark-age-alex-stamos",
    "source": "Nilay Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T15:00:00+00:00",
    "summary": "Today, I’m talking with Alex Stamos, chief security officer at Cognition and longtime cybersecurity expert, about what a mess cybersecurity is right now. This episode is part one of a special series l"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/1029460/elon-musk-cybertruck-death-election-backlash",
    "domain": "大厂 AI 动态",
    "title": "Good riddance, Cybertruck!",
    "url": "https://www.theverge.com/transportation/1029460/elon-musk-cybertruck-death-election-backlash",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T14:40:06+00:00",
    "summary": "I'm calling it: time of death, November 6th, 1:30 AM, by tweet. Elon Musk's declaration Friday that Tesla would be \"winding down\" production of the Cybertruck next year to make room for the Cybercab w"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1028930/zelda-ocarina-godzilla-minus-zero-affinity-installer",
    "domain": "大厂 AI 动态",
    "title": "Zelda is back and better than ever",
    "url": "https://www.theverge.com/tech/1028930/zelda-ocarina-godzilla-minus-zero-affinity-installer",
    "source": "David Pierce",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T13:49:01+00:00",
    "summary": "Hi, friends! Welcome to Installer No. 151, your guide to the best and Verge-iest stuff in the world. (If you're new here, welcome, get psyched because it's officially Bad Holiday Movie Season, and als"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1029126/anthropic-metr-report-accelerating-ai-development",
    "domain": "大厂 AI 动态",
    "title": "Why a new report on Anthropic automating AI development is alarming researchers",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1029126/anthropic-metr-report-accelerating-ai-development",
    "source": "Robert Hart",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T12:30:00+00:00",
    "summary": "Anthropic is using AI to build more powerful AI. And it appears to be working remarkably well, with the company's models improving roughly twice as quickly as a year ago, with little indication of slo"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1029380/openai-1-25-trillion-investment-valuation",
    "domain": "大厂 AI 动态",
    "title": "OpenAI valued at $1.25 trillion, as rival Anthropic nears its IPO",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1029380/openai-1-25-trillion-investment-valuation",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T23:46:18+00:00",
    "summary": "OpenAI is now valued at $1.25 trillion in a new round of funding that has raised another $11 billion, according to Bloomberg. That would make it one of the world's most valuable companies, not long af"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/07/after-the-midterms-things-are-looking-rocky-for-elon-musk-and-data-centers/",
    "domain": "大厂 AI 动态",
    "title": "After the midterms, things are looking rocky for Elon Musk and data centers",
    "url": "https://techcrunch.com/2026/11/07/after-the-midterms-things-are-looking-rocky-for-elon-musk-and-data-centers/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T22:07:22+00:00",
    "summary": "On Equity, we unpacked what the midterms mean for the tech industry."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/07/chinese-exec-was-recruited-to-spy-on-nvidia-ceo-according-to-us-intelligence-memo/",
    "domain": "大厂 AI 动态",
    "title": "Megaspeed exec was recruited to spy on Nvidia CEO, according to US intelligence memo",
    "url": "https://techcrunch.com/2026/11/07/chinese-exec-was-recruited-to-spy-on-nvidia-ceo-according-to-us-intelligence-memo/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T21:17:08+00:00",
    "summary": "A memo circulated earlier this year reportedly claimed that China’s Ministry of State Security recruited a female technology executive to spy on Nvidia's CEO."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/07/parents-want-safer-phones-for-kids-these-companies-are-answering-the-call/",
    "domain": "大厂 AI 动态",
    "title": "Parents want safer phones for kids. These companies are answering the call.",
    "url": "https://techcrunch.com/2026/11/07/parents-want-safer-phones-for-kids-these-companies-are-answering-the-call/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T19:00:00+00:00",
    "summary": "As parents look for alternatives to unrestricted smartphones, a growing number of companies are building phones designed specifically for kids, from feature-limited mobile devices to minimalist home p"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/07/binance-cfo-is-leaving-to-pursue-a-new-venture-after-6-3-billion-hack/",
    "domain": "大厂 AI 动态",
    "title": "Binance CFO is leaving to ‘pursue a new venture’ after $6.3 billion hack",
    "url": "https://techcrunch.com/2026/11/07/binance-cfo-is-leaving-to-pursue-a-new-venture-after-6-3-billion-hack/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T17:24:07+00:00",
    "summary": "The announcement comes barely more than a week after hackers stole $6.3 billion worth of cryptocurrency from Binance users."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/07/amazons-new-basic-kindle-proves-you-dont-need-all-the-bells-and-whistles/",
    "domain": "大厂 AI 动态",
    "title": "Amazon’s new basic Kindle proves you don’t need all the bells and whistles",
    "url": "https://techcrunch.com/2026/11/07/amazons-new-basic-kindle-proves-you-dont-need-all-the-bells-and-whistles/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T17:18:00+00:00",
    "summary": "Amazon's redesigned basic Kindle costs more than before, but its lighter build and improved display make a compelling case for skipping the pricier models."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/06/sequoia-shutting-down-its-scouts-program-marks-the-end-of-an-era/",
    "domain": "大厂 AI 动态",
    "title": "Sequoia shutting down its Scouts program marks the end of an era",
    "url": "https://techcrunch.com/2026/11/06/sequoia-shutting-down-its-scouts-program-marks-the-end-of-an-era/",
    "source": "Anna Heim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T05:01:54+00:00",
    "summary": "Sequoia pioneered the scouts model and many VC firms followed suit, but a consensus now seems to be forming that the model has reached limits in its current form."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/06/from-the-front-row-to-the-hot-seat-what-the-midterms-mean-for-big-tech/",
    "domain": "大厂 AI 动态",
    "title": "From the front row to the hot seat — what the midterms mean for Big Tech",
    "url": "https://techcrunch.com/2026/11/06/from-the-front-row-to-the-hot-seat-what-the-midterms-mean-for-big-tech/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T04:16:43+00:00",
    "summary": "After spending two years getting cozy with the White House, Big Tech is suddenly trying to make friends with Democrats, and the open question is whether that image makeover can hold up against what st"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/06/crusoe-sells-troubled-wyoming-data-center-project-to-google/",
    "domain": "大厂 AI 动态",
    "title": "Crusoe sells troubled Wyoming data center project to Google",
    "url": "https://techcrunch.com/2026/11/06/crusoe-sells-troubled-wyoming-data-center-project-to-google/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T01:40:28+00:00",
    "summary": "The deal highlights the challenges of developing massive AI data centers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/06/openai-reportedly-raises-an-additional-11-billion-at-a-1-25-trillion-valuation/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI reportedly raises an additional $11 billion at a $1.25 trillion valuation",
    "url": "https://techcrunch.com/2026/11/06/openai-reportedly-raises-an-additional-11-billion-at-a-1-25-trillion-valuation/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T22:53:46+00:00",
    "summary": "OpenAI has reportedly raised an additional $11 billion as part of a funding round that hasn't closed yet but is expected to in the coming weeks."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/06/the-duo-apps-are-coming-says-apple/",
    "domain": "大厂 AI 动态",
    "title": "The Duo apps are coming, says Apple",
    "url": "https://techcrunch.com/2026/11/06/the-duo-apps-are-coming-says-apple/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T21:38:05+00:00",
    "summary": "There are now 100,000 Duo-optimized apps, says Apple, and thousands more arrive daily."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/06/hundreds-of-artex-ai-hacking-tools-found-publicly-exposed-to-the-web/",
    "domain": "大厂 AI 动态",
    "title": "Hundreds of Artex AI hacking tools found publicly exposed to the web",
    "url": "https://techcrunch.com/2026/11/06/hundreds-of-artex-ai-hacking-tools-found-publicly-exposed-to-the-web/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T18:44:38+00:00",
    "summary": "Security researchers found hundreds of servers hosting the penetration testing tool Artex exposed to the internet, allowing anyone access to the hacking tool."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/06/meta-introduces-spaces-a-new-way-to-collaborate-with-your-muse-agent/",
    "domain": "大厂 AI 动态",
    "title": "Meta introduces Spaces, a new way to collaborate with your Muse agent",
    "url": "https://techcrunch.com/2026/11/06/meta-introduces-spaces-a-new-way-to-collaborate-with-your-muse-agent/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T18:44:20+00:00",
    "summary": "Meta's Muse agents continue to get new features and integrations. Spaces promises to be a new way to interact with the AI helpers."
  },
  {
    "id": "rss:https://techcrunch.com/video/after-the-midterms-is-the-ai-industry-in-for-a-rough-two-years/",
    "domain": "大厂 AI 动态",
    "title": "After the midterms, is the AI industry in for a rough two years?",
    "url": "https://techcrunch.com/video/after-the-midterms-is-the-ai-industry-in-for-a-rough-two-years/",
    "source": "Theresa Loconsolo, Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T17:23:52+00:00",
    "summary": "Democrats’ historic victories in this week’s U.S. midterm elections could also transform the tech industry. The public voted on 41 data center-related ballot measures on Tuesday — in all but one, the "
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/06/pentagon-offers-battery-startup-6k-250m-loan-to-build-u-s-factory/",
    "domain": "大厂 AI 动态",
    "title": "Pentagon offers battery startup 6K $250M loan to build US factory",
    "url": "https://techcrunch.com/2026/11/06/pentagon-offers-battery-startup-6k-250m-loan-to-build-u-s-factory/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T16:50:01+00:00",
    "summary": "The Pentagon has conditionally approved a $250 million loan to help 6K scale up its microwave-plasma battery material manufacturing process."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/06/fox-completes-its-22b-acquisition-of-roku/",
    "domain": "大厂 AI 动态",
    "title": "Fox completes its $22B acquisition of Roku",
    "url": "https://techcrunch.com/2026/11/06/fox-completes-its-22b-acquisition-of-roku/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T16:05:36+00:00",
    "summary": "A few months after DOJ investigators were probing the deal, Fox just completed its $22B acquisition of the streaming giant Roku."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/06/ramp-data-shows-ai-spending-stalling-just-as-anthropic-nears-its-ipo/",
    "domain": "大厂 AI 动态",
    "title": "Ramp data shows AI spending stalling just as Anthropic nears its IPO",
    "url": "https://techcrunch.com/2026/11/06/ramp-data-shows-ai-spending-stalling-just-as-anthropic-nears-its-ipo/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T15:54:47+00:00",
    "summary": "AI usage keeps climbing, but spending has stalled. Price cuts and smarter cost controls among the biggest spenders could challenge investor assumptions about AI hypergrowth."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/06/after-blocking-muse-amazon-now-lets-users-text-alexa-to-help-them-shop/",
    "domain": "大厂 AI 动态",
    "title": "After blocking Muse, Amazon now lets users text Alexa to help them shop",
    "url": "https://techcrunch.com/2026/11/06/after-blocking-muse-amazon-now-lets-users-text-alexa-to-help-them-shop/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T14:10:00+00:00",
    "summary": "Amazon said that the feature will roll out to millions of users in coming weeks."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/06/underdog-shows-off-a-32mb-speech-model-in-new-demo/",
    "domain": "大厂 AI 动态",
    "title": "Underdog shows off a 32MB speech model in new demo",
    "url": "https://techcrunch.com/2026/11/06/underdog-shows-off-a-32mb-speech-model-in-new-demo/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T13:02:16+00:00",
    "summary": "Despite its small size, Underdog's new model can generate both speech and music."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/06/physicl-raises-10m-to-make-the-digital-world-real-enough-for-robots/",
    "domain": "大厂 AI 动态",
    "title": "Physicl raises $10M to make the digital world real enough for robots",
    "url": "https://techcrunch.com/2026/11/06/physicl-raises-10m-to-make-the-digital-world-real-enough-for-robots/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T13:00:00+00:00",
    "summary": "Physicl is trying to solve the sim-to-real gap with a pipeline originally built to market goods online."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/06/tesla-will-stop-making-the-cybertruck-in-2027/",
    "domain": "大厂 AI 动态",
    "title": "Tesla will stop making the Cybertruck in 2027",
    "url": "https://techcrunch.com/2026/11/06/tesla-will-stop-making-the-cybertruck-in-2027/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T11:50:10+00:00",
    "summary": "The decision to wind down the EV comes after just a few short years of underwhelming sales. Elon Musk said the company will use the factory space to make more Cybercabs."
  },
  {
    "id": "rss:https://stratechery.com/2026/falling-leaves-and-stocks/",
    "domain": "大厂 AI 动态",
    "title": "2026.45: Falling Leaves (and Stocks)",
    "url": "https://stratechery.com/2026/falling-leaves-and-stocks/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T18:14:42+00:00",
    "summary": "The best Stratechery content from the week of November 2, 2026, including AI on the ballot, a Google state of the union, and China."
  },
  {
    "id": "rss:https://stratechery.com/2026/sharp-tech-on-video-the-u-s-votes-on-data-centers-implications-for-big-tech-googles-response-to-ai/",
    "domain": "大厂 AI 动态",
    "title": "Sharp Tech on Video: The U.S. Votes on Data Centers, Implications for Big Tech, Google’s Response to AI",
    "url": "https://stratechery.com/2026/sharp-tech-on-video-the-u-s-votes-on-data-centers-implications-for-big-tech-googles-response-to-ai/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T11:00:00+00:00",
    "summary": "Sharp Tech is, for the first time, available on video. You have two ways to consume it: YouTube, and here on Stratechery"
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/11/the-migration-that-transformed-africas-languages-genes-and-cultures/",
    "domain": "大厂 AI 动态",
    "title": "The Bantu expansion changed Africa. Scientists are still tracing how.",
    "url": "https://arstechnica.com/science/2026/11/the-migration-that-transformed-africas-languages-genes-and-cultures/",
    "source": "Katarina Zimmer, Knowable Magazine",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T12:15:55+00:00",
    "summary": "Genes and archaeology are revealing how Bantu speakers spread across much of Africa."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/11/british-soldier-ignored-order-to-pull-his-sim-card-then-got-blackmailed/",
    "domain": "大厂 AI 动态",
    "title": "British soldier ignored order to pull his SIM card, then got blackmailed",
    "url": "https://arstechnica.com/security/2026/11/british-soldier-ignored-order-to-pull-his-sim-card-then-got-blackmailed/",
    "source": "Cyrus Farivar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T11:00:34+00:00",
    "summary": "Soldier told repeatedly to lock down devices before deploying, got sextorted, court-martialed."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/11/man-unexpectedly-recovers-from-a-knife-wound-through-his-eye-and-brain/",
    "domain": "大厂 AI 动态",
    "title": "Doctors pull knife from man's eye that went through his brain—and he's fine now",
    "url": "https://arstechnica.com/health/2026/11/man-unexpectedly-recovers-from-a-knife-wound-through-his-eye-and-brain/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T23:09:45+00:00",
    "summary": "It's the exact path, not the apparent severity that matters most, doctors say."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/11/ships-loiter-near-subsea-cables-amid-irans-warnings-to-trump/",
    "domain": "大厂 AI 动态",
    "title": "Ships loiter near subsea cables amid Iran's warnings to Trump",
    "url": "https://arstechnica.com/gadgets/2026/11/ships-loiter-near-subsea-cables-amid-irans-warnings-to-trump/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T22:41:37+00:00",
    "summary": "Iran threatened to attack subsea cables if US escalates military strikes again."
  },
  {
    "id": "rss:https://arstechnica.com/gaming/2026/11/ea-producer-tells-the-inside-story-behind-new-wing-commander-remasters/",
    "domain": "大厂 AI 动态",
    "title": "Re-releases of Wing Commander, Ultima titles hit Steam and GOG",
    "url": "https://arstechnica.com/gaming/2026/11/ea-producer-tells-the-inside-story-behind-new-wing-commander-remasters/",
    "source": "Samuel Axon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T22:08:47+00:00",
    "summary": "It's mostly bad news from EA lately, but preservation efforts are nice to see."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/11/chainalysis-says-hackers-stole-credentials-and-tokens-for-all-of-its-customers/",
    "domain": "大厂 AI 动态",
    "title": "Chainalysis says hackers stole credentials and tokens for all of its customers",
    "url": "https://arstechnica.com/security/2026/11/chainalysis-says-hackers-stole-credentials-and-tokens-for-all-of-its-customers/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T20:56:41+00:00",
    "summary": "Company said a \"multifront cyberattack\" included AI agents and an on-path data snatch."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/11/earths-churning-mantle-may-have-created-the-great-unconformity/",
    "domain": "大厂 AI 动态",
    "title": "Earth's churning mantle may have created the Great Unconformity",
    "url": "https://arstechnica.com/science/2026/11/earths-churning-mantle-may-have-created-the-great-unconformity/",
    "source": "Jacek Krywko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T20:24:20+00:00",
    "summary": "Explaining the Great Unconformity, where Cambrian deposits sit on top of older rocks."
  },
  {
    "id": "hn:50381623",
    "domain": "股票",
    "title": "Nasdaq plummets 4% into correction territory",
    "url": "https://www.cnbc.com/2026/11/04/stock-market-today-live-updates.html",
    "source": "kristianp",
    "platform": "hackernews",
    "points": 226,
    "published_at": "2026-11-05T17:11:15+00:00",
    "summary": ""
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
    "points": 235,
    "published_at": "2026-11-03T00:08:53+00:00",
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
    "points": 91,
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
    "id": "hn:50232604",
    "domain": "股票",
    "title": "Microsoft and others tell crypto platform not to tokenize their stocks",
    "url": "https://gizmodo.com/microsoft-mcdonalds-verizon-and-others-tell-crypto-platform-not-to-tokenize-their-stocks-2000830368",
    "source": "gumby",
    "platform": "hackernews",
    "points": 100,
    "published_at": "2026-10-25T15:28:40+00:00",
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
    "points": 1139,
    "published_at": "2026-11-06T12:13:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:50385870",
    "domain": "金融",
    "title": "Cuban: Facebook knowingly runs AI deepfake scam ads; docs say $16B fraud revenue",
    "url": "https://finance.yahoo.com/technology/ai/articles/mark-cuban-says-facebook-knowingly-213000020.html",
    "source": "randycupertino",
    "platform": "hackernews",
    "points": 515,
    "published_at": "2026-11-05T23:09:57+00:00",
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
    "id": "hn:50239430",
    "domain": "金融",
    "title": "Tesla cancels Cybertruck in Australia and NZ after 7 years of deposits",
    "url": "https://electrek.co/2026/10/23/tesla-cancels-cybertruck-australia-new-zealand/",
    "source": "MilnerRoute",
    "platform": "hackernews",
    "points": 98,
    "published_at": "2026-10-26T05:13:15+00:00",
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
    "id": "hn:50372038",
    "domain": "金融",
    "title": "Harmony: Chat like Discord. Federated like email",
    "url": "https://mony.lol/",
    "source": "FinalDestiny",
    "platform": "hackernews",
    "points": 36,
    "published_at": "2026-11-04T21:49:40+00:00",
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
