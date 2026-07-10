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

- 今日日期：`2026-07-10`
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
  "date": "2026-07-10",
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
    "points": 1466395,
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
    "points": 1365121,
    "published_at": "2026-05-05T14:08:25+00:00",
    "summary": "Claude Code保姆级教学【收藏起来不会错！】\n从上手安装，到高级用法，这期一次讲全～\n花了三周做教程，希望能帮到你嘻嘻，感谢朋友们的三连+关注啦～"
  },
  {
    "id": "bvid:BV1j9MP6wEV9",
    "domain": "AI",
    "title": "从零开始，学会让桌面Agent帮你干活！【小白教程】",
    "url": "http://www.bilibili.com/video/av116861865887789",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 1202693,
    "published_at": "2026-07-05T02:00:00+00:00",
    "summary": "用不上codex的朋友们！新的国产Agent直接上手，来跑通8大用法～\n感谢朋友们的三连+关注～"
  },
  {
    "id": "bvid:BV1kX546QEjG",
    "domain": "AI",
    "title": "保姆级Claude Code速成，必学！简单！【附完整文档】",
    "url": "http://www.bilibili.com/video/av116554859545963",
    "source": "数字游牧人",
    "platform": "bilibili",
    "points": 955198,
    "published_at": "2026-05-11T09:02:15+00:00",
    "summary": "文档链接：https://lcnaoyjp4e3z.feishu.cn/wiki/MtJlwX0B5iy6y9k5GZTcdjSknTd"
  },
  {
    "id": "bvid:BV1yorUYWEGD",
    "domain": "AI",
    "title": "普通人也可以看的 AI 编程指南 | Cursor 教程｜Cursor 使用技巧和思路｜如何免费使用 Cursor｜AI 编程",
    "url": "http://www.bilibili.com/video/av113786467981446",
    "source": "不正经的前端啊",
    "platform": "bilibili",
    "points": 941055,
    "published_at": "2025-01-07T10:01:48+00:00",
    "summary": "普通人也可以看的 AI 编程指南\n全网最详细的 Cursor 教程\nCursor 核心功能、使用技巧和思路\n如何免费白嫖 Cursor"
  },
  {
    "id": "bvid:BV11NNAz5EKn",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！",
    "url": "http://www.bilibili.com/video/av116187623069851",
    "source": "AI-智能体搭建教程",
    "platform": "bilibili",
    "points": 864501,
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
    "points": 855468,
    "published_at": "2025-05-01T09:00:00+00:00",
    "summary": "up的科学星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 804588,
    "published_at": "2026-06-09T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“VibeCoding”免费获取\n【课程简介】从零开始，用自然语言指挥AI开发真实软件项目！"
  },
  {
    "id": "bvid:BV1Yi5M6DERk",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116560144369496",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 572778,
    "published_at": "2026-05-12T06:24:19+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 511687,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1VCVS6PEAd",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent零基础全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116668525186915",
    "source": "大模型入门教程",
    "platform": "bilibili",
    "points": 406000,
    "published_at": "2026-05-31T09:46:57+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1eK5DzHEWu",
    "domain": "AI",
    "title": "MCP实战指南，mcp视频教程，2小时学透mcp",
    "url": "http://www.bilibili.com/video/av114380213586544",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 381381,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1VDTv6rEtM",
    "domain": "AI",
    "title": "终于，Claude Code 封号原因被曝光了！竟然针对中国用户，植入隐形代码？",
    "url": "http://www.bilibili.com/video/av116844031774993",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 354216,
    "published_at": "2026-07-01T09:35:43+00:00",
    "summary": "Claude Code 封号原因终于找到了！国外开发者逆向 Claude Code 源码，发现 Anthropic 在客户端里藏了一套隐蔽的用户标记系统，这期视频带你完整还原封号真相。\n开源 AI 编程教程：github.com/liyupi/ai-guide\n编程学习教程+实战项目+简历模板：codefather.cn\n最近 AI 圈儿不太平啊，OpenAI Codex 封号、Cursor 地区"
  },
  {
    "id": "bvid:BV1BoM76iEih",
    "domain": "AI",
    "title": "爆肝2个月！90分钟拆解AI漫剧全流程（含选题+剧本+分镜+视频+配音+剪辑+变现），先码再学！",
    "url": "http://www.bilibili.com/video/av116887652405651",
    "source": "GenJi是真想教会你",
    "platform": "bilibili",
    "points": 285924,
    "published_at": "2026-07-09T04:02:06+00:00",
    "summary": "过去几个月，我把 AI 漫剧从入门到实操的教程系统整理出来了。\n内容包括思路、流程、工具、案例和一些踩坑经验，质量我自己真的很有信心，也希望能帮到想做 AI 漫剧的朋友。 \n这是一套免费的公益课程，如果你看完觉得有帮助，麻烦给个【点赞、投币、收藏】一键三连，就当作这门课的学费啦！\n做免费课程不容易，先谢谢大家支持！"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 235953,
    "published_at": "2025-04-15T00:59:13+00:00",
    "summary": "MCP终极指南 - 带你深入掌握MCP（基础篇）\n\n时间轴：\n01:05 MCP简要介绍\n02:47 安装 MCP Host（Cline）\n03:15 配置 Cline 用的 API Key\n06:01 第一个 MCP 问题\n06:31 概念解释：MCP Server 和 Tool\n09:13 配置 MCP Server\n14:19 使用 MCP Server\n15:24 MCP 交互流程详解\n1"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 179412,
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
    "points": 177783,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 176650,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 77638,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 70939,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1xBrDB9E42",
    "domain": "AI",
    "title": "独立开发太累？Godot + Claude Code 搭建 AI 辅助工作流，效率直接起飞！ | 地块召唤师开发实战 #01",
    "url": "http://www.bilibili.com/video/av115911319100158",
    "source": "像素夹心饼干",
    "platform": "bilibili",
    "points": 66806,
    "published_at": "2026-01-18T03:25:00+00:00",
    "summary": "大家好，这里是饼干！🍪\n这是我的新坑——**《地块召唤师》**开发实战分享的第一期。\n很多朋友问独立开发如何提升效率？这期视频我不聊虚的，直接公开我从 0 到 1 搭建的 AI + Godot 高效工作流。\n从游戏引擎的选择，到 Claude Code、Copilot 等 AI 工具的实战配置，再到如何用“明确需求”的方法论（SMART原则+双钻模型）来驾驭 AI，让它不仅仅是写代码的工具，更成为"
  },
  {
    "id": "bvid:BV1C6M46uEe3",
    "domain": "AI",
    "title": "AI 写网文能赚钱吗？我实测了一遍……【AI副业实验室01】【B站AI创造公开赛】",
    "url": "http://www.bilibili.com/video/av116877636469982",
    "source": "姚武酒",
    "platform": "bilibili",
    "points": 59618,
    "published_at": "2026-07-09T10:40:00+00:00",
    "summary": "欢迎来到《AI入局实验室》，我们探索拆解一切普通人可能入局的AI副业。\n\n第一期，从调研AI网文，到跑通AI网文的workflow，最后把跑出来的AI网文投稿到真实网站，\n\n全过程我会毫无保留地在视频里分享，替大家尝试一下AI副业的所有可能。"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 52928,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1Am9kBfEMN",
    "domain": "AI",
    "title": "AI智能体赋能课堂教学——技术很简单，难的是想法",
    "url": "http://www.bilibili.com/video/av116482180647922",
    "source": "爱可可-爱生活",
    "platform": "bilibili",
    "points": 48396,
    "published_at": "2026-04-28T11:55:25+00:00",
    "summary": "在AI迅猛发展的今天，课堂正在悄然发生变化。\n但真正的挑战，从来不是“会不会用工具”，而是——我们究竟希望学生学会什么？\n\n本讲座不教软件操作，不演示平台使用，\n而是聚焦一个更关键的问题：\n如何借助AI，让那些我们一直想实现却做不到的教学理想成为现实。\n\n通过真实课堂案例与可落地的方法模型，讲座将带领教师完成一次思维升级：\n从“让AI替你干活”，转向“用AI创造更好的学习体验”\n从“提高效率”，走"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 42110,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 29932,
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
    "points": 28744,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1W2Ts6YEXW",
    "domain": "AI",
    "title": "AI大模型+网络安全零基础入门全套教程：从Agent选型到AI挖洞全流程！AI挖洞提示词|AI解CTF题|AI审计代码|SRC挖洞|CS渗透|kali-码士集团",
    "url": "http://www.bilibili.com/video/av116854601286698",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 24338,
    "published_at": "2026-07-03T06:28:48+00:00",
    "summary": "迈入AI赋能的网络安全新时代！\n\n本课程带你打通大模型与安全实战的底层逻辑。从大模型演进到安全智能体（Agent）构建，硬核实战拉满！手把手教你利用大模型API自动化搞定信息收集、黑盒挖洞、代码审计、解CTF题目及报告编写。深度破解AI挖洞的高效提示词秘籍，攻克复杂场景下的Agent架构与成本选型。\n\n2026安全防线全面升级，带你用AI武装自己，成为驾驭大模型的稀缺AI安全专家！"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22610,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1LWTe6gEVc",
    "domain": "AI",
    "title": "Claude code帮我实现综述论文自由！",
    "url": "http://www.bilibili.com/video/av116842504918580",
    "source": "做科研的大师兄",
    "platform": "bilibili",
    "points": 21361,
    "published_at": "2026-07-01T03:07:40+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1JU7E6PEar",
    "domain": "AI",
    "title": "Cursor 已死？我为什么要退订 Cursor ？",
    "url": "http://www.bilibili.com/video/av116819553683121",
    "source": "祥子在学AI",
    "platform": "bilibili",
    "points": 20038,
    "published_at": "2026-06-27T01:52:00+00:00",
    "summary": "当了一年多的 Cursor 重度用户，最近把它退订了。\n\n不是它变差了，是 Claude Code 和 Codex 真的太好用了。\n\n几个真实感受： ① 大模型越来越强，我已经不怎么手写代码了 ② Cursor 套的是 VS Code 壳子，只属于程序员 ③ 底层模型不在一个量级——Claude 有 Opus 和 Fable 5，Codex 有 GPT 5.5/5.6，Cursor 的 Compo"
  },
  {
    "id": "bvid:BV1cCEi6sEU5",
    "domain": "AI",
    "title": "🦊他能成功吗？Claude Code 接管虚幻引擎5，打造一款游戏 | 带你走完整个流程",
    "url": "http://www.bilibili.com/video/av116731724959171",
    "source": "Apeak_虚幻丰哥",
    "platform": "bilibili",
    "points": 17932,
    "published_at": "2026-06-11T13:41:36+00:00",
    "summary": "Claude Code 接管虚幻引擎5，打造了一款游戏\n下载我的 CLAUDE.md（帮你省 token 的配置）\n链接：https://pan.quark.cn/s/b6e50b4b2535\n提取码：tbaE\nStefan 3D AI ：https://www.youtube.com/watch?v=iRcrZjOt5H8&amp;t=1s\n🔗 完整教程指南和链接：https://www.top"
  },
  {
    "id": "bvid:BV14erKYuEaE",
    "domain": "AI",
    "title": "最强编程AI Cursor+Unity制作一个史诗游戏(详细)",
    "url": "http://www.bilibili.com/video/av113774908413987",
    "source": "多西杰克",
    "platform": "bilibili",
    "points": 17525,
    "published_at": "2025-01-05T09:01:00+00:00",
    "summary": "网上惊呼Cursor AI厉害的内容很多，但结合Unity做游戏的不多，我就来实测一下，做一个AAA大作......"
  },
  {
    "id": "bvid:BV1hnjGzLE14",
    "domain": "AI",
    "title": "【小智教程】手挽手教你如何接入别人的MCP服务",
    "url": "http://www.bilibili.com/video/av114568722450105",
    "source": "空白泡泡糖果",
    "platform": "bilibili",
    "points": 17370,
    "published_at": "2025-05-25T13:36:25+00:00",
    "summary": "文档：https://icnt94i5ctj4.feishu.cn/docx/ZkR3d1lfUosIFCx4qWJcI4QunY0\nshay大佬的HA SSE接入文档：https://bbs.hassbian.com/thread-29314-1-1.html"
  },
  {
    "id": "bvid:BV13sJcz9Egm",
    "domain": "AI",
    "title": "让AI替你打工！教你用Trae+MCP自动操作网页，采集数据，有手就能学会！mcp教程，mcp实战，mcp开发",
    "url": "http://www.bilibili.com/video/av114521544852773",
    "source": "大模型实战课程",
    "platform": "bilibili",
    "points": 17058,
    "published_at": "2025-05-17T05:36:05+00:00",
    "summary": "让AI替你打工！教你用Trae+MCP自动操作网页，采集数据，有手就能学会！mcp教程，mcp实战，mcp开发"
  },
  {
    "id": "bvid:BV1DXTY6hEPv",
    "domain": "AI",
    "title": "Claude国内注册防封号：直接订阅Claude API｜Claude Pro/Max三种订阅方法，封号后如何退款？国内接码+微信支付开通，玩转Opus 4.8",
    "url": "http://www.bilibili.com/video/av116843108964309",
    "source": "Ai实测官",
    "platform": "bilibili",
    "points": 15105,
    "published_at": "2026-07-01T12:00:00+00:00",
    "summary": "Claude国内注册订阅全流程！接码、微信支付、防封号一条视频讲清楚，无需信用卡和美区ID。本期实测三种订阅方法（WildAI第三方/苹果礼品卡/Google Play），并独家对比封号后能否拿到官方退款——真金白银踩坑总结。\n直接订阅Claude 官方API才是防封号最好的方法。触发pro/max封号的机制在这里都不算数。\n新手也能跟着开通Claude Pro/Max，玩转Opus 4.8、Cl"
  },
  {
    "id": "bvid:BV18TZYY8EuJ",
    "domain": "AI",
    "title": "微软最新AI Agent入门课程 • 中英",
    "url": "http://www.bilibili.com/video/av114246130076146",
    "source": "Mindofuture",
    "platform": "bilibili",
    "points": 14000,
    "published_at": "2025-03-30T02:06:00+00:00",
    "summary": "在这门包含10节课的课程中，我们将带你从概念到代码，全面覆盖构建AI代理的基础知识。在这里找到完整的“AI代理入门”课程及代码示例\nhttps://github.com/microsoft/ai-agents-for-beginners\n\nP01 什么是AI代理\nP02 使用哪种AI代理框架\nP03 如何设计优秀的AI代理\nP04 什么是代理工具使用设计模式\nP05 什么是代理式RAG\nP06 如"
  },
  {
    "id": "bvid:BV1CbvxBwEah",
    "domain": "AI",
    "title": "真的不用服务器！用Cloudflare Workers+D1轻松搭建网站！",
    "url": "http://www.bilibili.com/video/av115803408045159",
    "source": "软件工程师Tim",
    "platform": "bilibili",
    "points": 13407,
    "published_at": "2025-12-29T14:51:53+00:00",
    "summary": "本期影片分享一下如何利用cloudflare workers搭建网站，并且利用d1免费数据库，实现无服务器的一个带前后端功能的网站。也就是说，即使你没有服务器，也能够搭建一个属于自己的网站。比如我自己搭建的这个案例网站在线留言板。就是完全搭建在cloudflare workers上面的，里面有静态页面 也有动态api接口。都是部署在workers上面的，并且集成了它提供的数据库。\n\n\n#cloud"
  },
  {
    "id": "bvid:BV1oXjc6CEWK",
    "domain": "AI",
    "title": "（2026版）这才是B站讲的最好的Vibe Coding企业级项目实战，Claude Code+Codex+Cursor丨一周学完，让你少走99%弯路！",
    "url": "http://www.bilibili.com/video/av116769742195971",
    "source": "京东架构师诸葛",
    "platform": "bilibili",
    "points": 12039,
    "published_at": "2026-06-18T06:52:48+00:00",
    "summary": "（2026版）这才是B站讲的最好的Vibe Coding企业级项目实战，Claude Code+Codex+Cursor丨一周学完，让你少走99%弯路！\n【视频配套学习笔记、Agent开发、大模型最新学习路线、系统学习、实战案例、电子书+问题解答】都在这了：https://www.bilibili.com/read/cv39979382/"
  },
  {
    "id": "bvid:BV1C3jt64EPS",
    "domain": "AI",
    "title": "B站讲的最好的Vibe Coding企业级项目实战教程（2026最新版）从入门到进阶，七天速通Claude Code+Codex+CursorAI工程化编程开发",
    "url": "http://www.bilibili.com/video/av116787425383675",
    "source": "图灵学院诸葛",
    "platform": "bilibili",
    "points": 11784,
    "published_at": "2026-06-21T09:48:04+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n 【本视频笔记代码、大模型最新学习路线、系统学习课程、实战案例、电子书+问题解答等戳这里获取→https://www.bilibili.com/read/cv39576966/?jump_opus=1】"
  },
  {
    "id": "bvid:BV1WBTX6kE1B",
    "domain": "AI",
    "title": "【2026版】这绝对是B站唯一将Vibe Coding从入门到实战讲明白的教程，手把手带你从入门到代码实战开发，存下吧，比啃书好太多了！拿走不谢，允许白嫖！",
    "url": "http://www.bilibili.com/video/av116871663722218",
    "source": "码士集团-马小雪",
    "platform": "bilibili",
    "points": 10117,
    "published_at": "2026-07-06T06:47:51+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！ 【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1oqMt6FEj8",
    "domain": "AI",
    "title": "【2026最新Claude Code】Claude Code保姆级完整教程-Claude Code新手保姆级教程-最强AI助手！从入门到进阶【附教程文档安装包】",
    "url": "http://www.bilibili.com/video/av116877216980674",
    "source": "资深bug设计工程师",
    "platform": "bilibili",
    "points": 9819,
    "published_at": "2026-07-07T06:18:15+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV12ojm64EU6",
    "domain": "AI",
    "title": "🧲 Claude Code 工作流：长程任务的规划和执行利器 ⛓️",
    "url": "http://www.bilibili.com/video/av116800494767674",
    "source": "沧海九粟",
    "platform": "bilibili",
    "points": 9396,
    "published_at": "2026-06-24T00:00:00+00:00",
    "summary": "GAC 平台：https://gaccode.com/signup?ref=UWDADYQI\n官方文档：https://code.claude.com/docs/en/workflows\n状态栏技能：https://github.com/webup/skills-cc#-webup-statusline"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 9167,
    "published_at": "2025-04-14T02:30:00+00:00",
    "summary": "MCP服务网站：https://smithery.ai/\nCherry Studio官方网站：https://cherry-ai.com/"
  },
  {
    "id": "bvid:BV1QU6GYFEio",
    "domain": "AI",
    "title": "[课程4] 用Cursor开发数据库真的很简单 | Agent应用 | 用Codebase解决跨文件错误",
    "url": "http://www.bilibili.com/video/av113742109021318",
    "source": "Zhu的AI日记",
    "platform": "bilibili",
    "points": 6995,
    "published_at": "2024-12-31T12:30:00+00:00",
    "summary": "***这是全网最完整的分享如何在不懂编程的情况下，利用结构化思维，用Cursor开发商业app的系列课程。\n《懒人记单词》是基于艾宾浩斯遗忘曲线设计的记单词神器，它可以对每一个单词进行人性化的解读，并在每一个遗忘周期到来时及时提醒，并通过单词释义选择，拼写和造句进行全方位的巩固，同时AI还能对你的句子进行多维度的评估，确保你对每一个单词不仅会认，而且会用。\n\n***你将在本视频中学到：\n1.数据库"
  },
  {
    "id": "bvid:BV1fNs9eiEm9",
    "domain": "AI",
    "title": "Cursor AI编程结合cocos3.8游戏开发教程-01",
    "url": "http://www.bilibili.com/video/av113187471105975",
    "source": "太阳8800",
    "platform": "bilibili",
    "points": 6517,
    "published_at": "2024-09-23T15:15:13+00:00",
    "summary": "开源源码仓库\nhttps://gitee.com/gamepublic/chess-cards"
  },
  {
    "id": "bvid:BV1u4G9zmEte",
    "domain": "AI",
    "title": "什么是MCP？VS Code中使用MCP Server",
    "url": "http://www.bilibili.com/video/av114426032168712",
    "source": "AI落地派",
    "platform": "bilibili",
    "points": 6452,
    "published_at": "2025-04-30T08:51:30+00:00",
    "summary": "什么是MCP，怎么样使用MCP Server，不用写SQL语句就可以查询数据库。\n\nMCP Servers\nhttps://smithery.ai/\nhttps://github.com/punkpeye/awesome-mcp-servers\nhttps://github.com/modelcontextprotocol/servers\n\nMCP Server for MySQL based o"
  },
  {
    "id": "bvid:BV19XqMBzENU",
    "domain": "AI",
    "title": "Cursor + OpenCode 最佳开源 AI 编程工具",
    "url": "http://www.bilibili.com/video/av115851978146202",
    "source": "独立开发者_猫哥",
    "platform": "bilibili",
    "points": 6431,
    "published_at": "2026-01-07T04:47:17+00:00",
    "summary": "OpenCode 是一款面向开发者的开源 AI CLI 编程工具，支持多模型并行、LSP 自动加载、极速响应与非订阅制计费。无论是命令行、桌面 App 还是 VS Code 插件，OpenCode 都提供高效、不啰嗦的 AI 编程体验，是 Cursor 与 Claude Code 的有力替代方案。"
  },
  {
    "id": "bvid:BV1jWcvzmEzc",
    "domain": "AI",
    "title": "Houdini干货|houdini自己的AI agent（agent工具推荐分享）",
    "url": "http://www.bilibili.com/video/av116057012505638",
    "source": "tiny涵",
    "platform": "bilibili",
    "points": 4819,
    "published_at": "2026-02-12T09:45:41+00:00",
    "summary": "原作者教程：https://www.bilibili.com/video/BV1pwcbzBEEh/?spm_id_from=333.1387.list.card_archive.click&amp;vd_source=da5aa377b2acefadd001ffd4902eca9b\n\nGithub download：https://github.com/Kazama-Suichiku/Houdi"
  },
  {
    "id": "bvid:BV13cmnBFEP9",
    "domain": "AI",
    "title": "Claude Code教程9：Claude Code与GitHub的高效联动",
    "url": "http://www.bilibili.com/video/av115689541077475",
    "source": "木乐乐的异想世界",
    "platform": "bilibili",
    "points": 4782,
    "published_at": "2025-12-09T12:17:23+00:00",
    "summary": "【Claude Code教程第9集中文翻译】Net Ninja带你解锁Claude Code与GitHub的高效联动！本集聚焦实用核心功能：无需复杂配置，在Claude聊天会话中即可设置GitHub集成——安装后自动创建两个关键GitHub Action：①自动审查拉取请求（PR）并给出精准反馈；②当仓库问题提及Claude时，自动在新功能分支处理该问题。注意：需先安装GitHub CLI（附官方"
  },
  {
    "id": "hn:48730713",
    "domain": "AI 算力 / 半导体",
    "title": "Zluda 6 release (run unmodified CUDA applications on non-Nvidia GPUs)",
    "url": "https://vosen.github.io/ZLUDA/blog/zluda-update-q1q2-2026/",
    "source": "Tiberium",
    "platform": "hackernews",
    "points": 163,
    "published_at": "2026-06-30T10:34:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:48597201",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung demonstrates 3D stacked FETs with triple nanosheet channels at 42nm",
    "url": "https://semiconductor.samsung.com/news-events/tech-blog/from-gaa-to-3d-stacked-fet-expanding-the-transistor-into-the-third-dimension/",
    "source": "its_ajseven",
    "platform": "hackernews",
    "points": 127,
    "published_at": "2026-06-19T11:03:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:48845518",
    "domain": "AI 算力 / 半导体",
    "title": "Reverse-engineering Nvidia's CUDA-checkpoint for faster cold starts",
    "url": "https://blog.doubleword.ai/what-happens-when-you-checkpoint-a-cuda-process",
    "source": "ilreb",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-07-09T13:29:52+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/simplifying-intelligent-wireless-design-and-security-certification-for-healthcare-devices/",
    "domain": "AI 算力 / 半导体",
    "title": "Simplifying Intelligent Wireless Design and Security Certification for Healthcare Devices",
    "url": "https://www.eetimes.com/simplifying-intelligent-wireless-design-and-security-certification-for-healthcare-devices/",
    "source": "Infineon Technologies and Arrow Electronics",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T17:32:02+00:00",
    "summary": "Join Infineon Technologies and Ezurio for a 60-minute webinar exploring the challenges of designing and certifying secured wireless devices for healthcare applications. The post Simplifying Intelligen"
  },
  {
    "id": "rss:https://www.eetimes.com/voyager-spacecraft-the-ultimate-power-management-challenge/",
    "domain": "AI 算力 / 半导体",
    "title": "Voyager Spacecraft: The Ultimate Power Management Challenge?",
    "url": "https://www.eetimes.com/voyager-spacecraft-the-ultimate-power-management-challenge/",
    "source": "Bill Schweber",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T14:00:00+00:00",
    "summary": "Voyager’s plutonium heart is fading, forcing NASA to kill instruments one by one; see how engineers ration watts 15B miles away. The post Voyager Spacecraft: The Ultimate Power Management Challenge? a"
  },
  {
    "id": "rss:https://www.eetimes.com/as-ai-moves-from-training-to-inference-optics-moves-closer-to-the-chip/",
    "domain": "AI 算力 / 半导体",
    "title": "As AI Moves from Training to Inference, Optics Moves Closer to the Chip",
    "url": "https://www.eetimes.com/as-ai-moves-from-training-to-inference-optics-moves-closer-to-the-chip/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T07:15:00+00:00",
    "summary": "Imec researchers argue that co-packaged optics will not be enough for future AI systems, pushing the industry toward 2.5D and eventually 3D optical I/O. The post As AI Moves from Training to Inference"
  },
  {
    "id": "rss:https://www.eetimes.com/white-house-executive-order-brings-new-urgency-to-post-quantum-cryptography/",
    "domain": "AI 算力 / 半导体",
    "title": "White House Executive Order Brings New Urgency to Post-Quantum Cryptography",
    "url": "https://www.eetimes.com/white-house-executive-order-brings-new-urgency-to-post-quantum-cryptography/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T17:00:00+00:00",
    "summary": "Quantum hackers won’t wait: White House orders PQC by 2030, forcing contractors and tech firms to move now. The post White House Executive Order Brings New Urgency to Post-Quantum Cryptography appeare"
  },
  {
    "id": "rss:https://www.eetimes.com/rise-of-the-ai-data-center-why-infrastructure-strategy-is-now-a-board-level-issue/",
    "domain": "AI 算力 / 半导体",
    "title": "Rise of the AI Data Center – Why Infrastructure Strategy Is Now a Board-Level Issue",
    "url": "https://www.eetimes.com/rise-of-the-ai-data-center-why-infrastructure-strategy-is-now-a-board-level-issue/",
    "source": "Delta Electronics Americas",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T14:00:00+00:00",
    "summary": "This white paper describes the critical engineering and strategic pain points behind today&#8217;s AI data center infrastructure gap and offers practical frameworks for resolving them. Whether you&#82"
  },
  {
    "id": "rss:https://www.eetimes.com/sambanova-raises-1-billion-signs-jpmorganchase-as-a-customer/",
    "domain": "AI 算力 / 半导体",
    "title": "SambaNova Raises $1B, Signs JPMorganChase as a Customer",
    "url": "https://www.eetimes.com/sambanova-raises-1-billion-signs-jpmorganchase-as-a-customer/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T07:45:00+00:00",
    "summary": "The enterprise market is beginning to kick in, SambaNova CEO tells EE Times. The post SambaNova Raises $1B, Signs JPMorganChase as a Customer appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/mems-heralds-an-overdue-step-change-in-switching-technology/",
    "domain": "AI 算力 / 半导体",
    "title": "MEMS Heralds an Overdue Step Change in Switching Technology",
    "url": "https://www.eetimes.com/mems-heralds-an-overdue-step-change-in-switching-technology/",
    "source": "Russ Garcia",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T07:40:00+00:00",
    "summary": "Ditch creaky relays: MEMS switches slash heat, power draw and bulk for AI data centers and automation. The post MEMS Heralds an Overdue Step Change in Switching Technology appeared first on EE Times."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/teamgroup-g70-pro-2tb-ssd-review",
    "domain": "AI 算力 / 半导体",
    "title": "TeamGroup G70 Pro 2TB SSD Review: Low latency meets affordable DRAM",
    "url": "https://www.tomshardware.com/pc-components/ssds/teamgroup-g70-pro-2tb-ssd-review",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T17:17:56+00:00",
    "summary": "The TeamGroup G70 Pro is a high-end drive without a high-end price. Good performance, but poor power efficiency keeps it in check."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/external-ssds/redditor-buys-suspicious-drives-on-ebay-just-to-report-the-scamming-sellers-if-they-get-a-fake-ssd-or-hdd-latest-16tb-find-has-weights-and-microsd-card-hot-glued-inside-the-enclosure-to-make-it-feel-legit",
    "domain": "AI 算力 / 半导体",
    "title": "Redditor buys suspicious drives on eBay just to report the scamming sellers if they get a fake SSD or HDD — latest '16TB' find has weights and microSD card hot-glued inside the enclosure to make it fe",
    "url": "https://www.tomshardware.com/pc-components/external-ssds/redditor-buys-suspicious-drives-on-ebay-just-to-report-the-scamming-sellers-if-they-get-a-fake-ssd-or-hdd-latest-16tb-find-has-weights-and-microsd-card-hot-glued-inside-the-enclosure-to-make-it-feel-legit",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T16:03:35+00:00",
    "summary": "u/Hartkralle says that eBay refunds them when they report these fake drives, so getting scammers banned from the platform is worth their effort. While fake sellers would likely just create a new accou"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/ingenious-father-fixes-dead-rtx-3070-with-a-jerry-rigged-capacitor-from-an-old-radio-saves-worried-son-usd120-in-repair-costs-gpu-works-better-than-before-now",
    "domain": "AI 算力 / 半导体",
    "title": "Ingenious father fixes dead RTX 3070 with a jerry-rigged capacitor from an old radio — Saves worried son $120 in repair costs, GPU 'works better than before' now",
    "url": "https://www.tomshardware.com/pc-components/gpus/ingenious-father-fixes-dead-rtx-3070-with-a-jerry-rigged-capacitor-from-an-old-radio-saves-worried-son-usd120-in-repair-costs-gpu-works-better-than-before-now",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T15:53:52+00:00",
    "summary": "A Russian family has just saved the house $120 in GPU repairs after the father fixed it with a salvaged capacitor from an old radio."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/while-the-u-s-flip-flops-on-chip-sanctions-china-is-building-its-own-chip-supply-market-export-controls-are-creating-conditions-for-a-sino-russian-chip-trade-alliance",
    "domain": "AI 算力 / 半导体",
    "title": "While the U.S. flip-flops on chip sanctions, China is building its own chip supply market — export controls are creating conditions for a Sino-Russian chip trade alliance",
    "url": "https://www.tomshardware.com/tech-industry/while-the-u-s-flip-flops-on-chip-sanctions-china-is-building-its-own-chip-supply-market-export-controls-are-creating-conditions-for-a-sino-russian-chip-trade-alliance",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T15:24:39+00:00",
    "summary": "As the U.S. makes up its mind on export controls for Chinese chips, China has been developing its own supply chain, and associated trade network."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-revives-aging-zen-2-processor-for-budget-pcs-ryzen-7-4700le-resurfaces-in-a-new-usd800-rtx-3050-prebuilt",
    "domain": "AI 算力 / 半导体",
    "title": "AMD revives aging Zen 2 processor for budget PCs — Ryzen 7 4700LE resurfaces in a new $800 RTX 3050 prebuilt",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-revives-aging-zen-2-processor-for-budget-pcs-ryzen-7-4700le-resurfaces-in-a-new-usd800-rtx-3050-prebuilt",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T14:30:22+00:00",
    "summary": "AMD's quiet revival of older Ryzen processors continues, with the Ryzen 7 4700LE now appearing in a prebuilt gaming desktop priced at $799.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-preps-28-core-nova-lake-s-cpus-for-dunlow-workstation-platform-entry-level-xeon-chip-features-lga1954-socket",
    "domain": "AI 算力 / 半导体",
    "title": "Intel preps 28-core Nova Lake-S CPUs for Dunlow workstation platform — Entry-level Xeon chip features LGA1954 socket",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-preps-28-core-nova-lake-s-cpus-for-dunlow-workstation-platform-entry-level-xeon-chip-features-lga1954-socket",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T14:24:21+00:00",
    "summary": "Intel readies Xeon 'Dunlow' platform with 28 cores in LGA1954 packaging for entry-level servers and workstations."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-shows-off-geforce-trading-cards-series-1-collectible-cards-show-off-games-gpus-and-tech-demos-and-will-be-available-for-free-at-upcoming-events",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia shows off GeForce Trading Cards Series 1 — collectible cards show off games, GPUs, and tech demos, and will be available for free at upcoming events",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-shows-off-geforce-trading-cards-series-1-collectible-cards-show-off-games-gpus-and-tech-demos-and-will-be-available-for-free-at-upcoming-events",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T14:12:10+00:00",
    "summary": "Nvidia is creating a set of collectible trading cards that will be given away for free during live events and giveaways this summer."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/professor-suspected-ai-powered-cheating-on-take-home-midterms-makes-finals-in-person-only-two-students-scored-within-10-percent-of-their-midterm-score",
    "domain": "AI 算力 / 半导体",
    "title": "Professor suspected AI-powered cheating on take-home midterms, makes finals in-person — only two students scored within 10% of their midterm score",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/professor-suspected-ai-powered-cheating-on-take-home-midterms-makes-finals-in-person-only-two-students-scored-within-10-percent-of-their-midterm-score",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T14:10:43+00:00",
    "summary": "A Brown University professor suspected that almost his entire class cheated on take-home mid-term exams using AI tools after they scored unusually high. In-person final exams showed that only two stud"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/segas-usd5m-investment-saved-nvidia-in-1996-now-jensen-huang-is-heading-to-tokyo-to-mark-30-years-of-partnership-akihabara-event-will-include-a-geforce-rtx-5090-fe-lottery-an-rtx-spark-presentation-and-more",
    "domain": "AI 算力 / 半导体",
    "title": "Sega’s $5M investment saved Nvidia in 1996, now Jensen Huang is heading to Tokyo to mark 30 years of partnership — Akihabara event will include a GeForce RTX 5090 FE lottery, an RTX Spark presentation",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/segas-usd5m-investment-saved-nvidia-in-1996-now-jensen-huang-is-heading-to-tokyo-to-mark-30-years-of-partnership-akihabara-event-will-include-a-geforce-rtx-5090-fe-lottery-an-rtx-spark-presentation-and-more",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T13:32:50+00:00",
    "summary": "Nvidia and Sega have scheduled an event next week to celebrate their history and longstanding friendship."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/alienware-aw3426dw-34-inch-qd-oled-gaming-monitor-review",
    "domain": "AI 算力 / 半导体",
    "title": "Alienware AW3426DW gaming monitor review: Premium gaming and OLED goodness in a value-priced package",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/alienware-aw3426dw-34-inch-qd-oled-gaming-monitor-review",
    "source": "Christian Eberle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T13:00:00+00:00",
    "summary": "Alienware delivers value from a 34-inch ultra-wide OLED with the AW3426DW. This WQHD curved screen sports Quantum Dot wide gamut color, HDR500, Dolby Vision, 280 Hz, and Adaptive-Sync."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/save-32-percent-on-this-samsung-1440p-gaming-monitor-with-a-fast-240hz-refresh-rate-now-usd169-score-this-27-inch-ips-display-upgrade-with-a-fast-200hz-refresh-rate-for-your-gaming-pc-with-an-usd80-discount",
    "domain": "AI 算力 / 半导体",
    "title": "Save 32% on this Samsung 1440p gaming monitor with a fast 240Hz refresh rate, now $169 — score this 27-inch IPS display upgrade with a fast 200Hz refresh rate for your gaming PC with an $80 discount",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/save-32-percent-on-this-samsung-1440p-gaming-monitor-with-a-fast-240hz-refresh-rate-now-usd169-score-this-27-inch-ips-display-upgrade-with-a-fast-200hz-refresh-rate-for-your-gaming-pc-with-an-usd80-discount",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T12:54:10+00:00",
    "summary": "This 27-inch Samsung Odyssey G53F gaming monitor is on sale for $169.99 right now, offering a 1440p resolution and fast 200Hz refresh rate at a great price."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amds-upcoming-zen-6-medusa-point-10-core-apu-pops-up-on-geekbench-chip-is-faster-than-ryzen-ai-9-hx-370-and-even-ryzen-ai-max-395",
    "domain": "AI 算力 / 半导体",
    "title": "AMD's upcoming Zen 6 Medusa Point 10-core APU pops up on Geekbench — chip is faster than Ryzen AI 9 HX 370 & even Ryzen AI Max+ 395",
    "url": "https://www.tomshardware.com/pc-components/cpus/amds-upcoming-zen-6-medusa-point-10-core-apu-pops-up-on-geekbench-chip-is-faster-than-ryzen-ai-9-hx-370-and-even-ryzen-ai-max-395",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T12:47:57+00:00",
    "summary": "A new 10-core engineering sample from AMD has surfaced on Geekbench, being identified as part of the Medusa Point family. It's likely the Ryzen AI 9 565 and its scores easily beat the Ryzen AI 9 HX 37"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/elon-musk-receives-ftc-greenlight-to-buy-mesh-optical-as-interconnects-emerge-as-ais-tightest-bottleneck-the-move-will-expand-musks-growing-stack-of-critical-ai-infrastructure",
    "domain": "AI 算力 / 半导体",
    "title": "Elon Musk receives FTC greenlight to buy Mesh Optical as interconnects emerge as AI's tightest bottleneck — the move will expand Musk's growing stack of critical AI infrastructure",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/elon-musk-receives-ftc-greenlight-to-buy-mesh-optical-as-interconnects-emerge-as-ais-tightest-bottleneck-the-move-will-expand-musks-growing-stack-of-critical-ai-infrastructure",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T12:42:23+00:00",
    "summary": "FTC clearance to acquire Mesh Optical hands Musk the missing layer between Terafab's chips and Gigasat's satellites, amid tightening interconnect AI bottleneck"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/hallusquatting-is-the-latest-agentic-ai-exploit-where-models-dream-up-potentially-malicious-urls-in-tool-calls-attack-exploits-a-fundamental-weakness-in-every-available-model",
    "domain": "AI 算力 / 半导体",
    "title": "New hack exploits AI hallucinations to trick agents into running malicious code — 'HalluSquatting' attack exploits a fundamental weakness in every available model",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/hallusquatting-is-the-latest-agentic-ai-exploit-where-models-dream-up-potentially-malicious-urls-in-tool-calls-attack-exploits-a-fundamental-weakness-in-every-available-model",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T11:15:00+00:00",
    "summary": "Attackers can exploit how AI bots hallucinate software URLs to create massive botnets. The vulnerability is endemic to every model."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/future-nostalgia-project-asks-retro-hoarders-to-copy-that-floppy-flips-the-early-1990s-anti-piracy-campaign-on-its-head-to-encourage-budding-archivists",
    "domain": "AI 算力 / 半导体",
    "title": "Future Nostalgia Project asks retro hoarders to ‘Copy That Floppy!’ — flips the early 1990s anti-piracy campaign on its head to encourage budding archivists",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/future-nostalgia-project-asks-retro-hoarders-to-copy-that-floppy-flips-the-early-1990s-anti-piracy-campaign-on-its-head-to-encourage-budding-archivists",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T11:07:00+00:00",
    "summary": "Flipping the infamous early 1990s anti-piracy campaign messaging on its head, the Future Nostalgia Project is asking retro hoarders to Copy That Floppy!"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/pc-building/save-usd60-on-this-hoto-diy-and-pc-maintenance-bundle-with-electric-screwdriver-and-4-in-1-air-duster-just-usd89-for-popular-usb-c-rechargeable-driver-with-25-bits-along-with-a-separate-blower-and-vacuum-cleaner-to-keep-your-setup-clean",
    "domain": "AI 算力 / 半导体",
    "title": "Save $60 on this Hoto DIY and PC maintenance bundle with electric screwdriver and 4-in-1 air duster — just $89 for popular USB-C rechargeable driver with 25 bits, along with a separate blower and vacu",
    "url": "https://www.tomshardware.com/desktops/pc-building/save-usd60-on-this-hoto-diy-and-pc-maintenance-bundle-with-electric-screwdriver-and-4-in-1-air-duster-just-usd89-for-popular-usb-c-rechargeable-driver-with-25-bits-along-with-a-separate-blower-and-vacuum-cleaner-to-keep-your-setup-clean",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T11:00:20+00:00",
    "summary": "Save nearly $61 on this two-for-one Hoto combo deal at Amazon right now, giving you the NEX O1 Pro mini electric screwdriver set with 25 bits with its AutoCare 4-in-1 air duster and vacuum cleaner in "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/amd-expo-ull-shows-middling-performance-gains-in-initial-tests-despite-price-increase-first-benchmarks-show-up-to-a-4-percent-improvement-with-ddr5-6000-cl36",
    "domain": "AI 算力 / 半导体",
    "title": "AMD EXPO ULL shows middling performance gains in initial tests despite eye-watering price increase — first benchmarks show up to a 4% improvement with DDR5-6000 CL36",
    "url": "https://www.tomshardware.com/pc-components/ram/amd-expo-ull-shows-middling-performance-gains-in-initial-tests-despite-price-increase-first-benchmarks-show-up-to-a-4-percent-improvement-with-ddr5-6000-cl36",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T10:50:00+00:00",
    "summary": "The first independent benchmarks for AMD's EXPO ULL memory are available, showing just up to a 4% improvement despite an increase in price."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-servers-will-consume-more-power-than-conventional-data-center-hardware-by-2027-gartner-forecasts",
    "domain": "AI 算力 / 半导体",
    "title": "AI servers will consume more power than all conventional data center hardware combined by 2027 — global data center electricity consumption set to grow by 26% this year, Gartner forecasts",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-servers-will-consume-more-power-than-conventional-data-center-hardware-by-2027-gartner-forecasts",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T10:25:00+00:00",
    "summary": "Global data center electricity consumption will grow 26% in 2026 to reach 565 TWh, up from 447 TWh in 2025."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/chinese-courts-allow-heirs-to-inherent-accounts-of-deceased-gamers-multiple-cases-spanning-years-establish-precedent-for-digital-ownership-of-games-in-game-items-and-microtransactions",
    "domain": "AI 算力 / 半导体",
    "title": "Chinese courts allow heirs to inherit accounts of deceased gamers — multiple cases spanning years establish precedent for digital ownership of games, in-game items, and microtransactions",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/chinese-courts-allow-heirs-to-inherent-accounts-of-deceased-gamers-multiple-cases-spanning-years-establish-precedent-for-digital-ownership-of-games-in-game-items-and-microtransactions",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T10:00:00+00:00",
    "summary": "A Reddit user named u/Slawrfp shared on the r/pcmasterrace subreddit that Chinese courts have allowed heirs to inherit games and other digital assets after the original user has since passed on. While"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/rapidus-fab-roadmap-examined",
    "domain": "AI 算力 / 半导体",
    "title": "Rapidus fab roadmap examined — first new leading-edge chipmaker in decades has one Hokkaido fab, a 2027 deadline, and 60 potential customers",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/rapidus-fab-roadmap-examined",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T16:29:26+00:00",
    "summary": "Rapidus is building Japan's entire return to leading-edge logic on one fab in Chitose, Hokkaido."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/china-alleges-that-claude-code-contains-backdoors-calls-mechanism-a-serious-threat-govt-claims-claude-sends-sensitive-information-to-remote-servers-without-consent",
    "domain": "AI 算力 / 半导体",
    "title": "China alleges that Claude Code contains backdoors, calls mechanism 'a serious threat' — Gov't claims Claude sends sensitive information to remote servers without consent",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/china-alleges-that-claude-code-contains-backdoors-calls-mechanism-a-serious-threat-govt-claims-claude-sends-sensitive-information-to-remote-servers-without-consent",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T15:54:14+00:00",
    "summary": "China is warning against the use of Claude Code versions released between April and June 2026 after it's revealed that hidden code is sending sensitive user information to remote servers. The governme"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/hidden-backdoor-found-in-tenda-routers-goes-unpatched-despite-warnings-from-cybersecurity-researchers-affected-firmware-allows-admin-access-without-a-password",
    "domain": "AI 算力 / 半导体",
    "title": "Hidden backdoor in Tenda routers goes unpatched as company ignores warnings from cybersecurity researchers — Chinese company's firmware allows admin access without a password",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/hidden-backdoor-found-in-tenda-routers-goes-unpatched-despite-warnings-from-cybersecurity-researchers-affected-firmware-allows-admin-access-without-a-password",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T15:16:25+00:00",
    "summary": "CERT/CC has disclosed a critical authentication backdoor affecting multiple Tenda router firmware versions. Tracked as CVE-2026-11405, the flaw grants full administrator access without valid credentia"
  },
  {
    "id": "rss:https://www.tomshardware.com/phones/budget-smartphone-market-collapses-under-the-weight-of-memory-shortages-sales-expected-to-drop-22-percent-memory-alone-now-comprises-up-to-64-percent-of-the-total-cost-of-lower-tier-smartphones",
    "domain": "AI 算力 / 半导体",
    "title": "Budget smartphone market collapses under the weight of memory shortages, sales expected to drop 22% — memory alone now comprises up to 64% of the total cost of lower-tier smartphones",
    "url": "https://www.tomshardware.com/phones/budget-smartphone-market-collapses-under-the-weight-of-memory-shortages-sales-expected-to-drop-22-percent-memory-alone-now-comprises-up-to-64-percent-of-the-total-cost-of-lower-tier-smartphones",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T15:15:36+00:00",
    "summary": "The global AI memory squeeze is pricing cheap phones out of existence and forcing mid-range devices to compromise on hardware."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/jedec-releases-new-sphbm4-standard-to-slash-ai-memory-costs-narrow-512-bit-interface-enables-dropping-expensive-interposers-for-organic-substrates",
    "domain": "AI 算力 / 半导体",
    "title": "JEDEC releases new SPHBM4 standard to slash AI memory costs — Narrow 512-bit interface enables dropping expensive interposers for organic substrates",
    "url": "https://www.tomshardware.com/pc-components/dram/jedec-releases-new-sphbm4-standard-to-slash-ai-memory-costs-narrow-512-bit-interface-enables-dropping-expensive-interposers-for-organic-substrates",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T15:03:33+00:00",
    "summary": "SPHBM4 promises HBM4-class bandwidth without usage of silicon interposer and CoWoS-like packaging."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/routers/global-consumer-wi-fi-router-shipments-fell-6-percent-in-q1-2026-mesh-systems-and-gaming-routers-still-prove-popular",
    "domain": "AI 算力 / 半导体",
    "title": "Global consumer Wi-Fi router shipments fell 6% in Q1 2026, down 34% from 2021 peak — mesh systems and gaming routers still prove popular",
    "url": "https://www.tomshardware.com/networking/routers/global-consumer-wi-fi-router-shipments-fell-6-percent-in-q1-2026-mesh-systems-and-gaming-routers-still-prove-popular",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T14:49:27+00:00",
    "summary": "Global consumer Wi-Fi router shipments have declined 34 percent from their peak in 2021"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/sipearls-long-awaited-rhea-cpu-finally-gets-in-the-lab-opening-the-door-for-europes-first-sovereign-hpc-cpu-availability-of-rhea1-is-scheduled-for-end-of-2026-sipearl-vp-says-following-long-development-process",
    "domain": "AI 算力 / 半导体",
    "title": "SiPearl's long-awaited Rhea CPU finally gets in the lab, opening the door for Europe's first sovereign HPC CPU — 'availability of Rhea1 is scheduled for end of 2026' SiPearl VP says, following long de",
    "url": "https://www.tomshardware.com/pc-components/cpus/sipearls-long-awaited-rhea-cpu-finally-gets-in-the-lab-opening-the-door-for-europes-first-sovereign-hpc-cpu-availability-of-rhea1-is-scheduled-for-end-of-2026-sipearl-vp-says-following-long-development-process",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T14:44:59+00:00",
    "summary": "How a limited run CPU could open the right doors for Europe's first HPC processors on markets its developers barely hoped to address any time soon."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/power-company-hikes-data-center-bills-by-30-percent-cuts-residential-electricity-costs-by-1-3-percent-oregon-approves-change-through-power-act-pushes-developments-using-more-than-20-megawatts-of-power-to-pay-their-fair-share",
    "domain": "AI 算力 / 半导体",
    "title": "Power company hikes data center bills by 30%, cuts residential electricity costs by 1.3% — Oregon approves change through POWER Act, pushes developments using more than 20 Megawatts of power to pay th",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/power-company-hikes-data-center-bills-by-30-percent-cuts-residential-electricity-costs-by-1-3-percent-oregon-approves-change-through-power-act-pushes-developments-using-more-than-20-megawatts-of-power-to-pay-their-fair-share",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T13:56:27+00:00",
    "summary": "Oregon approves the 29.7% price hike that Portland General Electric (PGE), the state's largest power provider, will impose on users that consume 20MW or more. This move is backed by Oregon's POWER Act"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/a-team-of-engineers-called-slopfix-charges-10000-a-week-to-delete-ai-generated-code-using-ai-agents",
    "domain": "AI 算力 / 半导体",
    "title": "'Slopfix' software team charges $10,000 a week to delete AI-generated code bloat — ironically, the team uses AI agents to trim messy repositories by up to 65%",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/a-team-of-engineers-called-slopfix-charges-10000-a-week-to-delete-ai-generated-code-using-ai-agents",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T13:19:17+00:00",
    "summary": "A software house known as 'Slopfix' has launched a fixed-price service that refactors AI-generated codebases, charging $10,000 for one week of work."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/wearable-tech/fi-ultra-becomes-first-dog-tracker-powered-by-starlink-satellites-the-fi-ultra-dog-tracker-makes-fido-trackable-via-satellite-onboard-gps-and-lte-connectivity",
    "domain": "AI 算力 / 半导体",
    "title": "Fi Ultra becomes first dog tracker powered by Starlink satellites – the Fi Ultra Dog Tracker makes Fido trackable via satellite, onboard GPS, and LTE connectivity",
    "url": "https://www.tomshardware.com/peripherals/wearable-tech/fi-ultra-becomes-first-dog-tracker-powered-by-starlink-satellites-the-fi-ultra-dog-tracker-makes-fido-trackable-via-satellite-onboard-gps-and-lte-connectivity",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T13:11:25+00:00",
    "summary": "Smart pet technology firm Fi has launched the Fi Ultra Dog Tracker today, the first such device with Starlink connectivity."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/air-cooling/cooler-master-v4-and-v8-3dhp-review",
    "domain": "AI 算力 / 半导体",
    "title": "Cooler Master V4 and V8 3DHP Review: A masterful engineering achievement",
    "url": "https://www.tomshardware.com/pc-components/air-cooling/cooler-master-v4-and-v8-3dhp-review",
    "source": "Albert Thomas",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T13:02:20+00:00",
    "summary": "Cooler Master’s 3DHP heatpipes, in its Master V4 and V8 coolers, are the biggest advancement in air cooling technology in years. But early adoption comes at a price."
  },
  {
    "id": "hn:48554206",
    "domain": "AI 算力 / 半导体",
    "title": "Semiconductor Lifeline Keeps Fighter Jets in the Air",
    "url": "https://spectrum.ieee.org/phoenix-semiconductors-legacychips-oems",
    "source": "rbanffy",
    "platform": "hackernews",
    "points": 79,
    "published_at": "2026-06-16T12:31:02+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/can-agentic-ai-solve-the-embedded-software-problem/",
    "domain": "AI 算力 / 半导体",
    "title": "Can Agentic AI Solve the Embedded Software Problem?",
    "url": "https://www.eetimes.com/can-agentic-ai-solve-the-embedded-software-problem/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T22:00:00+00:00",
    "summary": "Agents will also need CPU plus acceleration to run on edge devices, said Ambarella’s Muneyb Minhazuddin. The post Can Agentic AI Solve the Embedded Software Problem? appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/optimizing-electromechanical-hardware-for-extreme-defense-environments/",
    "domain": "AI 算力 / 半导体",
    "title": "Optimizing Electromechanical Hardware for Extreme Defense Environments",
    "url": "https://www.eetimes.com/optimizing-electromechanical-hardware-for-extreme-defense-environments/",
    "source": "Emily Newton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T17:00:00+00:00",
    "summary": "Commercial parts die fast in combat. See how advanced composites, coatings and MIL testing keep defense hardware alive under brutal stress. The post Optimizing Electromechanical Hardware for Extreme D"
  },
  {
    "id": "rss:https://www.eetimes.com/manufacturing-expands-in-june-amid-global-unrest/",
    "domain": "AI 算力 / 半导体",
    "title": "Manufacturing Expands in June Amid Global Unrest",
    "url": "https://www.eetimes.com/manufacturing-expands-in-june-amid-global-unrest/",
    "source": "News Desk",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T12:30:00+00:00",
    "summary": "U.S. manufacturing expanded in June, but Middle East conflict impacted raw materials. The post Manufacturing Expands in June Amid Global Unrest appeared first on EE Times."
  },
  {
    "id": "hn:48759308",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia offers startup customers chance to swap compute power for revenue share",
    "url": "https://www.cnbc.com/2026/07/02/nvidia-plans-to-offer-start-up-customers-access-to-revenue-sharing-deals.html",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 26,
    "published_at": "2026-07-02T10:41:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:48734960",
    "domain": "AI 算力 / 半导体",
    "title": "Etched has officially come out of stealth",
    "url": "https://www.bloomberg.com/news/articles/2026-06-30/ai-chip-startup-etched-says-jane-street-tsmc-linked-vc-invested",
    "source": "seventeen29",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-06-30T16:21:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:48601996",
    "domain": "AI 算力 / 半导体",
    "title": "ASML denies US Government report that EUV chipmaking tool was shipped to China",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/asml-denies-us-government-report-that-its-euv-chipmaking-tool-was-shipped-to-china-says-rumors-are-inaccurate-and-damaging-to-our-reputation",
    "source": "srameshc",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-06-19T19:03:30+00:00",
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
    "id": "hn:48735444",
    "domain": "大厂 AI 动态",
    "title": "Nano Banana 2 Lite",
    "url": "https://deepmind.google/models/gemini-image/flash-lite/",
    "source": "minimaxir",
    "platform": "hackernews",
    "points": 435,
    "published_at": "2026-06-30T16:48:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:48756602",
    "domain": "大厂 AI 动态",
    "title": "Kimi K2.7 Code is generally available in GitHub Copilot",
    "url": "https://github.blog/changelog/2026-07-01-kimi-k2-7-is-now-available-in-github-copilot/",
    "source": "unliftedq",
    "platform": "hackernews",
    "points": 417,
    "published_at": "2026-07-02T04:32:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:48473166",
    "domain": "大厂 AI 动态",
    "title": "AWS Bedrock to require sharing data with Anthropic for Mythos and future models",
    "url": "https://news.ycombinator.com/item?id=48473166",
    "source": "TomAnthony",
    "platform": "hackernews",
    "points": 427,
    "published_at": "2026-06-10T08:21:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:48662999",
    "domain": "大厂 AI 动态",
    "title": "Computer use in Gemini 3.5 Flash",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/",
    "source": "swolpers",
    "platform": "hackernews",
    "points": 242,
    "published_at": "2026-06-24T17:21:34+00:00",
    "summary": ""
  },
  {
    "id": "hn:48707103",
    "domain": "大厂 AI 动态",
    "title": "Google limits Meta's use of its Gemini AI models",
    "url": "https://www.cnbc.com/2026/06/28/google-limits-metas-use-of-its-gemini-ai-models-ft-reports.html",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 162,
    "published_at": "2026-06-28T13:30:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:48846086",
    "domain": "大厂 AI 动态",
    "title": "Ollama Raises $65M to Accelerate Open Models",
    "url": "https://ollama.com/blog/all-aboard-open-models",
    "source": "srikanth235",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-07-09T14:05:22+00:00",
    "summary": ""
  },
  {
    "id": "hn:48774429",
    "domain": "大厂 AI 动态",
    "title": "Gemini Code Assist will be shut down on July 17",
    "url": "https://docs.cloud.google.com/gemini/docs/code-review/review-repo-code",
    "source": "ushakov",
    "platform": "hackernews",
    "points": 64,
    "published_at": "2026-07-03T12:52:48+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/tech/963728/microsoft-sustainability-report-2026",
    "domain": "大厂 AI 动态",
    "title": "Microsoft’s carbon emissions went up 25 percent last year",
    "url": "https://www.theverge.com/tech/963728/microsoft-sustainability-report-2026",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T00:04:13+00:00",
    "summary": "Microsoft may once again be struggling to keep up with its own climate goals, according to its 2026 sustainability report. As reported by GeekWire, the report states that Microsoft's carbon emissions "
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/963738/openai-fidji-simo-steps-down-ceo-advisor",
    "domain": "大厂 AI 动态",
    "title": "Fidji Simo steps down from leading OpenAI’s AGI work due to illness",
    "url": "https://www.theverge.com/ai-artificial-intelligence/963738/openai-fidji-simo-steps-down-ceo-advisor",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T23:24:04+00:00",
    "summary": "OpenAI's Fidji Simo is departing her full-time role as the company's AGI chief and is transitioning to being a \"part-time advisor,\" she said on X. The news follows Simo's original announcement in Apri"
  },
  {
    "id": "rss:https://www.theverge.com/streaming/963733/netflix-always-on-channels-bundles",
    "domain": "大厂 AI 动态",
    "title": "Netflix reportedly considers adding always-on channels",
    "url": "https://www.theverge.com/streaming/963733/netflix-always-on-channels-bundles",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T23:00:31+00:00",
    "summary": "Netflix is thinking about adding always-on channels that would stream specific shows and movies, according to The Wall Street Journal. The move sounds like a Netflix version of always-on services like"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/963654/openai-chatgpt-atlas-ai-browser-shut-down-sunset",
    "domain": "大厂 AI 动态",
    "title": "The ChatGPT browser is already dead",
    "url": "https://www.theverge.com/ai-artificial-intelligence/963654/openai-chatgpt-atlas-ai-browser-shut-down-sunset",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T20:34:05+00:00",
    "summary": "OpenAI is already shutting down ChatGPT Atlas, its browser that could do tasks for you on your behalf, less than a year after launching it. Atlas was announced in October, but as part of its wave of n"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/963537/anker-soundcore-boom-2-bluetooth-speaker-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "The floatable, powerful Soundcore Boom 2 speaker is over half off",
    "url": "https://www.theverge.com/gadgets/963537/anker-soundcore-boom-2-bluetooth-speaker-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T20:32:18+00:00",
    "summary": "Bluetooth speakers with big sound and great features are hard to find for under $100, with most offerings being some variation of the same basic (and often small) design. Thankfully, through July 10th"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/963628/google-ai-generated-ads-label",
    "domain": "大厂 AI 动态",
    "title": "Google will now tell you if an ad was made with AI",
    "url": "https://www.theverge.com/ai-artificial-intelligence/963628/google-ai-generated-ads-label",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T20:11:38+00:00",
    "summary": "You can see if ads on Google Search, Google Discover, and YouTube were made or edited using AI from a new section in Google's \"My Ad Center,\" as reported earlier by TechCrunch. The update, announced o"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/963475/google-nest-thermostat-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Google&#8217;s Nest Thermostat has hit its best price of the year",
    "url": "https://www.theverge.com/gadgets/963475/google-nest-thermostat-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T17:33:46+00:00",
    "summary": "If you&#8217;re looking for a relatively affordable way to cut down on cooling costs, Google&#8217;s Nest Thermostat can help. It’s packed with smart controls and energy-saving features, and right now"
  },
  {
    "id": "rss:https://www.theverge.com/tech/963307/microsoft-patch-tuesday-ai-security-updates",
    "domain": "大厂 AI 动态",
    "title": "Microsoft’s patch Tuesdays are about to get bigger",
    "url": "https://www.theverge.com/tech/963307/microsoft-patch-tuesday-ai-security-updates",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T17:00:00+00:00",
    "summary": "Windows 11 updates could soon include fixes for more security issues at once. Microsoft said in a blog post on Thursday that it's now using AI to \"identify potential issues earlier,\" which means \"cust"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/963464/openai-gpt-5-6-codex-chatgpt-work",
    "domain": "大厂 AI 动态",
    "title": "OpenAI rolls out GPT-5.6 after government greenlight — and announces ‘ChatGPT Work’",
    "url": "https://www.theverge.com/ai-artificial-intelligence/963464/openai-gpt-5-6-codex-chatgpt-work",
    "source": "Hayden Field",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T17:00:00+00:00",
    "summary": "About two weeks after OpenAI's GPT-5.6 was caught up in regulatory drama - rolled out only to government-approved organizations during a \"limited preview\" period - the company has received the Trump a"
  },
  {
    "id": "rss:https://www.theverge.com/tech/963100/schlage-sense-pro-review-apple-home-key-uwb-handsfree-unlock",
    "domain": "大厂 AI 动态",
    "title": "Schlage’s Sense Pro unlocks the door so I don’t have to",
    "url": "https://www.theverge.com/tech/963100/schlage-sense-pro-review-apple-home-key-uwb-handsfree-unlock",
    "source": "Jennifer Pattison Tuohy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T15:45:46+00:00",
    "summary": "The Schlage Sense Pro is a beautiful smart lock. Sleek, discreet, and simple to use, it's Schlage's smartest lock to date. Thanks to ultra-wideband (UWB), it unlocks as I walk up to my front door; I d"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/09/after-apple-indias-smartphone-manufacturing-boom-enters-new-phase-with-vivo-jv/",
    "domain": "大厂 AI 动态",
    "title": "After Apple, India’s smartphone manufacturing boom enters new phase with Vivo JV",
    "url": "https://techcrunch.com/2026/07/09/after-apple-indias-smartphone-manufacturing-boom-enters-new-phase-with-vivo-jv/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T04:36:20+00:00",
    "summary": "Vivo's joint venture could become a template for Chinese smartphone makers in India."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/09/openai-says-gpt-5-6-is-the-preferred-model-for-microsoft-copilot-amid-breakup-chatter/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI says GPT 5.6 is the ‘preferred model’ for Microsoft Copilot 365 amid breakup chatter",
    "url": "https://techcrunch.com/2026/07/09/openai-says-gpt-5-6-is-the-preferred-model-for-microsoft-copilot-amid-breakup-chatter/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T00:16:54+00:00",
    "summary": "OpenAI's new family of models will continue to power Microsoft's suite of workplace and productivity apps."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/09/dont-want-to-invest-in-elon-musk-two-new-etfs-explicitly-exclude-him/",
    "domain": "大厂 AI 动态",
    "title": "Don’t want to invest in Elon Musk? Two new ETFs explicitly exclude him",
    "url": "https://techcrunch.com/2026/07/09/dont-want-to-invest-in-elon-musk-two-new-etfs-explicitly-exclude-him/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T00:13:00+00:00",
    "summary": "The new exchanged-traded funds exclude companies that are founded, controlled, or led by Elon Musk. That means no SpaceX or Tesla."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/09/fidji-simo-steps-down-from-openais-no-2-role/",
    "domain": "大厂 AI 动态",
    "title": "Fidji Simo steps down from OpenAI’s no. 2 role",
    "url": "https://techcrunch.com/2026/07/09/fidji-simo-steps-down-from-openais-no-2-role/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T23:38:00+00:00",
    "summary": "OpenAI's No. 2 executive, Fidji Simo, is stepping down from her full-time role after her medical leave proved longer than expected — a leadership vacuum that comes at a tricky time as the company eyes"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI launches its new family of models with GPT-5.6",
    "url": "https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T22:24:24+00:00",
    "summary": "OpenAI's latest family of models promises improvements across a range of areas, including cybersecurity."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/09/an-ai-agent-startup-just-let-its-agent-run-its-100-million-fundraise/",
    "domain": "大厂 AI 动态",
    "title": "An AI agent startup just let its agent run its $100M fundraise",
    "url": "https://techcrunch.com/2026/07/09/an-ai-agent-startup-just-let-its-agent-run-its-100-million-fundraise/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T22:08:58+00:00",
    "summary": "Lyzr, a startup that builds AI agents for enterprises, used its own AI agent to raise a $100 million round — proof, evidently, that the product actually works."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/09/openai-is-shutting-down-atlas-but-its-ai-browser-ambitions-are-still-growing/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI is shutting down Atlas, but its AI browser ambitions are still growing",
    "url": "https://techcrunch.com/2026/07/09/openai-is-shutting-down-atlas-but-its-ai-browser-ambitions-are-still-growing/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T22:03:54+00:00",
    "summary": "OpenAI is sunsetting its AI-powered browser after less than a year. But it's moving some agentic browsing features to its desktop app and a Chrome extension."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/09/elon-musk-praises-mythos-fable-promises-not-to-cut-off-anthropic/",
    "domain": "大厂 AI 动态",
    "title": "Elon Musk praises Mythos/Fable, promises not to ‘cut off’ Anthropic",
    "url": "https://techcrunch.com/2026/07/09/elon-musk-praises-mythos-fable-promises-not-to-cut-off-anthropic/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T21:57:42+00:00",
    "summary": "Should Anthropic trust Elon Musk to host its models? With about $40 billion in revenue at stake, Musk insists that the company can."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/09/can-ai-answer-the-3-trillion-question/",
    "domain": "大厂 AI 动态",
    "title": "Can AI answer the $3 trillion question?",
    "url": "https://techcrunch.com/2026/07/09/can-ai-answer-the-3-trillion-question/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T21:47:50+00:00",
    "summary": "The AI ROI debate has returned and the numbers are even bigger, as are, perhaps, the consequences."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/09/meta-enters-the-crowded-ai-coding-battle-with-muse-spark-1-1/",
    "domain": "大厂 AI 动态",
    "title": "Meta enters the crowded AI coding battle with Muse Spark 1.1",
    "url": "https://techcrunch.com/2026/07/09/meta-enters-the-crowded-ai-coding-battle-with-muse-spark-1-1/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T19:40:45+00:00",
    "summary": "Meta's pitch to users is Spark's ability to handle large agentic workloads, fix bugs, and help with large code migrations — the kind of automation that enterprises are increasingly turning to AI compa"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/09/charles-hudson-shares-the-common-mistakes-hes-seen-after-investing-in-500-startups/",
    "domain": "大厂 AI 动态",
    "title": "Charles Hudson shares the common mistakes he’s seen after investing in 500+ startups",
    "url": "https://techcrunch.com/2026/07/09/charles-hudson-shares-the-common-mistakes-hes-seen-after-investing-in-500-startups/",
    "source": "Maggie Nye",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T19:26:31+00:00",
    "summary": "In this week’s episode of Build Mode, Isabelle Johannessen talks with Precursor Ventures' Charles Hudson about the headwinds facing early-stage founders today and the most common mistakes founders sho"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/09/new-york-times-says-openai-hid-evidence-in-chatgpt-copyright-trial/",
    "domain": "大厂 AI 动态",
    "title": "New York Times says OpenAI hid evidence in ChatGPT copyright trial",
    "url": "https://techcrunch.com/2026/07/09/new-york-times-says-openai-hid-evidence-in-chatgpt-copyright-trial/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T19:05:58+00:00",
    "summary": "News publishers say OpenAI hid tools and datasets that could identify copyrighted journalism in ChatGPT outputs, escalating their lawsuit with a new motion for sanctions."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/09/slate-auto-teams-up-with-crayola-to-color-its-ev-truck/",
    "domain": "大厂 AI 动态",
    "title": "Slate Auto teams up with Crayola to color its EV truck",
    "url": "https://techcrunch.com/2026/07/09/slate-auto-teams-up-with-crayola-to-color-its-ev-truck/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T19:01:16+00:00",
    "summary": "Slate has an answer for owners who have always want to drive a truck with bright crayon colors."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/09/fanduel-sent-a-video-from-star-athlete-bryce-harper-to-a-customer-with-a-gambling-problem/",
    "domain": "大厂 AI 动态",
    "title": "FanDuel sent a video from star athlete Bryce Harper to a customer with a gambling problem",
    "url": "https://techcrunch.com/2026/07/09/fanduel-sent-a-video-from-star-athlete-bryce-harper-to-a-customer-with-a-gambling-problem/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T18:50:00+00:00",
    "summary": "The video call highlights the murky relationship between professional athletes and gambling apps."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/09/mercor-is-in-talks-for-a-20b-valuation/",
    "domain": "大厂 AI 动态",
    "title": "Mercor is in talks for a $20B valuation",
    "url": "https://techcrunch.com/2026/07/09/mercor-is-in-talks-for-a-20b-valuation/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T18:42:22+00:00",
    "summary": "A new $20 billion valuation would be a giant step up from the $10 billion valuation it reached in October."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/09/google-will-now-disclose-which-ads-are-made-with-ai/",
    "domain": "大厂 AI 动态",
    "title": "Google will now disclose which ads are made with AI",
    "url": "https://techcrunch.com/2026/07/09/google-will-now-disclose-which-ads-are-made-with-ai/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T18:40:51+00:00",
    "summary": "While Google prohibits misleading and deceptive ads, an ad can still leverage AI to create some type of synthetic or digitally altered content. Until now, that's something Google only required electio"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/09/paris-based-ai-voice-startup-gradium-raises-100m-seed-backed-by-nvidia/",
    "domain": "大厂 AI 动态",
    "title": "Paris-based AI voice startup Gradium raises $100M seed, backed by Nvidia",
    "url": "https://techcrunch.com/2026/07/09/paris-based-ai-voice-startup-gradium-raises-100m-seed-backed-by-nvidia/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T18:34:35+00:00",
    "summary": "The company is using the cash to open an office in the Bay Area and compete for talent there, \"strengthening its position at the heart of the world's leading AI ecosystem.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/09/how-did-the-government-decide-openais-frontier-model-was-safe-to-release/",
    "domain": "大厂 AI 动态",
    "title": "How did the government decide OpenAI’s frontier model was safe to release?",
    "url": "https://techcrunch.com/2026/07/09/how-did-the-government-decide-openais-frontier-model-was-safe-to-release/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T18:22:39+00:00",
    "summary": "\"Exactly what that dialog looked like between the government and Anthropic and OpenAI is unclear.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/09/how-to-stop-metas-ai-image-generator-from-using-your-instagram-photos/",
    "domain": "大厂 AI 动态",
    "title": "Instagram users: Here’s how to stop Meta’s AI from using your photos",
    "url": "https://techcrunch.com/2026/07/09/how-to-stop-metas-ai-image-generator-from-using-your-instagram-photos/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T17:56:47+00:00",
    "summary": "Muse Image allows users to generate AI images using photos from public Instagram accounts. As long as a person's profile is public, another user can tag that account and use their images as part of an"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/09/metas-new-ai-chips-will-begin-production-in-september/",
    "domain": "大厂 AI 动态",
    "title": "Meta’s new AI chips will begin production in September",
    "url": "https://techcrunch.com/2026/07/09/metas-new-ai-chips-will-begin-production-in-september/",
    "source": "Ram Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T17:17:37+00:00",
    "summary": "The company is taking a modular approach to designing these chips, anticipating that their needs will change as AI evolves rapidly by the time the chips are in production."
  },
  {
    "id": "rss:https://stratechery.com/2026/muse-image-grok-4-5-alex-karp-on-cnbc/",
    "domain": "大厂 AI 动态",
    "title": "Muse Image, Grok 4.5, Alex Karp on CNBC",
    "url": "https://stratechery.com/2026/muse-image-grok-4-5-alex-karp-on-cnbc/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T10:00:00+00:00",
    "summary": "The battle for verifiable data is increasingly defining the AI race, from Meta to Grok to the frontier labs."
  },
  {
    "id": "rss:https://stratechery.com/2026/xbox-cuts-bundling-and-the-internet-solvent-transaction-coordination-and-sunk-costs/",
    "domain": "大厂 AI 动态",
    "title": "XBOX Cuts; Bundling and the Internet Solvent; Transaction, Coordination, and Sunk Costs",
    "url": "https://stratechery.com/2026/xbox-cuts-bundling-and-the-internet-solvent-transaction-coordination-and-sunk-costs/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T10:00:00+00:00",
    "summary": "Microsoft's Xbox division is conducting big layoffs, as the company deals with abject failure of its Game Pass strategy."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/flores-hobbits-scavenged-komodo-dragons-elephant-kills-study-suggests/",
    "domain": "大厂 AI 动态",
    "title": "Flores Hobbits' eating habits offer clues about their evolutionary past",
    "url": "https://arstechnica.com/science/2026/07/flores-hobbits-scavenged-komodo-dragons-elephant-kills-study-suggests/",
    "source": "Kiona N. Smith",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T22:29:10+00:00",
    "summary": "If Homo floresiensis wasn't a fire-using hunter, its origins could be different than we thought."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/07/michigans-explosive-outbreak-of-diarrheal-parasite-jumps-to-over-1200-cases/",
    "domain": "大厂 AI 动态",
    "title": "Michigan's explosive outbreak of diarrheal parasite jumps to over 1,200 cases",
    "url": "https://arstechnica.com/health/2026/07/michigans-explosive-outbreak-of-diarrheal-parasite-jumps-to-over-1200-cases/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T21:56:44+00:00",
    "summary": "In neighboring Ohio, cases have reportedly reached over 500."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/07/openai-wants-its-new-tool-to-do-your-work-for-you-and-with-you/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI wants its new tool to do your work for you and with you",
    "url": "https://arstechnica.com/ai/2026/07/openai-wants-its-new-tool-to-do-your-work-for-you-and-with-you/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T21:25:55+00:00",
    "summary": "Rebranded Codex promises independent workflows that can run \"for hours if needed.\""
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/07/patch-for-windows-defender-0-day-could-allow-attackers-to-fill-hard-disk/",
    "domain": "大厂 AI 动态",
    "title": "Patch for Windows Defender 0-day could allow attackers to fill hard disk",
    "url": "https://arstechnica.com/security/2026/07/patch-for-windows-defender-0-day-could-allow-attackers-to-fill-hard-disk/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T20:52:55+00:00",
    "summary": "The feud between NightmareEclipse and Microsoft shows no signs of resolving soon."
  },
  {
    "id": "rss:https://arstechnica.com/information-technology/2026/07/allstate-accuses-broadcom-of-auditing-it-because-it-quit-vmware-ca/",
    "domain": "大厂 AI 动态",
    "title": "Allstate accuses Broadcom of auditing it because it quit VMware, CA",
    "url": "https://arstechnica.com/information-technology/2026/07/allstate-accuses-broadcom-of-auditing-it-because-it-quit-vmware-ca/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T20:28:55+00:00",
    "summary": "Broadcom accuses Allstate of dodging VMware audits."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/07/humanoid-robots-controlled-by-surgeons-did-world-first-operation-on-live-pigs/",
    "domain": "大厂 AI 动态",
    "title": "Humanoid robots controlled by surgeons did world-first operation on live pigs",
    "url": "https://arstechnica.com/ai/2026/07/humanoid-robots-controlled-by-surgeons-did-world-first-operation-on-live-pigs/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T20:12:03+00:00",
    "summary": "Preclinical trial is testing the feasibility of humanoid robots in surgery."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/judge-doesnt-like-elon-musk-settlement-with-sec-but-says-court-cant-block-it/",
    "domain": "大厂 AI 动态",
    "title": "Judge doesn't like Elon Musk settlement with SEC, but says court can't block it",
    "url": "https://arstechnica.com/tech-policy/2026/07/judge-doesnt-like-elon-musk-settlement-with-sec-but-says-court-cant-block-it/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T19:10:33+00:00",
    "summary": "Judge reluctantly approves $1.5M settlement with SEC over Twitter stock violation."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/openai-faked-inability-to-search-training-data-hid-billions-of-logs-nyt-says/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI may have made a fatal misstep in copyright fight with news orgs",
    "url": "https://arstechnica.com/tech-policy/2026/07/openai-faked-inability-to-search-training-data-hid-billions-of-logs-nyt-says/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T18:57:53+00:00",
    "summary": "OpenAI may be sanctioned for hiding, deleting ChatGPT logs in NYT copyright fight."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/07/surprised-doctors-find-10-inch-worm-in-mans-groin-during-elective-surgery/",
    "domain": "大厂 AI 动态",
    "title": "Surprised doctors find 10-inch worm in man's groin during elective surgery",
    "url": "https://arstechnica.com/health/2026/07/surprised-doctors-find-10-inch-worm-in-mans-groin-during-elective-surgery/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T15:33:41+00:00",
    "summary": "Oddly, it wasn't the first time this had happened to the man."
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/07/conspiracies-and-regrets-abound-in-dune-part-three-trailer/",
    "domain": "大厂 AI 动态",
    "title": "Conspiracies and regrets abound in Dune: Part Three trailer",
    "url": "https://arstechnica.com/culture/2026/07/conspiracies-and-regrets-abound-in-dune-part-three-trailer/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T14:45:44+00:00",
    "summary": "\"You promised me that you would never take power in your name.\""
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/07/ruf-debuts-new-flat-eight-engine-at-goodwood/",
    "domain": "大厂 AI 动态",
    "title": "Ruf debuts new flat-eight engine at Goodwood",
    "url": "https://arstechnica.com/cars/2026/07/ruf-debuts-new-flat-eight-engine-at-goodwood/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T14:32:48+00:00",
    "summary": "The 4.8 L eight-cylinder generates more than 1,000 hp and 1,000 Nm, Ruf says."
  },
  {
    "id": "hn:48678873",
    "domain": "股票",
    "title": "OpenAI leans toward waiting until next year for IPO",
    "url": "https://www.nytimes.com/2026/06/25/technology/openai-ipo-artificial-intelligence.html",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 179,
    "published_at": "2026-06-25T20:36:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:48853145",
    "domain": "股票",
    "title": "California universities stockpiling AR-15s, grenades and submachine guns",
    "url": "https://www.theguardian.com/us-news/2026/jul/09/california-universities-military-equipment",
    "source": "sizzle",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-07-09T22:20:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:48846617",
    "domain": "股票",
    "title": "Sony CEO Just Sold over Half His Stock",
    "url": "https://gamerant.com/sony-ceo-sells-stock/",
    "source": "josephcsible",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-07-09T14:37:45+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3776644",
    "domain": "股票",
    "title": "国产AI芯片独角兽燧原科技科创板IPO注册生效",
    "url": "https://wallstreetcn.com/articles/3776644",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T06:22:09+00:00",
    "summary": "腾讯为第一大股东。"
  },
  {
    "id": "wscn:3776643",
    "domain": "股票",
    "title": "中国航天迈入火箭回收时代，专家解析长十乙首飞亮点",
    "url": "https://wallstreetcn.com/articles/3776643",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T06:16:33+00:00",
    "summary": "此次任务是我国首次成功实施运载火箭一级可控回收，同时也是全球首次运载火箭网系回收，长征十号乙运载火箭成为我国首型成功实施回收的重复使用运载火箭。这标志着我国在重复使用火箭技术领域取得历史性突破，将为加快提升我国进出空间能力奠定坚实基础。中国航天也就此迈入火箭回收时代。"
  },
  {
    "id": "wscn:3776629",
    "domain": "股票",
    "title": "A股午后齐跌，创业板跌超3%，商业航天掀起涨停潮，创新药爆发，恒科指涨近2%，AI模型“双雄”下挫",
    "url": "https://wallstreetcn.com/articles/3776629",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T06:14:06+00:00",
    "summary": "盘面上，个股涨多跌少，沪深京三市近4500股飘红，量能明显放大，上午半天成交2.18万亿。沪深两市半日成交额2.17万亿，较上个交易日放量超4700亿。板块方面，医药股爆发，CRO、减肥药、创新药方向涨幅居前，文化传媒、电脑硬件、房地产、汽车板块活跃，半导体产业链回调，能源设备板块低迷。"
  },
  {
    "id": "wscn:3776640",
    "domain": "股票",
    "title": "三星开发AI PC专用芯片“GAIA”，已向联想、惠普供样测试",
    "url": "https://wallstreetcn.com/articles/3776640",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T06:08:36+00:00",
    "summary": "三星正以代号\"GAIA\"的AI加速芯片悄然杀入PC市场——这款采用4纳米制程、深度融合下一代PIM内存技术的专用NPU芯片，已向联想、惠普送样验证，最快明年量产。面对英伟达、高通、英特尔的强势围攻，三星选择差异化突围：不替代主处理器，而是以专用AI计算模块协同作战。"
  },
  {
    "id": "wscn:3776623",
    "domain": "股票",
    "title": "科技股反弹提振亚太市场，韩股再度熔断，日经上涨1.8%，日元走强，布油企稳76美元",
    "url": "https://wallstreetcn.com/articles/3776623",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T05:27:55+00:00",
    "summary": "韩国交易所启动KOSDAQ指数熔断机制，暂停KOSDAQ程序化买盘。韩股单日大涨5%，领涨亚太市场。日经225指数涨1.8%，东证指数涨0.7%。SK海力士完成265亿美元ADR发行，将于周五登陆纳斯达克，成为韩股上涨的核心催化剂。但财报季将是检验科技股估值能否持续的关键。"
  },
  {
    "id": "wscn:3776447",
    "domain": "股票",
    "title": "韬定律V2：性能打破物理极限，更重要的是如何重塑国产先进制程？",
    "url": "https://wallstreetcn.com/premium/articles/3776447?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T05:26:09+00:00",
    "summary": "华为“韬（τ）定律”V2版本发布，首次公开麒麟2026量产实测数据，验证逻辑折叠技术落地可行性，标志着国产先进制程从“追赶者”向“定义者”的历史性跨越。"
  },
  {
    "id": "wscn:3776638",
    "domain": "股票",
    "title": "中国可回收火箭里程碑时刻！长征十号乙首飞成功，实现全球首创海上网系回收",
    "url": "https://wallstreetcn.com/articles/3776638",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T05:16:28+00:00",
    "summary": "中国航天再创历史！2026年7月10日，长征十号乙运载火箭首飞成功，以全球首创\"海上网系捕获\"方式完成一子级回收，开辟出一条独立于SpaceX的全新技术路径。复用不足5次即可体现成本优势，复用10次以上单次发射成本有望骤降80%，面对国内2.8万颗卫星的庞大市场，这场降本革命才刚刚开始。"
  },
  {
    "id": "wscn:3776637",
    "domain": "股票",
    "title": "NAND单季涨70%后，SK海力士重启大连二期，与三星西安竞赛提速",
    "url": "https://wallstreetcn.com/articles/3776637",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T05:07:22+00:00",
    "summary": "受NAND价格大涨超70%的红利驱动，SK海力士计划于2026年下半年重启大连二期扩建，新增V8（238层）产线，月产能目标3万至5万片晶圆。与此同时，三星西安工厂已完成236层V8产线转换并进入量产，两大巨头在华同步扩产宣告NAND供给端重回扩张轨道。"
  },
  {
    "id": "wscn:3776621",
    "domain": "股票",
    "title": "五大工作组来了--沃什“统一战线”，意在降息？",
    "url": "https://wallstreetcn.com/articles/3776621",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T05:01:00+00:00",
    "summary": "美联储主席沃什推动的政策框架改革进入实质阶段——五大工作组7月9日正式亮相，汇聚前英国央行行长、诺贝尔经济学奖得主及Marc Andreessen等重量级人士。叠加此前，BEA悄然调整PCE统计方法，高盛、瑞银警示通胀读数将被系统性压低。中信建投预演了一套清晰的三步走路线图：人事布局、框架重塑、鸽派转向，终点直指四季度降息。"
  },
  {
    "id": "wscn:3776630",
    "domain": "股票",
    "title": "本轮AI何时见顶？过去二十年六个高景气行业案例：股价顶点领先基本面顶点约1-1.5 年，高景气行业往往呈现“M顶”",
    "url": "https://wallstreetcn.com/articles/3776630",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T05:00:32+00:00",
    "summary": "国信证券认为，历史上六大高景气行业数据揭示，股价顶部通常领先基本面拐点1至1.5年——\"业绩还在兑现\"并不等于\"行情还没见顶\"。高景气板块普遍呈现M顶形态，利好钝化正是早期预警信号。本轮AI算力行情的命运，关键取决于科技巨头Capex走向：当前总量扩张势头未止，但微软、Meta的资本开支二阶导已率先转负，拐点信号不容忽视。"
  },
  {
    "id": "wscn:3776625",
    "domain": "股票",
    "title": "全球炼油瓶颈：从霍尔木兹海峡转向俄罗斯",
    "url": "https://wallstreetcn.com/articles/3776625",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T04:29:25+00:00",
    "summary": "全球油市真正的瓶颈，已悄然从霍尔木兹海峡转移至俄罗斯炼厂。摩根大通数据显示，无人机持续轰炸使俄炼厂开工骤降至360万桶/日，较正常水平缩水近四成，俄罗斯排名前十的炼厂仅剩一家未受波及。原油或走向宽松，但柴油、燃料油缺口料将持续至2027年，霍尔木兹决定原油流量，俄罗斯炼厂才是成品油的真正命门。"
  },
  {
    "id": "wscn:3776562",
    "domain": "股票",
    "title": "交换机超级周期：AI\"第三个算力瓶颈\"，以太网主宰万亿盛宴？",
    "url": "https://wallstreetcn.com/premium/articles/3776562?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T04:12:03+00:00",
    "summary": "全球AI以太网数据中心交换机市场正经历前所未有的超级周期，2025-2030年CAGR高达61%，市场规模将从约81亿美元飙升至889亿美元。"
  },
  {
    "id": "wscn:3776631",
    "domain": "股票",
    "title": "大摩上调联想评级：从“内存逆风”到“服务器利润爆发”",
    "url": "https://wallstreetcn.com/articles/3776631",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T04:06:44+00:00",
    "summary": "摩根士丹利认为AI驱动需求从根本改变内存供需格局，联想凭借规模采购优势获得定价权，可将成本转嫁客户，将联想评级上调至\"增持\"。该行预计基础设施解决方案ISG业务预计2027财年收入暴增74%，利润占比将升至35%。"
  },
  {
    "id": "wscn:3776635",
    "domain": "股票",
    "title": "MiniMaxCEO闫俊杰发全员信：不再领取薪酬，个人将拿出4%股份用于团队激励，拿出1%股份支持开源发展",
    "url": "https://wallstreetcn.com/articles/3776635",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T03:30:26+00:00",
    "summary": "面对IPO后首次大规模解禁引发的股价重挫，MiniMax创始人闫俊杰宣布即日起放弃薪酬，直至公司实现AGI，并拿出个人4%股份用于激励团队，以\"创始人式押注\"稳定军心。与此同时，公司完成160亿港币新融资，吸引全球顶级主权基金参与。MiniMax还曝出正研发2.7万亿参数巨模型M3 Pro，规模远超现有旗舰模型M3参数。"
  },
  {
    "id": "wscn:3776627",
    "domain": "股票",
    "title": "洪灝：IPO市场吸引所有注意力，恒生科技指数仍在徘徊，短期会反弹几天，但高估值个股仍不够便宜，不值得长期持有",
    "url": "https://wallstreetcn.com/articles/3776627",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T02:11:52+00:00",
    "summary": "解禁潮来袭，港股高估值个股面临巨大抛压。"
  },
  {
    "id": "wscn:3776628",
    "domain": "股票",
    "title": "财长鼓励GPIF养老基金增加对国内金融资产投资，日本股债汇齐涨",
    "url": "https://wallstreetcn.com/articles/3776628",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T02:02:32+00:00",
    "summary": "日本财务大臣片山皋月承诺降低债务占GDP比例以确保市场信任，并支持GPIF加大日本资产投资。讲话后10年期国债收益率下行逾10个基点，日经225涨超2.2%，日元汇率跳涨0.4%。大和证券认为收益率下行将直接对股市构成支撑，而GPIF若加大国内资产配置，亦将对日元形成托底。"
  },
  {
    "id": "wscn:3776624",
    "domain": "股票",
    "title": "存储模组大厂透露：内存将继续涨价",
    "url": "https://wallstreetcn.com/articles/3776624",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T01:44:42+00:00",
    "summary": "威刚董事长陈立白披露，2026年三季度DRAM合约价将上涨20%-30%，NAND Flash将上涨35%-40%。TrendForce预计三季度DRAM季增13%-18%，NAND Flash季增10%-15%；瑞银则更为乐观，预计DRAM三季度涨32%，并认为供需紧张将持续至2028年上半年。"
  },
  {
    "id": "wscn:3776573",
    "domain": "股票",
    "title": "去杠杆风暴下半场：美韩半导体风险释放到什么程度？",
    "url": "https://wallstreetcn.com/premium/articles/3776573?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T01:43:50+00:00",
    "summary": "美韩半导体去杠杆或正进入中后期，流动性出清仍未完成，估值修复仍需等待基本面接力。"
  },
  {
    "id": "wscn:3776618",
    "domain": "股票",
    "title": "美国监管机构警告：Robotaxi对公众构成“危险”",
    "url": "https://wallstreetcn.com/articles/3776618",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T01:34:02+00:00",
    "summary": "美国国家公路交通安全管理局发函警告，自动驾驶车辆频繁阻碍急救人员通行，对公众构成“危险”。局长Jonathan Morrison要求各自动驾驶企业优先改善与急救人员的交互能力，并将于本月底前与各公司逐一会谈。"
  },
  {
    "id": "wscn:3776622",
    "domain": "股票",
    "title": "当费城半导体年内暴涨83%，而七巨头原地踏步，华尔街顶级策略师集体喊\"换牌\"",
    "url": "https://wallstreetcn.com/articles/3776622",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T01:06:14+00:00",
    "summary": "上半年\"科技七巨头\"几乎原地踏步，而标普500指数同期上涨9.3%。资金大量流向芯片股，费城半导体指数迄今累涨83%。七巨头估值虽已从32.6倍降至23.9倍，估值溢价接近历史低点，但市场对其AI投资回报前景仍持观望态度。摩根士丹利、高盛等机构则认为七巨头跌幅已过度，呼吁重新布局。"
  },
  {
    "id": "hn:48824532",
    "domain": "股票",
    "title": "SpaceX Shares Stumble in Nasdaq-100 Debut",
    "url": "https://www.wsj.com/finance/stocks/spacex-shares-stumble-in-nasdaq-100-debut-9ec10565",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-07-07T22:00:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:48826804",
    "domain": "股票",
    "title": "AI has taken over the stock market. The bond market is next",
    "url": "https://www.economist.com/finance-and-economics/2026/07/07/ai-has-taken-over-the-stock-market-the-bond-market-is-next",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-07-08T02:32:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:48504013",
    "domain": "股票",
    "title": "SpaceX's president is floating a Tesla merger as the company begins trading",
    "url": "https://qz.com/spacex-tesla-merger-gwynne-shotwell-ipo-061226",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 72,
    "published_at": "2026-06-12T13:47:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:48612095",
    "domain": "股票",
    "title": "Show HN: My Windows XP portfolio with working Game Boy and iPod",
    "url": "https://mitchivin.com/",
    "source": "mitchivin",
    "platform": "hackernews",
    "points": 71,
    "published_at": "2026-06-20T19:18:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:48787052",
    "domain": "股票",
    "title": "Elon Musk posted twice as often on UK race and immigration as about SpaceX IPO",
    "url": "https://www.theguardian.com/technology/2026/jul/04/elon-musk-uk-race-immigration-spacex-ipo",
    "source": "iamflimflam1",
    "platform": "hackernews",
    "points": 23,
    "published_at": "2026-07-04T17:18:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:48634931",
    "domain": "股票",
    "title": "SpaceX Drops 14% in One Day, Price Now Below IPO Launch",
    "url": "https://finance.yahoo.com/quote/SPCX/",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 62,
    "published_at": "2026-06-22T19:33:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:48774424",
    "domain": "股票",
    "title": "X has suddenly banned an account documenting Trump's corrupt stock trades",
    "url": "https://twitter.com/HQNewsNow/status/2072699828337864871",
    "source": "doener",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-07-03T12:52:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:48781228",
    "domain": "股票",
    "title": "After $18B IPO, Bending Spoons founder says success comes from minimizing luck",
    "url": "https://techcrunch.com/2026/07/01/after-18b-ipo-bending-spoons-founder-says-success-comes-from-minimizing-luck/",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-07-03T23:31:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:48777130",
    "domain": "股票",
    "title": "Tesla stock sinks 7% despite strong deliveries report, worst day in nearly 1y",
    "url": "https://www.cnbc.com/2026/07/02/tesla-tsla-q2-2026-vehicle-delivery-production.html",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-07-03T16:52:04+00:00",
    "summary": ""
  },
  {
    "id": "hn:48789829",
    "domain": "股票",
    "title": "Ask HN: When will the stock market crash?",
    "url": "https://news.ycombinator.com/item?id=48789829",
    "source": "roschdal",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-07-04T22:55:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:48505968",
    "domain": "股票",
    "title": "Elon Musk Becomes First Trillionaire as SpaceX Starts Trading",
    "url": "https://www.nytimes.com/live/2026/06/12/business/spacex-ipo-elon-musk/heres-the-latest",
    "source": "droidjj",
    "platform": "hackernews",
    "points": 50,
    "published_at": "2026-06-12T16:13:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48748464",
    "domain": "股票",
    "title": "The Stockholm Telephone Tower with Approximately 5,500 Telephone Lines, 1890",
    "url": "https://rarehistoricalphotos.com/the-stockholm-telephone-tower-1890/",
    "source": "thunderbong",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-07-01T15:27:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48598558",
    "domain": "股票",
    "title": "The average SpaceX buyer post-IPO is almost under water after two-day slide",
    "url": "https://www.cnbc.com/2026/06/18/the-average-spacex-buyer-post-ipo-is-almost-under-water-after-two-day-slide.html",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 40,
    "published_at": "2026-06-19T13:48:28+00:00",
    "summary": ""
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
    "id": "hn:48750160",
    "domain": "股票",
    "title": "Tech giants lose $2T in SpaceX's IPO month",
    "url": "https://english.elpais.com/economy-and-business/2026-07-01/tech-giants-lose-2-trillion-in-spacexs-ipo-month-the-valuations-were-unsustainable.html",
    "source": "01-_-",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-07-01T17:14:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:48714428",
    "domain": "股票",
    "title": "SpaceX just landed in 401(k)s due to key index rule changes",
    "url": "https://moneywise.com/news/top-stories/spacex-401k-anthropic-openai-ipo-index-fund-rules",
    "source": "voxadam",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-06-29T03:25:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:48700725",
    "domain": "股票",
    "title": "Cheap Drones Are Rewriting Warfare",
    "url": "https://www.barrons.com/articles/best-military-drone-stocks-4f90e7c6",
    "source": "Anon84",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-06-27T18:56:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:48506701",
    "domain": "股票",
    "title": "SpaceX increases almost 30% after biggest IPO",
    "url": "https://www.cnbc.com/2026/06/12/spacex-ipo-spcx-live-updates.html",
    "source": "somenameforme",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-06-12T17:10:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:48553976",
    "domain": "股票",
    "title": "SpaceX to acquire Cursor for $60B in stock, days after blockbuster IPO",
    "url": "https://techcrunch.com/2026/06/16/spacex-to-acquire-cursor-for-60b-in-stock-days-after-blockbuster-ipo/",
    "source": "frb",
    "platform": "hackernews",
    "points": 28,
    "published_at": "2026-06-16T12:09:34+00:00",
    "summary": ""
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
    "id": "hn:48496263",
    "domain": "股票",
    "title": "Musk's SpaceX prices record $75B IPO at $135 a share",
    "url": "https://www.reuters.com/world/musks-spacex-prices-record-75-billion-ipo-135-share-2026-06-11/",
    "source": "TechTechTech",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-06-11T20:53:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:48497351",
    "domain": "股票",
    "title": "SpaceX officially prices shares at $135 in the largest IPO ever",
    "url": "https://techcrunch.com/2026/06/11/spacex-officially-prices-shares-at-135-in-the-largest-ipo-ever/",
    "source": "7777777phil",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-06-11T22:36:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:48506306",
    "domain": "股票",
    "title": "SpaceX vaults over $2T valuation as stock jumps after record IPO",
    "url": "https://www.reuters.com/legal/transactional/after-record-ipo-musks-spacex-faces-next-test-market-debut-2026-06-12/",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-06-12T16:39:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:48611631",
    "domain": "股票",
    "title": "The Myth of SpaceX",
    "url": "https://www.theatlantic.com/technology/2026/06/spacex-starlink-ipo-elon-musk-trillionaire/687651/",
    "source": "paulpauper",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-06-20T18:30:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:48518603",
    "domain": "股票",
    "title": "SpaceX IPO made Musk a trillionaire. The old rules of capitalism no longer apply",
    "url": "https://www.theguardian.com/commentisfree/2026/jun/12/spacex-ipo-elon-musk-trillionaire",
    "source": "jmngomes",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-06-13T16:09:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:48552280",
    "domain": "股票",
    "title": "SpaceX IPO Is a Giant Unworkable Con",
    "url": "https://karlbode.com/the-spacex-ipo-is-a-giant-unworkable-con-orchestrated-by-an-overt-white-supremacist-huckster/",
    "source": "only_in_america",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-06-16T08:30:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:48486790",
    "domain": "股票",
    "title": "Elizabeth Warren Asks the SEC to Delay the SpaceX IPO",
    "url": "https://www.businessinsider.com/elizabeth-warren-spacex-ipo-delay-letter-sec-2026-6",
    "source": "borski",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-06-11T06:10:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:48759634",
    "domain": "金融",
    "title": "PeerTube is a free, decentralized and federated video platform",
    "url": "https://github.com/Chocobozzz/PeerTube",
    "source": "doener",
    "platform": "hackernews",
    "points": 680,
    "published_at": "2026-07-02T11:17:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:48717469",
    "domain": "金融",
    "title": "The CEO of Mullvad is the main financer of the Swedish Örebro party",
    "url": "https://det.social/@lostgen/116820546568940358",
    "source": "Risse",
    "platform": "hackernews",
    "points": 694,
    "published_at": "2026-06-29T10:45:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:48552687",
    "domain": "金融",
    "title": "Feds freaked over Fable 5 after 'fix this code', not jailbreak, say researchers",
    "url": "https://www.theregister.com/security/2026/06/15/feds-freaked-over-fable-5-after-simple-fix-this-code-prompt-not-jailbreak-says-researcher/5255827",
    "source": "_tk_",
    "platform": "hackernews",
    "points": 613,
    "published_at": "2026-06-16T09:26:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:48634585",
    "domain": "金融",
    "title": "Canada plans 'nuclear renaissance' with up to 10 reactors built by 2040",
    "url": "https://www.cbc.ca/news/politics/federal-nuclear-strategy-9.7244509",
    "source": "geox",
    "platform": "hackernews",
    "points": 593,
    "published_at": "2026-06-22T19:06:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:48484584",
    "domain": "金融",
    "title": "AI agent runs amok in Fedora and elsewhere",
    "url": "https://lwn.net/SubscriberLink/1077035/c7e7c14fbd60fae9/",
    "source": "tanelpoder",
    "platform": "hackernews",
    "points": 552,
    "published_at": "2026-06-11T00:10:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:48673787",
    "domain": "金融",
    "title": "Federal agents track down woman, demand she remove Instagram post about ICE",
    "url": "https://www.syracuse.com/news/2026/06/federal-agents-track-down-syracuse-woman-demand-she-remove-instagram-post-about-ice.html",
    "source": "coloneltcb",
    "platform": "hackernews",
    "points": 217,
    "published_at": "2026-06-25T14:16:17+00:00",
    "summary": ""
  },
  {
    "id": "hn:48647444",
    "domain": "金融",
    "title": "Digital euro clears key hurdle as EU seeks to break free from U.S. credit cards",
    "url": "https://finance.yahoo.com/markets/currencies/articles/ecb-secures-key-parliamentary-backing-102718449.html",
    "source": "madars",
    "platform": "hackernews",
    "points": 232,
    "published_at": "2026-06-23T16:27:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48777266",
    "domain": "金融",
    "title": "International chess federation sanctions Kramnik",
    "url": "https://www.fide.com/fide-ethics-disciplinary-commission-issues-a-decision-in-case-involving-gm-vladimir-kramnik/",
    "source": "DarkContinent",
    "platform": "hackernews",
    "points": 169,
    "published_at": "2026-07-03T17:04:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:48826703",
    "domain": "金融",
    "title": "Is The Economist Always Wrong?",
    "url": "https://www.economist.com/interactive/finance-and-economics/2026/07/02/is-the-economist-always-wrong",
    "source": "nreece",
    "platform": "hackernews",
    "points": 137,
    "published_at": "2026-07-08T02:17:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:48703613",
    "domain": "金融",
    "title": "Feds Killed Polestar and Spared Volvo",
    "url": "https://www.thedrive.com/news/feds-killed-polestar-and-spared-volvo-that-should-terrify-you",
    "source": "mraniki",
    "platform": "hackernews",
    "points": 175,
    "published_at": "2026-06-28T01:55:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:48783175",
    "domain": "金融",
    "title": "The LLVM Compiler Infrastructure",
    "url": "https://cacm.acm.org/federal-funding-of-academic-research/the-llvm-compiler-infrastructure/",
    "source": "tosh",
    "platform": "hackernews",
    "points": 79,
    "published_at": "2026-07-04T06:43:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:48849827",
    "domain": "金融",
    "title": "FrontierFinance: The largest open benchmark for investor workflows",
    "url": "https://research.samaya.ai/benchmarks/frontier-finance",
    "source": "ashwinpp",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-07-09T17:49:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:48785077",
    "domain": "金融",
    "title": "The Fediverse Is Not the Way Forward",
    "url": "https://trialandfailure.net/the-fediverse-is-not-the-way-forward/",
    "source": "ExMachina73",
    "platform": "hackernews",
    "points": 69,
    "published_at": "2026-07-04T12:53:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:48824584",
    "domain": "金融",
    "title": "JPMorgan, BofA and Others Explore Buying Card Network to Raise Debit-Card Fees",
    "url": "https://www.wsj.com/finance/banking/jpmorgan-bank-of-america-and-other-banks-explore-a-deal-to-shake-up-payments-world-9d8639fb",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 38,
    "published_at": "2026-07-07T22:04:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:48735748",
    "domain": "金融",
    "title": "Supreme Court takes sledgehammer to federal regulatory structure",
    "url": "https://www.npr.org/2026/06/29/nx-s1-5875161/supreme-court-takes-sledgehammer-to-much-of-federal-governments-regulatory-structure",
    "source": "marojejian",
    "platform": "hackernews",
    "points": 82,
    "published_at": "2026-06-30T17:05:58+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.07768",
    "domain": "金融",
    "title": "Cascading Effects of the COVID-19 Pandemic on Barangays in the Philippines",
    "url": "https://arxiv.org/abs/2607.07768",
    "source": "Naomi Ashley Amparo, John Frederick Muji, Paul James Montecillo, Jaymar Soriano, Vena Pearl Bongolan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T04:00:00+00:00",
    "summary": "arXiv:2607.07768v1 Announce Type: new Abstract: The COVID-19 pandemic disrupted socio-economic and healthcare systems in the Philippines, significantly affecting barangays. This study analyzes the cas"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.07770",
    "domain": "金融",
    "title": "Helping Hands, Healthier Infants: The Effect of Medicaid Doula Coverage Mandates on Birth Outcomes",
    "url": "https://arxiv.org/abs/2607.07770",
    "source": "Farhad V. Farahani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T04:00:00+00:00",
    "summary": "arXiv:2607.07770v1 Announce Type: new Abstract: Over the last decade a wave of U.S. states began reimbursing doula services through Medicaid, hoping to improve infant health and narrow stark racial ga"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.07849",
    "domain": "金融",
    "title": "The Impact of Publicly Funded Small Business Advisory Services: Firm Take-up and Performance in the United States",
    "url": "https://arxiv.org/abs/2607.07849",
    "source": "Scott Kaplan, Ryan Raimondi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T04:00:00+00:00",
    "summary": "arXiv:2607.07849v1 Announce Type: new Abstract: This paper studies the impact of geographic proximity to and utilization of publicly funded advisory services offered to US small businesses on firm tak"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.07864",
    "domain": "金融",
    "title": "Inflation as an emergent phenomenon",
    "url": "https://arxiv.org/abs/2607.07864",
    "source": "Alessio Emanuele Biondo, Mauro Gallegati",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T04:00:00+00:00",
    "summary": "arXiv:2607.07864v1 Announce Type: new Abstract: We develop an agent-based model in which inflation emerges from decentralized price-setting and credit-financed production in an endogenous-money econom"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.08153",
    "domain": "金融",
    "title": "A Comparative Review of Methods to Create a Composite Index for Sustainable and Inclusive Wellbeing",
    "url": "https://arxiv.org/abs/2607.08153",
    "source": "Ricardo da Silva Vieira, Mario Biggeri, Peter Benczur, Robert Costanza, Joseph Eastoe, Tuuli Hirvilammi, Ida Kubiszewski, Matteo Mazziotta, Kenneth Mulder, Taketo Muroya, Kelsey J. OConnor, Francesco Sarracino, Nikos Rigas, Enrico Giovannini, Rutger Hoekstra, Daniel Hopp, Edwin Horlings, Petra Krylova, Michele Melchiorri, Heriberto Tapia, Oscar Smallenbroek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T04:00:00+00:00",
    "summary": "arXiv:2607.08153v1 Announce Type: new Abstract: Societal goals need to shift from over-reliance on gross domestic product (GDP) to broader aspects of sustainable and inclusive wellbeing (SIW). However"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.08199",
    "domain": "金融",
    "title": "Volatility in Prediction Markets: A Structural Approach",
    "url": "https://arxiv.org/abs/2607.08199",
    "source": "Weiye Xi, Ciamac C. Moallemi, Mallesh Pai, Shouqiao Want",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T04:00:00+00:00",
    "summary": "arXiv:2607.08199v1 Announce Type: new Abstract: Forward-looking volatility forecasts are central inputs to derivatives pricing, market making, risk management, and volatility-linked trading strategies"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.08291",
    "domain": "金融",
    "title": "Robustness in Sequential Decision Making under Evolving Uncertainty: Evidence from High-Frequency Market Making",
    "url": "https://arxiv.org/abs/2607.08291",
    "source": "Ying Chen, Hoa Nguyen, Julian Sester, Hoang Hai Tran, Yijiong Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T04:00:00+00:00",
    "summary": "arXiv:2607.08291v1 Announce Type: new Abstract: We study sequential decision making under evolving uncertainty in high-frequency financial markets, where changing market dynamics continually challenge"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.08500",
    "domain": "金融",
    "title": "Estimating the Stochastic Discount Factor from Option Prices and Predicting the Equity Premium",
    "url": "https://arxiv.org/abs/2607.08500",
    "source": "Kenichiro Shiraya, Tomohisa Yamakami, Akira Yamazaki",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T04:00:00+00:00",
    "summary": "arXiv:2607.08500v1 Announce Type: new Abstract: This paper proposes a stochastic discount factor (SDF) scaled by time-varying volatility. By utilizing prices and market data implied solely from S\\&amp"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.08524",
    "domain": "金融",
    "title": "Stablecoins under Stress in a National Economy: Transaction-Level Evidence from Austrian Crypto-Asset Service Providers",
    "url": "https://arxiv.org/abs/2607.08524",
    "source": "Pietro Saggese, Michael Sigmund, Burkhard Raunig, Esther Segalla, Bernhard Haslhofer, Christos Makridis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T04:00:00+00:00",
    "summary": "arXiv:2607.08524v1 Announce Type: new Abstract: Cryptoassets are increasingly entangled with the traditional financial system, and how this activity integrates into national economies and behaves unde"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.08531",
    "domain": "金融",
    "title": "Optimal Prediction of Resistance and Support Levels under Constant Elasticity of Variance Processes",
    "url": "https://arxiv.org/abs/2607.08531",
    "source": "Ruibo Ma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T04:00:00+00:00",
    "summary": "arXiv:2607.08531v1 Announce Type: new Abstract: Assuming that the asset price $X$ follows a constant elasticity of variance process, this paper studies the optimal prediction problem $\\inf_{0\\leq \\tau"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.08610",
    "domain": "金融",
    "title": "Sharing economy in the era of full automation: Evidence from autonomous vehicle on-demand mobility services",
    "url": "https://arxiv.org/abs/2607.08610",
    "source": "Xiaoyan Wang, Kenan Zhang, Yaochen Ma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T04:00:00+00:00",
    "summary": "arXiv:2607.08610v1 Announce Type: new Abstract: The digital age has facilitated the sharing of underutilized assets. This paper focuses on privately owned autonomous vehicles (AVs), a unique class of "
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.08706",
    "domain": "金融",
    "title": "Directional AI Advice: Experimental Evidence from Healthcare",
    "url": "https://arxiv.org/abs/2607.08706",
    "source": "Yuyu Chen, Hongbin Li, Lingsheng Meng, Xinyao Qiu, Qingxu Yang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T04:00:00+00:00",
    "summary": "arXiv:2607.08706v1 Announce Type: new Abstract: Generative AI is fast becoming the first place people turn for expert advice. The advice it provides can be directional rather than neutral, shaped in p"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.08759",
    "domain": "金融",
    "title": "Measuring Consumption with Credit Card Data: Benchmarking and Beyond",
    "url": "https://arxiv.org/abs/2607.08759",
    "source": "Aditya Aladangady, Ricardo Duque Gabriel, Carlo Wix",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T04:00:00+00:00",
    "summary": "arXiv:2607.08759v1 Announce Type: new Abstract: We introduce a novel monthly county-level consumption dataset constructed from spending data on over 350 million credit cards in the Federal Reserve's Y"
  },
  {
    "id": "rss:https://arxiv.org/abs/2404.16777",
    "domain": "金融",
    "title": "Subset second-order stochastic dominance for enhanced indexation with diversification enforced by sector constraints",
    "url": "https://arxiv.org/abs/2404.16777",
    "source": "Cristiano Arbex Valle, John E Beasley, Nigel Meade",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T04:00:00+00:00",
    "summary": "arXiv:2404.16777v3 Announce Type: replace Abstract: In this paper we apply second-order stochastic dominance (SSD) to the problem of enhanced indexation with asset subset (sector) constraints. The pro"
  },
  {
    "id": "rss:https://arxiv.org/abs/2512.02362",
    "domain": "金融",
    "title": "Reconstructing Large Scale Production Networks",
    "url": "https://arxiv.org/abs/2512.02362",
    "source": "Ashwin Bhattathiripad, Vipin P Veetil",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T04:00:00+00:00",
    "summary": "arXiv:2512.02362v2 Announce Type: replace Abstract: Firm-to-firm production networks matter for aggregate propagation, but they are rarely observed. This paper reconstructs national-scale, weighted fi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2512.22109",
    "domain": "金融",
    "title": "Low-Turnover Rebalancing for Sparse Index Tracking",
    "url": "https://arxiv.org/abs/2512.22109",
    "source": "Dimitrios Roxanas",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T04:00:00+00:00",
    "summary": "arXiv:2512.22109v2 Announce Type: replace Abstract: Sparse index tracking is often evaluated through rolling reconstruction: a sparse portfolio is fitted on an in-sample window, held over the next per"
  },
  {
    "id": "rss:https://arxiv.org/abs/2601.20853",
    "domain": "金融",
    "title": "A Smoothed GMM for Dynamic Quantile Preferences Estimation",
    "url": "https://arxiv.org/abs/2601.20853",
    "source": "Xin Liu, Luciano de Castro, Antonio F. Galvao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T04:00:00+00:00",
    "summary": "arXiv:2601.20853v2 Announce Type: replace Abstract: This paper suggests methods for estimation of the $\\tau$-quantile, $\\tau \\in (0,1)$, as a parameter along with the other finite-dimensional paramete"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.00504",
    "domain": "金融",
    "title": "How optimistic inflow forecasts distort dispatch, prices, and contracts in hydro-dominated power systems: evidence from Brazil",
    "url": "https://arxiv.org/abs/2607.00504",
    "source": "Arthur Brigatto, Alexandre Street, Joaquim Dias Garcia",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T04:00:00+00:00",
    "summary": "arXiv:2607.00504v2 Announce Type: replace Abstract: Centralized hydrothermal planning models determine generation schedules and electricity spot prices based on inflow forecasts in audited-cost power "
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.04103",
    "domain": "金融",
    "title": "Governing Generative AI Across Financial Institutions: An SR 26-2-Compatible Framework for Generative AI Risk Control",
    "url": "https://arxiv.org/abs/2607.04103",
    "source": "Yiqing Wang, Yixin Kang, Luyun Lin, Siqi Mao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T04:00:00+00:00",
    "summary": "arXiv:2607.04103v2 Announce Type: replace Abstract: The release of SR 26-2 marks a significant modernization of U.S. model risk management by replacing SR 11-7 with a more risk-based and materiality-s"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.05011",
    "domain": "金融",
    "title": "Reaction-boundary variance and adjoint-consistent local-volatility projection",
    "url": "https://arxiv.org/abs/2607.05011",
    "source": "Chris Angstmann, Tim Gebbie",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T04:00:00+00:00",
    "summary": "arXiv:2607.05011v2 Announce Type: replace Abstract: We derive an operational-time variance kernel for a latent-order-book reaction boundary and use it to separate three objects usually collapsed in ca"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.05091",
    "domain": "金融",
    "title": "Any Axes Are Allowed: A Characteristic-Axis Integral Diagnosis of Factor Models",
    "url": "https://arxiv.org/abs/2607.05091",
    "source": "Useong Shin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T04:00:00+00:00",
    "summary": "arXiv:2607.05091v3 Announce Type: replace Abstract: This paper extends the cap-axis integral diagnostic to general characteristic axes, measuring factor-model pricing errors as bridge-alpha curves. A "
  },
  {
    "id": "rss:https://arxiv.org/abs/2505.23842",
    "domain": "金融",
    "title": "Fair Document Valuation in LLM Summaries via Shapley Values",
    "url": "https://arxiv.org/abs/2505.23842",
    "source": "Zikun Ye, Hema Yoganarasimhan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T04:00:00+00:00",
    "summary": "arXiv:2505.23842v5 Announce Type: replace-cross Abstract: Large Language Models (LLMs) increasingly power search engines and AI assistants that retrieve and summarize content from many sources. By ser"
  },
  {
    "id": "rss:https://arxiv.org/abs/2510.15612",
    "domain": "金融",
    "title": "SoK: Market Microstructure for Decentralized Prediction Markets (DePMs)",
    "url": "https://arxiv.org/abs/2510.15612",
    "source": "Nahid Rahman, Joseph Al-Chami, Jeremy Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T04:00:00+00:00",
    "summary": "arXiv:2510.15612v4 Announce Type: replace-cross Abstract: Decentralized prediction markets (DePMs) allow open participation in event-based wagering without fully relying on centralized intermediaries."
  },
  {
    "id": "hn:48791799",
    "domain": "金融",
    "title": "Is The Economist Always Wrong?",
    "url": "https://economist.com/interactive/finance-and-economics/2026/07/02/is-the-economist-always-wrong",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 58,
    "published_at": "2026-07-05T06:40:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:48653311",
    "domain": "金融",
    "title": "Prairieland defendants sentenced today to prison terms ranging from 30-100 years",
    "url": "https://prairielanddefendants.com/press-release/eight-federal-prairieland-defendants-sentenced-today-to-prison-terms-ranging-from-30-100-years-for-common-protest-activity/",
    "source": "panic",
    "platform": "hackernews",
    "points": 88,
    "published_at": "2026-06-23T23:54:00+00:00",
    "summary": ""
  },
  {
    "id": "hn:48734220",
    "domain": "金融",
    "title": "Supreme Court strikes down limits on party spending in federal elections",
    "url": "https://apnews.com/article/supreme-court-campaign-finance-party-spending-ohio-91e49ee112197ae1210a9abfa46986ed",
    "source": "khriss",
    "platform": "hackernews",
    "points": 67,
    "published_at": "2026-06-30T15:34:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:48756848",
    "domain": "金融",
    "title": "He sent a harsh email to ICE's top official. Federal agents tracked him down",
    "url": "https://www.npr.org/2026/07/01/nx-s1-5874124/dhs-tracks-ice-critic",
    "source": "OutOfHere",
    "platform": "hackernews",
    "points": 66,
    "published_at": "2026-07-02T05:20:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:48678494",
    "domain": "金融",
    "title": "Feds deny Polestar authorization to sell cars in US from model year 2027",
    "url": "https://arstechnica.com/cars/2026/06/feds-deny-polestar-authorization-to-sell-cars-in-us-from-model-year-2027/",
    "source": "Quinner",
    "platform": "hackernews",
    "points": 57,
    "published_at": "2026-06-25T20:00:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:48780128",
    "domain": "金融",
    "title": "AI First: How the Federal Government Is Prioritizing AI over People and Planet",
    "url": "https://stopgreedbuildgreen.climateandcommunity.org/posts/ai-first",
    "source": "eatox",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-07-03T21:21:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:48754128",
    "domain": "金融",
    "title": "US feds are actively hiring \"person who decides which models to ban\"",
    "url": "https://www.usajobs.gov/job/856265200",
    "source": "arm32",
    "platform": "hackernews",
    "points": 47,
    "published_at": "2026-07-01T22:45:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:48483445",
    "domain": "金融",
    "title": "US President says 'I love the inflation'",
    "url": "https://www.cnbc.com/2026/06/10/trump-inflation-cpi-iran-oil.html",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 66,
    "published_at": "2026-06-10T22:12:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:48609233",
    "domain": "金融",
    "title": "Big Tech is borrowing like never before",
    "url": "https://startupfortune.com/big-tech-is-borrowing-like-never-before-and-the-fed-just-made-that-a-lot-more-expensive/",
    "source": "krupan",
    "platform": "hackernews",
    "points": 64,
    "published_at": "2026-06-20T13:49:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:48796110",
    "domain": "金融",
    "title": "Moving back home used to be a sign of failure. Now it shows financial savvy",
    "url": "https://www.wsj.com/lifestyle/relationships/living-with-parents-finances-0c35530c",
    "source": "apparent",
    "platform": "hackernews",
    "points": 23,
    "published_at": "2026-07-05T17:34:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48723371",
    "domain": "金融",
    "title": "Feds Tracked Down an Anti-ICE Dad in NYC Hotel, but How?",
    "url": "https://gizmodo.com/federal-agents-reportedly-tracked-down-an-anti-ice-dad-in-a-new-york-hotel-its-not-clear-how-2000778714",
    "source": "ripe",
    "platform": "hackernews",
    "points": 42,
    "published_at": "2026-06-29T18:42:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:48779065",
    "domain": "金融",
    "title": "Tesla Robotaxi Launches in Miami",
    "url": "https://twitter.com/robotaxi/status/2073030246161367153",
    "source": "spikels",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-07-03T19:38:17+00:00",
    "summary": ""
  }
]
```
