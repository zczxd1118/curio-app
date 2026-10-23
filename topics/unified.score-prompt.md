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

- 今日日期：`2026-10-23`
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
  "date": "2026-10-23",
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
    "points": 2017332,
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
    "points": 1428180,
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
    "points": 1380706,
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
    "points": 1282571,
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
    "points": 903577,
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
    "points": 870318,
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
    "points": 727062,
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
    "points": 593772,
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
    "points": 425709,
    "published_at": "2025-03-13T13:18:09+00:00",
    "summary": "MCP是近期的AI领域的热点，特别是在海外社区获得热烈讨论，每天都有大量MCP工具诞生。本期视频我们从MCP的概念，技术原理，到多场景实战，一个视频看懂MCP的全部内容。\n\n\nMCP官方开源仓库：https://github.com/modelcontextprotocol/servers\nMCP合集网站：  https://smithery.ai/\nVscode下载：https://code.v"
  },
  {
    "id": "bvid:BV1eK5DzHEWu",
    "domain": "AI",
    "title": "MCP实战指南，mcp视频教程，2小时学透mcp",
    "url": "http://www.bilibili.com/video/av114380213586544",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 424285,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1ia9UBPESQ",
    "domain": "AI",
    "title": "在VScode中配置Claude Code并接入DeepSeek V4 Pro【oo唠嗑教程】",
    "url": "http://www.bilibili.com/video/av116487012549813",
    "source": "沉默的羔丸ovo",
    "platform": "bilibili",
    "points": 360487,
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
    "points": 330731,
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
    "points": 312571,
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
    "points": 284244,
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
    "points": 213919,
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
    "points": 184502,
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
    "points": 163222,
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
    "points": 151680,
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
    "points": 140828,
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
    "points": 103027,
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
    "points": 91578,
    "published_at": "2026-09-10T13:47:24+00:00",
    "summary": "这套课程围绕「AI+网络安全」展开，从AI智能体基础入门，到WorkBuddy、Trae等主流Agent工具的实际应用，再到API-Key接入、Skill使用等核心能力，逐步进入AI漏洞挖掘、代码审计、CTF题目分析等安全实战场景。同时结合SRC漏洞挖掘、HVV护网、安全竞赛以及网络安全就业方向，帮助你系统了解AI在网络安全学习、开发与实战中的应用方式。适合网络安全初学者、安全从业者以及希望利用A"
  },
  {
    "id": "bvid:BV1VL3F6pE9K",
    "domain": "AI",
    "title": "0基础入门智能体agent测试：AI测试基础+AI智能体(Agent)测试从零入门全攻略，2026最新版！",
    "url": "http://www.bilibili.com/video/av116991151113881",
    "source": "黑马测试",
    "platform": "bilibili",
    "points": 87009,
    "published_at": "2026-07-27T09:19:37+00:00",
    "summary": "还在卷传统软件测试？2026年必学的AI智能体(Agent)测试来了！本期视频专为0基础小白打造，从软件测试基础讲起...若要本视频配套资源笔记可加up主企微（请看置顶留言最后一句话）。"
  },
  {
    "id": "bvid:BV1XnuGzfEp7",
    "domain": "AI",
    "title": "让你手中的AI好用10倍！5个好玩实用的MCP推荐，让你不只会用AI搜索",
    "url": "http://www.bilibili.com/video/av114835262018810",
    "source": "田同学Tino",
    "platform": "bilibili",
    "points": 76853,
    "published_at": "2025-07-12T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV143wwz6E8F",
    "domain": "AI",
    "title": "Claude code科研使用展示与思路分享（提速就靠Ai）",
    "url": "http://www.bilibili.com/video/av116211882920985",
    "source": "科研推土机",
    "platform": "bilibili",
    "points": 76499,
    "published_at": "2026-03-11T18:12:00+00:00",
    "summary": "本期给大家带来的是Claude在Vscode的科研应用演示与我最近的一些心得使用心得，科研速度嘎嘎提升。论文复现画图、数据分析就靠Claude code。这个课程也是科研推土机「系统管理文献课程2.0」学员催我更新的内容，希望能帮助到大家～，这个视频重点讲两个事情：\n1️⃣ 资料获取，free不用怀疑，我是良心可言博主，，关注我(GZTSHNR)～\n2️⃣ 展示如何在VS code实操应用clau"
  },
  {
    "id": "bvid:BV1A24y1J7Dt",
    "domain": "AI",
    "title": "如何在VS Code中使用Cursor自动生成代码",
    "url": "http://www.bilibili.com/video/av781409810",
    "source": "许你再少年",
    "platform": "bilibili",
    "points": 74577,
    "published_at": "2023-03-23T11:32:23+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV19wXvBpEaL",
    "domain": "AI",
    "title": "认真用 Claude Code 的人，迟早会遇见 Everything Claude Code",
    "url": "http://www.bilibili.com/video/av116319122885806",
    "source": "极客魔导师",
    "platform": "bilibili",
    "points": 64047,
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
    "points": 56295,
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
    "points": 49555,
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
    "points": 47759,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1XiD5BQEAj",
    "domain": "AI",
    "title": "Claude Code 接入微信、一行命令把Claude Code装进微信、保姆级教程、微信支持Claude Code（cc-connect）远程开发",
    "url": "http://www.bilibili.com/video/av116350093694897",
    "source": "下班学AI",
    "platform": "bilibili",
    "points": 40838,
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
    "points": 34578,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29861,
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
    "points": 29013,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV18KJX6mEiH",
    "domain": "AI",
    "title": "太炸裂了！Claude Code 3.0彻底杀疯了！",
    "url": "http://www.bilibili.com/video/av117450007911196",
    "source": "烟神殿殿主",
    "platform": "bilibili",
    "points": 26889,
    "published_at": "2026-10-16T10:04:56+00:00",
    "summary": "原视频链接：https://www.youtube.com/watch?v=8nh1dcH4uJU\n本视频为AI技术搬运翻译，使用AI智能移除原视频广告营销内容，旨在降低信息差，帮助大家了解海外最新AI动态。\n翻译：烟神殿API,模型gemini-3.8-flash\n配音：使用的时FishTTS官方接口配音"
  },
  {
    "id": "bvid:BV1woHQ6kEtv",
    "domain": "AI",
    "title": "【2026最新版】Workbuddy财务自动化办公实战教程，搭建数字员工，能够秒做账、报税、报销、出报表、做财务分析、编制预算、处理合并报表",
    "url": "http://www.bilibili.com/video/av117404038466491",
    "source": "Max极客菌",
    "platform": "bilibili",
    "points": 26864,
    "published_at": "2026-10-08T07:22:21+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1sQaL6vEkb",
    "domain": "AI",
    "title": "小白向，ai入门第一课：agent的部署和使用！",
    "url": "http://www.bilibili.com/video/av117349378166797",
    "source": "沈三殊",
    "platform": "bilibili",
    "points": 25326,
    "published_at": "2026-09-28T15:30:36+00:00",
    "summary": "详细的agent部署介绍：https://pan.quark.cn/s/3846914c6da7\n欢迎来到ai的世界！！\n有疑问欢迎私信。"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 25251,
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
    "points": 23275,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV17Lap6VEUr",
    "domain": "AI",
    "title": "【全80集】Vibe Coding 零基础入门到实战教程，由浅入深（全程干货）",
    "url": "http://www.bilibili.com/video/av117353572468721",
    "source": "数据拾光屋",
    "platform": "bilibili",
    "points": 22462,
    "published_at": "2026-10-02T09:25:00+00:00",
    "summary": "本套教程专门为零基础学员而制，全程干货无废话，喜欢的小伙伴记得点赞三连喔 ~"
  },
  {
    "id": "bvid:BV1bBHm6MEG5",
    "domain": "AI",
    "title": "这绝对是b站讲的最好的Claude Code全套实战教程，手把手带你搞定国内环境安装配置，全程干货无废话！AI大模型/MCP/Skill/智能体/Agent",
    "url": "http://www.bilibili.com/video/av117402847155229",
    "source": "大模型饼饼",
    "platform": "bilibili",
    "points": 13241,
    "published_at": "2026-10-08T02:13:21+00:00",
    "summary": "这绝对是B站讲得最好的Claude Code全套实战教程！手把手带你搞定国内环境安装配置、基础操作、高阶实战技巧，课程不堆砌冗余理论，聚焦真实开发场景，带你吃透Claude Code核心能力，打通MCP、Skill与Agent智能体联动开发。不管你是想提升日常编码效率，还是入门AI智能体开发，这套教程都非常适合你，全程干货无废话！"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 12991,
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
    "points": 12187,
    "published_at": "2026-10-18T14:44:02+00:00",
    "summary": "cccodroid 是一个开源的安卓应用，把 Claude Code 装进你的安卓设备。不用 root，不刷机，也不套 Linux 虚拟环境，工具直接在安卓上原生运行。\n\n视频全程实机录屏（联想y700二代平板，骁龙 8+），没有连电脑：\n· 一句话让它改代码，先给计划，你点批准才动手\n· 终端里 pkg install rust，现场打包 APK 装上\n· docx / xlsx / pptx "
  },
  {
    "id": "bvid:BV1zV54zbEbU",
    "domain": "AI",
    "title": "2分钟在vscode里使用MCP服务",
    "url": "http://www.bilibili.com/video/av114365231531540",
    "source": "程序员三千",
    "platform": "bilibili",
    "points": 11380,
    "published_at": "2025-04-19T15:10:12+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1Yhb66LEaF",
    "domain": "AI",
    "title": "3分钟，教你什么是vibe coding",
    "url": "http://www.bilibili.com/video/av117115000524101",
    "source": "开聊pro",
    "platform": "bilibili",
    "points": 10284,
    "published_at": "2026-08-18T06:12:25+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1aSR4BKESW",
    "domain": "AI",
    "title": "安卓手机部署Claude Code",
    "url": "http://www.bilibili.com/video/av116526891993752",
    "source": "中国小骑士",
    "platform": "bilibili",
    "points": 8354,
    "published_at": "2026-05-06T09:24:14+00:00",
    "summary": "通过Termux安装Claude Code并且接入国内大模型"
  },
  {
    "id": "bvid:BV1wFpP6uE1s",
    "domain": "AI",
    "title": "【开源】让手机自己操作 App！手上的 ai Agent！GitHub开源安卓App推荐",
    "url": "http://www.bilibili.com/video/av117394643097499",
    "source": "补药满减哇",
    "platform": "bilibili",
    "points": 7338,
    "published_at": "2026-10-07T01:05:00+00:00",
    "summary": "开源安卓 AI Agent：RikkaHub Agent Pure\n它能「看懂」屏幕、自己操作各种 App，也能组队干活。\n\n⬇️ 下载 &amp; 源码（AGPL-3.0）\nhttps://github.com/wuyhong715/rikkahub-agent-pure\n\n▶ 本片讲两件事\n① 无障碍屏幕自动化：读控件树定位、实时决策，不是死坐标脚本\n② 专家团系统：每个专家有自己的模型/工具"
  },
  {
    "id": "bvid:BV1u4G9zmEte",
    "domain": "AI",
    "title": "什么是MCP？VS Code中使用MCP Server",
    "url": "http://www.bilibili.com/video/av114426032168712",
    "source": "AI落地派",
    "platform": "bilibili",
    "points": 7195,
    "published_at": "2025-04-30T08:51:30+00:00",
    "summary": "什么是MCP，怎么样使用MCP Server，不用写SQL语句就可以查询数据库。\n\nMCP Servers\nhttps://smithery.ai/\nhttps://github.com/punkpeye/awesome-mcp-servers\nhttps://github.com/modelcontextprotocol/servers\n\nMCP Server for MySQL based o"
  },
  {
    "id": "bvid:BV1UaYK6nEjP",
    "domain": "AI",
    "title": "【cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av117244419903051",
    "source": "茶子兀",
    "platform": "bilibili",
    "points": 7116,
    "published_at": "2026-09-10T02:39:36+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1YmJ36BEsf",
    "domain": "AI",
    "title": "告别手动，AI代劳：Claude Code + MCP 实现ABAQUS全自动建模",
    "url": "http://www.bilibili.com/video/av116754189653546",
    "source": "CAE老白",
    "platform": "bilibili",
    "points": 7013,
    "published_at": "2026-06-15T12:47:08+00:00",
    "summary": "用Claude Code + MCP给ABAQUS装上“AI大脑”：从自然语言到仿真模型的全自动之路"
  },
  {
    "id": "bvid:BV1fNs9eiEm9",
    "domain": "AI",
    "title": "Cursor AI编程结合cocos3.8游戏开发教程-01",
    "url": "http://www.bilibili.com/video/av113187471105975",
    "source": "太阳8800",
    "platform": "bilibili",
    "points": 6892,
    "published_at": "2024-09-23T15:15:13+00:00",
    "summary": "开源源码仓库\nhttps://gitee.com/gamepublic/chess-cards"
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
    "id": "hn:49844663",
    "domain": "AI 算力 / 半导体",
    "title": "ASML says it sold 'absolutely nothing' in Europe in 2026",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/asml-says-its-sells-absolutely-nothing-in-europe-calls-on-eu-to-help-create-demand",
    "source": "MC995",
    "platform": "hackernews",
    "points": 403,
    "published_at": "2026-09-25T13:49:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:50035886",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia in talks to acquire US 'open' model startup Reflection AI",
    "url": "https://www.ft.com/content/052610c5-22b4-4dd4-932e-b7f9f0628b6a",
    "source": "arkj",
    "platform": "hackernews",
    "points": 180,
    "published_at": "2026-10-10T18:48:35+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/two-dollars-and-a-test-suite/",
    "domain": "AI 算力 / 半导体",
    "title": "Two Dollars and a Test Suite",
    "url": "https://www.eetimes.com/two-dollars-and-a-test-suite/",
    "source": "Moshe Zalcberg",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T08:03:27+00:00",
    "summary": "The $2 damages award grabbed headlines, but the Arm-Qualcomm verdict’s bigger implication concerns who controls the compliance tests that custom chips must pass before shipping. The post Two Dollars a"
  },
  {
    "id": "rss:https://www.eetimes.com/from-cloud-ai-to-edge-ai-how-biwin-enables-the-next-generation-of-storage-and-memory-solutions/",
    "domain": "AI 算力 / 半导体",
    "title": "From Cloud AI to Edge AI: How BIWIN Enables the Next Generation of Storage and Memory Solutions",
    "url": "https://www.eetimes.com/from-cloud-ai-to-edge-ai-how-biwin-enables-the-next-generation-of-storage-and-memory-solutions/",
    "source": "EE Times",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T18:24:39+00:00",
    "summary": "See how BIWIN’s SSD, embedded storage, and memory portfolio supports faster, efficient AI from cloud data centers to edge wearables. The post From Cloud AI to Edge AI: How BIWIN Enables the Next Gener"
  },
  {
    "id": "rss:https://www.eetimes.com/deepx-building-open-software-ecosystem-to-scale-physical-ai-beyond-the-data-center/",
    "domain": "AI 算力 / 半导体",
    "title": "Deepx Building Open Software Ecosystem to Scale Physical AI Beyond the Data Center",
    "url": "https://www.eetimes.com/deepx-building-open-software-ecosystem-to-scale-physical-ai-beyond-the-data-center/",
    "source": "Stephen Las Marias",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T18:14:49+00:00",
    "summary": "Deepx is combining low-power AI accelerators and portable software with industry partnerships to bring physical AI into production. The post Deepx Building Open Software Ecosystem to Scale Physical AI"
  },
  {
    "id": "rss:https://www.eetimes.com/how-goodram-validates-dram-and-ssd-reliability-in-europe/",
    "domain": "AI 算力 / 半导体",
    "title": "How Goodram Validates DRAM and SSD Reliability in Europe",
    "url": "https://www.eetimes.com/how-goodram-validates-dram-and-ssd-reliability-in-europe/",
    "source": "GOODRAM",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T13:00:00+00:00",
    "summary": "Explore Goodram’s European approach to DRAM and SSD testing, from burn-in to platform validation, for reliable industrial and embedded systems. The post How Goodram Validates DRAM and SSD Reliability "
  },
  {
    "id": "rss:https://www.eetimes.com/everspin-expands-mram-push-into-ai-servers-data-centers-satellite-systems/",
    "domain": "AI 算力 / 半导体",
    "title": "Everspin Expands MRAM Push into AI Servers, Data Centers, Satellite Systems",
    "url": "https://www.eetimes.com/everspin-expands-mram-push-into-ai-servers-data-centers-satellite-systems/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T09:58:39+00:00",
    "summary": "In an exclusive interview, Everspin CEO Sanjeev Aggarwal discusses MRAM opportunities amid NOR flash supply constraints. The post Everspin Expands MRAM Push into AI Servers, Data Centers, Satellite Sy"
  },
  {
    "id": "rss:https://www.eetimes.com/when-gps-isnt-enough-building-a-second-layer-of-positioning/",
    "domain": "AI 算力 / 半导体",
    "title": "When GPS Isn’t Enough: Building a Second Layer of Positioning",
    "url": "https://www.eetimes.com/when-gps-isnt-enough-building-a-second-layer-of-positioning/",
    "source": "Steve Caliguri",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T19:00:00+00:00",
    "summary": "GPS jamming is rising. Learn how 4G, 5G, and NTN positioning give mission-critical devices a trusted fallback when GNSS fails. The post When GPS Isn&#8217;t Enough: Building a Second Layer of Position"
  },
  {
    "id": "rss:https://www.eetimes.com/indias-osat-buildout-puts-semiconductor-testing-in-focus/",
    "domain": "AI 算力 / 半导体",
    "title": "India’s OSAT Buildout Puts Semiconductor Testing in Focus",
    "url": "https://www.eetimes.com/indias-osat-buildout-puts-semiconductor-testing-in-focus/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T13:39:13+00:00",
    "summary": "NI said Kaynes Semicon has selected its semiconductor test systems, while other Indian OSATs continue to evaluate equipment as manufacturers prepare for production. The post India’s OSAT Buildout Puts"
  },
  {
    "id": "rss:https://www.eetimes.com/why-chip-design-ai-benchmarks-must-go-beyond-functional-correctness/",
    "domain": "AI 算力 / 半导体",
    "title": "Why Chip Design AI Benchmarks Must Go Beyond Functional Correctness",
    "url": "https://www.eetimes.com/why-chip-design-ai-benchmarks-must-go-beyond-functional-correctness/",
    "source": "Surya Gunukula, Jerry Yicheng Wang, Kevin Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T13:00:00+00:00",
    "summary": "Demand for custom silicon is rising as physical AI, data centers, automotive systems, and edge devices require architectures optimized for specific workloads, memory bandwidth, latency, and energy eff"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/gpus-from-nvidia-rtx-5090-stolen-usd470-000-shipment-from-brazil-airport-appear-for-sale-online-identified-by-serial-numbers-three-employees-identified-by-police-helped-steal-equipment",
    "domain": "AI 算力 / 半导体",
    "title": "GPUs from stolen $470,000 Nvidia RTX 5090 shipment at Brazil airport appear for sale online, identified by serial numbers",
    "url": "https://www.tomshardware.com/pc-components/gpus/gpus-from-nvidia-rtx-5090-stolen-usd470-000-shipment-from-brazil-airport-appear-for-sale-online-identified-by-serial-numbers-three-employees-identified-by-police-helped-steal-equipment",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T16:18:47+00:00",
    "summary": "One of the GPUs from a stolen shipment of RTX 5090 graphics cards has appeared for sale online. Police have identified three employees at an airport who stole the goods."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/sony-japan-marks-last-standalone-4k-blu-ray-player-as-discontinued-playstation-5-now-the-only-blu-ray-player-left-in-sonys-lineup",
    "domain": "AI 算力 / 半导体",
    "title": "Sony Japan marks last standalone 4K Blu-ray player as ‘Discontinued’",
    "url": "https://www.tomshardware.com/tech-industry/sony-japan-marks-last-standalone-4k-blu-ray-player-as-discontinued-playstation-5-now-the-only-blu-ray-player-left-in-sonys-lineup",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T14:04:08+00:00",
    "summary": "Sony is following the footsteps of LG in ending Blu-ray player production."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/tsmc-is-seeking-chipmaking-equipment-that-doesnt-contain-chinese-rare-earth-magnets-asks-suppliers-to-provide-alternative-motors-as-export-controls-threaten-fab-operations",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC is seeking chipmaking equipment that doesn't contain Chinese rare-earth magnets",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/tsmc-is-seeking-chipmaking-equipment-that-doesnt-contain-chinese-rare-earth-magnets-asks-suppliers-to-provide-alternative-motors-as-export-controls-threaten-fab-operations",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T13:45:00+00:00",
    "summary": "TSMC is reportedly asking equipment suppliers for factory machinery that doesn't use rare-earth components, as the chipmaker seeks to reduce exposure to China’s dominance of critical minerals and perm"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/one-easy-change-makes-microsofts-surface-laptop-ultra-with-rtx-spark-a-better-gaming-system-custom-resolutions-make-dlss-easier-on-the-device",
    "domain": "AI 算力 / 半导体",
    "title": "One easy change makes Microsoft's Surface Laptop Ultra with RTX Spark a better gaming system",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/one-easy-change-makes-microsofts-surface-laptop-ultra-with-rtx-spark-a-better-gaming-system-custom-resolutions-make-dlss-easier-on-the-device",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T13:30:00+00:00",
    "summary": "Microsoft's Surface Laptop Ultra with RTX Spark might not be a gaming laptop first and foremost, but it certainly wants to game. We found that creating a custom 1920x1080-equivalent resolution for its"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/leaked-private-keys-for-eight-ca-certificates-let-any-attacker-impersonate-any-domain-billions-of-older-devices-and-software-installations-may-be-vulnerable-after-round-of-fixes-patch-yours-immediately",
    "domain": "AI 算力 / 半导体",
    "title": "Leaked private keys for eight CA certificates let any attacker impersonate any domain",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/leaked-private-keys-for-eight-ca-certificates-let-any-attacker-impersonate-any-domain-billions-of-older-devices-and-software-installations-may-be-vulnerable-after-round-of-fixes-patch-yours-immediately",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T13:14:20+00:00",
    "summary": "Leaked private keys for eight CA certificates let any attacker impersonate any domain — billions of older devices and software installations may be vulnerable after round of fixes, patch yours immedia"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-ryzen-5-5500f-review",
    "domain": "AI 算力 / 半导体",
    "title": "AMD Ryzen 5 5500F review: Vermeer rides again for budget gaming PCs",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-ryzen-5-5500f-review",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T12:40:00+00:00",
    "summary": "After years with the Cezanne-based 5500, AMD has finally updated its $100 CPU to the 5500F in the Vermeer family, adding a 200 MHz boost in clock speed and a PCIe 4.0 upgrade."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/micron-pulls-the-plug-on-future-4f2-dram-after-two-decades-of-research-in-dramatic-shift-company-says-architecture-offers-no-meaningful-density-advantages-increases-manufacturing-complexity-and-costs-and-has-fundamental-scaling-limitations",
    "domain": "AI 算力 / 半导体",
    "title": "Micron pulls the plug on future 4F² DRAM after two decades of research in dramatic shift",
    "url": "https://www.tomshardware.com/pc-components/dram/micron-pulls-the-plug-on-future-4f2-dram-after-two-decades-of-research-in-dramatic-shift-company-says-architecture-offers-no-meaningful-density-advantages-increases-manufacturing-complexity-and-costs-and-has-fundamental-scaling-limitations",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T12:00:00+00:00",
    "summary": "Micron believes that more advanced process technologies will present more benefits in terms of DRAM bit density than smaller memory cells."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/retro-atari-vcs-platform-will-end-with-the-closure-of-its-software-store-in-february-2027-os-update-will-be-released-removing-reliance-on-atari-servers-and-opening-up-homebrew-development",
    "domain": "AI 算力 / 半导体",
    "title": "Retro Atari VCS platform will end with the closure of its software store in February 2027",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/retro-atari-vcs-platform-will-end-with-the-closure-of-its-software-store-in-february-2027-os-update-will-be-released-removing-reliance-on-atari-servers-and-opening-up-homebrew-development",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T11:45:00+00:00",
    "summary": "The modern Atari VCS is being officially retired with the firm’s decision to shut down the Linux-based AMD APU-powered machine's software store early next year."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/ea-is-closing-bioware-the-studio-behind-mass-effect-and-dragon-age-after-more-than-30-years-early-development-of-the-next-mass-effect-game-killed",
    "domain": "AI 算力 / 半导体",
    "title": "EA is closing BioWare, the studio behind Mass Effect and Dragon Age, after more than 30 years",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/ea-is-closing-bioware-the-studio-behind-mass-effect-and-dragon-age-after-more-than-30-years-early-development-of-the-next-mass-effect-game-killed",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T11:30:00+00:00",
    "summary": "EA is closing BioWare and its Edmonton studio after deciding not to move forward with early development of the next Mass Effect."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/17-russian-trawlers-logged-mapping-undersea-cables-connecting-the-us-and-europe-over-500-incidents-of-russian-vessels-loitering-over-critical-communications-cables-reported-in-under-5-years",
    "domain": "AI 算力 / 半导体",
    "title": "17 Russian trawlers logged mapping undersea cables connecting the US and Europe",
    "url": "https://www.tomshardware.com/tech-industry/17-russian-trawlers-logged-mapping-undersea-cables-connecting-the-us-and-europe-over-500-incidents-of-russian-vessels-loitering-over-critical-communications-cables-reported-in-under-5-years",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T11:15:00+00:00",
    "summary": "An investigation claimed that Russian boats have been spending the past five years mapping and surveying undersea cables."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/storage/lto-roadmap-extends-to-365-tb-per-cartridge-as-tape-storage-refuses-to-die-25-year-old-format-sees-400x-capacity-increase-without-changing-form-factor",
    "domain": "AI 算力 / 半导体",
    "title": "LTO roadmap extends to 365 TB per cartridge as tape storage refuses to die",
    "url": "https://www.tomshardware.com/pc-components/storage/lto-roadmap-extends-to-365-tb-per-cartridge-as-tape-storage-refuses-to-die-25-year-old-format-sees-400x-capacity-increase-without-changing-form-factor",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T11:00:00+00:00",
    "summary": "Despite all odds, the AI boom is increasing relevance of tape storage as technology enables cheap storage with zero power consumption in idle and ultimate security with air gap."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/best-buy-has-slashed-usd950-off-this-gorgeous-alienware-16x-aurora-gaming-laptop-with-oled-display-33-percent-price-reduction-on-arrow-lake-laptop-with-rtx-5070",
    "domain": "AI 算力 / 半导体",
    "title": "Best Buy has slashed $950 off this gorgeous Alienware 16X Aurora gaming laptop with OLED display",
    "url": "https://www.tomshardware.com/pc-components/ssds/best-buy-has-slashed-usd950-off-this-gorgeous-alienware-16x-aurora-gaming-laptop-with-oled-display-33-percent-price-reduction-on-arrow-lake-laptop-with-rtx-5070",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T10:59:58+00:00",
    "summary": "Save 33% on a new Alienware 16X Aurora gaming laptop at Best Buy. RTX 5070 graphics and a sharp OLED panel are highlights of this laptop build."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/save-usd238-on-this-9800x3d-combo-deal-with-32gb-ddr5-that-lets-you-start-a-4k-gaming-pc-build-for-just-over-usd1-000-newegg-bundle-ships-this-powerhouse-amd-cpu-with-a-gigabyte-x870e-am5-motherboard-and-a-free-240mm-aio-cooler",
    "domain": "AI 算力 / 半导体",
    "title": "Save $238 on this 9800X3D combo deal with 32GB DDR5 that lets you start a 4K gaming PC build for just over $1,000",
    "url": "https://www.tomshardware.com/pc-components/save-usd238-on-this-9800x3d-combo-deal-with-32gb-ddr5-that-lets-you-start-a-4k-gaming-pc-build-for-just-over-usd1-000-newegg-bundle-ships-this-powerhouse-amd-cpu-with-a-gigabyte-x870e-am5-motherboard-and-a-free-240mm-aio-cooler",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T10:32:09+00:00",
    "summary": "This Newegg combo deal combines the AMD Ryzen 7 9800X3D, 32GB of fast DDR5 RAM, and a Gigabyte AM5 X870E motherboard for $1,029.99, saving you over $238 in total."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/openai-says-gpt-5-6-sol-helped-uncover-critical-php-flaws-that-could-affect-70-percent-of-websites-ai-assisted-researchers-turned-two-year-old-bug-that-stumped-human-developers-into-working-exploits-in-two-weeks",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI says ChatGPT Sol helped uncover critical PHP flaws that could affect 70% of websites",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/openai-says-gpt-5-6-sol-helped-uncover-critical-php-flaws-that-could-affect-70-percent-of-websites-ai-assisted-researchers-turned-two-year-old-bug-that-stumped-human-developers-into-working-exploits-in-two-weeks",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T10:30:00+00:00",
    "summary": "OpenAI says researchers using GPT-5.6 Sol uncovered two critical PHP vulnerabilities with severity scores of 9.2 and demonstrated working exploits, after which the company coordinated fixes."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/googles-tpus-for-ai-workloads-now-run-in-at-metas-data-centers-tpus-sold-to-external-customers-for-the-first-time-threaten-nvidias-market-dominance",
    "domain": "AI 算力 / 半导体",
    "title": "Google’s TPUs for AI workloads now run in Meta's data centers",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/googles-tpus-for-ai-workloads-now-run-in-at-metas-data-centers-tpus-sold-to-external-customers-for-the-first-time-threaten-nvidias-market-dominance",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T10:00:00+00:00",
    "summary": "Google’s TPUs now serve AI in production at Meta, through new open-source engines that run PyTorch models natively on the chips."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/480-000-phishing-emails-sent-from-a-pc-hidden-behind-a-fridge-in-a-japanese-hotel-room-chinese-couple-arrested-over-fraud-operation-leaching-hotel-wi-fi",
    "domain": "AI 算力 / 半导体",
    "title": "480,000 phishing emails sent from a PC hidden behind a fridge in a Japanese hotel room",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/480-000-phishing-emails-sent-from-a-pc-hidden-behind-a-fridge-in-a-japanese-hotel-room-chinese-couple-arrested-over-fraud-operation-leaching-hotel-wi-fi",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T09:30:00+00:00",
    "summary": "Almost 500,000 phishing emails were sent from a PC hidden behind a fridge in a Kobe, Japan, hotel room."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/intel-installs-production-tools-at-fab-62-in-arizona-provides-updates-on-ohio-chip-fab-confirms-high-na-euv-for-high-volume-manufacturing-in-2028",
    "domain": "AI 算力 / 半导体",
    "title": "Intel installs production tools at Fab 62 in Arizona, provides updates on Ohio chip fab",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/intel-installs-production-tools-at-fab-62-in-arizona-provides-updates-on-ohio-chip-fab-confirms-high-na-euv-for-high-volume-manufacturing-in-2028",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T19:35:53+00:00",
    "summary": "Intel makes progress on its manufacturing expansion in Arizona and Ohio as it continues to expand advanced semiconductor manufacturing capacity in the U.S."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/4tb-samsung-990-pro-m-2-ssd-falls-27-percent-hits-20-cents-per-gigabyte-our-favorite-high-capacity-pcie-gen-4-drive-is-the-ultimate-storage-for-your-game-library",
    "domain": "AI 算力 / 半导体",
    "title": "4TB Samsung 990 Pro M.2 SSD falls 27%, hits 20 cents per gigabyte",
    "url": "https://www.tomshardware.com/pc-components/ssds/4tb-samsung-990-pro-m-2-ssd-falls-27-percent-hits-20-cents-per-gigabyte-our-favorite-high-capacity-pcie-gen-4-drive-is-the-ultimate-storage-for-your-game-library",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T16:07:49+00:00",
    "summary": "The 4TB Samsung 990 Pro has its astronomical AI-driven high price slashed by 27%."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/elon-musk-says-asml-and-other-critical-semiconductor-equipment-suppliers-will-expedite-shipments-to-terafab-facility-targets-volume-chip-production-by-q3-q4-2028-in-highly-aspirational-timeline",
    "domain": "AI 算力 / 半导体",
    "title": "ASML and other critical semiconductor equipment suppliers expedite shipments to Musk's Terafab",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/elon-musk-says-asml-and-other-critical-semiconductor-equipment-suppliers-will-expedite-shipments-to-terafab-facility-targets-volume-chip-production-by-q3-q4-2028-in-highly-aspirational-timeline",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T15:30:00+00:00",
    "summary": "Elon Musk says ASML and other semiconductor equipment suppliers are expediting deliveries for Terafab, as Tesla and SpaceX target volume chip production in Texas by late 2028 alongside a massive expan"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/linux/amd-brings-official-ryzen-overclocking-to-linux-with-aod-driver-support-no-official-app-but-third-party-options-should-arrive-soon",
    "domain": "AI 算力 / 半导体",
    "title": "AMD brings official Ryzen overclocking to Linux with AOD driver support",
    "url": "https://www.tomshardware.com/software/linux/amd-brings-official-ryzen-overclocking-to-linux-with-aod-driver-support-no-official-app-but-third-party-options-should-arrive-soon",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T14:52:23+00:00",
    "summary": "New driver enablement work from AMD brings full platform-level tuning control to Ryzen systems running Linux, finally."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/trump-announces-mandate-for-data-centers-to-pay-dividends-to-the-local-community-hopes-to-win-more-data-center-supporters-through-dividend-scheme",
    "domain": "AI 算力 / 半导体",
    "title": "Trump announces mandate forcing AI data centers to pay energy dividends to the local community",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/trump-announces-mandate-for-data-centers-to-pay-dividends-to-the-local-community-hopes-to-win-more-data-center-supporters-through-dividend-scheme",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T13:46:18+00:00",
    "summary": "Trump's latest post on Truth Social announces his plans to make data centers more popular among local communities."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/qualcomm-to-cut-jobs-globally-in-performance-based-layoffs-ceo-says-move-will-build-stronger-performance-culture-as-company-pivots-to-ai-data-center-and-edge-products",
    "domain": "AI 算力 / 半导体",
    "title": "Qualcomm to cut jobs globally in \"performance-based\" layoffs, as company pivots to AI data center and edge computing markets",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/qualcomm-to-cut-jobs-globally-in-performance-based-layoffs-ceo-says-move-will-build-stronger-performance-culture-as-company-pivots-to-ai-data-center-and-edge-products",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T13:00:00+00:00",
    "summary": "Qualcomm will begin performance-based layoffs worldwide in November as the chipmaker reallocates resources toward AI infrastructure, data centers, automotive, PCs, and edge computing, amid weaker cons"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/fadu-puts-the-filesystem-inside-the-ssds-flash-to-bypass-host-cpus-file-semantic-pcie-6-0-ssd-delivers-460-000-ops-s-to-gpus-and-dpus-samples-due-by-q3-2027",
    "domain": "AI 算力 / 半导体",
    "title": "FADU puts the filesystem inside the SSD's flash to bypass host CPUs",
    "url": "https://www.tomshardware.com/pc-components/ssds/fadu-puts-the-filesystem-inside-the-ssds-flash-to-bypass-host-cpus-file-semantic-pcie-6-0-ssd-delivers-460-000-ops-s-to-gpus-and-dpus-samples-due-by-q3-2027",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T12:30:00+00:00",
    "summary": "FADU’s FS-SSD carries NFSv3 file operations inside NVMe commands, letting GPUs, DPUs, and NICs read files without a host file system."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-and-intel-will-work-together-to-create-a-single-pytorch-code-path-for-ai-inference-on-cpus-amd-zendnn-library-gets-folded-into-intel-onednn-to-make-cpu-ai-simpler",
    "domain": "AI 算力 / 半导体",
    "title": "AMD and Intel will work together to create a single PyTorch code path for AI inference on CPUs",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-and-intel-will-work-together-to-create-a-single-pytorch-code-path-for-ai-inference-on-cpus-amd-zendnn-library-gets-folded-into-intel-onednn-to-make-cpu-ai-simpler",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T12:00:00+00:00",
    "summary": "AMD and Intel are working together to bring CPU inference optimizations for PyTorch under the unified oneDNN library."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/iran-threatens-to-attack-undersea-cables-in-the-strait-of-hormuz-calls-them-legitimate-new-targets-in-future-conflict-irgc-spokesman-warns-that-a-future-third-phase-in-war-with-us-could-lead-them-to-sever-global-data-links",
    "domain": "AI 算力 / 半导体",
    "title": "Iran threatens to attack undersea cables in the Strait of Hormuz, calls them 'legitimate new targets' in future conflict",
    "url": "https://www.tomshardware.com/tech-industry/iran-threatens-to-attack-undersea-cables-in-the-strait-of-hormuz-calls-them-legitimate-new-targets-in-future-conflict-irgc-spokesman-warns-that-a-future-third-phase-in-war-with-us-could-lead-them-to-sever-global-data-links",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T11:52:08+00:00",
    "summary": "Iran could attack seven undersea cables that run through the Strait of Hormuz, describing them as \"legitimate new targets\" in a potential \"third phase\" of further conflict with the United States."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/samsung-and-sk-hynix-are-upgrading-chinese-factories-to-produce-advanced-ram-chips-as-ai-data-center-competition-ramps-up-big-players-move-to-fight-off-the-threat-from-cxmt-and-co",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung and SK Hynix are upgrading Chinese factories to produce advanced RAM chips as AI data center competition ramps up",
    "url": "https://www.tomshardware.com/pc-components/dram/samsung-and-sk-hynix-are-upgrading-chinese-factories-to-produce-advanced-ram-chips-as-ai-data-center-competition-ramps-up-big-players-move-to-fight-off-the-threat-from-cxmt-and-co",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T11:49:44+00:00",
    "summary": "Samsung and SK Hynix are reportedly upgrading their factories to produce more advanced RAM chips designed for AI data centers in an attempt to fend off competition from Chinese companies."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/headphones-headsets/why-you-dont-need-an-audiophile-headset-for-gaming-comfort-convenience-and-a-good-mic-win-over-pure-audio-fidelity",
    "domain": "AI 算力 / 半导体",
    "title": "Why you don't need an audiophile headset for gaming — comfort, convenience, and a good mic win over pure audio fidelity",
    "url": "https://www.tomshardware.com/peripherals/headphones-headsets/why-you-dont-need-an-audiophile-headset-for-gaming-comfort-convenience-and-a-good-mic-win-over-pure-audio-fidelity",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T11:30:00+00:00",
    "summary": "Headsets are mainly about audio, but that doesn't mean that the \"objectively\" best-sounding headset by audiophile standards translates to the best-sounding headset by gaming standards."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/microns-taiwan-union-will-launch-a-one-day-strike-this-week-threatening-round-the-clock-fab-operations-workers-demand-concrete-terms-for-2026-bonus-and-clearer-profit-sharing-arrangements",
    "domain": "AI 算力 / 半导体",
    "title": "Micron's Taiwan union will launch a one-day strike this week, threatening memory production",
    "url": "https://www.tomshardware.com/pc-components/dram/microns-taiwan-union-will-launch-a-one-day-strike-this-week-threatening-round-the-clock-fab-operations-workers-demand-concrete-terms-for-2026-bonus-and-clearer-profit-sharing-arrangements",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T11:00:00+00:00",
    "summary": "Micron's Taiwan union is set to conduct a one-day strike at the company's Taoyuan DRAM facility as workers demand bonuses for this year and transparent terms of bonuses for upcoming years."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/save-a-massive-usd850-on-lenovos-legion-5i-gaming-laptop-with-this-32-percent-best-buy-discount-featuring-powerful-rtx-5070-graphics-and-a-3k-display-with-a-240hz-refresh-rate",
    "domain": "AI 算力 / 半导体",
    "title": "Save a massive $850 on Lenovo's Legion 5i gaming laptop with this 32% Best Buy discount",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/save-a-massive-usd850-on-lenovos-legion-5i-gaming-laptop-with-this-32-percent-best-buy-discount-featuring-powerful-rtx-5070-graphics-and-a-3k-display-with-a-240hz-refresh-rate",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T10:52:35+00:00",
    "summary": "Save $850 on a new Lenovo gaming laptop from Best Buy. Pick up the Legion 5i with RTX 5070 graphics and save 32%."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/score-a-1440p-ready-gaming-pc-with-an-rtx-5060-ti-16gb-for-under-usd1-500-right-now-saving-you-usd200-abs-cyclone-aqua-rig-ships-with-16gb-ddr5-1tb-ssd-and-a-20-core-intel-cpu",
    "domain": "AI 算力 / 半导体",
    "title": "Score a 1440p-ready gaming PC with an RTX 5060 Ti 16GB for under $1,500 right now, saving you $200",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/score-a-1440p-ready-gaming-pc-with-an-rtx-5060-ti-16gb-for-under-usd1-500-right-now-saving-you-usd200-abs-cyclone-aqua-rig-ships-with-16gb-ddr5-1tb-ssd-and-a-20-core-intel-cpu",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T10:50:14+00:00",
    "summary": "You can pick up this ABS Cyclone Aqua gaming PC with an RTX 5060 Ti 16GB, Intel Core i7-14700F, 16GB DDR5, and a 1TB SS with a $200 discount, now $1,499.99."
  },
  {
    "id": "hn:50086363",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's first GPU: GeForce 256",
    "url": "https://dfarq.homeip.net/nvidias-first-gpu-geforce-256/",
    "source": "ibobev",
    "platform": "hackernews",
    "points": 79,
    "published_at": "2026-10-14T12:05:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:50156364",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Vera's System Architecture: Pushing Bandwidth",
    "url": "https://chipsandcheese.com/p/nvidia-veras-system-architecture",
    "source": "pella",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-10-19T18:53:30+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/edge-ai-mcu-features-multimodal-compute-tiered-memory/",
    "domain": "AI 算力 / 半导体",
    "title": "Edge AI MCU Features Multimodal Compute, Tiered Memory",
    "url": "https://www.eetimes.com/edge-ai-mcu-features-multimodal-compute-tiered-memory/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T07:30:00+00:00",
    "summary": "A new MCU combines AI-native acceleration with integrated high-bandwidth DRAM scalable to hundreds of megabytes. The post Edge AI MCU Features Multimodal Compute, Tiered Memory appeared first on EE Ti"
  },
  {
    "id": "rss:https://www.eetimes.com/innovasea-packs-long-life-electronics-into-fish-tags/",
    "domain": "AI 算力 / 半导体",
    "title": "Innovasea Packs Long-Life Electronics into Fish Tags",
    "url": "https://www.eetimes.com/innovasea-packs-long-life-electronics-into-fish-tags/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T22:06:10+00:00",
    "summary": "A company on Canada’s east coast is pushing acoustic telemetry toward lighter payloads and decade-scale deployments by treating energy, sensing, and animal welfare as a single systems problem. The pos"
  },
  {
    "id": "hn:50110301",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia, Apple, Google, Microsoft, Amazon, Meta gave Trump $92M for his ballroom",
    "url": "https://www.theverge.com/policy/1012047/nvidia-apple-google-microsoft-amazon-meta-trump-ballroom",
    "source": "jacquesm",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-10-15T21:11:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:50062098",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia accused of trying to cut a deal with Anna's Archive",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-accused-of-trying-to-cut-a-deal-with-annas-archive-for-high-speed-access-to-the-massive-pirated-book-haul-allegedly-chased-stolen-data-to-fuel-its-llms",
    "source": "amai",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-10-12T19:57:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:50081435",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Reportedly Ending the RTX 5090, Reserves GB202 for Workstation GPUs",
    "url": "https://www.techpowerup.com/353578/nvidia-reportedly-ending-the-rtx-5090-reserves-gb202-silicon-for-workstation-gpus",
    "source": "kristianp",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-10-14T01:52:56+00:00",
    "summary": ""
  },
  {
    "id": "hn:50046896",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia-backed data centre firm Firmus scraps IPO as AI valuation concerns deepen",
    "url": "https://www.bbc.com/news/articles/ck9dzpw4ll8po",
    "source": "devonnull",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-10-11T19:26:05+00:00",
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
    "id": "hn:49913571",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/",
    "source": "bradleyg223",
    "platform": "hackernews",
    "points": 1705,
    "published_at": "2026-09-30T20:04:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:50073879",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon",
    "url": "https://deepmind.google/models/gemini/",
    "source": "737max",
    "platform": "hackernews",
    "points": 1466,
    "published_at": "2026-10-13T16:03:16+00:00",
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
    "id": "hn:49848269",
    "domain": "大厂 AI 动态",
    "title": "Ollaya – Ollama for open-source, Jev-style decision models",
    "url": "https://ollaya.dev/",
    "source": "Ardakilic",
    "platform": "hackernews",
    "points": 618,
    "published_at": "2026-09-25T18:33:50+00:00",
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
    "id": "hn:49817615",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.8 text-to-speech",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/",
    "source": "swolpers",
    "platform": "hackernews",
    "points": 331,
    "published_at": "2026-09-23T15:29:23+00:00",
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
    "points": 234,
    "published_at": "2026-10-13T16:55:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:49844896",
    "domain": "大厂 AI 动态",
    "title": "Microsoft abandons personal AI chatbot race with Copilot reboot",
    "url": "https://www.bloomberg.com/news/articles/2026-09-25/microsoft-abandons-personal-ai-chatbot-race-with-copilot-reboot",
    "source": "sbulaev",
    "platform": "hackernews",
    "points": 157,
    "published_at": "2026-09-25T14:07:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:49829387",
    "domain": "大厂 AI 动态",
    "title": "Hackers influence ChatGPT and Gemini to direct users to scam centers",
    "url": "https://medium.com/@arielsimon/dark-sourcery-how-hackers-manipulate-ai-to-scam-you-88df434d2073",
    "source": "ArielSimon",
    "platform": "hackernews",
    "points": 143,
    "published_at": "2026-09-24T11:54:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:49854945",
    "domain": "大厂 AI 动态",
    "title": "The Copilot+ PC brand is dead",
    "url": "https://www.windowscentral.com/microsoft/windows-11/the-copilot-pc-brand-is-dead-microsoft-and-pc-makers-quietly-pull-back-on-tarnished-windows-11-ai-pc-branding",
    "source": "bj-rn",
    "platform": "hackernews",
    "points": 122,
    "published_at": "2026-09-26T09:55:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:50198495",
    "domain": "大厂 AI 动态",
    "title": "Google Pushed AI into Schools–and Even Students Say It's Gone Too Far",
    "url": "https://www.wsj.com/tech/ai/google-ai-gemini-education-schools-1ec0972a",
    "source": "the-mitr",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-10-22T17:32:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:49914236",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon (High): Intelligence, Performance and Price Analysis",
    "url": "https://artificialanalysis.ai/models/gemini-4-argon",
    "source": "theanonymousone",
    "platform": "hackernews",
    "points": 113,
    "published_at": "2026-09-30T20:50:28+00:00",
    "summary": ""
  },
  {
    "id": "hn:50195420",
    "domain": "大厂 AI 动态",
    "title": "Why AI's Deepest Mind Believes the World Is About to Change Radically",
    "url": "https://www.wsj.com/tech/ai/demis-hassabis-ai-deepmind-google-isomorphic-2b4e3153",
    "source": "bookofjoe",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-10-22T13:58:47+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/tech/1017261/etsy-ai-rules-policies-restrictions-listing",
    "domain": "大厂 AI 动态",
    "title": "Etsy is cracking down on AI slop listings",
    "url": "https://www.theverge.com/tech/1017261/etsy-ai-rules-policies-restrictions-listing",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T00:09:58+00:00",
    "summary": "Etsy is announcing stricter rules about how AI can be used in listings to reduce the volume of AI slop on the platform. In a post, the company says that \"many active buyers say they can't tell which i"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/1017214/spotify-family-plan-sharing-qr-codes",
    "domain": "大厂 AI 动态",
    "title": "Spotify says yes, it is busting people for using Family Plan sharing too widely",
    "url": "https://www.theverge.com/entertainment/1017214/spotify-family-plan-sharing-qr-codes",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T23:02:43+00:00",
    "summary": "Spotify co-CEO Alex Norstr&#246;m confirmed on this week's earnings call that the company is trying to catch Spotify Family plan users who don't actually live together with a new QR code verification "
  },
  {
    "id": "rss:https://www.theverge.com/games/1016134/xbox-helix-price-1800-isnt-affordable-editorial",
    "domain": "大厂 AI 动态",
    "title": "The next-gen Xbox won’t cost you $1,800. It can’t. Can it?",
    "url": "https://www.theverge.com/games/1016134/xbox-helix-price-1800-isnt-affordable-editorial",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T23:00:00+00:00",
    "summary": "Fortune dropped a bombshell report on the future of gaming this week. According to the publication's Microsoft insiders, the next Xbox is projected to cost between $1,200 and $1,800 when it arrives in"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1017151/canva-craft-in-house-ai-model",
    "domain": "大厂 AI 动态",
    "title": "Canva’s first AI image model plans designs before generating them",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1017151/canva-craft-in-house-ai-model",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T21:51:25+00:00",
    "summary": "Canva is diving even deeper into AI with the launch of an image generation model that competes directly with those from OpenAI, Microsoft, and Google. The model, called Canva Craft, uses a two-stage a"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1017144/global-pc-shipments-dropped-q3-2026-ram",
    "domain": "大厂 AI 动态",
    "title": "PC shipments dropped over 20 percent in Q3 due to RAM price hikes",
    "url": "https://www.theverge.com/gadgets/1017144/global-pc-shipments-dropped-q3-2026-ram",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T21:30:39+00:00",
    "summary": "Demand for new PCs took a hit after months of price hikes, with Counterpoint Research reporting global PC shipments fell 21 percent year-over-year in Q3 2026. That's in line with earlier reports from "
  },
  {
    "id": "rss:https://www.theverge.com/tech/1016506/fall-2026-earnings-watch",
    "domain": "大厂 AI 动态",
    "title": "Fall 2026 earnings watch",
    "url": "https://www.theverge.com/tech/1016506/fall-2026-earnings-watch",
    "source": "Verge Staff",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T21:15:16+00:00",
    "summary": "Every company is suddenly an AI company. Compute is an asset. Cars are flying. We’ve been promised robots — again. It’s time again to dig through earnings reports, listen to investor calls, and call o"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1017082/meta-terms-update-ai-training-concerns",
    "domain": "大厂 AI 动态",
    "title": "Meta&#8217;s AI could still scrape news sites, legal experts say",
    "url": "https://www.theverge.com/tech/1017082/meta-terms-update-ai-training-concerns",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T20:32:05+00:00",
    "summary": "Meta has tweaked its business terms to remove language suggesting that it could freely train its AI models on news sites, like The Verge - but legal experts say these changes aren't enough to address "
  },
  {
    "id": "rss:https://www.theverge.com/tech/1017066/meta-muse-sharing-back-on-artifiacts",
    "domain": "大厂 AI 动态",
    "title": "Meta turns Muse sharing back on",
    "url": "https://www.theverge.com/tech/1017066/meta-muse-sharing-back-on-artifiacts",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T20:24:04+00:00",
    "summary": "Meta has re-enabled Muse sharing after security researchers had reported that public conversation links could be easy to find. The researchers said they had been able to find Muse pages like a marketi"
  },
  {
    "id": "rss:https://www.theverge.com/policy/1017016/fcc-block-foreign-surveillance-chips-hivision-huawei-loophole",
    "domain": "大厂 AI 动态",
    "title": "The FCC is beginning to block gadgets with ‘foreign surveillance chips’",
    "url": "https://www.theverge.com/policy/1017016/fcc-block-foreign-surveillance-chips-hivision-huawei-loophole",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T20:23:48+00:00",
    "summary": "On October 13th, Brendan Carr's FCC gave itself a new power - it can block gadgets for containing any computer chip made by any company on its list of potential threats to national security. Today, it"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1016879/spacex-tesla-cursed-katamari",
    "domain": "大厂 AI 动态",
    "title": "Sure, let’s smoosh SpaceX and Tesla together, who cares",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1016879/spacex-tesla-cursed-katamari",
    "source": "Elizabeth Lopatto",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T19:45:00+00:00",
    "summary": "Oh sure, SpaceX's credit risk is pretty high because it's about to borrow another $40 billion to spend on Nvidia chips, but who cares about that? SpaceX and Tesla have formed special committees to dis"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/22/oura-sues-rival-ultrahuman-again-threatening-its-u-s-smart-ring-comeback/",
    "domain": "大厂 AI 动态",
    "title": "Oura sues rival Ultrahuman again, threatening its U.S. smart ring comeback",
    "url": "https://techcrunch.com/2026/10/22/oura-sues-rival-ultrahuman-again-threatening-its-u-s-smart-ring-comeback/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T04:22:57+00:00",
    "summary": "Oura alleges in its newest lawsuit that Ultrahuman's Ring Pro infringes two of its patents."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/22/uber-rival-indrive-eyes-2027-robotaxi-tests-in-central-asia-with-pony-ai-and-nvidia/",
    "domain": "大厂 AI 动态",
    "title": "Uber rival inDrive eyes 2027 robotaxi tests in Central Asia with Pony.ai and Nvidia",
    "url": "https://techcrunch.com/2026/10/22/uber-rival-indrive-eyes-2027-robotaxi-tests-in-central-asia-with-pony-ai-and-nvidia/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T04:00:00+00:00",
    "summary": "inDrive plans to begin testing Pony.ai's robotaxis in Kazakhstan's capital in the first half of 2027."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/22/left-alone-with-nothing-to-do-ai-agents-started-playing/",
    "domain": "大厂 AI 动态",
    "title": "Left alone with nothing to do, AI agents started playing",
    "url": "https://techcrunch.com/2026/10/22/left-alone-with-nothing-to-do-ai-agents-started-playing/",
    "source": "Aditya Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T00:45:37+00:00",
    "summary": "MIT researchers marooned 13 AIs on a virtual island, and they responded by inventing games, mourning a lost ring and, eventually, getting better at their jobs."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/22/mark-zuckerbergs-creative-plan-to-pay-californias-proposed-billionaire-tax-without-losing-control-of-meta/",
    "domain": "大厂 AI 动态",
    "title": "Mark Zuckerberg’s creative plan to pay California’s proposed billionaire tax without losing control of Meta",
    "url": "https://techcrunch.com/2026/10/22/mark-zuckerbergs-creative-plan-to-pay-californias-proposed-billionaire-tax-without-losing-control-of-meta/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T23:50:41+00:00",
    "summary": "A newly launched stock class being offered was partially engineered to help Meta founder and CEO Mark Zuckerberg pay the \"billionaire's tax,\" should the measure be voted into law."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/22/ben-lamm-raises-200m-for-warhound-to-engineer-war-dogs-and-arm-them-with-anduril-gear/",
    "domain": "大厂 AI 动态",
    "title": "Warhound raises $200M to engineer war dogs and arm them with Anduril gear",
    "url": "https://techcrunch.com/2026/10/22/ben-lamm-raises-200m-for-warhound-to-engineer-war-dogs-and-arm-them-with-anduril-gear/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T23:15:00+00:00",
    "summary": "Warhound, the brainchild of Ben Lamm and Palmer Luckey, emerges from stealth to genetically engineer dogs for military and law enforcement."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/22/as-blockchain-investing-falls-out-of-vogue-a16z-crypto-rebrands-as-a16z-frontier/",
    "domain": "大厂 AI 动态",
    "title": "As blockchain investing falls out of vogue, a16z Crypto rebrands as a16z Frontier",
    "url": "https://techcrunch.com/2026/10/22/as-blockchain-investing-falls-out-of-vogue-a16z-crypto-rebrands-as-a16z-frontier/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T22:34:54+00:00",
    "summary": "The digital asset unit, helmed by Chris Dixon, broadens its scope."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/22/openai-working-on-new-30b-raise-at-1-25t-valuation-ahead-of-ipo/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI working on new $30B raise at $1.25T valuation ahead of IPO",
    "url": "https://techcrunch.com/2026/10/22/openai-working-on-new-30b-raise-at-1-25t-valuation-ahead-of-ipo/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T22:08:24+00:00",
    "summary": "Should OpenAI command an over $1 trillion valuation with this round, it would break records as the most highly valued private company ever."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/22/rivian-buys-world-model-startup-to-accelerate-self-driving-ambitions/",
    "domain": "大厂 AI 动态",
    "title": "Rivian buys world model startup to accelerate self-driving ambitions",
    "url": "https://techcrunch.com/2026/10/22/rivian-buys-world-model-startup-to-accelerate-self-driving-ambitions/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T21:05:05+00:00",
    "summary": "Third Dimension's technology uses AI to match the physical world, which when combined with Rivian's reams of data could turn into a valuable simulator."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/22/arc-browser-sunsets-december-22-as-the-browser-company-doubles-down-on-dia/",
    "domain": "大厂 AI 动态",
    "title": "Arc browser sunsets December 22 as The Browser Company doubles down on Dia",
    "url": "https://techcrunch.com/2026/10/22/arc-browser-sunsets-december-22-as-the-browser-company-doubles-down-on-dia/",
    "source": "Aditya Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T20:01:51+00:00",
    "summary": "Arc was fiercely beloved by a dedicated group of enthusiasts, but it never quite became the mass-market Chrome alternative its makers once envisioned."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/22/the-secret-to-fast-startup-growth-isnt-early-sales-top-names-in-tech-say/",
    "domain": "大厂 AI 动态",
    "title": "The secret to fast startup growth isn’t early sales, top names in tech say",
    "url": "https://techcrunch.com/2026/10/22/the-secret-to-fast-startup-growth-isnt-early-sales-top-names-in-tech-say/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T20:00:00+00:00",
    "summary": "At this year’s Disrupt, Lovable GTM lead Luke Arno, Polsia's Ben Broca, and Theory Ventures’ Tomasz Tunguz gave founders some tips on how to achieve true sales success in the first 90 days."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/22/1password-launches-a-way-for-ai-agents-to-log-in-on-your-behalf-without-seeing-your-password/",
    "domain": "大厂 AI 动态",
    "title": "1Password launches a way for AI agents to log in on your behalf without seeing your password",
    "url": "https://techcrunch.com/2026/10/22/1password-launches-a-way-for-ai-agents-to-log-in-on-your-behalf-without-seeing-your-password/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T19:07:09+00:00",
    "summary": "The new feature allows agents to log into a customer's personal accounts while still protecting the private credentials that secure those accounts."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/22/canva-releases-its-first-image-generation-model/",
    "domain": "大厂 AI 动态",
    "title": "Canva releases its first image generation model",
    "url": "https://techcrunch.com/2026/10/22/canva-releases-its-first-image-generation-model/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T19:00:00+00:00",
    "summary": "Canva is making its new image model available to all users, promising better, more customizable performance at lower costs."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/22/openai-makes-its-jev-competitor-widely-available-as-decision-model-competition-heats-up/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI makes its Jev competitor widely available as decision model competition heats up",
    "url": "https://techcrunch.com/2026/10/22/openai-makes-its-jev-competitor-widely-available-as-decision-model-competition-heats-up/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T19:00:00+00:00",
    "summary": "OpenAI is launching its decision model to the world. Can it compete with the original Jev?"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/22/microsofts-mustafa-suleyman-says-its-ai-outperforms-doctors-on-hard-cases-as-he-chases-medical-superintelligence/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft’s Mustafa Suleyman says its AI outperforms doctors on hard cases as he chases ‘medical superintelligence’",
    "url": "https://techcrunch.com/2026/10/22/microsofts-mustafa-suleyman-says-its-ai-outperforms-doctors-on-hard-cases-as-he-chases-medical-superintelligence/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T18:43:53+00:00",
    "summary": "Microsoft’s new AI diagnostic system beat generalist doctors on hard cases, according to a study in Science. But most of the improvement seems to come from the AI models underneath, not from Microsoft"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/22/former-openai-science-lead-launches-warp-science-to-automate-wet-labs-with-robots/",
    "domain": "大厂 AI 动态",
    "title": "Former OpenAI science lead launches Warp Science to automate wet labs with robots",
    "url": "https://techcrunch.com/2026/10/22/former-openai-science-lead-launches-warp-science-to-automate-wet-labs-with-robots/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T18:38:47+00:00",
    "summary": "Wearing cameras and sensor gloves, the startup’s human chemists will train robots to perform various lab tasks."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/22/elon-musk-made-a-1-billion-investment-in-skydance-report-says/",
    "domain": "大厂 AI 动态",
    "title": "Elon Musk made a $1B investment in Skydance, report says",
    "url": "https://techcrunch.com/2026/10/22/elon-musk-made-a-1-billion-investment-in-skydance-report-says/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T17:36:38+00:00",
    "summary": "The investment will provide a much-needed financial boost as the company seeks to cut costs and lift its stock price."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/22/chinese-hackers-spied-on-thousands-of-companies-after-breaching-it-giant-connectwise/",
    "domain": "大厂 AI 动态",
    "title": "Chinese hackers spied on thousands of companies after breaching IT giant ConnectWise",
    "url": "https://techcrunch.com/2026/10/22/chinese-hackers-spied-on-thousands-of-companies-after-breaching-it-giant-connectwise/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T16:47:17+00:00",
    "summary": "Microsoft points the blame for ConnectWise's breach at a China-aligned hacker, which relied on AI agents to rapidly hack into thousands of its customers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/22/techcrunch-disrupt-2026-startup-battlefield-200-celebrating-outstanding-achievements/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Disrupt 2026 Startup Battlefield 200: Celebrating outstanding achievements",
    "url": "https://techcrunch.com/2026/10/22/techcrunch-disrupt-2026-startup-battlefield-200-celebrating-outstanding-achievements/",
    "source": "Michael Schick, Isabelle Johannessen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T16:00:00+00:00",
    "summary": "Among the Startup Battlefield 200 were many industry-defining companies exhibiting and pitching on the Showcase Stage. Here are the standouts."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/22/uber-puts-all-30000-employees-on-chatgpt-work/",
    "domain": "大厂 AI 动态",
    "title": "Uber puts all 30,000 employees on ChatGPT Work",
    "url": "https://techcrunch.com/2026/10/22/uber-puts-all-30000-employees-on-chatgpt-work/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T16:00:00+00:00",
    "summary": "The ride-share giant previously deployed a much smaller pilot for ChatGPT Work but is now taking the enterprise agent company-wide."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/22/tesla-is-prepping-a-cybercab-onslaught/",
    "domain": "大厂 AI 动态",
    "title": "Tesla is prepping a Cybercab onslaught",
    "url": "https://techcrunch.com/2026/10/22/tesla-is-prepping-a-cybercab-onslaught/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T15:44:39+00:00",
    "summary": "The company is looking to roll out the gold two-seater robotaxis to other U.S. cities this year, even as it goes mum on the number of paid rides."
  },
  {
    "id": "rss:https://stratechery.com/2026/an-interview-with-craig-moffett-about-spacex-and-bubbles/",
    "domain": "大厂 AI 动态",
    "title": "An Interview with Craig Moffett About SpaceX and Bubbles",
    "url": "https://stratechery.com/2026/an-interview-with-craig-moffett-about-spacex-and-bubbles/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T10:00:00+00:00",
    "summary": "An interview with Craig Moffett about SpaceX, from launch to broadband to mobile, plus how he is applying the lessons of the dot-com bubble to today."
  },
  {
    "id": "rss:https://stratechery.com/2026/presented-by-stripe/",
    "domain": "大厂 AI 动态",
    "title": "Presented by Stripe",
    "url": "https://stratechery.com/2026/presented-by-stripe/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T17:35:31+00:00",
    "summary": "Stratechery is now presented by Stripe. What that means for me, for you, and for the future of Stratechery content."
  },
  {
    "id": "rss:https://stratechery.com/2026/netflix-earnings-business-or-franchise-disneys-deal/",
    "domain": "大厂 AI 动态",
    "title": "Netflix Earnings, Business or Franchise, Disney’s Deal",
    "url": "https://stratechery.com/2026/netflix-earnings-business-or-franchise-disneys-deal/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T10:00:00+00:00",
    "summary": "Netflix has a solid business, which is exactly the problem: the company increasingly seems like a business and not a franchise, at least in terms of growth."
  },
  {
    "id": "rss:https://arstechnica.com/gaming/2026/10/switch-2-jailbreak-gives-hackers-new-ways-to-run-homebrew-and-mod-games/",
    "domain": "大厂 AI 动态",
    "title": "Switch 2 security takes a hit as hackers unlock homebrew access",
    "url": "https://arstechnica.com/gaming/2026/10/switch-2-jailbreak-gives-hackers-new-ways-to-run-homebrew-and-mod-games/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T22:25:33+00:00",
    "summary": "\"Userland\" exploit relies on integer overflow found in \"SmileBasic\" interpreter."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/10/personalized-mrna-cancer-vaccine-cut-melanoma-death-recurrence-by-42/",
    "domain": "大厂 AI 动态",
    "title": "Moderna and Merck say their mRNA cancer vaccine cut death, recurrence by 42%",
    "url": "https://arstechnica.com/health/2026/10/personalized-mrna-cancer-vaccine-cut-melanoma-death-recurrence-by-42/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T22:12:19+00:00",
    "summary": "Markers released top-line results today after previously reporting the trial succeeded."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/10/latest-estimate-for-starship-launches-required-to-support-a-moon-landing-22/",
    "domain": "大厂 AI 动态",
    "title": "Latest estimate for Starship launches required to support a Moon landing? 22.",
    "url": "https://arstechnica.com/space/2026/10/latest-estimate-for-starship-launches-required-to-support-a-moon-landing-22/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T21:52:31+00:00",
    "summary": "\"We need to keep our eyes on numerous required fuelings for the lander.\""
  },
  {
    "id": "hn:49826087",
    "domain": "股票",
    "title": "16GB iPod Nano 3G Upgrade",
    "url": "https://tuckerosman.com/projects/16gb-ipod-nano",
    "source": "Ivoah",
    "platform": "hackernews",
    "points": 167,
    "published_at": "2026-09-24T03:58:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:50162431",
    "domain": "股票",
    "title": "The Secret Life of Circuits is now in stock everywhere",
    "url": "https://blog.coredump.cx/p/the-secret-life-of-circuits-is-now",
    "source": "surprisetalk",
    "platform": "hackernews",
    "points": 94,
    "published_at": "2026-10-20T07:15:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:49886005",
    "domain": "股票",
    "title": "Anthropic's IPO prospectus shows AI vision, surging costs",
    "url": "https://www.reuters.com/business/finance/anthropics-ipo-prospectus-shows-sweeping-ai-vision-surging-costs-2026-09-28/",
    "source": "6thbit",
    "platform": "hackernews",
    "points": 145,
    "published_at": "2026-09-28T23:40:59+00:00",
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
    "id": "hn:49914149",
    "domain": "股票",
    "title": "Anthropic's IPO Prospectus Is a Fucking Doozy",
    "url": "https://daringfireball.net/linked/2026/09/30/reuters-anthropic-ipo-prospectus",
    "source": "danaris",
    "platform": "hackernews",
    "points": 71,
    "published_at": "2026-09-30T20:44:19+00:00",
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
    "id": "hn:50019535",
    "domain": "股票",
    "title": "Meadows – a small language for stock-and-flow diagrams that run",
    "url": "https://lorezzed.github.io/meadows/",
    "source": "jjsalamon",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-10-09T12:29:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:50113666",
    "domain": "股票",
    "title": "South Korea's stock market down, president telling people not to commit suicide",
    "url": "https://twitter.com/litcapital/status/2110752546415382699",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-10-16T03:26:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:50113735",
    "domain": "股票",
    "title": "CoreWeave Founders Shield Fortunes with $3.3B Stock Sales",
    "url": "https://www.bloomberg.com/news/articles/2026-10-15/coreweave-founders-shield-fortunes-with-3-3-billion-stock-sales",
    "source": "qlte",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-10-16T03:34:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:50122366",
    "domain": "股票",
    "title": "Anthropic's Valuation Collapsed by $500B",
    "url": "https://www.telegraph.co.uk/business/2026/10/16/anthropic-valuation-ipo-ai-stock-listing/",
    "source": "novaRom",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-10-16T18:27:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:50029232",
    "domain": "股票",
    "title": "Data centre company's much-hyped Australian stock market listing imploded",
    "url": "https://www.theguardian.com/australia-news/2026/oct/09/firmus-australian-stock-market-listing-bust-finance",
    "source": "stubish",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-10-10T03:23:09+00:00",
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
    "id": "hn:50098423",
    "domain": "股票",
    "title": "Asia chip stocks fall, AI funding worries",
    "url": "https://www.cnbc.com/2026/10/15/sk-hynix-samsung-softbank-stocks-asia-tech-rout-ai-funding-worries.html",
    "source": "kristianp",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-10-15T02:29:41+00:00",
    "summary": ""
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
    "id": "hn:50086344",
    "domain": "股票",
    "title": "Humxn Commits $50M to Buy Skilled Trades Data for Robotics Training",
    "url": "https://markets.businessinsider.com/news/stocks/humxn-research-labs-wants-to-buy-50-million-worth-of-skilled-trades-farming-and-manufacturing-data-for-ai-robotics-training-1036622854",
    "source": "howdoweknowit",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-10-14T12:04:10+00:00",
    "summary": ""
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
    "id": "hn:50112657",
    "domain": "金融",
    "title": "Tesla Roadster",
    "url": "https://www.tesla.com/roadster",
    "source": "shekhar101",
    "platform": "hackernews",
    "points": 1644,
    "published_at": "2026-10-16T01:32:45+00:00",
    "summary": ""
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
    "id": "hn:49824686",
    "domain": "金融",
    "title": "Feds Target AI Critics as \"Foreign Agents\"",
    "url": "https://www.kenklippenstein.com/p/feds-think-ai-critics-are-foreign",
    "source": "nmeagent",
    "platform": "hackernews",
    "points": 396,
    "published_at": "2026-09-24T00:41:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:50173487",
    "domain": "金融",
    "title": "Feds suspect ransom negotiator ran ShinyHunters extortion site",
    "url": "https://krebsonsecurity.com/2026/10/feds-suspect-ransom-negotiator-ran-shinyhunters-extortion-site/",
    "source": "Bender",
    "platform": "hackernews",
    "points": 268,
    "published_at": "2026-10-20T22:21:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:49875913",
    "domain": "金融",
    "title": "Parley: Federated, decentralised chat that speaks plain IRC",
    "url": "https://git.mills.io/prologic/parley",
    "source": "davidcollantes",
    "platform": "hackernews",
    "points": 330,
    "published_at": "2026-09-28T10:30:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:50190168",
    "domain": "金融",
    "title": "Epic Games Inc v Apple Inc",
    "url": "https://www.judgments.fedcourt.gov.au/judgments/Judgments/fca/single/2026/2026fca1552",
    "source": "Mayzie",
    "platform": "hackernews",
    "points": 189,
    "published_at": "2026-10-22T01:52:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:49921118",
    "domain": "金融",
    "title": "Meta Uses A.I. Data Centers to Avoid Billions in Federal Taxes",
    "url": "https://www.nytimes.com/2026/09/30/technology/meta-ai-data-centers-taxes.html",
    "source": "gmays",
    "platform": "hackernews",
    "points": 259,
    "published_at": "2026-10-01T13:05:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:49822556",
    "domain": "金融",
    "title": "OpenAI breaches Medicare, Albanese reveals",
    "url": "https://www.smh.com.au/politics/federal/openai-breaches-medicare-albanese-reveals-20260924-p6100u.html",
    "source": "jonnonz",
    "platform": "hackernews",
    "points": 256,
    "published_at": "2026-09-23T21:01:48+00:00",
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
    "id": "hn:50189801",
    "domain": "金融",
    "title": "Tesla profits drop 43% in Q3",
    "url": "https://arstechnica.com/cars/2026/10/tesla-profits-drop-43-in-q3/",
    "source": "throw0101a",
    "platform": "hackernews",
    "points": 86,
    "published_at": "2026-10-22T01:02:23+00:00",
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
    "id": "hn:50090662",
    "domain": "金融",
    "title": "Tesla's Robotaxis Blow Through School Zones, NHTSA Petition Alleges",
    "url": "https://www.extremetech.com/cars/teslas-robotaxis-blow-through-school-zones-nhtsa-petition-alleges",
    "source": "speckx",
    "platform": "hackernews",
    "points": 146,
    "published_at": "2026-10-14T16:45:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:50141295",
    "domain": "金融",
    "title": "Tesla 'Cannot Guarantee' Roadster Reservation Holders Will Ever Get a Car",
    "url": "https://www.thedrive.com/news/tesla-cannot-guarantee-roadster-reservation-holders-will-ever-get-a-car",
    "source": "healsdata",
    "platform": "hackernews",
    "points": 121,
    "published_at": "2026-10-18T14:16:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:50202671",
    "domain": "金融",
    "title": "AI compute is the new oil–and needs a new market",
    "url": "https://www.economist.com/finance-and-economics/2026/10/22/ai-compute-is-the-new-oil-and-needs-a-new-market",
    "source": "ijidak",
    "platform": "hackernews",
    "points": 46,
    "published_at": "2026-10-22T23:45:16+00:00",
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
    "id": "hn:49916668",
    "domain": "金融",
    "title": "10-year Treasury yield climbs above 5.3% to a level not seen in 24 years",
    "url": "https://www.wsj.com/finance/investing/surging-yields-bring-the-bond-market-back-to-the-turn-of-the-century-2b74773f",
    "source": "kaycebasques",
    "platform": "hackernews",
    "points": 125,
    "published_at": "2026-10-01T01:40:50+00:00",
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
    "id": "hn:49832844",
    "domain": "金融",
    "title": "Federal judge orders Texas to air condition all prisons by the end of 2029",
    "url": "https://www.texastribune.org/2026/09/22/texas-prison-air-conditioning-lawsuit-ruling/",
    "source": "bonefishgrill",
    "platform": "hackernews",
    "points": 120,
    "published_at": "2026-09-24T16:15:34+00:00",
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
    "id": "hn:50116255",
    "domain": "金融",
    "title": "Tesla's new Roadster makes a flying debut, hitting 60 MPH in under a second",
    "url": "https://www.foxbusiness.com/technology/teslas-new-roadster-makes-flying-debut-hitting-60-mph-under-second",
    "source": "nsoonhui",
    "platform": "hackernews",
    "points": 70,
    "published_at": "2026-10-16T09:40:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:50114077",
    "domain": "金融",
    "title": "Tesla makes cars that fly? [video]",
    "url": "https://www.youtube.com/watch?v=7p5LxFdc-Qg",
    "source": "merinpapz10",
    "platform": "hackernews",
    "points": 69,
    "published_at": "2026-10-16T04:27:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:50118624",
    "domain": "金融",
    "title": "Tesla unveils 'flying' Roadster with SpaceX thrusters [video]",
    "url": "https://www.youtube.com/watch?v=eqOfmtTJD1A",
    "source": "skadamat",
    "platform": "hackernews",
    "points": 63,
    "published_at": "2026-10-16T14:12:15+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.30527",
    "domain": "金融",
    "title": "Austerity, Gender, and Multidimensional Deprivation Among Older Europeans: Evidence from SHARE",
    "url": "https://arxiv.org/abs/2610.30527",
    "source": "Nita Handastya",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T04:00:00+00:00",
    "summary": "arXiv:2610.30527v1 Announce Type: new Abstract: This paper studies whether fiscal consolidation is associated with deeper multidimensional deprivation among older women than among older men, and throu"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.30539",
    "domain": "金融",
    "title": "Dynamics of the Liquidity Profile in Concentrated Liquidity Provision: An SPIDE Approach",
    "url": "https://arxiv.org/abs/2610.30539",
    "source": "Cheuk Yin Lee, Jimmy Risk, Shen-Ning Tung, Tai-Ho Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T04:00:00+00:00",
    "summary": "arXiv:2610.30539v1 Announce Type: new Abstract: We model the dynamics of the liquidity profile in Uniswap~V3 and other concentrated-liquidity automated market makers with a stochastic partial integro-"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.30637",
    "domain": "金融",
    "title": "Multiple Stopping and Exercise Boundaries for American Put Options",
    "url": "https://arxiv.org/abs/2610.30637",
    "source": "Katsunori Ano",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T04:00:00+00:00",
    "summary": "arXiv:2610.30637v1 Announce Type: new Abstract: This article studies a finite-horizon American put option with up to $m$ exercise rights under the risk-neutral Black--Scholes model, where consecutive "
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.30752",
    "domain": "金融",
    "title": "The Delegation Divide: An Open Index of AI-Agent Delegability across Occupations and Countries",
    "url": "https://arxiv.org/abs/2610.30752",
    "source": "Cristian Espinal Maya (Universidad Nacional de Colombia), Santiago Jim\\'enez Londo\\~no (Universidad EAFIT)",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T04:00:00+00:00",
    "summary": "arXiv:2610.30752v1 Announce Type: new Abstract: 35.2% of task time in world employment is at least partly delegable to AI agents in 2026, and only 2.5% can be handed over in full. Existing measures sc"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.30886",
    "domain": "金融",
    "title": "The Reaction of Financial Markets to the Releases of DeepSeek R1 and Kimi K3: A Critical Analysis",
    "url": "https://arxiv.org/abs/2610.30886",
    "source": "Marco Taboga",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T04:00:00+00:00",
    "summary": "arXiv:2610.30886v1 Announce Type: new Abstract: This paper compares financial-market reactions to the releases of DeepSeek R1 in January 2025 and Kimi K3 in July 2026. Both AI models were presented as"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.31074",
    "domain": "金融",
    "title": "Directionally Correct Views in Portfolio Optimization",
    "url": "https://arxiv.org/abs/2610.31074",
    "source": "Ojas Kumar, Sreejit Dey, Sarvesh Ravichandran Iyer, Sandeep Juneja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T04:00:00+00:00",
    "summary": "arXiv:2610.31074v1 Announce Type: new Abstract: Portfolio optimization techniques often use historical data to estimate parameters for Markowitz-type or ML models. Effective allocation requires a way "
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.31141",
    "domain": "金融",
    "title": "Intraday Forecasting Ability and Liquidity Provision of Institutional Traders",
    "url": "https://arxiv.org/abs/2610.31141",
    "source": "Xinlei Hao, Jiajun Guo, Jussi Keppo, Xianhua Peng",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T04:00:00+00:00",
    "summary": "arXiv:2610.31141v1 Announce Type: new Abstract: This study uses a high-frequency dataset from a stock exchange to examine how forecasting ability and liquidity provision relate to institutional trader"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.31570",
    "domain": "金融",
    "title": "Uncertainty and Explainability in Deep Rough Volatility: A Neural Information-Theoretic Posterior Approach",
    "url": "https://arxiv.org/abs/2609.31570",
    "source": "Damiano Brigo, Rapha\\\"el Huser, Dan Leonte",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T04:00:00+00:00",
    "summary": "arXiv:2609.31570v1 Announce Type: cross Abstract: Deep learning has substantially accelerated the calibration of complex stochastic-volatility models, but neural point calibration alone does not captu"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.30307",
    "domain": "金融",
    "title": "The Customer Is the Builder: How AI Coding Agents Are Rewriting the Economics of Software",
    "url": "https://arxiv.org/abs/2610.30307",
    "source": "Ripon Chandra Malo, Zimeng Yu, Tong Qiu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T04:00:00+00:00",
    "summary": "arXiv:2610.30307v1 Announce Type: cross Abstract: AI coding agents could change whether organizations buy software or build the functionality they need. We focus on organizations and professional buye"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.30557",
    "domain": "金融",
    "title": "Governed Self-Evolution for Autonomous Investing: A Multi-Agent LLM System with an Invariant Core",
    "url": "https://arxiv.org/abs/2610.30557",
    "source": "Yebo Feng, Jingyang Dai, Liangrui Pan, Nelson Lau, Jiahua Xu, Yang Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T04:00:00+00:00",
    "summary": "arXiv:2610.30557v1 Announce Type: cross Abstract: LLM agents that act on live Web data must combine heterogeneous evidence, remember what they have done and improve from outcomes without weakening the"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.30858",
    "domain": "金融",
    "title": "Joules-to-GDP: How Much Economic Value Do AI Systems Produce per Unit of Energy?",
    "url": "https://arxiv.org/abs/2610.30858",
    "source": "Amirreza Zeinali, Jon Saad-Falcon, Avanika Narayan, Mersad Abbasi, Jonathan S. Hartley, John Hennessy, Christopher Re, Azalia Mirhoseini",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T04:00:00+00:00",
    "summary": "arXiv:2610.30858v1 Announce Type: cross Abstract: An AI system can produce more economically valuable work while delivering less value for the energy it consumes. We therefore ask: How much economic v"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.30891",
    "domain": "金融",
    "title": "Equilibria and Learning in Competitive Market Making",
    "url": "https://arxiv.org/abs/2610.30891",
    "source": "Matteo Onger, Luigi Foscari",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T04:00:00+00:00",
    "summary": "arXiv:2610.30891v1 Announce Type: cross Abstract: We propose a market-making game played among $N \\ge 2$ strategic market makers and a single non-strategic representative trader. In a continuous quote"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.31038",
    "domain": "金融",
    "title": "Multichoice Modeling: Exploring Decision Configuration Space under Uncertainty",
    "url": "https://arxiv.org/abs/2610.31038",
    "source": "Mariia Kozlova, Roman Stepanova, Alexander Walzer, Andrea Saltelli",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T04:00:00+00:00",
    "summary": "arXiv:2610.31038v1 Announce Type: cross Abstract: Decision support has become sophisticated at exploring uncertainty, but much less so at representing the architecture of the decision itself. As a res"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.31159",
    "domain": "金融",
    "title": "Beyond city pairs: Higher-order information in urban growth across borders",
    "url": "https://arxiv.org/abs/2610.31159",
    "source": "Cillian Hourican, Debraj Roy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T04:00:00+00:00",
    "summary": "arXiv:2610.31159v1 Announce Type: cross Abstract: We apply higher-order information measures to urban growth across borders and spatial units. We analyse 8,808 functional urban areas using gridded GDP"
  },
  {
    "id": "rss:https://arxiv.org/abs/2407.17014",
    "domain": "金融",
    "title": "Simulation in discrete choice models evaluation: SDCM, a simulation tool for performance evaluation of DCMs",
    "url": "https://arxiv.org/abs/2407.17014",
    "source": "Amirreza Talebi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T04:00:00+00:00",
    "summary": "arXiv:2407.17014v4 Announce Type: replace Abstract: Discrete choice models are widely used in economics, transportation, and marketing to explain and predict how decision makers choose among a finite "
  },
  {
    "id": "rss:https://arxiv.org/abs/2412.00658",
    "domain": "金融",
    "title": "Fast Approximate Modular Inference for Option Price Prediction",
    "url": "https://arxiv.org/abs/2412.00658",
    "source": "Worapree Maneesoonthorn, David T. Frazier, Gael M. Martin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T04:00:00+00:00",
    "summary": "arXiv:2412.00658v3 Announce Type: replace Abstract: A new approximate Bayesian inferential framework is proposed that exploits multiple information sources -- daily spot returns, high-frequency spot d"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.23915",
    "domain": "金融",
    "title": "Equilibrium in closed constant-function market maker economies",
    "url": "https://arxiv.org/abs/2608.23915",
    "source": "Muqiao Huang, Ruodu Wang, Yiyun Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T04:00:00+00:00",
    "summary": "arXiv:2608.23915v2 Announce Type: replace Abstract: We study equilibria in a closed, fee-free constant-function market maker (CFMM) economy with two assets and two agents. An interior state is a unila"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.35111",
    "domain": "金融",
    "title": "The missing price feedback: Why studies overstate local grid peaks from synchronized home batteries under real-time pricing",
    "url": "https://arxiv.org/abs/2609.35111",
    "source": "Lion Hirth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T04:00:00+00:00",
    "summary": "arXiv:2609.35111v2 Announce Type: replace Abstract: Existing studies consistently find that home batteries optimized against real-time electricity prices create new load peaks in local distribution gr"
  },
  {
    "id": "rss:https://arxiv.org/abs/2105.10965",
    "domain": "金融",
    "title": "Inference on Quantile Treatment Effects with Small Treatment Groups",
    "url": "https://arxiv.org/abs/2105.10965",
    "source": "Marina Dias, Demian Pouzo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T04:00:00+00:00",
    "summary": "arXiv:2105.10965v2 Announce Type: replace-cross Abstract: We develop inference for conditional quantile treatment effects that allows treatment groups to remain small as the overall sample grows. Such"
  },
  {
    "id": "rss:https://arxiv.org/abs/2311.12330",
    "domain": "金融",
    "title": "A General Framework for Importance Sampling with Markov Random Walks",
    "url": "https://arxiv.org/abs/2311.12330",
    "source": "Cheng-Der Fuh, Yanwei Jia, Steven Kou",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T04:00:00+00:00",
    "summary": "arXiv:2311.12330v3 Announce Type: replace-cross Abstract: Although stochastic models driven by latent Markov processes are widely used, the classical importance sampling methods based on the exponenti"
  },
  {
    "id": "rss:https://arxiv.org/abs/2603.00365",
    "domain": "金融",
    "title": "Randomized Recruitment Driven Sampling",
    "url": "https://arxiv.org/abs/2603.00365",
    "source": "Adam Visokay, Laura Boudreau, Rachel M. Heath, Tyler H. McCormick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T04:00:00+00:00",
    "summary": "arXiv:2603.00365v2 Announce Type: replace-cross Abstract: Surveys are critical inputs for research and policy, yet, enumerating a sampling frame is logistically infeasible or financially nonviable in "
  },
  {
    "id": "hn:49916955",
    "domain": "金融",
    "title": "Cities Are Forced to Funnel License Plate Data to a Federal Surveillance Program",
    "url": "https://www.404media.co/how-cities-are-forced-to-funnel-license-plate-data-to-a-massive-federal-surveillance-program-hidta/",
    "source": "ripe",
    "platform": "hackernews",
    "points": 93,
    "published_at": "2026-10-01T02:26:17+00:00",
    "summary": ""
  },
  {
    "id": "hn:50112380",
    "domain": "金融",
    "title": "Tesla Debuts 2026 Roadster",
    "url": "https://www.nytimes.com/2026/10/15/business/tesla-roadster-2026-ev-sports-car.html",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 38,
    "published_at": "2026-10-16T00:57:58+00:00",
    "summary": ""
  }
]
```
