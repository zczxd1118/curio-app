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

- 今日日期：`2026-06-06`
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
  "date": "2026-06-06",
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
    "points": 2875672,
    "published_at": "2026-01-15T03:56:12+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n1. 构建智能体设计模式：反射、工具使用、规划与多智能体工作流；\n2. 将人工智能与外部工具集成：数据库、API、网络搜索与代码执行；\n3. 评估并优化人工智能系统：性能指标、错误分析与生产部署"
  },
  {
    "id": "bvid:BV1yjz5BLEoY",
    "domain": "AI",
    "title": "黑马程序员大模型RAG与Agent智能体项目实战教程，基于主流的LangChain技术从大模型提示词到实战项目",
    "url": "http://www.bilibili.com/video/av115931552416097",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 2544969,
    "published_at": "2026-01-21T06:06:02+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260121\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\n人工智能开发热门教程：\nAI大模型开发：BV1h1V"
  },
  {
    "id": "bvid:BV1E7wtzaEdq",
    "domain": "AI",
    "title": "从 LLM 到 Agent Skill，一期视频带你打通底层逻辑！",
    "url": "http://www.bilibili.com/video/av116227955497963",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 1095534,
    "published_at": "2026-03-14T14:22:56+00:00",
    "summary": "AI 核心概念大串联：LLM, Token, Context, Context Window, Prompt, User Prompt, System Prompt, Tool, MCP, Agent, Agent Skill，一期视频带你打通 AI 底层逻辑！"
  },
  {
    "id": "bvid:BV1yorUYWEGD",
    "domain": "AI",
    "title": "普通人也可以看的 AI 编程指南 | Cursor 教程｜Cursor 使用技巧和思路｜如何免费使用 Cursor｜AI 编程",
    "url": "http://www.bilibili.com/video/av113786467981446",
    "source": "不正经的前端啊",
    "platform": "bilibili",
    "points": 936453,
    "published_at": "2025-01-07T10:01:48+00:00",
    "summary": "普通人也可以看的 AI 编程指南\n全网最详细的 Cursor 教程\nCursor 核心功能、使用技巧和思路\n如何免费白嫖 Cursor"
  },
  {
    "id": "bvid:BV1ZzvUBXEoL",
    "domain": "AI",
    "title": "【2026最新版】保姆级AI Agent智能体系统教程，手把手带你从0基础开始搭建企业级AI Agent智能体！全程干货无废话！让你少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av115818910194374",
    "source": "极客教学",
    "platform": "bilibili",
    "points": 751951,
    "published_at": "2026-01-01T08:40:14+00:00",
    "summary": "【2026最新版】保姆级AI Agent智能体系统教程，手把手带你从0基础开始搭建企业级AI Agent智能体！全程干货无废话！让你少走99%的弯路！"
  },
  {
    "id": "bvid:BV1WBG9zgECp",
    "domain": "AI",
    "title": "史上最强 AI 编程工具免费啦！Cursor 保姆级使用教程！新手友好！看到就是赚到！｜ 集成 MCP ！",
    "url": "http://www.bilibili.com/video/av114426116120045",
    "source": "AfterShip",
    "platform": "bilibili",
    "points": 661209,
    "published_at": "2025-05-01T04:00:00+00:00",
    "summary": "相信你已经在网上刷到过不少的 AI 工具，但如果你让我推荐最值得我们每个人学习的一款 AI 工具，那绝对就是史上最强的 AI 编程工具 —— Cursor。为此，我们录制了一个保姆级的 Cursor 新手教程，在这里免费分享给大家。即使你是一个对 AI 完全 0 基础的新手小白，看完这个视频后，你也可以彻底了解 Cursor 这个软件，并知道如何从 0 到 1 用 Cursor 做出入门级的 AI"
  },
  {
    "id": "bvid:BV11NNAz5EKn",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！",
    "url": "http://www.bilibili.com/video/av116187623069851",
    "source": "AI-智能体搭建教程",
    "platform": "bilibili",
    "points": 607377,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 348667,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1GyGX6TEDi",
    "domain": "AI",
    "title": "1个人，如何通过Vibe Coding快速实现变现？",
    "url": "http://www.bilibili.com/video/av116650858847182",
    "source": "老麦的工具库",
    "platform": "bilibili",
    "points": 340426,
    "published_at": "2026-05-29T12:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1BFouBYERu",
    "domain": "AI",
    "title": "手把手教你在Claude Code中熟练使用SKILL技能！",
    "url": "http://www.bilibili.com/video/av116453927814340",
    "source": "我是阿众",
    "platform": "bilibili",
    "points": 254210,
    "published_at": "2026-04-23T12:09:57+00:00",
    "summary": "本期视频耗时半个月制作，希望大家能够点赞三连加关注，感谢！\n\n内容包括了一下几个方面：\n00:27 Skill简介\n01:39 Skill和Plugin的区别\n02:51 安装他人的Skill\n04:44 手动创建自己的SKill\n07:30 控制Skill的触发行为\n08:01 Skill的查看和管理\n08:20 Skill的停用和删除\n08:55 找优质Skill的三种渠道"
  },
  {
    "id": "bvid:BV1AHDuBoE2S",
    "domain": "AI",
    "title": "锐评vibe coding工具“从夯到拉”",
    "url": "http://www.bilibili.com/video/av116347090502349",
    "source": "布鲁歇一歇",
    "platform": "bilibili",
    "points": 234170,
    "published_at": "2026-04-04T15:19:25+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1ui4y1m7Ap",
    "domain": "AI",
    "title": "挑战全网最硬核服务器基础知识",
    "url": "http://www.bilibili.com/video/av553433619",
    "source": "尚诚云课堂",
    "platform": "bilibili",
    "points": 228132,
    "published_at": "2022-04-22T10:33:01+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1qGc7zwEX6",
    "domain": "AI",
    "title": "史上最强 AI 编程工具Cursor来啦！Cursor保姆级使用教程！新手友好！看到就是赚到！！！",
    "url": "http://www.bilibili.com/video/av116061928226926",
    "source": "知名的阿呆同学",
    "platform": "bilibili",
    "points": 225681,
    "published_at": "2026-02-19T07:34:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1e3t4etExj",
    "domain": "AI",
    "title": "手摸手的AI编程cursor实战【小白教程】",
    "url": "http://www.bilibili.com/video/av113148447169565",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 222582,
    "published_at": "2024-09-17T01:00:00+00:00",
    "summary": "喜欢的朋友可以三连+关注～这对我真的很重要"
  },
  {
    "id": "bvid:BV1Yi5M6DERk",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116560144369496",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 221523,
    "published_at": "2026-05-12T06:24:19+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 173463,
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
    "points": 152128,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV16NvCBrEVs",
    "domain": "AI",
    "title": "什么是Vibe Coding，以及怎么使用？",
    "url": "http://www.bilibili.com/video/av115797133368973",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 143301,
    "published_at": "2025-12-28T12:36:33+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1RNTtzMENj",
    "domain": "AI",
    "title": "从零编写MCP并发布上线，超简单！手把手教程",
    "url": "http://www.bilibili.com/video/av114630814862349",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 140921,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV13YRjBTEPb",
    "domain": "AI",
    "title": "Hermes Agent零基础、保姆级教程，小白也能轻松玩转",
    "url": "http://www.bilibili.com/video/av116503638706867",
    "source": "iwenwiki",
    "platform": "bilibili",
    "points": 122047,
    "published_at": "2026-05-02T06:51:59+00:00",
    "summary": "全B站最详细的Hermes Agent教程，从部署到玩转！零基础，小白也能轻松玩转Hermes Agent，真正的AI助手，恐怖如斯！"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 98705,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1fRSfBWE5X",
    "domain": "AI",
    "title": "vlog｜白天上班 晚上vibe coding，准备一个月上架我的第一款App！",
    "url": "http://www.bilibili.com/video/av116357526003120",
    "source": "chocpink_AI版",
    "platform": "bilibili",
    "points": 95046,
    "published_at": "2026-04-06T11:33:25+00:00",
    "summary": "想了很久终于开始了这件事——vibe coding！\n\n下面快速总结了我用到的一些工具：\nApptweak：竞品调研\nfigma make、google stitch、impeccable插件：生成UI页面\nfigma mcp/plugin：连接到cursor\npinterest/小红书/iconfont：找图片/icon素材\nGrok：生图、素材优化\ncursor+Xcode（swift）：落地"
  },
  {
    "id": "bvid:BV1KoGE6cE53",
    "domain": "AI",
    "title": "🚀Claude Code重大突破：Workflow功能完整实战教程！ultrawork召唤无数个Agent协同！自动生成JS脚本实现可复用的精准可控工作流",
    "url": "http://www.bilibili.com/video/av116629702777532",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 93689,
    "published_at": "2026-05-24T13:11:48+00:00",
    "summary": "视频简介：\n 全球首测！Anthropic未官宣的Claude Code Workflow隐藏功能完整使用指南，三大阶段六种形态精准解析！AI编程进入脚本化新纪元\n\n 本期视频详细演示了Anthropic为Claude Code V2.1.47和V2.1.48秘密新增的颠覆性Workflow功能！这个被官方从Changelog中紧急删除却未从代码中移除的&quot;隐藏神器&quot;，将成为继M"
  },
  {
    "id": "bvid:BV1JRPKzyEyG",
    "domain": "AI",
    "title": "2026 程序员自救指南：Claude Code 企业级全链路实战。抛弃那些过时的付费课！这套教程能让你在裁员潮中多出 5 年职场竞争力。",
    "url": "http://www.bilibili.com/video/av116169419855077",
    "source": "AI大模型全栈",
    "platform": "bilibili",
    "points": 92381,
    "published_at": "2026-03-04T06:22:03+00:00",
    "summary": "【视频配套籽料、学习路线、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】"
  },
  {
    "id": "bvid:BV1KX9jB8E9M",
    "domain": "AI",
    "title": "【2026最新版】目前B站最全最细的 CurSor AI编程零基础全套教程，手把手教你搭建高效Cursor工作流，全程干货无废话！比付费效果强十倍",
    "url": "http://www.bilibili.com/video/av116328887225403",
    "source": "AI大模型技术教程",
    "platform": "bilibili",
    "points": 71572,
    "published_at": "2026-04-01T10:12:34+00:00",
    "summary": "视频配套文档课件笔记代码及AI大模型学习路线图戳这里获取→https://www.bilibili.com/read/cv41777105/?jump_opus=1"
  },
  {
    "id": "bvid:BV1YP5W6ZEP9",
    "domain": "AI",
    "title": "VibeCoding就该这么做！",
    "url": "http://www.bilibili.com/video/av116552997276199",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 63850,
    "published_at": "2026-05-14T09:00:00+00:00",
    "summary": "UV教程：https://www.bilibili.com/video/BV1Stwfe1E7s/\n代码及知识星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV1KocTzHE3Z",
    "domain": "AI",
    "title": "2027版 Cursor+Claude AI编程 1天快速上手 视频教程",
    "url": "http://www.bilibili.com/video/av116040285622077",
    "source": "java1234官方",
    "platform": "bilibili",
    "points": 62268,
    "published_at": "2026-02-09T10:57:55+00:00",
    "summary": "本课程主要讲解Cursor简介，Cursor下载安装，Cursor生成helloWorld网页，Cursor会话里的Cursor会话里的Agent,Plan,Debug,Ask区别以及使用，Cursor常用模型介绍，Cursor模型会话上下文介绍，以及最后利用Cursor Opus4.6快速生成一个Java项目 -SpringBoot4+Vue3的学生信息管理系统，利用Cursor Opus4.6"
  },
  {
    "id": "bvid:BV1ZjDYB7Eam",
    "domain": "AI",
    "title": "从 0 到 1：6小时掌握 Vibe Coding！ Claude Code ＋ AI 这支影片直接让你超越 90% AI 玩家",
    "url": "http://www.bilibili.com/video/av116362122894759",
    "source": "李哈利Harry",
    "platform": "bilibili",
    "points": 53298,
    "published_at": "2026-04-08T11:00:00+00:00",
    "summary": "🌟 加入AI大师社群并运用AI创业赚钱：https://www.skool.com/aiagent/about?ref=f2b566934c5c4639aaa47ab1fe39310e\n📌 加入我的免费 Skool 社群，获取模板：https://www.skool.com/aiagent8/about?ref=f2b566934c5c4639aaa47ab1fe39310e\n\n🚧 开始使用 n8"
  },
  {
    "id": "bvid:BV1VCVS6PEAd",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent零基础全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116668525186915",
    "source": "大模型入门教程",
    "platform": "bilibili",
    "points": 44537,
    "published_at": "2026-05-31T09:46:57+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1SY7C6nEwU",
    "domain": "AI",
    "title": "【开源】我制作了一个vibe coding键盘",
    "url": "http://www.bilibili.com/video/av116696660576856",
    "source": "工科男孙老师",
    "platform": "bilibili",
    "points": 34423,
    "published_at": "2026-06-05T10:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 34126,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 29556,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV1j67k6oENA",
    "domain": "AI",
    "title": "Claude Ultracode 超码 上线 | 操控100个Agent并行开发  保姆级实战教程",
    "url": "http://www.bilibili.com/video/av116697163896598",
    "source": "技术胖",
    "platform": "bilibili",
    "points": 28690,
    "published_at": "2026-06-05T11:05:27+00:00",
    "summary": "Ultracode 功能太好用了，就是Claude Code昨天新出的“超码”功能，如果你Vibe Coding ，那这个技巧一定要掌握。他解决了Claude Code 一次性跑不完大型任务的问题。\n本期视频很长，但看完你的AI Coding能力将超越整个团队。并且把视频内容整理成了文字版，放在评论区，方便你学习使用。视频很干，可以先喝口水润润喉咙。"
  },
  {
    "id": "bvid:BV1EZd3BBEB5",
    "domain": "AI",
    "title": "手把手实战教学：我是如何用一个周末掌握Claude Code的",
    "url": "http://www.bilibili.com/video/av116539105739515",
    "source": "AliAbdaal",
    "platform": "bilibili",
    "points": 26341,
    "published_at": "2026-05-09T13:00:00+00:00",
    "summary": "朋友们，有个叫Claude Code的工具，过去两个月我用它做了很多事情，它真的改变了我的整个工作方式，而且我感觉到Claude Code让人与人之间的差距加速变大。。。这个视频做完我就要发给还没尝试过的亲友！\n看完这条视频，你会了解如何让AI采访你来生成AI工具点子，如何筛选高杠杆项目，如何一边制作工具一边学习AI知识和开发技术概念。你会意识到，在AI时代，你最大的资产也许就是好奇心和突破技术摩"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22487,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1WwD9BEES7",
    "domain": "AI",
    "title": "保姆级ClaudeCode从0到1完整实战项目",
    "url": "http://www.bilibili.com/video/av116391835343750",
    "source": "是茂宇呀",
    "platform": "bilibili",
    "points": 18226,
    "published_at": "2026-04-12T12:59:04+00:00",
    "summary": "花了两天录制了这个教程帮助到家从0到1的完整做一个项目并带大家入门，项目中用到的相关提示词及文档教我都分享了在了www.maoyu.site"
  },
  {
    "id": "bvid:BV1HaVh6fEhn",
    "domain": "AI",
    "title": "AI编程进阶必修课！Claude Code+Harness AI 工程化实战！电商项目全流程落地，规范开发、代码治理、简历加分一站式吃透",
    "url": "http://www.bilibili.com/video/av116656764421367",
    "source": "图灵程序员诸葛",
    "platform": "bilibili",
    "points": 17784,
    "published_at": "2026-05-29T08:01:23+00:00",
    "summary": "大模型资料看这里聆取https://www.bilibili.com/read/cv49754608/?jump_opus=1"
  },
  {
    "id": "bvid:BV1HmojYNE76",
    "domain": "AI",
    "title": "15分钟Java快速构建MCP Server",
    "url": "http://www.bilibili.com/video/av114337213647750",
    "source": "有趣程序员的boredlife",
    "platform": "bilibili",
    "points": 17213,
    "published_at": "2025-04-14T16:26:09+00:00",
    "summary": "15分钟Java快速构建MCP Server"
  },
  {
    "id": "bvid:BV1v4rnBSEPp",
    "domain": "AI",
    "title": "ClaudeCode 使用教程 从零开发一个 AA 记账程序",
    "url": "http://www.bilibili.com/video/av115892159518525",
    "source": "基本没用0_0",
    "platform": "bilibili",
    "points": 14059,
    "published_at": "2026-01-14T07:42:40+00:00",
    "summary": "ClaudeCode 使用教程 从零开发一个 AA 记账程序\n看看 ClaudeCode 花了我 3$ 写出来了个什么东西😂\n\n中转站推荐：\nhttps://shop.xuedingtoken.com/?dist=QBYL2RSL\n\n\nGitHub 仓库地址：https://github.com/zty42/team-expense-tracker"
  },
  {
    "id": "bvid:BV1x6Vt6dEef",
    "domain": "AI",
    "title": "100 小时测试 Claude Code vs Codex（真实结果）",
    "url": "http://www.bilibili.com/video/av116656495925868",
    "source": "设计之道",
    "platform": "bilibili",
    "points": 12726,
    "published_at": "2026-05-29T06:44:49+00:00",
    "summary": "【海外 AI 订阅】\n国内直连，支付宝付款，不用代理，\n一站订阅 ChatGPT / Codex / Claude Code / X\n订阅链接：https://bewild.ai?code=SJZD\n订阅时请填优惠邀请码：SJZD，具体优惠金额以官网为准。\n\n【视频介绍】\n我花了 100 个小时测试 Claude Code 和 Codex，结果真的让我非常意外。\n相同的提示词、相同的项目构建、两个"
  },
  {
    "id": "bvid:BV1hEVd6yEcn",
    "domain": "AI",
    "title": "【2026最新】全B站最详细AI Agent开发教程，手把手教你搭建企业级Agent智能体！从入门到实战，学完即就业，带你玩转AI Agent！",
    "url": "http://www.bilibili.com/video/av116673440909829",
    "source": "Agent开发",
    "platform": "bilibili",
    "points": 10600,
    "published_at": "2026-06-01T06:35:48+00:00",
    "summary": "【2026最新】全B站最详细AI Agent开发教程，手把手教你搭建企业级Agent智能体！从入门到实战，学完即就业，带你玩转AI Agent！"
  },
  {
    "id": "bvid:BV13HEw6rEDa",
    "domain": "AI",
    "title": "【2026最新】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116691140872014",
    "source": "绕着宇宙飞一圈",
    "platform": "bilibili",
    "points": 9915,
    "published_at": "2026-06-04T09:39:37+00:00",
    "summary": "求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 9520,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1BBV661E7n",
    "domain": "AI",
    "title": "一天吃透ClaudeCode | 零基础从入门直达精通，告别低效敲代码，解锁Vibe Coding编程新范式！",
    "url": "http://www.bilibili.com/video/av116680856443049",
    "source": "码士集团-马小菲呀",
    "platform": "bilibili",
    "points": 9120,
    "published_at": "2026-06-04T06:01:16+00:00",
    "summary": "ClaudeCode零基础从入门直达精通，告别低效敲代码，解锁Vibe Coding编程新范式！"
  },
  {
    "id": "bvid:BV1cCVZ6NEym",
    "domain": "AI",
    "title": "这绝对是B站讲的最全最细的VibeCoding系统教程，手把手带你从环境安装到实战，包含所有干货！让你少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av116673944492771",
    "source": "峰识在大模型",
    "platform": "bilibili",
    "points": 8141,
    "published_at": "2026-06-01T08:53:14+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n本视频配套课件笔记代码/学习大纲/大模型学习路线戳这里获取→https://www.bilibili.com/opus/1195847460814061571?spm_id_from=333.1387.0.0\n另外有需要AI大模型学习路线图+必看书籍（国内外大牛著作）+入门及进阶视频教程+项目实战及源码提供+面试实战场景"
  },
  {
    "id": "bvid:BV1CEVm6kE53",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent零基础全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116685336021756",
    "source": "大模型官方课程",
    "platform": "bilibili",
    "points": 8016,
    "published_at": "2026-06-03T09:14:12+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1L3Vd6nEeB",
    "domain": "AI",
    "title": "【2026版】这可能是B站唯一将Codex+Claude Code讲明白的教程，从下载安装到环境配置、核心功能、使用技巧到项目实战讲透，存下吧，比啃书好太多了！",
    "url": "http://www.bilibili.com/video/av116673726257360",
    "source": "12点就睡的林同学",
    "platform": "bilibili",
    "points": 7790,
    "published_at": "2026-06-01T08:08:09+00:00",
    "summary": "别只收藏，不实操。这期 Codex保姆级完整教程 的配套资料，我已经整理好了，适合想系统学习 Codex、AI编程助手、AI开发提效 的同学。资料内容包括：\nCodex入门使用指南、安装与环境配置流程、常用功能操作清单、高效提示词模、编程实战案例拆解、常见问题与避坑总、从入门到项目落地的学习路线图\n如果你想真正学会 Codex，而不是只停留在“看过视频”的层面建议 视频 + 资料 一起搭配学习。"
  },
  {
    "id": "bvid:BV1ZSVG6eE3V",
    "domain": "AI",
    "title": "【cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av116662284130312",
    "source": "非六于期",
    "platform": "bilibili",
    "points": 7617,
    "published_at": "2026-05-30T07:13:36+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV19jL46gEab",
    "domain": "AI",
    "title": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！",
    "url": "http://www.bilibili.com/video/av116611415541849",
    "source": "Agent搭建",
    "platform": "bilibili",
    "points": 7471,
    "published_at": "2026-05-21T07:43:25+00:00",
    "summary": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！"
  },
  {
    "id": "bvid:BV1oUVc6vEEY",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的 AI 编程工具Cursor保姆级教程！Cursor保姆级安装使用教程！新手友好！看到就是赚到！！！",
    "url": "http://www.bilibili.com/video/av116639383159883",
    "source": "AI大模型教学",
    "platform": "bilibili",
    "points": 7203,
    "published_at": "2026-05-26T06:24:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:48377404",
    "domain": "AI 算力 / 半导体",
    "title": "Use your Nvidia GPU's VRAM as swap space on Linux",
    "url": "https://github.com/c0dejedi/nbd-vram",
    "source": "tanelpoder",
    "platform": "hackernews",
    "points": 467,
    "published_at": "2026-06-02T22:55:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:48352939",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia RTX Spark",
    "url": "https://www.nvidia.com/en-us/products/rtx-spark/",
    "source": "shenli3514",
    "platform": "hackernews",
    "points": 426,
    "published_at": "2026-06-01T05:24:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:48355720",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft builds MacBook Pro rival with NVIDIA-powered Surface Laptop Ultra",
    "url": "https://www.windowslatest.com/2026/06/01/microsoft-builds-its-ultimate-macbook-pro-rival-with-the-nvidia-powered-surface-laptop-ultra/",
    "source": "jbk",
    "platform": "hackernews",
    "points": 286,
    "published_at": "2026-06-01T12:04:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:48356654",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Cosmos 3",
    "url": "https://developer.nvidia.com/blog/develop-physical-ai-reasoning-world-and-action-models-with-nvidia-cosmos-3/",
    "source": "tosh",
    "platform": "hackernews",
    "points": 149,
    "published_at": "2026-06-01T13:32:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:48356312",
    "domain": "AI 算力 / 半导体",
    "title": "Launch HN: Expanse (YC P26) – Unlock Wasted GPU Capacity",
    "url": "https://news.ycombinator.com/item?id=48356312",
    "source": "ismaeel_bashir",
    "platform": "hackernews",
    "points": 101,
    "published_at": "2026-06-01T13:05:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:48398107",
    "domain": "AI 算力 / 半导体",
    "title": "Nemotron 3 Ultra: Open Moe Hybrid Mamba-Transformer for Agentic Reasoning [pdf]",
    "url": "https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf",
    "source": "victormustar",
    "platform": "hackernews",
    "points": 23,
    "published_at": "2026-06-04T13:06:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:48234574",
    "domain": "AI 算力 / 半导体",
    "title": "How do you build a semiconductor company on something that's free?",
    "url": "https://www.siliconimist.com/p/the-open-source-silicon-business",
    "source": "johncole",
    "platform": "hackernews",
    "points": 99,
    "published_at": "2026-05-22T11:49:04+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/geopolitics-ai-and-jensen-huang-fuel-electronics-rock-and-roll-era/",
    "domain": "AI 算力 / 半导体",
    "title": "Geopolitics, AI, and Jensen Huang Fuel Electronics’ Rock-and-Roll Era",
    "url": "https://www.eetimes.com/geopolitics-ai-and-jensen-huang-fuel-electronics-rock-and-roll-era/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T22:00:00+00:00",
    "summary": "Jensen Huang and AI frenzy steal the show at Computex 2026—dive in to see how Taiwan leads the electronics. The post Geopolitics, AI, and Jensen Huang Fuel Electronics’ Rock-and-Roll Era appeared firs"
  },
  {
    "id": "rss:https://www.eetimes.com/manufacturing-accelerates-in-may-amid-inflation-and-geopolitical-headwinds/",
    "domain": "AI 算力 / 半导体",
    "title": "Manufacturing Accelerates in May Amid Inflation and Geopolitical Headwinds",
    "url": "https://www.eetimes.com/manufacturing-accelerates-in-may-amid-inflation-and-geopolitical-headwinds/",
    "source": "News Desk",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T13:17:36+00:00",
    "summary": "Manufacturing expanded further in May despite Inflation and lower GDP. The post Manufacturing Accelerates in May Amid Inflation and Geopolitical Headwinds appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/chips-act-2-0-puts-demand-at-center-of-europes-semiconductor-strategy/",
    "domain": "AI 算力 / 半导体",
    "title": "Chips Act 2.0 Puts Demand at Center of Europe’s Semiconductor Strategy",
    "url": "https://www.eetimes.com/chips-act-2-0-puts-demand-at-center-of-europes-semiconductor-strategy/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T07:00:00+00:00",
    "summary": "Chips Act 2.0 shifts EU focus from factory subsidies to chip design and demand. The post Chips Act 2.0 Puts Demand at Center of Europe’s Semiconductor Strategy appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/netrasemi-brings-up-a2000-ai-chip-begins-customer-evaluation-phase/",
    "domain": "AI 算力 / 半导体",
    "title": "Netrasemi Brings Up A2000 AI Chip, Begins Customer Evaluation Phase",
    "url": "https://www.eetimes.com/netrasemi-brings-up-a2000-ai-chip-begins-customer-evaluation-phase/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T22:00:00+00:00",
    "summary": "Indian startup Netrasemi launched the A2000 AI chip built on a 12-nm technology node. The post Netrasemi Brings Up A2000 AI Chip, Begins Customer Evaluation Phase appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/computex-2026-are-we-heading-for-the-agentic-pc-era-yet/",
    "domain": "AI 算力 / 半导体",
    "title": "Computex 2026: Are We Heading for the Agentic PC Era Yet?",
    "url": "https://www.eetimes.com/computex-2026-are-we-heading-for-the-agentic-pc-era-yet/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T13:59:22+00:00",
    "summary": "In this video interview, explore whether agentic PCs are truly here as Nvidia and Microsoft unveil new tech at Computex 2026. The post Computex 2026: Are We Heading for the Agentic PC Era Yet? appeare"
  },
  {
    "id": "rss:https://www.eetimes.com/european-electronic-waste-dilemma/",
    "domain": "AI 算力 / 半导体",
    "title": "European Electronic Waste Dilemma",
    "url": "https://www.eetimes.com/european-electronic-waste-dilemma/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T07:30:00+00:00",
    "summary": "European electronic waste is being collected, but the economics of recycling are complex. The post European Electronic Waste Dilemma appeared first on EE Times."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/nsa-using-clause-mythos-for-offensive-cyber-operations-report-claims-says-half-a-dozen-anthropic-engineers-embedded-inside-the-agency",
    "domain": "AI 算力 / 半导体",
    "title": "NSA using Claude Mythos for 'offensive cyber operations,' report claims — says 'half-a-dozen' Anthropic engineers embedded inside the agency",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/nsa-using-clause-mythos-for-offensive-cyber-operations-report-claims-says-half-a-dozen-anthropic-engineers-embedded-inside-the-agency",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T16:53:46+00:00",
    "summary": "US National Security Agency reportedly using Mythos for conducting cyber-attacks — report reveals Anthropic engineers inside the NSA"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/mini-pcs/aoostar-mini-pcs-bring-elite-ryzen-power-in-a-tiny-footprint-for-under-usd400",
    "domain": "AI 算力 / 半导体",
    "title": "Aoostar mini-PCs bring elite Ryzen power in a tiny footprint for under $400",
    "url": "https://www.tomshardware.com/desktops/mini-pcs/aoostar-mini-pcs-bring-elite-ryzen-power-in-a-tiny-footprint-for-under-usd400",
    "source": "Sponsored",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T16:52:17+00:00",
    "summary": "Aoostar's Maco, G-Flip, and Gem12 Max mini-PCs go on sale for a limited time on AliExpress with free shipping from a local U.S. warehouse."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-will-reportedly-upgrade-its-wildcat-lake-refresh-to-an-8-core-config-next-year-leak-claims-top-end-silicon-tipped-to-feature-4-p-cores-and-4-lp-e-cores-as-part-of-core-400-series",
    "domain": "AI 算力 / 半导体",
    "title": "Intel will reportedly upgrade its Wildcat Lake refresh to an 8-core config next year, leak claims — top-end silicon tipped to feature 4 P-cores and 4 LP-E cores as part of 'Core 400' series",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-will-reportedly-upgrade-its-wildcat-lake-refresh-to-an-8-core-config-next-year-leak-claims-top-end-silicon-tipped-to-feature-4-p-cores-and-4-lp-e-cores-as-part-of-core-400-series",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T16:02:36+00:00",
    "summary": "Intel's Wildcat Lake refresh that's supposedly debuting next year will shift focus to a more upmarket audience, only refreshing its Core 5 and Core 7 tiers. The new silicon at the top-end would featur"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/acer-ma200-1tb-ssd-review",
    "domain": "AI 算力 / 半导体",
    "title": "Acer MA200 1TB SSD Review: Good enough, and that’s the point",
    "url": "https://www.tomshardware.com/pc-components/ssds/acer-ma200-1tb-ssd-review",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T15:36:58+00:00",
    "summary": "The Acer MA200 is a competent M.2 2230 NVMe SSD with reasonably good performance and power-efficiency, even if it’s not the fastest drive out there."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/seattle-to-pass-one-year-ai-data-center-moratorium-next-week-will-use-window-to-study-community-impact-of-ai-buildouts",
    "domain": "AI 算力 / 半导体",
    "title": "Seattle to pass one-year AI data center moratorium next week — will use window to study community impact of AI buildouts",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/seattle-to-pass-one-year-ai-data-center-moratorium-next-week-will-use-window-to-study-community-impact-of-ai-buildouts",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T15:29:37+00:00",
    "summary": "Two Seattle city council committees have passed a one-year moratorium and a resolution on data centers. The measures are still up for a vote in the full council, but many consider that simply as a for"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-is-reportedly-still-planning-fabled-rtx-50-super-series-for-2026-leak-claims-lineup-could-now-include-a-potential-rtx-5060-super-with-12gb-of-vram",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia is reportedly still planning fabled RTX 50 Super series for 2026, leak claims — lineup could now include a potential 'RTX 5060 Super' with 12GB of VRAM",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-is-reportedly-still-planning-fabled-rtx-50-super-series-for-2026-leak-claims-lineup-could-now-include-a-potential-rtx-5060-super-with-12gb-of-vram",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T15:17:59+00:00",
    "summary": "For almost a year, the RTX 50 Super series has been part of the rumor mill, but with the AI boom snatching production lines, causing memory prices to skyrocket, hype for the lineup had died down. Now,"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/valve-says-steam-machine-and-steam-frame-shipping-this-summer-company-confirms-release-window-as-it-expands-verified-program",
    "domain": "AI 算力 / 半导体",
    "title": "Valve says Steam Machine and Steam Frame 'shipping this summer' — company confirms release window as it expands Verified program",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/valve-says-steam-machine-and-steam-frame-shipping-this-summer-company-confirms-release-window-as-it-expands-verified-program",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T14:43:50+00:00",
    "summary": "Valve Steam Machine summer release is now set in stone — company launch window and expands Verified program"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/industry-coalition-urges-trump-administration-to-take-urgent-action-as-ai-data-centers-extreme-memory-consumption-threatens-other-industries-ai-driven-memory-chip-shortage-could-raise-prices-in-automotive-medical-telecommunications-sectors",
    "domain": "AI 算力 / 半导体",
    "title": "Industry coalition urges Trump administration to take urgent action as AI data centers' extreme memory consumption threatens other industries — AI-driven memory chip shortage could raise prices in aut",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/industry-coalition-urges-trump-administration-to-take-urgent-action-as-ai-data-centers-extreme-memory-consumption-threatens-other-industries-ai-driven-memory-chip-shortage-could-raise-prices-in-automotive-medical-telecommunications-sectors",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T12:20:01+00:00",
    "summary": "A coalition of nine U.S. trade associations has urged the Trump administration to address an AI-driven memory chip shortage, warning that soaring DRAM prices and constrained supply could raise costs f"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/elegoo-announces-bizarre-3d-printer-collab-with-emoji-brand-special-edition-centauri-carbon-2-combo-is-priced-at-usd489-usd",
    "domain": "AI 算力 / 半导体",
    "title": "Elegoo announces bizarre 3D printer collab with Emoji brand — special edition Centauri Carbon 2 Combo is priced at $489 USD",
    "url": "https://www.tomshardware.com/3d-printing/elegoo-announces-bizarre-3d-printer-collab-with-emoji-brand-special-edition-centauri-carbon-2-combo-is-priced-at-usd489-usd",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T12:00:00+00:00",
    "summary": "Elegoo announced the new machine as a fun and creative collab with the emoji® brand, a German company that has trademarked the commercial use of emojis on physical merch and media."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/vpn/save-55-percent-on-12-months-of-norton-vpn-coverage-pay-just-usd49-99-for-complete-protection-from-scams-malware-and-nefarious-ads",
    "domain": "AI 算力 / 半导体",
    "title": "Save 55% on 12 months of Norton VPN coverage — pay just $49.99 for complete protection from scams, malware, and nefarious ads",
    "url": "https://www.tomshardware.com/software/vpn/save-55-percent-on-12-months-of-norton-vpn-coverage-pay-just-usd49-99-for-complete-protection-from-scams-malware-and-nefarious-ads",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T11:39:33+00:00",
    "summary": "$4.17 per month for Norton VPN. Save 55% by picking up a 12-month subscription for just $49.99. Watch the World Cup from anywhere."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-says-claude-now-writes-more-than-80-percent-of-its-merged-code",
    "domain": "AI 算力 / 半导体",
    "title": "Anthropic warns Claude AI is building itself faster than expected, calls for option to halt frontier development —'recursive self improvement' increases risk humans lose control of AI",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-says-claude-now-writes-more-than-80-percent-of-its-merged-code",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T11:29:35+00:00",
    "summary": "Anthropic has published a report warning that the development path it’s on could eventually leave humans unable to control AI systems."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-usd550-on-this-4k-ready-gaming-pc-with-a-9800x3d-and-rx-9070-xt-now-just-usd1-749-huge-discount-makes-this-the-cheapest-pc-with-these-specs-on-sale-right-now-shipping-with-32gb-ddr5-and-a-1tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Save $550 on this 4K-ready gaming PC with a 9800X3D and RX 9070 XT, now just $1,749 — huge discount makes this the cheapest PC with these specs on sale right now, shipping with 32GB DDR5 and a 1TB SSD",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-usd550-on-this-4k-ready-gaming-pc-with-a-9800x3d-and-rx-9070-xt-now-just-usd1-749-huge-discount-makes-this-the-cheapest-pc-with-these-specs-on-sale-right-now-shipping-with-32gb-ddr5-and-a-1tb-ssd",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T11:18:11+00:00",
    "summary": "This $1,749 Skytech gaming PC is an elite-level rig for 1440p and 4K gaming, fitted with a 9800X3D, RX 9070 XT, 32GB DDR5, and a 1TB SSD."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/toms-hardware-unfiltered-computex-2026-day-4-the-b2b-shift-and-we-say-farewell-to-taipei",
    "domain": "AI 算力 / 半导体",
    "title": "Tom's Hardware Unfiltered: Computex 2026, Day 4 — the B2B shift, and we say farewell to Taipei",
    "url": "https://www.tomshardware.com/tech-industry/toms-hardware-unfiltered-computex-2026-day-4-the-b2b-shift-and-we-say-farewell-to-taipei",
    "source": "Paul Alcorn",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T11:12:41+00:00",
    "summary": "In the final entry in our series of daily Computex blogs, our team ruminates on their thoughts from the show itself."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/jensen-huang-says-every-edge-device-will-become-autonomous",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang says 'every edge device will become autonomous' — Nvidia maps one computing pattern from the cloud to robotics",
    "url": "https://www.tomshardware.com/tech-industry/jensen-huang-says-every-edge-device-will-become-autonomous",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T11:00:00+00:00",
    "summary": "\"There's a new computing pattern,\" the Nvidia CEO told reporters at a press gaggle the day after his GTC Taipei keynote."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/meta-putting-up-tents-across-the-us-to-house-ai-servers-like-a-scene-out-of-the-movie-mad-max-structures-take-three-months-to-build-and-use-jet-engines-for-power",
    "domain": "AI 算力 / 半导体",
    "title": "Meta putting up tents across the US to house AI servers, like ‘a scene out of the movie Mad Max’ — structures take three months to build and use jet engines for power",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/meta-putting-up-tents-across-the-us-to-house-ai-servers-like-a-scene-out-of-the-movie-mad-max-structures-take-three-months-to-build-and-use-jet-engines-for-power",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T10:59:42+00:00",
    "summary": "Meta is reportedly building more tents that house expensive data centers across the U.S., as it reportedly cuts construction time from two to three years to just a few months. It's also bringing its o"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/outlook-may-have-allowed-unencrypted-connections-for-decades-report-claims-fedora-and-dovecot-upgrade-reveal-protocol-downgrade-issue-present-since-at-least-2007",
    "domain": "AI 算力 / 半导体",
    "title": "Outlook may have allowed unencrypted connections for decades, report claims — Fedora and Dovecot upgrade reveal protocol downgrade issue present since at least 2007",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/outlook-may-have-allowed-unencrypted-connections-for-decades-report-claims-fedora-and-dovecot-upgrade-reveal-protocol-downgrade-issue-present-since-at-least-2007",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T10:30:00+00:00",
    "summary": "Ssh, don't tell the customer anything."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/pc-building/lightning-strike-enters-apartment-through-coaxial-internet-cable-blows-up-gamers-pc-surge-causes-extensive-damage-to-motherboard-destroys-router-and-leaves-burn-marks-on-the-wall",
    "domain": "AI 算力 / 半导体",
    "title": "Lightning strike enters apartment through coaxial internet cable, blows up gamer's PC — surge causes extensive damage to motherboard, destroys router, and leaves burn marks on the wall",
    "url": "https://www.tomshardware.com/desktops/pc-building/lightning-strike-enters-apartment-through-coaxial-internet-cable-blows-up-gamers-pc-surge-causes-extensive-damage-to-motherboard-destroys-router-and-leaves-burn-marks-on-the-wall",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T10:00:00+00:00",
    "summary": "While direct lightning strikes are difficult to defend against, proper grounding and protection for coaxial and network lines can help reduce the risk of costly hardware damage."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/indiana-mayor-secretly-recorded-saying-ai-data-center-protestors-have-sh-y-unkempt-houses-office-issues-statement-of-clarification-over-controversial-comments",
    "domain": "AI 算力 / 半导体",
    "title": "Indiana mayor secretly recorded saying AI data center protestors only live in 'sh***y' houses — office issues statement of clarification over controversial comments",
    "url": "https://www.tomshardware.com/tech-industry/indiana-mayor-secretly-recorded-saying-ai-data-center-protestors-have-sh-y-unkempt-houses-office-issues-statement-of-clarification-over-controversial-comments",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T09:00:00+00:00",
    "summary": "Shelbyville mayor Scott Ferguson (R) made these remarks likelly without knowing that he was being recorded, and it has ignited a political firestorm in the small town."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/docking-stations-hubs/take-your-openclaw-box-back-to-the-future-with-retro-mac-mini-mac-studio-docks-wokyis-tempts-nintendo-and-apple-lawyers-while-adding-a-screen-ports-and-style-to-your-modern-mini-mac",
    "domain": "AI 算力 / 半导体",
    "title": "Take your OpenClaw box back to the future with retro Mac Mini, Mac Studio docks — Wokyis tempts Nintendo and Apple lawyers, while adding a screen, ports, and style to your modern Mac",
    "url": "https://www.tomshardware.com/peripherals/docking-stations-hubs/take-your-openclaw-box-back-to-the-future-with-retro-mac-mini-mac-studio-docks-wokyis-tempts-nintendo-and-apple-lawyers-while-adding-a-screen-ports-and-style-to-your-modern-mini-mac",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T20:00:00+00:00",
    "summary": "Wokyis is already selling its M5 dock that turns your Mac Mini into a mini Macintosh. But it plans to add G7 NES-themed docks, as well, with up to 80Gbps of throughput and larger 7-inch screens."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/amds-frank-azor-pushes-back-against-claim-that-fsr-4-1-wont-be-ported-to-rdna-3-5-gpus-says-no-such-decision-has-been-made",
    "domain": "AI 算力 / 半导体",
    "title": "AMD's Frank Azor pushes back against claim that FSR 4.1 won't be ported to RDNA 3.5 GPUs — says 'no such decision' has been made",
    "url": "https://www.tomshardware.com/pc-components/gpus/amds-frank-azor-pushes-back-against-claim-that-fsr-4-1-wont-be-ported-to-rdna-3-5-gpus-says-no-such-decision-has-been-made",
    "source": "Aaron Klotz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T19:18:26+00:00",
    "summary": "AMD's Frank Azor hits back against allegations suggesting AMD will skip RDNA 3.5 integration with FSR 4.1."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/8gb-of-ram-is-back-on-laptops-companies-are-lowering-memory-offerings-to-make-affordable-notebooks-during-component-crisis",
    "domain": "AI 算力 / 半导体",
    "title": "8GB of RAM is back on laptops — companies are lowering memory offerings to make affordable notebooks during component crisis",
    "url": "https://www.tomshardware.com/laptops/8gb-of-ram-is-back-on-laptops-companies-are-lowering-memory-offerings-to-make-affordable-notebooks-during-component-crisis",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T16:34:39+00:00",
    "summary": "At Computex, Dell and Acer both introduced systems starting with 8GB of RAM to compete with the MacBook Neo, following a rush to 16GB systems in the last two years to bolster local AI."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/tsmc-ceo-c-c-wei-says-it-will-be-a-long-time-before-we-can-meet-customer-demand-tells-shareholders-that-he-will-keep-prices-stable-refrain-from-implementing-price-hikes",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC CEO C.C. Wei says, ‘It will be a long time before we can meet customer demand’ — tells shareholders that he will keep prices stable, refrain from implementing price hikes",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/tsmc-ceo-c-c-wei-says-it-will-be-a-long-time-before-we-can-meet-customer-demand-tells-shareholders-that-he-will-keep-prices-stable-refrain-from-implementing-price-hikes",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T16:18:52+00:00",
    "summary": "TSMC says it does not have enough capacity to handle all the demand from AI hyperscalers, with CEO C.C. Wei saying that it will take a long time before it can match customer demand. This is an opportu"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/qualcomm-roundtable-interview-transcript-svp-of-compute-and-gaming-talks-snapdragon-c-rtx-spark-and-the-agentic-ai-future",
    "domain": "AI 算力 / 半导体",
    "title": "Qualcomm Roundtable Interview transcript — SVP of Compute and Gaming talks Snapdragon C, RTX Spark, and the agentic AI future",
    "url": "https://www.tomshardware.com/pc-components/cpus/qualcomm-roundtable-interview-transcript-svp-of-compute-and-gaming-talks-snapdragon-c-rtx-spark-and-the-agentic-ai-future",
    "source": "Paul Alcorn",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T16:00:00+00:00",
    "summary": "Qualcomm has Snapdragon C to compete in the exciting low-cost laptop market, but it's also looking to build an entire agentic AI ecosystem on Qualcomm silicon."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/this-rtx-5070-ti-gaming-laptop-is-just-usd1-499-walmart-fights-ai-price-crisis-with-usd500-discount",
    "domain": "AI 算力 / 半导体",
    "title": "This RTX 5070 Ti gaming laptop is just $1,499 — Walmart fights AI price crisis with $500 discount",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/this-rtx-5070-ti-gaming-laptop-is-just-usd1-499-walmart-fights-ai-price-crisis-with-usd500-discount",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T15:56:13+00:00",
    "summary": "Get $500 off this MSI Vector A16 laptop."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/nintendo/nintendo-switch-2-with-user-replaceable-batteries-coming-to-the-eu-console-maker-confirms-it-will-comply-with-regulations-set-to-take-effect-from-2027",
    "domain": "AI 算力 / 半导体",
    "title": "Nintendo Switch 2 with user-replaceable batteries coming to the EU — console maker confirms it will comply with regulations set to take effect from 2027",
    "url": "https://www.tomshardware.com/video-games/nintendo/nintendo-switch-2-with-user-replaceable-batteries-coming-to-the-eu-console-maker-confirms-it-will-comply-with-regulations-set-to-take-effect-from-2027",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T15:51:23+00:00",
    "summary": "The European Union's new directives for easily user-replaceable batteries will force Nintendo to update its Switch 2 console with a revised model. The law goes into effect from February 18, 2027, whic"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/elon-musks-spacex-secures-100-percent-property-tax-exemption-for-planned-usd55-billion-terafab-semiconductor-factory-in-texas-county-approves-35-year-deal-worth-hundreds-of-millions-despite-resident-backlash",
    "domain": "AI 算力 / 半导体",
    "title": "Elon Musk's SpaceX secures 100% property tax exemption for planned $55 billion Terafab semiconductor factory in Texas — county approves 35-year deal worth hundreds of millions despite resident backlas",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/elon-musks-spacex-secures-100-percent-property-tax-exemption-for-planned-usd55-billion-terafab-semiconductor-factory-in-texas-county-approves-35-year-deal-worth-hundreds-of-millions-despite-resident-backlash",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T14:46:11+00:00",
    "summary": "SpaceX has secured a 35-year, 100% property tax abatement for its proposed $55 billion TeraFAB semiconductor facility in Texas. Elon Musk argues the exemption is essential to compete with global chipm"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/tech-sector-cut-us-jobs-by-38242-in-may",
    "domain": "AI 算力 / 半导体",
    "title": "US tech layoffs record single-highest month in two years, and more than any other sector — nearly 40,000 get the axe, AI the most cited reason for layoffs",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/tech-sector-cut-us-jobs-by-38242-in-may",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T14:28:35+00:00",
    "summary": "U.S. tech companies announced 38,242 job cuts in May, more than any other sector and the industry's heaviest month of reductions in nearly two years."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/silicon-motion-increases-sales-of-ssd-controllers-amid-nand-shortage-but-expects-nand-shortages-to-get-worse-in-2027-supply-conditions-will-become-even-worse",
    "domain": "AI 算力 / 半导体",
    "title": "Silicon Motion increases sales of SSD controllers amid NAND shortage, but expects NAND shortages to get worse in 2027 — 'supply conditions will become even worse'",
    "url": "https://www.tomshardware.com/pc-components/ssds/silicon-motion-increases-sales-of-ssd-controllers-amid-nand-shortage-but-expects-nand-shortages-to-get-worse-in-2027-supply-conditions-will-become-even-worse",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T13:08:29+00:00",
    "summary": "Sales of Silicon Motion’s SSD controllers are record high, but supply of NAND for client applications may get worse in 2027, the company tells us."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/pc-cases/hyte-shows-off-y50-chassis-aesthetic-cable-accessory-kit-new-fans-and-updates-nexus-software-sub-usd100-y50-brings-value-to-y-series-nexus-3-0-goes-web-based-now-works-on-mac-linux-windows-and-your-phone",
    "domain": "AI 算力 / 半导体",
    "title": "Hyte shows off Y50 chassis, aesthetic cable accessory kit, new fans, and updates Nexus Software — sub $100 Y50 brings value to Y-series, Nexus 3.0 goes web-based, now works on Mac, Linux, Windows, and",
    "url": "https://www.tomshardware.com/pc-components/pc-cases/hyte-shows-off-y50-chassis-aesthetic-cable-accessory-kit-new-fans-and-updates-nexus-software-sub-usd100-y50-brings-value-to-y-series-nexus-3-0-goes-web-based-now-works-on-mac-linux-windows-and-your-phone",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T12:09:54+00:00",
    "summary": "We stopped by Hyte at Computex 2026."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/best-of-computex-2026",
    "domain": "AI 算力 / 半导体",
    "title": "Best of Computex 2026: Innovating despite disruptions",
    "url": "https://www.tomshardware.com/tech-industry/best-of-computex-2026",
    "source": "The Editors of Tom&#039;s Hardware",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T12:00:00+00:00",
    "summary": "From affordable premium laptops to next-gen handhelds, and Nvidia bringing its Spark to Windows on Arm, these are the 11 best products introduced at this year’s show."
  },
  {
    "id": "hn:48354967",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia announces new AI chip for personal computers",
    "url": "https://www.bbc.com/news/articles/crmp9mppvzro",
    "source": "rishikeshs",
    "platform": "hackernews",
    "points": 46,
    "published_at": "2026-06-01T10:33:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:48220446",
    "domain": "AI 算力 / 半导体",
    "title": "IBM invented semiconductor manufacturing automation",
    "url": "https://spectrum.ieee.org/semiconductor-fabrication",
    "source": "rbanffy",
    "platform": "hackernews",
    "points": 81,
    "published_at": "2026-05-21T10:39:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:48291230",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Vera CPU Benchmarks: Olympus Cores Delivering Great Performance",
    "url": "https://www.phoronix.com/review/nvidia-vera-benchmarks",
    "source": "naves",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-05-27T08:15:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:48352693",
    "domain": "AI 算力 / 半导体",
    "title": "A powerful new chapter for Windows PCs, accelerated by Nvidia RTX Spark",
    "url": "https://blogs.windows.com/windowsexperience/2026/05/31/introducing-a-powerful-new-chapter-for-windows-pcs-accelerated-by-nvidia-rtx-spark/",
    "source": "WalterSobchak",
    "platform": "hackernews",
    "points": 34,
    "published_at": "2026-06-01T04:45:20+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/inchfab-sells-10m-mini-fabs-to-democratize-chipmaking/",
    "domain": "AI 算力 / 半导体",
    "title": "InchFab Sells $10M Mini Fabs to Democratize Chipmaking",
    "url": "https://www.eetimes.com/inchfab-sells-10m-mini-fabs-to-democratize-chipmaking/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T22:00:00+00:00",
    "summary": "InchFab's mini fabs are cost-competitive with larger 8-inch wafer fabs at the half-micron and larger nodes. The post InchFab Sells $10M Mini Fabs to Democratize Chipmaking appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/secure-your-supply-accelerate-your-designs-a-practical-guide-to-the-memory-super-cycle/",
    "domain": "AI 算力 / 半导体",
    "title": "Secure Your Supply, Accelerate Your Designs: A Practical Guide to the Memory Super Cycle",
    "url": "https://www.eetimes.com/secure-your-supply-accelerate-your-designs-a-practical-guide-to-the-memory-super-cycle/",
    "source": "Infineon Technologies and Arrow Electronics",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T18:16:56+00:00",
    "summary": "Date: Thursday, July 9, 2026 Time 15:00 CEST The AI revolution is reshaping the memory industry, presenting unique supply challenges—such as longer lead times and allocation-based supply—and new oppor"
  },
  {
    "id": "rss:https://www.eetimes.com/lpddr6-roadmap-leads-to-the-data-center/",
    "domain": "AI 算力 / 半导体",
    "title": "LPDDR6 Roadmap Leads to the Data Center",
    "url": "https://www.eetimes.com/lpddr6-roadmap-leads-to-the-data-center/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T14:30:00+00:00",
    "summary": "Low-power memory has evolved from its mobile device roots to meet the demands of AI data centers. The post LPDDR6 Roadmap Leads to the Data Center appeared first on EE Times."
  },
  {
    "id": "hn:48196570",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.5 Flash",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/",
    "source": "spectraldrift",
    "platform": "hackernews",
    "points": 962,
    "published_at": "2026-05-19T17:43:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:48111896",
    "domain": "大厂 AI 动态",
    "title": "Show HN: Needle: We Distilled Gemini Tool Calling into a 26M Model",
    "url": "https://github.com/cactus-compute/needle",
    "source": "HenryNdubuaku",
    "platform": "hackernews",
    "points": 776,
    "published_at": "2026-05-12T18:03:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:48192224",
    "domain": "大厂 AI 动态",
    "title": "Apple unveils new accessibility features",
    "url": "https://www.apple.com/newsroom/2026/05/apple-unveils-new-accessibility-features-and-updates-with-apple-intelligence/",
    "source": "interpol_p",
    "platform": "hackernews",
    "points": 726,
    "published_at": "2026-05-19T12:04:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:48233563",
    "domain": "大厂 AI 动态",
    "title": "Steve Wozniak cheered after telling students they have AI – actual intelligence",
    "url": "https://www.businessinsider.com/steve-wozniak-apple-ai-graduation-speech-2026-5",
    "source": "signa11",
    "platform": "hackernews",
    "points": 650,
    "published_at": "2026-05-22T09:04:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:48196867",
    "domain": "大厂 AI 动态",
    "title": "Gemini CLI will stop working from June 18, 2026",
    "url": "https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/",
    "source": "primaprashant",
    "platform": "hackernews",
    "points": 406,
    "published_at": "2026-05-19T18:03:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:48050278",
    "domain": "大厂 AI 动态",
    "title": "AlphaEvolve: Gemini-powered coding agent scaling impact across fields",
    "url": "https://deepmind.google/blog/alphaevolve-impact/",
    "source": "berlianta",
    "platform": "hackernews",
    "points": 327,
    "published_at": "2026-05-07T15:02:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:48196609",
    "domain": "大厂 AI 动态",
    "title": "Gemini Omni",
    "url": "https://deepmind.google/models/gemini-omni/",
    "source": "meetpateltech",
    "platform": "hackernews",
    "points": 323,
    "published_at": "2026-05-19T17:46:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:48272354",
    "domain": "大厂 AI 动态",
    "title": "Microsoft Copilot Cowork Exfiltrates Files",
    "url": "https://www.promptarmor.com/resources/microsoft-copilot-cowork-exfiltrates-files",
    "source": "Kneenex",
    "platform": "hackernews",
    "points": 264,
    "published_at": "2026-05-25T21:45:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:48111581",
    "domain": "大厂 AI 动态",
    "title": "Reimagining the mouse pointer for the AI era",
    "url": "https://deepmind.google/blog/ai-pointer/",
    "source": "devhouse",
    "platform": "hackernews",
    "points": 252,
    "published_at": "2026-05-12T17:40:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:48373764",
    "domain": "大厂 AI 动态",
    "title": "GitHub Copilot App",
    "url": "https://github.com/features/preview/github-app",
    "source": "theanonymousone",
    "platform": "hackernews",
    "points": 124,
    "published_at": "2026-06-02T17:58:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:48297467",
    "domain": "大厂 AI 动态",
    "title": "Gemini, Gophers, and Fingers. Oh My Alternative Internets Beyond HTTPS",
    "url": "https://brennan.day/gemini-gophers-and-fingers-oh-my-alternative-internets-beyond-https/",
    "source": "ChrisArchitect",
    "platform": "hackernews",
    "points": 147,
    "published_at": "2026-05-27T17:24:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:48413924",
    "domain": "大厂 AI 动态",
    "title": "Leak Reveals Microsoft Wants Its AI to Be 'Addictive'",
    "url": "https://kotaku.com/microsoft-ai-scout-addictive-satya-nadella-404-media-copilot-2000702924",
    "source": "thm",
    "platform": "hackernews",
    "points": 66,
    "published_at": "2026-06-05T15:32:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:48080702",
    "domain": "大厂 AI 动态",
    "title": "Gemini API File Search is now multimodal",
    "url": "https://blog.google/innovation-and-ai/technology/developers-tools/expanded-gemini-api-file-search-multimodal-rag/",
    "source": "gmays",
    "platform": "hackernews",
    "points": 156,
    "published_at": "2026-05-10T03:22:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:48084710",
    "domain": "大厂 AI 动态",
    "title": "Chrome's AI features may be hogging 4GB of your computer storage",
    "url": "https://www.theverge.com/tech/924933/google-chrome-4gb-gemini-nano-ai-features",
    "source": "birdculture",
    "platform": "hackernews",
    "points": 117,
    "published_at": "2026-05-10T15:22:46+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/943194/metanet-n-plus-plus-multiplayer-sequel",
    "domain": "大厂 AI 动态",
    "title": "More than a decade later, the team behind N++ is back with a multiplayer sequel",
    "url": "https://www.theverge.com/entertainment/943194/metanet-n-plus-plus-multiplayer-sequel",
    "source": "Andrew Webster",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T23:25:34+00:00",
    "summary": "Back in 2015, the two-person studio Metanet released N++, a brutally hard 2D platformer that was a decade in the making, building off of previous releases dating back to the freeware Flash title N. At"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/944229/grand-theft-auto-6-release-calendar-summer-game-fest",
    "domain": "大厂 AI 动态",
    "title": "Grand Theft Auto VI is warping the video game release calendar",
    "url": "https://www.theverge.com/entertainment/944229/grand-theft-auto-6-release-calendar-summer-game-fest",
    "source": "Andrew Webster",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T23:05:27+00:00",
    "summary": "Who's afraid of the next GTA? Based on the last few days of Summer Game Fest, just about everyone. Grand Theft Auto VI hasn't been present at any of the keynote events, but its presence was felt every"
  },
  {
    "id": "rss:https://www.theverge.com/games/939396/final-fantasy-vii-revelation-remake-trilogy-third-game-announcement",
    "domain": "大厂 AI 动态",
    "title": "Final Fantasy VII&#8217;s remake trilogy will conclude with Revelation",
    "url": "https://www.theverge.com/games/939396/final-fantasy-vii-revelation-remake-trilogy-third-game-announcement",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T22:52:06+00:00",
    "summary": "Square Enix has officially announced the third and final game in its Final Fantasy VII remake trilogy: Final Fantasy VII Revelation. It will release on multiple platforms simultaneously - PC, PS5, Xbo"
  },
  {
    "id": "rss:https://www.theverge.com/games/944151/control-resonant-hands-on",
    "domain": "大厂 AI 动态",
    "title": "Control Resonant is a sequel — and also a starting point",
    "url": "https://www.theverge.com/games/944151/control-resonant-hands-on",
    "source": "Kallie Plagge",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T21:45:44+00:00",
    "summary": "Chronologically, Control Resonant is a sequel to 2019's Control. But in most other ways, the games aren't directly connected. To developer Remedy, they're more like two sides of the same coin. When Re"
  },
  {
    "id": "rss:https://www.theverge.com/policy/944615/section-702-senate-vote-fails-pulte",
    "domain": "大厂 AI 动态",
    "title": "Congress still can’t decide what to do about warrantless surveillance",
    "url": "https://www.theverge.com/policy/944615/section-702-senate-vote-fails-pulte",
    "source": "Gaby Del Valle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T21:15:48+00:00",
    "summary": "The deadline to reauthorize Section 702 of the Foreign Intelligence Surveillance Act is coming up a week from now on June 12th, and legislators seem no closer to reaching a deal. If this sounds like d"
  },
  {
    "id": "rss:https://www.theverge.com/games/939484/summer-game-fest-live-2026-biggest-news-trailers-announcements",
    "domain": "大厂 AI 动态",
    "title": "Summer Game Fest Live 2026: The biggest news, trailers, and announcements",
    "url": "https://www.theverge.com/games/939484/summer-game-fest-live-2026-biggest-news-trailers-announcements",
    "source": "The Verge",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T20:40:00+00:00",
    "summary": "Geoff Keighley&#8217;s annual June showcase for videos games has officially happened, and it was a big one. Across a two hour event — and another hour for Day of the Devs — we got news about the third"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/944337/gone-in-60-minutes",
    "domain": "大厂 AI 动态",
    "title": "Gone in 60 minutes",
    "url": "https://www.theverge.com/entertainment/944337/gone-in-60-minutes",
    "source": "TC. Sottek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T18:44:20+00:00",
    "summary": "It should have been the final straw. The new power couple of editorial failure - Bari Weiss and Nick Bilton - had fired legendary 60 Minutes journalist Scott Pelley. Why? Because he dared to question "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/944095/sonos-era-100-google-nest-doorbell-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "The Sonos Era 100 speaker is down to its lowest price in months",
    "url": "https://www.theverge.com/gadgets/944095/sonos-era-100-google-nest-doorbell-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T17:00:47+00:00",
    "summary": "Whether you’re considering starting a Sonos speaker setup, or adding to an existing group, the Sonos Era 100 is worth picking up. The compact, capable smart speaker is currently marked down to $189 ($"
  },
  {
    "id": "rss:https://www.theverge.com/podcast/944058/ai-laptop-nvidia-build-gemini-spark-vergecast",
    "domain": "大厂 AI 动态",
    "title": "This is your laptop… on AI",
    "url": "https://www.theverge.com/podcast/944058/ai-laptop-nvidia-build-gemini-spark-vergecast",
    "source": "David Pierce",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T16:39:07+00:00",
    "summary": "We're now deep into developer conference season, and one of the themes so far is the relentless conviction from Big Tech companies that AI is going to change everything about how we do everything. Nvi"
  },
  {
    "id": "rss:https://www.theverge.com/report/944076/cbp-airport-phone-searches-seizure-minneapolis-activists",
    "domain": "大厂 AI 动态",
    "title": "What happens when your phone is confiscated at the airport",
    "url": "https://www.theverge.com/report/944076/cbp-airport-phone-searches-seizure-minneapolis-activists",
    "source": "Gaby Del Valle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T16:15:00+00:00",
    "summary": "Even if you've done nothing wrong, it's never a good idea to hand your phone to the cops. But international travelers at American airports often have no choice - even if they're US citizens. When Minn"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/05/reid-hoffman-is-leaving-microsofts-board-to-go-founder-mode-with-startup-manus/",
    "domain": "大厂 AI 动态",
    "title": "Reid Hoffman is leaving Microsoft’s board to go ‘founder mode’ with startup Manus",
    "url": "https://techcrunch.com/2026/06/05/reid-hoffman-is-leaving-microsofts-board-to-go-founder-mode-with-startup-manus/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T22:35:01+00:00",
    "summary": "After a very profitable decade on Microsoft's board, Reid Hoffman is stepping down to focus on his AI drug discovery startup Manus."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/05/founders-share-vc-horror-stories-and-some-are-naming-names/",
    "domain": "大厂 AI 动态",
    "title": "Founders share VC horror stories, and some are naming names",
    "url": "https://techcrunch.com/2026/06/05/founders-share-vc-horror-stories-and-some-are-naming-names/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T21:47:56+00:00",
    "summary": "A massive viral conversation sharing VC horror stories has taken place this week on X. Some are weird. Some are infuriating."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/05/former-cyber-executive-turned-whistleblower-accuses-ibm-of-covering-up-several-data-breaches/",
    "domain": "大厂 AI 动态",
    "title": "Former cyber executive turned whistleblower accuses IBM of covering up several data breaches",
    "url": "https://techcrunch.com/2026/06/05/former-cyber-executive-turned-whistleblower-accuses-ibm-of-covering-up-several-data-breaches/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T20:31:04+00:00",
    "summary": "IBM and two of its subsidiary companies were allegedly breached during the mid-2010s — a lawsuit filed by a former cybersecurity executive accuses IBM of not disclosing and actively covering it up."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/05/startup-battlefield-200-applications-officially-close-in-3-days/",
    "domain": "大厂 AI 动态",
    "title": "Startup Battlefield 200 applications officially close in 3 days",
    "url": "https://techcrunch.com/2026/06/05/startup-battlefield-200-applications-officially-close-in-3-days/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T20:00:00+00:00",
    "summary": "Applications for Startup Battlefield 200 officially close on June 8, 11:59 p.m. PT. Don't wait any longer. Secure your shot at competing on the Disrupt Stage at TechCrunch Disrupt 2026 this October at"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/05/google-will-pay-spacex-920m-per-month-for-compute/",
    "domain": "大厂 AI 动态",
    "title": "Google will pay SpaceX $920M per month for compute",
    "url": "https://techcrunch.com/2026/06/05/google-will-pay-spacex-920m-per-month-for-compute/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T18:57:20+00:00",
    "summary": "In a statement, a Google representative described the deal as a result of unexpected demand for its recently launched AI products."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/05/gms-electric-future-depends-on-a-new-battery-and-this-building/",
    "domain": "大厂 AI 动态",
    "title": "GM’s electric future depends on a new battery — and this facility",
    "url": "https://techcrunch.com/2026/06/05/gms-electric-future-depends-on-a-new-battery-and-this-building/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T17:44:18+00:00",
    "summary": "GM wants to slash EV prices by deploying new battery tech up to a year earlier than planned. This building is key to making that happen."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/05/as-vc-backed-e-bike-startups-went-bankrupt-bootstrapped-lectric-grew/",
    "domain": "大厂 AI 动态",
    "title": "As VC-backed e-bike startups went bankrupt, bootstrapped Lectric grew",
    "url": "https://techcrunch.com/2026/06/05/as-vc-backed-e-bike-startups-went-bankrupt-bootstrapped-lectric-grew/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T17:38:06+00:00",
    "summary": "Lectric, which says the U.S. market is ripe for competition and choice, has launched three new brands in the past six months."
  },
  {
    "id": "rss:https://techcrunch.com/video/the-most-interesting-startups-right-now-want-to-get-you-off-your-phone/",
    "domain": "大厂 AI 动态",
    "title": "The most interesting startups right now want to get you off your phone",
    "url": "https://techcrunch.com/video/the-most-interesting-startups-right-now-want-to-get-you-off-your-phone/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T17:17:06+00:00",
    "summary": "While the AI fundraising machine&#160;keeps breaking its own records, some founders are building in the other direction.&#160; Mirror founder Brynn Putnam just raised money for&#160;Board, a startup f"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/05/supabase-doubles-valuation-to-10b-in-8-months/",
    "domain": "大厂 AI 动态",
    "title": "Supabase doubles valuation to $10B in 8 months",
    "url": "https://techcrunch.com/2026/06/05/supabase-doubles-valuation-to-10b-in-8-months/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T16:32:27+00:00",
    "summary": "Supabase, an example of an open source project becoming a fast-growing company, has greatly benefited from AI tools like Claude, Codex, and other vibe-coding platforms."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/05/google-and-fbi-warn-of-ransomware-group-that-sends-fake-it-workers-to-hack-victims-in-person/",
    "domain": "大厂 AI 动态",
    "title": "Google and FBI warn of ransomware group that sends fake IT workers to hack victims in person",
    "url": "https://techcrunch.com/2026/06/05/google-and-fbi-warn-of-ransomware-group-that-sends-fake-it-workers-to-hack-victims-in-person/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T16:07:46+00:00",
    "summary": "Cybercriminals, part of a gang known as Silent Ransom Group, have sent people pretending to be IT support employees to law firms' offices, where the criminals have stolen data using USB drives or remo"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/05/the-token-bill-comes-due-inside-the-industry-scramble-to-manage-ais-runaway-costs/",
    "domain": "大厂 AI 动态",
    "title": "The token bill comes due: Inside the industry scramble to manage AI’s runaway costs",
    "url": "https://techcrunch.com/2026/06/05/the-token-bill-comes-due-inside-the-industry-scramble-to-manage-ais-runaway-costs/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T14:49:12+00:00",
    "summary": "\"The whole conversation shifted from tokenmaxxing and 'go fast' to 'we need guardrails, how do we control this?'\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/05/nasa-briefly-sheltered-space-station-astronauts-in-spacexs-dragon-due-to-leaks/",
    "domain": "大厂 AI 动态",
    "title": "NASA briefly sheltered space station astronauts in SpaceX’s Dragon due to leaks",
    "url": "https://techcrunch.com/2026/06/05/nasa-briefly-sheltered-space-station-astronauts-in-spacexs-dragon-due-to-leaks/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T14:42:52+00:00",
    "summary": "The space agency said Roscosmos discovered new leaks in the Russian service module."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/05/nsa-said-to-be-readying-anthropics-mythos-for-use-in-cyber-operations/",
    "domain": "大厂 AI 动态",
    "title": "NSA said to be readying Anthropic’s Mythos for use in cyber operations",
    "url": "https://techcrunch.com/2026/06/05/nsa-said-to-be-readying-anthropics-mythos-for-use-in-cyber-operations/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T14:32:57+00:00",
    "summary": "The U.S. eavesdropping agency is reportedly preparing Anthropic's Mythos for use in cyberattacks, despite a federal ban on using the AI model maker."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/05/airtrunk-commits-30b-to-build-5gw-of-ai-data-centers-in-india/",
    "domain": "大厂 AI 动态",
    "title": "AirTrunk commits $30B to build 5GW of AI data centers in India",
    "url": "https://techcrunch.com/2026/06/05/airtrunk-commits-30b-to-build-5gw-of-ai-data-centers-in-india/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T13:03:10+00:00",
    "summary": "The Australian data center operator plans to set up 5GW of capacity in India."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/04/mira-murati-steps-back-into-the-spotlight-carefully/",
    "domain": "大厂 AI 动态",
    "title": "Mira Murati steps back into the spotlight, carefully",
    "url": "https://techcrunch.com/2026/06/04/mira-murati-steps-back-into-the-spotlight-carefully/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T05:06:37+00:00",
    "summary": "In the current environment, remaining heads down has diminishing returns; at some point, you have to make some noise just to remind the market you exist."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/04/founders-fund-launches-game-show-starring-sam-altman-palmer-luckey-and-other-tech-elites/",
    "domain": "大厂 AI 动态",
    "title": "Founders Fund launches game show starring Sam Altman, Palmer Luckey, and other tech elites",
    "url": "https://techcrunch.com/2026/06/04/founders-fund-launches-game-show-starring-sam-altman-palmer-luckey-and-other-tech-elites/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T00:06:47+00:00",
    "summary": "The debut episode, moderated by Founders Fund chief marketing officer Mike Solana, included a star-studded cast of current tech luminaries."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/04/ahead-of-its-ipo-anthropics-daniela-amodei-shrugs-off-doubts-about-ais-returns/",
    "domain": "大厂 AI 动态",
    "title": "Ahead of its IPO, Anthropic’s Daniela Amodei shrugs off doubts about AI’s returns",
    "url": "https://techcrunch.com/2026/06/04/ahead-of-its-ipo-anthropics-daniela-amodei-shrugs-off-doubts-about-ais-returns/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T22:43:26+00:00",
    "summary": "Anthropic has been growing at a breakneck pace. The company announced that annualized revenue crossed $47 billion in May, up dramatically from roughly $9 billion at the end of 2025. That trajectory fa"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/04/airbnbs-brian-chesky-plans-to-launch-a-new-ai-lab/",
    "domain": "大厂 AI 动态",
    "title": "Airbnb’s Brian Chesky plans to launch a new AI lab",
    "url": "https://techcrunch.com/2026/06/04/airbnbs-brian-chesky-plans-to-launch-a-new-ai-lab/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T22:29:50+00:00",
    "summary": "The Airbnb CEO said last year it hasn't struck an LLM partnership because existing products weren't quite ready."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/04/filtr-is-a-new-privacy-tool-that-blocks-ads-in-almost-every-iphone-and-mac-app/",
    "domain": "大厂 AI 动态",
    "title": "Filtr is a new privacy tool that blocks ads in almost every iPhone and Mac app",
    "url": "https://techcrunch.com/2026/06/04/filtr-is-a-new-privacy-tool-that-blocks-ads-in-almost-every-iphone-and-mac-app/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T21:44:09+00:00",
    "summary": "This popular ad blocker app for iPhones, iPads, and Macs can now block ads from loading inside apps, including web browsers, thanks to a new feature in the latest Apple software."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/04/defense-tech-ai-and-fundraising-take-center-stage-at-strictlyvc-los-angeles-on-june-18/",
    "domain": "大厂 AI 动态",
    "title": "Defense tech, AI, and fundraising take center stage at StrictlyVC Los Angeles on June 18",
    "url": "https://techcrunch.com/2026/06/04/defense-tech-ai-and-fundraising-take-center-stage-at-strictlyvc-los-angeles-on-june-18/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T21:30:00+00:00",
    "summary": "On Thursday, June 18, at The Aerospace Corporation Campus, investors, founders, and tech leaders will gather for an evening of conversation exploring some of the most consequential shifts taking place"
  },
  {
    "id": "rss:https://stratechery.com/2026/power-shifts/",
    "domain": "大厂 AI 动态",
    "title": "2026.23: Power Shifts",
    "url": "https://stratechery.com/2026/power-shifts/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T17:00:00+00:00",
    "summary": "The best Stratechery content from the week of June 1, 2026, including Google and Microsoft, YouTubers taking over Hollywood, and a guide to the NBA Finals."
  },
  {
    "id": "rss:https://stratechery.com/2026/an-interview-with-microsoft-ceo-satya-nadella-about-finding-core-competencies/",
    "domain": "大厂 AI 动态",
    "title": "An Interview with Microsoft CEO Satya Nadella About Finding Core Competencies",
    "url": "https://stratechery.com/2026/an-interview-with-microsoft-ceo-satya-nadella-about-finding-core-competencies/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T10:00:00+00:00",
    "summary": "An interview with Microsoft CEO Satya Nadella about figuring out Microsoft's role in AI, the relationship with OpenAI, Capex, Software, and a potential new agentic platform."
  },
  {
    "id": "rss:https://www.producthunt.com/products/shram",
    "domain": "大厂 AI 动态",
    "title": "Minimi",
    "url": "https://www.producthunt.com/products/shram",
    "source": "Rohan Chaubey",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T08:29:10+00:00",
    "summary": "Your ambient memory for Claude Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/mai-image-2-3",
    "domain": "大厂 AI 动态",
    "title": "Microsoft MAI-Voice-2",
    "url": "https://www.producthunt.com/products/mai-image-2-3",
    "source": "Habib Ferdous",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T21:38:54+00:00",
    "summary": "Expressive TTS with voice cloning in 15 languages Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/clarafy",
    "domain": "大厂 AI 动态",
    "title": "Clarafy",
    "url": "https://www.producthunt.com/products/clarafy",
    "source": "Liam Tidholm",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T17:33:12+00:00",
    "summary": "Type messy and have it instantly polished Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/leni",
    "domain": "大厂 AI 动态",
    "title": "Leni",
    "url": "https://www.producthunt.com/products/leni",
    "source": "KP",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T11:54:13+00:00",
    "summary": "The world’s most accurate AI for investors Discussion | Link"
  },
  {
    "id": "hn:48405718",
    "domain": "股票",
    "title": "SpaceX, Other Mega IPOs Denied Fast Index Entry by S&P",
    "url": "https://www.bloomberg.com/news/articles/2026-06-04/s-p-dow-jones-keeps-megacap-ipo-rules-as-is-after-consultation",
    "source": "tristanj",
    "platform": "hackernews",
    "points": 976,
    "published_at": "2026-06-04T22:48:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:48373909",
    "domain": "股票",
    "title": "Morningstar values SpaceX at $780B, half its IPO target",
    "url": "https://www.reuters.com/business/media-telecom/morningstar-values-spacex-780-billion-half-its-ipo-target-2026-06-02/",
    "source": "berkeleyjunk",
    "platform": "hackernews",
    "points": 211,
    "published_at": "2026-06-02T18:09:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:48314363",
    "domain": "股票",
    "title": "Sam Altman and Dario Amodei are both walking back AI jobs apocalypse predictions",
    "url": "https://fortune.com/2026/05/26/sam-altman-dario-amodei-walking-back-ai-jobs-apocalypse-prophecies-ipo/",
    "source": "ianrahman",
    "platform": "hackernews",
    "points": 236,
    "published_at": "2026-05-28T19:43:14+00:00",
    "summary": ""
  },
  {
    "id": "hn:48394034",
    "domain": "股票",
    "title": "The SpaceX IPO will be the theft of the century",
    "url": "https://montanaskeptic.substack.com/p/the-spacex-ipo-will-be-the-theft",
    "source": "400thecat",
    "platform": "hackernews",
    "points": 141,
    "published_at": "2026-06-04T04:52:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:48210226",
    "domain": "股票",
    "title": "OpenAI Is Preparing to File for an IPO Soon",
    "url": "https://www.wsj.com/tech/ai/openai-is-preparing-to-file-for-an-ipo-very-soon-0ec95af5",
    "source": "louiereederson",
    "platform": "hackernews",
    "points": 206,
    "published_at": "2026-05-20T16:24:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:48134429",
    "domain": "股票",
    "title": "Sam Altman's Business Dealings Under GOP Scrutiny Ahead of OpenAI's IPO",
    "url": "https://www.wsj.com/tech/ai/sam-altmans-business-dealings-under-gop-scrutiny-ahead-of-openais-ipo-52c1cc4d",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 199,
    "published_at": "2026-05-14T12:27:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:48385866",
    "domain": "股票",
    "title": "SpaceX's IPO is a disaster waiting to happen for your pension fund",
    "url": "https://www.irishtimes.com/business/2026/06/03/heavily-in-debt-loss-making-with-eyes-on-sending-people-to-mars-why-would-anyone-invest-in-spacex/",
    "source": "anonymousDan",
    "platform": "hackernews",
    "points": 91,
    "published_at": "2026-06-03T16:02:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:48217052",
    "domain": "股票",
    "title": "OpenAI to confidentially file for IPO as soon as Friday",
    "url": "https://www.cnbc.com/2026/05/20/openai-ipo-filing.html",
    "source": "doppp",
    "platform": "hackernews",
    "points": 137,
    "published_at": "2026-05-21T02:24:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:48390053",
    "domain": "股票",
    "title": "Iran war drains US oil stocks to lowest level since 2004",
    "url": "https://www.ft.com/content/d0be73c8-b8d8-4ffd-874e-e97a6ecffef7",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 61,
    "published_at": "2026-06-03T21:06:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:48404734",
    "domain": "股票",
    "title": "Fidelity lowers SpaceX IPO entry requirement from $500,000 to just $2,000",
    "url": "https://finance.yahoo.com/markets/stocks/articles/fidelity-cuts-spacex-ipo-eligibility-183319186.html",
    "source": "tcp_handshaker",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-06-04T21:15:18+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3774019",
    "domain": "股票",
    "title": "普京：泽连斯基“粗鲁无礼”，会面“没有任何意义”",
    "url": "https://wallstreetcn.com/articles/3774019",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-06T05:44:15+00:00",
    "summary": "普京称泽连斯基公开信\"粗鲁无礼\"，并称与其会面\"毫无意义\"。普京还表示，既然乌克兰方面将双方的问题公开化，那么俄方也要透露一些此前不公开的内容：就在乌方商人转达泽连斯基\"希望会谈\"愿望的次日凌晨，乌军无人机即袭击了卢甘斯克宿舍楼。"
  },
  {
    "id": "wscn:3774017",
    "domain": "股票",
    "title": "“黑色星期五”的导火索？Semianalysis报告“重创”美光",
    "url": "https://wallstreetcn.com/articles/3774017",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-06T03:59:20+00:00",
    "summary": "SemiAnalysis发布关于英伟达削减内存容量的报告，被市场解读为AI需求降温，导致美光在获英伟达HBM4认证的同日股价重挫13%，创2025年4月以来最大单日跌幅。该机构虽否认看空，但因其屡次发布看空美光的误导性叙事且频遭基本面“打脸”，正引发市场对其研究质量的强烈质疑。"
  },
  {
    "id": "wscn:3774016",
    "domain": "股票",
    "title": "合计700亿美元！SpaceX先后与Anthropic和谷歌签下大单，“算力租赁”ARR高达260亿美元",
    "url": "https://wallstreetcn.com/articles/3774016",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-06T03:05:37+00:00",
    "summary": "SpaceX相继与Anthropic（每月12.5亿美元）和谷歌（每月9.2亿美元）签署算力租赁协议。此举为其计划融资750亿美元的IPO提供强劲支撑。但同时，旗下xAI实验室正面临核心人才流失与研发受挫等挑战，引发外界对其自主AI研发能力的质疑。"
  },
  {
    "id": "wscn:3774013",
    "domain": "股票",
    "title": "标杆“芯片融资”交易：阿波罗、黑石和博通联手“募资”350亿美元，用于Anthropic向谷歌租赁TPU",
    "url": "https://wallstreetcn.com/articles/3774013",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-06T02:25:48+00:00",
    "summary": "本次融资采用特殊目的载体（SPV）架构。SPV通过债务与股权的混合方式募集资金，350亿美元债务分三档发行，博通为A1（60亿）、A2（240亿）两档提供信用背书及残值兜底，B级票据45亿美元利率8.5%。此交易是迄今最大规模芯片融资。"
  },
  {
    "id": "wscn:3774015",
    "domain": "股票",
    "title": "美军打击伊朗目标，巴林、科威特拉响防空警报，特朗普坚称将很快从伊朗战事中“脱身”",
    "url": "https://wallstreetcn.com/articles/3774015",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-06T02:12:18+00:00",
    "summary": "美伊冲突持续升温，巴林、科威特相继拉响全国防空警报，美军击落4架伊朗无人机并空袭其沿海雷达站，伊朗导弹反击科威特、巴林美军基地。然而，特朗普声称将\"很快脱身\"，称伊朗军事力量已被\"彻底摧毁\"，但停火协议仍悬而未决。"
  },
  {
    "id": "wscn:3774007",
    "domain": "股票",
    "title": "黑色星期五！“人人赚钱”的全球AI大牛市遭遇“当头棒喝”",
    "url": "https://wallstreetcn.com/articles/3774007",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-06T01:44:38+00:00",
    "summary": "周五强劲非农数据引爆加息忧虑，而本周博通财报指引失望，已经刺破\"AI受益股坚不可摧\"神话，此外谷歌增发、Meta跟进融资传闻及SpaceX IPO预期叠加，引发资金虹吸效应。持续两个月的全球AI大牛市遭遇当头棒喝，周五费城半导体指数暴跌逾10%，单日市值蒸发逾1万亿美元。"
  },
  {
    "id": "wscn:3774010",
    "domain": "股票",
    "title": "美联储今年还会降息吗？整个华尔街只有1家投行还“坚持”：花旗",
    "url": "https://wallstreetcn.com/articles/3774010",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-06T01:35:27+00:00",
    "summary": "花旗仍预测年内将降息三次，认为当前就业强势难以持续，未来三个月劳动力市场将趋于疲软，届时将\"重新定价降息可能性，而非加息概率\"。强劲非农数据之后，目前利率互换市场已完全定价年内加息。华尔街主要投行纷纷放弃降息预测，部分转而预测加息。"
  },
  {
    "id": "wscn:3774011",
    "domain": "股票",
    "title": "90亿元“弹药”加码国际业务，国泰海通的下一个大动作",
    "url": "https://wallstreetcn.com/articles/3774011",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-06T01:33:35+00:00",
    "summary": "增资国泰海通金融控股"
  },
  {
    "id": "wscn:3773992",
    "domain": "股票",
    "title": "勿用长期慢变量论证短期经济现象 | 余永定解读见证失衡1",
    "url": "https://wallstreetcn.com/premium/articles/3773992?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-06T01:17:13+00:00",
    "summary": "经济现象必须按领域、时间维度和性质进行严格归类，不同问题应运用不同政策工具，不能混为一谈"
  },
  {
    "id": "wscn:3774009",
    "domain": "股票",
    "title": "美国就业：碳基和硅基的两重天",
    "url": "https://wallstreetcn.com/articles/3774009",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-06T01:12:14+00:00",
    "summary": "据国联民生，美国就业数据表面企稳，内里暗流涌动。信息业岗位自2022年峰值已净流失逾30万个，AI替代裁员占比突破20%，高学历青年就业规模骤降16%。但当前冲击仍以\"压制新增招聘\"为主，结构性重于总量性。长线预警更甚：智能体AI的落地将使影响从单纯“替代任务”跃升至端到端“替代岗位”，一场渐进的劳动力重构与“无就业繁荣”已然逼近。"
  },
  {
    "id": "wscn:3774008",
    "domain": "股票",
    "title": "强劲非农后，高盛“投降”：不再预计美联储今年降息",
    "url": "https://wallstreetcn.com/articles/3774008",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-06T00:57:54+00:00",
    "summary": "高盛认为，关税、高油价及AI需求三重推力将使2026年核心PCE通胀维持在3%以上，美联储缺乏降息紧迫感，因此放弃今年降息预期，将最后两次降息时间推迟至2027年6月和12月，同时将加息概率从10%上调至20%，并认为\"维持利率不变\"是合理替代方案。"
  },
  {
    "id": "wscn:3774006",
    "domain": "股票",
    "title": "大跌之夜，高盛合伙人喊“抄底”：今年这种买入的机会并不多",
    "url": "https://wallstreetcn.com/articles/3774006",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-06T00:41:28+00:00",
    "summary": "美股周五标普大跌2.6%，费城半导体指数暴跌逾10%，单日蒸发逾万亿美元。高盛美洲股票执行服务主管John Flood认为，认为此次回调本质是获利了结，属于历史上通常能回报买家的健康调整。他强调，标普500回调2%时买入往往有回报，这类机会全年难得。"
  },
  {
    "id": "wscn:3774003",
    "domain": "股票",
    "title": "币圈惨烈！比特币破6万美元，以太坊暴跌超10%，Strategy遭空头围猎",
    "url": "https://wallstreetcn.com/articles/3774003",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T23:54:08+00:00",
    "summary": "比特币本周暴跌16%，最低触及59,099美元，为2024年10月以来最低水平。核心原因是Strategy抛售与强劲非农数据推高美债收益率。比特币\"数字黄金\"与\"科技贝塔\"双重叙事同步瓦解，近期与美股新高走势严重背离。期权市场上针对Strategy的空头交易急剧升温，做空ETF近期上涨30%。"
  },
  {
    "id": "wscn:3774004",
    "domain": "股票",
    "title": "美国版“AI全民红利”？特朗普表态支持美国政府持有顶级AI公司股权",
    "url": "https://wallstreetcn.com/articles/3774004",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T23:46:56+00:00",
    "summary": "特朗普表示有意让美国政府持有顶级AI公司股权，并考虑向公众再分配收益。美国参议员Sanders也提出立法要求AI公司移交50%股权设立主权财富基金，但前白宫AI主管Sacks警告政府介入将引发\"国家化\"风险。此前韩国官员提议设立\"公民红利\"分享AI超额利润。AI扩张带来的电价上涨与就业压力，正将民众焦虑转化为政治诉求。"
  },
  {
    "id": "wscn:3774005",
    "domain": "股票",
    "title": "华尔街见闻早餐FM-Radio | 2026年6月6日",
    "url": "https://wallstreetcn.com/articles/3774005",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T23:42:55+00:00",
    "summary": "五分钟看懂全球市场，尽在财经早餐。"
  },
  {
    "id": "wscn:3774002",
    "domain": "股票",
    "title": "科技股暴跌与比特币重挫，SpaceX上市前夕散户资金面临终极考验",
    "url": "https://wallstreetcn.com/articles/3774002",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T23:33:56+00:00",
    "summary": "强劲非农数据打消降息预期，高估值资产全线承压。SpaceX史上最大IPO计划恰逢此时，前景添变数。数据显示散户现金储备已降至历史低位，且需与加密货币、AI概念股等众多投机标的争夺同一资金池。"
  },
  {
    "id": "wscn:3774000",
    "domain": "股票",
    "title": "“区区”17万的非农 凭什么让美股蒸发万亿！？",
    "url": "https://wallstreetcn.com/premium/articles/3774000?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T23:33:43+00:00",
    "summary": "就业数字暂时还撑着，但它是滞后指标——等它真正倒下的时候，衰退通常已经发生了。"
  },
  {
    "id": "wscn:3774001",
    "domain": "股票",
    "title": "报道：SpaceX IPO获超额认购，预计6月12日开盘交易",
    "url": "https://wallstreetcn.com/articles/3774001",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T23:00:18+00:00",
    "summary": "据媒体报道，马斯克旗下SpaceX认购订单已超可发行股份总量，预计6月11日定价，次日开盘交易，但目前仍处于路演早期阶段，相关细节仍可能发生变化。"
  },
  {
    "id": "wscn:3773990",
    "domain": "股票",
    "title": "“白宫股神”再吹票：特朗普：两房市值可达1万亿美元",
    "url": "https://wallstreetcn.com/articles/3773990",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T22:46:15+00:00",
    "summary": "周五美股盘初，房利美一度上涨10.4%，房地美一度上涨9.7%，随后大幅回落，最终房利美收跌0.74%，房地美收跌1.16%。此前英特尔、美光、戴尔等市场热门股大涨背后都有特朗普持仓或公开表态，市场对特朗普表态高度关注。"
  },
  {
    "id": "wscn:3773999",
    "domain": "股票",
    "title": "迈威尔科技与Flex将被纳入标普500",
    "url": "https://wallstreetcn.com/articles/3773999",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T22:26:56+00:00",
    "summary": "本次变动将于6月22日周一美股开盘时生效，届时Campbell's与Pool Corp将同步从指数中移除。纳入标普500意味着触达更广泛的投资群体，涵盖追踪该指数的被动基金，以及在投资范围上存在限制的主动基金。Marvell盘后股价上涨6%，Flex上涨4%。"
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
    "id": "hn:48391046",
    "domain": "股票",
    "title": "We Uncovered a Hidden Wealth Transfer in the SpaceX IPO. You're Holding the Bag [video]",
    "url": "https://www.youtube.com/watch?v=sYA-z0Y8WRQ",
    "source": "CharlesW",
    "platform": "hackernews",
    "points": 28,
    "published_at": "2026-06-03T22:32:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:48382926",
    "domain": "股票",
    "title": "Goldman Sachs CEO says markets in 'greed' mode as AI companies seek billions",
    "url": "https://www.cnbc.com/2026/06/02/goldman-ceo-david-solomon-greed-mode-ai-firms-ipos.html",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-06-03T12:08:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:48369063",
    "domain": "股票",
    "title": "Elon Musk Laid Out 602 Goals. We Counted How Many He Hit",
    "url": "https://www.nytimes.com/interactive/2026/06/02/technology/elon-musk-promises-spacex-ipo.html",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 23,
    "published_at": "2026-06-02T11:56:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:48383625",
    "domain": "股票",
    "title": "Dell inks $9.7B Pentagon contract after Trump acquires stock",
    "url": "https://www.washingtonpost.com/politics/2026/05/28/dell-inks-97-billion-pentagon-contract-after-trump-acquires-stock-praises-company/",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-06-03T13:19:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:48193111",
    "domain": "股票",
    "title": "Anthropic Is Preparing for IPO and We Should Be Worried",
    "url": "https://www.vincentschmalbach.com/anthropic-ipo-developers-should-be-worried-v2/",
    "source": "vincent_s",
    "platform": "hackernews",
    "points": 89,
    "published_at": "2026-05-19T13:30:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:48368083",
    "domain": "股票",
    "title": "Ask HN: What is your opinion on index rule changes to accommodate Mega-Cap IPOs?",
    "url": "https://news.ycombinator.com/item?id=48368083",
    "source": "figmert",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-06-02T09:55:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:48390904",
    "domain": "股票",
    "title": "SpaceX Sets Price for $1.77T IPO",
    "url": "https://www.cnbc.com/2026/06/03/spacex-ipo-stock-price-roadshow-musk.html",
    "source": "gen220",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-06-03T22:19:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:48281983",
    "domain": "股票",
    "title": "Show HN: A website that tracks every stock trade Congress makes",
    "url": "https://congress.kadoa.com/",
    "source": "hubraumhugo",
    "platform": "hackernews",
    "points": 63,
    "published_at": "2026-05-26T16:28:56+00:00",
    "summary": ""
  },
  {
    "id": "hn:48359035",
    "domain": "股票",
    "title": "Anthropic Files to Go Public, Setting Stage for Huge I.P.O.",
    "url": "https://www.nytimes.com/2026/06/01/technology/anthropic-ipo.html",
    "source": "jbegley",
    "platform": "hackernews",
    "points": 26,
    "published_at": "2026-06-01T16:27:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:48285468",
    "domain": "股票",
    "title": "There are now more ETFs than stocks in the US",
    "url": "https://www.apollo.com/wealth/the-daily-spark/more-etfs-than-stocks",
    "source": "akyuu",
    "platform": "hackernews",
    "points": 44,
    "published_at": "2026-05-26T20:22:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:48280561",
    "domain": "股票",
    "title": "Stockholm poised to become leading European geospatial intel player",
    "url": "https://www.intelligenceonline.com/europe-russia/2026/05/26/stockholm-poised-to-become-leading-european-geospatial-intel-player,110772386-eve",
    "source": "alephnerd",
    "platform": "hackernews",
    "points": 44,
    "published_at": "2026-05-26T14:44:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:48354214",
    "domain": "股票",
    "title": "How Not to Buy SpaceX Stock (It's Harder Than You Think)",
    "url": "https://cranberries.medium.com/how-not-to-buy-spacex-stock-its-harder-than-you-think-a37610cb8bd3",
    "source": "clktmr",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-06-01T08:50:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:48343303",
    "domain": "股票",
    "title": "The SpaceX IPO is great for Elon Musk and terrible for you",
    "url": "https://www.theverge.com/ai-artificial-intelligence/940001/elon-musk-spacex-ipo-ai",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-05-31T05:34:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:48231815",
    "domain": "股票",
    "title": "SpaceX not the behemoth everyone thought",
    "url": "https://www.axios.com/2026/05/21/spacex-ipo-musk-ai",
    "source": "kaycebasques",
    "platform": "hackernews",
    "points": 61,
    "published_at": "2026-05-22T04:03:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:48330421",
    "domain": "股票",
    "title": "The record divide between corporate profits and worker pay",
    "url": "https://www.wsj.com/finance/stocks/the-record-divide-between-corporate-profits-and-worker-pay-ea4c75bc",
    "source": "hhs",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-05-29T22:55:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:48229528",
    "domain": "股票",
    "title": "The SpaceX IPO It's Worse Than You Think [video]",
    "url": "https://www.youtube.com/watch?v=-X6YzlY_8tM",
    "source": "ZeljkoS",
    "platform": "hackernews",
    "points": 47,
    "published_at": "2026-05-21T22:19:28+00:00",
    "summary": ""
  },
  {
    "id": "hn:48254524",
    "domain": "股票",
    "title": "Reddit stock drops almost 6%, Meta launches standalone app for online forums",
    "url": "https://www.cnbc.com/2026/05/22/reddit-stock-drops-after-meta-launches-forum-app.html",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-05-24T04:58:51+00:00",
    "summary": ""
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
    "id": "hn:48297843",
    "domain": "股票",
    "title": "Steam Deck OLED is back in stock, with a price increase for both models",
    "url": "https://store.steampowered.com/news/group/45479024/view/672869045073085538",
    "source": "no_news_is",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-05-27T17:50:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:48088151",
    "domain": "金融",
    "title": "Maryland citizens hit with $2B power grid upgrade for out-of-state AI",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/maryland-citizens-slapped-with-usd2-billion-grid-upgrade-bill-for-out-of-state-ai-data-centers-state-complains-to-federal-energy-regulators-says-additional-cost-breaks-ratepayer-protection-pledge-promises",
    "source": "lemonberry",
    "platform": "hackernews",
    "points": 319,
    "published_at": "2026-05-10T21:16:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:48108313",
    "domain": "金融",
    "title": "US inflation jumps to 3.8% as energy costs surge from Iran war",
    "url": "https://www.bbc.com/news/articles/c202pgxx89lo",
    "source": "tartoran",
    "platform": "hackernews",
    "points": 260,
    "published_at": "2026-05-12T13:51:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:48100152",
    "domain": "金融",
    "title": "590k buyers paid $59M for Trump's gold phone, but not one has shipped",
    "url": "https://finance.yahoo.com/markets/stocks/articles/590-000-buyers-paid-59-223500998.html",
    "source": "surprisetalk",
    "platform": "hackernews",
    "points": 162,
    "published_at": "2026-05-11T20:19:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:48406282",
    "domain": "金融",
    "title": "S&P Global keeps fast index entry rules unchanged as SpaceX listing looms",
    "url": "https://www.reuters.com/business/finance/sp-global-keeps-fast-entry-proposal-unchanged-spacex-listing-looms-2026-06-04/",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 49,
    "published_at": "2026-06-04T23:55:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:48206387",
    "domain": "金融",
    "title": "The quadratic sandwich",
    "url": "https://fedemagnani.github.io/math/2026/04/08/the-quadratic-sandwich.html",
    "source": "cpp_frog",
    "platform": "hackernews",
    "points": 147,
    "published_at": "2026-05-20T12:06:56+00:00",
    "summary": ""
  },
  {
    "id": "hn:48384810",
    "domain": "金融",
    "title": "Tesla retroactively added 'supervised' to FSD contracts owners signed years ago",
    "url": "https://electrek.co/2026/06/03/tesla-retroactively-modified-fsd-contracts-supervised/",
    "source": "breve",
    "platform": "hackernews",
    "points": 72,
    "published_at": "2026-06-03T14:43:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:48360414",
    "domain": "金融",
    "title": "Making Debian or Fedora persistent live images",
    "url": "https://sigwait.org/~alex/blog/2026/05/28/smdBC8.html",
    "source": "henry_flower",
    "platform": "hackernews",
    "points": 89,
    "published_at": "2026-06-01T18:02:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:48401755",
    "domain": "金融",
    "title": "Fedora 43 Upgrade revealed 20 years old Outlook Security Bug",
    "url": "https://fedoramagazine.org/fedora-43-upgrade-revealed-20-years-old-outlook-security-bug/",
    "source": "thewebguyd",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-06-04T17:24:22+00:00",
    "summary": ""
  },
  {
    "id": "hn:48403461",
    "domain": "金融",
    "title": "Open Letter to President of Russian Federation from President of Ukraine",
    "url": "https://www.president.gov.ua/en/news/vidkritij-list-prezidentu-rosijskoyi-federaciyi-vid-preziden-104769",
    "source": "defly",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-06-04T19:27:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:48371952",
    "domain": "金融",
    "title": "Amazon joins Microsoft in sending message to employees",
    "url": "https://finance.yahoo.com/sectors/technology/articles/amazon-joins-microsoft-sending-shocking-171700630.html",
    "source": "hereticles",
    "platform": "hackernews",
    "points": 28,
    "published_at": "2026-06-02T15:58:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:48377347",
    "domain": "金融",
    "title": "Feds failing in bid to take a supercomputer from a climate research center",
    "url": "https://arstechnica.com/science/2026/06/judge-blocks-part-of-trump-admins-effort-to-hurt-colorado-research-center/",
    "source": "yodon",
    "platform": "hackernews",
    "points": 28,
    "published_at": "2026-06-02T22:46:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:48317563",
    "domain": "金融",
    "title": "Microsoft data suggests using AI is more expensive than hiring people",
    "url": "https://finance.yahoo.com/sectors/technology/articles/microsoft-data-suggests-using-ai-225900743.html",
    "source": "voxadam",
    "platform": "hackernews",
    "points": 68,
    "published_at": "2026-05-29T00:49:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:48055238",
    "domain": "金融",
    "title": "Cloudflare lays off 1,100 employees (~20% of workforce)",
    "url": "https://finance.yahoo.com/markets/stocks/articles/cloudflare-announces-first-quarter-2026-201500778.html",
    "source": "gcr",
    "platform": "hackernews",
    "points": 83,
    "published_at": "2026-05-07T21:22:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:48377419",
    "domain": "金融",
    "title": "FBI charges two NIH researchers with smuggling monkeypox to US from Congo",
    "url": "https://www.justice.gov/usao-edmi/pr/feds-charge-foreign-nationals-working-national-institutes-health-smuggling-monkeypox",
    "source": "delichon",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-06-02T22:58:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:48328797",
    "domain": "金融",
    "title": "Federal judge orders Trump's name be removed from Kennedy Center",
    "url": "https://www.msn.com/en-us/news/politics/federal-judge-orders-trump-s-name-be-removed-from-kennedy-center/ar-AA24neRw",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 27,
    "published_at": "2026-05-29T20:29:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:48327518",
    "domain": "金融",
    "title": "Americans Are Falling Behind on Their $1.25T Credit-Card Bill",
    "url": "https://www.wsj.com/personal-finance/credit/us-credit-card-debt-af5c7c77",
    "source": "tcp_handshaker",
    "platform": "hackernews",
    "points": 26,
    "published_at": "2026-05-29T18:41:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:48349067",
    "domain": "金融",
    "title": "Nearly Half of Home Insurance Claims Result in Zero Payout",
    "url": "https://www.wsj.com/finance/the-home-insurance-coin-flip-nearly-half-of-claims-result-in-zero-payout-4b49acaf",
    "source": "bookofjoe",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-05-31T19:45:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:48338988",
    "domain": "金融",
    "title": "Driver, 87, dies after Tesla on Autopilot mode crashes into pond",
    "url": "https://www.usatoday.com/story/news/nation/2026/05/29/tesla-on-autopilot-mode-crashes-into-pond-87-year-old-driver-dies/90319482007/",
    "source": "thinkcontext",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-05-30T17:59:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:48333813",
    "domain": "金融",
    "title": "Tesla Self-Certifies Level 4 Autonomous Vehicles in Texas",
    "url": "https://www.notateslaapp.com/news/4216/tesla-self-certifies-l4-autonomy-in-texas",
    "source": "frankacter",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-05-30T07:58:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:48210413",
    "domain": "金融",
    "title": "Standard Chartered CEO walks back comment about 'lower-value human capital'",
    "url": "https://www.wsj.com/finance/banking/ceo-walks-back-comment-about-replacing-lower-value-human-capital-with-ai-15bdfc5c",
    "source": "Brajeshwar",
    "platform": "hackernews",
    "points": 57,
    "published_at": "2026-05-20T16:38:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:48341005",
    "domain": "金融",
    "title": "Tesla's 'Full Self-Driving' fraud lawsuit gets first hearing in China",
    "url": "https://electrek.co/2026/05/30/tesla-fsd-china-lawsuit-first-hearing-10-owners/",
    "source": "breve",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-05-30T21:58:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:48364392",
    "domain": "金融",
    "title": "How to Silence the Federal Workforce",
    "url": "https://www.theatlantic.com/ideas/2026/06/trumps-intimidation-whistleblowers-nda/687377/",
    "source": "paulpauper",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-06-02T00:38:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:48271942",
    "domain": "金融",
    "title": "Show HN: Fungible – A local personal finance app in the terminal",
    "url": "https://github.com/tomfunk/fungible",
    "source": "tomfunk",
    "platform": "hackernews",
    "points": 30,
    "published_at": "2026-05-25T21:35:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:48271001",
    "domain": "金融",
    "title": "Stablecoins Are Private Money. That's Why They're a Risk to the Economy",
    "url": "https://www.wsj.com/finance/currencies/stablecoins-are-private-money-thats-why-theyre-a-risk-to-the-economy-d3498171",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 27,
    "published_at": "2026-05-25T20:02:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:48104043",
    "domain": "金融",
    "title": "Arcadia, CA, Mayor Federally Charged with Acting as Illegal Agent of PRC, Pleads",
    "url": "https://www.justice.gov/usao-cdca/pr/arcadia-mayor-federally-charged-acting-illegal-agent-peoples-republic-china",
    "source": "737min",
    "platform": "hackernews",
    "points": 37,
    "published_at": "2026-05-12T03:59:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:48307404",
    "domain": "金融",
    "title": "Why Tesla's AI trainers don't trust its self-driving tech – or its safety stats",
    "url": "https://www.reuters.com/investigations/why-teslas-ai-trainers-dont-trust-its-self-driving-tech-or-its-safety-stats-2026-05-28/",
    "source": "puzzlingcaptcha",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-05-28T11:21:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:48287165",
    "domain": "金融",
    "title": "Trump administration proposes NDAs for federal workers",
    "url": "https://www.reuters.com/world/us/trump-administration-proposes-non-disclosure-agreements-us-federal-workers-2026-05-26/",
    "source": "SubiculumCode",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-05-26T22:58:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:48199462",
    "domain": "金融",
    "title": "Invisible_playwright: Stealth Firefox that passes every bot detection test",
    "url": "https://github.com/feder-cr/invisible_playwright",
    "source": "thunderbong",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-05-19T20:51:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:48060663",
    "domain": "金融",
    "title": "Salary isn't everything: Why flexibility to work remotely is the future of work",
    "url": "https://thehill.com/opinion/finance/5859902-hybrid-work-performance-retention/",
    "source": "robtherobber",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-05-08T09:20:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:48115538",
    "domain": "金融",
    "title": "America is experiencing a productivity miracle",
    "url": "https://www.economist.com/finance-and-economics/2026/05/11/america-is-experiencing-a-productivity-miracle",
    "source": "mackmcconnell",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-05-12T22:39:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:48229518",
    "domain": "金融",
    "title": "Show HN: Smithereen – an early-Facebook-style Fediverse server",
    "url": "https://smithereen.software",
    "source": "grishka",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-05-21T22:18:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:48130202",
    "domain": "金融",
    "title": "Federalism for Anti-Fascists",
    "url": "https://medium.com/@carmitage/federalism-for-anti-fascists-e83fb20c6fc2",
    "source": "hkhn",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-05-14T01:49:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:48058421",
    "domain": "金融",
    "title": "Trump Is Getting Away with Murdering an American Industry",
    "url": "https://heatmap.news/plus/the-fight/spotlight/trump-federal-aviation-administration-wind-farms",
    "source": "gok",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-05-08T04:05:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:48225108",
    "domain": "金融",
    "title": "Jeff Bezos says bottom half of U.S. earners should pay no federal income tax",
    "url": "https://www.cbsnews.com/news/jeff-bezos-zero-federal-income-tax-lower-earners/",
    "source": "johnshades",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-05-21T16:11:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:48222708",
    "domain": "金融",
    "title": "Fedora Retiring Its Deepin Desktop Packages",
    "url": "https://www.phoronix.com/news/Fedora-Removing-Deepin",
    "source": "AdmiralAsshat",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-05-21T14:00:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:48156037",
    "domain": "金融",
    "title": "Senior NIAID Official Indicted for Concealing Records During Covid Pandemic",
    "url": "https://www.justice.gov/opa/pr/former-senior-niaid-official-indicted-concealing-federal-records-during-covid-19-pandemic-0",
    "source": "Jimmc414",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-05-16T01:44:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:48084491",
    "domain": "金融",
    "title": "Disgraced US gov software contractor found guilty of database destruction",
    "url": "https://www.theregister.com/cyber-crime/2026/05/08/former-us-contractor-convicted-in-federal-database-wipe-case/5237296",
    "source": "Bender",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-05-10T14:54:11+00:00",
    "summary": ""
  }
]
```
