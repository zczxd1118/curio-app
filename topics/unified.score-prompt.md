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

- 今日日期：`2026-07-24`
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
  "date": "2026-07-24",
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
    "points": 1591126,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1j9MP6wEV9",
    "domain": "AI",
    "title": "从零开始，学会让桌面Agent帮你干活！【小白教程】",
    "url": "http://www.bilibili.com/video/av116861865887789",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 1269485,
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
    "points": 993682,
    "published_at": "2026-05-11T09:02:15+00:00",
    "summary": "文档链接：https://lcnaoyjp4e3z.feishu.cn/wiki/MtJlwX0B5iy6y9k5GZTcdjSknTd"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 947267,
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
    "points": 943413,
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
    "points": 942287,
    "published_at": "2025-01-07T10:01:48+00:00",
    "summary": "普通人也可以看的 AI 编程指南\n全网最详细的 Cursor 教程\nCursor 核心功能、使用技巧和思路\n如何免费白嫖 Cursor"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 559473,
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
    "points": 519581,
    "published_at": "2026-05-31T09:46:57+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 426749,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 359556,
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
    "points": 300857,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 246642,
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
    "points": 201098,
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
    "points": 177731,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 172657,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV16NvCBrEVs",
    "domain": "AI",
    "title": "什么是Vibe Coding，以及怎么使用？",
    "url": "http://www.bilibili.com/video/av115797133368973",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 162360,
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
    "points": 160183,
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
    "points": 148963,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1ExV36wEsE",
    "domain": "AI",
    "title": "VS Code 安装 Claude Code 并接入 DeepSeek！Claude Code for VS Code！VSCode使用ClaudeCode插件",
    "url": "http://www.bilibili.com/video/av116662871268177",
    "source": "FutureAI实验室",
    "platform": "bilibili",
    "points": 146546,
    "published_at": "2026-05-30T09:44:52+00:00",
    "summary": "本节视频编号71，评论区自助领取配套文档，记得一键三连哦！"
  },
  {
    "id": "bvid:BV1g49KBqE1g",
    "domain": "AI",
    "title": "【Java+大模型】Java AI Agent✚Spring AI✚Spring AI Alibaba Agent Framework整体结构✚Skill！",
    "url": "http://www.bilibili.com/video/av116339758860081",
    "source": "图灵官方",
    "platform": "bilibili",
    "points": 115355,
    "published_at": "2026-04-03T08:15:24+00:00",
    "summary": "整理制作不易，大家记得点个关注，一键三连呀【点赞、收藏、转发】感谢支持~\n配套大模型笔记/AI大模型学习大纲/面试真题自取：https://www.bilibili.com/read/cv39638062/?spm_id_from=333.1387.0.0&amp;jump_opus=1"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 106733,
    "published_at": "2026-04-27T08:51:41+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n   喜欢视频课程的同学一键三连多多支持一下，长按点赞五秒=lv6大佬 可以的发送彩色弹幕哦。\n配套源码项目已打包评论区回复up"
  },
  {
    "id": "bvid:BV14V3xzfE2t",
    "domain": "AI",
    "title": "【胎教版】AI写小说拆解流程，45分钟干货量大管饱！",
    "url": "http://www.bilibili.com/video/av114782548005846",
    "source": "非凡写作官方",
    "platform": "bilibili",
    "points": 106279,
    "published_at": "2025-07-02T07:56:42+00:00",
    "summary": "45分钟史诗干货！AI写小说完整流程【保姆级教程】\n第一步 扫榜、第二步 制作对标书大纲、第三步 制作细纲、第四步 生成正文，全给你说明白！\n非凡写作，体验地址：https://www.feifan.space/"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 103381,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1gtKx6rEHr",
    "domain": "AI",
    "title": "Claude Code超强平替来了！彻底告别封号！",
    "url": "http://www.bilibili.com/video/av116954828374073",
    "source": "我是阿众",
    "platform": "bilibili",
    "points": 93537,
    "published_at": "2026-07-21T10:09:52+00:00",
    "summary": "不可否认 Claude Code确实很强\n但国内小伙伴想要安稳用上它  \n真的太折腾了\n首先你得会用魔法  \n然后 你还得想尽各种办法折腾海外订阅\n最狠的是\n不知道哪天你的账号可能就被封了\nAI工具本来就是为我们服务的\n可现在却成了每天提心吊胆伺候的大爷\n其实咱们真没必要非得死磕\n国内也有一个非常强的 Claude Code 平替工具\n那就是 Qoder CLI  \n今天咱们就不吹不黑  \n直接上"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 92721,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1GRKJ6fEgn",
    "domain": "AI",
    "title": "Kimi K3编程能力炸裂！在Claude Code中全方位实测代码能力，能否超越Fable 5和GPT-5.6l？结果远超我的预期！国产模型跻身世界第一梯队！",
    "url": "http://www.bilibili.com/video/av116934511239163",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 81756,
    "published_at": "2026-07-17T09:10:43+00:00",
    "summary": "视频简介：\n\n月之暗面最新发布的 Kimi K3，拥有2.8万亿参数和100万 Token 上下文窗口，它的真实编程能力究竟怎么样？\n\n本期视频将对 Kimi K3 进行一次完整的高难度编程实测。我们先在官方网页版测试 SVG 手绘灯泡、复杂过河动画、南宋古都轻功游戏和土星自行车比赛，再将 Kimi K3 接入 Claude Code，开发原生 macOS 音乐播放器、侏罗纪坦克射击游戏以及 iO"
  },
  {
    "id": "bvid:BV1A24y1J7Dt",
    "domain": "AI",
    "title": "如何在VS Code中使用Cursor自动生成代码",
    "url": "http://www.bilibili.com/video/av781409810",
    "source": "许你再少年",
    "platform": "bilibili",
    "points": 73874,
    "published_at": "2023-03-23T11:32:23+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 53287,
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
    "points": 43842,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 38948,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1W2Ts6YEXW",
    "domain": "AI",
    "title": "AI大模型+网络安全零基础入门全套教程：从Agent选型到AI挖洞全流程！AI挖洞提示词|AI解CTF题|AI审计代码|SRC挖洞|CS渗透|kali-码士集团",
    "url": "http://www.bilibili.com/video/av116854601286698",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 35675,
    "published_at": "2026-07-03T06:28:48+00:00",
    "summary": "迈入AI赋能的网络安全新时代！\n\n本课程带你打通大模型与安全实战的底层逻辑。从大模型演进到安全智能体（Agent）构建，硬核实战拉满！手把手教你利用大模型API自动化搞定信息收集、黑盒挖洞、代码审计、解CTF题目及报告编写。深度破解AI挖洞的高效提示词秘籍，攻克复杂场景下的Agent架构与成本选型。\n\n2026安全防线全面升级，带你用AI武装自己，成为驾驭大模型的稀缺AI安全专家！"
  },
  {
    "id": "bvid:BV1HaN162EPT",
    "domain": "AI",
    "title": "【Codex】2026最新Codex保姆级教程，ChatGPT + Codex 开发实战全流程，环境配置、核心功能、使用技巧到项目实战一学就会，少走99%弯路！",
    "url": "http://www.bilibili.com/video/av116911660665280",
    "source": "今天AI了吗",
    "platform": "bilibili",
    "points": 33998,
    "published_at": "2026-07-13T09:01:50+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 33899,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1AGRtBnE3S",
    "domain": "AI",
    "title": "别手动写测试用例了!2026最新Claude Code+Skills实现需求文档生成全量用例|全流程AI驱动软件测试落地方案,测试效率翻10倍！",
    "url": "http://www.bilibili.com/video/av116528787756865",
    "source": "清风说测试开发",
    "platform": "bilibili",
    "points": 30362,
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
    "points": 30076,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV1JU7E6PEar",
    "domain": "AI",
    "title": "Cursor 已死？我为什么要退订 Cursor ？",
    "url": "http://www.bilibili.com/video/av116819553683121",
    "source": "祥子在学AI",
    "platform": "bilibili",
    "points": 29979,
    "published_at": "2026-06-27T01:52:00+00:00",
    "summary": "当了一年多的 Cursor 重度用户，最近把它退订了。\n\n不是它变差了，是 Claude Code 和 Codex 真的太好用了。\n\n几个真实感受： ① 大模型越来越强，我已经不怎么手写代码了 ② Cursor 套的是 VS Code 壳子，只属于程序员 ③ 底层模型不在一个量级——Claude 有 Opus 和 Fable 5，Codex 有 GPT 5.5/5.6，Cursor 的 Compo"
  },
  {
    "id": "bvid:BV1g6fdYcEes",
    "domain": "AI",
    "title": "Cursor从小白到专家-第19课：如何用Cursor开发安卓APP？",
    "url": "http://www.bilibili.com/video/av113888322524233",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 28813,
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
    "points": 25600,
    "published_at": "2026-04-03T16:14:43+00:00",
    "summary": "每个参数都是干什么的，如何修改提示词的教程。\n不知道这是什么？请看合集内的视频~\n我做了一个 AI 的杀戮尖塔2MOD！\n可以和怪物对话，策反怪物，带着怪物爬塔（重写了几乎每一个怪物在友方时候的行为），还能给怪物打防御，带个沙虫全吃了！\n可以和上古之民对话，聊嗨了会给你 1～2 个额外赐福，还能帮你指示为未来\n可以让偷窃草蜢偷队友的 key 卡，想无限？偷了！\n可以和商人讨价还价，甚至白嫖\n多人的"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22643,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV14erKYuEaE",
    "domain": "AI",
    "title": "最强编程AI Cursor+Unity制作一个史诗游戏(详细)",
    "url": "http://www.bilibili.com/video/av113774908413987",
    "source": "多西杰克",
    "platform": "bilibili",
    "points": 17618,
    "published_at": "2025-01-05T09:01:00+00:00",
    "summary": "网上惊呼Cursor AI厉害的内容很多，但结合Unity做游戏的不多，我就来实测一下，做一个AAA大作......"
  },
  {
    "id": "bvid:BV1C3jt64EPS",
    "domain": "AI",
    "title": "B站讲的最好的Vibe Coding企业级项目实战教程（2026最新版）从入门到进阶，七天速通Claude Code+Codex+CursorAI工程化编程开发",
    "url": "http://www.bilibili.com/video/av116787425383675",
    "source": "图灵学院诸葛",
    "platform": "bilibili",
    "points": 17119,
    "published_at": "2026-06-21T09:48:04+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n 【本视频笔记代码、大模型最新学习路线、系统学习课程、实战案例、电子书+问题解答等戳这里获取→https://www.bilibili.com/read/cv39576966/?jump_opus=1】"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 16126,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1spTy6DEb4",
    "domain": "AI",
    "title": "Claude code接管科研全流程：cc-kaiti 带你从 0 走到开题报告和答辩 PPT",
    "url": "http://www.bilibili.com/video/av116866278233889",
    "source": "做科研的大师兄",
    "platform": "bilibili",
    "points": 15860,
    "published_at": "2026-07-05T07:53:28+00:00",
    "summary": "十二年科研经验加持的课题开题Skill，从零开始到拿到一份完整的开题报告及开题PPT，仅需一天！\n\n本次视频分享的cc-kaiti这个skill文件及配套的资料包，在后台私我“cc开题”获取~"
  },
  {
    "id": "bvid:BV1iDRQBrEF6",
    "domain": "AI",
    "title": "Claude + Blender 现在太强了 —— 完整免费设置",
    "url": "http://www.bilibili.com/video/av116543333601720",
    "source": "设计之道",
    "platform": "bilibili",
    "points": 15575,
    "published_at": "2026-05-09T07:11:36+00:00",
    "summary": "【简介】\nAnthropic 刚刚发布了用于创意工具的官方 Claude Connectors —— 其中 Blender 连接器对 3D 艺术家来说最重要。在本视频中，我将展示最佳的 Claude + Blender 免费设置，以及为什么这次更新可能会改变我们构建 3D 场景的方式。\n\n【你将学到】\n01:13 步骤 1：安装 Blender MCP 和 Claude Code\n02:31 步骤"
  },
  {
    "id": "bvid:BV16ggC6DEZK",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116963049212769",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 11427,
    "published_at": "2026-07-22T10:10:42+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1vLN769EJa",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Vibe Coding】教程！大模型入门到进阶，一套全解决！DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116894866677118",
    "source": "吴恩达的AI课",
    "platform": "bilibili",
    "points": 10721,
    "published_at": "2026-07-10T09:04:48+00:00",
    "summary": "【代码已整理】\n无论你是从零开始开发项目，还是对现有代码进行现代化改造，本课程都能为你提供一套严谨的工作流程，让你按自己的方式构建软件。"
  },
  {
    "id": "bvid:BV1ubK26aEbJ",
    "domain": "AI",
    "title": "【AI】这绝对是2026b站讲的最好的Agent Skill保姆级教程！AI大模型/Multi-Agent/Tool/WorkFlow/Agent/智能体架构",
    "url": "http://www.bilibili.com/video/av116950214778812",
    "source": "大模型饼饼",
    "platform": "bilibili",
    "points": 9896,
    "published_at": "2026-07-20T03:42:16+00:00",
    "summary": "如果视频对你有用的话，一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套资料+问题解答+请看评论区置顶领取哦】"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 9217,
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
    "points": 8737,
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
    "points": 7891,
    "published_at": "2026-06-08T10:17:31+00:00",
    "summary": "手把手教你如何使用最新乐鑫文档知识库，帮你在 Claude / Cursor 等平台解答问题、生成代码、迁移 ESP-IDF 版本、烧录固件。 MCP 服务器现已支持微信扫码一键登录，快来一试！\n\n视频重点内容包括👇：\n\n- 如何将 MCP 服务器添加到 VS Code\n- 让 Copilot 基于乐鑫文档对比旧版和最新版 I2C 驱动\n- 驱动迁移\n- Copilot 编译代码、烧录代码并监控输"
  },
  {
    "id": "hn:48873836",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia, CoreWeave, and Nebius: Inside the Circular Financing of the GPU Boom",
    "url": "https://io-fund.com/ai-stocks/nvidia-coreweave-nebius-circular-financing-gpu-boom",
    "source": "adletbalzhanov",
    "platform": "hackernews",
    "points": 370,
    "published_at": "2026-07-11T17:21:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48903715",
    "domain": "AI 算力 / 半导体",
    "title": "Alternative(s) to run CUDA on non-Nvidia hardware",
    "url": "https://www.hpcwire.com/2026/07/09/spectral-compute-aims-to-set-cuda-free-will-it-succeed/",
    "source": "alok-g",
    "platform": "hackernews",
    "points": 143,
    "published_at": "2026-07-14T08:24:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48971128",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia DGX Spark as a daily driver",
    "url": "https://daniel.lawrence.lu/blog/2026-07-15-dgx-spark-as-daily-driver/",
    "source": "plun9",
    "platform": "hackernews",
    "points": 101,
    "published_at": "2026-07-19T19:44:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:49012431",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia released its first official GeForce driver for Windows on Arm",
    "url": "https://videocardz.com/newz/nvidias-first-geforce-driver-for-windows-on-arm-confirms-rtx-spark-n1x-with-6144-or-5120-cuda-cores",
    "source": "robotnikman",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-07-22T19:49:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:48992221",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC eyes price hikes of up to 25% on chip production services in 2027",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/tsmc-eyes-price-hikes-of-up-to-25-percent-on-chip-production-services-in-2027-report-claims-plans-to-raise-baseline-prices-by-5-percent-to-10-percent-on-advanced-nodes",
    "source": "speckx",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-07-21T13:40:51+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/u-s-starts-genesis-mission-with-5b-for-first-projects/",
    "domain": "AI 算力 / 半导体",
    "title": "U.S. Starts Genesis Mission with $5B for First Projects",
    "url": "https://www.eetimes.com/u-s-starts-genesis-mission-with-5b-for-first-projects/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T23:00:00+00:00",
    "summary": "America drops $5B on AI’s Genesis Mission while China lines up $295B; see why the opening bet may already be too small. The post U.S. Starts Genesis Mission with $5B for First Projects appeared first "
  },
  {
    "id": "rss:https://www.eetimes.com/the-story-behind-fuse-eda-ai-system/",
    "domain": "AI 算力 / 半导体",
    "title": "The Story Behind Fuse EDA AI system",
    "url": "https://www.eetimes.com/the-story-behind-fuse-eda-ai-system/",
    "source": "Siemens EDA",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T19:35:36+00:00",
    "summary": "What does it take to build agentic AI for EDA that users can trust and verify? Listen in on this behind-the-scenes conversation around the development of a groundbreaking new platform. The post The St"
  },
  {
    "id": "rss:https://www.eetimes.com/etched-raises-300m-with-1b-in-pre-orders/",
    "domain": "AI 算力 / 半导体",
    "title": "Etched Raises $300M with $1B in Pre-Orders",
    "url": "https://www.eetimes.com/etched-raises-300m-with-1b-in-pre-orders/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T15:00:00+00:00",
    "summary": "AI chip startup Etched will start shipping its racks this summer. The post Etched Raises $300M with $1B in Pre-Orders appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/dac-2026-users-are-not-waiting-diy-ai-is-now-in-vogue/",
    "domain": "AI 算力 / 半导体",
    "title": "DAC 2026: Users Are Not Waiting; DIY AI Is Now in Vogue",
    "url": "https://www.eetimes.com/dac-2026-users-are-not-waiting-diy-ai-is-now-in-vogue/",
    "source": "Frank Schirrmeister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T07:45:00+00:00",
    "summary": "At DAC 2026, chip giants stop waiting for EDA vendors and build their own AI brains—see who’s seizing control. The post DAC 2026: Users Are Not Waiting; DIY AI Is Now in Vogue appeared first on EE Tim"
  },
  {
    "id": "rss:https://www.eetimes.com/from-rhetoric-to-metrics-raghib-hussain-first-year-as-altera-ceo/",
    "domain": "AI 算力 / 半导体",
    "title": "From Rhetoric to Metrics: Raghib Hussain’s First Year as Altera CEO",
    "url": "https://www.eetimes.com/from-rhetoric-to-metrics-raghib-hussain-first-year-as-altera-ceo/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T22:00:00+00:00",
    "summary": "Altera has taped out six chips in nine months, three ahead of schedule, as new CEO focuses on execution. The post From Rhetoric to Metrics: Raghib Hussain’s First Year as Altera CEO appeared first on "
  },
  {
    "id": "rss:https://www.eetimes.com/ai-in-eda-is-real-its-now-and-its-on-show-at-dac-2026/",
    "domain": "AI 算力 / 半导体",
    "title": "AI in EDA Is Real, It’s Now, and It’s on Show at DAC 2026",
    "url": "https://www.eetimes.com/ai-in-eda-is-real-its-now-and-its-on-show-at-dac-2026/",
    "source": "Frank Schirrmeister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T18:00:00+00:00",
    "summary": "AI in chip design has left the slide deck and hit DAC 2026’s floor—walk the stack and test the hype. The post AI in EDA Is Real, It’s Now, and It’s on Show at DAC 2026 appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/cea-leti-looks-beyond-sram-and-dram-as-ai-reshapes-the-memory-roadmap/",
    "domain": "AI 算力 / 半导体",
    "title": "CEA-Leti Looks Beyond SRAM and DRAM as AI Reshapes the Memory Roadmap",
    "url": "https://www.eetimes.com/cea-leti-looks-beyond-sram-and-dram-as-ai-reshapes-the-memory-roadmap/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T07:53:34+00:00",
    "summary": "CEA-Leti’s François Andrieu describes more embedded, persistent, and low-energy memories that will meet the growing demands of AI. The post CEA-Leti Looks Beyond SRAM and DRAM as AI Reshapes the Memor"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amds-new-x100-chip-lineup-puts-strix-halo-into-robots-apus-for-physical-ai-bring-zen-5-cpu-rdna-3-5-gpu-cores-to-compete-with-intels-panther-lake",
    "domain": "AI 算力 / 半导体",
    "title": "AMD’s new X100 chip lineup puts embedded Ryzen AI 'Strix Halo' chips into robots – APUs for physical AI bring Zen 5 CPU, RDNA 3.5 GPU cores to compete with Intel’s Panther Lake",
    "url": "https://www.tomshardware.com/pc-components/cpus/amds-new-x100-chip-lineup-puts-strix-halo-into-robots-apus-for-physical-ai-bring-zen-5-cpu-rdna-3-5-gpu-cores-to-compete-with-intels-panther-lake",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T18:30:00+00:00",
    "summary": "Countering Intel’s recent moves, AMD is bringing its Strix Halo APUs to the realm of robots, and physical AI. Designed for 24/7 operation and a 10-year embedded lifecycle, X100 will also be offered as"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/amd-takes-the-wraps-off-its-instinct-mi455x-ai-accelerator-cdna-5-and-helios-rack-scale-architecture-combine-to-take-the-fight-to-nvidia-in-the-data-center",
    "domain": "AI 算力 / 半导体",
    "title": "AMD takes the wraps off its Instinct MI455X AI accelerator — CDNA 5 and Helios rack-scale architecture combine to take the fight to Nvidia in the data center",
    "url": "https://www.tomshardware.com/pc-components/gpus/amd-takes-the-wraps-off-its-instinct-mi455x-ai-accelerator-cdna-5-and-helios-rack-scale-architecture-combine-to-take-the-fight-to-nvidia-in-the-data-center",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T18:05:44+00:00",
    "summary": "AMD showed off its MI455X accelerator at its Advancing AI 2026 event, demonstrating its strong competitive performance, large HBM memory capacity, and Helios rack-scale architecture."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/amd-and-cerebras-partner-on-low-latency-high-throughput-ai-inference-epyc-processors-in-helios-rack-scale-infrastructure-paired-with-cerebras-wafer-scale-engine-wse-solutions",
    "domain": "AI 算力 / 半导体",
    "title": "AMD and Cerebras partner on low-latency, high-throughput AI inference — EPYC processors in Helios rack-scale infrastructure paired with Cerebras' Wafer-Scale Engine (WSE) solutions",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/amd-and-cerebras-partner-on-low-latency-high-throughput-ai-inference-epyc-processors-in-helios-rack-scale-infrastructure-paired-with-cerebras-wafer-scale-engine-wse-solutions",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T17:45:00+00:00",
    "summary": "When AMD's Helios meets giant wafers from Cerebras, it is not like when Odysseus meets with the Laestrygonian Giants, they collaborate to build an ultimate data center solution."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-3090-and-rtx-3050-team-up-to-hit-144-fps-at-4k-lossless-scaling-turns-old-ampere-gpus-into-a-gaming-powerhouse",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia RTX 3090 and RTX 3050 team up to hit 144 FPS at 4K — Lossless Scaling turns old Ampere GPUs into a gaming powerhouse",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-3090-and-rtx-3050-team-up-to-hit-144-fps-at-4k-lossless-scaling-turns-old-ampere-gpus-into-a-gaming-powerhouse",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T17:39:03+00:00",
    "summary": "A gaming enthusiast leverages Lossless Scaling to supercharge a gaming PC with a GeForce RTX 3090 and GeForce RTX 3050 to deliver up to 144 FPS at 4K."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/new-semiconductor-firm-breaks-cover-backed-by-usd43-million-in-early-stage-funding-tylsemi-aims-to-deliver-custom-silicon-to-customers-without-breaking-the-bank",
    "domain": "AI 算力 / 半导体",
    "title": "New semiconductor firm breaks cover, backed by $43 million in early-stage funding — TYLsemi aims to deliver custom silicon to customers without breaking the bank",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/new-semiconductor-firm-breaks-cover-backed-by-usd43-million-in-early-stage-funding-tylsemi-aims-to-deliver-custom-silicon-to-customers-without-breaking-the-bank",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T17:34:06+00:00",
    "summary": "TYLsemi is set to offer pre-validated chiplets, along with custom ASIC design services, and build highly custom multi-tile processors at relatively low costs."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amds-256-core-epyc-9996-venice-claims-up-to-a-3-4x-jump-over-intel-xeon-competition-20-percent-over-nvidia-vera-zen-6-comes-with-up-to-1024mb-of-l3-16-channel-memory-and-5ghz-clock-speeds",
    "domain": "AI 算力 / 半导体",
    "title": "AMD’s 256-core Epyc 9996 ‘Venice’ claims up to a 3.4x jump over Intel Xeon competition, 20% over Nvidia Vera – Zen 6 comes with up to 1024MB of L3, 16-channel memory, and 5GHz+ clock speeds",
    "url": "https://www.tomshardware.com/pc-components/cpus/amds-256-core-epyc-9996-venice-claims-up-to-a-3-4x-jump-over-intel-xeon-competition-20-percent-over-nvidia-vera-zen-6-comes-with-up-to-1024mb-of-l3-16-channel-memory-and-5ghz-clock-speeds",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T17:24:50+00:00",
    "summary": "After over a year of teases, AMD has finally provided details on its 256-core Venice CPU with the Zen 6 architecture, now known as the Epyc 9996."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amds-venice-x-cpu-launches-in-2027-with-1152-mb-of-3d-v-cache-96-cores-and-5-15-ghz-boost-clock-zen-6-cpu-for-high-performance-computing-comes-with-major-pillars-of-venice",
    "domain": "AI 算力 / 半导体",
    "title": "AMD’s Venice-X CPU launches in 2027 with 1152 MB of 3D V-Cache, 96 cores, and 5.15 GHz boost clock – Zen 6 CPU for high-performance computing comes with major pillars of Venice",
    "url": "https://www.tomshardware.com/pc-components/cpus/amds-venice-x-cpu-launches-in-2027-with-1152-mb-of-3d-v-cache-96-cores-and-5-15-ghz-boost-clock-zen-6-cpu-for-high-performance-computing-comes-with-major-pillars-of-venice",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T17:17:54+00:00",
    "summary": "AMD is returning to 3D V-Cache in its data center range of CPUs with Venice-X, which it has confirmed will launch in the second half of 2027, with 1152 MB of L3 and clock speeds up to 5.15 GHz."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/geekbench-7-introduces-biggest-overhaul-yet-real-world-cpu-testing-new-media-workloads-ai-benchmarks-and-cuda-support",
    "domain": "AI 算力 / 半导体",
    "title": "Geekbench 7 introduces biggest overhaul yet — real-world CPU testing, new media workloads, AI benchmarks, and CUDA support",
    "url": "https://www.tomshardware.com/software/geekbench-7-introduces-biggest-overhaul-yet-real-world-cpu-testing-new-media-workloads-ai-benchmarks-and-cuda-support",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T17:00:00+00:00",
    "summary": "The latest update introduces more realistic CPU and GPU workloads, redesigned multi-core testing, AI-focused benchmarks, larger datasets, and CUDA support for Nvidia GPUs."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/ai-memory-shortage-is-now-increasing-the-price-of-cars-gm-warns-of-vast-cost-increases-byd-hikes-driver-assistance-prices-20-percent",
    "domain": "AI 算力 / 半导体",
    "title": "AI memory shortage is now increasing the price of cars — GM warns of vast cost increases, BYD hikes driver assistance prices 20%",
    "url": "https://www.tomshardware.com/pc-components/ram/ai-memory-shortage-is-now-increasing-the-price-of-cars-gm-warns-of-vast-cost-increases-byd-hikes-driver-assistance-prices-20-percent",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T15:57:19+00:00",
    "summary": "GM CFO Paul Jacobson says that the company's costs are expected to increase by $1.5 to $2 billion, primarily due to increasing memory chip costs. The move comes as the RAM shortage is affecting the au"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/bipartisan-bill-would-require-kill-switches-on-the-most-powerful-ai-models",
    "domain": "AI 算力 / 半导体",
    "title": "Kill switches for most powerful AI models proposed by Bipartisan bill — DHS could order throttling or full shutdown, with fines up to $20 million per day",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/bipartisan-bill-would-require-kill-switches-on-the-most-powerful-ai-models",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T15:02:31+00:00",
    "summary": "The bill amends the Homeland Security Act and covers companies earning at least $500 million in annual revenue from a model trained with compute costing more than $100 million."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/inside-optical-and-the-battle-for-scale-how-the-ai-industry-is-racing-to-integrate-photonic-interconnects",
    "domain": "AI 算力 / 半导体",
    "title": "Inside optical and the battle for scale – how the AI industry is racing to integrate photonic interconnects",
    "url": "https://www.tomshardware.com/tech-industry/inside-optical-and-the-battle-for-scale-how-the-ai-industry-is-racing-to-integrate-photonic-interconnects",
    "source": "Chris Stokel-Walker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T14:22:54+00:00",
    "summary": "With the limitations of copper looming, the industry is transitioning to photonic interconnects to scale data center capabilities. We spoke to experts such as Lightmatter chief executive Nick Harris a"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-and-amd-sign-long-term-server-cpu-deals-with-chinese-customers-as-prices-jump-over-40-percent",
    "domain": "AI 算力 / 半导体",
    "title": "Intel and AMD sign long-term server CPU deals with Chinese customers as prices jump over 40%, report claims — agreements purportedly guarantee purchase volumes for about a year without fixing prices",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-and-amd-sign-long-term-server-cpu-deals-with-chinese-customers-as-prices-jump-over-40-percent",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T13:49:39+00:00",
    "summary": "Some customers have discussed commitments running two years or longer, one source told Reuters."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/mini-pcs/arctic-senza-ai-370-fanless-mini-pc-review",
    "domain": "AI 算力 / 半导体",
    "title": "Arctic Senza AI 370 review: Strix Point in a stealthy under-desk fanless design",
    "url": "https://www.tomshardware.com/desktops/mini-pcs/arctic-senza-ai-370-fanless-mini-pc-review",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T13:00:54+00:00",
    "summary": "The Arctic Senza AI 370 is a fanless mini PC designed to mount under your desk. Everyday performance isn’t held back by the lack of active cooling, and its soldered dual-channel 32GB LPDDR5X-8000 is a"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-10-percent-on-the-brand-new-creality-pika-3d-scanner-easily-scan-models-and-textures-for-usd629",
    "domain": "AI 算力 / 半导体",
    "title": "Save 10% on the brand-new Creality Pika 3D scanner — easily scan models and textures for $629",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-10-percent-on-the-brand-new-creality-pika-3d-scanner-easily-scan-models-and-textures-for-usd629",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T11:55:18+00:00",
    "summary": "Pre-purchase Creality's portable Pika 3D scanner at a discount. First come, first served: a 10% saving if you act within 19 days."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/policy/142-ai-data-center-protests-staged-in-42-states-as-public-opposition-increases-organizers-brand-unaccountable-buildouts-as-an-unacceptable-infringement-on-our-liberty",
    "domain": "AI 算力 / 半导体",
    "title": "142 AI data center protests staged in 42 states as public opposition increases — organizers brand 'unaccountable' buildouts as an 'unacceptable infringement on our liberty'",
    "url": "https://www.tomshardware.com/tech-industry/policy/142-ai-data-center-protests-staged-in-42-states-as-public-opposition-increases-organizers-brand-unaccountable-buildouts-as-an-unacceptable-infringement-on-our-liberty",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T11:41:41+00:00",
    "summary": "Data center projects are facing increasing opposition from surrounding communities, making consent even far scarcer than the chips and power needed to run these facilities. Any developer planning to c"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/this-astonishing-usd850-gaming-pc-contains-well-over-usd1-200-worth-of-parts-including-usd400-of-32gb-ddr5-alone-get-a-potent-steam-machine-rival-thanks-to-this-budget-intel-arc-desktop",
    "domain": "AI 算力 / 半导体",
    "title": "This astonishing $850 gaming PC contains well over $1,200 worth of parts, including $400 of 32GB DDR5 alone — get a potent Steam Machine rival thanks to this budget Intel Arc desktop",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/this-astonishing-usd850-gaming-pc-contains-well-over-usd1-200-worth-of-parts-including-usd400-of-32gb-ddr5-alone-get-a-potent-steam-machine-rival-thanks-to-this-budget-intel-arc-desktop",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T10:31:08+00:00",
    "summary": "Save $150 on this gaming PC with Intel Core i5 14400F, Intel Arc B580, and 32GB of DDR5 RAM."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/oregon-will-start-charging-service-providers-for-undersea-cables-using-its-sea-floor-millions-accrued-over-years-will-go-toward-state-schools",
    "domain": "AI 算力 / 半导体",
    "title": "Oregon will start charging service providers for undersea cables using its sea floor — millions accrued over years will go toward state schools",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/oregon-will-start-charging-service-providers-for-undersea-cables-using-its-sea-floor-millions-accrued-over-years-will-go-toward-state-schools",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T10:20:00+00:00",
    "summary": "Oregon set to start charging service providers for undersea cables using its sea floor. It will funnel the millions accrued toward state schools."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/ambitious-modder-creates-grand-theft-auto-multiverse-with-real-time-portals-san-andreas-vice-city-and-gta-iii-all-run-simultaneously-with-cross-game-interactions",
    "domain": "AI 算力 / 半导体",
    "title": "Grand Theft Auto Multiverse with real-time portals created by ambitious modder — San Andreas, Vice City and GTA III all run simultaneously, with cross-game interactions",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/ambitious-modder-creates-grand-theft-auto-multiverse-with-real-time-portals-san-andreas-vice-city-and-gta-iii-all-run-simultaneously-with-cross-game-interactions",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T10:00:00+00:00",
    "summary": "A modder by the name of Dryxio has built perhaps the most impressive mod in the history of Grand Theft Auto by combining three different GTA games into one, connected through real-time, fully function"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/framework-nearly-doubles-memory-pricing-for-32gb-64gb-laptop-13-pro-overnight-ceo-says-absorbing-lpcamm2-supplier-hikes-would-put-our-ability-to-operate-at-real-financial-risk",
    "domain": "AI 算力 / 半导体",
    "title": "Framework nearly doubles memory pricing for 32GB, 64GB Laptop 13 Pro overnight — CEO says absorbing LPCAMM2 supplier hikes would put 'our ability to operate at real financial risk'",
    "url": "https://www.tomshardware.com/laptops/framework-nearly-doubles-memory-pricing-for-32gb-64gb-laptop-13-pro-overnight-ceo-says-absorbing-lpcamm2-supplier-hikes-would-put-our-ability-to-operate-at-real-financial-risk",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T20:50:46+00:00",
    "summary": "The company is making adjustments to some existing pre-orders."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/jensen-huang-argues-american-companies-should-be-allowed-to-use-chinese-ai-models-nvidia-ceo-says-backdoors-connected-to-china-are-misconceptions",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang argues American companies should be allowed to use Chinese AI models — Nvidia CEO says backdoors connected to China are misconceptions",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/jensen-huang-argues-american-companies-should-be-allowed-to-use-chinese-ai-models-nvidia-ceo-says-backdoors-connected-to-china-are-misconceptions",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T17:55:46+00:00",
    "summary": "Nvidia CEO Jensen Huang raised several points against the rising sentiment in Washington that U.S. firms should be prevented from accessing Chinese AI models. He also advocates for open models, which "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/intel-4-gets-its-first-foundry-customer-in-fortinet-three-years-after-intel-scoped-the-node-to-meteor-lake",
    "domain": "AI 算力 / 半导体",
    "title": "Fortinet becomes Intel 4's first foundry customer, following firewall ASIC deal — CEO Lip-Bu Tan's promised foundry wins begin to surface, but on a mature node",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/intel-4-gets-its-first-foundry-customer-in-fortinet-three-years-after-intel-scoped-the-node-to-meteor-lake",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T16:17:41+00:00",
    "summary": "Intel will design, package, and fabricate Fortinet's sixth-generation Security Processor (SP6) on its Intel 4 node."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/microsoft-announces-xbox-backward-compatibility-for-pc-will-let-gamers-play-classic-console-games-on-pcs-and-handhelds",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft announces Xbox Backward Compatibility for PC — will let gamers play classic console games on PCs and handhelds",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/microsoft-announces-xbox-backward-compatibility-for-pc-will-let-gamers-play-classic-console-games-on-pcs-and-handhelds",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T16:09:52+00:00",
    "summary": "Xbox Backward Compatibility on PC will let gamers play classic Xbox games on PC and handheld."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/usb/usbs-next-decade",
    "domain": "AI 算力 / 半导体",
    "title": "The future of USB connectivity (2026) — How USB4 Version 2 and Thunderbolt 5 are bringing copper to its physical limits",
    "url": "https://www.tomshardware.com/peripherals/usb/usbs-next-decade",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T15:40:28+00:00",
    "summary": "The USB ecosystem is entering another transition that will affect how laptops, desktops, storage devices, displays, and peripherals connect in the second half of the decade."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/amd-to-supply-anthropic-with-2-gigawatts-of-instinct-mi450-gpus",
    "domain": "AI 算力 / 半导体",
    "title": "AMD to supply Anthropic with 2 gigawatts of Instinct MI450 GPUs — will invest up to $5 billion in the Claude developer, which is already using MI355X GPUs",
    "url": "https://www.tomshardware.com/tech-industry/amd-to-supply-anthropic-with-2-gigawatts-of-instinct-mi450-gpus",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T15:38:58+00:00",
    "summary": "The first gigawatt is scheduled to come online in the first half of 2027 in AMD Helios rack-scale systems."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/bnef-nearly-doubles-its-us-data-center-power-forecast-to-194gw",
    "domain": "AI 算力 / 半导体",
    "title": "Data centers forecast to use 20% of US power by 2035 — analysts estimate usage will rocket to 194 gigawatts, 83% more than forecast seven months ago",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/bnef-nearly-doubles-its-us-data-center-power-forecast-to-194gw",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T14:21:58+00:00",
    "summary": "BNEF's December outlook put 2035 demand at 106 GW, and that figure was itself 36% above the projection the firm published in April 2025."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/apple-reportedly-working-on-mac-leasing-program-in-partnership-with-klarna-to-fight-ram-price-increases-apple-upgrade-would-let-users-finance-hardware-over-36-months-budget-models-excluded",
    "domain": "AI 算力 / 半导体",
    "title": "Apple reportedly working on Mac leasing program in partnership with Klarna to fight RAM price increases — 'Apple Upgrade' would let users finance hardware over 36 months, budget models excluded",
    "url": "https://www.tomshardware.com/tech-industry/apple-reportedly-working-on-mac-leasing-program-in-partnership-with-klarna-to-fight-ram-price-increases-apple-upgrade-would-let-users-finance-hardware-over-36-months-budget-models-excluded",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T13:34:36+00:00",
    "summary": "A new Bloomberg report is claiming that Apple is working on a leasing program called \"Apple Upgrade\" that will allow customers to finance hardware over the course of 2 or 3 years. At the end of the te"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/ai-tech-companies-have-hidden-debt-worth-around-usd1-65-trillion-report-claims-amount-is-122-percent-of-debt-reflected-on-the-balance-sheets-of-alphabet-amazon-meta-microsoft-and-oracle",
    "domain": "AI 算力 / 半导体",
    "title": "AI tech companies have ‘hidden debt’ worth around $1.65 trillion, report claims — amount is 122% of debt reflected on the balance sheets of Alphabet, Amazon, Meta, Microsoft, and Oracle",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/ai-tech-companies-have-hidden-debt-worth-around-usd1-65-trillion-report-claims-amount-is-122-percent-of-debt-reflected-on-the-balance-sheets-of-alphabet-amazon-meta-microsoft-and-oracle",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T13:23:33+00:00",
    "summary": "Five tech giants have $1.65 trillion in data center obligations that are listed off their balance sheets. These liabilities are added as footnotes in their quarterly statements but will become due and"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpu-drivers/chinese-modder-gets-geforce-rtx-4060-working-in-windows-11-on-huawei-arm-workstation-uses-modified-driver-borrowed-from-an-nvidia-rtx-spark",
    "domain": "AI 算力 / 半导体",
    "title": "Chinese modder gets GeForce RTX 4060 working in Windows 11 on Huawei Arm workstation — uses modified driver borrowed from an Nvidia RTX Spark",
    "url": "https://www.tomshardware.com/pc-components/gpu-drivers/chinese-modder-gets-geforce-rtx-4060-working-in-windows-11-on-huawei-arm-workstation-uses-modified-driver-borrowed-from-an-nvidia-rtx-spark",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T13:18:38+00:00",
    "summary": "Borrowing a driver from the upcoming RTX Spark, VoidTech managed to get x86 Windows games running on a Huawei Arm workstation."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/meta-to-use-custom-amd-instinct-mi400-accelerators-with-144gb-of-hbm4-for-select-workloads-report-claims-could-dramatically-reduce-cost-at-the-expense-of-versatility",
    "domain": "AI 算力 / 半导体",
    "title": "Meta to use custom AMD Instinct MI400 accelerators with 144GB of HBM4 for select workloads, report claims — could dramatically reduce cost at the expense of versatility",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/meta-to-use-custom-amd-instinct-mi400-accelerators-with-144gb-of-hbm4-for-select-workloads-report-claims-could-dramatically-reduce-cost-at-the-expense-of-versatility",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T11:36:15+00:00",
    "summary": "Meta will reportedly use a custom version of AMD's Instinct MI400-series accelerators with a memory system cut to 144GB of HBM4, allegedly for select workloads only."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/this-usd1-399-5070-gaming-laptop-is-one-of-the-best-value-deals-around-save-usd700-on-16-inch-model-with-32gb-of-ram-and-a-1tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Woot has slashed $600 off this RTX 5070 gaming laptop — get a Gigabyte Aero X16 with 32GB of RAM and Ryzen HX 370 for just $1,399",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/this-usd1-399-5070-gaming-laptop-is-one-of-the-best-value-deals-around-save-usd700-on-16-inch-model-with-32gb-of-ram-and-a-1tb-ssd",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T11:06:29+00:00",
    "summary": "Get a Gigabyte Aero X16 with RTX 5070, 32GB of RAM, 1TB SSD, and AMD Ryzen AI 9 HX 370 for $1,399."
  },
  {
    "id": "rss:https://www.eetimes.com/sk-hynix-nasdaq-debut-shows-global-memory-expansion-race/",
    "domain": "AI 算力 / 半导体",
    "title": "SK Hynix Nasdaq Debut Shows Global Memory Expansion Race",
    "url": "https://www.eetimes.com/sk-hynix-nasdaq-debut-shows-global-memory-expansion-race/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T20:10:00+00:00",
    "summary": "SK Hynix Nasdaq debut highlights capex-funded memory expansion. Both Samsung and Micron follow suit. The post SK Hynix Nasdaq Debut Shows Global Memory Expansion Race appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/how-quantum-computing-earns-its-place-in-the-data-center/",
    "domain": "AI 算力 / 半导体",
    "title": "How Quantum Computing Earns Its Place in the Data Center",
    "url": "https://www.eetimes.com/how-quantum-computing-earns-its-place-in-the-data-center/",
    "source": "Zeynep Korutürk, Kris Naudts, Donald Harmitt",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T13:08:25+00:00",
    "summary": "Quantum won’t win in labs; it must survive racks, cooling, power and networks. The post How Quantum Computing Earns Its Place in the Data Center appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/carbon-nanotube-firm-strengthens-executive-team-to-build-cnt-ecosystem/",
    "domain": "AI 算力 / 半导体",
    "title": "Carbon Nanotube Firm Strengthens Executive Team to Build CNT Ecosystem",
    "url": "https://www.eetimes.com/carbon-nanotube-firm-strengthens-executive-team-to-build-cnt-ecosystem/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T07:00:00+00:00",
    "summary": "Canatu stacks its C-suite to push CNTs into chips, cars, and diagnostics—watch how its new CEO plans to turn nanotube hype into yield. The post Carbon Nanotube Firm Strengthens Executive Team to Build"
  },
  {
    "id": "hn:48894277",
    "domain": "AI 算力 / 半导体",
    "title": "Apple's rumored M7 Ultra targets 1.5TB and Blackwell-class AI performance",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/apples-rumored-m7-ultra-targets-1-5tb-of-memory-and-blackwell-class-ai",
    "source": "rbanffy",
    "platform": "hackernews",
    "points": 26,
    "published_at": "2026-07-13T15:32:19+00:00",
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
    "id": "hn:48936451",
    "domain": "大厂 AI 动态",
    "title": "NotebookLM is now Gemini Notebook",
    "url": "https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/",
    "source": "xnx",
    "platform": "hackernews",
    "points": 371,
    "published_at": "2026-07-16T16:08:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:48925271",
    "domain": "大厂 AI 动态",
    "title": "Why I Left Google DeepMind",
    "url": "https://turntrout.com/why-i-left-google-deepmind",
    "source": "apsec112",
    "platform": "hackernews",
    "points": 368,
    "published_at": "2026-07-15T18:40:34+00:00",
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
    "id": "hn:48998606",
    "domain": "大厂 AI 动态",
    "title": "Gemini last models: temperature, top_p, and top_k are deprecated and ignored",
    "url": "https://ai.google.dev/gemini-api/docs/latest-model",
    "source": "greatgib",
    "platform": "hackernews",
    "points": 132,
    "published_at": "2026-07-21T21:27:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:48965880",
    "domain": "大厂 AI 动态",
    "title": "Ollama: All Aboard Open Models",
    "url": "https://ollama.com/blog/all-aboard-open-models",
    "source": "inferhaven",
    "platform": "hackernews",
    "points": 137,
    "published_at": "2026-07-19T07:59:44+00:00",
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
    "id": "hn:48864507",
    "domain": "大厂 AI 动态",
    "title": "Please don't discontinue Gemini 2.5 Flash",
    "url": "https://discuss.ai.google.dev/t/please-dont-discontinue-gemini-2-5-flash/174246",
    "source": "NickDob",
    "platform": "hackernews",
    "points": 135,
    "published_at": "2026-07-10T20:00:28+00:00",
    "summary": ""
  },
  {
    "id": "hn:48993130",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.6 Flash",
    "url": "https://console.cloud.google.com/agent-platform/publishers/google/model-garden/gemini-3.6-flash",
    "source": "marrf",
    "platform": "hackernews",
    "points": 74,
    "published_at": "2026-07-21T14:56:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:48959297",
    "domain": "大厂 AI 动态",
    "title": "Our Approach to Bioresilience: Isomorphic Labs and Google DeepMind",
    "url": "https://deepmind.google/blog/our-approach-to-bioresilience/",
    "source": "bookofjoe",
    "platform": "hackernews",
    "points": 83,
    "published_at": "2026-07-18T16:02:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:48983890",
    "domain": "大厂 AI 动态",
    "title": "Cue AI",
    "url": "https://deepmind.google/models/gemma/gemmaverse/cue-ai/",
    "source": "logickkk1",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-07-20T19:41:44+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/tech/970399/amazon-alexa-plus-ai-update-smart-home-devices",
    "domain": "大厂 AI 动态",
    "title": "Alexa Plus is getting an AI update to handle more complicated instructions",
    "url": "https://www.theverge.com/tech/970399/amazon-alexa-plus-ai-update-smart-home-devices",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T21:15:06+00:00",
    "summary": "Amazon is launching an update to its Alexa Plus assistant that will allow it to connect to smart home devices in new ways. With the update, which is currently in preview, Alexa Plus can link up with t"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/970254/amazon-echo-show-21-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "The Echo Show 21 is a great smart home hub that’s $80 off",
    "url": "https://www.theverge.com/gadgets/970254/amazon-echo-show-21-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T20:36:40+00:00",
    "summary": "Split between buying a smart calendar, a kitchen TV, a smart home hub, and a smart display? Amazon’s Echo Show 21 is all of those things in one, with a huge 21-inch screen. You can use it to control y"
  },
  {
    "id": "rss:https://www.theverge.com/policy/970284/brendan-carr-fcc-chairman-first-amendment",
    "domain": "大厂 AI 动态",
    "title": "FCC Chairman Brendan Carr’s war on the First Amendment",
    "url": "https://www.theverge.com/policy/970284/brendan-carr-fcc-chairman-first-amendment",
    "source": "Kevin Nguyen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T19:46:11+00:00",
    "summary": "As the chairman of the Federal Communications Commission, Brendan Carr has authority over the nation’s TV, radio, and internet. But since Donald Trump was elected to his second term, Carr has wielded "
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/970065/anthropic-voice-mode-claude-opus-sonnet-haiku-ai",
    "domain": "大厂 AI 动态",
    "title": "Claude’s voice mode is now available for Opus and Sonnet",
    "url": "https://www.theverge.com/ai-artificial-intelligence/970065/anthropic-voice-mode-claude-opus-sonnet-haiku-ai",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T19:00:00+00:00",
    "summary": "Until now, voice mode has only been available on Claude Haiku, Anthropic's faster but less powerful model. Now the company is making its Opus and Sonnet models available in voice mode, and extending i"
  },
  {
    "id": "rss:https://www.theverge.com/tech/970211/patreon-layoffs-ai",
    "domain": "大厂 AI 动态",
    "title": "Patreon is laying off 20 percent of workers",
    "url": "https://www.theverge.com/tech/970211/patreon-layoffs-ai",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T18:20:30+00:00",
    "summary": "Patreon is laying off 20 percent of its workers, or around 93 employees, as reported earlier by 404 Media. In a memo to employees, Patreon CEO Jack Conte writes that the company isn't making these cha"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/960331/corsair-frame-4500x-deal-pc-case-sale",
    "domain": "大厂 AI 动态",
    "title": "Corsair’s PC case with a panoramic glass design is $70 off",
    "url": "https://www.theverge.com/gadgets/960331/corsair-frame-4500x-deal-pc-case-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T17:20:00+00:00",
    "summary": "On the hunt for a PC case that’s loaded with features and has a unique look? Amazon, Best Buy, and Corsair are selling the Corsair Frame 4500X RS for $119.99, a $70 discount from the usual price. The "
  },
  {
    "id": "rss:https://www.theverge.com/transportation/970003/tesla-robotaxi-mileage-waymo-cities-earnings-musk",
    "domain": "大厂 AI 动态",
    "title": "Tesla’s robotaxi promises are clashing with reality",
    "url": "https://www.theverge.com/transportation/970003/tesla-robotaxi-mileage-waymo-cities-earnings-musk",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T17:09:31+00:00",
    "summary": "In an earnings call yesterday, Tesla CEO Elon Musk did his best to paint a positive portrait of the company's robotaxi program. New cities are being added, more miles are being driven, and more people"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/970012/primate-labs-geekbench-7-benchmark-test-software-update",
    "domain": "大厂 AI 动态",
    "title": "Geekbench 7 will push your computer or phone even harder for better benchmarking",
    "url": "https://www.theverge.com/gadgets/970012/primate-labs-geekbench-7-benchmark-test-software-update",
    "source": "Antonio G. Di Benedetto",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T17:00:00+00:00",
    "summary": "Primate Labs is releasing Geekbench 7, the latest generation of its popular benchmarking tool. Geekbench 7 features new video and audio encoding / decoding tests, a redesigned multi-core test, and lar"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/970115/openai-chatgpt-health-launch-claims",
    "domain": "大厂 AI 动态",
    "title": "OpenAI is making big claims as it rolls out ChatGPT Health to everyone",
    "url": "https://www.theverge.com/ai-artificial-intelligence/970115/openai-chatgpt-health-launch-claims",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T17:00:00+00:00",
    "summary": "OpenAI is rolling out ChatGPT Health to everyone in the US on Thursday, allowing more people to connect their medical records and health-tracking information to the chatbot. During a briefing, Ashley "
  },
  {
    "id": "rss:https://www.theverge.com/streaming/970099/amazon-prime-video-luna-gaming",
    "domain": "大厂 AI 动态",
    "title": "Amazon puts Luna cloud-streamed games like Fallout 4 inside Prime Video",
    "url": "https://www.theverge.com/streaming/970099/amazon-prime-video-luna-gaming",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T16:39:32+00:00",
    "summary": "The new strategy that Amazon gaming exec Jeff Gattis talked to The Verge about last month is getting clearer now that Prime Video has added a new Games tab on Fire TV devices. With Prime Gaming, Amazo"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/23/how-ai-guardrails-are-impeding-the-work-of-offensive-cybersecurity-researchers/",
    "domain": "大厂 AI 动态",
    "title": "How AI guardrails are impeding the work of offensive cybersecurity researchers",
    "url": "https://techcrunch.com/2026/07/23/how-ai-guardrails-are-impeding-the-work-of-offensive-cybersecurity-researchers/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T01:00:00+00:00",
    "summary": "We spoke with several cybersecurity researchers, who look for unknown vulnerabilities and develop tools to exploit them, about how OpenAI’s and Anthropic’s guardrails affect their work."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/23/meet-the-judges-who-will-crown-australias-next-breakout-startup/",
    "domain": "大厂 AI 动态",
    "title": "Meet the judges who will crown Australia’s next breakout startup",
    "url": "https://techcrunch.com/2026/07/23/meet-the-judges-who-will-crown-australias-next-breakout-startup/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T00:05:00+00:00",
    "summary": "TechCrunch Startup Battlefield is coming to Australia — and we're partnering with Stripe to find the country's most exciting early-stage startups."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/23/mobileye-ceo-amnon-shashua-to-step-aside-as-company-pushes-into-robotaxis-robotics/",
    "domain": "大厂 AI 动态",
    "title": "Mobileye CEO Amnon Shashua to step aside as company pushes into robotaxis, robotics",
    "url": "https://techcrunch.com/2026/07/23/mobileye-ceo-amnon-shashua-to-step-aside-as-company-pushes-into-robotaxis-robotics/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T22:40:08+00:00",
    "summary": "Shashua has been invited to take the chairman of the board seat."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/23/amd-takes-on-nvidia-with-its-helios-ai-rack-scale-system/",
    "domain": "大厂 AI 动态",
    "title": "AMD takes on Nvidia with its Helios AI rack-scale system",
    "url": "https://techcrunch.com/2026/07/23/amd-takes-on-nvidia-with-its-helios-ai-rack-scale-system/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T20:33:02+00:00",
    "summary": "AMD is challenging its chipmaker rival with a new rack-scale system that will start shipping to customers later this year."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/23/patreon-lays-off-off-20-of-its-workforce/",
    "domain": "大厂 AI 动态",
    "title": "Patreon lays off 20% of its workforce",
    "url": "https://techcrunch.com/2026/07/23/patreon-lays-off-off-20-of-its-workforce/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T20:30:07+00:00",
    "summary": "In a memo to staff that was posted online, Conte said the company's core business is strong, but the platform has to respond to market changes and adjust its cost structure to remain stable."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/23/insurance-startup-corgi-reportedly-raised-more-money-at-4b-its-third-round-in-eight-weeks/",
    "domain": "大厂 AI 动态",
    "title": "Insurance startup Corgi reportedly raised more money at $4B — its third round in 8 weeks",
    "url": "https://techcrunch.com/2026/07/23/insurance-startup-corgi-reportedly-raised-more-money-at-4b-its-third-round-in-eight-weeks/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T20:13:24+00:00",
    "summary": "In the AI-funding frenzy, many startups are raising back-to-back rounds at ever-increasing valuations — but even by those standards, Corgi stands out."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/23/teslas-door-handles-may-spur-new-u-s-safety-rules/",
    "domain": "大厂 AI 动态",
    "title": "Tesla’s door handles may spur new US safety rules",
    "url": "https://techcrunch.com/2026/07/23/teslas-door-handles-may-spur-new-u-s-safety-rules/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T20:06:21+00:00",
    "summary": "The new rule-making process follows a series of incidents, including fatal ones, in which people have become stuck inside cars."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/23/meta-drops-out-of-a-major-clean-energy-pact-as-its-natural-gas-buildout-accelerates/",
    "domain": "大厂 AI 动态",
    "title": "Meta drops out of a major clean energy pact as its natural gas buildout accelerates",
    "url": "https://techcrunch.com/2026/07/23/meta-drops-out-of-a-major-clean-energy-pact-as-its-natural-gas-buildout-accelerates/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T19:41:54+00:00",
    "summary": "Meta has made significant investments in natural gas over the past year. Now it's dropping out of an industry renewable energy group."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/23/anthropic-updates-claude-voice-mode-with-more-capable-models/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic updates Claude voice mode with more capable models",
    "url": "https://techcrunch.com/2026/07/23/anthropic-updates-claude-voice-mode-with-more-capable-models/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T19:00:00+00:00",
    "summary": "Claude's new voice model will let you reschedule your meeting or draft an email."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/23/aegisai-founded-by-former-google-security-execs-lands-36m-to-stop-ai-driven-spear-phishing/",
    "domain": "大厂 AI 动态",
    "title": "AegisAI, founded by former Google security execs, lands $36M to stop AI-driven spear phishing",
    "url": "https://techcrunch.com/2026/07/23/aegisai-founded-by-former-google-security-execs-lands-36m-to-stop-ai-driven-spear-phishing/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T18:38:34+00:00",
    "summary": "AegisAI co-founders developed AI agents that quickly analyze each message as a human would, paying attention to small anomalies that even the most elaborate checklist wouldn’t catch."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/23/us-government-says-iran-linked-hackers-are-disrupting-american-water-and-energy-providers/",
    "domain": "大厂 AI 动态",
    "title": "US government says Iran-linked hackers are disrupting American water and energy providers",
    "url": "https://techcrunch.com/2026/07/23/us-government-says-iran-linked-hackers-are-disrupting-american-water-and-energy-providers/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T17:27:08+00:00",
    "summary": "An updated government advisory warns that Iranian hackers are exploiting systems used by water and energy providers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/23/runway-bets-on-ai-model-routing-as-generative-media-gets-crowded/",
    "domain": "大厂 AI 动态",
    "title": "Runway launches AI model router as generative media gets crowded",
    "url": "https://techcrunch.com/2026/07/23/runway-bets-on-ai-model-routing-as-generative-media-gets-crowded/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T17:07:35+00:00",
    "summary": "The Media Router is a tool that automatically selects the best image, video, or audio generation model for a request based on whether a developer prioritizes quality, speed or cost."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/23/openai-makes-chatgpt-health-available-to-all-u-s-users/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI makes ChatGPT Health available to all US users",
    "url": "https://techcrunch.com/2026/07/23/openai-makes-chatgpt-health-available-to-all-u-s-users/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T17:00:00+00:00",
    "summary": "Users can also integrate their personal data from services like Apple Health, Function, and MyFitnessPal."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/23/teslas-robotaxis-are-moving-in-reverse/",
    "domain": "大厂 AI 动态",
    "title": "Tesla’s robotaxis are moving in reverse",
    "url": "https://techcrunch.com/2026/07/23/teslas-robotaxis-are-moving-in-reverse/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T16:29:59+00:00",
    "summary": "The number of paid robotaxi miles traveled fell 36% in the second quarter, despite expanding to new cities, according to Tesla's own figures."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/23/meta-launched-a-new-ai-optimism-ad-set-to-a-song-about-human-extinction/",
    "domain": "大厂 AI 动态",
    "title": "Meta launched a new AI optimism ad set to a song about human extinction",
    "url": "https://techcrunch.com/2026/07/23/meta-launched-a-new-ai-optimism-ad-set-to-a-song-about-human-extinction/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T16:28:50+00:00",
    "summary": "David Bowie's song \"Five Years,\" which Meta used in a supposedly inspiring advertisement, is about humans learning that they have five years left to live before the apocalypse."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/23/google-will-now-let-you-sign-in-to-your-account-with-a-selfie-video/",
    "domain": "大厂 AI 动态",
    "title": "Google will now let you sign in to your account with a selfie video",
    "url": "https://techcrunch.com/2026/07/23/google-will-now-let-you-sign-in-to-your-account-with-a-selfie-video/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T16:01:03+00:00",
    "summary": "The tech giant says selfie videos give users more options to sign in if they're ever locked out or don't have access to their usual phone or computer."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/23/ai-chip-startup-etched-defies-skeptics-hits-10-3b-valuation-from-big-name-investors/",
    "domain": "大厂 AI 动态",
    "title": "AI chip startup Etched defies skeptics, hits $10.3B valuation from big-name investors",
    "url": "https://techcrunch.com/2026/07/23/ai-chip-startup-etched-defies-skeptics-hits-10-3b-valuation-from-big-name-investors/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T15:00:00+00:00",
    "summary": "Etched, founded by three Harvard dropouts, has created new chips and memory components that speed up inference on any AI model -- no GPUs required, it says."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/23/edtech-platform-raises-4-5m-to-help-teach-students-how-to-vibe-code/",
    "domain": "大厂 AI 动态",
    "title": "Edtech platform raises $4.5M to help teach students how to vibe code",
    "url": "https://techcrunch.com/2026/07/23/edtech-platform-raises-4-5m-to-help-teach-students-how-to-vibe-code/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T15:00:00+00:00",
    "summary": "Imagi announced a $4.5 million seed round, with investors including Brighteye Ventures, Day One Capital, and artist Will.i.am."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/23/nvidia-is-sending-gpus-to-the-moon/",
    "domain": "大厂 AI 动态",
    "title": "Nvidia is sending GPUs to the moon",
    "url": "https://techcrunch.com/2026/07/23/nvidia-is-sending-gpus-to-the-moon/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T15:00:00+00:00",
    "summary": "If there's a place in the universe without GPUs, Nvidia is sending them there."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/23/google-closes-in-on-another-billion-user-product-with-gemini/",
    "domain": "大厂 AI 动态",
    "title": "Google’s Gemini nears billion-user milestone",
    "url": "https://techcrunch.com/2026/07/23/google-closes-in-on-another-billion-user-product-with-gemini/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T14:52:44+00:00",
    "summary": "Gemini had over 750 million monthly users in February."
  },
  {
    "id": "rss:https://stratechery.com/2026/openai-hacks-hugging-face-what-happened-alignment-and-paper-clips/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI Hacks Hugging Face, What Happened, Alignment and Paper Clips",
    "url": "https://stratechery.com/2026/openai-hacks-hugging-face-what-happened-alignment-and-paper-clips/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T10:00:00+00:00",
    "summary": "OpenAI accidentally hacked Hugging Face, but the takeaways are more encouraging than people realize."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/07/microsoft-responds-to-lg-monitors-installing-mcafee-ads-on-windows/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft responds to LG monitors installing McAfee ads on Windows",
    "url": "https://arstechnica.com/gadgets/2026/07/microsoft-responds-to-lg-monitors-installing-mcafee-ads-on-windows/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T20:47:33+00:00",
    "summary": "App is installed through Windows Update when certain LG monitors connect to a PC."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/07/fda-reports-new-outbreak-of-explosive-diarrhea-with-72-cases-identified/",
    "domain": "大厂 AI 动态",
    "title": "FDA reports new outbreak of explosive diarrhea with 72 cases identified",
    "url": "https://arstechnica.com/health/2026/07/fda-reports-new-outbreak-of-explosive-diarrhea-with-72-cases-identified/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T19:22:36+00:00",
    "summary": "The FDA hasn't said where the cases are or how they're linked."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/07/google-now-lets-you-log-into-your-account-with-a-selfie/",
    "domain": "大厂 AI 动态",
    "title": "Forgot your Google password? Now you can log in with a selfie.",
    "url": "https://arstechnica.com/gadgets/2026/07/google-now-lets-you-log-into-your-account-with-a-selfie/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T19:14:25+00:00",
    "summary": "Google's selfie videos can be used for account access, AI Avatars, and age verification."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/ai-kill-switch-act-would-let-trump-admin-order-shutdown-of-rogue-ai-systems/",
    "domain": "大厂 AI 动态",
    "title": "AI Kill Switch Act would let Trump admin order shutdown of rogue AI systems",
    "url": "https://arstechnica.com/tech-policy/2026/07/ai-kill-switch-act-would-let-trump-admin-order-shutdown-of-rogue-ai-systems/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T19:08:01+00:00",
    "summary": "Bill would let Homeland Security chief decide when an AI should be shut down."
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/07/final-coyote-vs-acme-trailer-drops-at-sdcc/",
    "domain": "大厂 AI 动态",
    "title": "Final Coyote vs. Acme trailer drops at SDCC",
    "url": "https://arstechnica.com/culture/2026/07/final-coyote-vs-acme-trailer-drops-at-sdcc/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T18:01:46+00:00",
    "summary": "Also, the full trailer for Zach Cregger's Resident Evil features a likable everyman."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/07/woman-loses-vision-in-one-eye-after-uti-bacteria-evolves-to-invade-her-brain/",
    "domain": "大厂 AI 动态",
    "title": "A woman got a UTI. Two years later, the bacteria had evolved, invaded her brain.",
    "url": "https://arstechnica.com/health/2026/07/woman-loses-vision-in-one-eye-after-uti-bacteria-evolves-to-invade-her-brain/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T16:58:26+00:00",
    "summary": "The case provides a novel report of the emergence of heterovirulence."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/google-hit-with-1-billion-in-fines-as-eu-braces-for-trump-battle/",
    "domain": "大厂 AI 动态",
    "title": "Google hit with $1 billion in fines as EU braces for Trump battle",
    "url": "https://arstechnica.com/tech-policy/2026/07/google-hit-with-1-billion-in-fines-as-eu-braces-for-trump-battle/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T16:41:36+00:00",
    "summary": "Google becomes third tech giant to face huge fines under the Digital Markets Act."
  },
  {
    "id": "hn:48933344",
    "domain": "股票",
    "title": "SpaceX stock erases all its gains and slides below IPO price in intraday trading",
    "url": "https://www.latimes.com/business/story/2026-07-16/spacex-stock-erases-gains-slides-below-ipo-price-in-intraday-trading",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 314,
    "published_at": "2026-07-16T12:02:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:48948435",
    "domain": "股票",
    "title": "Short sellers notch $8.7B profit as SpaceX shares dip to IPO price",
    "url": "https://www.reuters.com/business/media-telecom/short-sellers-rack-up-87-bln-profit-spacex-slips-below-ipo-price-ortex-2026-07-16/",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 168,
    "published_at": "2026-07-17T15:17:54+00:00",
    "summary": ""
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
    "id": "hn:49024958",
    "domain": "股票",
    "title": "DOT cranks up its campaign to strip bike lane references from federal websites",
    "url": "https://text.npr.org/nx-s1-5900901",
    "source": "Jtsummers",
    "platform": "hackernews",
    "points": 37,
    "published_at": "2026-07-23T17:11:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:49012630",
    "domain": "股票",
    "title": "Alphabet Announces Second Quarter 2026 Results [pdf]",
    "url": "https://s206.q4cdn.com/479360582/files/doc_financials/2026/q2/2026q2-alphabet-earnings-release.pdf",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 36,
    "published_at": "2026-07-22T20:04:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:48938001",
    "domain": "股票",
    "title": "SPCX is now Wall Street's most shorted new stock",
    "url": "https://invezz.com/news/2026/07/16/the-worlds-most-valuable-ipo-spcx-is-now-wall-streets-most-shorted-new-stock/",
    "source": "lbrito",
    "platform": "hackernews",
    "points": 81,
    "published_at": "2026-07-16T18:03:56+00:00",
    "summary": ""
  },
  {
    "id": "hn:48984021",
    "domain": "股票",
    "title": "Mark Cuban: fight inequality by giving all workers company stock",
    "url": "https://fortune.com/2026/07/20/mark-cuban-income-inequality-company-stock-spacex-ipo-cost-plus-drugs/",
    "source": "01-_-",
    "platform": "hackernews",
    "points": 46,
    "published_at": "2026-07-20T19:52:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48950580",
    "domain": "股票",
    "title": "SpaceX stock drops to a new low and loses $1T in value in a month",
    "url": "https://www.businessinsider.com/spacex-stock-drops-new-low-ipo-price-starship-launch-scrubbed-2026-7",
    "source": "01-_-",
    "platform": "hackernews",
    "points": 74,
    "published_at": "2026-07-17T18:26:02+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3777848",
    "domain": "股票",
    "title": "AI进入采购支付闭环：Visa与连连完成大中华区首笔B2B智能体真实交易",
    "url": "https://wallstreetcn.com/articles/3777848",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T04:40:08+00:00",
    "summary": "7月24日，Visa与连连数字联合宣布，双方已完成由连连AI智能体LoopXPay执行的首笔真实B2..."
  },
  {
    "id": "wscn:3777840",
    "domain": "股票",
    "title": "A股三大股指跌超1%，长鑫存储概念股、半导体设备逆势拉升，有色金属齐跌，恒科指跌超1%，阿里跌5%",
    "url": "https://wallstreetcn.com/articles/3777840",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T04:05:37+00:00",
    "summary": "盘面上，个股呈现普跌态势，沪深京三市近5000股飘绿。量能再度萎缩，上午半天成交1.23万亿。沪深两市半日成交额1.23万亿，较上个交易日缩量超2300亿。板块方面，有色金属、互联网、软件、电力板块跌幅居前，算力租赁、Kimi概念低迷；长鑫存储概念逆势走强，合肥城建涨停。"
  },
  {
    "id": "wscn:3777844",
    "domain": "股票",
    "title": "DeepSeek的反共识判断：国产卡不缺生态，只缺产能",
    "url": "https://wallstreetcn.com/premium/articles/3777844?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T03:43:37+00:00",
    "summary": "市场曾将DeepSeek的突破概括为“以算法效率替代算力堆叠”，但对此或有不一样的见解。效率优化只是为了在有限资源下训练更大模型，中国AI与美国的根本差距仍在算力；与此同时，AI编程、高级编译器与超节点正在削弱国产卡的生态约束。国产算力下一阶段的核心矛盾，会不会正从“能不能用”转向“为什么还不够用”？"
  },
  {
    "id": "wscn:3777845",
    "domain": "股票",
    "title": "新加坡主权基金GIC：中国AI将拉低全球AI成本，加速企业普及",
    "url": "https://wallstreetcn.com/articles/3777845",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T03:43:33+00:00",
    "summary": "新加坡主权基金GIC首席投资官Bryan Yeo表示，DeepSeek、Kimi等中国AI模型的崛起将大幅降低AI应用成本，推动使用场景指数级增长。GIC已将AI列为核心投资方向，同时对中国AI企业前景持积极态度。"
  },
  {
    "id": "wscn:3777847",
    "domain": "股票",
    "title": "AI烧钱开始涨价！Meta再融资120亿美元，借钱成本明显上升",
    "url": "https://wallstreetcn.com/articles/3777847",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T03:34:04+00:00",
    "summary": "Meta正为德克萨斯州近1吉瓦数据中心寻求120亿美元融资，收益率初步讨论已超7%，风险溢价较九个月前上一笔交易高出约0.4个百分点。债券市场正在为科技巨头的烧钱狂潮重新定价，而与Meta上笔270亿美元\"Hyperion\"项目挂钩的债券，本周已跌至面值的96美分。"
  },
  {
    "id": "wscn:3777846",
    "domain": "股票",
    "title": "快穿、无限男主与Token账本：一款AI乙游的摸索之路",
    "url": "https://wallstreetcn.com/articles/3777846",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T03:14:22+00:00",
    "summary": "”言出法随“"
  },
  {
    "id": "wscn:3777837",
    "domain": "股票",
    "title": "2026下半年，大宗商品进入“高频黑天鹅”时代！",
    "url": "https://wallstreetcn.com/articles/3777837",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T03:12:25+00:00",
    "summary": "花旗强调，自2020年以来极端事件密度空前，\"黑天鹅\"已近乎常态化。花旗研究梳理下半年大宗商品尾部风险：美伊冲突升级或推油价突破200美元/桶；关键矿产囤积竞赛或将铜价推至20000美元/吨以上；黄金短期或再跌15%-20%，中长期有望升至6000美元/盎司；AI泡沫破裂或繁荣将对能源及金属产生双向冲击。"
  },
  {
    "id": "wscn:3777836",
    "domain": "股票",
    "title": "马斯克最新访谈：AI可能灭绝人类，但就像一枚20%概率会爆炸的火箭，我还是会坐上去享受旅程！",
    "url": "https://wallstreetcn.com/articles/3777836",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T03:07:27+00:00",
    "summary": "马斯克最新放出惊人预言：5年内AI智力将超越人类，10年后人类大概率失去控制权——\"我们不过是黑猩猩的进化版\"。面对10%-20%的AI毁灭人类的概率，他却选择坦然\"上船\"：既然无法阻止，不如身在局中。他的终极赌注是：2036年，人类或将迎来物质极度丰盈的黄金时代。"
  },
  {
    "id": "wscn:3777758",
    "domain": "股票",
    "title": "汇丰财富洞察：中国AI投资潜力在哪里？|汇听环球财富",
    "url": "https://wallstreetcn.com/premium/articles/3777758?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T02:41:22+00:00",
    "summary": "↓点击收听↓\n \n中国股市的AI主线依然明确，但板块间较为分化，布局需要精选赛道。我们偏好半导体..."
  },
  {
    "id": "wscn:3777841",
    "domain": "股票",
    "title": "BBA又一次集体降价",
    "url": "https://wallstreetcn.com/articles/3777841",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T02:41:11+00:00",
    "summary": "豪华市场的结构调整。"
  },
  {
    "id": "wscn:3777839",
    "domain": "股票",
    "title": "通用汽车交出“双面财报”",
    "url": "https://wallstreetcn.com/articles/3777839",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T02:40:59+00:00",
    "summary": "重新打量中国市场。"
  },
  {
    "id": "wscn:3777762",
    "domain": "股票",
    "title": "5万亿投资启幕！电网设备63亿中标潮，产业高增速谁在受益？",
    "url": "https://wallstreetcn.com/premium/articles/3777762?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T02:31:33+00:00",
    "summary": "7月21-22日，国家电网2026年特高压及输变电设备第三次招标结果落地——中国西电、平高电气、风范股份、金冠股份四家公司合计中标逾63亿元，其中头部两家吃下近60亿元。"
  },
  {
    "id": "wscn:3777842",
    "domain": "股票",
    "title": "现代汽车二季度营收创新高，营业利润下滑逾两成",
    "url": "https://wallstreetcn.com/articles/3777842",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T02:23:27+00:00",
    "summary": "中国市场挑战依旧。"
  },
  {
    "id": "wscn:3777835",
    "domain": "股票",
    "title": "谷歌财报的四个焦点：云利润率、资本开支增长逻辑、TPU会计处理、SpaceX的算力租约",
    "url": "https://wallstreetcn.com/articles/3777835",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T01:31:08+00:00",
    "summary": "摩根士丹利表示，谷歌云增速与利润率双超预期，生成式AI变现能力初现。但硬币另一面，谷歌将2026年资本开支上限激进上调至2050亿美元，2027年或进一步冲至3750亿美元，大摩将2027/2028年每股盈利预测各下调7%和5%。这场AI军备竞赛，回报曙光与资本压力正同步放大。"
  },
  {
    "id": "wscn:3777774",
    "domain": "股票",
    "title": "霍尔木兹之外，红海告急：布油能否再破120美元/桶？",
    "url": "https://wallstreetcn.com/premium/articles/3777774?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T01:30:26+00:00",
    "summary": "胡塞红海袭击切断沙特原油管道替代出口，全球能源运输风险升级，布油冲击120美元概率显著上升。"
  },
  {
    "id": "wscn:3777830",
    "domain": "股票",
    "title": "油价破百！胡塞武装开辟“红海战场”，特朗普权衡“更大规模战争”，乌克兰也来“火上浇油”",
    "url": "https://wallstreetcn.com/articles/3777830",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T00:58:35+00:00",
    "summary": "布伦特原油单月涨幅有望创下今年3月霍尔木兹封锁以来最大月度涨幅。阿布扎比生产的穆尔班原油期货更飙升至108美元。市场分析人士警告，若霍尔木兹海峡持续受阻、曼德海峡封锁成真，油价存在进一步冲向120美元乃至更高的风险。"
  },
  {
    "id": "wscn:3777832",
    "domain": "股票",
    "title": "中金：AI的金融时刻",
    "url": "https://wallstreetcn.com/articles/3777832",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T00:49:06+00:00",
    "summary": "中金认为，AI资本开支正从现金流驱动转向债务扩张，未来五年或现3.5万亿美元融资缺口。投资要“回本”，需每年约1万亿美元收入，意味着未来五年收入须年均近翻倍增长。融资规模本身并非泡沫，真正的考验是：能否在债务到期与资产贬值之前，跑出现金流的正向循环。"
  },
  {
    "id": "wscn:3777640",
    "domain": "股票",
    "title": "CPO的理想，NPO的现实：国产超节点为何率先押注“近封装光学”？",
    "url": "https://wallstreetcn.com/premium/articles/3777640?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T00:45:03+00:00",
    "summary": "当国产算力竞争由单卡性能转向系统效率，NPO正在成为超节点补齐高速互联能力的关键拼图。腾讯明确26Q4部署时间表，并推动统一行业标准，既释放出光芯片、光引擎和封装设备的需求信号，也意味着国产AI芯片、交换系统与服务器整机将迎来新的系统级增量。CPO代表长期理想，但NPO会不会率先成为国产超节点规模化落地的现实答案？"
  },
  {
    "id": "wscn:3777831",
    "domain": "股票",
    "title": "如何看待金银的反弹？",
    "url": "https://wallstreetcn.com/articles/3777831",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T00:44:19+00:00",
    "summary": "国金证券认为，金银近期涨势源于科技动量瓦解、资金轮动，可能是“假反弹”。黄金尚未突破下行通道，ETF流入和投机仓位改善有限。下半年黄金震荡修复概率较大，配置价值高于趋势交易价值，建议回调中逐步布局，年底目标区间4300—4500美元/盎司。"
  },
  {
    "id": "wscn:3777834",
    "domain": "股票",
    "title": "韩国重拳收紧个股杠杆ETF：现金门槛升至3000万韩元，7月31日提前生效",
    "url": "https://wallstreetcn.com/articles/3777834",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T00:40:57+00:00",
    "summary": "新规明确存款仅限纯现金，剔除担保证券，卖股资金需T+2到账方可计入，且严禁券商后续放宽限制。新规适用范围涵盖韩国国内及海外交易所上市的所有单一个股杠杆产品，包括以三星电子、SK海力士为标的的国内产品，以及特斯拉、英伟达等海外个股杠杆ETF和ETN。"
  },
  {
    "id": "hn:48946872",
    "domain": "股票",
    "title": "US Corporate Insiders Are Selling Stocks at a Near Record Pace",
    "url": "https://www.bloomberg.com/news/articles/2026-07-17/us-corporate-insiders-are-selling-stocks-at-a-near-record-pace",
    "source": "pimienta",
    "platform": "hackernews",
    "points": 57,
    "published_at": "2026-07-17T13:00:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:48958985",
    "domain": "股票",
    "title": "Traders are increasingly betting against SpaceX just weeks after IPO",
    "url": "https://www.ft.com/content/2b96703d-440b-46db-8d86-9fff9ecc59d5",
    "source": "ethanhawksley",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-07-18T15:26:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:48974426",
    "domain": "股票",
    "title": "Big tech needs to justify AI spending as investors dump stocks",
    "url": "https://www.bloomberg.com/news/articles/2026-07-19/big-tech-needs-to-justify-ai-spending-as-investors-dump-stocks",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 45,
    "published_at": "2026-07-20T04:41:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:48907665",
    "domain": "股票",
    "title": "IBM is on pace for its worst day ever",
    "url": "https://www.cnn.com/2026/07/14/tech/ibm-stock-worst-day-ever",
    "source": "1970-01-01",
    "platform": "hackernews",
    "points": 48,
    "published_at": "2026-07-14T14:39:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:48923343",
    "domain": "股票",
    "title": "SpaceX stock sinks below $135 IPO price for the first time",
    "url": "https://www.cnbc.com/2026/07/15/spacex-spcx-stock-ipo-price.html",
    "source": "abduhl",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-07-15T16:30:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:48889982",
    "domain": "股票",
    "title": "Xbox CEO Asha Sharma, who laid off 3,200 employees, to lead task force on jobs",
    "url": "https://www.pcgamer.com/gaming-industry/us-federal-reserve-taps-xbox-ceo-asha-sharma-who-just-laid-off-3-200-employees-to-lead-task-force-on-jobs/",
    "source": "robtherobber",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-07-13T09:27:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:48905958",
    "domain": "股票",
    "title": "IBM shares down 23% as clients spend more on hardware and memory chips",
    "url": "https://www.cnbc.com/2026/07/14/ibm-warns-second-quarter-earnings-fell-short-of-expectations.html",
    "source": "rvz",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-07-14T12:44:17+00:00",
    "summary": ""
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
    "id": "hn:48787052",
    "domain": "股票",
    "title": "Elon Musk posted twice as often on UK race and immigration as about SpaceX IPO",
    "url": "https://www.theguardian.com/technology/2026/jul/04/elon-musk-uk-race-immigration-spacex-ipo",
    "source": "iamflimflam1",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-07-04T17:18:19+00:00",
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
    "id": "hn:48717469",
    "domain": "金融",
    "title": "The CEO of Mullvad is the main financer of the Swedish Örebro party",
    "url": "https://det.social/@lostgen/116820546568940358",
    "source": "Risse",
    "platform": "hackernews",
    "points": 695,
    "published_at": "2026-06-29T10:45:51+00:00",
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
    "id": "hn:48915953",
    "domain": "金融",
    "title": "Stripe and Advent have made a joint offer to acquire PayPal – sources",
    "url": "https://www.reuters.com/business/finance/stripe-advent-offer-buy-paypal-more-than-53-billion-sources-say-2026-07-15/",
    "source": "rvz",
    "platform": "hackernews",
    "points": 494,
    "published_at": "2026-07-15T03:32:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:48878126",
    "domain": "金融",
    "title": "Under federal rule, colleges must leave grads better off or lose financial aid",
    "url": "https://www.npr.org/2026/06/30/nx-s1-5835631/turner-camhi-do-no-harm-college-loans",
    "source": "nradov",
    "platform": "hackernews",
    "points": 198,
    "published_at": "2026-07-12T04:00:14+00:00",
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
    "id": "hn:48892638",
    "domain": "金融",
    "title": "Benchmarking 15 “E-Waste” GPUs with Modern Workloads",
    "url": "https://esologic.com/benchmarking-tesla-gpus/",
    "source": "eso_logic",
    "platform": "hackernews",
    "points": 141,
    "published_at": "2026-07-13T13:48:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:48826703",
    "domain": "金融",
    "title": "Is The Economist Always Wrong?",
    "url": "https://www.economist.com/interactive/finance-and-economics/2026/07/02/is-the-economist-always-wrong",
    "source": "nreece",
    "platform": "hackernews",
    "points": 138,
    "published_at": "2026-07-08T02:17:01+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.20667",
    "domain": "金融",
    "title": "Good Guys With Guns? The Relationship Between Legal Firearm Ownership and Firearm Deaths and Crime in Canada",
    "url": "https://arxiv.org/abs/2607.20667",
    "source": "Derek Mikola, Matthew D. Webb",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T04:00:00+00:00",
    "summary": "arXiv:2607.20667v1 Announce Type: new Abstract: Civilian firearm ownership is politically contentious, yet most evidence linking guns to crime and death comes from the U.S. Canada offers a unique case"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.20762",
    "domain": "金融",
    "title": "Quantifying Sub-Optimality in Routing for Automated Market Makers",
    "url": "https://arxiv.org/abs/2607.20762",
    "source": "Weiye Xi, Ciamac C. Moallemi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T04:00:00+00:00",
    "summary": "arXiv:2607.20762v1 Announce Type: new Abstract: We provide a large-scale empirical audit of DEX routing using 2.98 million WETH-USDC swaps on Ethereum. Comparing realized routes with optimized benchma"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.20807",
    "domain": "金融",
    "title": "Execution and Evaluation: A New Occupational Measure and Long-Run Employment Gradients",
    "url": "https://arxiv.org/abs/2607.20807",
    "source": "Li Gan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T04:00:00+00:00",
    "summary": "arXiv:2607.20807v1 Announce Type: new Abstract: Artificial intelligence automates execution more readily than evaluation: producing output is cheap, judging whether it is correct is not. Exposure meas"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.21048",
    "domain": "金融",
    "title": "Accelerating fossil gas independence in Europe",
    "url": "https://arxiv.org/abs/2607.21048",
    "source": "Lukas Franken, Iegor Riepin, Tom Brown",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T04:00:00+00:00",
    "summary": "arXiv:2607.21048v1 Announce Type: new Abstract: Recent price shocks have prompted calls to curb Europe's dependence on fossil gas imports, but the cost of this goal, and the consumer protection it aff"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.21170",
    "domain": "金融",
    "title": "Portfolio Optimization under Dynamic Rebalancing via Topological Data Analysis and News Sentiments",
    "url": "https://arxiv.org/abs/2607.21170",
    "source": "Divyanee Garg",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T04:00:00+00:00",
    "summary": "arXiv:2607.21170v1 Announce Type: new Abstract: Understanding similarity among financial assets is essential for effective portfolio diversification. This paper proposes a novel sentiment-adjusted por"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.21285",
    "domain": "金融",
    "title": "Electricity demand has not become more price-responsive despite ninety years of technological change",
    "url": "https://arxiv.org/abs/2607.21285",
    "source": "Peter Kudela, Tomas Havranek, Zuzana Irsova, Anna Kudelova, Vojtech Sikl",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T04:00:00+00:00",
    "summary": "arXiv:2607.21285v1 Announce Type: new Abstract: Energy planners have long assumed that electricity demand will grow more price-responsive as metering, automation, and storage spread, an assumption now"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.21459",
    "domain": "金融",
    "title": "The Evolution of Digital Search: From Blue Links to Delegated Decision-Making",
    "url": "https://arxiv.org/abs/2607.21459",
    "source": "David M. Rothschild, Nicole Immorlica, Brendan Lucier, Markus Mobius, Aleksandrs Slivkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T04:00:00+00:00",
    "summary": "arXiv:2607.21459v1 Announce Type: new Abstract: Digital search is undergoing a fundamental transformation from a human-driven process of discovery to an agent-mediated system of delegated decision-mak"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.21512",
    "domain": "金融",
    "title": "Group boarding for airplanes: benchmarking static policies and optimizing dynamic assignment with deep reinforcement learning",
    "url": "https://arxiv.org/abs/2607.21512",
    "source": "Minyu Shen, Weihua Gu, Junqi Ma, Boqian Song, Li Zhen, Gang Kou",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T04:00:00+00:00",
    "summary": "arXiv:2607.21512v1 Announce Type: new Abstract: Improving boarding efficiency reduces airplane turnaround time and improves passenger experience. Airlines typically assign passengers to a few sequenti"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.20781",
    "domain": "金融",
    "title": "The Human-AI Substitution Principle: When will you be replaced by AI in your organization?",
    "url": "https://arxiv.org/abs/2607.20781",
    "source": "Bonny Banerjee, Shreya Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T04:00:00+00:00",
    "summary": "arXiv:2607.20781v1 Announce Type: cross Abstract: Artificial Intelligence (AI) is rapidly transforming organizations, raising a fundamental organizational and economic question: when will a human empl"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.21268",
    "domain": "金融",
    "title": "pAI-Econ-claude: A Gated Human-in-the-Loop Multi-Agent Architecture for AI-Assisted Economic Theory Development",
    "url": "https://arxiv.org/abs/2607.21268",
    "source": "Chen Zhu, Xiaolu Wang, Weilong Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T04:00:00+00:00",
    "summary": "arXiv:2607.21268v1 Announce Type: cross Abstract: In many social-science research tasks, such as economics, LLM-based agents must produce outputs for which no cheap, task-complete, machine-readable co"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.21534",
    "domain": "金融",
    "title": "Generative AI Availability, Grades, and Student Satisfaction at a Large University",
    "url": "https://arxiv.org/abs/2607.21534",
    "source": "James M. Zumel Dumlao, Meng Wang, Zhonghan Xie, Junyao Hu, Ivan Bar, George Chaney III, Henry Gold, Misha Teplitskiy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T04:00:00+00:00",
    "summary": "arXiv:2607.21534v1 Announce Type: cross Abstract: The spread of generative AI (GenAI) in higher education has raised concerns that students offload cognitive effort to AI, earning high grades without "
  },
  {
    "id": "rss:https://arxiv.org/abs/2407.15147",
    "domain": "金融",
    "title": "Industry Dynamics with Cartels: The Case of the Container Shipping Industry",
    "url": "https://arxiv.org/abs/2407.15147",
    "source": "Suguru Otani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T04:00:00+00:00",
    "summary": "arXiv:2407.15147v2 Announce Type: replace Abstract: This paper studies how shipping conferences---explicit cartels---shaped container shipping through prices, entry, and investment from 1973--1990. I "
  },
  {
    "id": "rss:https://arxiv.org/abs/2506.21253",
    "domain": "金融",
    "title": "Suspense and Surprise in European Football",
    "url": "https://arxiv.org/abs/2506.21253",
    "source": "Raphael Flepp, Tim Pawlowski, Travis Richardson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T04:00:00+00:00",
    "summary": "arXiv:2506.21253v2 Announce Type: replace Abstract: A key criterion for evaluating sports competitions is their attractiveness to consumers. In this paper, we propose using match-level suspense and su"
  },
  {
    "id": "rss:https://arxiv.org/abs/2507.00575",
    "domain": "金融",
    "title": "Pathwise Roughness of Bitcoin Realized Volatility: Stability Across Time, Sampling, and Volatility Measures",
    "url": "https://arxiv.org/abs/2507.00575",
    "source": "Milan Pontiggia (MAGEFI - University of Bordeaux, France)",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T04:00:00+00:00",
    "summary": "arXiv:2507.00575v4 Announce Type: replace Abstract: This paper examines whether Bitcoin realized volatility admits a measurable pathwise roughness index and how stable that estimate is across time and"
  },
  {
    "id": "rss:https://arxiv.org/abs/2602.02483",
    "domain": "金融",
    "title": "Skill Substitution, Expectations, and the Business Cycle",
    "url": "https://arxiv.org/abs/2602.02483",
    "source": "Andreas Leibing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T04:00:00+00:00",
    "summary": "arXiv:2602.02483v2 Announce Type: replace Abstract: This paper studies how labor market conditions around high school graduation affect postsecondary skill investments. Using administrative data on mo"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.01933",
    "domain": "金融",
    "title": "Hiring Discrimination and the Task Content of Jobs: Evidence from a Large-Scale Resume Audit",
    "url": "https://arxiv.org/abs/2604.01933",
    "source": "Sharon Braun, Jonathan Bushnell, Zachary Cowell, David Dowling Samuel Goldstein, Andrew Johnson, George Miller, John M. Nunley, R. Alan Seals, Mingzhou Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T04:00:00+00:00",
    "summary": "arXiv:2604.01933v2 Announce Type: replace Abstract: We conducted a large-scale resume audit of 36,880 applications to 9,220 job advertisements for new college graduates across the United States. Firms"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.07655",
    "domain": "金融",
    "title": "Robustness to Model Uncertainties Drives More Rapid CO2 Emissions Reductions",
    "url": "https://arxiv.org/abs/2607.07655",
    "source": "Lisa Rennels, Frank Errickson, David Smith, Bryan Parthum, Klaus Keller, David Anthoff",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T04:00:00+00:00",
    "summary": "arXiv:2607.07655v2 Announce Type: replace Abstract: Evaluating the economic impacts of climate policies is important for designing a response to climate change. One typical approach to assessing mitig"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.08500",
    "domain": "金融",
    "title": "Estimating the Stochastic Discount Factor from Option Prices and Predicting the Equity Premium",
    "url": "https://arxiv.org/abs/2607.08500",
    "source": "Kenichiro Shiraya, Tomohisa Yamakami, Akira Yamazaki",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T04:00:00+00:00",
    "summary": "arXiv:2607.08500v2 Announce Type: replace Abstract: This paper proposes a stochastic discount factor (SDF) scaled by time-varying volatility. By utilizing prices and market data implied solely from S\\"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.17428",
    "domain": "金融",
    "title": "Uniform-Loss Automated Market Making for Prediction Markets",
    "url": "https://arxiv.org/abs/2607.17428",
    "source": "Ciamac C. Moallemi, Dan Robinson, Brian Zhu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T04:00:00+00:00",
    "summary": "arXiv:2607.17428v2 Announce Type: replace Abstract: Automated market makers (AMMs) for prediction markets descend from market scoring rules, where a mechanism operator subsidizes a market to aggregate"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.19562",
    "domain": "金融",
    "title": "The Direct and Indirect Effects of Genetics and Education",
    "url": "https://arxiv.org/abs/2607.19562",
    "source": "Senan Hogan-Hennessy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T04:00:00+00:00",
    "summary": "arXiv:2607.19562v2 Announce Type: replace Abstract: Genes associated with educational attainment causally improve labour market income, but the economic mechanism behind this relationship is not clear"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.20343",
    "domain": "金融",
    "title": "Path-Space Model Risk via Signature-Induced Optimal Transport",
    "url": "https://arxiv.org/abs/2607.20343",
    "source": "Tomoyuki Ichiba, Qijin Shi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T04:00:00+00:00",
    "summary": "arXiv:2607.20343v2 Announce Type: replace Abstract: We propose a signature-induced, optimal transport framework for path-space model risk, in which ambiguity between stochastic path laws is factorized"
  },
  {
    "id": "rss:https://arxiv.org/abs/2511.08202",
    "domain": "金融",
    "title": "Mean-Field Analytical Solution of the Mesa Boltzmann Wealth Model",
    "url": "https://arxiv.org/abs/2511.08202",
    "source": "Jiyuan Lyu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T04:00:00+00:00",
    "summary": "arXiv:2511.08202v2 Announce Type: replace-cross Abstract: The Boltzmann wealth model provided by the Mesa framework is a classic example in agent-based modeling, yet its statistical properties are typ"
  },
  {
    "id": "rss:https://arxiv.org/abs/2603.11838",
    "domain": "金融",
    "title": "DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining",
    "url": "https://arxiv.org/abs/2603.11838",
    "source": "Yutong Yan, Raphael Tang, Zhenyu Gao, Wenxi Jiang, Yao Lu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T04:00:00+00:00",
    "summary": "arXiv:2603.11838v2 Announce Type: replace-cross Abstract: Large language models pretrained on internet-scale data risk lookahead bias in forecasting tasks, as they may have already seen the true outco"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.01363",
    "domain": "金融",
    "title": "Crashing Waves vs. Rising Tides: Findings on AI Automation from Thousands of Worker Evaluations of Labor Market Tasks",
    "url": "https://arxiv.org/abs/2604.01363",
    "source": "Matthias Mertens, Adam Kuzee, Brittany S. Harris, Harry Lyu, Wensu Li, Jonathan Rosenfeld, Meiri Anto, Martin Fleming, Neil Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T04:00:00+00:00",
    "summary": "arXiv:2604.01363v3 Announce Type: replace-cross Abstract: We characterize AI automation as a continuum between crashing waves, in which capabilities jump abruptly across narrow task sets, and rising t"
  },
  {
    "id": "hn:48999329",
    "domain": "金融",
    "title": "A Man Who Runs the IRS Spied on Colleagues When He Worked at JPMorgan",
    "url": "https://www.wsj.com/finance/banking/irs-bisignano-spying-jpmorgan-6cd1ddf0",
    "source": "cwwc",
    "platform": "hackernews",
    "points": 25,
    "published_at": "2026-07-21T22:40:46+00:00",
    "summary": ""
  },
  {
    "id": "hn:49001708",
    "domain": "金融",
    "title": "Tesla Balance Bike",
    "url": "https://shop.tesla.com/product/balance-bike-for-kids",
    "source": "surprisetalk",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-07-22T04:00:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:48884775",
    "domain": "金融",
    "title": "Storm clouds gather over America's financial supremacy",
    "url": "https://www.economist.com/finance-and-economics/2026/07/12/storm-clouds-gather-over-americas-financial-supremacy",
    "source": "pseudolus",
    "platform": "hackernews",
    "points": 70,
    "published_at": "2026-07-12T21:04:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:48999988",
    "domain": "金融",
    "title": "Brazil and US clash over future of payments as Pix system stirs global interest",
    "url": "https://www.reuters.com/business/finance/brazil-us-clash-over-future-payments-popular-pix-system-stirs-global-interest-2026-07-21/",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-07-21T23:52:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:48986211",
    "domain": "金融",
    "title": "Delayed Boeing jets only fit for baked bean tins, Emirates boss says",
    "url": "https://finance.yahoo.com/technology/articles/delayed-boeing-jets-only-fit-162341761.html",
    "source": "devonnull",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-07-20T23:29:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:48735748",
    "domain": "金融",
    "title": "Supreme Court takes sledgehammer to federal regulatory structure",
    "url": "https://www.npr.org/2026/06/29/nx-s1-5875161/supreme-court-takes-sledgehammer-to-much-of-federal-governments-regulatory-structure",
    "source": "marojejian",
    "platform": "hackernews",
    "points": 83,
    "published_at": "2026-06-30T17:05:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:48783175",
    "domain": "金融",
    "title": "The LLVM Compiler Infrastructure",
    "url": "https://cacm.acm.org/federal-funding-of-academic-research/the-llvm-compiler-infrastructure/",
    "source": "tosh",
    "platform": "hackernews",
    "points": 80,
    "published_at": "2026-07-04T06:43:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:48953857",
    "domain": "金融",
    "title": "Nadella Blasts AI Industry's Double Standard",
    "url": "https://finance.biggo.com/news/438f299b-ca23-468d-b37d-0ffe09a4ca55",
    "source": "nittanymount",
    "platform": "hackernews",
    "points": 30,
    "published_at": "2026-07-18T00:28:46+00:00",
    "summary": ""
  },
  {
    "id": "hn:48785077",
    "domain": "金融",
    "title": "The Fediverse Is Not the Way Forward",
    "url": "https://trialandfailure.net/the-fediverse-is-not-the-way-forward/",
    "source": "ExMachina73",
    "platform": "hackernews",
    "points": 70,
    "published_at": "2026-07-04T12:53:12+00:00",
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
    "id": "hn:48880233",
    "domain": "金融",
    "title": "IT administrators are \"fed up\" with Microsoft's \"useless\" apps and Windows 11",
    "url": "https://www.neowin.net/news/it-admins-feel-overwhelmingly-sick-of-microsoft-and-windows-11-garbage-apps-products/",
    "source": "01-_-",
    "platform": "hackernews",
    "points": 46,
    "published_at": "2026-07-12T11:22:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:48791799",
    "domain": "金融",
    "title": "Is The Economist Always Wrong?",
    "url": "https://economist.com/interactive/finance-and-economics/2026/07/02/is-the-economist-always-wrong",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 59,
    "published_at": "2026-07-05T06:40:05+00:00",
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
    "id": "hn:48824584",
    "domain": "金融",
    "title": "JPMorgan, BofA and Others Explore Buying Card Network to Raise Debit-Card Fees",
    "url": "https://www.wsj.com/finance/banking/jpmorgan-bank-of-america-and-other-banks-explore-a-deal-to-shake-up-payments-world-9d8639fb",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-07-07T22:04:18+00:00",
    "summary": ""
  }
]
```
