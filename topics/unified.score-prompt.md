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

- 今日日期：`2026-11-02`
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
  "date": "2026-11-02",
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
    "points": 2068652,
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
    "points": 1461238,
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
    "points": 1421577,
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
    "points": 1400460,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1VZWc6dECG",
    "domain": "AI",
    "title": "【Re:从零开始的AI学习】第一季总集篇｜从入门到用好 AI",
    "url": "http://www.bilibili.com/video/av117430848391663",
    "source": "卡普迪姆",
    "platform": "bilibili",
    "points": 1144748,
    "published_at": "2026-10-13T00:57:21+00:00",
    "summary": "这次，我把【Re：从零开始的 AI 学习】第一季全 13 期完整连在一起啦！\n新来的朋友或者想要查漏补缺的伙伴，现在可以一口气通关！从 AI 入门与提示词技巧，到 Agent 玩法、主流模型对比与使用成本……跟着走一遍就能彻底搞懂。\n希望这个系列能给你带来哪怕一点点启发，欢迎点赞、投币、收藏一键三连支持！也超级欢迎转发安利给身边的朋友～\n\n【目录】\n00:00 导语\n00:32 AI 这三年发生了"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 887143,
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
    "points": 739436,
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
    "points": 595139,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV1AnQNYxEsy",
    "domain": "AI",
    "title": "MCP是啥？技术原理是什么？一个视频搞懂MCP的一切。Windows系统配置MCP，Cursor Cline使用MCP",
    "url": "http://www.bilibili.com/video/av114155298228756",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 426779,
    "published_at": "2025-03-13T13:18:09+00:00",
    "summary": "MCP是近期的AI领域的热点，特别是在海外社区获得热烈讨论，每天都有大量MCP工具诞生。本期视频我们从MCP的概念，技术原理，到多场景实战，一个视频看懂MCP的全部内容。\n\n\nMCP官方开源仓库：https://github.com/modelcontextprotocol/servers\nMCP合集网站：  https://smithery.ai/\nVscode下载：https://code.v"
  },
  {
    "id": "bvid:BV1REx46NEc4",
    "domain": "AI",
    "title": "【全网最全】DeepSeek Harness超详细教程！50分钟吃透DSH，让SuperAgent给你干活！",
    "url": "http://www.bilibili.com/video/av117540671982699",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 402720,
    "published_at": "2026-11-01T10:22:02+00:00",
    "summary": "DeepSeek Harness超详细教程！\n大家可以速速收藏啦~\n耗时60天制作！感谢大家的三联\n未来还会出其他AI教程，大家可以关注一下~"
  },
  {
    "id": "bvid:BV1ia9UBPESQ",
    "domain": "AI",
    "title": "在VScode中配置Claude Code并接入DeepSeek V4 Pro【oo唠嗑教程】",
    "url": "http://www.bilibili.com/video/av116487012549813",
    "source": "沉默的羔丸ovo",
    "platform": "bilibili",
    "points": 366210,
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
    "points": 343697,
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
    "points": 319331,
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
    "points": 291652,
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
    "points": 281918,
    "published_at": "2026-05-20T11:45:46+00:00",
    "summary": "全B站最详细的 ClaudeCode 桌面版教程，从安装到免登录，中文汉化，接入DeepSeek，安装使用自己的Skill，ClaudeCode真正的AI编程工具，恐怖如斯！\nAgent Skills课程在这里：https://www.bilibili.com/video/BV1ugdgBQED4/?spm_id_from=333.1387.homepage.video_card.click&am"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 223020,
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
    "points": 185520,
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
    "points": 164383,
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
    "points": 151735,
    "published_at": "2025-02-27T03:19:03+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1468g6DEWs",
    "domain": "AI",
    "title": "【全100集】(允许白嫖) 2026最全最细的AI教程零基础入门到精通，一周带你小白变大神！全程干货无废话！存下吧，少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av117115386404821",
    "source": "AI产品经理入门教程-",
    "platform": "bilibili",
    "points": 142501,
    "published_at": "2026-08-18T13:11:45+00:00",
    "summary": "【2026最新版AI教程零基础入门到精通｜配套学习路线+工具包+实战项目，看置顶评论自取】\n 本套教程专为零基础设计，从AI是什么到独立用AI解决实际问题，手把手带你系统走完从入门到精通的完整路径。 ✅ AI认知入门：什么是AI/大模型、它们能做什么不能做什么、别被营销话术忽悠\n✅ 核心技能掌握：提示词工程、多轮对话技巧、让AI稳定输出的方法论\n✅ 进阶能力突破：AI工作流搭建、智能体开发、多工具"
  },
  {
    "id": "bvid:BV1kGo6BdEsT",
    "domain": "AI",
    "title": "如何用Claude Skill 做高质量 PPT（附完整教程）",
    "url": "http://www.bilibili.com/video/av116474832361424",
    "source": "阿西_出海",
    "platform": "bilibili",
    "points": 103824,
    "published_at": "2026-04-27T04:45:20+00:00",
    "summary": "很多人问我上期爆了的那条视频里，那个 PPT 是怎么做的。\n其实我是用 Anthropic 最近出的 Claude Design 做的，这个功能一发出来就在全网传疯了，一条推文就冲上了 6000 多万曝光。\n本期视频我会带你手把手从 0 到 1 把这个Skill 装好，然后一起跑一个成品效果出来。"
  },
  {
    "id": "bvid:BV1dpdZYBE9q",
    "domain": "AI",
    "title": "零代码让AI秒接海量MCP工具！最适合小白的MCP集合平台",
    "url": "http://www.bilibili.com/video/av114340703243255",
    "source": "AI研究室-帆哥",
    "platform": "bilibili",
    "points": 103424,
    "published_at": "2025-04-15T11:00:00+00:00",
    "summary": "最近MCP太火了，阿里直接跟进把MCP整合到百炼平台里面了，做了一个MCP的“应用商店”。\n之前不管是在cursor还是Claude上还是需要配置一下MCP服务器，现在在百炼上就可以直接无脑添加MCP工具，非常方便。\n而且因为在平台上一体化，和大模型可以打包配置，让后端的运维部署变得更轻松。\n这个视频教你怎么用阿里云百炼的MCP工具创建一个agent应用。"
  },
  {
    "id": "bvid:BV1VL3F6pE9K",
    "domain": "AI",
    "title": "0基础入门智能体agent测试：AI测试基础+AI智能体(Agent)测试从零入门全攻略，2026最新版！",
    "url": "http://www.bilibili.com/video/av116991151113881",
    "source": "黑马测试",
    "platform": "bilibili",
    "points": 97991,
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
    "points": 94689,
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
    "points": 94209,
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
    "points": 77346,
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
    "points": 74747,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV19wXvBpEaL",
    "domain": "AI",
    "title": "认真用 Claude Code 的人，迟早会遇见 Everything Claude Code",
    "url": "http://www.bilibili.com/video/av116319122885806",
    "source": "极客魔导师",
    "platform": "bilibili",
    "points": 64094,
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
    "points": 56637,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV14rxM6qEnL",
    "domain": "AI",
    "title": "最新Skills开发教程，Agent skill实战|WorkBuddy+Codex+DeepSeek Harness",
    "url": "http://www.bilibili.com/video/av117511429295044",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 55101,
    "published_at": "2026-10-28T02:00:00+00:00",
    "summary": "【课程简介】Agent Skills零基础教程，从WorkBuddy、Codex上手到项目落地实战。"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 50004,
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
    "points": 47785,
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
    "points": 41961,
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
    "points": 41121,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV1g5nM6tEBf",
    "domain": "AI",
    "title": "DeepSeek V4.1 Flash 接入指南｜六大 Agent 工具一次配好",
    "url": "http://www.bilibili.com/video/av117459403150912",
    "source": "跟着小陈玩AI",
    "platform": "bilibili",
    "points": 38922,
    "published_at": "2026-10-18T02:13:56+00:00",
    "summary": "DeepSeek 发布 V4.1 Flash，跑分反超一众旗舰。本期实测把它接进 DeepSeek Harness、WorkBuddy、Kimi Code、小米 MIMO、ZCode、Codex、Claude Code 等工具，两种配置方法、模型名怎么填、哪里要避坑，一条视频全部讲清。"
  },
  {
    "id": "bvid:BV17Lap6VEUr",
    "domain": "AI",
    "title": "【全80集】Vibe Coding 零基础入门到实战教程，由浅入深（全程干货）",
    "url": "http://www.bilibili.com/video/av117353572468721",
    "source": "数据拾光屋",
    "platform": "bilibili",
    "points": 37489,
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
    "points": 35571,
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
    "points": 34625,
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
    "points": 30721,
    "published_at": "2026-09-28T15:30:36+00:00",
    "summary": "详细的agent部署介绍：https://pan.quark.cn/s/3846914c6da7\n欢迎来到ai的世界！！\n有疑问欢迎私信。"
  },
  {
    "id": "bvid:BV13tuqzwEm9",
    "domain": "AI",
    "title": "一个视频彻底掌握ClaudeCode使用MCP",
    "url": "http://www.bilibili.com/video/av114851586252599",
    "source": "创哥的AI实验室",
    "platform": "bilibili",
    "points": 30084,
    "published_at": "2025-07-14T12:32:55+00:00",
    "summary": "Claude Code命令行的方式，让MCP的操作也令很多朋友感觉不适，这个视频专门做了一些介绍。\n\n希望能帮助到大家。"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29914,
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
    "points": 29029,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 26014,
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
    "points": 25182,
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
    "points": 22843,
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
    "points": 21174,
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
    "points": 18480,
    "published_at": "2026-06-06T11:29:00+00:00",
    "summary": "这一期给大家分享下在codex里面如何配置和使用MCP，和skill一样，MCP也是我们平时用得比较多的，所以建议大家也可以学一下它的基础配置和使用~\n步骤都不难，跟着操作就可以了"
  },
  {
    "id": "bvid:BV1htCnY4ET6",
    "domain": "AI",
    "title": "用 Cursor AI 写 flutter 直接喂设计图就行 | flutter教程",
    "url": "http://www.bilibili.com/video/av113723805008238",
    "source": "独立开发者_猫哥",
    "platform": "bilibili",
    "points": 18176,
    "published_at": "2024-12-27T08:21:35+00:00",
    "summary": "✏️【关于本期视频】\n在上一篇文章《Flutter 使用 Cursor 和 Figma 快速生成界面代码》中，有同学提到他直接使用了设计稿的图片进行生成。我试了一下，效果确实很好。因此，我整理了一些文档，希望对大家有所帮助。\n下图展示了我没有手动编写任何代码实现的消息首页，支持上下滑动刷新数据。\n👉 文档 https://ducafecat.com/blog/use-cursor-ai-flutt"
  },
  {
    "id": "bvid:BV1wpxq6VEXx",
    "domain": "AI",
    "title": "【AI时代的STM32教程】AI Agent 初体验",
    "url": "http://www.bilibili.com/video/av117529699682124",
    "source": "keysking",
    "platform": "bilibili",
    "points": 16031,
    "published_at": "2026-10-30T11:52:06+00:00",
    "summary": "一句话，让 AI 帮我们完成第一个 STM32C5 程序！🚀\n本期我们一起认识 AI Agent，学习如何描述开发需求，并借助开源的 STM32C5DevSkills，让 AI 完成工程创建、芯片配置、代码编写和编译烧录，让律动小板上的小灯闪烁起来！\n也特别感谢 @意法半导体中国   对本系列教程的支持～下期我们再亲手走一遍开发流程，把 Agent 替我们完成的工作，一步步搞明白！"
  },
  {
    "id": "bvid:BV1yyQEBdEkm",
    "domain": "AI",
    "title": "【2026B站最全】Claude Code+软件测试实操教程!看完我直接删了收藏夹所有测试教程,从账号注册到Plan驱动测试项目,小白3天上手！",
    "url": "http://www.bilibili.com/video/av116408092525631",
    "source": "软件测试大神",
    "platform": "bilibili",
    "points": 15476,
    "published_at": "2026-04-15T09:55:02+00:00",
    "summary": "配套资料👉：https://b23.tv/qvhxmaQ\n包括:AI测试网站，几十个AI场景测试完整流程，skil文档，测试八股文，项目源码，测试用例模板，工具安装包，学习计划表，学习路线，100g测试新人资料包等等，资料百分百免费，放心领取~"
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
    "points": 358,
    "published_at": "2026-10-29T17:43:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:50219700",
    "domain": "AI 算力 / 半导体",
    "title": "GPU-unlock: FP/BF16 instruction issue rate on Nvidia 3000's cards",
    "url": "https://github.com/Zagitta/gpu-unlock",
    "source": "fragebogen",
    "platform": "hackernews",
    "points": 351,
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
    "points": 182,
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
    "id": "rss:https://www.eetimes.com/jevon-paradox-and-the-silicon-roadmap/",
    "domain": "AI 算力 / 半导体",
    "title": "Jevons’ Paradox and the Silicon Roadmap",
    "url": "https://www.eetimes.com/jevon-paradox-and-the-silicon-roadmap/",
    "source": "Moshe Zalcberg",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T08:58:48+00:00",
    "summary": "Jevons’ paradox may fuel AI demand, but the silicon roadmap could determine which chips retain their value and which become stranded assets. The post Jevons’ Paradox and the Silicon Roadmap appeared f"
  },
  {
    "id": "rss:https://www.eetimes.com/ai-reshapes-memory-architecture-as-macronix-expands-flash-portfolio/",
    "domain": "AI 算力 / 半导体",
    "title": "AI Reshapes Memory Architecture as Macronix Expands Flash Portfolio",
    "url": "https://www.eetimes.com/ai-reshapes-memory-architecture-as-macronix-expands-flash-portfolio/",
    "source": "EE Times Taiwan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T05:00:00+00:00",
    "summary": "AI-driven high-bandwidth memory demand is reshaping memory markets, boosting mature flash products as Macronix expands its portfolio for AI workloads. The post AI Reshapes Memory Architecture as Macro"
  },
  {
    "id": "rss:https://www.eetimes.com/designing-for-the-long-haul-building-obsolescence-resilient-product-lifecycles/",
    "domain": "AI 算力 / 半导体",
    "title": "Designing for the Long Haul: Building Obsolescence-Resilient Product Lifecycles",
    "url": "https://www.eetimes.com/designing-for-the-long-haul-building-obsolescence-resilient-product-lifecycles/",
    "source": "Rochester Electronics",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T14:00:00+00:00",
    "summary": "Semiconductor obsolescence is a design issue. Engineers protect long-life systems with critical-parts planning, authorized sourcing, and early dialogue. The post Designing for the Long Haul: Building "
  },
  {
    "id": "rss:https://www.eetimes.com/how-small-electronics-manufacturers-prevent-component-shortages/",
    "domain": "AI 算力 / 半导体",
    "title": "How Small Electronics Manufacturers Prevent Component Shortages",
    "url": "https://www.eetimes.com/how-small-electronics-manufacturers-prevent-component-shortages/",
    "source": "MRPeasy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T14:00:00+00:00",
    "summary": "Discover how electronics manufacturers can reduce material shortages by improving inventory accuracy, connecting purchasing to production, and using BOMs. The post How Small Electronics Manufacturers "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/new-ai-driven-windows-malware-feeds-stolen-data-to-claude-to-rank-victims-assets-by-value-then-deletes-itself-payload-builds-custom-target-assessment-can-switch-models-if-one-refuses-or-skip-the-ai-step-entirely",
    "domain": "AI 算力 / 半导体",
    "title": "New AI-driven Windows malware feeds stolen data to Claude to rank victims’ assets by value, then deletes itself",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/new-ai-driven-windows-malware-feeds-stolen-data-to-claude-to-rank-victims-assets-by-value-then-deletes-itself-payload-builds-custom-target-assessment-can-switch-models-if-one-refuses-or-skip-the-ai-step-entirely",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T21:00:00+00:00",
    "summary": "Cisco Talos says the VOLTA infostealer sends stolen victim data to Claude Opus 4.6 to rank assets by monetization value."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/gog-explores-reviving-physical-pc-game-releases-digital-storefront-needs-publisher-approvals-has-to-figure-out-the-logistics-and-legal-challenges",
    "domain": "AI 算力 / 半导体",
    "title": "GOG explores reviving physical PC game releases",
    "url": "https://www.tomshardware.com/video-games/gog-explores-reviving-physical-pc-game-releases-digital-storefront-needs-publisher-approvals-has-to-figure-out-the-logistics-and-legal-challenges",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T18:45:00+00:00",
    "summary": "GOG wants to sell physical games, in contrast to consoles going digital-only, giving gamers more freedom over their games. However, it still has to figure out logistics and publisher permissions."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/snag-a-nintendo-switch-2-for-only-usd469-while-stock-lasts-usd30-off-a-system-thats-not-often-on-sale",
    "domain": "AI 算力 / 半导体",
    "title": "Snag a Nintendo Switch 2 for only $469 while stock lasts — $30 off a system that's not often on sale",
    "url": "https://www.tomshardware.com/pc-components/snag-a-nintendo-switch-2-for-only-usd469-while-stock-lasts-usd30-off-a-system-thats-not-often-on-sale",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T18:09:28+00:00",
    "summary": "Snag a Nintendo Switch 2 for only $469 while stocks last — $30 off a system that's not often on sale"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/lucky-pc-buyer-gets-usd1-200-discount-on-9900x3d-gaming-pc-walmart-honors-usd1-099-shelf-price-on-usd2-299-unit",
    "domain": "AI 算力 / 半导体",
    "title": "Walmart honors massive shelf price mistake, lucky buyer gets two $2,299 CyberPowerPC gaming rigs for $1,099 each",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/lucky-pc-buyer-gets-usd1-200-discount-on-9900x3d-gaming-pc-walmart-honors-usd1-099-shelf-price-on-usd2-299-unit",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T15:53:45+00:00",
    "summary": "Redditor gets a gaming PC at more than 50% off in a physical Walmart retail store."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/brazilian-lawyers-busted-for-attempting-to-manipulate-courts-ai-with-prompt-injection-hidden-in-filing-courts-ai-flags-hidden-text-that-demanded-superficial-legal-scrutiny-lawyers-fined-usd16-000",
    "domain": "AI 算力 / 半导体",
    "title": "Brazilian lawyers busted for attempting to manipulate court's AI with prompt injection hidden in filing",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/brazilian-lawyers-busted-for-attempting-to-manipulate-courts-ai-with-prompt-injection-hidden-in-filing-courts-ai-flags-hidden-text-that-demanded-superficial-legal-scrutiny-lawyers-fined-usd16-000",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T15:05:00+00:00",
    "summary": "The lawyers of a plaintiff in a labor case attempted to use prompt injection to influence the court's AI but were caught. They won the case anyway, as the defendant did not respond, making the move to"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/biwin-m560-2tb-ssd-review",
    "domain": "AI 算力 / 半导体",
    "title": "Biwin M560 2TB SSD Review: The DRAM-less drive to beat",
    "url": "https://www.tomshardware.com/pc-components/ssds/biwin-m560-2tb-ssd-review",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T15:00:00+00:00",
    "summary": "The Biwin M560 brings SMI’s SM2504XT to retail with top-tier responsiveness and excellent efficiency, though not the fastest post-cache writes."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/anycubic-and-thingiverse-announce-exclusive-3d-printing-partnership-makeronline-platform-to-offer-1-click-multicolor-3mf-models",
    "domain": "AI 算力 / 半导体",
    "title": "Anycubic and Thingiverse announce exclusive 3D printing partnership",
    "url": "https://www.tomshardware.com/3d-printing/anycubic-and-thingiverse-announce-exclusive-3d-printing-partnership-makeronline-platform-to-offer-1-click-multicolor-3mf-models",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T15:00:00+00:00",
    "summary": "Thingiverse partners with Anycubic to bring models directly to 3D printers."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/bambu-labs-black-friday-sale-cuts-up-to-usd300-on-the-flagship-h2c-printer-and-more-deep-cuts-across-companys-3d-printer-and-filament-lineup",
    "domain": "AI 算力 / 半导体",
    "title": "Bambu Lab's Black Friday sale cuts up to $300 on the flagship H2C printer and more",
    "url": "https://www.tomshardware.com/3d-printing/bambu-labs-black-friday-sale-cuts-up-to-usd300-on-the-flagship-h2c-printer-and-more-deep-cuts-across-companys-3d-printer-and-filament-lineup",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T14:30:00+00:00",
    "summary": "Strike an early bargain in Bambu Lab's Black Friday sale. Running until December 1st, save up to $300 on their flagship 3D printer."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/sam-altman-travels-to-south-korea-to-meet-samsung-leadership-to-secure-more-ram-for-data-centers-amid-crushing-shortages-openai-ceo-meets-samsung-leadership-to-discuss-future-ai-data-centers",
    "domain": "AI 算力 / 半导体",
    "title": "Sam Altman meets with Samsung leadership to secure more RAM for data centers amid crushing shortages",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/sam-altman-travels-to-south-korea-to-meet-samsung-leadership-to-secure-more-ram-for-data-centers-amid-crushing-shortages-openai-ceo-meets-samsung-leadership-to-discuss-future-ai-data-centers",
    "source": "Newton Gitonga",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T14:21:23+00:00",
    "summary": "OpenAI CEO Sam Altman met with around 50 Samsung executives in South Korea on October 31 to discuss AI's future, business opportunities and the technology's impact on corporate operations. The meeting"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/open-source-usb-tool-unlocks-nvidias-half-speed-gpu-ai-limiter-on-windows-lifts-gpus-fp16-math-performance-up-to-65-percent-uefi-unlocker-covers-rtx-20-30-and-40-series-desktops-and-laptops",
    "domain": "AI 算力 / 半导体",
    "title": "Open-source USB tool unlocks Nvidia's half-speed GPU AI limiter on Windows",
    "url": "https://www.tomshardware.com/pc-components/gpus/open-source-usb-tool-unlocks-nvidias-half-speed-gpu-ai-limiter-on-windows-lifts-gpus-fp16-math-performance-up-to-65-percent-uefi-unlocker-covers-rtx-20-30-and-40-series-desktops-and-laptops",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T14:00:00+00:00",
    "summary": "An open-source UEFI tool, nv-uefi-unlocker, lifts Nvidia’s tensor rate cap on RTX 20, 30, and 40-series GPUs under Windows."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/police-chief-physically-unplugs-flock-cameras-after-the-company-ignores-contract-cancellation-city-takes-matters-into-its-own-hands-amid-privacy-controversies",
    "domain": "AI 算力 / 半导体",
    "title": "Police Chief physically unplugs Flock cameras after the company ignores contract cancellation",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/police-chief-physically-unplugs-flock-cameras-after-the-company-ignores-contract-cancellation-city-takes-matters-into-its-own-hands-amid-privacy-controversies",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T13:55:26+00:00",
    "summary": "The Plymouth City Council was left with no choice but to physically disconnect the cameras after Flock failed to respond to its demands."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/wearable-tech/elon-musk-says-neuralink-is-ready-to-cure-blindness-says-blindsight-will-enable-even-those-who-are-completely-blind-or-have-never-seen-to-see",
    "domain": "AI 算力 / 半导体",
    "title": "Elon Musk says Neuralink's 'BlindSight' is ready to cure blindness",
    "url": "https://www.tomshardware.com/peripherals/wearable-tech/elon-musk-says-neuralink-is-ready-to-cure-blindness-says-blindsight-will-enable-even-those-who-are-completely-blind-or-have-never-seen-to-see",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T13:30:00+00:00",
    "summary": "Neuralink's second product, Blindsight, aims to bring sight back for blind patients, with the company \"just waiting on regulatory approval.\""
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/lenovo-fingerprint-usb-stick-sold-as-aes-256-encrypted-had-a-plain-sd-card-inside-ai-assisted-follow-up-finds-a-backdoor-and-hardcoded-keys-in-other-secure-usb-products",
    "domain": "AI 算力 / 半导体",
    "title": "Lenovo's 'encrypted' fingerprint USB drive is just an unencrypted SD card in a fancy case",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/lenovo-fingerprint-usb-stick-sold-as-aes-256-encrypted-had-a-plain-sd-card-inside-ai-assisted-follow-up-finds-a-backdoor-and-hardcoded-keys-in-other-secure-usb-products",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T13:00:00+00:00",
    "summary": "Lenovo’s ThinkPlus FU100 fingerprint USB drive held an unencrypted SD card, and Codex found fixed keys in other ‘secure’ USB products."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/california-county-secures-autonomous-firefighting-drones-with-500-gallon-foam-payload-to-deal-with-wildfires-five-drone-strike-team-can-be-controlled-by-a-single-operator-conduct-nighttime-ops-and-access-difficult-terrain",
    "domain": "AI 算力 / 半导体",
    "title": "California county deploys autonomous firefighting drones with 500-gallon foam payload to attack wildfires",
    "url": "https://www.tomshardware.com/tech-industry/drones/california-county-secures-autonomous-firefighting-drones-with-500-gallon-foam-payload-to-deal-with-wildfires-five-drone-strike-team-can-be-controlled-by-a-single-operator-conduct-nighttime-ops-and-access-difficult-terrain",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T12:30:00+00:00",
    "summary": "These Seneca drones should help the San Bernardino County Fire Protection District achieve its goal of stopping 90% of fires before they grow larger than 10 square feet."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/space/voyager-1-probe-to-hit-historic-one-light-day-distance-from-earth-in-17-days-49-year-old-spacecraft-travels-16-billion-miles-and-survives-nearly-ten-times-the-length-of-its-original-five-year-mission",
    "domain": "AI 算力 / 半导体",
    "title": "Voyager 1 probe to hit historic one light-day distance from Earth in 17 days — 49-year-old spacecraft travels 16 billion miles",
    "url": "https://www.tomshardware.com/tech-industry/space/voyager-1-probe-to-hit-historic-one-light-day-distance-from-earth-in-17-days-49-year-old-spacecraft-travels-16-billion-miles-and-survives-nearly-ten-times-the-length-of-its-original-five-year-mission",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T12:00:00+00:00",
    "summary": "It took the space probe nearly 50 years to get to one light-day, with NASA scientists and engineers going through lengths to ensure that it could keep operating for as long as possible."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/space/usaf-successfully-tests-dropping-spacex-starfall-cargo-drop-pods-from-space-2-200-pound-capsule-drops-military-supplies-in-the-pacific-to-test-starcraft-like-supply-drops",
    "domain": "AI 算力 / 半导体",
    "title": "USAF successfully tests dropping SpaceX Starfall cargo drop pods from space",
    "url": "https://www.tomshardware.com/tech-industry/space/usaf-successfully-tests-dropping-spacex-starfall-cargo-drop-pods-from-space-2-200-pound-capsule-drops-military-supplies-in-the-pacific-to-test-starcraft-like-supply-drops",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T11:30:00+00:00",
    "summary": "The Rocket Cargo capability should allow U.S. forces to resupply quickly without risking aircrews and equipment, especially in contested areas."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/college-student-unofficially-breaks-world-record-for-fastest-jet-powered-drone-with-491-mph-aircraft-built-in-his-dorm-reaper-aims-to-grab-the-usd800-000-boom-prize",
    "domain": "AI 算力 / 半导体",
    "title": "College student unofficially breaks world record for fastest jet-powered drone with 491 mph aircraft built in his dorm",
    "url": "https://www.tomshardware.com/tech-industry/drones/college-student-unofficially-breaks-world-record-for-fastest-jet-powered-drone-with-491-mph-aircraft-built-in-his-dorm-reaper-aims-to-grab-the-usd800-000-boom-prize",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T11:00:00+00:00",
    "summary": "An undergraduate student from Georgia Tech is trying his hand at an $800k prize for the fastest jet-powered RC aircraft, achieving 790 km/h (491 mph) and breaking the previous world record."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/grab-the-award-winning-bambu-lab-p1s-3d-printer-with-ams-for-usd70-off-save-usd70-on-one-of-the-best-3d-printers-for-beginners",
    "domain": "AI 算力 / 半导体",
    "title": "Grab the award-winning Bambu Lab P1S 3D printer with AMS for $70 off",
    "url": "https://www.tomshardware.com/pc-components/grab-the-award-winning-bambu-lab-p1s-3d-printer-with-ams-for-usd70-off-save-usd70-on-one-of-the-best-3d-printers-for-beginners",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-31T19:19:50+00:00",
    "summary": "The Bambu Lab P1S earned our Editor's Choice recognition in testing, and this discounted bundle gives you access to its high-speed printing capabilities alongside the convenience of the AMS color prin"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/social-media/french-lawmakers-approve-usd11-2-billion-internet-tax-based-on-traffic-usage-costs-usd0-65-per-gigabyte-of-content-accessed-us-tech-giants-like-google-and-meta-face-new-levies-on-content-delivered-to-french-subscribers",
    "domain": "AI 算力 / 半导体",
    "title": "French lawmakers add $11.2 billion internet tax based on traffic usage to budget, costs $0.06 per gigabyte of content accessed",
    "url": "https://www.tomshardware.com/software/social-media/french-lawmakers-approve-usd11-2-billion-internet-tax-based-on-traffic-usage-costs-usd0-65-per-gigabyte-of-content-accessed-us-tech-giants-like-google-and-meta-face-new-levies-on-content-delivered-to-french-subscribers",
    "source": "Newton Gitonga",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-31T16:11:40+00:00",
    "summary": "French lawmakers have approved an amendment proposing a €0.055-per-gigabyte tax on digital content delivered to internet subscribers in France. The measure could generate an estimated €10 billion annu"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/ghost-students-using-ai-to-apply-for-student-loans-with-stolen-identities-dojs-operation-ghostbusters-busts-usd200-million-ring-faking-online-college-attendance-unsuspecting-victims-saddled-with-student-debt-they-didnt-sign-up-for",
    "domain": "AI 算力 / 半导体",
    "title": "'Ghost Students' using AI to apply for student loans with stolen identities, DOJ's Operation Ghostbusters busts $200 million ring",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/ghost-students-using-ai-to-apply-for-student-loans-with-stolen-identities-dojs-operation-ghostbusters-busts-usd200-million-ring-faking-online-college-attendance-unsuspecting-victims-saddled-with-student-debt-they-didnt-sign-up-for",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-31T15:37:41+00:00",
    "summary": "Fraudsters are using the identities of high school graduates who skipped college to apply for student loans and steal the excess proceeds that do not go to schools. They use AI to keep the charade goi"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/grab-a-new-3d-printer-this-halloween-weekend-with-prices-as-low-as-usd199-big-discounts-from-elegoo-creality-prusa-and-more-with-filament-and-resin-printers-and-consumables-on-sale",
    "domain": "AI 算力 / 半导体",
    "title": "Grab a new 3D printer this Halloween weekend, with prices as low as $199",
    "url": "https://www.tomshardware.com/3d-printing/grab-a-new-3d-printer-this-halloween-weekend-with-prices-as-low-as-usd199-big-discounts-from-elegoo-creality-prusa-and-more-with-filament-and-resin-printers-and-consumables-on-sale",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-31T14:00:00+00:00",
    "summary": "Pick up a bargain 3D printer, thanks to these big discounts on resin and filament 3DP models from big names like Creality, Elegoo, Prusa and more."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/motherboards/asrock-b860-challenger-wifi-motherboard-review",
    "domain": "AI 算力 / 半导体",
    "title": "ASRock B860 Challenger Wifi Motherboard Review: Entry-level ATX at a great price, with drawbacks",
    "url": "https://www.tomshardware.com/pc-components/motherboards/asrock-b860-challenger-wifi-motherboard-review",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-31T14:00:00+00:00",
    "summary": "ASRock’s B860 Challenger Wifi covers the basics and performs well, but slower USB ports, weaker VRMs, and a dated BIOS keep it from standing out, even at the lower price."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/firm-that-lets-you-rent-out-your-idle-mac-for-ai-inference-workloads-warns-of-plummeting-token-costs-darkbloom-network-sees-earnings-drop-to-usd1-23-a-day-as-anthropic-tokens-fall-77-percent",
    "domain": "AI 算力 / 半导体",
    "title": "Firm that lets you rent out your idle Mac for AI inference workloads warns of plummeting token costs",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/firm-that-lets-you-rent-out-your-idle-mac-for-ai-inference-workloads-warns-of-plummeting-token-costs-darkbloom-network-sees-earnings-drop-to-usd1-23-a-day-as-anthropic-tokens-fall-77-percent",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-31T13:49:09+00:00",
    "summary": "Mac users sharing their compute for AI inference are seeing declining revenues as token prices continue to drop, with Anthropic token falling 77% in under five months."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/this-week-in-toms-hardware-premium-october-31-2026-vera-cpus-available-on-oracle-clusters-building-an-agentic-cpu-benchmark-and-a-primer-to-llms",
    "domain": "AI 算力 / 半导体",
    "title": "This week in Tom's Hardware Premium: October 31, 2026",
    "url": "https://www.tomshardware.com/tech-industry/this-week-in-toms-hardware-premium-october-31-2026-vera-cpus-available-on-oracle-clusters-building-an-agentic-cpu-benchmark-and-a-primer-to-llms",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-31T13:30:00+00:00",
    "summary": "In case you're not yet subscribed to our Tom's Hardware Premium subscription service, here's what you've been missing out on this week"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-shifts-production-capacity-from-consumer-to-server-cpus-in-face-of-unprecedented-ai-demand-company-navigating-one-of-the-most-significant-supply-shortages-in-history",
    "domain": "AI 算力 / 半导体",
    "title": "Intel shifts production capacity from consumer to server CPUs in face of 'unprecedented' AI demand",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-shifts-production-capacity-from-consumer-to-server-cpus-in-face-of-unprecedented-ai-demand-company-navigating-one-of-the-most-significant-supply-shortages-in-history",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-31T13:00:00+00:00",
    "summary": "Intel is expanding chipmaking and advanced packaging capacity across the U.S., Ireland, and Malaysia to meet surging AI-driven demand for data center CPUs amid shrinking PC market and persistent suppl"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/developer-builds-a-complete-intel-486-pc-emulator-in-a-browser-100-percent-pure-javascript-retro486-includes-modular-tabs-for-screen-motherboard-storage-expansion-cards-and-more",
    "domain": "AI 算力 / 半导体",
    "title": "Developer builds a complete Intel 486 PC emulator in a browser",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/developer-builds-a-complete-intel-486-pc-emulator-in-a-browser-100-percent-pure-javascript-retro486-includes-modular-tabs-for-screen-motherboard-storage-expansion-cards-and-more",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-31T12:40:00+00:00",
    "summary": "A developer has created a full Intel 486 PC system, using 100% pure-JavaScript, in a browser."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/startup-uses-ai-agent-to-perform-controversial-brain-surgery-on-a-mouse-anthropic-sonnet-controlled-motorized-surgery-rig-ai-given-free-reign-to-treat-epilepsy-with-a-range-of-gene-therapy-vectors-after-opus-5-5-refused-to-conduct-biological-experiment",
    "domain": "AI 算力 / 半导体",
    "title": "AI agent used to perform controversial brain surgery on a mouse, Anthropic Sonnet controlled motorized surgery rig",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/startup-uses-ai-agent-to-perform-controversial-brain-surgery-on-a-mouse-anthropic-sonnet-controlled-motorized-surgery-rig-ai-given-free-reign-to-treat-epilepsy-with-a-range-of-gene-therapy-vectors-after-opus-5-5-refused-to-conduct-biological-experiment",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-31T12:00:00+00:00",
    "summary": "The team had to use Sonnet after Opus 5.5 outright refused to run the experiment, while Opus 5 warned that it could stop working in the midst of the operation."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/veteran-microsoft-engineer-makes-his-own-ram-from-scratch-using-ai-attempts-to-build-4mb-of-1970s-pdp-11-ram-from-scratch",
    "domain": "AI 算力 / 半导体",
    "title": "Veteran Microsoft engineer makes his own RAM from scratch using AI",
    "url": "https://www.tomshardware.com/pc-components/ram/veteran-microsoft-engineer-makes-his-own-ram-from-scratch-using-ai-attempts-to-build-4mb-of-1970s-pdp-11-ram-from-scratch",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-31T11:40:00+00:00",
    "summary": "Expensive memory forces former Microsoft engineer to make his own — Dave Plummer makes PDP-11 RAM from scratch"
  },
  {
    "id": "rss:https://www.eetimes.com/google-agentic-ai-will-drive-new-demands-on-data-center-cpus/",
    "domain": "AI 算力 / 半导体",
    "title": "Google: Agentic AI Will Drive New Demands on Data Center CPUs",
    "url": "https://www.eetimes.com/google-agentic-ai-will-drive-new-demands-on-data-center-cpus/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T20:13:41+00:00",
    "summary": "Agents present a bursty workload, leaving CPUs frequently idle, which is placing new demands on CPU infrastructure. The post Google: Agentic AI Will Drive New Demands on Data Center CPUs appeared firs"
  },
  {
    "id": "rss:https://www.eetimes.com/intels-q3-results-show-supply-chain-disruptions-and-pc-plunge/",
    "domain": "AI 算力 / 半导体",
    "title": "Intel’s Q3 Results Show Supply Chain Disruptions and PC Plunge",
    "url": "https://www.eetimes.com/intels-q3-results-show-supply-chain-disruptions-and-pc-plunge/",
    "source": "News Desk",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T16:37:20+00:00",
    "summary": "Intel faces a tough challenge as manufacturing bottlenecks and rising memory costs impact PC sales despite strong data center growth. The post Intel’s Q3 Results Show Supply Chain Disruptions and PC P"
  },
  {
    "id": "rss:https://www.eetimes.com/why-shrinking-component-geometries-force-a-rethink-of-bga-rework-heating-methods/",
    "domain": "AI 算力 / 半导体",
    "title": "Why Shrinking Component Geometries Force a Rethink of BGA Rework Heating Methods",
    "url": "https://www.eetimes.com/why-shrinking-component-geometries-force-a-rethink-of-bga-rework-heating-methods/",
    "source": "Emily Newton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T10:32:26+00:00",
    "summary": "As components shrink to 01005 scale and board densities rise, BGA rework requires more precise heat control. The post Why Shrinking Component Geometries Force a Rethink of BGA Rework Heating Methods a"
  },
  {
    "id": "rss:https://www.eetimes.com/infineons-oktobertech-edge-ai-sdvs-and-the-road-to-800-vdc/",
    "domain": "AI 算力 / 半导体",
    "title": "Infineon’s OktoberTech: Edge AI, SDVs, and the Road to 800 VDC",
    "url": "https://www.eetimes.com/infineons-oktobertech-edge-ai-sdvs-and-the-road-to-800-vdc/",
    "source": "Aalyia Shaukat",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T20:59:28+00:00",
    "summary": "Explore Infineon’s OktoberTech takeaways on edge AI, SDVs, GaN power, and the shift toward 800 V DC data centers. The post Infineon’s OktoberTech: Edge AI, SDVs, and the Road to 800 VDC appeared first"
  },
  {
    "id": "rss:https://www.eetimes.com/samsung-electronics-posts-80b-operating-profit-on-ai-memory-demand/",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung Electronics Posts $80B Operating Profit on AI Memory Demand",
    "url": "https://www.eetimes.com/samsung-electronics-posts-80b-operating-profit-on-ai-memory-demand/",
    "source": "News Desk",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T16:20:34+00:00",
    "summary": "Samsung reported third-quarter operating profit of $80 billion, but rising component prices caused an operating loss in mobile. The post Samsung Electronics Posts $80B Operating Profit on AI Memory De"
  },
  {
    "id": "rss:https://www.eetimes.com/how-vision-and-connectivity-enable-autonomous-agriculture/",
    "domain": "AI 算力 / 半导体",
    "title": "How Vision and Connectivity Enable Autonomous Agriculture",
    "url": "https://www.eetimes.com/how-vision-and-connectivity-enable-autonomous-agriculture/",
    "source": "Analog Devices, Arrow Electronics",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T16:07:54+00:00",
    "summary": "Join this webinar to explore how Gigabit Multimedia Serial Link (GMSL) technology helps enable the next generation of autonomous agricultural equipment. The post How Vision and Connectivity Enable Aut"
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
    "id": "rss:https://semianalysis.com/2025/09/08/huawei-ascend-production-ramp/",
    "domain": "AI 算力 / 半导体",
    "title": "Huawei Ascend Production Ramp: Die Banks, TSMC Continued Production, HBM is The Bottleneck",
    "url": "https://semianalysis.com/2025/09/08/huawei-ascend-production-ramp/",
    "source": "Jeff Koch",
    "platform": "rss",
    "points": null,
    "published_at": "2025-09-08T09:54:57+00:00",
    "summary": "Compute is the lifeblood of AI. He who controls the spice controls the universe the compute will control the production of tokens and reap the benefits of AI. Without compute you do not have a seat at"
  },
  {
    "id": "rss:https://semianalysis.com/2025/09/03/amazons-ai-resurgence-aws-anthropics-multi-gigawatt-trainium-expansion/",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon’s AI Resurgence: AWS & Anthropic’s Multi-Gigawatt Trainium Expansion",
    "url": "https://semianalysis.com/2025/09/03/amazons-ai-resurgence-aws-anthropics-multi-gigawatt-trainium-expansion/",
    "source": "Myron Xie",
    "platform": "rss",
    "points": null,
    "published_at": "2025-09-03T20:55:46+00:00",
    "summary": "Two-and-a-half years ago, we flagged a looming “cloud crisis” at AWS. Today, the evidence has mounted. AWS is the crown jewel of the Amazon empire, generating ~60% of group profits, and dominating the"
  },
  {
    "id": "rss:https://semianalysis.com/2025/08/20/h100-vs-gb200-nvl72-training-benchmarks/",
    "domain": "AI 算力 / 半导体",
    "title": "H100 vs GB200 NVL72 Training Benchmarks – Power, TCO, and Reliability Analysis, Software Improvement Over Time",
    "url": "https://semianalysis.com/2025/08/20/h100-vs-gb200-nvl72-training-benchmarks/",
    "source": "Daniel Nishball",
    "platform": "rss",
    "points": null,
    "published_at": "2025-08-20T04:56:35+00:00",
    "summary": "Frontier model training has pushed GPUs and AI systems to their absolute limits, making cost, efficiency, power, performance per TCO, and reliability central to the discussion on effective training. T"
  },
  {
    "id": "rss:https://semianalysis.com/2025/08/13/gpt-5-ad-monetization-and-the-superapp/",
    "domain": "AI 算力 / 半导体",
    "title": "GPT-5 Set the Stage for Ad Monetization and the SuperApp",
    "url": "https://semianalysis.com/2025/08/13/gpt-5-ad-monetization-and-the-superapp/",
    "source": "AJ Kourabi",
    "platform": "rss",
    "points": null,
    "published_at": "2025-08-13T00:27:14+00:00",
    "summary": "To many power users (Pro and Plus), GPT5 was a disappointing release. But with closer inspection, the real release is focused on the vast majority of ChatGPT’s users, which is the 700m+ free userbase "
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
    "points": 1017,
    "published_at": "2026-10-28T17:01:23+00:00",
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
    "id": "rss:https://www.theverge.com/tech/1023173/jackery-explorer-100d-portable-power-station-battery-lithium-iron-phosphate",
    "domain": "大厂 AI 动态",
    "title": "Jackery made its portable power stations even smaller",
    "url": "https://www.theverge.com/tech/1023173/jackery-explorer-100d-portable-power-station-battery-lithium-iron-phosphate",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T05:00:00+00:00",
    "summary": "Jackery announced a new portable power station that uses the safer and longer-lasting lithium iron phosphate (LFP) batteries the company first introduced in 2023. But what makes the new Explorer 100D "
  },
  {
    "id": "rss:https://www.theverge.com/science/1024239/nasa-commercial-space-save-hubble",
    "domain": "大厂 AI 动态",
    "title": "NASA hopes the commercial space industry can help save Hubble",
    "url": "https://www.theverge.com/science/1024239/nasa-commercial-space-save-hubble",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T21:09:21+00:00",
    "summary": "Gravity is a cruel mistress, slowly dragging the famed telescope ever closer to its ultimate demise with every day. Hubble is in no immediate danger of burning up in the Earth's atmosphere, but its ti"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1024232/flock-ignoring-cancel-contracts",
    "domain": "大厂 AI 动态",
    "title": "Flock keeps ignoring requests to cancel its contracts",
    "url": "https://www.theverge.com/tech/1024232/flock-ignoring-cancel-contracts",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T19:58:02+00:00",
    "summary": "While more cities are canceling their contracts with Flock Safety, just as many are discovering how difficult that can be in some instances. Plymouth, Minnesota's city council voted to terminate its c"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1024219/apples-homeview-could-add-security-camera-features",
    "domain": "大厂 AI 动态",
    "title": "Apple’s HomeView could add security camera features",
    "url": "https://www.theverge.com/tech/1024219/apples-homeview-could-add-security-camera-features",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T17:16:07+00:00",
    "summary": "Reddit user pdfu found hints hidden in the HomeView 27.2 code that Apple could be adding security camera features to its smart home hub. The strings describe a security camera mode with motion detecti"
  },
  {
    "id": "rss:https://www.theverge.com/games/1024206/playable-portal-prequel-f-stop-leak",
    "domain": "大厂 AI 动态",
    "title": "A fully playable version of Portal prequel F-Stop leaked",
    "url": "https://www.theverge.com/games/1024206/playable-portal-prequel-f-stop-leak",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T16:19:21+00:00",
    "summary": "Leakers have pieced together a playable version of the canceled Portal prequel F-Stop. Most of the assets came from the massive 12-terabyte leak that dropped this August. That didn't include the game'"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1024176/north-korea-binance-crypto-heist",
    "domain": "大厂 AI 动态",
    "title": "North Korea linked to massive Binance crypto heist",
    "url": "https://www.theverge.com/tech/1024176/north-korea-binance-crypto-heist",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T14:33:11+00:00",
    "summary": "The FBI says North Korea was behind the massive $6.3 billion crypto heist that hit Binance on October 29th. The FBI labeled the activity \"TraderTraitor\" and said that it had observed actors it has con"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1024108/homepod-mini-2-hands-on-siri-smart-home-mac-speaker",
    "domain": "大厂 AI 动态",
    "title": "HomePod Mini 2 first look: Three things I love and one disappointment",
    "url": "https://www.theverge.com/tech/1024108/homepod-mini-2-hands-on-siri-smart-home-mac-speaker",
    "source": "Jennifer Pattison Tuohy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T14:00:00+00:00",
    "summary": "When I first heard about the new $149 HomePod Mini 2 at Apple's Welcome Home event last month, I was disappointed. It's been six years since Apple launched its entry-level smart speaker, and all it go"
  },
  {
    "id": "rss:https://www.theverge.com/column/1022402/new-zelda-and-gta-represent-a-games-industry-that-no-longer-exists",
    "domain": "大厂 AI 动态",
    "title": "New Zelda and GTA represent a games industry that no longer exists",
    "url": "https://www.theverge.com/column/1022402/new-zelda-and-gta-represent-a-games-industry-that-no-longer-exists",
    "source": "Andrew Webster",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T13:00:00+00:00",
    "summary": "This is The Stepback, a weekly newsletter breaking down one essential story from the tech world. For more on the biggest game releases of the year, follow Andrew Webster. The Stepback arrives in our s"
  },
  {
    "id": "rss:https://www.theverge.com/policy/1023877/prop-45-california-data-centers-energy",
    "domain": "大厂 AI 动态",
    "title": "Prop 45 in California could be hiding a loophole for data centers",
    "url": "https://www.theverge.com/policy/1023877/prop-45-california-data-centers-energy",
    "source": "Justine Calma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T13:00:00+00:00",
    "summary": "A high-stakes California ballot measure pitched as a fast track for \"essential\" infrastructure could wind up giving data center developers a loophole to evade public scrutiny, environmental advocates "
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/1024096/halloween-spirit-youtube-horror",
    "domain": "大厂 AI 动态",
    "title": "Get in the spooky spirit with these horrors from YouTube",
    "url": "https://www.theverge.com/entertainment/1024096/halloween-spirit-youtube-horror",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-31T21:06:58+00:00",
    "summary": "Rather than recommend a single horror film or an unsettling album for our final installment of spooky season recs, I present you with a small selection of creepy, disturbing, and just plain weird vide"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/01/borrowed-reading-stories-from-our-extended-colleagues/",
    "domain": "大厂 AI 动态",
    "title": "Borrowed reading: stories from our extended colleagues",
    "url": "https://techcrunch.com/2026/11/01/borrowed-reading-stories-from-our-extended-colleagues/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T04:23:48+00:00",
    "summary": "Five stories worth your time from our extended colleagues at CIO, Computerworld, Macworld, and PCWorld."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/01/openai-might-rebrand-its-data-centers-as-ai-compute-campuses/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI might rebrand its data centers as ‘AI compute campuses’",
    "url": "https://techcrunch.com/2026/11/01/openai-might-rebrand-its-data-centers-as-ai-compute-campuses/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T21:55:23+00:00",
    "summary": "Data centers are deeply unpopular. But what if we called them something else?"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/01/ai-can-make-tech-ceos-lives-easier-what-about-everyone-else/",
    "domain": "大厂 AI 动态",
    "title": "AI can make tech CEOs’ lives easier. What about everyone else?",
    "url": "https://techcrunch.com/2026/11/01/ai-can-make-tech-ceos-lives-easier-what-about-everyone-else/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T20:57:58+00:00",
    "summary": "On Equity, we discuss why tech CEO statements can seem so tone deaf."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/01/techcrunch-mobility-a-new-bigger-av-boom-is-here/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Mobility: A new, bigger AV boom is here",
    "url": "https://techcrunch.com/2026/11/01/techcrunch-mobility-a-new-bigger-av-boom-is-here/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T17:04:00+00:00",
    "summary": "Welcome back to TechCrunch Mobility, your hub for the future of transportation and now, more than ever, the role AI is playing in it."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/01/binance-resumes-withdrawals-following-6-3-billion-breach/",
    "domain": "大厂 AI 动态",
    "title": "Binance resumes withdrawals following $6.3 billion breach",
    "url": "https://techcrunch.com/2026/11/01/binance-resumes-withdrawals-following-6-3-billion-breach/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T16:20:10+00:00",
    "summary": "The cryptocurrency exchange said it's now covered 95% of the stolen assets."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/01/pixel-11-pro-fold-sturdy-rectengale-in-a-wide-wide-world/",
    "domain": "大厂 AI 动态",
    "title": "Pixel 11 Pro Fold: Sturdy rectangle in a wide wide world",
    "url": "https://techcrunch.com/2026/11/01/pixel-11-pro-fold-sturdy-rectengale-in-a-wide-wide-world/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T15:00:00+00:00",
    "summary": "Google made a sturdy phone, but there is increasing competition in the foldable world."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/01/heres-what-renoa-the-first-new-fiber-in-25-years-feels-like/",
    "domain": "大厂 AI 动态",
    "title": "Here’s what ‘renoa’ — the first new fiber in 25 years — feels like",
    "url": "https://techcrunch.com/2026/11/01/heres-what-renoa-the-first-new-fiber-in-25-years-feels-like/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T14:00:00+00:00",
    "summary": "Startup Everbloom's new material, renoa, is the first new fiber in 25 years, and it feels very familiar."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/31/data-centers-are-now-a-midterm-issue-even-in-brooklyn/",
    "domain": "大厂 AI 动态",
    "title": "Data centers are now a midterm issue, even in Brooklyn",
    "url": "https://techcrunch.com/2026/10/31/data-centers-are-now-a-midterm-issue-even-in-brooklyn/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T02:22:10+00:00",
    "summary": "At a Brooklyn midterm party five days before Election Day, every conversation, from a council member’s fireside chat to a debate about the Democratic Party, kept circling back to AI and data centers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/31/apple-ceo-says-the-company-doesnt-want-to-ship-ai-for-ais-sake/",
    "domain": "大厂 AI 动态",
    "title": "Apple CEO says the company doesn’t ‘want to ship AI for AI’s sake’",
    "url": "https://techcrunch.com/2026/10/31/apple-ceo-says-the-company-doesnt-want-to-ship-ai-for-ais-sake/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-31T21:41:00+00:00",
    "summary": "Apple's new CEO defended the company's current position in the AI landscape."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/31/4-days-left-how-techcrunch-founder-summit-helps-you-make-more-useful-connections-to-scale/",
    "domain": "大厂 AI 动态",
    "title": "4 days left: How TechCrunch Founder Summit helps you make more useful connections to scale",
    "url": "https://techcrunch.com/2026/10/31/4-days-left-how-techcrunch-founder-summit-helps-you-make-more-useful-connections-to-scale/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-31T21:36:07+00:00",
    "summary": "On November 4 at Boston’s SoWa Power Station, get ready for a full day packed with meaningful networking opportunities, actionable insights, and connections that could change the trajectory of your id"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/31/judge-allows-naacp-lawsuit-over-xai-data-center-pollution-to-move-forward/",
    "domain": "大厂 AI 动态",
    "title": "Judge allows NAACP lawsuit over xAI data center pollution to move forward",
    "url": "https://techcrunch.com/2026/10/31/judge-allows-naacp-lawsuit-over-xai-data-center-pollution-to-move-forward/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-31T21:17:03+00:00",
    "summary": "An NAACP lawsuit accuses the SpaceX-owned AI company of violating the Clean Air Act."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/31/openai-reportedly-lowers-funding-target-for-new-round/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI reportedly lowers funding target for new round",
    "url": "https://techcrunch.com/2026/10/31/openai-reportedly-lowers-funding-target-for-new-round/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-31T16:12:55+00:00",
    "summary": "OpenAI’s latest funding round doesn't seem to be living up to expectations."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/31/tiktoks-road-to-becoming-a-super-app/",
    "domain": "大厂 AI 动态",
    "title": "From restaurant guides to payments, here’s how TikTok is building a super app",
    "url": "https://techcrunch.com/2026/10/31/tiktoks-road-to-becoming-a-super-app/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-31T15:41:57+00:00",
    "summary": "TikTok may be working to become the app that people use for most of their digital activities."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/31/i-took-two-iphones-on-vacation-the-duo-won-me-over/",
    "domain": "大厂 AI 动态",
    "title": "I took two iPhones on vacation. The Duo won me over.",
    "url": "https://techcrunch.com/2026/10/31/i-took-two-iphones-on-vacation-the-duo-won-me-over/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-31T14:00:00+00:00",
    "summary": "The iPhone Duo has its frustrations, but it’s also fun and engaging enough that I didn’t want to switch back to my Pro Max."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/10/seabirds-racing-home-over-the-ocean-can-get-jet-lagged/",
    "domain": "大厂 AI 动态",
    "title": "Seabirds racing home over the ocean can get jet-lagged",
    "url": "https://arstechnica.com/science/2026/10/seabirds-racing-home-over-the-ocean-can-get-jet-lagged/",
    "source": "Jacek Krywko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-31T11:15:26+00:00",
    "summary": "A long flight home from feeding grounds messes with birds' internal clocks."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/10/the-fda-wants-to-pull-its-approval-of-a-drug-its-not-so-easy/",
    "domain": "大厂 AI 动态",
    "title": "The FDA wants to pull its approval of a drug. It’s not so easy.",
    "url": "https://arstechnica.com/science/2026/10/the-fda-wants-to-pull-its-approval-of-a-drug-its-not-so-easy/",
    "source": "Sara Talpos, Undark Magazine",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-31T11:02:34+00:00",
    "summary": "The regulator says Tavneos was approved on the basis of manipulated study data. Should patients still have access to it?"
  },
  {
    "id": "rss:https://www.producthunt.com/products/help-381",
    "domain": "大厂 AI 动态",
    "title": "Help",
    "url": "https://www.producthunt.com/products/help-381",
    "source": "Chris Messina",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T07:05:48+00:00",
    "summary": "The app designed for targeted and transparent help Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/friday-work",
    "domain": "大厂 AI 动态",
    "title": "Friday Work",
    "url": "https://www.producthunt.com/products/friday-work",
    "source": "Arun Dass",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T22:55:35+00:00",
    "summary": "When Claude hits its limit, your task keeps going Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/xmind",
    "domain": "大厂 AI 动态",
    "title": "Xmind 2027",
    "url": "https://www.producthunt.com/products/xmind",
    "source": "Justin Jincaid",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T00:24:06+00:00",
    "summary": "Your mind map is now an AI thinking partner Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/agent-inbox",
    "domain": "大厂 AI 动态",
    "title": "Agent Inbox",
    "url": "https://www.producthunt.com/products/agent-inbox",
    "source": "Dima Grossman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T12:10:54+00:00",
    "summary": "Give your agent an email address, Slack and Telegram handle Discussion | Link"
  },
  {
    "id": "rss:https://sspai.com/post/118122",
    "domain": "大厂 AI 动态",
    "title": "TDS REVIEW｜Apple AirPods 5 半入耳降噪真无线耳机体验",
    "url": "https://sspai.com/post/118122",
    "source": "KingTsui",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T07:00:00+00:00",
    "summary": "这篇文章是TDSStudio在少数派上的第34篇文章，依然是全平台首发。时隔两年，我们又回来写AirPods半入耳型号了。在26年的苹果秋季event上，AirPods5给我们最大的印象其实还是主动降 ...查看全文"
  },
  {
    "id": "rss:https://sspai.com/post/115662",
    "domain": "大厂 AI 动态",
    "title": "Xnip 十周年：长截图的新生，也是新的起点",
    "url": "https://sspai.com/post/115662",
    "source": "lyx",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T03:00:41+00:00",
    "summary": "十年是一个里程碑，也是新的起点。查看全文"
  },
  {
    "id": "rss:https://sspai.com/post/118191",
    "domain": "大厂 AI 动态",
    "title": "派早报：Apple 智能将随 iOS 27.3 登陆中国",
    "url": "https://sspai.com/post/118191",
    "source": "少数派编辑部",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T23:22:45+00:00",
    "summary": "Apple 智能将随 iOS 27.3 登陆中国苹果对闪存的议价权受到压制Claude Code 官方扩展被植入后门美国 FCC 禁止中国实验室认证输美电子产品百度网盘通过磁力计数据规避「摇一摇」广告权限币安 63 亿美元资产被盗看看就行的简讯少数派的近期动态你可能错过的好文章查看全文"
  },
  {
    "id": "rss:https://sspai.com/post/116991",
    "domain": "大厂 AI 动态",
    "title": "怀旧手记｜夏普 Telios：20 多年前，Handheld PC 中的「少数派」",
    "url": "https://sspai.com/post/116991",
    "source": "随便好啦",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T07:02:46+00:00",
    "summary": "Matrix首页推荐Matrix是少数派的写作社区，我们主张分享真实的产品体验，有实用价值的经验与思考。我们会不定期挑选Matrix最优质的文章，展示来自用户的最真实的体验和观点。文章代表作者个人观点 ...查看全文"
  },
  {
    "id": "hn:50299212",
    "domain": "大厂 AI 动态",
    "title": "AGI Economics: Coordination vs. Competence",
    "url": "https://institute.deepmind.com/essays/the-economics-of-intelligence/",
    "source": "simonpure",
    "platform": "hackernews",
    "points": 27,
    "published_at": "2026-10-30T02:36:33+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/30/pile-ins-payouts-and-pacing-pressure-the-investors-behind-the-vcs-open-up/",
    "domain": "大厂 AI 动态",
    "title": "Pile-ins, payouts, and pacing pressure: the investors behind the VCs open up",
    "url": "https://techcrunch.com/2026/10/30/pile-ins-payouts-and-pacing-pressure-the-investors-behind-the-vcs-open-up/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-31T04:16:50+00:00",
    "summary": "The money behind the money is thrilled, mostly."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/30/nvidia-weighs-playing-the-cosigner-for-nscales-ai-data-center-in-west-virginia/",
    "domain": "大厂 AI 动态",
    "title": "Nvidia weighs playing the cosigner for Nscale’s AI data center in West Virginia",
    "url": "https://techcrunch.com/2026/10/30/nvidia-weighs-playing-the-cosigner-for-nscales-ai-data-center-in-west-virginia/",
    "source": "Aditya Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-31T01:20:05+00:00",
    "summary": "When investors get nervous about AI spending, it helps to have the chipmaker that sells the chips offer to cosign the loan."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/30/salesforces-ma-spree-continues-with-a-reported-375m-deal-for-defense-tech-startup-rune/",
    "domain": "大厂 AI 动态",
    "title": "Salesforce’s M&A spree continues with a reported $375M deal for defense tech startup Rune",
    "url": "https://techcrunch.com/2026/10/30/salesforces-ma-spree-continues-with-a-reported-375m-deal-for-defense-tech-startup-rune/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T23:21:23+00:00",
    "summary": "The AI logistics startup will bolster the CRM giant's Missionforce defense platform."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/30/ollie-a-privacy-focused-ai-assistant-is-shutting-down/",
    "domain": "大厂 AI 动态",
    "title": "Ollie, a privacy-focused AI assistant, is shutting down",
    "url": "https://techcrunch.com/2026/10/30/ollie-a-privacy-focused-ai-assistant-is-shutting-down/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T22:56:13+00:00",
    "summary": "As an increasing number of AI assistants flood the market, the founder of Ollie, an assistant that respected its users' privacy, says it will be shutting down in a week."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/30/intels-stock-crashes-knocking-12b-from-governments-stake/",
    "domain": "大厂 AI 动态",
    "title": "Intel’s stock crashes, knocking $12B from government’s stake",
    "url": "https://techcrunch.com/2026/10/30/intels-stock-crashes-knocking-12b-from-governments-stake/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T21:54:34+00:00",
    "summary": "Intel is being hurt by PC sales as the AI industry gobbles memory and other components causing PC prices to rise."
  },
  {
    "id": "rss:https://stratechery.com/2026/at-long-last/",
    "domain": "大厂 AI 动态",
    "title": "2026.44: At Long Last…",
    "url": "https://stratechery.com/2026/at-long-last/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T17:00:00+00:00",
    "summary": "The best Stratechery content from the week of October 26, 2026 including Anthropic numbers, the end of the Internet as we know it, and autocracies then and now."
  },
  {
    "id": "rss:https://stratechery.com/2026/sharp-tech-on-video-anthropics-s-1-and-what-it-means-for-meta-and-muse-you-can-see-everything-and-brewers/",
    "domain": "大厂 AI 动态",
    "title": "Sharp Tech on Video: Anthropic’s S-1 and What It Means for Meta and Muse, You Can See Everything, and Brewers!",
    "url": "https://stratechery.com/2026/sharp-tech-on-video-anthropics-s-1-and-what-it-means-for-meta-and-muse-you-can-see-everything-and-brewers/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T10:00:00+00:00",
    "summary": "Sharp Tech is, for the first time, available on video. You have three ways to consume it: YouTube, Spotify, and here on Stratechery."
  },
  {
    "id": "hn:50306008",
    "domain": "股票",
    "title": "US tech stocks see sharp falls over AI cost fears",
    "url": "https://www.bbc.co.uk/news/articles/cvwy72e0n72yo",
    "source": "mindracer",
    "platform": "hackernews",
    "points": 269,
    "published_at": "2026-10-30T16:13:02+00:00",
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
    "id": "hn:50162431",
    "domain": "股票",
    "title": "The Secret Life of Circuits is now in stock everywhere",
    "url": "https://blog.coredump.cx/p/the-secret-life-of-circuits-is-now",
    "source": "surprisetalk",
    "platform": "hackernews",
    "points": 102,
    "published_at": "2026-10-20T07:15:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:50280197",
    "domain": "股票",
    "title": "Alphabet Announces Third Quarter 2026 Results [pdf]",
    "url": "https://s206.q4cdn.com/479360582/files/doc_financials/2026/q3/2026q3-alphabet-earnings-release.pdf",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 81,
    "published_at": "2026-10-28T20:11:55+00:00",
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
    "points": 13,
    "published_at": "2026-11-01T14:56:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:50297025",
    "domain": "股票",
    "title": "Intel stock plunges after posting disappointing Q4 outlook",
    "url": "https://finance.yahoo.com/video/intel-stock-plunges-after-posting-disappointing-q4-outlook-200731652.html",
    "source": "baal80spam",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-10-29T22:21:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:50314793",
    "domain": "股票",
    "title": "'Big Short' Trader Steve Eisman on Anthropic IPO",
    "url": "https://www.youtube.com/watch?v=AMoKKtNFkDs",
    "source": "musha68k",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-10-31T10:48:21+00:00",
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
    "id": "hn:50265525",
    "domain": "股票",
    "title": "In China, the AI bubble has burst",
    "url": "https://finance.yahoo.com/markets/stocks/articles/analysis-china-ai-bubble-already-120038616.html",
    "source": "smurda",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-10-27T20:44:20+00:00",
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
    "id": "hn:50254255",
    "domain": "股票",
    "title": "Pentagon orders bases to plan for 90 days without the grid",
    "url": "https://fortune.com/2026/10/26/pentagon-fortress-bases-90-days-off-grid-uk-be-ready-stockpile/",
    "source": "russfink",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-10-27T03:02:29+00:00",
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
    "id": "hn:50193524",
    "domain": "股票",
    "title": "Chinese stocks turn biggest losers as global AI trade stumbles",
    "url": "https://theedgemalaysia.com/node/822195",
    "source": "miohtama",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-10-22T10:32:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:50210325",
    "domain": "股票",
    "title": "Built a site that teaches investing using the live market as the examples",
    "url": "https://www.stocksightfinance.com",
    "source": "kshitik",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-10-23T15:07:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:50159963",
    "domain": "股票",
    "title": "Investors temper Anthropic IPO valuation expectations over growth slowdown",
    "url": "https://www.reuters.com/business/finance/investors-temper-anthropic-ipo-valuation-expectations-over-revenue-growth-2026-10-15/",
    "source": "xqcgrek2",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-10-20T00:49:40+00:00",
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
    "id": "hn:50046896",
    "domain": "股票",
    "title": "Nvidia-backed data centre firm Firmus scraps IPO as AI valuation concerns deepen",
    "url": "https://www.bbc.com/news/articles/ck9dzpw4ll8po",
    "source": "devonnull",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-10-11T19:26:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:49977893",
    "domain": "股票",
    "title": "Show HN: A replacement motherboard for the iPod mini, 3G and 4G",
    "url": "https://certainthings.studio/sprout/",
    "source": "seanpod",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-10-06T13:10:05+00:00",
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
    "id": "hn:50291902",
    "domain": "金融",
    "title": "Alphabet heads for a $500B drop in market value, biggest in its history",
    "url": "https://finance.yahoo.com/markets/article/alphabet-heads-for-a-500-billion-drop-in-market-value-the-biggest-in-its-history-134824763.html",
    "source": "rawgabbit",
    "platform": "hackernews",
    "points": 61,
    "published_at": "2026-10-29T16:39:55+00:00",
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
    "id": "hn:50278678",
    "domain": "金融",
    "title": "Show HN: A proof-of-concept formalization of the IRS federal tax forms",
    "url": "https://github.com/emmilco/us-tax-model",
    "source": "RGS1811",
    "platform": "hackernews",
    "points": 82,
    "published_at": "2026-10-28T18:30:53+00:00",
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
    "id": "rss:https://arxiv.org/abs/2610.41624",
    "domain": "金融",
    "title": "Expected shortfall estimation and capital coverage under overlapping scenarios",
    "url": "https://arxiv.org/abs/2610.41624",
    "source": "Martin Aichele, Igor Cialenco, Damian Jelito, Marcin Pitera",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T05:00:00+00:00",
    "summary": "arXiv:2610.41624v1 Announce Type: new Abstract: Expected shortfall (ES) is routinely estimated from a short sample of profit-and-loss (P&amp;L) scenarios built from overlapping multi-day returns, whil"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.41740",
    "domain": "金融",
    "title": "A New GAUSS Software Component for Implementing Dynamic Tests of Contagion with an Application",
    "url": "https://arxiv.org/abs/2610.41740",
    "source": "Abdulnasser Hatemi-J, Alan Mustafa",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T05:00:00+00:00",
    "summary": "arXiv:2610.41740v1 Announce Type: new Abstract: The main goal of this article is to present a new software component created by the authors in GAUSS for implementing dynamic tests for contagion. These"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.42119",
    "domain": "金融",
    "title": "Functional Tensor Trains for High-Order Greeks and Exposure Tails of Multi-Asset Structured Products",
    "url": "https://arxiv.org/abs/2610.42119",
    "source": "Javier Lopez-Piqueres, Atithi Acharya, Yue Sun, Niraj Kumar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T05:00:00+00:00",
    "summary": "arXiv:2610.42119v1 Announce Type: new Abstract: Risk management of worst-of autocallables needs price sensitivities (Greeks) up to third order and the potential future exposure, a tail quantile of the"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.41019",
    "domain": "金融",
    "title": "Neural Network Methods in the 2BSDE Formalism for Solving the High-Dimensional Black--Scholes Equation with Transaction Costs",
    "url": "https://arxiv.org/abs/2610.41019",
    "source": "Guhesh Kumaran",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T05:00:00+00:00",
    "summary": "arXiv:2610.41019v1 Announce Type: cross Abstract: A 2BSDE system is written down for a $(D+1)$-dimensional Black--Scholes partial differential equation (PDE) with the Leland transaction cost model whi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.41103",
    "domain": "金融",
    "title": "Optimal climate policy in incomplete electricity markets",
    "url": "https://arxiv.org/abs/2610.41103",
    "source": "Emil Dimanchev, Steven A. Gabriel, Stein-Erik Fleten, Filippo Pecci, Magnus Korpas",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T05:00:00+00:00",
    "summary": "arXiv:2610.41103v1 Announce Type: cross Abstract: Incomplete long-term contracting in electricity markets can expose investors and consumers to inefficient levels of risk. This paper investigates how "
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.41447",
    "domain": "金融",
    "title": "Why delivered costs understate prices in an integrated global hydrogen market",
    "url": "https://arxiv.org/abs/2610.41447",
    "source": "Bastian Wei{\\ss}enburger, Martin Wietschel, Patrick Pl\\\"otz, Russell McKenna",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T05:00:00+00:00",
    "summary": "arXiv:2610.41447v1 Announce Type: cross Abstract: Delivered-cost estimates are often used as proxies for hydrogen import prices. Yet they measure average supply-chain costs, whereas marginal prices me"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.41689",
    "domain": "金融",
    "title": "QBX: A Compiler for Well-Formed, Auditable Alpha Programs",
    "url": "https://arxiv.org/abs/2610.41689",
    "source": "Yichong Bai, Kaigui Bian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T05:00:00+00:00",
    "summary": "arXiv:2610.41689v1 Announce Type: cross Abstract: Formulaic alpha miners increasingly differ in how they generate candidates, yet each system typically couples its own representation, evaluator, and s"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.41990",
    "domain": "金融",
    "title": "When is the deepest drawdown also the longest?",
    "url": "https://arxiv.org/abs/2610.41990",
    "source": "Yinhao Wu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T05:00:00+00:00",
    "summary": "arXiv:2610.41990v1 Announce Type: cross Abstract: Does the deepest drawdown take the longest to recover? For random walks with iid increments of positive finite mean, we find that the deepest and long"
  },
  {
    "id": "rss:https://arxiv.org/abs/2411.01582",
    "domain": "金融",
    "title": "Matching-LLM: Historically Anchored Synthetic Prediction of Public Opinion and Elections",
    "url": "https://arxiv.org/abs/2411.01582",
    "source": "Shapeng Jiang, Lijia Wei, Chen Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T05:00:00+00:00",
    "summary": "arXiv:2411.01582v4 Announce Type: replace Abstract: Large language models (LLMs) offer new opportunities for predicting public opinion and electoral behavior, but their synthetic responses may not ful"
  },
  {
    "id": "rss:https://arxiv.org/abs/2505.02678",
    "domain": "金融",
    "title": "A Nested Factor Model for Equity Markets: Reconciling Multifractal Stock Returns and Rough Index Volatilities",
    "url": "https://arxiv.org/abs/2505.02678",
    "source": "Othmane Zarhali, Cecilia Aubrun, Emmanuel Bacry, Jean-Philippe Bouchaud, Jean-Fran\\c{c}ois Muzy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T05:00:00+00:00",
    "summary": "arXiv:2505.02678v5 Announce Type: replace Abstract: The Nested factor model was introduced by Chicheportiche et al. to represent non-linear correlations between stocks. Stock returns are explained by "
  },
  {
    "id": "rss:https://arxiv.org/abs/2603.16886",
    "domain": "金融",
    "title": "A Controlled Comparison of Deep Learning Architectures for Multi-Horizon Financial Forecasting: Evidence from 918 Experiments",
    "url": "https://arxiv.org/abs/2603.16886",
    "source": "Nabeel Ahmad Saidd",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T05:00:00+00:00",
    "summary": "arXiv:2603.16886v2 Announce Type: replace Abstract: Reliable comparison of deep learning architectures for financial forecasting requires controlled evaluation that separates architectural effects fro"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.00051",
    "domain": "金融",
    "title": "Climate aware lending allocation under NGFS scenarios - A Monte Carlo approach",
    "url": "https://arxiv.org/abs/2610.00051",
    "source": "Marina Palaisti",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T05:00:00+00:00",
    "summary": "arXiv:2610.00051v2 Announce Type: replace Abstract: This paper examines climate-sensitive credit risk and lending allocation over a five-year horizon by mapping NGFS short-term transition and physical"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.00147",
    "domain": "金融",
    "title": "Admissible Portfolio Optimization: Information Constraints, Conditional Efficient Frontiers and the Price of Causal Identification",
    "url": "https://arxiv.org/abs/2610.00147",
    "source": "Alejandro Rodriguez Dominguez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T05:00:00+00:00",
    "summary": "arXiv:2610.00147v2 Announce Type: replace Abstract: Mean--variance portfolio choice takes the conditioning information as given, so that two errors about it, using variables not available at the decis"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.33400",
    "domain": "金融",
    "title": "Tracking High-Frequency Trading Activity in China and Its Effects on Market Quality",
    "url": "https://arxiv.org/abs/2610.33400",
    "source": "Li Guo, Frank Weikai Li, Ding Qi, Lijian Sun",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T05:00:00+00:00",
    "summary": "arXiv:2610.33400v2 Announce Type: replace Abstract: We develop a new order-level proxy for high-frequency trading (HFT) activity based on precise order placement and study its effects on market qualit"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.34133",
    "domain": "金融",
    "title": "Smart charging without rebound peaks: Wholesale price feedback limits distribution grid peaks from price-responsive electric vehicles",
    "url": "https://arxiv.org/abs/2610.34133",
    "source": "Lion Hirth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T05:00:00+00:00",
    "summary": "arXiv:2610.34133v2 Announce Type: replace Abstract: Studies on price-optimized EV charging consistently find that the common price signal synchronizes charging of the entire fleet of cars in the cheap"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.17490",
    "domain": "金融",
    "title": "Joint Exclusivity",
    "url": "https://arxiv.org/abs/2604.17490",
    "source": "Nawaf Mohammed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T05:00:00+00:00",
    "summary": "arXiv:2604.17490v4 Announce Type: replace-cross Abstract: We introduce \\emph{joint exclusivity} (JE), a relaxation of mutual exclusivity (ME) for non-negative random vectors that forbids only the simu"
  },
  {
    "id": "hn:50295332",
    "domain": "金融",
    "title": "Tesla caught altering specs following rear suspension collapse reports",
    "url": "https://carnewschina.com/2026/09/17/tesla-caught-quietly-altering-model-y-l-manual-specs-following-rear-suspension-collapse-reports/",
    "source": "Alien1Being",
    "platform": "hackernews",
    "points": 25,
    "published_at": "2026-10-29T20:24:13+00:00",
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
  }
]
```
