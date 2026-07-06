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

- 今日日期：`2026-07-06`
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
  "date": "2026-07-06",
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
    "id": "bvid:BV1DfrdByE2H",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Agent智能体】教程！大模型入门到进阶，一套全解决！Agentic AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av115897075242856",
    "source": "吴恩达Agent",
    "platform": "bilibili",
    "points": 3602140,
    "published_at": "2026-01-15T03:56:12+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n1. 构建智能体设计模式：反射、工具使用、规划与多智能体工作流；\n2. 将人工智能与外部工具集成：数据库、API、网络搜索与代码执行；\n3. 评估并优化人工智能系统：性能指标、错误分析与生产部署"
  },
  {
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "9分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 1431445,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1w9MczyETB",
    "domain": "AI",
    "title": "【Vibe Coding】0基础项目实战教学丨Claude Code，Codex，Cursor教程",
    "url": "http://www.bilibili.com/video/av114669670898752",
    "source": "蛋黄酱拌巧克力",
    "platform": "bilibili",
    "points": 1032919,
    "published_at": "2025-06-12T12:28:18+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1yorUYWEGD",
    "domain": "AI",
    "title": "普通人也可以看的 AI 编程指南 | Cursor 教程｜Cursor 使用技巧和思路｜如何免费使用 Cursor｜AI 编程",
    "url": "http://www.bilibili.com/video/av113786467981446",
    "source": "不正经的前端啊",
    "platform": "bilibili",
    "points": 940620,
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
    "points": 841127,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 748640,
    "published_at": "2026-06-09T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“VibeCoding”免费获取\n【课程简介】从零开始，用自然语言指挥AI开发真实软件项目！"
  },
  {
    "id": "bvid:BV1WBG9zgECp",
    "domain": "AI",
    "title": "史上最强 AI 编程工具免费啦！Cursor 保姆级使用教程！新手友好！看到就是赚到！｜ 集成 MCP ！",
    "url": "http://www.bilibili.com/video/av114426116120045",
    "source": "AfterShip",
    "platform": "bilibili",
    "points": 666050,
    "published_at": "2025-05-01T04:00:00+00:00",
    "summary": "相信你已经在网上刷到过不少的 AI 工具，但如果你让我推荐最值得我们每个人学习的一款 AI 工具，那绝对就是史上最强的 AI 编程工具 —— Cursor。为此，我们录制了一个保姆级的 Cursor 新手教程，在这里免费分享给大家。即使你是一个对 AI 完全 0 基础的新手小白，看完这个视频后，你也可以彻底了解 Cursor 这个软件，并知道如何从 0 到 1 用 Cursor 做出入门级的 AI"
  },
  {
    "id": "bvid:BV1Yi5M6DERk",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116560144369496",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 540072,
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
    "points": 495735,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1eK5DzHEWu",
    "domain": "AI",
    "title": "MCP实战指南，mcp视频教程，2小时学透mcp",
    "url": "http://www.bilibili.com/video/av114380213586544",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 379831,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1VCVS6PEAd",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent零基础全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116668525186915",
    "source": "大模型入门教程",
    "platform": "bilibili",
    "points": 345094,
    "published_at": "2026-05-31T09:46:57+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1VDTv6rEtM",
    "domain": "AI",
    "title": "终于，Claude Code 封号原因被曝光了！竟然针对中国用户，植入隐形代码？",
    "url": "http://www.bilibili.com/video/av116844031774993",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 331117,
    "published_at": "2026-07-01T09:35:43+00:00",
    "summary": "Claude Code 封号原因终于找到了！国外开发者逆向 Claude Code 源码，发现 Anthropic 在客户端里藏了一套隐蔽的用户标记系统，这期视频带你完整还原封号真相。\n开源 AI 编程教程：github.com/liyupi/ai-guide\n编程学习教程+实战项目+简历模板：codefather.cn\n最近 AI 圈儿不太平啊，OpenAI Codex 封号、Cursor 地区"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 176286,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 170512,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV16NvCBrEVs",
    "domain": "AI",
    "title": "什么是Vibe Coding，以及怎么使用？",
    "url": "http://www.bilibili.com/video/av115797133368973",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 160797,
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
    "points": 158862,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 142106,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 120805,
    "published_at": "2026-07-01T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260701\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\nAI大模型开发热门教程：\nAI大模型开发：BV1h1"
  },
  {
    "id": "bvid:BV1dpdZYBE9q",
    "domain": "AI",
    "title": "零代码让AI秒接海量MCP工具！最适合小白的MCP集合平台",
    "url": "http://www.bilibili.com/video/av114340703243255",
    "source": "AI研究室-帆哥",
    "platform": "bilibili",
    "points": 99526,
    "published_at": "2025-04-15T11:00:00+00:00",
    "summary": "最近MCP太火了，阿里直接跟进把MCP整合到百炼平台里面了，做了一个MCP的“应用商店”。\n之前不管是在cursor还是Claude上还是需要配置一下MCP服务器，现在在百炼上就可以直接无脑添加MCP工具，非常方便。\n而且因为在平台上一体化，和大模型可以打包配置，让后端的运维部署变得更轻松。\n这个视频教你怎么用阿里云百炼的MCP工具创建一个agent应用。"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 92407,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1A24y1J7Dt",
    "domain": "AI",
    "title": "如何在VS Code中使用Cursor自动生成代码",
    "url": "http://www.bilibili.com/video/av781409810",
    "source": "许你再少年",
    "platform": "bilibili",
    "points": 73560,
    "published_at": "2023-03-23T11:32:23+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1ZEJA6xEds",
    "domain": "AI",
    "title": "最新方法！国内免费无限制，使用Claude Code！",
    "url": "http://www.bilibili.com/video/av116746874848391",
    "source": "我是阿众",
    "platform": "bilibili",
    "points": 70075,
    "published_at": "2026-06-15T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 67727,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 67578,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1ZjDYB7Eam",
    "domain": "AI",
    "title": "从 0 到 1：6小时掌握 Vibe Coding！ Claude Code ＋ AI 这支影片直接让你超越 90% AI 玩家",
    "url": "http://www.bilibili.com/video/av116362122894759",
    "source": "李哈利Harry",
    "platform": "bilibili",
    "points": 62100,
    "published_at": "2026-04-08T11:00:00+00:00",
    "summary": "🌟 加入AI大师社群并运用AI创业赚钱：https://www.skool.com/aiagent/about?ref=f2b566934c5c4639aaa47ab1fe39310e\n📌 加入我的免费 Skool 社群，获取模板：https://www.skool.com/aiagent8/about?ref=f2b566934c5c4639aaa47ab1fe39310e\n\n🚧 开始使用 n8"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 52782,
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
    "points": 41545,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1YV7W6YEFU",
    "domain": "AI",
    "title": "方向错了！手机跟AI Agent到底该怎么结合？",
    "url": "http://www.bilibili.com/video/av116822892418628",
    "source": "我是HYK",
    "platform": "bilibili",
    "points": 31148,
    "published_at": "2026-06-28T03:00:00+00:00",
    "summary": "方向错了！一句话订票、点咖啡，这种极其容易出错的Agent，几乎没有坚持用下来的用户；现阶段手机需要的是短链路、点到为止的AI Agent。"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 29895,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV1bh3LzqEze",
    "domain": "AI",
    "title": "Chatbox AI终端：跨平台+MCP+知识库+开源+免费！一键连接所有AI语言模型！手把手安装使用指南！",
    "url": "http://www.bilibili.com/video/av114793218380950",
    "source": "_Smzh_",
    "platform": "bilibili",
    "points": 27678,
    "published_at": "2025-07-04T10:00:00+00:00",
    "summary": "chatbox官网：https://chatboxai.app\ngithub仓库：https://github.com/chatboxai/chatbox\n\nLM Studio教程：BV1usrLYTEZR\nTGW懒人包部署教程：BV1dVCzYUE7G\n本地语言模型个人推荐：BV1Bb421E7j7"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22598,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1cCEi6sEU5",
    "domain": "AI",
    "title": "🦊他能成功吗？Claude Code 接管虚幻引擎5，打造一款游戏 | 带你走完整个流程",
    "url": "http://www.bilibili.com/video/av116731724959171",
    "source": "Apeak_虚幻丰哥",
    "platform": "bilibili",
    "points": 17465,
    "published_at": "2026-06-11T13:41:36+00:00",
    "summary": "Claude Code 接管虚幻引擎5，打造了一款游戏\n下载我的 CLAUDE.md（帮你省 token 的配置）\n链接：https://pan.quark.cn/s/b6e50b4b2535\n提取码：tbaE\nStefan 3D AI ：https://www.youtube.com/watch?v=iRcrZjOt5H8&amp;t=1s\n🔗 完整教程指南和链接：https://www.top"
  },
  {
    "id": "bvid:BV1LWTe6gEVc",
    "domain": "AI",
    "title": "Claude code帮我实现综述论文自由！",
    "url": "http://www.bilibili.com/video/av116842504918580",
    "source": "做科研的大师兄",
    "platform": "bilibili",
    "points": 17399,
    "published_at": "2026-07-01T03:07:40+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1hnjGzLE14",
    "domain": "AI",
    "title": "【小智教程】手挽手教你如何接入别人的MCP服务",
    "url": "http://www.bilibili.com/video/av114568722450105",
    "source": "空白泡泡糖果",
    "platform": "bilibili",
    "points": 17320,
    "published_at": "2025-05-25T13:36:25+00:00",
    "summary": "文档：https://icnt94i5ctj4.feishu.cn/docx/ZkR3d1lfUosIFCx4qWJcI4QunY0\nshay大佬的HA SSE接入文档：https://bbs.hassbian.com/thread-29314-1-1.html"
  },
  {
    "id": "bvid:BV1JU7E6PEar",
    "domain": "AI",
    "title": "Cursor 已死？我为什么要退订 Cursor ？",
    "url": "http://www.bilibili.com/video/av116819553683121",
    "source": "小狗瑞恩Ryan",
    "platform": "bilibili",
    "points": 16909,
    "published_at": "2026-06-27T01:52:00+00:00",
    "summary": "当了一年多的 Cursor 重度用户，最近把它退订了。\n\n不是它变差了，是 Claude Code 和 Codex 真的太好用了。\n\n几个真实感受： ① 大模型越来越强，我已经不怎么手写代码了 ② Cursor 套的是 VS Code 壳子，只属于程序员 ③ 底层模型不在一个量级——Claude 有 Opus 和 Fable 5，Codex 有 GPT 5.5/5.6，Cursor 的 Compo"
  },
  {
    "id": "bvid:BV1hfTj6pEa6",
    "domain": "AI",
    "title": "【2026最新版】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完就涨薪！",
    "url": "http://www.bilibili.com/video/av116849316529790",
    "source": "AI大模型技术",
    "platform": "bilibili",
    "points": 15323,
    "published_at": "2026-07-02T08:01:51+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1iDRQBrEF6",
    "domain": "AI",
    "title": "Claude + Blender 现在太强了 —— 完整免费设置",
    "url": "http://www.bilibili.com/video/av116543333601720",
    "source": "设计之道",
    "platform": "bilibili",
    "points": 14809,
    "published_at": "2026-05-09T07:11:36+00:00",
    "summary": "【简介】\nAnthropic 刚刚发布了用于创意工具的官方 Claude Connectors —— 其中 Blender 连接器对 3D 艺术家来说最重要。在本视频中，我将展示最佳的 Claude + Blender 免费设置，以及为什么这次更新可能会改变我们构建 3D 场景的方式。\n\n【你将学到】\n01:13 步骤 1：安装 Blender MCP 和 Claude Code\n02:31 步骤"
  },
  {
    "id": "bvid:BV18TZYY8EuJ",
    "domain": "AI",
    "title": "微软最新AI Agent入门课程 • 中英",
    "url": "http://www.bilibili.com/video/av114246130076146",
    "source": "Mindofuture",
    "platform": "bilibili",
    "points": 13847,
    "published_at": "2025-03-30T02:06:00+00:00",
    "summary": "在这门包含10节课的课程中，我们将带你从概念到代码，全面覆盖构建AI代理的基础知识。在这里找到完整的“AI代理入门”课程及代码示例\nhttps://github.com/microsoft/ai-agents-for-beginners\n\nP01 什么是AI代理\nP02 使用哪种AI代理框架\nP03 如何设计优秀的AI代理\nP04 什么是代理工具使用设计模式\nP05 什么是代理式RAG\nP06 如"
  },
  {
    "id": "bvid:BV1etEQ6DETs",
    "domain": "AI",
    "title": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！",
    "url": "http://www.bilibili.com/video/av116724192118321",
    "source": "AI产品经理大模型",
    "platform": "bilibili",
    "points": 12180,
    "published_at": "2026-06-10T05:41:54+00:00",
    "summary": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！"
  },
  {
    "id": "bvid:BV1fiLr6XEj8",
    "domain": "AI",
    "title": "【大白哥AI与安全】手把手教你AI渗透,挖漏洞",
    "url": "http://www.bilibili.com/video/av116601936418546",
    "source": "大白哥AI与安全",
    "platform": "bilibili",
    "points": 11575,
    "published_at": "2026-05-19T15:33:02+00:00",
    "summary": "一键三连加关注，私信大白哥免费领取课件\n更多红队攻防实战课程，请私信大白哥咨询"
  },
  {
    "id": "bvid:BV1C3jt64EPS",
    "domain": "AI",
    "title": "B站讲的最好的Vibe Coding企业级项目实战教程（2026最新版）从入门到进阶，七天速通Claude Code+Codex+CursorAI工程化编程开发",
    "url": "http://www.bilibili.com/video/av116787425383675",
    "source": "图灵学院诸葛",
    "platform": "bilibili",
    "points": 10057,
    "published_at": "2026-06-21T09:48:04+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n 【本视频笔记代码、大模型最新学习路线、系统学习课程、实战案例、电子书+问题解答等戳这里获取→https://www.bilibili.com/read/cv39576966/?jump_opus=1】"
  },
  {
    "id": "bvid:BV191TY6KEHk",
    "domain": "AI",
    "title": "【全500集】目前B站最全最细的AI Agent零基础全套教程（从入门到精通），5天从入门到精通AI Agent，学完即可就业！看完这一套Agent教程就够了！",
    "url": "http://www.bilibili.com/video/av116843192851440",
    "source": "Agent智能体-",
    "platform": "bilibili",
    "points": 9951,
    "published_at": "2026-07-01T06:09:09+00:00",
    "summary": "【全500集】目前B站最全最细的AI Agent零基础全套教程（从入门到精通），5天从入门到精通AI Agent，学完即可就业！看完这一套AI Agent教程就够了！"
  },
  {
    "id": "bvid:BV1QuTv6BEf7",
    "domain": "AI",
    "title": "vibe coding｜打工人做App全流程分享！含大量提示词和prd～｜【b站AI创造公开赛】",
    "url": "http://www.bilibili.com/video/av116844484631808",
    "source": "chocpink_AI版",
    "platform": "bilibili",
    "points": 9382,
    "published_at": "2026-07-01T11:29:32+00:00",
    "summary": "我用3天 vibe coding出了我的第二个 App～\n总结了上次匆忙开始没有准备好 导致很多次来回调试和推翻重来的血泪经验，这次用AI vibe coding我的宗旨就是和AI打好配合，人工的部分重点放在了各种给AI的需求文档（虽然也是AI写的）～ 全流程AI来实现落地我只做掌控整体节奏、给AI提供素材/PRD和验收，并且验收通过率也是极高的，极大提高了AI开发可用性和我的效率！\n\n全程无代码"
  },
  {
    "id": "bvid:BV1DXTY6hEPv",
    "domain": "AI",
    "title": "Claude国内注册防封号：直接订阅Claude API｜Claude Pro/Max三种订阅方法，封号后如何退款？国内接码+微信支付开通，玩转Opus 4.8",
    "url": "http://www.bilibili.com/video/av116843108964309",
    "source": "Ai实测官",
    "platform": "bilibili",
    "points": 9336,
    "published_at": "2026-07-01T12:00:00+00:00",
    "summary": "Claude国内注册订阅全流程！接码、微信支付、防封号一条视频讲清楚，无需信用卡和美区ID。本期实测三种订阅方法（WildAI第三方/苹果礼品卡/Google Play），并独家对比封号后能否拿到官方退款——真金白银踩坑总结。\n直接订阅Claude 官方API才是防封号最好的方法。触发pro/max封号的机制在这里都不算数。\n新手也能跟着开通Claude Pro/Max，玩转Opus 4.8、Cl"
  },
  {
    "id": "bvid:BV16hTc6xEpF",
    "domain": "AI",
    "title": "【Codex实战】手摸手教你多Agent协同开发",
    "url": "http://www.bilibili.com/video/av116839870891259",
    "source": "路边爱吃瓜",
    "platform": "bilibili",
    "points": 9192,
    "published_at": "2026-06-30T16:00:22+00:00",
    "summary": "Codex多Agent协同开发"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 9155,
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
    "points": 8425,
    "published_at": "2025-06-04T07:08:58+00:00",
    "summary": "全程干货无废话！MCP最新实战教程，从环境部署、原理详解到项目实战，带你彻底吃透MCP！MCPServer开发，mcp开发，mcp教程，mcp项目 完整视频教程+讲解课件+学习笔记+AI大模型知识库已打包可分享！"
  },
  {
    "id": "bvid:BV1HhGo6aEvE",
    "domain": "AI",
    "title": "本地大模型也能联网搜索！LM Studio × MCP 接入教程",
    "url": "http://www.bilibili.com/video/av116635490911881",
    "source": "aopstudio",
    "platform": "bilibili",
    "points": 8047,
    "published_at": "2026-05-25T13:41:46+00:00",
    "summary": "本视频演示如何为 LM Studio 接入 MCP 联网搜索服务，让本地运行的大模型具备实时搜索网络的能力。\nMCP（Model Context Protocol）是 Anthropic 推出的开放协议，允许模型通过标准化接口调用外部工具。本次接入的搜索服务来自 MCPWorld，底层通过 npx 调用，无需额外部署服务端，配置完成后即可在 LM Studio 的对话界面中直接发起联网搜索。\n本视"
  },
  {
    "id": "bvid:BV1vcKS67Ee8",
    "domain": "AI",
    "title": "【AI Coding】这绝对是你看过讲的最好的Vibe Coding企业级项目实战，从入门到进阶，30分钟速通Claude Code✚Codex✚Cursor",
    "url": "http://www.bilibili.com/video/av116832321209292",
    "source": "图灵学院官方",
    "platform": "bilibili",
    "points": 6732,
    "published_at": "2026-06-29T08:02:48+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n【本视频笔记代码、大模型最新学习路线、系统学习课程、实战案例、电子书+问题解答等戳这里获取→https://www.bilibili.com/read/cv39576966/?jump_opus=1】"
  },
  {
    "id": "bvid:BV1vKTj6ZEZ1",
    "domain": "AI",
    "title": "Java AI Agent大模型开发，Spring AI+Spring AI Alibaba Agent+Skill，原理→框架→组件→调优→实战项目完整教程",
    "url": "http://www.bilibili.com/video/av116849819781343",
    "source": "java架构师徐庶",
    "platform": "bilibili",
    "points": 6618,
    "published_at": "2026-07-02T10:14:08+00:00",
    "summary": "这套视频是2026年Java后端转型AI Agent的完整闭环教程，不只教你调用大模型，更吃透Spring AI Alibaba底层架构与企业落地方案；学完既能搞定面试跳槽、拿到高薪AI岗，也能在现有公司落地智能客服、知识库、业务自动化等 AI项目!给大家整理了一份超全学习资料资料包含视频笔记+源码+面试题合集+简历模板+面试指导+Java+Al大模型全栈架构师学习路线图|职业规划领资料戳:htt"
  },
  {
    "id": "rss:https://www.eetimes.com/breakthrough-cnt-pellicles-deliver-66x-durability-and-sufficient-transmittance/",
    "domain": "AI 算力 / 半导体",
    "title": "Breakthrough CNT Pellicles Deliver 66x Durability and Sufficient Transmittance",
    "url": "https://www.eetimes.com/breakthrough-cnt-pellicles-deliver-66x-durability-and-sufficient-transmittance/",
    "source": "Lintec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T04:00:00+00:00",
    "summary": "Explore the latest breakthrough in CNT pellicles for EUV lithography: durability is up to 66 times higher, with less transmittance loss. The post Breakthrough CNT Pellicles Deliver 66x Durability and "
  },
  {
    "id": "rss:https://www.eetimes.com/inside-infineon-e5b-dresden-fab-virtual-fab-cloning-fast-tracked-the-launch/",
    "domain": "AI 算力 / 半导体",
    "title": "Inside Infineon’s €5B Dresden Fab: Virtual Fab Cloning Fast-Tracked the Launch",
    "url": "https://www.eetimes.com/inside-infineon-e5b-dresden-fab-virtual-fab-cloning-fast-tracked-the-launch/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T10:40:05+00:00",
    "summary": "At the opening of its Dresden smart power fab, Infineon’s COO said virtual fab cloning enabled delivery three months ahead of schedule. The post Inside Infineon&#8217;s €5B Dresden Fab: Virtual Fab Cl"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/get-an-rtx-3060-with-12-gb-of-vram-for-just-usd329-99-at-newegg-msi-ventus-2x-oc-model-back-in-stock-with-free-shipping",
    "domain": "AI 算力 / 半导体",
    "title": "Get an RTX 3060 with 12 GB of VRAM for just $329.99 at Newegg — MSI Ventus 2X OC model back in stock with free shipping",
    "url": "https://www.tomshardware.com/pc-components/get-an-rtx-3060-with-12-gb-of-vram-for-just-usd329-99-at-newegg-msi-ventus-2x-oc-model-back-in-stock-with-free-shipping",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T19:08:22+00:00",
    "summary": "Get an RTX 3060 with 12 GB of VRAM for just $329.99 at Newegg — MSI Ventus 2X OC model back in stock with free shipping"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/space/spacex-vaporizes-260-starlink-satellites-in-six-months-using-earths-atmosphere-new-environmental-concerns-emerge-over-burning-2-700-pound-orbital-data-centers-fcc-seeks-to-exempt-satellites-from-regulations",
    "domain": "AI 算力 / 半导体",
    "title": "SpaceX vaporizes 260 Starlink satellites in six months using Earth's atmosphere — new environmental concerns emerge over burning 2,700-pound orbital data centers, FCC seeks to exempt satellites from r",
    "url": "https://www.tomshardware.com/tech-industry/space/spacex-vaporizes-260-starlink-satellites-in-six-months-using-earths-atmosphere-new-environmental-concerns-emerge-over-burning-2-700-pound-orbital-data-centers-fcc-seeks-to-exempt-satellites-from-regulations",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T16:00:00+00:00",
    "summary": "SpaceX retired 260 Starlink satellites in six months, with hundreds more to follow, as debate grows over the atmospheric impact of satellite burn-ups."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/storage/rampocalyse-pricing-prompts-maker-to-construct-his-own-memory-using-ancient-apollo-era-tech-usb-drive-resurrects-hand-threaded-magnetic-core-memory-using-salvaged-russian-computer-parts",
    "domain": "AI 算力 / 半导体",
    "title": "RAMpocalyse pricing prompts maker to construct his own memory using ancient Apollo-era tech — USB drive resurrects hand-threaded magnetic core memory using salvaged Russian computer parts",
    "url": "https://www.tomshardware.com/pc-components/storage/rampocalyse-pricing-prompts-maker-to-construct-his-own-memory-using-ancient-apollo-era-tech-usb-drive-resurrects-hand-threaded-magnetic-core-memory-using-salvaged-russian-computer-parts",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T15:50:00+00:00",
    "summary": "DIYer shows how they made a handsome magnetic core memory USB drive using home CNC and 3D printing equipment. However, it isn't a homebrew answer to the AI-induced memory crisis with only 64 bits of d"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/germanys-1-5-million-project-to-build-the-worlds-largest-game-archive-collapses-after-funding-dries-up",
    "domain": "AI 算力 / 半导体",
    "title": "Germany's massive 60,000-game preservation project collapses after €1.5 million funding dries up — world's largest game archive was entirely publicly available, now abandoned just as Sony kills physic",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/germanys-1-5-million-project-to-build-the-worlds-largest-game-archive-collapses-after-funding-dries-up",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T15:37:27+00:00",
    "summary": "A German effort to assemble the world's largest publicly accessible video game archive is being wound down after roughly €1.5 million in public funding expired."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/reviewer-tests-rtx-4080m-desktop-graphics-card-powered-by-salvaged-laptop-silicon-performs-worse-than-slightly-more-expensive-rx-9070-gre-but-draws-only-100w-in-games",
    "domain": "AI 算力 / 半导体",
    "title": "Reviewer tests 'RTX 4080M' desktop graphics card powered by salvaged laptop silicon — performs worse than slightly more expensive RX 9070 GRE but draws only 100W in games",
    "url": "https://www.tomshardware.com/pc-components/gpus/reviewer-tests-rtx-4080m-desktop-graphics-card-powered-by-salvaged-laptop-silicon-performs-worse-than-slightly-more-expensive-rx-9070-gre-but-draws-only-100w-in-games",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T14:46:02+00:00",
    "summary": "Turns out, a modded RTX 4080M desktop GPU performs worse than similarly-priced official options. It currently costs roughly $400 in China and compared to the RX 9070 GRE, this custom card loses in eve"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/linux/hannah-montana-linux-gets-modern-remaster-after-nearly-two-decades-sweet-niblets-new-v26-is-built-on-debian-with-a-re-skin-of-kde-plasma",
    "domain": "AI 算力 / 半导体",
    "title": "Hannah Montana Linux gets modern remaster after nearly two decades — ‘Sweet niblets,’ new v26 is built on Debian with a re-skin of KDE Plasma",
    "url": "https://www.tomshardware.com/software/linux/hannah-montana-linux-gets-modern-remaster-after-nearly-two-decades-sweet-niblets-new-v26-is-built-on-debian-with-a-re-skin-of-kde-plasma",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T14:23:38+00:00",
    "summary": "Say whaaaat? Hannah Montana Linux is back. Basically abandonware since 2009, the distro has returned with a modern kernel and about 18 years worth of patches."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/us-navy-testing-3d-printed-fighter-jet-parts-for-quick-repairs-composite-parts-printed-at-forward-deployed-3d-printers-to-be-flight-tested-on-operational-f-a-18-super-hornets",
    "domain": "AI 算力 / 半导体",
    "title": "US Navy is flight-testing 3D printed fighter jet parts that cut repair times in half — forward-deployed 3D printers generate composite parts, flight testing to begin on operational F/A-18 Super Hornet",
    "url": "https://www.tomshardware.com/3d-printing/us-navy-testing-3d-printed-fighter-jet-parts-for-quick-repairs-composite-parts-printed-at-forward-deployed-3d-printers-to-be-flight-tested-on-operational-f-a-18-super-hornets",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T14:11:16+00:00",
    "summary": "The US Navy is experimenting with 3D-printed patches for composite parts, allowing forward bases to repair F/A-18 Super Hornets without waiting for replacement parts coming from the tail end of a logi"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/f1-25-2026-season-edition-gpu-benchmarks-from-pole-position-to-the-back-of-the-grid",
    "domain": "AI 算力 / 半导体",
    "title": "F1 25: 2026 Season Edition GPU benchmarks – From Pole Position to the Back of the Grid",
    "url": "https://www.tomshardware.com/pc-components/gpus/f1-25-2026-season-edition-gpu-benchmarks-from-pole-position-to-the-back-of-the-grid",
    "source": "Dan Mateescu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T14:05:19+00:00",
    "summary": "tktk"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/atomic-semi-rebrands-as-fab2-and-shifts-operations-to-texas",
    "domain": "AI 算力 / 半导体",
    "title": "Jim Keller's startup is building a factory to mass-produce small semiconductor fabs —Atomic Semi rebrands as 'Fab2' underlining intended role as a 'fab fab'",
    "url": "https://www.tomshardware.com/tech-industry/atomic-semi-rebrands-as-fab2-and-shifts-operations-to-texas",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T13:15:00+00:00",
    "summary": "Atomic Semi, the semiconductor tooling startup founded by chip architect Jim Keller and DIY fabrication pioneer Sam Zeloof, has rebranded as Fab2."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/lenovo-thinkpad-x1-carbon-gen-14-aura-edition-review",
    "domain": "AI 算力 / 半导体",
    "title": "Lenovo ThinkPad X1 Carbon Gen 14 Aura Edition review: A masterclass in mobility and usability",
    "url": "https://www.tomshardware.com/laptops/lenovo-thinkpad-x1-carbon-gen-14-aura-edition-review",
    "source": "Charles Jefferies",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T13:10:00+00:00",
    "summary": "A sublime ultraportable with world-class quality and OLED visuals, the ThinkPad X1 Carbon Gen 14 excels at everything it does."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows-11-identifier-used-to-track-scattered-spider-perp-after-microsoft-shared-info-with-fbi-19-year-old-us-estonian-hacker-arrested-over-alleged-ties-to-infamous-extortion-group",
    "domain": "AI 算力 / 半导体",
    "title": "Windows 11 identifier code used to track Scattered Spider perp after Microsoft shared info with FBI — 19-year-old US-Estonian hacker arrested over alleged ties to infamous extortion group",
    "url": "https://www.tomshardware.com/software/windows-11-identifier-used-to-track-scattered-spider-perp-after-microsoft-shared-info-with-fbi-19-year-old-us-estonian-hacker-arrested-over-alleged-ties-to-infamous-extortion-group",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T12:55:00+00:00",
    "summary": "Petet Stokes was arrested in Finland and extradited to the U.S. over alleged ties to the Scattered Spider group, with Microsoft helping in the investigation. He's in custody awaiting trial based on a "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/grab-this-rtx-5070-ti-oled-gaming-laptop-at-usd300-off-acer-predator-helios-neo-16s-ai-drops-to-usd1-899-99",
    "domain": "AI 算力 / 半导体",
    "title": "Grab this RTX 5070 Ti OLED gaming laptop at $300 off — Acer Predator Helios Neo 16S AI drops to $1,899.99",
    "url": "https://www.tomshardware.com/pc-components/grab-this-rtx-5070-ti-oled-gaming-laptop-at-usd300-off-acer-predator-helios-neo-16s-ai-drops-to-usd1-899-99",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T12:38:55+00:00",
    "summary": "The Acer Predator Helios Neo 16S AI combines an OLED 240 Hz display, Intel's Core Ultra 9 275HX, RTX 5070 Ti graphics, and 32GB of DDR5 memory, all while saving you $300 off its regular price."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/alibaba-bans-anthropics-claude-code-after-an-alleged-hidden-china-detection-backdoor-is-uncovered-employees-told-to-switch-to-qoder-as-the-rift-between-the-firms-widens",
    "domain": "AI 算力 / 半导体",
    "title": "Alibaba bans Anthropic's Claude Code after an alleged hidden China-detection backdoor is uncovered — employees told to switch to Qoder as the rift between the firms widens",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/alibaba-bans-anthropics-claude-code-after-an-alleged-hidden-china-detection-backdoor-is-uncovered-employees-told-to-switch-to-qoder-as-the-rift-between-the-firms-widens",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T12:20:00+00:00",
    "summary": "Alibaba banned Claude Code after an alleged hidden China-detection code was found, prompting staff to switch to Qoder as its feud with Anthropic deepens."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-keyboards/turtle-beach-command-series-kb7-review",
    "domain": "AI 算力 / 半导体",
    "title": "Turtle Beach Command Series KB7 Review: A keyboard with a touchscreen and a lot of potential",
    "url": "https://www.tomshardware.com/peripherals/gaming-keyboards/turtle-beach-command-series-kb7-review",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T12:10:00+00:00",
    "summary": "Turtle Beach's new \"Command Series\" KB7 TKL keyboard features a 4.3-inch touchscreen instead of the typical navigation cluster — like a Stream Deck, but as a touchscreen. Unfortunately, it lacks the s"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/ps5-disc-drive-purchase-cap-predates-sonys-disc-cutoff",
    "domain": "AI 算力 / 半导体",
    "title": "PS5 Disc Drive purchase cap predates Sony's disc cutoff — 'high demand' order limit has been on the store page since at least March 2025",
    "url": "https://www.tomshardware.com/video-games/playstation/ps5-disc-drive-purchase-cap-predates-sonys-disc-cutoff",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T12:00:00+00:00",
    "summary": "Meanwhile, the largest petition against the disc cutoff sat beyond 74,000 signatures on the morning of July 4th, closing in on its 75,000 goal."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/you-can-now-play-half-life-2-right-inside-your-browser-at-over-100-fps-with-save-states-and-console-support-ingenious-port-recreates-the-entire-game-campaign-using-webgl-2",
    "domain": "AI 算力 / 半导体",
    "title": "You can now play Half-Life 2 right inside your browser at over 100 FPS with save states & console support — Ingenious port recreates the entire game campaign using WebGL 2",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/you-can-now-play-half-life-2-right-inside-your-browser-at-over-100-fps-with-save-states-and-console-support-ingenious-port-recreates-the-entire-game-campaign-using-webgl-2",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T11:40:00+00:00",
    "summary": "An unofficial browser port of Half-Life 2 has popped up online, allowing you to play the original campaign without downloading anything. Developed in just three months by Slqnt and 98006, it even feat"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/fill-your-steam-library-without-spending-a-single-dime-scratch-your-shopping-itch-with-the-steam-summer-sale-simulator",
    "domain": "AI 算力 / 半导体",
    "title": "Fill your Steam library without spending a single dime — scratch your shopping itch with the Steam Summer Sale Simulator",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/fill-your-steam-library-without-spending-a-single-dime-scratch-your-shopping-itch-with-the-steam-summer-sale-simulator",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T11:20:00+00:00",
    "summary": "This website lets you \"buy\" all the Steam games you want without spending anything at all. It was primarily made for the dopamine hit, but the Achievements page is quite engaging, too."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/darpa-plans-30-year-endurance-nuclear-waste-batteries-to-power-next-gen-drones-says-report-project-symphonee-aims-to-harvest-strontium-90-to-power-persistent-military-drones",
    "domain": "AI 算力 / 半导体",
    "title": "DARPA plans 30-year endurance nuclear waste batteries to power next-gen drones, says report — project SYMPHONEE aims to harvest Strontium-90 to power persistent military drones",
    "url": "https://www.tomshardware.com/tech-industry/drones/darpa-plans-30-year-endurance-nuclear-waste-batteries-to-power-next-gen-drones-says-report-project-symphonee-aims-to-harvest-strontium-90-to-power-persistent-military-drones",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T10:49:55+00:00",
    "summary": "A report suggests that upcoming nuclear waste-powered radiovoltaic batteries could last as long as 30 years and power next-gen drones."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/50-feet-long-fiber-optic-hdmi-cable-and-steam-controller-2-is-enthusiasts-answer-to-the-steam-machine-dismisses-valves-new-console-for-a-diy-bazzite-setup-with-a-controller",
    "domain": "AI 算力 / 半导体",
    "title": "50-feet-long fiber optic HDMI cable and Steam Controller 2 is enthusiasts' answer to the Steam Machine — dismisses Valve's new console for a DIY Bazzite setup with a controller",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/50-feet-long-fiber-optic-hdmi-cable-and-steam-controller-2-is-enthusiasts-answer-to-the-steam-machine-dismisses-valves-new-console-for-a-diy-bazzite-setup-with-a-controller",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T16:58:51+00:00",
    "summary": "An enthusiast is DIYing his own Steam Machine through ancient, lost methods known as cables that turn his existing PC into the perfect couch gaming setup. As expected, the Steam Controller 2 is also i"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/console-gaming/sony-crammed-an-entire-ps1-into-a-dualshock-controller-that-connects-to-your-tv-but-killed-the-project-playstation-puga-offered-game-studios-a-mere-10-cents-per-unit-sold",
    "domain": "AI 算力 / 半导体",
    "title": "Sony crammed an entire PS1 into a DualShock controller that connects to your TV, but killed the project — PlayStation Puga offered game studios a mere 10 cents per unit sold",
    "url": "https://www.tomshardware.com/video-games/console-gaming/sony-crammed-an-entire-ps1-into-a-dualshock-controller-that-connects-to-your-tv-but-killed-the-project-playstation-puga-offered-game-studios-a-mere-10-cents-per-unit-sold",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T15:16:24+00:00",
    "summary": "Sony successfully built a PlayStation 1 console that fit inside a controller but had to cancel the project after game studios were unhappy with the royalties they would make from the project."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/chinese-ymtc-ssds-make-their-way-into-retail-lenovo-laptops-media-outlet-slams-ymtc-pcie-4-0-drive-for-below-average-for-an-ssd-in-an-office-laptop-in-review",
    "domain": "AI 算力 / 半导体",
    "title": "Chinese YMTC SSDs make their way into retail Lenovo laptops — media outlet slams YMTC PCIe 4.0 drive for 'below average for an SSD in an office laptop' in review",
    "url": "https://www.tomshardware.com/pc-components/ssds/chinese-ymtc-ssds-make-their-way-into-retail-lenovo-laptops-media-outlet-slams-ymtc-pcie-4-0-drive-for-below-average-for-an-ssd-in-an-office-laptop-in-review",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T15:07:08+00:00",
    "summary": "Lenovo has seemingly begun using YMTC SSDs in some of its laptop models, allowing the Chinese storage chip company to gain a foothold in the U.S. This is despite its inclusion on the U.S. Department o"
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/get-a-premium-27-inch-1440p-240-hz-oled-gaming-monitor-for-only-usd349-oled-for-the-price-of-ips",
    "domain": "AI 算力 / 半导体",
    "title": "Get a premium 27-inch 1440p 240 Hz OLED gaming monitor for only $349 — OLED for the price of IPS",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/get-a-premium-27-inch-1440p-240-hz-oled-gaming-monitor-for-only-usd349-oled-for-the-price-of-ips",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T14:16:28+00:00",
    "summary": "If you've been meaning to upgrade to an OLED monitor but budget options scare you off because of burn-in, Asus has the answer for you. Not only does this monitor feature great specs, but it also has a"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/cheyenne-suspends-data-center-fill-and-flush-and-closed-loop-discharges-after-meta-contractor-contaminated-its-reuse-water-system",
    "domain": "AI 算力 / 半导体",
    "title": "Meta data center water discharges suspended after contaminating the city's reclamation water supply with bacterium — system offline for months for cleaning, closed-loop cooling system purge spread rar",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/cheyenne-suspends-data-center-fill-and-flush-and-closed-loop-discharges-after-meta-contractor-contaminated-its-reuse-water-system",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T14:02:22+00:00",
    "summary": "Fill-and-flush is a commissioning step whereby crews fill a cooling loop's piping with water and flush it to clear debris before the system is run."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/aoc-u27g4xm-27-inch-4k-160-hz-dual-refresh-gaming-monitor-review",
    "domain": "AI 算力 / 半导体",
    "title": "AOC U27G4XM 27-inch 4K 160 Hz Dual-Refresh Gaming Monitor Review: Speed, Flexibility And Value",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/aoc-u27g4xm-27-inch-4k-160-hz-dual-refresh-gaming-monitor-review",
    "source": "Christian Eberle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T13:17:31+00:00",
    "summary": "AOC brings speed, flexibility, and value in its U27G4XM. It’s a 27-inch dual-mode IPS panel with 4K resolution at 160 Hz, FHD resolution at 320 Hz and Adaptive-Sync. It also has a Mini LED backlight w"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/memory-price-surge-begins-to-cool-as-consumers-hit-affordability-limit-ai-demand-still-keeps-dram-and-nand-prices-climbing-through-q3-2026",
    "domain": "AI 算力 / 半导体",
    "title": "Memory price surge begins to cool as consumers hit affordability limit — AI demand still keeps DRAM and NAND prices climbing through Q3 2026",
    "url": "https://www.tomshardware.com/pc-components/ram/memory-price-surge-begins-to-cool-as-consumers-hit-affordability-limit-ai-demand-still-keeps-dram-and-nand-prices-climbing-through-q3-2026",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T11:47:34+00:00",
    "summary": "TrendForce says DRAM and NAND prices will continue to rise through Q3 2026, but AI-driven gains are slowing as PC and smartphone makers reach their affordability limits."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/the-ultimate-4k-rtx-5090-gaming-titan-plummets-usd2-580-huge-discount-makes-the-alienware-area-51-with-24-core-cpu-and-64gb-ram-irresistible",
    "domain": "AI 算力 / 半导体",
    "title": "The ultimate 4K RTX 5090 gaming titan plummets $2,580 — huge discount makes the Alienware Area-51 with 24-core CPU and 64GB RAM irresistible",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/the-ultimate-4k-rtx-5090-gaming-titan-plummets-usd2-580-huge-discount-makes-the-alienware-area-51-with-24-core-cpu-and-64gb-ram-irresistible",
    "source": "Sponsored",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T11:43:13+00:00",
    "summary": "Dell has slashed the price of the Alienware Area-51 with a Core Ultra 9 285K, GeForce RTX 5090, and 64GB of DDR5 RAM by $2,580."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cooling/windows-guru-uses-stirling-engine-to-cool-amd-threadripper-3970x-waste-heat-energy-spins-the-engines-flywheel",
    "domain": "AI 算力 / 半导体",
    "title": "Windows guru uses 19th-century Stirling Engine tech for auxiliary cooling on AMD Threadripper 3970X system — waste heat energy spins the $40 engine's flywheel",
    "url": "https://www.tomshardware.com/pc-components/cooling/windows-guru-uses-stirling-engine-to-cool-amd-threadripper-3970x-waste-heat-energy-spins-the-engines-flywheel",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T11:30:00+00:00",
    "summary": "Windows development guru Dave W. Plummer shared a brief video demonstrating a novel Stirling Engine powered cooling solution for his AMD Threadripper chipset."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/enthusiast-hides-gaming-pc-inside-living-room-fan-using-3d-printed-parts-disassembled-atomman-g7-cooled-by-dreo-tower-fan-that-shifts-air-at-28-feet-per-second",
    "domain": "AI 算力 / 半导体",
    "title": "Enthusiast hides gaming PC inside living room fan using 3D-printed parts — disassembled AtomMan G7 cooled by Dreo tower fan that shifts air at 28 feet per second",
    "url": "https://www.tomshardware.com/3d-printing/enthusiast-hides-gaming-pc-inside-living-room-fan-using-3d-printed-parts-disassembled-atomman-g7-cooled-by-dreo-tower-fan-that-shifts-air-at-28-feet-per-second",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T11:00:00+00:00",
    "summary": "Creator Zac Builds mounted their mini-PC to the side of their living room fan to hide it plain sight."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/startup-unveils-3d-printed-nuclear-reactor-module-to-power-ai-data-centers-touted-as-the-worlds-first-subcritical-solid-state-factory-built-thorium-nuclear-reactor",
    "domain": "AI 算力 / 半导体",
    "title": "Startup unveils 3D-printed nuclear reactor module to power AI data centers —touted as ‘the world’s first subcritical, solid-state, factory-built thorium nuclear reactor’",
    "url": "https://www.tomshardware.com/3d-printing/startup-unveils-3d-printed-nuclear-reactor-module-to-power-ai-data-centers-touted-as-the-worlds-first-subcritical-solid-state-factory-built-thorium-nuclear-reactor",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T11:00:00+00:00",
    "summary": "Nuclear tech startup Ampera revealed a small modular reactor manufactured using 3D printing techniques. The company says that it expects to be the first one to mass produce these power sources for dat"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/companies-join-hands-to-collectively-dunk-on-playstations-all-digital-future-dominos-pizza-kfc-and-gamesir-all-threaten-an-end-to-physical-production",
    "domain": "AI 算力 / 半导体",
    "title": "Companies join hands to collectively dunk on PlayStation's all-digital future — Domino's pizza, KFC, and GameSir all threaten an end to physical production",
    "url": "https://www.tomshardware.com/tech-industry/companies-join-hands-to-collectively-dunk-on-playstations-all-digital-future-dominos-pizza-kfc-and-gamesir-all-threaten-an-end-to-physical-production",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T10:00:00+00:00",
    "summary": "Companies on social media are coming together to mock Sony's decision of ceasing production of physical discs for PlayStation games. These brands are shifting to a digital-only model in an even more a"
  },
  {
    "id": "rss:https://www.eetimes.com/sk-hynix-plans-713b-domestic-investment/",
    "domain": "AI 算力 / 半导体",
    "title": "SK Hynix Plans $713B Domestic Investment",
    "url": "https://www.eetimes.com/sk-hynix-plans-713b-domestic-investment/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T13:57:51+00:00",
    "summary": "SK Hynix is set to invest $713 billion to expand its semiconductor manufacturing capacity in South Korea and plans a Nasdaq listing. The post SK Hynix Plans $713B Domestic Investment appeared first on"
  },
  {
    "id": "rss:https://www.eetimes.com/spains-semiconductor-landscape-six-stories-from-a-growing-ecosystem/",
    "domain": "AI 算力 / 半导体",
    "title": "Spain’s Semiconductor Landscape: Six Stories from a Growing Ecosystem",
    "url": "https://www.eetimes.com/spains-semiconductor-landscape-six-stories-from-a-growing-ecosystem/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T07:10:19+00:00",
    "summary": "EE Times examines the companies, institutes, and policy initiatives positioning Spain within Europe’s next wave of semiconductor innovation. The post Spain’s Semiconductor Landscape: Six Stories from "
  },
  {
    "id": "rss:https://www.eetimes.com/turkey-needs-to-make-its-own-chips-not-just-design-them/",
    "domain": "AI 算力 / 半导体",
    "title": "Turkey Needs to Make Its Own Chips, Not Just Design Them",
    "url": "https://www.eetimes.com/turkey-needs-to-make-its-own-chips-not-just-design-them/",
    "source": "Oğuz Ergin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T12:42:59+00:00",
    "summary": "Turkey has built a strong chip design base, but without domestic manufacturing, its semiconductor sovereignty remains on loan. The post Turkey Needs to Make Its Own Chips, Not Just Design Them appeare"
  },
  {
    "id": "rss:https://www.eetimes.com/opensearch-powers-ai-data-infrastructure-as-agentic-workloads-scale/",
    "domain": "AI 算力 / 半导体",
    "title": "OpenSearch Powers AI Data Infrastructure as Agentic Workloads Scale",
    "url": "https://www.eetimes.com/opensearch-powers-ai-data-infrastructure-as-agentic-workloads-scale/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T07:40:09+00:00",
    "summary": "OpenSearch turns AI’s data deluge into hybrid search, observability, and agent monitoring while avoiding vendor lock-in. The post OpenSearch Powers AI Data Infrastructure as Agentic Workloads Scale ap"
  },
  {
    "id": "rss:https://www.eetimes.com/engineering-heterogeneity-at-scale/",
    "domain": "AI 算力 / 半导体",
    "title": "Engineering Heterogeneity at Scale",
    "url": "https://www.eetimes.com/engineering-heterogeneity-at-scale/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T20:49:24+00:00",
    "summary": "AI has outgrown traditional chips. The future belongs to integrated systems that stack compute, memory, photonics, and power, and HLSI is driving the shift. The post Engineering Heterogeneity at Scale"
  },
  {
    "id": "rss:https://www.eetimes.com/design-of-a-single-pair-ethernet-system-with-power-over-data-lines-spoe/",
    "domain": "AI 算力 / 半导体",
    "title": "Design of a Single Pair Ethernet System with Power over Data Lines (SPoE)",
    "url": "https://www.eetimes.com/design-of-a-single-pair-ethernet-system-with-power-over-data-lines-spoe/",
    "source": "Dr.-Ing. Heinz Zenkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T14:00:00+00:00",
    "summary": "Single Pair Ethernet is becoming increasingly popular in industrial networking due to the simplified cabling with just one twisted pair of wires. If power is also supplied via this, the SPE transmissi"
  },
  {
    "id": "rss:https://www.eetimes.com/oxmiq-raises-35m-for-gpu-ip-expands-focus-to-data-center-design/",
    "domain": "AI 算力 / 半导体",
    "title": "Oxmiq Raises $35M for GPU IP, Expands Focus to Data Center Design",
    "url": "https://www.eetimes.com/oxmiq-raises-35m-for-gpu-ip-expands-focus-to-data-center-design/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T13:15:00+00:00",
    "summary": "OxCore GPU IP is up and running on FPGA today, CEO Raja Koduri told EE Times. The post Oxmiq Raises $35M for GPU IP, Expands Focus to Data Center Design appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/rapid-component-obsolescence-is-reshaping-todays-semiconductor-procurement-dynamics/",
    "domain": "AI 算力 / 半导体",
    "title": "Rapid Component Obsolescence Is Reshaping Today’s Semiconductor Procurement Dynamics",
    "url": "https://www.eetimes.com/rapid-component-obsolescence-is-reshaping-todays-semiconductor-procurement-dynamics/",
    "source": "Landyn Murphy, Senior Content Marketing Specialist, Rochester Electronics",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T13:00:00+00:00",
    "summary": "Today’s semiconductor component&#160;landscape is more complex than ever. Obsolescence has shifted from an occasional disruption to a persistent operational risk. As product lifecycles shorten and sup"
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
    "id": "rss:https://semianalysis.com/2025/09/03/amazons-ai-resurgence-aws-anthropics-multi-gigawatt-trainium-expansion/",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon’s AI Resurgence: AWS & Anthropic’s Multi-Gigawatt Trainium Expansion",
    "url": "https://semianalysis.com/2025/09/03/amazons-ai-resurgence-aws-anthropics-multi-gigawatt-trainium-expansion/",
    "source": "Jeremie Eliahou Ontiveros",
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
    "source": "Dylan Patel",
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
    "source": "Doug OLaughlin",
    "platform": "rss",
    "points": null,
    "published_at": "2025-08-13T00:27:14+00:00",
    "summary": "To many power users (Pro and Plus), GPT5 was a disappointing release. But with closer inspection, the real release is focused on the vast majority of ChatGPT’s users, which is the 700m+ free userbase "
  },
  {
    "id": "rss:https://semianalysis.com/2025/08/12/scaling-the-memory-wall-the-rise-and-roadmap-of-hbm/",
    "domain": "AI 算力 / 半导体",
    "title": "Scaling the Memory Wall: The Rise and Roadmap of HBM",
    "url": "https://semianalysis.com/2025/08/12/scaling-the-memory-wall-the-rise-and-roadmap-of-hbm/",
    "source": "Dylan Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2025-08-12T01:16:06+00:00",
    "summary": "The first portion of this report will explain HBM, the manufacturing process, dynamics between vendors, KVCache offload, disaggregated prefill decode, and wide / high-rank EP. The rest of the report w"
  },
  {
    "id": "rss:https://semianalysis.com/2025/07/30/robotics-levels-of-autonomy/",
    "domain": "AI 算力 / 半导体",
    "title": "Robotics Levels of Autonomy",
    "url": "https://semianalysis.com/2025/07/30/robotics-levels-of-autonomy/",
    "source": "Reyk Knuhtsen",
    "platform": "rss",
    "points": null,
    "published_at": "2025-07-30T17:02:25+00:00",
    "summary": "Robots have powered manufacturing for decades, yet they stayed single-purpose and thrived only in perfect settings. Previous attempts at intelligent machines overpromised and underdelivered. But they "
  },
  {
    "id": "rss:https://semianalysis.com/2025/07/21/vlsi2025/",
    "domain": "AI 算力 / 半导体",
    "title": "Intel 18A Details & Cost, Future of DRAM 4F2 vs 3D, Backside Power Adoption (or Not), China’s FlipFET, Digital Twins from Atoms to Fabs, and More",
    "url": "https://semianalysis.com/2025/07/21/vlsi2025/",
    "source": "Dylan Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2025-07-21T14:23:37+00:00",
    "summary": "Long time readers will recall that SemiAnalysis covers more than just datacenters and AMD. Today we’re back to semiconductors with a tech-focused roundup of the best from this year’s VLSI conference, "
  },
  {
    "id": "rss:https://semianalysis.com/2025/07/11/meta-superintelligence-leadership-compute-talent-and-data/",
    "domain": "AI 算力 / 半导体",
    "title": "Meta Superintelligence – Leadership Compute, Talent, and Data",
    "url": "https://semianalysis.com/2025/07/11/meta-superintelligence-leadership-compute-talent-and-data/",
    "source": "Dylan Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2025-07-11T20:12:19+00:00",
    "summary": "Meta’s shocking purchase of 49% of Scale AI at a ~$30B valuation shows that money is of no concern for the $100B annual cashflow ad machine. Despite seemingly unlimited resources, Meta has been fallin"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/961505/wealthy-ai-schools-alpha-forge-prep",
    "domain": "大厂 AI 动态",
    "title": "Some of the nation’s rich are letting AI teach their kids",
    "url": "https://www.theverge.com/ai-artificial-intelligence/961505/wealthy-ai-schools-alpha-forge-prep",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T22:30:54+00:00",
    "summary": "Most Americans don't trust AI. It's proven that it doesn't know what safe toppings for pizza are. People don't even want to listen to AI music. But none of that matters for some of America's wealthy, "
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/961484/mr-lif-emergency-rations-ep-post-9-11-review",
    "domain": "大厂 AI 动态",
    "title": "Mr. Lif’s Emergency Rations EP is post-9/11 hip hop at its most daring",
    "url": "https://www.theverge.com/entertainment/961484/mr-lif-emergency-rations-ep-post-9-11-review",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T18:30:00+00:00",
    "summary": "There was a period in the early aughts when Definitive Jux (nee: Def Jux) seemed like it was going to be the future of hip hop. While the label featured plenty of experimental, boundary-pushing, and p"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/960838/grand-theft-auto-gta-6-vi-preorder-editions-buy",
    "domain": "大厂 AI 动态",
    "title": "Where to preorder Grand Theft Auto VI",
    "url": "https://www.theverge.com/gadgets/960838/grand-theft-auto-gta-6-vi-preorder-editions-buy",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T16:00:00+00:00",
    "summary": "Rockstar's long-awaited Grand Theft Auto VI is launching November 19th, 2026 for PlayStation 5 and Xbox Series S/X consoles. The game will be available digitally at launch, with physical cases contain"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/961468/google-ai-commercial-founding-fathers-declaration-of-independence",
    "domain": "大厂 AI 动态",
    "title": "Infuriating Google commercial imagines the founding fathers embracing AI",
    "url": "https://www.theverge.com/ai-artificial-intelligence/961468/google-ai-commercial-founding-fathers-declaration-of-independence",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T14:23:11+00:00",
    "summary": "\"Group project, but make it 1776.\" That's how a new commercial for Google Workspace opens. And things only get cringier from there. The clip imagines what it would be like if the founding fathers turn"
  },
  {
    "id": "rss:https://www.theverge.com/tech/959604/sourdough-sidekick-review-king-arthur-starter",
    "domain": "大厂 AI 动态",
    "title": "The Sourdough Sidekick automates the boring bit of baking",
    "url": "https://www.theverge.com/tech/959604/sourdough-sidekick-review-king-arthur-starter",
    "source": "Dominic Preston",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T14:00:00+00:00",
    "summary": "Baking sourdough bread is inherently old-fashioned, relying on natural fermentation and wild yeast instead of the simple, predictable commercial stuff. So it might sound anathema to bring a gadget int"
  },
  {
    "id": "rss:https://www.theverge.com/podcast/961470/keurig-coffee-k-up-version-history",
    "domain": "大厂 AI 动态",
    "title": "How Keurig saved — and ruined — your coffee",
    "url": "https://www.theverge.com/podcast/961470/keurig-coffee-k-up-version-history",
    "source": "David Pierce",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T13:51:56+00:00",
    "summary": "Before Keurig, the coffee in your office was almost certainly terrible. Old, burned, made by someone who would rather poorly eyeball than properly measure. Just altogether gross. After Keurig? You cou"
  },
  {
    "id": "rss:https://www.theverge.com/tech/960916/vizio-mini-led-quantum-tv-review",
    "domain": "大厂 AI 动态",
    "title": "Vizio accidentally made the best dumb TV on the market",
    "url": "https://www.theverge.com/tech/960916/vizio-mini-led-quantum-tv-review",
    "source": "John.Higgins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T13:00:00+00:00",
    "summary": "When I first started testing Vizio's 65-inch Mini LED Quantum TV, I thought the big story was that Vizio was back and that it had a quantum-dot TV for under $398 - the cheapest on the market. Vizio's "
  },
  {
    "id": "rss:https://www.theverge.com/column/960600/xbox-is-a-disaster",
    "domain": "大厂 AI 动态",
    "title": "Xbox is a disaster",
    "url": "https://www.theverge.com/column/960600/xbox-is-a-disaster",
    "source": "Andrew Webster",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T12:00:00+00:00",
    "summary": "This is The Stepback, a weekly newsletter breaking down one essential story from the tech world. For more on the bleak state of the video game industry, follow Andrew Webster. The Stepback arrives in "
  },
  {
    "id": "rss:https://www.theverge.com/science/961459/nasa-emergency-save-swift-observatory-katalyst-space-technologies",
    "domain": "大厂 AI 动态",
    "title": "NASA launched an emergency mission to stop the Swift Observatory from crashing to Earth",
    "url": "https://www.theverge.com/science/961459/nasa-emergency-save-swift-observatory-katalyst-space-technologies",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T19:06:27+00:00",
    "summary": "The Swift Observatory was launched in 2004, but recent solar storms have pushed its orbit lower, and it's in danger of burning up in Earth's atmosphere as soon as this year. To try and stave off its d"
  },
  {
    "id": "rss:https://www.theverge.com/policy/961449/white-house-mamdani-heatwave-deletion",
    "domain": "大厂 AI 动态",
    "title": "White House deletes thousands of web pages about energy conservation as heatwave slams US",
    "url": "https://www.theverge.com/policy/961449/white-house-mamdani-heatwave-deletion",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T16:19:06+00:00",
    "summary": "The US Department of Energy reportedly deleted about 6,000 pages related to energy conservation as a historic heatwave tears across the country. The deletion was suspiciously timed, following Republic"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/05/this-humanoid-robotics-company-is-going-public-but-its-ceo-isnt-promising-a-robot-in-your-home-anytime-soon/",
    "domain": "大厂 AI 动态",
    "title": "This humanoid robotics company is going public, but its CEO isn’t promising a robot in your home anytime soon",
    "url": "https://techcrunch.com/2026/07/05/this-humanoid-robotics-company-is-going-public-but-its-ceo-isnt-promising-a-robot-in-your-home-anytime-soon/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T06:05:29+00:00",
    "summary": "While other humanoid startups chase sky-high valuations, Agility Robotics is betting its future on execution — and a SPAC."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/05/ubers-european-expansion-plans-may-have-hit-a-speed-bump/",
    "domain": "大厂 AI 动态",
    "title": "Uber’s European expansion plans may have hit a speed bump",
    "url": "https://techcrunch.com/2026/07/05/ubers-european-expansion-plans-may-have-hit-a-speed-bump/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T21:35:17+00:00",
    "summary": "Back in February, Uber announced ambitious plans to launch in seven new European markets in 2026 — but now five of those launches are reportedly on hold."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/05/trump-memecoin-investors-lost-3-8-billion-analysis-finds/",
    "domain": "大厂 AI 动态",
    "title": "Trump memecoin investors lost $3.8 billion, analysis finds",
    "url": "https://techcrunch.com/2026/07/05/trump-memecoin-investors-lost-3-8-billion-analysis-finds/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T20:29:05+00:00",
    "summary": "Nearly 1 million people have lost a total of $3.8 billion after buying President Donald Trump’s $TRUMP memecoin, while Trump made $636 million."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/05/amazon-will-stop-accepting-new-customers-for-mechanical-turk/",
    "domain": "大厂 AI 动态",
    "title": "Amazon will stop accepting new customers for Mechanical Turk",
    "url": "https://techcrunch.com/2026/07/05/amazon-will-stop-accepting-new-customers-for-mechanical-turk/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T17:43:36+00:00",
    "summary": "These may be the last days of Amazon’s Mechanical Turk."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/05/5-desk-gadgets-that-can-make-your-workday-better/",
    "domain": "大厂 AI 动态",
    "title": "5 desk gadgets that can make your workday better",
    "url": "https://techcrunch.com/2026/07/05/5-desk-gadgets-that-can-make-your-workday-better/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T15:00:00+00:00",
    "summary": "The right desk gadgets can help you reduce clutter, stay focused, and add a little extra convenience to your day."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/05/what-is-bending-spoons-everything-to-know-about-aols-acquirer/",
    "domain": "大厂 AI 动态",
    "title": "What is Bending Spoons? The little-known AOL and Vimeo owner that’s now public",
    "url": "https://techcrunch.com/2026/07/05/what-is-bending-spoons-everything-to-know-about-aols-acquirer/",
    "source": "Anna Heim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T13:33:32+00:00",
    "summary": "Bending Spoons remains largely unknown, even as its portfolio of products has served more than a billion people."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/05/almost-40-new-unicorns-have-been-minted-so-far-this-year-here-they-are/",
    "domain": "大厂 AI 动态",
    "title": "Almost 90 new unicorns have been minted so far this year — here they are",
    "url": "https://techcrunch.com/2026/07/05/almost-40-new-unicorns-have-been-minted-so-far-this-year-here-they-are/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T12:47:39+00:00",
    "summary": "With AI igniting an investor frenzy, more startups are achieving unicorn status every month."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/04/new-google-commercial-imagines-a-declaration-of-independence-written-with-help-from-ai/",
    "domain": "大厂 AI 动态",
    "title": "New Google commercial imagines a Declaration of Independence written with help from AI",
    "url": "https://techcrunch.com/2026/07/04/new-google-commercial-imagines-a-declaration-of-independence-written-with-help-from-ai/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T20:55:25+00:00",
    "summary": "Two hundred and fifty years after the signing of the Declaration of Independence, a new commercial asks: What if the Founding Fathers had access to Google Workspace?"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/04/midjourney-wants-hollywood-studios-to-reveal-the-details-of-their-ai-usage/",
    "domain": "大厂 AI 动态",
    "title": "Midjourney wants Hollywood studios to reveal the details of their AI usage",
    "url": "https://techcrunch.com/2026/07/04/midjourney-wants-hollywood-studios-to-reveal-the-details-of-their-ai-usage/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T18:00:05+00:00",
    "summary": "As part of an ongoing legal dispute with three Hollywood studios, Midjourney is seeking to compel those studios to reveal how they use AI themselves."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/04/alibaba-reportedly-bans-employees-from-using-claude-code/",
    "domain": "大厂 AI 动态",
    "title": "Alibaba reportedly bans employees from using Claude Code",
    "url": "https://techcrunch.com/2026/07/04/alibaba-reportedly-bans-employees-from-using-claude-code/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T16:32:08+00:00",
    "summary": "Alibaba has reportedly classified Claude Code as high-risk software."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/04/what-is-mistral-ai-everything-to-know-about-the-openai-competitor/",
    "domain": "大厂 AI 动态",
    "title": "What is Mistral AI? Everything to know about the OpenAI competitor",
    "url": "https://techcrunch.com/2026/07/04/what-is-mistral-ai-everything-to-know-about-the-openai-competitor/",
    "source": "Anna Heim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T15:51:32+00:00",
    "summary": "Mistral AI, which offers some open source AI models, has raised significant funding since its creation in 2023, with the ambition to “put frontier AI in the hands of everyone.”"
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/chemical-accidents-rise-as-trump-administration-proposes-weakening-safety-rules/",
    "domain": "大厂 AI 动态",
    "title": "Chemical accidents rise as Trump administration proposes weakening safety rules",
    "url": "https://arstechnica.com/science/2026/07/chemical-accidents-rise-as-trump-administration-proposes-weakening-safety-rules/",
    "source": "Liza Gross, Inside Climate News",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T11:05:22+00:00",
    "summary": "Chemicals from accidents that injured or killed people increased by nearly 50 percent in recent years."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/the-missing-500-million-cosmic-bombardment-melted-earths-first-crust/",
    "domain": "大厂 AI 动态",
    "title": "The missing 500 million: Cosmic bombardment melted Earth's first crust",
    "url": "https://arstechnica.com/science/2026/07/the-missing-500-million-cosmic-bombardment-melted-earths-first-crust/",
    "source": "Jacek Krywko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T10:55:02+00:00",
    "summary": "The heat of the Hadean may have come from impacts as well as the interior."
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/07/review-supergirl-is-not-the-disaster-its-low-box-office-suggests/",
    "domain": "大厂 AI 动态",
    "title": "Review: Supergirl is not the disaster its low box office suggests",
    "url": "https://arstechnica.com/culture/2026/07/review-supergirl-is-not-the-disaster-its-low-box-office-suggests/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T16:49:14+00:00",
    "summary": "It’s a pretty good movie, but it needed to be a great movie to thrive in an oversaturated superhero market."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/when-the-ability-to-smell-goes-away/",
    "domain": "大厂 AI 动态",
    "title": "When the ability to smell goes away",
    "url": "https://arstechnica.com/science/2026/07/when-the-ability-to-smell-goes-away/",
    "source": "Victoria Clayton, Knowable Magazine",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T11:04:31+00:00",
    "summary": "Disturbances in this critical sense are often linked to problems with brain health."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/a-martian-rock-has-lots-of-carbon-on-it-and-its-not-clear-why/",
    "domain": "大厂 AI 动态",
    "title": "A martian rock has lots of carbon on it, and it's not clear why",
    "url": "https://arstechnica.com/science/2026/07/a-martian-rock-has-lots-of-carbon-on-it-and-its-not-clear-why/",
    "source": "Jacek Krywko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T11:00:41+00:00",
    "summary": "Biology could explain the find, but there are other potential explanations."
  },
  {
    "id": "rss:https://www.producthunt.com/products/meta",
    "domain": "大厂 AI 动态",
    "title": "Astryx",
    "url": "https://www.producthunt.com/products/meta",
    "source": "Zac Zuo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T03:52:49+00:00",
    "summary": "A customizable, agent-ready open-source design system Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/stanley-studio",
    "domain": "大厂 AI 动态",
    "title": "Stanley Studio",
    "url": "https://www.producthunt.com/products/stanley-studio",
    "source": "Daniel Park",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T03:37:29+00:00",
    "summary": "The AI video editor you hire that edits like a human Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/mozaik-4",
    "domain": "大厂 AI 动态",
    "title": "Mozaik",
    "url": "https://www.producthunt.com/products/mozaik-4",
    "source": "Miodrag Vilotijević",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T12:31:38+00:00",
    "summary": "TypeScript runtime for self-organizing AI agents Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/codemote-remote-control-for-any-ai",
    "domain": "大厂 AI 动态",
    "title": "CodeMote",
    "url": "https://www.producthunt.com/products/codemote-remote-control-for-any-ai",
    "source": "Salvatore Castellitti",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T13:39:06+00:00",
    "summary": "Claude Code, Codex, any CLI agent. Driven from your iPhone Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/lumina-16",
    "domain": "大厂 AI 动态",
    "title": "Lumina",
    "url": "https://www.producthunt.com/products/lumina-16",
    "source": "Wiktor Tkaczyk",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T09:22:08+00:00",
    "summary": "Stop Feeling Like a Fraud. Start Owning Your Success. Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/nixmac",
    "domain": "大厂 AI 动态",
    "title": "Nixmac",
    "url": "https://www.producthunt.com/products/nixmac",
    "source": "Cooper Maruyama",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T13:33:34+00:00",
    "summary": "Nix-darwin that speaks plain English Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/circlechat",
    "domain": "大厂 AI 动态",
    "title": "CircleChat",
    "url": "https://www.producthunt.com/products/circlechat",
    "source": "Tash Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T16:05:42+00:00",
    "summary": "Give your AI agents a slack, a task board, and a boss Discussion | Link"
  },
  {
    "id": "rss:https://36kr.com/p/3883721315971078?f=rss",
    "domain": "大厂 AI 动态",
    "title": "36氪首发｜前西门子、罗罗电动飞行团队创业做航空电驱系统，两轮连融数千万元",
    "url": "https://36kr.com/p/3883721315971078?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T05:26:21+00:00",
    "summary": "本文约3000字，建议阅读6分钟 作者&nbsp;|&nbsp;乔钰杰 编辑&nbsp;|&nbsp;袁斯来 硬氪获悉，开普动能航空技术有限责任公司（以下简称“开普动能”）近期连续完成种子轮及天使轮融资，两轮融资合计金额达数千万元人民币，由零以资本领投、新鼎资本跟投，唯快资本担任长期财务顾问。 随着eVTOL产业进入工程化阶段，航空电驱系统正成为产业链中技术壁垒最高的核心环节之一。作为电动飞行器“"
  },
  {
    "id": "rss:https://36kr.com/p/3883708118921480?f=rss",
    "domain": "大厂 AI 动态",
    "title": "上市前夜 | 哈工大在读博士以百亿市值冲港股IPO，创始三人只剩一人",
    "url": "https://36kr.com/p/3883708118921480?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T05:13:02+00:00",
    "summary": "本文约3600字，建议阅读8分钟 作者&nbsp;|&nbsp;彭孝秋 编者按：《上市前夜》栏目聚焦企业冲刺资本市场的关键时刻。每一份招股书里，都藏着一家企业上市前的野心、周期与隐忧。这是第二期——珞石机器人。 7月6日上午10点，珞石机器人港股IPO招股结束。此次IPO定价38港元，每手100股，对应市值99.46亿港元。合计募资8.75亿港元，五家基石认购31.4%。 珞石的IPO之路并不顺利"
  },
  {
    "id": "rss:https://36kr.com/p/3883706720727303?f=rss",
    "domain": "大厂 AI 动态",
    "title": "上市前夜｜4个月净利润38.4亿元，深圳存储黑马冲港股IPO",
    "url": "https://36kr.com/p/3883706720727303?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T05:11:37+00:00",
    "summary": "本文约3400字，建议阅读7分钟 作者&nbsp;|&nbsp;彭孝秋 编者按：《上市前夜》栏目聚焦企业冲刺资本市场的关键时刻。每一份招股书里，都藏着一家企业上市前的野心、周期与隐忧。这是第一期——深圳宏芯宇电子。 7月3日，一家名叫宏芯宇电子的深圳公司，向港交所递交了招股书，此次IPO独家保荐人是中信建投。 招股书里最亮眼的是这么一组数字：2026年前四个月，宏芯宇净利润38.41亿元，比上年同"
  },
  {
    "id": "rss:https://36kr.com/p/3883561480876297?f=rss",
    "domain": "大厂 AI 动态",
    "title": "跨境电商风向转变：新生代不再只拼价格，开始争“定价权”丨最前线",
    "url": "https://36kr.com/p/3883561480876297?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T02:43:23+00:00",
    "summary": "作者丨欧雪 编辑丨最前线 6月30日，亚马逊全球开店与福布斯中国联合发布“2026福布斯中国新生代跨境电商30人评选”，30位入选者平均年龄仅35岁，95后已开始崭露头角。 入选者既有3D打印、庭院机器人、AI助听器等硬核科技赛道的开拓者，也有家具、家居、服装等传统产业的变革者。他们来自广东、浙江、江苏三省，占比超过75%。更重要的是，这些年轻创业者共同票选出了三个年度关键词：“星辰大海”、“快与"
  },
  {
    "id": "rss:https://36kr.com/p/3883456791163138?f=rss",
    "domain": "大厂 AI 动态",
    "title": "AI 砍掉的第一批大厂人：高薪，高绩效，高P｜深氪",
    "url": "https://36kr.com/p/3883456791163138?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T02:26:34+00:00",
    "summary": "访谈｜任彩茹 兰杰 彭倩 文｜任彩茹 编辑｜乔芊 杨轩 “630”减员，AI是祸首还是替罪羊? “现在公司有（减员）名单，你在这里面。”5月中的一天，林越被组长叫进会议室，对方开门见山。 林越的第一反应是平静，他早有预料。早在今年三四月，一些互联网公司内部便传出要裁员的风声。开年以来，中国互联网大公司围绕AI提效激进开展的token竞赛、培训会、隐形考核等，无处不在。当所有人都被卷入一场“all "
  },
  {
    "id": "rss:https://36kr.com/p/3883513899380744?f=rss",
    "domain": "大厂 AI 动态",
    "title": "2026，量子计算迟到的狂欢：能拿订单、奔赴IPO、市值破百亿",
    "url": "https://36kr.com/p/3883513899380744?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T02:15:39+00:00",
    "summary": "图源/视觉中国 作者丨欧雪 编辑丨袁斯来 如果在七年前，有人告诉一个投资人，量子计算公司会有订单，还能在纳斯达克上市，市值破150亿美元，对方大概率会把这人当个骗子。 他们很多人都记得前几年那场“量子寒冬”。那一年，谷歌用量子处理器完成了一项计算， 200秒算出了超级计算机1万年才能得出的结果。人们以为， 量子霸权实现了，量子计算机真的能解决经典计算机无法解决的问题。 狂欢转瞬即逝。那终究只是一次"
  },
  {
    "id": "rss:https://36kr.com/p/3883400536453381?f=rss",
    "domain": "大厂 AI 动态",
    "title": "8点1氪丨7-11指控耐克新鞋配色抄袭；A股新版交易规则今起施行；华尔街称苹果采购长鑫内存是为了压价",
    "url": "https://36kr.com/p/3883400536453381?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T00:02:20+00:00",
    "summary": "今日热点导览 苹果Siri AI秋季上线，仅限iPhone 15 Pro及以上机型 蒋方舟再回应被清华教授指控论文造假 张雪称负债接近1亿元，本月将还清全部债务 黑石集团放弃全球最大数据中心项目，意味着该建设计划已宣告破产 印度政府：正调查苹果手机信息泄露事件 TOP3大新闻 7-11起诉耐克，指控其新鞋配色抄袭7-11标志性颜色 据报道，跨国连锁零售公司7-Eleven（7-11）已在美国得克萨"
  },
  {
    "id": "rss:https://36kr.com/p/3880060701388809?f=rss",
    "domain": "大厂 AI 动态",
    "title": "鄂尔多斯、和达金服共同领投，「贻如科技」完成超亿元A轮融资｜36氪首发",
    "url": "https://36kr.com/p/3880060701388809?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T23:50:00+00:00",
    "summary": "36氪获悉，生物基皮革公司「贻如科技」完成超亿元A轮融资，本轮融资由鄂尔多斯集团与和达金服共同领投，巢生资本跟投，易凯资本担任独家财务顾问。本轮资金将主要用于推动公司商业化开拓与产能建设，并依托AI技术加速生物基皮革的技术革新与产品迭代。 贻如科技成立于2021年，以合成生物学为底层技术，创造以生物基皮革为代表的新一代创新生物基材料——通过微生物发酵直接生产生物基树脂原料，经加工后制成皮革成品，实"
  },
  {
    "id": "rss:https://36kr.com/p/3882365879005186?f=rss",
    "domain": "大厂 AI 动态",
    "title": "硬氪首发 | 港大教授成立的忆生科技获数亿天使轮融资，致力于为机器人造一套记忆系统",
    "url": "https://36kr.com/p/3882365879005186?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T06:27:30+00:00",
    "summary": "作者&nbsp;|&nbsp;邱晓芬 编辑&nbsp;|&nbsp;袁斯来 硬氪获悉，「忆生科技」（TranscEngram）完成数亿元天使轮融资，本轮投资方阵容横跨产业资本与国资平台，包括正大旗下中生制药、浦东创投、张江科投、张江高科、弘信电子、云晖资本、沃肯资本、金舵资本等。 「忆生科技」致力于从科学第一性原理出发，用\"感知—预测—交互\"闭环构建机器人\"大脑+小脑\"统一系统，探索下一代可解释自"
  },
  {
    "id": "rss:https://36kr.com/p/3882364132077577?f=rss",
    "domain": "大厂 AI 动态",
    "title": "硬氪首发 | 清华车辆学院师兄弟创业具身智能，已完成数亿元天使融资，将落地汽车产业",
    "url": "https://36kr.com/p/3882364132077577?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T06:25:53+00:00",
    "summary": "作者&nbsp;|&nbsp;邱晓芬 编辑&nbsp;|&nbsp;袁斯来 硬氪获悉，具身智能公司「光象科技」宣布完成累计数亿元天使轮融资。 最新一轮由珠海科技产业集团、兴证资本、松禾资本、顺禧基金、慕华科创、SeeFund、亿宸资本、上市公司行云科技等头部财投与产投深度参与，老股东零一创投、L2F光源创业者基金持续加注。 本轮资金将重点投入物理原生基座模型的研发迭代，并推进具身智能机器人在工业场"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3883831227101191?f=rss",
    "domain": "大厂 AI 动态",
    "title": "上海电气集团等成立新公司，注册资本100万",
    "url": "https://36kr.com/newsflashes/3883831227101191?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T07:17:25+00:00",
    "summary": "36氪获悉，天眼查App显示，近日，上电城发（抚顺）新能源有限公司成立，法定代表人为杜志超，注册资本100万人民币，经营范围包括机械设备销售、机械电气设备销售、合同能源管理等，由上海电气旗下上海电气新能源发展有限公司、抚顺城发建设有限公司共同持股。"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3883821411545091?f=rss",
    "domain": "大厂 AI 动态",
    "title": "爱仕达与智元机器人签署战略合作协议，五大方向开展深度合作",
    "url": "https://36kr.com/newsflashes/3883821411545091?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T07:07:26+00:00",
    "summary": "爱仕达下属人形机器人子公司与智元机器人于7月6日正式签署战略合作协议。根据协议，双方将在采购订单与产品交付、具身智能机器人委托制造、具身智能机器人供应链合作、技术支持及场景化赋能、股权投资及合资公司设立五大方向开展深度合作。（财联社）"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3883816090939650?f=rss",
    "domain": "大厂 AI 动态",
    "title": "A股三大指数集体收跌，煤炭股走强",
    "url": "https://36kr.com/newsflashes/3883816090939650?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T07:02:01+00:00",
    "summary": "36氪获悉，A股三大指数集体收跌，沪指跌0.06%，深成指跌1.16%，创业板指跌1.77%；建材、通信设备、互联网板块领跌，中国巨石跌停，太辰光、格灵深瞳跌超8%；煤炭、农业、能源设备板块涨幅居前，昊华能源、贝肯能源涨停，新希望涨超7%。"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3883808696447237?f=rss",
    "domain": "大厂 AI 动态",
    "title": "沪深两市成交额突破3万亿",
    "url": "https://36kr.com/newsflashes/3883808696447237?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T06:54:30+00:00",
    "summary": "36氪获悉，沪深两市成交额突破3万亿，较上一个交易日此时缩量超700亿元。"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3883806713147648?f=rss",
    "domain": "大厂 AI 动态",
    "title": "宁德时代在厦门成立新公司，注册资本100亿",
    "url": "https://36kr.com/newsflashes/3883806713147648?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T06:52:29+00:00",
    "summary": "36氪获悉，天眼查App显示，近日，宁德时代零碳科技（厦门）有限公司成立，法定代表人为陈伟峰，注册资本100亿人民币，经营范围包括新兴能源技术研发、储能技术服务、电池制造、电池销售等，由宁德时代全资持股。"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3883798757683464?f=rss",
    "domain": "大厂 AI 动态",
    "title": "千问大模型升级实时语音识别大模型Fun-ASR-Realtime",
    "url": "https://36kr.com/newsflashes/3883798757683464?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T06:44:24+00:00",
    "summary": "36氪获悉，千问大模型正式升级实时语音识别大模型Fun-ASR-Realtime——一款首字延迟控制在百毫秒级别、识别准确率接近离线模型的流式语音识别模型，支持16种方言和30种语言。"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3883793305481224?f=rss",
    "domain": "大厂 AI 动态",
    "title": "长城汽车在义乌成立新汽车销售公司，注册资本500万",
    "url": "https://36kr.com/newsflashes/3883793305481224?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T06:38:51+00:00",
    "summary": "36氪获悉，天眼查App显示，近日，魏智选（义乌）汽车销售有限公司成立，法定代表人为谭健，注册资本500万人民币，经营范围包括汽车销售、汽车零配件零售、小微型客车租赁经营服务、机动车修理和维护等，由长城汽车旗下长城智选信息科技（保定）有限公司全资持股。"
  },
  {
    "id": "wscn:3776268",
    "domain": "股票",
    "title": "笃定AI将颠覆经济，美国富人抢着送孩子上\"AI学校\"：对冲基金老板、硅谷VC都在报名",
    "url": "https://wallstreetcn.com/articles/3776268",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T07:15:32+00:00",
    "summary": "硅谷VC和对冲基金经理们正将孩子送入一种颠覆性学校——学费高达每年7.5万美元，没有\"老师\"只有\"向导\"，AI每天追踪学习状态并动态调整课程。Alpha School秋季将扩张至全美近二十所校区，Forge Prep首届仅招34人却收到逾600份申请。然而，斯坦福教授直指其贬低教学专业性，顶尖学者也拒绝为缺乏实证的模式背书。"
  },
  {
    "id": "wscn:3776265",
    "domain": "股票",
    "title": "英特尔上调多款CPU价格，服务器芯片最高涨超1300美元",
    "url": "https://wallstreetcn.com/articles/3776265",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T06:58:32+00:00",
    "summary": "英特尔正式宣布上调部分消费级与服务器级处理器售价，涨幅从数十美元到逾千美元不等。消费端Arrow Lake系列调价温和且仅针对特定SKU，更多折射出需求旺盛而非纯粹成本转嫁；服务器端Xeon芯片涨幅更大，部分型号较发布价暴涨逾1300美元。"
  },
  {
    "id": "wscn:3776263",
    "domain": "股票",
    "title": "HBM封装技术生变：三星、SK海力士双双推迟HBM混合键合导入",
    "url": "https://wallstreetcn.com/articles/3776263",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T06:54:55+00:00",
    "summary": "三星与SK海力士相继将混合键合技术的HBM导入节点推后——原定HBM4首发，如今可能延至第七代HBM4E甚至更晚。厚度标准放宽、散热替代方案落地，令这项技术的紧迫性骤降。但随着HBM5E的I/O数量或再度翻倍至4096个，混合键合并非被抛弃，而是在等待那个间距极限真正到来的时刻。"
  },
  {
    "id": "wscn:3776261",
    "domain": "股票",
    "title": "1190亿美债长端拍卖直面\"假期大考\"，沃什\"去前瞻指引\"底牌如何重定价收益率曲线？",
    "url": "https://wallstreetcn.com/articles/3776261",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T06:54:15+00:00",
    "summary": "美国财政部将在本周完成1190亿美元的国债发行计划，其中周二拍卖3年期国债开场，周三和周四分别跟进10年期和30年期标志性长债。市场普遍关注的是，假期归来后的投资者需求能否承接长端供给。"
  },
  {
    "id": "wscn:3776267",
    "domain": "股票",
    "title": "日本“经济复苏”是真是假？投资者狂欢，日本人勒紧裤腰带",
    "url": "https://wallstreetcn.com/articles/3776267",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T06:51:23+00:00",
    "summary": "日本股市与企业利润飙升，但普通民众正因日元贬值推高物价而缩减开支。“日本复苏”呈现资本热络与民间紧缩的严重撕裂。尽管外资对冲机制加剧日元抛压、甚至有190的贬值预测，但机构预计10月央行加息或推动日元向152修复。复苏成色最终取决于红利能否惠及家庭。"
  },
  {
    "id": "wscn:3776271",
    "domain": "股票",
    "title": "星动纪元完成新一轮10亿元融资，2026年来累计融资近50亿",
    "url": "https://wallstreetcn.com/articles/3776271",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T06:37:41+00:00",
    "summary": "人形机器人正在从“能动”走向“能干活”"
  },
  {
    "id": "wscn:3775383",
    "domain": "股票",
    "title": "铷铯：AI与新能源的“战略稀缺金属”，供需断崖打开4倍增长空间？",
    "url": "https://wallstreetcn.com/premium/articles/3775383?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T06:31:43+00:00",
    "summary": "全球铷铯资源极度稀缺、供给高度垄断，而钙钛矿光伏、太空能源、6G通信、量子技术等新兴需求的爆发式增长，正在推动铷铯盐市场从“吨级”向“千吨级”跨越。"
  },
  {
    "id": "wscn:3776266",
    "domain": "股票",
    "title": "科技股遭对冲基金连抛四周，高盛交易员：“买入一切AI”时代终结！",
    "url": "https://wallstreetcn.com/articles/3776266",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T05:57:45+00:00",
    "summary": "对冲基金连续四周抛售科技股，芯片组合暴跌19%。这并非AI神话破灭，而是残酷的风格洗牌：资金正加速出清拥挤仓位，市场将重新奖励“质量与执行力”，大分化降临。"
  },
  {
    "id": "wscn:3776264",
    "domain": "股票",
    "title": "一周展望：黄金结束周线连跌后开启下半年行情",
    "url": "https://wallstreetcn.com/articles/3776264",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T05:42:48+00:00",
    "summary": "本周将正式开启2026年的下半年行情。\n上周美国6月非农不及预期后，美联储加息压力有所缓解，美元指数..."
  },
  {
    "id": "wscn:3776259",
    "domain": "股票",
    "title": "三星明日初步财报：Q2利润预计暴增18倍，高管内部放话“一年利润顶40年”",
    "url": "https://wallstreetcn.com/articles/3776259",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T05:37:42+00:00",
    "summary": "三星电子二季度营业利润一致预期高达84.6万亿韩元，若达标将超越英伟达刷新全球科技企业单季利润历史纪录；管理层更罕见主动背书，称“今年利润将超过40年累计总和”，背后是DRAM/NAND价格单季飙升逾50%、AI推理需求超预期。然而，公司奖金拨备超40万亿韩元悬而未决，苹果被迫涨价引发需求弹性警报，2万亿美元扩产豪赌更被指“周期顶部融资”。"
  },
  {
    "id": "wscn:3776252",
    "domain": "股票",
    "title": "科创50深V反转涨超2%，芯片半导体齐跌，创新药再爆发，恒科指涨超1%，科网股多反弹",
    "url": "https://wallstreetcn.com/articles/3776252",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T04:03:35+00:00",
    "summary": "盘面上，个股跌多涨少，沪深京三市约3600股飘绿，上午半天成交2.22万亿。沪深两市半日成交额2.21万亿，较上个交易日放量近1500亿。板块方面，半导体产业链领跌，玻璃纤维、玻璃基板、稀土、6G、商业航天概念跌幅居前；超硬材料、GPU、创新药仿制药方向表现强势。"
  },
  {
    "id": "wscn:3776072",
    "domain": "股票",
    "title": "风口浪尖的光芯片：产能仍然紧缺，叙事却为何开始松动？",
    "url": "https://wallstreetcn.com/premium/articles/3776072?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T03:42:20+00:00",
    "summary": "光芯片正从光模块的“辅助器件”跃升为AI算力产业链的“核心瓶颈”，高端EML/CW激光器供需缺口超30%，订单排至2028年，光芯片行业正迎来量价齐升的最强景气周期。"
  },
  {
    "id": "wscn:3776249",
    "domain": "股票",
    "title": "上半年暴涨92%！高盛预计韩股下半年“动荡”，但能再涨20%，杠杆水平没有表面看起来“那么高”",
    "url": "https://wallstreetcn.com/articles/3776249",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T03:18:47+00:00",
    "summary": "高盛维持韩国KOSPI指数12000点目标，意味着涨幅超20%，核心支撑来自320%的全年盈利增长预期及6.65倍的历史低估值。散户杠杆风险低于市场担忧，保证金贷款/存款比率实际在下降。下半年机会可能扩散至工业、能源、治理改革和半导体资本开支链条。"
  },
  {
    "id": "wscn:3776130",
    "domain": "股票",
    "title": "本周重磅日程：中国通胀数据、三星业绩预告、SK海力士美股首秀、智谱MiniMax解禁",
    "url": "https://wallstreetcn.com/articles/3776130",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T03:10:02+00:00",
    "summary": "中国6月CPI、PPI及外储数据本周公布，市场关注价格“K型分化”是否延续。美联储6月会议纪要出炉，此外美国将就对60国加征关税举行听证会。苹果、OpenAI、Meta等科技巨头CEO将齐聚太阳谷峰会，美股二季报序幕开启。智谱、MiniMax港股解禁，流动性压力骤升。SpaceX将入纳指，SK海力士ADR美股首秀、三星业绩预告，OpenAI GPT-5.6即将发布。"
  },
  {
    "id": "wscn:3776256",
    "domain": "股票",
    "title": "华泰宏观：韩国出口增7成印证AI链火热需求",
    "url": "https://wallstreetcn.com/articles/3776256",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T03:00:58+00:00",
    "summary": "韩国6月出口同比飙升70.9%，半导体与计算机出口合计贡献增速近八成，AI链需求持续向数据中心建材、有色金属等上游蔓延。华泰证券认为，费城半导体指数等领先指标预示韩国出口景气将延续，中国集成电路出口同比有望升至120%，亚洲AI供应链全面受益。"
  },
  {
    "id": "wscn:3776251",
    "domain": "股票",
    "title": "为什么光的涨价逻辑更为“健康”？",
    "url": "https://wallstreetcn.com/articles/3776251",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T02:58:37+00:00",
    "summary": "国盛证券表示，光模块涨价逻辑更为良性，从400G到1.6T，单价持续上行，但折算到每比特传输成本却在持续下降。这种\"技术升级驱动溢价\"的模式，不仅不挤压下游，反而摊薄算力集群整体互联成本。光模块的涨价本质上是在“做大总盘子”——它通过创造增量价值，让上下游共同受益，形成正向循环的产业生态。"
  },
  {
    "id": "wscn:3776253",
    "domain": "股票",
    "title": "以色列宣布“无限期”驻军黎巴嫩、加沙地带和叙利亚三大安全区，内塔尼亚胡赴美会晤特朗普",
    "url": "https://wallstreetcn.com/articles/3776253",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T02:40:54+00:00",
    "summary": "尽管三方停火框架协议已于6月底达成，以军仍持续对黎巴嫩多地发动空袭。以色列防长宣布将在黎巴嫩、加沙及叙利亚无限期驻军。消息称，以军在黎以边境和黎巴嫩南部设立多个检查站，并继续在黎巴嫩南部进行军事行动。此为，内塔尼亚胡即将赴美与特朗普会晤，中东局势再度牵动全球神经。"
  },
  {
    "id": "wscn:3776254",
    "domain": "股票",
    "title": "启境GT7全国用户试驾开启！产品表现收获广大用户一致好评",
    "url": "https://wallstreetcn.com/articles/3776254",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T02:21:05+00:00",
    "summary": "近日，由广汽集团与华为乾崑联合打造的首款车型启境GT7正式上市，官方售价20.99-32.99万。与..."
  },
  {
    "id": "wscn:3776247",
    "domain": "股票",
    "title": "中金：港股市场的底部特征",
    "url": "https://wallstreetcn.com/articles/3776247",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T02:16:24+00:00",
    "summary": "中金表示，港股自去年10月高点已回调逾9个月、跌幅超30%，互联网板块更重挫40%。弱势根源三重叠加：居民信贷脉冲跌回924前低位、AI赛道与港股结构错配、南向及海外资金双双降至历史低配。回购激增、RSI超卖、部分龙头估值创十年新低，赔率已现，但大底尚未确立——真正的反转，有待政策转向或AI龙头系统性突破。"
  },
  {
    "id": "wscn:3776250",
    "domain": "股票",
    "title": "宋雪涛：地方投融资模式正在发生二十年来最深刻的变化",
    "url": "https://wallstreetcn.com/articles/3776250",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T02:15:36+00:00",
    "summary": "国金宏观宋雪涛团队认为，地方正从“GDP锦标赛”转向“高质量发展马拉松”，产业生态、人才环境、营商制度将取代土地和补贴，成为地方竞争的核心维度。"
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
    "id": "rss:https://www.netinterest.co/p/defying-the-surveys",
    "domain": "股票",
    "title": "Defying the Surveys",
    "url": "https://www.netinterest.co/p/defying-the-surveys",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-04-17T16:54:51+00:00",
    "summary": "Banks report a resilient quarter &#8211; and a lurking threat"
  },
  {
    "id": "rss:https://www.netinterest.co/p/shuffling-risk",
    "domain": "股票",
    "title": "Shuffling Risk",
    "url": "https://www.netinterest.co/p/shuffling-risk",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-04-10T15:10:44+00:00",
    "summary": "An Asset Class Reborn"
  },
  {
    "id": "rss:https://www.netinterest.co/p/new-pod-the-race-to-secure-a-bank",
    "domain": "股票",
    "title": "NEW POD! The Race to Secure a Bank Charter with Adam Shapiro of Klaros Group",
    "url": "https://www.netinterest.co/p/new-pod-the-race-to-secure-a-bank",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-03-31T15:45:44+00:00",
    "summary": "Net Interest Extra ep 21"
  },
  {
    "id": "rss:https://www.netinterest.co/p/revolut-unbound",
    "domain": "股票",
    "title": "Revolut Unbound",
    "url": "https://www.netinterest.co/p/revolut-unbound",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-03-27T16:20:38+00:00",
    "summary": "The Quest to Build the World&#8217;s First Truly Global Bank"
  },
  {
    "id": "rss:https://www.netinterest.co/p/the-underwriters-of-hormuz",
    "domain": "股票",
    "title": "The Underwriters of Hormuz",
    "url": "https://www.netinterest.co/p/the-underwriters-of-hormuz",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-03-20T16:23:35+00:00",
    "summary": "A post on marine insurance &#8211; by popular demand"
  },
  {
    "id": "rss:https://www.netinterest.co/p/new-pod-market-intelligence-in-the",
    "domain": "股票",
    "title": "🎙️ Market Intelligence in the Age of AI: An Interview with Morningstar CEO, Kunal Kapoor",
    "url": "https://www.netinterest.co/p/new-pod-market-intelligence-in-the",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-03-17T16:30:34+00:00",
    "summary": "Net Interest Extra ep 20"
  },
  {
    "id": "rss:https://www.netinterest.co/p/redemption-day",
    "domain": "股票",
    "title": "Redemption Day",
    "url": "https://www.netinterest.co/p/redemption-day",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-03-13T18:09:28+00:00",
    "summary": "When the exit is smaller than the entrance"
  },
  {
    "id": "rss:https://www.netinterest.co/p/learning-from-lloyd",
    "domain": "股票",
    "title": "Learning from Lloyd",
    "url": "https://www.netinterest.co/p/learning-from-lloyd",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-03-06T17:42:54+00:00",
    "summary": "Blankfein, Goldman and the Next Market Reckoning"
  },
  {
    "id": "rss:https://www.netinterest.co/p/new-pod-how-credit-markets-shaped",
    "domain": "股票",
    "title": "🎙️ How Credit Markets Shaped a Nation: An Interview with Sarah Quinn",
    "url": "https://www.netinterest.co/p/new-pod-how-credit-markets-shaped",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-03-03T16:45:21+00:00",
    "summary": "Net Interest Extra ep 19"
  }
]
```
