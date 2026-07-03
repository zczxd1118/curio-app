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

- 今日日期：`2026-07-03`
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
  "date": "2026-07-03",
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
    "points": 1402722,
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
    "points": 1321205,
    "published_at": "2026-05-05T14:08:25+00:00",
    "summary": "Claude Code保姆级教学【收藏起来不会错！】\n从上手安装，到高级用法，这期一次讲全～\n花了三周做教程，希望能帮到你嘻嘻，感谢朋友们的三连+关注啦～"
  },
  {
    "id": "bvid:BV1yorUYWEGD",
    "domain": "AI",
    "title": "普通人也可以看的 AI 编程指南 | Cursor 教程｜Cursor 使用技巧和思路｜如何免费使用 Cursor｜AI 编程",
    "url": "http://www.bilibili.com/video/av113786467981446",
    "source": "不正经的前端啊",
    "platform": "bilibili",
    "points": 940313,
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
    "points": 825368,
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
    "points": 706065,
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
    "points": 665456,
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
    "points": 517288,
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
    "points": 482618,
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
    "points": 378701,
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
    "points": 311476,
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
    "points": 265869,
    "published_at": "2026-07-01T09:35:43+00:00",
    "summary": "Claude Code 封号原因终于找到了！国外开发者逆向 Claude Code 源码，发现 Anthropic 在客户端里藏了一套隐蔽的用户标记系统，这期视频带你完整还原封号真相。\n开源 AI 编程教程：github.com/liyupi/ai-guide\n编程学习教程+实战项目+简历模板：codefather.cn\n最近 AI 圈儿不太平啊，OpenAI Codex 封号、Cursor 地区"
  },
  {
    "id": "bvid:BV1qGc7zwEX6",
    "domain": "AI",
    "title": "史上最强 AI 编程工具Cursor来啦！Cursor保姆级使用教程！新手友好！看到就是赚到！！！",
    "url": "http://www.bilibili.com/video/av116061928226926",
    "source": "知名的阿呆同学",
    "platform": "bilibili",
    "points": 248752,
    "published_at": "2026-02-19T07:34:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1kxLD6HEYN",
    "domain": "AI",
    "title": "Claude Code怎么全自动跑13小时？实测GLM 5.2开源天花板",
    "url": "http://www.bilibili.com/video/av116763920438810",
    "source": "小白debug",
    "platform": "bilibili",
    "points": 211847,
    "published_at": "2026-06-17T10:14:02+00:00",
    "summary": "我手搓了一个Openclaw"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 176055,
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
    "points": 165485,
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
    "points": 160400,
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
    "points": 158633,
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
    "points": 145912,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 121122,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1ExV36wEsE",
    "domain": "AI",
    "title": "VS Code 安装 Claude Code 并接入 DeepSeek！Claude Code for VS Code！VSCode使用ClaudeCode插件",
    "url": "http://www.bilibili.com/video/av116662871268177",
    "source": "FutureAI实验室",
    "platform": "bilibili",
    "points": 115256,
    "published_at": "2026-05-30T09:44:52+00:00",
    "summary": "本节视频编号71，评论区自助领取配套文档，记得一键三连哦！"
  },
  {
    "id": "bvid:BV1WJjF67Eky",
    "domain": "AI",
    "title": "对Claude code上瘾了",
    "url": "http://www.bilibili.com/video/av116768819384530",
    "source": "小王很南",
    "platform": "bilibili",
    "points": 103280,
    "published_at": "2026-06-18T02:50:04+00:00",
    "summary": "我做的交互网站"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 69433,
    "published_at": "2026-07-01T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260701\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\nAI大模型开发热门教程：\nAI大模型开发：BV1h1"
  },
  {
    "id": "bvid:BV1ZjDYB7Eam",
    "domain": "AI",
    "title": "从 0 到 1：6小时掌握 Vibe Coding！ Claude Code ＋ AI 这支影片直接让你超越 90% AI 玩家",
    "url": "http://www.bilibili.com/video/av116362122894759",
    "source": "李哈利Harry",
    "platform": "bilibili",
    "points": 61836,
    "published_at": "2026-04-08T11:00:00+00:00",
    "summary": "🌟 加入AI大师社群并运用AI创业赚钱：https://www.skool.com/aiagent/about?ref=f2b566934c5c4639aaa47ab1fe39310e\n📌 加入我的免费 Skool 社群，获取模板：https://www.skool.com/aiagent8/about?ref=f2b566934c5c4639aaa47ab1fe39310e\n\n🚧 开始使用 n8"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 61723,
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
    "points": 54778,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 52689,
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
    "points": 47307,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 41140,
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
    "points": 29866,
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
    "points": 28703,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1YV7W6YEFU",
    "domain": "AI",
    "title": "方向错了！手机跟AI Agent到底该怎么结合？",
    "url": "http://www.bilibili.com/video/av116822892418628",
    "source": "我是HYK",
    "platform": "bilibili",
    "points": 28506,
    "published_at": "2026-06-28T03:00:00+00:00",
    "summary": "方向错了！一句话订票、点咖啡，这种极其容易出错的Agent，几乎没有坚持用下来的用户；现阶段手机需要的是短链路、点到为止的AI Agent。"
  },
  {
    "id": "bvid:BV1bh3LzqEze",
    "domain": "AI",
    "title": "Chatbox AI终端：跨平台+MCP+知识库+开源+免费！一键连接所有AI语言模型！手把手安装使用指南！",
    "url": "http://www.bilibili.com/video/av114793218380950",
    "source": "_Smzh_",
    "platform": "bilibili",
    "points": 27622,
    "published_at": "2025-07-04T10:00:00+00:00",
    "summary": "chatbox官网：https://chatboxai.app\ngithub仓库：https://github.com/chatboxai/chatbox\n\nLM Studio教程：BV1usrLYTEZR\nTGW懒人包部署教程：BV1dVCzYUE7G\n本地语言模型个人推荐：BV1Bb421E7j7"
  },
  {
    "id": "bvid:BV1RUDsBWEHb",
    "domain": "AI",
    "title": "【2026最新版】目前B站最全最细的Cursor+Skills实战指南教程，手把手带你开发爆款app，全程干货无废话！比付费效果强十倍！",
    "url": "http://www.bilibili.com/video/av116373464350785",
    "source": "AI大模型技术教程",
    "platform": "bilibili",
    "points": 24951,
    "published_at": "2026-04-09T10:15:00+00:00",
    "summary": "制作不易，麻烦各位观众老爷一键三连呀【点赞、投币、收藏】感谢支持～\nCursor+Skills频配套文档课件笔记代码及AI大模型学习路线图戳这里获取→https://www.bilibili.com/read/cv41777105/?jump_opus=1"
  },
  {
    "id": "bvid:BV1nf42127MW",
    "domain": "AI",
    "title": "用AI Agent做一个法律咨询助手，罗老看了都直呼内行 feat.通义千问大模型&amp;阿里云百炼平台",
    "url": "http://www.bilibili.com/video/av1204786228",
    "source": "御风大世界",
    "platform": "bilibili",
    "points": 21253,
    "published_at": "2024-05-21T05:09:48+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV14erKYuEaE",
    "domain": "AI",
    "title": "最强编程AI Cursor+Unity制作一个史诗游戏(详细)",
    "url": "http://www.bilibili.com/video/av113774908413987",
    "source": "多西杰克",
    "platform": "bilibili",
    "points": 17479,
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
    "points": 17284,
    "published_at": "2025-05-25T13:36:25+00:00",
    "summary": "文档：https://icnt94i5ctj4.feishu.cn/docx/ZkR3d1lfUosIFCx4qWJcI4QunY0\nshay大佬的HA SSE接入文档：https://bbs.hassbian.com/thread-29314-1-1.html"
  },
  {
    "id": "bvid:BV1cCEi6sEU5",
    "domain": "AI",
    "title": "🦊他能成功吗？Claude Code 接管虚幻引擎5，打造一款游戏 | 带你走完整个流程",
    "url": "http://www.bilibili.com/video/av116731724959171",
    "source": "Apeak_虚幻丰哥",
    "platform": "bilibili",
    "points": 17086,
    "published_at": "2026-06-11T13:41:36+00:00",
    "summary": "Claude Code 接管虚幻引擎5，打造了一款游戏\n下载我的 CLAUDE.md（帮你省 token 的配置）\n链接：https://pan.quark.cn/s/b6e50b4b2535\n提取码：tbaE\nStefan 3D AI ：https://www.youtube.com/watch?v=iRcrZjOt5H8&amp;t=1s\n🔗 完整教程指南和链接：https://www.top"
  },
  {
    "id": "bvid:BV1JU7E6PEar",
    "domain": "AI",
    "title": "Cursor 已死？我为什么要退订 Cursor ？",
    "url": "http://www.bilibili.com/video/av116819553683121",
    "source": "小狗瑞恩Ryan",
    "platform": "bilibili",
    "points": 14615,
    "published_at": "2026-06-27T01:52:00+00:00",
    "summary": "当了一年多的 Cursor 重度用户，最近把它退订了。\n\n不是它变差了，是 Claude Code 和 Codex 真的太好用了。\n\n几个真实感受： ① 大模型越来越强，我已经不怎么手写代码了 ② Cursor 套的是 VS Code 壳子，只属于程序员 ③ 底层模型不在一个量级——Claude 有 Opus 和 Fable 5，Codex 有 GPT 5.5/5.6，Cursor 的 Compo"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "穷在街头无人问lhj",
    "platform": "bilibili",
    "points": 11718,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1etEQ6DETs",
    "domain": "AI",
    "title": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！",
    "url": "http://www.bilibili.com/video/av116724192118321",
    "source": "AI产品经理大模型",
    "platform": "bilibili",
    "points": 11660,
    "published_at": "2026-06-10T05:41:54+00:00",
    "summary": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！"
  },
  {
    "id": "bvid:BV1LWTe6gEVc",
    "domain": "AI",
    "title": "Claude code帮我实现综述论文自由！",
    "url": "http://www.bilibili.com/video/av116842504918580",
    "source": "做科研的大师兄",
    "platform": "bilibili",
    "points": 10460,
    "published_at": "2026-07-01T03:07:40+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1jCJs6UECL",
    "domain": "AI",
    "title": "豆包最新推出办公任务模式，你的专属办公Agent 来了！",
    "url": "http://www.bilibili.com/video/av116743888444368",
    "source": "翻奇兽AI",
    "platform": "bilibili",
    "points": 9853,
    "published_at": "2026-06-13T17:11:14+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 9139,
    "published_at": "2025-04-14T02:30:00+00:00",
    "summary": "MCP服务网站：https://smithery.ai/\nCherry Studio官方网站：https://cherry-ai.com/"
  },
  {
    "id": "bvid:BV1C3jt64EPS",
    "domain": "AI",
    "title": "B站讲的最好的Vibe Coding企业级项目实战教程（2026最新版）从入门到进阶，七天速通Claude Code+Codex+CursorAI工程化编程开发",
    "url": "http://www.bilibili.com/video/av116787425383675",
    "source": "图灵学院诸葛",
    "platform": "bilibili",
    "points": 9022,
    "published_at": "2026-06-21T09:48:04+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n 【本视频笔记代码、大模型最新学习路线、系统学习课程、实战案例、电子书+问题解答等戳这里获取→https://www.bilibili.com/read/cv39576966/?jump_opus=1】"
  },
  {
    "id": "bvid:BV1GD7qzREVA",
    "domain": "AI",
    "title": "【MCP部署实战】手把手教你把MCP接入各大热门工具，保姆级教学，我奶听了都能学会，CherryStudio配置MCP",
    "url": "http://www.bilibili.com/video/av114623818763366",
    "source": "亿点点大模型",
    "platform": "bilibili",
    "points": 8402,
    "published_at": "2025-06-04T07:08:58+00:00",
    "summary": "全程干货无废话！MCP最新实战教程，从环境部署、原理详解到项目实战，带你彻底吃透MCP！MCPServer开发，mcp开发，mcp教程，mcp项目 完整视频教程+讲解课件+学习笔记+AI大模型知识库已打包可分享！"
  },
  {
    "id": "bvid:BV12ojm64EU6",
    "domain": "AI",
    "title": "🧲 Claude Code 工作流：长程任务的规划和执行利器 ⛓️",
    "url": "http://www.bilibili.com/video/av116800494767674",
    "source": "沧海九粟",
    "platform": "bilibili",
    "points": 8377,
    "published_at": "2026-06-24T00:00:00+00:00",
    "summary": "GAC 平台：https://gaccode.com/signup?ref=UWDADYQI\n官方文档：https://code.claude.com/docs/en/workflows\n状态栏技能：https://github.com/webup/skills-cc#-webup-statusline"
  },
  {
    "id": "bvid:BV1QU6GYFEio",
    "domain": "AI",
    "title": "[课程4] 用Cursor开发数据库真的很简单 | Agent应用 | 用Codebase解决跨文件错误",
    "url": "http://www.bilibili.com/video/av113742109021318",
    "source": "Zhu的AI日记",
    "platform": "bilibili",
    "points": 6990,
    "published_at": "2024-12-31T12:30:00+00:00",
    "summary": "***这是全网最完整的分享如何在不懂编程的情况下，利用结构化思维，用Cursor开发商业app的系列课程。\n《懒人记单词》是基于艾宾浩斯遗忘曲线设计的记单词神器，它可以对每一个单词进行人性化的解读，并在每一个遗忘周期到来时及时提醒，并通过单词释义选择，拼写和造句进行全方位的巩固，同时AI还能对你的句子进行多维度的评估，确保你对每一个单词不仅会认，而且会用。\n\n***你将在本视频中学到：\n1.数据库"
  },
  {
    "id": "bvid:BV1QuTv6BEf7",
    "domain": "AI",
    "title": "vibe coding｜打工人做App全流程分享！含大量提示词和prd～｜【b站AI创造公开赛】",
    "url": "http://www.bilibili.com/video/av116844484631808",
    "source": "chocpink_AI版",
    "platform": "bilibili",
    "points": 6573,
    "published_at": "2026-07-01T11:29:32+00:00",
    "summary": "我用3天 vibe coding出了我的第二个 App～\n总结了上次匆忙开始没有准备好 导致很多次来回调试和推翻重来的血泪经验，这次用AI vibe coding我的宗旨就是和AI打好配合，人工的部分重点放在了各种给AI的需求文档（虽然也是AI写的）～ 全流程AI来实现落地我只做掌控整体节奏、给AI提供素材/PRD和验收，并且验收通过率也是极高的，极大提高了AI开发可用性和我的效率！\n\n全程无代码"
  },
  {
    "id": "bvid:BV1fNs9eiEm9",
    "domain": "AI",
    "title": "Cursor AI编程结合cocos3.8游戏开发教程-01",
    "url": "http://www.bilibili.com/video/av113187471105975",
    "source": "太阳8800",
    "platform": "bilibili",
    "points": 6492,
    "published_at": "2024-09-23T15:15:13+00:00",
    "summary": "开源源码仓库\nhttps://gitee.com/gamepublic/chess-cards"
  },
  {
    "id": "bvid:BV1uz8jzdEZy",
    "domain": "AI",
    "title": "AI Agent 设计助手功能教程丨自然语言交互驱动 AI 智能设计花境、导出苗木清单",
    "url": "http://www.bilibili.com/video/av114929986241780",
    "source": "D5渲染器",
    "platform": "bilibili",
    "points": 6388,
    "published_at": "2025-07-28T10:55:00+00:00",
    "summary": "全新上线的D5 2.11版本正式推出D5 AI 设计助手（AI Agent），能够准确理解设计意图，智能处理复杂任务。与 AI 设计助手对话，通过自然语言交互驱动 AI 完成专业任务。首次上线带来了「花境生成器」「智能苗木清单」「D5 Bot」，未来设计助手还将具备更多能力，令创作者更专注核心创意塑造和方案决策。\n\n获取D5渲染器： https://www.d5render.cn/\n\n2.11宣传"
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
    "id": "rss:https://www.eetimes.com/sales-forecasting-guide-for-electronics-manufacturing-smbs/",
    "domain": "AI 算力 / 半导体",
    "title": "Sales Forecasting Guide for Electronics Manufacturing SMBs",
    "url": "https://www.eetimes.com/sales-forecasting-guide-for-electronics-manufacturing-smbs/",
    "source": "MRPeasy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T13:00:00+00:00",
    "summary": "Sales forecasting helps manufacturers estimate future demand so they can plan production, purchasing, and capacity before customer orders become urgent. The post Sales Forecasting Guide for Electronic"
  },
  {
    "id": "rss:https://www.eetimes.com/eu-chips-act-2-award-winning-sequel-or-straight-to-video/",
    "domain": "AI 算力 / 半导体",
    "title": "EU Chips Act 2: Award-Winning Sequel or Straight to Video?",
    "url": "https://www.eetimes.com/eu-chips-act-2-award-winning-sequel-or-straight-to-video/",
    "source": "Bram De Muer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T07:45:07+00:00",
    "summary": "EU Chips Act 2.0 gets the plot right: Fabs aren’t enough. Europe needs design-layer muscle and multi-foundry freedom. The post EU Chips Act 2: Award-Winning Sequel or Straight to Video? appeared first"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/sk-hynix-to-invest-usd712-5-billion-in-south-korean-operations-cheongju-nand-expansion-yongin-semiconductor-cluster-for-dram-detailed",
    "domain": "AI 算力 / 半导体",
    "title": "SK hynix to invest $712.5 billion in South Korean operations — Cheongju NAND expansion, Yongin Semiconductor Cluster for DRAM detailed",
    "url": "https://www.tomshardware.com/pc-components/dram/sk-hynix-to-invest-usd712-5-billion-in-south-korean-operations-cheongju-nand-expansion-yongin-semiconductor-cluster-for-dram-detailed",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T16:28:35+00:00",
    "summary": "SK hynix announces major plan to spend $712.5 billion in its operations in South Korea, but the only detailed investments are spendings on a new NAND fab and a packaging facility."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/palantir-ceo-alex-karp-claims-ai-companies-are-stealing-customers-data-while-charging-them-for-unproductive-tokens-says-livid-businesses-are-paying-for-tokens-that-create-no-value",
    "domain": "AI 算力 / 半导体",
    "title": "Palantir CEO Alex Karp claims AI companies are stealing customers' data while charging them for unproductive tokens — says 'livid' businesses 'are paying for tokens that create no value'",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/palantir-ceo-alex-karp-claims-ai-companies-are-stealing-customers-data-while-charging-them-for-unproductive-tokens-says-livid-businesses-are-paying-for-tokens-that-create-no-value",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T16:27:40+00:00",
    "summary": "Palantir CEO Alex Karp boldly states in an interview that claims AI companies are stealing customer's data while charging them for unproductive services."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/nvidia-to-take-a-cut-of-ai-cloud-revenue-on-top-of-hardware-sales",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia offers to take a cut of AI cloud revenue on top of hardware sales in new optional financing vehicle — trades tokens for revenue cut",
    "url": "https://www.tomshardware.com/tech-industry/nvidia-to-take-a-cut-of-ai-cloud-revenue-on-top-of-hardware-sales",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T15:46:31+00:00",
    "summary": "Nvidia has announced a new business model under which it’ll be able to double-dip for revenue on the same silicon."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/u-s-pc-shipments-drop-7-percent-market-isnt-expected-to-bounce-back-until-2029-price-hikes-and-component-shortages-take-hold-as-pc-market-declines-omdia-report-suggests",
    "domain": "AI 算力 / 半导体",
    "title": "U.S PC shipments drop 7%, market isn't expected to bounce back until 2029 — price hikes and component shortages take hold as PC market declines, Omdia report suggests",
    "url": "https://www.tomshardware.com/tech-industry/u-s-pc-shipments-drop-7-percent-market-isnt-expected-to-bounce-back-until-2029-price-hikes-and-component-shortages-take-hold-as-pc-market-declines-omdia-report-suggests",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T15:35:37+00:00",
    "summary": "New data suggests PC shipments are already down in 2026 and are likely to get worse in the latter half of the year, but that could be setting the stage for a resurgence in the years to come."
  },
  {
    "id": "rss:https://www.tomshardware.com/gift-guides-seasonal-sales/save-up-to-39-percent-on-a-new-3d-printer-this-weekend-thanks-to-these-july-4th-deals-discounted-printers-filament-and-resin-from-bambu-lab-creality-elegoo-and-more-for-3dp-beginners-and-experienced-pros-alike",
    "domain": "AI 算力 / 半导体",
    "title": "Save up to 39% on a new 3D printer this weekend, thanks to these July 4th deals — discounted printers, filament, and resin from Bambu Lab, Creality, Elegoo, and more for 3DP beginners and experienced ",
    "url": "https://www.tomshardware.com/gift-guides-seasonal-sales/save-up-to-39-percent-on-a-new-3d-printer-this-weekend-thanks-to-these-july-4th-deals-discounted-printers-filament-and-resin-from-bambu-lab-creality-elegoo-and-more-for-3dp-beginners-and-experienced-pros-alike",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T15:18:04+00:00",
    "summary": "These are some of the top 3D printer deals available right now during this Independence Day weekend."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/servers/supermicro-denies-that-its-offices-were-raided-by-taiwanese-authorities-in-nvidia-gpu-smuggling-case-company-says-that-it-coordinated-with-the-police-and-provided-access-to-investigated-employees-workstations-and-gadgets",
    "domain": "AI 算力 / 半导体",
    "title": "Supermicro denies that its offices were raided by Taiwanese authorities in Nvidia GPU smuggling case — company says that it coordinated with the police and provided access to investigated employees’ w",
    "url": "https://www.tomshardware.com/desktops/servers/supermicro-denies-that-its-offices-were-raided-by-taiwanese-authorities-in-nvidia-gpu-smuggling-case-company-says-that-it-coordinated-with-the-police-and-provided-access-to-investigated-employees-workstations-and-gadgets",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T14:10:56+00:00",
    "summary": "The company insists that it's cooperating with Taiwanese authorities and has voluntarily provided access to its premises. It also confirmed with the police that it's the individual, not the institutio"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/digital-archivists-rush-to-save-ps3-game-data-before-sony-shuts-down-the-store-forever-in-2027-rpcs3-emulator-urges-users-to-preserve-all-content",
    "domain": "AI 算力 / 半导体",
    "title": "Digital archivists rush to save PS3 game data before Sony shuts down the store forever in 2027 — RPCS3 emulator urges users to preserve all content",
    "url": "https://www.tomshardware.com/video-games/playstation/digital-archivists-rush-to-save-ps3-game-data-before-sony-shuts-down-the-store-forever-in-2027-rpcs3-emulator-urges-users-to-preserve-all-content",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T13:52:33+00:00",
    "summary": "Sony is shutting down PSN for PS3 consoles next year, so preservationists are being asked to wake up from their slumber to archive everything before it's too late."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/air-cooling/montech-nx600-review",
    "domain": "AI 算力 / 半导体",
    "title": "Montech NX600 Review: A budget dual tower with jet-engine fans",
    "url": "https://www.tomshardware.com/pc-components/air-cooling/montech-nx600-review",
    "source": "Albert Thomas",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T13:30:00+00:00",
    "summary": "Montech’s NX600 is a new dual-tower air cooler powered by six heatpipes and two 28mm thick high-performance 120mm fans. We’ve tested it with AMD’s Ryzen 9 9950X3D to benchmark its thermal efficiency."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/meta-reportedly-plans-to-rent-out-its-ai-compute",
    "domain": "AI 算力 / 半导体",
    "title": "Meta reportedly plans to rent out its AI compute, sending AI stocks tumbling — 'Meta Compute' would put company in direct competition with AWS",
    "url": "https://www.tomshardware.com/tech-industry/meta-reportedly-plans-to-rent-out-its-ai-compute",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T13:01:25+00:00",
    "summary": "Meta is reportedly weighing two service models: selling developers access to AI models hosted on its own infrastructure, or selling raw computing capacity."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/motherboards/asus-b850-creator-wifi-neo-motherboard-review",
    "domain": "AI 算力 / 半导体",
    "title": "Asus B850-Creator Wifi Neo motherboard review: AM5 Creator mobo looks the part, but is missing useful features",
    "url": "https://www.tomshardware.com/pc-components/motherboards/asus-b850-creator-wifi-neo-motherboard-review",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T13:00:00+00:00",
    "summary": "Asus' B850-Creator Wifi Neo offers fast dual 5 GbE, 3x video outputs, and loads of EZ PC DIY/AI features, but lacks enough USB ports (no 40 Gbps at all) and is expensive for the B850 platform."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-hikes-pricing-for-its-flagship-desktop-pc-chips-by-up-to-usd50-official-core-ultra-270k-plus-and-250k-plus-product-pages-now-recommend-prices-of-up-to-usd349-and-usd229-respectively",
    "domain": "AI 算力 / 半导体",
    "title": "Intel hikes pricing for its flagship desktop PC chips by up to $50 — official Core Ultra 270K Plus and 250K Plus product pages now recommend prices of up to $349 and $229, respectively",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-hikes-pricing-for-its-flagship-desktop-pc-chips-by-up-to-usd50-official-core-ultra-270k-plus-and-250k-plus-product-pages-now-recommend-prices-of-up-to-usd349-and-usd229-respectively",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T12:58:25+00:00",
    "summary": "Intel's Arrow Lake Refresh processors remain among the company's strongest desktop offerings, but newly updated pricing makes both CPUs noticeably more expensive than when they debuted in March."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-floats-5-percent-government-stake-days-after-washington-delayed-gpt-5-6",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI mulling giving US gov't a 5% stake in the company, days after Washington delayed GPT-5.6 — Altman reportedly wants every leading U.S. AI lab paying into an Alaska-style public fund",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-floats-5-percent-government-stake-days-after-washington-delayed-gpt-5-6",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T12:06:36+00:00",
    "summary": "Altman is understood to have raised the idea with President Donald Trump, Commerce Secretary Howard Lutnick, and Treasury Secretary Scott Bessent."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/startup-activates-nuclear-microreactor-live-on-stage-to-power-an-nvidia-rtx-spark-desktop-pc-firm-working-with-nvidia-to-build-a-30mw-closed-loop-ai-factory-that-doesnt-use-local-water",
    "domain": "AI 算力 / 半导体",
    "title": "Startup activates nuclear microreactor live on stage to power an Nvidia RTX Spark desktop PC — firm working with Nvidia to build a 30MW closed loop AI factory that doesn’t use local water",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/startup-activates-nuclear-microreactor-live-on-stage-to-power-an-nvidia-rtx-spark-desktop-pc-firm-working-with-nvidia-to-build-a-30mw-closed-loop-ai-factory-that-doesnt-use-local-water",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T11:58:58+00:00",
    "summary": "Valar Atomics claims to be the first startup to produce nuclear power, and it demonstrated that ability on stage by using its Ward 250 microreactor to power an RTX Spark unit. It also announced a part"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-usd521-on-this-4k-capable-rtx-5070-gaming-pc-from-cyberpowerpc-now-just-usd1-349-huge-price-drop-for-budget-friendly-rig-with-impressive-intel-core-ultra-250kf-cpu-16gb-ddr5-and-1tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Save $521 on this 4K-capable RTX 5070 gaming PC from CyberPowerPC, now just $1,349 — huge price drop for budget-friendly rig with impressive Intel Core Ultra 250KF CPU, 16GB DDR5, and 1TB SSD",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-usd521-on-this-4k-capable-rtx-5070-gaming-pc-from-cyberpowerpc-now-just-usd1-349-huge-price-drop-for-budget-friendly-rig-with-impressive-intel-core-ultra-250kf-cpu-16gb-ddr5-and-1tb-ssd",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T11:06:45+00:00",
    "summary": "Save over $500 on this powerful CyberPowerPC gaming machine with an RTX 5070 and brand-new Intel Core Ultra 5 250KF CPU, alongside a 1TB SSD and 16GB of DDR5 RAM, all for only $1,349."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/hp-has-slashed-usd1-300-off-this-colossal-5080-gaming-laptop-for-july-4-34-percent-discount-gets-you-32gb-of-ram-and-24-core-arrow-lake-mobile-gaming-for-usd2-499",
    "domain": "AI 算力 / 半导体",
    "title": "HP has slashed $1,300 off this colossal 5080 gaming laptop for July 4 — 34% discount gets you 32GB of RAM and 24-core Arrow Lake mobile gaming for $2,499",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/hp-has-slashed-usd1-300-off-this-colossal-5080-gaming-laptop-for-july-4-34-percent-discount-gets-you-32gb-of-ram-and-24-core-arrow-lake-mobile-gaming-for-usd2-499",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T11:05:37+00:00",
    "summary": "Get $1,300 off this HP Omen Max Gaming laptop with Intel Core Ultra 9 275HX, RTX 5080, and 32GB of RAM."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/possible-amd-rx-7900-xtx-engineering-sample-with-red-pcb-surfaces-prototype-came-with-no-backplate-and-custom-vbios-but-matches-rx-7900-gre-specs",
    "domain": "AI 算力 / 半导体",
    "title": "Possible AMD RX 7900 XTX engineering sample with red PCB surfaces — prototype came with no backplate & custom VBIOS but matches RX 7900 GRE specs",
    "url": "https://www.tomshardware.com/pc-components/gpus/possible-amd-rx-7900-xtx-engineering-sample-with-red-pcb-surfaces-prototype-came-with-no-backplate-and-custom-vbios-but-matches-rx-7900-gre-specs",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T11:00:00+00:00",
    "summary": "It seems like a never-before-seen engineering sample for AMD's last-gen Radeon RX 7900 XTX has just popped up online, featuring specs that indicate it's a binned down model."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/singapore-cops-seize-usd42-million-mansion-freeze-usd772k-bank-account-of-suspected-nvidia-ai-gpu-smugglers-individuals-alleged-to-have-illegally-exported-data-center-servers-to-china-charged-with-fraud-money-laundering",
    "domain": "AI 算力 / 半导体",
    "title": "Singapore cops seize $42 million mansion, freeze $772k bank account of suspected Nvidia AI GPU smugglers — individuals alleged to have illegally exported data center servers to China charged with frau",
    "url": "https://www.tomshardware.com/tech-industry/singapore-cops-seize-usd42-million-mansion-freeze-usd772k-bank-account-of-suspected-nvidia-ai-gpu-smugglers-individuals-alleged-to-have-illegally-exported-data-center-servers-to-china-charged-with-fraud-money-laundering",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T11:00:00+00:00",
    "summary": "Four individuals suspected of smuggling Nvidia AI GPUs into China by using Singapore as a transshipment point are facing multiple charges. Singaporean authorities say they are not obliged to enforce f"
  },
  {
    "id": "rss:https://www.tomshardware.com/gift-guides-seasonal-sales/the-best-tech-deals-this-july-4th-save-on-gaming-desktops-laptops-gpus-gaming-chairs-monitors-and-more",
    "domain": "AI 算力 / 半导体",
    "title": "The best tech deals this July 4th — save on gaming desktops, laptops, GPUs, gaming chairs, monitors, and more",
    "url": "https://www.tomshardware.com/gift-guides-seasonal-sales/the-best-tech-deals-this-july-4th-save-on-gaming-desktops-laptops-gpus-gaming-chairs-monitors-and-more",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T10:58:46+00:00",
    "summary": "See our favorite tech deals over July 4th — the best prices on gaming PCs, gaming laptops, monitors, and components."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/apples-hide-my-email-service-reportedly-reveals-users-actual-email-addresses-with-little-effort-cupertino-has-seemingly-known-about-the-problem-for-a-year-but-has-yet-to-fix-it",
    "domain": "AI 算力 / 半导体",
    "title": "Apple's Hide My Email service reportedly reveals users' actual email addresses with little effort — Cupertino has seemingly known about the problem for a year but has yet to fix it",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/apples-hide-my-email-service-reportedly-reveals-users-actual-email-addresses-with-little-effort-cupertino-has-seemingly-known-about-the-problem-for-a-year-but-has-yet-to-fix-it",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T10:40:00+00:00",
    "summary": "Apple's Hide My Email service still reveals users' actual email addresses with little effort — even though it's been a year since the company was notified about problem."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/intel-expands-production-of-photomasks-in-california-euv-and-high-na-euv-in-the-focal-point",
    "domain": "AI 算力 / 半导体",
    "title": "Intel expands production of photomasks in California: EUV and High-NA EUV in the focal point",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/intel-expands-production-of-photomasks-in-california-euv-and-high-na-euv-in-the-focal-point",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T10:20:00+00:00",
    "summary": "Intel begins expansion of its Bowers Campus in Santa Clara to produce more photomasks in-house, which is set to be crucial as process technologies get more sophisticated."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/googles-camera-based-recaptcha-asks-for-a-hand-scan-to-prove-youre-human",
    "domain": "AI 算力 / 半导体",
    "title": "Google testing controversial webcam-based reCAPTCHA that asks for a hand scan to prove you're human — testers beat it with a stock photo",
    "url": "https://www.tomshardware.com/tech-industry/googles-camera-based-recaptcha-asks-for-a-hand-scan-to-prove-youre-human",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T10:00:00+00:00",
    "summary": "Google is testing a reCAPTCHA check that switches on a user's camera and asks them to wave or hold up an open palm."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/elon-musk-categorically-denies-spacex-is-making-an-ai-device-with-proprietary-os-says-rumors-of-a-handheld-thinner-than-an-iphone-are-utterly-false",
    "domain": "AI 算力 / 半导体",
    "title": "Elon Musk categorically denies SpaceX is making an AI device with proprietary OS — says rumors of a handheld thinner than an iPhone are 'utterly false'",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/elon-musk-categorically-denies-spacex-is-making-an-ai-device-with-proprietary-os-says-rumors-of-a-handheld-thinner-than-an-iphone-are-utterly-false",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T09:48:09+00:00",
    "summary": "SpaceX is reportedly working on a handheld device that runs a proprietary operating system and features advanced AI capabilities from xAI, but Elon Musk denies existence of the product."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/32gb-corsair-vengeance-ddr5-is-usd314-in-this-woot-sale-the-lowest-standalone-ram-price-in-months-thanks-to-usd125-discount",
    "domain": "AI 算力 / 半导体",
    "title": "32GB Corsair Vengeance DDR5 is $359 in this Woot sale — the lowest standalone RAM price in months, thanks to $80 discount",
    "url": "https://www.tomshardware.com/pc-components/32gb-corsair-vengeance-ddr5-is-usd314-in-this-woot-sale-the-lowest-standalone-ram-price-in-months-thanks-to-usd125-discount",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T09:45:08+00:00",
    "summary": "Get Corsair Vengeance DDR5 for just $314 at Woot."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/console-gaming/xbox-reportedly-testing-a-way-to-digitize-physical-games-in-the-wake-of-playstation-killing-game-discs-feature-said-to-go-back-to-xbox-one-era-games",
    "domain": "AI 算力 / 半导体",
    "title": "Xbox reportedly testing a way to digitize physical games in the wake of PlayStation killing game discs — feature said to go back to Xbox One-era games",
    "url": "https://www.tomshardware.com/video-games/console-gaming/xbox-reportedly-testing-a-way-to-digitize-physical-games-in-the-wake-of-playstation-killing-game-discs-feature-said-to-go-back-to-xbox-one-era-games",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T19:19:25+00:00",
    "summary": "Microsoft is reportedly testing a feature to digitize physical games going back to the Xbox One with digital copies tied to the owner of the physical disc."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/tesla-hires-17-year-intel-veteran-responsible-for-billion-dollar-fab-startups-gary-jiang-likely-chosen-to-oversee-fab-efforts-for-terafabs-licensing-of-14a",
    "domain": "AI 算力 / 半导体",
    "title": "Tesla hires 17-year Intel veteran responsible for billion-dollar fab startups — Gary Jiang likely chosen to oversee fab efforts for Terafab's licensing of 14A",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/tesla-hires-17-year-intel-veteran-responsible-for-billion-dollar-fab-startups-gary-jiang-likely-chosen-to-oversee-fab-efforts-for-terafabs-licensing-of-14a",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T14:07:26+00:00",
    "summary": "Tesla hires an Intel veteran, who most recently was responsible for installing advanced tools at Intel's Arizona fab that is now ramping production of chips using 18A fabrication process."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/get-32gb-ddr5-for-less-than-usd260-in-this-b-and-h-ram-bundle-deal-for-an-amd-am5-build-save-usd119-on-this-pc-parts-kit-that-includes-a-ryzen-5-cpu-and-an-asus-b650e-motherboard",
    "domain": "AI 算力 / 半导体",
    "title": "Get 16GB DDR5 for less than $260 in this B&H RAM bundle deal for an AMD AM5 build — save $119 on this PC parts kit that includes a Ryzen 5 CPU and an Asus B650E motherboard",
    "url": "https://www.tomshardware.com/pc-components/get-32gb-ddr5-for-less-than-usd260-in-this-b-and-h-ram-bundle-deal-for-an-amd-am5-build-save-usd119-on-this-pc-parts-kit-that-includes-a-ryzen-5-cpu-and-an-asus-b650e-motherboard",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T14:01:49+00:00",
    "summary": "Save 18% on a solid AMD AM5 starter bundle with a Ryzen 5 7600X, 16GB DDR5-6000 RAM, and an Asus B650E motherboard, a solid and affordable foundation today with an easy path to future Ryzen upgrades t"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/sony-officially-kills-the-playstation-disc-ending-physical-game-production-in-2028-shutting-down-the-playstation-store-on-the-playstation-3-and-ps-vita-systems",
    "domain": "AI 算力 / 半导体",
    "title": "Sony officially kills the PlayStation disc, ending physical game production in 2028 — shutting down the PlayStation Store on the PlayStation 3 and PS Vita systems",
    "url": "https://www.tomshardware.com/video-games/playstation/sony-officially-kills-the-playstation-disc-ending-physical-game-production-in-2028-shutting-down-the-playstation-store-on-the-playstation-3-and-ps-vita-systems",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T13:56:51+00:00",
    "summary": "While Nintendo remains a holdout, this announcement essentially sounds the death knell for physical media in cutting-edge gaming."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/starlink-offers-50-percent-discount-free-hardware-rental-for-residents-surrounding-its-data-centers-move-comes-as-elon-musk-faces-lawsuits-from-residents-complaining-about-noise-and-air-pollution-from-developments",
    "domain": "AI 算力 / 半导体",
    "title": "Elon Musk offers Starlink discount to AI data center neighbors following air and noise pollution lawsuits — 50% off plans and free hardware rental",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/starlink-offers-50-percent-discount-free-hardware-rental-for-residents-surrounding-its-data-centers-move-comes-as-elon-musk-faces-lawsuits-from-residents-complaining-about-noise-and-air-pollution-from-developments",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T13:50:06+00:00",
    "summary": "SpaceXAI is trying to win residents living close to the Colossus 1 and 2 data centers by giving them discounted internet access. However, critics say that this is just a PR stunt to help win the commu"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-restores-claude-fable-5-as-us-lifts-export-controls",
    "domain": "AI 算力 / 半导体",
    "title": "Anthropic restores Claude Fable 5 as US lifts export controls — single filter now blocks prompt that could identify software vulnerabilities and write code to exploit them",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-restores-claude-fable-5-as-us-lifts-export-controls",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T11:30:51+00:00",
    "summary": "Anthropic has restored global access to Claude Fable 5, a day after the U.S. Department of Commerce withdrew the export controls."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/vpn/grab-a-massive-usd464-saving-on-a-two-year-nordvpn-subscription-with-three-extra-months-free-69-percent-saving-unlocks-this-privacy-first-vpn-service-with-scam-protection-password-manager-1tb-cloud-storage-ad-blocking-and-more",
    "domain": "AI 算力 / 半导体",
    "title": "Grab a massive $464 saving on a two-year NordVPN subscription with three extra months free — 69% saving unlocks this privacy-first VPN service with scam protection, password manager, 1TB cloud storage",
    "url": "https://www.tomshardware.com/software/vpn/grab-a-massive-usd464-saving-on-a-two-year-nordvpn-subscription-with-three-extra-months-free-69-percent-saving-unlocks-this-privacy-first-vpn-service-with-scam-protection-password-manager-1tb-cloud-storage-ad-blocking-and-more",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T11:12:36+00:00",
    "summary": "A big sale on NordVPN's top Prime package means you can save over $464 on a 2-year sub with three additional months thrown in for free."
  },
  {
    "id": "rss:https://www.eetimes.com/heat-telemetry-and-the-rise-of-the-self-aware-spacecraft/",
    "domain": "AI 算力 / 半导体",
    "title": "Heat, Telemetry, and the Rise of the Self-Aware Spacecraft",
    "url": "https://www.eetimes.com/heat-telemetry-and-the-rise-of-the-self-aware-spacecraft/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T19:54:50+00:00",
    "summary": "Satellites are getting brains...and fevers. See how telemetry, heat control, and AI are turning spacecraft into self-protecting machines. The post Heat, Telemetry, and the Rise of the Self-Aware Space"
  },
  {
    "id": "rss:https://www.eetimes.com/model-context-protocol-emerges-as-a-common-framework-for-enterprise-ai-systems/",
    "domain": "AI 算力 / 半导体",
    "title": "Model Context Protocol Emerges as a Common Framework for Enterprise AI Systems",
    "url": "https://www.eetimes.com/model-context-protocol-emerges-as-a-common-framework-for-enterprise-ai-systems/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T07:00:00+00:00",
    "summary": "MCP gives enterprise AI a common, open plumbing layer to connect models with tools, data, and agents. The post Model Context Protocol Emerges as a Common Framework for Enterprise AI Systems appeared f"
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
    "id": "rss:https://www.theverge.com/games/961203/sony-austria-thalgau-end-disc-production-microlenses-instead",
    "domain": "大厂 AI 动态",
    "title": "Sony’s PlayStation disc factory is already being repurposed",
    "url": "https://www.theverge.com/games/961203/sony-austria-thalgau-end-disc-production-microlenses-instead",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T01:05:13+00:00",
    "summary": "The video game disc is dead, and Sony's been planning to kill it for some time, according to a report out of Austria. The man who leads Sony's discmaking operations, Sony DADC president Dietmar Tanzer"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/961161/tesla-fsd-katy-tx-manslaughter-charges",
    "domain": "大厂 AI 动态",
    "title": "Tesla driver faces manslaughter charges over Texas crash that killed a woman inside her home",
    "url": "https://www.theverge.com/transportation/961161/tesla-fsd-katy-tx-manslaughter-charges",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T22:09:33+00:00",
    "summary": "The man whose Tesla struck and killed a woman inside her Texas home last month is now facing manslaughter charges, as reported earlier by The Wall Street Journal and local news outlet KHOU 11. 44-year"
  },
  {
    "id": "rss:https://www.theverge.com/tech/961086/meta-pocket-app-gizmo-ai",
    "domain": "大厂 AI 动态",
    "title": "Meta has a new app called Pocket that is absolutely nothing like the old Pocket",
    "url": "https://www.theverge.com/tech/961086/meta-pocket-app-gizmo-ai",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T21:09:06+00:00",
    "summary": "Mozilla shut down the well-loved read-it-later Pocket app last year, and now Meta is launching an app called Pocket with an entirely different, AI-focused pitch: this new app lets you make and share l"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/958906/best-july-4th-tech-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "The best July 4th sales we found so far",
    "url": "https://www.theverge.com/gadgets/958906/best-july-4th-tech-deal-sale",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T20:15:45+00:00",
    "summary": "July 4th sales are typically a precursor to what we&#8217;d see during a mid-July Prime Day, but obviously things are flipped around this year. Last week&#8217;s big Prime Day sale is over, yet there "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/960558/weber-july-4th-grill-griddle-sale-deal",
    "domain": "大厂 AI 动态",
    "title": "Weber marks down grills and griddles to their best prices ever for July 4th",
    "url": "https://www.theverge.com/gadgets/960558/weber-july-4th-grill-griddle-sale-deal",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T18:19:03+00:00",
    "summary": "If our recent Decoder interview with Weber Blackstone CEO Roger Dahle has you craving freshly grilled meats or veggies, Weber just so happens to have a variety of grills, smokers, griddles, and access"
  },
  {
    "id": "rss:https://www.theverge.com/podcast/960810/video-game-disc-dead-vergecast",
    "domain": "大厂 AI 动态",
    "title": "The video game disc is dead",
    "url": "https://www.theverge.com/podcast/960810/video-game-disc-dead-vergecast",
    "source": "David Pierce",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T16:31:09+00:00",
    "summary": "For decades, to be a gamer was to accumulate a lot of stuff. Consoles, controllers, accessories, weird VR gloves that never worked properly, but mostly the games themselves. Over the years, games have"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/960260/the-odyssey-christopher-nolan-influencers-screenings",
    "domain": "大厂 AI 动态",
    "title": "Influencer screenings aren’t going away",
    "url": "https://www.theverge.com/entertainment/960260/the-odyssey-christopher-nolan-influencers-screenings",
    "source": "Charles Pulliam-Moore",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T15:50:26+00:00",
    "summary": "For a few days, it seemed like Universal decided that there would be no advanced screenings of Christopher Nolan's The Odyssey for influencers. But on Monday, influencers sat alongside traditional cri"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/960664/godox-key-light-elgato-insta360-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Godox’s feature-packed key light is down to its best price yet",
    "url": "https://www.theverge.com/gadgets/960664/godox-key-light-elgato-insta360-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T15:00:00+00:00",
    "summary": "If you don’t want to spend $180 on the Elgato Key Light, the Godox ES45 Desktop LED Key Light is a more affordable option that offers nearly as much brightness and plenty of features, including adjust"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/957685/tesla-q2-2026-sales-production-delivery-report",
    "domain": "大厂 AI 动态",
    "title": "Tesla&#8217;s Q2 sales jump 25 percent",
    "url": "https://www.theverge.com/transportation/957685/tesla-q2-2026-sales-production-delivery-report",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T14:14:48+00:00",
    "summary": "Tesla just released its second-quarter delivery and production report, showing that the automaker is starting to recover after a particularly brutal sales year in 2025. The company said that it produc"
  },
  {
    "id": "rss:https://www.theverge.com/podcast/959792/digitas-ceo-amy-lanzi-cannes-ad-industry-marketing-ai-creators",
    "domain": "大厂 AI 动态",
    "title": "AI won’t save advertising, says Digitas’ Amy Lanzi",
    "url": "https://www.theverge.com/podcast/959792/digitas-ceo-amy-lanzi-cannes-ad-industry-marketing-ai-creators",
    "source": "Nilay Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T14:00:00+00:00",
    "summary": "We’ve got a special Decoder today — I had the chance to talk with Amy Lanzi, the CEO of Digitas North America, in front of a live audience at the Uber Villa at the Cannes Lions advertising festival in"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/02/politician-who-investigated-spyware-abuses-had-his-phone-hacked-with-pegasus-spyware/",
    "domain": "大厂 AI 动态",
    "title": "Politician who investigated spyware abuses had his phone hacked with Pegasus spyware",
    "url": "https://techcrunch.com/2026/07/02/politician-who-investigated-spyware-abuses-had-his-phone-hacked-with-pegasus-spyware/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T05:05:00+00:00",
    "summary": "A government customer of NSO Group used the company's Pegasus spyware to hack into the phone of a European politician, who at the time was serving on an EU committee tasked with investigating the spyw"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/02/last-chance-to-apply-startup-battlefield-australia-applications-close-july-6-2/",
    "domain": "大厂 AI 动态",
    "title": "Last chance to apply — Startup Battlefield Australia applications close July 6",
    "url": "https://techcrunch.com/2026/07/02/last-chance-to-apply-startup-battlefield-australia-applications-close-july-6-2/",
    "source": "Isabelle Johannessen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T00:00:00+00:00",
    "summary": "If you're going to apply for Startup Battlefield Australia, now is the time. Applications close July 6, and once the deadline passes, the opportunity is gone."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/02/mark-zuckerberg-tells-staff-that-ai-agents-havent-progressed-as-quickly-as-hed-hoped/",
    "domain": "大厂 AI 动态",
    "title": "Mark Zuckerberg tells staff that AI agents haven’t progressed as quickly as he’d hoped",
    "url": "https://techcrunch.com/2026/07/02/mark-zuckerberg-tells-staff-that-ai-agents-havent-progressed-as-quickly-as-hed-hoped/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T23:38:10+00:00",
    "summary": "At an internal meeting, the Meta CEO reportedly said that AI development efforts were not moving as quickly as anticipated."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/02/private-space-pilots-are-flying-orbital-missions-for-the-us-space-force/",
    "domain": "大厂 AI 动态",
    "title": "Private space pilots are flying orbital missions for the US Space Force",
    "url": "https://techcrunch.com/2026/07/02/private-space-pilots-are-flying-orbital-missions-for-the-us-space-force/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T23:01:06+00:00",
    "summary": "True Anomaly and Rocket Lab are performing Top Gun-style satellite fly-bys for the U.S. military."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/02/thiel-capitals-jack-selby-nabs-stakes-in-hot-startups-like-etched-through-arizona-connections/",
    "domain": "大厂 AI 动态",
    "title": "Thiel Capital’s Jack Selby nabs stakes in hot startups like Etched through Arizona connections",
    "url": "https://techcrunch.com/2026/07/02/thiel-capitals-jack-selby-nabs-stakes-in-hot-startups-like-etched-through-arizona-connections/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T21:57:10+00:00",
    "summary": "Selby's VC firm, Copper Sky Capital, is currently raising a $300 million second fund, according to a regulatory filing."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/02/iqm-europes-first-public-quantum-company-admits-the-future-of-the-tech-is-uncertain/",
    "domain": "大厂 AI 动态",
    "title": "IQM, Europe’s first public quantum company, admits the future of the tech is uncertain",
    "url": "https://techcrunch.com/2026/07/02/iqm-europes-first-public-quantum-company-admits-the-future-of-the-tech-is-uncertain/",
    "source": "Anna Heim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T20:42:48+00:00",
    "summary": "IQM, a full-stack quantum company out of Finland, went public on the Nasdaq today at a valuation of about $1.9 billion."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/02/jersey-mikes-ipo-illustrates-how-bad-the-ai-hype-has-become/",
    "domain": "大厂 AI 动态",
    "title": "Jersey Mike’s IPO illustrates how bad the AI hype has become",
    "url": "https://techcrunch.com/2026/07/02/jersey-mikes-ipo-illustrates-how-bad-the-ai-hype-has-become/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T20:11:59+00:00",
    "summary": "Just for kicks, I took a look at Jersey Mike's IPO documents. Surely a sandwich shop would have no need to mention AI. But lo and behold."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/02/a-warning-sign-about-ais-real-cost-courtesy-of-google-and-amazon/",
    "domain": "大厂 AI 动态",
    "title": "A warning sign about AI’s real cost, courtesy of Google and Amazon",
    "url": "https://techcrunch.com/2026/07/02/a-warning-sign-about-ais-real-cost-courtesy-of-google-and-amazon/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T19:14:46+00:00",
    "summary": "AI has made it a lot harder for tech companies like Amazon and Google to deliver on their net-zero pledges."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/02/meta-quietly-launches-vibe-coded-gaming-app-pocket/",
    "domain": "大厂 AI 动态",
    "title": "Meta quietly launches vibe-coded gaming app Pocket",
    "url": "https://techcrunch.com/2026/07/02/meta-quietly-launches-vibe-coded-gaming-app-pocket/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T18:44:02+00:00",
    "summary": "Meta has quietly launched Pocket, an experimental AI app that lets users generate and share interactive mini games using text prompts."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/02/travel-app-hopper-to-pay-35m-in-ftc-settlement-over-unfairly-charging-hidden-fees/",
    "domain": "大厂 AI 动态",
    "title": "Travel app Hopper to pay $35M in FTC settlement over ‘unfairly’ charging hidden fees",
    "url": "https://techcrunch.com/2026/07/02/travel-app-hopper-to-pay-35m-in-ftc-settlement-over-unfairly-charging-hidden-fees/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T18:39:14+00:00",
    "summary": "Hopper will pay $35 million to settle FTC allegations that it used deceptive “dark patterns” to hide fees and mislead travelers about the costs and benefits of services."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/02/anthropic-is-discussing-a-new-custom-chip-with-samsung/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic is discussing a new custom chip with Samsung",
    "url": "https://techcrunch.com/2026/07/02/anthropic-is-discussing-a-new-custom-chip-with-samsung/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T18:31:09+00:00",
    "summary": "The news comes about a week after OpenAI announced its own custom AI chip in a partnership with Broadcom."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/02/boeing-owned-wisk-aero-accused-of-firing-manager-who-raised-safety-concerns/",
    "domain": "大厂 AI 动态",
    "title": "Boeing-owned Wisk Aero accused of firing manager who raised safety concerns",
    "url": "https://techcrunch.com/2026/07/02/boeing-owned-wisk-aero-accused-of-firing-manager-who-raised-safety-concerns/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T17:30:04+00:00",
    "summary": "A former software manager claims Wisk rushed software testing ahead of a crucial 2025 flight test."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/02/melinda-gates-venture-firm-backs-magnify-ventures-46-6m-fund-ii/",
    "domain": "大厂 AI 动态",
    "title": "Melinda Gates’ venture firm backs Magnify Ventures’ $46.6M Fund II",
    "url": "https://techcrunch.com/2026/07/02/melinda-gates-venture-firm-backs-magnify-ventures-46-6m-fund-ii/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T15:26:43+00:00",
    "summary": "Early-stage firm Magnify Ventures has raised a $46.6 million Fund II from LPs, including Melinda French Gates’ Pivotal Ventures."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/02/openai-proposed-donating-5-of-its-equity-to-a-us-sovereign-wealth-fund/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI proposed donating 5% of its equity to a US sovereign wealth fund",
    "url": "https://techcrunch.com/2026/07/02/openai-proposed-donating-5-of-its-equity-to-a-us-sovereign-wealth-fund/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T15:20:51+00:00",
    "summary": "OpenAI CEO Sam Altman has reportedly proposed giving 5% of the company’s equity to a U.S. sovereign wealth fund, reviving discussions about letting the public share in the financial gains from the AI "
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/02/popular-tv-tracking-app-tv-time-is-shutting-down-as-company-focuses-on-ai/",
    "domain": "大厂 AI 动态",
    "title": "Popular TV-tracking app TV Time is shutting down as company focuses on AI",
    "url": "https://techcrunch.com/2026/07/02/popular-tv-tracking-app-tv-time-is-shutting-down-as-company-focuses-on-ai/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T15:14:03+00:00",
    "summary": "TV Time, the popular TV-tracking app, is shutting down on July 15 as parent company Whip Media pivots toward enterprise AI products."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/02/lucid-motors-cfo-is-out-as-its-new-ceo-continues-leadership-shakeup/",
    "domain": "大厂 AI 动态",
    "title": "Lucid Motors’ CFO is out as its new CEO continues leadership shakeup",
    "url": "https://techcrunch.com/2026/07/02/lucid-motors-cfo-is-out-as-its-new-ceo-continues-leadership-shakeup/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T14:53:39+00:00",
    "summary": "The company announced a new slate of executive hires meant to help turn things around, as Gravity SUV sales are not taking off as expected."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/02/us-government-says-it-got-hacked-again/",
    "domain": "大厂 AI 动态",
    "title": "US government says it got hacked — again",
    "url": "https://techcrunch.com/2026/07/02/us-government-says-it-got-hacked-again/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T14:22:36+00:00",
    "summary": "A top Democrat on the Senate's Intelligence Committee warned that the information accessed on a Homeland Security intelligence-sharing network may risk national security."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft launches its own AI deployment company with $2.5 billion commitment",
    "url": "https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T13:53:00+00:00",
    "summary": "Microsoft follows Amazon, OpenAI, and Anthropic with its new AI deployment group."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/02/tesla-saw-a-massive-sales-jump-in-the-second-quarter/",
    "domain": "大厂 AI 动态",
    "title": "Tesla saw a massive sales jump in the second quarter",
    "url": "https://techcrunch.com/2026/07/02/tesla-saw-a-massive-sales-jump-in-the-second-quarter/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T13:20:15+00:00",
    "summary": "The company delivered more than 480,000 EVs globally, seemingly thanks to geographic expansion and cheaper versions of the Model 3, Model Y, and Cybertruck."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/02/rivian-thinks-it-will-sell-more-evs-than-expected-this-year/",
    "domain": "大厂 AI 动态",
    "title": "Rivian raises EV sales forecast as Q2 production ramps up",
    "url": "https://techcrunch.com/2026/07/02/rivian-thinks-it-will-sell-more-evs-than-expected-this-year/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T12:30:00+00:00",
    "summary": "The company now expects to ship a few thousand more vehicles by the end of 2026 than it previously expected, after launching its R2 SUV last month."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/07/new-pamstealer-macos-malware-uses-clever-tradecraft-to-remain-stealthy/",
    "domain": "大厂 AI 动态",
    "title": "Newly discovered PamStealer isn't your typical macOS malware",
    "url": "https://arstechnica.com/security/2026/07/new-pamstealer-macos-malware-uses-clever-tradecraft-to-remain-stealthy/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T19:38:57+00:00",
    "summary": "The discovery underscores the increased effort being poured into Mac infostealers."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/07/faa-proposal-supersonic-airliners-can-fly-over-us-cities-if-theyre-quiet/",
    "domain": "大厂 AI 动态",
    "title": "FAA proposal: Supersonic airliners can fly over US cities if they’re quiet",
    "url": "https://arstechnica.com/gadgets/2026/07/faa-proposal-supersonic-airliners-can-fly-over-us-cities-if-theyre-quiet/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T17:29:37+00:00",
    "summary": "New US rules would legalize quiet supersonic flights without the sonic boom."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/07/ars-live-recap-when-are-the-big-rockets-nasa-desperately-needs-going-to-be-ready/",
    "domain": "大厂 AI 动态",
    "title": "Ars Live recap: When are the big rockets NASA desperately needs going to be ready?",
    "url": "https://arstechnica.com/space/2026/07/ars-live-recap-when-are-the-big-rockets-nasa-desperately-needs-going-to-be-ready/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T16:46:47+00:00",
    "summary": "I have not seen anyone put out a date for a new rocket, and actually hit it."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/07/250-used-to-get-you-a-lifetime-plex-pass-now-you-get-a-five-year-subscription/",
    "domain": "大厂 AI 动态",
    "title": "Plex debuts 5-year membership pass for $250",
    "url": "https://arstechnica.com/gadgets/2026/07/250-used-to-get-you-a-lifetime-plex-pass-now-you-get-a-five-year-subscription/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T16:35:59+00:00",
    "summary": "Plex is pushing customers to newer features and more frequent payments."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/07/africa-cdc-confirms-marburg-case-in-uganda-as-ebola-outbreak-rages/",
    "domain": "大厂 AI 动态",
    "title": "Africa CDC confirms Marburg case in Uganda as Ebola outbreak rages",
    "url": "https://arstechnica.com/health/2026/07/africa-cdc-confirms-marburg-case-in-uganda-as-ebola-outbreak-rages/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T16:30:37+00:00",
    "summary": "Early reports indicate there may be another case, but spread is thought to be localized."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/artificial-cell-manages-a-few-rounds-of-cell-division/",
    "domain": "大厂 AI 动态",
    "title": "Artificial cell manages a few rounds of cell division",
    "url": "https://arstechnica.com/science/2026/07/artificial-cell-manages-a-few-rounds-of-cell-division/",
    "source": "John Timmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T16:21:23+00:00",
    "summary": "It only works for a few divisions thanks to a lot of added materials."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/07/google-loses-long-running-appeal-of-record-eu-fine-will-have-to-cough-up-4-7-billion/",
    "domain": "大厂 AI 动态",
    "title": "Google loses long-running appeal of record EU fine, will have to cough up $4.7 billion",
    "url": "https://arstechnica.com/gadgets/2026/07/google-loses-long-running-appeal-of-record-eu-fine-will-have-to-cough-up-4-7-billion/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T16:15:41+00:00",
    "summary": "The EU went after Google for the practice of bundling its search engine and browser with Android."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/openai-floats-giving-us-5-stake-to-win-over-ai-haters/",
    "domain": "大厂 AI 动态",
    "title": "Trump gets OpenAI to offer US 5% stake, far lower than Sanders’ target",
    "url": "https://arstechnica.com/tech-policy/2026/07/openai-floats-giving-us-5-stake-to-win-over-ai-haters/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T15:12:25+00:00",
    "summary": "Insiders say Sam Altman is in active talks with the Trump administration."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/musks-x-poses-serious-risk-to-americans-privacy-advocates-warn-ftc/",
    "domain": "大厂 AI 动态",
    "title": "Musk’s X poses “serious risk to Americans’ privacy,” advocates warn FTC",
    "url": "https://arstechnica.com/tech-policy/2026/07/musks-x-poses-serious-risk-to-americans-privacy-advocates-warn-ftc/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T14:39:17+00:00",
    "summary": "FTC urged to reject Elon Musk’s bid to end X monitoring amid AI concerns."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/07/tesla-sales-increase-by-25-in-q2-2026/",
    "domain": "大厂 AI 动态",
    "title": "Tesla sales increase by 25% in Q2 2026",
    "url": "https://arstechnica.com/cars/2026/07/tesla-sales-increase-by-25-in-q2-2026/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T14:11:07+00:00",
    "summary": "Deliveries outstripped production, suggesting Tesla has cleared some inventory."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/07/womans-puzzling-decline-turns-out-to-be-cobalt-poisoning-from-hip-replacement/",
    "domain": "大厂 AI 动态",
    "title": "Woman's hip replacement disintegrates, causing severe metal poisoning",
    "url": "https://arstechnica.com/health/2026/07/womans-puzzling-decline-turns-out-to-be-cobalt-poisoning-from-hip-replacement/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T14:04:28+00:00",
    "summary": "Doctors find grey fluid and dead, metallic flesh inside poisoned woman's hip."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/07/googles-ai-buildout-drove-37-increase-in-electricity-use-in-2025/",
    "domain": "大厂 AI 动态",
    "title": "Google’s AI buildout drove 37% increase in electricity use in 2025",
    "url": "https://arstechnica.com/ai/2026/07/googles-ai-buildout-drove-37-increase-in-electricity-use-in-2025/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T11:15:49+00:00",
    "summary": "Google tries balancing AI data center emissions with clean energy efforts."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/editorial-the-most-important-thing-you-can-do-to-protect-science/",
    "domain": "大厂 AI 动态",
    "title": "Editorial: It's time to step up and have your say for science",
    "url": "https://arstechnica.com/science/2026/07/editorial-the-most-important-thing-you-can-do-to-protect-science/",
    "source": "John Timmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T10:00:27+00:00",
    "summary": "Your comments on a dangerous rule putting politicals in charge of science can matter."
  },
  {
    "id": "rss:https://arstechnica.com/information-technology/2026/07/t-mobile-moving-tens-of-thousands-of-virtual-machines-off-vmware-amid-lawsuit/",
    "domain": "大厂 AI 动态",
    "title": "T-Mobile moving tens of thousands of virtual machines off VMware amid lawsuit",
    "url": "https://arstechnica.com/information-technology/2026/07/t-mobile-moving-tens-of-thousands-of-virtual-machines-off-vmware-amid-lawsuit/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T21:21:21+00:00",
    "summary": "T-Mobile wants Broadcom to keep supporting its VMware perpetual licenses."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/07/nasa-chief-praises-progress-blue-origin-is-making-after-launch-failure/",
    "domain": "大厂 AI 动态",
    "title": "NASA chief praises progress Blue Origin is making after launch failure",
    "url": "https://arstechnica.com/space/2026/07/nasa-chief-praises-progress-blue-origin-is-making-after-launch-failure/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T19:57:36+00:00",
    "summary": "\"We've got time into 2027 before we're getting nervous.\""
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/us-home-battery-installations-hit-record-high-in-early-2026/",
    "domain": "大厂 AI 动态",
    "title": "US home battery installations hit record high on rising electricity costs",
    "url": "https://arstechnica.com/science/2026/07/us-home-battery-installations-hit-record-high-in-early-2026/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T19:11:15+00:00",
    "summary": "Record home battery installations unlock options for grids—and AI data centers."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/museums-could-use-ravenous-superworms-to-clean-skeletons/",
    "domain": "大厂 AI 动态",
    "title": "Superworms could replace beetles for cleaning skeletal remains",
    "url": "https://arstechnica.com/science/2026/07/museums-could-use-ravenous-superworms-to-clean-skeletons/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T18:59:21+00:00",
    "summary": "An optimal ratio of 10-15 grams of larvae per gram of specimen minimized cleaning time with no bone damage."
  },
  {
    "id": "rss:https://arstechnica.com/gaming/2026/07/sony-will-stop-making-physical-copies-of-playstation-games-in-2028/",
    "domain": "大厂 AI 动态",
    "title": "Sony announces end of PlayStation discs, parts of digital store in the same day",
    "url": "https://arstechnica.com/gaming/2026/07/sony-will-stop-making-physical-copies-of-playstation-games-in-2028/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T18:41:49+00:00",
    "summary": "“We will own nothing, it's truly sad.”"
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/07/the-volvo-ex30-cross-country-review-a-victim-of-geopolitics/",
    "domain": "大厂 AI 动态",
    "title": "A good little EV you won't be able to buy soon: The Volvo EX30 Cross Country",
    "url": "https://arstechnica.com/cars/2026/07/the-volvo-ex30-cross-country-review-a-victim-of-geopolitics/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T18:24:04+00:00",
    "summary": "Tariffs and anti-China policies killed this little Volvo in the United States."
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/07/ithacas-king-defies-the-gods-in-final-the-odyssey-trailer/",
    "domain": "大厂 AI 动态",
    "title": "Ithaca's king defies the gods in final The Odyssey trailer",
    "url": "https://arstechnica.com/culture/2026/07/ithacas-king-defies-the-gods-in-final-the-odyssey-trailer/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T16:58:30+00:00",
    "summary": "\"You gods don't speak in ways we understand.\""
  },
  {
    "id": "wscn:3776134",
    "domain": "股票",
    "title": "Meta算力过剩疑云背后：扎克伯格说AI进展慢了，AI负责人新模型说已追上GPT-5.5",
    "url": "https://wallstreetcn.com/articles/3776134",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T06:23:31+00:00",
    "summary": "Meta“卖算力”原因曝光？扎克伯格承认AI智能体过去四个月进展慢于预期，然而AI负责人Alexandr Wang同一时间透露，代号“西瓜”的新模型已在基准测试上追上OpenAI的GPT-5.5，且算力投入比上一代高出一个数量级。Meta算力到底过没过剩？争议还在继续。"
  },
  {
    "id": "wscn:3776136",
    "domain": "股票",
    "title": "铠侠第十代NAND送样、CEO喊话“需求依然旺盛，或增加资本支出”，股价深V大反弹！",
    "url": "https://wallstreetcn.com/articles/3776136",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T06:22:54+00:00",
    "summary": "更多消息，持续更新中"
  },
  {
    "id": "wscn:3776132",
    "domain": "股票",
    "title": "报道：三星电子第三季度DRAM价格将上调至多20%",
    "url": "https://wallstreetcn.com/articles/3776132",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T05:37:37+00:00",
    "summary": "三星电子正对客户展开强硬价格谈判，目标将第三季度通用DRAM及LPDDR均价最高上调20%以上——此前两个季度涨幅已高达90%和50%。AI基础设施投资持续升温、长期供应协议加速锁价，多重结构性因素叠加，内存厂商高盈利有望延续至明年。"
  },
  {
    "id": "wscn:3776124",
    "domain": "股票",
    "title": "AI情绪逆转！日韩股市大反弹，韩股涨5%触发熔断、三星涨9%，金铜拉涨",
    "url": "https://wallstreetcn.com/articles/3776124",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T05:21:58+00:00",
    "summary": "AI情绪急速逆转，日韩股市上演惊天V型反转——韩国KOSPI一度跌超3%，最终暴涨5%并触发熔断；三星电子涨近9%，铠侠涨超10%，此前一度跌超12%。导火索直指Anthropic与三星定制AI芯片洽谈传闻。与此同时，美就业数据疲软压低加息预期，铜价、黄金齐涨。"
  },
  {
    "id": "wscn:3776069",
    "domain": "股票",
    "title": "从5万到10亿，对话“期货天王”傅海棠：亲历市场激荡二十六年，穿越周期靠什么?",
    "url": "https://wallstreetcn.com/articles/3776069",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T04:54:53+00:00",
    "summary": "从“5万到1.2亿”的投研框架：什么才是投资的“正道”"
  },
  {
    "id": "wscn:3776131",
    "domain": "股票",
    "title": "杠杆ETF规模一年暴涨431%，韩国国会启动制度整改讨论",
    "url": "https://wallstreetcn.com/articles/3776131",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T04:07:45+00:00",
    "summary": "韩国共同民主党特委将于6日召开内部闭门审查会议，启动资本市场政策审查，重点调查单一股票杠杆ETF监管问题。三星电子、SK海力士杠杆ETF上市后规模急速膨胀，被指加剧市场波动、损害散户利益。金融监督院院长公开承认政策失误，党内已就收紧监管形成共识，拟从零审视监管框架。"
  },
  {
    "id": "wscn:3776072",
    "domain": "股票",
    "title": "风口浪尖的光芯片：产能仍然紧缺，叙事却为何开始松动？",
    "url": "https://wallstreetcn.com/premium/articles/3776072?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T03:38:15+00:00",
    "summary": "光芯片正从光模块的“辅助器件”跃升为AI算力产业链的“核心瓶颈”，高端EML/CW激光器供需缺口超30%，订单排至2028年，光芯片行业正迎来量价齐升的最强景气周期。"
  },
  {
    "id": "wscn:3776125",
    "domain": "股票",
    "title": "中国6月RatingDog服务业PMI 54.1，新业务出口创年内新高",
    "url": "https://wallstreetcn.com/articles/3776125",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T03:01:20+00:00",
    "summary": "中国RatingDog6月服务业PMI54.1，虽较5月高点微幅回落，仍位居近三年第三高位。新业务出口增速创年内新高，销售价格在沉寂两月后强势重返扩张，涨幅为逾一年最强；就业连续两月扩张，增速刷新2024年7月以来纪录，服务业复苏动能正加速积聚。"
  },
  {
    "id": "wscn:3776126",
    "domain": "股票",
    "title": "非农“哑火”，花旗：加息理由已“不复存在”，预计美联储10月重启降息",
    "url": "https://wallstreetcn.com/articles/3776126",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T02:52:11+00:00",
    "summary": "花旗认为，6月美国非农就业仅新增5.7万人，远低预期，近三月均值骤降至11.1万人；失业率下降\"虚有其表\"，实则源于劳动参与率骤跌。\"加息理由已消失\"——油价回落、薪资降温、核心PCE或被下修20至30基点，多重通胀压力同步消退。美联储将于10月重启降息，年底前再降一次，利率区间落至3.0%至3.25%。"
  },
  {
    "id": "wscn:3776128",
    "domain": "股票",
    "title": "BAT全上车，快手可灵AI投后估值达到180亿美元",
    "url": "https://wallstreetcn.com/articles/3776128",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T02:45:41+00:00",
    "summary": "投后估值已相当于快手整体市值的约76%"
  },
  {
    "id": "wscn:3776121",
    "domain": "股票",
    "title": "韩国AI大跃进",
    "url": "https://wallstreetcn.com/articles/3776121",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T02:13:56+00:00",
    "summary": "韩国总统李在明向两位曾身陷囹圄的财阀掌门人鞠躬致敬，背后是一场豪赌——三星与SK未来十年合计投入21万亿元人民币，押注AI、半导体与能源基础设施。这是半个世纪前朴正熙\"重化工业宣言\"的现代版本，却藏着一个关键差异：这一次，财阀砸下的是真金白银的经营利润，而非政府担保的银行信贷。繁荣已在路上，但1997年的教训从未走远。"
  },
  {
    "id": "wscn:3776123",
    "domain": "股票",
    "title": "SemiAnalysis驳斥“算力过剩论”：Meta算力扩张远超想象，明年资本开支将“高得惊人”",
    "url": "https://wallstreetcn.com/articles/3776123",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T02:01:08+00:00",
    "summary": "Meta今年上半年已签约超5GW数据中心容量，预计明年资本开支将“高得惊人”，SemiAnalysis认为市场对“算力过剩”的担忧是误判。更关键的是，Meta手握AI模型、广告扩容、API服务与高溢价短期租赁四大变现王牌，每一GW算力都有高价值出口，让Meta的算力投资进可攻退可守。"
  },
  {
    "id": "wscn:3775708",
    "domain": "股票",
    "title": "霍尔木兹海峡加速重启，原油跌势是否已接近尾声？",
    "url": "https://wallstreetcn.com/premium/articles/3775708?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T02:01:00+00:00",
    "summary": "霍尔木兹海峡复航致供应激增，油价暴跌，但库存偏低、补库及欧佩克减产将限制跌幅，跌势或近尾声。"
  },
  {
    "id": "wscn:3776119",
    "domain": "股票",
    "title": "高盛对冲基金主管的“半年度总结”：这种情况以前只发生过一次",
    "url": "https://wallstreetcn.com/articles/3776119",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T01:18:08+00:00",
    "summary": "标普500上半年录得约10%回报，若年末守住7530点，将创68年指数史上第二次连续四年两位数回报纪录。AI基础设施浪潮席卷全球，内存板块狂飙250%，北亚股市集体爆发；\"七巨头\"却意外原地踏步，其余493只成分股反涨16%。高盛警示：AI估值需越来越乐观的假设支撑，监管黑天鹅正悄然逼近。"
  },
  {
    "id": "wscn:3776118",
    "domain": "股票",
    "title": "“AI鬼故事”不断！“老牌PE”黑石意外退出“全球最大数据中心园区”",
    "url": "https://wallstreetcn.com/articles/3776118",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T01:09:15+00:00",
    "summary": "黑石旗下QTS Realty Trust宣布放弃弗吉尼亚州\"数字门户\"项目，这一原规划投资逾1000亿美元、占地2100英亩的全球最大数据中心园区计划就此终结。此前合作方Compass Datacenters已于5月撤出，法律诉讼与社区反对是主因。"
  },
  {
    "id": "wscn:3776113",
    "domain": "股票",
    "title": "海事史上最大豪赌！美伊战前70亿美元“囤积”超级油轮，这位韩国大亨赚翻了",
    "url": "https://wallstreetcn.com/articles/3776113",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T00:37:24+00:00",
    "summary": "韩国航运大亨Ga-Hyun Chung在美以攻击伊朗前，斥资约70亿美元大举购买油轮，其公司Sinokor由此掌控全球约10%的VLCC。霍尔木兹海峡封闭后，VLCC日租金在今年3月飙升至逾38.5万美元，创Clarksons自2000年以来最高纪录。随着海峡重新开放，油轮需求再度升温，这位低调大亨有望再度获益。"
  },
  {
    "id": "wscn:3776068",
    "domain": "股票",
    "title": "工业母机：需求复苏只是开始，国产替代才是真正的α",
    "url": "https://wallstreetcn.com/premium/articles/3776068?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T00:36:29+00:00",
    "summary": "工业母机产业正处于“周期向上”、“高端供给受限”、“AI结构增量”的三重共振窗口期。"
  },
  {
    "id": "wscn:3776111",
    "domain": "股票",
    "title": "“掌控”美联储，特朗普一直没放弃",
    "url": "https://wallstreetcn.com/articles/3776111",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T00:34:40+00:00",
    "summary": "美最高法院虽以程序瑕疵为由阻止特朗普解雇理事库克，但白宫将此视为操作指引，宣布启动新一轮合规罢免程序。鲍威尔理事留任亦令特朗普不满，特朗普盟友正寄望于监察长报告或其他途径，推动鲍威尔离开。与此同时，白宫借亚特兰大联储行长空缺积极布局人事渗透。"
  },
  {
    "id": "wscn:3776117",
    "domain": "股票",
    "title": "德国宣布“全面经济改革计划”，包括“提高退休年龄，放宽企业裁员管制”，总理：“我理解人们对过去的怀念，但我们不能躲在过去”",
    "url": "https://wallstreetcn.com/articles/3776117",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T00:28:39+00:00",
    "summary": "德国推出涵盖34项措施的经济改革方案，涉及减税、退休年龄从67岁提高至70岁、放宽企业裁员管制及大幅精简官僚程序。总理默茨表示“不能躲在过去”。商界反应不一，部分行业协会认为力度不足。改革同时也是总理默茨在支持率持续下滑背景下的政治豪赌。"
  },
  {
    "id": "wscn:3776112",
    "domain": "股票",
    "title": "华尔街对下半年“乐观得很一致”：相信市场会“克服一切”",
    "url": "https://wallstreetcn.com/articles/3776112",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T00:27:57+00:00",
    "summary": "历经地缘冲突与利率剧震，华尔街以罕见一致的乐观姿态迎接下半年。然而好消息或已尽数定价——策略师预测标普年末仅余约3%上行空间。核心争议不在涨跌方向，而在AI红利能否从芯片硬件向电网、工业等实体经济真正扩散。"
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
  },
  {
    "id": "rss:https://www.netinterest.co/p/two-tribes",
    "domain": "股票",
    "title": "Two Tribes",
    "url": "https://www.netinterest.co/p/two-tribes",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-02-27T17:42:58+00:00",
    "summary": "Private Credit, Public Markets and the AI Reckoning"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.01550",
    "domain": "金融",
    "title": "Is Trend Still Your Friend?: A Microstructural Account of the Demise of Short-Term Trend-Following",
    "url": "https://arxiv.org/abs/2607.01550",
    "source": "Jutta G. Kurth, Zoltan Eisler, Adam Rej, Jean-Philippe Bouchaud",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T04:00:00+00:00",
    "summary": "arXiv:2607.01550v1 Announce Type: new Abstract: Systematic trend following has, on average, been profitable for at least two centuries; yet since approximately 2009, short-term trends have ceased to d"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.01561",
    "domain": "金融",
    "title": "Decomposing Wage Stagnation: Employment Reallocation, Wage Structure,and Demographics",
    "url": "https://arxiv.org/abs/2607.01561",
    "source": "Ken Yamada",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T04:00:00+00:00",
    "summary": "arXiv:2607.01561v1 Announce Type: new Abstract: Average wages in Japan rose until the mid-1990s but stagnated thereafter. This paper studies Japan's long-run wage stagnation by decomposing changes in "
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.01705",
    "domain": "金融",
    "title": "Portfolio Optimization under Fast and Slow Latent Mean-Reverting and Momentum Drift",
    "url": "https://arxiv.org/abs/2607.01705",
    "source": "Dannin J. Eccles, Roger Lee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T04:00:00+00:00",
    "summary": "arXiv:2607.01705v1 Announce Type: new Abstract: We consider a class of partial-information portfolio optimization problems in which the drift of a risky asset is driven by two latent stochastic factor"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.01765",
    "domain": "金融",
    "title": "A Cap-Axis Integral Diagnostic of Factor Models",
    "url": "https://arxiv.org/abs/2607.01765",
    "source": "Useong Shin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T04:00:00+00:00",
    "summary": "arXiv:2607.01765v1 Announce Type: new Abstract: I propose a cap-axis integral diagnostic for factor-model evaluation. Low-dimensional factor models can improve the maximum-Sharpe frontier while leavin"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.01254",
    "domain": "金融",
    "title": "The Benchmark Ceiling: Human Judgment, Evaluation Scarcity, and the Political Economy of AI Capability Measurement",
    "url": "https://arxiv.org/abs/2607.01254",
    "source": "Mark Esposito, Liu Zhang, Ali Ansari",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T04:00:00+00:00",
    "summary": "arXiv:2607.01254v1 Announce Type: cross Abstract: Benchmarks are the primary instruments through which AI capability is measured, compared, and governed. This paper argues that the validity of frontie"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.01377",
    "domain": "金融",
    "title": "Liquidity Premium and Investment Horizons",
    "url": "https://arxiv.org/abs/2607.01377",
    "source": "Irene Aldridge",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T04:00:00+00:00",
    "summary": "arXiv:2607.01377v1 Announce Type: cross Abstract: We estimate Kyle's (1985) price-impact coefficient $\\lambda$ directly from daily equity order flow and test its ability to forecast the cross-section "
  },
  {
    "id": "rss:https://arxiv.org/abs/2107.01730",
    "domain": "金融",
    "title": "Asymptotic Analysis of Risk Premia Under Linear Risk Sharing with Law-Invariant Risk Measures",
    "url": "https://arxiv.org/abs/2107.01730",
    "source": "Thomas Knispel, Roger J. A. Laeven, Gregor Svindland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T04:00:00+00:00",
    "summary": "arXiv:2107.01730v3 Announce Type: replace Abstract: We investigate the asymptotic behavior of the risk premium associated with a linear risk sharing contract in an infinitely expanding risk pool. We c"
  },
  {
    "id": "rss:https://arxiv.org/abs/2409.13070",
    "domain": "金融",
    "title": "Heat modulated affine stochastic volatility models for forward curve dynamics",
    "url": "https://arxiv.org/abs/2409.13070",
    "source": "Sven Karbach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T04:00:00+00:00",
    "summary": "arXiv:2409.13070v2 Announce Type: replace Abstract: We present a function-valued stochastic volatility model designed to capture the continuous-time evolution of forward curves in fixed-income or comm"
  },
  {
    "id": "rss:https://arxiv.org/abs/2410.01114",
    "domain": "金融",
    "title": "Attribution and Persuasion: The Paradox of Interpretable AI",
    "url": "https://arxiv.org/abs/2410.01114",
    "source": "Hanzhe Li, Jin Li, Ye Luo, Xiaowei Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T04:00:00+00:00",
    "summary": "arXiv:2410.01114v3 Announce Type: replace Abstract: This paper studies AI persuasion by distinguishing between two reasons for disagreement: attention differences, where the AI detects features the de"
  },
  {
    "id": "rss:https://arxiv.org/abs/2503.09083",
    "domain": "金融",
    "title": "Impact of Engagement Allocation Across Social Platform Modalities on E-Commerce Performance",
    "url": "https://arxiv.org/abs/2503.09083",
    "source": "Xiaoning Wang, Yakov Bart, Serguei Netessine, Lynn Wu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T04:00:00+00:00",
    "summary": "arXiv:2503.09083v2 Announce Type: replace Abstract: Firms increasingly operate across multiple social media platforms, yet it remains unclear whether diversifying engagement across platforms enhances "
  },
  {
    "id": "rss:https://arxiv.org/abs/2503.19089",
    "domain": "金融",
    "title": "Cursed Job Market Signaling",
    "url": "https://arxiv.org/abs/2503.19089",
    "source": "Po-Hsuan Lin, Yen Ling Tan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T04:00:00+00:00",
    "summary": "arXiv:2503.19089v4 Announce Type: replace Abstract: We study how cursedness, the tendency to neglect how other people's strategies depend on their private information, affects information transmission"
  },
  {
    "id": "rss:https://arxiv.org/abs/2505.11599",
    "domain": "金融",
    "title": "Can LLMs Credibly Transform the Creation of Panel Data from Diverse Historical Tables?",
    "url": "https://arxiv.org/abs/2505.11599",
    "source": "Ver\\'onica B\\\"acker-Peral, Vitaly Meursault, Christopher Severen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T04:00:00+00:00",
    "summary": "arXiv:2505.11599v2 Announce Type: replace Abstract: Multimodal LLMs offer the potential for a watershed change for the digitization of historical tables by enabling low-cost processing that is centere"
  },
  {
    "id": "rss:https://arxiv.org/abs/2511.05438",
    "domain": "金融",
    "title": "Impacts of large-scale food fortification on the cost of nutrient-adequate diets: a modeling study in 89 countries",
    "url": "https://arxiv.org/abs/2511.05438",
    "source": "Leah Costlow, Yan Bai, Katherine P. Adams, Ty Beal, Kathryn G. Dewey, Christopher M. Free, Valerie M. Friesen, Mduduzi N. N. Mbuya, Stella Nordhagen, Florencia C. Vasta, William A. Masters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T04:00:00+00:00",
    "summary": "arXiv:2511.05438v2 Announce Type: replace Abstract: Large-scale food fortification (LSFF) is a widely accepted intervention to alleviate micronutrient deficiencies, yet policy implementation is often "
  },
  {
    "id": "rss:https://arxiv.org/abs/2603.03152",
    "domain": "金融",
    "title": "Political Shocks and Price Discovery in Prediction Markets: Evidence from the 2024 U.S. Presidential Election",
    "url": "https://arxiv.org/abs/2603.03152",
    "source": "Kwok Ping Tsang, Zichao Yang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T04:00:00+00:00",
    "summary": "arXiv:2603.03152v3 Announce Type: replace Abstract: Using transaction-level matched trades from Polymarket's 2024 U.S. presidential election market, we study how traders and prices respond to three pr"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.08765",
    "domain": "金融",
    "title": "Reliability-Aware ETF Tail-Risk Monitoring",
    "url": "https://arxiv.org/abs/2604.08765",
    "source": "Tenghan Zhong, Keyuan Wu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T04:00:00+00:00",
    "summary": "arXiv:2604.08765v3 Announce Type: replace Abstract: Daily ETF risk monitoring can become unreliable when market data quality degrades, market conditions shift, or predictive performance becomes unstab"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.10402",
    "domain": "金融",
    "title": "Risk-Sensitive Specialist Routing for Volatility Forecasting",
    "url": "https://arxiv.org/abs/2604.10402",
    "source": "Tenghan Zhong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T04:00:00+00:00",
    "summary": "arXiv:2604.10402v4 Announce Type: replace Abstract: Volatility forecasting becomes challenging when market conditions shift and model performance varies across market states. Motivated by this instabi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.29056",
    "domain": "金融",
    "title": "Green Transformational Leadership and Sustainable Nursing Practices: Evidence from the Healthcare Sector",
    "url": "https://arxiv.org/abs/2606.29056",
    "source": "Thabit Atobishi, Saeed Nosratabadi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T04:00:00+00:00",
    "summary": "arXiv:2606.29056v2 Announce Type: replace Abstract: The healthcare sector contributes approximately 4.4% of global greenhouse gas emissions, yet research on the organizational determinants of sustaina"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.00551",
    "domain": "金融",
    "title": "Talking Politics with Artificial Intelligence",
    "url": "https://arxiv.org/abs/2607.00551",
    "source": "Ziwen Zu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T04:00:00+00:00",
    "summary": "arXiv:2607.00551v2 Announce Type: replace Abstract: Large language models (LLMs), a prominent form of artificial intelligence (AI), are becoming everyday interfaces for political questions, but most e"
  },
  {
    "id": "rss:https://arxiv.org/abs/2601.14534",
    "domain": "金融",
    "title": "The Algorithmic Barrier: A Framework for Artificial Frictional Unemployment and Information Asymmetry in Automated Recruitment Systems",
    "url": "https://arxiv.org/abs/2601.14534",
    "source": "Ibrahim Denis Fofanah",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T04:00:00+00:00",
    "summary": "arXiv:2601.14534v2 Announce Type: replace-cross Abstract: The United States labor market has entered a period in which high job vacancy rates and prolonged unemployment persist together. Classical the"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.10005",
    "domain": "金融",
    "title": "What Happens When Institutional Liquidity Enters Prediction Markets: Identification, Measurement, and a Synthetic Proof of Concept",
    "url": "https://arxiv.org/abs/2604.10005",
    "source": "Shaw Dalen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T04:00:00+00:00",
    "summary": "arXiv:2604.10005v3 Announce Type: replace-cross Abstract: Prediction markets are starting to look less like crowd polls and more like electronic markets. The central question is therefore no longer on"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.08998",
    "domain": "金融",
    "title": "The Token Not Taken: Sampling, State, and the Stochasticity of AI Agents",
    "url": "https://arxiv.org/abs/2606.08998",
    "source": "Muhammad Zia Hydari, Raja Iqbal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T04:00:00+00:00",
    "summary": "arXiv:2606.08998v3 Announce Type: replace-cross Abstract: Agentic AI systems can behave differently across runs: the same request may produce a different plan, a different tool call, a different code "
  }
]
```
