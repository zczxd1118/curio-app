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

- 今日日期：`2026-07-16`
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
  "date": "2026-07-16",
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
    "points": 3781743,
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
    "points": 1515761,
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
    "points": 1233838,
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
    "points": 976013,
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
    "points": 941691,
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
    "points": 896979,
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
    "points": 870513,
    "published_at": "2026-06-09T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“VibeCoding”免费获取\n【课程简介】从零开始，用自然语言指挥AI开发真实软件项目！"
  },
  {
    "id": "bvid:BV1aDMezREUj",
    "domain": "AI",
    "title": "Cursor使用教程，2小时玩转cursor，cursor无限续杯",
    "url": "http://www.bilibili.com/video/av114691716154833",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 579215,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 530462,
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
    "points": 472865,
    "published_at": "2026-05-31T09:46:57+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1AnQNYxEsy",
    "domain": "AI",
    "title": "MCP是啥？技术原理是什么？一个视频搞懂MCP的一切。Windows系统配置MCP，Cursor Cline使用MCP",
    "url": "http://www.bilibili.com/video/av114155298228756",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 417409,
    "published_at": "2025-03-13T13:18:09+00:00",
    "summary": "MCP是近期的AI领域的热点，特别是在海外社区获得热烈讨论，每天都有大量MCP工具诞生。本期视频我们从MCP的概念，技术原理，到多场景实战，一个视频看懂MCP的全部内容。\n\n\nMCP官方开源仓库：https://github.com/modelcontextprotocol/servers\nMCP合集网站：  https://smithery.ai/\nVscode下载：https://code.v"
  },
  {
    "id": "bvid:BV1nkXkYfEfF",
    "domain": "AI",
    "title": "零基础也能用AI编程!豆包电脑版让你3分钟做出实用工具",
    "url": "http://www.bilibili.com/video/av114200730933577",
    "source": "花叔v",
    "platform": "bilibili",
    "points": 384092,
    "published_at": "2025-03-22T04:02:08+00:00",
    "summary": "很多人都想学编程,但被高门槛劝退。本期给大家介绍一款零门槛的AI编程工具-豆包电脑版。通过3个实战案例,带你体验如何用AI轻松实现编程。\n\n豆包电脑版特点:\n- 中文界面,所见即所得\n- 支持html代码预览\n- 支持Python运行\n- 可生成完整项目代码\n- 历史版本管理\n- 代码一键导出\n\n时间戳\n00:00 为什么要学AI编程\n03:19 案例1:图片压缩网站实战\n04:15 案例2:数据"
  },
  {
    "id": "bvid:BV1EPedzoE7o",
    "domain": "AI",
    "title": "（已离职）冒死上传！已经替大家付费了，花7980买的AI视频制作全套系统教程，逼自己一个月学完，AI邪术爆涨！允许白嫖，拿走不谢，全程干货无废话！！",
    "url": "http://www.bilibili.com/video/av115088161771178",
    "source": "即梦AI动态漫制作",
    "platform": "bilibili",
    "points": 305062,
    "published_at": "2025-08-25T07:19:10+00:00",
    "summary": "一名专注研究 AIGC 5年的 资深 设计师 视频配套 软件 | 素材 | 学习咨询：【点击置顶评论】\n觉得视频有帮助的话，记得点赞、投币、收藏，加关注"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 256456,
    "published_at": "2026-07-01T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260701\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\nAI大模型开发热门教程：\nAI大模型开发：BV1h1"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 240679,
    "published_at": "2025-04-15T00:59:13+00:00",
    "summary": "MCP终极指南 - 带你深入掌握MCP（基础篇）\n\n时间轴：\n01:05 MCP简要介绍\n02:47 安装 MCP Host（Cline）\n03:15 配置 Cline 用的 API Key\n06:01 第一个 MCP 问题\n06:31 概念解释：MCP Server 和 Tool\n09:13 配置 MCP Server\n14:19 使用 MCP Server\n15:24 MCP 交互流程详解\n1"
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 238414,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 225285,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 187935,
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
    "points": 177221,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV16NvCBrEVs",
    "domain": "AI",
    "title": "什么是Vibe Coding，以及怎么使用？",
    "url": "http://www.bilibili.com/video/av115797133368973",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 161704,
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
    "points": 159802,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV1QE7N6jEuQ",
    "domain": "AI",
    "title": "真的被自己用心开发的昔涟Agent这段话感动到了",
    "url": "http://www.bilibili.com/video/av116794052316703",
    "source": "Playa0",
    "platform": "bilibili",
    "points": 135656,
    "published_at": "2026-06-22T13:44:15+00:00",
    "summary": "从最初生啃Transformer，硬逼着自己啃懂多头注意力和QKV权重，到一步步跟着claude学习RAG、检索重拍、Prompt、关键词召回优化、MCP与Function call，但是，自己上手了发现，自己还是啥也不懂，于是在glm gpt claude gemini 豆包 这几个模型之间疯狂切换，靠着想让昔涟早点被搭出来，硬逼着自己学，自己从零设计一套prompt架构能让她尽可能的贴合人设的"
  },
  {
    "id": "bvid:BV1WJjF67Eky",
    "domain": "AI",
    "title": "对Claude code上瘾了",
    "url": "http://www.bilibili.com/video/av116768819384530",
    "source": "小王很南",
    "platform": "bilibili",
    "points": 129460,
    "published_at": "2026-06-18T02:50:04+00:00",
    "summary": "我做的交互网站"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 122180,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1EVuqzrEMJ",
    "domain": "AI",
    "title": "【保姆级教程】手把手教你低成本制作AI女友，【一定要看置顶评论】，可随身携带，自由对话",
    "url": "http://www.bilibili.com/video/av114851468812000",
    "source": "往生堂研发",
    "platform": "bilibili",
    "points": 107694,
    "published_at": "2025-07-14T12:03:53+00:00",
    "summary": "文档地址\nhttps://github.com/xinnan-tech/xiaozhi-esp32-server/blob/main/docs/Deployment.md?_refluxos=a10#%E6%96%B9%E5%BC%8F%E4%B8%80docker%E5%8F%AA%E8%BF%90%E8%A1%8Cserver"
  },
  {
    "id": "bvid:BV1dpdZYBE9q",
    "domain": "AI",
    "title": "零代码让AI秒接海量MCP工具！最适合小白的MCP集合平台",
    "url": "http://www.bilibili.com/video/av114340703243255",
    "source": "AI研究室-帆哥",
    "platform": "bilibili",
    "points": 99581,
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
    "points": 92571,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 90323,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 87024,
    "published_at": "2026-04-27T08:51:41+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n   喜欢视频课程的同学一键三连多多支持一下，长按点赞五秒=lv6大佬 可以的发送彩色弹幕哦。\n配套源码项目已打包评论区回复up"
  },
  {
    "id": "bvid:BV1J3jq6EEe4",
    "domain": "AI",
    "title": "豆包居然可以免费开mc大型mod服务器！？",
    "url": "http://www.bilibili.com/video/av116775077350683",
    "source": "awa_mitama",
    "platform": "bilibili",
    "points": 74909,
    "published_at": "2026-06-19T05:27:45+00:00",
    "summary": "使用豆包的服务器来开我的世界服务器！"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 53084,
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
    "points": 42843,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1AeMF6bEsR",
    "domain": "AI",
    "title": "使用大疆Action5Pro搭建mc服务器",
    "url": "http://www.bilibili.com/video/av116860674644698",
    "source": "鱼-salmon",
    "platform": "bilibili",
    "points": 41594,
    "published_at": "2026-07-04T08:12:27+00:00",
    "summary": "action5pro搭载QCS8550(基于骁龙8gen2打造)芯片，运行linux系统\n感谢酷安@刷机迟早砖 提供的端口开启文件"
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 38339,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1g6fdYcEes",
    "domain": "AI",
    "title": "Cursor从小白到专家-第19课：如何用Cursor开发安卓APP？",
    "url": "http://www.bilibili.com/video/av113888322524233",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 28772,
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
    "points": 26586,
    "published_at": "2026-07-03T06:28:48+00:00",
    "summary": "迈入AI赋能的网络安全新时代！\n\n本课程带你打通大模型与安全实战的底层逻辑。从大模型演进到安全智能体（Agent）构建，硬核实战拉满！手把手教你利用大模型API自动化搞定信息收集、黑盒挖洞、代码审计、解CTF题目及报告编写。深度破解AI挖洞的高效提示词秘籍，攻克复杂场景下的Agent架构与成本选型。\n\n2026安全防线全面升级，带你用AI武装自己，成为驾驭大模型的稀缺AI安全专家！"
  },
  {
    "id": "bvid:BV1RUDsBWEHb",
    "domain": "AI",
    "title": "【2026最新版】目前B站最全最细的Cursor+Skills实战指南教程，手把手带你开发爆款app，全程干货无废话！比付费效果强十倍！",
    "url": "http://www.bilibili.com/video/av116373464350785",
    "source": "AI大模型技术教程",
    "platform": "bilibili",
    "points": 26169,
    "published_at": "2026-04-09T10:15:00+00:00",
    "summary": "制作不易，麻烦各位观众老爷一键三连呀【点赞、投币、收藏】感谢支持～\nCursor+Skills频配套文档课件笔记代码及AI大模型学习路线图戳这里获取→https://www.bilibili.com/read/cv41777105/?jump_opus=1"
  },
  {
    "id": "bvid:BV1LWTe6gEVc",
    "domain": "AI",
    "title": "Claude code帮我实现综述论文自由！",
    "url": "http://www.bilibili.com/video/av116842504918580",
    "source": "做科研的大师兄",
    "platform": "bilibili",
    "points": 24251,
    "published_at": "2026-07-01T03:07:40+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22626,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV191TY6KEHk",
    "domain": "AI",
    "title": "【全500集】目前B站最全最细的AI Agent零基础全套教程（从入门到精通），5天从入门到精通AI Agent，学完即可就业！看完这一套Agent教程就够了！",
    "url": "http://www.bilibili.com/video/av116843192851440",
    "source": "Agent智能体-",
    "platform": "bilibili",
    "points": 20940,
    "published_at": "2026-07-01T06:09:09+00:00",
    "summary": "【全500集】目前B站最全最细的AI Agent零基础全套教程（从入门到精通），5天从入门到精通AI Agent，学完即可就业！看完这一套AI Agent教程就够了！"
  },
  {
    "id": "bvid:BV1htCnY4ET6",
    "domain": "AI",
    "title": "用 Cursor AI 写 flutter 直接喂设计图就行 | flutter教程",
    "url": "http://www.bilibili.com/video/av113723805008238",
    "source": "独立开发者_猫哥",
    "platform": "bilibili",
    "points": 17845,
    "published_at": "2024-12-27T08:21:35+00:00",
    "summary": "✏️【关于本期视频】\n在上一篇文章《Flutter 使用 Cursor 和 Figma 快速生成界面代码》中，有同学提到他直接使用了设计稿的图片进行生成。我试了一下，效果确实很好。因此，我整理了一些文档，希望对大家有所帮助。\n下图展示了我没有手动编写任何代码实现的消息首页，支持上下滑动刷新数据。\n👉 文档 https://ducafecat.com/blog/use-cursor-ai-flutt"
  },
  {
    "id": "bvid:BV1ZHAozLE7b",
    "domain": "AI",
    "title": "【SynthPilot】Claude Code FPGA开发通关教程",
    "url": "http://www.bilibili.com/video/av116164755790661",
    "source": "晓川科研站",
    "platform": "bilibili",
    "points": 15484,
    "published_at": "2026-03-03T10:26:33+00:00",
    "summary": "全网首个AI Agent FPGA开发教程。SynthPilot通过MCP协议打通Vivado全链路，AI自主写码、综合、读报告、改Bug、迭代——真正的Agent模式闭环开发。从零开始，带你见证FPGA开发方式的代际变革。\n获取工具:synthpilot.dev\n晓川交流群:1007696121"
  },
  {
    "id": "bvid:BV1iDRQBrEF6",
    "domain": "AI",
    "title": "Claude + Blender 现在太强了 —— 完整免费设置",
    "url": "http://www.bilibili.com/video/av116543333601720",
    "source": "设计之道",
    "platform": "bilibili",
    "points": 15263,
    "published_at": "2026-05-09T07:11:36+00:00",
    "summary": "【简介】\nAnthropic 刚刚发布了用于创意工具的官方 Claude Connectors —— 其中 Blender 连接器对 3D 艺术家来说最重要。在本视频中，我将展示最佳的 Claude + Blender 免费设置，以及为什么这次更新可能会改变我们构建 3D 场景的方式。\n\n【你将学到】\n01:13 步骤 1：安装 Blender MCP 和 Claude Code\n02:31 步骤"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 14543,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1C3jt64EPS",
    "domain": "AI",
    "title": "B站讲的最好的Vibe Coding企业级项目实战教程（2026最新版）从入门到进阶，七天速通Claude Code+Codex+CursorAI工程化编程开发",
    "url": "http://www.bilibili.com/video/av116787425383675",
    "source": "图灵学院诸葛",
    "platform": "bilibili",
    "points": 14182,
    "published_at": "2026-06-21T09:48:04+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n 【本视频笔记代码、大模型最新学习路线、系统学习课程、实战案例、电子书+问题解答等戳这里获取→https://www.bilibili.com/read/cv39576966/?jump_opus=1】"
  },
  {
    "id": "bvid:BV14a4y1T7Cp",
    "domain": "AI",
    "title": "VS Code + CursorCode 插件，AI 帮你编写、调试代码",
    "url": "http://www.bilibili.com/video/av654787185",
    "source": "马隆工作室",
    "platform": "bilibili",
    "points": 14066,
    "published_at": "2023-04-11T11:48:41+00:00",
    "summary": "免费， VS Code + CursorCode 插件，AI 帮你编写、调试代码"
  },
  {
    "id": "bvid:BV1jZ5F6eEzQ",
    "domain": "AI",
    "title": "答应我，别再和AI一起拉屎了；Vibe Coding如何避免屎山",
    "url": "http://www.bilibili.com/video/av116677031236717",
    "source": "写代码小猴子Tong",
    "platform": "bilibili",
    "points": 12798,
    "published_at": "2026-06-01T23:00:00+00:00",
    "summary": "复杂度之战05：答应我，不要再和AI一起拉屎了；Vibe Coding如何避免写出屎山\n\n为什么你的项目越写越难改?\n为什么 AI 写的代码局部没有问题,合在一起就是一坨屎山?\n\n从一个最简单的数学事实讲起:软件复杂度的增长为啥会这么快。用一个圆的动画,直观演示&quot;解耦&quot;是如何降低屎山的规模的。\n\n本期内容: \n▸ 为什么屎山会膨胀得如此之快 \n▸ 一个圆讲清楚解耦的威力 \n▸ "
  },
  {
    "id": "bvid:BV1TtwCehEzG",
    "domain": "AI",
    "title": "cursor新手必会的怎么回退代码 防止改错改乱代码 提高效率开发",
    "url": "http://www.bilibili.com/video/av113855472605087",
    "source": "项目禅",
    "platform": "bilibili",
    "points": 11293,
    "published_at": "2025-01-19T14:29:21+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1GvmzBUEfj",
    "domain": "AI",
    "title": "【AI杂谈】3 claude code概念讲解与配置",
    "url": "http://www.bilibili.com/video/av115718414668601",
    "source": "左-岚",
    "platform": "bilibili",
    "points": 9318,
    "published_at": "2025-12-14T14:38:05+00:00",
    "summary": "飞书的ai杂谈目录下\nhttps://my.feishu.cn/wiki/space/7600816265116011716\n\n米醋工作室 AI 开发环境配置完整指南https://www.micu.wiki/t/topic/571\nClaude Code 常见问题与故障排查https://www.micu.wiki/t/topic/570\nClaude Code 核心概念详解\nhttps://w"
  },
  {
    "id": "bvid:BV1B97868EZK",
    "domain": "AI",
    "title": "Claude Code全流程开发实战丨MCP实战、Skills+Agent多工具协作、AI编程、自动化工作流、私有化部署、转行AI岗",
    "url": "http://www.bilibili.com/video/av116810192131401",
    "source": "博学谷",
    "platform": "bilibili",
    "points": 9272,
    "published_at": "2026-06-25T10:11:09+00:00",
    "summary": "视频配套资源领取方式戳：https://www.bilibili.com/opus/1217780115004456969\n或关注【博学谷】公综号回复关键词领取：260625\n学完本课程，你将能够独立完成AI Agent 研发与落地：深度掌握 Claude Code 辅助编程、Skill 技能包编排与 MCP 协议集成打通私有系统连接的“桥梁”，并能学会私有化部署。最终凭借“AI Coding 重"
  },
  {
    "id": "hn:48873836",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia, CoreWeave, and Nebius: Inside the Circular Financing of the GPU Boom",
    "url": "https://io-fund.com/ai-stocks/nvidia-coreweave-nebius-circular-financing-gpu-boom",
    "source": "adletbalzhanov",
    "platform": "hackernews",
    "points": 368,
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
    "points": 141,
    "published_at": "2026-07-14T08:24:49+00:00",
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
    "id": "rss:https://www.eetimes.com/how-nidec-is-rethinking-gear-design-for-humanoid-and-mobile-robots/",
    "domain": "AI 算力 / 半导体",
    "title": "How Nidec Is Rethinking Gear Design for Humanoid and Mobile Robots",
    "url": "https://www.eetimes.com/how-nidec-is-rethinking-gear-design-for-humanoid-and-mobile-robots/",
    "source": "EE Times Staff",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T21:06:44+00:00",
    "summary": "Nidec tackles the brutal gearbox tradeoffs behind humanoid robots, from zero backlash to lighter integrated actuators. The post How Nidec Is Rethinking Gear Design for Humanoid and Mobile Robots appea"
  },
  {
    "id": "rss:https://www.eetimes.com/tyl-semi-de-risks-chiplets-with-new-business-model/",
    "domain": "AI 算力 / 半导体",
    "title": "TYLsemi De-Risks Chiplets With New Business Model",
    "url": "https://www.eetimes.com/tyl-semi-de-risks-chiplets-with-new-business-model/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T19:00:00+00:00",
    "summary": "Startup TYLsemi wants to address the gap between ASIC houses and design services, taking on the risk of developing large chiplet-based chips for AI infrastructure customers. The post TYLsemi De-Risks "
  },
  {
    "id": "rss:https://www.eetimes.com/why-tl3228-is-the-go-to-standard-chip-powering-true-8k-wireless-gaming-peripherals/",
    "domain": "AI 算力 / 半导体",
    "title": "Why TL3228 Is the Go-To Standard Chip Powering True 8K Wireless Gaming Peripherals",
    "url": "https://www.eetimes.com/why-tl3228-is-the-go-to-standard-chip-powering-true-8k-wireless-gaming-peripherals/",
    "source": "Telink",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T13:00:00+00:00",
    "summary": "The TL3228 integrates a dual-core RISC-V processor consisting of a high-performance D25F core and an energy-efficient N22 core. The post Why TL3228 Is the Go-To Standard Chip Powering True 8K Wireless"
  },
  {
    "id": "rss:https://www.eetimes.com/massive-stock-full-chain-service-your-global-semiconductor-partner/",
    "domain": "AI 算力 / 半导体",
    "title": "Massive Stock, Full-Chain Service — Your Global Semiconductor Partner",
    "url": "https://www.eetimes.com/massive-stock-full-chain-service-your-global-semiconductor-partner/",
    "source": "NEW IDEAS INDUSTRIAL CO., LIMITED",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T13:00:00+00:00",
    "summary": "Discover how New Ideas Industrial can stabilize your semiconductor supply chain for AI, storage, and UAV applications. The post Massive Stock, Full-Chain Service — Your Global Semiconductor Partner ap"
  },
  {
    "id": "rss:https://www.eetimes.com/after-magdeburg-intel-builds-on-ireland-existing-strength/",
    "domain": "AI 算力 / 半导体",
    "title": "After Magdeburg, Intel Builds on Ireland’s Existing Strength",
    "url": "https://www.eetimes.com/after-magdeburg-intel-builds-on-ireland-existing-strength/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T11:24:18+00:00",
    "summary": "Leixlip cannot replace Magdeburg, but it shows the value of expanding where fabs, demand, and ecosystems already exist. The post After Magdeburg, Intel Builds on Ireland’s Existing Strength appeared f"
  },
  {
    "id": "rss:https://www.eetimes.com/probabilistic-computing-is-already-here-here-is-how-it-works/",
    "domain": "AI 算力 / 半导体",
    "title": "Probabilistic Computing Is Already Here; Here Is How It Works",
    "url": "https://www.eetimes.com/probabilistic-computing-is-already-here-here-is-how-it-works/",
    "source": "Phillip Stanley-Marbel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T07:21:54+00:00",
    "summary": "Probabilistic computing is addressing Monte Carlo bottlenecks, with UxHw hardware in use at Boeing and CERN. The post Probabilistic Computing Is Already Here; Here Is How It Works appeared first on EE"
  },
  {
    "id": "rss:https://www.eetimes.com/electronic-design-industry-rides-chip-wave-apac-leads-q1-2026-growth/",
    "domain": "AI 算力 / 半导体",
    "title": "Electronic Design Industry Rides Chip Wave, APAC Leads Q1 2026 Growth",
    "url": "https://www.eetimes.com/electronic-design-industry-rides-chip-wave-apac-leads-q1-2026-growth/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T17:00:00+00:00",
    "summary": "Chip design tools are cashing in: Q1 EDA revenue hit $5.7B as APAC surged 17.7% and hyperscalers went DIY. The post Electronic Design Industry Rides Chip Wave, APAC Leads Q1 2026 Growth appeared first"
  },
  {
    "id": "rss:https://www.eetimes.com/five-test-considerations-to-prepare-for-q-day/",
    "domain": "AI 算力 / 半导体",
    "title": "Five Test Considerations to Prepare for Q-Day",
    "url": "https://www.eetimes.com/five-test-considerations-to-prepare-for-q-day/",
    "source": "Sameh Yamany",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T12:30:00+00:00",
    "summary": "Q-Day is coming fast, and “harvest now, decrypt later” is already in play. The post Five Test Considerations to Prepare for Q-Day appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/solving-motion-connectivity-and-efficiency-challenges-in-factory-automation/",
    "domain": "AI 算力 / 半导体",
    "title": "Solving Motion, Connectivity, and Efficiency Challenges in Factory Automation",
    "url": "https://www.eetimes.com/solving-motion-connectivity-and-efficiency-challenges-in-factory-automation/",
    "source": "Arrow Electronics and Microchip Technology",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T08:46:25+00:00",
    "summary": "Explore factory automation challenges from the designer’s perspective and discover how to tackle development while improving performance. The post Solving Motion, Connectivity, and Efficiency Challeng"
  },
  {
    "id": "rss:https://www.eetimes.com/spain-semiconductor-industry-convenes-to-forge-domestic-alliances/",
    "domain": "AI 算力 / 半导体",
    "title": "Spain Semiconductor Industry Convenes to Forge Domestic Alliances",
    "url": "https://www.eetimes.com/spain-semiconductor-industry-convenes-to-forge-domestic-alliances/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T07:32:41+00:00",
    "summary": "AESEMI holds the first semiconductor MatchMaking day in Spain to forge new alliances and consolidate the ecosystem. The post Spain Semiconductor Industry Convenes to Forge Domestic Alliances appeared "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidias-huang-vows-to-deliver-giant-amounts-of-vera-rubin-company-says-that-our-roadmap-is-intact",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's Huang vows to deliver 'giant amounts' of Vera Rubin — company says that 'our roadmap is intact'",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidias-huang-vows-to-deliver-giant-amounts-of-vera-rubin-company-says-that-our-roadmap-is-intact",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T19:07:17+00:00",
    "summary": "Chief executive of Nvidia says the company is on track to produce 'giant amounts' of Vera Rubin-based machines, but fails to address rumored delays of Kyber NVL144 racks from 2027 to 2028."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ddr5/cxmts-ddr5-ram-isnt-as-performant-or-as-consistent-as-sk-hynix-dies-early-testing-shows-reveals-resistance-to-voltage-scaling-and-inferior-manual-overclocking-capabilities",
    "domain": "AI 算力 / 半导体",
    "title": "CXMT's DDR5 RAM isn't as performant or as consistent as SK hynix dies, early testing shows — reveals resistance to voltage scaling and inferior manual overclocking capabilities",
    "url": "https://www.tomshardware.com/pc-components/ddr5/cxmts-ddr5-ram-isnt-as-performant-or-as-consistent-as-sk-hynix-dies-early-testing-shows-reveals-resistance-to-voltage-scaling-and-inferior-manual-overclocking-capabilities",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T16:34:54+00:00",
    "summary": "Asus is claiming that CXMT-made DDR5 RAM performs worse than SK Hynix-made DDR5 at the same clock speeds, while being harder to manually overclock as well. It also allegedly doesn't scale with voltage"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/liquid-cooling/asrock-phantom-gaming-and-steel-legend-360-lcd-review",
    "domain": "AI 算力 / 半导体",
    "title": "ASRock Phantom Gaming and Steel Legend 360 LCD review: An impressive cooling debut",
    "url": "https://www.tomshardware.com/pc-components/liquid-cooling/asrock-phantom-gaming-and-steel-legend-360-lcd-review",
    "source": "Albert Thomas",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T16:11:45+00:00",
    "summary": "ASRock has entered the cooling market with the Phantom Gaming 360 LCD and Steel Legend 360 LCD AIOs. We’ve tested both liquid coolers with AMD’s Ryzen 9 9950X3D to benchmark their thermal proficiency."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/intel-becomes-the-first-company-to-ship-high-volume-logic-chips-made-with-asmls-high-na-euv-select-panther-lake-layers-on-18a-are-now-dual-qualified-for-0-55-na-scanners",
    "domain": "AI 算力 / 半导体",
    "title": "Intel becomes the first company to ship high-volume logic chips made with ASML's High NA EUV — select Panther Lake layers on 18A are now dual-qualified for 0.55 NA scanners",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/intel-becomes-the-first-company-to-ship-high-volume-logic-chips-made-with-asmls-high-na-euv-select-panther-lake-layers-on-18a-are-now-dual-qualified-for-0-55-na-scanners",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T15:33:13+00:00",
    "summary": "Intel is using ASML’s High-NA EUV tools to pattern select Panther Lake layers, marking the technology’s first use in high-volume logic production"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/grab-a-dji-osmo-camera-at-some-of-lowest-us-prices-ever",
    "domain": "AI 算力 / 半导体",
    "title": "Grab a DJI Osmo camera at some of lowest US prices ever",
    "url": "https://www.tomshardware.com/pc-components/grab-a-dji-osmo-camera-at-some-of-lowest-us-prices-ever",
    "source": "Sponsored",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T15:18:10+00:00",
    "summary": "An exclusive sale on AliExpress slashes prices on DJI’s Osmo ultra-compact handheld cameras, bringing them to some of the lowest prices in the U.S."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/intels-emib-packaging-gains-traction-as-chip-designers-look-to-skirt-tsmcs-cowos-constraints-googles-reported-decision-for-9th-gen-tpus-highlights-intels-attractive-alternative",
    "domain": "AI 算力 / 半导体",
    "title": "Intel's EMIB packaging gains traction as chip designers look to skirt TSMC's CoWoS constraints — Google's reported decision for 9th-gen TPUs highlights Intel's attractive alternative",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/intels-emib-packaging-gains-traction-as-chip-designers-look-to-skirt-tsmcs-cowos-constraints-googles-reported-decision-for-9th-gen-tpus-highlights-intels-attractive-alternative",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T14:45:15+00:00",
    "summary": "Google has reportedly chosen Intel's EMIB-T over TSMC's CoWoS-L for its next-generation TPU, codenamed Humufish. But will Google be alone in its alleged decision?"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/pcie-gen7-development-has-already-started-says-silicon-motions-alex-chou-nvidias-storage-next-initiative-is-becoming-a-focal-point",
    "domain": "AI 算力 / 半导体",
    "title": "'PCIe Gen7 development has already started,' says Silicon Motion's Alex Chou — Nvidia's Storage Next initiative is becoming a focal point",
    "url": "https://www.tomshardware.com/pc-components/ssds/pcie-gen7-development-has-already-started-says-silicon-motions-alex-chou-nvidias-storage-next-initiative-is-becoming-a-focal-point",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T14:09:24+00:00",
    "summary": "Silicon Motion is a relatively new entrant to the data center storage market, which has quickly landed orders from various customers and is now ramping up shipments of its high-end PCIe 5.0 SSD contro"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/save-usd400-on-a-27-inch-lg-ultragear-oled-monitor-limited-time-discount-nets-you-an-awesome-oled-monitor-with-fast-240hz-refresh-rate-for-your-gaming-pc",
    "domain": "AI 算力 / 半导体",
    "title": "Save $400 on a 27-inch LG Ultragear OLED Monitor — limited-time discount nets you an awesome OLED monitor with fast 240Hz refresh rate for your gaming PC",
    "url": "https://www.tomshardware.com/pc-components/save-usd400-on-a-27-inch-lg-ultragear-oled-monitor-limited-time-discount-nets-you-an-awesome-oled-monitor-with-fast-240hz-refresh-rate-for-your-gaming-pc",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T13:40:14+00:00",
    "summary": "Save $400 on LG’s 27-inch UltraGear 27GS93QE OLED gaming monitor, now $499.99 - with QHD 240 Hz OLED panel, true blacks, and FreeSync/G-Sync support, this deal is worth grabbing."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/pc-gamer-turns-steam-games-into-cartridges-with-ingenious-2-5-inch-ssd-system-games-are-stored-on-128gb-drives-alongside-a-script-to-auto-start-the-title-once-plugged-in",
    "domain": "AI 算力 / 半导体",
    "title": "PC gamer turns Steam games into cartridges with ingenious 2.5-inch SSD system — games are stored on 128GB drives alongside a script to auto-start the title once plugged in",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/pc-gamer-turns-steam-games-into-cartridges-with-ingenious-2-5-inch-ssd-system-games-are-stored-on-128gb-drives-alongside-a-script-to-auto-start-the-title-once-plugged-in",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T12:16:35+00:00",
    "summary": "A PC gamer has created and demonstrated a handy Steam Game Cartridge system."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/palit-officially-announces-rtx-3060-return-with-new-infinity-2-oc-launch-2021-gpu-with-12gb-of-vram-is-an-ai-crisis-stopgap",
    "domain": "AI 算力 / 半导体",
    "title": "Palit officially announces RTX 3060 return with 'new' Infinity 2 OC launch — 2021 GPU with 12GB of VRAM is an AI crisis stopgap",
    "url": "https://www.tomshardware.com/pc-components/gpus/palit-officially-announces-rtx-3060-return-with-new-infinity-2-oc-launch-2021-gpu-with-12gb-of-vram-is-an-ai-crisis-stopgap",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T11:59:06+00:00",
    "summary": "Nvidia has rebooted its five-year-old RTX 3060 graphics card, as is, for the modern AI era, bringing back the GPU officially at its original $329 price. It still features 12GB of VRAM, which serves as"
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/routers/elon-musks-starlink-releases-smaller-and-lighter-v5-residential-kit-offers-speeds-of-up-to-375-mbps-and-almost-half-the-power-consumption-of-v4",
    "domain": "AI 算力 / 半导体",
    "title": "Elon Musk's Starlink releases smaller and lighter V5 residential kit — offers speeds of up to 375 Mbps and almost half the power consumption of V4",
    "url": "https://www.tomshardware.com/networking/routers/elon-musks-starlink-releases-smaller-and-lighter-v5-residential-kit-offers-speeds-of-up-to-375-mbps-and-almost-half-the-power-consumption-of-v4",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T11:47:52+00:00",
    "summary": "Starlink just released a new generation of its Starlink terminal, which reduces its weight by more than 50% and is significantly smaller, too. This should make it easier to install, especially for DIY"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/score-16gb-of-ddr5-ram-for-just-usd61-99-in-this-newegg-parts-bundle-with-the-7800x3d-epic-kit-deal-for-a-gaming-pc-build-nets-you-usd189-in-savings-and-ships-with-a-gigabyte-motherboard-and-free-msi-mag-cooler",
    "domain": "AI 算力 / 半导体",
    "title": "Score 16GB of DDR5 RAM for just $61.99 in this Newegg parts bundle with the 7800X3D — epic kit deal for a gaming PC build nets you $189 in savings and ships with a Gigabyte motherboard and free MSI MA",
    "url": "https://www.tomshardware.com/pc-components/score-16gb-of-ddr5-ram-for-just-usd61-99-in-this-newegg-parts-bundle-with-the-7800x3d-epic-kit-deal-for-a-gaming-pc-build-nets-you-usd189-in-savings-and-ships-with-a-gigabyte-motherboard-and-free-msi-mag-cooler",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T11:30:15+00:00",
    "summary": "This 7800X3D bundle from Newegg saves you $188 and ships with a Gigabyte motherboard and 16GB of DDR5 RAM for just $636.99 overall."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/best-buy-has-slashed-usd900-off-this-asus-64gb-2-in-1-touchscreen-gaming-laptop-usd2-099-rog-flow-z13-is-great-for-both-gaming-and-ai-use",
    "domain": "AI 算力 / 半导体",
    "title": "Best Buy has slashed $900 off this Asus 64GB 2-in-1 touchscreen gaming laptop — $2,099 RoG Flow Z13 is great for both gaming and AI use",
    "url": "https://www.tomshardware.com/laptops/best-buy-has-slashed-usd900-off-this-asus-64gb-2-in-1-touchscreen-gaming-laptop-usd2-099-rog-flow-z13-is-great-for-both-gaming-and-ai-use",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T11:24:13+00:00",
    "summary": "Gaming laptop or touchscreen tablet, you choose. Save $900 on the Asus RoG Flow Z13 at Best Buy."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/nvidia-and-sega-team-up-to-deliver-rtx-spark-support-for-future-games-partnership-kicks-off-next-year-with-upcoming-virtua-fighter-crossroads",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia and Sega team up to deliver RTX Spark support for future games — partnership kicks off next year with upcoming Virtua Fighter Crossroads",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/nvidia-and-sega-team-up-to-deliver-rtx-spark-support-for-future-games-partnership-kicks-off-next-year-with-upcoming-virtua-fighter-crossroads",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T11:20:09+00:00",
    "summary": "Nvidia and Sega announced today that the upcoming Virtua Fighter Crossroads will support the RTX Spark platform when the game launches in 2027. Sega is also promising Spark support in its future title"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/intel-commits-5-7-billion-to-ireland-one-year-after-cancelling-its-german-and-polish-fab-projects",
    "domain": "AI 算力 / 半导体",
    "title": "Intel's big $5 billion bet on Ireland aims to right the wrongs of the cancelled Magdeburg, Germany complex — Fab 34's proven pipeline and Intel 3 node should help the company meet insatiable HPC deman",
    "url": "https://www.tomshardware.com/tech-industry/intel-commits-5-7-billion-to-ireland-one-year-after-cancelling-its-german-and-polish-fab-projects",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T11:20:00+00:00",
    "summary": "The announcement comes just shy of a year after CEO Lip-Bu Tan cancelled Intel's planned €30 billion fab complex in Germany and a €4.6 billion assembly and test plant in Poland."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/linux/developer-successfully-ports-linux-to-1994-sega-32x-genesis-and-megadrive-expansion-runs-open-source-os-on-paltry-23mhz-processors-and-256kb-of-ram",
    "domain": "AI 算力 / 半导体",
    "title": "Developer successfully ports Linux to 1994 Sega 32X — Genesis and MegaDrive expansion runs open-source OS on paltry 23MHz processors and 256KB of RAM",
    "url": "https://www.tomshardware.com/software/linux/developer-successfully-ports-linux-to-1994-sega-32x-genesis-and-megadrive-expansion-runs-open-source-os-on-paltry-23mhz-processors-and-256kb-of-ram",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T10:04:30+00:00",
    "summary": "The adventurous developer who recently ported Linux to the Atari Jaguar (1993) has brewed up a version of the open source OS for the Sega 32X (1994)."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/sound-cards/legendary-gravis-ultrasound-sound-card-gets-new-open-source-clone-beavis-ultrasound-remake-includes-complete-kicad-schematics-pcb-layout-sample-rom-and-more",
    "domain": "AI 算力 / 半导体",
    "title": "Legendary Gravis Ultrasound sound card gets new open-source clone — Beavis Ultrasound remake includes complete KiCad schematics, PCB layout, sample ROM, and more",
    "url": "https://www.tomshardware.com/pc-components/sound-cards/legendary-gravis-ultrasound-sound-card-gets-new-open-source-clone-beavis-ultrasound-remake-includes-complete-kicad-schematics-pcb-layout-sample-rom-and-more",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T10:00:00+00:00",
    "summary": "There’s a new remake of the legendary Gravis Ultrasound ISA soundcard on the block with the arrival of the open source Beavis Ultrasound project."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/cxmt-close-to-matching-microns-memory-capacity-in-2026-research-claims-would-put-china-on-track-to-become-worlds-second-largest-dram-producer",
    "domain": "AI 算力 / 半导体",
    "title": "CXMT close to matching Micron's memory capacity in 2026, research claims — would put China on track to become world's second-largest DRAM producer",
    "url": "https://www.tomshardware.com/pc-components/dram/cxmt-close-to-matching-microns-memory-capacity-in-2026-research-claims-would-put-china-on-track-to-become-worlds-second-largest-dram-producer",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T09:48:03+00:00",
    "summary": "As CXMT's DRAM capacity set to match Micron's, China's DRAM industry could become world's second largest after South Korea."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/ukraines-55000-plywood-drone-flew-2500-km-and-shut-down-russias-largest-oil-refinery",
    "domain": "AI 算力 / 半导体",
    "title": "Ukraine conducts record drone strike of 2,500km after 12-hour flight — $55,000 unit made of plywood halts operations at Russia's largest gasoline producer",
    "url": "https://www.tomshardware.com/tech-industry/drones/ukraines-55000-plywood-drone-flew-2500-km-and-shut-down-russias-largest-oil-refinery",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T09:29:21+00:00",
    "summary": "Ukrainian FP-1 drones struck the Gazprom Neft oil refinery in Omsk, Siberia, on July 6 after flying roughly 2,500 km over more than 12 hours."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/ps5-emulation-ramps-up-in-wake-of-sonys-end-to-physical-media-ps5-titles-now-booting-across-different-emulators-with-rapid-community-development-for-both-2d-and-3d-games",
    "domain": "AI 算力 / 半导体",
    "title": "PS5 emulation ramps up in response to Sony killing physical games — PS5 titles now booting across different emulators with rapid community development for both 2D and 3D games",
    "url": "https://www.tomshardware.com/video-games/playstation/ps5-emulation-ramps-up-in-wake-of-sonys-end-to-physical-media-ps5-titles-now-booting-across-different-emulators-with-rapid-community-development-for-both-2d-and-3d-games",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T09:00:00+00:00",
    "summary": "SharpEmu and KytyPS5 are two emulators that have exploded in terms of development milestones in the past two weeks, receiving several high-profile updates that have now made it possible to run a handf"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/us-govt-allows-chinese-telecom-giant-zte-to-purchase-nvidia-h200-ai-chips-firm-joins-alibaba-tencent-and-bytedance-in-access-to-hopper-tech",
    "domain": "AI 算力 / 半导体",
    "title": "US gov't allows Chinese telecom giant ZTE to purchase Nvidia H200 AI chips — firm joins Alibaba, Tencent, and ByteDance in access to Hopper tech",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/us-govt-allows-chinese-telecom-giant-zte-to-purchase-nvidia-h200-ai-chips-firm-joins-alibaba-tencent-and-bytedance-in-access-to-hopper-tech",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T19:46:26+00:00",
    "summary": "The United States has licensed Chinese telecom giant ZTE to purchase restricted Nvidia H200 AI chips, but Chinese regulators and domestic procurement initiatives may limit the material impact of the c"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/samsung-990-2tb-ssd-review",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung 990 2TB SSD Review: New flash, familiar speeds",
    "url": "https://www.tomshardware.com/pc-components/ssds/samsung-990-2tb-ssd-review",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T16:00:00+00:00",
    "summary": "The Samsung 990 is the QLC variant of the manufacturer’s 990 EVO Plus. Despite having newer flash, it largely performs like last-gen, with mediocre power efficiency."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/elon-musks-colossus-2-data-center-installed-59-natural-gas-turbines-without-permission-report-claims-thousands-of-tons-of-pollutants-reportedly-impact-black-communities-in-mississippi-already-suffering-from-elevated-lung-disease-rates",
    "domain": "AI 算力 / 半导体",
    "title": "Elon Musk’s Colossus 2 data center installed 59 natural gas turbines without permission, report claims — thousands of tons of pollutants reportedly impact black communities in Mississippi already suff",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/elon-musks-colossus-2-data-center-installed-59-natural-gas-turbines-without-permission-report-claims-thousands-of-tons-of-pollutants-reportedly-impact-black-communities-in-mississippi-already-suffering-from-elevated-lung-disease-rates",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T15:55:29+00:00",
    "summary": "The population of the communities surrounding the Colossus 2 site, which is in the center of a lawsuit involving unpermitted natural gas turbines and pollution, is predominantly black."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/china-claims-chip-exports-nearly-doubled-to-177-billion-in-the-first-half-of-2026",
    "domain": "AI 算力 / 半导体",
    "title": "China claims chip exports nearly doubled to $177 billion in the first half of 2026 as memory prices surged — 96% year-on-year increase inflated by hikes",
    "url": "https://www.tomshardware.com/tech-industry/china-claims-chip-exports-nearly-doubled-to-177-billion-in-the-first-half-of-2026",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T14:52:27+00:00",
    "summary": "The Chinese customs administration attributed the surge to global demand for AI hardware."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-invests-usd5-7-billion-in-ireland-fab-aims-to-boost-output-of-xeon-6-next-gen-xeon-products-built-on-intel-3-process",
    "domain": "AI 算力 / 半导体",
    "title": "Intel invests $5.7 billion in Ireland fab — aims to boost output of Xeon 6, next-gen Xeon products built on Intel 3 process",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-invests-usd5-7-billion-in-ireland-fab-aims-to-boost-output-of-xeon-6-next-gen-xeon-products-built-on-intel-3-process",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T13:09:10+00:00",
    "summary": "Intel to modernize semiconductor production facility in Ireland in a bid to increase output of Xeon 6 and other Xeon products made using Intel 3 fabrication process."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/razer-blade-16-2026-review",
    "domain": "AI 算力 / 半导体",
    "title": "Razer Blade 16 (2026) review: Competitive gaming performance and class-leading endurance",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/razer-blade-16-2026-review",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T13:00:00+00:00",
    "summary": "If you can stomach the nearly $5,000 price tag, the Razer Blade 16 delivers on gaming performance and endurance."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/new-york-enacts-one-year-data-center-ban-on-projects-larger-than-50-megawatts-first-us-state-to-implement-moratorium-will-also-pursue-repealing-tax-exemptions",
    "domain": "AI 算力 / 半导体",
    "title": "New York enacts one-year data center ban on projects larger than 50 megawatts — first US state to implement moratorium; will also pursue repealing tax exemptions",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/new-york-enacts-one-year-data-center-ban-on-projects-larger-than-50-megawatts-first-us-state-to-implement-moratorium-will-also-pursue-repealing-tax-exemptions",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T12:17:43+00:00",
    "summary": "New York is the first to pass a statewide data center moratorium, which pauses all projects greater than 50 MW for one year. The governor's office said that it will create a GEIS to hold developments "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-ryzen-7-5800x3d-is-back-in-stock-with-up-to-usd173-in-savings-thanks-to-these-newegg-deals-free-usd70-msi-mag-cooler-brings-costs-well-below-msrp-for-the-standalone-cpu-alongside-an-extra-usd100-off-for-a-16gb-ram-and-motherboard-bundle",
    "domain": "AI 算力 / 半导体",
    "title": "AMD Ryzen 7 5800X3D is back in stock with up to $173 in savings, thanks to these Newegg deals — free $70 MSI MAG cooler brings costs well below MSRP for the standalone CPU, alongside an extra $100 off",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-ryzen-7-5800x3d-is-back-in-stock-with-up-to-usd173-in-savings-thanks-to-these-newegg-deals-free-usd70-msi-mag-cooler-brings-costs-well-below-msrp-for-the-standalone-cpu-alongside-an-extra-usd100-off-for-a-16gb-ram-and-motherboard-bundle",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T11:39:27+00:00",
    "summary": "The AMD Ryzen 7 5800X3D is back in stock and on sale, with up to $173 in savings to be had at Newegg."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/nvidia-slashes-list-of-authorized-customers-in-asia-in-a-bid-to-reduce-ai-chip-smuggling-report-claims-company-sent-field-inspectors-called-customers-to-check-if-business-is-genuine-after-pressure-from-washington",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia slashes list of authorized customers in Asia in a bid to reduce AI chip smuggling, report claims — company sent field inspectors, called customers to check if business is genuine after pressure",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/nvidia-slashes-list-of-authorized-customers-in-asia-in-a-bid-to-reduce-ai-chip-smuggling-report-claims-company-sent-field-inspectors-called-customers-to-check-if-business-is-genuine-after-pressure-from-washington",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T11:08:54+00:00",
    "summary": "The company culled its list of verified customers, cutting out more than half of its existing client list to reduce incidents of smuggling. Remaining clients have passed more stringent checks, includi"
  },
  {
    "id": "rss:https://www.tomshardware.com/speakers/drops-usd130-desktop-pc-speakers-are-now-just-usd23-save-a-massive-82-percent-on-these-dual-orientation-bmr1-v2-speakers",
    "domain": "AI 算力 / 半导体",
    "title": "Drop's $130 desktop PC speakers are now just $23 — save a massive 82% on these dual-orientation BMR1 V2 speakers",
    "url": "https://www.tomshardware.com/speakers/drops-usd130-desktop-pc-speakers-are-now-just-usd23-save-a-massive-82-percent-on-these-dual-orientation-bmr1-v2-speakers",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T11:04:14+00:00",
    "summary": "Save a massive 82% on these slimline dual-orientation Drop BMR1 V2 nearfield monitor speakers. Pay only $23 to bathe your desktop setup in sound."
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
    "id": "hn:48845518",
    "domain": "AI 算力 / 半导体",
    "title": "Reverse-engineering Nvidia's CUDA-checkpoint for faster cold starts",
    "url": "https://blog.doubleword.ai/what-happens-when-you-checkpoint-a-cuda-process",
    "source": "ilreb",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-07-09T13:29:52+00:00",
    "summary": ""
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
    "id": "hn:48925271",
    "domain": "大厂 AI 动态",
    "title": "Why I Left Google DeepMind",
    "url": "https://turntrout.com/why-i-left-google-deepmind",
    "source": "apsec112",
    "platform": "hackernews",
    "points": 311,
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
    "id": "rss:https://www.theverge.com/tech/966022/skullcandy-cruser-1080-anc-bose-tuning-noise-cancelling-wireless-headphones",
    "domain": "大厂 AI 动态",
    "title": "Skullcandy’s bass-boosting Crusher headphones now come with Bose’s ANC",
    "url": "https://www.theverge.com/tech/966022/skullcandy-cruser-1080-anc-bose-tuning-noise-cancelling-wireless-headphones",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T00:00:00+00:00",
    "summary": "Skullcandy announced a new version of its Crusher wireless headphones today featuring a few of Bose's audio technologies including its QuietControl ANC and head-tracking spatial audio. The Crusher hea"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/966209/hp-omnibook-x-flip-oled-laptop-windows-11-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "HP&#8217;s OLED-equipped 2-in-1 laptop is a solid back-to-school deal",
    "url": "https://www.theverge.com/gadgets/966209/hp-omnibook-x-flip-oled-laptop-windows-11-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T22:47:11+00:00",
    "summary": "With storage and memory prices still at an all-time high, we’re happy to tell you about a solid deal on a good laptop when we find one, rare as they are. Best Buy is selling the HP OmniBook X Flip 2 i"
  },
  {
    "id": "rss:https://www.theverge.com/tech/966219/apple-care-plus-price-increase",
    "domain": "大厂 AI 动态",
    "title": "Apple’s reportedly raising the price for AppleCare Plus on Macs and iPads",
    "url": "https://www.theverge.com/tech/966219/apple-care-plus-price-increase",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T22:39:40+00:00",
    "summary": "An AppleCare Plus subscription for a Mac or iPad will cost more soon, with prices going up by $0.50 per month or $5 per year for new sign-ups while remaining the same for existing subscribers, accordi"
  },
  {
    "id": "rss:https://www.theverge.com/games/966106/valve-ifixit-will-keep-selling-steam-deck-lcd-battery",
    "domain": "大厂 AI 动态",
    "title": "Valve says iFixit will keep selling Steam Deck batteries after all",
    "url": "https://www.theverge.com/games/966106/valve-ifixit-will-keep-selling-steam-deck-lcd-battery",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T22:16:46+00:00",
    "summary": "Valve has been incredibly friendly to customers who need repairs - which is why it was so surprising to hear that Valve was already discontinuing the battery for the Steam Deck LCD handheld. It would "
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/966293/xai-grok-user-lawsuit-csam",
    "domain": "大厂 AI 动态",
    "title": "xAI sues a man for using Grok to generate CSAM &#8216;deepfakes&#8217;",
    "url": "https://www.theverge.com/ai-artificial-intelligence/966293/xai-grok-user-lawsuit-csam",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T21:33:20+00:00",
    "summary": "The Elon Musk-owned xAI is suing a South Carolina man who allegedly used the company's Grok AI chatbot to generate child sexual abuse material (CSAM). In a lawsuit reported earlier by Reuters, xAI cla"
  },
  {
    "id": "rss:https://www.theverge.com/policy/966283/fcc-broadcast-ownership-cap-brendan-carr",
    "domain": "大厂 AI 动态",
    "title": "Brendan Carr plans to let broadcast giants dominate the airwaves",
    "url": "https://www.theverge.com/policy/966283/fcc-broadcast-ownership-cap-brendan-carr",
    "source": "Lauren Feiner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T21:30:17+00:00",
    "summary": "The Federal Communications Commission will vote next month on whether a single company can own broadcast stations that reach more than 39 percent of US TV households. In a Breitbart op-ed on Wednesday"
  },
  {
    "id": "rss:https://www.theverge.com/games/966181/roblox-connect-video-chat-calling-service-shut-down",
    "domain": "大厂 AI 动态",
    "title": "Roblox is shutting down its video chat service",
    "url": "https://www.theverge.com/games/966181/roblox-connect-video-chat-calling-service-shut-down",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T20:02:26+00:00",
    "summary": "Roblox will be shutting down Roblox Connect, its video calling service introduced in 2023. Roblox Connect let you video chat with other people using your Roblox avatar, which would be able to mimic th"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/965616/ash-koosha-odysseus-the-fall-foundtain-zero-tilly-norwood",
    "domain": "大厂 AI 动态",
    "title": "AI slop movies are the new direct-to-video cash grabs",
    "url": "https://www.theverge.com/entertainment/965616/ash-koosha-odysseus-the-fall-foundtain-zero-tilly-norwood",
    "source": "Charles Pulliam-Moore",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T20:00:00+00:00",
    "summary": "This weekend, cinephiles across the world will march to their local theaters to feast their eyes on Christopher Nolan's new adaptation of The Odyssey. It's on track to rake in anywhere between $80-$10"
  },
  {
    "id": "rss:https://www.theverge.com/policy/966111/cyclospora-explosive-diarrhea-parasite-fda-cdc-taco-bell",
    "domain": "大厂 AI 动态",
    "title": "Enshittification",
    "url": "https://www.theverge.com/policy/966111/cyclospora-explosive-diarrhea-parasite-fda-cdc-taco-bell",
    "source": "Gaby Del Valle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T18:40:00+00:00",
    "summary": "Bryan, a food broker from Michigan, wasn't sure if he'd be able to make it to urgent care in time. He started feeling off on Thursday, and by Saturday, he was having to use the bathroom every 15 to 30"
  },
  {
    "id": "rss:https://www.theverge.com/tech/966120/google-pixel-11-camera-bar-teaser",
    "domain": "大厂 AI 动态",
    "title": "Something&#8217;s glowing on the Pixel 11&#8217;s camera bar",
    "url": "https://www.theverge.com/tech/966120/google-pixel-11-camera-bar-teaser",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T18:24:22+00:00",
    "summary": "A new teaser for Google's upcoming Pixel 11 lineup reveals that the phones will feature some kind of glowing orb on the camera bar, as reported by 9to5Google. Google's store page for the Pixel 11 has "
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/15/lululemon-backs-nylon-recycling-startup-syntetica-in-30m-series-a/",
    "domain": "大厂 AI 动态",
    "title": "Lululemon backs nylon-recycling startup Syntetica in $30M Series A",
    "url": "https://techcrunch.com/2026/07/15/lululemon-backs-nylon-recycling-startup-syntetica-in-30m-series-a/",
    "source": "Anna Heim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T04:00:00+00:00",
    "summary": "Syntetica, a French startup that has developed a novel approach to recycling nylon, has already obtained big-name partners and investors."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/15/applied-computing-wants-to-give-oil-and-gas-operators-an-ai-model-for-the-entire-plant/",
    "domain": "大厂 AI 动态",
    "title": "Applied Computing wants to give oil and gas operators an AI model for the entire plant",
    "url": "https://techcrunch.com/2026/07/15/applied-computing-wants-to-give-oil-and-gas-operators-an-ai-model-for-the-entire-plant/",
    "source": "Ram Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T04:00:00+00:00",
    "summary": "Applied Computing has raised a $20M Series A to build a foundation AI model for the oil, gas and petrochemical industry."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/15/why-greylock-capped-its-new-fund-at-1-5b-when-it-says-it-could-have-raised-more/",
    "domain": "大厂 AI 动态",
    "title": "Why Greylock capped its new fund at $1.5B when it says it could have raised more",
    "url": "https://techcrunch.com/2026/07/15/why-greylock-capped-its-new-fund-at-1-5b-when-it-says-it-could-have-raised-more/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T00:20:42+00:00",
    "summary": "By keeping the number of investments to about 25 per fund, Greylock aims to remain what it calls \"the most important partner\" to its founders."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/15/microsoft-is-reportedly-training-salespeople-to-talk-down-openai-and-anthropic/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft is reportedly training salespeople to talk down OpenAI and Anthropic",
    "url": "https://techcrunch.com/2026/07/15/microsoft-is-reportedly-training-salespeople-to-talk-down-openai-and-anthropic/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T23:59:44+00:00",
    "summary": "Microsoft is looking to sell its in-house AI models as more efficient and cost-effective than its competitors' models."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/15/tesla-driver-in-fatal-texas-crash-pressed-accelerator-100-ntsb-confirms/",
    "domain": "大厂 AI 动态",
    "title": "Tesla driver in fatal Texas crash pressed accelerator 100%, NTSB confirms",
    "url": "https://techcrunch.com/2026/07/15/tesla-driver-in-fatal-texas-crash-pressed-accelerator-100-ntsb-confirms/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T20:22:52+00:00",
    "summary": "The safety board confirmed Tesla's account of the crash, which the company shared days after it happened last month."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/15/daniel-eks-body-scanning-startup-neko-health-raises-another-700m/",
    "domain": "大厂 AI 动态",
    "title": "Daniel Ek’s body-scanning startup Neko Health raises another $700M",
    "url": "https://techcrunch.com/2026/07/15/daniel-eks-body-scanning-startup-neko-health-raises-another-700m/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T19:46:54+00:00",
    "summary": "Neko Health has developed proprietary body-scanning technology, which it couples with bloodwork, to assess a person's health."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/15/amid-hardware-legal-battle-openai-releases-a-230-keyboard-for-codex/",
    "domain": "大厂 AI 动态",
    "title": "Amid hardware legal battle, OpenAI releases a $230 keyboard for Codex",
    "url": "https://techcrunch.com/2026/07/15/amid-hardware-legal-battle-openai-releases-a-230-keyboard-for-codex/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T19:41:38+00:00",
    "summary": "OpenAI, which is in the middle of a legal battle with Apple over hardware trade theft allegations, just released a light-up keyboard designed to be paired with its agentic coding app."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/15/microsoft-patches-bug-in-video-game-age-of-empires-ii/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft patches bug in video game Age of Empires II",
    "url": "https://techcrunch.com/2026/07/15/microsoft-patches-bug-in-video-game-age-of-empires-ii/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T18:47:01+00:00",
    "summary": "The vulnerability in the decades-old game could have allowed hackers to take over victims’ computers with a malicious game invite."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/15/apple-quietly-reveals-how-its-maps-ads-will-differ-from-googles/",
    "domain": "大厂 AI 动态",
    "title": "Apple bans home services from its upcoming Maps ads",
    "url": "https://techcrunch.com/2026/07/15/apple-quietly-reveals-how-its-maps-ads-will-differ-from-googles/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T18:21:22+00:00",
    "summary": "Apple has published the policies governing its upcoming Maps advertising business, revealing a strategy that differs from Google’s. The new rules prohibit home services businesses like plumbers, elect"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/15/spacex-falls-to-135-ipo-price-ahead-of-starship-launch/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX falls to $135 IPO price ahead of Starship launch",
    "url": "https://techcrunch.com/2026/07/15/spacex-falls-to-135-ipo-price-ahead-of-starship-launch/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T18:06:05+00:00",
    "summary": "The stock has steadily fallen from the euphoric post-IPO high, showing that markets may be sobering up to the promises CEO Elon Musk made before and after SpaceX went public."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/15/thinking-machines-amps-up-its-bet-against-one-size-fits-all-ai-with-its-first-open-model-inkling/",
    "domain": "大厂 AI 动态",
    "title": "Thinking Machines amps up its bet against one-size-fits-all AI with its first open model, Inkling",
    "url": "https://techcrunch.com/2026/07/15/thinking-machines-amps-up-its-bet-against-one-size-fits-all-ai-with-its-first-open-model-inkling/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T18:04:06+00:00",
    "summary": "It's the company's first public proof point after a year and a half spent building AI infrastructure largely out of public view."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/15/phone-maker-oneplus-reportedly-plans-to-wind-down-us-and-europe-operations/",
    "domain": "大厂 AI 动态",
    "title": "Phone maker OnePlus reportedly plans to wind down US and Europe operations",
    "url": "https://techcrunch.com/2026/07/15/phone-maker-oneplus-reportedly-plans-to-wind-down-us-and-europe-operations/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T17:53:32+00:00",
    "summary": "OnePlus could also wind down its operations in India by 2027."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/15/googles-biggest-clean-power-project-is-40-miles-north-of-xais-unpermitted-gas-power-plant/",
    "domain": "大厂 AI 动态",
    "title": "Google’s biggest clean power project is 40 miles north of xAI’s unpermitted gas power plant",
    "url": "https://techcrunch.com/2026/07/15/googles-biggest-clean-power-project-is-40-miles-north-of-xais-unpermitted-gas-power-plant/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T17:39:54+00:00",
    "summary": "Google's biggest solar and battery project stands in sharp contrast with xAI's nearby unpermitted power plant."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/15/hack-suggests-ai-music-generator-suno-scraped-youtube-for-training-data/",
    "domain": "大厂 AI 动态",
    "title": "Hack suggests AI music generator Suno scraped YouTube for training data",
    "url": "https://techcrunch.com/2026/07/15/hack-suggests-ai-music-generator-suno-scraped-youtube-for-training-data/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T17:00:34+00:00",
    "summary": "The hacker used an employee's credentials to access source code, which revealed how Suno scraped decades of audio."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/15/whatnot-acquires-shaped-to-power-real-time-live-shopping-recommendations/",
    "domain": "大厂 AI 动态",
    "title": "Whatnot acquires Shaped to power real-time live shopping recommendations",
    "url": "https://techcrunch.com/2026/07/15/whatnot-acquires-shaped-to-power-real-time-live-shopping-recommendations/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T17:00:00+00:00",
    "summary": "Livestream shopping platform Whatnot has acquired AI startup Shaped, a machine learning company focused on real-time recommendations and search. The deal will bolster Whatnot’s personalization and dis"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/15/microsoft-patches-record-number-of-security-vulnerabilities-citing-its-use-of-ai/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft patches record number of security vulnerabilities, citing its use of AI",
    "url": "https://techcrunch.com/2026/07/15/microsoft-patches-record-number-of-security-vulnerabilities-citing-its-use-of-ai/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T16:20:18+00:00",
    "summary": "Microsoft's monthly release of security fixes, dubbed Patch Tuesday, resolved a record 570 security vulnerabilities across the company's product line, thanks to discoveries with AI."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/15/stripe-and-advent-reportedly-offered-to-buy-paypal-for-around-53-4b/",
    "domain": "大厂 AI 动态",
    "title": "Stripe and Advent reportedly offered to buy PayPal for around $53.4B",
    "url": "https://techcrunch.com/2026/07/15/stripe-and-advent-reportedly-offered-to-buy-paypal-for-around-53-4b/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T15:30:26+00:00",
    "summary": "If completed, the acquisition would unite two of the biggest names in digital payments."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/15/apple-intelligence-approved-for-launch-in-china-with-alibabas-qwen-ai/",
    "domain": "大厂 AI 动态",
    "title": "Apple Intelligence approved for launch in China with Alibaba’s Qwen AI",
    "url": "https://techcrunch.com/2026/07/15/apple-intelligence-approved-for-launch-in-china-with-alibabas-qwen-ai/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T15:29:33+00:00",
    "summary": "The deal, which was rumored to be in the works last year, marks an important step for Apple's AI ambitions in a key market."
  },
  {
    "id": "rss:https://techcrunch.com/video/inside-ode-with-anthropic-the-startup-betting-ai-services-are-the-future-of-enterprise/",
    "domain": "大厂 AI 动态",
    "title": "Inside Ode with Anthropic, the startup betting AI services are the future of enterprise",
    "url": "https://techcrunch.com/video/inside-ode-with-anthropic-the-startup-betting-ai-services-are-the-future-of-enterprise/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T15:00:00+00:00",
    "summary": "Can a handful of engineers really do the work of an army of consultants?&#160;That’s&#160;the bet behind Ode with Anthropic —&#160;the joint venture dedicated to embedding forward-deployed engineers i"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/15/spotify-expands-parent-managed-accounts-to-users-on-its-free-tier/",
    "domain": "大厂 AI 动态",
    "title": "Spotify expands parent-managed accounts to users on its free tier",
    "url": "https://techcrunch.com/2026/07/15/spotify-expands-parent-managed-accounts-to-users-on-its-free-tier/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T14:42:10+00:00",
    "summary": "The feature was previously only available to paid subscribers."
  },
  {
    "id": "rss:https://stratechery.com/2026/ibm-misses-ibms-mainframe-moat-ibms-many-ai-problems/",
    "domain": "大厂 AI 动态",
    "title": "IBM Misses, IBM’s Mainframe Moat, IBM’s Many AI Problems",
    "url": "https://stratechery.com/2026/ibm-misses-ibms-mainframe-moat-ibms-many-ai-problems/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T10:00:19+00:00",
    "summary": "IBM announced preliminary results that spooked the software market generally; this is a story, however, specifically about IBM and its mainframe franchise."
  },
  {
    "id": "rss:https://stratechery.com/2026/the-openai-super-app-chatgpt-codex-whither-chat/",
    "domain": "大厂 AI 动态",
    "title": "The OpenAI Super App, ChatGPT = Codex, Whither Chat",
    "url": "https://stratechery.com/2026/the-openai-super-app-chatgpt-codex-whither-chat/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T10:00:00+00:00",
    "summary": "OpenAI has refashioned Codex as the new ChatGPT; is the company abandoning the chat category they pioneered?"
  },
  {
    "id": "rss:https://arstechnica.com/gaming/2026/07/hundreds-rally-at-bethesda-hq-to-protest-xbox-layoffs-and-ars-was-there/",
    "domain": "大厂 AI 动态",
    "title": "Hundreds rally at Bethesda HQ to protest Xbox layoffs, and Ars was there",
    "url": "https://arstechnica.com/gaming/2026/07/hundreds-rally-at-bethesda-hq-to-protest-xbox-layoffs-and-ars-was-there/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T22:36:28+00:00",
    "summary": "Union wants to halt a \"perpetual cycle\" of layoffs, get back to contract bargaining."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/07/apollo-11s-broken-switch-and-mission-saving-pen-sell-for-860k/",
    "domain": "大厂 AI 动态",
    "title": "Buzz Aldrin sells famous felt-tip pen that helped launch Apollo from the Moon",
    "url": "https://arstechnica.com/space/2026/07/apollo-11s-broken-switch-and-mission-saving-pen-sell-for-860k/",
    "source": "Robert Pearlman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T22:10:41+00:00",
    "summary": "While an impressive sale, the pen and switch did not break records."
  },
  {
    "id": "rss:https://arstechnica.com/information-technology/2026/07/sheetz-moves-838-stores-off-vmware-broadcom-created-too-much-uncertainty/",
    "domain": "大厂 AI 动态",
    "title": "Sheetz is quitting VMware, migrating 11,000 virtual machines",
    "url": "https://arstechnica.com/information-technology/2026/07/sheetz-moves-838-stores-off-vmware-broadcom-created-too-much-uncertainty/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T21:41:56+00:00",
    "summary": "The convenience store chain will use StorMagic instead."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/judge-trump-cant-deport-researchers-just-for-working-in-content-moderation/",
    "domain": "大厂 AI 动态",
    "title": "Judge: Trump can’t deport researchers just for working in content moderation",
    "url": "https://arstechnica.com/tech-policy/2026/07/judge-trump-cant-deport-researchers-just-for-working-in-content-moderation/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T21:26:02+00:00",
    "summary": "Disinformation researchers praise ruling blocking Trump visa denials and deportations."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/07/engineer-identifies-and-explains-every-90s-computer-seen-in-jurassic-park/",
    "domain": "大厂 AI 动态",
    "title": "Engineer identifies and explains every '90s computer seen in Jurassic Park",
    "url": "https://arstechnica.com/gadgets/2026/07/engineer-identifies-and-explains-every-90s-computer-seen-in-jurassic-park/",
    "source": "Samuel Axon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T21:04:22+00:00",
    "summary": "Yes, it was, in fact, a Unix system."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/07/windows-0-day-drops-the-same-day-microsoft-releases-record-number-of-patches/",
    "domain": "大厂 AI 动态",
    "title": "Windows 0-day drops the same day Microsoft releases record number of patches",
    "url": "https://arstechnica.com/security/2026/07/windows-0-day-drops-the-same-day-microsoft-releases-record-number-of-patches/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T19:59:48+00:00",
    "summary": "HiveLegacy is a \"powerful primitive\" that's likely capable of other nefarious actions."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/fcc-to-repeal-39-tv-ownership-cap-in-boost-for-trump-friendly-news-orgs/",
    "domain": "大厂 AI 动态",
    "title": "FCC to repeal 39% TV ownership cap in boost for Trump-friendly news orgs",
    "url": "https://arstechnica.com/tech-policy/2026/07/fcc-to-repeal-39-tv-ownership-cap-in-boost-for-trump-friendly-news-orgs/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T18:52:22+00:00",
    "summary": "FCC chairman claims power to repeal TV ownership limit set by Congress."
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/07/in-memoriam-seven-of-our-favorite-sam-neill-films/",
    "domain": "大厂 AI 动态",
    "title": "In memoriam: 7 of our favorite Sam Neill films",
    "url": "https://arstechnica.com/culture/2026/07/in-memoriam-seven-of-our-favorite-sam-neill-films/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T18:39:58+00:00",
    "summary": "The actor, who starred in 1993's Jurassic Park, died Monday in Sydney, Australia, at the age of 78."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/07/third-party-app-stores-coming-to-google-play-next-week-as-epic-settlement-withdrawn/",
    "domain": "大厂 AI 动态",
    "title": "Third-party app stores coming to Google Play next week as Epic settlement withdrawn",
    "url": "https://arstechnica.com/gadgets/2026/07/third-party-app-stores-coming-to-google-play-next-week-as-epic-settlement-withdrawn/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T16:55:12+00:00",
    "summary": "With the settlement withdrawn, Google is now bound by the court's full antitrust remedies."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/07/openais-first-branded-hardware-is-a-light-up-keyboard/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI's first branded hardware is... a light-up keyboard?",
    "url": "https://arstechnica.com/ai/2026/07/openais-first-branded-hardware-is-a-light-up-keyboard/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T16:00:33+00:00",
    "summary": "The Codex Micro is designed to monitor multiple agentic threads at a glance."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/07/a-most-improbable-astronaut-just-went-to-space/",
    "domain": "大厂 AI 动态",
    "title": "A most improbable astronaut just went to space",
    "url": "https://arstechnica.com/space/2026/07/a-most-improbable-astronaut-just-went-to-space/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T11:30:07+00:00",
    "summary": "\"I pretty much, at that point in time, gave up on being an astronaut.\""
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/07/how-hard-is-it-to-build-orbital-data-centers-actually/",
    "domain": "大厂 AI 动态",
    "title": "How hard is it to build orbital data centers, actually?",
    "url": "https://arstechnica.com/space/2026/07/how-hard-is-it-to-build-orbital-data-centers-actually/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T11:00:09+00:00",
    "summary": "\"The ISS radiators are expensive and heavy. We're focused on making them cheap and light.\""
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
    "points": 35,
    "published_at": "2026-07-15T16:30:41+00:00",
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
    "id": "wscn:3777020",
    "domain": "股票",
    "title": "一次CPI降温难言加息终结，沃什的答案或在缩表",
    "url": "https://wallstreetcn.com/premium/articles/3777020?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T05:36:05+00:00",
    "summary": "6月CPI单月降温难改政策观望，沃什力推缩表替代加息，年内利率或维持不变。"
  },
  {
    "id": "wscn:3777092",
    "domain": "股票",
    "title": "台积电Q2净利润7066亿元新台币大超预期，毛利率67.7%，AI芯片需求强劲势头持续",
    "url": "https://wallstreetcn.com/articles/3777092",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T05:31:31+00:00",
    "summary": "更多消息，持续更新中"
  },
  {
    "id": "wscn:3777075",
    "domain": "股票",
    "title": "半导体抛售潮重创亚太股市，韩股暴跌7%触发熔断，SK海力士下跌11%，布油转跌",
    "url": "https://wallstreetcn.com/articles/3777075",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T05:25:50+00:00",
    "summary": "韩国Kospi一度达7.6%并触发熔断，SK海力士与三星电子领跌，日本日经225指数同步下跌2.9%。布伦特原油转跌0.5%至每桶84.50美元，结束了此前的三日连涨。通胀数据意外走软令美联储加息预期降温，美债走强，但能源价格上行风险正为货币政策前景埋下新变数。"
  },
  {
    "id": "wscn:3777091",
    "domain": "股票",
    "title": "美国宣布对部分巴西进口商品加征25%关税，巴西总统：单边措施“没有道理”",
    "url": "https://wallstreetcn.com/articles/3777091",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T05:23:46+00:00",
    "summary": "美国贸易代表办公室在一份声明中表示，巴西在数字贸易、关税、知识产权、乙醇供应和森林砍伐方面的政策对美国商业造成了负担，将于7月22日正式实施关税措施。巴西政府及总统卢拉对此强烈拒绝，强调不承认缺乏多边贸易规则支撑的调查合法性。"
  },
  {
    "id": "wscn:3777077",
    "domain": "股票",
    "title": "创业板跌超1%，芯片半导体持续调整，存储龙头再跌停，医药股拉升，恒科指大涨超3%，科网股全线大涨",
    "url": "https://wallstreetcn.com/articles/3777077",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T05:23:25+00:00",
    "summary": "个股涨多跌少，沪深京三市约3300股飘红，上午半天成交1.49万亿。沪深两市半日成交额1.48万亿，较上个交易日缩量超过2300亿。板块方面，半导体、算力硬件产业链持续调整，先进封装、光刻机、存储器方向领跌；氟化工、稀土、油气、煤炭、券商板块跌幅居前。影视股连续反弹，AI应用、金融科技、黄金、大消费、医药板块逆势走强。"
  },
  {
    "id": "wscn:3776952",
    "domain": "股票",
    "title": "骑虎记：韩国怎样一步步把国运押在了存储芯片上",
    "url": "https://wallstreetcn.com/premium/articles/3776952?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T05:16:20+00:00",
    "summary": "所有参与者都需要音乐继续响着。"
  },
  {
    "id": "wscn:3777060",
    "domain": "股票",
    "title": "奥本海默撤销IBM 350美元目标价：软件增速仅及预期一半，股价短期将维持震荡",
    "url": "https://wallstreetcn.com/articles/3777060",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T04:15:20+00:00",
    "summary": "华尔街投行Oppenheimer下调IBM评级，指出2026至2027年软件两位数增长\"面临较大挑战\"。IT预算压缩可能对基础设施软件供应商构成短期风险，这对IBM的多条业务线均构成压力。分析师判断看涨逻辑的兑现\"需要更长时间\"，预计股价短期将维持区间震荡。"
  },
  {
    "id": "wscn:3777085",
    "domain": "股票",
    "title": "自研芯片难堪重任，苹果转向收购突围AI服务器困局",
    "url": "https://wallstreetcn.com/articles/3777085",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T03:34:05+00:00",
    "summary": "苹果自研M2 Ultra服务器芯片无力承载谷歌Gemini大模型，新版Siri被迫借道谷歌云上的英伟达GPU运行。下一代服务器芯片Baltra已延期，真正具备竞争力的M7 Ultra要到2029年才能就绪。为填补技术空白，苹果近期主动接触多家芯片初创公司并与银行家洽谈收购。"
  },
  {
    "id": "wscn:3777089",
    "domain": "股票",
    "title": "AI热潮推高通胀粘性，韩国央行加息落地，KOSPI暴跌7%触发年内第八次熔断",
    "url": "https://wallstreetcn.com/articles/3777089",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T03:27:32+00:00",
    "summary": "韩国央行今日加息25个基点至2.75%，为三年半来首次，全员通过。AI芯片出口推高经济、6月CPI达3.2%、房价连涨75周且韩元走弱，三重压力下行长明确表示将继续加息。KOSPI当日暴跌6.90%，触发年内第八次熔断。叠加杠杆ETF抛压与美股存储股崩盘，构成韩股“黑色星期四”的三重打击。"
  },
  {
    "id": "wscn:3774897",
    "domain": "股票",
    "title": "下半年资产配置机会在哪里？听徐小庆分享股债汇市场最新洞察，推演配置逻辑",
    "url": "https://wallstreetcn.com/articles/3774897",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T03:27:00+00:00",
    "summary": "7月19日徐小庆主讲Alpha线上闭门私享会：展望2026下半年大类资产配置风向，哪些资产最值得关注？"
  },
  {
    "id": "wscn:3777087",
    "domain": "股票",
    "title": "日债3%生死线！前日本央行官员警告：财政扩张恐触发央行被迫购债",
    "url": "https://wallstreetcn.com/articles/3777087",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T03:26:37+00:00",
    "summary": "前日本央行官员Seiji Adachi警告，若10年期日债收益率突破3%这一防线，将引发市场对日本财政可持续性的强烈质疑，政府极可能施压央行加码购债以压低利率。这将使央行陷入“财政主导”困境，严重阻碍其加息至1.25%及货币政策正常化进程。"
  },
  {
    "id": "wscn:3776634",
    "domain": "股票",
    "title": "CDU液冷泵:一场由AI机柜功率推动的产业升级，能否演绎“量价齐升”的成长叙事？",
    "url": "https://wallstreetcn.com/premium/articles/3776634?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T03:16:46+00:00",
    "summary": "随着AI芯片功耗提升，液冷成为高密度算力基础设施，核心部件CDU液冷泵受市场关注。作为决定流量能效的核心，CDU架构演进带动水泵向大功率、电子智能化升级。2026年下半年，英伟达与谷歌液冷平台集中部署，行业迎批量采购。其投资逻辑在于液冷渗透率提高、单泵功率上升、双泵冗余及电子屏蔽化推动的“量增与结构升级”。国内厂商具成本与响应优势，但头部认证、持续交付及长期可靠性是核心竞争力。"
  },
  {
    "id": "wscn:3777083",
    "domain": "股票",
    "title": "存储为何再度跳水？",
    "url": "https://wallstreetcn.com/articles/3777083",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T03:02:02+00:00",
    "summary": "存储芯片股本周遭遇\"过山车\"行情，美光周三单日暴跌10%，SK海力士ADR重挫9%。巴菲特炮轰AI投机泡沫引爆情绪逆转，广发香港同步下调三季度DRAM涨价预期，客户对30%涨幅强烈抵制。基本面依然亮眼，但供给扩张与需求规格下调的双重压力，正在动摇市场对高价格持续性的信心。"
  },
  {
    "id": "wscn:3777080",
    "domain": "股票",
    "title": "拆解长鑫招股书：存储的周期叙事走到哪儿了？",
    "url": "https://wallstreetcn.com/articles/3777080",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T02:30:44+00:00",
    "summary": "长鑫科技295亿元IPO叩开科创板，深拆招股书可见：2027年下半年到2028年初，可能将是本轮存储周期的阶段性高点。HBM长协锁价弱弹性，DRAM红利已近拐点。业绩暴增背后，HBM代差与募投克制，让估值天花板悬而未决。"
  },
  {
    "id": "wscn:3777081",
    "domain": "股票",
    "title": "6月信贷数据：票据持续高增，居民贷款和企业中长贷仍偏弱",
    "url": "https://wallstreetcn.com/articles/3777081",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T02:30:39+00:00",
    "summary": "6月金融数据显示信贷结构明显分化：票据融资连续三月同比多增超4000亿元，而居民信贷与企业中长贷持续走弱，企业投资意愿审慎，产能利用率创2016年以来非疫情阶段新低。企业债券成上半年社融主要支撑，下半年财政发力有望接续。央行流动性投放力度加大，货币与财政政策协同空间仍在。"
  },
  {
    "id": "wscn:3776762",
    "domain": "股票",
    "title": "WAIC大会前瞻：从\"单点突破\"到\"系统化产业兑现\"，国产算力能否加速崛起？",
    "url": "https://wallstreetcn.com/premium/articles/3776762?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T02:29:25+00:00",
    "summary": "2026年世界人工智能大会暨人工智能全球治理高级别会议（WAIC 2026）开幕在即，全球人工智能产业正处于从“以参数规模为核心的纯模型竞赛”向“以系统工程交付、通用智能体操作系统及物理世界可感知应用为导向的商业化兑现”的关键分水岭。"
  },
  {
    "id": "wscn:3777079",
    "domain": "股票",
    "title": "霍华德·马克斯：AI改变了我的判断，但没人能预测未来、不确定性仍是投资的本质",
    "url": "https://wallstreetcn.com/articles/3777079",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T02:12:23+00:00",
    "summary": "橡树资本霍华德·马克斯坦言，AI的“自主性”与“不可预测性”是人类历史上从未出现过的特质。但他同时警告，正因AI无法训练“无历史先例”的情境，人类判断仍有价值。他回顾了2008年雷曼破产后以每周4.5亿美元速度投出70亿美元的决策过程，强调真正的投资勇气是在不确定中行动，而非等待确定性。"
  },
  {
    "id": "wscn:3777073",
    "domain": "股票",
    "title": "戴蒙警告：向公众开放Mythos如同\"将弹道导弹交给个人\"",
    "url": "https://wallstreetcn.com/articles/3777073",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T01:48:22+00:00",
    "summary": "摩根大通CEO戴蒙将Anthropic旗下顶级AI模型Mythos比作\"弹道导弹\"——一旦向公众开放，后果不堪设想。这款因漏洞挖掘能力过强而被拒绝公开发布的模型，正让华尔街与华盛顿同步绷紧神经。摩根大通已是极少数获准使用Mythos的机构之一，数百名员工正全力强化防御。"
  },
  {
    "id": "wscn:3777078",
    "domain": "股票",
    "title": "76亿押注长鑫，阿里投资之变",
    "url": "https://wallstreetcn.com/articles/3777078",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T01:47:23+00:00",
    "summary": "年内A股最大IPO——长鑫科技580亿元科创板上市背后，阿里巴巴是最大赢家：76亿元押注，IPO前夜突击加仓至5%，预计浮盈17倍、账面价值逾1300亿元。这不只是一笔财务投资，更是阿里\"卖掉新零售、买入AI底座\"战略转型的缩影——三年投出360亿，当前浮盈已超2100亿元。"
  },
  {
    "id": "wscn:3777062",
    "domain": "股票",
    "title": "美联储《褐皮书》难于启齿的“秘密”：美国的隐形滞胀正在加剧",
    "url": "https://wallstreetcn.com/premium/articles/3777062?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T01:23:43+00:00",
    "summary": "利润表的窟窿如果一直填不上，下一个被拿来填的可能就是岗位"
  },
  {
    "id": "hn:48899454",
    "domain": "股票",
    "title": "$65K to work at Anthropic? Debate ensues amid IPO wave",
    "url": "https://missionlocal.org/2026/07/anthropic-sf-affordability-ipo-housing-evictions-rent/",
    "source": "gcheong",
    "platform": "hackernews",
    "points": 30,
    "published_at": "2026-07-13T21:56:52+00:00",
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
    "id": "hn:48853145",
    "domain": "股票",
    "title": "California universities stockpiling AR-15s, grenades and submachine guns",
    "url": "https://www.theguardian.com/us-news/2026/jul/09/california-universities-military-equipment",
    "source": "sizzle",
    "platform": "hackernews",
    "points": 13,
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
    "id": "hn:48774424",
    "domain": "股票",
    "title": "X has suddenly banned an account documenting Trump's corrupt stock trades",
    "url": "https://twitter.com/HQNewsNow/status/2072699828337864871",
    "source": "doener",
    "platform": "hackernews",
    "points": 22,
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
    "points": 695,
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
    "id": "hn:48915953",
    "domain": "金融",
    "title": "Stripe and Advent have made a joint offer to acquire PayPal – sources",
    "url": "https://www.reuters.com/business/finance/stripe-advent-offer-buy-paypal-more-than-53-billion-sources-say-2026-07-15/",
    "source": "rvz",
    "platform": "hackernews",
    "points": 409,
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
    "id": "rss:https://arxiv.org/abs/2607.13353",
    "domain": "金融",
    "title": "Is Deep Hedging Reinforcement Learning?",
    "url": "https://arxiv.org/abs/2607.13353",
    "source": "Fr\\'ed\\'eric Godin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T04:00:00+00:00",
    "summary": "arXiv:2607.13353v1 Announce Type: new Abstract: The deep hedging framework of Buehler et al. (2019) trains a neural network policy, via Monte Carlo simulation of price paths and stochastic gradient de"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.13526",
    "domain": "金融",
    "title": "Mapping Diplomatic Representation in Europe, 1648-1715",
    "url": "https://arxiv.org/abs/2607.13526",
    "source": "Magnus Lundgren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T04:00:00+00:00",
    "summary": "arXiv:2607.13526v1 Announce Type: new Abstract: This paper introduces new data on diplomatic representation in Europe between 1648 and 1715, drawn from Band I of the Repertorium der diplomatischen Ver"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.13844",
    "domain": "金融",
    "title": "Messy Research, Certification and the Monetization of Science",
    "url": "https://arxiv.org/abs/2607.13844",
    "source": "Johan Fourie",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T04:00:00+00:00",
    "summary": "arXiv:2607.13844v1 Announce Type: new Abstract: I study how cheaper AI-assisted research changes the institutions that certify science. AI lowers the cost of producing a polished manuscript faster tha"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.13916",
    "domain": "金融",
    "title": "Detecting unusual trading patterns on cryptocurrency exchanges by means of complexity measures",
    "url": "https://arxiv.org/abs/2607.13916",
    "source": "Jakub Zwydak, Marcin W\\k{a}torek, Jaros{\\l}aw Kwapie\\'n, Stanis{\\l}aw Dro\\.zd\\.z",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T04:00:00+00:00",
    "summary": "arXiv:2607.13916v1 Announce Type: new Abstract: Artificial transaction generation remains an important source of potential market manipulation on cryptocurrency exchanges, as it may distort reported l"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.13968",
    "domain": "金融",
    "title": "Measuring Sentiment News with Transformer-Based Language Models",
    "url": "https://arxiv.org/abs/2607.13968",
    "source": "Maria Saveria Mavillonio, Stefano Borgioli, Caterina Giannetti, Chiara Ongari, Giampiero M. Gallo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T04:00:00+00:00",
    "summary": "arXiv:2607.13968v1 Announce Type: new Abstract: Measuring sentiment from financial news is a central task in economics and finance, yet most existing indicators rely on dictionary-based approaches tha"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.13112",
    "domain": "金融",
    "title": "Anchored Geodesic Analysis for Multivariate Extremes",
    "url": "https://arxiv.org/abs/2607.13112",
    "source": "Alberto Quaini, Chen Zhou",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T04:00:00+00:00",
    "summary": "arXiv:2607.13112v1 Announce Type: cross Abstract: Extremal dependence is naturally described by the angular law of large multivariate observations. We introduce anchored geodesic component analysis (A"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.13607",
    "domain": "金融",
    "title": "Equilibrium stability as a driver of cooperation among Q-learners",
    "url": "https://arxiv.org/abs/2607.13607",
    "source": "Janusz M. Meylahn, Maximilian Sch\\\"afer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T04:00:00+00:00",
    "summary": "arXiv:2607.13607v1 Announce Type: cross Abstract: Algorithmic collusion among pricing algorithms has raised concerns about sustained supra-competitive prices and their implications for social welfare."
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.13929",
    "domain": "金融",
    "title": "VAIOM: Continuous-Input, Discrete-Output Decoder-Only Financial Sequence Modeling",
    "url": "https://arxiv.org/abs/2607.13929",
    "source": "Yiming Ma, Xinyu Chen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T04:00:00+00:00",
    "summary": "arXiv:2607.13929v1 Announce Type: cross Abstract: Financial observations are continuous, heterogeneous, and noisy, whereas decoder-only next-token models are usually built around discrete symbolic inp"
  },
  {
    "id": "rss:https://arxiv.org/abs/2404.13637",
    "domain": "金融",
    "title": "Extremal cases of distortion risk measures with partial information",
    "url": "https://arxiv.org/abs/2404.13637",
    "source": "Mengshuo Zhao, Narayanaswamy Balakrishnan, Chuancun Yin, Hui Shao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T04:00:00+00:00",
    "summary": "arXiv:2404.13637v5 Announce Type: replace Abstract: This paper investigates the impact of distributional uncertainty on key risk measures under the partial knowledge of underlying distributions charac"
  },
  {
    "id": "rss:https://arxiv.org/abs/2411.04321",
    "domain": "金融",
    "title": "Robust and Fast Bass Local Volatility",
    "url": "https://arxiv.org/abs/2411.04321",
    "source": "Hao Qin, Charlie Che, Ruozhong Yang, Liming Feng",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T04:00:00+00:00",
    "summary": "arXiv:2411.04321v3 Announce Type: replace Abstract: The Bass Local Volatility Model, as studied in {henry2021bass}, stands out for its ability to eliminate the need for interpolation between maturitie"
  },
  {
    "id": "rss:https://arxiv.org/abs/2501.17600",
    "domain": "金融",
    "title": "Towards post-growth policymaking: Barriers and enablers for wellbeing economy and Doughnut economics government initiatives",
    "url": "https://arxiv.org/abs/2501.17600",
    "source": "Laura Angresius, Milena Buchs, Alessia Greselin, Daniel W. O'Neill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T04:00:00+00:00",
    "summary": "arXiv:2501.17600v3 Announce Type: replace Abstract: Providing wellbeing for all while safeguarding planetary boundaries requires governments to pursue post-growth policies. An important question is ho"
  },
  {
    "id": "rss:https://arxiv.org/abs/2510.11261",
    "domain": "金融",
    "title": "Mean-Field Price Formation on Trees with Multi-Population and Non-Rational Agents",
    "url": "https://arxiv.org/abs/2510.11261",
    "source": "Masaaki Fujii",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T04:00:00+00:00",
    "summary": "arXiv:2510.11261v4 Announce Type: replace Abstract: This work solves the equilibrium price formation problem for the risky stock by combining mean-field game theory with the binomial tree framework, a"
  },
  {
    "id": "rss:https://arxiv.org/abs/2511.21929",
    "domain": "金融",
    "title": "Extended Convolution Bounds on the Fr\\'{e}chet Problem: Robust Risk Aggregation and Risk Sharing",
    "url": "https://arxiv.org/abs/2511.21929",
    "source": "Peng Liu, Yang Liu, Houhan Teng",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T04:00:00+00:00",
    "summary": "arXiv:2511.21929v2 Announce Type: replace Abstract: In this paper, we provide extended convolution bounds for the Fr\\'{e}chet problem and discuss related implications in quantitative risk management. "
  },
  {
    "id": "rss:https://arxiv.org/abs/2601.07664",
    "domain": "金融",
    "title": "Crypto Pricing with Hidden Factors",
    "url": "https://arxiv.org/abs/2601.07664",
    "source": "Matthew Brigida",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T04:00:00+00:00",
    "summary": "arXiv:2601.07664v2 Announce Type: replace Abstract: We estimate risk premia in the cross-section of cryptocurrency returns using the Giglio-Xiu (2021) three-pass approach, allowing for omitted latent "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.02528",
    "domain": "金融",
    "title": "Auditing Asset-Specific Preferences in Financial Large Language Models: Evidence from Bitcoin Representations and Portfolio Allocation",
    "url": "https://arxiv.org/abs/2606.02528",
    "source": "Wenbin Wu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T04:00:00+00:00",
    "summary": "arXiv:2606.02528v2 Announce Type: replace Abstract: Large language models now power robo-advisors and trading agents, yet whether they carry built-in biases toward specific assets is largely untested."
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.11328",
    "domain": "金融",
    "title": "Strategic OTC market making with reputation feedback",
    "url": "https://arxiv.org/abs/2607.11328",
    "source": "Alexander Barzykin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T04:00:00+00:00",
    "summary": "arXiv:2607.11328v2 Announce Type: replace Abstract: Electronic over-the-counter (OTC) liquidity provision is increasingly shaped not only by the price of the next quote, but also by a dealer's accumul"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.12479",
    "domain": "金融",
    "title": "Ito-Wentzell Formula and Dupire Stochastic PDE",
    "url": "https://arxiv.org/abs/2607.12479",
    "source": "Vladimir Lucic",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T04:00:00+00:00",
    "summary": "arXiv:2607.12479v2 Announce Type: replace Abstract: Starting from the classic result of Wentzell, we derive a conditional forward equation and an associated stochastic Dupire PDE for a local-stochasti"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.13002",
    "domain": "金融",
    "title": "Shared Bidding Algorithms and Competition: Evidence from Electricity Markets",
    "url": "https://arxiv.org/abs/2607.13002",
    "source": "Nicolas Eschenbaum",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T04:00:00+00:00",
    "summary": "arXiv:2607.13002v2 Announce Type: replace Abstract: Competing firms increasingly delegate pricing and bidding decisions to algorithms supplied by the same third-party providers. We study whether a sha"
  },
  {
    "id": "rss:https://arxiv.org/abs/2504.02814",
    "domain": "金融",
    "title": "Convergence of the Markovian Iteration for Coupled FBSDEs via a Differentiation Approach",
    "url": "https://arxiv.org/abs/2504.02814",
    "source": "Zhipeng Huang, Cornelis W. Oosterlee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T04:00:00+00:00",
    "summary": "arXiv:2504.02814v2 Announce Type: replace-cross Abstract: In this paper, we investigate the Markovian iteration method for solving coupled forward-backward stochastic differential equations (FBSDEs) w"
  },
  {
    "id": "rss:https://arxiv.org/abs/2511.01923",
    "domain": "金融",
    "title": "The Efficiency Costs of Information Assurance in AI-Enabled Labor Markets: Evidence from LinkedIn's Policy Changes",
    "url": "https://arxiv.org/abs/2511.01923",
    "source": "Lei Chen, Chaoyue Gao, Alvin Leung, Gavin Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T04:00:00+00:00",
    "summary": "arXiv:2511.01923v2 Announce Type: replace-cross Abstract: Generative artificial intelligence (GenAI) systems rely heavily on user-generated data for training. As governments and platforms impose incre"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.13866",
    "domain": "金融",
    "title": "AI Alignment Amplifies the Role of Race, Gender, and Disability in Hiring Decisions",
    "url": "https://arxiv.org/abs/2605.13866",
    "source": "Ze Wang, Guobin Shen, Michael Thaler",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T04:00:00+00:00",
    "summary": "arXiv:2605.13866v2 Announce Type: replace-cross Abstract: Humans increasingly delegate consequential decisions to language models, yet whether these systems reproduce or reshape human patterns of disc"
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
    "id": "hn:48824584",
    "domain": "金融",
    "title": "JPMorgan, BofA and Others Explore Buying Card Network to Raise Debit-Card Fees",
    "url": "https://www.wsj.com/finance/banking/jpmorgan-bank-of-america-and-other-banks-explore-a-deal-to-shake-up-payments-world-9d8639fb",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-07-07T22:04:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:48849827",
    "domain": "金融",
    "title": "FrontierFinance: The largest open benchmark for investor workflows",
    "url": "https://research.samaya.ai/benchmarks/frontier-finance",
    "source": "ashwinpp",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-07-09T17:49:05+00:00",
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
  }
]
```
