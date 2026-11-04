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

- 今日日期：`2026-11-04`
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
  "date": "2026-11-04",
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
    "points": 2078587,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1REx46NEc4",
    "domain": "AI",
    "title": "【全网最全】DeepSeek Harness超详细教程！50分钟吃透DSH，让SuperAgent给你干活！",
    "url": "http://www.bilibili.com/video/av117540671982699",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 1540245,
    "published_at": "2026-11-01T10:22:02+00:00",
    "summary": "DeepSeek Harness超详细教程！\n大家可以速速收藏啦~\n耗时60天制作！感谢大家的三联\n未来还会出其他AI教程，大家可以关注一下~"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 1467514,
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
    "points": 1429596,
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
    "points": 1421893,
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
    "points": 909140,
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
    "points": 889912,
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
    "points": 741866,
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
    "points": 595460,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV13YRjBTEPb",
    "domain": "AI",
    "title": "Hermes Agent零基础、保姆级教程，小白也能轻松玩转",
    "url": "http://www.bilibili.com/video/av116503638706867",
    "source": "iwenwiki",
    "platform": "bilibili",
    "points": 428907,
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
    "points": 427012,
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
    "points": 367312,
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
    "points": 345858,
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
    "points": 320669,
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
    "points": 293043,
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
    "points": 225102,
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
    "points": 185734,
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
    "points": 164661,
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
    "points": 161697,
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
    "points": 151752,
    "published_at": "2025-02-27T03:19:03+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 149049,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1kGo6BdEsT",
    "domain": "AI",
    "title": "如何用Claude Skill 做高质量 PPT（附完整教程）",
    "url": "http://www.bilibili.com/video/av116474832361424",
    "source": "阿西_出海",
    "platform": "bilibili",
    "points": 103997,
    "published_at": "2026-04-27T04:45:20+00:00",
    "summary": "很多人问我上期爆了的那条视频里，那个 PPT 是怎么做的。\n其实我是用 Anthropic 最近出的 Claude Design 做的，这个功能一发出来就在全网传疯了，一条推文就冲上了 6000 多万曝光。\n本期视频我会带你手把手从 0 到 1 把这个Skill 装好，然后一起跑一个成品效果出来。"
  },
  {
    "id": "bvid:BV1VL3F6pE9K",
    "domain": "AI",
    "title": "0基础入门智能体agent测试：AI测试基础+AI智能体(Agent)测试从零入门全攻略，2026最新版！",
    "url": "http://www.bilibili.com/video/av116991151113881",
    "source": "黑马测试",
    "platform": "bilibili",
    "points": 100856,
    "published_at": "2026-07-27T09:19:37+00:00",
    "summary": "还在卷传统软件测试？2026年必学的AI智能体(Agent)测试来了！本期视频专为0基础小白打造，从软件测试基础讲起...若要本视频配套资源笔记可加up主企微（请看置顶留言最后一句话）。"
  },
  {
    "id": "bvid:BV1K6YM69ESq",
    "domain": "AI",
    "title": "AI+网络安全实战：从Agent入门到AI智能体挖漏洞教程！网络安全|信息安全|黑客技术|渗透测试|SRC漏洞挖掘|AI审计|HVV护网行动|靶场练习-码士集团",
    "url": "http://www.bilibili.com/video/av117247037213495",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 95328,
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
    "points": 94236,
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
    "points": 77444,
    "published_at": "2025-07-12T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV14rxM6qEnL",
    "domain": "AI",
    "title": "最新Skills开发教程，Agent skill实战|WorkBuddy+Codex+DeepSeek Harness",
    "url": "http://www.bilibili.com/video/av117511429295044",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 67292,
    "published_at": "2026-10-28T02:00:00+00:00",
    "summary": "【课程简介】Agent Skills零基础教程，从WorkBuddy、Codex上手到项目落地实战。"
  },
  {
    "id": "bvid:BV1woHQ6kEtv",
    "domain": "AI",
    "title": "【2026最新版】Workbuddy财务自动化办公实战教程，搭建数字员工，能够秒做账、报税、报销、出报表、做财务分析、编制预算、处理合并报表",
    "url": "http://www.bilibili.com/video/av117404038466491",
    "source": "Max极客菌",
    "platform": "bilibili",
    "points": 57232,
    "published_at": "2026-10-08T07:22:21+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 56694,
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
    "points": 50089,
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
    "points": 47797,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1hxMbzqEzU",
    "domain": "AI",
    "title": "小智MCP自由了！我开源了个命令行神器实现多MCP聚合",
    "url": "http://www.bilibili.com/video/av114686414625640",
    "source": "闪电蘑菇",
    "platform": "bilibili",
    "points": 43022,
    "published_at": "2025-06-15T08:31:55+00:00",
    "summary": "- 我写的小智客户端命令行工具\n - github: https://github.com/shenjingnan/xiaozhi-client\n - gitee: https://gitee.com/shenjingnan/xiaozhi-client\n\n- 小智官方MCP示例代码仓库：\n - github: https://github.com/78/mcp-calculator\n - git"
  },
  {
    "id": "bvid:BV1uVSUBkEfZ",
    "domain": "AI",
    "title": "Microsoft Copilot完整教程(上) 从入门到Agent 一站式掌握AI办公",
    "url": "http://www.bilibili.com/video/av116351721084069",
    "source": "星小脉",
    "platform": "bilibili",
    "points": 42510,
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
    "points": 41190,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV17Lap6VEUr",
    "domain": "AI",
    "title": "【全80集】Vibe Coding 零基础入门到实战教程，由浅入深（全程干货）",
    "url": "http://www.bilibili.com/video/av117353572468721",
    "source": "数据拾光屋",
    "platform": "bilibili",
    "points": 40956,
    "published_at": "2026-10-02T09:25:00+00:00",
    "summary": "本套教程专门为零基础学员而制，全程干货无废话，喜欢的小伙伴记得点赞三连喔 ~"
  },
  {
    "id": "bvid:BV1hmb26ZEws",
    "domain": "AI",
    "title": "DeepSeek Harness 实测  Claude Code 对比后，梁神我错了 差距比我想的大",
    "url": "http://www.bilibili.com/video/av117100337236191",
    "source": "程序员晓刘",
    "platform": "bilibili",
    "points": 36458,
    "published_at": "2026-08-15T16:01:38+00:00",
    "summary": "这期用同一个 DeepSeek Pro 0813 模型，分别在 Claude Code 和 DeepSeek Harness 里完成同样的任务，对比工具链对最终效果的影响。\n实测内容包括：\nFPS 游戏 Demo、灯塔预警沙盘、手枪组装动画、显示器组装动画，以及 DeepSeek Harness 的插件化源码流程。\n整体看下来，模型本身当然重要，但 Harness 在插件化、流程记录、缓存命中和任"
  },
  {
    "id": "bvid:BV1gwcAzkEhw",
    "domain": "AI",
    "title": "Claude Code Agent Teams上手指南+项目实测",
    "url": "http://www.bilibili.com/video/av116037064331269",
    "source": "程序员阿江-Relakkes",
    "platform": "bilibili",
    "points": 36187,
    "published_at": "2026-02-08T23:30:00+00:00",
    "summary": "用Claude Code干复杂任务总碰到三个问题：\n\n上下文越来越长开始遗忘、任务只能串行效率低、单Agent视角单一容易漏检。\n\nClaude官方发布的Agent Teams功能正好解决这些痛点\n\n一个Team Lead拆任务，多个Teammate并行执行，还能互相通信协调。\n\n本期视频从核心概念、使用场景、底层架构到真实项目实战，带你完整搞懂Agent Teams的正确打开方式。"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 34637,
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
    "points": 31437,
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
    "points": 31304,
    "published_at": "2026-09-28T15:30:36+00:00",
    "summary": "详细的agent部署介绍：https://pan.quark.cn/s/3846914c6da7\n欢迎来到ai的世界！！\n有疑问欢迎私信。"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29926,
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
    "points": 29033,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV11K9gBqEnW",
    "domain": "AI",
    "title": "【杀戮尖塔2】AI MOD 配置教程第一期来辣！手把手教你怎么改提示词！以及如何设计自己的爬塔玩法",
    "url": "http://www.bilibili.com/video/av116341654755924",
    "source": "分歧点WhatIf",
    "platform": "bilibili",
    "points": 28708,
    "published_at": "2026-04-03T16:14:43+00:00",
    "summary": "每个参数都是干什么的，如何修改提示词的教程。\n不知道这是什么？请看合集内的视频~\n我做了一个 AI 的杀戮尖塔2MOD！\n可以和怪物对话，策反怪物，带着怪物爬塔（重写了几乎每一个怪物在友方时候的行为），还能给怪物打防御，带个沙虫全吃了！\n可以和上古之民对话，聊嗨了会给你 1～2 个额外赐福，还能帮你指示为未来\n可以让偷窃草蜢偷队友的 key 卡，想无限？偷了！\n可以和商人讨价还价，甚至白嫖\n多人的"
  },
  {
    "id": "bvid:BV18cnF6NEjC",
    "domain": "AI",
    "title": "实测！Grok Cursor等多模型整合后，性价比如何？",
    "url": "http://www.bilibili.com/video/av117471180821997",
    "source": "野生吃货",
    "platform": "bilibili",
    "points": 26395,
    "published_at": "2026-10-20T03:50:25+00:00",
    "summary": "简介无推广内容\n视频中演示网站有正规ICP备案"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 26169,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1nQQDB3EQ2",
    "domain": "AI",
    "title": "从零实现Clude Code（第一话）——Agent Loop",
    "url": "http://www.bilibili.com/video/av116273857961234",
    "source": "日新月异max",
    "platform": "bilibili",
    "points": 25737,
    "published_at": "2026-03-22T16:52:32+00:00",
    "summary": "&quot;One loop &amp; Bash is all you need&quot; -- 一个工具 + 一个循环 = 一个智能体。\nHarness 层: 循环 -- 模型与真实世界的第一道连接。"
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 25578,
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
    "points": 22844,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV188UHYkEdg",
    "domain": "AI",
    "title": "Cursor / Windsurf + Android Studio 高效AI编程：零基础也能开发安卓应用",
    "url": "http://www.bilibili.com/video/av113502647750313",
    "source": "kate人不错",
    "platform": "bilibili",
    "points": 21175,
    "published_at": "2024-11-18T07:04:36+00:00",
    "summary": "欢迎关注我的知识星球：https://t.zsxq.com/FF0He\n\n我会分享最新AI资讯、源代码、回答你的提问。\n\n视频亮点：\n\n双工具对比：解析 Cursor 和 Windsurf 各自优势\n实战案例：从五子棋到卡路里计算AI应用的完整开发过程\n专业部署：Android Studio 配置与构建技巧\n\n时间戳：\n\n0:00 - 引言\n\n0:26 - 我开发的应用演示\n\n2:33 - Rea"
  },
  {
    "id": "bvid:BV1f57C6YErb",
    "domain": "AI",
    "title": "手把手教你Codex安装和使用MCP！新手必备~",
    "url": "http://www.bilibili.com/video/av116696861907147",
    "source": "Raina测试",
    "platform": "bilibili",
    "points": 18651,
    "published_at": "2026-06-06T11:29:00+00:00",
    "summary": "这一期给大家分享下在codex里面如何配置和使用MCP，和skill一样，MCP也是我们平时用得比较多的，所以建议大家也可以学一下它的基础配置和使用~\n步骤都不难，跟着操作就可以了"
  },
  {
    "id": "hn:49970667",
    "domain": "AI 算力 / 半导体",
    "title": "Opus 5.5 agents discover two room-temperature magnetic semiconductor candidates",
    "url": "https://www.vals.ai/blogs/room-temperature-magnetic-semiconductors",
    "source": "outlier99",
    "platform": "hackernews",
    "points": 495,
    "published_at": "2026-10-05T21:00:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:50293047",
    "domain": "AI 算力 / 半导体",
    "title": "Alleged Chinese spy had 'close relationship' with Nvidia boss Jensen Huang",
    "url": "https://nypost.com/2026/10/29/business/alleged-chinese-spy-had-close-relationship-with-nvidia-boss-jensen-huang-report/",
    "source": "mgh2",
    "platform": "hackernews",
    "points": 360,
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
    "points": 281,
    "published_at": "2026-11-03T07:04:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:50219700",
    "domain": "AI 算力 / 半导体",
    "title": "GPU-unlock: FP/BF16 instruction issue rate on Nvidia 3000's cards",
    "url": "https://github.com/Zagitta/gpu-unlock",
    "source": "fragebogen",
    "platform": "hackernews",
    "points": 352,
    "published_at": "2026-10-24T09:58:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:50327058",
    "domain": "AI 算力 / 半导体",
    "title": "Seoul Viosys begins production of rare-earth-free white light emitter",
    "url": "https://www.semiconductor-today.com/news_items/2026/oct/seoul-291026.shtml",
    "source": "gmays",
    "platform": "hackernews",
    "points": 193,
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
    "id": "hn:50362905",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia RTX Spark encrypted firmware slows inference speed to 35% on Linux",
    "url": "https://www.mindstudio.ai/blog/linux-nvidia-rtx-spark-laptop",
    "source": "novaRom",
    "platform": "hackernews",
    "points": 56,
    "published_at": "2026-11-04T08:46:29+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/quantum-roadmaps-are-finally-meeting-reality/",
    "domain": "AI 算力 / 半导体",
    "title": "Quantum Roadmaps Are Finally Meeting Reality",
    "url": "https://www.eetimes.com/quantum-roadmaps-are-finally-meeting-reality/",
    "source": "Marie Lepske",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T09:11:15+00:00",
    "summary": "Quantum computing revenue surpassed $1 billion in 2025, but missed forecasts highlight the gap between commercial expectations and delivery. The post Quantum Roadmaps Are Finally Meeting Reality appea"
  },
  {
    "id": "rss:https://www.eetimes.com/is-there-room-for-small-scale-osats-in-india-chip-packaging-boom/",
    "domain": "AI 算力 / 半导体",
    "title": "Is There Room for Small-Scale OSATs in India’s Chip Packaging Boom?",
    "url": "https://www.eetimes.com/is-there-room-for-small-scale-osats-in-india-chip-packaging-boom/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T23:30:00+00:00",
    "summary": "Small OSATs in India can start with ₹1.5–₹2 billion (~$15.8–$21 million), consultant Nitin Dodia said. But anchor customers, skilled staff, and qualification determine who survives. The post Is There "
  },
  {
    "id": "rss:https://www.eetimes.com/u-s-manufacturing-activity-gains-momentum-in-october/",
    "domain": "AI 算力 / 半导体",
    "title": "U.S. Manufacturing Activity Gains Momentum in October",
    "url": "https://www.eetimes.com/u-s-manufacturing-activity-gains-momentum-in-october/",
    "source": "News Desk",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T19:08:38+00:00",
    "summary": "Economic activity in the U.S. manufacturing sector expanded in October driven by accelerating production and steady gains in new orders. The post U.S. Manufacturing Activity Gains Momentum in October "
  },
  {
    "id": "rss:https://www.eetimes.com/accepting-orders-for-the-led-light-sourced-projection-aligners/",
    "domain": "AI 算力 / 半导体",
    "title": "Accepting Orders for the LED Light-Sourced Projection Aligners",
    "url": "https://www.eetimes.com/accepting-orders-for-the-led-light-sourced-projection-aligners/",
    "source": "USHIO INC.",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T15:54:08+00:00",
    "summary": "Ushio has been accepting orders for LED-based UX-4 wafer aligners since July 2026, offering mercury-free, high-throughput lithography. The post Accepting Orders for the LED Light-Sourced Projection Al"
  },
  {
    "id": "rss:https://www.eetimes.com/bringing-design-data-management-into-the-developer-workflow/",
    "domain": "AI 算力 / 半导体",
    "title": "Bringing Design Data Management into the Developer Workflow",
    "url": "https://www.eetimes.com/bringing-design-data-management-into-the-developer-workflow/",
    "source": "Keysight Technologies",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T15:00:00+00:00",
    "summary": "As digital design workflows increasingly center on modern, text-based development environments, engineers expect the same efficiency from design data management as they do from coding tools. Visual St"
  },
  {
    "id": "rss:https://www.eetimes.com/ai-hardwares-hidden-cost-between-orders-and-output/",
    "domain": "AI 算力 / 半导体",
    "title": "AI Hardware’s Hidden Cost: Between Orders and Output",
    "url": "https://www.eetimes.com/ai-hardwares-hidden-cost-between-orders-and-output/",
    "source": "Ron Honig",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T14:08:41+00:00",
    "summary": "Alphabet’s TPU inventory, Intel’s manufacturing tradeoffs, and equipment suppliers’ balance sheets show how capital builds up along the path to usable AI computing capacity. The post AI Hardware’s Hid"
  },
  {
    "id": "rss:https://www.eetimes.com/five-things-you-didnt-know-about-co-packaged-optics/",
    "domain": "AI 算力 / 半导体",
    "title": "Five Things You Didn’t Know About Co-Packaged Optics",
    "url": "https://www.eetimes.com/five-things-you-didnt-know-about-co-packaged-optics/",
    "source": "Chee Ping Lee, managing director of Advanced Packaging Strategic Marketing at Lam Research",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T14:00:00+00:00",
    "summary": "CPO may be a photonics breakthrough, but commercial success hinges equally on advanced packaging that integrates, connects and protects components at scale. The post Five Things You Didn’t Know About "
  },
  {
    "id": "rss:https://www.eetimes.com/marvell-snaps-photonics-chipmaker-lumentum-to-bolster-ai-connectivity/",
    "domain": "AI 算力 / 半导体",
    "title": "Marvell Snaps Photonics Chipmaker Lumentum to Bolster AI Connectivity",
    "url": "https://www.eetimes.com/marvell-snaps-photonics-chipmaker-lumentum-to-bolster-ai-connectivity/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T08:50:21+00:00",
    "summary": "The $115 billion deal aims to create a category leader in AI connectivity by co-designing network processors and lasers for optical transceivers. The post Marvell Snaps Photonics Chipmaker Lumentum to"
  },
  {
    "id": "rss:https://www.eetimes.com/macronix-builds-hardware-security-into-nor-flash-ahead-of-eu-cyber-resilience-act/",
    "domain": "AI 算力 / 半导体",
    "title": "Macronix Builds Hardware Security into NOR Flash Ahead of EU Cyber Resilience Act",
    "url": "https://www.eetimes.com/macronix-builds-hardware-security-into-nor-flash-ahead-of-eu-cyber-resilience-act/",
    "source": "EE Times Taiwan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T05:30:00+00:00",
    "summary": "The European Union's Cyber Resilience Act (CRA), which becomes mandatory in December 2027, is raising the bar for cybersecurity in connected devices. Rather than relying on software patches to address"
  },
  {
    "id": "rss:https://www.eetimes.com/inside-automotive-dms-oms-technology-challenges-power-solutions/",
    "domain": "AI 算力 / 半导体",
    "title": "Inside Automotive DMS & OMS: Technology, Challenges & Power Solutions",
    "url": "https://www.eetimes.com/inside-automotive-dms-oms-technology-challenges-power-solutions/",
    "source": "Monotlithic Power Systems",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T19:33:59+00:00",
    "summary": "Join our expert for an in-depth look inside today's DMS and OMS architectures. You'll gain practical insights into camera design, power delivery, and thermal management strategies, while learning how "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/us-army-successfully-flies-a-hybrid-electric-drone-with-3d-printed-heavy-fuel-rotary-engine-400v-motor-generator-uses-advanced-engineering-to-ditch-a-bulky-liquid-cooling-system",
    "domain": "AI 算力 / 半导体",
    "title": "US Army successfully flies a hybrid electric drone with 3D-printed heavy-fuel rotary engine — 400v motor-generator uses advanced engineering to ditch a bulky liquid cooling system",
    "url": "https://www.tomshardware.com/tech-industry/drones/us-army-successfully-flies-a-hybrid-electric-drone-with-3d-printed-heavy-fuel-rotary-engine-400v-motor-generator-uses-advanced-engineering-to-ditch-a-bulky-liquid-cooling-system",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T10:30:00+00:00",
    "summary": "The US Army VICTOR drone uses an optimized heavy-fuel rotary engine developed with metal 3D printing for rapid prototyping."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/windows-11-8gb-ram-configurations-get-a-performance-boost-as-ai-demand-keeps-pushing-prices-up-microsoft-says-windows-is-now-20-percent-more-responsive-multitasking-40-percent-faster-on-memory-constrained-machines",
    "domain": "AI 算力 / 半导体",
    "title": "Windows 11 8GB RAM configurations get a performance boost",
    "url": "https://www.tomshardware.com/software/windows/windows-11-8gb-ram-configurations-get-a-performance-boost-as-ai-demand-keeps-pushing-prices-up-microsoft-says-windows-is-now-20-percent-more-responsive-multitasking-40-percent-faster-on-memory-constrained-machines",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T17:00:00+00:00",
    "summary": "Microsoft claims that it has made drastic improvements to the performance of Windows 11 while using 8GB of RAM."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/openai-introduces-program-to-reduce-ai-data-center-energy-demand-during-peak-hours-company-testing-grid-protectors-program-system-in-georgia",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI introduces program to reduce AI data center energy demand during peak hours",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/openai-introduces-program-to-reduce-ai-data-center-energy-demand-during-peak-hours-company-testing-grid-protectors-program-system-in-georgia",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T15:56:51+00:00",
    "summary": "The Grid Protectors Program applies load shedding, a technique in use since the 1970s, to data centers."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/intel-14a-moves-closer-to-production-as-pdk-0-9-becomes-available-process-design-kit-gives-developers-important-production-milestone-ahead-of-1-0-in-2027",
    "domain": "AI 算力 / 半导体",
    "title": "Intel 14A moves closer to production as PDK 0.9 becomes available",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/intel-14a-moves-closer-to-production-as-pdk-0-9-becomes-available-process-design-kit-gives-developers-important-production-milestone-ahead-of-1-0-in-2027",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T15:20:27+00:00",
    "summary": "Intel says its next-generation process technology is reaching expected performance and yield maturity."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/elon-musks-xai-installs-eight-converted-jet-engines-to-power-mississippi-data-center-permits-allow-25-percent-higher-limit-for-pollutants-concerns-raised-over-carbon-monoxide",
    "domain": "AI 算力 / 半导体",
    "title": "8 converted jet engines are powering xAI data centers as companies look for new energy sources",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/elon-musks-xai-installs-eight-converted-jet-engines-to-power-mississippi-data-center-permits-allow-25-percent-higher-limit-for-pollutants-concerns-raised-over-carbon-monoxide",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T15:02:09+00:00",
    "summary": "A Mississippi xAI data center is using eight converted jet engine turbines as a power source despite the known health risks of the carbon monoxide and volatile organic compounds they produce."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/apple-faces-unprecedented-memory-cost-increases-as-ram-prices-continue-to-surge-manufacturing-bill-climbs-by-usd33-billion-rising-component-expenses-threaten-margins-through-the-holiday-quarter-and-into-2027",
    "domain": "AI 算力 / 半导体",
    "title": "Apple faces unprecedented memory cost increases as RAM prices continue to surge, manufacturing bill climbs by $33 billion",
    "url": "https://www.tomshardware.com/pc-components/dram/apple-faces-unprecedented-memory-cost-increases-as-ram-prices-continue-to-surge-manufacturing-bill-climbs-by-usd33-billion-rising-component-expenses-threaten-margins-through-the-holiday-quarter-and-into-2027",
    "source": "Newton Gitonga",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T14:28:59+00:00",
    "summary": "Samsung, SK hynix, and Micron are facing strong demand for memory from AI data centers, prompting manufacturers to prioritize higher-margin server products and high-bandwidth memory. That shift is tig"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/docking-stations-hubs/hands-on-with-the-dockcase-mount-ling-2-pro-handheld-dock-with-a-built-in-capture-card-and-space-for-up-to-4tb-of-nvme-storage",
    "domain": "AI 算力 / 半导体",
    "title": "Hands-on with the DockCase Mount Ling 2 Pro",
    "url": "https://www.tomshardware.com/peripherals/docking-stations-hubs/hands-on-with-the-dockcase-mount-ling-2-pro-handheld-dock-with-a-built-in-capture-card-and-space-for-up-to-4tb-of-nvme-storage",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T14:20:22+00:00",
    "summary": "The Mount Ling 2 Pro is a dock for Nintendo Switch 2, Steam Deck, or other PC handhelds that doubles as a capture card and a vehicle for up to 4TB of NVMe SSD storage."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/bambu-lab-h3c-3d-printer-review",
    "domain": "AI 算力 / 半导体",
    "title": "Bambu Lab H3C 3D printer review: A nine-tool monster",
    "url": "https://www.tomshardware.com/3d-printing/bambu-lab-h3c-3d-printer-review",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T14:00:00+00:00",
    "summary": "The Bambu Lab H3C is a massive tool changer that handles TPU like nobody’s business."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/nvidia-tells-data-center-operators-to-limit-business-from-chinese-customers-with-new-global-restrictions-report-claims-allegedly-restricted-to-49-percent-of-the-total-ensuring-51-percent-are-non-chinese-outfits",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia tells data center operators to limit business from Chinese customers with new global restrictions, report claims",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/nvidia-tells-data-center-operators-to-limit-business-from-chinese-customers-with-new-global-restrictions-report-claims-allegedly-restricted-to-49-percent-of-the-total-ensuring-51-percent-are-non-chinese-outfits",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T13:31:11+00:00",
    "summary": "Nvidia has told cloud providers who use its data center products that they must sell less than half of their services to Chinese companies as part of a new policy that will further impact China's abil"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/corsair-has-slashed-usd180-off-its-blistering-mp700-se-gen-5-ssd-now-14-cents-per-gb-get-4tb-of-ssd-storage-for-usd579-the-cheapest-drive-on-the-market",
    "domain": "AI 算力 / 半导体",
    "title": "Corsair has slashed $180 off its blistering MP700 SE Gen 5 SSD",
    "url": "https://www.tomshardware.com/pc-components/ssds/corsair-has-slashed-usd180-off-its-blistering-mp700-se-gen-5-ssd-now-14-cents-per-gb-get-4tb-of-ssd-storage-for-usd579-the-cheapest-drive-on-the-market",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T13:25:30+00:00",
    "summary": "The 4TB Corsair MP 700 Pro SE is $180 off, the cheapest 4TB Gen 5 SSD you can buy right now."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/google-reveals-new-gemini-4-carbon-ai-model-narrowly-beating-claude-opus-5-5-frontier-ai-model-is-also-the-least-likely-to-hallucinate-benchmarks-claim",
    "domain": "AI 算力 / 半导体",
    "title": "Google reveals new Gemini 4 Carbon AI model, narrowly beating Claude Opus 5.5",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/google-reveals-new-gemini-4-carbon-ai-model-narrowly-beating-claude-opus-5-5-frontier-ai-model-is-also-the-least-likely-to-hallucinate-benchmarks-claim",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T13:00:00+00:00",
    "summary": "Last week, Google released its latest AI model, Gemini 4 Carbon, topping intelligence rankings charts."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/china-deploys-worlds-first-800-volt-dc-power-system-for-massive-ai-data-center-seeks-to-quench-power-needs-with-higher-conversion-and-efficiency-inside-a-smaller-footprint",
    "domain": "AI 算力 / 半导体",
    "title": "China deploys 'world's first' 800-volt DC power system for massive AI data center",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/china-deploys-worlds-first-800-volt-dc-power-system-for-massive-ai-data-center-seeks-to-quench-power-needs-with-higher-conversion-and-efficiency-inside-a-smaller-footprint",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T12:40:09+00:00",
    "summary": "Firm says it has completed the world’s first commercial data center deployment of an integrated 800-volt DC power system."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/chinese-survey-ship-loitering-near-undersea-cable-ignores-philippine-demands-to-withdraw-evasive-action-point-to-growing-prc-threats-to-data-lines-in-the-pacific",
    "domain": "AI 算力 / 半导体",
    "title": "Chinese survey ship loitering near undersea cable ignores Philippine demands to withdraw",
    "url": "https://www.tomshardware.com/tech-industry/chinese-survey-ship-loitering-near-undersea-cable-ignores-philippine-demands-to-withdraw-evasive-action-point-to-growing-prc-threats-to-data-lines-in-the-pacific",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T12:31:11+00:00",
    "summary": "A Chinese research vessel ignored the Philippine coast guard's attempts to move it as it loitered over an undersea cable near its coast as the PRC continues to use civilian vessels as \"gray-zone\" warf"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/the-sgbc-is-an-fpga-game-boy-console-that-can-rip-your-cartridges-to-an-sd-card-natively-it-even-has-game-link-cable-support",
    "domain": "AI 算力 / 半导体",
    "title": "Engineer creates retro FPGA Game Boy console that can rip your cartridges to an SD card natively",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/the-sgbc-is-an-fpga-game-boy-console-that-can-rip-your-cartridges-to-an-sd-card-natively-it-even-has-game-link-cable-support",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T12:30:00+00:00",
    "summary": "Joining the FPGA console trend is the SGBC, a Game Boy console that natively supports a Game Boy cartridge slot and copying cartridge ROMs to a microSD card."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/snag-this-360hz-qd-oled-gaming-monitor-for-only-usd349-sumptuous-27-inch-display-also-features-an-integrated-wi-fi-antenna",
    "domain": "AI 算力 / 半导体",
    "title": "Snag this 360Hz QD-OLED gaming monitor for only $349",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/snag-this-360hz-qd-oled-gaming-monitor-for-only-usd349-sumptuous-27-inch-display-also-features-an-integrated-wi-fi-antenna",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T12:17:30+00:00",
    "summary": "An affordable OLED monitor upgrade for just $349. Featuring a blistering 360Hz refresh rate and an integrated WiFi antenna."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/ai-chip-smugglers-exploit-trade-control-loophole-to-bring-banned-hbm-from-south-korea-into-china-expensive-memory-chips-packaged-with-cheap-unsanctioned-processors-to-become-legal-exports",
    "domain": "AI 算力 / 半导体",
    "title": "AI chip smugglers exploit trade control loophole to bring banned HBM from South Korea into China",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/ai-chip-smugglers-exploit-trade-control-loophole-to-bring-banned-hbm-from-south-korea-into-china-expensive-memory-chips-packaged-with-cheap-unsanctioned-processors-to-become-legal-exports",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T12:04:32+00:00",
    "summary": "Customs authorities only check the performance specifications of a server's processors, allowing smugglers to attach high-end memory chips to low-end processors and ship them into China."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/steam-survey-shockwaves-felt-as-proportion-of-32gb-ram-systems-drops-by-more-than-5-percent-the-percentage-of-pc-gamers-with-1tb-total-storage-also-shrunk-by-nearly-5-percent",
    "domain": "AI 算力 / 半导体",
    "title": "Steam Survey shockwaves felt as proportion of 32GB RAM systems drops by more than 5%",
    "url": "https://www.tomshardware.com/pc-components/ram/steam-survey-shockwaves-felt-as-proportion-of-32gb-ram-systems-drops-by-more-than-5-percent-the-percentage-of-pc-gamers-with-1tb-total-storage-also-shrunk-by-nearly-5-percent",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T12:00:00+00:00",
    "summary": "The latest Steam Survey appears to show that gamers blessed with systems packing 32GB or more RAM and 1TB or more storage are a dying breed."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/developer-manages-to-run-windows-11-26h2-with-just-128mb-of-ram-just-3-1-percent-of-recommended-minimum-stripped-down-installation-can-access-desktop-file-explorer-and-notepad",
    "domain": "AI 算力 / 半导体",
    "title": "Developer manages to run Windows 11 26H2 with just 128MB of RAM, just 3.1% of recommended minimum",
    "url": "https://www.tomshardware.com/software/windows/developer-manages-to-run-windows-11-26h2-with-just-128mb-of-ram-just-3-1-percent-of-recommended-minimum-stripped-down-installation-can-access-desktop-file-explorer-and-notepad",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T11:30:00+00:00",
    "summary": "The developer's latest experiment takes Windows 11's hardware requirements to an extreme, managing to retain basic desktop functionality with just 128MB of memory, although the resulting installation "
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/grab-a-huge-usd1-229-saving-on-this-18-inch-alienware-gaming-laptop-with-an-rtx-5070-area-51-machine-packs-a-24-core-intel-cpu-32gb-ddr5-and-a-1tb-ssd-for-usd2-449-99",
    "domain": "AI 算力 / 半导体",
    "title": "Grab a huge $1,229 saving on this 18-inch Alienware gaming laptop with an RTX 5070",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/grab-a-huge-usd1-229-saving-on-this-18-inch-alienware-gaming-laptop-with-an-rtx-5070-area-51-machine-packs-a-24-core-intel-cpu-32gb-ddr5-and-a-1tb-ssd-for-usd2-449-99",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T11:06:59+00:00",
    "summary": "Grab a $1,229 saving on this Alienware Area 51 gaming laptop right now with an RTX 5070 and 32GB DDR5."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/mini-pcs/amazon-closes-ai-creators-account-after-he-attempts-to-buy-seven-nvidia-dgx-spark-mini-pcs-epic-ceo-tim-sweeney-says-his-regular-orders-were-canceled-before-arrival-after-he-tried-to-buy-two-gpus",
    "domain": "AI 算力 / 半导体",
    "title": "Creator says Amazon closed his account after he tried to buy seven Nvidia DGX Sparks",
    "url": "https://www.tomshardware.com/desktops/mini-pcs/amazon-closes-ai-creators-account-after-he-attempts-to-buy-seven-nvidia-dgx-spark-mini-pcs-epic-ceo-tim-sweeney-says-his-regular-orders-were-canceled-before-arrival-after-he-tried-to-buy-two-gpus",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T11:00:00+00:00",
    "summary": "Nick Saraev says Amazon closed his account after canceling Nvidia DGX Spark orders; Tim Sweeney reports canceled orders after a GPU buy."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/openai-considers-rebranding-data-centers-to-ai-compute-campuses-as-data-center-backlash-intensifies-company-reportedly-sees-2028-presidential-election-becoming-an-ai-issue",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI considers rebranding data centers to 'AI compute campuses\" as data center backlash intensifies",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/openai-considers-rebranding-data-centers-to-ai-compute-campuses-as-data-center-backlash-intensifies-company-reportedly-sees-2028-presidential-election-becoming-an-ai-issue",
    "source": "Newton Gitonga",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T19:15:31+00:00",
    "summary": "OpenAI expects AI to become a major issue in the 2028 presidential election and is preparing a policy and public relations push after the U.S. midterm elections. The company is also promoting the term"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/tachyum-developer-of-heavily-delayed-universal-prodigy-processor-voluntarily-files-for-bankruptcy-future-of-prodigy-ip-unknown-as-company-begins-bankruptcy-proceedings",
    "domain": "AI 算力 / 半导体",
    "title": "Tachyum, developer of heavily-delayed universal Prodigy processor, voluntarily files for bankruptcy",
    "url": "https://www.tomshardware.com/pc-components/cpus/tachyum-developer-of-heavily-delayed-universal-prodigy-processor-voluntarily-files-for-bankruptcy-future-of-prodigy-ip-unknown-as-company-begins-bankruptcy-proceedings",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T18:07:21+00:00",
    "summary": "Tachyum files for bankruptcy, the court in Bratislava initiates bankruptcy proceedings."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/putin-demands-russian-data-centers-supply-capacity-to-the-state-in-wake-of-ukraine-drone-attacks-10-percent-capacity-must-be-available-for-state-it-infrastructure-with-24-hours-notice",
    "domain": "AI 算力 / 半导体",
    "title": "Putin demands Russian data centers supply capacity to the state in wake of Ukraine drone attacks",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/putin-demands-russian-data-centers-supply-capacity-to-the-state-in-wake-of-ukraine-drone-attacks-10-percent-capacity-must-be-available-for-state-it-infrastructure-with-24-hours-notice",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T18:00:32+00:00",
    "summary": "President Putin has told non-state Russian data centers that they must set aside 10% of their total capacity for use by the country's own IT infrastructure."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/creality-k3-review",
    "domain": "AI 算力 / 半导体",
    "title": "Creality K3 Review: It’s a Tool Changer, not a game changer",
    "url": "https://www.tomshardware.com/3d-printing/creality-k3-review",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T16:40:58+00:00",
    "summary": "Creality’s four-color tool changer is a good one, but is it too late?"
  },
  {
    "id": "rss:https://www.tomshardware.com/raspberry-pi/16gb-raspberry-pi-5-hiked-to-usd385-more-than-triple-its-launch-price-makers-are-already-shifting-to-pico-esp32-for-small-projects-mini-pcs-for-more-ambitious-tasks",
    "domain": "AI 算力 / 半导体",
    "title": "16GB Raspberry Pi 5 hiked to $385, more than triple its launch price",
    "url": "https://www.tomshardware.com/raspberry-pi/16gb-raspberry-pi-5-hiked-to-usd385-more-than-triple-its-launch-price-makers-are-already-shifting-to-pico-esp32-for-small-projects-mini-pcs-for-more-ambitious-tasks",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T16:17:35+00:00",
    "summary": "The Raspberry Pi 16GB has gone up in price by $80 to $385. It now costs more than triple its January 2025 launch price."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/america-hates-data-centers-new-database-reveals-more-than-90-percent-of-10-000-public-comments-are-negative-only-21-percent-mention-ai-73-percent-of-meetings-had-no-data-center-supporters-water-is-the-number-one-concern",
    "domain": "AI 算力 / 半导体",
    "title": "'America hates data centers' — New data highlights public sentiment",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/america-hates-data-centers-new-database-reveals-more-than-90-percent-of-10-000-public-comments-are-negative-only-21-percent-mention-ai-73-percent-of-meetings-had-no-data-center-supporters-water-is-the-number-one-concern",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T15:19:12+00:00",
    "summary": "A new website seeks to distill over 10,000 public comments about data centers in the community across more than 410 local governments, and the consensus is that people don't like them one bit."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/gamers-asus-tuf-monitor-blocks-bullet-fired-through-wall-during-call-of-duty-session-says-280hz-monitor-is-the-best-usd280-i-ever-spent",
    "domain": "AI 算力 / 半导体",
    "title": "Gamer's Asus TUF monitor blocks bullet fired through wall during Call of Duty session",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/gamers-asus-tuf-monitor-blocks-bullet-fired-through-wall-during-call-of-duty-session-says-280hz-monitor-is-the-best-usd280-i-ever-spent",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T14:34:50+00:00",
    "summary": "A Redditor was playing Call of Duty when they heard gunfire outside their home. After hitting the deck, they discovered that their monitor had potentially saved their life."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/macbooks/apple-finally-has-a-touchscreen-macbook-why-now",
    "domain": "AI 算力 / 半导体",
    "title": "Apple finally has a touchscreen MacBook. Why now?",
    "url": "https://www.tomshardware.com/laptops/macbooks/apple-finally-has-a-touchscreen-macbook-why-now",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T14:00:00+00:00",
    "summary": "Apple is introducing a touchscreen laptop in the MacBook Pro with a PROLED XDR Display. Here's where it falls in the long timeline of touchscreen laptops."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/nvidia-brev-security-breach-may-have-exposed-ssh-keys-used-to-access-customer-vms-investigation-finds-unauthorized-activity-spanning-16-days-but-no-evidence-of-misuse",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Brev security breach may have exposed SSH keys used to access customer VMs",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/nvidia-brev-security-breach-may-have-exposed-ssh-keys-used-to-access-customer-vms-investigation-finds-unauthorized-activity-spanning-16-days-but-no-evidence-of-misuse",
    "source": "Newton Gitonga",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T14:00:00+00:00",
    "summary": "Nvidia is investigating a security incident involving its Brev cloud development platform after detecting unauthorized activity between October 4 and October 20. The incident may have exposed SSH keys"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-engineer-successfully-compiles-a-32-bit-risc-v-cpu-in-qwen-3-5-4b-llm-inserted-directly-into-its-weights-built-in-cpu-can-run-processor-arithmetic-operations-code-and-of-course-doom",
    "domain": "AI 算力 / 半导体",
    "title": "AI model gets a 32-bit RISC-V CPU compiled directly into its weights, then runs DOOM on it",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-engineer-successfully-compiles-a-32-bit-risc-v-cpu-in-qwen-3-5-4b-llm-inserted-directly-into-its-weights-built-in-cpu-can-run-processor-arithmetic-operations-code-and-of-course-doom",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T13:30:00+00:00",
    "summary": "Qwenputer is an experimental blend of the stock Qwen 3.5 4B LLM with a 32-bit RISC-V CPU compiled and inserted directly into its weights."
  },
  {
    "id": "rss:https://semianalysis.com/2025/09/16/xais-colossus-2-first-gigawatt-datacenter/",
    "domain": "AI 算力 / 半导体",
    "title": "xAI’s Colossus 2 – First Gigawatt Datacenter In The World, Unique RL Methodology, Capital Raise",
    "url": "https://semianalysis.com/2025/09/16/xais-colossus-2-first-gigawatt-datacenter/",
    "source": "AJ Kourabi",
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
    "source": "Ivan Chiam",
    "platform": "rss",
    "points": null,
    "published_at": "2025-09-10T19:57:18+00:00",
    "summary": "Nvidia announced the Rubin CPX, a solution that is specifically designed to be optimized for the prefill phase, with the single-die Rubin CPX heavily emphasizing compute FLOPS over memory bandwidth. T"
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
    "points": 1018,
    "published_at": "2026-10-28T17:01:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:50288019",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Carbon is the new #1 on the Artificial Analysis Intelligence Index v5",
    "url": "https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1",
    "source": "theHocineSaad",
    "platform": "hackernews",
    "points": 338,
    "published_at": "2026-10-29T12:41:56+00:00",
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
    "points": 90,
    "published_at": "2026-11-03T17:55:26+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/tech/1026148/amd-earnings-q3-2026-data-center-pc",
    "domain": "大厂 AI 动态",
    "title": "AMD rides data center riches to &#8216;largest and most profitable&#8217; quarter in history",
    "url": "https://www.theverge.com/tech/1026148/amd-earnings-q3-2026-data-center-pc",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T01:15:34+00:00",
    "summary": "AMD CEO Lisa Su said in the company's quarterly earnings call on Tuesday that Q3 2026 was \"was the largest and most profitable in our history.\" AMD reported a record $13.4 billion in quarterly revenue"
  },
  {
    "id": "rss:https://www.theverge.com/games/1026112/the-legend-of-zelda-ocarina-of-time-remake-nintendo-switch-2-news",
    "domain": "大厂 AI 动态",
    "title": "All the news about The Legend of Zelda: Ocarina of Time remake",
    "url": "https://www.theverge.com/games/1026112/the-legend-of-zelda-ocarina-of-time-remake-nintendo-switch-2-news",
    "source": "Verge Staff",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T01:02:53+00:00",
    "summary": "Ahead of the release of Rockstar Games&#8217; Grand Theft Auto VI, Nintendo is launching its own fall juggernaut: a Switch 2 remake of The Legend of Zelda: Ocarina of Time. The remake, which is releas"
  },
  {
    "id": "rss:https://www.theverge.com/games/1026085/nexus-mods-ai-disclosures",
    "domain": "大厂 AI 动态",
    "title": "The biggest modding site in PC gaming is taking a stance on AI",
    "url": "https://www.theverge.com/games/1026085/nexus-mods-ai-disclosures",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T00:42:10+00:00",
    "summary": "The PC gaming mods repository Nexus Mods is making disclosures about AI mandatory for uploads of new mods, meaning that mod authors will have to declare \"whether AI has been used in their work,\" the s"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1025826/ai-bubble-pimco-apollo-bonds",
    "domain": "大厂 AI 动态",
    "title": "Please stop asking me when the AI bubble will pop",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1025826/ai-bubble-pimco-apollo-bonds",
    "source": "Elizabeth Lopatto",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T23:37:45+00:00",
    "summary": "People, including on this staff, keep asking me with varying degrees of excitement or trepidation when the AI bubble will burst. I'll tell you what I tell them: If I knew that, I would make a life-cha"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1025971/canva-changes-layoffs",
    "domain": "大厂 AI 动态",
    "title": "Canva is announcing changes and layoffs affecting 22 percent of its staff",
    "url": "https://www.theverge.com/tech/1025971/canva-changes-layoffs",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T22:59:36+00:00",
    "summary": "Canva is making significant changes affecting 1,271 people, which is 22 percent of its staff, co-founder and CEO Melanie Perkins announced today. \"For some people, this will mean changes to their role"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1025903/sonos-presets-27voice-ai-early-access",
    "domain": "大厂 AI 动态",
    "title": "Sonos adds new Presets and prepares for the 27voice AI beta",
    "url": "https://www.theverge.com/tech/1025903/sonos-presets-27voice-ai-early-access",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T22:20:50+00:00",
    "summary": "Sonos is rolling out a big app update that includes new Presets and early access to its AI voice assistant. You can create a preset to play music at a specific volume in a certain room, which will app"
  },
  {
    "id": "rss:https://www.theverge.com/games/1025722/valve-steam-game-increase-submissions",
    "domain": "大厂 AI 动态",
    "title": "Valve is making changes to deal with a ‘significant increase’ in Steam game submissions",
    "url": "https://www.theverge.com/games/1025722/valve-steam-game-increase-submissions",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T22:15:33+00:00",
    "summary": "In a new post today, Valve acknowledged that it's seen \"a significant increase in submissions for store and page review in recent months\" and says it's \"running a little behind\" by taking \"up to 12 bu"
  },
  {
    "id": "rss:https://www.theverge.com/news/1025576/binance-cyrpto-theft-explained",
    "domain": "大厂 AI 动态",
    "title": "Binance says hackers used fake job interviews and an internal AI tool to pull off the $6.3 billion heist",
    "url": "https://www.theverge.com/news/1025576/binance-cyrpto-theft-explained",
    "source": "Richard Lawler",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T22:04:02+00:00",
    "summary": "The largest crypto theft to date was pulled off by combining some well-known hacking techniques over the course of a few months, according to Binance. A postmortem from the company says the process st"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1025835/audio-intelligence-live-rewind-siri-recap-apple-watch",
    "domain": "大厂 AI 动态",
    "title": "Here’s what it’s like to use Audio Intelligence on the Apple Watch",
    "url": "https://www.theverge.com/tech/1025835/audio-intelligence-live-rewind-siri-recap-apple-watch",
    "source": "Victoria Song",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T21:21:04+00:00",
    "summary": "It's impossible to paint a full picture of what Audio Intelligence on the Apple Watch Series 12 and Ultra 4 will be right now. The watchOS 27.3 developer beta just dropped earlier this afternoon, and "
  },
  {
    "id": "rss:https://www.theverge.com/tech/1025745/fake-jeff-bezos-hair-replacement-photos-debunk",
    "domain": "大厂 AI 动态",
    "title": "Those Jeff Bezos hair transplant photos are very fake",
    "url": "https://www.theverge.com/tech/1025745/fake-jeff-bezos-hair-replacement-photos-debunk",
    "source": "Jess Weatherbed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T21:01:07+00:00",
    "summary": "Amazon founder Jeff Bezos and actor Jason Statham have a distinctive feature in common: They're both famously bald, and that definitely hasn't changed in the last few days. However, there are some ima"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/03/indias-eloelo-nabs-80m-from-nbc-universal-to-bet-on-the-countrys-rising-microdrama-market/",
    "domain": "大厂 AI 动态",
    "title": "India’s EloElo nabs $80M from NBCUniversal to bet on the country’s rising microdrama market",
    "url": "https://techcrunch.com/2026/11/03/indias-eloelo-nabs-80m-from-nbc-universal-to-bet-on-the-countrys-rising-microdrama-market/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T04:45:00+00:00",
    "summary": "StoryTV has more than 33 million monthly active users according to Sensor Tower figures"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/03/anthropic-is-working-on-a-system-to-prove-ai-models-identity/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic is working on a system to prove AI models’ identity",
    "url": "https://techcrunch.com/2026/11/03/anthropic-is-working-on-a-system-to-prove-ai-models-identity/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T22:41:03+00:00",
    "summary": "Called FlashProve, the system would let anyone check that an AI response really came from the model it claims to be from."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/03/data-centers-are-turning-to-old-jet-engines-as-the-wait-for-power-grows/",
    "domain": "大厂 AI 动态",
    "title": "Data centers are turning to old jet engines as the wait for power grows",
    "url": "https://techcrunch.com/2026/11/03/data-centers-are-turning-to-old-jet-engines-as-the-wait-for-power-grows/",
    "source": "Aditya Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T22:19:53+00:00",
    "summary": "The years-long wait for access to the grid and new turbines is causing data center builders to turn to an unusual, less-efficient and less environmentally friendly solution: once-discarded jet engines"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/03/ted-schleins-ballistic-ventures-seeks-490m-for-new-funds-amid-ai-driven-cybersecurity-boom/",
    "domain": "大厂 AI 动态",
    "title": "Ted Schlein’s Ballistic Ventures seeks $490M for new funds amid AI-driven cybersecurity boom",
    "url": "https://techcrunch.com/2026/11/03/ted-schleins-ballistic-ventures-seeks-490m-for-new-funds-amid-ai-driven-cybersecurity-boom/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T21:43:08+00:00",
    "summary": "Cybersecurity-focused Ballistic Ventures is seeking to raise $360 million for a new flagship fund and another $130 million for a separate investment vehicle."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/03/hiding-inside-palantirs-skyrocketing-quarter-is-a-foreboding-signal/",
    "domain": "大厂 AI 动态",
    "title": "Hiding inside Palantir’s skyrocketing quarter is a foreboding signal",
    "url": "https://techcrunch.com/2026/11/03/hiding-inside-palantirs-skyrocketing-quarter-is-a-foreboding-signal/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T21:05:55+00:00",
    "summary": "Palantir's U.S. commercial revenue surpassed U.S. government revenue for the first time ever."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/03/orbital-matter-3d-printed-the-first-rigid-beam-in-the-vacuum-of-space/",
    "domain": "大厂 AI 动态",
    "title": "Orbital Matter 3D-printed the first rigid beam in the vacuum of space",
    "url": "https://techcrunch.com/2026/11/03/orbital-matter-3d-printed-the-first-rigid-beam-in-the-vacuum-of-space/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T20:57:17+00:00",
    "summary": "An in-space construction first could be an enabler for the space data centers of the future."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/03/researchers-warned-of-north-korean-hacking-tactics-years-before-record-6-3b-binance-heist/",
    "domain": "大厂 AI 动态",
    "title": "Researchers warned of North Korean hacking tactics years before record $6.3B Binance heist",
    "url": "https://techcrunch.com/2026/11/03/researchers-warned-of-north-korean-hacking-tactics-years-before-record-6-3b-binance-heist/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T19:45:48+00:00",
    "summary": "Cybersecurity experts have long warned of the persistent and patient threat from North Korea's long-running hacks. The world's largest crypto exchange was still caught off-guard."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/03/ai-inference-startup-fal-doubles-its-valuation-to-16b-as-demand-surges/",
    "domain": "大厂 AI 动态",
    "title": "AI inference startup Fal doubles its valuation to $16B as demand surges",
    "url": "https://techcrunch.com/2026/11/03/ai-inference-startup-fal-doubles-its-valuation-to-16b-as-demand-surges/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T19:34:43+00:00",
    "summary": "The five-year-old startup raised a $1.3 billion round led by Bessemer."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/03/reddit-tests-ads-in-search-results-as-traffic-declines-and-growth-concerns-mount/",
    "domain": "大厂 AI 动态",
    "title": "Reddit tests ads in search results as traffic declines and growth concerns mount",
    "url": "https://techcrunch.com/2026/11/03/reddit-tests-ads-in-search-results-as-traffic-declines-and-growth-concerns-mount/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T19:24:37+00:00",
    "summary": "The new ad placements could help Reddit squeeze more revenue from existing users as Google's AI search changes how people discover its content."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/03/ten-years-later-pokemon-go-to-the-polls-still-haunts-the-internet/",
    "domain": "大厂 AI 动态",
    "title": "Ten years later, ‘Pokémon Go to the polls’ still haunts the internet",
    "url": "https://techcrunch.com/2026/11/03/ten-years-later-pokemon-go-to-the-polls-still-haunts-the-internet/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T19:04:52+00:00",
    "summary": "Hillary Clinton's 2016 political gaffe has become an irony-shrouded rallying cry for jaded young voters who still dare to hope for change."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/03/ferraris-controversial-luce-ev-is-sold-out-for-2027/",
    "domain": "大厂 AI 动态",
    "title": "Ferrari’s controversial Luce EV is sold out for 2027",
    "url": "https://techcrunch.com/2026/11/03/ferraris-controversial-luce-ev-is-sold-out-for-2027/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T18:51:33+00:00",
    "summary": "The Luce, Ferrari's first electric car and one of its most polarizing models, is \"fully allocated\" through 2027, according to CEO Benedetto Vigna."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/03/netflixs-new-ai-discover-tab-helps-you-find-something-to-watch-based-on-your-mood/",
    "domain": "大厂 AI 动态",
    "title": "Netflix’s new AI Discover tab helps you find something to watch based on your mood",
    "url": "https://techcrunch.com/2026/11/03/netflixs-new-ai-discover-tab-helps-you-find-something-to-watch-based-on-your-mood/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T18:42:16+00:00",
    "summary": "The first experimental feature under the tab will allow users to get recommendations based on what they're currently in the mood for."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/03/crowdstrike-to-shell-out-nearly-500m-for-2-ai-security-startups-as-the-market-for-securing-agents-takes-off/",
    "domain": "大厂 AI 动态",
    "title": "CrowdStrike to shell out nearly $500M for 2 AI security startups as the market for securing agents takes off",
    "url": "https://techcrunch.com/2026/11/03/crowdstrike-to-shell-out-nearly-500m-for-2-ai-security-startups-as-the-market-for-securing-agents-takes-off/",
    "source": "Ram Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T17:56:52+00:00",
    "summary": "CrowdStrike said it will buy Fiddler AI, which makes AI agent observability software, and Dreadnode, which helps companies automate AI security testing."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/03/anthropic-is-still-grappling-with-the-economics-of-compute/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic is still grappling with the economics of compute",
    "url": "https://techcrunch.com/2026/11/03/anthropic-is-still-grappling-with-the-economics-of-compute/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T17:07:01+00:00",
    "summary": "At a moment when Anthropic's compute margins should be getting better, they’re getting worse."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/03/rivian-spinout-also-owns-up-to-mistakes-in-delayed-e-bike-launch/",
    "domain": "大厂 AI 动态",
    "title": "Rivian spinout Also was working on an e-moto project in Kenya — until it walked away",
    "url": "https://techcrunch.com/2026/11/03/rivian-spinout-also-owns-up-to-mistakes-in-delayed-e-bike-launch/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T16:49:09+00:00",
    "summary": "Also co-founder and president Chris Yu told TechCrunch that he wanted to prioritize autonomous vehicles."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/03/google-will-let-schools-disable-its-ai-tools-but-not-without-sacrificing-search/",
    "domain": "大厂 AI 动态",
    "title": "Google will let schools disable its AI tools, but not without sacrificing Search",
    "url": "https://techcrunch.com/2026/11/03/google-will-let-schools-disable-its-ai-tools-but-not-without-sacrificing-search/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T16:30:34+00:00",
    "summary": "Schools choosing to restrict AI altogether will no longer be able to access Google Search, as AI features are now integrated into the search engine."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/03/new-york-citys-mamdani-criticizes-madison-square-garden-owner-over-surveillance-tech/",
    "domain": "大厂 AI 动态",
    "title": "New York City’s Mamdani criticizes Madison Square Garden owner over surveillance tech",
    "url": "https://techcrunch.com/2026/11/03/new-york-citys-mamdani-criticizes-madison-square-garden-owner-over-surveillance-tech/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T16:04:55+00:00",
    "summary": "The mayor's comments come after the entertainment giant's data breach last year, which exposed James Dolan's surveillance."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/03/apple-restricts-dating-apps-and-ai-companions-to-users-18-and-up/",
    "domain": "大厂 AI 动态",
    "title": "Apple restricts dating apps and AI companions to users 18 and up",
    "url": "https://techcrunch.com/2026/11/03/apple-restricts-dating-apps-and-ai-companions-to-users-18-and-up/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T15:38:27+00:00",
    "summary": "Apple's new App Store rules will require 18+ ratings for dating apps and AI companions that offer sexual or romantic content."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/03/the-techcrunch-founder-summit-agenda-is-only-half-the-reason-to-be-in-boston-on-nov-4/",
    "domain": "大厂 AI 动态",
    "title": "The TechCrunch Founder Summit agenda is only half the reason to be in Boston on November 4",
    "url": "https://techcrunch.com/2026/11/03/the-techcrunch-founder-summit-agenda-is-only-half-the-reason-to-be-in-boston-on-nov-4/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T14:30:00+00:00",
    "summary": "On November 4, TechCrunch Founder Summit 2026 brings founders and VCs to Boston's SoWa Power Station for practical insights and connections. Register before prices increase at the door."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/03/tomorrow-techcrunch-founder-summit-takes-over-boston-and-when-pass-rates-increase/",
    "domain": "大厂 AI 动态",
    "title": "Tomorrow: TechCrunch Founder Summit takes over Boston and when pass rates increase",
    "url": "https://techcrunch.com/2026/11/03/tomorrow-techcrunch-founder-summit-takes-over-boston-and-when-pass-rates-increase/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T14:00:00+00:00",
    "summary": "Secure your TechCrunch Founder Summit pass savings before prices increase tomorrow at 9 a.m. ET. Save up to $100 on your pass, and get a second for free."
  },
  {
    "id": "rss:https://stratechery.com/2026/apple-earnings-memory-problems-the-hardware-company-regression/",
    "domain": "大厂 AI 动态",
    "title": "Apple Earnings, Memory Problems, The Hardware Company Regression",
    "url": "https://stratechery.com/2026/apple-earnings-memory-problems-the-hardware-company-regression/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T11:00:00+00:00",
    "summary": "Apple's earnings suggest that the company's hardware business is doing better than ever, even in the face of memory challenges. Does the software story help or hurt?"
  },
  {
    "id": "rss:https://stratechery.com/2026/google-earnings-facebook-deja-vu-the-agent-play/",
    "domain": "大厂 AI 动态",
    "title": "Google Earnings, Facebook Déjà Vu, The Agent Play",
    "url": "https://stratechery.com/2026/google-earnings-facebook-deja-vu-the-agent-play/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T11:00:00+00:00",
    "summary": "Google's earnings miss looks a lot like Facebook's, and that's a credit to Google. The company is being more aggressive than they get credit for."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/11/california-fights-preposterous-trump-admin-demand-to-scrap-state-broadband-laws/",
    "domain": "大厂 AI 动态",
    "title": "California fights \"preposterous\" Trump admin demand to scrap state broadband laws",
    "url": "https://arstechnica.com/tech-policy/2026/11/california-fights-preposterous-trump-admin-demand-to-scrap-state-broadband-laws/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T22:39:37+00:00",
    "summary": "State tries to obtain broadband funds despite rejecting Trump admin condition."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/11/russia-looks-to-hide-data-centers-underground-as-ukrainian-drones-strike-back/",
    "domain": "大厂 AI 动态",
    "title": "Ukraine’s drone strikes spur hasty Russian plans for underground data centers",
    "url": "https://arstechnica.com/ai/2026/11/russia-looks-to-hide-data-centers-underground-as-ukrainian-drones-strike-back/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T20:39:55+00:00",
    "summary": "Russia tries to fix exposed digital infrastructure as data center war backfires."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/11/nyt-demands-brave-shut-down-its-paywall-blocker-and-end-deals-with-ai-firms/",
    "domain": "大厂 AI 动态",
    "title": "NYT demands Brave shut down its paywall blocker and end deals with AI firms",
    "url": "https://arstechnica.com/tech-policy/2026/11/nyt-demands-brave-shut-down-its-paywall-blocker-and-end-deals-with-ai-firms/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T18:30:27+00:00",
    "summary": "Lawsuit calls Brave \"supplier, dealer, and distributor\" of stolen news content."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/11/yes-to-storage-no-to-piano-black-how-car-interior-design-is-changing/",
    "domain": "大厂 AI 动态",
    "title": "Buttons are back and storage is king when it comes to car interiors",
    "url": "https://arstechnica.com/cars/2026/11/yes-to-storage-no-to-piano-black-how-car-interior-design-is-changing/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T18:19:31+00:00",
    "summary": "We talk with Nissan designer Hiren Patel about how vehicle interior designs are changing."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/11/google-will-let-schools-skip-ai-tools-but-they-have-to-give-up-search-too/",
    "domain": "大厂 AI 动态",
    "title": "Google will let schools skip AI tools, but they have to give up search, too",
    "url": "https://arstechnica.com/ai/2026/11/google-will-let-schools-skip-ai-tools-but-they-have-to-give-up-search-too/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T17:54:43+00:00",
    "summary": "Google will offer schools AI tools that purportedly don't give away the answers."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/11/another-child-dies-of-measles-as-cdc-reportedly-holds-up-health-alert/",
    "domain": "大厂 AI 动态",
    "title": "Another child dies of measles as CDC reportedly holds up health alert",
    "url": "https://arstechnica.com/health/2026/11/another-child-dies-of-measles-as-cdc-reportedly-holds-up-health-alert/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T17:21:29+00:00",
    "summary": "NY governor pointed to Kennedy's long-standing anti-vaccine work as spurring outbreaks."
  },
  {
    "id": "rss:https://arstechnica.com/google/2026/11/google-dismantles-botnet-secretly-running-on-1-3-million-android-tv-boxes/",
    "domain": "大厂 AI 动态",
    "title": "Google dismantles botnet secretly running on 1.3 million Android TV boxes",
    "url": "https://arstechnica.com/google/2026/11/google-dismantles-botnet-secretly-running-on-1-3-million-android-tv-boxes/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T17:08:21+00:00",
    "summary": "Google has cut ties with the company behind the botnet campaign."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/11/this-space-company-is-betting-its-future-on-a-propellant-available-everywhere/",
    "domain": "大厂 AI 动态",
    "title": "This space company is betting its future on a propellant available everywhere",
    "url": "https://arstechnica.com/space/2026/11/this-space-company-is-betting-its-future-on-a-propellant-available-everywhere/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T16:50:32+00:00",
    "summary": "Is that water in your spacecraft, or are you just happy to see the delta-V?"
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/11/uefi-bootkit-infected-fully-patched-windows-machines-is-microsoft-to-blame/",
    "domain": "大厂 AI 动态",
    "title": "UEFI bootkit infected fully patched Windows machines. Is Microsoft to blame?",
    "url": "https://arstechnica.com/security/2026/11/uefi-bootkit-infected-fully-patched-windows-machines-is-microsoft-to-blame/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T16:03:13+00:00",
    "summary": "UEFI bootkit BlackX exploits Microsoft's lack of clarity around Secure Boot protections."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/11/trump-wanted-to-give-no-kings-no-air-then-meta-suspended-its-instagram/",
    "domain": "大厂 AI 动态",
    "title": "Trump wanted to give No Kings no air. Then, Meta suspended its Instagram.",
    "url": "https://arstechnica.com/tech-policy/2026/11/trump-wanted-to-give-no-kings-no-air-then-meta-suspended-its-instagram/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T15:39:30+00:00",
    "summary": "Meta faces pressure to protect No Kings Instagram on election day."
  },
  {
    "id": "hn:50346153",
    "domain": "股票",
    "title": "Intel stock collapse worsens as $3.5T chip rout spreads",
    "url": "https://finance.yahoo.com/markets/article/the-intel-stock-collapse-is-getting-worse--and-the-37-trillion-chip-rout-is-spreading-212154947.html",
    "source": "entryleveljobsc",
    "platform": "hackernews",
    "points": 232,
    "published_at": "2026-11-03T00:08:53+00:00",
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
    "id": "hn:50342284",
    "domain": "股票",
    "title": "Oracle files to sell $20B in new stock, bonds to finance AI buildout",
    "url": "https://www.cnbc.com/2026/11/02/oracle-files-to-sell-20-billion-in-new-stock-bonds-to-finance-ai-buildout.html",
    "source": "smartmic",
    "platform": "hackernews",
    "points": 197,
    "published_at": "2026-11-02T19:27:37+00:00",
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
    "id": "hn:50352405",
    "domain": "股票",
    "title": "US Hedge Funds Just Sold Every AI Stock They Bought Since 2025",
    "url": "https://finance.yahoo.com/markets/stocks/articles/us-hedge-funds-just-sold-113114644.html",
    "source": "robin_reala",
    "platform": "hackernews",
    "points": 37,
    "published_at": "2026-11-03T14:27:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:50362274",
    "domain": "股票",
    "title": "AI stocks slide as Texas governor result raises data center risks",
    "url": "https://www.cnbc.com/2026/11/04/ai-stocks-texas-governor-data-centers.html",
    "source": "1659447091",
    "platform": "hackernews",
    "points": 35,
    "published_at": "2026-11-04T07:00:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:50351712",
    "domain": "股票",
    "title": "Anthropic's IPO Filing Warns It May Be 'Imminently' Close to RSI",
    "url": "https://epyhia.com/anthropic-s-ipo-filing-warns-it-may-be-imminently-close-to-recursive",
    "source": "arbuge",
    "platform": "hackernews",
    "points": 30,
    "published_at": "2026-11-03T13:26:43+00:00",
    "summary": ""
  },
  {
    "id": "hn:50348591",
    "domain": "股票",
    "title": "How AI is creating a lopsided US economy",
    "url": "https://www.abc.net.au/news/2026-10-19/ai-stock-market-concentration-data/107261078",
    "source": "gmays",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-11-03T05:58:27+00:00",
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
    "id": "hn:50325107",
    "domain": "股票",
    "title": "The question we should all be asking about AI",
    "url": "https://www.cnn.com/2026/10/30/business/ai-stocks-bonds-debt",
    "source": "heresie-dabord",
    "platform": "hackernews",
    "points": 23,
    "published_at": "2026-11-01T12:44:36+00:00",
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
    "id": "hn:50360067",
    "domain": "金融",
    "title": "Tesla allegedly misled South Korean customers about automated-driving tech",
    "url": "https://www.reuters.com/business/autos-transportation/tesla-misled-south-korean-customers-about-automated-driving-tech-consumer-group-2026-11-04/",
    "source": "EA-3167",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-11-04T00:19:50+00:00",
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
    "id": "hn:50189801",
    "domain": "金融",
    "title": "Tesla profits drop 43% in Q3",
    "url": "https://arstechnica.com/cars/2026/10/tesla-profits-drop-43-in-q3/",
    "source": "throw0101a",
    "platform": "hackernews",
    "points": 87,
    "published_at": "2026-10-22T01:02:23+00:00",
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
    "id": "rss:https://arxiv.org/abs/2310.12255",
    "domain": "金融",
    "title": "Walraswap: equilibrium-based decentralized exchange integrating external AMM liquidity",
    "url": "https://arxiv.org/abs/2310.12255",
    "source": "Sergio A. Yuhjtman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-04T05:00:00+00:00",
    "summary": "arXiv:2310.12255v3 Announce Type: replace Abstract: This article advocates the development of a decentralized exchange protocol for Ethereum based on Walrasian equilibrium. Building on previous work ("
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
    "id": "hn:50295332",
    "domain": "金融",
    "title": "Tesla caught altering specs following rear suspension collapse reports",
    "url": "https://carnewschina.com/2026/09/17/tesla-caught-quietly-altering-model-y-l-manual-specs-following-rear-suspension-collapse-reports/",
    "source": "Alien1Being",
    "platform": "hackernews",
    "points": 26,
    "published_at": "2026-10-29T20:24:13+00:00",
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
    "id": "hn:50202423",
    "domain": "金融",
    "title": "Elon Musk pours $366M into midterm Republican campaigns",
    "url": "https://www.cnbc.com/2026/10/22/elon-musk-midterm-election-spacex-tesla.html",
    "source": "Alien1Being",
    "platform": "hackernews",
    "points": 23,
    "published_at": "2026-10-22T23:17:23+00:00",
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
