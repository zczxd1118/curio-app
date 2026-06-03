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

- 今日日期：`2026-06-03`
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
  "date": "2026-06-03",
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
    "id": "bvid:BV11NNAz5EKn",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！",
    "url": "http://www.bilibili.com/video/av116187623069851",
    "source": "AI-智能体搭建教程",
    "platform": "bilibili",
    "points": 580472,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1eK5DzHEWu",
    "domain": "AI",
    "title": "MCP实战指南，mcp视频教程，2小时学透mcp",
    "url": "http://www.bilibili.com/video/av114380213586544",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 365885,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1GyGX6TEDi",
    "domain": "AI",
    "title": "1个人，如何通过Vibe Coding快速实现变现？",
    "url": "http://www.bilibili.com/video/av116650858847182",
    "source": "老麦的工具库",
    "platform": "bilibili",
    "points": 338358,
    "published_at": "2026-05-29T12:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 325103,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1SQo5BAEBo",
    "domain": "AI",
    "title": "trae使用教程【B站最详细，零基础必看！】trae小白入门到精通traeCN教程traeexceltrae项目实战trae安装教程用教程trae开发小程序",
    "url": "http://www.bilibili.com/video/av116458407336746",
    "source": "trae教程",
    "platform": "bilibili",
    "points": 299168,
    "published_at": "2026-04-24T07:10:58+00:00",
    "summary": "trae使用教程trae小白入门到精通traeCN教程traeexceltrae项目实战trae安装教程用trae开发小程序traecn使用教程"
  },
  {
    "id": "bvid:BV1AHDuBoE2S",
    "domain": "AI",
    "title": "锐评vibe coding工具“从夯到拉”",
    "url": "http://www.bilibili.com/video/av116347090502349",
    "source": "布鲁歇一歇",
    "platform": "bilibili",
    "points": 231414,
    "published_at": "2026-04-04T15:19:25+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1qGc7zwEX6",
    "domain": "AI",
    "title": "史上最强 AI 编程工具Cursor来啦！Cursor保姆级使用教程！新手友好！看到就是赚到！！！",
    "url": "http://www.bilibili.com/video/av116061928226926",
    "source": "知名的阿呆同学",
    "platform": "bilibili",
    "points": 222922,
    "published_at": "2026-02-19T07:34:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1Yi5M6DERk",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116560144369496",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 183790,
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
    "points": 173128,
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
    "points": 150483,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV1DaruB2ELU",
    "domain": "AI",
    "title": "APP 从 0 → 上线发布！免费 Vibe Coding 流程：Stitch + AI Studio + Antigravity！",
    "url": "http://www.bilibili.com/video/av115867111130186",
    "source": "陶渊xiao明",
    "platform": "bilibili",
    "points": 143713,
    "published_at": "2026-01-10T09:30:00+00:00",
    "summary": "这期视频，我们完整演示了一套「真正能上线」的 Vibe Coding 开发流程 🚀\n\n不是做 Demo，也不是只生成页面，而是从一个想法出发，\n一步步做出一个 包含前端、后端、数据库、部署 的完整 App。\n\n我们会用一个「在线宠物领养 App」作为真实案例，\n把整个流程从头到尾全部跑一遍 🐶🐱\n\n适合人群：\n✔️ 想快速把想法做成产品的人\n✔️ 不想从零手写前后端的开发者\n✔️ 对 AI 编程 "
  },
  {
    "id": "bvid:BV16NvCBrEVs",
    "domain": "AI",
    "title": "什么是Vibe Coding，以及怎么使用？",
    "url": "http://www.bilibili.com/video/av115797133368973",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 141393,
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
    "points": 140365,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV11urFBrEc4",
    "domain": "AI",
    "title": "🚀告别Vibe Coding！用Superpowers让Claude Code写出工程级代码，一次通过零报错！遵循TDD最佳实践！支持Codex",
    "url": "http://www.bilibili.com/video/av115877227860495",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 130992,
    "published_at": "2026-01-11T15:43:58+00:00",
    "summary": "🚀开发者必看！Superpowers把专业工程团队方法论固化成Skills，让Claude Code告别越写越乱的困境：规格驱动+代码质量双重保障！AI编程新范式！头脑风暴+计划+执行一条龙自动化\n\n\n🚀🚀🚀 视频简介：\n🎬 本期视频详细演示了开源AI编程工作流系统Superpowers的完整使用方法，并通过开发一款iOS时间线笔记原生应用来实测其效果。\n🔧 核心内容：\nSuperpowers工作"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 88902,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1KX9jB8E9M",
    "domain": "AI",
    "title": "【2026最新版】目前B站最全最细的 CurSor AI编程零基础全套教程，手把手教你搭建高效Cursor工作流，全程干货无废话！比付费效果强十倍",
    "url": "http://www.bilibili.com/video/av116328887225403",
    "source": "AI大模型技术教程",
    "platform": "bilibili",
    "points": 70405,
    "published_at": "2026-04-01T10:12:34+00:00",
    "summary": "视频配套文档课件笔记代码及AI大模型学习路线图戳这里获取→https://www.bilibili.com/read/cv41777105/?jump_opus=1"
  },
  {
    "id": "bvid:BV1XdFzz7Ei8",
    "domain": "AI",
    "title": "不写代码就能轻松开发应用？Cursor+Gemini 超强指挥官工作法！",
    "url": "http://www.bilibili.com/video/av116021511853604",
    "source": "PM刘搞定",
    "platform": "bilibili",
    "points": 55868,
    "published_at": "2026-02-06T03:17:18+00:00",
    "summary": "如何像传统互联网大厂一样指挥AI干活？本期视频通过一个“个人工作台”的实战项目，拆解了一套利用 LLM (Gemini) 辅助 Cursor 开发的高效工作流。\n\n核心内容：\n角色转换：你不是程序员，你是产品经理（PM）。\n文档驱动：如何用 AI 生成标准的产品文档 (PRD)、UI 文档和技术方案。\n避坑指南：如何防止 Cursor “手搓核弹”或开发中途“失忆”。\n\n实操流程：\nStep 1："
  },
  {
    "id": "bvid:BV1ZjDYB7Eam",
    "domain": "AI",
    "title": "从 0 到 1：6小时掌握 Vibe Coding！ Claude Code ＋ AI 这支影片直接让你超越 90% AI 玩家",
    "url": "http://www.bilibili.com/video/av116362122894759",
    "source": "李哈利Harry",
    "platform": "bilibili",
    "points": 51657,
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
    "points": 50362,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1c8NFzhEMi",
    "domain": "AI",
    "title": "一个CLI干掉所有MCP工具，省99%的token mcp2cli",
    "url": "http://www.bilibili.com/video/av116204349953548",
    "source": "探索未至之境",
    "platform": "bilibili",
    "points": 48446,
    "published_at": "2026-03-10T10:18:17+00:00",
    "summary": "深度解析GitHub热门项目mcp2cli——一个能把任何MCP服务器或OpenAPI规范变成命令行工具的Python项目。它用&quot;懒发现&quot;机制，把MCP协议的token浪费从数十万降到几千，节省高达99%。整个核心实现只有一个Python文件，却支持三种接入模式、OAuth认证和智能缓存。发布仅一天就获得372颗星，但社区也有激烈争议：CLI真的能取代MCP吗？准确率会不会受影"
  },
  {
    "id": "bvid:BV13K1YBtE6e",
    "domain": "AI",
    "title": "【GMM】MCP 使用说明",
    "url": "http://www.bilibili.com/video/av115485010168640",
    "source": "3DM小莫",
    "platform": "bilibili",
    "points": 35748,
    "published_at": "2025-11-03T09:19:08+00:00",
    "summary": "MCP 支持 是 Gloss Mod Manager（GMM ）在 1.62.0 新增的一个功能， 你需要至少更新到 1.62 才能使用此功能；\n\n你可以使用任何支持 MCP 的客户端 和 AI 使用它, 但建议你的 AI 最大 Token 至少有 32K, 否则部分功能可能会受影响。\n\n相关代码已经开源，欢迎参与维护:  https://github.com/GlossMod/Gloss-Mod"
  },
  {
    "id": "bvid:BV1thXHY2EXh",
    "domain": "AI",
    "title": "Cursor+three.js，简单提示词也能生成交互式3D",
    "url": "http://www.bilibili.com/video/av114205059521179",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 33344,
    "published_at": "2025-03-22T08:11:40+00:00",
    "summary": "上周发布了 Cursor+Blender MCP 快速实现3D建模的教程，但由于目前MCP还不是特别稳定，加上配置有点麻烦不一定能一次成功，所以不少小伙伴被劝退了。\n.\n后面我发现借助three.js，就能让大家通过简单的提示词，轻松实现一些还不错的交互式3D场景，非常适合放在一些教学或者科普场景。大家快去试试吧 ~ \n.\n欢迎加入我的知识星球，有问必答：https://t.zsxq.com/fD"
  },
  {
    "id": "bvid:BV1ap2fBvEt9",
    "domain": "AI",
    "title": "如何使用「Operit AI」：你的下一代AI手机助手",
    "url": "http://www.bilibili.com/video/av115677243447909",
    "source": "默睦",
    "platform": "bilibili",
    "points": 29192,
    "published_at": "2025-12-07T08:06:42+00:00",
    "summary": "下载地址：https://github.com/AAswordman/Operit\n\n相关软件资料下载：https://www.123pan.com/s/IKgAjv-Hinsv.html\n\n官方交流群：458862019"
  },
  {
    "id": "bvid:BV1VCVS6PEAd",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent零基础全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116668525186915",
    "source": "大模型入门教程",
    "platform": "bilibili",
    "points": 21921,
    "published_at": "2026-05-31T09:46:57+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1duRMBDEh9",
    "domain": "AI",
    "title": "手把手带你从0搭建第二大脑｜Obsidian × AI Agent 全流程实操教程",
    "url": "http://www.bilibili.com/video/av116498135916107",
    "source": "Martina在进化",
    "platform": "bilibili",
    "points": 18082,
    "published_at": "2026-05-01T07:29:46+00:00",
    "summary": "上一期讲完第二大脑的概念之后，好多朋友说——听懂了，但还是不知道怎么下手。\n所以这一期我直接带大家从0操作一遍，全程手把手。\n✦ 下载哪个软件、装在哪里 \n✦ Obsidian基础功能 + Markdown格式快速入门 \n✦ 免费同步方案（不花那$4/月） \n✦ 国内外AI Agent工具怎么选（Claude Code vs Hermes） \n✦ 怎么让AI帮你搭LLM Wiki知识库 \n✦ We"
  },
  {
    "id": "bvid:BV14erKYuEaE",
    "domain": "AI",
    "title": "最强编程AI Cursor+Unity制作一个史诗游戏(详细)",
    "url": "http://www.bilibili.com/video/av113774908413987",
    "source": "多西杰克",
    "platform": "bilibili",
    "points": 17199,
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
    "points": 16927,
    "published_at": "2025-05-25T13:36:25+00:00",
    "summary": "文档：https://icnt94i5ctj4.feishu.cn/docx/ZkR3d1lfUosIFCx4qWJcI4QunY0\nshay大佬的HA SSE接入文档：https://bbs.hassbian.com/thread-29314-1-1.html"
  },
  {
    "id": "bvid:BV1HxDrB5Em2",
    "domain": "AI",
    "title": "【B站天花板】全网最细最全的Agent应用开发教程|手把手教你搭建企业级智能体，全程干货无废话，小白直接上手不踩坑,帮你少走 99% 弯路！ LLM|大模型",
    "url": "http://www.bilibili.com/video/av116367441334742",
    "source": "AI-Agent开发",
    "platform": "bilibili",
    "points": 16673,
    "published_at": "2026-04-08T05:40:05+00:00",
    "summary": "【B站天花板】全网最细最全的Agent应用开发教程|手把手教你搭建企业级智能体，全程干货无废话，小白直接上手不踩坑,帮你少走 99% 弯路！ LLM|大模型"
  },
  {
    "id": "bvid:BV1W9cZzxEYs",
    "domain": "AI",
    "title": "AI 当助手！Claude 深度协助 UE5 游戏开发全流程",
    "url": "http://www.bilibili.com/video/av116209752277031",
    "source": "叁昧火游戏",
    "platform": "bilibili",
    "points": 14595,
    "published_at": "2026-03-11T12:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1WtoTBiEuR",
    "domain": "AI",
    "title": "Claude Code多Agent模式实战分享",
    "url": "http://www.bilibili.com/video/av116454666012312",
    "source": "Simon林_",
    "platform": "bilibili",
    "points": 14060,
    "published_at": "2026-04-23T15:18:08+00:00",
    "summary": "Claude Code有2种多Agent模式：多个subagents模式和多个独立agent模式"
  },
  {
    "id": "bvid:BV1wuLHzDEGA",
    "domain": "AI",
    "title": "【Godot&amp;Cursor】0.亲测一个月后，我选择Godot+Cursor组合做独立游戏",
    "url": "http://www.bilibili.com/video/av114398869853632",
    "source": "破妄-胖",
    "platform": "bilibili",
    "points": 13462,
    "published_at": "2025-04-25T13:43:22+00:00",
    "summary": "飞书文档：https://sh67ozct1z.feishu.cn/docx/Hn5jd0cE6op1Sux9RrFcl8Npnbd"
  },
  {
    "id": "bvid:BV18TZYY8EuJ",
    "domain": "AI",
    "title": "微软最新AI Agent入门课程 • 中英",
    "url": "http://www.bilibili.com/video/av114246130076146",
    "source": "Mindofuture",
    "platform": "bilibili",
    "points": 12687,
    "published_at": "2025-03-30T02:06:00+00:00",
    "summary": "在这门包含10节课的课程中，我们将带你从概念到代码，全面覆盖构建AI代理的基础知识。在这里找到完整的“AI代理入门”课程及代码示例\nhttps://github.com/microsoft/ai-agents-for-beginners\n\nP01 什么是AI代理\nP02 使用哪种AI代理框架\nP03 如何设计优秀的AI代理\nP04 什么是代理工具使用设计模式\nP05 什么是代理式RAG\nP06 如"
  },
  {
    "id": "bvid:BV1yT8qzMEbd",
    "domain": "AI",
    "title": "基于SpringAI开发Java版mcp服务",
    "url": "http://www.bilibili.com/video/av114942720148945",
    "source": "程序员Cafe",
    "platform": "bilibili",
    "points": 11111,
    "published_at": "2025-07-30T15:05:27+00:00",
    "summary": "如何用Java开发一个mcp服务？如何把已有的spingboot微服务改造成mcp服务呢？如何在mcp客户端调用mcp服务？\n今天来一个保姆级教学"
  },
  {
    "id": "bvid:BV1L9VZ6bE2r",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！！",
    "url": "http://www.bilibili.com/video/av116673893893645",
    "source": "马小洋qwer",
    "platform": "bilibili",
    "points": 8871,
    "published_at": "2026-06-01T08:30:19+00:00",
    "summary": "视频制作不易，如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托~这对我真的很重要！"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 8921,
    "published_at": "2025-04-14T02:30:00+00:00",
    "summary": "MCP服务网站：https://smithery.ai/\nCherry Studio官方网站：https://cherry-ai.com/"
  },
  {
    "id": "bvid:BV1RtGU6hEDd",
    "domain": "AI",
    "title": "DeepSeek-Reasonix 【保姆级教程】：专为 DeepSeek 打造的 AI 编程 Agent客户端，长会话成本到底能省多少？",
    "url": "http://www.bilibili.com/video/av116647486556383",
    "source": "程序员晓刘",
    "platform": "bilibili",
    "points": 7914,
    "published_at": "2026-05-27T16:33:52+00:00",
    "summary": "本期体验 DeepSeek-Reasonix 这个开源项目，主要看客户端界面、模型模式、会话导入、MCP 配置、记忆与缓存等功能。内容基于个人使用记录，不做夸张结论，适合对 DeepSeek 生态和 AI 编程工具感兴趣的朋友参考。"
  },
  {
    "id": "bvid:BV19jL46gEab",
    "domain": "AI",
    "title": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！",
    "url": "http://www.bilibili.com/video/av116611415541849",
    "source": "Agent搭建",
    "platform": "bilibili",
    "points": 7349,
    "published_at": "2026-05-21T07:43:25+00:00",
    "summary": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！"
  },
  {
    "id": "bvid:BV1caVh6fE6Z",
    "domain": "AI",
    "title": "【2026最新版】绝对是B站讲的最细的Claude Code教程，从国内环境安装出发，项目开发及个人使用总结带你玩转 Vibe Coding！",
    "url": "http://www.bilibili.com/video/av116656764358481",
    "source": "AI大模型_",
    "platform": "bilibili",
    "points": 7276,
    "published_at": "2026-05-29T07:53:39+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n本视频配套课件笔记代码/学习大纲/大模型学习路线戳这里获取→https://www.bilibili.com/opus/1195847460814061571?spm_id_from=333.1387.0.0\n另外有需要AI大模型学习路线图+必看书籍（国内外大牛著作）+入门及进阶视频教程+项目实战及源码提供+面试实战场景"
  },
  {
    "id": "bvid:BV1nyVZ6vEZF",
    "domain": "AI",
    "title": "【AI+自动化测试全套教程】7天精通AI自动化测试，还不会AI就要被淘汰了！（学完即就业）",
    "url": "http://www.bilibili.com/video/av116673927453339",
    "source": "黑马测试人",
    "platform": "bilibili",
    "points": 7117,
    "published_at": "2026-06-01T09:12:55+00:00",
    "summary": "免费领取配套视频资料+源码+课件+学习笔记！（备注B站）\n配套资源领取处：\nhttps://www.bilibili.com/read/cv28338591\n喜欢本教程的B友们【点赞+投币+收藏】一键三连呀（゜-゜）つロ 干杯~"
  },
  {
    "id": "bvid:BV1eUVJ6EEB9",
    "domain": "AI",
    "title": "2026搞懂Java+AI大模型全套教程 | Spring AI+RAG+AI Agent+DeepSeek+航空AI智能客服项目实战，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116668374254145",
    "source": "程序员诸葛",
    "platform": "bilibili",
    "points": 7051,
    "published_at": "2026-05-31T09:12:07+00:00",
    "summary": "整理制作不易，大家记得点个关注，一键三连呀【点赞、收藏、转发】感谢支持~\n配套笔记和100万字面试宝典+场景题，简历模板，Java P 5~P8技术栈学习路线自取：https://t.bilibili.com/783606020197842963"
  },
  {
    "id": "bvid:BV1QU6GYFEio",
    "domain": "AI",
    "title": "[课程4] 用Cursor开发数据库真的很简单 | Agent应用 | 用Codebase解决跨文件错误",
    "url": "http://www.bilibili.com/video/av113742109021318",
    "source": "Zhu的AI日记",
    "platform": "bilibili",
    "points": 6948,
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
    "points": 6343,
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
    "points": 5942,
    "published_at": "2025-04-30T08:51:30+00:00",
    "summary": "什么是MCP，怎么样使用MCP Server，不用写SQL语句就可以查询数据库。\n\nMCP Servers\nhttps://smithery.ai/\nhttps://github.com/punkpeye/awesome-mcp-servers\nhttps://github.com/modelcontextprotocol/servers\n\nMCP Server for MySQL based o"
  },
  {
    "id": "bvid:BV1BJvSBxEjw",
    "domain": "AI",
    "title": "用 Rust 构建你的第一个 AI Agent —— 完整教程（本地 LLM + 网络搜索）",
    "url": "http://www.bilibili.com/video/av115818809525301",
    "source": "ppt的bug",
    "platform": "bilibili",
    "points": 5297,
    "published_at": "2026-01-02T02:15:00+00:00",
    "summary": "https://www.youtube.com/watch?v=dVj9Wtg9MXQ\n🦀 使用 Rig 框架和 Ollama，用 Rust 构建一个可用于生产环境的 AI 研究型 Agent！\n 本完整教程将手把手带你创建一个智能代理，它能够进行网页搜索并综合整理信息——全部在你的本地机器上运行，无需任何 API 成本。\n在本视频中，你将学到：\n✅ 如何设计和组织一个 Rust AI Agent"
  },
  {
    "id": "bvid:BV1rE1SBpEha",
    "domain": "AI",
    "title": "【MCP】使用FastMCP快速实现MCP服务端和客户端功能",
    "url": "http://www.bilibili.com/video/av115512960883264",
    "source": "胖虎遛二狗",
    "platform": "bilibili",
    "points": 5264,
    "published_at": "2025-11-08T07:50:20+00:00",
    "summary": "相关文档：https://gofastmcp.com/getting-started/welcome\n大模型系列教程： https://github.com/echonoshy/cgft-llm"
  },
  {
    "id": "bvid:BV1f5DvB4Eoa",
    "domain": "AI",
    "title": "AI 直接操控 Cocos Creator！78 个自动化工具一键搞定场景搭建 让 AI 接管你的 Cocos Creator 编辑器 | Link CC MC",
    "url": "http://www.bilibili.com/video/av116362978528338",
    "source": "一个凡人鸭",
    "platform": "bilibili",
    "points": 5079,
    "published_at": "2026-04-07T10:40:52+00:00",
    "summary": "让 AI 直接操控 Cocos Creator 编辑器！\nLink CC MCP 是一款 AI 驱动的 Cocos Creator 编辑器自动化插件，通过 MCP 协议连接 Cursor 等 AI 编辑器，提供 78 个编辑器操作工具。\n你可以用自然语言让 AI：\n✦ 创建节点、搭建 UI 层级\n✦ 添加/修改组件、绑定脚本\n✦ 管理场景、资源、预制体\n✦ 截图查看场景效果\n✦ 批量操作、动画生成"
  },
  {
    "id": "bvid:BV1ZSVG6eE3V",
    "domain": "AI",
    "title": "【cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av116662284130312",
    "source": "非六于期",
    "platform": "bilibili",
    "points": 4921,
    "published_at": "2026-05-30T07:13:36+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1rhdgBMEK2",
    "domain": "AI",
    "title": "Claude Code + Figma MCP：传统 UI 开发流程已死？",
    "url": "http://www.bilibili.com/video/av116538183124050",
    "source": "犬哥网站",
    "platform": "bilibili",
    "points": 4874,
    "published_at": "2026-05-08T12:00:00+00:00",
    "summary": "▬▬▬▬▬ 🏆️ 犬哥专业服务 🏆️ ▬▬▬▬▬\n网页设计＆数位行销服务 ➜ https://frankknow.com\nWordPress 优质主机：https://frankknow.com/wordpress-hosting/\n\n▬▬▬▬▬ 🏆️ 精选架站系列 🏆️ ▬▬▬▬▬\n新手自学架站（网域＋主机＋WordPress 架站，一次学会）➜ https://frankknow.com/wp"
  },
  {
    "id": "bvid:BV1FXVz67Epw",
    "domain": "AI",
    "title": "【Claude Code】B站讲得最好的Claude Code教程，没有之一！国内直连保姆级教学，从安装到项目实战，开启Vibe Coding革命【附脚本】",
    "url": "http://www.bilibili.com/video/av116679279379085",
    "source": "马士兵学堂",
    "platform": "bilibili",
    "points": 4684,
    "published_at": "2026-06-02T07:27:09+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1Uc7Sz2EqJ",
    "domain": "AI",
    "title": "自动化挖漏洞哪家强？LLM+Burpsuite 组合出道，黑客看了直呼 “蚌埠住了”！",
    "url": "http://www.bilibili.com/video/av114612527701492",
    "source": "水獭安全",
    "platform": "bilibili",
    "points": 4782,
    "published_at": "2025-06-02T07:17:41+00:00",
    "summary": "通过 MCP 服务构建&quot;AI渗透测试工程师&quot;，实现Burp Suite的智能调度与自动化漏洞狩猎。"
  },
  {
    "id": "hn:48352939",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia RTX Spark",
    "url": "https://www.nvidia.com/en-us/products/rtx-spark/",
    "source": "shenli3514",
    "platform": "hackernews",
    "points": 422,
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
    "points": 284,
    "published_at": "2026-06-01T12:04:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:48377404",
    "domain": "AI 算力 / 半导体",
    "title": "Use your Nvidia GPU's VRAM as swap space on Linux",
    "url": "https://github.com/c0dejedi/nbd-vram",
    "source": "tanelpoder",
    "platform": "hackernews",
    "points": 282,
    "published_at": "2026-06-02T22:55:33+00:00",
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
    "points": 98,
    "published_at": "2026-06-01T13:05:02+00:00",
    "summary": ""
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
    "id": "hn:48012477",
    "domain": "AI 算力 / 半导体",
    "title": "Offenders sentenced up to 10 years for spying on TSMC",
    "url": "https://www.taipeitimes.com/News/front/archives/2026/04/28/2003856358",
    "source": "ironyman",
    "platform": "hackernews",
    "points": 127,
    "published_at": "2026-05-04T18:04:33+00:00",
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
    "id": "hn:48361912",
    "domain": "AI 算力 / 半导体",
    "title": "Michael Burry Just Called Nvidia's SpaceX Chip Deal 'Fugazi.'",
    "url": "https://247wallst.com/investing/2026/06/01/michael-burry-just-called-nvidias-spacex-chip-deal-fugazi-heres-why-it-all-seems-wrong/",
    "source": "johnbarron",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-06-01T20:06:32+00:00",
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
    "id": "rss:https://www.eetimes.com/taiwan-minister-emphasizes-collaboration-and-future-focus-on-photonics-wbg-and-quantum/",
    "domain": "AI 算力 / 半导体",
    "title": "Taiwan Minister Emphasizes Collaboration and Future Focus on Photonics, WBG, and Quantum",
    "url": "https://www.eetimes.com/taiwan-minister-emphasizes-collaboration-and-future-focus-on-photonics-wbg-and-quantum/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T06:00:00+00:00",
    "summary": "NSTC Minister Wu shares Taiwan's four-pillar shift from chipmaker to AI enabler. The post Taiwan Minister Emphasizes Collaboration and Future Focus on Photonics, WBG, and Quantum appeared first on EE "
  },
  {
    "id": "rss:https://www.eetimes.com/photonics-a-foundational-scaling-layer-for-ai-era-computing/",
    "domain": "AI 算力 / 半导体",
    "title": "Photonics: A Foundational Scaling Layer for AI-Era Computing",
    "url": "https://www.eetimes.com/photonics-a-foundational-scaling-layer-for-ai-era-computing/",
    "source": "Maurice Steinman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T00:08:10+00:00",
    "summary": "Photonics supercharges AI computing by shattering data bottlenecks. The post Photonics: A Foundational Scaling Layer for AI-Era Computing appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/physical-ai-pushes-chipmakers-up-the-value-chain/",
    "domain": "AI 算力 / 半导体",
    "title": "Physical AI Pushes Chipmakers Up the Value Chain",
    "url": "https://www.eetimes.com/physical-ai-pushes-chipmakers-up-the-value-chain/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T14:00:00+00:00",
    "summary": "At the TSMC European Symposium, European semiconductor CEOs spoke about how AI in influencing business. The post Physical AI Pushes Chipmakers Up the Value Chain appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/sciosense-launches-ufc23-ultrasonic-flow-converter-for-high-precision-ultra-low-power-smart-metering/",
    "domain": "AI 算力 / 半导体",
    "title": "ScioSense Launches UFC23 Ultrasonic Flow Converter for High-Precision, Ultra-Low-Power Smart Metering",
    "url": "https://www.eetimes.com/sciosense-launches-ufc23-ultrasonic-flow-converter-for-high-precision-ultra-low-power-smart-metering/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T07:00:00+00:00",
    "summary": "The UFC23 ultrasonic flow converter is claimed to allow manufacturers to retain flexibility over system architecture and microcontroller selection. The post ScioSense Launches UFC23 Ultrasonic Flow Co"
  },
  {
    "id": "rss:https://www.eetimes.com/tsmc-defends-transistor-scaling-amid-huaweis-hers-law-proposal/",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC Defends Transistor Scaling Amid Huawei’s ‘Her’s Law’ Proposal",
    "url": "https://www.eetimes.com/tsmc-defends-transistor-scaling-amid-huaweis-hers-law-proposal/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T18:12:48+00:00",
    "summary": "Kevin Zhang said 3D integration is important, but transistor scaling remains the semiconductor industry's primary driver of performance and energy-efficiency gains. The post TSMC Defends Transistor Sc"
  },
  {
    "id": "rss:https://www.eetimes.com/early-memory-contention-checks-reduce-ic-design-risks/",
    "domain": "AI 算力 / 半导体",
    "title": "Early Memory Contention Checks Reduce IC Design Risks",
    "url": "https://www.eetimes.com/early-memory-contention-checks-reduce-ic-design-risks/",
    "source": "Chun-hsiang Chang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T14:00:00+00:00",
    "summary": "Automated schematic-level contention analysis detects memory bottlenecks early, improving SoC reliability, predictability, and silicon quality. The post Early Memory Contention Checks Reduce IC Design"
  },
  {
    "id": "rss:https://www.eetimes.com/high-voltage-gan-bi-directional-switches-strong-performance-simpler-to-use/",
    "domain": "AI 算力 / 半导体",
    "title": "High-Voltage GaN Bi-Directional Switches: Strong Performance, Simpler to Use",
    "url": "https://www.eetimes.com/high-voltage-gan-bi-directional-switches-strong-performance-simpler-to-use/",
    "source": "Renesas",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T14:00:00+00:00",
    "summary": "The demand for more efficient power solutions continues to put pressure on designers to optimize system design without compromising performance. Read how you can simplify high-voltage power conversion"
  },
  {
    "id": "rss:https://www.eetimes.com/product-recall-management-guide-for-electronics-manufacturing-smbs/",
    "domain": "AI 算力 / 半导体",
    "title": "Product Recall Management Guide for Electronics Manufacturing SMBs",
    "url": "https://www.eetimes.com/product-recall-management-guide-for-electronics-manufacturing-smbs/",
    "source": "MRPeasy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T13:00:00+00:00",
    "summary": "This guide explains what product recalls are, what risks they create, and how small and midsize manufacturers can handle them in an organized way. The post Product Recall Management Guide for Electron"
  },
  {
    "id": "rss:https://www.eetimes.com/ai-accelerated-software-security-vulnerability-discovery-is-hardware-next/",
    "domain": "AI 算力 / 半导体",
    "title": "AI-Accelerated Software Security Vulnerability Discovery: Is Hardware Next?",
    "url": "https://www.eetimes.com/ai-accelerated-software-security-vulnerability-discovery-is-hardware-next/",
    "source": "Andreas Kuehlmann, General Manager – Security Solutions, Arteris",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T13:00:00+00:00",
    "summary": "AI is revolutionizing software vulnerability discovery. Could hardware security be next? Explore risks, AI threats and chip defense strategies. In depth. The post AI-Accelerated Software Security Vuln"
  },
  {
    "id": "rss:https://www.eetimes.com/nikon-leveraging-arf-scanner-price-to-challenge-asml/",
    "domain": "AI 算力 / 半导体",
    "title": "Nikon Leveraging ArF Scanner Price to Challenge ASML",
    "url": "https://www.eetimes.com/nikon-leveraging-arf-scanner-price-to-challenge-asml/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T11:57:55+00:00",
    "summary": "The Japanese litho firm is lowering the price of its ArF tools while also launching a brand-new immersion platform by 2028. The post Nikon Leveraging ArF Scanner Price to Challenge ASML appeared first"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-keyboards/cherry-xtrfy-launches-first-8k-ultra-wideband-gaming-keyboard-featuring-more-compact-70-percent-layout",
    "domain": "AI 算力 / 半导体",
    "title": "Cherry XTRFY launches first 8K ultra-wideband gaming keyboard — featuring more compact 70-percent layout",
    "url": "https://www.tomshardware.com/peripherals/gaming-keyboards/cherry-xtrfy-launches-first-8k-ultra-wideband-gaming-keyboard-featuring-more-compact-70-percent-layout",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T23:11:02+00:00",
    "summary": "Cherry XTRFY launched the first 8K ultra-wideband wireless gaming keyboard at Computex 2026. The keyboard features a 70-percent layout, low-profile switches, and a gasket mount design."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-addresses-arrow-lake-blunder-we-needed-to-build-back-our-reputation-says-arrow-lake-refreshs-low-price-a-key-first-step-laying-the-groundwork-for-nova-lake",
    "domain": "AI 算力 / 半导体",
    "title": "Intel addresses Arrow Lake blunder: 'We needed to build back our reputation' — says Arrow Lake Refresh's low price a key first step, laying the groundwork for Nova Lake",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-addresses-arrow-lake-blunder-we-needed-to-build-back-our-reputation-says-arrow-lake-refreshs-low-price-a-key-first-step-laying-the-groundwork-for-nova-lake",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T20:00:00+00:00",
    "summary": "Intel knows that Arrow Lake dealt a blow to its reputation among enthusiasts. Arrow Lake Refresh was an effort to correct that issue, laying the groundwork for Nova Lake later this year."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/quantum-computing/microsoft-announces-majorana-2-quantum-computing-chip-claims-a-practical-machine-will-come-in-2029",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft announces Majorana 2 quantum computing chip — claims a practical machine will come in 2029",
    "url": "https://www.tomshardware.com/tech-industry/quantum-computing/microsoft-announces-majorana-2-quantum-computing-chip-claims-a-practical-machine-will-come-in-2029",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T19:37:59+00:00",
    "summary": "Microsoft's Majorana 2 quantum computing chip switches to lead-based materials. Microsoft is accelerating its roadmap and expects a practical machine in 2029."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/routers/asus-unveils-its-first-wi-fi-8-router-rog-rapture-gt-bn98-pro-offers-up-to-2x-real-world-throughput-uplift-over-wi-fi-7",
    "domain": "AI 算力 / 半导体",
    "title": "Asus unveils its first Wi-Fi 8 router — ROG Rapture GT-BN98 Pro offers up to 2x real-world throughput uplift over Wi-Fi 7",
    "url": "https://www.tomshardware.com/networking/routers/asus-unveils-its-first-wi-fi-8-router-rog-rapture-gt-bn98-pro-offers-up-to-2x-real-world-throughput-uplift-over-wi-fi-7",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T18:52:45+00:00",
    "summary": "Wi-Fi 8 is aimed at improving real-world performance over Wi-Fi 7"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intels-next-gen-lga1954-socket-will-support-nova-lake-razor-lake-and-beyond-finally-an-intel-socket-that-outlives-its-cpus",
    "domain": "AI 算力 / 半导体",
    "title": "Intel’s next-gen LGA1954 socket will support Nova Lake, Razor Lake, and beyond — finally an Intel socket that outlives its CPUs",
    "url": "https://www.tomshardware.com/pc-components/cpus/intels-next-gen-lga1954-socket-will-support-nova-lake-razor-lake-and-beyond-finally-an-intel-socket-that-outlives-its-cpus",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T17:32:36+00:00",
    "summary": "Reputable Intel hardware leaker Jaykihn reveals new information about Intel's next-generation LGA1954 socket."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/mini-pcs/microsoft-debuts-surface-rtx-spark-dev-box-nvidia-powered-mini-pc-helps-devs-get-ready-for-an-agentic-windows",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft debuts Surface RTX Spark Dev Box — Nvidia-powered mini-PC helps devs get ready for an agentic Windows",
    "url": "https://www.tomshardware.com/desktops/mini-pcs/microsoft-debuts-surface-rtx-spark-dev-box-nvidia-powered-mini-pc-helps-devs-get-ready-for-an-agentic-windows",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T16:47:17+00:00",
    "summary": "At Microsoft Build, the company debuted its Surface RTX Spark Dev Box, a system for developers to come up with new AI applications."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/routers/msi-unveils-latest-set-of-wifi-7-gaming-routers-touting-ultra-fast-speeds-flagship-radix-be19000-model-comes-with-a-built-in-ssd-slot-for-nas-lite-experience-and-wireless-speeds-up-to-19-gbps",
    "domain": "AI 算力 / 半导体",
    "title": "MSI unveils latest set of WiFi 7 gaming routers touting ultra-fast speeds — flagship RadiXBE19000 model comes with a built-in SSD slot for 'NAS Lite' experience and wireless speeds up to 19 Gbps",
    "url": "https://www.tomshardware.com/networking/routers/msi-unveils-latest-set-of-wifi-7-gaming-routers-touting-ultra-fast-speeds-flagship-radix-be19000-model-comes-with-a-built-in-ssd-slot-for-nas-lite-experience-and-wireless-speeds-up-to-19-gbps",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T16:34:20+00:00",
    "summary": "MSI have revealed three new gaming routers with WiFi 7 support at Computex, with its flagship BE19000 model featuring a built-in SSD slot, eight antennas and a sci fi-esque translucent design."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/computex-2026-day-one-wrap-up-arm-makes-a-bold-play-for-windows-pcs-pcie-6-0-ssds-are-coming-asus-embraces-black-and-gold-for-rog-20th",
    "domain": "AI 算力 / 半导体",
    "title": "Computex 2026 Day One Wrap-Up: Arm makes a bold play for Windows PCs, PCIe 6.0 SSDs are coming, Asus embraces black and gold for ROG 20th",
    "url": "https://www.tomshardware.com/pc-components/cpus/computex-2026-day-one-wrap-up-arm-makes-a-bold-play-for-windows-pcs-pcie-6-0-ssds-are-coming-asus-embraces-black-and-gold-for-rog-20th",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T16:18:07+00:00",
    "summary": "Our team is on the ground in Taipei bringing you the latest from Computex 2026"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/power-supplies/cooler-master-shows-off-new-mwe-gold-v4-power-supplies-and-gpu-shield-adapter-per-pin-monitoring-can-dynamically-scale-down-power-to-stop-cables-melting",
    "domain": "AI 算力 / 半导体",
    "title": "Cooler Master shows off new MWE Gold V4 Power supplies and GPU Shield adapter — per-pin monitoring can dynamically scale down power to stop cables melting",
    "url": "https://www.tomshardware.com/pc-components/power-supplies/cooler-master-shows-off-new-mwe-gold-v4-power-supplies-and-gpu-shield-adapter-per-pin-monitoring-can-dynamically-scale-down-power-to-stop-cables-melting",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T15:59:56+00:00",
    "summary": "Cooler Master has new power supplies and a GPU Shield adapter on display at Computex."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/mainland-chinese-exhibitors-locked-out-of-computex-2026",
    "domain": "AI 算力 / 半导体",
    "title": "Mainland Chinese exhibitors reportedly locked out of Computex 2026, as Taiwan entry permits stall — parties complain applications left pending or hit with last-minute documentation requests",
    "url": "https://www.tomshardware.com/tech-industry/mainland-chinese-exhibitors-locked-out-of-computex-2026",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T15:43:37+00:00",
    "summary": "Mainland Chinese companies among the 219 listed mainland exhibitors at Computex 2026 in Taipei have been kept off the show floor by stalled entry permits."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-reportedly-no-longer-working-on-6-core-nova-lake-mobile-sku-alleges-new-rumor-wildcat-lake-refresh-to-become-focus-for-next-gen-budget-markets-instead",
    "domain": "AI 算力 / 半导体",
    "title": "Intel reportedly no longer working on 6-core Nova Lake mobile SKU, alleges new rumor — Wildcat Lake Refresh to become focus for next-gen budget markets instead",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-reportedly-no-longer-working-on-6-core-nova-lake-mobile-sku-alleges-new-rumor-wildcat-lake-refresh-to-become-focus-for-next-gen-budget-markets-instead",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T15:39:39+00:00",
    "summary": "Intel is still on schedule to at least announce Nova Lake at the end of the year, even if all rumors say the timelines have moved to next year. Apparently, the lowest-end 6-core Nova Lake mobile part "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-is-considering-a-potential-ryzen-5-9600x3d-company-says-six-core-zen-5-x3d-chip-maybe-something-we-look-at-doing-later-this-year",
    "domain": "AI 算力 / 半导体",
    "title": "AMD is considering a potential Ryzen 5 9600X3D — company says six-core Zen 5 X3D chip 'maybe something we look at doing... later this year'",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-is-considering-a-potential-ryzen-5-9600x3d-company-says-six-core-zen-5-x3d-chip-maybe-something-we-look-at-doing-later-this-year",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T15:00:00+00:00",
    "summary": "AMD says that six-core X3D chips don't make sense for a broad market for a number of reasons, but a six-core X3D chip with the Zen 5 architecture is something the company is considering."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cooling/cooler-master-shows-off-new-haf-500-chassis-aluminum-fans-and-new-air-coolers-new-v8-cooler-masterfan-anm-and-updated-silencio-600-and-haf-chassis-add-to-an-already-comprehensive-product-stack",
    "domain": "AI 算力 / 半导体",
    "title": "Cooler Master shows off new HAF II 500 chassis, aluminum fans, and new air coolers — New V8 Cooler, Masterfan A, and updated Silencio 600 and HAF chassis’ add to an already comprehensive product stack",
    "url": "https://www.tomshardware.com/pc-components/cooling/cooler-master-shows-off-new-haf-500-chassis-aluminum-fans-and-new-air-coolers-new-v8-cooler-masterfan-anm-and-updated-silencio-600-and-haf-chassis-add-to-an-already-comprehensive-product-stack",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T14:32:11+00:00",
    "summary": "Cooler Master had a lot of things to show off at Computex 2026."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/phison-shows-pcie-6-0-x3-ssd-controller-with-28-gb-s-of-bandwidth-and-6-8-million-iops-supports-2-petabytes-per-drive-also-new-power-sipping-e37t-ssds-for-pcie-5-0-systems-consume-a-mere-4-5w",
    "domain": "AI 算力 / 半导体",
    "title": "Phison shows PCIe 6.0 X3 SSD controller with 28 GB/s of bandwidth and 6.8 million IOPS, supports 2 petabytes per drive— also new power-sipping E37T SSDs for PCIe 5.0 systems consume a mere 4.5W",
    "url": "https://www.tomshardware.com/pc-components/ssds/phison-shows-pcie-6-0-x3-ssd-controller-with-28-gb-s-of-bandwidth-and-6-8-million-iops-supports-2-petabytes-per-drive-also-new-power-sipping-e37t-ssds-for-pcie-5-0-systems-consume-a-mere-4-5w",
    "source": "Paul Alcorn",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T13:54:22+00:00",
    "summary": "Phison's booth at Computex 2026 had its new PCIe 6.0 SSD controller, dubbed the X3, on display, with claims of up to 28 GB/s of sequential throughput and 6.8 million IOPS in random read/write workload"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/intel-xeon-6-plus-roundtable-transcript-computex-2026",
    "domain": "AI 算力 / 半导体",
    "title": "Intel Xeon 6+ Computex roundtable interview transcript — Kira Boyko and Tim Wilson on 18A wafer allocation, Clearwater Forest, and dropping hyper-threading",
    "url": "https://www.tomshardware.com/tech-industry/intel-xeon-6-plus-roundtable-transcript-computex-2026",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T12:24:32+00:00",
    "summary": "Intel launched its Xeon 6+ processors at Computex, and on Monday, two of the individuals responsible for the product sat down with the press to answer questions."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/bernie-sanders-pushes-for-50-percent-public-ownership-of-american-ai-companies-proposes-ai-sovereign-wealth-fund-that-would-hold-direct-ownership-stakes-in-largest-ai-firms",
    "domain": "AI 算力 / 半导体",
    "title": "Bernie Sanders pushes for 50% public ownership of American AI companies — proposes AI sovereign wealth fund that would hold direct ownership stakes in largest AI firms",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/bernie-sanders-pushes-for-50-percent-public-ownership-of-american-ai-companies-proposes-ai-sovereign-wealth-fund-that-would-hold-direct-ownership-stakes-in-largest-ai-firms",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T12:15:57+00:00",
    "summary": "The U.S. Senator is arguing that since AI companies use public data to generate a lot of revenue, the public should benefit from it as well. He also said that the people should have a say in the direc"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/grab-this-rtx-5070-gaming-pc-with-a-7800x3d-from-cyberpowerpc-for-under-usd1-960-right-now-exclusive-discount-available-on-4k-ready-pre-built-rig-with-32gb-ddr5-and-1tb-ssd-that-knocks-usd210-off",
    "domain": "AI 算力 / 半导体",
    "title": "Grab this RTX 5070 gaming PC with a 7800X3D from CyberPowerPC for under $1,960 right now — exclusive discount available on 4K-ready pre-built rig with 32GB DDR5 and 1TB SSD that knocks $210 off",
    "url": "https://www.tomshardware.com/pc-components/grab-this-rtx-5070-gaming-pc-with-a-7800x3d-from-cyberpowerpc-for-under-usd1-960-right-now-exclusive-discount-available-on-4k-ready-pre-built-rig-with-32gb-ddr5-and-1tb-ssd-that-knocks-usd210-off",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T11:35:57+00:00",
    "summary": "Save $210 on this powerful CyberPowerPC gaming rig, powered by the AMD Ryzen 7 7800X3D and the all-impressive RTX 5070, alongside a 1TB SSD and 32GB of DDR5 RAM, all for just $1,959.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gigabyte-showcases-new-infinity-products-for-its-40th-anniversary-the-x870-infinity-next-halo-motherboard-boasts-metal-3d-printed-elements-aero-wood-goes-dark-microatx-stealth-boards-infinity-style-gpus-extend-down-the-product-stack",
    "domain": "AI 算力 / 半导体",
    "title": "Gigabyte showcases new Infinity products for its 40th anniversary — X870 Infinity Next halo motherboard boasts metal 3D-printed elements, Aero Wood goes dark, MicroATX Stealth boards, Infinity-style G",
    "url": "https://www.tomshardware.com/pc-components/gigabyte-showcases-new-infinity-products-for-its-40th-anniversary-the-x870-infinity-next-halo-motherboard-boasts-metal-3d-printed-elements-aero-wood-goes-dark-microatx-stealth-boards-infinity-style-gpus-extend-down-the-product-stack",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T11:30:00+00:00",
    "summary": "Gigabyte showcases stunning new Infinity products for its 40th anniversary"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/sk-hynix-to-double-memory-wafer-capacity-over-five-years",
    "domain": "AI 算力 / 半导体",
    "title": "SK hynix to double memory wafer capacity within five years, chairman says — AI-driven shortage will persist until at least 2030",
    "url": "https://www.tomshardware.com/pc-components/dram/sk-hynix-to-double-memory-wafer-capacity-over-five-years",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T11:25:00+00:00",
    "summary": "SK hynix will double its memory wafer capacity within five years, SK Group chairman Chey Tae-won told reporters at Computex in Taipei on June 2nd."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/jensen-huang-says-nvidia-wants-to-reinvent-the-single-most-important-tool-of-humanity-with-rtx-spark-nvidia-ceo-touts-support-of-literally-every-computer-maker-in-the-world-for-its-agentic-ai-pc-platform",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang says Nvidia wants to 'reinvent the single most important tool of humanity' with RTX Spark — Nvidia CEO touts support of 'literally every computer maker in the world' for its agentic AI PC",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/jensen-huang-says-nvidia-wants-to-reinvent-the-single-most-important-tool-of-humanity-with-rtx-spark-nvidia-ceo-touts-support-of-literally-every-computer-maker-in-the-world-for-its-agentic-ai-pc-platform",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T11:20:00+00:00",
    "summary": "In a press Q&amp;A held at Computex 2026, Nvidia CEO Jensen Huang discussed why the company is entering the PC market now and its ambitions for the future of computing."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/toms-hardware-unfiltered-computex-2026-day-1-night-markets-taking-the-mrt-train-and-a-slew-of-demos",
    "domain": "AI 算力 / 半导体",
    "title": "Tom's Hardware Unfiltered: Computex 2026, Day 1 — night markets, taking the MRT train, and a slew of demos",
    "url": "https://www.tomshardware.com/tech-industry/toms-hardware-unfiltered-computex-2026-day-1-night-markets-taking-the-mrt-train-and-a-slew-of-demos",
    "source": "Paul Alcorn",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T11:06:04+00:00",
    "summary": "The Tom's Hardware team in Taipei reports back on what they've been up to as Computex 2026 begins to gather momentum. Take a look at how we're making"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones-to-protect-undersea-cables-from-russian-sabotage-touted-in-new-defense-pact-us-one-of-three-partners-developing-new-tech-to-protect-usd1-8-trillion-in-daily-transactions",
    "domain": "AI 算力 / 半导体",
    "title": "Drones to protect undersea cables from Russian sabotage touted in new defense pact — US one of three partners developing new tech to protect $1.8 trillion in daily transactions",
    "url": "https://www.tomshardware.com/tech-industry/drones-to-protect-undersea-cables-from-russian-sabotage-touted-in-new-defense-pact-us-one-of-three-partners-developing-new-tech-to-protect-usd1-8-trillion-in-daily-transactions",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T11:00:00+00:00",
    "summary": "The Australian, UK, and U.S. governments just announced a cooperation to develop new technologies to protect underwater cables. The move comes after recent incidents of damages to undersea cables acro"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/take-home-gigabytes-aero-x16-gaming-laptop-for-just-usd1-389-99-and-save-usd610-packed-with-32gb-of-ram-and-a-powerful-rtx-5070-gpu",
    "domain": "AI 算力 / 半导体",
    "title": "Take home Gigabyte's Aero X16 gaming laptop for just $1,389.99 and save $610 — packed with 32GB of RAM and a powerful RTX 5070 GPU",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/take-home-gigabytes-aero-x16-gaming-laptop-for-just-usd1-389-99-and-save-usd610-packed-with-32gb-of-ram-and-a-powerful-rtx-5070-gpu",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T10:56:16+00:00",
    "summary": "Gigabyte's Aero X16 packs 32GB of RAM, a 1TB SSD, and a powerful Nvidia RTX 5070 GPU all for $1389.99 in this Best Buy deal."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-had-to-re-engineer-the-ryzen-7-5800x3d-for-a-re-release-10th-anniversary-edition-chip-had-a-whole-body-of-engineering-work-put-into-it",
    "domain": "AI 算力 / 半导体",
    "title": "AMD ‘had to re-engineer’ the Ryzen 7 5800X3D for a re-release — 10th Anniversary Edition chip had ‘a whole body of engineering work’ put into it",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-had-to-re-engineer-the-ryzen-7-5800x3d-for-a-re-release-10th-anniversary-edition-chip-had-a-whole-body-of-engineering-work-put-into-it",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T10:41:03+00:00",
    "summary": "AMD just reintroduced the Ryzen 7 5800X3D, but it wasn't as simple as spinning up the old manufacturing process, as the original bonding method TSMC used was no longer available."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-arc-g3-interview-transcript-intels-senior-product-director-talks-new-handheld-chips-arrow-lake-refresh-and-rtx-spark",
    "domain": "AI 算力 / 半导体",
    "title": "Intel Arc G3 interview transcript — Intel's Senior Product Director talks new handheld chips, Arrow Lake Refresh, and RTX Spark",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-arc-g3-interview-transcript-intels-senior-product-director-talks-new-handheld-chips-arrow-lake-refresh-and-rtx-spark",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T10:30:00+00:00",
    "summary": "Intel's Nish Neelalojanan spoke to us at Computex 2026 about Intel's new G3 chip line, how it impacts the burgeoning handheld gaming market, and how Intel is responding to rising chip and memory price"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/frore-systems-solid-state-airjet-mini-cools-intels-wildcat-lake-laptop-reference-design-15w-of-sustained-fanless-cooling-helps-macbook-neo-competitor-reach-a-svelte-11-3-mm-remain-silent",
    "domain": "AI 算力 / 半导体",
    "title": "Frore System’s solid-state AirJet Mini cools Intel’s Wildcat Lake laptop reference design – 15W of sustained, fanless cooling helps MacBook Neo competitor reach a svelte 11.3 mm, remain silent",
    "url": "https://www.tomshardware.com/laptops/frore-systems-solid-state-airjet-mini-cools-intels-wildcat-lake-laptop-reference-design-15w-of-sustained-fanless-cooling-helps-macbook-neo-competitor-reach-a-svelte-11-3-mm-remain-silent",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T10:10:00+00:00",
    "summary": "Frore has worked with Intel to feature its AirJet solid-state cooling chip inside its much-hyped Wildcat Lake reference laptop. These laptops will need to stay slim, quiet, and affordable if they want"
  },
  {
    "id": "rss:https://www.tomshardware.com/speakers/teens-bluetooth-speaker-named-bomb-caused-a-10-hour-delay-on-flight-from-newark-to-spain-passenger-reported-concerns-to-flight-attendant-at-32-000-feet-forcing-plane-back-to-the-us",
    "domain": "AI 算力 / 半导体",
    "title": "Teen’s Bluetooth speaker named ‘BOMB’ caused a 10-hour delay on flight from Newark to Spain — passenger reported concerns to flight attendant at 32,000 feet, forcing plane back to the US",
    "url": "https://www.tomshardware.com/speakers/teens-bluetooth-speaker-named-bomb-caused-a-10-hour-delay-on-flight-from-newark-to-spain-passenger-reported-concerns-to-flight-attendant-at-32-000-feet-forcing-plane-back-to-the-us",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T10:00:00+00:00",
    "summary": "Passengers on United Airlines flight UA236 on Saturday were subjected to deplaning, TSA rescreening, and over 10 hours of delays thanks to a teen foolishly naming their Bluetooth speaker 'BOMB.'"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-says-something-has-to-give-with-memory-prices-company-says-it-will-continue-to-make-sure-that-there-are-products-which-can-take-care-of-older-memory-technologies",
    "domain": "AI 算力 / 半导体",
    "title": "Intel says 'something has to give' with memory prices — company says it 'will continue to make sure that there are products which can take care of older memory technologies'",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-says-something-has-to-give-with-memory-prices-company-says-it-will-continue-to-make-sure-that-there-are-products-which-can-take-care-of-older-memory-technologies",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T09:30:00+00:00",
    "summary": "Intel sat down with Tom's Hardware at Computex 2026, and the company says it recognizes the importance of Raptor Lake and DDR4 platforms as the memory crunch continues."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/chinese-military-has-been-acquiring-nvidia-chips-even-post-washington-export-controls-research-claims-multiple-institutions-linked-to-the-pla-asked-for-nvidia-ai-chips-according-to-publicly-available-documents",
    "domain": "AI 算力 / 半导体",
    "title": "Chinese military has been acquiring Nvidia chips, even post-Washington export controls, research claims — multiple institutions linked to the PLA asked for Nvidia AI chips, according to publicly avail",
    "url": "https://www.tomshardware.com/tech-industry/chinese-military-has-been-acquiring-nvidia-chips-even-post-washington-export-controls-research-claims-multiple-institutions-linked-to-the-pla-asked-for-nvidia-ai-chips-according-to-publicly-available-documents",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T09:00:00+00:00",
    "summary": "A business-intelligence researcher said that the Chinese military has been actively acquiring Nvidia AI chips, even after the U.S. put export controls on them. Public documents show that some institut"
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
    "points": 108,
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
    "id": "hn:48029334",
    "domain": "大厂 AI 动态",
    "title": "Zuckerberg 'personally authorized' Meta's copyright infringement, publishers say",
    "url": "https://apnews.com/article/meta-mark-zuckerberg-ai-publishers-lawsuit-llama-5609846d4d840014974a847b01079c32",
    "source": "jethronethro",
    "platform": "hackernews",
    "points": 156,
    "published_at": "2026-05-05T22:07:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:48364983",
    "domain": "大厂 AI 动态",
    "title": "Angry devs vow to flee GitHub Copilot as metered billing takes hold",
    "url": "https://www.theregister.com/ai-and-ml/2026/06/02/github-copilot-users-threaten-exit-as-metered-billing-kicks-in/5249826",
    "source": "jay_kyburz",
    "platform": "hackernews",
    "points": 49,
    "published_at": "2026-06-02T01:55:07+00:00",
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
    "id": "hn:48221976",
    "domain": "大厂 AI 动态",
    "title": "Gemini randomly dumped its system prompt",
    "url": "https://gist.github.com/mkaramuk/44a44d83178e632ec0dd1f02186d822c",
    "source": "mkaramuk",
    "platform": "hackernews",
    "points": 94,
    "published_at": "2026-05-21T13:04:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:48029753",
    "domain": "大厂 AI 动态",
    "title": "Xbox CEO ends Copilot AI development and overhauls leadership",
    "url": "https://www.dexerto.com/gaming/xbox-ceo-ends-copilot-ai-development-overhauls-leadership-3361353/",
    "source": "gmays",
    "platform": "hackernews",
    "points": 113,
    "published_at": "2026-05-05T22:43:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:48031707",
    "domain": "大厂 AI 动态",
    "title": "Update on \"Co-authored-by: Copilot\" in commit messages",
    "url": "https://github.com/microsoft/vscode/issues/314311",
    "source": "extesy",
    "platform": "hackernews",
    "points": 102,
    "published_at": "2026-05-06T03:15:05+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/941516/god-of-war-laufey-ps5-trailer",
    "domain": "大厂 AI 动态",
    "title": "God of War Laufey is coming to the PS5",
    "url": "https://www.theverge.com/entertainment/941516/god-of-war-laufey-ps5-trailer",
    "source": "Andrew Webster",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T22:16:08+00:00",
    "summary": "Sony ended its big State of Play showcase with a major reveal: the next God of War. The new title is called God of War Laufey, and is once again developed by Sony's Santa Monica Studio. Currently, the"
  },
  {
    "id": "rss:https://www.theverge.com/games/942113/remedy-control-resonant-release-date-trailer",
    "domain": "大厂 AI 动态",
    "title": "Remedy’s Control sequel launches in September",
    "url": "https://www.theverge.com/games/942113/remedy-control-resonant-release-date-trailer",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T21:55:32+00:00",
    "summary": "Control Resonant, the upcoming sequel to Remedy Entertainment's Control, will be released on September 24th, 2026, according to a trailer that premiered during Tuesday's PlayStation State of Play show"
  },
  {
    "id": "rss:https://www.theverge.com/games/939378/marvels-wolverine-playstation-trailer-state-of-play-june-2026",
    "domain": "大厂 AI 动态",
    "title": "Here&#8217;s seven bloody minutes of Wolverine on the PS5",
    "url": "https://www.theverge.com/games/939378/marvels-wolverine-playstation-trailer-state-of-play-june-2026",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T21:11:46+00:00",
    "summary": "At its big State of Play show on Tuesday, Sony shared new look Marvel's Wolverine, the next big title from Insomniac Games that's launching exclusively on PS5 on September 15th. Dressed in the iconic "
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/940913/playstation-state-of-play-june-2026-news-trailers",
    "domain": "大厂 AI 动态",
    "title": "PlayStation State of Play June 2026: All the news and trailers",
    "url": "https://www.theverge.com/entertainment/940913/playstation-state-of-play-june-2026-news-trailers",
    "source": "Andrew Webster",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T20:40:00+00:00",
    "summary": "While the majority of Summer Game Fest takes place over the weekend, Sony is getting a jump on things with its next State of Play showcase, which airs on June 2nd at 5PM ET. It&#8217;s coming at a piv"
  },
  {
    "id": "rss:https://www.theverge.com/games/941360/intel-arc-g3-extreme-msi-claw-next-gen-handheld-preview",
    "domain": "大厂 AI 动态",
    "title": "I held the next-gen handheld",
    "url": "https://www.theverge.com/games/941360/intel-arc-g3-extreme-msi-claw-next-gen-handheld-preview",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T19:56:02+00:00",
    "summary": "Intel couldn't catch a break. Layoffs. Shakedowns. Crashing CPUs torpedoing its reputation, sending desktop gamers fleeing to AMD. Apple and Qualcomm pushing Intel out of multiple flagship laptops. A "
  },
  {
    "id": "rss:https://www.theverge.com/tech/941738/microsoft-build-2026-biggest-announcements",
    "domain": "大厂 AI 动态",
    "title": "Microsoft Build 2026: The 7 biggest announcements",
    "url": "https://www.theverge.com/tech/941738/microsoft-build-2026-biggest-announcements",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T19:23:52+00:00",
    "summary": "Microsoft just kicked off Build 2026 with a keynote from CEO Satya Nadella and other company leaders. As expected, it was filled with announcements, ranging from new Surface hardware to an always-on p"
  },
  {
    "id": "rss:https://www.theverge.com/policy/941775/trump-ai-executive-order",
    "domain": "大厂 AI 动态",
    "title": "Trump signs executive order to review AI models before they’re released",
    "url": "https://www.theverge.com/policy/941775/trump-ai-executive-order",
    "source": "Lauren Feiner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T18:33:42+00:00",
    "summary": "President Donald Trump signed an executive order Tuesday creating a \"voluntary framework\" for AI companies to share their frontier models with the federal government before they're released \"to promot"
  },
  {
    "id": "rss:https://www.theverge.com/news/940874/microsoft-majorana-2-quantum-chip-build",
    "domain": "大厂 AI 动态",
    "title": "Microsoft’s next-gen quantum chip cuts timeline to useful quantum computing",
    "url": "https://www.theverge.com/news/940874/microsoft-majorana-2-quantum-chip-build",
    "source": "Tom Warren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T18:15:00+00:00",
    "summary": "Microsoft claimed last year that it had made a key breakthrough in quantum computing with Majorana 1, the company's first quantum processor. While physicists were immediately skeptical of Microsoft's "
  },
  {
    "id": "rss:https://www.theverge.com/tech/941664/microsoft-ai-model-reasoning-mai-thinking-1-build-2026",
    "domain": "大厂 AI 动态",
    "title": "Microsoft’s first advanced reasoning AI is here",
    "url": "https://www.theverge.com/tech/941664/microsoft-ai-model-reasoning-mai-thinking-1-build-2026",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T18:12:44+00:00",
    "summary": "Microsoft announced a bunch of new in-house AI models at Build 2026, including a new \"flagship\" model: MAI-Thinking-1. It's an ambitious step into model development for Microsoft, which introduced its"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/941763/ultimate-ears-wonderboom-fractal-design-scape-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "The durable, floatable UE Wonderboom 4 speaker is cheaper than ever",
    "url": "https://www.theverge.com/gadgets/941763/ultimate-ears-wonderboom-fractal-design-scape-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T18:05:35+00:00",
    "summary": "I like the UE Wonderboom 4 Bluetooth speaker so much that I bought two of them, though I wish I could have paid less for them. Fortunately, you can stock up on the cheap, so long as you like the color"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/02/squishmallows-dentures-and-an-i-heart-hot-dads-bag-uber-has-found-thousands-of-items-left-in-robotaxis/",
    "domain": "大厂 AI 动态",
    "title": "Squishmallows, dentures, and an ‘I Heart Hot Dads’ bag: Uber has found thousands of items left in robotaxis",
    "url": "https://techcrunch.com/2026/06/02/squishmallows-dentures-and-an-i-heart-hot-dads-bag-uber-has-found-thousands-of-items-left-in-robotaxis/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T23:25:20+00:00",
    "summary": "Even in a future of robot taxis, someone still has to return the things passengers leave behind."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/02/cyera-eyes-12b-valuation-at-80x-arr-multiple-despite-operating-losses/",
    "domain": "大厂 AI 动态",
    "title": "Cyera eyes $12B valuation at 80x ARR multiple despite operating losses",
    "url": "https://techcrunch.com/2026/06/02/cyera-eyes-12b-valuation-at-80x-arr-multiple-despite-operating-losses/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T22:50:56+00:00",
    "summary": "The cybersecurity company is nearing a $300 million round led by Evolution Equity Partners."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/02/cyberdeck-tiktok-trend-reject-big-tech/",
    "domain": "大厂 AI 动态",
    "title": "Cyberdecks are having a moment, rejecting big tech surveillance with style and substance",
    "url": "https://techcrunch.com/2026/06/02/cyberdeck-tiktok-trend-reject-big-tech/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T20:20:00+00:00",
    "summary": "Over the last few months, these DIY hardware communities have exploded in popularity as people on social media show off their solar-powered game emulators, pocket-sized ereaders, and clamshell purse c"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/02/uber-caps-employee-ai-spending-after-blowing-through-budget-in-four-months/",
    "domain": "大厂 AI 动态",
    "title": "Uber caps employee AI spending after blowing through budget in 4 months",
    "url": "https://techcrunch.com/2026/06/02/uber-caps-employee-ai-spending-after-blowing-through-budget-in-four-months/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T19:11:48+00:00",
    "summary": "Uber's cutback has occurred after the company had reportedly encouraged staff to use AI as much as possible."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/02/new-microsoft-tool-lets-devs-spin-up-ai-behavior-tests-using-text-descriptions/",
    "domain": "大厂 AI 动态",
    "title": "New Microsoft tool lets devs spin up AI behavior tests using text descriptions",
    "url": "https://techcrunch.com/2026/06/02/new-microsoft-tool-lets-devs-spin-up-ai-behavior-tests-using-text-descriptions/",
    "source": "Ram Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T19:02:21+00:00",
    "summary": "Microsoft on Tuesday took the wraps off Adaptive Spec-driven Scoring for Evaluation and Regression Testing, an open source framework for spinning up AI evaluations."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/02/a-startup-everand-is-now-bundling-ebooks-audiobooks-and-book-clubs-in-challenge-to-amazon/",
    "domain": "大厂 AI 动态",
    "title": "A startup, Everand, is now bundling e-books, audiobooks, and book clubs in challenge to Amazon",
    "url": "https://techcrunch.com/2026/06/02/a-startup-everand-is-now-bundling-ebooks-audiobooks-and-book-clubs-in-challenge-to-amazon/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T18:31:22+00:00",
    "summary": "A new reading subscription from Everand offers access to both e-books and audiobooks, and Fable's book club community."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/02/martin-scorsese-becomes-the-latest-and-most-unlikely-hollywood-voice-for-ai/",
    "domain": "大厂 AI 动态",
    "title": "Martin Scorsese becomes the latest — and most unlikely — Hollywood voice for AI",
    "url": "https://techcrunch.com/2026/06/02/martin-scorsese-becomes-the-latest-and-most-unlikely-hollywood-voice-for-ai/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T18:16:53+00:00",
    "summary": "The caveat is that one of the world's most famous living directors is using the tech solely for storyboarding."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/02/microsoft-launches-scout-an-openclaw-inspired-personal-assistant/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft launches Scout, an OpenClaw-inspired personal assistant",
    "url": "https://techcrunch.com/2026/06/02/microsoft-launches-scout-an-openclaw-inspired-personal-assistant/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T18:02:44+00:00",
    "summary": "Launched at Build, Microsoft Scout is a new AI assistant meant to bring the power and flexibility of OpenClaw into the Microsoft 365 system."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/02/ex-anduril-engineer-raises-42m-to-build-the-amazon-of-composite-parts/",
    "domain": "大厂 AI 动态",
    "title": "Ex-Anduril engineer raises $42M to build the Amazon of composite parts",
    "url": "https://techcrunch.com/2026/06/02/ex-anduril-engineer-raises-42m-to-build-the-amazon-of-composite-parts/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T18:00:00+00:00",
    "summary": "Layup Parts co-founder Zack Eakin has drawn on a motorsports background, and his experience working for Palmer Luckey and Elon Musk, to tackle making faster, cheaper, and better composites."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/02/google-rolls-out-fake-call-detection-to-protect-against-ai-deepfake-impersonation-scams/",
    "domain": "大厂 AI 动态",
    "title": "Google rolls out fake call detection to protect against AI deepfake impersonation scams",
    "url": "https://techcrunch.com/2026/06/02/google-rolls-out-fake-call-detection-to-protect-against-ai-deepfake-impersonation-scams/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T18:00:00+00:00",
    "summary": "As people increasingly refuse to answer calls from unknown numbers, scammers are shifting their tactics by spoofing trusted phone numbers and using AI deepfake technology to sound like authority figur"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/02/microsoft-offers-devs-a-better-way-to-control-ai-agent-behavior/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft offers devs a better way to control AI agent behavior",
    "url": "https://techcrunch.com/2026/06/02/microsoft-offers-devs-a-better-way-to-control-ai-agent-behavior/",
    "source": "Ram Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T18:00:00+00:00",
    "summary": "The specification lets developer, compliance, and security teams define their own policies for agents to follow in portable policy files."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/02/amazon-faces-class-action-lawsuit-over-ring-facial-recognition-feature/",
    "domain": "大厂 AI 动态",
    "title": "Amazon faces class action lawsuit over Ring facial-recognition feature",
    "url": "https://techcrunch.com/2026/06/02/amazon-faces-class-action-lawsuit-over-ring-facial-recognition-feature/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T17:47:28+00:00",
    "summary": "The class action lawsuit, filed in Seattle by Virginia resident Charles Sigwalt, claims that Ring's Familiar Faces feature stores images of passersby without consent."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/02/focused-energy-raises-whopping-240m-series-a-for-laser-powered-fusion-tech/",
    "domain": "大厂 AI 动态",
    "title": "Focused Energy raises whopping $240M Series A for laser-powered fusion tech",
    "url": "https://techcrunch.com/2026/06/02/focused-energy-raises-whopping-240m-series-a-for-laser-powered-fusion-tech/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T17:01:17+00:00",
    "summary": "Another fusion startup has raised another a massive round to make this type of power a reality."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/02/trump-signs-narrower-executive-order-on-ai-oversight-after-industry-objections/",
    "domain": "大厂 AI 动态",
    "title": "Trump signs narrower executive order on AI oversight after industry objections",
    "url": "https://techcrunch.com/2026/06/02/trump-signs-narrower-executive-order-on-ai-oversight-after-industry-objections/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T16:23:08+00:00",
    "summary": "After industry objections, President Trump signed a revised AI executive order requiring only voluntary prerelease government reviews of advanced models."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/02/openai-launches-new-codex-tools-for-white-collar-work/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI launches new Codex tools for white-collar work",
    "url": "https://techcrunch.com/2026/06/02/openai-launches-new-codex-tools-for-white-collar-work/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T16:00:00+00:00",
    "summary": "OpenAI released a set of six plug-ins aimed at specific jobs: data analytics, creative production, sales, product design, equity investing, and investment banking. Available from within the Codex app,"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/02/board-the-new-game-startup-from-mirror-founder-brynn-putnam-raises-20m-has-already-sold-thousands/",
    "domain": "大厂 AI 动态",
    "title": "Board, the new game startup from Mirror founder Brynn Putnam, raises $20M, has already sold thousands",
    "url": "https://techcrunch.com/2026/06/02/board-the-new-game-startup-from-mirror-founder-brynn-putnam-raises-20m-has-already-sold-thousands/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T15:56:08+00:00",
    "summary": "Board, the startup building what it calls \"together tech\" designed to bring people into the same room, has closed a Series A led by Union Square Ventures."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/02/password-manager-dashlane-says-hackers-stole-some-customers-password-vaults/",
    "domain": "大厂 AI 动态",
    "title": "Password manager Dashlane says hackers stole some customers’ password vaults",
    "url": "https://techcrunch.com/2026/06/02/password-manager-dashlane-says-hackers-stole-some-customers-password-vaults/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T15:40:11+00:00",
    "summary": "The password manager giant said hackers were able to \"brute-force\" its two-factor system, allowing them to access customer accounts and download their password vaults."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/02/why-vivatech-2026-is-the-place-to-see-europes-ai-strategy-take-shape/",
    "domain": "大厂 AI 动态",
    "title": "Why VivaTech 2026 is the place to see Europe’s AI strategy take shape",
    "url": "https://techcrunch.com/2026/06/02/why-vivatech-2026-is-the-place-to-see-europes-ai-strategy-take-shape/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T15:05:00+00:00",
    "summary": "TechCrunch is partnering with VivaTech 2026 to spotlight some of the most important conversations shaping the future of artificial intelligence. Join us in Paris June 17-20!"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/02/meta-tests-series-for-episodic-reels-on-instagram-and-facebook/",
    "domain": "大厂 AI 动态",
    "title": "Meta tests ‘Series’ for episodic Reels on Instagram and Facebook",
    "url": "https://techcrunch.com/2026/06/02/meta-tests-series-for-episodic-reels-on-instagram-and-facebook/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T15:00:00+00:00",
    "summary": "Meta told TechCrunch that it's considering ways to monetize the new feature, but didn't share specifics on what that could look like."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/02/x-caters-to-creators-with-new-react-with-video-feature/",
    "domain": "大厂 AI 动态",
    "title": "X caters to creators with new ‘React with Video’ feature",
    "url": "https://techcrunch.com/2026/06/02/x-caters-to-creators-with-new-react-with-video-feature/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T14:46:28+00:00",
    "summary": "X will now let you 'react with video' to posts."
  },
  {
    "id": "rss:https://stratechery.com/2026/the-google-capital-company/",
    "domain": "大厂 AI 动态",
    "title": "The Google Capital Company",
    "url": "https://stratechery.com/2026/the-google-capital-company/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-02T10:00:00+00:00",
    "summary": "Google has issued equity to Berkshire Hathaway in a deal that signals far more demand and a future where capital is the ultimate commodity."
  },
  {
    "id": "rss:https://stratechery.com/2026/youtubers-win-the-box-office-goodbye-gatekeepers-the-youtube-bar/",
    "domain": "大厂 AI 动态",
    "title": "YouTubers Win the Box Office, Goodbye Gatekeepers, The YouTube Bar",
    "url": "https://stratechery.com/2026/youtubers-win-the-box-office-goodbye-gatekeepers-the-youtube-bar/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T10:00:00+00:00",
    "summary": "YouTubers are ruling the box office, and it shouldn't be a surprise: succeeding on YouTube is a much higher bar than the gates that currently govern Hollywood."
  },
  {
    "id": "hn:48373909",
    "domain": "股票",
    "title": "Morningstar values SpaceX at $780B, half its IPO target",
    "url": "https://www.reuters.com/business/media-telecom/morningstar-values-spacex-780-billion-half-its-ipo-target-2026-06-02/",
    "source": "berkeleyjunk",
    "platform": "hackernews",
    "points": 198,
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
    "points": 235,
    "published_at": "2026-05-28T19:43:14+00:00",
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
    "id": "hn:48369063",
    "domain": "股票",
    "title": "Elon Musk Laid Out 602 Goals. We Counted How Many He Hit",
    "url": "https://www.nytimes.com/interactive/2026/06/02/technology/elon-musk-promises-spacex-ipo.html",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-06-02T11:56:54+00:00",
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
    "id": "wscn:3773737",
    "domain": "股票",
    "title": "创业板冲高回落涨逾1.5%，算力硬件再爆发、“易中天”齐创新高，恒科指跌近3%，科网股集体下跌",
    "url": "https://wallstreetcn.com/articles/3773737",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T08:16:07+00:00",
    "summary": "盘面上，个股跌多涨少，沪深京三市超3700股飘绿，今日成交3.15万亿。沪深两市成交额3.13万亿，较上一个交易日放量近3400亿。板块方面，半导体、算力硬件产业链再度爆发，CPO、超硬材料方向领涨；工业金属、光刻机、存储器、商业航天题材活跃；煤炭、电力、油气板块走强。AI应用、短剧游戏、电商概念股调整。"
  },
  {
    "id": "wscn:3773770",
    "domain": "股票",
    "title": "美国计划对60个经济体加征关税，中方表态",
    "url": "https://wallstreetcn.com/articles/3773770",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T07:59:04+00:00",
    "summary": "针对美国贸易代表办公室计划以“未禁止进口强迫劳动产品”为由对60个经济体加征关税，外交部发言人毛宁表示，中方一贯反对各种形式的单边关税措施，关税战、贸易战不符合任何一方的利益，经贸问题应该在平等、尊重、互惠的基础上通过对话协商解决。她还表示，中国不存在所谓的“强迫劳动”，也反对以此为借口搞政治操弄。"
  },
  {
    "id": "wscn:3773763",
    "domain": "股票",
    "title": "错过二十年后终于出手，伯克希尔押注谷歌成为AI时代的“BNSF铁路公司”",
    "url": "https://wallstreetcn.com/articles/3773763",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T07:49:09+00:00",
    "summary": "巴菲特亲眼目睹谷歌商业奇迹却观望二十年，如今继任者Greg Abel用100亿美元打破沉默——以伯克希尔巨额现金复刻\"喜诗糖果供养BNSF铁路\"的经典逻辑，押注谷歌云成为AI时代的下一个现金引擎。当算力争夺白热化，谁的现金流最强，谁就赢得未来。"
  },
  {
    "id": "wscn:3773742",
    "domain": "股票",
    "title": "AI热情点燃股市，日经大涨3%再新高，日元160关口附近波动，油价涨超2%，比特币跌至6.7万美元",
    "url": "https://wallstreetcn.com/articles/3773742",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T07:44:30+00:00",
    "summary": "人工智能热潮推动股市攀升至历史新高，MSCI全球所有国家指数上涨0.1%创纪录。美股指期货基本持平，日经225指数盘中一度大涨3%创下新高。美元小幅走强，日元再度逼近160关口。同时，美国国务卿鲁比奥披露伊朗已在霍尔木兹海峡大范围布雷，布伦特原油升至97美元/桶，但市场整体情绪未被压垮。"
  },
  {
    "id": "wscn:3773767",
    "domain": "股票",
    "title": "日元短线跳涨，高市早苗：随时根据需要对汇率采取适当措施",
    "url": "https://wallstreetcn.com/articles/3773767",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T07:42:19+00:00",
    "summary": "更多消息，持续更新中"
  },
  {
    "id": "wscn:3773760",
    "domain": "股票",
    "title": "Perplexity：一个指标就能决定谁将赢得AI竞赛",
    "url": "https://wallstreetcn.com/articles/3773760",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T07:42:06+00:00",
    "summary": "AI竞赛的终极胜负手是“每瓦每用户token价值”？Perplexity CEO指出，能在单位能耗下创造最大经济价值的公司——即在准确性、延迟、成本、隐私与智能间取得最佳平衡者——将赢得最高估值。"
  },
  {
    "id": "wscn:3773765",
    "domain": "股票",
    "title": "OpenAI超级应用来了：Codex与ChatGPT合并，数周内上线",
    "url": "https://wallstreetcn.com/articles/3773765",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T07:38:46+00:00",
    "summary": "OpenAI领导层表示，合并的核心逻辑在于Codex在许多任务上的表现已优于ChatGPT——尤其是在处理长时间、多步骤任务以及调用外部工具方面。Codex拥有更优越的\"harness\"——即帮助AI智能体调用工具、代替用户执行操作的底层软件框架。分析称，此举旨在将Codex能力延伸至9亿消费端用户，冲刺IPO前扩大营收，同时应对Anthropic的激烈竞争。"
  },
  {
    "id": "wscn:3773761",
    "domain": "股票",
    "title": "顾全全正式告别字节seed，下一站或为AI制药",
    "url": "https://wallstreetcn.com/articles/3773761",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T07:05:42+00:00",
    "summary": "AI行业人才快速流动。"
  },
  {
    "id": "wscn:3773051",
    "domain": "股票",
    "title": "AI算力跨域互联激增：DCI与相干光通信革命爆发在即？",
    "url": "https://wallstreetcn.com/premium/articles/3773051?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T06:46:22+00:00",
    "summary": "预计2026年光传输设备市场全年增速预测从10%大幅上修至16%，预计年收入将首次自2000年以来突破180亿美元；2026年第一季度该市场同比飙升20%，DCI直采相关收入同比增长约40%。"
  },
  {
    "id": "wscn:3773754",
    "domain": "股票",
    "title": "如果把马斯克的财富具象化：每小时进账360万、身家超125个国家GDP、普通人需工作1100万年",
    "url": "https://wallstreetcn.com/articles/3773754",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T06:45:29+00:00",
    "summary": "马斯克净资产已达9700亿美元，距全球首位万亿富翁仅一步之遥。其财富折算下来每秒进账992美元，超越125个国家年度GDP，是洛克菲勒财富占比的两倍。而普通美国家庭若想与之比肩，需不间断工作逾1100万年。"
  },
  {
    "id": "wscn:3773758",
    "domain": "股票",
    "title": "Alphabet卖股800亿是个转折点？科技巨头AI融资从借债转向发股",
    "url": "https://wallstreetcn.com/articles/3773758",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T06:32:36+00:00",
    "summary": "AI军备竞赛烧钱逻辑正在转折：Alphabet宣布发行800亿美元股权为未来两年AI资本支出融资，或许标志科技巨头从大举举债转向出售股权。五大巨头2026年合计资本支出将近7500亿美元，现金流缺口持续扩大，微软、Meta、亚马逊或将被迫跟进，股权市场或面临融资洪峰。"
  },
  {
    "id": "wscn:3773756",
    "domain": "股票",
    "title": "韩股上看12000点、日经225年底冲70000点！华尔街大行批量看多日韩股市",
    "url": "https://wallstreetcn.com/articles/3773756",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T06:26:49+00:00",
    "summary": "高盛将韩国KOSPI指数目标大幅上调至12000点，较周二收盘价隐含约36%的上行空间，核心看好AI硬件投资带来的盈利超级周期；高盛与花旗亦看多日股，花旗预计日经225年底冲70000点，主要得益于企业盈利强劲、外资持续流入及股东回报创新高。"
  },
  {
    "id": "wscn:3773759",
    "domain": "股票",
    "title": "AI数据中心等不起电网，也等不起燃气轮机，SOFC从“备胎”变标配",
    "url": "https://wallstreetcn.com/articles/3773759",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T06:26:20+00:00",
    "summary": "国金证券认为，固体氧化物燃料电池（SOFC）已进入“从1到10”的规模化放量与业绩兑现期。凭借90天极速交付、55%~65%的高效能与近零排放，精准卡位AI数据中心供电缺口。SOFC正加速逼近燃气轮机平价拐点，Bloom Energy订单的爆发也正带动国内供应链企业集体受益。"
  },
  {
    "id": "wscn:3773755",
    "domain": "股票",
    "title": "2个月暴涨44%，美国软件股“杀回来”了！中国互联网是“亚太版IGV”吗？",
    "url": "https://wallstreetcn.com/articles/3773755",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T06:22:00+00:00",
    "summary": "美国软件股正上演二十五年来最强反弹，IGV期权与散户资金创纪录流入。与此同时，中国互联网板块大幅反弹引发“补涨”联想，摩根大通认为，一旦投资者接受类似叙事，其走势可能同样剧烈，但两者盈利趋势与商业模式存在本质差异，难以复制同类行情。"
  },
  {
    "id": "wscn:3773676",
    "domain": "股票",
    "title": "厄尔尼诺的深远影响：碳基通胀回归，硅基资产重估提前到来",
    "url": "https://wallstreetcn.com/articles/3773676",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T06:00:03+00:00",
    "summary": "浙商证券认为，2026年厄尔尼诺已基本确立，其影响或超越传统农产品定价逻辑。全球变暖导致雨带北移，棕榈油、铜等品种面临供给冲击；同时高温推升电力和数据中心成本，碳基资源涨价向AI产业链传导，或提前触发科技股估值重估，并加大美联储降息掣肘。"
  },
  {
    "id": "wscn:3773753",
    "domain": "股票",
    "title": "7800亿美元才是合理估值？SpaceX被丹麦基金拉进黑名单后，再遭重磅质疑",
    "url": "https://wallstreetcn.com/articles/3773753",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T05:56:42+00:00",
    "summary": "史上最大IPO冲刺在即，SpaceX却遭遇估值与治理的双面夹击：晨星给出7800亿美元公允价值，不足1.8万亿目标估值的一半；丹麦养老基金以治理\"灾难性\"为由将其拉黑，马斯克或掌控85%投票权。质疑声浪之下，SpaceX仍加速推进，募资最高750亿美元，承销费率创历史新低，最快6月12日纳斯达克挂牌。"
  },
  {
    "id": "wscn:3773713",
    "domain": "股票",
    "title": "当印钞机开始卖股票 美股近十年最大的托底力量正在反转",
    "url": "https://wallstreetcn.com/premium/articles/3773713?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T05:35:46+00:00",
    "summary": "供给侧的条件在松动。买盘的质量在下降。估值处在155年来第二高的位置。"
  },
  {
    "id": "wscn:3773751",
    "domain": "股票",
    "title": "报道：DeepSeek据悉在首轮融资中预计筹资约70亿美元，估值最高可达590亿美元",
    "url": "https://wallstreetcn.com/articles/3773751",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T05:24:53+00:00",
    "summary": "据报道，腾讯和宁德时代将成为DeepSeek最大的外部投资者，网易和京东也计划参与投资。"
  },
  {
    "id": "wscn:3773323",
    "domain": "股票",
    "title": "mSAP：M10如何引领PCB新材料迭代升级？",
    "url": "https://wallstreetcn.com/premium/articles/3773323?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T04:08:40+00:00",
    "summary": "随着AI算力架构由CoWoS向CoWoP升级，PCB产业链正经历一场技术与价值的双重跃迁。mSAP工艺已成为1.6T及以上光模块的必选，而M8-M10等级的高速CCL材料正成为行业竞争的制高点。"
  },
  {
    "id": "wscn:3773743",
    "domain": "股票",
    "title": "人民币多头情绪创15年新高，强势周期或延伸至年底",
    "url": "https://wallstreetcn.com/articles/3773743",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T04:08:26+00:00",
    "summary": "人民币多头情绪飙升至2011年以来峰值，离岸汇率徘徊逾三年高位，年内累涨超3%。估值洼地、科技出口强劲与人民币国际化三重驱动下，CIPS日均结算量创历史纪录。德意志银行喊价6.5，TS Lombard更激进预言破6.0。"
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
    "points": 43,
    "published_at": "2026-05-26T14:44:31+00:00",
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
    "id": "hn:48210908",
    "domain": "股票",
    "title": "OpenAI Is Preparing to File for an IPO in the Coming Days or Weeks",
    "url": "https://www.wsj.com/tech/ai/openai-ipo-filing-date-0ec95af5",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 36,
    "published_at": "2026-05-20T17:13:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:48227827",
    "domain": "股票",
    "title": "SpaceX's IPO Bagship carries full payload of Elon's mistakes",
    "url": "https://jamesthomason.com/spacex-ipo-bagship-carries-full-payload-of-elons-mistakes/",
    "source": "dollar",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-05-21T19:30:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:48205351",
    "domain": "股票",
    "title": "Cities: Skylines Uses a Stock-Market Analogy to Influence Gameplay",
    "url": "http://jkm.dev/posts/cities-skylines-trading-market/",
    "source": "birdculture",
    "platform": "hackernews",
    "points": 30,
    "published_at": "2026-05-20T09:55:02+00:00",
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
    "id": "hn:48261390",
    "domain": "股票",
    "title": "Show HN: My homelab is outperforming the stock market",
    "url": "https://stocks.sjer.red",
    "source": "shepherdjerred",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-05-24T21:54:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:48044444",
    "domain": "股票",
    "title": "SpaceX IPO gives Musk unchecked power and forbids investor lawsuits",
    "url": "https://arstechnica.com/tech-policy/2026/05/report-spacex-ipo-gives-musk-unchecked-power-and-forbids-investor-lawsuits/",
    "source": "pzxc",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-05-07T01:47:05+00:00",
    "summary": ""
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
    "id": "hn:48023533",
    "domain": "金融",
    "title": "Agents for financial services and insurance",
    "url": "https://www.anthropic.com/news/finance-agents",
    "source": "louiereederson",
    "platform": "hackernews",
    "points": 257,
    "published_at": "2026-05-05T15:05:47+00:00",
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
    "id": "hn:48371952",
    "domain": "金融",
    "title": "Amazon joins Microsoft in sending message to employees",
    "url": "https://finance.yahoo.com/sectors/technology/articles/amazon-joins-microsoft-sending-shocking-171700630.html",
    "source": "hereticles",
    "platform": "hackernews",
    "points": 26,
    "published_at": "2026-06-02T15:58:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:48364392",
    "domain": "金融",
    "title": "How to Silence the Federal Workforce",
    "url": "https://www.theatlantic.com/ideas/2026/06/trumps-intimidation-whistleblowers-nda/687377/",
    "source": "paulpauper",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-06-02T00:38:21+00:00",
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
    "id": "hn:48007503",
    "domain": "金融",
    "title": "Why Almost Everyone Loses–Except a Few Sharks–On Prediction Markets",
    "url": "https://www.wsj.com/finance/investing/polymarket-kalshi-betting-profits-prediction-markets-eb23ac11",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 104,
    "published_at": "2026-05-04T11:49:16+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.02945",
    "domain": "金融",
    "title": "Infinite Horizon Optimal Consumption: Intertemporal Hedging under Epstein-Zin Preferences",
    "url": "https://arxiv.org/abs/2606.02945",
    "source": "Erhan Bayraktar, Emmet Lawless",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T04:00:00+00:00",
    "summary": "arXiv:2606.02945v1 Announce Type: new Abstract: We study an infinite-horizon optimal consumption-investment problem for an investor with Epstein-Zin stochastic differential utility with stochastic inv"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.03153",
    "domain": "金融",
    "title": "Mind the Gap in the Mining Game",
    "url": "https://arxiv.org/abs/2606.03153",
    "source": "Kyoung-Kuk Kim, Donghwa Seo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T04:00:00+00:00",
    "summary": "arXiv:2606.03153v1 Announce Type: new Abstract: We analyze intentional block delays (mining gaps) in Proof-of-Work blockchain systems, where miners strategically balance mining rewards against operati"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.03158",
    "domain": "金融",
    "title": "Portfolio Choice with Competing Precautionary and Accumulation Goals",
    "url": "https://arxiv.org/abs/2606.03158",
    "source": "Steven Campbell, Agostino Capponi, Ananya Parashar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T04:00:00+00:00",
    "summary": "arXiv:2606.03158v1 Announce Type: new Abstract: We study optimal portfolio choice for a household simultaneously managing a random-deadline goal, such as a medical emergency or job loss, and a fixed-d"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.03184",
    "domain": "金融",
    "title": "FinStressTS: A Parametric Synthetic Benchmark for Time-Series Forecasting in Finance",
    "url": "https://arxiv.org/abs/2606.03184",
    "source": "Jiaze Sun, Kelvin J. L. Koa, Ruiyang Ni, Yize Liu, Haonan Chen, Ke-Wei Huang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T04:00:00+00:00",
    "summary": "arXiv:2606.03184v1 Announce Type: new Abstract: Financial forecasting is difficult due to low signal-to-noise ratios, latent factors, heavy tails, regime shifts, and jumps. Real-world benchmarks offer"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.03457",
    "domain": "金融",
    "title": "Hybrid News Sentiment Engine: Real-Time Market Analysis via Adaptive Ensemble Learning on News-Price Pairs",
    "url": "https://arxiv.org/abs/2606.03457",
    "source": "Andreas Aigner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T04:00:00+00:00",
    "summary": "arXiv:2606.03457v1 Announce Type: new Abstract: We present a hybrid news sentiment engine that continuously learns market sentiment from paired news headlines and concurrent asset-price snapshots with"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.03491",
    "domain": "金融",
    "title": "Reputation, Exposure, and Exit: Organizational Turnover after #MeToo",
    "url": "https://arxiv.org/abs/2606.03491",
    "source": "Roy Baharad, Asaf Eckstein, Gideon Parchomovsky, Rok Spruk",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T04:00:00+00:00",
    "summary": "arXiv:2606.03491v1 Announce Type: new Abstract: We study how economy-wide reputational shocks reshape corporate governance by examining board and executive turnover following the MeToo movement. We co"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.03763",
    "domain": "金融",
    "title": "Merit or networks? What decides where research is published",
    "url": "https://arxiv.org/abs/2606.03763",
    "source": "Ning Li",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T04:00:00+00:00",
    "summary": "arXiv:2606.03763v1 Announce Type: new Abstract: Does scientific publishing reward the quality of ideas or the advantage of connections? The question is universal to prestige-driven science, yet it has"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.03030",
    "domain": "金融",
    "title": "Do Matching Mechanisms Work with LLM Agents?",
    "url": "https://arxiv.org/abs/2606.03030",
    "source": "Yukihiro Hoshino, Ayato Kitadai, Nariaki Nishino",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T04:00:00+00:00",
    "summary": "arXiv:2606.03030v1 Announce Type: cross Abstract: This study examines whether standard matching mechanisms function as intended in LLM-agent markets, where LLM agents make allocation-related decisions"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.03548",
    "domain": "金融",
    "title": "Cost of Manipulation in AMM-Based Oracles",
    "url": "https://arxiv.org/abs/2606.03548",
    "source": "Sebastian M\\\"uller, Nordine Moumeni, Adel Messaoudi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T04:00:00+00:00",
    "summary": "arXiv:2606.03548v1 Announce Type: cross Abstract: We study the robustness of AMM-based on-chain price oracles to strategic manipulation. An attacker trades against constant product automated market ma"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.03767",
    "domain": "金融",
    "title": "Trading Frictions in Dynamic Cap-and-Trade Markets",
    "url": "https://arxiv.org/abs/2606.03767",
    "source": "Nicola Borri, Yukun Liu, Aleh Tsyvinski, Xi Wu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T04:00:00+00:00",
    "summary": "arXiv:2606.03767v1 Announce Type: cross Abstract: We develop a dynamic stochastic model of markets with an externality and multiple trading frictions, and cap-and-trade as the leading application. Slo"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.03777",
    "domain": "金融",
    "title": "From Control Boundary to Insurance Claim: Reconstructing AI-Mediated Losses Through the CER Framework",
    "url": "https://arxiv.org/abs/2606.03777",
    "source": "Alex Leung, Rex Zhang, Kentaroh Toyoda, SiewMei Loh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T04:00:00+00:00",
    "summary": "arXiv:2606.03777v1 Announce Type: cross Abstract: AI losses that arise through an insured organization's generative or agentic AI system require state reconstruction, not merely event reconstruction, "
  },
  {
    "id": "rss:https://arxiv.org/abs/2409.12721",
    "domain": "金融",
    "title": "Market Simulation under Adverse Selection",
    "url": "https://arxiv.org/abs/2409.12721",
    "source": "Luca Lalor, Anatoliy Swishchuk",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T04:00:00+00:00",
    "summary": "arXiv:2409.12721v3 Announce Type: replace Abstract: In this paper, we study the effects of fill probabilities and adverse fills on the trading strategy simulation process. We specifically focus on a s"
  },
  {
    "id": "rss:https://arxiv.org/abs/2410.13103",
    "domain": "金融",
    "title": "Delegated portfolio management with random default",
    "url": "https://arxiv.org/abs/2410.13103",
    "source": "Alberto Gennaro, Thibaut Mastrolia",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T04:00:00+00:00",
    "summary": "arXiv:2410.13103v2 Announce Type: replace Abstract: We are considering the problem of optimal portfolio delegation between an investor and a portfolio manager under a random default time. We focus on "
  },
  {
    "id": "rss:https://arxiv.org/abs/2509.22088",
    "domain": "金融",
    "title": "Factor-Based Conditional Diffusion Model for Contextual Portfolio Optimization",
    "url": "https://arxiv.org/abs/2509.22088",
    "source": "Xuefeng Gao, Mengying He, Xuedong He, Jiale Zha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T04:00:00+00:00",
    "summary": "arXiv:2509.22088v3 Announce Type: replace Abstract: We propose a novel conditional diffusion model for contextual portfolio optimization that learns the cross-sectional distribution of next-day stock "
  },
  {
    "id": "rss:https://arxiv.org/abs/2510.12049",
    "domain": "金融",
    "title": "Generative AI and Sales Productivity: Field Experiments in Online Retail",
    "url": "https://arxiv.org/abs/2510.12049",
    "source": "Lu Fang, Zhe Yuan, Kaifu Zhang, Dante Donati, Miklos Sarvary",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T04:00:00+00:00",
    "summary": "arXiv:2510.12049v5 Announce Type: replace Abstract: We quantify the short-term impact of Generative Artificial Intelligence (GenAI) on sales performance through a series of large-scale randomized fiel"
  },
  {
    "id": "rss:https://arxiv.org/abs/2512.18342",
    "domain": "金融",
    "title": "Preventive Care Disruptions and Emergency Hospitalizations",
    "url": "https://arxiv.org/abs/2512.18342",
    "source": "Moslem Rashidi, Luke B. Connelly, Gianluca Fiorentini",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T04:00:00+00:00",
    "summary": "arXiv:2512.18342v4 Announce Type: replace Abstract: This paper studies whether interruptions to organized breast cancer screening lead to greater later use of emergency hospital care. It focuses on th"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.05140",
    "domain": "金融",
    "title": "A Practical Guide to Strip Caplet Volatilities",
    "url": "https://arxiv.org/abs/2605.05140",
    "source": "Fabien Le Floc'h",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T04:00:00+00:00",
    "summary": "arXiv:2605.05140v4 Announce Type: replace Abstract: We study caplet stripping, the problem of recovering a caplet volatility term structure consistent with quoted cap volatilities. Many academic paper"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.12151",
    "domain": "金融",
    "title": "RED-2400: A Public Benchmark of Algorithmically-Rejected Trading Events with Outcome Labels",
    "url": "https://arxiv.org/abs/2605.12151",
    "source": "Arati U. Kamat",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T04:00:00+00:00",
    "summary": "arXiv:2605.12151v2 Announce Type: replace Abstract: RED-2400 is a public benchmark of 6,660 algorithmically-rejected trading events from a live Solana decentralised-exchange filter stack, observed con"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.18343",
    "domain": "金融",
    "title": "Explicit Rational Formulae for Bachelier (Normal) Implied Volatility",
    "url": "https://arxiv.org/abs/2605.18343",
    "source": "Fabien Le Floc'h",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T04:00:00+00:00",
    "summary": "arXiv:2605.18343v2 Announce Type: replace Abstract: We present two explicit rational formulae for Bachelier, or normal, implied volatility. The formulae take the option price, forward, strike, and exp"
  },
  {
    "id": "rss:https://arxiv.org/abs/2508.13174",
    "domain": "金融",
    "title": "AlphaEval: A Comprehensive and Efficient Evaluation Framework for Formula Alpha Mining",
    "url": "https://arxiv.org/abs/2508.13174",
    "source": "Hongjun Ding, Binqi Chen, Jinsheng Huang, Taian Guo, Zhengyang Mao, Guoyi Shao, Lutong Zou, Luchen Liu, Ming Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T04:00:00+00:00",
    "summary": "arXiv:2508.13174v2 Announce Type: replace-cross Abstract: Formula alpha mining, which generates predictive signals from financial data, is critical for quantitative investment. Although various algori"
  },
  {
    "id": "rss:https://arxiv.org/abs/2511.19701",
    "domain": "金融",
    "title": "Optimal dividend and capital injection under self-exciting claims",
    "url": "https://arxiv.org/abs/2511.19701",
    "source": "Paulin Aubert, Etienne Chevalier, Vathana Ly Vath",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T04:00:00+00:00",
    "summary": "arXiv:2511.19701v2 Announce Type: replace-cross Abstract: In this paper, we study an optimal dividend and capital-injection problem in a Cram\\'er--Lundberg model where claim arrivals follow a Hawkes p"
  },
  {
    "id": "rss:https://arxiv.org/abs/2601.12441",
    "domain": "金融",
    "title": "The Dynamic and Endogenous Behavior of Re-Offense Risk: An Agent-Based Simulation Study of Treatment Allocation in Incarceration Diversion Programs",
    "url": "https://arxiv.org/abs/2601.12441",
    "source": "Chuwen Zhang, Pengyi Shi, Amy Ward",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T04:00:00+00:00",
    "summary": "arXiv:2601.12441v2 Announce Type: replace-cross Abstract: Incarceration-diversion treatment programs aim to improve societal reintegration and reduce recidivism, but limited capacity forces policymake"
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
    "id": "hn:48221518",
    "domain": "金融",
    "title": "Tesla Cybertruck driver arrested after driving into lake to use 'wade mode'",
    "url": "https://www.bbc.co.uk/news/articles/c072x1kml44o",
    "source": "LaSombra",
    "platform": "hackernews",
    "points": 35,
    "published_at": "2026-05-21T12:24:58+00:00",
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
    "id": "hn:48033721",
    "domain": "金融",
    "title": "Fedora is now the default Linux recommendation, and Ubuntu did this to itself",
    "url": "https://www.xda-developers.com/fedora-becoming-default-linux-recommendation-ubuntu-fault/",
    "source": "bundie",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-05-06T08:27:54+00:00",
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
  }
]
```
